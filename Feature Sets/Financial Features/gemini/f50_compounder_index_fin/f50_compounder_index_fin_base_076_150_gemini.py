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

def f50_compounder_index_fin_quality_valuation_index_ewma_504d_v076_signal(netinc, equity, pb):
    """Exponential moving average of ROE relative to P/B valuation over 504d window."""
    res = _ewma(_ratio(netinc, equity) / pb, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_compounder_index_fin_pb_ewma_756d_v077_signal(pb):
    """Exponential moving average of Raw level of pb over 756d window."""
    res = _ewma(pb, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_compounder_index_fin_netinc_ewma_756d_v078_signal(netinc):
    """Exponential moving average of Raw level of netinc over 756d window."""
    res = _ewma(netinc, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_compounder_index_fin_equity_ewma_756d_v079_signal(equity):
    """Exponential moving average of Raw level of equity over 756d window."""
    res = _ewma(equity, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_compounder_index_fin_quality_valuation_index_ewma_756d_v080_signal(netinc, equity, pb):
    """Exponential moving average of ROE relative to P/B valuation over 756d window."""
    res = _ewma(_ratio(netinc, equity) / pb, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_compounder_index_fin_pb_ewma_1008d_v081_signal(pb):
    """Exponential moving average of Raw level of pb over 1008d window."""
    res = _ewma(pb, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_compounder_index_fin_netinc_ewma_1008d_v082_signal(netinc):
    """Exponential moving average of Raw level of netinc over 1008d window."""
    res = _ewma(netinc, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_compounder_index_fin_equity_ewma_1008d_v083_signal(equity):
    """Exponential moving average of Raw level of equity over 1008d window."""
    res = _ewma(equity, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_compounder_index_fin_quality_valuation_index_ewma_1008d_v084_signal(netinc, equity, pb):
    """Exponential moving average of ROE relative to P/B valuation over 1008d window."""
    res = _ewma(_ratio(netinc, equity) / pb, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_compounder_index_fin_pb_ewma_1260d_v085_signal(pb):
    """Exponential moving average of Raw level of pb over 1260d window."""
    res = _ewma(pb, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_compounder_index_fin_netinc_ewma_1260d_v086_signal(netinc):
    """Exponential moving average of Raw level of netinc over 1260d window."""
    res = _ewma(netinc, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_compounder_index_fin_equity_ewma_1260d_v087_signal(equity):
    """Exponential moving average of Raw level of equity over 1260d window."""
    res = _ewma(equity, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_compounder_index_fin_quality_valuation_index_ewma_1260d_v088_signal(netinc, equity, pb):
    """Exponential moving average of ROE relative to P/B valuation over 1260d window."""
    res = _ewma(_ratio(netinc, equity) / pb, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_compounder_index_fin_pb_z_5d_v089_signal(pb):
    """Z-score of Raw level of pb over 5d window."""
    res = _z(pb, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_compounder_index_fin_netinc_z_5d_v090_signal(netinc):
    """Z-score of Raw level of netinc over 5d window."""
    res = _z(netinc, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_compounder_index_fin_equity_z_5d_v091_signal(equity):
    """Z-score of Raw level of equity over 5d window."""
    res = _z(equity, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_compounder_index_fin_quality_valuation_index_z_5d_v092_signal(netinc, equity, pb):
    """Z-score of ROE relative to P/B valuation over 5d window."""
    res = _z(_ratio(netinc, equity) / pb, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_compounder_index_fin_pb_z_10d_v093_signal(pb):
    """Z-score of Raw level of pb over 10d window."""
    res = _z(pb, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_compounder_index_fin_netinc_z_10d_v094_signal(netinc):
    """Z-score of Raw level of netinc over 10d window."""
    res = _z(netinc, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_compounder_index_fin_equity_z_10d_v095_signal(equity):
    """Z-score of Raw level of equity over 10d window."""
    res = _z(equity, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_compounder_index_fin_quality_valuation_index_z_10d_v096_signal(netinc, equity, pb):
    """Z-score of ROE relative to P/B valuation over 10d window."""
    res = _z(_ratio(netinc, equity) / pb, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_compounder_index_fin_pb_z_21d_v097_signal(pb):
    """Z-score of Raw level of pb over 21d window."""
    res = _z(pb, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_compounder_index_fin_netinc_z_21d_v098_signal(netinc):
    """Z-score of Raw level of netinc over 21d window."""
    res = _z(netinc, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_compounder_index_fin_equity_z_21d_v099_signal(equity):
    """Z-score of Raw level of equity over 21d window."""
    res = _z(equity, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_compounder_index_fin_quality_valuation_index_z_21d_v100_signal(netinc, equity, pb):
    """Z-score of ROE relative to P/B valuation over 21d window."""
    res = _z(_ratio(netinc, equity) / pb, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_compounder_index_fin_pb_z_42d_v101_signal(pb):
    """Z-score of Raw level of pb over 42d window."""
    res = _z(pb, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_compounder_index_fin_netinc_z_42d_v102_signal(netinc):
    """Z-score of Raw level of netinc over 42d window."""
    res = _z(netinc, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_compounder_index_fin_equity_z_42d_v103_signal(equity):
    """Z-score of Raw level of equity over 42d window."""
    res = _z(equity, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_compounder_index_fin_quality_valuation_index_z_42d_v104_signal(netinc, equity, pb):
    """Z-score of ROE relative to P/B valuation over 42d window."""
    res = _z(_ratio(netinc, equity) / pb, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_compounder_index_fin_pb_z_63d_v105_signal(pb):
    """Z-score of Raw level of pb over 63d window."""
    res = _z(pb, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_compounder_index_fin_netinc_z_63d_v106_signal(netinc):
    """Z-score of Raw level of netinc over 63d window."""
    res = _z(netinc, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_compounder_index_fin_equity_z_63d_v107_signal(equity):
    """Z-score of Raw level of equity over 63d window."""
    res = _z(equity, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_compounder_index_fin_quality_valuation_index_z_63d_v108_signal(netinc, equity, pb):
    """Z-score of ROE relative to P/B valuation over 63d window."""
    res = _z(_ratio(netinc, equity) / pb, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_compounder_index_fin_pb_z_126d_v109_signal(pb):
    """Z-score of Raw level of pb over 126d window."""
    res = _z(pb, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_compounder_index_fin_netinc_z_126d_v110_signal(netinc):
    """Z-score of Raw level of netinc over 126d window."""
    res = _z(netinc, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_compounder_index_fin_equity_z_126d_v111_signal(equity):
    """Z-score of Raw level of equity over 126d window."""
    res = _z(equity, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_compounder_index_fin_quality_valuation_index_z_126d_v112_signal(netinc, equity, pb):
    """Z-score of ROE relative to P/B valuation over 126d window."""
    res = _z(_ratio(netinc, equity) / pb, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_compounder_index_fin_pb_z_252d_v113_signal(pb):
    """Z-score of Raw level of pb over 252d window."""
    res = _z(pb, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_compounder_index_fin_netinc_z_252d_v114_signal(netinc):
    """Z-score of Raw level of netinc over 252d window."""
    res = _z(netinc, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_compounder_index_fin_equity_z_252d_v115_signal(equity):
    """Z-score of Raw level of equity over 252d window."""
    res = _z(equity, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_compounder_index_fin_quality_valuation_index_z_252d_v116_signal(netinc, equity, pb):
    """Z-score of ROE relative to P/B valuation over 252d window."""
    res = _z(_ratio(netinc, equity) / pb, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_compounder_index_fin_pb_z_504d_v117_signal(pb):
    """Z-score of Raw level of pb over 504d window."""
    res = _z(pb, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_compounder_index_fin_netinc_z_504d_v118_signal(netinc):
    """Z-score of Raw level of netinc over 504d window."""
    res = _z(netinc, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_compounder_index_fin_equity_z_504d_v119_signal(equity):
    """Z-score of Raw level of equity over 504d window."""
    res = _z(equity, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_compounder_index_fin_quality_valuation_index_z_504d_v120_signal(netinc, equity, pb):
    """Z-score of ROE relative to P/B valuation over 504d window."""
    res = _z(_ratio(netinc, equity) / pb, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_compounder_index_fin_pb_z_756d_v121_signal(pb):
    """Z-score of Raw level of pb over 756d window."""
    res = _z(pb, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_compounder_index_fin_netinc_z_756d_v122_signal(netinc):
    """Z-score of Raw level of netinc over 756d window."""
    res = _z(netinc, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_compounder_index_fin_equity_z_756d_v123_signal(equity):
    """Z-score of Raw level of equity over 756d window."""
    res = _z(equity, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_compounder_index_fin_quality_valuation_index_z_756d_v124_signal(netinc, equity, pb):
    """Z-score of ROE relative to P/B valuation over 756d window."""
    res = _z(_ratio(netinc, equity) / pb, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_compounder_index_fin_pb_z_1008d_v125_signal(pb):
    """Z-score of Raw level of pb over 1008d window."""
    res = _z(pb, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_compounder_index_fin_netinc_z_1008d_v126_signal(netinc):
    """Z-score of Raw level of netinc over 1008d window."""
    res = _z(netinc, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_compounder_index_fin_equity_z_1008d_v127_signal(equity):
    """Z-score of Raw level of equity over 1008d window."""
    res = _z(equity, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_compounder_index_fin_quality_valuation_index_z_1008d_v128_signal(netinc, equity, pb):
    """Z-score of ROE relative to P/B valuation over 1008d window."""
    res = _z(_ratio(netinc, equity) / pb, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_compounder_index_fin_pb_z_1260d_v129_signal(pb):
    """Z-score of Raw level of pb over 1260d window."""
    res = _z(pb, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_compounder_index_fin_netinc_z_1260d_v130_signal(netinc):
    """Z-score of Raw level of netinc over 1260d window."""
    res = _z(netinc, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_compounder_index_fin_equity_z_1260d_v131_signal(equity):
    """Z-score of Raw level of equity over 1260d window."""
    res = _z(equity, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_compounder_index_fin_quality_valuation_index_z_1260d_v132_signal(netinc, equity, pb):
    """Z-score of ROE relative to P/B valuation over 1260d window."""
    res = _z(_ratio(netinc, equity) / pb, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_compounder_index_fin_pb_dd_5d_v133_signal(pb):
    """Drawdown of Raw level of pb over 5d window."""
    res = _drawdown(pb, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_compounder_index_fin_netinc_dd_5d_v134_signal(netinc):
    """Drawdown of Raw level of netinc over 5d window."""
    res = _drawdown(netinc, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_compounder_index_fin_equity_dd_5d_v135_signal(equity):
    """Drawdown of Raw level of equity over 5d window."""
    res = _drawdown(equity, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_compounder_index_fin_quality_valuation_index_dd_5d_v136_signal(netinc, equity, pb):
    """Drawdown of ROE relative to P/B valuation over 5d window."""
    res = _drawdown(_ratio(netinc, equity) / pb, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_compounder_index_fin_pb_dd_10d_v137_signal(pb):
    """Drawdown of Raw level of pb over 10d window."""
    res = _drawdown(pb, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_compounder_index_fin_netinc_dd_10d_v138_signal(netinc):
    """Drawdown of Raw level of netinc over 10d window."""
    res = _drawdown(netinc, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_compounder_index_fin_equity_dd_10d_v139_signal(equity):
    """Drawdown of Raw level of equity over 10d window."""
    res = _drawdown(equity, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_compounder_index_fin_quality_valuation_index_dd_10d_v140_signal(netinc, equity, pb):
    """Drawdown of ROE relative to P/B valuation over 10d window."""
    res = _drawdown(_ratio(netinc, equity) / pb, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_compounder_index_fin_pb_dd_21d_v141_signal(pb):
    """Drawdown of Raw level of pb over 21d window."""
    res = _drawdown(pb, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_compounder_index_fin_netinc_dd_21d_v142_signal(netinc):
    """Drawdown of Raw level of netinc over 21d window."""
    res = _drawdown(netinc, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_compounder_index_fin_equity_dd_21d_v143_signal(equity):
    """Drawdown of Raw level of equity over 21d window."""
    res = _drawdown(equity, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_compounder_index_fin_quality_valuation_index_dd_21d_v144_signal(netinc, equity, pb):
    """Drawdown of ROE relative to P/B valuation over 21d window."""
    res = _drawdown(_ratio(netinc, equity) / pb, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_compounder_index_fin_pb_dd_42d_v145_signal(pb):
    """Drawdown of Raw level of pb over 42d window."""
    res = _drawdown(pb, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_compounder_index_fin_netinc_dd_42d_v146_signal(netinc):
    """Drawdown of Raw level of netinc over 42d window."""
    res = _drawdown(netinc, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_compounder_index_fin_equity_dd_42d_v147_signal(equity):
    """Drawdown of Raw level of equity over 42d window."""
    res = _drawdown(equity, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_compounder_index_fin_quality_valuation_index_dd_42d_v148_signal(netinc, equity, pb):
    """Drawdown of ROE relative to P/B valuation over 42d window."""
    res = _drawdown(_ratio(netinc, equity) / pb, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_compounder_index_fin_pb_dd_63d_v149_signal(pb):
    """Drawdown of Raw level of pb over 63d window."""
    res = _drawdown(pb, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_compounder_index_fin_netinc_dd_63d_v150_signal(netinc):
    """Drawdown of Raw level of netinc over 63d window."""
    res = _drawdown(netinc, 63)
    return res.replace([np.inf, -np.inf], np.nan)


# ===== Feature Registry =====
REGISTRY = {
    "f50_compounder_index_fin_quality_valuation_index_ewma_504d_v076_signal": {"func": f50_compounder_index_fin_quality_valuation_index_ewma_504d_v076_signal},
    "f50_compounder_index_fin_pb_ewma_756d_v077_signal": {"func": f50_compounder_index_fin_pb_ewma_756d_v077_signal},
    "f50_compounder_index_fin_netinc_ewma_756d_v078_signal": {"func": f50_compounder_index_fin_netinc_ewma_756d_v078_signal},
    "f50_compounder_index_fin_equity_ewma_756d_v079_signal": {"func": f50_compounder_index_fin_equity_ewma_756d_v079_signal},
    "f50_compounder_index_fin_quality_valuation_index_ewma_756d_v080_signal": {"func": f50_compounder_index_fin_quality_valuation_index_ewma_756d_v080_signal},
    "f50_compounder_index_fin_pb_ewma_1008d_v081_signal": {"func": f50_compounder_index_fin_pb_ewma_1008d_v081_signal},
    "f50_compounder_index_fin_netinc_ewma_1008d_v082_signal": {"func": f50_compounder_index_fin_netinc_ewma_1008d_v082_signal},
    "f50_compounder_index_fin_equity_ewma_1008d_v083_signal": {"func": f50_compounder_index_fin_equity_ewma_1008d_v083_signal},
    "f50_compounder_index_fin_quality_valuation_index_ewma_1008d_v084_signal": {"func": f50_compounder_index_fin_quality_valuation_index_ewma_1008d_v084_signal},
    "f50_compounder_index_fin_pb_ewma_1260d_v085_signal": {"func": f50_compounder_index_fin_pb_ewma_1260d_v085_signal},
    "f50_compounder_index_fin_netinc_ewma_1260d_v086_signal": {"func": f50_compounder_index_fin_netinc_ewma_1260d_v086_signal},
    "f50_compounder_index_fin_equity_ewma_1260d_v087_signal": {"func": f50_compounder_index_fin_equity_ewma_1260d_v087_signal},
    "f50_compounder_index_fin_quality_valuation_index_ewma_1260d_v088_signal": {"func": f50_compounder_index_fin_quality_valuation_index_ewma_1260d_v088_signal},
    "f50_compounder_index_fin_pb_z_5d_v089_signal": {"func": f50_compounder_index_fin_pb_z_5d_v089_signal},
    "f50_compounder_index_fin_netinc_z_5d_v090_signal": {"func": f50_compounder_index_fin_netinc_z_5d_v090_signal},
    "f50_compounder_index_fin_equity_z_5d_v091_signal": {"func": f50_compounder_index_fin_equity_z_5d_v091_signal},
    "f50_compounder_index_fin_quality_valuation_index_z_5d_v092_signal": {"func": f50_compounder_index_fin_quality_valuation_index_z_5d_v092_signal},
    "f50_compounder_index_fin_pb_z_10d_v093_signal": {"func": f50_compounder_index_fin_pb_z_10d_v093_signal},
    "f50_compounder_index_fin_netinc_z_10d_v094_signal": {"func": f50_compounder_index_fin_netinc_z_10d_v094_signal},
    "f50_compounder_index_fin_equity_z_10d_v095_signal": {"func": f50_compounder_index_fin_equity_z_10d_v095_signal},
    "f50_compounder_index_fin_quality_valuation_index_z_10d_v096_signal": {"func": f50_compounder_index_fin_quality_valuation_index_z_10d_v096_signal},
    "f50_compounder_index_fin_pb_z_21d_v097_signal": {"func": f50_compounder_index_fin_pb_z_21d_v097_signal},
    "f50_compounder_index_fin_netinc_z_21d_v098_signal": {"func": f50_compounder_index_fin_netinc_z_21d_v098_signal},
    "f50_compounder_index_fin_equity_z_21d_v099_signal": {"func": f50_compounder_index_fin_equity_z_21d_v099_signal},
    "f50_compounder_index_fin_quality_valuation_index_z_21d_v100_signal": {"func": f50_compounder_index_fin_quality_valuation_index_z_21d_v100_signal},
    "f50_compounder_index_fin_pb_z_42d_v101_signal": {"func": f50_compounder_index_fin_pb_z_42d_v101_signal},
    "f50_compounder_index_fin_netinc_z_42d_v102_signal": {"func": f50_compounder_index_fin_netinc_z_42d_v102_signal},
    "f50_compounder_index_fin_equity_z_42d_v103_signal": {"func": f50_compounder_index_fin_equity_z_42d_v103_signal},
    "f50_compounder_index_fin_quality_valuation_index_z_42d_v104_signal": {"func": f50_compounder_index_fin_quality_valuation_index_z_42d_v104_signal},
    "f50_compounder_index_fin_pb_z_63d_v105_signal": {"func": f50_compounder_index_fin_pb_z_63d_v105_signal},
    "f50_compounder_index_fin_netinc_z_63d_v106_signal": {"func": f50_compounder_index_fin_netinc_z_63d_v106_signal},
    "f50_compounder_index_fin_equity_z_63d_v107_signal": {"func": f50_compounder_index_fin_equity_z_63d_v107_signal},
    "f50_compounder_index_fin_quality_valuation_index_z_63d_v108_signal": {"func": f50_compounder_index_fin_quality_valuation_index_z_63d_v108_signal},
    "f50_compounder_index_fin_pb_z_126d_v109_signal": {"func": f50_compounder_index_fin_pb_z_126d_v109_signal},
    "f50_compounder_index_fin_netinc_z_126d_v110_signal": {"func": f50_compounder_index_fin_netinc_z_126d_v110_signal},
    "f50_compounder_index_fin_equity_z_126d_v111_signal": {"func": f50_compounder_index_fin_equity_z_126d_v111_signal},
    "f50_compounder_index_fin_quality_valuation_index_z_126d_v112_signal": {"func": f50_compounder_index_fin_quality_valuation_index_z_126d_v112_signal},
    "f50_compounder_index_fin_pb_z_252d_v113_signal": {"func": f50_compounder_index_fin_pb_z_252d_v113_signal},
    "f50_compounder_index_fin_netinc_z_252d_v114_signal": {"func": f50_compounder_index_fin_netinc_z_252d_v114_signal},
    "f50_compounder_index_fin_equity_z_252d_v115_signal": {"func": f50_compounder_index_fin_equity_z_252d_v115_signal},
    "f50_compounder_index_fin_quality_valuation_index_z_252d_v116_signal": {"func": f50_compounder_index_fin_quality_valuation_index_z_252d_v116_signal},
    "f50_compounder_index_fin_pb_z_504d_v117_signal": {"func": f50_compounder_index_fin_pb_z_504d_v117_signal},
    "f50_compounder_index_fin_netinc_z_504d_v118_signal": {"func": f50_compounder_index_fin_netinc_z_504d_v118_signal},
    "f50_compounder_index_fin_equity_z_504d_v119_signal": {"func": f50_compounder_index_fin_equity_z_504d_v119_signal},
    "f50_compounder_index_fin_quality_valuation_index_z_504d_v120_signal": {"func": f50_compounder_index_fin_quality_valuation_index_z_504d_v120_signal},
    "f50_compounder_index_fin_pb_z_756d_v121_signal": {"func": f50_compounder_index_fin_pb_z_756d_v121_signal},
    "f50_compounder_index_fin_netinc_z_756d_v122_signal": {"func": f50_compounder_index_fin_netinc_z_756d_v122_signal},
    "f50_compounder_index_fin_equity_z_756d_v123_signal": {"func": f50_compounder_index_fin_equity_z_756d_v123_signal},
    "f50_compounder_index_fin_quality_valuation_index_z_756d_v124_signal": {"func": f50_compounder_index_fin_quality_valuation_index_z_756d_v124_signal},
    "f50_compounder_index_fin_pb_z_1008d_v125_signal": {"func": f50_compounder_index_fin_pb_z_1008d_v125_signal},
    "f50_compounder_index_fin_netinc_z_1008d_v126_signal": {"func": f50_compounder_index_fin_netinc_z_1008d_v126_signal},
    "f50_compounder_index_fin_equity_z_1008d_v127_signal": {"func": f50_compounder_index_fin_equity_z_1008d_v127_signal},
    "f50_compounder_index_fin_quality_valuation_index_z_1008d_v128_signal": {"func": f50_compounder_index_fin_quality_valuation_index_z_1008d_v128_signal},
    "f50_compounder_index_fin_pb_z_1260d_v129_signal": {"func": f50_compounder_index_fin_pb_z_1260d_v129_signal},
    "f50_compounder_index_fin_netinc_z_1260d_v130_signal": {"func": f50_compounder_index_fin_netinc_z_1260d_v130_signal},
    "f50_compounder_index_fin_equity_z_1260d_v131_signal": {"func": f50_compounder_index_fin_equity_z_1260d_v131_signal},
    "f50_compounder_index_fin_quality_valuation_index_z_1260d_v132_signal": {"func": f50_compounder_index_fin_quality_valuation_index_z_1260d_v132_signal},
    "f50_compounder_index_fin_pb_dd_5d_v133_signal": {"func": f50_compounder_index_fin_pb_dd_5d_v133_signal},
    "f50_compounder_index_fin_netinc_dd_5d_v134_signal": {"func": f50_compounder_index_fin_netinc_dd_5d_v134_signal},
    "f50_compounder_index_fin_equity_dd_5d_v135_signal": {"func": f50_compounder_index_fin_equity_dd_5d_v135_signal},
    "f50_compounder_index_fin_quality_valuation_index_dd_5d_v136_signal": {"func": f50_compounder_index_fin_quality_valuation_index_dd_5d_v136_signal},
    "f50_compounder_index_fin_pb_dd_10d_v137_signal": {"func": f50_compounder_index_fin_pb_dd_10d_v137_signal},
    "f50_compounder_index_fin_netinc_dd_10d_v138_signal": {"func": f50_compounder_index_fin_netinc_dd_10d_v138_signal},
    "f50_compounder_index_fin_equity_dd_10d_v139_signal": {"func": f50_compounder_index_fin_equity_dd_10d_v139_signal},
    "f50_compounder_index_fin_quality_valuation_index_dd_10d_v140_signal": {"func": f50_compounder_index_fin_quality_valuation_index_dd_10d_v140_signal},
    "f50_compounder_index_fin_pb_dd_21d_v141_signal": {"func": f50_compounder_index_fin_pb_dd_21d_v141_signal},
    "f50_compounder_index_fin_netinc_dd_21d_v142_signal": {"func": f50_compounder_index_fin_netinc_dd_21d_v142_signal},
    "f50_compounder_index_fin_equity_dd_21d_v143_signal": {"func": f50_compounder_index_fin_equity_dd_21d_v143_signal},
    "f50_compounder_index_fin_quality_valuation_index_dd_21d_v144_signal": {"func": f50_compounder_index_fin_quality_valuation_index_dd_21d_v144_signal},
    "f50_compounder_index_fin_pb_dd_42d_v145_signal": {"func": f50_compounder_index_fin_pb_dd_42d_v145_signal},
    "f50_compounder_index_fin_netinc_dd_42d_v146_signal": {"func": f50_compounder_index_fin_netinc_dd_42d_v146_signal},
    "f50_compounder_index_fin_equity_dd_42d_v147_signal": {"func": f50_compounder_index_fin_equity_dd_42d_v147_signal},
    "f50_compounder_index_fin_quality_valuation_index_dd_42d_v148_signal": {"func": f50_compounder_index_fin_quality_valuation_index_dd_42d_v148_signal},
    "f50_compounder_index_fin_pb_dd_63d_v149_signal": {"func": f50_compounder_index_fin_pb_dd_63d_v149_signal},
    "f50_compounder_index_fin_netinc_dd_63d_v150_signal": {"func": f50_compounder_index_fin_netinc_dd_63d_v150_signal},
}

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "deferredrev": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "equity": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "deposits": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "divyield": np.random.normal(100, 10, n).cumsum(), "bvps": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "tangibles": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "grossmargin": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "liabilitiesc": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "pb": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum()
    })
    print(f"Verifying {len(REGISTRY)} functions for family 50...")
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
