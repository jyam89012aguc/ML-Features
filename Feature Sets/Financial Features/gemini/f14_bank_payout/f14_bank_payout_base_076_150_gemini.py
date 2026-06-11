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

def f14_bank_payout_cash_payout_safety_ewma_504d_v076_signal(fcf, netinc):
    """Exponential moving average of Cash flow conversion safety over 504d window."""
    res = _ewma(_ratio(fcf, netinc), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_bank_payout_fcf_ewma_756d_v077_signal(fcf):
    """Exponential moving average of Raw level of fcf over 756d window."""
    res = _ewma(fcf, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_bank_payout_netinc_ewma_756d_v078_signal(netinc):
    """Exponential moving average of Raw level of netinc over 756d window."""
    res = _ewma(netinc, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_bank_payout_divyield_ewma_756d_v079_signal(divyield):
    """Exponential moving average of Raw level of divyield over 756d window."""
    res = _ewma(divyield, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_bank_payout_cash_payout_safety_ewma_756d_v080_signal(fcf, netinc):
    """Exponential moving average of Cash flow conversion safety over 756d window."""
    res = _ewma(_ratio(fcf, netinc), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_bank_payout_fcf_ewma_1008d_v081_signal(fcf):
    """Exponential moving average of Raw level of fcf over 1008d window."""
    res = _ewma(fcf, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_bank_payout_netinc_ewma_1008d_v082_signal(netinc):
    """Exponential moving average of Raw level of netinc over 1008d window."""
    res = _ewma(netinc, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_bank_payout_divyield_ewma_1008d_v083_signal(divyield):
    """Exponential moving average of Raw level of divyield over 1008d window."""
    res = _ewma(divyield, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_bank_payout_cash_payout_safety_ewma_1008d_v084_signal(fcf, netinc):
    """Exponential moving average of Cash flow conversion safety over 1008d window."""
    res = _ewma(_ratio(fcf, netinc), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_bank_payout_fcf_ewma_1260d_v085_signal(fcf):
    """Exponential moving average of Raw level of fcf over 1260d window."""
    res = _ewma(fcf, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_bank_payout_netinc_ewma_1260d_v086_signal(netinc):
    """Exponential moving average of Raw level of netinc over 1260d window."""
    res = _ewma(netinc, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_bank_payout_divyield_ewma_1260d_v087_signal(divyield):
    """Exponential moving average of Raw level of divyield over 1260d window."""
    res = _ewma(divyield, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_bank_payout_cash_payout_safety_ewma_1260d_v088_signal(fcf, netinc):
    """Exponential moving average of Cash flow conversion safety over 1260d window."""
    res = _ewma(_ratio(fcf, netinc), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_bank_payout_fcf_z_5d_v089_signal(fcf):
    """Z-score of Raw level of fcf over 5d window."""
    res = _z(fcf, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_bank_payout_netinc_z_5d_v090_signal(netinc):
    """Z-score of Raw level of netinc over 5d window."""
    res = _z(netinc, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_bank_payout_divyield_z_5d_v091_signal(divyield):
    """Z-score of Raw level of divyield over 5d window."""
    res = _z(divyield, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_bank_payout_cash_payout_safety_z_5d_v092_signal(fcf, netinc):
    """Z-score of Cash flow conversion safety over 5d window."""
    res = _z(_ratio(fcf, netinc), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_bank_payout_fcf_z_10d_v093_signal(fcf):
    """Z-score of Raw level of fcf over 10d window."""
    res = _z(fcf, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_bank_payout_netinc_z_10d_v094_signal(netinc):
    """Z-score of Raw level of netinc over 10d window."""
    res = _z(netinc, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_bank_payout_divyield_z_10d_v095_signal(divyield):
    """Z-score of Raw level of divyield over 10d window."""
    res = _z(divyield, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_bank_payout_cash_payout_safety_z_10d_v096_signal(fcf, netinc):
    """Z-score of Cash flow conversion safety over 10d window."""
    res = _z(_ratio(fcf, netinc), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_bank_payout_fcf_z_21d_v097_signal(fcf):
    """Z-score of Raw level of fcf over 21d window."""
    res = _z(fcf, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_bank_payout_netinc_z_21d_v098_signal(netinc):
    """Z-score of Raw level of netinc over 21d window."""
    res = _z(netinc, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_bank_payout_divyield_z_21d_v099_signal(divyield):
    """Z-score of Raw level of divyield over 21d window."""
    res = _z(divyield, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_bank_payout_cash_payout_safety_z_21d_v100_signal(fcf, netinc):
    """Z-score of Cash flow conversion safety over 21d window."""
    res = _z(_ratio(fcf, netinc), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_bank_payout_fcf_z_42d_v101_signal(fcf):
    """Z-score of Raw level of fcf over 42d window."""
    res = _z(fcf, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_bank_payout_netinc_z_42d_v102_signal(netinc):
    """Z-score of Raw level of netinc over 42d window."""
    res = _z(netinc, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_bank_payout_divyield_z_42d_v103_signal(divyield):
    """Z-score of Raw level of divyield over 42d window."""
    res = _z(divyield, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_bank_payout_cash_payout_safety_z_42d_v104_signal(fcf, netinc):
    """Z-score of Cash flow conversion safety over 42d window."""
    res = _z(_ratio(fcf, netinc), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_bank_payout_fcf_z_63d_v105_signal(fcf):
    """Z-score of Raw level of fcf over 63d window."""
    res = _z(fcf, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_bank_payout_netinc_z_63d_v106_signal(netinc):
    """Z-score of Raw level of netinc over 63d window."""
    res = _z(netinc, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_bank_payout_divyield_z_63d_v107_signal(divyield):
    """Z-score of Raw level of divyield over 63d window."""
    res = _z(divyield, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_bank_payout_cash_payout_safety_z_63d_v108_signal(fcf, netinc):
    """Z-score of Cash flow conversion safety over 63d window."""
    res = _z(_ratio(fcf, netinc), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_bank_payout_fcf_z_126d_v109_signal(fcf):
    """Z-score of Raw level of fcf over 126d window."""
    res = _z(fcf, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_bank_payout_netinc_z_126d_v110_signal(netinc):
    """Z-score of Raw level of netinc over 126d window."""
    res = _z(netinc, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_bank_payout_divyield_z_126d_v111_signal(divyield):
    """Z-score of Raw level of divyield over 126d window."""
    res = _z(divyield, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_bank_payout_cash_payout_safety_z_126d_v112_signal(fcf, netinc):
    """Z-score of Cash flow conversion safety over 126d window."""
    res = _z(_ratio(fcf, netinc), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_bank_payout_fcf_z_252d_v113_signal(fcf):
    """Z-score of Raw level of fcf over 252d window."""
    res = _z(fcf, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_bank_payout_netinc_z_252d_v114_signal(netinc):
    """Z-score of Raw level of netinc over 252d window."""
    res = _z(netinc, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_bank_payout_divyield_z_252d_v115_signal(divyield):
    """Z-score of Raw level of divyield over 252d window."""
    res = _z(divyield, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_bank_payout_cash_payout_safety_z_252d_v116_signal(fcf, netinc):
    """Z-score of Cash flow conversion safety over 252d window."""
    res = _z(_ratio(fcf, netinc), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_bank_payout_fcf_z_504d_v117_signal(fcf):
    """Z-score of Raw level of fcf over 504d window."""
    res = _z(fcf, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_bank_payout_netinc_z_504d_v118_signal(netinc):
    """Z-score of Raw level of netinc over 504d window."""
    res = _z(netinc, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_bank_payout_divyield_z_504d_v119_signal(divyield):
    """Z-score of Raw level of divyield over 504d window."""
    res = _z(divyield, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_bank_payout_cash_payout_safety_z_504d_v120_signal(fcf, netinc):
    """Z-score of Cash flow conversion safety over 504d window."""
    res = _z(_ratio(fcf, netinc), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_bank_payout_fcf_z_756d_v121_signal(fcf):
    """Z-score of Raw level of fcf over 756d window."""
    res = _z(fcf, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_bank_payout_netinc_z_756d_v122_signal(netinc):
    """Z-score of Raw level of netinc over 756d window."""
    res = _z(netinc, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_bank_payout_divyield_z_756d_v123_signal(divyield):
    """Z-score of Raw level of divyield over 756d window."""
    res = _z(divyield, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_bank_payout_cash_payout_safety_z_756d_v124_signal(fcf, netinc):
    """Z-score of Cash flow conversion safety over 756d window."""
    res = _z(_ratio(fcf, netinc), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_bank_payout_fcf_z_1008d_v125_signal(fcf):
    """Z-score of Raw level of fcf over 1008d window."""
    res = _z(fcf, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_bank_payout_netinc_z_1008d_v126_signal(netinc):
    """Z-score of Raw level of netinc over 1008d window."""
    res = _z(netinc, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_bank_payout_divyield_z_1008d_v127_signal(divyield):
    """Z-score of Raw level of divyield over 1008d window."""
    res = _z(divyield, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_bank_payout_cash_payout_safety_z_1008d_v128_signal(fcf, netinc):
    """Z-score of Cash flow conversion safety over 1008d window."""
    res = _z(_ratio(fcf, netinc), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_bank_payout_fcf_z_1260d_v129_signal(fcf):
    """Z-score of Raw level of fcf over 1260d window."""
    res = _z(fcf, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_bank_payout_netinc_z_1260d_v130_signal(netinc):
    """Z-score of Raw level of netinc over 1260d window."""
    res = _z(netinc, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_bank_payout_divyield_z_1260d_v131_signal(divyield):
    """Z-score of Raw level of divyield over 1260d window."""
    res = _z(divyield, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_bank_payout_cash_payout_safety_z_1260d_v132_signal(fcf, netinc):
    """Z-score of Cash flow conversion safety over 1260d window."""
    res = _z(_ratio(fcf, netinc), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_bank_payout_fcf_dd_5d_v133_signal(fcf):
    """Drawdown of Raw level of fcf over 5d window."""
    res = _drawdown(fcf, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_bank_payout_netinc_dd_5d_v134_signal(netinc):
    """Drawdown of Raw level of netinc over 5d window."""
    res = _drawdown(netinc, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_bank_payout_divyield_dd_5d_v135_signal(divyield):
    """Drawdown of Raw level of divyield over 5d window."""
    res = _drawdown(divyield, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_bank_payout_cash_payout_safety_dd_5d_v136_signal(fcf, netinc):
    """Drawdown of Cash flow conversion safety over 5d window."""
    res = _drawdown(_ratio(fcf, netinc), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_bank_payout_fcf_dd_10d_v137_signal(fcf):
    """Drawdown of Raw level of fcf over 10d window."""
    res = _drawdown(fcf, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_bank_payout_netinc_dd_10d_v138_signal(netinc):
    """Drawdown of Raw level of netinc over 10d window."""
    res = _drawdown(netinc, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_bank_payout_divyield_dd_10d_v139_signal(divyield):
    """Drawdown of Raw level of divyield over 10d window."""
    res = _drawdown(divyield, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_bank_payout_cash_payout_safety_dd_10d_v140_signal(fcf, netinc):
    """Drawdown of Cash flow conversion safety over 10d window."""
    res = _drawdown(_ratio(fcf, netinc), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_bank_payout_fcf_dd_21d_v141_signal(fcf):
    """Drawdown of Raw level of fcf over 21d window."""
    res = _drawdown(fcf, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_bank_payout_netinc_dd_21d_v142_signal(netinc):
    """Drawdown of Raw level of netinc over 21d window."""
    res = _drawdown(netinc, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_bank_payout_divyield_dd_21d_v143_signal(divyield):
    """Drawdown of Raw level of divyield over 21d window."""
    res = _drawdown(divyield, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_bank_payout_cash_payout_safety_dd_21d_v144_signal(fcf, netinc):
    """Drawdown of Cash flow conversion safety over 21d window."""
    res = _drawdown(_ratio(fcf, netinc), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_bank_payout_fcf_dd_42d_v145_signal(fcf):
    """Drawdown of Raw level of fcf over 42d window."""
    res = _drawdown(fcf, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_bank_payout_netinc_dd_42d_v146_signal(netinc):
    """Drawdown of Raw level of netinc over 42d window."""
    res = _drawdown(netinc, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_bank_payout_divyield_dd_42d_v147_signal(divyield):
    """Drawdown of Raw level of divyield over 42d window."""
    res = _drawdown(divyield, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_bank_payout_cash_payout_safety_dd_42d_v148_signal(fcf, netinc):
    """Drawdown of Cash flow conversion safety over 42d window."""
    res = _drawdown(_ratio(fcf, netinc), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_bank_payout_fcf_dd_63d_v149_signal(fcf):
    """Drawdown of Raw level of fcf over 63d window."""
    res = _drawdown(fcf, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f14_bank_payout_netinc_dd_63d_v150_signal(netinc):
    """Drawdown of Raw level of netinc over 63d window."""
    res = _drawdown(netinc, 63)
    return res.replace([np.inf, -np.inf], np.nan)


# ===== Feature Registry =====
REGISTRY = {
    "f14_bank_payout_cash_payout_safety_ewma_504d_v076_signal": {"func": f14_bank_payout_cash_payout_safety_ewma_504d_v076_signal},
    "f14_bank_payout_fcf_ewma_756d_v077_signal": {"func": f14_bank_payout_fcf_ewma_756d_v077_signal},
    "f14_bank_payout_netinc_ewma_756d_v078_signal": {"func": f14_bank_payout_netinc_ewma_756d_v078_signal},
    "f14_bank_payout_divyield_ewma_756d_v079_signal": {"func": f14_bank_payout_divyield_ewma_756d_v079_signal},
    "f14_bank_payout_cash_payout_safety_ewma_756d_v080_signal": {"func": f14_bank_payout_cash_payout_safety_ewma_756d_v080_signal},
    "f14_bank_payout_fcf_ewma_1008d_v081_signal": {"func": f14_bank_payout_fcf_ewma_1008d_v081_signal},
    "f14_bank_payout_netinc_ewma_1008d_v082_signal": {"func": f14_bank_payout_netinc_ewma_1008d_v082_signal},
    "f14_bank_payout_divyield_ewma_1008d_v083_signal": {"func": f14_bank_payout_divyield_ewma_1008d_v083_signal},
    "f14_bank_payout_cash_payout_safety_ewma_1008d_v084_signal": {"func": f14_bank_payout_cash_payout_safety_ewma_1008d_v084_signal},
    "f14_bank_payout_fcf_ewma_1260d_v085_signal": {"func": f14_bank_payout_fcf_ewma_1260d_v085_signal},
    "f14_bank_payout_netinc_ewma_1260d_v086_signal": {"func": f14_bank_payout_netinc_ewma_1260d_v086_signal},
    "f14_bank_payout_divyield_ewma_1260d_v087_signal": {"func": f14_bank_payout_divyield_ewma_1260d_v087_signal},
    "f14_bank_payout_cash_payout_safety_ewma_1260d_v088_signal": {"func": f14_bank_payout_cash_payout_safety_ewma_1260d_v088_signal},
    "f14_bank_payout_fcf_z_5d_v089_signal": {"func": f14_bank_payout_fcf_z_5d_v089_signal},
    "f14_bank_payout_netinc_z_5d_v090_signal": {"func": f14_bank_payout_netinc_z_5d_v090_signal},
    "f14_bank_payout_divyield_z_5d_v091_signal": {"func": f14_bank_payout_divyield_z_5d_v091_signal},
    "f14_bank_payout_cash_payout_safety_z_5d_v092_signal": {"func": f14_bank_payout_cash_payout_safety_z_5d_v092_signal},
    "f14_bank_payout_fcf_z_10d_v093_signal": {"func": f14_bank_payout_fcf_z_10d_v093_signal},
    "f14_bank_payout_netinc_z_10d_v094_signal": {"func": f14_bank_payout_netinc_z_10d_v094_signal},
    "f14_bank_payout_divyield_z_10d_v095_signal": {"func": f14_bank_payout_divyield_z_10d_v095_signal},
    "f14_bank_payout_cash_payout_safety_z_10d_v096_signal": {"func": f14_bank_payout_cash_payout_safety_z_10d_v096_signal},
    "f14_bank_payout_fcf_z_21d_v097_signal": {"func": f14_bank_payout_fcf_z_21d_v097_signal},
    "f14_bank_payout_netinc_z_21d_v098_signal": {"func": f14_bank_payout_netinc_z_21d_v098_signal},
    "f14_bank_payout_divyield_z_21d_v099_signal": {"func": f14_bank_payout_divyield_z_21d_v099_signal},
    "f14_bank_payout_cash_payout_safety_z_21d_v100_signal": {"func": f14_bank_payout_cash_payout_safety_z_21d_v100_signal},
    "f14_bank_payout_fcf_z_42d_v101_signal": {"func": f14_bank_payout_fcf_z_42d_v101_signal},
    "f14_bank_payout_netinc_z_42d_v102_signal": {"func": f14_bank_payout_netinc_z_42d_v102_signal},
    "f14_bank_payout_divyield_z_42d_v103_signal": {"func": f14_bank_payout_divyield_z_42d_v103_signal},
    "f14_bank_payout_cash_payout_safety_z_42d_v104_signal": {"func": f14_bank_payout_cash_payout_safety_z_42d_v104_signal},
    "f14_bank_payout_fcf_z_63d_v105_signal": {"func": f14_bank_payout_fcf_z_63d_v105_signal},
    "f14_bank_payout_netinc_z_63d_v106_signal": {"func": f14_bank_payout_netinc_z_63d_v106_signal},
    "f14_bank_payout_divyield_z_63d_v107_signal": {"func": f14_bank_payout_divyield_z_63d_v107_signal},
    "f14_bank_payout_cash_payout_safety_z_63d_v108_signal": {"func": f14_bank_payout_cash_payout_safety_z_63d_v108_signal},
    "f14_bank_payout_fcf_z_126d_v109_signal": {"func": f14_bank_payout_fcf_z_126d_v109_signal},
    "f14_bank_payout_netinc_z_126d_v110_signal": {"func": f14_bank_payout_netinc_z_126d_v110_signal},
    "f14_bank_payout_divyield_z_126d_v111_signal": {"func": f14_bank_payout_divyield_z_126d_v111_signal},
    "f14_bank_payout_cash_payout_safety_z_126d_v112_signal": {"func": f14_bank_payout_cash_payout_safety_z_126d_v112_signal},
    "f14_bank_payout_fcf_z_252d_v113_signal": {"func": f14_bank_payout_fcf_z_252d_v113_signal},
    "f14_bank_payout_netinc_z_252d_v114_signal": {"func": f14_bank_payout_netinc_z_252d_v114_signal},
    "f14_bank_payout_divyield_z_252d_v115_signal": {"func": f14_bank_payout_divyield_z_252d_v115_signal},
    "f14_bank_payout_cash_payout_safety_z_252d_v116_signal": {"func": f14_bank_payout_cash_payout_safety_z_252d_v116_signal},
    "f14_bank_payout_fcf_z_504d_v117_signal": {"func": f14_bank_payout_fcf_z_504d_v117_signal},
    "f14_bank_payout_netinc_z_504d_v118_signal": {"func": f14_bank_payout_netinc_z_504d_v118_signal},
    "f14_bank_payout_divyield_z_504d_v119_signal": {"func": f14_bank_payout_divyield_z_504d_v119_signal},
    "f14_bank_payout_cash_payout_safety_z_504d_v120_signal": {"func": f14_bank_payout_cash_payout_safety_z_504d_v120_signal},
    "f14_bank_payout_fcf_z_756d_v121_signal": {"func": f14_bank_payout_fcf_z_756d_v121_signal},
    "f14_bank_payout_netinc_z_756d_v122_signal": {"func": f14_bank_payout_netinc_z_756d_v122_signal},
    "f14_bank_payout_divyield_z_756d_v123_signal": {"func": f14_bank_payout_divyield_z_756d_v123_signal},
    "f14_bank_payout_cash_payout_safety_z_756d_v124_signal": {"func": f14_bank_payout_cash_payout_safety_z_756d_v124_signal},
    "f14_bank_payout_fcf_z_1008d_v125_signal": {"func": f14_bank_payout_fcf_z_1008d_v125_signal},
    "f14_bank_payout_netinc_z_1008d_v126_signal": {"func": f14_bank_payout_netinc_z_1008d_v126_signal},
    "f14_bank_payout_divyield_z_1008d_v127_signal": {"func": f14_bank_payout_divyield_z_1008d_v127_signal},
    "f14_bank_payout_cash_payout_safety_z_1008d_v128_signal": {"func": f14_bank_payout_cash_payout_safety_z_1008d_v128_signal},
    "f14_bank_payout_fcf_z_1260d_v129_signal": {"func": f14_bank_payout_fcf_z_1260d_v129_signal},
    "f14_bank_payout_netinc_z_1260d_v130_signal": {"func": f14_bank_payout_netinc_z_1260d_v130_signal},
    "f14_bank_payout_divyield_z_1260d_v131_signal": {"func": f14_bank_payout_divyield_z_1260d_v131_signal},
    "f14_bank_payout_cash_payout_safety_z_1260d_v132_signal": {"func": f14_bank_payout_cash_payout_safety_z_1260d_v132_signal},
    "f14_bank_payout_fcf_dd_5d_v133_signal": {"func": f14_bank_payout_fcf_dd_5d_v133_signal},
    "f14_bank_payout_netinc_dd_5d_v134_signal": {"func": f14_bank_payout_netinc_dd_5d_v134_signal},
    "f14_bank_payout_divyield_dd_5d_v135_signal": {"func": f14_bank_payout_divyield_dd_5d_v135_signal},
    "f14_bank_payout_cash_payout_safety_dd_5d_v136_signal": {"func": f14_bank_payout_cash_payout_safety_dd_5d_v136_signal},
    "f14_bank_payout_fcf_dd_10d_v137_signal": {"func": f14_bank_payout_fcf_dd_10d_v137_signal},
    "f14_bank_payout_netinc_dd_10d_v138_signal": {"func": f14_bank_payout_netinc_dd_10d_v138_signal},
    "f14_bank_payout_divyield_dd_10d_v139_signal": {"func": f14_bank_payout_divyield_dd_10d_v139_signal},
    "f14_bank_payout_cash_payout_safety_dd_10d_v140_signal": {"func": f14_bank_payout_cash_payout_safety_dd_10d_v140_signal},
    "f14_bank_payout_fcf_dd_21d_v141_signal": {"func": f14_bank_payout_fcf_dd_21d_v141_signal},
    "f14_bank_payout_netinc_dd_21d_v142_signal": {"func": f14_bank_payout_netinc_dd_21d_v142_signal},
    "f14_bank_payout_divyield_dd_21d_v143_signal": {"func": f14_bank_payout_divyield_dd_21d_v143_signal},
    "f14_bank_payout_cash_payout_safety_dd_21d_v144_signal": {"func": f14_bank_payout_cash_payout_safety_dd_21d_v144_signal},
    "f14_bank_payout_fcf_dd_42d_v145_signal": {"func": f14_bank_payout_fcf_dd_42d_v145_signal},
    "f14_bank_payout_netinc_dd_42d_v146_signal": {"func": f14_bank_payout_netinc_dd_42d_v146_signal},
    "f14_bank_payout_divyield_dd_42d_v147_signal": {"func": f14_bank_payout_divyield_dd_42d_v147_signal},
    "f14_bank_payout_cash_payout_safety_dd_42d_v148_signal": {"func": f14_bank_payout_cash_payout_safety_dd_42d_v148_signal},
    "f14_bank_payout_fcf_dd_63d_v149_signal": {"func": f14_bank_payout_fcf_dd_63d_v149_signal},
    "f14_bank_payout_netinc_dd_63d_v150_signal": {"func": f14_bank_payout_netinc_dd_63d_v150_signal},
}

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "deferredrev": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "equity": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "deposits": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "divyield": np.random.normal(100, 10, n).cumsum(), "bvps": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "tangibles": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "grossmargin": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "liabilitiesc": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum()
    })
    print(f"Verifying {len(REGISTRY)} functions for family 14...")
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
