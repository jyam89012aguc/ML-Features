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

def f38_spec_underwriting_uw_efficiency_ewma_504d_v076_signal(ebitdamargin, grossmargin):
    """Exponential moving average of Underwriting profit efficiency over 504d window."""
    res = _ewma(_ratio(ebitdamargin, grossmargin), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_grossmargin_ewma_756d_v077_signal(grossmargin):
    """Exponential moving average of Raw level of grossmargin over 756d window."""
    res = _ewma(grossmargin, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_ebitdamargin_ewma_756d_v078_signal(ebitdamargin):
    """Exponential moving average of Raw level of ebitdamargin over 756d window."""
    res = _ewma(ebitdamargin, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_revenue_ewma_756d_v079_signal(revenue):
    """Exponential moving average of Raw level of revenue over 756d window."""
    res = _ewma(revenue, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_uw_efficiency_ewma_756d_v080_signal(ebitdamargin, grossmargin):
    """Exponential moving average of Underwriting profit efficiency over 756d window."""
    res = _ewma(_ratio(ebitdamargin, grossmargin), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_grossmargin_ewma_1008d_v081_signal(grossmargin):
    """Exponential moving average of Raw level of grossmargin over 1008d window."""
    res = _ewma(grossmargin, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_ebitdamargin_ewma_1008d_v082_signal(ebitdamargin):
    """Exponential moving average of Raw level of ebitdamargin over 1008d window."""
    res = _ewma(ebitdamargin, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_revenue_ewma_1008d_v083_signal(revenue):
    """Exponential moving average of Raw level of revenue over 1008d window."""
    res = _ewma(revenue, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_uw_efficiency_ewma_1008d_v084_signal(ebitdamargin, grossmargin):
    """Exponential moving average of Underwriting profit efficiency over 1008d window."""
    res = _ewma(_ratio(ebitdamargin, grossmargin), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_grossmargin_ewma_1260d_v085_signal(grossmargin):
    """Exponential moving average of Raw level of grossmargin over 1260d window."""
    res = _ewma(grossmargin, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_ebitdamargin_ewma_1260d_v086_signal(ebitdamargin):
    """Exponential moving average of Raw level of ebitdamargin over 1260d window."""
    res = _ewma(ebitdamargin, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_revenue_ewma_1260d_v087_signal(revenue):
    """Exponential moving average of Raw level of revenue over 1260d window."""
    res = _ewma(revenue, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_uw_efficiency_ewma_1260d_v088_signal(ebitdamargin, grossmargin):
    """Exponential moving average of Underwriting profit efficiency over 1260d window."""
    res = _ewma(_ratio(ebitdamargin, grossmargin), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_grossmargin_z_5d_v089_signal(grossmargin):
    """Z-score of Raw level of grossmargin over 5d window."""
    res = _z(grossmargin, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_ebitdamargin_z_5d_v090_signal(ebitdamargin):
    """Z-score of Raw level of ebitdamargin over 5d window."""
    res = _z(ebitdamargin, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_revenue_z_5d_v091_signal(revenue):
    """Z-score of Raw level of revenue over 5d window."""
    res = _z(revenue, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_uw_efficiency_z_5d_v092_signal(ebitdamargin, grossmargin):
    """Z-score of Underwriting profit efficiency over 5d window."""
    res = _z(_ratio(ebitdamargin, grossmargin), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_grossmargin_z_10d_v093_signal(grossmargin):
    """Z-score of Raw level of grossmargin over 10d window."""
    res = _z(grossmargin, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_ebitdamargin_z_10d_v094_signal(ebitdamargin):
    """Z-score of Raw level of ebitdamargin over 10d window."""
    res = _z(ebitdamargin, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_revenue_z_10d_v095_signal(revenue):
    """Z-score of Raw level of revenue over 10d window."""
    res = _z(revenue, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_uw_efficiency_z_10d_v096_signal(ebitdamargin, grossmargin):
    """Z-score of Underwriting profit efficiency over 10d window."""
    res = _z(_ratio(ebitdamargin, grossmargin), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_grossmargin_z_21d_v097_signal(grossmargin):
    """Z-score of Raw level of grossmargin over 21d window."""
    res = _z(grossmargin, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_ebitdamargin_z_21d_v098_signal(ebitdamargin):
    """Z-score of Raw level of ebitdamargin over 21d window."""
    res = _z(ebitdamargin, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_revenue_z_21d_v099_signal(revenue):
    """Z-score of Raw level of revenue over 21d window."""
    res = _z(revenue, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_uw_efficiency_z_21d_v100_signal(ebitdamargin, grossmargin):
    """Z-score of Underwriting profit efficiency over 21d window."""
    res = _z(_ratio(ebitdamargin, grossmargin), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_grossmargin_z_42d_v101_signal(grossmargin):
    """Z-score of Raw level of grossmargin over 42d window."""
    res = _z(grossmargin, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_ebitdamargin_z_42d_v102_signal(ebitdamargin):
    """Z-score of Raw level of ebitdamargin over 42d window."""
    res = _z(ebitdamargin, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_revenue_z_42d_v103_signal(revenue):
    """Z-score of Raw level of revenue over 42d window."""
    res = _z(revenue, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_uw_efficiency_z_42d_v104_signal(ebitdamargin, grossmargin):
    """Z-score of Underwriting profit efficiency over 42d window."""
    res = _z(_ratio(ebitdamargin, grossmargin), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_grossmargin_z_63d_v105_signal(grossmargin):
    """Z-score of Raw level of grossmargin over 63d window."""
    res = _z(grossmargin, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_ebitdamargin_z_63d_v106_signal(ebitdamargin):
    """Z-score of Raw level of ebitdamargin over 63d window."""
    res = _z(ebitdamargin, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_revenue_z_63d_v107_signal(revenue):
    """Z-score of Raw level of revenue over 63d window."""
    res = _z(revenue, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_uw_efficiency_z_63d_v108_signal(ebitdamargin, grossmargin):
    """Z-score of Underwriting profit efficiency over 63d window."""
    res = _z(_ratio(ebitdamargin, grossmargin), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_grossmargin_z_126d_v109_signal(grossmargin):
    """Z-score of Raw level of grossmargin over 126d window."""
    res = _z(grossmargin, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_ebitdamargin_z_126d_v110_signal(ebitdamargin):
    """Z-score of Raw level of ebitdamargin over 126d window."""
    res = _z(ebitdamargin, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_revenue_z_126d_v111_signal(revenue):
    """Z-score of Raw level of revenue over 126d window."""
    res = _z(revenue, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_uw_efficiency_z_126d_v112_signal(ebitdamargin, grossmargin):
    """Z-score of Underwriting profit efficiency over 126d window."""
    res = _z(_ratio(ebitdamargin, grossmargin), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_grossmargin_z_252d_v113_signal(grossmargin):
    """Z-score of Raw level of grossmargin over 252d window."""
    res = _z(grossmargin, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_ebitdamargin_z_252d_v114_signal(ebitdamargin):
    """Z-score of Raw level of ebitdamargin over 252d window."""
    res = _z(ebitdamargin, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_revenue_z_252d_v115_signal(revenue):
    """Z-score of Raw level of revenue over 252d window."""
    res = _z(revenue, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_uw_efficiency_z_252d_v116_signal(ebitdamargin, grossmargin):
    """Z-score of Underwriting profit efficiency over 252d window."""
    res = _z(_ratio(ebitdamargin, grossmargin), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_grossmargin_z_504d_v117_signal(grossmargin):
    """Z-score of Raw level of grossmargin over 504d window."""
    res = _z(grossmargin, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_ebitdamargin_z_504d_v118_signal(ebitdamargin):
    """Z-score of Raw level of ebitdamargin over 504d window."""
    res = _z(ebitdamargin, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_revenue_z_504d_v119_signal(revenue):
    """Z-score of Raw level of revenue over 504d window."""
    res = _z(revenue, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_uw_efficiency_z_504d_v120_signal(ebitdamargin, grossmargin):
    """Z-score of Underwriting profit efficiency over 504d window."""
    res = _z(_ratio(ebitdamargin, grossmargin), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_grossmargin_z_756d_v121_signal(grossmargin):
    """Z-score of Raw level of grossmargin over 756d window."""
    res = _z(grossmargin, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_ebitdamargin_z_756d_v122_signal(ebitdamargin):
    """Z-score of Raw level of ebitdamargin over 756d window."""
    res = _z(ebitdamargin, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_revenue_z_756d_v123_signal(revenue):
    """Z-score of Raw level of revenue over 756d window."""
    res = _z(revenue, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_uw_efficiency_z_756d_v124_signal(ebitdamargin, grossmargin):
    """Z-score of Underwriting profit efficiency over 756d window."""
    res = _z(_ratio(ebitdamargin, grossmargin), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_grossmargin_z_1008d_v125_signal(grossmargin):
    """Z-score of Raw level of grossmargin over 1008d window."""
    res = _z(grossmargin, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_ebitdamargin_z_1008d_v126_signal(ebitdamargin):
    """Z-score of Raw level of ebitdamargin over 1008d window."""
    res = _z(ebitdamargin, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_revenue_z_1008d_v127_signal(revenue):
    """Z-score of Raw level of revenue over 1008d window."""
    res = _z(revenue, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_uw_efficiency_z_1008d_v128_signal(ebitdamargin, grossmargin):
    """Z-score of Underwriting profit efficiency over 1008d window."""
    res = _z(_ratio(ebitdamargin, grossmargin), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_grossmargin_z_1260d_v129_signal(grossmargin):
    """Z-score of Raw level of grossmargin over 1260d window."""
    res = _z(grossmargin, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_ebitdamargin_z_1260d_v130_signal(ebitdamargin):
    """Z-score of Raw level of ebitdamargin over 1260d window."""
    res = _z(ebitdamargin, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_revenue_z_1260d_v131_signal(revenue):
    """Z-score of Raw level of revenue over 1260d window."""
    res = _z(revenue, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_uw_efficiency_z_1260d_v132_signal(ebitdamargin, grossmargin):
    """Z-score of Underwriting profit efficiency over 1260d window."""
    res = _z(_ratio(ebitdamargin, grossmargin), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_grossmargin_dd_5d_v133_signal(grossmargin):
    """Drawdown of Raw level of grossmargin over 5d window."""
    res = _drawdown(grossmargin, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_ebitdamargin_dd_5d_v134_signal(ebitdamargin):
    """Drawdown of Raw level of ebitdamargin over 5d window."""
    res = _drawdown(ebitdamargin, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_revenue_dd_5d_v135_signal(revenue):
    """Drawdown of Raw level of revenue over 5d window."""
    res = _drawdown(revenue, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_uw_efficiency_dd_5d_v136_signal(ebitdamargin, grossmargin):
    """Drawdown of Underwriting profit efficiency over 5d window."""
    res = _drawdown(_ratio(ebitdamargin, grossmargin), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_grossmargin_dd_10d_v137_signal(grossmargin):
    """Drawdown of Raw level of grossmargin over 10d window."""
    res = _drawdown(grossmargin, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_ebitdamargin_dd_10d_v138_signal(ebitdamargin):
    """Drawdown of Raw level of ebitdamargin over 10d window."""
    res = _drawdown(ebitdamargin, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_revenue_dd_10d_v139_signal(revenue):
    """Drawdown of Raw level of revenue over 10d window."""
    res = _drawdown(revenue, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_uw_efficiency_dd_10d_v140_signal(ebitdamargin, grossmargin):
    """Drawdown of Underwriting profit efficiency over 10d window."""
    res = _drawdown(_ratio(ebitdamargin, grossmargin), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_grossmargin_dd_21d_v141_signal(grossmargin):
    """Drawdown of Raw level of grossmargin over 21d window."""
    res = _drawdown(grossmargin, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_ebitdamargin_dd_21d_v142_signal(ebitdamargin):
    """Drawdown of Raw level of ebitdamargin over 21d window."""
    res = _drawdown(ebitdamargin, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_revenue_dd_21d_v143_signal(revenue):
    """Drawdown of Raw level of revenue over 21d window."""
    res = _drawdown(revenue, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_uw_efficiency_dd_21d_v144_signal(ebitdamargin, grossmargin):
    """Drawdown of Underwriting profit efficiency over 21d window."""
    res = _drawdown(_ratio(ebitdamargin, grossmargin), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_grossmargin_dd_42d_v145_signal(grossmargin):
    """Drawdown of Raw level of grossmargin over 42d window."""
    res = _drawdown(grossmargin, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_ebitdamargin_dd_42d_v146_signal(ebitdamargin):
    """Drawdown of Raw level of ebitdamargin over 42d window."""
    res = _drawdown(ebitdamargin, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_revenue_dd_42d_v147_signal(revenue):
    """Drawdown of Raw level of revenue over 42d window."""
    res = _drawdown(revenue, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_uw_efficiency_dd_42d_v148_signal(ebitdamargin, grossmargin):
    """Drawdown of Underwriting profit efficiency over 42d window."""
    res = _drawdown(_ratio(ebitdamargin, grossmargin), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_grossmargin_dd_63d_v149_signal(grossmargin):
    """Drawdown of Raw level of grossmargin over 63d window."""
    res = _drawdown(grossmargin, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_spec_underwriting_ebitdamargin_dd_63d_v150_signal(ebitdamargin):
    """Drawdown of Raw level of ebitdamargin over 63d window."""
    res = _drawdown(ebitdamargin, 63)
    return res.replace([np.inf, -np.inf], np.nan)


# ===== Feature Registry =====
REGISTRY = {
    "f38_spec_underwriting_uw_efficiency_ewma_504d_v076_signal": {"func": f38_spec_underwriting_uw_efficiency_ewma_504d_v076_signal},
    "f38_spec_underwriting_grossmargin_ewma_756d_v077_signal": {"func": f38_spec_underwriting_grossmargin_ewma_756d_v077_signal},
    "f38_spec_underwriting_ebitdamargin_ewma_756d_v078_signal": {"func": f38_spec_underwriting_ebitdamargin_ewma_756d_v078_signal},
    "f38_spec_underwriting_revenue_ewma_756d_v079_signal": {"func": f38_spec_underwriting_revenue_ewma_756d_v079_signal},
    "f38_spec_underwriting_uw_efficiency_ewma_756d_v080_signal": {"func": f38_spec_underwriting_uw_efficiency_ewma_756d_v080_signal},
    "f38_spec_underwriting_grossmargin_ewma_1008d_v081_signal": {"func": f38_spec_underwriting_grossmargin_ewma_1008d_v081_signal},
    "f38_spec_underwriting_ebitdamargin_ewma_1008d_v082_signal": {"func": f38_spec_underwriting_ebitdamargin_ewma_1008d_v082_signal},
    "f38_spec_underwriting_revenue_ewma_1008d_v083_signal": {"func": f38_spec_underwriting_revenue_ewma_1008d_v083_signal},
    "f38_spec_underwriting_uw_efficiency_ewma_1008d_v084_signal": {"func": f38_spec_underwriting_uw_efficiency_ewma_1008d_v084_signal},
    "f38_spec_underwriting_grossmargin_ewma_1260d_v085_signal": {"func": f38_spec_underwriting_grossmargin_ewma_1260d_v085_signal},
    "f38_spec_underwriting_ebitdamargin_ewma_1260d_v086_signal": {"func": f38_spec_underwriting_ebitdamargin_ewma_1260d_v086_signal},
    "f38_spec_underwriting_revenue_ewma_1260d_v087_signal": {"func": f38_spec_underwriting_revenue_ewma_1260d_v087_signal},
    "f38_spec_underwriting_uw_efficiency_ewma_1260d_v088_signal": {"func": f38_spec_underwriting_uw_efficiency_ewma_1260d_v088_signal},
    "f38_spec_underwriting_grossmargin_z_5d_v089_signal": {"func": f38_spec_underwriting_grossmargin_z_5d_v089_signal},
    "f38_spec_underwriting_ebitdamargin_z_5d_v090_signal": {"func": f38_spec_underwriting_ebitdamargin_z_5d_v090_signal},
    "f38_spec_underwriting_revenue_z_5d_v091_signal": {"func": f38_spec_underwriting_revenue_z_5d_v091_signal},
    "f38_spec_underwriting_uw_efficiency_z_5d_v092_signal": {"func": f38_spec_underwriting_uw_efficiency_z_5d_v092_signal},
    "f38_spec_underwriting_grossmargin_z_10d_v093_signal": {"func": f38_spec_underwriting_grossmargin_z_10d_v093_signal},
    "f38_spec_underwriting_ebitdamargin_z_10d_v094_signal": {"func": f38_spec_underwriting_ebitdamargin_z_10d_v094_signal},
    "f38_spec_underwriting_revenue_z_10d_v095_signal": {"func": f38_spec_underwriting_revenue_z_10d_v095_signal},
    "f38_spec_underwriting_uw_efficiency_z_10d_v096_signal": {"func": f38_spec_underwriting_uw_efficiency_z_10d_v096_signal},
    "f38_spec_underwriting_grossmargin_z_21d_v097_signal": {"func": f38_spec_underwriting_grossmargin_z_21d_v097_signal},
    "f38_spec_underwriting_ebitdamargin_z_21d_v098_signal": {"func": f38_spec_underwriting_ebitdamargin_z_21d_v098_signal},
    "f38_spec_underwriting_revenue_z_21d_v099_signal": {"func": f38_spec_underwriting_revenue_z_21d_v099_signal},
    "f38_spec_underwriting_uw_efficiency_z_21d_v100_signal": {"func": f38_spec_underwriting_uw_efficiency_z_21d_v100_signal},
    "f38_spec_underwriting_grossmargin_z_42d_v101_signal": {"func": f38_spec_underwriting_grossmargin_z_42d_v101_signal},
    "f38_spec_underwriting_ebitdamargin_z_42d_v102_signal": {"func": f38_spec_underwriting_ebitdamargin_z_42d_v102_signal},
    "f38_spec_underwriting_revenue_z_42d_v103_signal": {"func": f38_spec_underwriting_revenue_z_42d_v103_signal},
    "f38_spec_underwriting_uw_efficiency_z_42d_v104_signal": {"func": f38_spec_underwriting_uw_efficiency_z_42d_v104_signal},
    "f38_spec_underwriting_grossmargin_z_63d_v105_signal": {"func": f38_spec_underwriting_grossmargin_z_63d_v105_signal},
    "f38_spec_underwriting_ebitdamargin_z_63d_v106_signal": {"func": f38_spec_underwriting_ebitdamargin_z_63d_v106_signal},
    "f38_spec_underwriting_revenue_z_63d_v107_signal": {"func": f38_spec_underwriting_revenue_z_63d_v107_signal},
    "f38_spec_underwriting_uw_efficiency_z_63d_v108_signal": {"func": f38_spec_underwriting_uw_efficiency_z_63d_v108_signal},
    "f38_spec_underwriting_grossmargin_z_126d_v109_signal": {"func": f38_spec_underwriting_grossmargin_z_126d_v109_signal},
    "f38_spec_underwriting_ebitdamargin_z_126d_v110_signal": {"func": f38_spec_underwriting_ebitdamargin_z_126d_v110_signal},
    "f38_spec_underwriting_revenue_z_126d_v111_signal": {"func": f38_spec_underwriting_revenue_z_126d_v111_signal},
    "f38_spec_underwriting_uw_efficiency_z_126d_v112_signal": {"func": f38_spec_underwriting_uw_efficiency_z_126d_v112_signal},
    "f38_spec_underwriting_grossmargin_z_252d_v113_signal": {"func": f38_spec_underwriting_grossmargin_z_252d_v113_signal},
    "f38_spec_underwriting_ebitdamargin_z_252d_v114_signal": {"func": f38_spec_underwriting_ebitdamargin_z_252d_v114_signal},
    "f38_spec_underwriting_revenue_z_252d_v115_signal": {"func": f38_spec_underwriting_revenue_z_252d_v115_signal},
    "f38_spec_underwriting_uw_efficiency_z_252d_v116_signal": {"func": f38_spec_underwriting_uw_efficiency_z_252d_v116_signal},
    "f38_spec_underwriting_grossmargin_z_504d_v117_signal": {"func": f38_spec_underwriting_grossmargin_z_504d_v117_signal},
    "f38_spec_underwriting_ebitdamargin_z_504d_v118_signal": {"func": f38_spec_underwriting_ebitdamargin_z_504d_v118_signal},
    "f38_spec_underwriting_revenue_z_504d_v119_signal": {"func": f38_spec_underwriting_revenue_z_504d_v119_signal},
    "f38_spec_underwriting_uw_efficiency_z_504d_v120_signal": {"func": f38_spec_underwriting_uw_efficiency_z_504d_v120_signal},
    "f38_spec_underwriting_grossmargin_z_756d_v121_signal": {"func": f38_spec_underwriting_grossmargin_z_756d_v121_signal},
    "f38_spec_underwriting_ebitdamargin_z_756d_v122_signal": {"func": f38_spec_underwriting_ebitdamargin_z_756d_v122_signal},
    "f38_spec_underwriting_revenue_z_756d_v123_signal": {"func": f38_spec_underwriting_revenue_z_756d_v123_signal},
    "f38_spec_underwriting_uw_efficiency_z_756d_v124_signal": {"func": f38_spec_underwriting_uw_efficiency_z_756d_v124_signal},
    "f38_spec_underwriting_grossmargin_z_1008d_v125_signal": {"func": f38_spec_underwriting_grossmargin_z_1008d_v125_signal},
    "f38_spec_underwriting_ebitdamargin_z_1008d_v126_signal": {"func": f38_spec_underwriting_ebitdamargin_z_1008d_v126_signal},
    "f38_spec_underwriting_revenue_z_1008d_v127_signal": {"func": f38_spec_underwriting_revenue_z_1008d_v127_signal},
    "f38_spec_underwriting_uw_efficiency_z_1008d_v128_signal": {"func": f38_spec_underwriting_uw_efficiency_z_1008d_v128_signal},
    "f38_spec_underwriting_grossmargin_z_1260d_v129_signal": {"func": f38_spec_underwriting_grossmargin_z_1260d_v129_signal},
    "f38_spec_underwriting_ebitdamargin_z_1260d_v130_signal": {"func": f38_spec_underwriting_ebitdamargin_z_1260d_v130_signal},
    "f38_spec_underwriting_revenue_z_1260d_v131_signal": {"func": f38_spec_underwriting_revenue_z_1260d_v131_signal},
    "f38_spec_underwriting_uw_efficiency_z_1260d_v132_signal": {"func": f38_spec_underwriting_uw_efficiency_z_1260d_v132_signal},
    "f38_spec_underwriting_grossmargin_dd_5d_v133_signal": {"func": f38_spec_underwriting_grossmargin_dd_5d_v133_signal},
    "f38_spec_underwriting_ebitdamargin_dd_5d_v134_signal": {"func": f38_spec_underwriting_ebitdamargin_dd_5d_v134_signal},
    "f38_spec_underwriting_revenue_dd_5d_v135_signal": {"func": f38_spec_underwriting_revenue_dd_5d_v135_signal},
    "f38_spec_underwriting_uw_efficiency_dd_5d_v136_signal": {"func": f38_spec_underwriting_uw_efficiency_dd_5d_v136_signal},
    "f38_spec_underwriting_grossmargin_dd_10d_v137_signal": {"func": f38_spec_underwriting_grossmargin_dd_10d_v137_signal},
    "f38_spec_underwriting_ebitdamargin_dd_10d_v138_signal": {"func": f38_spec_underwriting_ebitdamargin_dd_10d_v138_signal},
    "f38_spec_underwriting_revenue_dd_10d_v139_signal": {"func": f38_spec_underwriting_revenue_dd_10d_v139_signal},
    "f38_spec_underwriting_uw_efficiency_dd_10d_v140_signal": {"func": f38_spec_underwriting_uw_efficiency_dd_10d_v140_signal},
    "f38_spec_underwriting_grossmargin_dd_21d_v141_signal": {"func": f38_spec_underwriting_grossmargin_dd_21d_v141_signal},
    "f38_spec_underwriting_ebitdamargin_dd_21d_v142_signal": {"func": f38_spec_underwriting_ebitdamargin_dd_21d_v142_signal},
    "f38_spec_underwriting_revenue_dd_21d_v143_signal": {"func": f38_spec_underwriting_revenue_dd_21d_v143_signal},
    "f38_spec_underwriting_uw_efficiency_dd_21d_v144_signal": {"func": f38_spec_underwriting_uw_efficiency_dd_21d_v144_signal},
    "f38_spec_underwriting_grossmargin_dd_42d_v145_signal": {"func": f38_spec_underwriting_grossmargin_dd_42d_v145_signal},
    "f38_spec_underwriting_ebitdamargin_dd_42d_v146_signal": {"func": f38_spec_underwriting_ebitdamargin_dd_42d_v146_signal},
    "f38_spec_underwriting_revenue_dd_42d_v147_signal": {"func": f38_spec_underwriting_revenue_dd_42d_v147_signal},
    "f38_spec_underwriting_uw_efficiency_dd_42d_v148_signal": {"func": f38_spec_underwriting_uw_efficiency_dd_42d_v148_signal},
    "f38_spec_underwriting_grossmargin_dd_63d_v149_signal": {"func": f38_spec_underwriting_grossmargin_dd_63d_v149_signal},
    "f38_spec_underwriting_ebitdamargin_dd_63d_v150_signal": {"func": f38_spec_underwriting_ebitdamargin_dd_63d_v150_signal},
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
