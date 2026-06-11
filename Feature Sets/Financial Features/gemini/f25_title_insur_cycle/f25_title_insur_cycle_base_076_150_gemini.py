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

def f25_title_insur_cycle_revenue_cycle_ewma_504d_v076_signal(revenue):
    """Exponential moving average of Revenue relative to long-term cycle over 504d window."""
    res = _ewma(_ratio(revenue, _sma(revenue, 1260)), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_revenue_ewma_756d_v077_signal(revenue):
    """Exponential moving average of Raw level of revenue over 756d window."""
    res = _ewma(revenue, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_inventory_ewma_756d_v078_signal(inventory):
    """Exponential moving average of Raw level of inventory over 756d window."""
    res = _ewma(inventory, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_cor_ewma_756d_v079_signal(cor):
    """Exponential moving average of Raw level of cor over 756d window."""
    res = _ewma(cor, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_revenue_cycle_ewma_756d_v080_signal(revenue):
    """Exponential moving average of Revenue relative to long-term cycle over 756d window."""
    res = _ewma(_ratio(revenue, _sma(revenue, 1260)), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_revenue_ewma_1008d_v081_signal(revenue):
    """Exponential moving average of Raw level of revenue over 1008d window."""
    res = _ewma(revenue, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_inventory_ewma_1008d_v082_signal(inventory):
    """Exponential moving average of Raw level of inventory over 1008d window."""
    res = _ewma(inventory, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_cor_ewma_1008d_v083_signal(cor):
    """Exponential moving average of Raw level of cor over 1008d window."""
    res = _ewma(cor, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_revenue_cycle_ewma_1008d_v084_signal(revenue):
    """Exponential moving average of Revenue relative to long-term cycle over 1008d window."""
    res = _ewma(_ratio(revenue, _sma(revenue, 1260)), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_revenue_ewma_1260d_v085_signal(revenue):
    """Exponential moving average of Raw level of revenue over 1260d window."""
    res = _ewma(revenue, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_inventory_ewma_1260d_v086_signal(inventory):
    """Exponential moving average of Raw level of inventory over 1260d window."""
    res = _ewma(inventory, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_cor_ewma_1260d_v087_signal(cor):
    """Exponential moving average of Raw level of cor over 1260d window."""
    res = _ewma(cor, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_revenue_cycle_ewma_1260d_v088_signal(revenue):
    """Exponential moving average of Revenue relative to long-term cycle over 1260d window."""
    res = _ewma(_ratio(revenue, _sma(revenue, 1260)), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_revenue_z_5d_v089_signal(revenue):
    """Z-score of Raw level of revenue over 5d window."""
    res = _z(revenue, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_inventory_z_5d_v090_signal(inventory):
    """Z-score of Raw level of inventory over 5d window."""
    res = _z(inventory, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_cor_z_5d_v091_signal(cor):
    """Z-score of Raw level of cor over 5d window."""
    res = _z(cor, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_revenue_cycle_z_5d_v092_signal(revenue):
    """Z-score of Revenue relative to long-term cycle over 5d window."""
    res = _z(_ratio(revenue, _sma(revenue, 1260)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_revenue_z_10d_v093_signal(revenue):
    """Z-score of Raw level of revenue over 10d window."""
    res = _z(revenue, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_inventory_z_10d_v094_signal(inventory):
    """Z-score of Raw level of inventory over 10d window."""
    res = _z(inventory, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_cor_z_10d_v095_signal(cor):
    """Z-score of Raw level of cor over 10d window."""
    res = _z(cor, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_revenue_cycle_z_10d_v096_signal(revenue):
    """Z-score of Revenue relative to long-term cycle over 10d window."""
    res = _z(_ratio(revenue, _sma(revenue, 1260)), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_revenue_z_21d_v097_signal(revenue):
    """Z-score of Raw level of revenue over 21d window."""
    res = _z(revenue, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_inventory_z_21d_v098_signal(inventory):
    """Z-score of Raw level of inventory over 21d window."""
    res = _z(inventory, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_cor_z_21d_v099_signal(cor):
    """Z-score of Raw level of cor over 21d window."""
    res = _z(cor, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_revenue_cycle_z_21d_v100_signal(revenue):
    """Z-score of Revenue relative to long-term cycle over 21d window."""
    res = _z(_ratio(revenue, _sma(revenue, 1260)), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_revenue_z_42d_v101_signal(revenue):
    """Z-score of Raw level of revenue over 42d window."""
    res = _z(revenue, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_inventory_z_42d_v102_signal(inventory):
    """Z-score of Raw level of inventory over 42d window."""
    res = _z(inventory, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_cor_z_42d_v103_signal(cor):
    """Z-score of Raw level of cor over 42d window."""
    res = _z(cor, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_revenue_cycle_z_42d_v104_signal(revenue):
    """Z-score of Revenue relative to long-term cycle over 42d window."""
    res = _z(_ratio(revenue, _sma(revenue, 1260)), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_revenue_z_63d_v105_signal(revenue):
    """Z-score of Raw level of revenue over 63d window."""
    res = _z(revenue, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_inventory_z_63d_v106_signal(inventory):
    """Z-score of Raw level of inventory over 63d window."""
    res = _z(inventory, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_cor_z_63d_v107_signal(cor):
    """Z-score of Raw level of cor over 63d window."""
    res = _z(cor, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_revenue_cycle_z_63d_v108_signal(revenue):
    """Z-score of Revenue relative to long-term cycle over 63d window."""
    res = _z(_ratio(revenue, _sma(revenue, 1260)), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_revenue_z_126d_v109_signal(revenue):
    """Z-score of Raw level of revenue over 126d window."""
    res = _z(revenue, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_inventory_z_126d_v110_signal(inventory):
    """Z-score of Raw level of inventory over 126d window."""
    res = _z(inventory, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_cor_z_126d_v111_signal(cor):
    """Z-score of Raw level of cor over 126d window."""
    res = _z(cor, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_revenue_cycle_z_126d_v112_signal(revenue):
    """Z-score of Revenue relative to long-term cycle over 126d window."""
    res = _z(_ratio(revenue, _sma(revenue, 1260)), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_revenue_z_252d_v113_signal(revenue):
    """Z-score of Raw level of revenue over 252d window."""
    res = _z(revenue, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_inventory_z_252d_v114_signal(inventory):
    """Z-score of Raw level of inventory over 252d window."""
    res = _z(inventory, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_cor_z_252d_v115_signal(cor):
    """Z-score of Raw level of cor over 252d window."""
    res = _z(cor, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_revenue_cycle_z_252d_v116_signal(revenue):
    """Z-score of Revenue relative to long-term cycle over 252d window."""
    res = _z(_ratio(revenue, _sma(revenue, 1260)), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_revenue_z_504d_v117_signal(revenue):
    """Z-score of Raw level of revenue over 504d window."""
    res = _z(revenue, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_inventory_z_504d_v118_signal(inventory):
    """Z-score of Raw level of inventory over 504d window."""
    res = _z(inventory, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_cor_z_504d_v119_signal(cor):
    """Z-score of Raw level of cor over 504d window."""
    res = _z(cor, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_revenue_cycle_z_504d_v120_signal(revenue):
    """Z-score of Revenue relative to long-term cycle over 504d window."""
    res = _z(_ratio(revenue, _sma(revenue, 1260)), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_revenue_z_756d_v121_signal(revenue):
    """Z-score of Raw level of revenue over 756d window."""
    res = _z(revenue, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_inventory_z_756d_v122_signal(inventory):
    """Z-score of Raw level of inventory over 756d window."""
    res = _z(inventory, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_cor_z_756d_v123_signal(cor):
    """Z-score of Raw level of cor over 756d window."""
    res = _z(cor, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_revenue_cycle_z_756d_v124_signal(revenue):
    """Z-score of Revenue relative to long-term cycle over 756d window."""
    res = _z(_ratio(revenue, _sma(revenue, 1260)), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_revenue_z_1008d_v125_signal(revenue):
    """Z-score of Raw level of revenue over 1008d window."""
    res = _z(revenue, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_inventory_z_1008d_v126_signal(inventory):
    """Z-score of Raw level of inventory over 1008d window."""
    res = _z(inventory, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_cor_z_1008d_v127_signal(cor):
    """Z-score of Raw level of cor over 1008d window."""
    res = _z(cor, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_revenue_cycle_z_1008d_v128_signal(revenue):
    """Z-score of Revenue relative to long-term cycle over 1008d window."""
    res = _z(_ratio(revenue, _sma(revenue, 1260)), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_revenue_z_1260d_v129_signal(revenue):
    """Z-score of Raw level of revenue over 1260d window."""
    res = _z(revenue, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_inventory_z_1260d_v130_signal(inventory):
    """Z-score of Raw level of inventory over 1260d window."""
    res = _z(inventory, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_cor_z_1260d_v131_signal(cor):
    """Z-score of Raw level of cor over 1260d window."""
    res = _z(cor, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_revenue_cycle_z_1260d_v132_signal(revenue):
    """Z-score of Revenue relative to long-term cycle over 1260d window."""
    res = _z(_ratio(revenue, _sma(revenue, 1260)), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_revenue_dd_5d_v133_signal(revenue):
    """Drawdown of Raw level of revenue over 5d window."""
    res = _drawdown(revenue, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_inventory_dd_5d_v134_signal(inventory):
    """Drawdown of Raw level of inventory over 5d window."""
    res = _drawdown(inventory, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_cor_dd_5d_v135_signal(cor):
    """Drawdown of Raw level of cor over 5d window."""
    res = _drawdown(cor, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_revenue_cycle_dd_5d_v136_signal(revenue):
    """Drawdown of Revenue relative to long-term cycle over 5d window."""
    res = _drawdown(_ratio(revenue, _sma(revenue, 1260)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_revenue_dd_10d_v137_signal(revenue):
    """Drawdown of Raw level of revenue over 10d window."""
    res = _drawdown(revenue, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_inventory_dd_10d_v138_signal(inventory):
    """Drawdown of Raw level of inventory over 10d window."""
    res = _drawdown(inventory, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_cor_dd_10d_v139_signal(cor):
    """Drawdown of Raw level of cor over 10d window."""
    res = _drawdown(cor, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_revenue_cycle_dd_10d_v140_signal(revenue):
    """Drawdown of Revenue relative to long-term cycle over 10d window."""
    res = _drawdown(_ratio(revenue, _sma(revenue, 1260)), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_revenue_dd_21d_v141_signal(revenue):
    """Drawdown of Raw level of revenue over 21d window."""
    res = _drawdown(revenue, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_inventory_dd_21d_v142_signal(inventory):
    """Drawdown of Raw level of inventory over 21d window."""
    res = _drawdown(inventory, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_cor_dd_21d_v143_signal(cor):
    """Drawdown of Raw level of cor over 21d window."""
    res = _drawdown(cor, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_revenue_cycle_dd_21d_v144_signal(revenue):
    """Drawdown of Revenue relative to long-term cycle over 21d window."""
    res = _drawdown(_ratio(revenue, _sma(revenue, 1260)), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_revenue_dd_42d_v145_signal(revenue):
    """Drawdown of Raw level of revenue over 42d window."""
    res = _drawdown(revenue, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_inventory_dd_42d_v146_signal(inventory):
    """Drawdown of Raw level of inventory over 42d window."""
    res = _drawdown(inventory, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_cor_dd_42d_v147_signal(cor):
    """Drawdown of Raw level of cor over 42d window."""
    res = _drawdown(cor, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_revenue_cycle_dd_42d_v148_signal(revenue):
    """Drawdown of Revenue relative to long-term cycle over 42d window."""
    res = _drawdown(_ratio(revenue, _sma(revenue, 1260)), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_revenue_dd_63d_v149_signal(revenue):
    """Drawdown of Raw level of revenue over 63d window."""
    res = _drawdown(revenue, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_title_insur_cycle_inventory_dd_63d_v150_signal(inventory):
    """Drawdown of Raw level of inventory over 63d window."""
    res = _drawdown(inventory, 63)
    return res.replace([np.inf, -np.inf], np.nan)


# ===== Feature Registry =====
REGISTRY = {
    "f25_title_insur_cycle_revenue_cycle_ewma_504d_v076_signal": {"func": f25_title_insur_cycle_revenue_cycle_ewma_504d_v076_signal},
    "f25_title_insur_cycle_revenue_ewma_756d_v077_signal": {"func": f25_title_insur_cycle_revenue_ewma_756d_v077_signal},
    "f25_title_insur_cycle_inventory_ewma_756d_v078_signal": {"func": f25_title_insur_cycle_inventory_ewma_756d_v078_signal},
    "f25_title_insur_cycle_cor_ewma_756d_v079_signal": {"func": f25_title_insur_cycle_cor_ewma_756d_v079_signal},
    "f25_title_insur_cycle_revenue_cycle_ewma_756d_v080_signal": {"func": f25_title_insur_cycle_revenue_cycle_ewma_756d_v080_signal},
    "f25_title_insur_cycle_revenue_ewma_1008d_v081_signal": {"func": f25_title_insur_cycle_revenue_ewma_1008d_v081_signal},
    "f25_title_insur_cycle_inventory_ewma_1008d_v082_signal": {"func": f25_title_insur_cycle_inventory_ewma_1008d_v082_signal},
    "f25_title_insur_cycle_cor_ewma_1008d_v083_signal": {"func": f25_title_insur_cycle_cor_ewma_1008d_v083_signal},
    "f25_title_insur_cycle_revenue_cycle_ewma_1008d_v084_signal": {"func": f25_title_insur_cycle_revenue_cycle_ewma_1008d_v084_signal},
    "f25_title_insur_cycle_revenue_ewma_1260d_v085_signal": {"func": f25_title_insur_cycle_revenue_ewma_1260d_v085_signal},
    "f25_title_insur_cycle_inventory_ewma_1260d_v086_signal": {"func": f25_title_insur_cycle_inventory_ewma_1260d_v086_signal},
    "f25_title_insur_cycle_cor_ewma_1260d_v087_signal": {"func": f25_title_insur_cycle_cor_ewma_1260d_v087_signal},
    "f25_title_insur_cycle_revenue_cycle_ewma_1260d_v088_signal": {"func": f25_title_insur_cycle_revenue_cycle_ewma_1260d_v088_signal},
    "f25_title_insur_cycle_revenue_z_5d_v089_signal": {"func": f25_title_insur_cycle_revenue_z_5d_v089_signal},
    "f25_title_insur_cycle_inventory_z_5d_v090_signal": {"func": f25_title_insur_cycle_inventory_z_5d_v090_signal},
    "f25_title_insur_cycle_cor_z_5d_v091_signal": {"func": f25_title_insur_cycle_cor_z_5d_v091_signal},
    "f25_title_insur_cycle_revenue_cycle_z_5d_v092_signal": {"func": f25_title_insur_cycle_revenue_cycle_z_5d_v092_signal},
    "f25_title_insur_cycle_revenue_z_10d_v093_signal": {"func": f25_title_insur_cycle_revenue_z_10d_v093_signal},
    "f25_title_insur_cycle_inventory_z_10d_v094_signal": {"func": f25_title_insur_cycle_inventory_z_10d_v094_signal},
    "f25_title_insur_cycle_cor_z_10d_v095_signal": {"func": f25_title_insur_cycle_cor_z_10d_v095_signal},
    "f25_title_insur_cycle_revenue_cycle_z_10d_v096_signal": {"func": f25_title_insur_cycle_revenue_cycle_z_10d_v096_signal},
    "f25_title_insur_cycle_revenue_z_21d_v097_signal": {"func": f25_title_insur_cycle_revenue_z_21d_v097_signal},
    "f25_title_insur_cycle_inventory_z_21d_v098_signal": {"func": f25_title_insur_cycle_inventory_z_21d_v098_signal},
    "f25_title_insur_cycle_cor_z_21d_v099_signal": {"func": f25_title_insur_cycle_cor_z_21d_v099_signal},
    "f25_title_insur_cycle_revenue_cycle_z_21d_v100_signal": {"func": f25_title_insur_cycle_revenue_cycle_z_21d_v100_signal},
    "f25_title_insur_cycle_revenue_z_42d_v101_signal": {"func": f25_title_insur_cycle_revenue_z_42d_v101_signal},
    "f25_title_insur_cycle_inventory_z_42d_v102_signal": {"func": f25_title_insur_cycle_inventory_z_42d_v102_signal},
    "f25_title_insur_cycle_cor_z_42d_v103_signal": {"func": f25_title_insur_cycle_cor_z_42d_v103_signal},
    "f25_title_insur_cycle_revenue_cycle_z_42d_v104_signal": {"func": f25_title_insur_cycle_revenue_cycle_z_42d_v104_signal},
    "f25_title_insur_cycle_revenue_z_63d_v105_signal": {"func": f25_title_insur_cycle_revenue_z_63d_v105_signal},
    "f25_title_insur_cycle_inventory_z_63d_v106_signal": {"func": f25_title_insur_cycle_inventory_z_63d_v106_signal},
    "f25_title_insur_cycle_cor_z_63d_v107_signal": {"func": f25_title_insur_cycle_cor_z_63d_v107_signal},
    "f25_title_insur_cycle_revenue_cycle_z_63d_v108_signal": {"func": f25_title_insur_cycle_revenue_cycle_z_63d_v108_signal},
    "f25_title_insur_cycle_revenue_z_126d_v109_signal": {"func": f25_title_insur_cycle_revenue_z_126d_v109_signal},
    "f25_title_insur_cycle_inventory_z_126d_v110_signal": {"func": f25_title_insur_cycle_inventory_z_126d_v110_signal},
    "f25_title_insur_cycle_cor_z_126d_v111_signal": {"func": f25_title_insur_cycle_cor_z_126d_v111_signal},
    "f25_title_insur_cycle_revenue_cycle_z_126d_v112_signal": {"func": f25_title_insur_cycle_revenue_cycle_z_126d_v112_signal},
    "f25_title_insur_cycle_revenue_z_252d_v113_signal": {"func": f25_title_insur_cycle_revenue_z_252d_v113_signal},
    "f25_title_insur_cycle_inventory_z_252d_v114_signal": {"func": f25_title_insur_cycle_inventory_z_252d_v114_signal},
    "f25_title_insur_cycle_cor_z_252d_v115_signal": {"func": f25_title_insur_cycle_cor_z_252d_v115_signal},
    "f25_title_insur_cycle_revenue_cycle_z_252d_v116_signal": {"func": f25_title_insur_cycle_revenue_cycle_z_252d_v116_signal},
    "f25_title_insur_cycle_revenue_z_504d_v117_signal": {"func": f25_title_insur_cycle_revenue_z_504d_v117_signal},
    "f25_title_insur_cycle_inventory_z_504d_v118_signal": {"func": f25_title_insur_cycle_inventory_z_504d_v118_signal},
    "f25_title_insur_cycle_cor_z_504d_v119_signal": {"func": f25_title_insur_cycle_cor_z_504d_v119_signal},
    "f25_title_insur_cycle_revenue_cycle_z_504d_v120_signal": {"func": f25_title_insur_cycle_revenue_cycle_z_504d_v120_signal},
    "f25_title_insur_cycle_revenue_z_756d_v121_signal": {"func": f25_title_insur_cycle_revenue_z_756d_v121_signal},
    "f25_title_insur_cycle_inventory_z_756d_v122_signal": {"func": f25_title_insur_cycle_inventory_z_756d_v122_signal},
    "f25_title_insur_cycle_cor_z_756d_v123_signal": {"func": f25_title_insur_cycle_cor_z_756d_v123_signal},
    "f25_title_insur_cycle_revenue_cycle_z_756d_v124_signal": {"func": f25_title_insur_cycle_revenue_cycle_z_756d_v124_signal},
    "f25_title_insur_cycle_revenue_z_1008d_v125_signal": {"func": f25_title_insur_cycle_revenue_z_1008d_v125_signal},
    "f25_title_insur_cycle_inventory_z_1008d_v126_signal": {"func": f25_title_insur_cycle_inventory_z_1008d_v126_signal},
    "f25_title_insur_cycle_cor_z_1008d_v127_signal": {"func": f25_title_insur_cycle_cor_z_1008d_v127_signal},
    "f25_title_insur_cycle_revenue_cycle_z_1008d_v128_signal": {"func": f25_title_insur_cycle_revenue_cycle_z_1008d_v128_signal},
    "f25_title_insur_cycle_revenue_z_1260d_v129_signal": {"func": f25_title_insur_cycle_revenue_z_1260d_v129_signal},
    "f25_title_insur_cycle_inventory_z_1260d_v130_signal": {"func": f25_title_insur_cycle_inventory_z_1260d_v130_signal},
    "f25_title_insur_cycle_cor_z_1260d_v131_signal": {"func": f25_title_insur_cycle_cor_z_1260d_v131_signal},
    "f25_title_insur_cycle_revenue_cycle_z_1260d_v132_signal": {"func": f25_title_insur_cycle_revenue_cycle_z_1260d_v132_signal},
    "f25_title_insur_cycle_revenue_dd_5d_v133_signal": {"func": f25_title_insur_cycle_revenue_dd_5d_v133_signal},
    "f25_title_insur_cycle_inventory_dd_5d_v134_signal": {"func": f25_title_insur_cycle_inventory_dd_5d_v134_signal},
    "f25_title_insur_cycle_cor_dd_5d_v135_signal": {"func": f25_title_insur_cycle_cor_dd_5d_v135_signal},
    "f25_title_insur_cycle_revenue_cycle_dd_5d_v136_signal": {"func": f25_title_insur_cycle_revenue_cycle_dd_5d_v136_signal},
    "f25_title_insur_cycle_revenue_dd_10d_v137_signal": {"func": f25_title_insur_cycle_revenue_dd_10d_v137_signal},
    "f25_title_insur_cycle_inventory_dd_10d_v138_signal": {"func": f25_title_insur_cycle_inventory_dd_10d_v138_signal},
    "f25_title_insur_cycle_cor_dd_10d_v139_signal": {"func": f25_title_insur_cycle_cor_dd_10d_v139_signal},
    "f25_title_insur_cycle_revenue_cycle_dd_10d_v140_signal": {"func": f25_title_insur_cycle_revenue_cycle_dd_10d_v140_signal},
    "f25_title_insur_cycle_revenue_dd_21d_v141_signal": {"func": f25_title_insur_cycle_revenue_dd_21d_v141_signal},
    "f25_title_insur_cycle_inventory_dd_21d_v142_signal": {"func": f25_title_insur_cycle_inventory_dd_21d_v142_signal},
    "f25_title_insur_cycle_cor_dd_21d_v143_signal": {"func": f25_title_insur_cycle_cor_dd_21d_v143_signal},
    "f25_title_insur_cycle_revenue_cycle_dd_21d_v144_signal": {"func": f25_title_insur_cycle_revenue_cycle_dd_21d_v144_signal},
    "f25_title_insur_cycle_revenue_dd_42d_v145_signal": {"func": f25_title_insur_cycle_revenue_dd_42d_v145_signal},
    "f25_title_insur_cycle_inventory_dd_42d_v146_signal": {"func": f25_title_insur_cycle_inventory_dd_42d_v146_signal},
    "f25_title_insur_cycle_cor_dd_42d_v147_signal": {"func": f25_title_insur_cycle_cor_dd_42d_v147_signal},
    "f25_title_insur_cycle_revenue_cycle_dd_42d_v148_signal": {"func": f25_title_insur_cycle_revenue_cycle_dd_42d_v148_signal},
    "f25_title_insur_cycle_revenue_dd_63d_v149_signal": {"func": f25_title_insur_cycle_revenue_dd_63d_v149_signal},
    "f25_title_insur_cycle_inventory_dd_63d_v150_signal": {"func": f25_title_insur_cycle_inventory_dd_63d_v150_signal},
}

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "deferredrev": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "equity": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "deposits": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "divyield": np.random.normal(100, 10, n).cumsum(), "bvps": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "tangibles": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "grossmargin": np.random.normal(100, 10, n).cumsum(), "revenue": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "liabilitiesc": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum()
    })
    print(f"Verifying {len(REGISTRY)} functions for family 25...")
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
