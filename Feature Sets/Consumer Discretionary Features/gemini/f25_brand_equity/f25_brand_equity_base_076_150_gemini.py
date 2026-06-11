import pandas as pd
import numpy as np
import inspect

# ===== High-Performance Alpha Helpers =====
def _sma(s, w): return s.rolling(w, min_periods=min(w, 20) if w > 20 else min(w, 2)).mean()
def _std(s, w): return s.rolling(w, min_periods=min(w, 20) if w > 20 else min(w, 2)).std()
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

def f25_brand_equity_equity_moat_z_504d_v076_signal(grossmargin, pe):
    """Z-score for relative outlier detection of Brand margin amplified by market valuation multiples over 504d window."""
    res = _z(grossmargin * pe, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_grossmargin_z_756d_v077_signal(grossmargin):
    """Z-score for relative outlier detection of Raw level of grossmargin over 756d window."""
    res = _z(grossmargin, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_pe_z_756d_v078_signal(pe):
    """Z-score for relative outlier detection of Raw level of pe over 756d window."""
    res = _z(pe, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_pb_z_756d_v079_signal(pb):
    """Z-score for relative outlier detection of Raw level of pb over 756d window."""
    res = _z(pb, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_equity_moat_z_756d_v080_signal(grossmargin, pe):
    """Z-score for relative outlier detection of Brand margin amplified by market valuation multiples over 756d window."""
    res = _z(grossmargin * pe, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_grossmargin_z_1008d_v081_signal(grossmargin):
    """Z-score for relative outlier detection of Raw level of grossmargin over 1008d window."""
    res = _z(grossmargin, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_pe_z_1008d_v082_signal(pe):
    """Z-score for relative outlier detection of Raw level of pe over 1008d window."""
    res = _z(pe, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_pb_z_1008d_v083_signal(pb):
    """Z-score for relative outlier detection of Raw level of pb over 1008d window."""
    res = _z(pb, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_equity_moat_z_1008d_v084_signal(grossmargin, pe):
    """Z-score for relative outlier detection of Brand margin amplified by market valuation multiples over 1008d window."""
    res = _z(grossmargin * pe, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_grossmargin_z_1260d_v085_signal(grossmargin):
    """Z-score for relative outlier detection of Raw level of grossmargin over 1260d window."""
    res = _z(grossmargin, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_pe_z_1260d_v086_signal(pe):
    """Z-score for relative outlier detection of Raw level of pe over 1260d window."""
    res = _z(pe, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_pb_z_1260d_v087_signal(pb):
    """Z-score for relative outlier detection of Raw level of pb over 1260d window."""
    res = _z(pb, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_equity_moat_z_1260d_v088_signal(grossmargin, pe):
    """Z-score for relative outlier detection of Brand margin amplified by market valuation multiples over 1260d window."""
    res = _z(grossmargin * pe, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_grossmargin_dd_5d_v089_signal(grossmargin):
    """Drawdown from peak to identify cycle troughs of Raw level of grossmargin over 5d window."""
    res = _drawdown(grossmargin, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_pe_dd_5d_v090_signal(pe):
    """Drawdown from peak to identify cycle troughs of Raw level of pe over 5d window."""
    res = _drawdown(pe, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_pb_dd_5d_v091_signal(pb):
    """Drawdown from peak to identify cycle troughs of Raw level of pb over 5d window."""
    res = _drawdown(pb, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_equity_moat_dd_5d_v092_signal(grossmargin, pe):
    """Drawdown from peak to identify cycle troughs of Brand margin amplified by market valuation multiples over 5d window."""
    res = _drawdown(grossmargin * pe, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_grossmargin_dd_10d_v093_signal(grossmargin):
    """Drawdown from peak to identify cycle troughs of Raw level of grossmargin over 10d window."""
    res = _drawdown(grossmargin, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_pe_dd_10d_v094_signal(pe):
    """Drawdown from peak to identify cycle troughs of Raw level of pe over 10d window."""
    res = _drawdown(pe, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_pb_dd_10d_v095_signal(pb):
    """Drawdown from peak to identify cycle troughs of Raw level of pb over 10d window."""
    res = _drawdown(pb, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_equity_moat_dd_10d_v096_signal(grossmargin, pe):
    """Drawdown from peak to identify cycle troughs of Brand margin amplified by market valuation multiples over 10d window."""
    res = _drawdown(grossmargin * pe, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_grossmargin_dd_21d_v097_signal(grossmargin):
    """Drawdown from peak to identify cycle troughs of Raw level of grossmargin over 21d window."""
    res = _drawdown(grossmargin, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_pe_dd_21d_v098_signal(pe):
    """Drawdown from peak to identify cycle troughs of Raw level of pe over 21d window."""
    res = _drawdown(pe, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_pb_dd_21d_v099_signal(pb):
    """Drawdown from peak to identify cycle troughs of Raw level of pb over 21d window."""
    res = _drawdown(pb, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_equity_moat_dd_21d_v100_signal(grossmargin, pe):
    """Drawdown from peak to identify cycle troughs of Brand margin amplified by market valuation multiples over 21d window."""
    res = _drawdown(grossmargin * pe, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_grossmargin_dd_42d_v101_signal(grossmargin):
    """Drawdown from peak to identify cycle troughs of Raw level of grossmargin over 42d window."""
    res = _drawdown(grossmargin, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_pe_dd_42d_v102_signal(pe):
    """Drawdown from peak to identify cycle troughs of Raw level of pe over 42d window."""
    res = _drawdown(pe, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_pb_dd_42d_v103_signal(pb):
    """Drawdown from peak to identify cycle troughs of Raw level of pb over 42d window."""
    res = _drawdown(pb, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_equity_moat_dd_42d_v104_signal(grossmargin, pe):
    """Drawdown from peak to identify cycle troughs of Brand margin amplified by market valuation multiples over 42d window."""
    res = _drawdown(grossmargin * pe, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_grossmargin_dd_63d_v105_signal(grossmargin):
    """Drawdown from peak to identify cycle troughs of Raw level of grossmargin over 63d window."""
    res = _drawdown(grossmargin, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_pe_dd_63d_v106_signal(pe):
    """Drawdown from peak to identify cycle troughs of Raw level of pe over 63d window."""
    res = _drawdown(pe, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_pb_dd_63d_v107_signal(pb):
    """Drawdown from peak to identify cycle troughs of Raw level of pb over 63d window."""
    res = _drawdown(pb, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_equity_moat_dd_63d_v108_signal(grossmargin, pe):
    """Drawdown from peak to identify cycle troughs of Brand margin amplified by market valuation multiples over 63d window."""
    res = _drawdown(grossmargin * pe, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_grossmargin_dd_126d_v109_signal(grossmargin):
    """Drawdown from peak to identify cycle troughs of Raw level of grossmargin over 126d window."""
    res = _drawdown(grossmargin, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_pe_dd_126d_v110_signal(pe):
    """Drawdown from peak to identify cycle troughs of Raw level of pe over 126d window."""
    res = _drawdown(pe, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_pb_dd_126d_v111_signal(pb):
    """Drawdown from peak to identify cycle troughs of Raw level of pb over 126d window."""
    res = _drawdown(pb, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_equity_moat_dd_126d_v112_signal(grossmargin, pe):
    """Drawdown from peak to identify cycle troughs of Brand margin amplified by market valuation multiples over 126d window."""
    res = _drawdown(grossmargin * pe, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_grossmargin_dd_252d_v113_signal(grossmargin):
    """Drawdown from peak to identify cycle troughs of Raw level of grossmargin over 252d window."""
    res = _drawdown(grossmargin, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_pe_dd_252d_v114_signal(pe):
    """Drawdown from peak to identify cycle troughs of Raw level of pe over 252d window."""
    res = _drawdown(pe, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_pb_dd_252d_v115_signal(pb):
    """Drawdown from peak to identify cycle troughs of Raw level of pb over 252d window."""
    res = _drawdown(pb, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_equity_moat_dd_252d_v116_signal(grossmargin, pe):
    """Drawdown from peak to identify cycle troughs of Brand margin amplified by market valuation multiples over 252d window."""
    res = _drawdown(grossmargin * pe, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_grossmargin_dd_504d_v117_signal(grossmargin):
    """Drawdown from peak to identify cycle troughs of Raw level of grossmargin over 504d window."""
    res = _drawdown(grossmargin, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_pe_dd_504d_v118_signal(pe):
    """Drawdown from peak to identify cycle troughs of Raw level of pe over 504d window."""
    res = _drawdown(pe, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_pb_dd_504d_v119_signal(pb):
    """Drawdown from peak to identify cycle troughs of Raw level of pb over 504d window."""
    res = _drawdown(pb, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_equity_moat_dd_504d_v120_signal(grossmargin, pe):
    """Drawdown from peak to identify cycle troughs of Brand margin amplified by market valuation multiples over 504d window."""
    res = _drawdown(grossmargin * pe, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_grossmargin_dd_756d_v121_signal(grossmargin):
    """Drawdown from peak to identify cycle troughs of Raw level of grossmargin over 756d window."""
    res = _drawdown(grossmargin, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_pe_dd_756d_v122_signal(pe):
    """Drawdown from peak to identify cycle troughs of Raw level of pe over 756d window."""
    res = _drawdown(pe, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_pb_dd_756d_v123_signal(pb):
    """Drawdown from peak to identify cycle troughs of Raw level of pb over 756d window."""
    res = _drawdown(pb, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_equity_moat_dd_756d_v124_signal(grossmargin, pe):
    """Drawdown from peak to identify cycle troughs of Brand margin amplified by market valuation multiples over 756d window."""
    res = _drawdown(grossmargin * pe, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_grossmargin_dd_1008d_v125_signal(grossmargin):
    """Drawdown from peak to identify cycle troughs of Raw level of grossmargin over 1008d window."""
    res = _drawdown(grossmargin, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_pe_dd_1008d_v126_signal(pe):
    """Drawdown from peak to identify cycle troughs of Raw level of pe over 1008d window."""
    res = _drawdown(pe, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_pb_dd_1008d_v127_signal(pb):
    """Drawdown from peak to identify cycle troughs of Raw level of pb over 1008d window."""
    res = _drawdown(pb, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_equity_moat_dd_1008d_v128_signal(grossmargin, pe):
    """Drawdown from peak to identify cycle troughs of Brand margin amplified by market valuation multiples over 1008d window."""
    res = _drawdown(grossmargin * pe, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_grossmargin_dd_1260d_v129_signal(grossmargin):
    """Drawdown from peak to identify cycle troughs of Raw level of grossmargin over 1260d window."""
    res = _drawdown(grossmargin, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_pe_dd_1260d_v130_signal(pe):
    """Drawdown from peak to identify cycle troughs of Raw level of pe over 1260d window."""
    res = _drawdown(pe, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_pb_dd_1260d_v131_signal(pb):
    """Drawdown from peak to identify cycle troughs of Raw level of pb over 1260d window."""
    res = _drawdown(pb, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_equity_moat_dd_1260d_v132_signal(grossmargin, pe):
    """Drawdown from peak to identify cycle troughs of Brand margin amplified by market valuation multiples over 1260d window."""
    res = _drawdown(grossmargin * pe, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_grossmargin_rec_5d_v133_signal(grossmargin):
    """Recovery from trough for turnaround signals of Raw level of grossmargin over 5d window."""
    res = _recovery(grossmargin, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_pe_rec_5d_v134_signal(pe):
    """Recovery from trough for turnaround signals of Raw level of pe over 5d window."""
    res = _recovery(pe, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_pb_rec_5d_v135_signal(pb):
    """Recovery from trough for turnaround signals of Raw level of pb over 5d window."""
    res = _recovery(pb, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_equity_moat_rec_5d_v136_signal(grossmargin, pe):
    """Recovery from trough for turnaround signals of Brand margin amplified by market valuation multiples over 5d window."""
    res = _recovery(grossmargin * pe, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_grossmargin_rec_10d_v137_signal(grossmargin):
    """Recovery from trough for turnaround signals of Raw level of grossmargin over 10d window."""
    res = _recovery(grossmargin, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_pe_rec_10d_v138_signal(pe):
    """Recovery from trough for turnaround signals of Raw level of pe over 10d window."""
    res = _recovery(pe, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_pb_rec_10d_v139_signal(pb):
    """Recovery from trough for turnaround signals of Raw level of pb over 10d window."""
    res = _recovery(pb, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_equity_moat_rec_10d_v140_signal(grossmargin, pe):
    """Recovery from trough for turnaround signals of Brand margin amplified by market valuation multiples over 10d window."""
    res = _recovery(grossmargin * pe, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_grossmargin_rec_21d_v141_signal(grossmargin):
    """Recovery from trough for turnaround signals of Raw level of grossmargin over 21d window."""
    res = _recovery(grossmargin, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_pe_rec_21d_v142_signal(pe):
    """Recovery from trough for turnaround signals of Raw level of pe over 21d window."""
    res = _recovery(pe, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_pb_rec_21d_v143_signal(pb):
    """Recovery from trough for turnaround signals of Raw level of pb over 21d window."""
    res = _recovery(pb, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_equity_moat_rec_21d_v144_signal(grossmargin, pe):
    """Recovery from trough for turnaround signals of Brand margin amplified by market valuation multiples over 21d window."""
    res = _recovery(grossmargin * pe, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_grossmargin_rec_42d_v145_signal(grossmargin):
    """Recovery from trough for turnaround signals of Raw level of grossmargin over 42d window."""
    res = _recovery(grossmargin, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_pe_rec_42d_v146_signal(pe):
    """Recovery from trough for turnaround signals of Raw level of pe over 42d window."""
    res = _recovery(pe, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_pb_rec_42d_v147_signal(pb):
    """Recovery from trough for turnaround signals of Raw level of pb over 42d window."""
    res = _recovery(pb, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_equity_moat_rec_42d_v148_signal(grossmargin, pe):
    """Recovery from trough for turnaround signals of Brand margin amplified by market valuation multiples over 42d window."""
    res = _recovery(grossmargin * pe, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_grossmargin_rec_63d_v149_signal(grossmargin):
    """Recovery from trough for turnaround signals of Raw level of grossmargin over 63d window."""
    res = _recovery(grossmargin, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f25_brand_equity_pe_rec_63d_v150_signal(pe):
    """Recovery from trough for turnaround signals of Raw level of pe over 63d window."""
    res = _recovery(pe, 63)
    return res.replace([np.inf, -np.inf], np.nan)


# ===== Feature Registry =====
REGISTRY = {
    "f25_brand_equity_equity_moat_z_504d_v076_signal": {"inputs": [], "func": f25_brand_equity_equity_moat_z_504d_v076_signal},    "f25_brand_equity_grossmargin_z_756d_v077_signal": {"inputs": [], "func": f25_brand_equity_grossmargin_z_756d_v077_signal},    "f25_brand_equity_pe_z_756d_v078_signal": {"inputs": [], "func": f25_brand_equity_pe_z_756d_v078_signal},    "f25_brand_equity_pb_z_756d_v079_signal": {"inputs": [], "func": f25_brand_equity_pb_z_756d_v079_signal},    "f25_brand_equity_equity_moat_z_756d_v080_signal": {"inputs": [], "func": f25_brand_equity_equity_moat_z_756d_v080_signal},    "f25_brand_equity_grossmargin_z_1008d_v081_signal": {"inputs": [], "func": f25_brand_equity_grossmargin_z_1008d_v081_signal},    "f25_brand_equity_pe_z_1008d_v082_signal": {"inputs": [], "func": f25_brand_equity_pe_z_1008d_v082_signal},    "f25_brand_equity_pb_z_1008d_v083_signal": {"inputs": [], "func": f25_brand_equity_pb_z_1008d_v083_signal},    "f25_brand_equity_equity_moat_z_1008d_v084_signal": {"inputs": [], "func": f25_brand_equity_equity_moat_z_1008d_v084_signal},    "f25_brand_equity_grossmargin_z_1260d_v085_signal": {"inputs": [], "func": f25_brand_equity_grossmargin_z_1260d_v085_signal},    "f25_brand_equity_pe_z_1260d_v086_signal": {"inputs": [], "func": f25_brand_equity_pe_z_1260d_v086_signal},    "f25_brand_equity_pb_z_1260d_v087_signal": {"inputs": [], "func": f25_brand_equity_pb_z_1260d_v087_signal},    "f25_brand_equity_equity_moat_z_1260d_v088_signal": {"inputs": [], "func": f25_brand_equity_equity_moat_z_1260d_v088_signal},    "f25_brand_equity_grossmargin_dd_5d_v089_signal": {"inputs": [], "func": f25_brand_equity_grossmargin_dd_5d_v089_signal},    "f25_brand_equity_pe_dd_5d_v090_signal": {"inputs": [], "func": f25_brand_equity_pe_dd_5d_v090_signal},    "f25_brand_equity_pb_dd_5d_v091_signal": {"inputs": [], "func": f25_brand_equity_pb_dd_5d_v091_signal},    "f25_brand_equity_equity_moat_dd_5d_v092_signal": {"inputs": [], "func": f25_brand_equity_equity_moat_dd_5d_v092_signal},    "f25_brand_equity_grossmargin_dd_10d_v093_signal": {"inputs": [], "func": f25_brand_equity_grossmargin_dd_10d_v093_signal},    "f25_brand_equity_pe_dd_10d_v094_signal": {"inputs": [], "func": f25_brand_equity_pe_dd_10d_v094_signal},    "f25_brand_equity_pb_dd_10d_v095_signal": {"inputs": [], "func": f25_brand_equity_pb_dd_10d_v095_signal},    "f25_brand_equity_equity_moat_dd_10d_v096_signal": {"inputs": [], "func": f25_brand_equity_equity_moat_dd_10d_v096_signal},    "f25_brand_equity_grossmargin_dd_21d_v097_signal": {"inputs": [], "func": f25_brand_equity_grossmargin_dd_21d_v097_signal},    "f25_brand_equity_pe_dd_21d_v098_signal": {"inputs": [], "func": f25_brand_equity_pe_dd_21d_v098_signal},    "f25_brand_equity_pb_dd_21d_v099_signal": {"inputs": [], "func": f25_brand_equity_pb_dd_21d_v099_signal},    "f25_brand_equity_equity_moat_dd_21d_v100_signal": {"inputs": [], "func": f25_brand_equity_equity_moat_dd_21d_v100_signal},    "f25_brand_equity_grossmargin_dd_42d_v101_signal": {"inputs": [], "func": f25_brand_equity_grossmargin_dd_42d_v101_signal},    "f25_brand_equity_pe_dd_42d_v102_signal": {"inputs": [], "func": f25_brand_equity_pe_dd_42d_v102_signal},    "f25_brand_equity_pb_dd_42d_v103_signal": {"inputs": [], "func": f25_brand_equity_pb_dd_42d_v103_signal},    "f25_brand_equity_equity_moat_dd_42d_v104_signal": {"inputs": [], "func": f25_brand_equity_equity_moat_dd_42d_v104_signal},    "f25_brand_equity_grossmargin_dd_63d_v105_signal": {"inputs": [], "func": f25_brand_equity_grossmargin_dd_63d_v105_signal},    "f25_brand_equity_pe_dd_63d_v106_signal": {"inputs": [], "func": f25_brand_equity_pe_dd_63d_v106_signal},    "f25_brand_equity_pb_dd_63d_v107_signal": {"inputs": [], "func": f25_brand_equity_pb_dd_63d_v107_signal},    "f25_brand_equity_equity_moat_dd_63d_v108_signal": {"inputs": [], "func": f25_brand_equity_equity_moat_dd_63d_v108_signal},    "f25_brand_equity_grossmargin_dd_126d_v109_signal": {"inputs": [], "func": f25_brand_equity_grossmargin_dd_126d_v109_signal},    "f25_brand_equity_pe_dd_126d_v110_signal": {"inputs": [], "func": f25_brand_equity_pe_dd_126d_v110_signal},    "f25_brand_equity_pb_dd_126d_v111_signal": {"inputs": [], "func": f25_brand_equity_pb_dd_126d_v111_signal},    "f25_brand_equity_equity_moat_dd_126d_v112_signal": {"inputs": [], "func": f25_brand_equity_equity_moat_dd_126d_v112_signal},    "f25_brand_equity_grossmargin_dd_252d_v113_signal": {"inputs": [], "func": f25_brand_equity_grossmargin_dd_252d_v113_signal},    "f25_brand_equity_pe_dd_252d_v114_signal": {"inputs": [], "func": f25_brand_equity_pe_dd_252d_v114_signal},    "f25_brand_equity_pb_dd_252d_v115_signal": {"inputs": [], "func": f25_brand_equity_pb_dd_252d_v115_signal},    "f25_brand_equity_equity_moat_dd_252d_v116_signal": {"inputs": [], "func": f25_brand_equity_equity_moat_dd_252d_v116_signal},    "f25_brand_equity_grossmargin_dd_504d_v117_signal": {"inputs": [], "func": f25_brand_equity_grossmargin_dd_504d_v117_signal},    "f25_brand_equity_pe_dd_504d_v118_signal": {"inputs": [], "func": f25_brand_equity_pe_dd_504d_v118_signal},    "f25_brand_equity_pb_dd_504d_v119_signal": {"inputs": [], "func": f25_brand_equity_pb_dd_504d_v119_signal},    "f25_brand_equity_equity_moat_dd_504d_v120_signal": {"inputs": [], "func": f25_brand_equity_equity_moat_dd_504d_v120_signal},    "f25_brand_equity_grossmargin_dd_756d_v121_signal": {"inputs": [], "func": f25_brand_equity_grossmargin_dd_756d_v121_signal},    "f25_brand_equity_pe_dd_756d_v122_signal": {"inputs": [], "func": f25_brand_equity_pe_dd_756d_v122_signal},    "f25_brand_equity_pb_dd_756d_v123_signal": {"inputs": [], "func": f25_brand_equity_pb_dd_756d_v123_signal},    "f25_brand_equity_equity_moat_dd_756d_v124_signal": {"inputs": [], "func": f25_brand_equity_equity_moat_dd_756d_v124_signal},    "f25_brand_equity_grossmargin_dd_1008d_v125_signal": {"inputs": [], "func": f25_brand_equity_grossmargin_dd_1008d_v125_signal},    "f25_brand_equity_pe_dd_1008d_v126_signal": {"inputs": [], "func": f25_brand_equity_pe_dd_1008d_v126_signal},    "f25_brand_equity_pb_dd_1008d_v127_signal": {"inputs": [], "func": f25_brand_equity_pb_dd_1008d_v127_signal},    "f25_brand_equity_equity_moat_dd_1008d_v128_signal": {"inputs": [], "func": f25_brand_equity_equity_moat_dd_1008d_v128_signal},    "f25_brand_equity_grossmargin_dd_1260d_v129_signal": {"inputs": [], "func": f25_brand_equity_grossmargin_dd_1260d_v129_signal},    "f25_brand_equity_pe_dd_1260d_v130_signal": {"inputs": [], "func": f25_brand_equity_pe_dd_1260d_v130_signal},    "f25_brand_equity_pb_dd_1260d_v131_signal": {"inputs": [], "func": f25_brand_equity_pb_dd_1260d_v131_signal},    "f25_brand_equity_equity_moat_dd_1260d_v132_signal": {"inputs": [], "func": f25_brand_equity_equity_moat_dd_1260d_v132_signal},    "f25_brand_equity_grossmargin_rec_5d_v133_signal": {"inputs": [], "func": f25_brand_equity_grossmargin_rec_5d_v133_signal},    "f25_brand_equity_pe_rec_5d_v134_signal": {"inputs": [], "func": f25_brand_equity_pe_rec_5d_v134_signal},    "f25_brand_equity_pb_rec_5d_v135_signal": {"inputs": [], "func": f25_brand_equity_pb_rec_5d_v135_signal},    "f25_brand_equity_equity_moat_rec_5d_v136_signal": {"inputs": [], "func": f25_brand_equity_equity_moat_rec_5d_v136_signal},    "f25_brand_equity_grossmargin_rec_10d_v137_signal": {"inputs": [], "func": f25_brand_equity_grossmargin_rec_10d_v137_signal},    "f25_brand_equity_pe_rec_10d_v138_signal": {"inputs": [], "func": f25_brand_equity_pe_rec_10d_v138_signal},    "f25_brand_equity_pb_rec_10d_v139_signal": {"inputs": [], "func": f25_brand_equity_pb_rec_10d_v139_signal},    "f25_brand_equity_equity_moat_rec_10d_v140_signal": {"inputs": [], "func": f25_brand_equity_equity_moat_rec_10d_v140_signal},    "f25_brand_equity_grossmargin_rec_21d_v141_signal": {"inputs": [], "func": f25_brand_equity_grossmargin_rec_21d_v141_signal},    "f25_brand_equity_pe_rec_21d_v142_signal": {"inputs": [], "func": f25_brand_equity_pe_rec_21d_v142_signal},    "f25_brand_equity_pb_rec_21d_v143_signal": {"inputs": [], "func": f25_brand_equity_pb_rec_21d_v143_signal},    "f25_brand_equity_equity_moat_rec_21d_v144_signal": {"inputs": [], "func": f25_brand_equity_equity_moat_rec_21d_v144_signal},    "f25_brand_equity_grossmargin_rec_42d_v145_signal": {"inputs": [], "func": f25_brand_equity_grossmargin_rec_42d_v145_signal},    "f25_brand_equity_pe_rec_42d_v146_signal": {"inputs": [], "func": f25_brand_equity_pe_rec_42d_v146_signal},    "f25_brand_equity_pb_rec_42d_v147_signal": {"inputs": [], "func": f25_brand_equity_pb_rec_42d_v147_signal},    "f25_brand_equity_equity_moat_rec_42d_v148_signal": {"inputs": [], "func": f25_brand_equity_equity_moat_rec_42d_v148_signal},    "f25_brand_equity_grossmargin_rec_63d_v149_signal": {"inputs": [], "func": f25_brand_equity_grossmargin_rec_63d_v149_signal},    "f25_brand_equity_pe_rec_63d_v150_signal": {"inputs": [], "func": f25_brand_equity_pe_rec_63d_v150_signal},
}

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "grossmargin": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "pe": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "pb": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "deferredrev": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "liabilitiesc": np.random.normal(100, 10, n).cumsum()
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
            if res.dropna().empty: raise ValueError("All NaNs produced")
        except Exception as e:
            print(f"Error in {name}: {e}")
            break
    print("Success.")
