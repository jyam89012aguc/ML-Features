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

def f11_thrift_alpha_tangible_yield_ewma_504d_v076_signal(tangibles, marketcap):
    """Exponential moving average of Tangible assets per market dollar over 504d window."""
    res = _ewma(_ratio(tangibles, marketcap), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_tangibles_ewma_756d_v077_signal(tangibles):
    """Exponential moving average of Raw level of tangibles over 756d window."""
    res = _ewma(tangibles, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_marketcap_ewma_756d_v078_signal(marketcap):
    """Exponential moving average of Raw level of marketcap over 756d window."""
    res = _ewma(marketcap, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_pb_ewma_756d_v079_signal(pb):
    """Exponential moving average of Raw level of pb over 756d window."""
    res = _ewma(pb, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_tangible_yield_ewma_756d_v080_signal(tangibles, marketcap):
    """Exponential moving average of Tangible assets per market dollar over 756d window."""
    res = _ewma(_ratio(tangibles, marketcap), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_tangibles_ewma_1008d_v081_signal(tangibles):
    """Exponential moving average of Raw level of tangibles over 1008d window."""
    res = _ewma(tangibles, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_marketcap_ewma_1008d_v082_signal(marketcap):
    """Exponential moving average of Raw level of marketcap over 1008d window."""
    res = _ewma(marketcap, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_pb_ewma_1008d_v083_signal(pb):
    """Exponential moving average of Raw level of pb over 1008d window."""
    res = _ewma(pb, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_tangible_yield_ewma_1008d_v084_signal(tangibles, marketcap):
    """Exponential moving average of Tangible assets per market dollar over 1008d window."""
    res = _ewma(_ratio(tangibles, marketcap), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_tangibles_ewma_1260d_v085_signal(tangibles):
    """Exponential moving average of Raw level of tangibles over 1260d window."""
    res = _ewma(tangibles, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_marketcap_ewma_1260d_v086_signal(marketcap):
    """Exponential moving average of Raw level of marketcap over 1260d window."""
    res = _ewma(marketcap, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_pb_ewma_1260d_v087_signal(pb):
    """Exponential moving average of Raw level of pb over 1260d window."""
    res = _ewma(pb, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_tangible_yield_ewma_1260d_v088_signal(tangibles, marketcap):
    """Exponential moving average of Tangible assets per market dollar over 1260d window."""
    res = _ewma(_ratio(tangibles, marketcap), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_tangibles_z_5d_v089_signal(tangibles):
    """Z-score of Raw level of tangibles over 5d window."""
    res = _z(tangibles, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_marketcap_z_5d_v090_signal(marketcap):
    """Z-score of Raw level of marketcap over 5d window."""
    res = _z(marketcap, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_pb_z_5d_v091_signal(pb):
    """Z-score of Raw level of pb over 5d window."""
    res = _z(pb, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_tangible_yield_z_5d_v092_signal(tangibles, marketcap):
    """Z-score of Tangible assets per market dollar over 5d window."""
    res = _z(_ratio(tangibles, marketcap), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_tangibles_z_10d_v093_signal(tangibles):
    """Z-score of Raw level of tangibles over 10d window."""
    res = _z(tangibles, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_marketcap_z_10d_v094_signal(marketcap):
    """Z-score of Raw level of marketcap over 10d window."""
    res = _z(marketcap, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_pb_z_10d_v095_signal(pb):
    """Z-score of Raw level of pb over 10d window."""
    res = _z(pb, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_tangible_yield_z_10d_v096_signal(tangibles, marketcap):
    """Z-score of Tangible assets per market dollar over 10d window."""
    res = _z(_ratio(tangibles, marketcap), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_tangibles_z_21d_v097_signal(tangibles):
    """Z-score of Raw level of tangibles over 21d window."""
    res = _z(tangibles, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_marketcap_z_21d_v098_signal(marketcap):
    """Z-score of Raw level of marketcap over 21d window."""
    res = _z(marketcap, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_pb_z_21d_v099_signal(pb):
    """Z-score of Raw level of pb over 21d window."""
    res = _z(pb, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_tangible_yield_z_21d_v100_signal(tangibles, marketcap):
    """Z-score of Tangible assets per market dollar over 21d window."""
    res = _z(_ratio(tangibles, marketcap), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_tangibles_z_42d_v101_signal(tangibles):
    """Z-score of Raw level of tangibles over 42d window."""
    res = _z(tangibles, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_marketcap_z_42d_v102_signal(marketcap):
    """Z-score of Raw level of marketcap over 42d window."""
    res = _z(marketcap, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_pb_z_42d_v103_signal(pb):
    """Z-score of Raw level of pb over 42d window."""
    res = _z(pb, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_tangible_yield_z_42d_v104_signal(tangibles, marketcap):
    """Z-score of Tangible assets per market dollar over 42d window."""
    res = _z(_ratio(tangibles, marketcap), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_tangibles_z_63d_v105_signal(tangibles):
    """Z-score of Raw level of tangibles over 63d window."""
    res = _z(tangibles, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_marketcap_z_63d_v106_signal(marketcap):
    """Z-score of Raw level of marketcap over 63d window."""
    res = _z(marketcap, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_pb_z_63d_v107_signal(pb):
    """Z-score of Raw level of pb over 63d window."""
    res = _z(pb, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_tangible_yield_z_63d_v108_signal(tangibles, marketcap):
    """Z-score of Tangible assets per market dollar over 63d window."""
    res = _z(_ratio(tangibles, marketcap), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_tangibles_z_126d_v109_signal(tangibles):
    """Z-score of Raw level of tangibles over 126d window."""
    res = _z(tangibles, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_marketcap_z_126d_v110_signal(marketcap):
    """Z-score of Raw level of marketcap over 126d window."""
    res = _z(marketcap, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_pb_z_126d_v111_signal(pb):
    """Z-score of Raw level of pb over 126d window."""
    res = _z(pb, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_tangible_yield_z_126d_v112_signal(tangibles, marketcap):
    """Z-score of Tangible assets per market dollar over 126d window."""
    res = _z(_ratio(tangibles, marketcap), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_tangibles_z_252d_v113_signal(tangibles):
    """Z-score of Raw level of tangibles over 252d window."""
    res = _z(tangibles, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_marketcap_z_252d_v114_signal(marketcap):
    """Z-score of Raw level of marketcap over 252d window."""
    res = _z(marketcap, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_pb_z_252d_v115_signal(pb):
    """Z-score of Raw level of pb over 252d window."""
    res = _z(pb, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_tangible_yield_z_252d_v116_signal(tangibles, marketcap):
    """Z-score of Tangible assets per market dollar over 252d window."""
    res = _z(_ratio(tangibles, marketcap), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_tangibles_z_504d_v117_signal(tangibles):
    """Z-score of Raw level of tangibles over 504d window."""
    res = _z(tangibles, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_marketcap_z_504d_v118_signal(marketcap):
    """Z-score of Raw level of marketcap over 504d window."""
    res = _z(marketcap, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_pb_z_504d_v119_signal(pb):
    """Z-score of Raw level of pb over 504d window."""
    res = _z(pb, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_tangible_yield_z_504d_v120_signal(tangibles, marketcap):
    """Z-score of Tangible assets per market dollar over 504d window."""
    res = _z(_ratio(tangibles, marketcap), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_tangibles_z_756d_v121_signal(tangibles):
    """Z-score of Raw level of tangibles over 756d window."""
    res = _z(tangibles, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_marketcap_z_756d_v122_signal(marketcap):
    """Z-score of Raw level of marketcap over 756d window."""
    res = _z(marketcap, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_pb_z_756d_v123_signal(pb):
    """Z-score of Raw level of pb over 756d window."""
    res = _z(pb, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_tangible_yield_z_756d_v124_signal(tangibles, marketcap):
    """Z-score of Tangible assets per market dollar over 756d window."""
    res = _z(_ratio(tangibles, marketcap), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_tangibles_z_1008d_v125_signal(tangibles):
    """Z-score of Raw level of tangibles over 1008d window."""
    res = _z(tangibles, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_marketcap_z_1008d_v126_signal(marketcap):
    """Z-score of Raw level of marketcap over 1008d window."""
    res = _z(marketcap, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_pb_z_1008d_v127_signal(pb):
    """Z-score of Raw level of pb over 1008d window."""
    res = _z(pb, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_tangible_yield_z_1008d_v128_signal(tangibles, marketcap):
    """Z-score of Tangible assets per market dollar over 1008d window."""
    res = _z(_ratio(tangibles, marketcap), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_tangibles_z_1260d_v129_signal(tangibles):
    """Z-score of Raw level of tangibles over 1260d window."""
    res = _z(tangibles, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_marketcap_z_1260d_v130_signal(marketcap):
    """Z-score of Raw level of marketcap over 1260d window."""
    res = _z(marketcap, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_pb_z_1260d_v131_signal(pb):
    """Z-score of Raw level of pb over 1260d window."""
    res = _z(pb, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_tangible_yield_z_1260d_v132_signal(tangibles, marketcap):
    """Z-score of Tangible assets per market dollar over 1260d window."""
    res = _z(_ratio(tangibles, marketcap), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_tangibles_dd_5d_v133_signal(tangibles):
    """Drawdown of Raw level of tangibles over 5d window."""
    res = _drawdown(tangibles, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_marketcap_dd_5d_v134_signal(marketcap):
    """Drawdown of Raw level of marketcap over 5d window."""
    res = _drawdown(marketcap, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_pb_dd_5d_v135_signal(pb):
    """Drawdown of Raw level of pb over 5d window."""
    res = _drawdown(pb, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_tangible_yield_dd_5d_v136_signal(tangibles, marketcap):
    """Drawdown of Tangible assets per market dollar over 5d window."""
    res = _drawdown(_ratio(tangibles, marketcap), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_tangibles_dd_10d_v137_signal(tangibles):
    """Drawdown of Raw level of tangibles over 10d window."""
    res = _drawdown(tangibles, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_marketcap_dd_10d_v138_signal(marketcap):
    """Drawdown of Raw level of marketcap over 10d window."""
    res = _drawdown(marketcap, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_pb_dd_10d_v139_signal(pb):
    """Drawdown of Raw level of pb over 10d window."""
    res = _drawdown(pb, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_tangible_yield_dd_10d_v140_signal(tangibles, marketcap):
    """Drawdown of Tangible assets per market dollar over 10d window."""
    res = _drawdown(_ratio(tangibles, marketcap), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_tangibles_dd_21d_v141_signal(tangibles):
    """Drawdown of Raw level of tangibles over 21d window."""
    res = _drawdown(tangibles, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_marketcap_dd_21d_v142_signal(marketcap):
    """Drawdown of Raw level of marketcap over 21d window."""
    res = _drawdown(marketcap, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_pb_dd_21d_v143_signal(pb):
    """Drawdown of Raw level of pb over 21d window."""
    res = _drawdown(pb, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_tangible_yield_dd_21d_v144_signal(tangibles, marketcap):
    """Drawdown of Tangible assets per market dollar over 21d window."""
    res = _drawdown(_ratio(tangibles, marketcap), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_tangibles_dd_42d_v145_signal(tangibles):
    """Drawdown of Raw level of tangibles over 42d window."""
    res = _drawdown(tangibles, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_marketcap_dd_42d_v146_signal(marketcap):
    """Drawdown of Raw level of marketcap over 42d window."""
    res = _drawdown(marketcap, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_pb_dd_42d_v147_signal(pb):
    """Drawdown of Raw level of pb over 42d window."""
    res = _drawdown(pb, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_tangible_yield_dd_42d_v148_signal(tangibles, marketcap):
    """Drawdown of Tangible assets per market dollar over 42d window."""
    res = _drawdown(_ratio(tangibles, marketcap), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_tangibles_dd_63d_v149_signal(tangibles):
    """Drawdown of Raw level of tangibles over 63d window."""
    res = _drawdown(tangibles, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_marketcap_dd_63d_v150_signal(marketcap):
    """Drawdown of Raw level of marketcap over 63d window."""
    res = _drawdown(marketcap, 63)
    return res.replace([np.inf, -np.inf], np.nan)


# ===== Feature Registry =====
REGISTRY = {
    "f11_thrift_alpha_tangible_yield_ewma_504d_v076_signal": {"func": f11_thrift_alpha_tangible_yield_ewma_504d_v076_signal},
    "f11_thrift_alpha_tangibles_ewma_756d_v077_signal": {"func": f11_thrift_alpha_tangibles_ewma_756d_v077_signal},
    "f11_thrift_alpha_marketcap_ewma_756d_v078_signal": {"func": f11_thrift_alpha_marketcap_ewma_756d_v078_signal},
    "f11_thrift_alpha_pb_ewma_756d_v079_signal": {"func": f11_thrift_alpha_pb_ewma_756d_v079_signal},
    "f11_thrift_alpha_tangible_yield_ewma_756d_v080_signal": {"func": f11_thrift_alpha_tangible_yield_ewma_756d_v080_signal},
    "f11_thrift_alpha_tangibles_ewma_1008d_v081_signal": {"func": f11_thrift_alpha_tangibles_ewma_1008d_v081_signal},
    "f11_thrift_alpha_marketcap_ewma_1008d_v082_signal": {"func": f11_thrift_alpha_marketcap_ewma_1008d_v082_signal},
    "f11_thrift_alpha_pb_ewma_1008d_v083_signal": {"func": f11_thrift_alpha_pb_ewma_1008d_v083_signal},
    "f11_thrift_alpha_tangible_yield_ewma_1008d_v084_signal": {"func": f11_thrift_alpha_tangible_yield_ewma_1008d_v084_signal},
    "f11_thrift_alpha_tangibles_ewma_1260d_v085_signal": {"func": f11_thrift_alpha_tangibles_ewma_1260d_v085_signal},
    "f11_thrift_alpha_marketcap_ewma_1260d_v086_signal": {"func": f11_thrift_alpha_marketcap_ewma_1260d_v086_signal},
    "f11_thrift_alpha_pb_ewma_1260d_v087_signal": {"func": f11_thrift_alpha_pb_ewma_1260d_v087_signal},
    "f11_thrift_alpha_tangible_yield_ewma_1260d_v088_signal": {"func": f11_thrift_alpha_tangible_yield_ewma_1260d_v088_signal},
    "f11_thrift_alpha_tangibles_z_5d_v089_signal": {"func": f11_thrift_alpha_tangibles_z_5d_v089_signal},
    "f11_thrift_alpha_marketcap_z_5d_v090_signal": {"func": f11_thrift_alpha_marketcap_z_5d_v090_signal},
    "f11_thrift_alpha_pb_z_5d_v091_signal": {"func": f11_thrift_alpha_pb_z_5d_v091_signal},
    "f11_thrift_alpha_tangible_yield_z_5d_v092_signal": {"func": f11_thrift_alpha_tangible_yield_z_5d_v092_signal},
    "f11_thrift_alpha_tangibles_z_10d_v093_signal": {"func": f11_thrift_alpha_tangibles_z_10d_v093_signal},
    "f11_thrift_alpha_marketcap_z_10d_v094_signal": {"func": f11_thrift_alpha_marketcap_z_10d_v094_signal},
    "f11_thrift_alpha_pb_z_10d_v095_signal": {"func": f11_thrift_alpha_pb_z_10d_v095_signal},
    "f11_thrift_alpha_tangible_yield_z_10d_v096_signal": {"func": f11_thrift_alpha_tangible_yield_z_10d_v096_signal},
    "f11_thrift_alpha_tangibles_z_21d_v097_signal": {"func": f11_thrift_alpha_tangibles_z_21d_v097_signal},
    "f11_thrift_alpha_marketcap_z_21d_v098_signal": {"func": f11_thrift_alpha_marketcap_z_21d_v098_signal},
    "f11_thrift_alpha_pb_z_21d_v099_signal": {"func": f11_thrift_alpha_pb_z_21d_v099_signal},
    "f11_thrift_alpha_tangible_yield_z_21d_v100_signal": {"func": f11_thrift_alpha_tangible_yield_z_21d_v100_signal},
    "f11_thrift_alpha_tangibles_z_42d_v101_signal": {"func": f11_thrift_alpha_tangibles_z_42d_v101_signal},
    "f11_thrift_alpha_marketcap_z_42d_v102_signal": {"func": f11_thrift_alpha_marketcap_z_42d_v102_signal},
    "f11_thrift_alpha_pb_z_42d_v103_signal": {"func": f11_thrift_alpha_pb_z_42d_v103_signal},
    "f11_thrift_alpha_tangible_yield_z_42d_v104_signal": {"func": f11_thrift_alpha_tangible_yield_z_42d_v104_signal},
    "f11_thrift_alpha_tangibles_z_63d_v105_signal": {"func": f11_thrift_alpha_tangibles_z_63d_v105_signal},
    "f11_thrift_alpha_marketcap_z_63d_v106_signal": {"func": f11_thrift_alpha_marketcap_z_63d_v106_signal},
    "f11_thrift_alpha_pb_z_63d_v107_signal": {"func": f11_thrift_alpha_pb_z_63d_v107_signal},
    "f11_thrift_alpha_tangible_yield_z_63d_v108_signal": {"func": f11_thrift_alpha_tangible_yield_z_63d_v108_signal},
    "f11_thrift_alpha_tangibles_z_126d_v109_signal": {"func": f11_thrift_alpha_tangibles_z_126d_v109_signal},
    "f11_thrift_alpha_marketcap_z_126d_v110_signal": {"func": f11_thrift_alpha_marketcap_z_126d_v110_signal},
    "f11_thrift_alpha_pb_z_126d_v111_signal": {"func": f11_thrift_alpha_pb_z_126d_v111_signal},
    "f11_thrift_alpha_tangible_yield_z_126d_v112_signal": {"func": f11_thrift_alpha_tangible_yield_z_126d_v112_signal},
    "f11_thrift_alpha_tangibles_z_252d_v113_signal": {"func": f11_thrift_alpha_tangibles_z_252d_v113_signal},
    "f11_thrift_alpha_marketcap_z_252d_v114_signal": {"func": f11_thrift_alpha_marketcap_z_252d_v114_signal},
    "f11_thrift_alpha_pb_z_252d_v115_signal": {"func": f11_thrift_alpha_pb_z_252d_v115_signal},
    "f11_thrift_alpha_tangible_yield_z_252d_v116_signal": {"func": f11_thrift_alpha_tangible_yield_z_252d_v116_signal},
    "f11_thrift_alpha_tangibles_z_504d_v117_signal": {"func": f11_thrift_alpha_tangibles_z_504d_v117_signal},
    "f11_thrift_alpha_marketcap_z_504d_v118_signal": {"func": f11_thrift_alpha_marketcap_z_504d_v118_signal},
    "f11_thrift_alpha_pb_z_504d_v119_signal": {"func": f11_thrift_alpha_pb_z_504d_v119_signal},
    "f11_thrift_alpha_tangible_yield_z_504d_v120_signal": {"func": f11_thrift_alpha_tangible_yield_z_504d_v120_signal},
    "f11_thrift_alpha_tangibles_z_756d_v121_signal": {"func": f11_thrift_alpha_tangibles_z_756d_v121_signal},
    "f11_thrift_alpha_marketcap_z_756d_v122_signal": {"func": f11_thrift_alpha_marketcap_z_756d_v122_signal},
    "f11_thrift_alpha_pb_z_756d_v123_signal": {"func": f11_thrift_alpha_pb_z_756d_v123_signal},
    "f11_thrift_alpha_tangible_yield_z_756d_v124_signal": {"func": f11_thrift_alpha_tangible_yield_z_756d_v124_signal},
    "f11_thrift_alpha_tangibles_z_1008d_v125_signal": {"func": f11_thrift_alpha_tangibles_z_1008d_v125_signal},
    "f11_thrift_alpha_marketcap_z_1008d_v126_signal": {"func": f11_thrift_alpha_marketcap_z_1008d_v126_signal},
    "f11_thrift_alpha_pb_z_1008d_v127_signal": {"func": f11_thrift_alpha_pb_z_1008d_v127_signal},
    "f11_thrift_alpha_tangible_yield_z_1008d_v128_signal": {"func": f11_thrift_alpha_tangible_yield_z_1008d_v128_signal},
    "f11_thrift_alpha_tangibles_z_1260d_v129_signal": {"func": f11_thrift_alpha_tangibles_z_1260d_v129_signal},
    "f11_thrift_alpha_marketcap_z_1260d_v130_signal": {"func": f11_thrift_alpha_marketcap_z_1260d_v130_signal},
    "f11_thrift_alpha_pb_z_1260d_v131_signal": {"func": f11_thrift_alpha_pb_z_1260d_v131_signal},
    "f11_thrift_alpha_tangible_yield_z_1260d_v132_signal": {"func": f11_thrift_alpha_tangible_yield_z_1260d_v132_signal},
    "f11_thrift_alpha_tangibles_dd_5d_v133_signal": {"func": f11_thrift_alpha_tangibles_dd_5d_v133_signal},
    "f11_thrift_alpha_marketcap_dd_5d_v134_signal": {"func": f11_thrift_alpha_marketcap_dd_5d_v134_signal},
    "f11_thrift_alpha_pb_dd_5d_v135_signal": {"func": f11_thrift_alpha_pb_dd_5d_v135_signal},
    "f11_thrift_alpha_tangible_yield_dd_5d_v136_signal": {"func": f11_thrift_alpha_tangible_yield_dd_5d_v136_signal},
    "f11_thrift_alpha_tangibles_dd_10d_v137_signal": {"func": f11_thrift_alpha_tangibles_dd_10d_v137_signal},
    "f11_thrift_alpha_marketcap_dd_10d_v138_signal": {"func": f11_thrift_alpha_marketcap_dd_10d_v138_signal},
    "f11_thrift_alpha_pb_dd_10d_v139_signal": {"func": f11_thrift_alpha_pb_dd_10d_v139_signal},
    "f11_thrift_alpha_tangible_yield_dd_10d_v140_signal": {"func": f11_thrift_alpha_tangible_yield_dd_10d_v140_signal},
    "f11_thrift_alpha_tangibles_dd_21d_v141_signal": {"func": f11_thrift_alpha_tangibles_dd_21d_v141_signal},
    "f11_thrift_alpha_marketcap_dd_21d_v142_signal": {"func": f11_thrift_alpha_marketcap_dd_21d_v142_signal},
    "f11_thrift_alpha_pb_dd_21d_v143_signal": {"func": f11_thrift_alpha_pb_dd_21d_v143_signal},
    "f11_thrift_alpha_tangible_yield_dd_21d_v144_signal": {"func": f11_thrift_alpha_tangible_yield_dd_21d_v144_signal},
    "f11_thrift_alpha_tangibles_dd_42d_v145_signal": {"func": f11_thrift_alpha_tangibles_dd_42d_v145_signal},
    "f11_thrift_alpha_marketcap_dd_42d_v146_signal": {"func": f11_thrift_alpha_marketcap_dd_42d_v146_signal},
    "f11_thrift_alpha_pb_dd_42d_v147_signal": {"func": f11_thrift_alpha_pb_dd_42d_v147_signal},
    "f11_thrift_alpha_tangible_yield_dd_42d_v148_signal": {"func": f11_thrift_alpha_tangible_yield_dd_42d_v148_signal},
    "f11_thrift_alpha_tangibles_dd_63d_v149_signal": {"func": f11_thrift_alpha_tangibles_dd_63d_v149_signal},
    "f11_thrift_alpha_marketcap_dd_63d_v150_signal": {"func": f11_thrift_alpha_marketcap_dd_63d_v150_signal},
}

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "deferredrev": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "equity": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "deposits": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "divyield": np.random.normal(100, 10, n).cumsum(), "bvps": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "tangibles": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "grossmargin": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "liabilitiesc": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "pb": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum()
    })
    print(f"Verifying {len(REGISTRY)} functions for family 11...")
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
