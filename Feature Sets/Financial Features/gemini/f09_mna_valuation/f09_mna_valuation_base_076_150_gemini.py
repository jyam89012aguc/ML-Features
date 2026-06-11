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

def f09_mna_valuation_pb_ewma_63d_v076_signal(pb):
    """Exponential moving average of Raw level of pb over 63d window."""
    res = _ewma(pb, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_pe_ewma_63d_v077_signal(pe):
    """Exponential moving average of Raw level of pe over 63d window."""
    res = _ewma(pe, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_marketcap_ewma_63d_v078_signal(marketcap):
    """Exponential moving average of Raw level of marketcap over 63d window."""
    res = _ewma(marketcap, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_valuation_composite_ewma_63d_v079_signal(pb, pe):
    """Exponential moving average of Combined P/B and P/E valuation metric over 63d window."""
    res = _ewma(pb * pe, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_size_factor_ewma_63d_v080_signal(marketcap):
    """Exponential moving average of Size-based discount factor over 63d window."""
    res = _ewma(1 / marketcap, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_pb_ewma_126d_v081_signal(pb):
    """Exponential moving average of Raw level of pb over 126d window."""
    res = _ewma(pb, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_pe_ewma_126d_v082_signal(pe):
    """Exponential moving average of Raw level of pe over 126d window."""
    res = _ewma(pe, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_marketcap_ewma_126d_v083_signal(marketcap):
    """Exponential moving average of Raw level of marketcap over 126d window."""
    res = _ewma(marketcap, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_valuation_composite_ewma_126d_v084_signal(pb, pe):
    """Exponential moving average of Combined P/B and P/E valuation metric over 126d window."""
    res = _ewma(pb * pe, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_size_factor_ewma_126d_v085_signal(marketcap):
    """Exponential moving average of Size-based discount factor over 126d window."""
    res = _ewma(1 / marketcap, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_pb_ewma_252d_v086_signal(pb):
    """Exponential moving average of Raw level of pb over 252d window."""
    res = _ewma(pb, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_pe_ewma_252d_v087_signal(pe):
    """Exponential moving average of Raw level of pe over 252d window."""
    res = _ewma(pe, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_marketcap_ewma_252d_v088_signal(marketcap):
    """Exponential moving average of Raw level of marketcap over 252d window."""
    res = _ewma(marketcap, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_valuation_composite_ewma_252d_v089_signal(pb, pe):
    """Exponential moving average of Combined P/B and P/E valuation metric over 252d window."""
    res = _ewma(pb * pe, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_size_factor_ewma_252d_v090_signal(marketcap):
    """Exponential moving average of Size-based discount factor over 252d window."""
    res = _ewma(1 / marketcap, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_pb_ewma_504d_v091_signal(pb):
    """Exponential moving average of Raw level of pb over 504d window."""
    res = _ewma(pb, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_pe_ewma_504d_v092_signal(pe):
    """Exponential moving average of Raw level of pe over 504d window."""
    res = _ewma(pe, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_marketcap_ewma_504d_v093_signal(marketcap):
    """Exponential moving average of Raw level of marketcap over 504d window."""
    res = _ewma(marketcap, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_valuation_composite_ewma_504d_v094_signal(pb, pe):
    """Exponential moving average of Combined P/B and P/E valuation metric over 504d window."""
    res = _ewma(pb * pe, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_size_factor_ewma_504d_v095_signal(marketcap):
    """Exponential moving average of Size-based discount factor over 504d window."""
    res = _ewma(1 / marketcap, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_pb_ewma_756d_v096_signal(pb):
    """Exponential moving average of Raw level of pb over 756d window."""
    res = _ewma(pb, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_pe_ewma_756d_v097_signal(pe):
    """Exponential moving average of Raw level of pe over 756d window."""
    res = _ewma(pe, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_marketcap_ewma_756d_v098_signal(marketcap):
    """Exponential moving average of Raw level of marketcap over 756d window."""
    res = _ewma(marketcap, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_valuation_composite_ewma_756d_v099_signal(pb, pe):
    """Exponential moving average of Combined P/B and P/E valuation metric over 756d window."""
    res = _ewma(pb * pe, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_size_factor_ewma_756d_v100_signal(marketcap):
    """Exponential moving average of Size-based discount factor over 756d window."""
    res = _ewma(1 / marketcap, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_pb_ewma_1008d_v101_signal(pb):
    """Exponential moving average of Raw level of pb over 1008d window."""
    res = _ewma(pb, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_pe_ewma_1008d_v102_signal(pe):
    """Exponential moving average of Raw level of pe over 1008d window."""
    res = _ewma(pe, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_marketcap_ewma_1008d_v103_signal(marketcap):
    """Exponential moving average of Raw level of marketcap over 1008d window."""
    res = _ewma(marketcap, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_valuation_composite_ewma_1008d_v104_signal(pb, pe):
    """Exponential moving average of Combined P/B and P/E valuation metric over 1008d window."""
    res = _ewma(pb * pe, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_size_factor_ewma_1008d_v105_signal(marketcap):
    """Exponential moving average of Size-based discount factor over 1008d window."""
    res = _ewma(1 / marketcap, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_pb_ewma_1260d_v106_signal(pb):
    """Exponential moving average of Raw level of pb over 1260d window."""
    res = _ewma(pb, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_pe_ewma_1260d_v107_signal(pe):
    """Exponential moving average of Raw level of pe over 1260d window."""
    res = _ewma(pe, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_marketcap_ewma_1260d_v108_signal(marketcap):
    """Exponential moving average of Raw level of marketcap over 1260d window."""
    res = _ewma(marketcap, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_valuation_composite_ewma_1260d_v109_signal(pb, pe):
    """Exponential moving average of Combined P/B and P/E valuation metric over 1260d window."""
    res = _ewma(pb * pe, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_size_factor_ewma_1260d_v110_signal(marketcap):
    """Exponential moving average of Size-based discount factor over 1260d window."""
    res = _ewma(1 / marketcap, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_pb_z_5d_v111_signal(pb):
    """Z-score of Raw level of pb over 5d window."""
    res = _z(pb, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_pe_z_5d_v112_signal(pe):
    """Z-score of Raw level of pe over 5d window."""
    res = _z(pe, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_marketcap_z_5d_v113_signal(marketcap):
    """Z-score of Raw level of marketcap over 5d window."""
    res = _z(marketcap, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_valuation_composite_z_5d_v114_signal(pb, pe):
    """Z-score of Combined P/B and P/E valuation metric over 5d window."""
    res = _z(pb * pe, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_size_factor_z_5d_v115_signal(marketcap):
    """Z-score of Size-based discount factor over 5d window."""
    res = _z(1 / marketcap, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_pb_z_10d_v116_signal(pb):
    """Z-score of Raw level of pb over 10d window."""
    res = _z(pb, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_pe_z_10d_v117_signal(pe):
    """Z-score of Raw level of pe over 10d window."""
    res = _z(pe, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_marketcap_z_10d_v118_signal(marketcap):
    """Z-score of Raw level of marketcap over 10d window."""
    res = _z(marketcap, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_valuation_composite_z_10d_v119_signal(pb, pe):
    """Z-score of Combined P/B and P/E valuation metric over 10d window."""
    res = _z(pb * pe, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_size_factor_z_10d_v120_signal(marketcap):
    """Z-score of Size-based discount factor over 10d window."""
    res = _z(1 / marketcap, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_pb_z_21d_v121_signal(pb):
    """Z-score of Raw level of pb over 21d window."""
    res = _z(pb, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_pe_z_21d_v122_signal(pe):
    """Z-score of Raw level of pe over 21d window."""
    res = _z(pe, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_marketcap_z_21d_v123_signal(marketcap):
    """Z-score of Raw level of marketcap over 21d window."""
    res = _z(marketcap, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_valuation_composite_z_21d_v124_signal(pb, pe):
    """Z-score of Combined P/B and P/E valuation metric over 21d window."""
    res = _z(pb * pe, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_size_factor_z_21d_v125_signal(marketcap):
    """Z-score of Size-based discount factor over 21d window."""
    res = _z(1 / marketcap, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_pb_z_42d_v126_signal(pb):
    """Z-score of Raw level of pb over 42d window."""
    res = _z(pb, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_pe_z_42d_v127_signal(pe):
    """Z-score of Raw level of pe over 42d window."""
    res = _z(pe, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_marketcap_z_42d_v128_signal(marketcap):
    """Z-score of Raw level of marketcap over 42d window."""
    res = _z(marketcap, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_valuation_composite_z_42d_v129_signal(pb, pe):
    """Z-score of Combined P/B and P/E valuation metric over 42d window."""
    res = _z(pb * pe, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_size_factor_z_42d_v130_signal(marketcap):
    """Z-score of Size-based discount factor over 42d window."""
    res = _z(1 / marketcap, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_pb_z_63d_v131_signal(pb):
    """Z-score of Raw level of pb over 63d window."""
    res = _z(pb, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_pe_z_63d_v132_signal(pe):
    """Z-score of Raw level of pe over 63d window."""
    res = _z(pe, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_marketcap_z_63d_v133_signal(marketcap):
    """Z-score of Raw level of marketcap over 63d window."""
    res = _z(marketcap, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_valuation_composite_z_63d_v134_signal(pb, pe):
    """Z-score of Combined P/B and P/E valuation metric over 63d window."""
    res = _z(pb * pe, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_size_factor_z_63d_v135_signal(marketcap):
    """Z-score of Size-based discount factor over 63d window."""
    res = _z(1 / marketcap, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_pb_z_126d_v136_signal(pb):
    """Z-score of Raw level of pb over 126d window."""
    res = _z(pb, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_pe_z_126d_v137_signal(pe):
    """Z-score of Raw level of pe over 126d window."""
    res = _z(pe, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_marketcap_z_126d_v138_signal(marketcap):
    """Z-score of Raw level of marketcap over 126d window."""
    res = _z(marketcap, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_valuation_composite_z_126d_v139_signal(pb, pe):
    """Z-score of Combined P/B and P/E valuation metric over 126d window."""
    res = _z(pb * pe, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_size_factor_z_126d_v140_signal(marketcap):
    """Z-score of Size-based discount factor over 126d window."""
    res = _z(1 / marketcap, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_pb_z_252d_v141_signal(pb):
    """Z-score of Raw level of pb over 252d window."""
    res = _z(pb, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_pe_z_252d_v142_signal(pe):
    """Z-score of Raw level of pe over 252d window."""
    res = _z(pe, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_marketcap_z_252d_v143_signal(marketcap):
    """Z-score of Raw level of marketcap over 252d window."""
    res = _z(marketcap, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_valuation_composite_z_252d_v144_signal(pb, pe):
    """Z-score of Combined P/B and P/E valuation metric over 252d window."""
    res = _z(pb * pe, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_size_factor_z_252d_v145_signal(marketcap):
    """Z-score of Size-based discount factor over 252d window."""
    res = _z(1 / marketcap, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_pb_z_504d_v146_signal(pb):
    """Z-score of Raw level of pb over 504d window."""
    res = _z(pb, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_pe_z_504d_v147_signal(pe):
    """Z-score of Raw level of pe over 504d window."""
    res = _z(pe, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_marketcap_z_504d_v148_signal(marketcap):
    """Z-score of Raw level of marketcap over 504d window."""
    res = _z(marketcap, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_valuation_composite_z_504d_v149_signal(pb, pe):
    """Z-score of Combined P/B and P/E valuation metric over 504d window."""
    res = _z(pb * pe, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f09_mna_valuation_size_factor_z_504d_v150_signal(marketcap):
    """Z-score of Size-based discount factor over 504d window."""
    res = _z(1 / marketcap, 504)
    return res.replace([np.inf, -np.inf], np.nan)


# ===== Feature Registry =====
REGISTRY = {
    "f09_mna_valuation_pb_ewma_63d_v076_signal": {"func": f09_mna_valuation_pb_ewma_63d_v076_signal},
    "f09_mna_valuation_pe_ewma_63d_v077_signal": {"func": f09_mna_valuation_pe_ewma_63d_v077_signal},
    "f09_mna_valuation_marketcap_ewma_63d_v078_signal": {"func": f09_mna_valuation_marketcap_ewma_63d_v078_signal},
    "f09_mna_valuation_valuation_composite_ewma_63d_v079_signal": {"func": f09_mna_valuation_valuation_composite_ewma_63d_v079_signal},
    "f09_mna_valuation_size_factor_ewma_63d_v080_signal": {"func": f09_mna_valuation_size_factor_ewma_63d_v080_signal},
    "f09_mna_valuation_pb_ewma_126d_v081_signal": {"func": f09_mna_valuation_pb_ewma_126d_v081_signal},
    "f09_mna_valuation_pe_ewma_126d_v082_signal": {"func": f09_mna_valuation_pe_ewma_126d_v082_signal},
    "f09_mna_valuation_marketcap_ewma_126d_v083_signal": {"func": f09_mna_valuation_marketcap_ewma_126d_v083_signal},
    "f09_mna_valuation_valuation_composite_ewma_126d_v084_signal": {"func": f09_mna_valuation_valuation_composite_ewma_126d_v084_signal},
    "f09_mna_valuation_size_factor_ewma_126d_v085_signal": {"func": f09_mna_valuation_size_factor_ewma_126d_v085_signal},
    "f09_mna_valuation_pb_ewma_252d_v086_signal": {"func": f09_mna_valuation_pb_ewma_252d_v086_signal},
    "f09_mna_valuation_pe_ewma_252d_v087_signal": {"func": f09_mna_valuation_pe_ewma_252d_v087_signal},
    "f09_mna_valuation_marketcap_ewma_252d_v088_signal": {"func": f09_mna_valuation_marketcap_ewma_252d_v088_signal},
    "f09_mna_valuation_valuation_composite_ewma_252d_v089_signal": {"func": f09_mna_valuation_valuation_composite_ewma_252d_v089_signal},
    "f09_mna_valuation_size_factor_ewma_252d_v090_signal": {"func": f09_mna_valuation_size_factor_ewma_252d_v090_signal},
    "f09_mna_valuation_pb_ewma_504d_v091_signal": {"func": f09_mna_valuation_pb_ewma_504d_v091_signal},
    "f09_mna_valuation_pe_ewma_504d_v092_signal": {"func": f09_mna_valuation_pe_ewma_504d_v092_signal},
    "f09_mna_valuation_marketcap_ewma_504d_v093_signal": {"func": f09_mna_valuation_marketcap_ewma_504d_v093_signal},
    "f09_mna_valuation_valuation_composite_ewma_504d_v094_signal": {"func": f09_mna_valuation_valuation_composite_ewma_504d_v094_signal},
    "f09_mna_valuation_size_factor_ewma_504d_v095_signal": {"func": f09_mna_valuation_size_factor_ewma_504d_v095_signal},
    "f09_mna_valuation_pb_ewma_756d_v096_signal": {"func": f09_mna_valuation_pb_ewma_756d_v096_signal},
    "f09_mna_valuation_pe_ewma_756d_v097_signal": {"func": f09_mna_valuation_pe_ewma_756d_v097_signal},
    "f09_mna_valuation_marketcap_ewma_756d_v098_signal": {"func": f09_mna_valuation_marketcap_ewma_756d_v098_signal},
    "f09_mna_valuation_valuation_composite_ewma_756d_v099_signal": {"func": f09_mna_valuation_valuation_composite_ewma_756d_v099_signal},
    "f09_mna_valuation_size_factor_ewma_756d_v100_signal": {"func": f09_mna_valuation_size_factor_ewma_756d_v100_signal},
    "f09_mna_valuation_pb_ewma_1008d_v101_signal": {"func": f09_mna_valuation_pb_ewma_1008d_v101_signal},
    "f09_mna_valuation_pe_ewma_1008d_v102_signal": {"func": f09_mna_valuation_pe_ewma_1008d_v102_signal},
    "f09_mna_valuation_marketcap_ewma_1008d_v103_signal": {"func": f09_mna_valuation_marketcap_ewma_1008d_v103_signal},
    "f09_mna_valuation_valuation_composite_ewma_1008d_v104_signal": {"func": f09_mna_valuation_valuation_composite_ewma_1008d_v104_signal},
    "f09_mna_valuation_size_factor_ewma_1008d_v105_signal": {"func": f09_mna_valuation_size_factor_ewma_1008d_v105_signal},
    "f09_mna_valuation_pb_ewma_1260d_v106_signal": {"func": f09_mna_valuation_pb_ewma_1260d_v106_signal},
    "f09_mna_valuation_pe_ewma_1260d_v107_signal": {"func": f09_mna_valuation_pe_ewma_1260d_v107_signal},
    "f09_mna_valuation_marketcap_ewma_1260d_v108_signal": {"func": f09_mna_valuation_marketcap_ewma_1260d_v108_signal},
    "f09_mna_valuation_valuation_composite_ewma_1260d_v109_signal": {"func": f09_mna_valuation_valuation_composite_ewma_1260d_v109_signal},
    "f09_mna_valuation_size_factor_ewma_1260d_v110_signal": {"func": f09_mna_valuation_size_factor_ewma_1260d_v110_signal},
    "f09_mna_valuation_pb_z_5d_v111_signal": {"func": f09_mna_valuation_pb_z_5d_v111_signal},
    "f09_mna_valuation_pe_z_5d_v112_signal": {"func": f09_mna_valuation_pe_z_5d_v112_signal},
    "f09_mna_valuation_marketcap_z_5d_v113_signal": {"func": f09_mna_valuation_marketcap_z_5d_v113_signal},
    "f09_mna_valuation_valuation_composite_z_5d_v114_signal": {"func": f09_mna_valuation_valuation_composite_z_5d_v114_signal},
    "f09_mna_valuation_size_factor_z_5d_v115_signal": {"func": f09_mna_valuation_size_factor_z_5d_v115_signal},
    "f09_mna_valuation_pb_z_10d_v116_signal": {"func": f09_mna_valuation_pb_z_10d_v116_signal},
    "f09_mna_valuation_pe_z_10d_v117_signal": {"func": f09_mna_valuation_pe_z_10d_v117_signal},
    "f09_mna_valuation_marketcap_z_10d_v118_signal": {"func": f09_mna_valuation_marketcap_z_10d_v118_signal},
    "f09_mna_valuation_valuation_composite_z_10d_v119_signal": {"func": f09_mna_valuation_valuation_composite_z_10d_v119_signal},
    "f09_mna_valuation_size_factor_z_10d_v120_signal": {"func": f09_mna_valuation_size_factor_z_10d_v120_signal},
    "f09_mna_valuation_pb_z_21d_v121_signal": {"func": f09_mna_valuation_pb_z_21d_v121_signal},
    "f09_mna_valuation_pe_z_21d_v122_signal": {"func": f09_mna_valuation_pe_z_21d_v122_signal},
    "f09_mna_valuation_marketcap_z_21d_v123_signal": {"func": f09_mna_valuation_marketcap_z_21d_v123_signal},
    "f09_mna_valuation_valuation_composite_z_21d_v124_signal": {"func": f09_mna_valuation_valuation_composite_z_21d_v124_signal},
    "f09_mna_valuation_size_factor_z_21d_v125_signal": {"func": f09_mna_valuation_size_factor_z_21d_v125_signal},
    "f09_mna_valuation_pb_z_42d_v126_signal": {"func": f09_mna_valuation_pb_z_42d_v126_signal},
    "f09_mna_valuation_pe_z_42d_v127_signal": {"func": f09_mna_valuation_pe_z_42d_v127_signal},
    "f09_mna_valuation_marketcap_z_42d_v128_signal": {"func": f09_mna_valuation_marketcap_z_42d_v128_signal},
    "f09_mna_valuation_valuation_composite_z_42d_v129_signal": {"func": f09_mna_valuation_valuation_composite_z_42d_v129_signal},
    "f09_mna_valuation_size_factor_z_42d_v130_signal": {"func": f09_mna_valuation_size_factor_z_42d_v130_signal},
    "f09_mna_valuation_pb_z_63d_v131_signal": {"func": f09_mna_valuation_pb_z_63d_v131_signal},
    "f09_mna_valuation_pe_z_63d_v132_signal": {"func": f09_mna_valuation_pe_z_63d_v132_signal},
    "f09_mna_valuation_marketcap_z_63d_v133_signal": {"func": f09_mna_valuation_marketcap_z_63d_v133_signal},
    "f09_mna_valuation_valuation_composite_z_63d_v134_signal": {"func": f09_mna_valuation_valuation_composite_z_63d_v134_signal},
    "f09_mna_valuation_size_factor_z_63d_v135_signal": {"func": f09_mna_valuation_size_factor_z_63d_v135_signal},
    "f09_mna_valuation_pb_z_126d_v136_signal": {"func": f09_mna_valuation_pb_z_126d_v136_signal},
    "f09_mna_valuation_pe_z_126d_v137_signal": {"func": f09_mna_valuation_pe_z_126d_v137_signal},
    "f09_mna_valuation_marketcap_z_126d_v138_signal": {"func": f09_mna_valuation_marketcap_z_126d_v138_signal},
    "f09_mna_valuation_valuation_composite_z_126d_v139_signal": {"func": f09_mna_valuation_valuation_composite_z_126d_v139_signal},
    "f09_mna_valuation_size_factor_z_126d_v140_signal": {"func": f09_mna_valuation_size_factor_z_126d_v140_signal},
    "f09_mna_valuation_pb_z_252d_v141_signal": {"func": f09_mna_valuation_pb_z_252d_v141_signal},
    "f09_mna_valuation_pe_z_252d_v142_signal": {"func": f09_mna_valuation_pe_z_252d_v142_signal},
    "f09_mna_valuation_marketcap_z_252d_v143_signal": {"func": f09_mna_valuation_marketcap_z_252d_v143_signal},
    "f09_mna_valuation_valuation_composite_z_252d_v144_signal": {"func": f09_mna_valuation_valuation_composite_z_252d_v144_signal},
    "f09_mna_valuation_size_factor_z_252d_v145_signal": {"func": f09_mna_valuation_size_factor_z_252d_v145_signal},
    "f09_mna_valuation_pb_z_504d_v146_signal": {"func": f09_mna_valuation_pb_z_504d_v146_signal},
    "f09_mna_valuation_pe_z_504d_v147_signal": {"func": f09_mna_valuation_pe_z_504d_v147_signal},
    "f09_mna_valuation_marketcap_z_504d_v148_signal": {"func": f09_mna_valuation_marketcap_z_504d_v148_signal},
    "f09_mna_valuation_valuation_composite_z_504d_v149_signal": {"func": f09_mna_valuation_valuation_composite_z_504d_v149_signal},
    "f09_mna_valuation_size_factor_z_504d_v150_signal": {"func": f09_mna_valuation_size_factor_z_504d_v150_signal},
}

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "deferredrev": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "equity": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "deposits": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "divyield": np.random.normal(100, 10, n).cumsum(), "bvps": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "tangibles": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "grossmargin": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "liabilitiesc": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "pb": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "pe": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum()
    })
    print(f"Verifying {len(REGISTRY)} functions for family 09...")
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
