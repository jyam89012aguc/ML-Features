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

def f03_brand_momentum_revenue_z_63d_v076_signal(revenue):
    """Z-score for relative outlier detection of Raw level of revenue over 63d window."""
    res = _z(revenue, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_sgna_z_63d_v077_signal(sgna):
    """Z-score for relative outlier detection of Raw level of sgna over 63d window."""
    res = _z(sgna, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_marketcap_z_63d_v078_signal(marketcap):
    """Z-score for relative outlier detection of Raw level of marketcap over 63d window."""
    res = _z(marketcap, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_brand_leverage_z_63d_v079_signal(revenue, sgna):
    """Z-score for relative outlier detection of Sales generated per dollar of marketing/admin over 63d window."""
    res = _z(_ratio(revenue, sgna), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_mkt_cap_per_rev_z_63d_v080_signal(marketcap, revenue):
    """Z-score for relative outlier detection of Valuation ascribed per unit of sales over 63d window."""
    res = _z(_ratio(marketcap, revenue), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_revenue_z_126d_v081_signal(revenue):
    """Z-score for relative outlier detection of Raw level of revenue over 126d window."""
    res = _z(revenue, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_sgna_z_126d_v082_signal(sgna):
    """Z-score for relative outlier detection of Raw level of sgna over 126d window."""
    res = _z(sgna, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_marketcap_z_126d_v083_signal(marketcap):
    """Z-score for relative outlier detection of Raw level of marketcap over 126d window."""
    res = _z(marketcap, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_brand_leverage_z_126d_v084_signal(revenue, sgna):
    """Z-score for relative outlier detection of Sales generated per dollar of marketing/admin over 126d window."""
    res = _z(_ratio(revenue, sgna), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_mkt_cap_per_rev_z_126d_v085_signal(marketcap, revenue):
    """Z-score for relative outlier detection of Valuation ascribed per unit of sales over 126d window."""
    res = _z(_ratio(marketcap, revenue), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_revenue_z_252d_v086_signal(revenue):
    """Z-score for relative outlier detection of Raw level of revenue over 252d window."""
    res = _z(revenue, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_sgna_z_252d_v087_signal(sgna):
    """Z-score for relative outlier detection of Raw level of sgna over 252d window."""
    res = _z(sgna, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_marketcap_z_252d_v088_signal(marketcap):
    """Z-score for relative outlier detection of Raw level of marketcap over 252d window."""
    res = _z(marketcap, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_brand_leverage_z_252d_v089_signal(revenue, sgna):
    """Z-score for relative outlier detection of Sales generated per dollar of marketing/admin over 252d window."""
    res = _z(_ratio(revenue, sgna), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_mkt_cap_per_rev_z_252d_v090_signal(marketcap, revenue):
    """Z-score for relative outlier detection of Valuation ascribed per unit of sales over 252d window."""
    res = _z(_ratio(marketcap, revenue), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_revenue_z_504d_v091_signal(revenue):
    """Z-score for relative outlier detection of Raw level of revenue over 504d window."""
    res = _z(revenue, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_sgna_z_504d_v092_signal(sgna):
    """Z-score for relative outlier detection of Raw level of sgna over 504d window."""
    res = _z(sgna, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_marketcap_z_504d_v093_signal(marketcap):
    """Z-score for relative outlier detection of Raw level of marketcap over 504d window."""
    res = _z(marketcap, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_brand_leverage_z_504d_v094_signal(revenue, sgna):
    """Z-score for relative outlier detection of Sales generated per dollar of marketing/admin over 504d window."""
    res = _z(_ratio(revenue, sgna), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_mkt_cap_per_rev_z_504d_v095_signal(marketcap, revenue):
    """Z-score for relative outlier detection of Valuation ascribed per unit of sales over 504d window."""
    res = _z(_ratio(marketcap, revenue), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_revenue_z_756d_v096_signal(revenue):
    """Z-score for relative outlier detection of Raw level of revenue over 756d window."""
    res = _z(revenue, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_sgna_z_756d_v097_signal(sgna):
    """Z-score for relative outlier detection of Raw level of sgna over 756d window."""
    res = _z(sgna, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_marketcap_z_756d_v098_signal(marketcap):
    """Z-score for relative outlier detection of Raw level of marketcap over 756d window."""
    res = _z(marketcap, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_brand_leverage_z_756d_v099_signal(revenue, sgna):
    """Z-score for relative outlier detection of Sales generated per dollar of marketing/admin over 756d window."""
    res = _z(_ratio(revenue, sgna), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_mkt_cap_per_rev_z_756d_v100_signal(marketcap, revenue):
    """Z-score for relative outlier detection of Valuation ascribed per unit of sales over 756d window."""
    res = _z(_ratio(marketcap, revenue), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_revenue_z_1008d_v101_signal(revenue):
    """Z-score for relative outlier detection of Raw level of revenue over 1008d window."""
    res = _z(revenue, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_sgna_z_1008d_v102_signal(sgna):
    """Z-score for relative outlier detection of Raw level of sgna over 1008d window."""
    res = _z(sgna, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_marketcap_z_1008d_v103_signal(marketcap):
    """Z-score for relative outlier detection of Raw level of marketcap over 1008d window."""
    res = _z(marketcap, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_brand_leverage_z_1008d_v104_signal(revenue, sgna):
    """Z-score for relative outlier detection of Sales generated per dollar of marketing/admin over 1008d window."""
    res = _z(_ratio(revenue, sgna), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_mkt_cap_per_rev_z_1008d_v105_signal(marketcap, revenue):
    """Z-score for relative outlier detection of Valuation ascribed per unit of sales over 1008d window."""
    res = _z(_ratio(marketcap, revenue), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_revenue_z_1260d_v106_signal(revenue):
    """Z-score for relative outlier detection of Raw level of revenue over 1260d window."""
    res = _z(revenue, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_sgna_z_1260d_v107_signal(sgna):
    """Z-score for relative outlier detection of Raw level of sgna over 1260d window."""
    res = _z(sgna, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_marketcap_z_1260d_v108_signal(marketcap):
    """Z-score for relative outlier detection of Raw level of marketcap over 1260d window."""
    res = _z(marketcap, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_brand_leverage_z_1260d_v109_signal(revenue, sgna):
    """Z-score for relative outlier detection of Sales generated per dollar of marketing/admin over 1260d window."""
    res = _z(_ratio(revenue, sgna), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_mkt_cap_per_rev_z_1260d_v110_signal(marketcap, revenue):
    """Z-score for relative outlier detection of Valuation ascribed per unit of sales over 1260d window."""
    res = _z(_ratio(marketcap, revenue), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_revenue_dd_5d_v111_signal(revenue):
    """Drawdown from peak to identify cycle troughs of Raw level of revenue over 5d window."""
    res = _drawdown(revenue, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_sgna_dd_5d_v112_signal(sgna):
    """Drawdown from peak to identify cycle troughs of Raw level of sgna over 5d window."""
    res = _drawdown(sgna, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_marketcap_dd_5d_v113_signal(marketcap):
    """Drawdown from peak to identify cycle troughs of Raw level of marketcap over 5d window."""
    res = _drawdown(marketcap, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_brand_leverage_dd_5d_v114_signal(revenue, sgna):
    """Drawdown from peak to identify cycle troughs of Sales generated per dollar of marketing/admin over 5d window."""
    res = _drawdown(_ratio(revenue, sgna), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_mkt_cap_per_rev_dd_5d_v115_signal(marketcap, revenue):
    """Drawdown from peak to identify cycle troughs of Valuation ascribed per unit of sales over 5d window."""
    res = _drawdown(_ratio(marketcap, revenue), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_revenue_dd_10d_v116_signal(revenue):
    """Drawdown from peak to identify cycle troughs of Raw level of revenue over 10d window."""
    res = _drawdown(revenue, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_sgna_dd_10d_v117_signal(sgna):
    """Drawdown from peak to identify cycle troughs of Raw level of sgna over 10d window."""
    res = _drawdown(sgna, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_marketcap_dd_10d_v118_signal(marketcap):
    """Drawdown from peak to identify cycle troughs of Raw level of marketcap over 10d window."""
    res = _drawdown(marketcap, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_brand_leverage_dd_10d_v119_signal(revenue, sgna):
    """Drawdown from peak to identify cycle troughs of Sales generated per dollar of marketing/admin over 10d window."""
    res = _drawdown(_ratio(revenue, sgna), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_mkt_cap_per_rev_dd_10d_v120_signal(marketcap, revenue):
    """Drawdown from peak to identify cycle troughs of Valuation ascribed per unit of sales over 10d window."""
    res = _drawdown(_ratio(marketcap, revenue), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_revenue_dd_21d_v121_signal(revenue):
    """Drawdown from peak to identify cycle troughs of Raw level of revenue over 21d window."""
    res = _drawdown(revenue, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_sgna_dd_21d_v122_signal(sgna):
    """Drawdown from peak to identify cycle troughs of Raw level of sgna over 21d window."""
    res = _drawdown(sgna, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_marketcap_dd_21d_v123_signal(marketcap):
    """Drawdown from peak to identify cycle troughs of Raw level of marketcap over 21d window."""
    res = _drawdown(marketcap, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_brand_leverage_dd_21d_v124_signal(revenue, sgna):
    """Drawdown from peak to identify cycle troughs of Sales generated per dollar of marketing/admin over 21d window."""
    res = _drawdown(_ratio(revenue, sgna), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_mkt_cap_per_rev_dd_21d_v125_signal(marketcap, revenue):
    """Drawdown from peak to identify cycle troughs of Valuation ascribed per unit of sales over 21d window."""
    res = _drawdown(_ratio(marketcap, revenue), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_revenue_dd_42d_v126_signal(revenue):
    """Drawdown from peak to identify cycle troughs of Raw level of revenue over 42d window."""
    res = _drawdown(revenue, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_sgna_dd_42d_v127_signal(sgna):
    """Drawdown from peak to identify cycle troughs of Raw level of sgna over 42d window."""
    res = _drawdown(sgna, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_marketcap_dd_42d_v128_signal(marketcap):
    """Drawdown from peak to identify cycle troughs of Raw level of marketcap over 42d window."""
    res = _drawdown(marketcap, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_brand_leverage_dd_42d_v129_signal(revenue, sgna):
    """Drawdown from peak to identify cycle troughs of Sales generated per dollar of marketing/admin over 42d window."""
    res = _drawdown(_ratio(revenue, sgna), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_mkt_cap_per_rev_dd_42d_v130_signal(marketcap, revenue):
    """Drawdown from peak to identify cycle troughs of Valuation ascribed per unit of sales over 42d window."""
    res = _drawdown(_ratio(marketcap, revenue), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_revenue_dd_63d_v131_signal(revenue):
    """Drawdown from peak to identify cycle troughs of Raw level of revenue over 63d window."""
    res = _drawdown(revenue, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_sgna_dd_63d_v132_signal(sgna):
    """Drawdown from peak to identify cycle troughs of Raw level of sgna over 63d window."""
    res = _drawdown(sgna, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_marketcap_dd_63d_v133_signal(marketcap):
    """Drawdown from peak to identify cycle troughs of Raw level of marketcap over 63d window."""
    res = _drawdown(marketcap, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_brand_leverage_dd_63d_v134_signal(revenue, sgna):
    """Drawdown from peak to identify cycle troughs of Sales generated per dollar of marketing/admin over 63d window."""
    res = _drawdown(_ratio(revenue, sgna), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_mkt_cap_per_rev_dd_63d_v135_signal(marketcap, revenue):
    """Drawdown from peak to identify cycle troughs of Valuation ascribed per unit of sales over 63d window."""
    res = _drawdown(_ratio(marketcap, revenue), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_revenue_dd_126d_v136_signal(revenue):
    """Drawdown from peak to identify cycle troughs of Raw level of revenue over 126d window."""
    res = _drawdown(revenue, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_sgna_dd_126d_v137_signal(sgna):
    """Drawdown from peak to identify cycle troughs of Raw level of sgna over 126d window."""
    res = _drawdown(sgna, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_marketcap_dd_126d_v138_signal(marketcap):
    """Drawdown from peak to identify cycle troughs of Raw level of marketcap over 126d window."""
    res = _drawdown(marketcap, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_brand_leverage_dd_126d_v139_signal(revenue, sgna):
    """Drawdown from peak to identify cycle troughs of Sales generated per dollar of marketing/admin over 126d window."""
    res = _drawdown(_ratio(revenue, sgna), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_mkt_cap_per_rev_dd_126d_v140_signal(marketcap, revenue):
    """Drawdown from peak to identify cycle troughs of Valuation ascribed per unit of sales over 126d window."""
    res = _drawdown(_ratio(marketcap, revenue), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_revenue_dd_252d_v141_signal(revenue):
    """Drawdown from peak to identify cycle troughs of Raw level of revenue over 252d window."""
    res = _drawdown(revenue, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_sgna_dd_252d_v142_signal(sgna):
    """Drawdown from peak to identify cycle troughs of Raw level of sgna over 252d window."""
    res = _drawdown(sgna, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_marketcap_dd_252d_v143_signal(marketcap):
    """Drawdown from peak to identify cycle troughs of Raw level of marketcap over 252d window."""
    res = _drawdown(marketcap, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_brand_leverage_dd_252d_v144_signal(revenue, sgna):
    """Drawdown from peak to identify cycle troughs of Sales generated per dollar of marketing/admin over 252d window."""
    res = _drawdown(_ratio(revenue, sgna), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_mkt_cap_per_rev_dd_252d_v145_signal(marketcap, revenue):
    """Drawdown from peak to identify cycle troughs of Valuation ascribed per unit of sales over 252d window."""
    res = _drawdown(_ratio(marketcap, revenue), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_revenue_dd_504d_v146_signal(revenue):
    """Drawdown from peak to identify cycle troughs of Raw level of revenue over 504d window."""
    res = _drawdown(revenue, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_sgna_dd_504d_v147_signal(sgna):
    """Drawdown from peak to identify cycle troughs of Raw level of sgna over 504d window."""
    res = _drawdown(sgna, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_marketcap_dd_504d_v148_signal(marketcap):
    """Drawdown from peak to identify cycle troughs of Raw level of marketcap over 504d window."""
    res = _drawdown(marketcap, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_brand_leverage_dd_504d_v149_signal(revenue, sgna):
    """Drawdown from peak to identify cycle troughs of Sales generated per dollar of marketing/admin over 504d window."""
    res = _drawdown(_ratio(revenue, sgna), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_brand_momentum_mkt_cap_per_rev_dd_504d_v150_signal(marketcap, revenue):
    """Drawdown from peak to identify cycle troughs of Valuation ascribed per unit of sales over 504d window."""
    res = _drawdown(_ratio(marketcap, revenue), 504)
    return res.replace([np.inf, -np.inf], np.nan)


# ===== Feature Registry =====
REGISTRY = {
    "f03_brand_momentum_revenue_z_63d_v076_signal": {"inputs": [], "func": f03_brand_momentum_revenue_z_63d_v076_signal},    "f03_brand_momentum_sgna_z_63d_v077_signal": {"inputs": [], "func": f03_brand_momentum_sgna_z_63d_v077_signal},    "f03_brand_momentum_marketcap_z_63d_v078_signal": {"inputs": [], "func": f03_brand_momentum_marketcap_z_63d_v078_signal},    "f03_brand_momentum_brand_leverage_z_63d_v079_signal": {"inputs": [], "func": f03_brand_momentum_brand_leverage_z_63d_v079_signal},    "f03_brand_momentum_mkt_cap_per_rev_z_63d_v080_signal": {"inputs": [], "func": f03_brand_momentum_mkt_cap_per_rev_z_63d_v080_signal},    "f03_brand_momentum_revenue_z_126d_v081_signal": {"inputs": [], "func": f03_brand_momentum_revenue_z_126d_v081_signal},    "f03_brand_momentum_sgna_z_126d_v082_signal": {"inputs": [], "func": f03_brand_momentum_sgna_z_126d_v082_signal},    "f03_brand_momentum_marketcap_z_126d_v083_signal": {"inputs": [], "func": f03_brand_momentum_marketcap_z_126d_v083_signal},    "f03_brand_momentum_brand_leverage_z_126d_v084_signal": {"inputs": [], "func": f03_brand_momentum_brand_leverage_z_126d_v084_signal},    "f03_brand_momentum_mkt_cap_per_rev_z_126d_v085_signal": {"inputs": [], "func": f03_brand_momentum_mkt_cap_per_rev_z_126d_v085_signal},    "f03_brand_momentum_revenue_z_252d_v086_signal": {"inputs": [], "func": f03_brand_momentum_revenue_z_252d_v086_signal},    "f03_brand_momentum_sgna_z_252d_v087_signal": {"inputs": [], "func": f03_brand_momentum_sgna_z_252d_v087_signal},    "f03_brand_momentum_marketcap_z_252d_v088_signal": {"inputs": [], "func": f03_brand_momentum_marketcap_z_252d_v088_signal},    "f03_brand_momentum_brand_leverage_z_252d_v089_signal": {"inputs": [], "func": f03_brand_momentum_brand_leverage_z_252d_v089_signal},    "f03_brand_momentum_mkt_cap_per_rev_z_252d_v090_signal": {"inputs": [], "func": f03_brand_momentum_mkt_cap_per_rev_z_252d_v090_signal},    "f03_brand_momentum_revenue_z_504d_v091_signal": {"inputs": [], "func": f03_brand_momentum_revenue_z_504d_v091_signal},    "f03_brand_momentum_sgna_z_504d_v092_signal": {"inputs": [], "func": f03_brand_momentum_sgna_z_504d_v092_signal},    "f03_brand_momentum_marketcap_z_504d_v093_signal": {"inputs": [], "func": f03_brand_momentum_marketcap_z_504d_v093_signal},    "f03_brand_momentum_brand_leverage_z_504d_v094_signal": {"inputs": [], "func": f03_brand_momentum_brand_leverage_z_504d_v094_signal},    "f03_brand_momentum_mkt_cap_per_rev_z_504d_v095_signal": {"inputs": [], "func": f03_brand_momentum_mkt_cap_per_rev_z_504d_v095_signal},    "f03_brand_momentum_revenue_z_756d_v096_signal": {"inputs": [], "func": f03_brand_momentum_revenue_z_756d_v096_signal},    "f03_brand_momentum_sgna_z_756d_v097_signal": {"inputs": [], "func": f03_brand_momentum_sgna_z_756d_v097_signal},    "f03_brand_momentum_marketcap_z_756d_v098_signal": {"inputs": [], "func": f03_brand_momentum_marketcap_z_756d_v098_signal},    "f03_brand_momentum_brand_leverage_z_756d_v099_signal": {"inputs": [], "func": f03_brand_momentum_brand_leverage_z_756d_v099_signal},    "f03_brand_momentum_mkt_cap_per_rev_z_756d_v100_signal": {"inputs": [], "func": f03_brand_momentum_mkt_cap_per_rev_z_756d_v100_signal},    "f03_brand_momentum_revenue_z_1008d_v101_signal": {"inputs": [], "func": f03_brand_momentum_revenue_z_1008d_v101_signal},    "f03_brand_momentum_sgna_z_1008d_v102_signal": {"inputs": [], "func": f03_brand_momentum_sgna_z_1008d_v102_signal},    "f03_brand_momentum_marketcap_z_1008d_v103_signal": {"inputs": [], "func": f03_brand_momentum_marketcap_z_1008d_v103_signal},    "f03_brand_momentum_brand_leverage_z_1008d_v104_signal": {"inputs": [], "func": f03_brand_momentum_brand_leverage_z_1008d_v104_signal},    "f03_brand_momentum_mkt_cap_per_rev_z_1008d_v105_signal": {"inputs": [], "func": f03_brand_momentum_mkt_cap_per_rev_z_1008d_v105_signal},    "f03_brand_momentum_revenue_z_1260d_v106_signal": {"inputs": [], "func": f03_brand_momentum_revenue_z_1260d_v106_signal},    "f03_brand_momentum_sgna_z_1260d_v107_signal": {"inputs": [], "func": f03_brand_momentum_sgna_z_1260d_v107_signal},    "f03_brand_momentum_marketcap_z_1260d_v108_signal": {"inputs": [], "func": f03_brand_momentum_marketcap_z_1260d_v108_signal},    "f03_brand_momentum_brand_leverage_z_1260d_v109_signal": {"inputs": [], "func": f03_brand_momentum_brand_leverage_z_1260d_v109_signal},    "f03_brand_momentum_mkt_cap_per_rev_z_1260d_v110_signal": {"inputs": [], "func": f03_brand_momentum_mkt_cap_per_rev_z_1260d_v110_signal},    "f03_brand_momentum_revenue_dd_5d_v111_signal": {"inputs": [], "func": f03_brand_momentum_revenue_dd_5d_v111_signal},    "f03_brand_momentum_sgna_dd_5d_v112_signal": {"inputs": [], "func": f03_brand_momentum_sgna_dd_5d_v112_signal},    "f03_brand_momentum_marketcap_dd_5d_v113_signal": {"inputs": [], "func": f03_brand_momentum_marketcap_dd_5d_v113_signal},    "f03_brand_momentum_brand_leverage_dd_5d_v114_signal": {"inputs": [], "func": f03_brand_momentum_brand_leverage_dd_5d_v114_signal},    "f03_brand_momentum_mkt_cap_per_rev_dd_5d_v115_signal": {"inputs": [], "func": f03_brand_momentum_mkt_cap_per_rev_dd_5d_v115_signal},    "f03_brand_momentum_revenue_dd_10d_v116_signal": {"inputs": [], "func": f03_brand_momentum_revenue_dd_10d_v116_signal},    "f03_brand_momentum_sgna_dd_10d_v117_signal": {"inputs": [], "func": f03_brand_momentum_sgna_dd_10d_v117_signal},    "f03_brand_momentum_marketcap_dd_10d_v118_signal": {"inputs": [], "func": f03_brand_momentum_marketcap_dd_10d_v118_signal},    "f03_brand_momentum_brand_leverage_dd_10d_v119_signal": {"inputs": [], "func": f03_brand_momentum_brand_leverage_dd_10d_v119_signal},    "f03_brand_momentum_mkt_cap_per_rev_dd_10d_v120_signal": {"inputs": [], "func": f03_brand_momentum_mkt_cap_per_rev_dd_10d_v120_signal},    "f03_brand_momentum_revenue_dd_21d_v121_signal": {"inputs": [], "func": f03_brand_momentum_revenue_dd_21d_v121_signal},    "f03_brand_momentum_sgna_dd_21d_v122_signal": {"inputs": [], "func": f03_brand_momentum_sgna_dd_21d_v122_signal},    "f03_brand_momentum_marketcap_dd_21d_v123_signal": {"inputs": [], "func": f03_brand_momentum_marketcap_dd_21d_v123_signal},    "f03_brand_momentum_brand_leverage_dd_21d_v124_signal": {"inputs": [], "func": f03_brand_momentum_brand_leverage_dd_21d_v124_signal},    "f03_brand_momentum_mkt_cap_per_rev_dd_21d_v125_signal": {"inputs": [], "func": f03_brand_momentum_mkt_cap_per_rev_dd_21d_v125_signal},    "f03_brand_momentum_revenue_dd_42d_v126_signal": {"inputs": [], "func": f03_brand_momentum_revenue_dd_42d_v126_signal},    "f03_brand_momentum_sgna_dd_42d_v127_signal": {"inputs": [], "func": f03_brand_momentum_sgna_dd_42d_v127_signal},    "f03_brand_momentum_marketcap_dd_42d_v128_signal": {"inputs": [], "func": f03_brand_momentum_marketcap_dd_42d_v128_signal},    "f03_brand_momentum_brand_leverage_dd_42d_v129_signal": {"inputs": [], "func": f03_brand_momentum_brand_leverage_dd_42d_v129_signal},    "f03_brand_momentum_mkt_cap_per_rev_dd_42d_v130_signal": {"inputs": [], "func": f03_brand_momentum_mkt_cap_per_rev_dd_42d_v130_signal},    "f03_brand_momentum_revenue_dd_63d_v131_signal": {"inputs": [], "func": f03_brand_momentum_revenue_dd_63d_v131_signal},    "f03_brand_momentum_sgna_dd_63d_v132_signal": {"inputs": [], "func": f03_brand_momentum_sgna_dd_63d_v132_signal},    "f03_brand_momentum_marketcap_dd_63d_v133_signal": {"inputs": [], "func": f03_brand_momentum_marketcap_dd_63d_v133_signal},    "f03_brand_momentum_brand_leverage_dd_63d_v134_signal": {"inputs": [], "func": f03_brand_momentum_brand_leverage_dd_63d_v134_signal},    "f03_brand_momentum_mkt_cap_per_rev_dd_63d_v135_signal": {"inputs": [], "func": f03_brand_momentum_mkt_cap_per_rev_dd_63d_v135_signal},    "f03_brand_momentum_revenue_dd_126d_v136_signal": {"inputs": [], "func": f03_brand_momentum_revenue_dd_126d_v136_signal},    "f03_brand_momentum_sgna_dd_126d_v137_signal": {"inputs": [], "func": f03_brand_momentum_sgna_dd_126d_v137_signal},    "f03_brand_momentum_marketcap_dd_126d_v138_signal": {"inputs": [], "func": f03_brand_momentum_marketcap_dd_126d_v138_signal},    "f03_brand_momentum_brand_leverage_dd_126d_v139_signal": {"inputs": [], "func": f03_brand_momentum_brand_leverage_dd_126d_v139_signal},    "f03_brand_momentum_mkt_cap_per_rev_dd_126d_v140_signal": {"inputs": [], "func": f03_brand_momentum_mkt_cap_per_rev_dd_126d_v140_signal},    "f03_brand_momentum_revenue_dd_252d_v141_signal": {"inputs": [], "func": f03_brand_momentum_revenue_dd_252d_v141_signal},    "f03_brand_momentum_sgna_dd_252d_v142_signal": {"inputs": [], "func": f03_brand_momentum_sgna_dd_252d_v142_signal},    "f03_brand_momentum_marketcap_dd_252d_v143_signal": {"inputs": [], "func": f03_brand_momentum_marketcap_dd_252d_v143_signal},    "f03_brand_momentum_brand_leverage_dd_252d_v144_signal": {"inputs": [], "func": f03_brand_momentum_brand_leverage_dd_252d_v144_signal},    "f03_brand_momentum_mkt_cap_per_rev_dd_252d_v145_signal": {"inputs": [], "func": f03_brand_momentum_mkt_cap_per_rev_dd_252d_v145_signal},    "f03_brand_momentum_revenue_dd_504d_v146_signal": {"inputs": [], "func": f03_brand_momentum_revenue_dd_504d_v146_signal},    "f03_brand_momentum_sgna_dd_504d_v147_signal": {"inputs": [], "func": f03_brand_momentum_sgna_dd_504d_v147_signal},    "f03_brand_momentum_marketcap_dd_504d_v148_signal": {"inputs": [], "func": f03_brand_momentum_marketcap_dd_504d_v148_signal},    "f03_brand_momentum_brand_leverage_dd_504d_v149_signal": {"inputs": [], "func": f03_brand_momentum_brand_leverage_dd_504d_v149_signal},    "f03_brand_momentum_mkt_cap_per_rev_dd_504d_v150_signal": {"inputs": [], "func": f03_brand_momentum_mkt_cap_per_rev_dd_504d_v150_signal},
}

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "grossmargin": np.random.normal(100, 10, n).cumsum(), "revenue": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "deferredrev": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "liabilitiesc": np.random.normal(100, 10, n).cumsum()
    })
    
    print(f"Verifying {len(REGISTRY)} functions for family 03...")
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
