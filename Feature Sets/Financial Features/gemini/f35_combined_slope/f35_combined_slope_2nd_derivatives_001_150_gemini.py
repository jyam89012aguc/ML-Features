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

def f35_combined_slope_cor_slope_pct_5d_v001_signal(cor):
    """Percentage slope for Raw level of cor over 5d window."""
    res = _slope_pct(cor, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_revenue_slope_pct_5d_v002_signal(revenue):
    """Percentage slope for Raw level of revenue over 5d window."""
    res = _slope_pct(revenue, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_sgna_slope_pct_5d_v003_signal(sgna):
    """Percentage slope for Raw level of sgna over 5d window."""
    res = _slope_pct(sgna, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_expense_velocity_slope_pct_5d_v004_signal(cor, sgna, revenue):
    """Percentage slope for Total expense momentum over 5d window."""
    res = _slope_pct(_slope_pct(_ratio(cor + sgna, revenue), 63), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_cor_slope_pct_10d_v005_signal(cor):
    """Percentage slope for Raw level of cor over 10d window."""
    res = _slope_pct(cor, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_revenue_slope_pct_10d_v006_signal(revenue):
    """Percentage slope for Raw level of revenue over 10d window."""
    res = _slope_pct(revenue, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_sgna_slope_pct_10d_v007_signal(sgna):
    """Percentage slope for Raw level of sgna over 10d window."""
    res = _slope_pct(sgna, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_expense_velocity_slope_pct_10d_v008_signal(cor, sgna, revenue):
    """Percentage slope for Total expense momentum over 10d window."""
    res = _slope_pct(_slope_pct(_ratio(cor + sgna, revenue), 63), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_cor_slope_pct_21d_v009_signal(cor):
    """Percentage slope for Raw level of cor over 21d window."""
    res = _slope_pct(cor, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_revenue_slope_pct_21d_v010_signal(revenue):
    """Percentage slope for Raw level of revenue over 21d window."""
    res = _slope_pct(revenue, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_sgna_slope_pct_21d_v011_signal(sgna):
    """Percentage slope for Raw level of sgna over 21d window."""
    res = _slope_pct(sgna, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_expense_velocity_slope_pct_21d_v012_signal(cor, sgna, revenue):
    """Percentage slope for Total expense momentum over 21d window."""
    res = _slope_pct(_slope_pct(_ratio(cor + sgna, revenue), 63), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_cor_slope_pct_42d_v013_signal(cor):
    """Percentage slope for Raw level of cor over 42d window."""
    res = _slope_pct(cor, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_revenue_slope_pct_42d_v014_signal(revenue):
    """Percentage slope for Raw level of revenue over 42d window."""
    res = _slope_pct(revenue, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_sgna_slope_pct_42d_v015_signal(sgna):
    """Percentage slope for Raw level of sgna over 42d window."""
    res = _slope_pct(sgna, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_expense_velocity_slope_pct_42d_v016_signal(cor, sgna, revenue):
    """Percentage slope for Total expense momentum over 42d window."""
    res = _slope_pct(_slope_pct(_ratio(cor + sgna, revenue), 63), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_cor_slope_pct_63d_v017_signal(cor):
    """Percentage slope for Raw level of cor over 63d window."""
    res = _slope_pct(cor, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_revenue_slope_pct_63d_v018_signal(revenue):
    """Percentage slope for Raw level of revenue over 63d window."""
    res = _slope_pct(revenue, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_sgna_slope_pct_63d_v019_signal(sgna):
    """Percentage slope for Raw level of sgna over 63d window."""
    res = _slope_pct(sgna, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_expense_velocity_slope_pct_63d_v020_signal(cor, sgna, revenue):
    """Percentage slope for Total expense momentum over 63d window."""
    res = _slope_pct(_slope_pct(_ratio(cor + sgna, revenue), 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_cor_slope_pct_126d_v021_signal(cor):
    """Percentage slope for Raw level of cor over 126d window."""
    res = _slope_pct(cor, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_revenue_slope_pct_126d_v022_signal(revenue):
    """Percentage slope for Raw level of revenue over 126d window."""
    res = _slope_pct(revenue, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_sgna_slope_pct_126d_v023_signal(sgna):
    """Percentage slope for Raw level of sgna over 126d window."""
    res = _slope_pct(sgna, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_expense_velocity_slope_pct_126d_v024_signal(cor, sgna, revenue):
    """Percentage slope for Total expense momentum over 126d window."""
    res = _slope_pct(_slope_pct(_ratio(cor + sgna, revenue), 63), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_cor_slope_pct_252d_v025_signal(cor):
    """Percentage slope for Raw level of cor over 252d window."""
    res = _slope_pct(cor, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_revenue_slope_pct_252d_v026_signal(revenue):
    """Percentage slope for Raw level of revenue over 252d window."""
    res = _slope_pct(revenue, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_sgna_slope_pct_252d_v027_signal(sgna):
    """Percentage slope for Raw level of sgna over 252d window."""
    res = _slope_pct(sgna, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_expense_velocity_slope_pct_252d_v028_signal(cor, sgna, revenue):
    """Percentage slope for Total expense momentum over 252d window."""
    res = _slope_pct(_slope_pct(_ratio(cor + sgna, revenue), 63), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_cor_slope_pct_504d_v029_signal(cor):
    """Percentage slope for Raw level of cor over 504d window."""
    res = _slope_pct(cor, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_revenue_slope_pct_504d_v030_signal(revenue):
    """Percentage slope for Raw level of revenue over 504d window."""
    res = _slope_pct(revenue, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_sgna_slope_pct_504d_v031_signal(sgna):
    """Percentage slope for Raw level of sgna over 504d window."""
    res = _slope_pct(sgna, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_expense_velocity_slope_pct_504d_v032_signal(cor, sgna, revenue):
    """Percentage slope for Total expense momentum over 504d window."""
    res = _slope_pct(_slope_pct(_ratio(cor + sgna, revenue), 63), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_cor_slope_pct_756d_v033_signal(cor):
    """Percentage slope for Raw level of cor over 756d window."""
    res = _slope_pct(cor, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_revenue_slope_pct_756d_v034_signal(revenue):
    """Percentage slope for Raw level of revenue over 756d window."""
    res = _slope_pct(revenue, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_sgna_slope_pct_756d_v035_signal(sgna):
    """Percentage slope for Raw level of sgna over 756d window."""
    res = _slope_pct(sgna, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_expense_velocity_slope_pct_756d_v036_signal(cor, sgna, revenue):
    """Percentage slope for Total expense momentum over 756d window."""
    res = _slope_pct(_slope_pct(_ratio(cor + sgna, revenue), 63), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_cor_slope_pct_1008d_v037_signal(cor):
    """Percentage slope for Raw level of cor over 1008d window."""
    res = _slope_pct(cor, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_revenue_slope_pct_1008d_v038_signal(revenue):
    """Percentage slope for Raw level of revenue over 1008d window."""
    res = _slope_pct(revenue, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_sgna_slope_pct_1008d_v039_signal(sgna):
    """Percentage slope for Raw level of sgna over 1008d window."""
    res = _slope_pct(sgna, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_expense_velocity_slope_pct_1008d_v040_signal(cor, sgna, revenue):
    """Percentage slope for Total expense momentum over 1008d window."""
    res = _slope_pct(_slope_pct(_ratio(cor + sgna, revenue), 63), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_cor_slope_pct_1260d_v041_signal(cor):
    """Percentage slope for Raw level of cor over 1260d window."""
    res = _slope_pct(cor, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_revenue_slope_pct_1260d_v042_signal(revenue):
    """Percentage slope for Raw level of revenue over 1260d window."""
    res = _slope_pct(revenue, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_sgna_slope_pct_1260d_v043_signal(sgna):
    """Percentage slope for Raw level of sgna over 1260d window."""
    res = _slope_pct(sgna, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_expense_velocity_slope_pct_1260d_v044_signal(cor, sgna, revenue):
    """Percentage slope for Total expense momentum over 1260d window."""
    res = _slope_pct(_slope_pct(_ratio(cor + sgna, revenue), 63), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_cor_jerk_5d_v045_signal(cor):
    """Acceleration/Jerk for Raw level of cor over 5d window."""
    res = _jerk(cor, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_revenue_jerk_5d_v046_signal(revenue):
    """Acceleration/Jerk for Raw level of revenue over 5d window."""
    res = _jerk(revenue, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_sgna_jerk_5d_v047_signal(sgna):
    """Acceleration/Jerk for Raw level of sgna over 5d window."""
    res = _jerk(sgna, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_expense_velocity_jerk_5d_v048_signal(cor, sgna, revenue):
    """Acceleration/Jerk for Total expense momentum over 5d window."""
    res = _jerk(_slope_pct(_ratio(cor + sgna, revenue), 63), 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_cor_jerk_10d_v049_signal(cor):
    """Acceleration/Jerk for Raw level of cor over 10d window."""
    res = _jerk(cor, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_revenue_jerk_10d_v050_signal(revenue):
    """Acceleration/Jerk for Raw level of revenue over 10d window."""
    res = _jerk(revenue, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_sgna_jerk_10d_v051_signal(sgna):
    """Acceleration/Jerk for Raw level of sgna over 10d window."""
    res = _jerk(sgna, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_expense_velocity_jerk_10d_v052_signal(cor, sgna, revenue):
    """Acceleration/Jerk for Total expense momentum over 10d window."""
    res = _jerk(_slope_pct(_ratio(cor + sgna, revenue), 63), 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_cor_jerk_21d_v053_signal(cor):
    """Acceleration/Jerk for Raw level of cor over 21d window."""
    res = _jerk(cor, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_revenue_jerk_21d_v054_signal(revenue):
    """Acceleration/Jerk for Raw level of revenue over 21d window."""
    res = _jerk(revenue, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_sgna_jerk_21d_v055_signal(sgna):
    """Acceleration/Jerk for Raw level of sgna over 21d window."""
    res = _jerk(sgna, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_expense_velocity_jerk_21d_v056_signal(cor, sgna, revenue):
    """Acceleration/Jerk for Total expense momentum over 21d window."""
    res = _jerk(_slope_pct(_ratio(cor + sgna, revenue), 63), 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_cor_jerk_42d_v057_signal(cor):
    """Acceleration/Jerk for Raw level of cor over 42d window."""
    res = _jerk(cor, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_revenue_jerk_42d_v058_signal(revenue):
    """Acceleration/Jerk for Raw level of revenue over 42d window."""
    res = _jerk(revenue, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_sgna_jerk_42d_v059_signal(sgna):
    """Acceleration/Jerk for Raw level of sgna over 42d window."""
    res = _jerk(sgna, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_expense_velocity_jerk_42d_v060_signal(cor, sgna, revenue):
    """Acceleration/Jerk for Total expense momentum over 42d window."""
    res = _jerk(_slope_pct(_ratio(cor + sgna, revenue), 63), 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_cor_jerk_63d_v061_signal(cor):
    """Acceleration/Jerk for Raw level of cor over 63d window."""
    res = _jerk(cor, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_revenue_jerk_63d_v062_signal(revenue):
    """Acceleration/Jerk for Raw level of revenue over 63d window."""
    res = _jerk(revenue, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_sgna_jerk_63d_v063_signal(sgna):
    """Acceleration/Jerk for Raw level of sgna over 63d window."""
    res = _jerk(sgna, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_expense_velocity_jerk_63d_v064_signal(cor, sgna, revenue):
    """Acceleration/Jerk for Total expense momentum over 63d window."""
    res = _jerk(_slope_pct(_ratio(cor + sgna, revenue), 63), 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_cor_jerk_126d_v065_signal(cor):
    """Acceleration/Jerk for Raw level of cor over 126d window."""
    res = _jerk(cor, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_revenue_jerk_126d_v066_signal(revenue):
    """Acceleration/Jerk for Raw level of revenue over 126d window."""
    res = _jerk(revenue, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_sgna_jerk_126d_v067_signal(sgna):
    """Acceleration/Jerk for Raw level of sgna over 126d window."""
    res = _jerk(sgna, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_expense_velocity_jerk_126d_v068_signal(cor, sgna, revenue):
    """Acceleration/Jerk for Total expense momentum over 126d window."""
    res = _jerk(_slope_pct(_ratio(cor + sgna, revenue), 63), 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_cor_jerk_252d_v069_signal(cor):
    """Acceleration/Jerk for Raw level of cor over 252d window."""
    res = _jerk(cor, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_revenue_jerk_252d_v070_signal(revenue):
    """Acceleration/Jerk for Raw level of revenue over 252d window."""
    res = _jerk(revenue, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_sgna_jerk_252d_v071_signal(sgna):
    """Acceleration/Jerk for Raw level of sgna over 252d window."""
    res = _jerk(sgna, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_expense_velocity_jerk_252d_v072_signal(cor, sgna, revenue):
    """Acceleration/Jerk for Total expense momentum over 252d window."""
    res = _jerk(_slope_pct(_ratio(cor + sgna, revenue), 63), 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_cor_jerk_504d_v073_signal(cor):
    """Acceleration/Jerk for Raw level of cor over 504d window."""
    res = _jerk(cor, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_revenue_jerk_504d_v074_signal(revenue):
    """Acceleration/Jerk for Raw level of revenue over 504d window."""
    res = _jerk(revenue, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_sgna_jerk_504d_v075_signal(sgna):
    """Acceleration/Jerk for Raw level of sgna over 504d window."""
    res = _jerk(sgna, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_expense_velocity_jerk_504d_v076_signal(cor, sgna, revenue):
    """Acceleration/Jerk for Total expense momentum over 504d window."""
    res = _jerk(_slope_pct(_ratio(cor + sgna, revenue), 63), 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_cor_jerk_756d_v077_signal(cor):
    """Acceleration/Jerk for Raw level of cor over 756d window."""
    res = _jerk(cor, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_revenue_jerk_756d_v078_signal(revenue):
    """Acceleration/Jerk for Raw level of revenue over 756d window."""
    res = _jerk(revenue, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_sgna_jerk_756d_v079_signal(sgna):
    """Acceleration/Jerk for Raw level of sgna over 756d window."""
    res = _jerk(sgna, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_expense_velocity_jerk_756d_v080_signal(cor, sgna, revenue):
    """Acceleration/Jerk for Total expense momentum over 756d window."""
    res = _jerk(_slope_pct(_ratio(cor + sgna, revenue), 63), 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_cor_jerk_1008d_v081_signal(cor):
    """Acceleration/Jerk for Raw level of cor over 1008d window."""
    res = _jerk(cor, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_revenue_jerk_1008d_v082_signal(revenue):
    """Acceleration/Jerk for Raw level of revenue over 1008d window."""
    res = _jerk(revenue, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_sgna_jerk_1008d_v083_signal(sgna):
    """Acceleration/Jerk for Raw level of sgna over 1008d window."""
    res = _jerk(sgna, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_expense_velocity_jerk_1008d_v084_signal(cor, sgna, revenue):
    """Acceleration/Jerk for Total expense momentum over 1008d window."""
    res = _jerk(_slope_pct(_ratio(cor + sgna, revenue), 63), 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_cor_jerk_1260d_v085_signal(cor):
    """Acceleration/Jerk for Raw level of cor over 1260d window."""
    res = _jerk(cor, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_revenue_jerk_1260d_v086_signal(revenue):
    """Acceleration/Jerk for Raw level of revenue over 1260d window."""
    res = _jerk(revenue, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_sgna_jerk_1260d_v087_signal(sgna):
    """Acceleration/Jerk for Raw level of sgna over 1260d window."""
    res = _jerk(sgna, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_expense_velocity_jerk_1260d_v088_signal(cor, sgna, revenue):
    """Acceleration/Jerk for Total expense momentum over 1260d window."""
    res = _jerk(_slope_pct(_ratio(cor + sgna, revenue), 63), 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_cor_slope_diff_norm_5d_v089_signal(cor):
    """Normalized slope change for Raw level of cor over 5d window."""
    res = (_slope_pct(cor, 5).diff(5) / _sma(cor.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_revenue_slope_diff_norm_5d_v090_signal(revenue):
    """Normalized slope change for Raw level of revenue over 5d window."""
    res = (_slope_pct(revenue, 5).diff(5) / _sma(revenue.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_sgna_slope_diff_norm_5d_v091_signal(sgna):
    """Normalized slope change for Raw level of sgna over 5d window."""
    res = (_slope_pct(sgna, 5).diff(5) / _sma(sgna.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_expense_velocity_slope_diff_norm_5d_v092_signal(cor, sgna, revenue):
    """Normalized slope change for Total expense momentum over 5d window."""
    res = (_slope_pct(_slope_pct(_ratio(cor + sgna, revenue), 63), 5).diff(5) / _sma(_slope_pct(_ratio(cor + sgna, revenue), 63).abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_cor_slope_diff_norm_10d_v093_signal(cor):
    """Normalized slope change for Raw level of cor over 10d window."""
    res = (_slope_pct(cor, 10).diff(10) / _sma(cor.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_revenue_slope_diff_norm_10d_v094_signal(revenue):
    """Normalized slope change for Raw level of revenue over 10d window."""
    res = (_slope_pct(revenue, 10).diff(10) / _sma(revenue.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_sgna_slope_diff_norm_10d_v095_signal(sgna):
    """Normalized slope change for Raw level of sgna over 10d window."""
    res = (_slope_pct(sgna, 10).diff(10) / _sma(sgna.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_expense_velocity_slope_diff_norm_10d_v096_signal(cor, sgna, revenue):
    """Normalized slope change for Total expense momentum over 10d window."""
    res = (_slope_pct(_slope_pct(_ratio(cor + sgna, revenue), 63), 10).diff(10) / _sma(_slope_pct(_ratio(cor + sgna, revenue), 63).abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_cor_slope_diff_norm_21d_v097_signal(cor):
    """Normalized slope change for Raw level of cor over 21d window."""
    res = (_slope_pct(cor, 21).diff(21) / _sma(cor.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_revenue_slope_diff_norm_21d_v098_signal(revenue):
    """Normalized slope change for Raw level of revenue over 21d window."""
    res = (_slope_pct(revenue, 21).diff(21) / _sma(revenue.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_sgna_slope_diff_norm_21d_v099_signal(sgna):
    """Normalized slope change for Raw level of sgna over 21d window."""
    res = (_slope_pct(sgna, 21).diff(21) / _sma(sgna.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_expense_velocity_slope_diff_norm_21d_v100_signal(cor, sgna, revenue):
    """Normalized slope change for Total expense momentum over 21d window."""
    res = (_slope_pct(_slope_pct(_ratio(cor + sgna, revenue), 63), 21).diff(21) / _sma(_slope_pct(_ratio(cor + sgna, revenue), 63).abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_cor_slope_diff_norm_42d_v101_signal(cor):
    """Normalized slope change for Raw level of cor over 42d window."""
    res = (_slope_pct(cor, 42).diff(42) / _sma(cor.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_revenue_slope_diff_norm_42d_v102_signal(revenue):
    """Normalized slope change for Raw level of revenue over 42d window."""
    res = (_slope_pct(revenue, 42).diff(42) / _sma(revenue.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_sgna_slope_diff_norm_42d_v103_signal(sgna):
    """Normalized slope change for Raw level of sgna over 42d window."""
    res = (_slope_pct(sgna, 42).diff(42) / _sma(sgna.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_expense_velocity_slope_diff_norm_42d_v104_signal(cor, sgna, revenue):
    """Normalized slope change for Total expense momentum over 42d window."""
    res = (_slope_pct(_slope_pct(_ratio(cor + sgna, revenue), 63), 42).diff(42) / _sma(_slope_pct(_ratio(cor + sgna, revenue), 63).abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_cor_slope_diff_norm_63d_v105_signal(cor):
    """Normalized slope change for Raw level of cor over 63d window."""
    res = (_slope_pct(cor, 63).diff(63) / _sma(cor.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_revenue_slope_diff_norm_63d_v106_signal(revenue):
    """Normalized slope change for Raw level of revenue over 63d window."""
    res = (_slope_pct(revenue, 63).diff(63) / _sma(revenue.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_sgna_slope_diff_norm_63d_v107_signal(sgna):
    """Normalized slope change for Raw level of sgna over 63d window."""
    res = (_slope_pct(sgna, 63).diff(63) / _sma(sgna.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_expense_velocity_slope_diff_norm_63d_v108_signal(cor, sgna, revenue):
    """Normalized slope change for Total expense momentum over 63d window."""
    res = (_slope_pct(_slope_pct(_ratio(cor + sgna, revenue), 63), 63).diff(63) / _sma(_slope_pct(_ratio(cor + sgna, revenue), 63).abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_cor_slope_diff_norm_126d_v109_signal(cor):
    """Normalized slope change for Raw level of cor over 126d window."""
    res = (_slope_pct(cor, 126).diff(126) / _sma(cor.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_revenue_slope_diff_norm_126d_v110_signal(revenue):
    """Normalized slope change for Raw level of revenue over 126d window."""
    res = (_slope_pct(revenue, 126).diff(126) / _sma(revenue.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_sgna_slope_diff_norm_126d_v111_signal(sgna):
    """Normalized slope change for Raw level of sgna over 126d window."""
    res = (_slope_pct(sgna, 126).diff(126) / _sma(sgna.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_expense_velocity_slope_diff_norm_126d_v112_signal(cor, sgna, revenue):
    """Normalized slope change for Total expense momentum over 126d window."""
    res = (_slope_pct(_slope_pct(_ratio(cor + sgna, revenue), 63), 126).diff(126) / _sma(_slope_pct(_ratio(cor + sgna, revenue), 63).abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_cor_slope_diff_norm_252d_v113_signal(cor):
    """Normalized slope change for Raw level of cor over 252d window."""
    res = (_slope_pct(cor, 252).diff(252) / _sma(cor.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_revenue_slope_diff_norm_252d_v114_signal(revenue):
    """Normalized slope change for Raw level of revenue over 252d window."""
    res = (_slope_pct(revenue, 252).diff(252) / _sma(revenue.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_sgna_slope_diff_norm_252d_v115_signal(sgna):
    """Normalized slope change for Raw level of sgna over 252d window."""
    res = (_slope_pct(sgna, 252).diff(252) / _sma(sgna.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_expense_velocity_slope_diff_norm_252d_v116_signal(cor, sgna, revenue):
    """Normalized slope change for Total expense momentum over 252d window."""
    res = (_slope_pct(_slope_pct(_ratio(cor + sgna, revenue), 63), 252).diff(252) / _sma(_slope_pct(_ratio(cor + sgna, revenue), 63).abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_cor_slope_diff_norm_504d_v117_signal(cor):
    """Normalized slope change for Raw level of cor over 504d window."""
    res = (_slope_pct(cor, 504).diff(504) / _sma(cor.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_revenue_slope_diff_norm_504d_v118_signal(revenue):
    """Normalized slope change for Raw level of revenue over 504d window."""
    res = (_slope_pct(revenue, 504).diff(504) / _sma(revenue.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_sgna_slope_diff_norm_504d_v119_signal(sgna):
    """Normalized slope change for Raw level of sgna over 504d window."""
    res = (_slope_pct(sgna, 504).diff(504) / _sma(sgna.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_expense_velocity_slope_diff_norm_504d_v120_signal(cor, sgna, revenue):
    """Normalized slope change for Total expense momentum over 504d window."""
    res = (_slope_pct(_slope_pct(_ratio(cor + sgna, revenue), 63), 504).diff(504) / _sma(_slope_pct(_ratio(cor + sgna, revenue), 63).abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_cor_slope_diff_norm_756d_v121_signal(cor):
    """Normalized slope change for Raw level of cor over 756d window."""
    res = (_slope_pct(cor, 756).diff(756) / _sma(cor.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_revenue_slope_diff_norm_756d_v122_signal(revenue):
    """Normalized slope change for Raw level of revenue over 756d window."""
    res = (_slope_pct(revenue, 756).diff(756) / _sma(revenue.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_sgna_slope_diff_norm_756d_v123_signal(sgna):
    """Normalized slope change for Raw level of sgna over 756d window."""
    res = (_slope_pct(sgna, 756).diff(756) / _sma(sgna.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_expense_velocity_slope_diff_norm_756d_v124_signal(cor, sgna, revenue):
    """Normalized slope change for Total expense momentum over 756d window."""
    res = (_slope_pct(_slope_pct(_ratio(cor + sgna, revenue), 63), 756).diff(756) / _sma(_slope_pct(_ratio(cor + sgna, revenue), 63).abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_cor_slope_diff_norm_1008d_v125_signal(cor):
    """Normalized slope change for Raw level of cor over 1008d window."""
    res = (_slope_pct(cor, 1008).diff(1008) / _sma(cor.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_revenue_slope_diff_norm_1008d_v126_signal(revenue):
    """Normalized slope change for Raw level of revenue over 1008d window."""
    res = (_slope_pct(revenue, 1008).diff(1008) / _sma(revenue.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_sgna_slope_diff_norm_1008d_v127_signal(sgna):
    """Normalized slope change for Raw level of sgna over 1008d window."""
    res = (_slope_pct(sgna, 1008).diff(1008) / _sma(sgna.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_expense_velocity_slope_diff_norm_1008d_v128_signal(cor, sgna, revenue):
    """Normalized slope change for Total expense momentum over 1008d window."""
    res = (_slope_pct(_slope_pct(_ratio(cor + sgna, revenue), 63), 1008).diff(1008) / _sma(_slope_pct(_ratio(cor + sgna, revenue), 63).abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_cor_slope_diff_norm_1260d_v129_signal(cor):
    """Normalized slope change for Raw level of cor over 1260d window."""
    res = (_slope_pct(cor, 1260).diff(1260) / _sma(cor.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_revenue_slope_diff_norm_1260d_v130_signal(revenue):
    """Normalized slope change for Raw level of revenue over 1260d window."""
    res = (_slope_pct(revenue, 1260).diff(1260) / _sma(revenue.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_sgna_slope_diff_norm_1260d_v131_signal(sgna):
    """Normalized slope change for Raw level of sgna over 1260d window."""
    res = (_slope_pct(sgna, 1260).diff(1260) / _sma(sgna.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_expense_velocity_slope_diff_norm_1260d_v132_signal(cor, sgna, revenue):
    """Normalized slope change for Total expense momentum over 1260d window."""
    res = (_slope_pct(_slope_pct(_ratio(cor + sgna, revenue), 63), 1260).diff(1260) / _sma(_slope_pct(_ratio(cor + sgna, revenue), 63).abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_cor_mom_z_5d_v133_signal(cor):
    """Relative momentum strength for Raw level of cor over 5d window."""
    res = _z(_slope_pct(cor, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_revenue_mom_z_5d_v134_signal(revenue):
    """Relative momentum strength for Raw level of revenue over 5d window."""
    res = _z(_slope_pct(revenue, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_sgna_mom_z_5d_v135_signal(sgna):
    """Relative momentum strength for Raw level of sgna over 5d window."""
    res = _z(_slope_pct(sgna, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_expense_velocity_mom_z_5d_v136_signal(cor, sgna, revenue):
    """Relative momentum strength for Total expense momentum over 5d window."""
    res = _z(_slope_pct(_slope_pct(_ratio(cor + sgna, revenue), 63), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_cor_mom_z_10d_v137_signal(cor):
    """Relative momentum strength for Raw level of cor over 10d window."""
    res = _z(_slope_pct(cor, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_revenue_mom_z_10d_v138_signal(revenue):
    """Relative momentum strength for Raw level of revenue over 10d window."""
    res = _z(_slope_pct(revenue, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_sgna_mom_z_10d_v139_signal(sgna):
    """Relative momentum strength for Raw level of sgna over 10d window."""
    res = _z(_slope_pct(sgna, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_expense_velocity_mom_z_10d_v140_signal(cor, sgna, revenue):
    """Relative momentum strength for Total expense momentum over 10d window."""
    res = _z(_slope_pct(_slope_pct(_ratio(cor + sgna, revenue), 63), 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_cor_mom_z_21d_v141_signal(cor):
    """Relative momentum strength for Raw level of cor over 21d window."""
    res = _z(_slope_pct(cor, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_revenue_mom_z_21d_v142_signal(revenue):
    """Relative momentum strength for Raw level of revenue over 21d window."""
    res = _z(_slope_pct(revenue, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_sgna_mom_z_21d_v143_signal(sgna):
    """Relative momentum strength for Raw level of sgna over 21d window."""
    res = _z(_slope_pct(sgna, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_expense_velocity_mom_z_21d_v144_signal(cor, sgna, revenue):
    """Relative momentum strength for Total expense momentum over 21d window."""
    res = _z(_slope_pct(_slope_pct(_ratio(cor + sgna, revenue), 63), 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_cor_mom_z_42d_v145_signal(cor):
    """Relative momentum strength for Raw level of cor over 42d window."""
    res = _z(_slope_pct(cor, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_revenue_mom_z_42d_v146_signal(revenue):
    """Relative momentum strength for Raw level of revenue over 42d window."""
    res = _z(_slope_pct(revenue, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_sgna_mom_z_42d_v147_signal(sgna):
    """Relative momentum strength for Raw level of sgna over 42d window."""
    res = _z(_slope_pct(sgna, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_expense_velocity_mom_z_42d_v148_signal(cor, sgna, revenue):
    """Relative momentum strength for Total expense momentum over 42d window."""
    res = _z(_slope_pct(_slope_pct(_ratio(cor + sgna, revenue), 63), 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_cor_mom_z_63d_v149_signal(cor):
    """Relative momentum strength for Raw level of cor over 63d window."""
    res = _z(_slope_pct(cor, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_combined_slope_revenue_mom_z_63d_v150_signal(revenue):
    """Relative momentum strength for Raw level of revenue over 63d window."""
    res = _z(_slope_pct(revenue, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)


# ===== Feature Registry =====
REGISTRY = {
    "f35_combined_slope_cor_slope_pct_5d_v001_signal": {"func": f35_combined_slope_cor_slope_pct_5d_v001_signal},
    "f35_combined_slope_revenue_slope_pct_5d_v002_signal": {"func": f35_combined_slope_revenue_slope_pct_5d_v002_signal},
    "f35_combined_slope_sgna_slope_pct_5d_v003_signal": {"func": f35_combined_slope_sgna_slope_pct_5d_v003_signal},
    "f35_combined_slope_expense_velocity_slope_pct_5d_v004_signal": {"func": f35_combined_slope_expense_velocity_slope_pct_5d_v004_signal},
    "f35_combined_slope_cor_slope_pct_10d_v005_signal": {"func": f35_combined_slope_cor_slope_pct_10d_v005_signal},
    "f35_combined_slope_revenue_slope_pct_10d_v006_signal": {"func": f35_combined_slope_revenue_slope_pct_10d_v006_signal},
    "f35_combined_slope_sgna_slope_pct_10d_v007_signal": {"func": f35_combined_slope_sgna_slope_pct_10d_v007_signal},
    "f35_combined_slope_expense_velocity_slope_pct_10d_v008_signal": {"func": f35_combined_slope_expense_velocity_slope_pct_10d_v008_signal},
    "f35_combined_slope_cor_slope_pct_21d_v009_signal": {"func": f35_combined_slope_cor_slope_pct_21d_v009_signal},
    "f35_combined_slope_revenue_slope_pct_21d_v010_signal": {"func": f35_combined_slope_revenue_slope_pct_21d_v010_signal},
    "f35_combined_slope_sgna_slope_pct_21d_v011_signal": {"func": f35_combined_slope_sgna_slope_pct_21d_v011_signal},
    "f35_combined_slope_expense_velocity_slope_pct_21d_v012_signal": {"func": f35_combined_slope_expense_velocity_slope_pct_21d_v012_signal},
    "f35_combined_slope_cor_slope_pct_42d_v013_signal": {"func": f35_combined_slope_cor_slope_pct_42d_v013_signal},
    "f35_combined_slope_revenue_slope_pct_42d_v014_signal": {"func": f35_combined_slope_revenue_slope_pct_42d_v014_signal},
    "f35_combined_slope_sgna_slope_pct_42d_v015_signal": {"func": f35_combined_slope_sgna_slope_pct_42d_v015_signal},
    "f35_combined_slope_expense_velocity_slope_pct_42d_v016_signal": {"func": f35_combined_slope_expense_velocity_slope_pct_42d_v016_signal},
    "f35_combined_slope_cor_slope_pct_63d_v017_signal": {"func": f35_combined_slope_cor_slope_pct_63d_v017_signal},
    "f35_combined_slope_revenue_slope_pct_63d_v018_signal": {"func": f35_combined_slope_revenue_slope_pct_63d_v018_signal},
    "f35_combined_slope_sgna_slope_pct_63d_v019_signal": {"func": f35_combined_slope_sgna_slope_pct_63d_v019_signal},
    "f35_combined_slope_expense_velocity_slope_pct_63d_v020_signal": {"func": f35_combined_slope_expense_velocity_slope_pct_63d_v020_signal},
    "f35_combined_slope_cor_slope_pct_126d_v021_signal": {"func": f35_combined_slope_cor_slope_pct_126d_v021_signal},
    "f35_combined_slope_revenue_slope_pct_126d_v022_signal": {"func": f35_combined_slope_revenue_slope_pct_126d_v022_signal},
    "f35_combined_slope_sgna_slope_pct_126d_v023_signal": {"func": f35_combined_slope_sgna_slope_pct_126d_v023_signal},
    "f35_combined_slope_expense_velocity_slope_pct_126d_v024_signal": {"func": f35_combined_slope_expense_velocity_slope_pct_126d_v024_signal},
    "f35_combined_slope_cor_slope_pct_252d_v025_signal": {"func": f35_combined_slope_cor_slope_pct_252d_v025_signal},
    "f35_combined_slope_revenue_slope_pct_252d_v026_signal": {"func": f35_combined_slope_revenue_slope_pct_252d_v026_signal},
    "f35_combined_slope_sgna_slope_pct_252d_v027_signal": {"func": f35_combined_slope_sgna_slope_pct_252d_v027_signal},
    "f35_combined_slope_expense_velocity_slope_pct_252d_v028_signal": {"func": f35_combined_slope_expense_velocity_slope_pct_252d_v028_signal},
    "f35_combined_slope_cor_slope_pct_504d_v029_signal": {"func": f35_combined_slope_cor_slope_pct_504d_v029_signal},
    "f35_combined_slope_revenue_slope_pct_504d_v030_signal": {"func": f35_combined_slope_revenue_slope_pct_504d_v030_signal},
    "f35_combined_slope_sgna_slope_pct_504d_v031_signal": {"func": f35_combined_slope_sgna_slope_pct_504d_v031_signal},
    "f35_combined_slope_expense_velocity_slope_pct_504d_v032_signal": {"func": f35_combined_slope_expense_velocity_slope_pct_504d_v032_signal},
    "f35_combined_slope_cor_slope_pct_756d_v033_signal": {"func": f35_combined_slope_cor_slope_pct_756d_v033_signal},
    "f35_combined_slope_revenue_slope_pct_756d_v034_signal": {"func": f35_combined_slope_revenue_slope_pct_756d_v034_signal},
    "f35_combined_slope_sgna_slope_pct_756d_v035_signal": {"func": f35_combined_slope_sgna_slope_pct_756d_v035_signal},
    "f35_combined_slope_expense_velocity_slope_pct_756d_v036_signal": {"func": f35_combined_slope_expense_velocity_slope_pct_756d_v036_signal},
    "f35_combined_slope_cor_slope_pct_1008d_v037_signal": {"func": f35_combined_slope_cor_slope_pct_1008d_v037_signal},
    "f35_combined_slope_revenue_slope_pct_1008d_v038_signal": {"func": f35_combined_slope_revenue_slope_pct_1008d_v038_signal},
    "f35_combined_slope_sgna_slope_pct_1008d_v039_signal": {"func": f35_combined_slope_sgna_slope_pct_1008d_v039_signal},
    "f35_combined_slope_expense_velocity_slope_pct_1008d_v040_signal": {"func": f35_combined_slope_expense_velocity_slope_pct_1008d_v040_signal},
    "f35_combined_slope_cor_slope_pct_1260d_v041_signal": {"func": f35_combined_slope_cor_slope_pct_1260d_v041_signal},
    "f35_combined_slope_revenue_slope_pct_1260d_v042_signal": {"func": f35_combined_slope_revenue_slope_pct_1260d_v042_signal},
    "f35_combined_slope_sgna_slope_pct_1260d_v043_signal": {"func": f35_combined_slope_sgna_slope_pct_1260d_v043_signal},
    "f35_combined_slope_expense_velocity_slope_pct_1260d_v044_signal": {"func": f35_combined_slope_expense_velocity_slope_pct_1260d_v044_signal},
    "f35_combined_slope_cor_jerk_5d_v045_signal": {"func": f35_combined_slope_cor_jerk_5d_v045_signal},
    "f35_combined_slope_revenue_jerk_5d_v046_signal": {"func": f35_combined_slope_revenue_jerk_5d_v046_signal},
    "f35_combined_slope_sgna_jerk_5d_v047_signal": {"func": f35_combined_slope_sgna_jerk_5d_v047_signal},
    "f35_combined_slope_expense_velocity_jerk_5d_v048_signal": {"func": f35_combined_slope_expense_velocity_jerk_5d_v048_signal},
    "f35_combined_slope_cor_jerk_10d_v049_signal": {"func": f35_combined_slope_cor_jerk_10d_v049_signal},
    "f35_combined_slope_revenue_jerk_10d_v050_signal": {"func": f35_combined_slope_revenue_jerk_10d_v050_signal},
    "f35_combined_slope_sgna_jerk_10d_v051_signal": {"func": f35_combined_slope_sgna_jerk_10d_v051_signal},
    "f35_combined_slope_expense_velocity_jerk_10d_v052_signal": {"func": f35_combined_slope_expense_velocity_jerk_10d_v052_signal},
    "f35_combined_slope_cor_jerk_21d_v053_signal": {"func": f35_combined_slope_cor_jerk_21d_v053_signal},
    "f35_combined_slope_revenue_jerk_21d_v054_signal": {"func": f35_combined_slope_revenue_jerk_21d_v054_signal},
    "f35_combined_slope_sgna_jerk_21d_v055_signal": {"func": f35_combined_slope_sgna_jerk_21d_v055_signal},
    "f35_combined_slope_expense_velocity_jerk_21d_v056_signal": {"func": f35_combined_slope_expense_velocity_jerk_21d_v056_signal},
    "f35_combined_slope_cor_jerk_42d_v057_signal": {"func": f35_combined_slope_cor_jerk_42d_v057_signal},
    "f35_combined_slope_revenue_jerk_42d_v058_signal": {"func": f35_combined_slope_revenue_jerk_42d_v058_signal},
    "f35_combined_slope_sgna_jerk_42d_v059_signal": {"func": f35_combined_slope_sgna_jerk_42d_v059_signal},
    "f35_combined_slope_expense_velocity_jerk_42d_v060_signal": {"func": f35_combined_slope_expense_velocity_jerk_42d_v060_signal},
    "f35_combined_slope_cor_jerk_63d_v061_signal": {"func": f35_combined_slope_cor_jerk_63d_v061_signal},
    "f35_combined_slope_revenue_jerk_63d_v062_signal": {"func": f35_combined_slope_revenue_jerk_63d_v062_signal},
    "f35_combined_slope_sgna_jerk_63d_v063_signal": {"func": f35_combined_slope_sgna_jerk_63d_v063_signal},
    "f35_combined_slope_expense_velocity_jerk_63d_v064_signal": {"func": f35_combined_slope_expense_velocity_jerk_63d_v064_signal},
    "f35_combined_slope_cor_jerk_126d_v065_signal": {"func": f35_combined_slope_cor_jerk_126d_v065_signal},
    "f35_combined_slope_revenue_jerk_126d_v066_signal": {"func": f35_combined_slope_revenue_jerk_126d_v066_signal},
    "f35_combined_slope_sgna_jerk_126d_v067_signal": {"func": f35_combined_slope_sgna_jerk_126d_v067_signal},
    "f35_combined_slope_expense_velocity_jerk_126d_v068_signal": {"func": f35_combined_slope_expense_velocity_jerk_126d_v068_signal},
    "f35_combined_slope_cor_jerk_252d_v069_signal": {"func": f35_combined_slope_cor_jerk_252d_v069_signal},
    "f35_combined_slope_revenue_jerk_252d_v070_signal": {"func": f35_combined_slope_revenue_jerk_252d_v070_signal},
    "f35_combined_slope_sgna_jerk_252d_v071_signal": {"func": f35_combined_slope_sgna_jerk_252d_v071_signal},
    "f35_combined_slope_expense_velocity_jerk_252d_v072_signal": {"func": f35_combined_slope_expense_velocity_jerk_252d_v072_signal},
    "f35_combined_slope_cor_jerk_504d_v073_signal": {"func": f35_combined_slope_cor_jerk_504d_v073_signal},
    "f35_combined_slope_revenue_jerk_504d_v074_signal": {"func": f35_combined_slope_revenue_jerk_504d_v074_signal},
    "f35_combined_slope_sgna_jerk_504d_v075_signal": {"func": f35_combined_slope_sgna_jerk_504d_v075_signal},
    "f35_combined_slope_expense_velocity_jerk_504d_v076_signal": {"func": f35_combined_slope_expense_velocity_jerk_504d_v076_signal},
    "f35_combined_slope_cor_jerk_756d_v077_signal": {"func": f35_combined_slope_cor_jerk_756d_v077_signal},
    "f35_combined_slope_revenue_jerk_756d_v078_signal": {"func": f35_combined_slope_revenue_jerk_756d_v078_signal},
    "f35_combined_slope_sgna_jerk_756d_v079_signal": {"func": f35_combined_slope_sgna_jerk_756d_v079_signal},
    "f35_combined_slope_expense_velocity_jerk_756d_v080_signal": {"func": f35_combined_slope_expense_velocity_jerk_756d_v080_signal},
    "f35_combined_slope_cor_jerk_1008d_v081_signal": {"func": f35_combined_slope_cor_jerk_1008d_v081_signal},
    "f35_combined_slope_revenue_jerk_1008d_v082_signal": {"func": f35_combined_slope_revenue_jerk_1008d_v082_signal},
    "f35_combined_slope_sgna_jerk_1008d_v083_signal": {"func": f35_combined_slope_sgna_jerk_1008d_v083_signal},
    "f35_combined_slope_expense_velocity_jerk_1008d_v084_signal": {"func": f35_combined_slope_expense_velocity_jerk_1008d_v084_signal},
    "f35_combined_slope_cor_jerk_1260d_v085_signal": {"func": f35_combined_slope_cor_jerk_1260d_v085_signal},
    "f35_combined_slope_revenue_jerk_1260d_v086_signal": {"func": f35_combined_slope_revenue_jerk_1260d_v086_signal},
    "f35_combined_slope_sgna_jerk_1260d_v087_signal": {"func": f35_combined_slope_sgna_jerk_1260d_v087_signal},
    "f35_combined_slope_expense_velocity_jerk_1260d_v088_signal": {"func": f35_combined_slope_expense_velocity_jerk_1260d_v088_signal},
    "f35_combined_slope_cor_slope_diff_norm_5d_v089_signal": {"func": f35_combined_slope_cor_slope_diff_norm_5d_v089_signal},
    "f35_combined_slope_revenue_slope_diff_norm_5d_v090_signal": {"func": f35_combined_slope_revenue_slope_diff_norm_5d_v090_signal},
    "f35_combined_slope_sgna_slope_diff_norm_5d_v091_signal": {"func": f35_combined_slope_sgna_slope_diff_norm_5d_v091_signal},
    "f35_combined_slope_expense_velocity_slope_diff_norm_5d_v092_signal": {"func": f35_combined_slope_expense_velocity_slope_diff_norm_5d_v092_signal},
    "f35_combined_slope_cor_slope_diff_norm_10d_v093_signal": {"func": f35_combined_slope_cor_slope_diff_norm_10d_v093_signal},
    "f35_combined_slope_revenue_slope_diff_norm_10d_v094_signal": {"func": f35_combined_slope_revenue_slope_diff_norm_10d_v094_signal},
    "f35_combined_slope_sgna_slope_diff_norm_10d_v095_signal": {"func": f35_combined_slope_sgna_slope_diff_norm_10d_v095_signal},
    "f35_combined_slope_expense_velocity_slope_diff_norm_10d_v096_signal": {"func": f35_combined_slope_expense_velocity_slope_diff_norm_10d_v096_signal},
    "f35_combined_slope_cor_slope_diff_norm_21d_v097_signal": {"func": f35_combined_slope_cor_slope_diff_norm_21d_v097_signal},
    "f35_combined_slope_revenue_slope_diff_norm_21d_v098_signal": {"func": f35_combined_slope_revenue_slope_diff_norm_21d_v098_signal},
    "f35_combined_slope_sgna_slope_diff_norm_21d_v099_signal": {"func": f35_combined_slope_sgna_slope_diff_norm_21d_v099_signal},
    "f35_combined_slope_expense_velocity_slope_diff_norm_21d_v100_signal": {"func": f35_combined_slope_expense_velocity_slope_diff_norm_21d_v100_signal},
    "f35_combined_slope_cor_slope_diff_norm_42d_v101_signal": {"func": f35_combined_slope_cor_slope_diff_norm_42d_v101_signal},
    "f35_combined_slope_revenue_slope_diff_norm_42d_v102_signal": {"func": f35_combined_slope_revenue_slope_diff_norm_42d_v102_signal},
    "f35_combined_slope_sgna_slope_diff_norm_42d_v103_signal": {"func": f35_combined_slope_sgna_slope_diff_norm_42d_v103_signal},
    "f35_combined_slope_expense_velocity_slope_diff_norm_42d_v104_signal": {"func": f35_combined_slope_expense_velocity_slope_diff_norm_42d_v104_signal},
    "f35_combined_slope_cor_slope_diff_norm_63d_v105_signal": {"func": f35_combined_slope_cor_slope_diff_norm_63d_v105_signal},
    "f35_combined_slope_revenue_slope_diff_norm_63d_v106_signal": {"func": f35_combined_slope_revenue_slope_diff_norm_63d_v106_signal},
    "f35_combined_slope_sgna_slope_diff_norm_63d_v107_signal": {"func": f35_combined_slope_sgna_slope_diff_norm_63d_v107_signal},
    "f35_combined_slope_expense_velocity_slope_diff_norm_63d_v108_signal": {"func": f35_combined_slope_expense_velocity_slope_diff_norm_63d_v108_signal},
    "f35_combined_slope_cor_slope_diff_norm_126d_v109_signal": {"func": f35_combined_slope_cor_slope_diff_norm_126d_v109_signal},
    "f35_combined_slope_revenue_slope_diff_norm_126d_v110_signal": {"func": f35_combined_slope_revenue_slope_diff_norm_126d_v110_signal},
    "f35_combined_slope_sgna_slope_diff_norm_126d_v111_signal": {"func": f35_combined_slope_sgna_slope_diff_norm_126d_v111_signal},
    "f35_combined_slope_expense_velocity_slope_diff_norm_126d_v112_signal": {"func": f35_combined_slope_expense_velocity_slope_diff_norm_126d_v112_signal},
    "f35_combined_slope_cor_slope_diff_norm_252d_v113_signal": {"func": f35_combined_slope_cor_slope_diff_norm_252d_v113_signal},
    "f35_combined_slope_revenue_slope_diff_norm_252d_v114_signal": {"func": f35_combined_slope_revenue_slope_diff_norm_252d_v114_signal},
    "f35_combined_slope_sgna_slope_diff_norm_252d_v115_signal": {"func": f35_combined_slope_sgna_slope_diff_norm_252d_v115_signal},
    "f35_combined_slope_expense_velocity_slope_diff_norm_252d_v116_signal": {"func": f35_combined_slope_expense_velocity_slope_diff_norm_252d_v116_signal},
    "f35_combined_slope_cor_slope_diff_norm_504d_v117_signal": {"func": f35_combined_slope_cor_slope_diff_norm_504d_v117_signal},
    "f35_combined_slope_revenue_slope_diff_norm_504d_v118_signal": {"func": f35_combined_slope_revenue_slope_diff_norm_504d_v118_signal},
    "f35_combined_slope_sgna_slope_diff_norm_504d_v119_signal": {"func": f35_combined_slope_sgna_slope_diff_norm_504d_v119_signal},
    "f35_combined_slope_expense_velocity_slope_diff_norm_504d_v120_signal": {"func": f35_combined_slope_expense_velocity_slope_diff_norm_504d_v120_signal},
    "f35_combined_slope_cor_slope_diff_norm_756d_v121_signal": {"func": f35_combined_slope_cor_slope_diff_norm_756d_v121_signal},
    "f35_combined_slope_revenue_slope_diff_norm_756d_v122_signal": {"func": f35_combined_slope_revenue_slope_diff_norm_756d_v122_signal},
    "f35_combined_slope_sgna_slope_diff_norm_756d_v123_signal": {"func": f35_combined_slope_sgna_slope_diff_norm_756d_v123_signal},
    "f35_combined_slope_expense_velocity_slope_diff_norm_756d_v124_signal": {"func": f35_combined_slope_expense_velocity_slope_diff_norm_756d_v124_signal},
    "f35_combined_slope_cor_slope_diff_norm_1008d_v125_signal": {"func": f35_combined_slope_cor_slope_diff_norm_1008d_v125_signal},
    "f35_combined_slope_revenue_slope_diff_norm_1008d_v126_signal": {"func": f35_combined_slope_revenue_slope_diff_norm_1008d_v126_signal},
    "f35_combined_slope_sgna_slope_diff_norm_1008d_v127_signal": {"func": f35_combined_slope_sgna_slope_diff_norm_1008d_v127_signal},
    "f35_combined_slope_expense_velocity_slope_diff_norm_1008d_v128_signal": {"func": f35_combined_slope_expense_velocity_slope_diff_norm_1008d_v128_signal},
    "f35_combined_slope_cor_slope_diff_norm_1260d_v129_signal": {"func": f35_combined_slope_cor_slope_diff_norm_1260d_v129_signal},
    "f35_combined_slope_revenue_slope_diff_norm_1260d_v130_signal": {"func": f35_combined_slope_revenue_slope_diff_norm_1260d_v130_signal},
    "f35_combined_slope_sgna_slope_diff_norm_1260d_v131_signal": {"func": f35_combined_slope_sgna_slope_diff_norm_1260d_v131_signal},
    "f35_combined_slope_expense_velocity_slope_diff_norm_1260d_v132_signal": {"func": f35_combined_slope_expense_velocity_slope_diff_norm_1260d_v132_signal},
    "f35_combined_slope_cor_mom_z_5d_v133_signal": {"func": f35_combined_slope_cor_mom_z_5d_v133_signal},
    "f35_combined_slope_revenue_mom_z_5d_v134_signal": {"func": f35_combined_slope_revenue_mom_z_5d_v134_signal},
    "f35_combined_slope_sgna_mom_z_5d_v135_signal": {"func": f35_combined_slope_sgna_mom_z_5d_v135_signal},
    "f35_combined_slope_expense_velocity_mom_z_5d_v136_signal": {"func": f35_combined_slope_expense_velocity_mom_z_5d_v136_signal},
    "f35_combined_slope_cor_mom_z_10d_v137_signal": {"func": f35_combined_slope_cor_mom_z_10d_v137_signal},
    "f35_combined_slope_revenue_mom_z_10d_v138_signal": {"func": f35_combined_slope_revenue_mom_z_10d_v138_signal},
    "f35_combined_slope_sgna_mom_z_10d_v139_signal": {"func": f35_combined_slope_sgna_mom_z_10d_v139_signal},
    "f35_combined_slope_expense_velocity_mom_z_10d_v140_signal": {"func": f35_combined_slope_expense_velocity_mom_z_10d_v140_signal},
    "f35_combined_slope_cor_mom_z_21d_v141_signal": {"func": f35_combined_slope_cor_mom_z_21d_v141_signal},
    "f35_combined_slope_revenue_mom_z_21d_v142_signal": {"func": f35_combined_slope_revenue_mom_z_21d_v142_signal},
    "f35_combined_slope_sgna_mom_z_21d_v143_signal": {"func": f35_combined_slope_sgna_mom_z_21d_v143_signal},
    "f35_combined_slope_expense_velocity_mom_z_21d_v144_signal": {"func": f35_combined_slope_expense_velocity_mom_z_21d_v144_signal},
    "f35_combined_slope_cor_mom_z_42d_v145_signal": {"func": f35_combined_slope_cor_mom_z_42d_v145_signal},
    "f35_combined_slope_revenue_mom_z_42d_v146_signal": {"func": f35_combined_slope_revenue_mom_z_42d_v146_signal},
    "f35_combined_slope_sgna_mom_z_42d_v147_signal": {"func": f35_combined_slope_sgna_mom_z_42d_v147_signal},
    "f35_combined_slope_expense_velocity_mom_z_42d_v148_signal": {"func": f35_combined_slope_expense_velocity_mom_z_42d_v148_signal},
    "f35_combined_slope_cor_mom_z_63d_v149_signal": {"func": f35_combined_slope_cor_mom_z_63d_v149_signal},
    "f35_combined_slope_revenue_mom_z_63d_v150_signal": {"func": f35_combined_slope_revenue_mom_z_63d_v150_signal},
}

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "deferredrev": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "equity": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "deposits": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "divyield": np.random.normal(100, 10, n).cumsum(), "bvps": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "tangibles": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "grossmargin": np.random.normal(100, 10, n).cumsum(), "revenue": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "liabilitiesc": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum()
    })
    print(f"Verifying {len(REGISTRY)} functions for family 35...")
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
