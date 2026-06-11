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

def f07_insur_underwriting_cor_slope_pct_5d_v001_signal(cor):
    """Percentage slope for Raw level of cor over 5d window."""
    res = _slope_pct(cor, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_revenue_slope_pct_5d_v002_signal(revenue):
    """Percentage slope for Raw level of revenue over 5d window."""
    res = _slope_pct(revenue, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_grossmargin_slope_pct_5d_v003_signal(grossmargin):
    """Percentage slope for Raw level of grossmargin over 5d window."""
    res = _slope_pct(grossmargin, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_combined_ratio_slope_pct_5d_v004_signal(cor, revenue):
    """Percentage slope for Insurance combined ratio proxy over 5d window."""
    res = _slope_pct(_ratio(cor, revenue), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_uw_profitability_slope_pct_5d_v005_signal(grossmargin):
    """Percentage slope for Underwriting profitability over 5d window."""
    res = _slope_pct(grossmargin, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_loss_load_slope_pct_5d_v006_signal(cor, grossmargin):
    """Percentage slope for Relative cost of premiums over 5d window."""
    res = _slope_pct(_ratio(cor, grossmargin + cor), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_cor_slope_pct_10d_v007_signal(cor):
    """Percentage slope for Raw level of cor over 10d window."""
    res = _slope_pct(cor, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_revenue_slope_pct_10d_v008_signal(revenue):
    """Percentage slope for Raw level of revenue over 10d window."""
    res = _slope_pct(revenue, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_grossmargin_slope_pct_10d_v009_signal(grossmargin):
    """Percentage slope for Raw level of grossmargin over 10d window."""
    res = _slope_pct(grossmargin, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_combined_ratio_slope_pct_10d_v010_signal(cor, revenue):
    """Percentage slope for Insurance combined ratio proxy over 10d window."""
    res = _slope_pct(_ratio(cor, revenue), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_uw_profitability_slope_pct_10d_v011_signal(grossmargin):
    """Percentage slope for Underwriting profitability over 10d window."""
    res = _slope_pct(grossmargin, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_loss_load_slope_pct_10d_v012_signal(cor, grossmargin):
    """Percentage slope for Relative cost of premiums over 10d window."""
    res = _slope_pct(_ratio(cor, grossmargin + cor), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_cor_slope_pct_21d_v013_signal(cor):
    """Percentage slope for Raw level of cor over 21d window."""
    res = _slope_pct(cor, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_revenue_slope_pct_21d_v014_signal(revenue):
    """Percentage slope for Raw level of revenue over 21d window."""
    res = _slope_pct(revenue, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_grossmargin_slope_pct_21d_v015_signal(grossmargin):
    """Percentage slope for Raw level of grossmargin over 21d window."""
    res = _slope_pct(grossmargin, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_combined_ratio_slope_pct_21d_v016_signal(cor, revenue):
    """Percentage slope for Insurance combined ratio proxy over 21d window."""
    res = _slope_pct(_ratio(cor, revenue), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_uw_profitability_slope_pct_21d_v017_signal(grossmargin):
    """Percentage slope for Underwriting profitability over 21d window."""
    res = _slope_pct(grossmargin, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_loss_load_slope_pct_21d_v018_signal(cor, grossmargin):
    """Percentage slope for Relative cost of premiums over 21d window."""
    res = _slope_pct(_ratio(cor, grossmargin + cor), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_cor_slope_pct_42d_v019_signal(cor):
    """Percentage slope for Raw level of cor over 42d window."""
    res = _slope_pct(cor, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_revenue_slope_pct_42d_v020_signal(revenue):
    """Percentage slope for Raw level of revenue over 42d window."""
    res = _slope_pct(revenue, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_grossmargin_slope_pct_42d_v021_signal(grossmargin):
    """Percentage slope for Raw level of grossmargin over 42d window."""
    res = _slope_pct(grossmargin, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_combined_ratio_slope_pct_42d_v022_signal(cor, revenue):
    """Percentage slope for Insurance combined ratio proxy over 42d window."""
    res = _slope_pct(_ratio(cor, revenue), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_uw_profitability_slope_pct_42d_v023_signal(grossmargin):
    """Percentage slope for Underwriting profitability over 42d window."""
    res = _slope_pct(grossmargin, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_loss_load_slope_pct_42d_v024_signal(cor, grossmargin):
    """Percentage slope for Relative cost of premiums over 42d window."""
    res = _slope_pct(_ratio(cor, grossmargin + cor), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_cor_slope_pct_63d_v025_signal(cor):
    """Percentage slope for Raw level of cor over 63d window."""
    res = _slope_pct(cor, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_revenue_slope_pct_63d_v026_signal(revenue):
    """Percentage slope for Raw level of revenue over 63d window."""
    res = _slope_pct(revenue, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_grossmargin_slope_pct_63d_v027_signal(grossmargin):
    """Percentage slope for Raw level of grossmargin over 63d window."""
    res = _slope_pct(grossmargin, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_combined_ratio_slope_pct_63d_v028_signal(cor, revenue):
    """Percentage slope for Insurance combined ratio proxy over 63d window."""
    res = _slope_pct(_ratio(cor, revenue), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_uw_profitability_slope_pct_63d_v029_signal(grossmargin):
    """Percentage slope for Underwriting profitability over 63d window."""
    res = _slope_pct(grossmargin, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_loss_load_slope_pct_63d_v030_signal(cor, grossmargin):
    """Percentage slope for Relative cost of premiums over 63d window."""
    res = _slope_pct(_ratio(cor, grossmargin + cor), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_cor_slope_pct_126d_v031_signal(cor):
    """Percentage slope for Raw level of cor over 126d window."""
    res = _slope_pct(cor, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_revenue_slope_pct_126d_v032_signal(revenue):
    """Percentage slope for Raw level of revenue over 126d window."""
    res = _slope_pct(revenue, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_grossmargin_slope_pct_126d_v033_signal(grossmargin):
    """Percentage slope for Raw level of grossmargin over 126d window."""
    res = _slope_pct(grossmargin, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_combined_ratio_slope_pct_126d_v034_signal(cor, revenue):
    """Percentage slope for Insurance combined ratio proxy over 126d window."""
    res = _slope_pct(_ratio(cor, revenue), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_uw_profitability_slope_pct_126d_v035_signal(grossmargin):
    """Percentage slope for Underwriting profitability over 126d window."""
    res = _slope_pct(grossmargin, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_loss_load_slope_pct_126d_v036_signal(cor, grossmargin):
    """Percentage slope for Relative cost of premiums over 126d window."""
    res = _slope_pct(_ratio(cor, grossmargin + cor), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_cor_slope_pct_252d_v037_signal(cor):
    """Percentage slope for Raw level of cor over 252d window."""
    res = _slope_pct(cor, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_revenue_slope_pct_252d_v038_signal(revenue):
    """Percentage slope for Raw level of revenue over 252d window."""
    res = _slope_pct(revenue, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_grossmargin_slope_pct_252d_v039_signal(grossmargin):
    """Percentage slope for Raw level of grossmargin over 252d window."""
    res = _slope_pct(grossmargin, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_combined_ratio_slope_pct_252d_v040_signal(cor, revenue):
    """Percentage slope for Insurance combined ratio proxy over 252d window."""
    res = _slope_pct(_ratio(cor, revenue), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_uw_profitability_slope_pct_252d_v041_signal(grossmargin):
    """Percentage slope for Underwriting profitability over 252d window."""
    res = _slope_pct(grossmargin, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_loss_load_slope_pct_252d_v042_signal(cor, grossmargin):
    """Percentage slope for Relative cost of premiums over 252d window."""
    res = _slope_pct(_ratio(cor, grossmargin + cor), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_cor_slope_pct_504d_v043_signal(cor):
    """Percentage slope for Raw level of cor over 504d window."""
    res = _slope_pct(cor, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_revenue_slope_pct_504d_v044_signal(revenue):
    """Percentage slope for Raw level of revenue over 504d window."""
    res = _slope_pct(revenue, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_grossmargin_slope_pct_504d_v045_signal(grossmargin):
    """Percentage slope for Raw level of grossmargin over 504d window."""
    res = _slope_pct(grossmargin, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_combined_ratio_slope_pct_504d_v046_signal(cor, revenue):
    """Percentage slope for Insurance combined ratio proxy over 504d window."""
    res = _slope_pct(_ratio(cor, revenue), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_uw_profitability_slope_pct_504d_v047_signal(grossmargin):
    """Percentage slope for Underwriting profitability over 504d window."""
    res = _slope_pct(grossmargin, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_loss_load_slope_pct_504d_v048_signal(cor, grossmargin):
    """Percentage slope for Relative cost of premiums over 504d window."""
    res = _slope_pct(_ratio(cor, grossmargin + cor), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_cor_slope_pct_756d_v049_signal(cor):
    """Percentage slope for Raw level of cor over 756d window."""
    res = _slope_pct(cor, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_revenue_slope_pct_756d_v050_signal(revenue):
    """Percentage slope for Raw level of revenue over 756d window."""
    res = _slope_pct(revenue, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_grossmargin_slope_pct_756d_v051_signal(grossmargin):
    """Percentage slope for Raw level of grossmargin over 756d window."""
    res = _slope_pct(grossmargin, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_combined_ratio_slope_pct_756d_v052_signal(cor, revenue):
    """Percentage slope for Insurance combined ratio proxy over 756d window."""
    res = _slope_pct(_ratio(cor, revenue), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_uw_profitability_slope_pct_756d_v053_signal(grossmargin):
    """Percentage slope for Underwriting profitability over 756d window."""
    res = _slope_pct(grossmargin, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_loss_load_slope_pct_756d_v054_signal(cor, grossmargin):
    """Percentage slope for Relative cost of premiums over 756d window."""
    res = _slope_pct(_ratio(cor, grossmargin + cor), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_cor_slope_pct_1008d_v055_signal(cor):
    """Percentage slope for Raw level of cor over 1008d window."""
    res = _slope_pct(cor, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_revenue_slope_pct_1008d_v056_signal(revenue):
    """Percentage slope for Raw level of revenue over 1008d window."""
    res = _slope_pct(revenue, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_grossmargin_slope_pct_1008d_v057_signal(grossmargin):
    """Percentage slope for Raw level of grossmargin over 1008d window."""
    res = _slope_pct(grossmargin, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_combined_ratio_slope_pct_1008d_v058_signal(cor, revenue):
    """Percentage slope for Insurance combined ratio proxy over 1008d window."""
    res = _slope_pct(_ratio(cor, revenue), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_uw_profitability_slope_pct_1008d_v059_signal(grossmargin):
    """Percentage slope for Underwriting profitability over 1008d window."""
    res = _slope_pct(grossmargin, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_loss_load_slope_pct_1008d_v060_signal(cor, grossmargin):
    """Percentage slope for Relative cost of premiums over 1008d window."""
    res = _slope_pct(_ratio(cor, grossmargin + cor), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_cor_slope_pct_1260d_v061_signal(cor):
    """Percentage slope for Raw level of cor over 1260d window."""
    res = _slope_pct(cor, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_revenue_slope_pct_1260d_v062_signal(revenue):
    """Percentage slope for Raw level of revenue over 1260d window."""
    res = _slope_pct(revenue, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_grossmargin_slope_pct_1260d_v063_signal(grossmargin):
    """Percentage slope for Raw level of grossmargin over 1260d window."""
    res = _slope_pct(grossmargin, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_combined_ratio_slope_pct_1260d_v064_signal(cor, revenue):
    """Percentage slope for Insurance combined ratio proxy over 1260d window."""
    res = _slope_pct(_ratio(cor, revenue), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_uw_profitability_slope_pct_1260d_v065_signal(grossmargin):
    """Percentage slope for Underwriting profitability over 1260d window."""
    res = _slope_pct(grossmargin, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_loss_load_slope_pct_1260d_v066_signal(cor, grossmargin):
    """Percentage slope for Relative cost of premiums over 1260d window."""
    res = _slope_pct(_ratio(cor, grossmargin + cor), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_cor_jerk_5d_v067_signal(cor):
    """Acceleration/Jerk for Raw level of cor over 5d window."""
    res = _jerk(cor, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_revenue_jerk_5d_v068_signal(revenue):
    """Acceleration/Jerk for Raw level of revenue over 5d window."""
    res = _jerk(revenue, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_grossmargin_jerk_5d_v069_signal(grossmargin):
    """Acceleration/Jerk for Raw level of grossmargin over 5d window."""
    res = _jerk(grossmargin, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_combined_ratio_jerk_5d_v070_signal(cor, revenue):
    """Acceleration/Jerk for Insurance combined ratio proxy over 5d window."""
    res = _jerk(_ratio(cor, revenue), 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_uw_profitability_jerk_5d_v071_signal(grossmargin):
    """Acceleration/Jerk for Underwriting profitability over 5d window."""
    res = _jerk(grossmargin, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_loss_load_jerk_5d_v072_signal(cor, grossmargin):
    """Acceleration/Jerk for Relative cost of premiums over 5d window."""
    res = _jerk(_ratio(cor, grossmargin + cor), 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_cor_jerk_10d_v073_signal(cor):
    """Acceleration/Jerk for Raw level of cor over 10d window."""
    res = _jerk(cor, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_revenue_jerk_10d_v074_signal(revenue):
    """Acceleration/Jerk for Raw level of revenue over 10d window."""
    res = _jerk(revenue, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_grossmargin_jerk_10d_v075_signal(grossmargin):
    """Acceleration/Jerk for Raw level of grossmargin over 10d window."""
    res = _jerk(grossmargin, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_combined_ratio_jerk_10d_v076_signal(cor, revenue):
    """Acceleration/Jerk for Insurance combined ratio proxy over 10d window."""
    res = _jerk(_ratio(cor, revenue), 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_uw_profitability_jerk_10d_v077_signal(grossmargin):
    """Acceleration/Jerk for Underwriting profitability over 10d window."""
    res = _jerk(grossmargin, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_loss_load_jerk_10d_v078_signal(cor, grossmargin):
    """Acceleration/Jerk for Relative cost of premiums over 10d window."""
    res = _jerk(_ratio(cor, grossmargin + cor), 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_cor_jerk_21d_v079_signal(cor):
    """Acceleration/Jerk for Raw level of cor over 21d window."""
    res = _jerk(cor, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_revenue_jerk_21d_v080_signal(revenue):
    """Acceleration/Jerk for Raw level of revenue over 21d window."""
    res = _jerk(revenue, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_grossmargin_jerk_21d_v081_signal(grossmargin):
    """Acceleration/Jerk for Raw level of grossmargin over 21d window."""
    res = _jerk(grossmargin, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_combined_ratio_jerk_21d_v082_signal(cor, revenue):
    """Acceleration/Jerk for Insurance combined ratio proxy over 21d window."""
    res = _jerk(_ratio(cor, revenue), 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_uw_profitability_jerk_21d_v083_signal(grossmargin):
    """Acceleration/Jerk for Underwriting profitability over 21d window."""
    res = _jerk(grossmargin, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_loss_load_jerk_21d_v084_signal(cor, grossmargin):
    """Acceleration/Jerk for Relative cost of premiums over 21d window."""
    res = _jerk(_ratio(cor, grossmargin + cor), 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_cor_jerk_42d_v085_signal(cor):
    """Acceleration/Jerk for Raw level of cor over 42d window."""
    res = _jerk(cor, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_revenue_jerk_42d_v086_signal(revenue):
    """Acceleration/Jerk for Raw level of revenue over 42d window."""
    res = _jerk(revenue, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_grossmargin_jerk_42d_v087_signal(grossmargin):
    """Acceleration/Jerk for Raw level of grossmargin over 42d window."""
    res = _jerk(grossmargin, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_combined_ratio_jerk_42d_v088_signal(cor, revenue):
    """Acceleration/Jerk for Insurance combined ratio proxy over 42d window."""
    res = _jerk(_ratio(cor, revenue), 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_uw_profitability_jerk_42d_v089_signal(grossmargin):
    """Acceleration/Jerk for Underwriting profitability over 42d window."""
    res = _jerk(grossmargin, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_loss_load_jerk_42d_v090_signal(cor, grossmargin):
    """Acceleration/Jerk for Relative cost of premiums over 42d window."""
    res = _jerk(_ratio(cor, grossmargin + cor), 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_cor_jerk_63d_v091_signal(cor):
    """Acceleration/Jerk for Raw level of cor over 63d window."""
    res = _jerk(cor, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_revenue_jerk_63d_v092_signal(revenue):
    """Acceleration/Jerk for Raw level of revenue over 63d window."""
    res = _jerk(revenue, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_grossmargin_jerk_63d_v093_signal(grossmargin):
    """Acceleration/Jerk for Raw level of grossmargin over 63d window."""
    res = _jerk(grossmargin, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_combined_ratio_jerk_63d_v094_signal(cor, revenue):
    """Acceleration/Jerk for Insurance combined ratio proxy over 63d window."""
    res = _jerk(_ratio(cor, revenue), 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_uw_profitability_jerk_63d_v095_signal(grossmargin):
    """Acceleration/Jerk for Underwriting profitability over 63d window."""
    res = _jerk(grossmargin, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_loss_load_jerk_63d_v096_signal(cor, grossmargin):
    """Acceleration/Jerk for Relative cost of premiums over 63d window."""
    res = _jerk(_ratio(cor, grossmargin + cor), 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_cor_jerk_126d_v097_signal(cor):
    """Acceleration/Jerk for Raw level of cor over 126d window."""
    res = _jerk(cor, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_revenue_jerk_126d_v098_signal(revenue):
    """Acceleration/Jerk for Raw level of revenue over 126d window."""
    res = _jerk(revenue, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_grossmargin_jerk_126d_v099_signal(grossmargin):
    """Acceleration/Jerk for Raw level of grossmargin over 126d window."""
    res = _jerk(grossmargin, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_combined_ratio_jerk_126d_v100_signal(cor, revenue):
    """Acceleration/Jerk for Insurance combined ratio proxy over 126d window."""
    res = _jerk(_ratio(cor, revenue), 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_uw_profitability_jerk_126d_v101_signal(grossmargin):
    """Acceleration/Jerk for Underwriting profitability over 126d window."""
    res = _jerk(grossmargin, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_loss_load_jerk_126d_v102_signal(cor, grossmargin):
    """Acceleration/Jerk for Relative cost of premiums over 126d window."""
    res = _jerk(_ratio(cor, grossmargin + cor), 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_cor_jerk_252d_v103_signal(cor):
    """Acceleration/Jerk for Raw level of cor over 252d window."""
    res = _jerk(cor, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_revenue_jerk_252d_v104_signal(revenue):
    """Acceleration/Jerk for Raw level of revenue over 252d window."""
    res = _jerk(revenue, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_grossmargin_jerk_252d_v105_signal(grossmargin):
    """Acceleration/Jerk for Raw level of grossmargin over 252d window."""
    res = _jerk(grossmargin, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_combined_ratio_jerk_252d_v106_signal(cor, revenue):
    """Acceleration/Jerk for Insurance combined ratio proxy over 252d window."""
    res = _jerk(_ratio(cor, revenue), 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_uw_profitability_jerk_252d_v107_signal(grossmargin):
    """Acceleration/Jerk for Underwriting profitability over 252d window."""
    res = _jerk(grossmargin, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_loss_load_jerk_252d_v108_signal(cor, grossmargin):
    """Acceleration/Jerk for Relative cost of premiums over 252d window."""
    res = _jerk(_ratio(cor, grossmargin + cor), 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_cor_jerk_504d_v109_signal(cor):
    """Acceleration/Jerk for Raw level of cor over 504d window."""
    res = _jerk(cor, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_revenue_jerk_504d_v110_signal(revenue):
    """Acceleration/Jerk for Raw level of revenue over 504d window."""
    res = _jerk(revenue, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_grossmargin_jerk_504d_v111_signal(grossmargin):
    """Acceleration/Jerk for Raw level of grossmargin over 504d window."""
    res = _jerk(grossmargin, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_combined_ratio_jerk_504d_v112_signal(cor, revenue):
    """Acceleration/Jerk for Insurance combined ratio proxy over 504d window."""
    res = _jerk(_ratio(cor, revenue), 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_uw_profitability_jerk_504d_v113_signal(grossmargin):
    """Acceleration/Jerk for Underwriting profitability over 504d window."""
    res = _jerk(grossmargin, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_loss_load_jerk_504d_v114_signal(cor, grossmargin):
    """Acceleration/Jerk for Relative cost of premiums over 504d window."""
    res = _jerk(_ratio(cor, grossmargin + cor), 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_cor_jerk_756d_v115_signal(cor):
    """Acceleration/Jerk for Raw level of cor over 756d window."""
    res = _jerk(cor, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_revenue_jerk_756d_v116_signal(revenue):
    """Acceleration/Jerk for Raw level of revenue over 756d window."""
    res = _jerk(revenue, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_grossmargin_jerk_756d_v117_signal(grossmargin):
    """Acceleration/Jerk for Raw level of grossmargin over 756d window."""
    res = _jerk(grossmargin, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_combined_ratio_jerk_756d_v118_signal(cor, revenue):
    """Acceleration/Jerk for Insurance combined ratio proxy over 756d window."""
    res = _jerk(_ratio(cor, revenue), 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_uw_profitability_jerk_756d_v119_signal(grossmargin):
    """Acceleration/Jerk for Underwriting profitability over 756d window."""
    res = _jerk(grossmargin, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_loss_load_jerk_756d_v120_signal(cor, grossmargin):
    """Acceleration/Jerk for Relative cost of premiums over 756d window."""
    res = _jerk(_ratio(cor, grossmargin + cor), 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_cor_jerk_1008d_v121_signal(cor):
    """Acceleration/Jerk for Raw level of cor over 1008d window."""
    res = _jerk(cor, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_revenue_jerk_1008d_v122_signal(revenue):
    """Acceleration/Jerk for Raw level of revenue over 1008d window."""
    res = _jerk(revenue, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_grossmargin_jerk_1008d_v123_signal(grossmargin):
    """Acceleration/Jerk for Raw level of grossmargin over 1008d window."""
    res = _jerk(grossmargin, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_combined_ratio_jerk_1008d_v124_signal(cor, revenue):
    """Acceleration/Jerk for Insurance combined ratio proxy over 1008d window."""
    res = _jerk(_ratio(cor, revenue), 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_uw_profitability_jerk_1008d_v125_signal(grossmargin):
    """Acceleration/Jerk for Underwriting profitability over 1008d window."""
    res = _jerk(grossmargin, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_loss_load_jerk_1008d_v126_signal(cor, grossmargin):
    """Acceleration/Jerk for Relative cost of premiums over 1008d window."""
    res = _jerk(_ratio(cor, grossmargin + cor), 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_cor_jerk_1260d_v127_signal(cor):
    """Acceleration/Jerk for Raw level of cor over 1260d window."""
    res = _jerk(cor, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_revenue_jerk_1260d_v128_signal(revenue):
    """Acceleration/Jerk for Raw level of revenue over 1260d window."""
    res = _jerk(revenue, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_grossmargin_jerk_1260d_v129_signal(grossmargin):
    """Acceleration/Jerk for Raw level of grossmargin over 1260d window."""
    res = _jerk(grossmargin, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_combined_ratio_jerk_1260d_v130_signal(cor, revenue):
    """Acceleration/Jerk for Insurance combined ratio proxy over 1260d window."""
    res = _jerk(_ratio(cor, revenue), 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_uw_profitability_jerk_1260d_v131_signal(grossmargin):
    """Acceleration/Jerk for Underwriting profitability over 1260d window."""
    res = _jerk(grossmargin, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_loss_load_jerk_1260d_v132_signal(cor, grossmargin):
    """Acceleration/Jerk for Relative cost of premiums over 1260d window."""
    res = _jerk(_ratio(cor, grossmargin + cor), 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_cor_slope_diff_norm_5d_v133_signal(cor):
    """Normalized slope change for Raw level of cor over 5d window."""
    res = (_slope_pct(cor, 5).diff(5) / _sma(cor.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_revenue_slope_diff_norm_5d_v134_signal(revenue):
    """Normalized slope change for Raw level of revenue over 5d window."""
    res = (_slope_pct(revenue, 5).diff(5) / _sma(revenue.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_grossmargin_slope_diff_norm_5d_v135_signal(grossmargin):
    """Normalized slope change for Raw level of grossmargin over 5d window."""
    res = (_slope_pct(grossmargin, 5).diff(5) / _sma(grossmargin.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_combined_ratio_slope_diff_norm_5d_v136_signal(cor, revenue):
    """Normalized slope change for Insurance combined ratio proxy over 5d window."""
    res = (_slope_pct(_ratio(cor, revenue), 5).diff(5) / _sma(_ratio(cor, revenue).abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_uw_profitability_slope_diff_norm_5d_v137_signal(grossmargin):
    """Normalized slope change for Underwriting profitability over 5d window."""
    res = (_slope_pct(grossmargin, 5).diff(5) / _sma(grossmargin.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_loss_load_slope_diff_norm_5d_v138_signal(cor, grossmargin):
    """Normalized slope change for Relative cost of premiums over 5d window."""
    res = (_slope_pct(_ratio(cor, grossmargin + cor), 5).diff(5) / _sma(_ratio(cor, grossmargin + cor).abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_cor_slope_diff_norm_10d_v139_signal(cor):
    """Normalized slope change for Raw level of cor over 10d window."""
    res = (_slope_pct(cor, 10).diff(10) / _sma(cor.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_revenue_slope_diff_norm_10d_v140_signal(revenue):
    """Normalized slope change for Raw level of revenue over 10d window."""
    res = (_slope_pct(revenue, 10).diff(10) / _sma(revenue.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_grossmargin_slope_diff_norm_10d_v141_signal(grossmargin):
    """Normalized slope change for Raw level of grossmargin over 10d window."""
    res = (_slope_pct(grossmargin, 10).diff(10) / _sma(grossmargin.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_combined_ratio_slope_diff_norm_10d_v142_signal(cor, revenue):
    """Normalized slope change for Insurance combined ratio proxy over 10d window."""
    res = (_slope_pct(_ratio(cor, revenue), 10).diff(10) / _sma(_ratio(cor, revenue).abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_uw_profitability_slope_diff_norm_10d_v143_signal(grossmargin):
    """Normalized slope change for Underwriting profitability over 10d window."""
    res = (_slope_pct(grossmargin, 10).diff(10) / _sma(grossmargin.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_loss_load_slope_diff_norm_10d_v144_signal(cor, grossmargin):
    """Normalized slope change for Relative cost of premiums over 10d window."""
    res = (_slope_pct(_ratio(cor, grossmargin + cor), 10).diff(10) / _sma(_ratio(cor, grossmargin + cor).abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_cor_slope_diff_norm_21d_v145_signal(cor):
    """Normalized slope change for Raw level of cor over 21d window."""
    res = (_slope_pct(cor, 21).diff(21) / _sma(cor.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_revenue_slope_diff_norm_21d_v146_signal(revenue):
    """Normalized slope change for Raw level of revenue over 21d window."""
    res = (_slope_pct(revenue, 21).diff(21) / _sma(revenue.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_grossmargin_slope_diff_norm_21d_v147_signal(grossmargin):
    """Normalized slope change for Raw level of grossmargin over 21d window."""
    res = (_slope_pct(grossmargin, 21).diff(21) / _sma(grossmargin.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_combined_ratio_slope_diff_norm_21d_v148_signal(cor, revenue):
    """Normalized slope change for Insurance combined ratio proxy over 21d window."""
    res = (_slope_pct(_ratio(cor, revenue), 21).diff(21) / _sma(_ratio(cor, revenue).abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_uw_profitability_slope_diff_norm_21d_v149_signal(grossmargin):
    """Normalized slope change for Underwriting profitability over 21d window."""
    res = (_slope_pct(grossmargin, 21).diff(21) / _sma(grossmargin.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_loss_load_slope_diff_norm_21d_v150_signal(cor, grossmargin):
    """Normalized slope change for Relative cost of premiums over 21d window."""
    res = (_slope_pct(_ratio(cor, grossmargin + cor), 21).diff(21) / _sma(_ratio(cor, grossmargin + cor).abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)


# ===== Feature Registry =====
REGISTRY = {
    "f07_insur_underwriting_cor_slope_pct_5d_v001_signal": {"func": f07_insur_underwriting_cor_slope_pct_5d_v001_signal},
    "f07_insur_underwriting_revenue_slope_pct_5d_v002_signal": {"func": f07_insur_underwriting_revenue_slope_pct_5d_v002_signal},
    "f07_insur_underwriting_grossmargin_slope_pct_5d_v003_signal": {"func": f07_insur_underwriting_grossmargin_slope_pct_5d_v003_signal},
    "f07_insur_underwriting_combined_ratio_slope_pct_5d_v004_signal": {"func": f07_insur_underwriting_combined_ratio_slope_pct_5d_v004_signal},
    "f07_insur_underwriting_uw_profitability_slope_pct_5d_v005_signal": {"func": f07_insur_underwriting_uw_profitability_slope_pct_5d_v005_signal},
    "f07_insur_underwriting_loss_load_slope_pct_5d_v006_signal": {"func": f07_insur_underwriting_loss_load_slope_pct_5d_v006_signal},
    "f07_insur_underwriting_cor_slope_pct_10d_v007_signal": {"func": f07_insur_underwriting_cor_slope_pct_10d_v007_signal},
    "f07_insur_underwriting_revenue_slope_pct_10d_v008_signal": {"func": f07_insur_underwriting_revenue_slope_pct_10d_v008_signal},
    "f07_insur_underwriting_grossmargin_slope_pct_10d_v009_signal": {"func": f07_insur_underwriting_grossmargin_slope_pct_10d_v009_signal},
    "f07_insur_underwriting_combined_ratio_slope_pct_10d_v010_signal": {"func": f07_insur_underwriting_combined_ratio_slope_pct_10d_v010_signal},
    "f07_insur_underwriting_uw_profitability_slope_pct_10d_v011_signal": {"func": f07_insur_underwriting_uw_profitability_slope_pct_10d_v011_signal},
    "f07_insur_underwriting_loss_load_slope_pct_10d_v012_signal": {"func": f07_insur_underwriting_loss_load_slope_pct_10d_v012_signal},
    "f07_insur_underwriting_cor_slope_pct_21d_v013_signal": {"func": f07_insur_underwriting_cor_slope_pct_21d_v013_signal},
    "f07_insur_underwriting_revenue_slope_pct_21d_v014_signal": {"func": f07_insur_underwriting_revenue_slope_pct_21d_v014_signal},
    "f07_insur_underwriting_grossmargin_slope_pct_21d_v015_signal": {"func": f07_insur_underwriting_grossmargin_slope_pct_21d_v015_signal},
    "f07_insur_underwriting_combined_ratio_slope_pct_21d_v016_signal": {"func": f07_insur_underwriting_combined_ratio_slope_pct_21d_v016_signal},
    "f07_insur_underwriting_uw_profitability_slope_pct_21d_v017_signal": {"func": f07_insur_underwriting_uw_profitability_slope_pct_21d_v017_signal},
    "f07_insur_underwriting_loss_load_slope_pct_21d_v018_signal": {"func": f07_insur_underwriting_loss_load_slope_pct_21d_v018_signal},
    "f07_insur_underwriting_cor_slope_pct_42d_v019_signal": {"func": f07_insur_underwriting_cor_slope_pct_42d_v019_signal},
    "f07_insur_underwriting_revenue_slope_pct_42d_v020_signal": {"func": f07_insur_underwriting_revenue_slope_pct_42d_v020_signal},
    "f07_insur_underwriting_grossmargin_slope_pct_42d_v021_signal": {"func": f07_insur_underwriting_grossmargin_slope_pct_42d_v021_signal},
    "f07_insur_underwriting_combined_ratio_slope_pct_42d_v022_signal": {"func": f07_insur_underwriting_combined_ratio_slope_pct_42d_v022_signal},
    "f07_insur_underwriting_uw_profitability_slope_pct_42d_v023_signal": {"func": f07_insur_underwriting_uw_profitability_slope_pct_42d_v023_signal},
    "f07_insur_underwriting_loss_load_slope_pct_42d_v024_signal": {"func": f07_insur_underwriting_loss_load_slope_pct_42d_v024_signal},
    "f07_insur_underwriting_cor_slope_pct_63d_v025_signal": {"func": f07_insur_underwriting_cor_slope_pct_63d_v025_signal},
    "f07_insur_underwriting_revenue_slope_pct_63d_v026_signal": {"func": f07_insur_underwriting_revenue_slope_pct_63d_v026_signal},
    "f07_insur_underwriting_grossmargin_slope_pct_63d_v027_signal": {"func": f07_insur_underwriting_grossmargin_slope_pct_63d_v027_signal},
    "f07_insur_underwriting_combined_ratio_slope_pct_63d_v028_signal": {"func": f07_insur_underwriting_combined_ratio_slope_pct_63d_v028_signal},
    "f07_insur_underwriting_uw_profitability_slope_pct_63d_v029_signal": {"func": f07_insur_underwriting_uw_profitability_slope_pct_63d_v029_signal},
    "f07_insur_underwriting_loss_load_slope_pct_63d_v030_signal": {"func": f07_insur_underwriting_loss_load_slope_pct_63d_v030_signal},
    "f07_insur_underwriting_cor_slope_pct_126d_v031_signal": {"func": f07_insur_underwriting_cor_slope_pct_126d_v031_signal},
    "f07_insur_underwriting_revenue_slope_pct_126d_v032_signal": {"func": f07_insur_underwriting_revenue_slope_pct_126d_v032_signal},
    "f07_insur_underwriting_grossmargin_slope_pct_126d_v033_signal": {"func": f07_insur_underwriting_grossmargin_slope_pct_126d_v033_signal},
    "f07_insur_underwriting_combined_ratio_slope_pct_126d_v034_signal": {"func": f07_insur_underwriting_combined_ratio_slope_pct_126d_v034_signal},
    "f07_insur_underwriting_uw_profitability_slope_pct_126d_v035_signal": {"func": f07_insur_underwriting_uw_profitability_slope_pct_126d_v035_signal},
    "f07_insur_underwriting_loss_load_slope_pct_126d_v036_signal": {"func": f07_insur_underwriting_loss_load_slope_pct_126d_v036_signal},
    "f07_insur_underwriting_cor_slope_pct_252d_v037_signal": {"func": f07_insur_underwriting_cor_slope_pct_252d_v037_signal},
    "f07_insur_underwriting_revenue_slope_pct_252d_v038_signal": {"func": f07_insur_underwriting_revenue_slope_pct_252d_v038_signal},
    "f07_insur_underwriting_grossmargin_slope_pct_252d_v039_signal": {"func": f07_insur_underwriting_grossmargin_slope_pct_252d_v039_signal},
    "f07_insur_underwriting_combined_ratio_slope_pct_252d_v040_signal": {"func": f07_insur_underwriting_combined_ratio_slope_pct_252d_v040_signal},
    "f07_insur_underwriting_uw_profitability_slope_pct_252d_v041_signal": {"func": f07_insur_underwriting_uw_profitability_slope_pct_252d_v041_signal},
    "f07_insur_underwriting_loss_load_slope_pct_252d_v042_signal": {"func": f07_insur_underwriting_loss_load_slope_pct_252d_v042_signal},
    "f07_insur_underwriting_cor_slope_pct_504d_v043_signal": {"func": f07_insur_underwriting_cor_slope_pct_504d_v043_signal},
    "f07_insur_underwriting_revenue_slope_pct_504d_v044_signal": {"func": f07_insur_underwriting_revenue_slope_pct_504d_v044_signal},
    "f07_insur_underwriting_grossmargin_slope_pct_504d_v045_signal": {"func": f07_insur_underwriting_grossmargin_slope_pct_504d_v045_signal},
    "f07_insur_underwriting_combined_ratio_slope_pct_504d_v046_signal": {"func": f07_insur_underwriting_combined_ratio_slope_pct_504d_v046_signal},
    "f07_insur_underwriting_uw_profitability_slope_pct_504d_v047_signal": {"func": f07_insur_underwriting_uw_profitability_slope_pct_504d_v047_signal},
    "f07_insur_underwriting_loss_load_slope_pct_504d_v048_signal": {"func": f07_insur_underwriting_loss_load_slope_pct_504d_v048_signal},
    "f07_insur_underwriting_cor_slope_pct_756d_v049_signal": {"func": f07_insur_underwriting_cor_slope_pct_756d_v049_signal},
    "f07_insur_underwriting_revenue_slope_pct_756d_v050_signal": {"func": f07_insur_underwriting_revenue_slope_pct_756d_v050_signal},
    "f07_insur_underwriting_grossmargin_slope_pct_756d_v051_signal": {"func": f07_insur_underwriting_grossmargin_slope_pct_756d_v051_signal},
    "f07_insur_underwriting_combined_ratio_slope_pct_756d_v052_signal": {"func": f07_insur_underwriting_combined_ratio_slope_pct_756d_v052_signal},
    "f07_insur_underwriting_uw_profitability_slope_pct_756d_v053_signal": {"func": f07_insur_underwriting_uw_profitability_slope_pct_756d_v053_signal},
    "f07_insur_underwriting_loss_load_slope_pct_756d_v054_signal": {"func": f07_insur_underwriting_loss_load_slope_pct_756d_v054_signal},
    "f07_insur_underwriting_cor_slope_pct_1008d_v055_signal": {"func": f07_insur_underwriting_cor_slope_pct_1008d_v055_signal},
    "f07_insur_underwriting_revenue_slope_pct_1008d_v056_signal": {"func": f07_insur_underwriting_revenue_slope_pct_1008d_v056_signal},
    "f07_insur_underwriting_grossmargin_slope_pct_1008d_v057_signal": {"func": f07_insur_underwriting_grossmargin_slope_pct_1008d_v057_signal},
    "f07_insur_underwriting_combined_ratio_slope_pct_1008d_v058_signal": {"func": f07_insur_underwriting_combined_ratio_slope_pct_1008d_v058_signal},
    "f07_insur_underwriting_uw_profitability_slope_pct_1008d_v059_signal": {"func": f07_insur_underwriting_uw_profitability_slope_pct_1008d_v059_signal},
    "f07_insur_underwriting_loss_load_slope_pct_1008d_v060_signal": {"func": f07_insur_underwriting_loss_load_slope_pct_1008d_v060_signal},
    "f07_insur_underwriting_cor_slope_pct_1260d_v061_signal": {"func": f07_insur_underwriting_cor_slope_pct_1260d_v061_signal},
    "f07_insur_underwriting_revenue_slope_pct_1260d_v062_signal": {"func": f07_insur_underwriting_revenue_slope_pct_1260d_v062_signal},
    "f07_insur_underwriting_grossmargin_slope_pct_1260d_v063_signal": {"func": f07_insur_underwriting_grossmargin_slope_pct_1260d_v063_signal},
    "f07_insur_underwriting_combined_ratio_slope_pct_1260d_v064_signal": {"func": f07_insur_underwriting_combined_ratio_slope_pct_1260d_v064_signal},
    "f07_insur_underwriting_uw_profitability_slope_pct_1260d_v065_signal": {"func": f07_insur_underwriting_uw_profitability_slope_pct_1260d_v065_signal},
    "f07_insur_underwriting_loss_load_slope_pct_1260d_v066_signal": {"func": f07_insur_underwriting_loss_load_slope_pct_1260d_v066_signal},
    "f07_insur_underwriting_cor_jerk_5d_v067_signal": {"func": f07_insur_underwriting_cor_jerk_5d_v067_signal},
    "f07_insur_underwriting_revenue_jerk_5d_v068_signal": {"func": f07_insur_underwriting_revenue_jerk_5d_v068_signal},
    "f07_insur_underwriting_grossmargin_jerk_5d_v069_signal": {"func": f07_insur_underwriting_grossmargin_jerk_5d_v069_signal},
    "f07_insur_underwriting_combined_ratio_jerk_5d_v070_signal": {"func": f07_insur_underwriting_combined_ratio_jerk_5d_v070_signal},
    "f07_insur_underwriting_uw_profitability_jerk_5d_v071_signal": {"func": f07_insur_underwriting_uw_profitability_jerk_5d_v071_signal},
    "f07_insur_underwriting_loss_load_jerk_5d_v072_signal": {"func": f07_insur_underwriting_loss_load_jerk_5d_v072_signal},
    "f07_insur_underwriting_cor_jerk_10d_v073_signal": {"func": f07_insur_underwriting_cor_jerk_10d_v073_signal},
    "f07_insur_underwriting_revenue_jerk_10d_v074_signal": {"func": f07_insur_underwriting_revenue_jerk_10d_v074_signal},
    "f07_insur_underwriting_grossmargin_jerk_10d_v075_signal": {"func": f07_insur_underwriting_grossmargin_jerk_10d_v075_signal},
    "f07_insur_underwriting_combined_ratio_jerk_10d_v076_signal": {"func": f07_insur_underwriting_combined_ratio_jerk_10d_v076_signal},
    "f07_insur_underwriting_uw_profitability_jerk_10d_v077_signal": {"func": f07_insur_underwriting_uw_profitability_jerk_10d_v077_signal},
    "f07_insur_underwriting_loss_load_jerk_10d_v078_signal": {"func": f07_insur_underwriting_loss_load_jerk_10d_v078_signal},
    "f07_insur_underwriting_cor_jerk_21d_v079_signal": {"func": f07_insur_underwriting_cor_jerk_21d_v079_signal},
    "f07_insur_underwriting_revenue_jerk_21d_v080_signal": {"func": f07_insur_underwriting_revenue_jerk_21d_v080_signal},
    "f07_insur_underwriting_grossmargin_jerk_21d_v081_signal": {"func": f07_insur_underwriting_grossmargin_jerk_21d_v081_signal},
    "f07_insur_underwriting_combined_ratio_jerk_21d_v082_signal": {"func": f07_insur_underwriting_combined_ratio_jerk_21d_v082_signal},
    "f07_insur_underwriting_uw_profitability_jerk_21d_v083_signal": {"func": f07_insur_underwriting_uw_profitability_jerk_21d_v083_signal},
    "f07_insur_underwriting_loss_load_jerk_21d_v084_signal": {"func": f07_insur_underwriting_loss_load_jerk_21d_v084_signal},
    "f07_insur_underwriting_cor_jerk_42d_v085_signal": {"func": f07_insur_underwriting_cor_jerk_42d_v085_signal},
    "f07_insur_underwriting_revenue_jerk_42d_v086_signal": {"func": f07_insur_underwriting_revenue_jerk_42d_v086_signal},
    "f07_insur_underwriting_grossmargin_jerk_42d_v087_signal": {"func": f07_insur_underwriting_grossmargin_jerk_42d_v087_signal},
    "f07_insur_underwriting_combined_ratio_jerk_42d_v088_signal": {"func": f07_insur_underwriting_combined_ratio_jerk_42d_v088_signal},
    "f07_insur_underwriting_uw_profitability_jerk_42d_v089_signal": {"func": f07_insur_underwriting_uw_profitability_jerk_42d_v089_signal},
    "f07_insur_underwriting_loss_load_jerk_42d_v090_signal": {"func": f07_insur_underwriting_loss_load_jerk_42d_v090_signal},
    "f07_insur_underwriting_cor_jerk_63d_v091_signal": {"func": f07_insur_underwriting_cor_jerk_63d_v091_signal},
    "f07_insur_underwriting_revenue_jerk_63d_v092_signal": {"func": f07_insur_underwriting_revenue_jerk_63d_v092_signal},
    "f07_insur_underwriting_grossmargin_jerk_63d_v093_signal": {"func": f07_insur_underwriting_grossmargin_jerk_63d_v093_signal},
    "f07_insur_underwriting_combined_ratio_jerk_63d_v094_signal": {"func": f07_insur_underwriting_combined_ratio_jerk_63d_v094_signal},
    "f07_insur_underwriting_uw_profitability_jerk_63d_v095_signal": {"func": f07_insur_underwriting_uw_profitability_jerk_63d_v095_signal},
    "f07_insur_underwriting_loss_load_jerk_63d_v096_signal": {"func": f07_insur_underwriting_loss_load_jerk_63d_v096_signal},
    "f07_insur_underwriting_cor_jerk_126d_v097_signal": {"func": f07_insur_underwriting_cor_jerk_126d_v097_signal},
    "f07_insur_underwriting_revenue_jerk_126d_v098_signal": {"func": f07_insur_underwriting_revenue_jerk_126d_v098_signal},
    "f07_insur_underwriting_grossmargin_jerk_126d_v099_signal": {"func": f07_insur_underwriting_grossmargin_jerk_126d_v099_signal},
    "f07_insur_underwriting_combined_ratio_jerk_126d_v100_signal": {"func": f07_insur_underwriting_combined_ratio_jerk_126d_v100_signal},
    "f07_insur_underwriting_uw_profitability_jerk_126d_v101_signal": {"func": f07_insur_underwriting_uw_profitability_jerk_126d_v101_signal},
    "f07_insur_underwriting_loss_load_jerk_126d_v102_signal": {"func": f07_insur_underwriting_loss_load_jerk_126d_v102_signal},
    "f07_insur_underwriting_cor_jerk_252d_v103_signal": {"func": f07_insur_underwriting_cor_jerk_252d_v103_signal},
    "f07_insur_underwriting_revenue_jerk_252d_v104_signal": {"func": f07_insur_underwriting_revenue_jerk_252d_v104_signal},
    "f07_insur_underwriting_grossmargin_jerk_252d_v105_signal": {"func": f07_insur_underwriting_grossmargin_jerk_252d_v105_signal},
    "f07_insur_underwriting_combined_ratio_jerk_252d_v106_signal": {"func": f07_insur_underwriting_combined_ratio_jerk_252d_v106_signal},
    "f07_insur_underwriting_uw_profitability_jerk_252d_v107_signal": {"func": f07_insur_underwriting_uw_profitability_jerk_252d_v107_signal},
    "f07_insur_underwriting_loss_load_jerk_252d_v108_signal": {"func": f07_insur_underwriting_loss_load_jerk_252d_v108_signal},
    "f07_insur_underwriting_cor_jerk_504d_v109_signal": {"func": f07_insur_underwriting_cor_jerk_504d_v109_signal},
    "f07_insur_underwriting_revenue_jerk_504d_v110_signal": {"func": f07_insur_underwriting_revenue_jerk_504d_v110_signal},
    "f07_insur_underwriting_grossmargin_jerk_504d_v111_signal": {"func": f07_insur_underwriting_grossmargin_jerk_504d_v111_signal},
    "f07_insur_underwriting_combined_ratio_jerk_504d_v112_signal": {"func": f07_insur_underwriting_combined_ratio_jerk_504d_v112_signal},
    "f07_insur_underwriting_uw_profitability_jerk_504d_v113_signal": {"func": f07_insur_underwriting_uw_profitability_jerk_504d_v113_signal},
    "f07_insur_underwriting_loss_load_jerk_504d_v114_signal": {"func": f07_insur_underwriting_loss_load_jerk_504d_v114_signal},
    "f07_insur_underwriting_cor_jerk_756d_v115_signal": {"func": f07_insur_underwriting_cor_jerk_756d_v115_signal},
    "f07_insur_underwriting_revenue_jerk_756d_v116_signal": {"func": f07_insur_underwriting_revenue_jerk_756d_v116_signal},
    "f07_insur_underwriting_grossmargin_jerk_756d_v117_signal": {"func": f07_insur_underwriting_grossmargin_jerk_756d_v117_signal},
    "f07_insur_underwriting_combined_ratio_jerk_756d_v118_signal": {"func": f07_insur_underwriting_combined_ratio_jerk_756d_v118_signal},
    "f07_insur_underwriting_uw_profitability_jerk_756d_v119_signal": {"func": f07_insur_underwriting_uw_profitability_jerk_756d_v119_signal},
    "f07_insur_underwriting_loss_load_jerk_756d_v120_signal": {"func": f07_insur_underwriting_loss_load_jerk_756d_v120_signal},
    "f07_insur_underwriting_cor_jerk_1008d_v121_signal": {"func": f07_insur_underwriting_cor_jerk_1008d_v121_signal},
    "f07_insur_underwriting_revenue_jerk_1008d_v122_signal": {"func": f07_insur_underwriting_revenue_jerk_1008d_v122_signal},
    "f07_insur_underwriting_grossmargin_jerk_1008d_v123_signal": {"func": f07_insur_underwriting_grossmargin_jerk_1008d_v123_signal},
    "f07_insur_underwriting_combined_ratio_jerk_1008d_v124_signal": {"func": f07_insur_underwriting_combined_ratio_jerk_1008d_v124_signal},
    "f07_insur_underwriting_uw_profitability_jerk_1008d_v125_signal": {"func": f07_insur_underwriting_uw_profitability_jerk_1008d_v125_signal},
    "f07_insur_underwriting_loss_load_jerk_1008d_v126_signal": {"func": f07_insur_underwriting_loss_load_jerk_1008d_v126_signal},
    "f07_insur_underwriting_cor_jerk_1260d_v127_signal": {"func": f07_insur_underwriting_cor_jerk_1260d_v127_signal},
    "f07_insur_underwriting_revenue_jerk_1260d_v128_signal": {"func": f07_insur_underwriting_revenue_jerk_1260d_v128_signal},
    "f07_insur_underwriting_grossmargin_jerk_1260d_v129_signal": {"func": f07_insur_underwriting_grossmargin_jerk_1260d_v129_signal},
    "f07_insur_underwriting_combined_ratio_jerk_1260d_v130_signal": {"func": f07_insur_underwriting_combined_ratio_jerk_1260d_v130_signal},
    "f07_insur_underwriting_uw_profitability_jerk_1260d_v131_signal": {"func": f07_insur_underwriting_uw_profitability_jerk_1260d_v131_signal},
    "f07_insur_underwriting_loss_load_jerk_1260d_v132_signal": {"func": f07_insur_underwriting_loss_load_jerk_1260d_v132_signal},
    "f07_insur_underwriting_cor_slope_diff_norm_5d_v133_signal": {"func": f07_insur_underwriting_cor_slope_diff_norm_5d_v133_signal},
    "f07_insur_underwriting_revenue_slope_diff_norm_5d_v134_signal": {"func": f07_insur_underwriting_revenue_slope_diff_norm_5d_v134_signal},
    "f07_insur_underwriting_grossmargin_slope_diff_norm_5d_v135_signal": {"func": f07_insur_underwriting_grossmargin_slope_diff_norm_5d_v135_signal},
    "f07_insur_underwriting_combined_ratio_slope_diff_norm_5d_v136_signal": {"func": f07_insur_underwriting_combined_ratio_slope_diff_norm_5d_v136_signal},
    "f07_insur_underwriting_uw_profitability_slope_diff_norm_5d_v137_signal": {"func": f07_insur_underwriting_uw_profitability_slope_diff_norm_5d_v137_signal},
    "f07_insur_underwriting_loss_load_slope_diff_norm_5d_v138_signal": {"func": f07_insur_underwriting_loss_load_slope_diff_norm_5d_v138_signal},
    "f07_insur_underwriting_cor_slope_diff_norm_10d_v139_signal": {"func": f07_insur_underwriting_cor_slope_diff_norm_10d_v139_signal},
    "f07_insur_underwriting_revenue_slope_diff_norm_10d_v140_signal": {"func": f07_insur_underwriting_revenue_slope_diff_norm_10d_v140_signal},
    "f07_insur_underwriting_grossmargin_slope_diff_norm_10d_v141_signal": {"func": f07_insur_underwriting_grossmargin_slope_diff_norm_10d_v141_signal},
    "f07_insur_underwriting_combined_ratio_slope_diff_norm_10d_v142_signal": {"func": f07_insur_underwriting_combined_ratio_slope_diff_norm_10d_v142_signal},
    "f07_insur_underwriting_uw_profitability_slope_diff_norm_10d_v143_signal": {"func": f07_insur_underwriting_uw_profitability_slope_diff_norm_10d_v143_signal},
    "f07_insur_underwriting_loss_load_slope_diff_norm_10d_v144_signal": {"func": f07_insur_underwriting_loss_load_slope_diff_norm_10d_v144_signal},
    "f07_insur_underwriting_cor_slope_diff_norm_21d_v145_signal": {"func": f07_insur_underwriting_cor_slope_diff_norm_21d_v145_signal},
    "f07_insur_underwriting_revenue_slope_diff_norm_21d_v146_signal": {"func": f07_insur_underwriting_revenue_slope_diff_norm_21d_v146_signal},
    "f07_insur_underwriting_grossmargin_slope_diff_norm_21d_v147_signal": {"func": f07_insur_underwriting_grossmargin_slope_diff_norm_21d_v147_signal},
    "f07_insur_underwriting_combined_ratio_slope_diff_norm_21d_v148_signal": {"func": f07_insur_underwriting_combined_ratio_slope_diff_norm_21d_v148_signal},
    "f07_insur_underwriting_uw_profitability_slope_diff_norm_21d_v149_signal": {"func": f07_insur_underwriting_uw_profitability_slope_diff_norm_21d_v149_signal},
    "f07_insur_underwriting_loss_load_slope_diff_norm_21d_v150_signal": {"func": f07_insur_underwriting_loss_load_slope_diff_norm_21d_v150_signal},
}

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "deferredrev": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "equity": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "deposits": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "divyield": np.random.normal(100, 10, n).cumsum(), "bvps": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "tangibles": np.random.normal(100, 10, n).cumsum(), "grossmargin": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "revenue": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "liabilitiesc": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum()
    })
    print(f"Verifying {len(REGISTRY)} functions for family 07...")
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
