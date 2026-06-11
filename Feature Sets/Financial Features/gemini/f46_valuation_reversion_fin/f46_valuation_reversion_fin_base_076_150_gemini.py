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

def f46_valuation_reversion_fin_pb_cycle_z_ewma_504d_v076_signal(pb):
    """Exponential moving average of Long-term valuation cycle Z-score over 504d window."""
    res = _ewma(_z(pb, 1260), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_pb_ewma_756d_v077_signal(pb):
    """Exponential moving average of Raw level of pb over 756d window."""
    res = _ewma(pb, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_pe_ewma_756d_v078_signal(pe):
    """Exponential moving average of Raw level of pe over 756d window."""
    res = _ewma(pe, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_ev_ewma_756d_v079_signal(ev):
    """Exponential moving average of Raw level of ev over 756d window."""
    res = _ewma(ev, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_pb_cycle_z_ewma_756d_v080_signal(pb):
    """Exponential moving average of Long-term valuation cycle Z-score over 756d window."""
    res = _ewma(_z(pb, 1260), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_pb_ewma_1008d_v081_signal(pb):
    """Exponential moving average of Raw level of pb over 1008d window."""
    res = _ewma(pb, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_pe_ewma_1008d_v082_signal(pe):
    """Exponential moving average of Raw level of pe over 1008d window."""
    res = _ewma(pe, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_ev_ewma_1008d_v083_signal(ev):
    """Exponential moving average of Raw level of ev over 1008d window."""
    res = _ewma(ev, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_pb_cycle_z_ewma_1008d_v084_signal(pb):
    """Exponential moving average of Long-term valuation cycle Z-score over 1008d window."""
    res = _ewma(_z(pb, 1260), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_pb_ewma_1260d_v085_signal(pb):
    """Exponential moving average of Raw level of pb over 1260d window."""
    res = _ewma(pb, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_pe_ewma_1260d_v086_signal(pe):
    """Exponential moving average of Raw level of pe over 1260d window."""
    res = _ewma(pe, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_ev_ewma_1260d_v087_signal(ev):
    """Exponential moving average of Raw level of ev over 1260d window."""
    res = _ewma(ev, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_pb_cycle_z_ewma_1260d_v088_signal(pb):
    """Exponential moving average of Long-term valuation cycle Z-score over 1260d window."""
    res = _ewma(_z(pb, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_pb_z_5d_v089_signal(pb):
    """Z-score of Raw level of pb over 5d window."""
    res = _z(pb, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_pe_z_5d_v090_signal(pe):
    """Z-score of Raw level of pe over 5d window."""
    res = _z(pe, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_ev_z_5d_v091_signal(ev):
    """Z-score of Raw level of ev over 5d window."""
    res = _z(ev, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_pb_cycle_z_z_5d_v092_signal(pb):
    """Z-score of Long-term valuation cycle Z-score over 5d window."""
    res = _z(_z(pb, 1260), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_pb_z_10d_v093_signal(pb):
    """Z-score of Raw level of pb over 10d window."""
    res = _z(pb, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_pe_z_10d_v094_signal(pe):
    """Z-score of Raw level of pe over 10d window."""
    res = _z(pe, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_ev_z_10d_v095_signal(ev):
    """Z-score of Raw level of ev over 10d window."""
    res = _z(ev, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_pb_cycle_z_z_10d_v096_signal(pb):
    """Z-score of Long-term valuation cycle Z-score over 10d window."""
    res = _z(_z(pb, 1260), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_pb_z_21d_v097_signal(pb):
    """Z-score of Raw level of pb over 21d window."""
    res = _z(pb, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_pe_z_21d_v098_signal(pe):
    """Z-score of Raw level of pe over 21d window."""
    res = _z(pe, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_ev_z_21d_v099_signal(ev):
    """Z-score of Raw level of ev over 21d window."""
    res = _z(ev, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_pb_cycle_z_z_21d_v100_signal(pb):
    """Z-score of Long-term valuation cycle Z-score over 21d window."""
    res = _z(_z(pb, 1260), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_pb_z_42d_v101_signal(pb):
    """Z-score of Raw level of pb over 42d window."""
    res = _z(pb, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_pe_z_42d_v102_signal(pe):
    """Z-score of Raw level of pe over 42d window."""
    res = _z(pe, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_ev_z_42d_v103_signal(ev):
    """Z-score of Raw level of ev over 42d window."""
    res = _z(ev, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_pb_cycle_z_z_42d_v104_signal(pb):
    """Z-score of Long-term valuation cycle Z-score over 42d window."""
    res = _z(_z(pb, 1260), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_pb_z_63d_v105_signal(pb):
    """Z-score of Raw level of pb over 63d window."""
    res = _z(pb, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_pe_z_63d_v106_signal(pe):
    """Z-score of Raw level of pe over 63d window."""
    res = _z(pe, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_ev_z_63d_v107_signal(ev):
    """Z-score of Raw level of ev over 63d window."""
    res = _z(ev, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_pb_cycle_z_z_63d_v108_signal(pb):
    """Z-score of Long-term valuation cycle Z-score over 63d window."""
    res = _z(_z(pb, 1260), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_pb_z_126d_v109_signal(pb):
    """Z-score of Raw level of pb over 126d window."""
    res = _z(pb, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_pe_z_126d_v110_signal(pe):
    """Z-score of Raw level of pe over 126d window."""
    res = _z(pe, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_ev_z_126d_v111_signal(ev):
    """Z-score of Raw level of ev over 126d window."""
    res = _z(ev, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_pb_cycle_z_z_126d_v112_signal(pb):
    """Z-score of Long-term valuation cycle Z-score over 126d window."""
    res = _z(_z(pb, 1260), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_pb_z_252d_v113_signal(pb):
    """Z-score of Raw level of pb over 252d window."""
    res = _z(pb, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_pe_z_252d_v114_signal(pe):
    """Z-score of Raw level of pe over 252d window."""
    res = _z(pe, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_ev_z_252d_v115_signal(ev):
    """Z-score of Raw level of ev over 252d window."""
    res = _z(ev, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_pb_cycle_z_z_252d_v116_signal(pb):
    """Z-score of Long-term valuation cycle Z-score over 252d window."""
    res = _z(_z(pb, 1260), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_pb_z_504d_v117_signal(pb):
    """Z-score of Raw level of pb over 504d window."""
    res = _z(pb, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_pe_z_504d_v118_signal(pe):
    """Z-score of Raw level of pe over 504d window."""
    res = _z(pe, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_ev_z_504d_v119_signal(ev):
    """Z-score of Raw level of ev over 504d window."""
    res = _z(ev, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_pb_cycle_z_z_504d_v120_signal(pb):
    """Z-score of Long-term valuation cycle Z-score over 504d window."""
    res = _z(_z(pb, 1260), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_pb_z_756d_v121_signal(pb):
    """Z-score of Raw level of pb over 756d window."""
    res = _z(pb, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_pe_z_756d_v122_signal(pe):
    """Z-score of Raw level of pe over 756d window."""
    res = _z(pe, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_ev_z_756d_v123_signal(ev):
    """Z-score of Raw level of ev over 756d window."""
    res = _z(ev, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_pb_cycle_z_z_756d_v124_signal(pb):
    """Z-score of Long-term valuation cycle Z-score over 756d window."""
    res = _z(_z(pb, 1260), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_pb_z_1008d_v125_signal(pb):
    """Z-score of Raw level of pb over 1008d window."""
    res = _z(pb, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_pe_z_1008d_v126_signal(pe):
    """Z-score of Raw level of pe over 1008d window."""
    res = _z(pe, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_ev_z_1008d_v127_signal(ev):
    """Z-score of Raw level of ev over 1008d window."""
    res = _z(ev, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_pb_cycle_z_z_1008d_v128_signal(pb):
    """Z-score of Long-term valuation cycle Z-score over 1008d window."""
    res = _z(_z(pb, 1260), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_pb_z_1260d_v129_signal(pb):
    """Z-score of Raw level of pb over 1260d window."""
    res = _z(pb, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_pe_z_1260d_v130_signal(pe):
    """Z-score of Raw level of pe over 1260d window."""
    res = _z(pe, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_ev_z_1260d_v131_signal(ev):
    """Z-score of Raw level of ev over 1260d window."""
    res = _z(ev, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_pb_cycle_z_z_1260d_v132_signal(pb):
    """Z-score of Long-term valuation cycle Z-score over 1260d window."""
    res = _z(_z(pb, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_pb_dd_5d_v133_signal(pb):
    """Drawdown of Raw level of pb over 5d window."""
    res = _drawdown(pb, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_pe_dd_5d_v134_signal(pe):
    """Drawdown of Raw level of pe over 5d window."""
    res = _drawdown(pe, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_ev_dd_5d_v135_signal(ev):
    """Drawdown of Raw level of ev over 5d window."""
    res = _drawdown(ev, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_pb_cycle_z_dd_5d_v136_signal(pb):
    """Drawdown of Long-term valuation cycle Z-score over 5d window."""
    res = _drawdown(_z(pb, 1260), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_pb_dd_10d_v137_signal(pb):
    """Drawdown of Raw level of pb over 10d window."""
    res = _drawdown(pb, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_pe_dd_10d_v138_signal(pe):
    """Drawdown of Raw level of pe over 10d window."""
    res = _drawdown(pe, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_ev_dd_10d_v139_signal(ev):
    """Drawdown of Raw level of ev over 10d window."""
    res = _drawdown(ev, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_pb_cycle_z_dd_10d_v140_signal(pb):
    """Drawdown of Long-term valuation cycle Z-score over 10d window."""
    res = _drawdown(_z(pb, 1260), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_pb_dd_21d_v141_signal(pb):
    """Drawdown of Raw level of pb over 21d window."""
    res = _drawdown(pb, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_pe_dd_21d_v142_signal(pe):
    """Drawdown of Raw level of pe over 21d window."""
    res = _drawdown(pe, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_ev_dd_21d_v143_signal(ev):
    """Drawdown of Raw level of ev over 21d window."""
    res = _drawdown(ev, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_pb_cycle_z_dd_21d_v144_signal(pb):
    """Drawdown of Long-term valuation cycle Z-score over 21d window."""
    res = _drawdown(_z(pb, 1260), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_pb_dd_42d_v145_signal(pb):
    """Drawdown of Raw level of pb over 42d window."""
    res = _drawdown(pb, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_pe_dd_42d_v146_signal(pe):
    """Drawdown of Raw level of pe over 42d window."""
    res = _drawdown(pe, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_ev_dd_42d_v147_signal(ev):
    """Drawdown of Raw level of ev over 42d window."""
    res = _drawdown(ev, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_pb_cycle_z_dd_42d_v148_signal(pb):
    """Drawdown of Long-term valuation cycle Z-score over 42d window."""
    res = _drawdown(_z(pb, 1260), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_pb_dd_63d_v149_signal(pb):
    """Drawdown of Raw level of pb over 63d window."""
    res = _drawdown(pb, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_valuation_reversion_fin_pe_dd_63d_v150_signal(pe):
    """Drawdown of Raw level of pe over 63d window."""
    res = _drawdown(pe, 63)
    return res.replace([np.inf, -np.inf], np.nan)


# ===== Feature Registry =====
REGISTRY = {
    "f46_valuation_reversion_fin_pb_cycle_z_ewma_504d_v076_signal": {"func": f46_valuation_reversion_fin_pb_cycle_z_ewma_504d_v076_signal},
    "f46_valuation_reversion_fin_pb_ewma_756d_v077_signal": {"func": f46_valuation_reversion_fin_pb_ewma_756d_v077_signal},
    "f46_valuation_reversion_fin_pe_ewma_756d_v078_signal": {"func": f46_valuation_reversion_fin_pe_ewma_756d_v078_signal},
    "f46_valuation_reversion_fin_ev_ewma_756d_v079_signal": {"func": f46_valuation_reversion_fin_ev_ewma_756d_v079_signal},
    "f46_valuation_reversion_fin_pb_cycle_z_ewma_756d_v080_signal": {"func": f46_valuation_reversion_fin_pb_cycle_z_ewma_756d_v080_signal},
    "f46_valuation_reversion_fin_pb_ewma_1008d_v081_signal": {"func": f46_valuation_reversion_fin_pb_ewma_1008d_v081_signal},
    "f46_valuation_reversion_fin_pe_ewma_1008d_v082_signal": {"func": f46_valuation_reversion_fin_pe_ewma_1008d_v082_signal},
    "f46_valuation_reversion_fin_ev_ewma_1008d_v083_signal": {"func": f46_valuation_reversion_fin_ev_ewma_1008d_v083_signal},
    "f46_valuation_reversion_fin_pb_cycle_z_ewma_1008d_v084_signal": {"func": f46_valuation_reversion_fin_pb_cycle_z_ewma_1008d_v084_signal},
    "f46_valuation_reversion_fin_pb_ewma_1260d_v085_signal": {"func": f46_valuation_reversion_fin_pb_ewma_1260d_v085_signal},
    "f46_valuation_reversion_fin_pe_ewma_1260d_v086_signal": {"func": f46_valuation_reversion_fin_pe_ewma_1260d_v086_signal},
    "f46_valuation_reversion_fin_ev_ewma_1260d_v087_signal": {"func": f46_valuation_reversion_fin_ev_ewma_1260d_v087_signal},
    "f46_valuation_reversion_fin_pb_cycle_z_ewma_1260d_v088_signal": {"func": f46_valuation_reversion_fin_pb_cycle_z_ewma_1260d_v088_signal},
    "f46_valuation_reversion_fin_pb_z_5d_v089_signal": {"func": f46_valuation_reversion_fin_pb_z_5d_v089_signal},
    "f46_valuation_reversion_fin_pe_z_5d_v090_signal": {"func": f46_valuation_reversion_fin_pe_z_5d_v090_signal},
    "f46_valuation_reversion_fin_ev_z_5d_v091_signal": {"func": f46_valuation_reversion_fin_ev_z_5d_v091_signal},
    "f46_valuation_reversion_fin_pb_cycle_z_z_5d_v092_signal": {"func": f46_valuation_reversion_fin_pb_cycle_z_z_5d_v092_signal},
    "f46_valuation_reversion_fin_pb_z_10d_v093_signal": {"func": f46_valuation_reversion_fin_pb_z_10d_v093_signal},
    "f46_valuation_reversion_fin_pe_z_10d_v094_signal": {"func": f46_valuation_reversion_fin_pe_z_10d_v094_signal},
    "f46_valuation_reversion_fin_ev_z_10d_v095_signal": {"func": f46_valuation_reversion_fin_ev_z_10d_v095_signal},
    "f46_valuation_reversion_fin_pb_cycle_z_z_10d_v096_signal": {"func": f46_valuation_reversion_fin_pb_cycle_z_z_10d_v096_signal},
    "f46_valuation_reversion_fin_pb_z_21d_v097_signal": {"func": f46_valuation_reversion_fin_pb_z_21d_v097_signal},
    "f46_valuation_reversion_fin_pe_z_21d_v098_signal": {"func": f46_valuation_reversion_fin_pe_z_21d_v098_signal},
    "f46_valuation_reversion_fin_ev_z_21d_v099_signal": {"func": f46_valuation_reversion_fin_ev_z_21d_v099_signal},
    "f46_valuation_reversion_fin_pb_cycle_z_z_21d_v100_signal": {"func": f46_valuation_reversion_fin_pb_cycle_z_z_21d_v100_signal},
    "f46_valuation_reversion_fin_pb_z_42d_v101_signal": {"func": f46_valuation_reversion_fin_pb_z_42d_v101_signal},
    "f46_valuation_reversion_fin_pe_z_42d_v102_signal": {"func": f46_valuation_reversion_fin_pe_z_42d_v102_signal},
    "f46_valuation_reversion_fin_ev_z_42d_v103_signal": {"func": f46_valuation_reversion_fin_ev_z_42d_v103_signal},
    "f46_valuation_reversion_fin_pb_cycle_z_z_42d_v104_signal": {"func": f46_valuation_reversion_fin_pb_cycle_z_z_42d_v104_signal},
    "f46_valuation_reversion_fin_pb_z_63d_v105_signal": {"func": f46_valuation_reversion_fin_pb_z_63d_v105_signal},
    "f46_valuation_reversion_fin_pe_z_63d_v106_signal": {"func": f46_valuation_reversion_fin_pe_z_63d_v106_signal},
    "f46_valuation_reversion_fin_ev_z_63d_v107_signal": {"func": f46_valuation_reversion_fin_ev_z_63d_v107_signal},
    "f46_valuation_reversion_fin_pb_cycle_z_z_63d_v108_signal": {"func": f46_valuation_reversion_fin_pb_cycle_z_z_63d_v108_signal},
    "f46_valuation_reversion_fin_pb_z_126d_v109_signal": {"func": f46_valuation_reversion_fin_pb_z_126d_v109_signal},
    "f46_valuation_reversion_fin_pe_z_126d_v110_signal": {"func": f46_valuation_reversion_fin_pe_z_126d_v110_signal},
    "f46_valuation_reversion_fin_ev_z_126d_v111_signal": {"func": f46_valuation_reversion_fin_ev_z_126d_v111_signal},
    "f46_valuation_reversion_fin_pb_cycle_z_z_126d_v112_signal": {"func": f46_valuation_reversion_fin_pb_cycle_z_z_126d_v112_signal},
    "f46_valuation_reversion_fin_pb_z_252d_v113_signal": {"func": f46_valuation_reversion_fin_pb_z_252d_v113_signal},
    "f46_valuation_reversion_fin_pe_z_252d_v114_signal": {"func": f46_valuation_reversion_fin_pe_z_252d_v114_signal},
    "f46_valuation_reversion_fin_ev_z_252d_v115_signal": {"func": f46_valuation_reversion_fin_ev_z_252d_v115_signal},
    "f46_valuation_reversion_fin_pb_cycle_z_z_252d_v116_signal": {"func": f46_valuation_reversion_fin_pb_cycle_z_z_252d_v116_signal},
    "f46_valuation_reversion_fin_pb_z_504d_v117_signal": {"func": f46_valuation_reversion_fin_pb_z_504d_v117_signal},
    "f46_valuation_reversion_fin_pe_z_504d_v118_signal": {"func": f46_valuation_reversion_fin_pe_z_504d_v118_signal},
    "f46_valuation_reversion_fin_ev_z_504d_v119_signal": {"func": f46_valuation_reversion_fin_ev_z_504d_v119_signal},
    "f46_valuation_reversion_fin_pb_cycle_z_z_504d_v120_signal": {"func": f46_valuation_reversion_fin_pb_cycle_z_z_504d_v120_signal},
    "f46_valuation_reversion_fin_pb_z_756d_v121_signal": {"func": f46_valuation_reversion_fin_pb_z_756d_v121_signal},
    "f46_valuation_reversion_fin_pe_z_756d_v122_signal": {"func": f46_valuation_reversion_fin_pe_z_756d_v122_signal},
    "f46_valuation_reversion_fin_ev_z_756d_v123_signal": {"func": f46_valuation_reversion_fin_ev_z_756d_v123_signal},
    "f46_valuation_reversion_fin_pb_cycle_z_z_756d_v124_signal": {"func": f46_valuation_reversion_fin_pb_cycle_z_z_756d_v124_signal},
    "f46_valuation_reversion_fin_pb_z_1008d_v125_signal": {"func": f46_valuation_reversion_fin_pb_z_1008d_v125_signal},
    "f46_valuation_reversion_fin_pe_z_1008d_v126_signal": {"func": f46_valuation_reversion_fin_pe_z_1008d_v126_signal},
    "f46_valuation_reversion_fin_ev_z_1008d_v127_signal": {"func": f46_valuation_reversion_fin_ev_z_1008d_v127_signal},
    "f46_valuation_reversion_fin_pb_cycle_z_z_1008d_v128_signal": {"func": f46_valuation_reversion_fin_pb_cycle_z_z_1008d_v128_signal},
    "f46_valuation_reversion_fin_pb_z_1260d_v129_signal": {"func": f46_valuation_reversion_fin_pb_z_1260d_v129_signal},
    "f46_valuation_reversion_fin_pe_z_1260d_v130_signal": {"func": f46_valuation_reversion_fin_pe_z_1260d_v130_signal},
    "f46_valuation_reversion_fin_ev_z_1260d_v131_signal": {"func": f46_valuation_reversion_fin_ev_z_1260d_v131_signal},
    "f46_valuation_reversion_fin_pb_cycle_z_z_1260d_v132_signal": {"func": f46_valuation_reversion_fin_pb_cycle_z_z_1260d_v132_signal},
    "f46_valuation_reversion_fin_pb_dd_5d_v133_signal": {"func": f46_valuation_reversion_fin_pb_dd_5d_v133_signal},
    "f46_valuation_reversion_fin_pe_dd_5d_v134_signal": {"func": f46_valuation_reversion_fin_pe_dd_5d_v134_signal},
    "f46_valuation_reversion_fin_ev_dd_5d_v135_signal": {"func": f46_valuation_reversion_fin_ev_dd_5d_v135_signal},
    "f46_valuation_reversion_fin_pb_cycle_z_dd_5d_v136_signal": {"func": f46_valuation_reversion_fin_pb_cycle_z_dd_5d_v136_signal},
    "f46_valuation_reversion_fin_pb_dd_10d_v137_signal": {"func": f46_valuation_reversion_fin_pb_dd_10d_v137_signal},
    "f46_valuation_reversion_fin_pe_dd_10d_v138_signal": {"func": f46_valuation_reversion_fin_pe_dd_10d_v138_signal},
    "f46_valuation_reversion_fin_ev_dd_10d_v139_signal": {"func": f46_valuation_reversion_fin_ev_dd_10d_v139_signal},
    "f46_valuation_reversion_fin_pb_cycle_z_dd_10d_v140_signal": {"func": f46_valuation_reversion_fin_pb_cycle_z_dd_10d_v140_signal},
    "f46_valuation_reversion_fin_pb_dd_21d_v141_signal": {"func": f46_valuation_reversion_fin_pb_dd_21d_v141_signal},
    "f46_valuation_reversion_fin_pe_dd_21d_v142_signal": {"func": f46_valuation_reversion_fin_pe_dd_21d_v142_signal},
    "f46_valuation_reversion_fin_ev_dd_21d_v143_signal": {"func": f46_valuation_reversion_fin_ev_dd_21d_v143_signal},
    "f46_valuation_reversion_fin_pb_cycle_z_dd_21d_v144_signal": {"func": f46_valuation_reversion_fin_pb_cycle_z_dd_21d_v144_signal},
    "f46_valuation_reversion_fin_pb_dd_42d_v145_signal": {"func": f46_valuation_reversion_fin_pb_dd_42d_v145_signal},
    "f46_valuation_reversion_fin_pe_dd_42d_v146_signal": {"func": f46_valuation_reversion_fin_pe_dd_42d_v146_signal},
    "f46_valuation_reversion_fin_ev_dd_42d_v147_signal": {"func": f46_valuation_reversion_fin_ev_dd_42d_v147_signal},
    "f46_valuation_reversion_fin_pb_cycle_z_dd_42d_v148_signal": {"func": f46_valuation_reversion_fin_pb_cycle_z_dd_42d_v148_signal},
    "f46_valuation_reversion_fin_pb_dd_63d_v149_signal": {"func": f46_valuation_reversion_fin_pb_dd_63d_v149_signal},
    "f46_valuation_reversion_fin_pe_dd_63d_v150_signal": {"func": f46_valuation_reversion_fin_pe_dd_63d_v150_signal},
}

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "deferredrev": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "equity": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "deposits": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "divyield": np.random.normal(100, 10, n).cumsum(), "bvps": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "tangibles": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "grossmargin": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "liabilitiesc": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "pb": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "ev": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "pe": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum()
    })
    print(f"Verifying {len(REGISTRY)} functions for family 46...")
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
