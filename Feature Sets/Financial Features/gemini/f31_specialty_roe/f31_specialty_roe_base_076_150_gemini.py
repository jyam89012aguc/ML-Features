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

def f31_specialty_roe_adjusted_roe_ewma_504d_v076_signal(netinc, equity, roic):
    """Exponential moving average of ROIC-amplified ROE over 504d window."""
    res = _ewma(_ratio(netinc, equity) * roic, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_netinc_ewma_756d_v077_signal(netinc):
    """Exponential moving average of Raw level of netinc over 756d window."""
    res = _ewma(netinc, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_equity_ewma_756d_v078_signal(equity):
    """Exponential moving average of Raw level of equity over 756d window."""
    res = _ewma(equity, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_roic_ewma_756d_v079_signal(roic):
    """Exponential moving average of Raw level of roic over 756d window."""
    res = _ewma(roic, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_adjusted_roe_ewma_756d_v080_signal(netinc, equity, roic):
    """Exponential moving average of ROIC-amplified ROE over 756d window."""
    res = _ewma(_ratio(netinc, equity) * roic, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_netinc_ewma_1008d_v081_signal(netinc):
    """Exponential moving average of Raw level of netinc over 1008d window."""
    res = _ewma(netinc, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_equity_ewma_1008d_v082_signal(equity):
    """Exponential moving average of Raw level of equity over 1008d window."""
    res = _ewma(equity, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_roic_ewma_1008d_v083_signal(roic):
    """Exponential moving average of Raw level of roic over 1008d window."""
    res = _ewma(roic, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_adjusted_roe_ewma_1008d_v084_signal(netinc, equity, roic):
    """Exponential moving average of ROIC-amplified ROE over 1008d window."""
    res = _ewma(_ratio(netinc, equity) * roic, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_netinc_ewma_1260d_v085_signal(netinc):
    """Exponential moving average of Raw level of netinc over 1260d window."""
    res = _ewma(netinc, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_equity_ewma_1260d_v086_signal(equity):
    """Exponential moving average of Raw level of equity over 1260d window."""
    res = _ewma(equity, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_roic_ewma_1260d_v087_signal(roic):
    """Exponential moving average of Raw level of roic over 1260d window."""
    res = _ewma(roic, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_adjusted_roe_ewma_1260d_v088_signal(netinc, equity, roic):
    """Exponential moving average of ROIC-amplified ROE over 1260d window."""
    res = _ewma(_ratio(netinc, equity) * roic, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_netinc_z_5d_v089_signal(netinc):
    """Z-score of Raw level of netinc over 5d window."""
    res = _z(netinc, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_equity_z_5d_v090_signal(equity):
    """Z-score of Raw level of equity over 5d window."""
    res = _z(equity, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_roic_z_5d_v091_signal(roic):
    """Z-score of Raw level of roic over 5d window."""
    res = _z(roic, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_adjusted_roe_z_5d_v092_signal(netinc, equity, roic):
    """Z-score of ROIC-amplified ROE over 5d window."""
    res = _z(_ratio(netinc, equity) * roic, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_netinc_z_10d_v093_signal(netinc):
    """Z-score of Raw level of netinc over 10d window."""
    res = _z(netinc, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_equity_z_10d_v094_signal(equity):
    """Z-score of Raw level of equity over 10d window."""
    res = _z(equity, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_roic_z_10d_v095_signal(roic):
    """Z-score of Raw level of roic over 10d window."""
    res = _z(roic, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_adjusted_roe_z_10d_v096_signal(netinc, equity, roic):
    """Z-score of ROIC-amplified ROE over 10d window."""
    res = _z(_ratio(netinc, equity) * roic, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_netinc_z_21d_v097_signal(netinc):
    """Z-score of Raw level of netinc over 21d window."""
    res = _z(netinc, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_equity_z_21d_v098_signal(equity):
    """Z-score of Raw level of equity over 21d window."""
    res = _z(equity, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_roic_z_21d_v099_signal(roic):
    """Z-score of Raw level of roic over 21d window."""
    res = _z(roic, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_adjusted_roe_z_21d_v100_signal(netinc, equity, roic):
    """Z-score of ROIC-amplified ROE over 21d window."""
    res = _z(_ratio(netinc, equity) * roic, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_netinc_z_42d_v101_signal(netinc):
    """Z-score of Raw level of netinc over 42d window."""
    res = _z(netinc, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_equity_z_42d_v102_signal(equity):
    """Z-score of Raw level of equity over 42d window."""
    res = _z(equity, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_roic_z_42d_v103_signal(roic):
    """Z-score of Raw level of roic over 42d window."""
    res = _z(roic, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_adjusted_roe_z_42d_v104_signal(netinc, equity, roic):
    """Z-score of ROIC-amplified ROE over 42d window."""
    res = _z(_ratio(netinc, equity) * roic, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_netinc_z_63d_v105_signal(netinc):
    """Z-score of Raw level of netinc over 63d window."""
    res = _z(netinc, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_equity_z_63d_v106_signal(equity):
    """Z-score of Raw level of equity over 63d window."""
    res = _z(equity, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_roic_z_63d_v107_signal(roic):
    """Z-score of Raw level of roic over 63d window."""
    res = _z(roic, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_adjusted_roe_z_63d_v108_signal(netinc, equity, roic):
    """Z-score of ROIC-amplified ROE over 63d window."""
    res = _z(_ratio(netinc, equity) * roic, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_netinc_z_126d_v109_signal(netinc):
    """Z-score of Raw level of netinc over 126d window."""
    res = _z(netinc, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_equity_z_126d_v110_signal(equity):
    """Z-score of Raw level of equity over 126d window."""
    res = _z(equity, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_roic_z_126d_v111_signal(roic):
    """Z-score of Raw level of roic over 126d window."""
    res = _z(roic, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_adjusted_roe_z_126d_v112_signal(netinc, equity, roic):
    """Z-score of ROIC-amplified ROE over 126d window."""
    res = _z(_ratio(netinc, equity) * roic, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_netinc_z_252d_v113_signal(netinc):
    """Z-score of Raw level of netinc over 252d window."""
    res = _z(netinc, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_equity_z_252d_v114_signal(equity):
    """Z-score of Raw level of equity over 252d window."""
    res = _z(equity, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_roic_z_252d_v115_signal(roic):
    """Z-score of Raw level of roic over 252d window."""
    res = _z(roic, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_adjusted_roe_z_252d_v116_signal(netinc, equity, roic):
    """Z-score of ROIC-amplified ROE over 252d window."""
    res = _z(_ratio(netinc, equity) * roic, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_netinc_z_504d_v117_signal(netinc):
    """Z-score of Raw level of netinc over 504d window."""
    res = _z(netinc, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_equity_z_504d_v118_signal(equity):
    """Z-score of Raw level of equity over 504d window."""
    res = _z(equity, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_roic_z_504d_v119_signal(roic):
    """Z-score of Raw level of roic over 504d window."""
    res = _z(roic, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_adjusted_roe_z_504d_v120_signal(netinc, equity, roic):
    """Z-score of ROIC-amplified ROE over 504d window."""
    res = _z(_ratio(netinc, equity) * roic, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_netinc_z_756d_v121_signal(netinc):
    """Z-score of Raw level of netinc over 756d window."""
    res = _z(netinc, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_equity_z_756d_v122_signal(equity):
    """Z-score of Raw level of equity over 756d window."""
    res = _z(equity, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_roic_z_756d_v123_signal(roic):
    """Z-score of Raw level of roic over 756d window."""
    res = _z(roic, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_adjusted_roe_z_756d_v124_signal(netinc, equity, roic):
    """Z-score of ROIC-amplified ROE over 756d window."""
    res = _z(_ratio(netinc, equity) * roic, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_netinc_z_1008d_v125_signal(netinc):
    """Z-score of Raw level of netinc over 1008d window."""
    res = _z(netinc, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_equity_z_1008d_v126_signal(equity):
    """Z-score of Raw level of equity over 1008d window."""
    res = _z(equity, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_roic_z_1008d_v127_signal(roic):
    """Z-score of Raw level of roic over 1008d window."""
    res = _z(roic, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_adjusted_roe_z_1008d_v128_signal(netinc, equity, roic):
    """Z-score of ROIC-amplified ROE over 1008d window."""
    res = _z(_ratio(netinc, equity) * roic, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_netinc_z_1260d_v129_signal(netinc):
    """Z-score of Raw level of netinc over 1260d window."""
    res = _z(netinc, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_equity_z_1260d_v130_signal(equity):
    """Z-score of Raw level of equity over 1260d window."""
    res = _z(equity, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_roic_z_1260d_v131_signal(roic):
    """Z-score of Raw level of roic over 1260d window."""
    res = _z(roic, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_adjusted_roe_z_1260d_v132_signal(netinc, equity, roic):
    """Z-score of ROIC-amplified ROE over 1260d window."""
    res = _z(_ratio(netinc, equity) * roic, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_netinc_dd_5d_v133_signal(netinc):
    """Drawdown of Raw level of netinc over 5d window."""
    res = _drawdown(netinc, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_equity_dd_5d_v134_signal(equity):
    """Drawdown of Raw level of equity over 5d window."""
    res = _drawdown(equity, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_roic_dd_5d_v135_signal(roic):
    """Drawdown of Raw level of roic over 5d window."""
    res = _drawdown(roic, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_adjusted_roe_dd_5d_v136_signal(netinc, equity, roic):
    """Drawdown of ROIC-amplified ROE over 5d window."""
    res = _drawdown(_ratio(netinc, equity) * roic, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_netinc_dd_10d_v137_signal(netinc):
    """Drawdown of Raw level of netinc over 10d window."""
    res = _drawdown(netinc, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_equity_dd_10d_v138_signal(equity):
    """Drawdown of Raw level of equity over 10d window."""
    res = _drawdown(equity, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_roic_dd_10d_v139_signal(roic):
    """Drawdown of Raw level of roic over 10d window."""
    res = _drawdown(roic, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_adjusted_roe_dd_10d_v140_signal(netinc, equity, roic):
    """Drawdown of ROIC-amplified ROE over 10d window."""
    res = _drawdown(_ratio(netinc, equity) * roic, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_netinc_dd_21d_v141_signal(netinc):
    """Drawdown of Raw level of netinc over 21d window."""
    res = _drawdown(netinc, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_equity_dd_21d_v142_signal(equity):
    """Drawdown of Raw level of equity over 21d window."""
    res = _drawdown(equity, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_roic_dd_21d_v143_signal(roic):
    """Drawdown of Raw level of roic over 21d window."""
    res = _drawdown(roic, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_adjusted_roe_dd_21d_v144_signal(netinc, equity, roic):
    """Drawdown of ROIC-amplified ROE over 21d window."""
    res = _drawdown(_ratio(netinc, equity) * roic, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_netinc_dd_42d_v145_signal(netinc):
    """Drawdown of Raw level of netinc over 42d window."""
    res = _drawdown(netinc, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_equity_dd_42d_v146_signal(equity):
    """Drawdown of Raw level of equity over 42d window."""
    res = _drawdown(equity, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_roic_dd_42d_v147_signal(roic):
    """Drawdown of Raw level of roic over 42d window."""
    res = _drawdown(roic, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_adjusted_roe_dd_42d_v148_signal(netinc, equity, roic):
    """Drawdown of ROIC-amplified ROE over 42d window."""
    res = _drawdown(_ratio(netinc, equity) * roic, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_netinc_dd_63d_v149_signal(netinc):
    """Drawdown of Raw level of netinc over 63d window."""
    res = _drawdown(netinc, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f31_specialty_roe_equity_dd_63d_v150_signal(equity):
    """Drawdown of Raw level of equity over 63d window."""
    res = _drawdown(equity, 63)
    return res.replace([np.inf, -np.inf], np.nan)


# ===== Feature Registry =====
REGISTRY = {
    "f31_specialty_roe_adjusted_roe_ewma_504d_v076_signal": {"func": f31_specialty_roe_adjusted_roe_ewma_504d_v076_signal},
    "f31_specialty_roe_netinc_ewma_756d_v077_signal": {"func": f31_specialty_roe_netinc_ewma_756d_v077_signal},
    "f31_specialty_roe_equity_ewma_756d_v078_signal": {"func": f31_specialty_roe_equity_ewma_756d_v078_signal},
    "f31_specialty_roe_roic_ewma_756d_v079_signal": {"func": f31_specialty_roe_roic_ewma_756d_v079_signal},
    "f31_specialty_roe_adjusted_roe_ewma_756d_v080_signal": {"func": f31_specialty_roe_adjusted_roe_ewma_756d_v080_signal},
    "f31_specialty_roe_netinc_ewma_1008d_v081_signal": {"func": f31_specialty_roe_netinc_ewma_1008d_v081_signal},
    "f31_specialty_roe_equity_ewma_1008d_v082_signal": {"func": f31_specialty_roe_equity_ewma_1008d_v082_signal},
    "f31_specialty_roe_roic_ewma_1008d_v083_signal": {"func": f31_specialty_roe_roic_ewma_1008d_v083_signal},
    "f31_specialty_roe_adjusted_roe_ewma_1008d_v084_signal": {"func": f31_specialty_roe_adjusted_roe_ewma_1008d_v084_signal},
    "f31_specialty_roe_netinc_ewma_1260d_v085_signal": {"func": f31_specialty_roe_netinc_ewma_1260d_v085_signal},
    "f31_specialty_roe_equity_ewma_1260d_v086_signal": {"func": f31_specialty_roe_equity_ewma_1260d_v086_signal},
    "f31_specialty_roe_roic_ewma_1260d_v087_signal": {"func": f31_specialty_roe_roic_ewma_1260d_v087_signal},
    "f31_specialty_roe_adjusted_roe_ewma_1260d_v088_signal": {"func": f31_specialty_roe_adjusted_roe_ewma_1260d_v088_signal},
    "f31_specialty_roe_netinc_z_5d_v089_signal": {"func": f31_specialty_roe_netinc_z_5d_v089_signal},
    "f31_specialty_roe_equity_z_5d_v090_signal": {"func": f31_specialty_roe_equity_z_5d_v090_signal},
    "f31_specialty_roe_roic_z_5d_v091_signal": {"func": f31_specialty_roe_roic_z_5d_v091_signal},
    "f31_specialty_roe_adjusted_roe_z_5d_v092_signal": {"func": f31_specialty_roe_adjusted_roe_z_5d_v092_signal},
    "f31_specialty_roe_netinc_z_10d_v093_signal": {"func": f31_specialty_roe_netinc_z_10d_v093_signal},
    "f31_specialty_roe_equity_z_10d_v094_signal": {"func": f31_specialty_roe_equity_z_10d_v094_signal},
    "f31_specialty_roe_roic_z_10d_v095_signal": {"func": f31_specialty_roe_roic_z_10d_v095_signal},
    "f31_specialty_roe_adjusted_roe_z_10d_v096_signal": {"func": f31_specialty_roe_adjusted_roe_z_10d_v096_signal},
    "f31_specialty_roe_netinc_z_21d_v097_signal": {"func": f31_specialty_roe_netinc_z_21d_v097_signal},
    "f31_specialty_roe_equity_z_21d_v098_signal": {"func": f31_specialty_roe_equity_z_21d_v098_signal},
    "f31_specialty_roe_roic_z_21d_v099_signal": {"func": f31_specialty_roe_roic_z_21d_v099_signal},
    "f31_specialty_roe_adjusted_roe_z_21d_v100_signal": {"func": f31_specialty_roe_adjusted_roe_z_21d_v100_signal},
    "f31_specialty_roe_netinc_z_42d_v101_signal": {"func": f31_specialty_roe_netinc_z_42d_v101_signal},
    "f31_specialty_roe_equity_z_42d_v102_signal": {"func": f31_specialty_roe_equity_z_42d_v102_signal},
    "f31_specialty_roe_roic_z_42d_v103_signal": {"func": f31_specialty_roe_roic_z_42d_v103_signal},
    "f31_specialty_roe_adjusted_roe_z_42d_v104_signal": {"func": f31_specialty_roe_adjusted_roe_z_42d_v104_signal},
    "f31_specialty_roe_netinc_z_63d_v105_signal": {"func": f31_specialty_roe_netinc_z_63d_v105_signal},
    "f31_specialty_roe_equity_z_63d_v106_signal": {"func": f31_specialty_roe_equity_z_63d_v106_signal},
    "f31_specialty_roe_roic_z_63d_v107_signal": {"func": f31_specialty_roe_roic_z_63d_v107_signal},
    "f31_specialty_roe_adjusted_roe_z_63d_v108_signal": {"func": f31_specialty_roe_adjusted_roe_z_63d_v108_signal},
    "f31_specialty_roe_netinc_z_126d_v109_signal": {"func": f31_specialty_roe_netinc_z_126d_v109_signal},
    "f31_specialty_roe_equity_z_126d_v110_signal": {"func": f31_specialty_roe_equity_z_126d_v110_signal},
    "f31_specialty_roe_roic_z_126d_v111_signal": {"func": f31_specialty_roe_roic_z_126d_v111_signal},
    "f31_specialty_roe_adjusted_roe_z_126d_v112_signal": {"func": f31_specialty_roe_adjusted_roe_z_126d_v112_signal},
    "f31_specialty_roe_netinc_z_252d_v113_signal": {"func": f31_specialty_roe_netinc_z_252d_v113_signal},
    "f31_specialty_roe_equity_z_252d_v114_signal": {"func": f31_specialty_roe_equity_z_252d_v114_signal},
    "f31_specialty_roe_roic_z_252d_v115_signal": {"func": f31_specialty_roe_roic_z_252d_v115_signal},
    "f31_specialty_roe_adjusted_roe_z_252d_v116_signal": {"func": f31_specialty_roe_adjusted_roe_z_252d_v116_signal},
    "f31_specialty_roe_netinc_z_504d_v117_signal": {"func": f31_specialty_roe_netinc_z_504d_v117_signal},
    "f31_specialty_roe_equity_z_504d_v118_signal": {"func": f31_specialty_roe_equity_z_504d_v118_signal},
    "f31_specialty_roe_roic_z_504d_v119_signal": {"func": f31_specialty_roe_roic_z_504d_v119_signal},
    "f31_specialty_roe_adjusted_roe_z_504d_v120_signal": {"func": f31_specialty_roe_adjusted_roe_z_504d_v120_signal},
    "f31_specialty_roe_netinc_z_756d_v121_signal": {"func": f31_specialty_roe_netinc_z_756d_v121_signal},
    "f31_specialty_roe_equity_z_756d_v122_signal": {"func": f31_specialty_roe_equity_z_756d_v122_signal},
    "f31_specialty_roe_roic_z_756d_v123_signal": {"func": f31_specialty_roe_roic_z_756d_v123_signal},
    "f31_specialty_roe_adjusted_roe_z_756d_v124_signal": {"func": f31_specialty_roe_adjusted_roe_z_756d_v124_signal},
    "f31_specialty_roe_netinc_z_1008d_v125_signal": {"func": f31_specialty_roe_netinc_z_1008d_v125_signal},
    "f31_specialty_roe_equity_z_1008d_v126_signal": {"func": f31_specialty_roe_equity_z_1008d_v126_signal},
    "f31_specialty_roe_roic_z_1008d_v127_signal": {"func": f31_specialty_roe_roic_z_1008d_v127_signal},
    "f31_specialty_roe_adjusted_roe_z_1008d_v128_signal": {"func": f31_specialty_roe_adjusted_roe_z_1008d_v128_signal},
    "f31_specialty_roe_netinc_z_1260d_v129_signal": {"func": f31_specialty_roe_netinc_z_1260d_v129_signal},
    "f31_specialty_roe_equity_z_1260d_v130_signal": {"func": f31_specialty_roe_equity_z_1260d_v130_signal},
    "f31_specialty_roe_roic_z_1260d_v131_signal": {"func": f31_specialty_roe_roic_z_1260d_v131_signal},
    "f31_specialty_roe_adjusted_roe_z_1260d_v132_signal": {"func": f31_specialty_roe_adjusted_roe_z_1260d_v132_signal},
    "f31_specialty_roe_netinc_dd_5d_v133_signal": {"func": f31_specialty_roe_netinc_dd_5d_v133_signal},
    "f31_specialty_roe_equity_dd_5d_v134_signal": {"func": f31_specialty_roe_equity_dd_5d_v134_signal},
    "f31_specialty_roe_roic_dd_5d_v135_signal": {"func": f31_specialty_roe_roic_dd_5d_v135_signal},
    "f31_specialty_roe_adjusted_roe_dd_5d_v136_signal": {"func": f31_specialty_roe_adjusted_roe_dd_5d_v136_signal},
    "f31_specialty_roe_netinc_dd_10d_v137_signal": {"func": f31_specialty_roe_netinc_dd_10d_v137_signal},
    "f31_specialty_roe_equity_dd_10d_v138_signal": {"func": f31_specialty_roe_equity_dd_10d_v138_signal},
    "f31_specialty_roe_roic_dd_10d_v139_signal": {"func": f31_specialty_roe_roic_dd_10d_v139_signal},
    "f31_specialty_roe_adjusted_roe_dd_10d_v140_signal": {"func": f31_specialty_roe_adjusted_roe_dd_10d_v140_signal},
    "f31_specialty_roe_netinc_dd_21d_v141_signal": {"func": f31_specialty_roe_netinc_dd_21d_v141_signal},
    "f31_specialty_roe_equity_dd_21d_v142_signal": {"func": f31_specialty_roe_equity_dd_21d_v142_signal},
    "f31_specialty_roe_roic_dd_21d_v143_signal": {"func": f31_specialty_roe_roic_dd_21d_v143_signal},
    "f31_specialty_roe_adjusted_roe_dd_21d_v144_signal": {"func": f31_specialty_roe_adjusted_roe_dd_21d_v144_signal},
    "f31_specialty_roe_netinc_dd_42d_v145_signal": {"func": f31_specialty_roe_netinc_dd_42d_v145_signal},
    "f31_specialty_roe_equity_dd_42d_v146_signal": {"func": f31_specialty_roe_equity_dd_42d_v146_signal},
    "f31_specialty_roe_roic_dd_42d_v147_signal": {"func": f31_specialty_roe_roic_dd_42d_v147_signal},
    "f31_specialty_roe_adjusted_roe_dd_42d_v148_signal": {"func": f31_specialty_roe_adjusted_roe_dd_42d_v148_signal},
    "f31_specialty_roe_netinc_dd_63d_v149_signal": {"func": f31_specialty_roe_netinc_dd_63d_v149_signal},
    "f31_specialty_roe_equity_dd_63d_v150_signal": {"func": f31_specialty_roe_equity_dd_63d_v150_signal},
}

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "deferredrev": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "equity": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "deposits": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "divyield": np.random.normal(100, 10, n).cumsum(), "bvps": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "tangibles": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "grossmargin": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "liabilitiesc": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum()
    })
    print(f"Verifying {len(REGISTRY)} functions for family 31...")
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
