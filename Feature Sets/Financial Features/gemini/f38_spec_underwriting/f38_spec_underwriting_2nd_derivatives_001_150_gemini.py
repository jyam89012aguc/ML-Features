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

def f38_spec_underwriting_grossmargin_slope_pct_5d_v001_signal(grossmargin):
    """Percentage slope for Raw level of grossmargin over 5d window."""
    res = _slope_pct(grossmargin, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_ebitdamargin_slope_pct_5d_v002_signal(ebitdamargin):
    """Percentage slope for Raw level of ebitdamargin over 5d window."""
    res = _slope_pct(ebitdamargin, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_revenue_slope_pct_5d_v003_signal(revenue):
    """Percentage slope for Raw level of revenue over 5d window."""
    res = _slope_pct(revenue, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_uw_efficiency_slope_pct_5d_v004_signal(ebitdamargin, grossmargin):
    """Percentage slope for Underwriting profit efficiency over 5d window."""
    res = _slope_pct(_ratio(ebitdamargin, grossmargin), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_grossmargin_slope_pct_10d_v005_signal(grossmargin):
    """Percentage slope for Raw level of grossmargin over 10d window."""
    res = _slope_pct(grossmargin, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_ebitdamargin_slope_pct_10d_v006_signal(ebitdamargin):
    """Percentage slope for Raw level of ebitdamargin over 10d window."""
    res = _slope_pct(ebitdamargin, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_revenue_slope_pct_10d_v007_signal(revenue):
    """Percentage slope for Raw level of revenue over 10d window."""
    res = _slope_pct(revenue, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_uw_efficiency_slope_pct_10d_v008_signal(ebitdamargin, grossmargin):
    """Percentage slope for Underwriting profit efficiency over 10d window."""
    res = _slope_pct(_ratio(ebitdamargin, grossmargin), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_grossmargin_slope_pct_21d_v009_signal(grossmargin):
    """Percentage slope for Raw level of grossmargin over 21d window."""
    res = _slope_pct(grossmargin, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_ebitdamargin_slope_pct_21d_v010_signal(ebitdamargin):
    """Percentage slope for Raw level of ebitdamargin over 21d window."""
    res = _slope_pct(ebitdamargin, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_revenue_slope_pct_21d_v011_signal(revenue):
    """Percentage slope for Raw level of revenue over 21d window."""
    res = _slope_pct(revenue, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_uw_efficiency_slope_pct_21d_v012_signal(ebitdamargin, grossmargin):
    """Percentage slope for Underwriting profit efficiency over 21d window."""
    res = _slope_pct(_ratio(ebitdamargin, grossmargin), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_grossmargin_slope_pct_42d_v013_signal(grossmargin):
    """Percentage slope for Raw level of grossmargin over 42d window."""
    res = _slope_pct(grossmargin, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_ebitdamargin_slope_pct_42d_v014_signal(ebitdamargin):
    """Percentage slope for Raw level of ebitdamargin over 42d window."""
    res = _slope_pct(ebitdamargin, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_revenue_slope_pct_42d_v015_signal(revenue):
    """Percentage slope for Raw level of revenue over 42d window."""
    res = _slope_pct(revenue, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_uw_efficiency_slope_pct_42d_v016_signal(ebitdamargin, grossmargin):
    """Percentage slope for Underwriting profit efficiency over 42d window."""
    res = _slope_pct(_ratio(ebitdamargin, grossmargin), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_grossmargin_slope_pct_63d_v017_signal(grossmargin):
    """Percentage slope for Raw level of grossmargin over 63d window."""
    res = _slope_pct(grossmargin, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_ebitdamargin_slope_pct_63d_v018_signal(ebitdamargin):
    """Percentage slope for Raw level of ebitdamargin over 63d window."""
    res = _slope_pct(ebitdamargin, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_revenue_slope_pct_63d_v019_signal(revenue):
    """Percentage slope for Raw level of revenue over 63d window."""
    res = _slope_pct(revenue, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_uw_efficiency_slope_pct_63d_v020_signal(ebitdamargin, grossmargin):
    """Percentage slope for Underwriting profit efficiency over 63d window."""
    res = _slope_pct(_ratio(ebitdamargin, grossmargin), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_grossmargin_slope_pct_126d_v021_signal(grossmargin):
    """Percentage slope for Raw level of grossmargin over 126d window."""
    res = _slope_pct(grossmargin, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_ebitdamargin_slope_pct_126d_v022_signal(ebitdamargin):
    """Percentage slope for Raw level of ebitdamargin over 126d window."""
    res = _slope_pct(ebitdamargin, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_revenue_slope_pct_126d_v023_signal(revenue):
    """Percentage slope for Raw level of revenue over 126d window."""
    res = _slope_pct(revenue, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_uw_efficiency_slope_pct_126d_v024_signal(ebitdamargin, grossmargin):
    """Percentage slope for Underwriting profit efficiency over 126d window."""
    res = _slope_pct(_ratio(ebitdamargin, grossmargin), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_grossmargin_slope_pct_252d_v025_signal(grossmargin):
    """Percentage slope for Raw level of grossmargin over 252d window."""
    res = _slope_pct(grossmargin, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_ebitdamargin_slope_pct_252d_v026_signal(ebitdamargin):
    """Percentage slope for Raw level of ebitdamargin over 252d window."""
    res = _slope_pct(ebitdamargin, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_revenue_slope_pct_252d_v027_signal(revenue):
    """Percentage slope for Raw level of revenue over 252d window."""
    res = _slope_pct(revenue, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_uw_efficiency_slope_pct_252d_v028_signal(ebitdamargin, grossmargin):
    """Percentage slope for Underwriting profit efficiency over 252d window."""
    res = _slope_pct(_ratio(ebitdamargin, grossmargin), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_grossmargin_slope_pct_504d_v029_signal(grossmargin):
    """Percentage slope for Raw level of grossmargin over 504d window."""
    res = _slope_pct(grossmargin, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_ebitdamargin_slope_pct_504d_v030_signal(ebitdamargin):
    """Percentage slope for Raw level of ebitdamargin over 504d window."""
    res = _slope_pct(ebitdamargin, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_revenue_slope_pct_504d_v031_signal(revenue):
    """Percentage slope for Raw level of revenue over 504d window."""
    res = _slope_pct(revenue, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_uw_efficiency_slope_pct_504d_v032_signal(ebitdamargin, grossmargin):
    """Percentage slope for Underwriting profit efficiency over 504d window."""
    res = _slope_pct(_ratio(ebitdamargin, grossmargin), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_grossmargin_slope_pct_756d_v033_signal(grossmargin):
    """Percentage slope for Raw level of grossmargin over 756d window."""
    res = _slope_pct(grossmargin, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_ebitdamargin_slope_pct_756d_v034_signal(ebitdamargin):
    """Percentage slope for Raw level of ebitdamargin over 756d window."""
    res = _slope_pct(ebitdamargin, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_revenue_slope_pct_756d_v035_signal(revenue):
    """Percentage slope for Raw level of revenue over 756d window."""
    res = _slope_pct(revenue, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_uw_efficiency_slope_pct_756d_v036_signal(ebitdamargin, grossmargin):
    """Percentage slope for Underwriting profit efficiency over 756d window."""
    res = _slope_pct(_ratio(ebitdamargin, grossmargin), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_grossmargin_slope_pct_1008d_v037_signal(grossmargin):
    """Percentage slope for Raw level of grossmargin over 1008d window."""
    res = _slope_pct(grossmargin, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_ebitdamargin_slope_pct_1008d_v038_signal(ebitdamargin):
    """Percentage slope for Raw level of ebitdamargin over 1008d window."""
    res = _slope_pct(ebitdamargin, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_revenue_slope_pct_1008d_v039_signal(revenue):
    """Percentage slope for Raw level of revenue over 1008d window."""
    res = _slope_pct(revenue, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_uw_efficiency_slope_pct_1008d_v040_signal(ebitdamargin, grossmargin):
    """Percentage slope for Underwriting profit efficiency over 1008d window."""
    res = _slope_pct(_ratio(ebitdamargin, grossmargin), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_grossmargin_slope_pct_1260d_v041_signal(grossmargin):
    """Percentage slope for Raw level of grossmargin over 1260d window."""
    res = _slope_pct(grossmargin, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_ebitdamargin_slope_pct_1260d_v042_signal(ebitdamargin):
    """Percentage slope for Raw level of ebitdamargin over 1260d window."""
    res = _slope_pct(ebitdamargin, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_revenue_slope_pct_1260d_v043_signal(revenue):
    """Percentage slope for Raw level of revenue over 1260d window."""
    res = _slope_pct(revenue, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_uw_efficiency_slope_pct_1260d_v044_signal(ebitdamargin, grossmargin):
    """Percentage slope for Underwriting profit efficiency over 1260d window."""
    res = _slope_pct(_ratio(ebitdamargin, grossmargin), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_grossmargin_jerk_5d_v045_signal(grossmargin):
    """Acceleration/Jerk for Raw level of grossmargin over 5d window."""
    res = _jerk(grossmargin, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_ebitdamargin_jerk_5d_v046_signal(ebitdamargin):
    """Acceleration/Jerk for Raw level of ebitdamargin over 5d window."""
    res = _jerk(ebitdamargin, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_revenue_jerk_5d_v047_signal(revenue):
    """Acceleration/Jerk for Raw level of revenue over 5d window."""
    res = _jerk(revenue, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_uw_efficiency_jerk_5d_v048_signal(ebitdamargin, grossmargin):
    """Acceleration/Jerk for Underwriting profit efficiency over 5d window."""
    res = _jerk(_ratio(ebitdamargin, grossmargin), 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_grossmargin_jerk_10d_v049_signal(grossmargin):
    """Acceleration/Jerk for Raw level of grossmargin over 10d window."""
    res = _jerk(grossmargin, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_ebitdamargin_jerk_10d_v050_signal(ebitdamargin):
    """Acceleration/Jerk for Raw level of ebitdamargin over 10d window."""
    res = _jerk(ebitdamargin, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_revenue_jerk_10d_v051_signal(revenue):
    """Acceleration/Jerk for Raw level of revenue over 10d window."""
    res = _jerk(revenue, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_uw_efficiency_jerk_10d_v052_signal(ebitdamargin, grossmargin):
    """Acceleration/Jerk for Underwriting profit efficiency over 10d window."""
    res = _jerk(_ratio(ebitdamargin, grossmargin), 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_grossmargin_jerk_21d_v053_signal(grossmargin):
    """Acceleration/Jerk for Raw level of grossmargin over 21d window."""
    res = _jerk(grossmargin, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_ebitdamargin_jerk_21d_v054_signal(ebitdamargin):
    """Acceleration/Jerk for Raw level of ebitdamargin over 21d window."""
    res = _jerk(ebitdamargin, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_revenue_jerk_21d_v055_signal(revenue):
    """Acceleration/Jerk for Raw level of revenue over 21d window."""
    res = _jerk(revenue, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_uw_efficiency_jerk_21d_v056_signal(ebitdamargin, grossmargin):
    """Acceleration/Jerk for Underwriting profit efficiency over 21d window."""
    res = _jerk(_ratio(ebitdamargin, grossmargin), 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_grossmargin_jerk_42d_v057_signal(grossmargin):
    """Acceleration/Jerk for Raw level of grossmargin over 42d window."""
    res = _jerk(grossmargin, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_ebitdamargin_jerk_42d_v058_signal(ebitdamargin):
    """Acceleration/Jerk for Raw level of ebitdamargin over 42d window."""
    res = _jerk(ebitdamargin, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_revenue_jerk_42d_v059_signal(revenue):
    """Acceleration/Jerk for Raw level of revenue over 42d window."""
    res = _jerk(revenue, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_uw_efficiency_jerk_42d_v060_signal(ebitdamargin, grossmargin):
    """Acceleration/Jerk for Underwriting profit efficiency over 42d window."""
    res = _jerk(_ratio(ebitdamargin, grossmargin), 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_grossmargin_jerk_63d_v061_signal(grossmargin):
    """Acceleration/Jerk for Raw level of grossmargin over 63d window."""
    res = _jerk(grossmargin, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_ebitdamargin_jerk_63d_v062_signal(ebitdamargin):
    """Acceleration/Jerk for Raw level of ebitdamargin over 63d window."""
    res = _jerk(ebitdamargin, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_revenue_jerk_63d_v063_signal(revenue):
    """Acceleration/Jerk for Raw level of revenue over 63d window."""
    res = _jerk(revenue, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_uw_efficiency_jerk_63d_v064_signal(ebitdamargin, grossmargin):
    """Acceleration/Jerk for Underwriting profit efficiency over 63d window."""
    res = _jerk(_ratio(ebitdamargin, grossmargin), 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_grossmargin_jerk_126d_v065_signal(grossmargin):
    """Acceleration/Jerk for Raw level of grossmargin over 126d window."""
    res = _jerk(grossmargin, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_ebitdamargin_jerk_126d_v066_signal(ebitdamargin):
    """Acceleration/Jerk for Raw level of ebitdamargin over 126d window."""
    res = _jerk(ebitdamargin, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_revenue_jerk_126d_v067_signal(revenue):
    """Acceleration/Jerk for Raw level of revenue over 126d window."""
    res = _jerk(revenue, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_uw_efficiency_jerk_126d_v068_signal(ebitdamargin, grossmargin):
    """Acceleration/Jerk for Underwriting profit efficiency over 126d window."""
    res = _jerk(_ratio(ebitdamargin, grossmargin), 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_grossmargin_jerk_252d_v069_signal(grossmargin):
    """Acceleration/Jerk for Raw level of grossmargin over 252d window."""
    res = _jerk(grossmargin, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_ebitdamargin_jerk_252d_v070_signal(ebitdamargin):
    """Acceleration/Jerk for Raw level of ebitdamargin over 252d window."""
    res = _jerk(ebitdamargin, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_revenue_jerk_252d_v071_signal(revenue):
    """Acceleration/Jerk for Raw level of revenue over 252d window."""
    res = _jerk(revenue, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_uw_efficiency_jerk_252d_v072_signal(ebitdamargin, grossmargin):
    """Acceleration/Jerk for Underwriting profit efficiency over 252d window."""
    res = _jerk(_ratio(ebitdamargin, grossmargin), 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_grossmargin_jerk_504d_v073_signal(grossmargin):
    """Acceleration/Jerk for Raw level of grossmargin over 504d window."""
    res = _jerk(grossmargin, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_ebitdamargin_jerk_504d_v074_signal(ebitdamargin):
    """Acceleration/Jerk for Raw level of ebitdamargin over 504d window."""
    res = _jerk(ebitdamargin, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_revenue_jerk_504d_v075_signal(revenue):
    """Acceleration/Jerk for Raw level of revenue over 504d window."""
    res = _jerk(revenue, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_uw_efficiency_jerk_504d_v076_signal(ebitdamargin, grossmargin):
    """Acceleration/Jerk for Underwriting profit efficiency over 504d window."""
    res = _jerk(_ratio(ebitdamargin, grossmargin), 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_grossmargin_jerk_756d_v077_signal(grossmargin):
    """Acceleration/Jerk for Raw level of grossmargin over 756d window."""
    res = _jerk(grossmargin, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_ebitdamargin_jerk_756d_v078_signal(ebitdamargin):
    """Acceleration/Jerk for Raw level of ebitdamargin over 756d window."""
    res = _jerk(ebitdamargin, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_revenue_jerk_756d_v079_signal(revenue):
    """Acceleration/Jerk for Raw level of revenue over 756d window."""
    res = _jerk(revenue, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_uw_efficiency_jerk_756d_v080_signal(ebitdamargin, grossmargin):
    """Acceleration/Jerk for Underwriting profit efficiency over 756d window."""
    res = _jerk(_ratio(ebitdamargin, grossmargin), 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_grossmargin_jerk_1008d_v081_signal(grossmargin):
    """Acceleration/Jerk for Raw level of grossmargin over 1008d window."""
    res = _jerk(grossmargin, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_ebitdamargin_jerk_1008d_v082_signal(ebitdamargin):
    """Acceleration/Jerk for Raw level of ebitdamargin over 1008d window."""
    res = _jerk(ebitdamargin, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_revenue_jerk_1008d_v083_signal(revenue):
    """Acceleration/Jerk for Raw level of revenue over 1008d window."""
    res = _jerk(revenue, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_uw_efficiency_jerk_1008d_v084_signal(ebitdamargin, grossmargin):
    """Acceleration/Jerk for Underwriting profit efficiency over 1008d window."""
    res = _jerk(_ratio(ebitdamargin, grossmargin), 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_grossmargin_jerk_1260d_v085_signal(grossmargin):
    """Acceleration/Jerk for Raw level of grossmargin over 1260d window."""
    res = _jerk(grossmargin, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_ebitdamargin_jerk_1260d_v086_signal(ebitdamargin):
    """Acceleration/Jerk for Raw level of ebitdamargin over 1260d window."""
    res = _jerk(ebitdamargin, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_revenue_jerk_1260d_v087_signal(revenue):
    """Acceleration/Jerk for Raw level of revenue over 1260d window."""
    res = _jerk(revenue, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_uw_efficiency_jerk_1260d_v088_signal(ebitdamargin, grossmargin):
    """Acceleration/Jerk for Underwriting profit efficiency over 1260d window."""
    res = _jerk(_ratio(ebitdamargin, grossmargin), 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_grossmargin_slope_diff_norm_5d_v089_signal(grossmargin):
    """Normalized slope change for Raw level of grossmargin over 5d window."""
    res = (_slope_pct(grossmargin, 5).diff(5) / _sma(grossmargin.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_ebitdamargin_slope_diff_norm_5d_v090_signal(ebitdamargin):
    """Normalized slope change for Raw level of ebitdamargin over 5d window."""
    res = (_slope_pct(ebitdamargin, 5).diff(5) / _sma(ebitdamargin.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_revenue_slope_diff_norm_5d_v091_signal(revenue):
    """Normalized slope change for Raw level of revenue over 5d window."""
    res = (_slope_pct(revenue, 5).diff(5) / _sma(revenue.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_uw_efficiency_slope_diff_norm_5d_v092_signal(ebitdamargin, grossmargin):
    """Normalized slope change for Underwriting profit efficiency over 5d window."""
    res = (_slope_pct(_ratio(ebitdamargin, grossmargin), 5).diff(5) / _sma(_ratio(ebitdamargin, grossmargin).abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_grossmargin_slope_diff_norm_10d_v093_signal(grossmargin):
    """Normalized slope change for Raw level of grossmargin over 10d window."""
    res = (_slope_pct(grossmargin, 10).diff(10) / _sma(grossmargin.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_ebitdamargin_slope_diff_norm_10d_v094_signal(ebitdamargin):
    """Normalized slope change for Raw level of ebitdamargin over 10d window."""
    res = (_slope_pct(ebitdamargin, 10).diff(10) / _sma(ebitdamargin.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_revenue_slope_diff_norm_10d_v095_signal(revenue):
    """Normalized slope change for Raw level of revenue over 10d window."""
    res = (_slope_pct(revenue, 10).diff(10) / _sma(revenue.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_uw_efficiency_slope_diff_norm_10d_v096_signal(ebitdamargin, grossmargin):
    """Normalized slope change for Underwriting profit efficiency over 10d window."""
    res = (_slope_pct(_ratio(ebitdamargin, grossmargin), 10).diff(10) / _sma(_ratio(ebitdamargin, grossmargin).abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_grossmargin_slope_diff_norm_21d_v097_signal(grossmargin):
    """Normalized slope change for Raw level of grossmargin over 21d window."""
    res = (_slope_pct(grossmargin, 21).diff(21) / _sma(grossmargin.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_ebitdamargin_slope_diff_norm_21d_v098_signal(ebitdamargin):
    """Normalized slope change for Raw level of ebitdamargin over 21d window."""
    res = (_slope_pct(ebitdamargin, 21).diff(21) / _sma(ebitdamargin.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_revenue_slope_diff_norm_21d_v099_signal(revenue):
    """Normalized slope change for Raw level of revenue over 21d window."""
    res = (_slope_pct(revenue, 21).diff(21) / _sma(revenue.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_uw_efficiency_slope_diff_norm_21d_v100_signal(ebitdamargin, grossmargin):
    """Normalized slope change for Underwriting profit efficiency over 21d window."""
    res = (_slope_pct(_ratio(ebitdamargin, grossmargin), 21).diff(21) / _sma(_ratio(ebitdamargin, grossmargin).abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_grossmargin_slope_diff_norm_42d_v101_signal(grossmargin):
    """Normalized slope change for Raw level of grossmargin over 42d window."""
    res = (_slope_pct(grossmargin, 42).diff(42) / _sma(grossmargin.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_ebitdamargin_slope_diff_norm_42d_v102_signal(ebitdamargin):
    """Normalized slope change for Raw level of ebitdamargin over 42d window."""
    res = (_slope_pct(ebitdamargin, 42).diff(42) / _sma(ebitdamargin.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_revenue_slope_diff_norm_42d_v103_signal(revenue):
    """Normalized slope change for Raw level of revenue over 42d window."""
    res = (_slope_pct(revenue, 42).diff(42) / _sma(revenue.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_uw_efficiency_slope_diff_norm_42d_v104_signal(ebitdamargin, grossmargin):
    """Normalized slope change for Underwriting profit efficiency over 42d window."""
    res = (_slope_pct(_ratio(ebitdamargin, grossmargin), 42).diff(42) / _sma(_ratio(ebitdamargin, grossmargin).abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_grossmargin_slope_diff_norm_63d_v105_signal(grossmargin):
    """Normalized slope change for Raw level of grossmargin over 63d window."""
    res = (_slope_pct(grossmargin, 63).diff(63) / _sma(grossmargin.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_ebitdamargin_slope_diff_norm_63d_v106_signal(ebitdamargin):
    """Normalized slope change for Raw level of ebitdamargin over 63d window."""
    res = (_slope_pct(ebitdamargin, 63).diff(63) / _sma(ebitdamargin.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_revenue_slope_diff_norm_63d_v107_signal(revenue):
    """Normalized slope change for Raw level of revenue over 63d window."""
    res = (_slope_pct(revenue, 63).diff(63) / _sma(revenue.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_uw_efficiency_slope_diff_norm_63d_v108_signal(ebitdamargin, grossmargin):
    """Normalized slope change for Underwriting profit efficiency over 63d window."""
    res = (_slope_pct(_ratio(ebitdamargin, grossmargin), 63).diff(63) / _sma(_ratio(ebitdamargin, grossmargin).abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_grossmargin_slope_diff_norm_126d_v109_signal(grossmargin):
    """Normalized slope change for Raw level of grossmargin over 126d window."""
    res = (_slope_pct(grossmargin, 126).diff(126) / _sma(grossmargin.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_ebitdamargin_slope_diff_norm_126d_v110_signal(ebitdamargin):
    """Normalized slope change for Raw level of ebitdamargin over 126d window."""
    res = (_slope_pct(ebitdamargin, 126).diff(126) / _sma(ebitdamargin.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_revenue_slope_diff_norm_126d_v111_signal(revenue):
    """Normalized slope change for Raw level of revenue over 126d window."""
    res = (_slope_pct(revenue, 126).diff(126) / _sma(revenue.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_uw_efficiency_slope_diff_norm_126d_v112_signal(ebitdamargin, grossmargin):
    """Normalized slope change for Underwriting profit efficiency over 126d window."""
    res = (_slope_pct(_ratio(ebitdamargin, grossmargin), 126).diff(126) / _sma(_ratio(ebitdamargin, grossmargin).abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_grossmargin_slope_diff_norm_252d_v113_signal(grossmargin):
    """Normalized slope change for Raw level of grossmargin over 252d window."""
    res = (_slope_pct(grossmargin, 252).diff(252) / _sma(grossmargin.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_ebitdamargin_slope_diff_norm_252d_v114_signal(ebitdamargin):
    """Normalized slope change for Raw level of ebitdamargin over 252d window."""
    res = (_slope_pct(ebitdamargin, 252).diff(252) / _sma(ebitdamargin.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_revenue_slope_diff_norm_252d_v115_signal(revenue):
    """Normalized slope change for Raw level of revenue over 252d window."""
    res = (_slope_pct(revenue, 252).diff(252) / _sma(revenue.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_uw_efficiency_slope_diff_norm_252d_v116_signal(ebitdamargin, grossmargin):
    """Normalized slope change for Underwriting profit efficiency over 252d window."""
    res = (_slope_pct(_ratio(ebitdamargin, grossmargin), 252).diff(252) / _sma(_ratio(ebitdamargin, grossmargin).abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_grossmargin_slope_diff_norm_504d_v117_signal(grossmargin):
    """Normalized slope change for Raw level of grossmargin over 504d window."""
    res = (_slope_pct(grossmargin, 504).diff(504) / _sma(grossmargin.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_ebitdamargin_slope_diff_norm_504d_v118_signal(ebitdamargin):
    """Normalized slope change for Raw level of ebitdamargin over 504d window."""
    res = (_slope_pct(ebitdamargin, 504).diff(504) / _sma(ebitdamargin.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_revenue_slope_diff_norm_504d_v119_signal(revenue):
    """Normalized slope change for Raw level of revenue over 504d window."""
    res = (_slope_pct(revenue, 504).diff(504) / _sma(revenue.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_uw_efficiency_slope_diff_norm_504d_v120_signal(ebitdamargin, grossmargin):
    """Normalized slope change for Underwriting profit efficiency over 504d window."""
    res = (_slope_pct(_ratio(ebitdamargin, grossmargin), 504).diff(504) / _sma(_ratio(ebitdamargin, grossmargin).abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_grossmargin_slope_diff_norm_756d_v121_signal(grossmargin):
    """Normalized slope change for Raw level of grossmargin over 756d window."""
    res = (_slope_pct(grossmargin, 756).diff(756) / _sma(grossmargin.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_ebitdamargin_slope_diff_norm_756d_v122_signal(ebitdamargin):
    """Normalized slope change for Raw level of ebitdamargin over 756d window."""
    res = (_slope_pct(ebitdamargin, 756).diff(756) / _sma(ebitdamargin.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_revenue_slope_diff_norm_756d_v123_signal(revenue):
    """Normalized slope change for Raw level of revenue over 756d window."""
    res = (_slope_pct(revenue, 756).diff(756) / _sma(revenue.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_uw_efficiency_slope_diff_norm_756d_v124_signal(ebitdamargin, grossmargin):
    """Normalized slope change for Underwriting profit efficiency over 756d window."""
    res = (_slope_pct(_ratio(ebitdamargin, grossmargin), 756).diff(756) / _sma(_ratio(ebitdamargin, grossmargin).abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_grossmargin_slope_diff_norm_1008d_v125_signal(grossmargin):
    """Normalized slope change for Raw level of grossmargin over 1008d window."""
    res = (_slope_pct(grossmargin, 1008).diff(1008) / _sma(grossmargin.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_ebitdamargin_slope_diff_norm_1008d_v126_signal(ebitdamargin):
    """Normalized slope change for Raw level of ebitdamargin over 1008d window."""
    res = (_slope_pct(ebitdamargin, 1008).diff(1008) / _sma(ebitdamargin.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_revenue_slope_diff_norm_1008d_v127_signal(revenue):
    """Normalized slope change for Raw level of revenue over 1008d window."""
    res = (_slope_pct(revenue, 1008).diff(1008) / _sma(revenue.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_uw_efficiency_slope_diff_norm_1008d_v128_signal(ebitdamargin, grossmargin):
    """Normalized slope change for Underwriting profit efficiency over 1008d window."""
    res = (_slope_pct(_ratio(ebitdamargin, grossmargin), 1008).diff(1008) / _sma(_ratio(ebitdamargin, grossmargin).abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_grossmargin_slope_diff_norm_1260d_v129_signal(grossmargin):
    """Normalized slope change for Raw level of grossmargin over 1260d window."""
    res = (_slope_pct(grossmargin, 1260).diff(1260) / _sma(grossmargin.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_ebitdamargin_slope_diff_norm_1260d_v130_signal(ebitdamargin):
    """Normalized slope change for Raw level of ebitdamargin over 1260d window."""
    res = (_slope_pct(ebitdamargin, 1260).diff(1260) / _sma(ebitdamargin.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_revenue_slope_diff_norm_1260d_v131_signal(revenue):
    """Normalized slope change for Raw level of revenue over 1260d window."""
    res = (_slope_pct(revenue, 1260).diff(1260) / _sma(revenue.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_uw_efficiency_slope_diff_norm_1260d_v132_signal(ebitdamargin, grossmargin):
    """Normalized slope change for Underwriting profit efficiency over 1260d window."""
    res = (_slope_pct(_ratio(ebitdamargin, grossmargin), 1260).diff(1260) / _sma(_ratio(ebitdamargin, grossmargin).abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_grossmargin_mom_z_5d_v133_signal(grossmargin):
    """Relative momentum strength for Raw level of grossmargin over 5d window."""
    res = _z(_slope_pct(grossmargin, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_ebitdamargin_mom_z_5d_v134_signal(ebitdamargin):
    """Relative momentum strength for Raw level of ebitdamargin over 5d window."""
    res = _z(_slope_pct(ebitdamargin, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_revenue_mom_z_5d_v135_signal(revenue):
    """Relative momentum strength for Raw level of revenue over 5d window."""
    res = _z(_slope_pct(revenue, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_uw_efficiency_mom_z_5d_v136_signal(ebitdamargin, grossmargin):
    """Relative momentum strength for Underwriting profit efficiency over 5d window."""
    res = _z(_slope_pct(_ratio(ebitdamargin, grossmargin), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_grossmargin_mom_z_10d_v137_signal(grossmargin):
    """Relative momentum strength for Raw level of grossmargin over 10d window."""
    res = _z(_slope_pct(grossmargin, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_ebitdamargin_mom_z_10d_v138_signal(ebitdamargin):
    """Relative momentum strength for Raw level of ebitdamargin over 10d window."""
    res = _z(_slope_pct(ebitdamargin, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_revenue_mom_z_10d_v139_signal(revenue):
    """Relative momentum strength for Raw level of revenue over 10d window."""
    res = _z(_slope_pct(revenue, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_uw_efficiency_mom_z_10d_v140_signal(ebitdamargin, grossmargin):
    """Relative momentum strength for Underwriting profit efficiency over 10d window."""
    res = _z(_slope_pct(_ratio(ebitdamargin, grossmargin), 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_grossmargin_mom_z_21d_v141_signal(grossmargin):
    """Relative momentum strength for Raw level of grossmargin over 21d window."""
    res = _z(_slope_pct(grossmargin, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_ebitdamargin_mom_z_21d_v142_signal(ebitdamargin):
    """Relative momentum strength for Raw level of ebitdamargin over 21d window."""
    res = _z(_slope_pct(ebitdamargin, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_revenue_mom_z_21d_v143_signal(revenue):
    """Relative momentum strength for Raw level of revenue over 21d window."""
    res = _z(_slope_pct(revenue, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_uw_efficiency_mom_z_21d_v144_signal(ebitdamargin, grossmargin):
    """Relative momentum strength for Underwriting profit efficiency over 21d window."""
    res = _z(_slope_pct(_ratio(ebitdamargin, grossmargin), 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_grossmargin_mom_z_42d_v145_signal(grossmargin):
    """Relative momentum strength for Raw level of grossmargin over 42d window."""
    res = _z(_slope_pct(grossmargin, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_ebitdamargin_mom_z_42d_v146_signal(ebitdamargin):
    """Relative momentum strength for Raw level of ebitdamargin over 42d window."""
    res = _z(_slope_pct(ebitdamargin, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_revenue_mom_z_42d_v147_signal(revenue):
    """Relative momentum strength for Raw level of revenue over 42d window."""
    res = _z(_slope_pct(revenue, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_uw_efficiency_mom_z_42d_v148_signal(ebitdamargin, grossmargin):
    """Relative momentum strength for Underwriting profit efficiency over 42d window."""
    res = _z(_slope_pct(_ratio(ebitdamargin, grossmargin), 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_grossmargin_mom_z_63d_v149_signal(grossmargin):
    """Relative momentum strength for Raw level of grossmargin over 63d window."""
    res = _z(_slope_pct(grossmargin, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_ebitdamargin_mom_z_63d_v150_signal(ebitdamargin):
    """Relative momentum strength for Raw level of ebitdamargin over 63d window."""
    res = _z(_slope_pct(ebitdamargin, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)


# ===== Feature Registry =====
REGISTRY = {
    "f38_spec_underwriting_grossmargin_slope_pct_5d_v001_signal": {"func": f38_spec_underwriting_grossmargin_slope_pct_5d_v001_signal},
    "f38_spec_underwriting_ebitdamargin_slope_pct_5d_v002_signal": {"func": f38_spec_underwriting_ebitdamargin_slope_pct_5d_v002_signal},
    "f38_spec_underwriting_revenue_slope_pct_5d_v003_signal": {"func": f38_spec_underwriting_revenue_slope_pct_5d_v003_signal},
    "f38_spec_underwriting_uw_efficiency_slope_pct_5d_v004_signal": {"func": f38_spec_underwriting_uw_efficiency_slope_pct_5d_v004_signal},
    "f38_spec_underwriting_grossmargin_slope_pct_10d_v005_signal": {"func": f38_spec_underwriting_grossmargin_slope_pct_10d_v005_signal},
    "f38_spec_underwriting_ebitdamargin_slope_pct_10d_v006_signal": {"func": f38_spec_underwriting_ebitdamargin_slope_pct_10d_v006_signal},
    "f38_spec_underwriting_revenue_slope_pct_10d_v007_signal": {"func": f38_spec_underwriting_revenue_slope_pct_10d_v007_signal},
    "f38_spec_underwriting_uw_efficiency_slope_pct_10d_v008_signal": {"func": f38_spec_underwriting_uw_efficiency_slope_pct_10d_v008_signal},
    "f38_spec_underwriting_grossmargin_slope_pct_21d_v009_signal": {"func": f38_spec_underwriting_grossmargin_slope_pct_21d_v009_signal},
    "f38_spec_underwriting_ebitdamargin_slope_pct_21d_v010_signal": {"func": f38_spec_underwriting_ebitdamargin_slope_pct_21d_v010_signal},
    "f38_spec_underwriting_revenue_slope_pct_21d_v011_signal": {"func": f38_spec_underwriting_revenue_slope_pct_21d_v011_signal},
    "f38_spec_underwriting_uw_efficiency_slope_pct_21d_v012_signal": {"func": f38_spec_underwriting_uw_efficiency_slope_pct_21d_v012_signal},
    "f38_spec_underwriting_grossmargin_slope_pct_42d_v013_signal": {"func": f38_spec_underwriting_grossmargin_slope_pct_42d_v013_signal},
    "f38_spec_underwriting_ebitdamargin_slope_pct_42d_v014_signal": {"func": f38_spec_underwriting_ebitdamargin_slope_pct_42d_v014_signal},
    "f38_spec_underwriting_revenue_slope_pct_42d_v015_signal": {"func": f38_spec_underwriting_revenue_slope_pct_42d_v015_signal},
    "f38_spec_underwriting_uw_efficiency_slope_pct_42d_v016_signal": {"func": f38_spec_underwriting_uw_efficiency_slope_pct_42d_v016_signal},
    "f38_spec_underwriting_grossmargin_slope_pct_63d_v017_signal": {"func": f38_spec_underwriting_grossmargin_slope_pct_63d_v017_signal},
    "f38_spec_underwriting_ebitdamargin_slope_pct_63d_v018_signal": {"func": f38_spec_underwriting_ebitdamargin_slope_pct_63d_v018_signal},
    "f38_spec_underwriting_revenue_slope_pct_63d_v019_signal": {"func": f38_spec_underwriting_revenue_slope_pct_63d_v019_signal},
    "f38_spec_underwriting_uw_efficiency_slope_pct_63d_v020_signal": {"func": f38_spec_underwriting_uw_efficiency_slope_pct_63d_v020_signal},
    "f38_spec_underwriting_grossmargin_slope_pct_126d_v021_signal": {"func": f38_spec_underwriting_grossmargin_slope_pct_126d_v021_signal},
    "f38_spec_underwriting_ebitdamargin_slope_pct_126d_v022_signal": {"func": f38_spec_underwriting_ebitdamargin_slope_pct_126d_v022_signal},
    "f38_spec_underwriting_revenue_slope_pct_126d_v023_signal": {"func": f38_spec_underwriting_revenue_slope_pct_126d_v023_signal},
    "f38_spec_underwriting_uw_efficiency_slope_pct_126d_v024_signal": {"func": f38_spec_underwriting_uw_efficiency_slope_pct_126d_v024_signal},
    "f38_spec_underwriting_grossmargin_slope_pct_252d_v025_signal": {"func": f38_spec_underwriting_grossmargin_slope_pct_252d_v025_signal},
    "f38_spec_underwriting_ebitdamargin_slope_pct_252d_v026_signal": {"func": f38_spec_underwriting_ebitdamargin_slope_pct_252d_v026_signal},
    "f38_spec_underwriting_revenue_slope_pct_252d_v027_signal": {"func": f38_spec_underwriting_revenue_slope_pct_252d_v027_signal},
    "f38_spec_underwriting_uw_efficiency_slope_pct_252d_v028_signal": {"func": f38_spec_underwriting_uw_efficiency_slope_pct_252d_v028_signal},
    "f38_spec_underwriting_grossmargin_slope_pct_504d_v029_signal": {"func": f38_spec_underwriting_grossmargin_slope_pct_504d_v029_signal},
    "f38_spec_underwriting_ebitdamargin_slope_pct_504d_v030_signal": {"func": f38_spec_underwriting_ebitdamargin_slope_pct_504d_v030_signal},
    "f38_spec_underwriting_revenue_slope_pct_504d_v031_signal": {"func": f38_spec_underwriting_revenue_slope_pct_504d_v031_signal},
    "f38_spec_underwriting_uw_efficiency_slope_pct_504d_v032_signal": {"func": f38_spec_underwriting_uw_efficiency_slope_pct_504d_v032_signal},
    "f38_spec_underwriting_grossmargin_slope_pct_756d_v033_signal": {"func": f38_spec_underwriting_grossmargin_slope_pct_756d_v033_signal},
    "f38_spec_underwriting_ebitdamargin_slope_pct_756d_v034_signal": {"func": f38_spec_underwriting_ebitdamargin_slope_pct_756d_v034_signal},
    "f38_spec_underwriting_revenue_slope_pct_756d_v035_signal": {"func": f38_spec_underwriting_revenue_slope_pct_756d_v035_signal},
    "f38_spec_underwriting_uw_efficiency_slope_pct_756d_v036_signal": {"func": f38_spec_underwriting_uw_efficiency_slope_pct_756d_v036_signal},
    "f38_spec_underwriting_grossmargin_slope_pct_1008d_v037_signal": {"func": f38_spec_underwriting_grossmargin_slope_pct_1008d_v037_signal},
    "f38_spec_underwriting_ebitdamargin_slope_pct_1008d_v038_signal": {"func": f38_spec_underwriting_ebitdamargin_slope_pct_1008d_v038_signal},
    "f38_spec_underwriting_revenue_slope_pct_1008d_v039_signal": {"func": f38_spec_underwriting_revenue_slope_pct_1008d_v039_signal},
    "f38_spec_underwriting_uw_efficiency_slope_pct_1008d_v040_signal": {"func": f38_spec_underwriting_uw_efficiency_slope_pct_1008d_v040_signal},
    "f38_spec_underwriting_grossmargin_slope_pct_1260d_v041_signal": {"func": f38_spec_underwriting_grossmargin_slope_pct_1260d_v041_signal},
    "f38_spec_underwriting_ebitdamargin_slope_pct_1260d_v042_signal": {"func": f38_spec_underwriting_ebitdamargin_slope_pct_1260d_v042_signal},
    "f38_spec_underwriting_revenue_slope_pct_1260d_v043_signal": {"func": f38_spec_underwriting_revenue_slope_pct_1260d_v043_signal},
    "f38_spec_underwriting_uw_efficiency_slope_pct_1260d_v044_signal": {"func": f38_spec_underwriting_uw_efficiency_slope_pct_1260d_v044_signal},
    "f38_spec_underwriting_grossmargin_jerk_5d_v045_signal": {"func": f38_spec_underwriting_grossmargin_jerk_5d_v045_signal},
    "f38_spec_underwriting_ebitdamargin_jerk_5d_v046_signal": {"func": f38_spec_underwriting_ebitdamargin_jerk_5d_v046_signal},
    "f38_spec_underwriting_revenue_jerk_5d_v047_signal": {"func": f38_spec_underwriting_revenue_jerk_5d_v047_signal},
    "f38_spec_underwriting_uw_efficiency_jerk_5d_v048_signal": {"func": f38_spec_underwriting_uw_efficiency_jerk_5d_v048_signal},
    "f38_spec_underwriting_grossmargin_jerk_10d_v049_signal": {"func": f38_spec_underwriting_grossmargin_jerk_10d_v049_signal},
    "f38_spec_underwriting_ebitdamargin_jerk_10d_v050_signal": {"func": f38_spec_underwriting_ebitdamargin_jerk_10d_v050_signal},
    "f38_spec_underwriting_revenue_jerk_10d_v051_signal": {"func": f38_spec_underwriting_revenue_jerk_10d_v051_signal},
    "f38_spec_underwriting_uw_efficiency_jerk_10d_v052_signal": {"func": f38_spec_underwriting_uw_efficiency_jerk_10d_v052_signal},
    "f38_spec_underwriting_grossmargin_jerk_21d_v053_signal": {"func": f38_spec_underwriting_grossmargin_jerk_21d_v053_signal},
    "f38_spec_underwriting_ebitdamargin_jerk_21d_v054_signal": {"func": f38_spec_underwriting_ebitdamargin_jerk_21d_v054_signal},
    "f38_spec_underwriting_revenue_jerk_21d_v055_signal": {"func": f38_spec_underwriting_revenue_jerk_21d_v055_signal},
    "f38_spec_underwriting_uw_efficiency_jerk_21d_v056_signal": {"func": f38_spec_underwriting_uw_efficiency_jerk_21d_v056_signal},
    "f38_spec_underwriting_grossmargin_jerk_42d_v057_signal": {"func": f38_spec_underwriting_grossmargin_jerk_42d_v057_signal},
    "f38_spec_underwriting_ebitdamargin_jerk_42d_v058_signal": {"func": f38_spec_underwriting_ebitdamargin_jerk_42d_v058_signal},
    "f38_spec_underwriting_revenue_jerk_42d_v059_signal": {"func": f38_spec_underwriting_revenue_jerk_42d_v059_signal},
    "f38_spec_underwriting_uw_efficiency_jerk_42d_v060_signal": {"func": f38_spec_underwriting_uw_efficiency_jerk_42d_v060_signal},
    "f38_spec_underwriting_grossmargin_jerk_63d_v061_signal": {"func": f38_spec_underwriting_grossmargin_jerk_63d_v061_signal},
    "f38_spec_underwriting_ebitdamargin_jerk_63d_v062_signal": {"func": f38_spec_underwriting_ebitdamargin_jerk_63d_v062_signal},
    "f38_spec_underwriting_revenue_jerk_63d_v063_signal": {"func": f38_spec_underwriting_revenue_jerk_63d_v063_signal},
    "f38_spec_underwriting_uw_efficiency_jerk_63d_v064_signal": {"func": f38_spec_underwriting_uw_efficiency_jerk_63d_v064_signal},
    "f38_spec_underwriting_grossmargin_jerk_126d_v065_signal": {"func": f38_spec_underwriting_grossmargin_jerk_126d_v065_signal},
    "f38_spec_underwriting_ebitdamargin_jerk_126d_v066_signal": {"func": f38_spec_underwriting_ebitdamargin_jerk_126d_v066_signal},
    "f38_spec_underwriting_revenue_jerk_126d_v067_signal": {"func": f38_spec_underwriting_revenue_jerk_126d_v067_signal},
    "f38_spec_underwriting_uw_efficiency_jerk_126d_v068_signal": {"func": f38_spec_underwriting_uw_efficiency_jerk_126d_v068_signal},
    "f38_spec_underwriting_grossmargin_jerk_252d_v069_signal": {"func": f38_spec_underwriting_grossmargin_jerk_252d_v069_signal},
    "f38_spec_underwriting_ebitdamargin_jerk_252d_v070_signal": {"func": f38_spec_underwriting_ebitdamargin_jerk_252d_v070_signal},
    "f38_spec_underwriting_revenue_jerk_252d_v071_signal": {"func": f38_spec_underwriting_revenue_jerk_252d_v071_signal},
    "f38_spec_underwriting_uw_efficiency_jerk_252d_v072_signal": {"func": f38_spec_underwriting_uw_efficiency_jerk_252d_v072_signal},
    "f38_spec_underwriting_grossmargin_jerk_504d_v073_signal": {"func": f38_spec_underwriting_grossmargin_jerk_504d_v073_signal},
    "f38_spec_underwriting_ebitdamargin_jerk_504d_v074_signal": {"func": f38_spec_underwriting_ebitdamargin_jerk_504d_v074_signal},
    "f38_spec_underwriting_revenue_jerk_504d_v075_signal": {"func": f38_spec_underwriting_revenue_jerk_504d_v075_signal},
    "f38_spec_underwriting_uw_efficiency_jerk_504d_v076_signal": {"func": f38_spec_underwriting_uw_efficiency_jerk_504d_v076_signal},
    "f38_spec_underwriting_grossmargin_jerk_756d_v077_signal": {"func": f38_spec_underwriting_grossmargin_jerk_756d_v077_signal},
    "f38_spec_underwriting_ebitdamargin_jerk_756d_v078_signal": {"func": f38_spec_underwriting_ebitdamargin_jerk_756d_v078_signal},
    "f38_spec_underwriting_revenue_jerk_756d_v079_signal": {"func": f38_spec_underwriting_revenue_jerk_756d_v079_signal},
    "f38_spec_underwriting_uw_efficiency_jerk_756d_v080_signal": {"func": f38_spec_underwriting_uw_efficiency_jerk_756d_v080_signal},
    "f38_spec_underwriting_grossmargin_jerk_1008d_v081_signal": {"func": f38_spec_underwriting_grossmargin_jerk_1008d_v081_signal},
    "f38_spec_underwriting_ebitdamargin_jerk_1008d_v082_signal": {"func": f38_spec_underwriting_ebitdamargin_jerk_1008d_v082_signal},
    "f38_spec_underwriting_revenue_jerk_1008d_v083_signal": {"func": f38_spec_underwriting_revenue_jerk_1008d_v083_signal},
    "f38_spec_underwriting_uw_efficiency_jerk_1008d_v084_signal": {"func": f38_spec_underwriting_uw_efficiency_jerk_1008d_v084_signal},
    "f38_spec_underwriting_grossmargin_jerk_1260d_v085_signal": {"func": f38_spec_underwriting_grossmargin_jerk_1260d_v085_signal},
    "f38_spec_underwriting_ebitdamargin_jerk_1260d_v086_signal": {"func": f38_spec_underwriting_ebitdamargin_jerk_1260d_v086_signal},
    "f38_spec_underwriting_revenue_jerk_1260d_v087_signal": {"func": f38_spec_underwriting_revenue_jerk_1260d_v087_signal},
    "f38_spec_underwriting_uw_efficiency_jerk_1260d_v088_signal": {"func": f38_spec_underwriting_uw_efficiency_jerk_1260d_v088_signal},
    "f38_spec_underwriting_grossmargin_slope_diff_norm_5d_v089_signal": {"func": f38_spec_underwriting_grossmargin_slope_diff_norm_5d_v089_signal},
    "f38_spec_underwriting_ebitdamargin_slope_diff_norm_5d_v090_signal": {"func": f38_spec_underwriting_ebitdamargin_slope_diff_norm_5d_v090_signal},
    "f38_spec_underwriting_revenue_slope_diff_norm_5d_v091_signal": {"func": f38_spec_underwriting_revenue_slope_diff_norm_5d_v091_signal},
    "f38_spec_underwriting_uw_efficiency_slope_diff_norm_5d_v092_signal": {"func": f38_spec_underwriting_uw_efficiency_slope_diff_norm_5d_v092_signal},
    "f38_spec_underwriting_grossmargin_slope_diff_norm_10d_v093_signal": {"func": f38_spec_underwriting_grossmargin_slope_diff_norm_10d_v093_signal},
    "f38_spec_underwriting_ebitdamargin_slope_diff_norm_10d_v094_signal": {"func": f38_spec_underwriting_ebitdamargin_slope_diff_norm_10d_v094_signal},
    "f38_spec_underwriting_revenue_slope_diff_norm_10d_v095_signal": {"func": f38_spec_underwriting_revenue_slope_diff_norm_10d_v095_signal},
    "f38_spec_underwriting_uw_efficiency_slope_diff_norm_10d_v096_signal": {"func": f38_spec_underwriting_uw_efficiency_slope_diff_norm_10d_v096_signal},
    "f38_spec_underwriting_grossmargin_slope_diff_norm_21d_v097_signal": {"func": f38_spec_underwriting_grossmargin_slope_diff_norm_21d_v097_signal},
    "f38_spec_underwriting_ebitdamargin_slope_diff_norm_21d_v098_signal": {"func": f38_spec_underwriting_ebitdamargin_slope_diff_norm_21d_v098_signal},
    "f38_spec_underwriting_revenue_slope_diff_norm_21d_v099_signal": {"func": f38_spec_underwriting_revenue_slope_diff_norm_21d_v099_signal},
    "f38_spec_underwriting_uw_efficiency_slope_diff_norm_21d_v100_signal": {"func": f38_spec_underwriting_uw_efficiency_slope_diff_norm_21d_v100_signal},
    "f38_spec_underwriting_grossmargin_slope_diff_norm_42d_v101_signal": {"func": f38_spec_underwriting_grossmargin_slope_diff_norm_42d_v101_signal},
    "f38_spec_underwriting_ebitdamargin_slope_diff_norm_42d_v102_signal": {"func": f38_spec_underwriting_ebitdamargin_slope_diff_norm_42d_v102_signal},
    "f38_spec_underwriting_revenue_slope_diff_norm_42d_v103_signal": {"func": f38_spec_underwriting_revenue_slope_diff_norm_42d_v103_signal},
    "f38_spec_underwriting_uw_efficiency_slope_diff_norm_42d_v104_signal": {"func": f38_spec_underwriting_uw_efficiency_slope_diff_norm_42d_v104_signal},
    "f38_spec_underwriting_grossmargin_slope_diff_norm_63d_v105_signal": {"func": f38_spec_underwriting_grossmargin_slope_diff_norm_63d_v105_signal},
    "f38_spec_underwriting_ebitdamargin_slope_diff_norm_63d_v106_signal": {"func": f38_spec_underwriting_ebitdamargin_slope_diff_norm_63d_v106_signal},
    "f38_spec_underwriting_revenue_slope_diff_norm_63d_v107_signal": {"func": f38_spec_underwriting_revenue_slope_diff_norm_63d_v107_signal},
    "f38_spec_underwriting_uw_efficiency_slope_diff_norm_63d_v108_signal": {"func": f38_spec_underwriting_uw_efficiency_slope_diff_norm_63d_v108_signal},
    "f38_spec_underwriting_grossmargin_slope_diff_norm_126d_v109_signal": {"func": f38_spec_underwriting_grossmargin_slope_diff_norm_126d_v109_signal},
    "f38_spec_underwriting_ebitdamargin_slope_diff_norm_126d_v110_signal": {"func": f38_spec_underwriting_ebitdamargin_slope_diff_norm_126d_v110_signal},
    "f38_spec_underwriting_revenue_slope_diff_norm_126d_v111_signal": {"func": f38_spec_underwriting_revenue_slope_diff_norm_126d_v111_signal},
    "f38_spec_underwriting_uw_efficiency_slope_diff_norm_126d_v112_signal": {"func": f38_spec_underwriting_uw_efficiency_slope_diff_norm_126d_v112_signal},
    "f38_spec_underwriting_grossmargin_slope_diff_norm_252d_v113_signal": {"func": f38_spec_underwriting_grossmargin_slope_diff_norm_252d_v113_signal},
    "f38_spec_underwriting_ebitdamargin_slope_diff_norm_252d_v114_signal": {"func": f38_spec_underwriting_ebitdamargin_slope_diff_norm_252d_v114_signal},
    "f38_spec_underwriting_revenue_slope_diff_norm_252d_v115_signal": {"func": f38_spec_underwriting_revenue_slope_diff_norm_252d_v115_signal},
    "f38_spec_underwriting_uw_efficiency_slope_diff_norm_252d_v116_signal": {"func": f38_spec_underwriting_uw_efficiency_slope_diff_norm_252d_v116_signal},
    "f38_spec_underwriting_grossmargin_slope_diff_norm_504d_v117_signal": {"func": f38_spec_underwriting_grossmargin_slope_diff_norm_504d_v117_signal},
    "f38_spec_underwriting_ebitdamargin_slope_diff_norm_504d_v118_signal": {"func": f38_spec_underwriting_ebitdamargin_slope_diff_norm_504d_v118_signal},
    "f38_spec_underwriting_revenue_slope_diff_norm_504d_v119_signal": {"func": f38_spec_underwriting_revenue_slope_diff_norm_504d_v119_signal},
    "f38_spec_underwriting_uw_efficiency_slope_diff_norm_504d_v120_signal": {"func": f38_spec_underwriting_uw_efficiency_slope_diff_norm_504d_v120_signal},
    "f38_spec_underwriting_grossmargin_slope_diff_norm_756d_v121_signal": {"func": f38_spec_underwriting_grossmargin_slope_diff_norm_756d_v121_signal},
    "f38_spec_underwriting_ebitdamargin_slope_diff_norm_756d_v122_signal": {"func": f38_spec_underwriting_ebitdamargin_slope_diff_norm_756d_v122_signal},
    "f38_spec_underwriting_revenue_slope_diff_norm_756d_v123_signal": {"func": f38_spec_underwriting_revenue_slope_diff_norm_756d_v123_signal},
    "f38_spec_underwriting_uw_efficiency_slope_diff_norm_756d_v124_signal": {"func": f38_spec_underwriting_uw_efficiency_slope_diff_norm_756d_v124_signal},
    "f38_spec_underwriting_grossmargin_slope_diff_norm_1008d_v125_signal": {"func": f38_spec_underwriting_grossmargin_slope_diff_norm_1008d_v125_signal},
    "f38_spec_underwriting_ebitdamargin_slope_diff_norm_1008d_v126_signal": {"func": f38_spec_underwriting_ebitdamargin_slope_diff_norm_1008d_v126_signal},
    "f38_spec_underwriting_revenue_slope_diff_norm_1008d_v127_signal": {"func": f38_spec_underwriting_revenue_slope_diff_norm_1008d_v127_signal},
    "f38_spec_underwriting_uw_efficiency_slope_diff_norm_1008d_v128_signal": {"func": f38_spec_underwriting_uw_efficiency_slope_diff_norm_1008d_v128_signal},
    "f38_spec_underwriting_grossmargin_slope_diff_norm_1260d_v129_signal": {"func": f38_spec_underwriting_grossmargin_slope_diff_norm_1260d_v129_signal},
    "f38_spec_underwriting_ebitdamargin_slope_diff_norm_1260d_v130_signal": {"func": f38_spec_underwriting_ebitdamargin_slope_diff_norm_1260d_v130_signal},
    "f38_spec_underwriting_revenue_slope_diff_norm_1260d_v131_signal": {"func": f38_spec_underwriting_revenue_slope_diff_norm_1260d_v131_signal},
    "f38_spec_underwriting_uw_efficiency_slope_diff_norm_1260d_v132_signal": {"func": f38_spec_underwriting_uw_efficiency_slope_diff_norm_1260d_v132_signal},
    "f38_spec_underwriting_grossmargin_mom_z_5d_v133_signal": {"func": f38_spec_underwriting_grossmargin_mom_z_5d_v133_signal},
    "f38_spec_underwriting_ebitdamargin_mom_z_5d_v134_signal": {"func": f38_spec_underwriting_ebitdamargin_mom_z_5d_v134_signal},
    "f38_spec_underwriting_revenue_mom_z_5d_v135_signal": {"func": f38_spec_underwriting_revenue_mom_z_5d_v135_signal},
    "f38_spec_underwriting_uw_efficiency_mom_z_5d_v136_signal": {"func": f38_spec_underwriting_uw_efficiency_mom_z_5d_v136_signal},
    "f38_spec_underwriting_grossmargin_mom_z_10d_v137_signal": {"func": f38_spec_underwriting_grossmargin_mom_z_10d_v137_signal},
    "f38_spec_underwriting_ebitdamargin_mom_z_10d_v138_signal": {"func": f38_spec_underwriting_ebitdamargin_mom_z_10d_v138_signal},
    "f38_spec_underwriting_revenue_mom_z_10d_v139_signal": {"func": f38_spec_underwriting_revenue_mom_z_10d_v139_signal},
    "f38_spec_underwriting_uw_efficiency_mom_z_10d_v140_signal": {"func": f38_spec_underwriting_uw_efficiency_mom_z_10d_v140_signal},
    "f38_spec_underwriting_grossmargin_mom_z_21d_v141_signal": {"func": f38_spec_underwriting_grossmargin_mom_z_21d_v141_signal},
    "f38_spec_underwriting_ebitdamargin_mom_z_21d_v142_signal": {"func": f38_spec_underwriting_ebitdamargin_mom_z_21d_v142_signal},
    "f38_spec_underwriting_revenue_mom_z_21d_v143_signal": {"func": f38_spec_underwriting_revenue_mom_z_21d_v143_signal},
    "f38_spec_underwriting_uw_efficiency_mom_z_21d_v144_signal": {"func": f38_spec_underwriting_uw_efficiency_mom_z_21d_v144_signal},
    "f38_spec_underwriting_grossmargin_mom_z_42d_v145_signal": {"func": f38_spec_underwriting_grossmargin_mom_z_42d_v145_signal},
    "f38_spec_underwriting_ebitdamargin_mom_z_42d_v146_signal": {"func": f38_spec_underwriting_ebitdamargin_mom_z_42d_v146_signal},
    "f38_spec_underwriting_revenue_mom_z_42d_v147_signal": {"func": f38_spec_underwriting_revenue_mom_z_42d_v147_signal},
    "f38_spec_underwriting_uw_efficiency_mom_z_42d_v148_signal": {"func": f38_spec_underwriting_uw_efficiency_mom_z_42d_v148_signal},
    "f38_spec_underwriting_grossmargin_mom_z_63d_v149_signal": {"func": f38_spec_underwriting_grossmargin_mom_z_63d_v149_signal},
    "f38_spec_underwriting_ebitdamargin_mom_z_63d_v150_signal": {"func": f38_spec_underwriting_ebitdamargin_mom_z_63d_v150_signal},
}

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "deferredrev": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "equity": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "deposits": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "divyield": np.random.normal(100, 10, n).cumsum(), "bvps": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "tangibles": np.random.normal(100, 10, n).cumsum(), "grossmargin": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "revenue": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "liabilitiesc": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum()
    })
    print(f"Verifying {len(REGISTRY)} functions for family 38...")
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
