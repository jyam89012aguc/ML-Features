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

def f06_loan_quality_netinc_slope_pct_5d_v001_signal(netinc):
    """Percentage slope for Raw level of netinc over 5d window."""
    res = _slope_pct(netinc, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_ebt_slope_pct_5d_v002_signal(ebt):
    """Percentage slope for Raw level of ebt over 5d window."""
    res = _slope_pct(ebt, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_revenue_slope_pct_5d_v003_signal(revenue):
    """Percentage slope for Raw level of revenue over 5d window."""
    res = _slope_pct(revenue, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_provision_drag_slope_pct_5d_v004_signal(ebt, netinc, revenue):
    """Percentage slope for Provisioning and load proxy over 5d window."""
    res = _slope_pct(_ratio(ebt - netinc, revenue), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_net_margin_slope_pct_5d_v005_signal(netinc, revenue):
    """Percentage slope for Revenue-to-net income efficiency over 5d window."""
    res = _slope_pct(_ratio(netinc, revenue), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_netinc_slope_pct_10d_v006_signal(netinc):
    """Percentage slope for Raw level of netinc over 10d window."""
    res = _slope_pct(netinc, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_ebt_slope_pct_10d_v007_signal(ebt):
    """Percentage slope for Raw level of ebt over 10d window."""
    res = _slope_pct(ebt, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_revenue_slope_pct_10d_v008_signal(revenue):
    """Percentage slope for Raw level of revenue over 10d window."""
    res = _slope_pct(revenue, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_provision_drag_slope_pct_10d_v009_signal(ebt, netinc, revenue):
    """Percentage slope for Provisioning and load proxy over 10d window."""
    res = _slope_pct(_ratio(ebt - netinc, revenue), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_net_margin_slope_pct_10d_v010_signal(netinc, revenue):
    """Percentage slope for Revenue-to-net income efficiency over 10d window."""
    res = _slope_pct(_ratio(netinc, revenue), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_netinc_slope_pct_21d_v011_signal(netinc):
    """Percentage slope for Raw level of netinc over 21d window."""
    res = _slope_pct(netinc, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_ebt_slope_pct_21d_v012_signal(ebt):
    """Percentage slope for Raw level of ebt over 21d window."""
    res = _slope_pct(ebt, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_revenue_slope_pct_21d_v013_signal(revenue):
    """Percentage slope for Raw level of revenue over 21d window."""
    res = _slope_pct(revenue, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_provision_drag_slope_pct_21d_v014_signal(ebt, netinc, revenue):
    """Percentage slope for Provisioning and load proxy over 21d window."""
    res = _slope_pct(_ratio(ebt - netinc, revenue), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_net_margin_slope_pct_21d_v015_signal(netinc, revenue):
    """Percentage slope for Revenue-to-net income efficiency over 21d window."""
    res = _slope_pct(_ratio(netinc, revenue), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_netinc_slope_pct_42d_v016_signal(netinc):
    """Percentage slope for Raw level of netinc over 42d window."""
    res = _slope_pct(netinc, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_ebt_slope_pct_42d_v017_signal(ebt):
    """Percentage slope for Raw level of ebt over 42d window."""
    res = _slope_pct(ebt, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_revenue_slope_pct_42d_v018_signal(revenue):
    """Percentage slope for Raw level of revenue over 42d window."""
    res = _slope_pct(revenue, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_provision_drag_slope_pct_42d_v019_signal(ebt, netinc, revenue):
    """Percentage slope for Provisioning and load proxy over 42d window."""
    res = _slope_pct(_ratio(ebt - netinc, revenue), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_net_margin_slope_pct_42d_v020_signal(netinc, revenue):
    """Percentage slope for Revenue-to-net income efficiency over 42d window."""
    res = _slope_pct(_ratio(netinc, revenue), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_netinc_slope_pct_63d_v021_signal(netinc):
    """Percentage slope for Raw level of netinc over 63d window."""
    res = _slope_pct(netinc, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_ebt_slope_pct_63d_v022_signal(ebt):
    """Percentage slope for Raw level of ebt over 63d window."""
    res = _slope_pct(ebt, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_revenue_slope_pct_63d_v023_signal(revenue):
    """Percentage slope for Raw level of revenue over 63d window."""
    res = _slope_pct(revenue, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_provision_drag_slope_pct_63d_v024_signal(ebt, netinc, revenue):
    """Percentage slope for Provisioning and load proxy over 63d window."""
    res = _slope_pct(_ratio(ebt - netinc, revenue), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_net_margin_slope_pct_63d_v025_signal(netinc, revenue):
    """Percentage slope for Revenue-to-net income efficiency over 63d window."""
    res = _slope_pct(_ratio(netinc, revenue), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_netinc_slope_pct_126d_v026_signal(netinc):
    """Percentage slope for Raw level of netinc over 126d window."""
    res = _slope_pct(netinc, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_ebt_slope_pct_126d_v027_signal(ebt):
    """Percentage slope for Raw level of ebt over 126d window."""
    res = _slope_pct(ebt, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_revenue_slope_pct_126d_v028_signal(revenue):
    """Percentage slope for Raw level of revenue over 126d window."""
    res = _slope_pct(revenue, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_provision_drag_slope_pct_126d_v029_signal(ebt, netinc, revenue):
    """Percentage slope for Provisioning and load proxy over 126d window."""
    res = _slope_pct(_ratio(ebt - netinc, revenue), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_net_margin_slope_pct_126d_v030_signal(netinc, revenue):
    """Percentage slope for Revenue-to-net income efficiency over 126d window."""
    res = _slope_pct(_ratio(netinc, revenue), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_netinc_slope_pct_252d_v031_signal(netinc):
    """Percentage slope for Raw level of netinc over 252d window."""
    res = _slope_pct(netinc, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_ebt_slope_pct_252d_v032_signal(ebt):
    """Percentage slope for Raw level of ebt over 252d window."""
    res = _slope_pct(ebt, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_revenue_slope_pct_252d_v033_signal(revenue):
    """Percentage slope for Raw level of revenue over 252d window."""
    res = _slope_pct(revenue, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_provision_drag_slope_pct_252d_v034_signal(ebt, netinc, revenue):
    """Percentage slope for Provisioning and load proxy over 252d window."""
    res = _slope_pct(_ratio(ebt - netinc, revenue), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_net_margin_slope_pct_252d_v035_signal(netinc, revenue):
    """Percentage slope for Revenue-to-net income efficiency over 252d window."""
    res = _slope_pct(_ratio(netinc, revenue), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_netinc_slope_pct_504d_v036_signal(netinc):
    """Percentage slope for Raw level of netinc over 504d window."""
    res = _slope_pct(netinc, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_ebt_slope_pct_504d_v037_signal(ebt):
    """Percentage slope for Raw level of ebt over 504d window."""
    res = _slope_pct(ebt, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_revenue_slope_pct_504d_v038_signal(revenue):
    """Percentage slope for Raw level of revenue over 504d window."""
    res = _slope_pct(revenue, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_provision_drag_slope_pct_504d_v039_signal(ebt, netinc, revenue):
    """Percentage slope for Provisioning and load proxy over 504d window."""
    res = _slope_pct(_ratio(ebt - netinc, revenue), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_net_margin_slope_pct_504d_v040_signal(netinc, revenue):
    """Percentage slope for Revenue-to-net income efficiency over 504d window."""
    res = _slope_pct(_ratio(netinc, revenue), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_netinc_slope_pct_756d_v041_signal(netinc):
    """Percentage slope for Raw level of netinc over 756d window."""
    res = _slope_pct(netinc, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_ebt_slope_pct_756d_v042_signal(ebt):
    """Percentage slope for Raw level of ebt over 756d window."""
    res = _slope_pct(ebt, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_revenue_slope_pct_756d_v043_signal(revenue):
    """Percentage slope for Raw level of revenue over 756d window."""
    res = _slope_pct(revenue, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_provision_drag_slope_pct_756d_v044_signal(ebt, netinc, revenue):
    """Percentage slope for Provisioning and load proxy over 756d window."""
    res = _slope_pct(_ratio(ebt - netinc, revenue), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_net_margin_slope_pct_756d_v045_signal(netinc, revenue):
    """Percentage slope for Revenue-to-net income efficiency over 756d window."""
    res = _slope_pct(_ratio(netinc, revenue), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_netinc_slope_pct_1008d_v046_signal(netinc):
    """Percentage slope for Raw level of netinc over 1008d window."""
    res = _slope_pct(netinc, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_ebt_slope_pct_1008d_v047_signal(ebt):
    """Percentage slope for Raw level of ebt over 1008d window."""
    res = _slope_pct(ebt, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_revenue_slope_pct_1008d_v048_signal(revenue):
    """Percentage slope for Raw level of revenue over 1008d window."""
    res = _slope_pct(revenue, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_provision_drag_slope_pct_1008d_v049_signal(ebt, netinc, revenue):
    """Percentage slope for Provisioning and load proxy over 1008d window."""
    res = _slope_pct(_ratio(ebt - netinc, revenue), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_net_margin_slope_pct_1008d_v050_signal(netinc, revenue):
    """Percentage slope for Revenue-to-net income efficiency over 1008d window."""
    res = _slope_pct(_ratio(netinc, revenue), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_netinc_slope_pct_1260d_v051_signal(netinc):
    """Percentage slope for Raw level of netinc over 1260d window."""
    res = _slope_pct(netinc, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_ebt_slope_pct_1260d_v052_signal(ebt):
    """Percentage slope for Raw level of ebt over 1260d window."""
    res = _slope_pct(ebt, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_revenue_slope_pct_1260d_v053_signal(revenue):
    """Percentage slope for Raw level of revenue over 1260d window."""
    res = _slope_pct(revenue, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_provision_drag_slope_pct_1260d_v054_signal(ebt, netinc, revenue):
    """Percentage slope for Provisioning and load proxy over 1260d window."""
    res = _slope_pct(_ratio(ebt - netinc, revenue), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_net_margin_slope_pct_1260d_v055_signal(netinc, revenue):
    """Percentage slope for Revenue-to-net income efficiency over 1260d window."""
    res = _slope_pct(_ratio(netinc, revenue), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_netinc_jerk_5d_v056_signal(netinc):
    """Acceleration/Jerk for Raw level of netinc over 5d window."""
    res = _jerk(netinc, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_ebt_jerk_5d_v057_signal(ebt):
    """Acceleration/Jerk for Raw level of ebt over 5d window."""
    res = _jerk(ebt, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_revenue_jerk_5d_v058_signal(revenue):
    """Acceleration/Jerk for Raw level of revenue over 5d window."""
    res = _jerk(revenue, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_provision_drag_jerk_5d_v059_signal(ebt, netinc, revenue):
    """Acceleration/Jerk for Provisioning and load proxy over 5d window."""
    res = _jerk(_ratio(ebt - netinc, revenue), 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_net_margin_jerk_5d_v060_signal(netinc, revenue):
    """Acceleration/Jerk for Revenue-to-net income efficiency over 5d window."""
    res = _jerk(_ratio(netinc, revenue), 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_netinc_jerk_10d_v061_signal(netinc):
    """Acceleration/Jerk for Raw level of netinc over 10d window."""
    res = _jerk(netinc, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_ebt_jerk_10d_v062_signal(ebt):
    """Acceleration/Jerk for Raw level of ebt over 10d window."""
    res = _jerk(ebt, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_revenue_jerk_10d_v063_signal(revenue):
    """Acceleration/Jerk for Raw level of revenue over 10d window."""
    res = _jerk(revenue, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_provision_drag_jerk_10d_v064_signal(ebt, netinc, revenue):
    """Acceleration/Jerk for Provisioning and load proxy over 10d window."""
    res = _jerk(_ratio(ebt - netinc, revenue), 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_net_margin_jerk_10d_v065_signal(netinc, revenue):
    """Acceleration/Jerk for Revenue-to-net income efficiency over 10d window."""
    res = _jerk(_ratio(netinc, revenue), 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_netinc_jerk_21d_v066_signal(netinc):
    """Acceleration/Jerk for Raw level of netinc over 21d window."""
    res = _jerk(netinc, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_ebt_jerk_21d_v067_signal(ebt):
    """Acceleration/Jerk for Raw level of ebt over 21d window."""
    res = _jerk(ebt, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_revenue_jerk_21d_v068_signal(revenue):
    """Acceleration/Jerk for Raw level of revenue over 21d window."""
    res = _jerk(revenue, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_provision_drag_jerk_21d_v069_signal(ebt, netinc, revenue):
    """Acceleration/Jerk for Provisioning and load proxy over 21d window."""
    res = _jerk(_ratio(ebt - netinc, revenue), 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_net_margin_jerk_21d_v070_signal(netinc, revenue):
    """Acceleration/Jerk for Revenue-to-net income efficiency over 21d window."""
    res = _jerk(_ratio(netinc, revenue), 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_netinc_jerk_42d_v071_signal(netinc):
    """Acceleration/Jerk for Raw level of netinc over 42d window."""
    res = _jerk(netinc, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_ebt_jerk_42d_v072_signal(ebt):
    """Acceleration/Jerk for Raw level of ebt over 42d window."""
    res = _jerk(ebt, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_revenue_jerk_42d_v073_signal(revenue):
    """Acceleration/Jerk for Raw level of revenue over 42d window."""
    res = _jerk(revenue, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_provision_drag_jerk_42d_v074_signal(ebt, netinc, revenue):
    """Acceleration/Jerk for Provisioning and load proxy over 42d window."""
    res = _jerk(_ratio(ebt - netinc, revenue), 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_net_margin_jerk_42d_v075_signal(netinc, revenue):
    """Acceleration/Jerk for Revenue-to-net income efficiency over 42d window."""
    res = _jerk(_ratio(netinc, revenue), 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_netinc_jerk_63d_v076_signal(netinc):
    """Acceleration/Jerk for Raw level of netinc over 63d window."""
    res = _jerk(netinc, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_ebt_jerk_63d_v077_signal(ebt):
    """Acceleration/Jerk for Raw level of ebt over 63d window."""
    res = _jerk(ebt, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_revenue_jerk_63d_v078_signal(revenue):
    """Acceleration/Jerk for Raw level of revenue over 63d window."""
    res = _jerk(revenue, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_provision_drag_jerk_63d_v079_signal(ebt, netinc, revenue):
    """Acceleration/Jerk for Provisioning and load proxy over 63d window."""
    res = _jerk(_ratio(ebt - netinc, revenue), 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_net_margin_jerk_63d_v080_signal(netinc, revenue):
    """Acceleration/Jerk for Revenue-to-net income efficiency over 63d window."""
    res = _jerk(_ratio(netinc, revenue), 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_netinc_jerk_126d_v081_signal(netinc):
    """Acceleration/Jerk for Raw level of netinc over 126d window."""
    res = _jerk(netinc, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_ebt_jerk_126d_v082_signal(ebt):
    """Acceleration/Jerk for Raw level of ebt over 126d window."""
    res = _jerk(ebt, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_revenue_jerk_126d_v083_signal(revenue):
    """Acceleration/Jerk for Raw level of revenue over 126d window."""
    res = _jerk(revenue, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_provision_drag_jerk_126d_v084_signal(ebt, netinc, revenue):
    """Acceleration/Jerk for Provisioning and load proxy over 126d window."""
    res = _jerk(_ratio(ebt - netinc, revenue), 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_net_margin_jerk_126d_v085_signal(netinc, revenue):
    """Acceleration/Jerk for Revenue-to-net income efficiency over 126d window."""
    res = _jerk(_ratio(netinc, revenue), 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_netinc_jerk_252d_v086_signal(netinc):
    """Acceleration/Jerk for Raw level of netinc over 252d window."""
    res = _jerk(netinc, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_ebt_jerk_252d_v087_signal(ebt):
    """Acceleration/Jerk for Raw level of ebt over 252d window."""
    res = _jerk(ebt, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_revenue_jerk_252d_v088_signal(revenue):
    """Acceleration/Jerk for Raw level of revenue over 252d window."""
    res = _jerk(revenue, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_provision_drag_jerk_252d_v089_signal(ebt, netinc, revenue):
    """Acceleration/Jerk for Provisioning and load proxy over 252d window."""
    res = _jerk(_ratio(ebt - netinc, revenue), 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_net_margin_jerk_252d_v090_signal(netinc, revenue):
    """Acceleration/Jerk for Revenue-to-net income efficiency over 252d window."""
    res = _jerk(_ratio(netinc, revenue), 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_netinc_jerk_504d_v091_signal(netinc):
    """Acceleration/Jerk for Raw level of netinc over 504d window."""
    res = _jerk(netinc, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_ebt_jerk_504d_v092_signal(ebt):
    """Acceleration/Jerk for Raw level of ebt over 504d window."""
    res = _jerk(ebt, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_revenue_jerk_504d_v093_signal(revenue):
    """Acceleration/Jerk for Raw level of revenue over 504d window."""
    res = _jerk(revenue, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_provision_drag_jerk_504d_v094_signal(ebt, netinc, revenue):
    """Acceleration/Jerk for Provisioning and load proxy over 504d window."""
    res = _jerk(_ratio(ebt - netinc, revenue), 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_net_margin_jerk_504d_v095_signal(netinc, revenue):
    """Acceleration/Jerk for Revenue-to-net income efficiency over 504d window."""
    res = _jerk(_ratio(netinc, revenue), 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_netinc_jerk_756d_v096_signal(netinc):
    """Acceleration/Jerk for Raw level of netinc over 756d window."""
    res = _jerk(netinc, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_ebt_jerk_756d_v097_signal(ebt):
    """Acceleration/Jerk for Raw level of ebt over 756d window."""
    res = _jerk(ebt, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_revenue_jerk_756d_v098_signal(revenue):
    """Acceleration/Jerk for Raw level of revenue over 756d window."""
    res = _jerk(revenue, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_provision_drag_jerk_756d_v099_signal(ebt, netinc, revenue):
    """Acceleration/Jerk for Provisioning and load proxy over 756d window."""
    res = _jerk(_ratio(ebt - netinc, revenue), 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_net_margin_jerk_756d_v100_signal(netinc, revenue):
    """Acceleration/Jerk for Revenue-to-net income efficiency over 756d window."""
    res = _jerk(_ratio(netinc, revenue), 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_netinc_jerk_1008d_v101_signal(netinc):
    """Acceleration/Jerk for Raw level of netinc over 1008d window."""
    res = _jerk(netinc, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_ebt_jerk_1008d_v102_signal(ebt):
    """Acceleration/Jerk for Raw level of ebt over 1008d window."""
    res = _jerk(ebt, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_revenue_jerk_1008d_v103_signal(revenue):
    """Acceleration/Jerk for Raw level of revenue over 1008d window."""
    res = _jerk(revenue, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_provision_drag_jerk_1008d_v104_signal(ebt, netinc, revenue):
    """Acceleration/Jerk for Provisioning and load proxy over 1008d window."""
    res = _jerk(_ratio(ebt - netinc, revenue), 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_net_margin_jerk_1008d_v105_signal(netinc, revenue):
    """Acceleration/Jerk for Revenue-to-net income efficiency over 1008d window."""
    res = _jerk(_ratio(netinc, revenue), 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_netinc_jerk_1260d_v106_signal(netinc):
    """Acceleration/Jerk for Raw level of netinc over 1260d window."""
    res = _jerk(netinc, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_ebt_jerk_1260d_v107_signal(ebt):
    """Acceleration/Jerk for Raw level of ebt over 1260d window."""
    res = _jerk(ebt, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_revenue_jerk_1260d_v108_signal(revenue):
    """Acceleration/Jerk for Raw level of revenue over 1260d window."""
    res = _jerk(revenue, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_provision_drag_jerk_1260d_v109_signal(ebt, netinc, revenue):
    """Acceleration/Jerk for Provisioning and load proxy over 1260d window."""
    res = _jerk(_ratio(ebt - netinc, revenue), 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_net_margin_jerk_1260d_v110_signal(netinc, revenue):
    """Acceleration/Jerk for Revenue-to-net income efficiency over 1260d window."""
    res = _jerk(_ratio(netinc, revenue), 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_netinc_slope_diff_norm_5d_v111_signal(netinc):
    """Normalized slope change for Raw level of netinc over 5d window."""
    res = (_slope_pct(netinc, 5).diff(5) / _sma(netinc.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_ebt_slope_diff_norm_5d_v112_signal(ebt):
    """Normalized slope change for Raw level of ebt over 5d window."""
    res = (_slope_pct(ebt, 5).diff(5) / _sma(ebt.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_revenue_slope_diff_norm_5d_v113_signal(revenue):
    """Normalized slope change for Raw level of revenue over 5d window."""
    res = (_slope_pct(revenue, 5).diff(5) / _sma(revenue.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_provision_drag_slope_diff_norm_5d_v114_signal(ebt, netinc, revenue):
    """Normalized slope change for Provisioning and load proxy over 5d window."""
    res = (_slope_pct(_ratio(ebt - netinc, revenue), 5).diff(5) / _sma(_ratio(ebt - netinc, revenue).abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_net_margin_slope_diff_norm_5d_v115_signal(netinc, revenue):
    """Normalized slope change for Revenue-to-net income efficiency over 5d window."""
    res = (_slope_pct(_ratio(netinc, revenue), 5).diff(5) / _sma(_ratio(netinc, revenue).abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_netinc_slope_diff_norm_10d_v116_signal(netinc):
    """Normalized slope change for Raw level of netinc over 10d window."""
    res = (_slope_pct(netinc, 10).diff(10) / _sma(netinc.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_ebt_slope_diff_norm_10d_v117_signal(ebt):
    """Normalized slope change for Raw level of ebt over 10d window."""
    res = (_slope_pct(ebt, 10).diff(10) / _sma(ebt.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_revenue_slope_diff_norm_10d_v118_signal(revenue):
    """Normalized slope change for Raw level of revenue over 10d window."""
    res = (_slope_pct(revenue, 10).diff(10) / _sma(revenue.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_provision_drag_slope_diff_norm_10d_v119_signal(ebt, netinc, revenue):
    """Normalized slope change for Provisioning and load proxy over 10d window."""
    res = (_slope_pct(_ratio(ebt - netinc, revenue), 10).diff(10) / _sma(_ratio(ebt - netinc, revenue).abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_net_margin_slope_diff_norm_10d_v120_signal(netinc, revenue):
    """Normalized slope change for Revenue-to-net income efficiency over 10d window."""
    res = (_slope_pct(_ratio(netinc, revenue), 10).diff(10) / _sma(_ratio(netinc, revenue).abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_netinc_slope_diff_norm_21d_v121_signal(netinc):
    """Normalized slope change for Raw level of netinc over 21d window."""
    res = (_slope_pct(netinc, 21).diff(21) / _sma(netinc.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_ebt_slope_diff_norm_21d_v122_signal(ebt):
    """Normalized slope change for Raw level of ebt over 21d window."""
    res = (_slope_pct(ebt, 21).diff(21) / _sma(ebt.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_revenue_slope_diff_norm_21d_v123_signal(revenue):
    """Normalized slope change for Raw level of revenue over 21d window."""
    res = (_slope_pct(revenue, 21).diff(21) / _sma(revenue.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_provision_drag_slope_diff_norm_21d_v124_signal(ebt, netinc, revenue):
    """Normalized slope change for Provisioning and load proxy over 21d window."""
    res = (_slope_pct(_ratio(ebt - netinc, revenue), 21).diff(21) / _sma(_ratio(ebt - netinc, revenue).abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_net_margin_slope_diff_norm_21d_v125_signal(netinc, revenue):
    """Normalized slope change for Revenue-to-net income efficiency over 21d window."""
    res = (_slope_pct(_ratio(netinc, revenue), 21).diff(21) / _sma(_ratio(netinc, revenue).abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_netinc_slope_diff_norm_42d_v126_signal(netinc):
    """Normalized slope change for Raw level of netinc over 42d window."""
    res = (_slope_pct(netinc, 42).diff(42) / _sma(netinc.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_ebt_slope_diff_norm_42d_v127_signal(ebt):
    """Normalized slope change for Raw level of ebt over 42d window."""
    res = (_slope_pct(ebt, 42).diff(42) / _sma(ebt.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_revenue_slope_diff_norm_42d_v128_signal(revenue):
    """Normalized slope change for Raw level of revenue over 42d window."""
    res = (_slope_pct(revenue, 42).diff(42) / _sma(revenue.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_provision_drag_slope_diff_norm_42d_v129_signal(ebt, netinc, revenue):
    """Normalized slope change for Provisioning and load proxy over 42d window."""
    res = (_slope_pct(_ratio(ebt - netinc, revenue), 42).diff(42) / _sma(_ratio(ebt - netinc, revenue).abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_net_margin_slope_diff_norm_42d_v130_signal(netinc, revenue):
    """Normalized slope change for Revenue-to-net income efficiency over 42d window."""
    res = (_slope_pct(_ratio(netinc, revenue), 42).diff(42) / _sma(_ratio(netinc, revenue).abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_netinc_slope_diff_norm_63d_v131_signal(netinc):
    """Normalized slope change for Raw level of netinc over 63d window."""
    res = (_slope_pct(netinc, 63).diff(63) / _sma(netinc.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_ebt_slope_diff_norm_63d_v132_signal(ebt):
    """Normalized slope change for Raw level of ebt over 63d window."""
    res = (_slope_pct(ebt, 63).diff(63) / _sma(ebt.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_revenue_slope_diff_norm_63d_v133_signal(revenue):
    """Normalized slope change for Raw level of revenue over 63d window."""
    res = (_slope_pct(revenue, 63).diff(63) / _sma(revenue.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_provision_drag_slope_diff_norm_63d_v134_signal(ebt, netinc, revenue):
    """Normalized slope change for Provisioning and load proxy over 63d window."""
    res = (_slope_pct(_ratio(ebt - netinc, revenue), 63).diff(63) / _sma(_ratio(ebt - netinc, revenue).abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_net_margin_slope_diff_norm_63d_v135_signal(netinc, revenue):
    """Normalized slope change for Revenue-to-net income efficiency over 63d window."""
    res = (_slope_pct(_ratio(netinc, revenue), 63).diff(63) / _sma(_ratio(netinc, revenue).abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_netinc_slope_diff_norm_126d_v136_signal(netinc):
    """Normalized slope change for Raw level of netinc over 126d window."""
    res = (_slope_pct(netinc, 126).diff(126) / _sma(netinc.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_ebt_slope_diff_norm_126d_v137_signal(ebt):
    """Normalized slope change for Raw level of ebt over 126d window."""
    res = (_slope_pct(ebt, 126).diff(126) / _sma(ebt.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_revenue_slope_diff_norm_126d_v138_signal(revenue):
    """Normalized slope change for Raw level of revenue over 126d window."""
    res = (_slope_pct(revenue, 126).diff(126) / _sma(revenue.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_provision_drag_slope_diff_norm_126d_v139_signal(ebt, netinc, revenue):
    """Normalized slope change for Provisioning and load proxy over 126d window."""
    res = (_slope_pct(_ratio(ebt - netinc, revenue), 126).diff(126) / _sma(_ratio(ebt - netinc, revenue).abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_net_margin_slope_diff_norm_126d_v140_signal(netinc, revenue):
    """Normalized slope change for Revenue-to-net income efficiency over 126d window."""
    res = (_slope_pct(_ratio(netinc, revenue), 126).diff(126) / _sma(_ratio(netinc, revenue).abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_netinc_slope_diff_norm_252d_v141_signal(netinc):
    """Normalized slope change for Raw level of netinc over 252d window."""
    res = (_slope_pct(netinc, 252).diff(252) / _sma(netinc.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_ebt_slope_diff_norm_252d_v142_signal(ebt):
    """Normalized slope change for Raw level of ebt over 252d window."""
    res = (_slope_pct(ebt, 252).diff(252) / _sma(ebt.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_revenue_slope_diff_norm_252d_v143_signal(revenue):
    """Normalized slope change for Raw level of revenue over 252d window."""
    res = (_slope_pct(revenue, 252).diff(252) / _sma(revenue.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_provision_drag_slope_diff_norm_252d_v144_signal(ebt, netinc, revenue):
    """Normalized slope change for Provisioning and load proxy over 252d window."""
    res = (_slope_pct(_ratio(ebt - netinc, revenue), 252).diff(252) / _sma(_ratio(ebt - netinc, revenue).abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_net_margin_slope_diff_norm_252d_v145_signal(netinc, revenue):
    """Normalized slope change for Revenue-to-net income efficiency over 252d window."""
    res = (_slope_pct(_ratio(netinc, revenue), 252).diff(252) / _sma(_ratio(netinc, revenue).abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_netinc_slope_diff_norm_504d_v146_signal(netinc):
    """Normalized slope change for Raw level of netinc over 504d window."""
    res = (_slope_pct(netinc, 504).diff(504) / _sma(netinc.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_ebt_slope_diff_norm_504d_v147_signal(ebt):
    """Normalized slope change for Raw level of ebt over 504d window."""
    res = (_slope_pct(ebt, 504).diff(504) / _sma(ebt.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_revenue_slope_diff_norm_504d_v148_signal(revenue):
    """Normalized slope change for Raw level of revenue over 504d window."""
    res = (_slope_pct(revenue, 504).diff(504) / _sma(revenue.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_provision_drag_slope_diff_norm_504d_v149_signal(ebt, netinc, revenue):
    """Normalized slope change for Provisioning and load proxy over 504d window."""
    res = (_slope_pct(_ratio(ebt - netinc, revenue), 504).diff(504) / _sma(_ratio(ebt - netinc, revenue).abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_net_margin_slope_diff_norm_504d_v150_signal(netinc, revenue):
    """Normalized slope change for Revenue-to-net income efficiency over 504d window."""
    res = (_slope_pct(_ratio(netinc, revenue), 504).diff(504) / _sma(_ratio(netinc, revenue).abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)


# ===== Feature Registry =====
REGISTRY = {
    "f06_loan_quality_netinc_slope_pct_5d_v001_signal": {"func": f06_loan_quality_netinc_slope_pct_5d_v001_signal},
    "f06_loan_quality_ebt_slope_pct_5d_v002_signal": {"func": f06_loan_quality_ebt_slope_pct_5d_v002_signal},
    "f06_loan_quality_revenue_slope_pct_5d_v003_signal": {"func": f06_loan_quality_revenue_slope_pct_5d_v003_signal},
    "f06_loan_quality_provision_drag_slope_pct_5d_v004_signal": {"func": f06_loan_quality_provision_drag_slope_pct_5d_v004_signal},
    "f06_loan_quality_net_margin_slope_pct_5d_v005_signal": {"func": f06_loan_quality_net_margin_slope_pct_5d_v005_signal},
    "f06_loan_quality_netinc_slope_pct_10d_v006_signal": {"func": f06_loan_quality_netinc_slope_pct_10d_v006_signal},
    "f06_loan_quality_ebt_slope_pct_10d_v007_signal": {"func": f06_loan_quality_ebt_slope_pct_10d_v007_signal},
    "f06_loan_quality_revenue_slope_pct_10d_v008_signal": {"func": f06_loan_quality_revenue_slope_pct_10d_v008_signal},
    "f06_loan_quality_provision_drag_slope_pct_10d_v009_signal": {"func": f06_loan_quality_provision_drag_slope_pct_10d_v009_signal},
    "f06_loan_quality_net_margin_slope_pct_10d_v010_signal": {"func": f06_loan_quality_net_margin_slope_pct_10d_v010_signal},
    "f06_loan_quality_netinc_slope_pct_21d_v011_signal": {"func": f06_loan_quality_netinc_slope_pct_21d_v011_signal},
    "f06_loan_quality_ebt_slope_pct_21d_v012_signal": {"func": f06_loan_quality_ebt_slope_pct_21d_v012_signal},
    "f06_loan_quality_revenue_slope_pct_21d_v013_signal": {"func": f06_loan_quality_revenue_slope_pct_21d_v013_signal},
    "f06_loan_quality_provision_drag_slope_pct_21d_v014_signal": {"func": f06_loan_quality_provision_drag_slope_pct_21d_v014_signal},
    "f06_loan_quality_net_margin_slope_pct_21d_v015_signal": {"func": f06_loan_quality_net_margin_slope_pct_21d_v015_signal},
    "f06_loan_quality_netinc_slope_pct_42d_v016_signal": {"func": f06_loan_quality_netinc_slope_pct_42d_v016_signal},
    "f06_loan_quality_ebt_slope_pct_42d_v017_signal": {"func": f06_loan_quality_ebt_slope_pct_42d_v017_signal},
    "f06_loan_quality_revenue_slope_pct_42d_v018_signal": {"func": f06_loan_quality_revenue_slope_pct_42d_v018_signal},
    "f06_loan_quality_provision_drag_slope_pct_42d_v019_signal": {"func": f06_loan_quality_provision_drag_slope_pct_42d_v019_signal},
    "f06_loan_quality_net_margin_slope_pct_42d_v020_signal": {"func": f06_loan_quality_net_margin_slope_pct_42d_v020_signal},
    "f06_loan_quality_netinc_slope_pct_63d_v021_signal": {"func": f06_loan_quality_netinc_slope_pct_63d_v021_signal},
    "f06_loan_quality_ebt_slope_pct_63d_v022_signal": {"func": f06_loan_quality_ebt_slope_pct_63d_v022_signal},
    "f06_loan_quality_revenue_slope_pct_63d_v023_signal": {"func": f06_loan_quality_revenue_slope_pct_63d_v023_signal},
    "f06_loan_quality_provision_drag_slope_pct_63d_v024_signal": {"func": f06_loan_quality_provision_drag_slope_pct_63d_v024_signal},
    "f06_loan_quality_net_margin_slope_pct_63d_v025_signal": {"func": f06_loan_quality_net_margin_slope_pct_63d_v025_signal},
    "f06_loan_quality_netinc_slope_pct_126d_v026_signal": {"func": f06_loan_quality_netinc_slope_pct_126d_v026_signal},
    "f06_loan_quality_ebt_slope_pct_126d_v027_signal": {"func": f06_loan_quality_ebt_slope_pct_126d_v027_signal},
    "f06_loan_quality_revenue_slope_pct_126d_v028_signal": {"func": f06_loan_quality_revenue_slope_pct_126d_v028_signal},
    "f06_loan_quality_provision_drag_slope_pct_126d_v029_signal": {"func": f06_loan_quality_provision_drag_slope_pct_126d_v029_signal},
    "f06_loan_quality_net_margin_slope_pct_126d_v030_signal": {"func": f06_loan_quality_net_margin_slope_pct_126d_v030_signal},
    "f06_loan_quality_netinc_slope_pct_252d_v031_signal": {"func": f06_loan_quality_netinc_slope_pct_252d_v031_signal},
    "f06_loan_quality_ebt_slope_pct_252d_v032_signal": {"func": f06_loan_quality_ebt_slope_pct_252d_v032_signal},
    "f06_loan_quality_revenue_slope_pct_252d_v033_signal": {"func": f06_loan_quality_revenue_slope_pct_252d_v033_signal},
    "f06_loan_quality_provision_drag_slope_pct_252d_v034_signal": {"func": f06_loan_quality_provision_drag_slope_pct_252d_v034_signal},
    "f06_loan_quality_net_margin_slope_pct_252d_v035_signal": {"func": f06_loan_quality_net_margin_slope_pct_252d_v035_signal},
    "f06_loan_quality_netinc_slope_pct_504d_v036_signal": {"func": f06_loan_quality_netinc_slope_pct_504d_v036_signal},
    "f06_loan_quality_ebt_slope_pct_504d_v037_signal": {"func": f06_loan_quality_ebt_slope_pct_504d_v037_signal},
    "f06_loan_quality_revenue_slope_pct_504d_v038_signal": {"func": f06_loan_quality_revenue_slope_pct_504d_v038_signal},
    "f06_loan_quality_provision_drag_slope_pct_504d_v039_signal": {"func": f06_loan_quality_provision_drag_slope_pct_504d_v039_signal},
    "f06_loan_quality_net_margin_slope_pct_504d_v040_signal": {"func": f06_loan_quality_net_margin_slope_pct_504d_v040_signal},
    "f06_loan_quality_netinc_slope_pct_756d_v041_signal": {"func": f06_loan_quality_netinc_slope_pct_756d_v041_signal},
    "f06_loan_quality_ebt_slope_pct_756d_v042_signal": {"func": f06_loan_quality_ebt_slope_pct_756d_v042_signal},
    "f06_loan_quality_revenue_slope_pct_756d_v043_signal": {"func": f06_loan_quality_revenue_slope_pct_756d_v043_signal},
    "f06_loan_quality_provision_drag_slope_pct_756d_v044_signal": {"func": f06_loan_quality_provision_drag_slope_pct_756d_v044_signal},
    "f06_loan_quality_net_margin_slope_pct_756d_v045_signal": {"func": f06_loan_quality_net_margin_slope_pct_756d_v045_signal},
    "f06_loan_quality_netinc_slope_pct_1008d_v046_signal": {"func": f06_loan_quality_netinc_slope_pct_1008d_v046_signal},
    "f06_loan_quality_ebt_slope_pct_1008d_v047_signal": {"func": f06_loan_quality_ebt_slope_pct_1008d_v047_signal},
    "f06_loan_quality_revenue_slope_pct_1008d_v048_signal": {"func": f06_loan_quality_revenue_slope_pct_1008d_v048_signal},
    "f06_loan_quality_provision_drag_slope_pct_1008d_v049_signal": {"func": f06_loan_quality_provision_drag_slope_pct_1008d_v049_signal},
    "f06_loan_quality_net_margin_slope_pct_1008d_v050_signal": {"func": f06_loan_quality_net_margin_slope_pct_1008d_v050_signal},
    "f06_loan_quality_netinc_slope_pct_1260d_v051_signal": {"func": f06_loan_quality_netinc_slope_pct_1260d_v051_signal},
    "f06_loan_quality_ebt_slope_pct_1260d_v052_signal": {"func": f06_loan_quality_ebt_slope_pct_1260d_v052_signal},
    "f06_loan_quality_revenue_slope_pct_1260d_v053_signal": {"func": f06_loan_quality_revenue_slope_pct_1260d_v053_signal},
    "f06_loan_quality_provision_drag_slope_pct_1260d_v054_signal": {"func": f06_loan_quality_provision_drag_slope_pct_1260d_v054_signal},
    "f06_loan_quality_net_margin_slope_pct_1260d_v055_signal": {"func": f06_loan_quality_net_margin_slope_pct_1260d_v055_signal},
    "f06_loan_quality_netinc_jerk_5d_v056_signal": {"func": f06_loan_quality_netinc_jerk_5d_v056_signal},
    "f06_loan_quality_ebt_jerk_5d_v057_signal": {"func": f06_loan_quality_ebt_jerk_5d_v057_signal},
    "f06_loan_quality_revenue_jerk_5d_v058_signal": {"func": f06_loan_quality_revenue_jerk_5d_v058_signal},
    "f06_loan_quality_provision_drag_jerk_5d_v059_signal": {"func": f06_loan_quality_provision_drag_jerk_5d_v059_signal},
    "f06_loan_quality_net_margin_jerk_5d_v060_signal": {"func": f06_loan_quality_net_margin_jerk_5d_v060_signal},
    "f06_loan_quality_netinc_jerk_10d_v061_signal": {"func": f06_loan_quality_netinc_jerk_10d_v061_signal},
    "f06_loan_quality_ebt_jerk_10d_v062_signal": {"func": f06_loan_quality_ebt_jerk_10d_v062_signal},
    "f06_loan_quality_revenue_jerk_10d_v063_signal": {"func": f06_loan_quality_revenue_jerk_10d_v063_signal},
    "f06_loan_quality_provision_drag_jerk_10d_v064_signal": {"func": f06_loan_quality_provision_drag_jerk_10d_v064_signal},
    "f06_loan_quality_net_margin_jerk_10d_v065_signal": {"func": f06_loan_quality_net_margin_jerk_10d_v065_signal},
    "f06_loan_quality_netinc_jerk_21d_v066_signal": {"func": f06_loan_quality_netinc_jerk_21d_v066_signal},
    "f06_loan_quality_ebt_jerk_21d_v067_signal": {"func": f06_loan_quality_ebt_jerk_21d_v067_signal},
    "f06_loan_quality_revenue_jerk_21d_v068_signal": {"func": f06_loan_quality_revenue_jerk_21d_v068_signal},
    "f06_loan_quality_provision_drag_jerk_21d_v069_signal": {"func": f06_loan_quality_provision_drag_jerk_21d_v069_signal},
    "f06_loan_quality_net_margin_jerk_21d_v070_signal": {"func": f06_loan_quality_net_margin_jerk_21d_v070_signal},
    "f06_loan_quality_netinc_jerk_42d_v071_signal": {"func": f06_loan_quality_netinc_jerk_42d_v071_signal},
    "f06_loan_quality_ebt_jerk_42d_v072_signal": {"func": f06_loan_quality_ebt_jerk_42d_v072_signal},
    "f06_loan_quality_revenue_jerk_42d_v073_signal": {"func": f06_loan_quality_revenue_jerk_42d_v073_signal},
    "f06_loan_quality_provision_drag_jerk_42d_v074_signal": {"func": f06_loan_quality_provision_drag_jerk_42d_v074_signal},
    "f06_loan_quality_net_margin_jerk_42d_v075_signal": {"func": f06_loan_quality_net_margin_jerk_42d_v075_signal},
    "f06_loan_quality_netinc_jerk_63d_v076_signal": {"func": f06_loan_quality_netinc_jerk_63d_v076_signal},
    "f06_loan_quality_ebt_jerk_63d_v077_signal": {"func": f06_loan_quality_ebt_jerk_63d_v077_signal},
    "f06_loan_quality_revenue_jerk_63d_v078_signal": {"func": f06_loan_quality_revenue_jerk_63d_v078_signal},
    "f06_loan_quality_provision_drag_jerk_63d_v079_signal": {"func": f06_loan_quality_provision_drag_jerk_63d_v079_signal},
    "f06_loan_quality_net_margin_jerk_63d_v080_signal": {"func": f06_loan_quality_net_margin_jerk_63d_v080_signal},
    "f06_loan_quality_netinc_jerk_126d_v081_signal": {"func": f06_loan_quality_netinc_jerk_126d_v081_signal},
    "f06_loan_quality_ebt_jerk_126d_v082_signal": {"func": f06_loan_quality_ebt_jerk_126d_v082_signal},
    "f06_loan_quality_revenue_jerk_126d_v083_signal": {"func": f06_loan_quality_revenue_jerk_126d_v083_signal},
    "f06_loan_quality_provision_drag_jerk_126d_v084_signal": {"func": f06_loan_quality_provision_drag_jerk_126d_v084_signal},
    "f06_loan_quality_net_margin_jerk_126d_v085_signal": {"func": f06_loan_quality_net_margin_jerk_126d_v085_signal},
    "f06_loan_quality_netinc_jerk_252d_v086_signal": {"func": f06_loan_quality_netinc_jerk_252d_v086_signal},
    "f06_loan_quality_ebt_jerk_252d_v087_signal": {"func": f06_loan_quality_ebt_jerk_252d_v087_signal},
    "f06_loan_quality_revenue_jerk_252d_v088_signal": {"func": f06_loan_quality_revenue_jerk_252d_v088_signal},
    "f06_loan_quality_provision_drag_jerk_252d_v089_signal": {"func": f06_loan_quality_provision_drag_jerk_252d_v089_signal},
    "f06_loan_quality_net_margin_jerk_252d_v090_signal": {"func": f06_loan_quality_net_margin_jerk_252d_v090_signal},
    "f06_loan_quality_netinc_jerk_504d_v091_signal": {"func": f06_loan_quality_netinc_jerk_504d_v091_signal},
    "f06_loan_quality_ebt_jerk_504d_v092_signal": {"func": f06_loan_quality_ebt_jerk_504d_v092_signal},
    "f06_loan_quality_revenue_jerk_504d_v093_signal": {"func": f06_loan_quality_revenue_jerk_504d_v093_signal},
    "f06_loan_quality_provision_drag_jerk_504d_v094_signal": {"func": f06_loan_quality_provision_drag_jerk_504d_v094_signal},
    "f06_loan_quality_net_margin_jerk_504d_v095_signal": {"func": f06_loan_quality_net_margin_jerk_504d_v095_signal},
    "f06_loan_quality_netinc_jerk_756d_v096_signal": {"func": f06_loan_quality_netinc_jerk_756d_v096_signal},
    "f06_loan_quality_ebt_jerk_756d_v097_signal": {"func": f06_loan_quality_ebt_jerk_756d_v097_signal},
    "f06_loan_quality_revenue_jerk_756d_v098_signal": {"func": f06_loan_quality_revenue_jerk_756d_v098_signal},
    "f06_loan_quality_provision_drag_jerk_756d_v099_signal": {"func": f06_loan_quality_provision_drag_jerk_756d_v099_signal},
    "f06_loan_quality_net_margin_jerk_756d_v100_signal": {"func": f06_loan_quality_net_margin_jerk_756d_v100_signal},
    "f06_loan_quality_netinc_jerk_1008d_v101_signal": {"func": f06_loan_quality_netinc_jerk_1008d_v101_signal},
    "f06_loan_quality_ebt_jerk_1008d_v102_signal": {"func": f06_loan_quality_ebt_jerk_1008d_v102_signal},
    "f06_loan_quality_revenue_jerk_1008d_v103_signal": {"func": f06_loan_quality_revenue_jerk_1008d_v103_signal},
    "f06_loan_quality_provision_drag_jerk_1008d_v104_signal": {"func": f06_loan_quality_provision_drag_jerk_1008d_v104_signal},
    "f06_loan_quality_net_margin_jerk_1008d_v105_signal": {"func": f06_loan_quality_net_margin_jerk_1008d_v105_signal},
    "f06_loan_quality_netinc_jerk_1260d_v106_signal": {"func": f06_loan_quality_netinc_jerk_1260d_v106_signal},
    "f06_loan_quality_ebt_jerk_1260d_v107_signal": {"func": f06_loan_quality_ebt_jerk_1260d_v107_signal},
    "f06_loan_quality_revenue_jerk_1260d_v108_signal": {"func": f06_loan_quality_revenue_jerk_1260d_v108_signal},
    "f06_loan_quality_provision_drag_jerk_1260d_v109_signal": {"func": f06_loan_quality_provision_drag_jerk_1260d_v109_signal},
    "f06_loan_quality_net_margin_jerk_1260d_v110_signal": {"func": f06_loan_quality_net_margin_jerk_1260d_v110_signal},
    "f06_loan_quality_netinc_slope_diff_norm_5d_v111_signal": {"func": f06_loan_quality_netinc_slope_diff_norm_5d_v111_signal},
    "f06_loan_quality_ebt_slope_diff_norm_5d_v112_signal": {"func": f06_loan_quality_ebt_slope_diff_norm_5d_v112_signal},
    "f06_loan_quality_revenue_slope_diff_norm_5d_v113_signal": {"func": f06_loan_quality_revenue_slope_diff_norm_5d_v113_signal},
    "f06_loan_quality_provision_drag_slope_diff_norm_5d_v114_signal": {"func": f06_loan_quality_provision_drag_slope_diff_norm_5d_v114_signal},
    "f06_loan_quality_net_margin_slope_diff_norm_5d_v115_signal": {"func": f06_loan_quality_net_margin_slope_diff_norm_5d_v115_signal},
    "f06_loan_quality_netinc_slope_diff_norm_10d_v116_signal": {"func": f06_loan_quality_netinc_slope_diff_norm_10d_v116_signal},
    "f06_loan_quality_ebt_slope_diff_norm_10d_v117_signal": {"func": f06_loan_quality_ebt_slope_diff_norm_10d_v117_signal},
    "f06_loan_quality_revenue_slope_diff_norm_10d_v118_signal": {"func": f06_loan_quality_revenue_slope_diff_norm_10d_v118_signal},
    "f06_loan_quality_provision_drag_slope_diff_norm_10d_v119_signal": {"func": f06_loan_quality_provision_drag_slope_diff_norm_10d_v119_signal},
    "f06_loan_quality_net_margin_slope_diff_norm_10d_v120_signal": {"func": f06_loan_quality_net_margin_slope_diff_norm_10d_v120_signal},
    "f06_loan_quality_netinc_slope_diff_norm_21d_v121_signal": {"func": f06_loan_quality_netinc_slope_diff_norm_21d_v121_signal},
    "f06_loan_quality_ebt_slope_diff_norm_21d_v122_signal": {"func": f06_loan_quality_ebt_slope_diff_norm_21d_v122_signal},
    "f06_loan_quality_revenue_slope_diff_norm_21d_v123_signal": {"func": f06_loan_quality_revenue_slope_diff_norm_21d_v123_signal},
    "f06_loan_quality_provision_drag_slope_diff_norm_21d_v124_signal": {"func": f06_loan_quality_provision_drag_slope_diff_norm_21d_v124_signal},
    "f06_loan_quality_net_margin_slope_diff_norm_21d_v125_signal": {"func": f06_loan_quality_net_margin_slope_diff_norm_21d_v125_signal},
    "f06_loan_quality_netinc_slope_diff_norm_42d_v126_signal": {"func": f06_loan_quality_netinc_slope_diff_norm_42d_v126_signal},
    "f06_loan_quality_ebt_slope_diff_norm_42d_v127_signal": {"func": f06_loan_quality_ebt_slope_diff_norm_42d_v127_signal},
    "f06_loan_quality_revenue_slope_diff_norm_42d_v128_signal": {"func": f06_loan_quality_revenue_slope_diff_norm_42d_v128_signal},
    "f06_loan_quality_provision_drag_slope_diff_norm_42d_v129_signal": {"func": f06_loan_quality_provision_drag_slope_diff_norm_42d_v129_signal},
    "f06_loan_quality_net_margin_slope_diff_norm_42d_v130_signal": {"func": f06_loan_quality_net_margin_slope_diff_norm_42d_v130_signal},
    "f06_loan_quality_netinc_slope_diff_norm_63d_v131_signal": {"func": f06_loan_quality_netinc_slope_diff_norm_63d_v131_signal},
    "f06_loan_quality_ebt_slope_diff_norm_63d_v132_signal": {"func": f06_loan_quality_ebt_slope_diff_norm_63d_v132_signal},
    "f06_loan_quality_revenue_slope_diff_norm_63d_v133_signal": {"func": f06_loan_quality_revenue_slope_diff_norm_63d_v133_signal},
    "f06_loan_quality_provision_drag_slope_diff_norm_63d_v134_signal": {"func": f06_loan_quality_provision_drag_slope_diff_norm_63d_v134_signal},
    "f06_loan_quality_net_margin_slope_diff_norm_63d_v135_signal": {"func": f06_loan_quality_net_margin_slope_diff_norm_63d_v135_signal},
    "f06_loan_quality_netinc_slope_diff_norm_126d_v136_signal": {"func": f06_loan_quality_netinc_slope_diff_norm_126d_v136_signal},
    "f06_loan_quality_ebt_slope_diff_norm_126d_v137_signal": {"func": f06_loan_quality_ebt_slope_diff_norm_126d_v137_signal},
    "f06_loan_quality_revenue_slope_diff_norm_126d_v138_signal": {"func": f06_loan_quality_revenue_slope_diff_norm_126d_v138_signal},
    "f06_loan_quality_provision_drag_slope_diff_norm_126d_v139_signal": {"func": f06_loan_quality_provision_drag_slope_diff_norm_126d_v139_signal},
    "f06_loan_quality_net_margin_slope_diff_norm_126d_v140_signal": {"func": f06_loan_quality_net_margin_slope_diff_norm_126d_v140_signal},
    "f06_loan_quality_netinc_slope_diff_norm_252d_v141_signal": {"func": f06_loan_quality_netinc_slope_diff_norm_252d_v141_signal},
    "f06_loan_quality_ebt_slope_diff_norm_252d_v142_signal": {"func": f06_loan_quality_ebt_slope_diff_norm_252d_v142_signal},
    "f06_loan_quality_revenue_slope_diff_norm_252d_v143_signal": {"func": f06_loan_quality_revenue_slope_diff_norm_252d_v143_signal},
    "f06_loan_quality_provision_drag_slope_diff_norm_252d_v144_signal": {"func": f06_loan_quality_provision_drag_slope_diff_norm_252d_v144_signal},
    "f06_loan_quality_net_margin_slope_diff_norm_252d_v145_signal": {"func": f06_loan_quality_net_margin_slope_diff_norm_252d_v145_signal},
    "f06_loan_quality_netinc_slope_diff_norm_504d_v146_signal": {"func": f06_loan_quality_netinc_slope_diff_norm_504d_v146_signal},
    "f06_loan_quality_ebt_slope_diff_norm_504d_v147_signal": {"func": f06_loan_quality_ebt_slope_diff_norm_504d_v147_signal},
    "f06_loan_quality_revenue_slope_diff_norm_504d_v148_signal": {"func": f06_loan_quality_revenue_slope_diff_norm_504d_v148_signal},
    "f06_loan_quality_provision_drag_slope_diff_norm_504d_v149_signal": {"func": f06_loan_quality_provision_drag_slope_diff_norm_504d_v149_signal},
    "f06_loan_quality_net_margin_slope_diff_norm_504d_v150_signal": {"func": f06_loan_quality_net_margin_slope_diff_norm_504d_v150_signal},
}

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "deferredrev": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "equity": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "deposits": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "divyield": np.random.normal(100, 10, n).cumsum(), "bvps": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "tangibles": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "grossmargin": np.random.normal(100, 10, n).cumsum(), "revenue": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "liabilitiesc": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum()
    })
    print(f"Verifying {len(REGISTRY)} functions for family 06...")
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
