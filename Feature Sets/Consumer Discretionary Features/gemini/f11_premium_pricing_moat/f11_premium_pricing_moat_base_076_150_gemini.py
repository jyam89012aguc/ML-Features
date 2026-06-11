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

def f11_premium_pricing_moat_pricing_power_index_z_504d_v076_signal(grossmargin, ebitdamargin):
    """Z-score for relative outlier detection of Compound index of manufacturing and operating efficiency over 504d window."""
    res = _z(grossmargin * ebitdamargin, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_premium_pricing_moat_grossmargin_z_756d_v077_signal(grossmargin):
    """Z-score for relative outlier detection of Raw level of grossmargin over 756d window."""
    res = _z(grossmargin, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_premium_pricing_moat_ebitdamargin_z_756d_v078_signal(ebitdamargin):
    """Z-score for relative outlier detection of Raw level of ebitdamargin over 756d window."""
    res = _z(ebitdamargin, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_premium_pricing_moat_marketcap_z_756d_v079_signal(marketcap):
    """Z-score for relative outlier detection of Raw level of marketcap over 756d window."""
    res = _z(marketcap, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_premium_pricing_moat_pricing_power_index_z_756d_v080_signal(grossmargin, ebitdamargin):
    """Z-score for relative outlier detection of Compound index of manufacturing and operating efficiency over 756d window."""
    res = _z(grossmargin * ebitdamargin, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_premium_pricing_moat_grossmargin_z_1008d_v081_signal(grossmargin):
    """Z-score for relative outlier detection of Raw level of grossmargin over 1008d window."""
    res = _z(grossmargin, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_premium_pricing_moat_ebitdamargin_z_1008d_v082_signal(ebitdamargin):
    """Z-score for relative outlier detection of Raw level of ebitdamargin over 1008d window."""
    res = _z(ebitdamargin, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_premium_pricing_moat_marketcap_z_1008d_v083_signal(marketcap):
    """Z-score for relative outlier detection of Raw level of marketcap over 1008d window."""
    res = _z(marketcap, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_premium_pricing_moat_pricing_power_index_z_1008d_v084_signal(grossmargin, ebitdamargin):
    """Z-score for relative outlier detection of Compound index of manufacturing and operating efficiency over 1008d window."""
    res = _z(grossmargin * ebitdamargin, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_premium_pricing_moat_grossmargin_z_1260d_v085_signal(grossmargin):
    """Z-score for relative outlier detection of Raw level of grossmargin over 1260d window."""
    res = _z(grossmargin, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_premium_pricing_moat_ebitdamargin_z_1260d_v086_signal(ebitdamargin):
    """Z-score for relative outlier detection of Raw level of ebitdamargin over 1260d window."""
    res = _z(ebitdamargin, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_premium_pricing_moat_marketcap_z_1260d_v087_signal(marketcap):
    """Z-score for relative outlier detection of Raw level of marketcap over 1260d window."""
    res = _z(marketcap, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_premium_pricing_moat_pricing_power_index_z_1260d_v088_signal(grossmargin, ebitdamargin):
    """Z-score for relative outlier detection of Compound index of manufacturing and operating efficiency over 1260d window."""
    res = _z(grossmargin * ebitdamargin, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_premium_pricing_moat_grossmargin_dd_5d_v089_signal(grossmargin):
    """Drawdown from peak to identify cycle troughs of Raw level of grossmargin over 5d window."""
    res = _drawdown(grossmargin, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_premium_pricing_moat_ebitdamargin_dd_5d_v090_signal(ebitdamargin):
    """Drawdown from peak to identify cycle troughs of Raw level of ebitdamargin over 5d window."""
    res = _drawdown(ebitdamargin, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_premium_pricing_moat_marketcap_dd_5d_v091_signal(marketcap):
    """Drawdown from peak to identify cycle troughs of Raw level of marketcap over 5d window."""
    res = _drawdown(marketcap, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_premium_pricing_moat_pricing_power_index_dd_5d_v092_signal(grossmargin, ebitdamargin):
    """Drawdown from peak to identify cycle troughs of Compound index of manufacturing and operating efficiency over 5d window."""
    res = _drawdown(grossmargin * ebitdamargin, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_premium_pricing_moat_grossmargin_dd_10d_v093_signal(grossmargin):
    """Drawdown from peak to identify cycle troughs of Raw level of grossmargin over 10d window."""
    res = _drawdown(grossmargin, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_premium_pricing_moat_ebitdamargin_dd_10d_v094_signal(ebitdamargin):
    """Drawdown from peak to identify cycle troughs of Raw level of ebitdamargin over 10d window."""
    res = _drawdown(ebitdamargin, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_premium_pricing_moat_marketcap_dd_10d_v095_signal(marketcap):
    """Drawdown from peak to identify cycle troughs of Raw level of marketcap over 10d window."""
    res = _drawdown(marketcap, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_premium_pricing_moat_pricing_power_index_dd_10d_v096_signal(grossmargin, ebitdamargin):
    """Drawdown from peak to identify cycle troughs of Compound index of manufacturing and operating efficiency over 10d window."""
    res = _drawdown(grossmargin * ebitdamargin, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_premium_pricing_moat_grossmargin_dd_21d_v097_signal(grossmargin):
    """Drawdown from peak to identify cycle troughs of Raw level of grossmargin over 21d window."""
    res = _drawdown(grossmargin, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_premium_pricing_moat_ebitdamargin_dd_21d_v098_signal(ebitdamargin):
    """Drawdown from peak to identify cycle troughs of Raw level of ebitdamargin over 21d window."""
    res = _drawdown(ebitdamargin, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_premium_pricing_moat_marketcap_dd_21d_v099_signal(marketcap):
    """Drawdown from peak to identify cycle troughs of Raw level of marketcap over 21d window."""
    res = _drawdown(marketcap, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_premium_pricing_moat_pricing_power_index_dd_21d_v100_signal(grossmargin, ebitdamargin):
    """Drawdown from peak to identify cycle troughs of Compound index of manufacturing and operating efficiency over 21d window."""
    res = _drawdown(grossmargin * ebitdamargin, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_premium_pricing_moat_grossmargin_dd_42d_v101_signal(grossmargin):
    """Drawdown from peak to identify cycle troughs of Raw level of grossmargin over 42d window."""
    res = _drawdown(grossmargin, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_premium_pricing_moat_ebitdamargin_dd_42d_v102_signal(ebitdamargin):
    """Drawdown from peak to identify cycle troughs of Raw level of ebitdamargin over 42d window."""
    res = _drawdown(ebitdamargin, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_premium_pricing_moat_marketcap_dd_42d_v103_signal(marketcap):
    """Drawdown from peak to identify cycle troughs of Raw level of marketcap over 42d window."""
    res = _drawdown(marketcap, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_premium_pricing_moat_pricing_power_index_dd_42d_v104_signal(grossmargin, ebitdamargin):
    """Drawdown from peak to identify cycle troughs of Compound index of manufacturing and operating efficiency over 42d window."""
    res = _drawdown(grossmargin * ebitdamargin, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_premium_pricing_moat_grossmargin_dd_63d_v105_signal(grossmargin):
    """Drawdown from peak to identify cycle troughs of Raw level of grossmargin over 63d window."""
    res = _drawdown(grossmargin, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_premium_pricing_moat_ebitdamargin_dd_63d_v106_signal(ebitdamargin):
    """Drawdown from peak to identify cycle troughs of Raw level of ebitdamargin over 63d window."""
    res = _drawdown(ebitdamargin, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_premium_pricing_moat_marketcap_dd_63d_v107_signal(marketcap):
    """Drawdown from peak to identify cycle troughs of Raw level of marketcap over 63d window."""
    res = _drawdown(marketcap, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_premium_pricing_moat_pricing_power_index_dd_63d_v108_signal(grossmargin, ebitdamargin):
    """Drawdown from peak to identify cycle troughs of Compound index of manufacturing and operating efficiency over 63d window."""
    res = _drawdown(grossmargin * ebitdamargin, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_premium_pricing_moat_grossmargin_dd_126d_v109_signal(grossmargin):
    """Drawdown from peak to identify cycle troughs of Raw level of grossmargin over 126d window."""
    res = _drawdown(grossmargin, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_premium_pricing_moat_ebitdamargin_dd_126d_v110_signal(ebitdamargin):
    """Drawdown from peak to identify cycle troughs of Raw level of ebitdamargin over 126d window."""
    res = _drawdown(ebitdamargin, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_premium_pricing_moat_marketcap_dd_126d_v111_signal(marketcap):
    """Drawdown from peak to identify cycle troughs of Raw level of marketcap over 126d window."""
    res = _drawdown(marketcap, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_premium_pricing_moat_pricing_power_index_dd_126d_v112_signal(grossmargin, ebitdamargin):
    """Drawdown from peak to identify cycle troughs of Compound index of manufacturing and operating efficiency over 126d window."""
    res = _drawdown(grossmargin * ebitdamargin, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_premium_pricing_moat_grossmargin_dd_252d_v113_signal(grossmargin):
    """Drawdown from peak to identify cycle troughs of Raw level of grossmargin over 252d window."""
    res = _drawdown(grossmargin, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_premium_pricing_moat_ebitdamargin_dd_252d_v114_signal(ebitdamargin):
    """Drawdown from peak to identify cycle troughs of Raw level of ebitdamargin over 252d window."""
    res = _drawdown(ebitdamargin, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_premium_pricing_moat_marketcap_dd_252d_v115_signal(marketcap):
    """Drawdown from peak to identify cycle troughs of Raw level of marketcap over 252d window."""
    res = _drawdown(marketcap, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_premium_pricing_moat_pricing_power_index_dd_252d_v116_signal(grossmargin, ebitdamargin):
    """Drawdown from peak to identify cycle troughs of Compound index of manufacturing and operating efficiency over 252d window."""
    res = _drawdown(grossmargin * ebitdamargin, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_premium_pricing_moat_grossmargin_dd_504d_v117_signal(grossmargin):
    """Drawdown from peak to identify cycle troughs of Raw level of grossmargin over 504d window."""
    res = _drawdown(grossmargin, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_premium_pricing_moat_ebitdamargin_dd_504d_v118_signal(ebitdamargin):
    """Drawdown from peak to identify cycle troughs of Raw level of ebitdamargin over 504d window."""
    res = _drawdown(ebitdamargin, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_premium_pricing_moat_marketcap_dd_504d_v119_signal(marketcap):
    """Drawdown from peak to identify cycle troughs of Raw level of marketcap over 504d window."""
    res = _drawdown(marketcap, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_premium_pricing_moat_pricing_power_index_dd_504d_v120_signal(grossmargin, ebitdamargin):
    """Drawdown from peak to identify cycle troughs of Compound index of manufacturing and operating efficiency over 504d window."""
    res = _drawdown(grossmargin * ebitdamargin, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_premium_pricing_moat_grossmargin_dd_756d_v121_signal(grossmargin):
    """Drawdown from peak to identify cycle troughs of Raw level of grossmargin over 756d window."""
    res = _drawdown(grossmargin, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_premium_pricing_moat_ebitdamargin_dd_756d_v122_signal(ebitdamargin):
    """Drawdown from peak to identify cycle troughs of Raw level of ebitdamargin over 756d window."""
    res = _drawdown(ebitdamargin, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_premium_pricing_moat_marketcap_dd_756d_v123_signal(marketcap):
    """Drawdown from peak to identify cycle troughs of Raw level of marketcap over 756d window."""
    res = _drawdown(marketcap, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_premium_pricing_moat_pricing_power_index_dd_756d_v124_signal(grossmargin, ebitdamargin):
    """Drawdown from peak to identify cycle troughs of Compound index of manufacturing and operating efficiency over 756d window."""
    res = _drawdown(grossmargin * ebitdamargin, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_premium_pricing_moat_grossmargin_dd_1008d_v125_signal(grossmargin):
    """Drawdown from peak to identify cycle troughs of Raw level of grossmargin over 1008d window."""
    res = _drawdown(grossmargin, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_premium_pricing_moat_ebitdamargin_dd_1008d_v126_signal(ebitdamargin):
    """Drawdown from peak to identify cycle troughs of Raw level of ebitdamargin over 1008d window."""
    res = _drawdown(ebitdamargin, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_premium_pricing_moat_marketcap_dd_1008d_v127_signal(marketcap):
    """Drawdown from peak to identify cycle troughs of Raw level of marketcap over 1008d window."""
    res = _drawdown(marketcap, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_premium_pricing_moat_pricing_power_index_dd_1008d_v128_signal(grossmargin, ebitdamargin):
    """Drawdown from peak to identify cycle troughs of Compound index of manufacturing and operating efficiency over 1008d window."""
    res = _drawdown(grossmargin * ebitdamargin, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_premium_pricing_moat_grossmargin_dd_1260d_v129_signal(grossmargin):
    """Drawdown from peak to identify cycle troughs of Raw level of grossmargin over 1260d window."""
    res = _drawdown(grossmargin, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_premium_pricing_moat_ebitdamargin_dd_1260d_v130_signal(ebitdamargin):
    """Drawdown from peak to identify cycle troughs of Raw level of ebitdamargin over 1260d window."""
    res = _drawdown(ebitdamargin, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_premium_pricing_moat_marketcap_dd_1260d_v131_signal(marketcap):
    """Drawdown from peak to identify cycle troughs of Raw level of marketcap over 1260d window."""
    res = _drawdown(marketcap, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_premium_pricing_moat_pricing_power_index_dd_1260d_v132_signal(grossmargin, ebitdamargin):
    """Drawdown from peak to identify cycle troughs of Compound index of manufacturing and operating efficiency over 1260d window."""
    res = _drawdown(grossmargin * ebitdamargin, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_premium_pricing_moat_grossmargin_rec_5d_v133_signal(grossmargin):
    """Recovery from trough for turnaround signals of Raw level of grossmargin over 5d window."""
    res = _recovery(grossmargin, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_premium_pricing_moat_ebitdamargin_rec_5d_v134_signal(ebitdamargin):
    """Recovery from trough for turnaround signals of Raw level of ebitdamargin over 5d window."""
    res = _recovery(ebitdamargin, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_premium_pricing_moat_marketcap_rec_5d_v135_signal(marketcap):
    """Recovery from trough for turnaround signals of Raw level of marketcap over 5d window."""
    res = _recovery(marketcap, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_premium_pricing_moat_pricing_power_index_rec_5d_v136_signal(grossmargin, ebitdamargin):
    """Recovery from trough for turnaround signals of Compound index of manufacturing and operating efficiency over 5d window."""
    res = _recovery(grossmargin * ebitdamargin, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_premium_pricing_moat_grossmargin_rec_10d_v137_signal(grossmargin):
    """Recovery from trough for turnaround signals of Raw level of grossmargin over 10d window."""
    res = _recovery(grossmargin, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_premium_pricing_moat_ebitdamargin_rec_10d_v138_signal(ebitdamargin):
    """Recovery from trough for turnaround signals of Raw level of ebitdamargin over 10d window."""
    res = _recovery(ebitdamargin, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_premium_pricing_moat_marketcap_rec_10d_v139_signal(marketcap):
    """Recovery from trough for turnaround signals of Raw level of marketcap over 10d window."""
    res = _recovery(marketcap, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_premium_pricing_moat_pricing_power_index_rec_10d_v140_signal(grossmargin, ebitdamargin):
    """Recovery from trough for turnaround signals of Compound index of manufacturing and operating efficiency over 10d window."""
    res = _recovery(grossmargin * ebitdamargin, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_premium_pricing_moat_grossmargin_rec_21d_v141_signal(grossmargin):
    """Recovery from trough for turnaround signals of Raw level of grossmargin over 21d window."""
    res = _recovery(grossmargin, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_premium_pricing_moat_ebitdamargin_rec_21d_v142_signal(ebitdamargin):
    """Recovery from trough for turnaround signals of Raw level of ebitdamargin over 21d window."""
    res = _recovery(ebitdamargin, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_premium_pricing_moat_marketcap_rec_21d_v143_signal(marketcap):
    """Recovery from trough for turnaround signals of Raw level of marketcap over 21d window."""
    res = _recovery(marketcap, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_premium_pricing_moat_pricing_power_index_rec_21d_v144_signal(grossmargin, ebitdamargin):
    """Recovery from trough for turnaround signals of Compound index of manufacturing and operating efficiency over 21d window."""
    res = _recovery(grossmargin * ebitdamargin, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_premium_pricing_moat_grossmargin_rec_42d_v145_signal(grossmargin):
    """Recovery from trough for turnaround signals of Raw level of grossmargin over 42d window."""
    res = _recovery(grossmargin, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_premium_pricing_moat_ebitdamargin_rec_42d_v146_signal(ebitdamargin):
    """Recovery from trough for turnaround signals of Raw level of ebitdamargin over 42d window."""
    res = _recovery(ebitdamargin, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_premium_pricing_moat_marketcap_rec_42d_v147_signal(marketcap):
    """Recovery from trough for turnaround signals of Raw level of marketcap over 42d window."""
    res = _recovery(marketcap, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_premium_pricing_moat_pricing_power_index_rec_42d_v148_signal(grossmargin, ebitdamargin):
    """Recovery from trough for turnaround signals of Compound index of manufacturing and operating efficiency over 42d window."""
    res = _recovery(grossmargin * ebitdamargin, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_premium_pricing_moat_grossmargin_rec_63d_v149_signal(grossmargin):
    """Recovery from trough for turnaround signals of Raw level of grossmargin over 63d window."""
    res = _recovery(grossmargin, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_premium_pricing_moat_ebitdamargin_rec_63d_v150_signal(ebitdamargin):
    """Recovery from trough for turnaround signals of Raw level of ebitdamargin over 63d window."""
    res = _recovery(ebitdamargin, 63)
    return res.replace([np.inf, -np.inf], np.nan)


# ===== Feature Registry =====
REGISTRY = {
    "f11_premium_pricing_moat_pricing_power_index_z_504d_v076_signal": {"inputs": [], "func": f11_premium_pricing_moat_pricing_power_index_z_504d_v076_signal},    "f11_premium_pricing_moat_grossmargin_z_756d_v077_signal": {"inputs": [], "func": f11_premium_pricing_moat_grossmargin_z_756d_v077_signal},    "f11_premium_pricing_moat_ebitdamargin_z_756d_v078_signal": {"inputs": [], "func": f11_premium_pricing_moat_ebitdamargin_z_756d_v078_signal},    "f11_premium_pricing_moat_marketcap_z_756d_v079_signal": {"inputs": [], "func": f11_premium_pricing_moat_marketcap_z_756d_v079_signal},    "f11_premium_pricing_moat_pricing_power_index_z_756d_v080_signal": {"inputs": [], "func": f11_premium_pricing_moat_pricing_power_index_z_756d_v080_signal},    "f11_premium_pricing_moat_grossmargin_z_1008d_v081_signal": {"inputs": [], "func": f11_premium_pricing_moat_grossmargin_z_1008d_v081_signal},    "f11_premium_pricing_moat_ebitdamargin_z_1008d_v082_signal": {"inputs": [], "func": f11_premium_pricing_moat_ebitdamargin_z_1008d_v082_signal},    "f11_premium_pricing_moat_marketcap_z_1008d_v083_signal": {"inputs": [], "func": f11_premium_pricing_moat_marketcap_z_1008d_v083_signal},    "f11_premium_pricing_moat_pricing_power_index_z_1008d_v084_signal": {"inputs": [], "func": f11_premium_pricing_moat_pricing_power_index_z_1008d_v084_signal},    "f11_premium_pricing_moat_grossmargin_z_1260d_v085_signal": {"inputs": [], "func": f11_premium_pricing_moat_grossmargin_z_1260d_v085_signal},    "f11_premium_pricing_moat_ebitdamargin_z_1260d_v086_signal": {"inputs": [], "func": f11_premium_pricing_moat_ebitdamargin_z_1260d_v086_signal},    "f11_premium_pricing_moat_marketcap_z_1260d_v087_signal": {"inputs": [], "func": f11_premium_pricing_moat_marketcap_z_1260d_v087_signal},    "f11_premium_pricing_moat_pricing_power_index_z_1260d_v088_signal": {"inputs": [], "func": f11_premium_pricing_moat_pricing_power_index_z_1260d_v088_signal},    "f11_premium_pricing_moat_grossmargin_dd_5d_v089_signal": {"inputs": [], "func": f11_premium_pricing_moat_grossmargin_dd_5d_v089_signal},    "f11_premium_pricing_moat_ebitdamargin_dd_5d_v090_signal": {"inputs": [], "func": f11_premium_pricing_moat_ebitdamargin_dd_5d_v090_signal},    "f11_premium_pricing_moat_marketcap_dd_5d_v091_signal": {"inputs": [], "func": f11_premium_pricing_moat_marketcap_dd_5d_v091_signal},    "f11_premium_pricing_moat_pricing_power_index_dd_5d_v092_signal": {"inputs": [], "func": f11_premium_pricing_moat_pricing_power_index_dd_5d_v092_signal},    "f11_premium_pricing_moat_grossmargin_dd_10d_v093_signal": {"inputs": [], "func": f11_premium_pricing_moat_grossmargin_dd_10d_v093_signal},    "f11_premium_pricing_moat_ebitdamargin_dd_10d_v094_signal": {"inputs": [], "func": f11_premium_pricing_moat_ebitdamargin_dd_10d_v094_signal},    "f11_premium_pricing_moat_marketcap_dd_10d_v095_signal": {"inputs": [], "func": f11_premium_pricing_moat_marketcap_dd_10d_v095_signal},    "f11_premium_pricing_moat_pricing_power_index_dd_10d_v096_signal": {"inputs": [], "func": f11_premium_pricing_moat_pricing_power_index_dd_10d_v096_signal},    "f11_premium_pricing_moat_grossmargin_dd_21d_v097_signal": {"inputs": [], "func": f11_premium_pricing_moat_grossmargin_dd_21d_v097_signal},    "f11_premium_pricing_moat_ebitdamargin_dd_21d_v098_signal": {"inputs": [], "func": f11_premium_pricing_moat_ebitdamargin_dd_21d_v098_signal},    "f11_premium_pricing_moat_marketcap_dd_21d_v099_signal": {"inputs": [], "func": f11_premium_pricing_moat_marketcap_dd_21d_v099_signal},    "f11_premium_pricing_moat_pricing_power_index_dd_21d_v100_signal": {"inputs": [], "func": f11_premium_pricing_moat_pricing_power_index_dd_21d_v100_signal},    "f11_premium_pricing_moat_grossmargin_dd_42d_v101_signal": {"inputs": [], "func": f11_premium_pricing_moat_grossmargin_dd_42d_v101_signal},    "f11_premium_pricing_moat_ebitdamargin_dd_42d_v102_signal": {"inputs": [], "func": f11_premium_pricing_moat_ebitdamargin_dd_42d_v102_signal},    "f11_premium_pricing_moat_marketcap_dd_42d_v103_signal": {"inputs": [], "func": f11_premium_pricing_moat_marketcap_dd_42d_v103_signal},    "f11_premium_pricing_moat_pricing_power_index_dd_42d_v104_signal": {"inputs": [], "func": f11_premium_pricing_moat_pricing_power_index_dd_42d_v104_signal},    "f11_premium_pricing_moat_grossmargin_dd_63d_v105_signal": {"inputs": [], "func": f11_premium_pricing_moat_grossmargin_dd_63d_v105_signal},    "f11_premium_pricing_moat_ebitdamargin_dd_63d_v106_signal": {"inputs": [], "func": f11_premium_pricing_moat_ebitdamargin_dd_63d_v106_signal},    "f11_premium_pricing_moat_marketcap_dd_63d_v107_signal": {"inputs": [], "func": f11_premium_pricing_moat_marketcap_dd_63d_v107_signal},    "f11_premium_pricing_moat_pricing_power_index_dd_63d_v108_signal": {"inputs": [], "func": f11_premium_pricing_moat_pricing_power_index_dd_63d_v108_signal},    "f11_premium_pricing_moat_grossmargin_dd_126d_v109_signal": {"inputs": [], "func": f11_premium_pricing_moat_grossmargin_dd_126d_v109_signal},    "f11_premium_pricing_moat_ebitdamargin_dd_126d_v110_signal": {"inputs": [], "func": f11_premium_pricing_moat_ebitdamargin_dd_126d_v110_signal},    "f11_premium_pricing_moat_marketcap_dd_126d_v111_signal": {"inputs": [], "func": f11_premium_pricing_moat_marketcap_dd_126d_v111_signal},    "f11_premium_pricing_moat_pricing_power_index_dd_126d_v112_signal": {"inputs": [], "func": f11_premium_pricing_moat_pricing_power_index_dd_126d_v112_signal},    "f11_premium_pricing_moat_grossmargin_dd_252d_v113_signal": {"inputs": [], "func": f11_premium_pricing_moat_grossmargin_dd_252d_v113_signal},    "f11_premium_pricing_moat_ebitdamargin_dd_252d_v114_signal": {"inputs": [], "func": f11_premium_pricing_moat_ebitdamargin_dd_252d_v114_signal},    "f11_premium_pricing_moat_marketcap_dd_252d_v115_signal": {"inputs": [], "func": f11_premium_pricing_moat_marketcap_dd_252d_v115_signal},    "f11_premium_pricing_moat_pricing_power_index_dd_252d_v116_signal": {"inputs": [], "func": f11_premium_pricing_moat_pricing_power_index_dd_252d_v116_signal},    "f11_premium_pricing_moat_grossmargin_dd_504d_v117_signal": {"inputs": [], "func": f11_premium_pricing_moat_grossmargin_dd_504d_v117_signal},    "f11_premium_pricing_moat_ebitdamargin_dd_504d_v118_signal": {"inputs": [], "func": f11_premium_pricing_moat_ebitdamargin_dd_504d_v118_signal},    "f11_premium_pricing_moat_marketcap_dd_504d_v119_signal": {"inputs": [], "func": f11_premium_pricing_moat_marketcap_dd_504d_v119_signal},    "f11_premium_pricing_moat_pricing_power_index_dd_504d_v120_signal": {"inputs": [], "func": f11_premium_pricing_moat_pricing_power_index_dd_504d_v120_signal},    "f11_premium_pricing_moat_grossmargin_dd_756d_v121_signal": {"inputs": [], "func": f11_premium_pricing_moat_grossmargin_dd_756d_v121_signal},    "f11_premium_pricing_moat_ebitdamargin_dd_756d_v122_signal": {"inputs": [], "func": f11_premium_pricing_moat_ebitdamargin_dd_756d_v122_signal},    "f11_premium_pricing_moat_marketcap_dd_756d_v123_signal": {"inputs": [], "func": f11_premium_pricing_moat_marketcap_dd_756d_v123_signal},    "f11_premium_pricing_moat_pricing_power_index_dd_756d_v124_signal": {"inputs": [], "func": f11_premium_pricing_moat_pricing_power_index_dd_756d_v124_signal},    "f11_premium_pricing_moat_grossmargin_dd_1008d_v125_signal": {"inputs": [], "func": f11_premium_pricing_moat_grossmargin_dd_1008d_v125_signal},    "f11_premium_pricing_moat_ebitdamargin_dd_1008d_v126_signal": {"inputs": [], "func": f11_premium_pricing_moat_ebitdamargin_dd_1008d_v126_signal},    "f11_premium_pricing_moat_marketcap_dd_1008d_v127_signal": {"inputs": [], "func": f11_premium_pricing_moat_marketcap_dd_1008d_v127_signal},    "f11_premium_pricing_moat_pricing_power_index_dd_1008d_v128_signal": {"inputs": [], "func": f11_premium_pricing_moat_pricing_power_index_dd_1008d_v128_signal},    "f11_premium_pricing_moat_grossmargin_dd_1260d_v129_signal": {"inputs": [], "func": f11_premium_pricing_moat_grossmargin_dd_1260d_v129_signal},    "f11_premium_pricing_moat_ebitdamargin_dd_1260d_v130_signal": {"inputs": [], "func": f11_premium_pricing_moat_ebitdamargin_dd_1260d_v130_signal},    "f11_premium_pricing_moat_marketcap_dd_1260d_v131_signal": {"inputs": [], "func": f11_premium_pricing_moat_marketcap_dd_1260d_v131_signal},    "f11_premium_pricing_moat_pricing_power_index_dd_1260d_v132_signal": {"inputs": [], "func": f11_premium_pricing_moat_pricing_power_index_dd_1260d_v132_signal},    "f11_premium_pricing_moat_grossmargin_rec_5d_v133_signal": {"inputs": [], "func": f11_premium_pricing_moat_grossmargin_rec_5d_v133_signal},    "f11_premium_pricing_moat_ebitdamargin_rec_5d_v134_signal": {"inputs": [], "func": f11_premium_pricing_moat_ebitdamargin_rec_5d_v134_signal},    "f11_premium_pricing_moat_marketcap_rec_5d_v135_signal": {"inputs": [], "func": f11_premium_pricing_moat_marketcap_rec_5d_v135_signal},    "f11_premium_pricing_moat_pricing_power_index_rec_5d_v136_signal": {"inputs": [], "func": f11_premium_pricing_moat_pricing_power_index_rec_5d_v136_signal},    "f11_premium_pricing_moat_grossmargin_rec_10d_v137_signal": {"inputs": [], "func": f11_premium_pricing_moat_grossmargin_rec_10d_v137_signal},    "f11_premium_pricing_moat_ebitdamargin_rec_10d_v138_signal": {"inputs": [], "func": f11_premium_pricing_moat_ebitdamargin_rec_10d_v138_signal},    "f11_premium_pricing_moat_marketcap_rec_10d_v139_signal": {"inputs": [], "func": f11_premium_pricing_moat_marketcap_rec_10d_v139_signal},    "f11_premium_pricing_moat_pricing_power_index_rec_10d_v140_signal": {"inputs": [], "func": f11_premium_pricing_moat_pricing_power_index_rec_10d_v140_signal},    "f11_premium_pricing_moat_grossmargin_rec_21d_v141_signal": {"inputs": [], "func": f11_premium_pricing_moat_grossmargin_rec_21d_v141_signal},    "f11_premium_pricing_moat_ebitdamargin_rec_21d_v142_signal": {"inputs": [], "func": f11_premium_pricing_moat_ebitdamargin_rec_21d_v142_signal},    "f11_premium_pricing_moat_marketcap_rec_21d_v143_signal": {"inputs": [], "func": f11_premium_pricing_moat_marketcap_rec_21d_v143_signal},    "f11_premium_pricing_moat_pricing_power_index_rec_21d_v144_signal": {"inputs": [], "func": f11_premium_pricing_moat_pricing_power_index_rec_21d_v144_signal},    "f11_premium_pricing_moat_grossmargin_rec_42d_v145_signal": {"inputs": [], "func": f11_premium_pricing_moat_grossmargin_rec_42d_v145_signal},    "f11_premium_pricing_moat_ebitdamargin_rec_42d_v146_signal": {"inputs": [], "func": f11_premium_pricing_moat_ebitdamargin_rec_42d_v146_signal},    "f11_premium_pricing_moat_marketcap_rec_42d_v147_signal": {"inputs": [], "func": f11_premium_pricing_moat_marketcap_rec_42d_v147_signal},    "f11_premium_pricing_moat_pricing_power_index_rec_42d_v148_signal": {"inputs": [], "func": f11_premium_pricing_moat_pricing_power_index_rec_42d_v148_signal},    "f11_premium_pricing_moat_grossmargin_rec_63d_v149_signal": {"inputs": [], "func": f11_premium_pricing_moat_grossmargin_rec_63d_v149_signal},    "f11_premium_pricing_moat_ebitdamargin_rec_63d_v150_signal": {"inputs": [], "func": f11_premium_pricing_moat_ebitdamargin_rec_63d_v150_signal},
}

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "grossmargin": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "deferredrev": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "liabilitiesc": np.random.normal(100, 10, n).cumsum()
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
            if res.dropna().empty: raise ValueError("All NaNs produced")
        except Exception as e:
            print(f"Error in {name}: {e}")
            break
    print("Success.")
