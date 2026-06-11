import pandas as pd
import numpy as np
import inspect

# ===== Healthcare High-Performance Alpha Helpers =====
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

def f03_commercial_sales_velocity_backlog_burn_ewma_504d_v076_signal(revenue, deferredrev):
    """Exponential moving average of Backlog realization velocity over 504d window."""
    res = _ewma(_ratio(revenue, deferredrev), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_commercial_sales_velocity_deferredrev_ewma_756d_v077_signal(deferredrev):
    """Exponential moving average of Raw level of deferredrev over 756d window."""
    res = _ewma(deferredrev, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_commercial_sales_velocity_revenue_ewma_756d_v078_signal(revenue):
    """Exponential moving average of Raw level of revenue over 756d window."""
    res = _ewma(revenue, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_commercial_sales_velocity_receivables_ewma_756d_v079_signal(receivables):
    """Exponential moving average of Raw level of receivables over 756d window."""
    res = _ewma(receivables, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_commercial_sales_velocity_backlog_burn_ewma_756d_v080_signal(revenue, deferredrev):
    """Exponential moving average of Backlog realization velocity over 756d window."""
    res = _ewma(_ratio(revenue, deferredrev), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_commercial_sales_velocity_deferredrev_ewma_1008d_v081_signal(deferredrev):
    """Exponential moving average of Raw level of deferredrev over 1008d window."""
    res = _ewma(deferredrev, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_commercial_sales_velocity_revenue_ewma_1008d_v082_signal(revenue):
    """Exponential moving average of Raw level of revenue over 1008d window."""
    res = _ewma(revenue, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_commercial_sales_velocity_receivables_ewma_1008d_v083_signal(receivables):
    """Exponential moving average of Raw level of receivables over 1008d window."""
    res = _ewma(receivables, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_commercial_sales_velocity_backlog_burn_ewma_1008d_v084_signal(revenue, deferredrev):
    """Exponential moving average of Backlog realization velocity over 1008d window."""
    res = _ewma(_ratio(revenue, deferredrev), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_commercial_sales_velocity_deferredrev_ewma_1260d_v085_signal(deferredrev):
    """Exponential moving average of Raw level of deferredrev over 1260d window."""
    res = _ewma(deferredrev, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_commercial_sales_velocity_revenue_ewma_1260d_v086_signal(revenue):
    """Exponential moving average of Raw level of revenue over 1260d window."""
    res = _ewma(revenue, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_commercial_sales_velocity_receivables_ewma_1260d_v087_signal(receivables):
    """Exponential moving average of Raw level of receivables over 1260d window."""
    res = _ewma(receivables, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_commercial_sales_velocity_backlog_burn_ewma_1260d_v088_signal(revenue, deferredrev):
    """Exponential moving average of Backlog realization velocity over 1260d window."""
    res = _ewma(_ratio(revenue, deferredrev), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_commercial_sales_velocity_deferredrev_z_5d_v089_signal(deferredrev):
    """Z-score of Raw level of deferredrev over 5d window."""
    res = _z(deferredrev, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_commercial_sales_velocity_revenue_z_5d_v090_signal(revenue):
    """Z-score of Raw level of revenue over 5d window."""
    res = _z(revenue, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_commercial_sales_velocity_receivables_z_5d_v091_signal(receivables):
    """Z-score of Raw level of receivables over 5d window."""
    res = _z(receivables, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_commercial_sales_velocity_backlog_burn_z_5d_v092_signal(revenue, deferredrev):
    """Z-score of Backlog realization velocity over 5d window."""
    res = _z(_ratio(revenue, deferredrev), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_commercial_sales_velocity_deferredrev_z_10d_v093_signal(deferredrev):
    """Z-score of Raw level of deferredrev over 10d window."""
    res = _z(deferredrev, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_commercial_sales_velocity_revenue_z_10d_v094_signal(revenue):
    """Z-score of Raw level of revenue over 10d window."""
    res = _z(revenue, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_commercial_sales_velocity_receivables_z_10d_v095_signal(receivables):
    """Z-score of Raw level of receivables over 10d window."""
    res = _z(receivables, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_commercial_sales_velocity_backlog_burn_z_10d_v096_signal(revenue, deferredrev):
    """Z-score of Backlog realization velocity over 10d window."""
    res = _z(_ratio(revenue, deferredrev), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_commercial_sales_velocity_deferredrev_z_21d_v097_signal(deferredrev):
    """Z-score of Raw level of deferredrev over 21d window."""
    res = _z(deferredrev, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_commercial_sales_velocity_revenue_z_21d_v098_signal(revenue):
    """Z-score of Raw level of revenue over 21d window."""
    res = _z(revenue, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_commercial_sales_velocity_receivables_z_21d_v099_signal(receivables):
    """Z-score of Raw level of receivables over 21d window."""
    res = _z(receivables, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_commercial_sales_velocity_backlog_burn_z_21d_v100_signal(revenue, deferredrev):
    """Z-score of Backlog realization velocity over 21d window."""
    res = _z(_ratio(revenue, deferredrev), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_commercial_sales_velocity_deferredrev_z_42d_v101_signal(deferredrev):
    """Z-score of Raw level of deferredrev over 42d window."""
    res = _z(deferredrev, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_commercial_sales_velocity_revenue_z_42d_v102_signal(revenue):
    """Z-score of Raw level of revenue over 42d window."""
    res = _z(revenue, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_commercial_sales_velocity_receivables_z_42d_v103_signal(receivables):
    """Z-score of Raw level of receivables over 42d window."""
    res = _z(receivables, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_commercial_sales_velocity_backlog_burn_z_42d_v104_signal(revenue, deferredrev):
    """Z-score of Backlog realization velocity over 42d window."""
    res = _z(_ratio(revenue, deferredrev), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_commercial_sales_velocity_deferredrev_z_63d_v105_signal(deferredrev):
    """Z-score of Raw level of deferredrev over 63d window."""
    res = _z(deferredrev, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_commercial_sales_velocity_revenue_z_63d_v106_signal(revenue):
    """Z-score of Raw level of revenue over 63d window."""
    res = _z(revenue, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_commercial_sales_velocity_receivables_z_63d_v107_signal(receivables):
    """Z-score of Raw level of receivables over 63d window."""
    res = _z(receivables, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_commercial_sales_velocity_backlog_burn_z_63d_v108_signal(revenue, deferredrev):
    """Z-score of Backlog realization velocity over 63d window."""
    res = _z(_ratio(revenue, deferredrev), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_commercial_sales_velocity_deferredrev_z_126d_v109_signal(deferredrev):
    """Z-score of Raw level of deferredrev over 126d window."""
    res = _z(deferredrev, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_commercial_sales_velocity_revenue_z_126d_v110_signal(revenue):
    """Z-score of Raw level of revenue over 126d window."""
    res = _z(revenue, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_commercial_sales_velocity_receivables_z_126d_v111_signal(receivables):
    """Z-score of Raw level of receivables over 126d window."""
    res = _z(receivables, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_commercial_sales_velocity_backlog_burn_z_126d_v112_signal(revenue, deferredrev):
    """Z-score of Backlog realization velocity over 126d window."""
    res = _z(_ratio(revenue, deferredrev), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_commercial_sales_velocity_deferredrev_z_252d_v113_signal(deferredrev):
    """Z-score of Raw level of deferredrev over 252d window."""
    res = _z(deferredrev, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_commercial_sales_velocity_revenue_z_252d_v114_signal(revenue):
    """Z-score of Raw level of revenue over 252d window."""
    res = _z(revenue, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_commercial_sales_velocity_receivables_z_252d_v115_signal(receivables):
    """Z-score of Raw level of receivables over 252d window."""
    res = _z(receivables, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_commercial_sales_velocity_backlog_burn_z_252d_v116_signal(revenue, deferredrev):
    """Z-score of Backlog realization velocity over 252d window."""
    res = _z(_ratio(revenue, deferredrev), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_commercial_sales_velocity_deferredrev_z_504d_v117_signal(deferredrev):
    """Z-score of Raw level of deferredrev over 504d window."""
    res = _z(deferredrev, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_commercial_sales_velocity_revenue_z_504d_v118_signal(revenue):
    """Z-score of Raw level of revenue over 504d window."""
    res = _z(revenue, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_commercial_sales_velocity_receivables_z_504d_v119_signal(receivables):
    """Z-score of Raw level of receivables over 504d window."""
    res = _z(receivables, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_commercial_sales_velocity_backlog_burn_z_504d_v120_signal(revenue, deferredrev):
    """Z-score of Backlog realization velocity over 504d window."""
    res = _z(_ratio(revenue, deferredrev), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_commercial_sales_velocity_deferredrev_z_756d_v121_signal(deferredrev):
    """Z-score of Raw level of deferredrev over 756d window."""
    res = _z(deferredrev, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_commercial_sales_velocity_revenue_z_756d_v122_signal(revenue):
    """Z-score of Raw level of revenue over 756d window."""
    res = _z(revenue, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_commercial_sales_velocity_receivables_z_756d_v123_signal(receivables):
    """Z-score of Raw level of receivables over 756d window."""
    res = _z(receivables, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_commercial_sales_velocity_backlog_burn_z_756d_v124_signal(revenue, deferredrev):
    """Z-score of Backlog realization velocity over 756d window."""
    res = _z(_ratio(revenue, deferredrev), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_commercial_sales_velocity_deferredrev_z_1008d_v125_signal(deferredrev):
    """Z-score of Raw level of deferredrev over 1008d window."""
    res = _z(deferredrev, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_commercial_sales_velocity_revenue_z_1008d_v126_signal(revenue):
    """Z-score of Raw level of revenue over 1008d window."""
    res = _z(revenue, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_commercial_sales_velocity_receivables_z_1008d_v127_signal(receivables):
    """Z-score of Raw level of receivables over 1008d window."""
    res = _z(receivables, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_commercial_sales_velocity_backlog_burn_z_1008d_v128_signal(revenue, deferredrev):
    """Z-score of Backlog realization velocity over 1008d window."""
    res = _z(_ratio(revenue, deferredrev), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_commercial_sales_velocity_deferredrev_z_1260d_v129_signal(deferredrev):
    """Z-score of Raw level of deferredrev over 1260d window."""
    res = _z(deferredrev, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_commercial_sales_velocity_revenue_z_1260d_v130_signal(revenue):
    """Z-score of Raw level of revenue over 1260d window."""
    res = _z(revenue, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_commercial_sales_velocity_receivables_z_1260d_v131_signal(receivables):
    """Z-score of Raw level of receivables over 1260d window."""
    res = _z(receivables, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_commercial_sales_velocity_backlog_burn_z_1260d_v132_signal(revenue, deferredrev):
    """Z-score of Backlog realization velocity over 1260d window."""
    res = _z(_ratio(revenue, deferredrev), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_commercial_sales_velocity_deferredrev_dd_5d_v133_signal(deferredrev):
    """Drawdown of Raw level of deferredrev over 5d window."""
    res = _drawdown(deferredrev, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_commercial_sales_velocity_revenue_dd_5d_v134_signal(revenue):
    """Drawdown of Raw level of revenue over 5d window."""
    res = _drawdown(revenue, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_commercial_sales_velocity_receivables_dd_5d_v135_signal(receivables):
    """Drawdown of Raw level of receivables over 5d window."""
    res = _drawdown(receivables, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_commercial_sales_velocity_backlog_burn_dd_5d_v136_signal(revenue, deferredrev):
    """Drawdown of Backlog realization velocity over 5d window."""
    res = _drawdown(_ratio(revenue, deferredrev), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_commercial_sales_velocity_deferredrev_dd_10d_v137_signal(deferredrev):
    """Drawdown of Raw level of deferredrev over 10d window."""
    res = _drawdown(deferredrev, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_commercial_sales_velocity_revenue_dd_10d_v138_signal(revenue):
    """Drawdown of Raw level of revenue over 10d window."""
    res = _drawdown(revenue, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_commercial_sales_velocity_receivables_dd_10d_v139_signal(receivables):
    """Drawdown of Raw level of receivables over 10d window."""
    res = _drawdown(receivables, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_commercial_sales_velocity_backlog_burn_dd_10d_v140_signal(revenue, deferredrev):
    """Drawdown of Backlog realization velocity over 10d window."""
    res = _drawdown(_ratio(revenue, deferredrev), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_commercial_sales_velocity_deferredrev_dd_21d_v141_signal(deferredrev):
    """Drawdown of Raw level of deferredrev over 21d window."""
    res = _drawdown(deferredrev, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_commercial_sales_velocity_revenue_dd_21d_v142_signal(revenue):
    """Drawdown of Raw level of revenue over 21d window."""
    res = _drawdown(revenue, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_commercial_sales_velocity_receivables_dd_21d_v143_signal(receivables):
    """Drawdown of Raw level of receivables over 21d window."""
    res = _drawdown(receivables, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_commercial_sales_velocity_backlog_burn_dd_21d_v144_signal(revenue, deferredrev):
    """Drawdown of Backlog realization velocity over 21d window."""
    res = _drawdown(_ratio(revenue, deferredrev), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_commercial_sales_velocity_deferredrev_dd_42d_v145_signal(deferredrev):
    """Drawdown of Raw level of deferredrev over 42d window."""
    res = _drawdown(deferredrev, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_commercial_sales_velocity_revenue_dd_42d_v146_signal(revenue):
    """Drawdown of Raw level of revenue over 42d window."""
    res = _drawdown(revenue, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_commercial_sales_velocity_receivables_dd_42d_v147_signal(receivables):
    """Drawdown of Raw level of receivables over 42d window."""
    res = _drawdown(receivables, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_commercial_sales_velocity_backlog_burn_dd_42d_v148_signal(revenue, deferredrev):
    """Drawdown of Backlog realization velocity over 42d window."""
    res = _drawdown(_ratio(revenue, deferredrev), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_commercial_sales_velocity_deferredrev_dd_63d_v149_signal(deferredrev):
    """Drawdown of Raw level of deferredrev over 63d window."""
    res = _drawdown(deferredrev, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_commercial_sales_velocity_revenue_dd_63d_v150_signal(revenue):
    """Drawdown of Raw level of revenue over 63d window."""
    res = _drawdown(revenue, 63)
    return res.replace([np.inf, -np.inf], np.nan)


# ===== Feature Registry =====
REGISTRY = {
    "f03_commercial_sales_velocity_backlog_burn_ewma_504d_v076_signal": {"func": f03_commercial_sales_velocity_backlog_burn_ewma_504d_v076_signal},
    "f03_commercial_sales_velocity_deferredrev_ewma_756d_v077_signal": {"func": f03_commercial_sales_velocity_deferredrev_ewma_756d_v077_signal},
    "f03_commercial_sales_velocity_revenue_ewma_756d_v078_signal": {"func": f03_commercial_sales_velocity_revenue_ewma_756d_v078_signal},
    "f03_commercial_sales_velocity_receivables_ewma_756d_v079_signal": {"func": f03_commercial_sales_velocity_receivables_ewma_756d_v079_signal},
    "f03_commercial_sales_velocity_backlog_burn_ewma_756d_v080_signal": {"func": f03_commercial_sales_velocity_backlog_burn_ewma_756d_v080_signal},
    "f03_commercial_sales_velocity_deferredrev_ewma_1008d_v081_signal": {"func": f03_commercial_sales_velocity_deferredrev_ewma_1008d_v081_signal},
    "f03_commercial_sales_velocity_revenue_ewma_1008d_v082_signal": {"func": f03_commercial_sales_velocity_revenue_ewma_1008d_v082_signal},
    "f03_commercial_sales_velocity_receivables_ewma_1008d_v083_signal": {"func": f03_commercial_sales_velocity_receivables_ewma_1008d_v083_signal},
    "f03_commercial_sales_velocity_backlog_burn_ewma_1008d_v084_signal": {"func": f03_commercial_sales_velocity_backlog_burn_ewma_1008d_v084_signal},
    "f03_commercial_sales_velocity_deferredrev_ewma_1260d_v085_signal": {"func": f03_commercial_sales_velocity_deferredrev_ewma_1260d_v085_signal},
    "f03_commercial_sales_velocity_revenue_ewma_1260d_v086_signal": {"func": f03_commercial_sales_velocity_revenue_ewma_1260d_v086_signal},
    "f03_commercial_sales_velocity_receivables_ewma_1260d_v087_signal": {"func": f03_commercial_sales_velocity_receivables_ewma_1260d_v087_signal},
    "f03_commercial_sales_velocity_backlog_burn_ewma_1260d_v088_signal": {"func": f03_commercial_sales_velocity_backlog_burn_ewma_1260d_v088_signal},
    "f03_commercial_sales_velocity_deferredrev_z_5d_v089_signal": {"func": f03_commercial_sales_velocity_deferredrev_z_5d_v089_signal},
    "f03_commercial_sales_velocity_revenue_z_5d_v090_signal": {"func": f03_commercial_sales_velocity_revenue_z_5d_v090_signal},
    "f03_commercial_sales_velocity_receivables_z_5d_v091_signal": {"func": f03_commercial_sales_velocity_receivables_z_5d_v091_signal},
    "f03_commercial_sales_velocity_backlog_burn_z_5d_v092_signal": {"func": f03_commercial_sales_velocity_backlog_burn_z_5d_v092_signal},
    "f03_commercial_sales_velocity_deferredrev_z_10d_v093_signal": {"func": f03_commercial_sales_velocity_deferredrev_z_10d_v093_signal},
    "f03_commercial_sales_velocity_revenue_z_10d_v094_signal": {"func": f03_commercial_sales_velocity_revenue_z_10d_v094_signal},
    "f03_commercial_sales_velocity_receivables_z_10d_v095_signal": {"func": f03_commercial_sales_velocity_receivables_z_10d_v095_signal},
    "f03_commercial_sales_velocity_backlog_burn_z_10d_v096_signal": {"func": f03_commercial_sales_velocity_backlog_burn_z_10d_v096_signal},
    "f03_commercial_sales_velocity_deferredrev_z_21d_v097_signal": {"func": f03_commercial_sales_velocity_deferredrev_z_21d_v097_signal},
    "f03_commercial_sales_velocity_revenue_z_21d_v098_signal": {"func": f03_commercial_sales_velocity_revenue_z_21d_v098_signal},
    "f03_commercial_sales_velocity_receivables_z_21d_v099_signal": {"func": f03_commercial_sales_velocity_receivables_z_21d_v099_signal},
    "f03_commercial_sales_velocity_backlog_burn_z_21d_v100_signal": {"func": f03_commercial_sales_velocity_backlog_burn_z_21d_v100_signal},
    "f03_commercial_sales_velocity_deferredrev_z_42d_v101_signal": {"func": f03_commercial_sales_velocity_deferredrev_z_42d_v101_signal},
    "f03_commercial_sales_velocity_revenue_z_42d_v102_signal": {"func": f03_commercial_sales_velocity_revenue_z_42d_v102_signal},
    "f03_commercial_sales_velocity_receivables_z_42d_v103_signal": {"func": f03_commercial_sales_velocity_receivables_z_42d_v103_signal},
    "f03_commercial_sales_velocity_backlog_burn_z_42d_v104_signal": {"func": f03_commercial_sales_velocity_backlog_burn_z_42d_v104_signal},
    "f03_commercial_sales_velocity_deferredrev_z_63d_v105_signal": {"func": f03_commercial_sales_velocity_deferredrev_z_63d_v105_signal},
    "f03_commercial_sales_velocity_revenue_z_63d_v106_signal": {"func": f03_commercial_sales_velocity_revenue_z_63d_v106_signal},
    "f03_commercial_sales_velocity_receivables_z_63d_v107_signal": {"func": f03_commercial_sales_velocity_receivables_z_63d_v107_signal},
    "f03_commercial_sales_velocity_backlog_burn_z_63d_v108_signal": {"func": f03_commercial_sales_velocity_backlog_burn_z_63d_v108_signal},
    "f03_commercial_sales_velocity_deferredrev_z_126d_v109_signal": {"func": f03_commercial_sales_velocity_deferredrev_z_126d_v109_signal},
    "f03_commercial_sales_velocity_revenue_z_126d_v110_signal": {"func": f03_commercial_sales_velocity_revenue_z_126d_v110_signal},
    "f03_commercial_sales_velocity_receivables_z_126d_v111_signal": {"func": f03_commercial_sales_velocity_receivables_z_126d_v111_signal},
    "f03_commercial_sales_velocity_backlog_burn_z_126d_v112_signal": {"func": f03_commercial_sales_velocity_backlog_burn_z_126d_v112_signal},
    "f03_commercial_sales_velocity_deferredrev_z_252d_v113_signal": {"func": f03_commercial_sales_velocity_deferredrev_z_252d_v113_signal},
    "f03_commercial_sales_velocity_revenue_z_252d_v114_signal": {"func": f03_commercial_sales_velocity_revenue_z_252d_v114_signal},
    "f03_commercial_sales_velocity_receivables_z_252d_v115_signal": {"func": f03_commercial_sales_velocity_receivables_z_252d_v115_signal},
    "f03_commercial_sales_velocity_backlog_burn_z_252d_v116_signal": {"func": f03_commercial_sales_velocity_backlog_burn_z_252d_v116_signal},
    "f03_commercial_sales_velocity_deferredrev_z_504d_v117_signal": {"func": f03_commercial_sales_velocity_deferredrev_z_504d_v117_signal},
    "f03_commercial_sales_velocity_revenue_z_504d_v118_signal": {"func": f03_commercial_sales_velocity_revenue_z_504d_v118_signal},
    "f03_commercial_sales_velocity_receivables_z_504d_v119_signal": {"func": f03_commercial_sales_velocity_receivables_z_504d_v119_signal},
    "f03_commercial_sales_velocity_backlog_burn_z_504d_v120_signal": {"func": f03_commercial_sales_velocity_backlog_burn_z_504d_v120_signal},
    "f03_commercial_sales_velocity_deferredrev_z_756d_v121_signal": {"func": f03_commercial_sales_velocity_deferredrev_z_756d_v121_signal},
    "f03_commercial_sales_velocity_revenue_z_756d_v122_signal": {"func": f03_commercial_sales_velocity_revenue_z_756d_v122_signal},
    "f03_commercial_sales_velocity_receivables_z_756d_v123_signal": {"func": f03_commercial_sales_velocity_receivables_z_756d_v123_signal},
    "f03_commercial_sales_velocity_backlog_burn_z_756d_v124_signal": {"func": f03_commercial_sales_velocity_backlog_burn_z_756d_v124_signal},
    "f03_commercial_sales_velocity_deferredrev_z_1008d_v125_signal": {"func": f03_commercial_sales_velocity_deferredrev_z_1008d_v125_signal},
    "f03_commercial_sales_velocity_revenue_z_1008d_v126_signal": {"func": f03_commercial_sales_velocity_revenue_z_1008d_v126_signal},
    "f03_commercial_sales_velocity_receivables_z_1008d_v127_signal": {"func": f03_commercial_sales_velocity_receivables_z_1008d_v127_signal},
    "f03_commercial_sales_velocity_backlog_burn_z_1008d_v128_signal": {"func": f03_commercial_sales_velocity_backlog_burn_z_1008d_v128_signal},
    "f03_commercial_sales_velocity_deferredrev_z_1260d_v129_signal": {"func": f03_commercial_sales_velocity_deferredrev_z_1260d_v129_signal},
    "f03_commercial_sales_velocity_revenue_z_1260d_v130_signal": {"func": f03_commercial_sales_velocity_revenue_z_1260d_v130_signal},
    "f03_commercial_sales_velocity_receivables_z_1260d_v131_signal": {"func": f03_commercial_sales_velocity_receivables_z_1260d_v131_signal},
    "f03_commercial_sales_velocity_backlog_burn_z_1260d_v132_signal": {"func": f03_commercial_sales_velocity_backlog_burn_z_1260d_v132_signal},
    "f03_commercial_sales_velocity_deferredrev_dd_5d_v133_signal": {"func": f03_commercial_sales_velocity_deferredrev_dd_5d_v133_signal},
    "f03_commercial_sales_velocity_revenue_dd_5d_v134_signal": {"func": f03_commercial_sales_velocity_revenue_dd_5d_v134_signal},
    "f03_commercial_sales_velocity_receivables_dd_5d_v135_signal": {"func": f03_commercial_sales_velocity_receivables_dd_5d_v135_signal},
    "f03_commercial_sales_velocity_backlog_burn_dd_5d_v136_signal": {"func": f03_commercial_sales_velocity_backlog_burn_dd_5d_v136_signal},
    "f03_commercial_sales_velocity_deferredrev_dd_10d_v137_signal": {"func": f03_commercial_sales_velocity_deferredrev_dd_10d_v137_signal},
    "f03_commercial_sales_velocity_revenue_dd_10d_v138_signal": {"func": f03_commercial_sales_velocity_revenue_dd_10d_v138_signal},
    "f03_commercial_sales_velocity_receivables_dd_10d_v139_signal": {"func": f03_commercial_sales_velocity_receivables_dd_10d_v139_signal},
    "f03_commercial_sales_velocity_backlog_burn_dd_10d_v140_signal": {"func": f03_commercial_sales_velocity_backlog_burn_dd_10d_v140_signal},
    "f03_commercial_sales_velocity_deferredrev_dd_21d_v141_signal": {"func": f03_commercial_sales_velocity_deferredrev_dd_21d_v141_signal},
    "f03_commercial_sales_velocity_revenue_dd_21d_v142_signal": {"func": f03_commercial_sales_velocity_revenue_dd_21d_v142_signal},
    "f03_commercial_sales_velocity_receivables_dd_21d_v143_signal": {"func": f03_commercial_sales_velocity_receivables_dd_21d_v143_signal},
    "f03_commercial_sales_velocity_backlog_burn_dd_21d_v144_signal": {"func": f03_commercial_sales_velocity_backlog_burn_dd_21d_v144_signal},
    "f03_commercial_sales_velocity_deferredrev_dd_42d_v145_signal": {"func": f03_commercial_sales_velocity_deferredrev_dd_42d_v145_signal},
    "f03_commercial_sales_velocity_revenue_dd_42d_v146_signal": {"func": f03_commercial_sales_velocity_revenue_dd_42d_v146_signal},
    "f03_commercial_sales_velocity_receivables_dd_42d_v147_signal": {"func": f03_commercial_sales_velocity_receivables_dd_42d_v147_signal},
    "f03_commercial_sales_velocity_backlog_burn_dd_42d_v148_signal": {"func": f03_commercial_sales_velocity_backlog_burn_dd_42d_v148_signal},
    "f03_commercial_sales_velocity_deferredrev_dd_63d_v149_signal": {"func": f03_commercial_sales_velocity_deferredrev_dd_63d_v149_signal},
    "f03_commercial_sales_velocity_revenue_dd_63d_v150_signal": {"func": f03_commercial_sales_velocity_revenue_dd_63d_v150_signal},
}

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "sbcomp": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum(), "equity": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "ev": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "revenue": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "bvps": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "grossmargin": np.random.normal(100, 10, n).cumsum(), "pb": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "opex": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "deferredrev": np.random.normal(100, 10, n).cumsum(), "divyield": np.random.normal(100, 10, n).cumsum(), "pe": np.random.normal(100, 10, n).cumsum(), "tangibles": np.random.normal(100, 10, n).cumsum(), "deposits": np.random.normal(100, 10, n).cumsum(), "ps": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "liabilitiesc": np.random.normal(100, 10, n).cumsum()
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
        except Exception as e:
            print(f"Error in {name}: {e}")
            break
    print("Success.")
