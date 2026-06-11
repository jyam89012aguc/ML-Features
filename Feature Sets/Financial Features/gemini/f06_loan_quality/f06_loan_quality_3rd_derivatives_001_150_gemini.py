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

def f06_loan_quality_netinc_slope_diff_norm_756d_v151_signal(netinc):
    """Normalized slope change for Raw level of netinc over 756d window."""
    res = (_slope_pct(netinc, 756).diff(756) / _sma(netinc.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_ebt_slope_diff_norm_756d_v152_signal(ebt):
    """Normalized slope change for Raw level of ebt over 756d window."""
    res = (_slope_pct(ebt, 756).diff(756) / _sma(ebt.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_revenue_slope_diff_norm_756d_v153_signal(revenue):
    """Normalized slope change for Raw level of revenue over 756d window."""
    res = (_slope_pct(revenue, 756).diff(756) / _sma(revenue.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_provision_drag_slope_diff_norm_756d_v154_signal(ebt, netinc, revenue):
    """Normalized slope change for Provisioning and load proxy over 756d window."""
    res = (_slope_pct(_ratio(ebt - netinc, revenue), 756).diff(756) / _sma(_ratio(ebt - netinc, revenue).abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_net_margin_slope_diff_norm_756d_v155_signal(netinc, revenue):
    """Normalized slope change for Revenue-to-net income efficiency over 756d window."""
    res = (_slope_pct(_ratio(netinc, revenue), 756).diff(756) / _sma(_ratio(netinc, revenue).abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_netinc_slope_diff_norm_1008d_v156_signal(netinc):
    """Normalized slope change for Raw level of netinc over 1008d window."""
    res = (_slope_pct(netinc, 1008).diff(1008) / _sma(netinc.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_ebt_slope_diff_norm_1008d_v157_signal(ebt):
    """Normalized slope change for Raw level of ebt over 1008d window."""
    res = (_slope_pct(ebt, 1008).diff(1008) / _sma(ebt.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_revenue_slope_diff_norm_1008d_v158_signal(revenue):
    """Normalized slope change for Raw level of revenue over 1008d window."""
    res = (_slope_pct(revenue, 1008).diff(1008) / _sma(revenue.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_provision_drag_slope_diff_norm_1008d_v159_signal(ebt, netinc, revenue):
    """Normalized slope change for Provisioning and load proxy over 1008d window."""
    res = (_slope_pct(_ratio(ebt - netinc, revenue), 1008).diff(1008) / _sma(_ratio(ebt - netinc, revenue).abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_net_margin_slope_diff_norm_1008d_v160_signal(netinc, revenue):
    """Normalized slope change for Revenue-to-net income efficiency over 1008d window."""
    res = (_slope_pct(_ratio(netinc, revenue), 1008).diff(1008) / _sma(_ratio(netinc, revenue).abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_netinc_slope_diff_norm_1260d_v161_signal(netinc):
    """Normalized slope change for Raw level of netinc over 1260d window."""
    res = (_slope_pct(netinc, 1260).diff(1260) / _sma(netinc.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_ebt_slope_diff_norm_1260d_v162_signal(ebt):
    """Normalized slope change for Raw level of ebt over 1260d window."""
    res = (_slope_pct(ebt, 1260).diff(1260) / _sma(ebt.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_revenue_slope_diff_norm_1260d_v163_signal(revenue):
    """Normalized slope change for Raw level of revenue over 1260d window."""
    res = (_slope_pct(revenue, 1260).diff(1260) / _sma(revenue.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_provision_drag_slope_diff_norm_1260d_v164_signal(ebt, netinc, revenue):
    """Normalized slope change for Provisioning and load proxy over 1260d window."""
    res = (_slope_pct(_ratio(ebt - netinc, revenue), 1260).diff(1260) / _sma(_ratio(ebt - netinc, revenue).abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_net_margin_slope_diff_norm_1260d_v165_signal(netinc, revenue):
    """Normalized slope change for Revenue-to-net income efficiency over 1260d window."""
    res = (_slope_pct(_ratio(netinc, revenue), 1260).diff(1260) / _sma(_ratio(netinc, revenue).abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_netinc_mom_z_5d_v166_signal(netinc):
    """Relative momentum strength for Raw level of netinc over 5d window."""
    res = _z(_slope_pct(netinc, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_ebt_mom_z_5d_v167_signal(ebt):
    """Relative momentum strength for Raw level of ebt over 5d window."""
    res = _z(_slope_pct(ebt, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_revenue_mom_z_5d_v168_signal(revenue):
    """Relative momentum strength for Raw level of revenue over 5d window."""
    res = _z(_slope_pct(revenue, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_provision_drag_mom_z_5d_v169_signal(ebt, netinc, revenue):
    """Relative momentum strength for Provisioning and load proxy over 5d window."""
    res = _z(_slope_pct(_ratio(ebt - netinc, revenue), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_net_margin_mom_z_5d_v170_signal(netinc, revenue):
    """Relative momentum strength for Revenue-to-net income efficiency over 5d window."""
    res = _z(_slope_pct(_ratio(netinc, revenue), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_netinc_mom_z_10d_v171_signal(netinc):
    """Relative momentum strength for Raw level of netinc over 10d window."""
    res = _z(_slope_pct(netinc, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_ebt_mom_z_10d_v172_signal(ebt):
    """Relative momentum strength for Raw level of ebt over 10d window."""
    res = _z(_slope_pct(ebt, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_revenue_mom_z_10d_v173_signal(revenue):
    """Relative momentum strength for Raw level of revenue over 10d window."""
    res = _z(_slope_pct(revenue, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_provision_drag_mom_z_10d_v174_signal(ebt, netinc, revenue):
    """Relative momentum strength for Provisioning and load proxy over 10d window."""
    res = _z(_slope_pct(_ratio(ebt - netinc, revenue), 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_net_margin_mom_z_10d_v175_signal(netinc, revenue):
    """Relative momentum strength for Revenue-to-net income efficiency over 10d window."""
    res = _z(_slope_pct(_ratio(netinc, revenue), 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_netinc_mom_z_21d_v176_signal(netinc):
    """Relative momentum strength for Raw level of netinc over 21d window."""
    res = _z(_slope_pct(netinc, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_ebt_mom_z_21d_v177_signal(ebt):
    """Relative momentum strength for Raw level of ebt over 21d window."""
    res = _z(_slope_pct(ebt, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_revenue_mom_z_21d_v178_signal(revenue):
    """Relative momentum strength for Raw level of revenue over 21d window."""
    res = _z(_slope_pct(revenue, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_provision_drag_mom_z_21d_v179_signal(ebt, netinc, revenue):
    """Relative momentum strength for Provisioning and load proxy over 21d window."""
    res = _z(_slope_pct(_ratio(ebt - netinc, revenue), 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_net_margin_mom_z_21d_v180_signal(netinc, revenue):
    """Relative momentum strength for Revenue-to-net income efficiency over 21d window."""
    res = _z(_slope_pct(_ratio(netinc, revenue), 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_netinc_mom_z_42d_v181_signal(netinc):
    """Relative momentum strength for Raw level of netinc over 42d window."""
    res = _z(_slope_pct(netinc, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_ebt_mom_z_42d_v182_signal(ebt):
    """Relative momentum strength for Raw level of ebt over 42d window."""
    res = _z(_slope_pct(ebt, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_revenue_mom_z_42d_v183_signal(revenue):
    """Relative momentum strength for Raw level of revenue over 42d window."""
    res = _z(_slope_pct(revenue, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_provision_drag_mom_z_42d_v184_signal(ebt, netinc, revenue):
    """Relative momentum strength for Provisioning and load proxy over 42d window."""
    res = _z(_slope_pct(_ratio(ebt - netinc, revenue), 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_net_margin_mom_z_42d_v185_signal(netinc, revenue):
    """Relative momentum strength for Revenue-to-net income efficiency over 42d window."""
    res = _z(_slope_pct(_ratio(netinc, revenue), 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_netinc_mom_z_63d_v186_signal(netinc):
    """Relative momentum strength for Raw level of netinc over 63d window."""
    res = _z(_slope_pct(netinc, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_ebt_mom_z_63d_v187_signal(ebt):
    """Relative momentum strength for Raw level of ebt over 63d window."""
    res = _z(_slope_pct(ebt, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_revenue_mom_z_63d_v188_signal(revenue):
    """Relative momentum strength for Raw level of revenue over 63d window."""
    res = _z(_slope_pct(revenue, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_provision_drag_mom_z_63d_v189_signal(ebt, netinc, revenue):
    """Relative momentum strength for Provisioning and load proxy over 63d window."""
    res = _z(_slope_pct(_ratio(ebt - netinc, revenue), 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_net_margin_mom_z_63d_v190_signal(netinc, revenue):
    """Relative momentum strength for Revenue-to-net income efficiency over 63d window."""
    res = _z(_slope_pct(_ratio(netinc, revenue), 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_netinc_mom_z_126d_v191_signal(netinc):
    """Relative momentum strength for Raw level of netinc over 126d window."""
    res = _z(_slope_pct(netinc, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_ebt_mom_z_126d_v192_signal(ebt):
    """Relative momentum strength for Raw level of ebt over 126d window."""
    res = _z(_slope_pct(ebt, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_revenue_mom_z_126d_v193_signal(revenue):
    """Relative momentum strength for Raw level of revenue over 126d window."""
    res = _z(_slope_pct(revenue, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_provision_drag_mom_z_126d_v194_signal(ebt, netinc, revenue):
    """Relative momentum strength for Provisioning and load proxy over 126d window."""
    res = _z(_slope_pct(_ratio(ebt - netinc, revenue), 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_net_margin_mom_z_126d_v195_signal(netinc, revenue):
    """Relative momentum strength for Revenue-to-net income efficiency over 126d window."""
    res = _z(_slope_pct(_ratio(netinc, revenue), 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_netinc_mom_z_252d_v196_signal(netinc):
    """Relative momentum strength for Raw level of netinc over 252d window."""
    res = _z(_slope_pct(netinc, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_ebt_mom_z_252d_v197_signal(ebt):
    """Relative momentum strength for Raw level of ebt over 252d window."""
    res = _z(_slope_pct(ebt, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_revenue_mom_z_252d_v198_signal(revenue):
    """Relative momentum strength for Raw level of revenue over 252d window."""
    res = _z(_slope_pct(revenue, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_provision_drag_mom_z_252d_v199_signal(ebt, netinc, revenue):
    """Relative momentum strength for Provisioning and load proxy over 252d window."""
    res = _z(_slope_pct(_ratio(ebt - netinc, revenue), 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_net_margin_mom_z_252d_v200_signal(netinc, revenue):
    """Relative momentum strength for Revenue-to-net income efficiency over 252d window."""
    res = _z(_slope_pct(_ratio(netinc, revenue), 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_netinc_mom_z_504d_v201_signal(netinc):
    """Relative momentum strength for Raw level of netinc over 504d window."""
    res = _z(_slope_pct(netinc, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_ebt_mom_z_504d_v202_signal(ebt):
    """Relative momentum strength for Raw level of ebt over 504d window."""
    res = _z(_slope_pct(ebt, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_revenue_mom_z_504d_v203_signal(revenue):
    """Relative momentum strength for Raw level of revenue over 504d window."""
    res = _z(_slope_pct(revenue, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_provision_drag_mom_z_504d_v204_signal(ebt, netinc, revenue):
    """Relative momentum strength for Provisioning and load proxy over 504d window."""
    res = _z(_slope_pct(_ratio(ebt - netinc, revenue), 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_net_margin_mom_z_504d_v205_signal(netinc, revenue):
    """Relative momentum strength for Revenue-to-net income efficiency over 504d window."""
    res = _z(_slope_pct(_ratio(netinc, revenue), 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_netinc_mom_z_756d_v206_signal(netinc):
    """Relative momentum strength for Raw level of netinc over 756d window."""
    res = _z(_slope_pct(netinc, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_ebt_mom_z_756d_v207_signal(ebt):
    """Relative momentum strength for Raw level of ebt over 756d window."""
    res = _z(_slope_pct(ebt, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_revenue_mom_z_756d_v208_signal(revenue):
    """Relative momentum strength for Raw level of revenue over 756d window."""
    res = _z(_slope_pct(revenue, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_provision_drag_mom_z_756d_v209_signal(ebt, netinc, revenue):
    """Relative momentum strength for Provisioning and load proxy over 756d window."""
    res = _z(_slope_pct(_ratio(ebt - netinc, revenue), 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_net_margin_mom_z_756d_v210_signal(netinc, revenue):
    """Relative momentum strength for Revenue-to-net income efficiency over 756d window."""
    res = _z(_slope_pct(_ratio(netinc, revenue), 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_netinc_mom_z_1008d_v211_signal(netinc):
    """Relative momentum strength for Raw level of netinc over 1008d window."""
    res = _z(_slope_pct(netinc, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_ebt_mom_z_1008d_v212_signal(ebt):
    """Relative momentum strength for Raw level of ebt over 1008d window."""
    res = _z(_slope_pct(ebt, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_revenue_mom_z_1008d_v213_signal(revenue):
    """Relative momentum strength for Raw level of revenue over 1008d window."""
    res = _z(_slope_pct(revenue, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_provision_drag_mom_z_1008d_v214_signal(ebt, netinc, revenue):
    """Relative momentum strength for Provisioning and load proxy over 1008d window."""
    res = _z(_slope_pct(_ratio(ebt - netinc, revenue), 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_net_margin_mom_z_1008d_v215_signal(netinc, revenue):
    """Relative momentum strength for Revenue-to-net income efficiency over 1008d window."""
    res = _z(_slope_pct(_ratio(netinc, revenue), 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_netinc_mom_z_1260d_v216_signal(netinc):
    """Relative momentum strength for Raw level of netinc over 1260d window."""
    res = _z(_slope_pct(netinc, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_ebt_mom_z_1260d_v217_signal(ebt):
    """Relative momentum strength for Raw level of ebt over 1260d window."""
    res = _z(_slope_pct(ebt, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_revenue_mom_z_1260d_v218_signal(revenue):
    """Relative momentum strength for Raw level of revenue over 1260d window."""
    res = _z(_slope_pct(revenue, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_provision_drag_mom_z_1260d_v219_signal(ebt, netinc, revenue):
    """Relative momentum strength for Provisioning and load proxy over 1260d window."""
    res = _z(_slope_pct(_ratio(ebt - netinc, revenue), 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_net_margin_mom_z_1260d_v220_signal(netinc, revenue):
    """Relative momentum strength for Revenue-to-net income efficiency over 1260d window."""
    res = _z(_slope_pct(_ratio(netinc, revenue), 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_netinc_vol_slope_5d_v221_signal(netinc):
    """Volatility of momentum for Raw level of netinc over 5d window."""
    res = _std(_slope_pct(netinc, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_ebt_vol_slope_5d_v222_signal(ebt):
    """Volatility of momentum for Raw level of ebt over 5d window."""
    res = _std(_slope_pct(ebt, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_revenue_vol_slope_5d_v223_signal(revenue):
    """Volatility of momentum for Raw level of revenue over 5d window."""
    res = _std(_slope_pct(revenue, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_provision_drag_vol_slope_5d_v224_signal(ebt, netinc, revenue):
    """Volatility of momentum for Provisioning and load proxy over 5d window."""
    res = _std(_slope_pct(_ratio(ebt - netinc, revenue), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_net_margin_vol_slope_5d_v225_signal(netinc, revenue):
    """Volatility of momentum for Revenue-to-net income efficiency over 5d window."""
    res = _std(_slope_pct(_ratio(netinc, revenue), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_netinc_vol_slope_10d_v226_signal(netinc):
    """Volatility of momentum for Raw level of netinc over 10d window."""
    res = _std(_slope_pct(netinc, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_ebt_vol_slope_10d_v227_signal(ebt):
    """Volatility of momentum for Raw level of ebt over 10d window."""
    res = _std(_slope_pct(ebt, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_revenue_vol_slope_10d_v228_signal(revenue):
    """Volatility of momentum for Raw level of revenue over 10d window."""
    res = _std(_slope_pct(revenue, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_provision_drag_vol_slope_10d_v229_signal(ebt, netinc, revenue):
    """Volatility of momentum for Provisioning and load proxy over 10d window."""
    res = _std(_slope_pct(_ratio(ebt - netinc, revenue), 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_net_margin_vol_slope_10d_v230_signal(netinc, revenue):
    """Volatility of momentum for Revenue-to-net income efficiency over 10d window."""
    res = _std(_slope_pct(_ratio(netinc, revenue), 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_netinc_vol_slope_21d_v231_signal(netinc):
    """Volatility of momentum for Raw level of netinc over 21d window."""
    res = _std(_slope_pct(netinc, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_ebt_vol_slope_21d_v232_signal(ebt):
    """Volatility of momentum for Raw level of ebt over 21d window."""
    res = _std(_slope_pct(ebt, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_revenue_vol_slope_21d_v233_signal(revenue):
    """Volatility of momentum for Raw level of revenue over 21d window."""
    res = _std(_slope_pct(revenue, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_provision_drag_vol_slope_21d_v234_signal(ebt, netinc, revenue):
    """Volatility of momentum for Provisioning and load proxy over 21d window."""
    res = _std(_slope_pct(_ratio(ebt - netinc, revenue), 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_net_margin_vol_slope_21d_v235_signal(netinc, revenue):
    """Volatility of momentum for Revenue-to-net income efficiency over 21d window."""
    res = _std(_slope_pct(_ratio(netinc, revenue), 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_netinc_vol_slope_42d_v236_signal(netinc):
    """Volatility of momentum for Raw level of netinc over 42d window."""
    res = _std(_slope_pct(netinc, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_ebt_vol_slope_42d_v237_signal(ebt):
    """Volatility of momentum for Raw level of ebt over 42d window."""
    res = _std(_slope_pct(ebt, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_revenue_vol_slope_42d_v238_signal(revenue):
    """Volatility of momentum for Raw level of revenue over 42d window."""
    res = _std(_slope_pct(revenue, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_provision_drag_vol_slope_42d_v239_signal(ebt, netinc, revenue):
    """Volatility of momentum for Provisioning and load proxy over 42d window."""
    res = _std(_slope_pct(_ratio(ebt - netinc, revenue), 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_net_margin_vol_slope_42d_v240_signal(netinc, revenue):
    """Volatility of momentum for Revenue-to-net income efficiency over 42d window."""
    res = _std(_slope_pct(_ratio(netinc, revenue), 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_netinc_vol_slope_63d_v241_signal(netinc):
    """Volatility of momentum for Raw level of netinc over 63d window."""
    res = _std(_slope_pct(netinc, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_ebt_vol_slope_63d_v242_signal(ebt):
    """Volatility of momentum for Raw level of ebt over 63d window."""
    res = _std(_slope_pct(ebt, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_revenue_vol_slope_63d_v243_signal(revenue):
    """Volatility of momentum for Raw level of revenue over 63d window."""
    res = _std(_slope_pct(revenue, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_provision_drag_vol_slope_63d_v244_signal(ebt, netinc, revenue):
    """Volatility of momentum for Provisioning and load proxy over 63d window."""
    res = _std(_slope_pct(_ratio(ebt - netinc, revenue), 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_net_margin_vol_slope_63d_v245_signal(netinc, revenue):
    """Volatility of momentum for Revenue-to-net income efficiency over 63d window."""
    res = _std(_slope_pct(_ratio(netinc, revenue), 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_netinc_vol_slope_126d_v246_signal(netinc):
    """Volatility of momentum for Raw level of netinc over 126d window."""
    res = _std(_slope_pct(netinc, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_ebt_vol_slope_126d_v247_signal(ebt):
    """Volatility of momentum for Raw level of ebt over 126d window."""
    res = _std(_slope_pct(ebt, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_revenue_vol_slope_126d_v248_signal(revenue):
    """Volatility of momentum for Raw level of revenue over 126d window."""
    res = _std(_slope_pct(revenue, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_provision_drag_vol_slope_126d_v249_signal(ebt, netinc, revenue):
    """Volatility of momentum for Provisioning and load proxy over 126d window."""
    res = _std(_slope_pct(_ratio(ebt - netinc, revenue), 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_net_margin_vol_slope_126d_v250_signal(netinc, revenue):
    """Volatility of momentum for Revenue-to-net income efficiency over 126d window."""
    res = _std(_slope_pct(_ratio(netinc, revenue), 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_netinc_vol_slope_252d_v251_signal(netinc):
    """Volatility of momentum for Raw level of netinc over 252d window."""
    res = _std(_slope_pct(netinc, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_ebt_vol_slope_252d_v252_signal(ebt):
    """Volatility of momentum for Raw level of ebt over 252d window."""
    res = _std(_slope_pct(ebt, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_revenue_vol_slope_252d_v253_signal(revenue):
    """Volatility of momentum for Raw level of revenue over 252d window."""
    res = _std(_slope_pct(revenue, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_provision_drag_vol_slope_252d_v254_signal(ebt, netinc, revenue):
    """Volatility of momentum for Provisioning and load proxy over 252d window."""
    res = _std(_slope_pct(_ratio(ebt - netinc, revenue), 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_net_margin_vol_slope_252d_v255_signal(netinc, revenue):
    """Volatility of momentum for Revenue-to-net income efficiency over 252d window."""
    res = _std(_slope_pct(_ratio(netinc, revenue), 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_netinc_vol_slope_504d_v256_signal(netinc):
    """Volatility of momentum for Raw level of netinc over 504d window."""
    res = _std(_slope_pct(netinc, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_ebt_vol_slope_504d_v257_signal(ebt):
    """Volatility of momentum for Raw level of ebt over 504d window."""
    res = _std(_slope_pct(ebt, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_revenue_vol_slope_504d_v258_signal(revenue):
    """Volatility of momentum for Raw level of revenue over 504d window."""
    res = _std(_slope_pct(revenue, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_provision_drag_vol_slope_504d_v259_signal(ebt, netinc, revenue):
    """Volatility of momentum for Provisioning and load proxy over 504d window."""
    res = _std(_slope_pct(_ratio(ebt - netinc, revenue), 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_net_margin_vol_slope_504d_v260_signal(netinc, revenue):
    """Volatility of momentum for Revenue-to-net income efficiency over 504d window."""
    res = _std(_slope_pct(_ratio(netinc, revenue), 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_netinc_vol_slope_756d_v261_signal(netinc):
    """Volatility of momentum for Raw level of netinc over 756d window."""
    res = _std(_slope_pct(netinc, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_ebt_vol_slope_756d_v262_signal(ebt):
    """Volatility of momentum for Raw level of ebt over 756d window."""
    res = _std(_slope_pct(ebt, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_revenue_vol_slope_756d_v263_signal(revenue):
    """Volatility of momentum for Raw level of revenue over 756d window."""
    res = _std(_slope_pct(revenue, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_provision_drag_vol_slope_756d_v264_signal(ebt, netinc, revenue):
    """Volatility of momentum for Provisioning and load proxy over 756d window."""
    res = _std(_slope_pct(_ratio(ebt - netinc, revenue), 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_net_margin_vol_slope_756d_v265_signal(netinc, revenue):
    """Volatility of momentum for Revenue-to-net income efficiency over 756d window."""
    res = _std(_slope_pct(_ratio(netinc, revenue), 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_netinc_vol_slope_1008d_v266_signal(netinc):
    """Volatility of momentum for Raw level of netinc over 1008d window."""
    res = _std(_slope_pct(netinc, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_ebt_vol_slope_1008d_v267_signal(ebt):
    """Volatility of momentum for Raw level of ebt over 1008d window."""
    res = _std(_slope_pct(ebt, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_revenue_vol_slope_1008d_v268_signal(revenue):
    """Volatility of momentum for Raw level of revenue over 1008d window."""
    res = _std(_slope_pct(revenue, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_provision_drag_vol_slope_1008d_v269_signal(ebt, netinc, revenue):
    """Volatility of momentum for Provisioning and load proxy over 1008d window."""
    res = _std(_slope_pct(_ratio(ebt - netinc, revenue), 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_net_margin_vol_slope_1008d_v270_signal(netinc, revenue):
    """Volatility of momentum for Revenue-to-net income efficiency over 1008d window."""
    res = _std(_slope_pct(_ratio(netinc, revenue), 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_netinc_vol_slope_1260d_v271_signal(netinc):
    """Volatility of momentum for Raw level of netinc over 1260d window."""
    res = _std(_slope_pct(netinc, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_ebt_vol_slope_1260d_v272_signal(ebt):
    """Volatility of momentum for Raw level of ebt over 1260d window."""
    res = _std(_slope_pct(ebt, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_revenue_vol_slope_1260d_v273_signal(revenue):
    """Volatility of momentum for Raw level of revenue over 1260d window."""
    res = _std(_slope_pct(revenue, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_provision_drag_vol_slope_1260d_v274_signal(ebt, netinc, revenue):
    """Volatility of momentum for Provisioning and load proxy over 1260d window."""
    res = _std(_slope_pct(_ratio(ebt - netinc, revenue), 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_net_margin_vol_slope_1260d_v275_signal(netinc, revenue):
    """Volatility of momentum for Revenue-to-net income efficiency over 1260d window."""
    res = _std(_slope_pct(_ratio(netinc, revenue), 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_netinc_ewma_slope_5d_v276_signal(netinc):
    """Exponential momentum smoothing for Raw level of netinc over 5d window."""
    res = _ewma(_slope_pct(netinc, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_ebt_ewma_slope_5d_v277_signal(ebt):
    """Exponential momentum smoothing for Raw level of ebt over 5d window."""
    res = _ewma(_slope_pct(ebt, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_revenue_ewma_slope_5d_v278_signal(revenue):
    """Exponential momentum smoothing for Raw level of revenue over 5d window."""
    res = _ewma(_slope_pct(revenue, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_provision_drag_ewma_slope_5d_v279_signal(ebt, netinc, revenue):
    """Exponential momentum smoothing for Provisioning and load proxy over 5d window."""
    res = _ewma(_slope_pct(_ratio(ebt - netinc, revenue), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_net_margin_ewma_slope_5d_v280_signal(netinc, revenue):
    """Exponential momentum smoothing for Revenue-to-net income efficiency over 5d window."""
    res = _ewma(_slope_pct(_ratio(netinc, revenue), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_netinc_ewma_slope_10d_v281_signal(netinc):
    """Exponential momentum smoothing for Raw level of netinc over 10d window."""
    res = _ewma(_slope_pct(netinc, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_ebt_ewma_slope_10d_v282_signal(ebt):
    """Exponential momentum smoothing for Raw level of ebt over 10d window."""
    res = _ewma(_slope_pct(ebt, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_revenue_ewma_slope_10d_v283_signal(revenue):
    """Exponential momentum smoothing for Raw level of revenue over 10d window."""
    res = _ewma(_slope_pct(revenue, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_provision_drag_ewma_slope_10d_v284_signal(ebt, netinc, revenue):
    """Exponential momentum smoothing for Provisioning and load proxy over 10d window."""
    res = _ewma(_slope_pct(_ratio(ebt - netinc, revenue), 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_net_margin_ewma_slope_10d_v285_signal(netinc, revenue):
    """Exponential momentum smoothing for Revenue-to-net income efficiency over 10d window."""
    res = _ewma(_slope_pct(_ratio(netinc, revenue), 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_netinc_ewma_slope_21d_v286_signal(netinc):
    """Exponential momentum smoothing for Raw level of netinc over 21d window."""
    res = _ewma(_slope_pct(netinc, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_ebt_ewma_slope_21d_v287_signal(ebt):
    """Exponential momentum smoothing for Raw level of ebt over 21d window."""
    res = _ewma(_slope_pct(ebt, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_revenue_ewma_slope_21d_v288_signal(revenue):
    """Exponential momentum smoothing for Raw level of revenue over 21d window."""
    res = _ewma(_slope_pct(revenue, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_provision_drag_ewma_slope_21d_v289_signal(ebt, netinc, revenue):
    """Exponential momentum smoothing for Provisioning and load proxy over 21d window."""
    res = _ewma(_slope_pct(_ratio(ebt - netinc, revenue), 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_net_margin_ewma_slope_21d_v290_signal(netinc, revenue):
    """Exponential momentum smoothing for Revenue-to-net income efficiency over 21d window."""
    res = _ewma(_slope_pct(_ratio(netinc, revenue), 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_netinc_ewma_slope_42d_v291_signal(netinc):
    """Exponential momentum smoothing for Raw level of netinc over 42d window."""
    res = _ewma(_slope_pct(netinc, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_ebt_ewma_slope_42d_v292_signal(ebt):
    """Exponential momentum smoothing for Raw level of ebt over 42d window."""
    res = _ewma(_slope_pct(ebt, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_revenue_ewma_slope_42d_v293_signal(revenue):
    """Exponential momentum smoothing for Raw level of revenue over 42d window."""
    res = _ewma(_slope_pct(revenue, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_provision_drag_ewma_slope_42d_v294_signal(ebt, netinc, revenue):
    """Exponential momentum smoothing for Provisioning and load proxy over 42d window."""
    res = _ewma(_slope_pct(_ratio(ebt - netinc, revenue), 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_net_margin_ewma_slope_42d_v295_signal(netinc, revenue):
    """Exponential momentum smoothing for Revenue-to-net income efficiency over 42d window."""
    res = _ewma(_slope_pct(_ratio(netinc, revenue), 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_netinc_ewma_slope_63d_v296_signal(netinc):
    """Exponential momentum smoothing for Raw level of netinc over 63d window."""
    res = _ewma(_slope_pct(netinc, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_ebt_ewma_slope_63d_v297_signal(ebt):
    """Exponential momentum smoothing for Raw level of ebt over 63d window."""
    res = _ewma(_slope_pct(ebt, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_revenue_ewma_slope_63d_v298_signal(revenue):
    """Exponential momentum smoothing for Raw level of revenue over 63d window."""
    res = _ewma(_slope_pct(revenue, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_provision_drag_ewma_slope_63d_v299_signal(ebt, netinc, revenue):
    """Exponential momentum smoothing for Provisioning and load proxy over 63d window."""
    res = _ewma(_slope_pct(_ratio(ebt - netinc, revenue), 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_net_margin_ewma_slope_63d_v300_signal(netinc, revenue):
    """Exponential momentum smoothing for Revenue-to-net income efficiency over 63d window."""
    res = _ewma(_slope_pct(_ratio(netinc, revenue), 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)


# ===== Feature Registry =====
REGISTRY = {
    "f06_loan_quality_netinc_slope_diff_norm_756d_v151_signal": {"func": f06_loan_quality_netinc_slope_diff_norm_756d_v151_signal},
    "f06_loan_quality_ebt_slope_diff_norm_756d_v152_signal": {"func": f06_loan_quality_ebt_slope_diff_norm_756d_v152_signal},
    "f06_loan_quality_revenue_slope_diff_norm_756d_v153_signal": {"func": f06_loan_quality_revenue_slope_diff_norm_756d_v153_signal},
    "f06_loan_quality_provision_drag_slope_diff_norm_756d_v154_signal": {"func": f06_loan_quality_provision_drag_slope_diff_norm_756d_v154_signal},
    "f06_loan_quality_net_margin_slope_diff_norm_756d_v155_signal": {"func": f06_loan_quality_net_margin_slope_diff_norm_756d_v155_signal},
    "f06_loan_quality_netinc_slope_diff_norm_1008d_v156_signal": {"func": f06_loan_quality_netinc_slope_diff_norm_1008d_v156_signal},
    "f06_loan_quality_ebt_slope_diff_norm_1008d_v157_signal": {"func": f06_loan_quality_ebt_slope_diff_norm_1008d_v157_signal},
    "f06_loan_quality_revenue_slope_diff_norm_1008d_v158_signal": {"func": f06_loan_quality_revenue_slope_diff_norm_1008d_v158_signal},
    "f06_loan_quality_provision_drag_slope_diff_norm_1008d_v159_signal": {"func": f06_loan_quality_provision_drag_slope_diff_norm_1008d_v159_signal},
    "f06_loan_quality_net_margin_slope_diff_norm_1008d_v160_signal": {"func": f06_loan_quality_net_margin_slope_diff_norm_1008d_v160_signal},
    "f06_loan_quality_netinc_slope_diff_norm_1260d_v161_signal": {"func": f06_loan_quality_netinc_slope_diff_norm_1260d_v161_signal},
    "f06_loan_quality_ebt_slope_diff_norm_1260d_v162_signal": {"func": f06_loan_quality_ebt_slope_diff_norm_1260d_v162_signal},
    "f06_loan_quality_revenue_slope_diff_norm_1260d_v163_signal": {"func": f06_loan_quality_revenue_slope_diff_norm_1260d_v163_signal},
    "f06_loan_quality_provision_drag_slope_diff_norm_1260d_v164_signal": {"func": f06_loan_quality_provision_drag_slope_diff_norm_1260d_v164_signal},
    "f06_loan_quality_net_margin_slope_diff_norm_1260d_v165_signal": {"func": f06_loan_quality_net_margin_slope_diff_norm_1260d_v165_signal},
    "f06_loan_quality_netinc_mom_z_5d_v166_signal": {"func": f06_loan_quality_netinc_mom_z_5d_v166_signal},
    "f06_loan_quality_ebt_mom_z_5d_v167_signal": {"func": f06_loan_quality_ebt_mom_z_5d_v167_signal},
    "f06_loan_quality_revenue_mom_z_5d_v168_signal": {"func": f06_loan_quality_revenue_mom_z_5d_v168_signal},
    "f06_loan_quality_provision_drag_mom_z_5d_v169_signal": {"func": f06_loan_quality_provision_drag_mom_z_5d_v169_signal},
    "f06_loan_quality_net_margin_mom_z_5d_v170_signal": {"func": f06_loan_quality_net_margin_mom_z_5d_v170_signal},
    "f06_loan_quality_netinc_mom_z_10d_v171_signal": {"func": f06_loan_quality_netinc_mom_z_10d_v171_signal},
    "f06_loan_quality_ebt_mom_z_10d_v172_signal": {"func": f06_loan_quality_ebt_mom_z_10d_v172_signal},
    "f06_loan_quality_revenue_mom_z_10d_v173_signal": {"func": f06_loan_quality_revenue_mom_z_10d_v173_signal},
    "f06_loan_quality_provision_drag_mom_z_10d_v174_signal": {"func": f06_loan_quality_provision_drag_mom_z_10d_v174_signal},
    "f06_loan_quality_net_margin_mom_z_10d_v175_signal": {"func": f06_loan_quality_net_margin_mom_z_10d_v175_signal},
    "f06_loan_quality_netinc_mom_z_21d_v176_signal": {"func": f06_loan_quality_netinc_mom_z_21d_v176_signal},
    "f06_loan_quality_ebt_mom_z_21d_v177_signal": {"func": f06_loan_quality_ebt_mom_z_21d_v177_signal},
    "f06_loan_quality_revenue_mom_z_21d_v178_signal": {"func": f06_loan_quality_revenue_mom_z_21d_v178_signal},
    "f06_loan_quality_provision_drag_mom_z_21d_v179_signal": {"func": f06_loan_quality_provision_drag_mom_z_21d_v179_signal},
    "f06_loan_quality_net_margin_mom_z_21d_v180_signal": {"func": f06_loan_quality_net_margin_mom_z_21d_v180_signal},
    "f06_loan_quality_netinc_mom_z_42d_v181_signal": {"func": f06_loan_quality_netinc_mom_z_42d_v181_signal},
    "f06_loan_quality_ebt_mom_z_42d_v182_signal": {"func": f06_loan_quality_ebt_mom_z_42d_v182_signal},
    "f06_loan_quality_revenue_mom_z_42d_v183_signal": {"func": f06_loan_quality_revenue_mom_z_42d_v183_signal},
    "f06_loan_quality_provision_drag_mom_z_42d_v184_signal": {"func": f06_loan_quality_provision_drag_mom_z_42d_v184_signal},
    "f06_loan_quality_net_margin_mom_z_42d_v185_signal": {"func": f06_loan_quality_net_margin_mom_z_42d_v185_signal},
    "f06_loan_quality_netinc_mom_z_63d_v186_signal": {"func": f06_loan_quality_netinc_mom_z_63d_v186_signal},
    "f06_loan_quality_ebt_mom_z_63d_v187_signal": {"func": f06_loan_quality_ebt_mom_z_63d_v187_signal},
    "f06_loan_quality_revenue_mom_z_63d_v188_signal": {"func": f06_loan_quality_revenue_mom_z_63d_v188_signal},
    "f06_loan_quality_provision_drag_mom_z_63d_v189_signal": {"func": f06_loan_quality_provision_drag_mom_z_63d_v189_signal},
    "f06_loan_quality_net_margin_mom_z_63d_v190_signal": {"func": f06_loan_quality_net_margin_mom_z_63d_v190_signal},
    "f06_loan_quality_netinc_mom_z_126d_v191_signal": {"func": f06_loan_quality_netinc_mom_z_126d_v191_signal},
    "f06_loan_quality_ebt_mom_z_126d_v192_signal": {"func": f06_loan_quality_ebt_mom_z_126d_v192_signal},
    "f06_loan_quality_revenue_mom_z_126d_v193_signal": {"func": f06_loan_quality_revenue_mom_z_126d_v193_signal},
    "f06_loan_quality_provision_drag_mom_z_126d_v194_signal": {"func": f06_loan_quality_provision_drag_mom_z_126d_v194_signal},
    "f06_loan_quality_net_margin_mom_z_126d_v195_signal": {"func": f06_loan_quality_net_margin_mom_z_126d_v195_signal},
    "f06_loan_quality_netinc_mom_z_252d_v196_signal": {"func": f06_loan_quality_netinc_mom_z_252d_v196_signal},
    "f06_loan_quality_ebt_mom_z_252d_v197_signal": {"func": f06_loan_quality_ebt_mom_z_252d_v197_signal},
    "f06_loan_quality_revenue_mom_z_252d_v198_signal": {"func": f06_loan_quality_revenue_mom_z_252d_v198_signal},
    "f06_loan_quality_provision_drag_mom_z_252d_v199_signal": {"func": f06_loan_quality_provision_drag_mom_z_252d_v199_signal},
    "f06_loan_quality_net_margin_mom_z_252d_v200_signal": {"func": f06_loan_quality_net_margin_mom_z_252d_v200_signal},
    "f06_loan_quality_netinc_mom_z_504d_v201_signal": {"func": f06_loan_quality_netinc_mom_z_504d_v201_signal},
    "f06_loan_quality_ebt_mom_z_504d_v202_signal": {"func": f06_loan_quality_ebt_mom_z_504d_v202_signal},
    "f06_loan_quality_revenue_mom_z_504d_v203_signal": {"func": f06_loan_quality_revenue_mom_z_504d_v203_signal},
    "f06_loan_quality_provision_drag_mom_z_504d_v204_signal": {"func": f06_loan_quality_provision_drag_mom_z_504d_v204_signal},
    "f06_loan_quality_net_margin_mom_z_504d_v205_signal": {"func": f06_loan_quality_net_margin_mom_z_504d_v205_signal},
    "f06_loan_quality_netinc_mom_z_756d_v206_signal": {"func": f06_loan_quality_netinc_mom_z_756d_v206_signal},
    "f06_loan_quality_ebt_mom_z_756d_v207_signal": {"func": f06_loan_quality_ebt_mom_z_756d_v207_signal},
    "f06_loan_quality_revenue_mom_z_756d_v208_signal": {"func": f06_loan_quality_revenue_mom_z_756d_v208_signal},
    "f06_loan_quality_provision_drag_mom_z_756d_v209_signal": {"func": f06_loan_quality_provision_drag_mom_z_756d_v209_signal},
    "f06_loan_quality_net_margin_mom_z_756d_v210_signal": {"func": f06_loan_quality_net_margin_mom_z_756d_v210_signal},
    "f06_loan_quality_netinc_mom_z_1008d_v211_signal": {"func": f06_loan_quality_netinc_mom_z_1008d_v211_signal},
    "f06_loan_quality_ebt_mom_z_1008d_v212_signal": {"func": f06_loan_quality_ebt_mom_z_1008d_v212_signal},
    "f06_loan_quality_revenue_mom_z_1008d_v213_signal": {"func": f06_loan_quality_revenue_mom_z_1008d_v213_signal},
    "f06_loan_quality_provision_drag_mom_z_1008d_v214_signal": {"func": f06_loan_quality_provision_drag_mom_z_1008d_v214_signal},
    "f06_loan_quality_net_margin_mom_z_1008d_v215_signal": {"func": f06_loan_quality_net_margin_mom_z_1008d_v215_signal},
    "f06_loan_quality_netinc_mom_z_1260d_v216_signal": {"func": f06_loan_quality_netinc_mom_z_1260d_v216_signal},
    "f06_loan_quality_ebt_mom_z_1260d_v217_signal": {"func": f06_loan_quality_ebt_mom_z_1260d_v217_signal},
    "f06_loan_quality_revenue_mom_z_1260d_v218_signal": {"func": f06_loan_quality_revenue_mom_z_1260d_v218_signal},
    "f06_loan_quality_provision_drag_mom_z_1260d_v219_signal": {"func": f06_loan_quality_provision_drag_mom_z_1260d_v219_signal},
    "f06_loan_quality_net_margin_mom_z_1260d_v220_signal": {"func": f06_loan_quality_net_margin_mom_z_1260d_v220_signal},
    "f06_loan_quality_netinc_vol_slope_5d_v221_signal": {"func": f06_loan_quality_netinc_vol_slope_5d_v221_signal},
    "f06_loan_quality_ebt_vol_slope_5d_v222_signal": {"func": f06_loan_quality_ebt_vol_slope_5d_v222_signal},
    "f06_loan_quality_revenue_vol_slope_5d_v223_signal": {"func": f06_loan_quality_revenue_vol_slope_5d_v223_signal},
    "f06_loan_quality_provision_drag_vol_slope_5d_v224_signal": {"func": f06_loan_quality_provision_drag_vol_slope_5d_v224_signal},
    "f06_loan_quality_net_margin_vol_slope_5d_v225_signal": {"func": f06_loan_quality_net_margin_vol_slope_5d_v225_signal},
    "f06_loan_quality_netinc_vol_slope_10d_v226_signal": {"func": f06_loan_quality_netinc_vol_slope_10d_v226_signal},
    "f06_loan_quality_ebt_vol_slope_10d_v227_signal": {"func": f06_loan_quality_ebt_vol_slope_10d_v227_signal},
    "f06_loan_quality_revenue_vol_slope_10d_v228_signal": {"func": f06_loan_quality_revenue_vol_slope_10d_v228_signal},
    "f06_loan_quality_provision_drag_vol_slope_10d_v229_signal": {"func": f06_loan_quality_provision_drag_vol_slope_10d_v229_signal},
    "f06_loan_quality_net_margin_vol_slope_10d_v230_signal": {"func": f06_loan_quality_net_margin_vol_slope_10d_v230_signal},
    "f06_loan_quality_netinc_vol_slope_21d_v231_signal": {"func": f06_loan_quality_netinc_vol_slope_21d_v231_signal},
    "f06_loan_quality_ebt_vol_slope_21d_v232_signal": {"func": f06_loan_quality_ebt_vol_slope_21d_v232_signal},
    "f06_loan_quality_revenue_vol_slope_21d_v233_signal": {"func": f06_loan_quality_revenue_vol_slope_21d_v233_signal},
    "f06_loan_quality_provision_drag_vol_slope_21d_v234_signal": {"func": f06_loan_quality_provision_drag_vol_slope_21d_v234_signal},
    "f06_loan_quality_net_margin_vol_slope_21d_v235_signal": {"func": f06_loan_quality_net_margin_vol_slope_21d_v235_signal},
    "f06_loan_quality_netinc_vol_slope_42d_v236_signal": {"func": f06_loan_quality_netinc_vol_slope_42d_v236_signal},
    "f06_loan_quality_ebt_vol_slope_42d_v237_signal": {"func": f06_loan_quality_ebt_vol_slope_42d_v237_signal},
    "f06_loan_quality_revenue_vol_slope_42d_v238_signal": {"func": f06_loan_quality_revenue_vol_slope_42d_v238_signal},
    "f06_loan_quality_provision_drag_vol_slope_42d_v239_signal": {"func": f06_loan_quality_provision_drag_vol_slope_42d_v239_signal},
    "f06_loan_quality_net_margin_vol_slope_42d_v240_signal": {"func": f06_loan_quality_net_margin_vol_slope_42d_v240_signal},
    "f06_loan_quality_netinc_vol_slope_63d_v241_signal": {"func": f06_loan_quality_netinc_vol_slope_63d_v241_signal},
    "f06_loan_quality_ebt_vol_slope_63d_v242_signal": {"func": f06_loan_quality_ebt_vol_slope_63d_v242_signal},
    "f06_loan_quality_revenue_vol_slope_63d_v243_signal": {"func": f06_loan_quality_revenue_vol_slope_63d_v243_signal},
    "f06_loan_quality_provision_drag_vol_slope_63d_v244_signal": {"func": f06_loan_quality_provision_drag_vol_slope_63d_v244_signal},
    "f06_loan_quality_net_margin_vol_slope_63d_v245_signal": {"func": f06_loan_quality_net_margin_vol_slope_63d_v245_signal},
    "f06_loan_quality_netinc_vol_slope_126d_v246_signal": {"func": f06_loan_quality_netinc_vol_slope_126d_v246_signal},
    "f06_loan_quality_ebt_vol_slope_126d_v247_signal": {"func": f06_loan_quality_ebt_vol_slope_126d_v247_signal},
    "f06_loan_quality_revenue_vol_slope_126d_v248_signal": {"func": f06_loan_quality_revenue_vol_slope_126d_v248_signal},
    "f06_loan_quality_provision_drag_vol_slope_126d_v249_signal": {"func": f06_loan_quality_provision_drag_vol_slope_126d_v249_signal},
    "f06_loan_quality_net_margin_vol_slope_126d_v250_signal": {"func": f06_loan_quality_net_margin_vol_slope_126d_v250_signal},
    "f06_loan_quality_netinc_vol_slope_252d_v251_signal": {"func": f06_loan_quality_netinc_vol_slope_252d_v251_signal},
    "f06_loan_quality_ebt_vol_slope_252d_v252_signal": {"func": f06_loan_quality_ebt_vol_slope_252d_v252_signal},
    "f06_loan_quality_revenue_vol_slope_252d_v253_signal": {"func": f06_loan_quality_revenue_vol_slope_252d_v253_signal},
    "f06_loan_quality_provision_drag_vol_slope_252d_v254_signal": {"func": f06_loan_quality_provision_drag_vol_slope_252d_v254_signal},
    "f06_loan_quality_net_margin_vol_slope_252d_v255_signal": {"func": f06_loan_quality_net_margin_vol_slope_252d_v255_signal},
    "f06_loan_quality_netinc_vol_slope_504d_v256_signal": {"func": f06_loan_quality_netinc_vol_slope_504d_v256_signal},
    "f06_loan_quality_ebt_vol_slope_504d_v257_signal": {"func": f06_loan_quality_ebt_vol_slope_504d_v257_signal},
    "f06_loan_quality_revenue_vol_slope_504d_v258_signal": {"func": f06_loan_quality_revenue_vol_slope_504d_v258_signal},
    "f06_loan_quality_provision_drag_vol_slope_504d_v259_signal": {"func": f06_loan_quality_provision_drag_vol_slope_504d_v259_signal},
    "f06_loan_quality_net_margin_vol_slope_504d_v260_signal": {"func": f06_loan_quality_net_margin_vol_slope_504d_v260_signal},
    "f06_loan_quality_netinc_vol_slope_756d_v261_signal": {"func": f06_loan_quality_netinc_vol_slope_756d_v261_signal},
    "f06_loan_quality_ebt_vol_slope_756d_v262_signal": {"func": f06_loan_quality_ebt_vol_slope_756d_v262_signal},
    "f06_loan_quality_revenue_vol_slope_756d_v263_signal": {"func": f06_loan_quality_revenue_vol_slope_756d_v263_signal},
    "f06_loan_quality_provision_drag_vol_slope_756d_v264_signal": {"func": f06_loan_quality_provision_drag_vol_slope_756d_v264_signal},
    "f06_loan_quality_net_margin_vol_slope_756d_v265_signal": {"func": f06_loan_quality_net_margin_vol_slope_756d_v265_signal},
    "f06_loan_quality_netinc_vol_slope_1008d_v266_signal": {"func": f06_loan_quality_netinc_vol_slope_1008d_v266_signal},
    "f06_loan_quality_ebt_vol_slope_1008d_v267_signal": {"func": f06_loan_quality_ebt_vol_slope_1008d_v267_signal},
    "f06_loan_quality_revenue_vol_slope_1008d_v268_signal": {"func": f06_loan_quality_revenue_vol_slope_1008d_v268_signal},
    "f06_loan_quality_provision_drag_vol_slope_1008d_v269_signal": {"func": f06_loan_quality_provision_drag_vol_slope_1008d_v269_signal},
    "f06_loan_quality_net_margin_vol_slope_1008d_v270_signal": {"func": f06_loan_quality_net_margin_vol_slope_1008d_v270_signal},
    "f06_loan_quality_netinc_vol_slope_1260d_v271_signal": {"func": f06_loan_quality_netinc_vol_slope_1260d_v271_signal},
    "f06_loan_quality_ebt_vol_slope_1260d_v272_signal": {"func": f06_loan_quality_ebt_vol_slope_1260d_v272_signal},
    "f06_loan_quality_revenue_vol_slope_1260d_v273_signal": {"func": f06_loan_quality_revenue_vol_slope_1260d_v273_signal},
    "f06_loan_quality_provision_drag_vol_slope_1260d_v274_signal": {"func": f06_loan_quality_provision_drag_vol_slope_1260d_v274_signal},
    "f06_loan_quality_net_margin_vol_slope_1260d_v275_signal": {"func": f06_loan_quality_net_margin_vol_slope_1260d_v275_signal},
    "f06_loan_quality_netinc_ewma_slope_5d_v276_signal": {"func": f06_loan_quality_netinc_ewma_slope_5d_v276_signal},
    "f06_loan_quality_ebt_ewma_slope_5d_v277_signal": {"func": f06_loan_quality_ebt_ewma_slope_5d_v277_signal},
    "f06_loan_quality_revenue_ewma_slope_5d_v278_signal": {"func": f06_loan_quality_revenue_ewma_slope_5d_v278_signal},
    "f06_loan_quality_provision_drag_ewma_slope_5d_v279_signal": {"func": f06_loan_quality_provision_drag_ewma_slope_5d_v279_signal},
    "f06_loan_quality_net_margin_ewma_slope_5d_v280_signal": {"func": f06_loan_quality_net_margin_ewma_slope_5d_v280_signal},
    "f06_loan_quality_netinc_ewma_slope_10d_v281_signal": {"func": f06_loan_quality_netinc_ewma_slope_10d_v281_signal},
    "f06_loan_quality_ebt_ewma_slope_10d_v282_signal": {"func": f06_loan_quality_ebt_ewma_slope_10d_v282_signal},
    "f06_loan_quality_revenue_ewma_slope_10d_v283_signal": {"func": f06_loan_quality_revenue_ewma_slope_10d_v283_signal},
    "f06_loan_quality_provision_drag_ewma_slope_10d_v284_signal": {"func": f06_loan_quality_provision_drag_ewma_slope_10d_v284_signal},
    "f06_loan_quality_net_margin_ewma_slope_10d_v285_signal": {"func": f06_loan_quality_net_margin_ewma_slope_10d_v285_signal},
    "f06_loan_quality_netinc_ewma_slope_21d_v286_signal": {"func": f06_loan_quality_netinc_ewma_slope_21d_v286_signal},
    "f06_loan_quality_ebt_ewma_slope_21d_v287_signal": {"func": f06_loan_quality_ebt_ewma_slope_21d_v287_signal},
    "f06_loan_quality_revenue_ewma_slope_21d_v288_signal": {"func": f06_loan_quality_revenue_ewma_slope_21d_v288_signal},
    "f06_loan_quality_provision_drag_ewma_slope_21d_v289_signal": {"func": f06_loan_quality_provision_drag_ewma_slope_21d_v289_signal},
    "f06_loan_quality_net_margin_ewma_slope_21d_v290_signal": {"func": f06_loan_quality_net_margin_ewma_slope_21d_v290_signal},
    "f06_loan_quality_netinc_ewma_slope_42d_v291_signal": {"func": f06_loan_quality_netinc_ewma_slope_42d_v291_signal},
    "f06_loan_quality_ebt_ewma_slope_42d_v292_signal": {"func": f06_loan_quality_ebt_ewma_slope_42d_v292_signal},
    "f06_loan_quality_revenue_ewma_slope_42d_v293_signal": {"func": f06_loan_quality_revenue_ewma_slope_42d_v293_signal},
    "f06_loan_quality_provision_drag_ewma_slope_42d_v294_signal": {"func": f06_loan_quality_provision_drag_ewma_slope_42d_v294_signal},
    "f06_loan_quality_net_margin_ewma_slope_42d_v295_signal": {"func": f06_loan_quality_net_margin_ewma_slope_42d_v295_signal},
    "f06_loan_quality_netinc_ewma_slope_63d_v296_signal": {"func": f06_loan_quality_netinc_ewma_slope_63d_v296_signal},
    "f06_loan_quality_ebt_ewma_slope_63d_v297_signal": {"func": f06_loan_quality_ebt_ewma_slope_63d_v297_signal},
    "f06_loan_quality_revenue_ewma_slope_63d_v298_signal": {"func": f06_loan_quality_revenue_ewma_slope_63d_v298_signal},
    "f06_loan_quality_provision_drag_ewma_slope_63d_v299_signal": {"func": f06_loan_quality_provision_drag_ewma_slope_63d_v299_signal},
    "f06_loan_quality_net_margin_ewma_slope_63d_v300_signal": {"func": f06_loan_quality_net_margin_ewma_slope_63d_v300_signal},
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
