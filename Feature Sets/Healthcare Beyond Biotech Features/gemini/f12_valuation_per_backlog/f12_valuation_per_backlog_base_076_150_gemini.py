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

def f12_valuation_per_backlog_sales_efficiency_ewma_504d_v076_signal(revenue, sgna):
    """Exponential moving average of Revenue yield on sales spend over 504d window."""
    res = _ewma(_ratio(revenue, sgna), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_valuation_per_backlog_sgna_ewma_756d_v077_signal(sgna):
    """Exponential moving average of Raw level of sgna over 756d window."""
    res = _ewma(sgna, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_valuation_per_backlog_revenue_ewma_756d_v078_signal(revenue):
    """Exponential moving average of Raw level of revenue over 756d window."""
    res = _ewma(revenue, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_valuation_per_backlog_netinc_ewma_756d_v079_signal(netinc):
    """Exponential moving average of Raw level of netinc over 756d window."""
    res = _ewma(netinc, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_valuation_per_backlog_sales_efficiency_ewma_756d_v080_signal(revenue, sgna):
    """Exponential moving average of Revenue yield on sales spend over 756d window."""
    res = _ewma(_ratio(revenue, sgna), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_valuation_per_backlog_sgna_ewma_1008d_v081_signal(sgna):
    """Exponential moving average of Raw level of sgna over 1008d window."""
    res = _ewma(sgna, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_valuation_per_backlog_revenue_ewma_1008d_v082_signal(revenue):
    """Exponential moving average of Raw level of revenue over 1008d window."""
    res = _ewma(revenue, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_valuation_per_backlog_netinc_ewma_1008d_v083_signal(netinc):
    """Exponential moving average of Raw level of netinc over 1008d window."""
    res = _ewma(netinc, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_valuation_per_backlog_sales_efficiency_ewma_1008d_v084_signal(revenue, sgna):
    """Exponential moving average of Revenue yield on sales spend over 1008d window."""
    res = _ewma(_ratio(revenue, sgna), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_valuation_per_backlog_sgna_ewma_1260d_v085_signal(sgna):
    """Exponential moving average of Raw level of sgna over 1260d window."""
    res = _ewma(sgna, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_valuation_per_backlog_revenue_ewma_1260d_v086_signal(revenue):
    """Exponential moving average of Raw level of revenue over 1260d window."""
    res = _ewma(revenue, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_valuation_per_backlog_netinc_ewma_1260d_v087_signal(netinc):
    """Exponential moving average of Raw level of netinc over 1260d window."""
    res = _ewma(netinc, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_valuation_per_backlog_sales_efficiency_ewma_1260d_v088_signal(revenue, sgna):
    """Exponential moving average of Revenue yield on sales spend over 1260d window."""
    res = _ewma(_ratio(revenue, sgna), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_valuation_per_backlog_sgna_z_5d_v089_signal(sgna):
    """Z-score of Raw level of sgna over 5d window."""
    res = _z(sgna, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_valuation_per_backlog_revenue_z_5d_v090_signal(revenue):
    """Z-score of Raw level of revenue over 5d window."""
    res = _z(revenue, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_valuation_per_backlog_netinc_z_5d_v091_signal(netinc):
    """Z-score of Raw level of netinc over 5d window."""
    res = _z(netinc, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_valuation_per_backlog_sales_efficiency_z_5d_v092_signal(revenue, sgna):
    """Z-score of Revenue yield on sales spend over 5d window."""
    res = _z(_ratio(revenue, sgna), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_valuation_per_backlog_sgna_z_10d_v093_signal(sgna):
    """Z-score of Raw level of sgna over 10d window."""
    res = _z(sgna, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_valuation_per_backlog_revenue_z_10d_v094_signal(revenue):
    """Z-score of Raw level of revenue over 10d window."""
    res = _z(revenue, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_valuation_per_backlog_netinc_z_10d_v095_signal(netinc):
    """Z-score of Raw level of netinc over 10d window."""
    res = _z(netinc, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_valuation_per_backlog_sales_efficiency_z_10d_v096_signal(revenue, sgna):
    """Z-score of Revenue yield on sales spend over 10d window."""
    res = _z(_ratio(revenue, sgna), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_valuation_per_backlog_sgna_z_21d_v097_signal(sgna):
    """Z-score of Raw level of sgna over 21d window."""
    res = _z(sgna, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_valuation_per_backlog_revenue_z_21d_v098_signal(revenue):
    """Z-score of Raw level of revenue over 21d window."""
    res = _z(revenue, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_valuation_per_backlog_netinc_z_21d_v099_signal(netinc):
    """Z-score of Raw level of netinc over 21d window."""
    res = _z(netinc, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_valuation_per_backlog_sales_efficiency_z_21d_v100_signal(revenue, sgna):
    """Z-score of Revenue yield on sales spend over 21d window."""
    res = _z(_ratio(revenue, sgna), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_valuation_per_backlog_sgna_z_42d_v101_signal(sgna):
    """Z-score of Raw level of sgna over 42d window."""
    res = _z(sgna, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_valuation_per_backlog_revenue_z_42d_v102_signal(revenue):
    """Z-score of Raw level of revenue over 42d window."""
    res = _z(revenue, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_valuation_per_backlog_netinc_z_42d_v103_signal(netinc):
    """Z-score of Raw level of netinc over 42d window."""
    res = _z(netinc, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_valuation_per_backlog_sales_efficiency_z_42d_v104_signal(revenue, sgna):
    """Z-score of Revenue yield on sales spend over 42d window."""
    res = _z(_ratio(revenue, sgna), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_valuation_per_backlog_sgna_z_63d_v105_signal(sgna):
    """Z-score of Raw level of sgna over 63d window."""
    res = _z(sgna, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_valuation_per_backlog_revenue_z_63d_v106_signal(revenue):
    """Z-score of Raw level of revenue over 63d window."""
    res = _z(revenue, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_valuation_per_backlog_netinc_z_63d_v107_signal(netinc):
    """Z-score of Raw level of netinc over 63d window."""
    res = _z(netinc, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_valuation_per_backlog_sales_efficiency_z_63d_v108_signal(revenue, sgna):
    """Z-score of Revenue yield on sales spend over 63d window."""
    res = _z(_ratio(revenue, sgna), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_valuation_per_backlog_sgna_z_126d_v109_signal(sgna):
    """Z-score of Raw level of sgna over 126d window."""
    res = _z(sgna, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_valuation_per_backlog_revenue_z_126d_v110_signal(revenue):
    """Z-score of Raw level of revenue over 126d window."""
    res = _z(revenue, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_valuation_per_backlog_netinc_z_126d_v111_signal(netinc):
    """Z-score of Raw level of netinc over 126d window."""
    res = _z(netinc, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_valuation_per_backlog_sales_efficiency_z_126d_v112_signal(revenue, sgna):
    """Z-score of Revenue yield on sales spend over 126d window."""
    res = _z(_ratio(revenue, sgna), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_valuation_per_backlog_sgna_z_252d_v113_signal(sgna):
    """Z-score of Raw level of sgna over 252d window."""
    res = _z(sgna, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_valuation_per_backlog_revenue_z_252d_v114_signal(revenue):
    """Z-score of Raw level of revenue over 252d window."""
    res = _z(revenue, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_valuation_per_backlog_netinc_z_252d_v115_signal(netinc):
    """Z-score of Raw level of netinc over 252d window."""
    res = _z(netinc, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_valuation_per_backlog_sales_efficiency_z_252d_v116_signal(revenue, sgna):
    """Z-score of Revenue yield on sales spend over 252d window."""
    res = _z(_ratio(revenue, sgna), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_valuation_per_backlog_sgna_z_504d_v117_signal(sgna):
    """Z-score of Raw level of sgna over 504d window."""
    res = _z(sgna, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_valuation_per_backlog_revenue_z_504d_v118_signal(revenue):
    """Z-score of Raw level of revenue over 504d window."""
    res = _z(revenue, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_valuation_per_backlog_netinc_z_504d_v119_signal(netinc):
    """Z-score of Raw level of netinc over 504d window."""
    res = _z(netinc, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_valuation_per_backlog_sales_efficiency_z_504d_v120_signal(revenue, sgna):
    """Z-score of Revenue yield on sales spend over 504d window."""
    res = _z(_ratio(revenue, sgna), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_valuation_per_backlog_sgna_z_756d_v121_signal(sgna):
    """Z-score of Raw level of sgna over 756d window."""
    res = _z(sgna, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_valuation_per_backlog_revenue_z_756d_v122_signal(revenue):
    """Z-score of Raw level of revenue over 756d window."""
    res = _z(revenue, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_valuation_per_backlog_netinc_z_756d_v123_signal(netinc):
    """Z-score of Raw level of netinc over 756d window."""
    res = _z(netinc, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_valuation_per_backlog_sales_efficiency_z_756d_v124_signal(revenue, sgna):
    """Z-score of Revenue yield on sales spend over 756d window."""
    res = _z(_ratio(revenue, sgna), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_valuation_per_backlog_sgna_z_1008d_v125_signal(sgna):
    """Z-score of Raw level of sgna over 1008d window."""
    res = _z(sgna, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_valuation_per_backlog_revenue_z_1008d_v126_signal(revenue):
    """Z-score of Raw level of revenue over 1008d window."""
    res = _z(revenue, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_valuation_per_backlog_netinc_z_1008d_v127_signal(netinc):
    """Z-score of Raw level of netinc over 1008d window."""
    res = _z(netinc, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_valuation_per_backlog_sales_efficiency_z_1008d_v128_signal(revenue, sgna):
    """Z-score of Revenue yield on sales spend over 1008d window."""
    res = _z(_ratio(revenue, sgna), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_valuation_per_backlog_sgna_z_1260d_v129_signal(sgna):
    """Z-score of Raw level of sgna over 1260d window."""
    res = _z(sgna, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_valuation_per_backlog_revenue_z_1260d_v130_signal(revenue):
    """Z-score of Raw level of revenue over 1260d window."""
    res = _z(revenue, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_valuation_per_backlog_netinc_z_1260d_v131_signal(netinc):
    """Z-score of Raw level of netinc over 1260d window."""
    res = _z(netinc, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_valuation_per_backlog_sales_efficiency_z_1260d_v132_signal(revenue, sgna):
    """Z-score of Revenue yield on sales spend over 1260d window."""
    res = _z(_ratio(revenue, sgna), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_valuation_per_backlog_sgna_dd_5d_v133_signal(sgna):
    """Drawdown of Raw level of sgna over 5d window."""
    res = _drawdown(sgna, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_valuation_per_backlog_revenue_dd_5d_v134_signal(revenue):
    """Drawdown of Raw level of revenue over 5d window."""
    res = _drawdown(revenue, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_valuation_per_backlog_netinc_dd_5d_v135_signal(netinc):
    """Drawdown of Raw level of netinc over 5d window."""
    res = _drawdown(netinc, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_valuation_per_backlog_sales_efficiency_dd_5d_v136_signal(revenue, sgna):
    """Drawdown of Revenue yield on sales spend over 5d window."""
    res = _drawdown(_ratio(revenue, sgna), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_valuation_per_backlog_sgna_dd_10d_v137_signal(sgna):
    """Drawdown of Raw level of sgna over 10d window."""
    res = _drawdown(sgna, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_valuation_per_backlog_revenue_dd_10d_v138_signal(revenue):
    """Drawdown of Raw level of revenue over 10d window."""
    res = _drawdown(revenue, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_valuation_per_backlog_netinc_dd_10d_v139_signal(netinc):
    """Drawdown of Raw level of netinc over 10d window."""
    res = _drawdown(netinc, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_valuation_per_backlog_sales_efficiency_dd_10d_v140_signal(revenue, sgna):
    """Drawdown of Revenue yield on sales spend over 10d window."""
    res = _drawdown(_ratio(revenue, sgna), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_valuation_per_backlog_sgna_dd_21d_v141_signal(sgna):
    """Drawdown of Raw level of sgna over 21d window."""
    res = _drawdown(sgna, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_valuation_per_backlog_revenue_dd_21d_v142_signal(revenue):
    """Drawdown of Raw level of revenue over 21d window."""
    res = _drawdown(revenue, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_valuation_per_backlog_netinc_dd_21d_v143_signal(netinc):
    """Drawdown of Raw level of netinc over 21d window."""
    res = _drawdown(netinc, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_valuation_per_backlog_sales_efficiency_dd_21d_v144_signal(revenue, sgna):
    """Drawdown of Revenue yield on sales spend over 21d window."""
    res = _drawdown(_ratio(revenue, sgna), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_valuation_per_backlog_sgna_dd_42d_v145_signal(sgna):
    """Drawdown of Raw level of sgna over 42d window."""
    res = _drawdown(sgna, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_valuation_per_backlog_revenue_dd_42d_v146_signal(revenue):
    """Drawdown of Raw level of revenue over 42d window."""
    res = _drawdown(revenue, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_valuation_per_backlog_netinc_dd_42d_v147_signal(netinc):
    """Drawdown of Raw level of netinc over 42d window."""
    res = _drawdown(netinc, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_valuation_per_backlog_sales_efficiency_dd_42d_v148_signal(revenue, sgna):
    """Drawdown of Revenue yield on sales spend over 42d window."""
    res = _drawdown(_ratio(revenue, sgna), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_valuation_per_backlog_sgna_dd_63d_v149_signal(sgna):
    """Drawdown of Raw level of sgna over 63d window."""
    res = _drawdown(sgna, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_valuation_per_backlog_revenue_dd_63d_v150_signal(revenue):
    """Drawdown of Raw level of revenue over 63d window."""
    res = _drawdown(revenue, 63)
    return res.replace([np.inf, -np.inf], np.nan)


# ===== Feature Registry =====
REGISTRY = {
    "f12_valuation_per_backlog_sales_efficiency_ewma_504d_v076_signal": {"func": f12_valuation_per_backlog_sales_efficiency_ewma_504d_v076_signal},
    "f12_valuation_per_backlog_sgna_ewma_756d_v077_signal": {"func": f12_valuation_per_backlog_sgna_ewma_756d_v077_signal},
    "f12_valuation_per_backlog_revenue_ewma_756d_v078_signal": {"func": f12_valuation_per_backlog_revenue_ewma_756d_v078_signal},
    "f12_valuation_per_backlog_netinc_ewma_756d_v079_signal": {"func": f12_valuation_per_backlog_netinc_ewma_756d_v079_signal},
    "f12_valuation_per_backlog_sales_efficiency_ewma_756d_v080_signal": {"func": f12_valuation_per_backlog_sales_efficiency_ewma_756d_v080_signal},
    "f12_valuation_per_backlog_sgna_ewma_1008d_v081_signal": {"func": f12_valuation_per_backlog_sgna_ewma_1008d_v081_signal},
    "f12_valuation_per_backlog_revenue_ewma_1008d_v082_signal": {"func": f12_valuation_per_backlog_revenue_ewma_1008d_v082_signal},
    "f12_valuation_per_backlog_netinc_ewma_1008d_v083_signal": {"func": f12_valuation_per_backlog_netinc_ewma_1008d_v083_signal},
    "f12_valuation_per_backlog_sales_efficiency_ewma_1008d_v084_signal": {"func": f12_valuation_per_backlog_sales_efficiency_ewma_1008d_v084_signal},
    "f12_valuation_per_backlog_sgna_ewma_1260d_v085_signal": {"func": f12_valuation_per_backlog_sgna_ewma_1260d_v085_signal},
    "f12_valuation_per_backlog_revenue_ewma_1260d_v086_signal": {"func": f12_valuation_per_backlog_revenue_ewma_1260d_v086_signal},
    "f12_valuation_per_backlog_netinc_ewma_1260d_v087_signal": {"func": f12_valuation_per_backlog_netinc_ewma_1260d_v087_signal},
    "f12_valuation_per_backlog_sales_efficiency_ewma_1260d_v088_signal": {"func": f12_valuation_per_backlog_sales_efficiency_ewma_1260d_v088_signal},
    "f12_valuation_per_backlog_sgna_z_5d_v089_signal": {"func": f12_valuation_per_backlog_sgna_z_5d_v089_signal},
    "f12_valuation_per_backlog_revenue_z_5d_v090_signal": {"func": f12_valuation_per_backlog_revenue_z_5d_v090_signal},
    "f12_valuation_per_backlog_netinc_z_5d_v091_signal": {"func": f12_valuation_per_backlog_netinc_z_5d_v091_signal},
    "f12_valuation_per_backlog_sales_efficiency_z_5d_v092_signal": {"func": f12_valuation_per_backlog_sales_efficiency_z_5d_v092_signal},
    "f12_valuation_per_backlog_sgna_z_10d_v093_signal": {"func": f12_valuation_per_backlog_sgna_z_10d_v093_signal},
    "f12_valuation_per_backlog_revenue_z_10d_v094_signal": {"func": f12_valuation_per_backlog_revenue_z_10d_v094_signal},
    "f12_valuation_per_backlog_netinc_z_10d_v095_signal": {"func": f12_valuation_per_backlog_netinc_z_10d_v095_signal},
    "f12_valuation_per_backlog_sales_efficiency_z_10d_v096_signal": {"func": f12_valuation_per_backlog_sales_efficiency_z_10d_v096_signal},
    "f12_valuation_per_backlog_sgna_z_21d_v097_signal": {"func": f12_valuation_per_backlog_sgna_z_21d_v097_signal},
    "f12_valuation_per_backlog_revenue_z_21d_v098_signal": {"func": f12_valuation_per_backlog_revenue_z_21d_v098_signal},
    "f12_valuation_per_backlog_netinc_z_21d_v099_signal": {"func": f12_valuation_per_backlog_netinc_z_21d_v099_signal},
    "f12_valuation_per_backlog_sales_efficiency_z_21d_v100_signal": {"func": f12_valuation_per_backlog_sales_efficiency_z_21d_v100_signal},
    "f12_valuation_per_backlog_sgna_z_42d_v101_signal": {"func": f12_valuation_per_backlog_sgna_z_42d_v101_signal},
    "f12_valuation_per_backlog_revenue_z_42d_v102_signal": {"func": f12_valuation_per_backlog_revenue_z_42d_v102_signal},
    "f12_valuation_per_backlog_netinc_z_42d_v103_signal": {"func": f12_valuation_per_backlog_netinc_z_42d_v103_signal},
    "f12_valuation_per_backlog_sales_efficiency_z_42d_v104_signal": {"func": f12_valuation_per_backlog_sales_efficiency_z_42d_v104_signal},
    "f12_valuation_per_backlog_sgna_z_63d_v105_signal": {"func": f12_valuation_per_backlog_sgna_z_63d_v105_signal},
    "f12_valuation_per_backlog_revenue_z_63d_v106_signal": {"func": f12_valuation_per_backlog_revenue_z_63d_v106_signal},
    "f12_valuation_per_backlog_netinc_z_63d_v107_signal": {"func": f12_valuation_per_backlog_netinc_z_63d_v107_signal},
    "f12_valuation_per_backlog_sales_efficiency_z_63d_v108_signal": {"func": f12_valuation_per_backlog_sales_efficiency_z_63d_v108_signal},
    "f12_valuation_per_backlog_sgna_z_126d_v109_signal": {"func": f12_valuation_per_backlog_sgna_z_126d_v109_signal},
    "f12_valuation_per_backlog_revenue_z_126d_v110_signal": {"func": f12_valuation_per_backlog_revenue_z_126d_v110_signal},
    "f12_valuation_per_backlog_netinc_z_126d_v111_signal": {"func": f12_valuation_per_backlog_netinc_z_126d_v111_signal},
    "f12_valuation_per_backlog_sales_efficiency_z_126d_v112_signal": {"func": f12_valuation_per_backlog_sales_efficiency_z_126d_v112_signal},
    "f12_valuation_per_backlog_sgna_z_252d_v113_signal": {"func": f12_valuation_per_backlog_sgna_z_252d_v113_signal},
    "f12_valuation_per_backlog_revenue_z_252d_v114_signal": {"func": f12_valuation_per_backlog_revenue_z_252d_v114_signal},
    "f12_valuation_per_backlog_netinc_z_252d_v115_signal": {"func": f12_valuation_per_backlog_netinc_z_252d_v115_signal},
    "f12_valuation_per_backlog_sales_efficiency_z_252d_v116_signal": {"func": f12_valuation_per_backlog_sales_efficiency_z_252d_v116_signal},
    "f12_valuation_per_backlog_sgna_z_504d_v117_signal": {"func": f12_valuation_per_backlog_sgna_z_504d_v117_signal},
    "f12_valuation_per_backlog_revenue_z_504d_v118_signal": {"func": f12_valuation_per_backlog_revenue_z_504d_v118_signal},
    "f12_valuation_per_backlog_netinc_z_504d_v119_signal": {"func": f12_valuation_per_backlog_netinc_z_504d_v119_signal},
    "f12_valuation_per_backlog_sales_efficiency_z_504d_v120_signal": {"func": f12_valuation_per_backlog_sales_efficiency_z_504d_v120_signal},
    "f12_valuation_per_backlog_sgna_z_756d_v121_signal": {"func": f12_valuation_per_backlog_sgna_z_756d_v121_signal},
    "f12_valuation_per_backlog_revenue_z_756d_v122_signal": {"func": f12_valuation_per_backlog_revenue_z_756d_v122_signal},
    "f12_valuation_per_backlog_netinc_z_756d_v123_signal": {"func": f12_valuation_per_backlog_netinc_z_756d_v123_signal},
    "f12_valuation_per_backlog_sales_efficiency_z_756d_v124_signal": {"func": f12_valuation_per_backlog_sales_efficiency_z_756d_v124_signal},
    "f12_valuation_per_backlog_sgna_z_1008d_v125_signal": {"func": f12_valuation_per_backlog_sgna_z_1008d_v125_signal},
    "f12_valuation_per_backlog_revenue_z_1008d_v126_signal": {"func": f12_valuation_per_backlog_revenue_z_1008d_v126_signal},
    "f12_valuation_per_backlog_netinc_z_1008d_v127_signal": {"func": f12_valuation_per_backlog_netinc_z_1008d_v127_signal},
    "f12_valuation_per_backlog_sales_efficiency_z_1008d_v128_signal": {"func": f12_valuation_per_backlog_sales_efficiency_z_1008d_v128_signal},
    "f12_valuation_per_backlog_sgna_z_1260d_v129_signal": {"func": f12_valuation_per_backlog_sgna_z_1260d_v129_signal},
    "f12_valuation_per_backlog_revenue_z_1260d_v130_signal": {"func": f12_valuation_per_backlog_revenue_z_1260d_v130_signal},
    "f12_valuation_per_backlog_netinc_z_1260d_v131_signal": {"func": f12_valuation_per_backlog_netinc_z_1260d_v131_signal},
    "f12_valuation_per_backlog_sales_efficiency_z_1260d_v132_signal": {"func": f12_valuation_per_backlog_sales_efficiency_z_1260d_v132_signal},
    "f12_valuation_per_backlog_sgna_dd_5d_v133_signal": {"func": f12_valuation_per_backlog_sgna_dd_5d_v133_signal},
    "f12_valuation_per_backlog_revenue_dd_5d_v134_signal": {"func": f12_valuation_per_backlog_revenue_dd_5d_v134_signal},
    "f12_valuation_per_backlog_netinc_dd_5d_v135_signal": {"func": f12_valuation_per_backlog_netinc_dd_5d_v135_signal},
    "f12_valuation_per_backlog_sales_efficiency_dd_5d_v136_signal": {"func": f12_valuation_per_backlog_sales_efficiency_dd_5d_v136_signal},
    "f12_valuation_per_backlog_sgna_dd_10d_v137_signal": {"func": f12_valuation_per_backlog_sgna_dd_10d_v137_signal},
    "f12_valuation_per_backlog_revenue_dd_10d_v138_signal": {"func": f12_valuation_per_backlog_revenue_dd_10d_v138_signal},
    "f12_valuation_per_backlog_netinc_dd_10d_v139_signal": {"func": f12_valuation_per_backlog_netinc_dd_10d_v139_signal},
    "f12_valuation_per_backlog_sales_efficiency_dd_10d_v140_signal": {"func": f12_valuation_per_backlog_sales_efficiency_dd_10d_v140_signal},
    "f12_valuation_per_backlog_sgna_dd_21d_v141_signal": {"func": f12_valuation_per_backlog_sgna_dd_21d_v141_signal},
    "f12_valuation_per_backlog_revenue_dd_21d_v142_signal": {"func": f12_valuation_per_backlog_revenue_dd_21d_v142_signal},
    "f12_valuation_per_backlog_netinc_dd_21d_v143_signal": {"func": f12_valuation_per_backlog_netinc_dd_21d_v143_signal},
    "f12_valuation_per_backlog_sales_efficiency_dd_21d_v144_signal": {"func": f12_valuation_per_backlog_sales_efficiency_dd_21d_v144_signal},
    "f12_valuation_per_backlog_sgna_dd_42d_v145_signal": {"func": f12_valuation_per_backlog_sgna_dd_42d_v145_signal},
    "f12_valuation_per_backlog_revenue_dd_42d_v146_signal": {"func": f12_valuation_per_backlog_revenue_dd_42d_v146_signal},
    "f12_valuation_per_backlog_netinc_dd_42d_v147_signal": {"func": f12_valuation_per_backlog_netinc_dd_42d_v147_signal},
    "f12_valuation_per_backlog_sales_efficiency_dd_42d_v148_signal": {"func": f12_valuation_per_backlog_sales_efficiency_dd_42d_v148_signal},
    "f12_valuation_per_backlog_sgna_dd_63d_v149_signal": {"func": f12_valuation_per_backlog_sgna_dd_63d_v149_signal},
    "f12_valuation_per_backlog_revenue_dd_63d_v150_signal": {"func": f12_valuation_per_backlog_revenue_dd_63d_v150_signal},
}

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "sbcomp": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum(), "equity": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "ev": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "revenue": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "bvps": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "grossmargin": np.random.normal(100, 10, n).cumsum(), "pb": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "opex": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "deferredrev": np.random.normal(100, 10, n).cumsum(), "divyield": np.random.normal(100, 10, n).cumsum(), "pe": np.random.normal(100, 10, n).cumsum(), "tangibles": np.random.normal(100, 10, n).cumsum(), "deposits": np.random.normal(100, 10, n).cumsum(), "ps": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "liabilitiesc": np.random.normal(100, 10, n).cumsum()
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
        except Exception as e:
            print(f"Error in {name}: {e}")
            break
    print("Success.")
