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

def f34_liquidity_coverage_quick_ratio_fin_ewma_504d_v076_signal(cashneq, liabilitiesc):
    """Exponential moving average of Quick liquidity ratio over 504d window."""
    res = _ewma(_ratio(cashneq, liabilitiesc), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_liquidity_coverage_cashneq_ewma_756d_v077_signal(cashneq):
    """Exponential moving average of Raw level of cashneq over 756d window."""
    res = _ewma(cashneq, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_liquidity_coverage_liabilitiesc_ewma_756d_v078_signal(liabilitiesc):
    """Exponential moving average of Raw level of liabilitiesc over 756d window."""
    res = _ewma(liabilitiesc, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_liquidity_coverage_assets_ewma_756d_v079_signal(assets):
    """Exponential moving average of Raw level of assets over 756d window."""
    res = _ewma(assets, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_liquidity_coverage_quick_ratio_fin_ewma_756d_v080_signal(cashneq, liabilitiesc):
    """Exponential moving average of Quick liquidity ratio over 756d window."""
    res = _ewma(_ratio(cashneq, liabilitiesc), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_liquidity_coverage_cashneq_ewma_1008d_v081_signal(cashneq):
    """Exponential moving average of Raw level of cashneq over 1008d window."""
    res = _ewma(cashneq, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_liquidity_coverage_liabilitiesc_ewma_1008d_v082_signal(liabilitiesc):
    """Exponential moving average of Raw level of liabilitiesc over 1008d window."""
    res = _ewma(liabilitiesc, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_liquidity_coverage_assets_ewma_1008d_v083_signal(assets):
    """Exponential moving average of Raw level of assets over 1008d window."""
    res = _ewma(assets, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_liquidity_coverage_quick_ratio_fin_ewma_1008d_v084_signal(cashneq, liabilitiesc):
    """Exponential moving average of Quick liquidity ratio over 1008d window."""
    res = _ewma(_ratio(cashneq, liabilitiesc), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_liquidity_coverage_cashneq_ewma_1260d_v085_signal(cashneq):
    """Exponential moving average of Raw level of cashneq over 1260d window."""
    res = _ewma(cashneq, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_liquidity_coverage_liabilitiesc_ewma_1260d_v086_signal(liabilitiesc):
    """Exponential moving average of Raw level of liabilitiesc over 1260d window."""
    res = _ewma(liabilitiesc, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_liquidity_coverage_assets_ewma_1260d_v087_signal(assets):
    """Exponential moving average of Raw level of assets over 1260d window."""
    res = _ewma(assets, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_liquidity_coverage_quick_ratio_fin_ewma_1260d_v088_signal(cashneq, liabilitiesc):
    """Exponential moving average of Quick liquidity ratio over 1260d window."""
    res = _ewma(_ratio(cashneq, liabilitiesc), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_liquidity_coverage_cashneq_z_5d_v089_signal(cashneq):
    """Z-score of Raw level of cashneq over 5d window."""
    res = _z(cashneq, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_liquidity_coverage_liabilitiesc_z_5d_v090_signal(liabilitiesc):
    """Z-score of Raw level of liabilitiesc over 5d window."""
    res = _z(liabilitiesc, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_liquidity_coverage_assets_z_5d_v091_signal(assets):
    """Z-score of Raw level of assets over 5d window."""
    res = _z(assets, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_liquidity_coverage_quick_ratio_fin_z_5d_v092_signal(cashneq, liabilitiesc):
    """Z-score of Quick liquidity ratio over 5d window."""
    res = _z(_ratio(cashneq, liabilitiesc), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_liquidity_coverage_cashneq_z_10d_v093_signal(cashneq):
    """Z-score of Raw level of cashneq over 10d window."""
    res = _z(cashneq, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_liquidity_coverage_liabilitiesc_z_10d_v094_signal(liabilitiesc):
    """Z-score of Raw level of liabilitiesc over 10d window."""
    res = _z(liabilitiesc, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_liquidity_coverage_assets_z_10d_v095_signal(assets):
    """Z-score of Raw level of assets over 10d window."""
    res = _z(assets, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_liquidity_coverage_quick_ratio_fin_z_10d_v096_signal(cashneq, liabilitiesc):
    """Z-score of Quick liquidity ratio over 10d window."""
    res = _z(_ratio(cashneq, liabilitiesc), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_liquidity_coverage_cashneq_z_21d_v097_signal(cashneq):
    """Z-score of Raw level of cashneq over 21d window."""
    res = _z(cashneq, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_liquidity_coverage_liabilitiesc_z_21d_v098_signal(liabilitiesc):
    """Z-score of Raw level of liabilitiesc over 21d window."""
    res = _z(liabilitiesc, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_liquidity_coverage_assets_z_21d_v099_signal(assets):
    """Z-score of Raw level of assets over 21d window."""
    res = _z(assets, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_liquidity_coverage_quick_ratio_fin_z_21d_v100_signal(cashneq, liabilitiesc):
    """Z-score of Quick liquidity ratio over 21d window."""
    res = _z(_ratio(cashneq, liabilitiesc), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_liquidity_coverage_cashneq_z_42d_v101_signal(cashneq):
    """Z-score of Raw level of cashneq over 42d window."""
    res = _z(cashneq, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_liquidity_coverage_liabilitiesc_z_42d_v102_signal(liabilitiesc):
    """Z-score of Raw level of liabilitiesc over 42d window."""
    res = _z(liabilitiesc, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_liquidity_coverage_assets_z_42d_v103_signal(assets):
    """Z-score of Raw level of assets over 42d window."""
    res = _z(assets, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_liquidity_coverage_quick_ratio_fin_z_42d_v104_signal(cashneq, liabilitiesc):
    """Z-score of Quick liquidity ratio over 42d window."""
    res = _z(_ratio(cashneq, liabilitiesc), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_liquidity_coverage_cashneq_z_63d_v105_signal(cashneq):
    """Z-score of Raw level of cashneq over 63d window."""
    res = _z(cashneq, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_liquidity_coverage_liabilitiesc_z_63d_v106_signal(liabilitiesc):
    """Z-score of Raw level of liabilitiesc over 63d window."""
    res = _z(liabilitiesc, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_liquidity_coverage_assets_z_63d_v107_signal(assets):
    """Z-score of Raw level of assets over 63d window."""
    res = _z(assets, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_liquidity_coverage_quick_ratio_fin_z_63d_v108_signal(cashneq, liabilitiesc):
    """Z-score of Quick liquidity ratio over 63d window."""
    res = _z(_ratio(cashneq, liabilitiesc), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_liquidity_coverage_cashneq_z_126d_v109_signal(cashneq):
    """Z-score of Raw level of cashneq over 126d window."""
    res = _z(cashneq, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_liquidity_coverage_liabilitiesc_z_126d_v110_signal(liabilitiesc):
    """Z-score of Raw level of liabilitiesc over 126d window."""
    res = _z(liabilitiesc, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_liquidity_coverage_assets_z_126d_v111_signal(assets):
    """Z-score of Raw level of assets over 126d window."""
    res = _z(assets, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_liquidity_coverage_quick_ratio_fin_z_126d_v112_signal(cashneq, liabilitiesc):
    """Z-score of Quick liquidity ratio over 126d window."""
    res = _z(_ratio(cashneq, liabilitiesc), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_liquidity_coverage_cashneq_z_252d_v113_signal(cashneq):
    """Z-score of Raw level of cashneq over 252d window."""
    res = _z(cashneq, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_liquidity_coverage_liabilitiesc_z_252d_v114_signal(liabilitiesc):
    """Z-score of Raw level of liabilitiesc over 252d window."""
    res = _z(liabilitiesc, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_liquidity_coverage_assets_z_252d_v115_signal(assets):
    """Z-score of Raw level of assets over 252d window."""
    res = _z(assets, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_liquidity_coverage_quick_ratio_fin_z_252d_v116_signal(cashneq, liabilitiesc):
    """Z-score of Quick liquidity ratio over 252d window."""
    res = _z(_ratio(cashneq, liabilitiesc), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_liquidity_coverage_cashneq_z_504d_v117_signal(cashneq):
    """Z-score of Raw level of cashneq over 504d window."""
    res = _z(cashneq, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_liquidity_coverage_liabilitiesc_z_504d_v118_signal(liabilitiesc):
    """Z-score of Raw level of liabilitiesc over 504d window."""
    res = _z(liabilitiesc, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_liquidity_coverage_assets_z_504d_v119_signal(assets):
    """Z-score of Raw level of assets over 504d window."""
    res = _z(assets, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_liquidity_coverage_quick_ratio_fin_z_504d_v120_signal(cashneq, liabilitiesc):
    """Z-score of Quick liquidity ratio over 504d window."""
    res = _z(_ratio(cashneq, liabilitiesc), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_liquidity_coverage_cashneq_z_756d_v121_signal(cashneq):
    """Z-score of Raw level of cashneq over 756d window."""
    res = _z(cashneq, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_liquidity_coverage_liabilitiesc_z_756d_v122_signal(liabilitiesc):
    """Z-score of Raw level of liabilitiesc over 756d window."""
    res = _z(liabilitiesc, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_liquidity_coverage_assets_z_756d_v123_signal(assets):
    """Z-score of Raw level of assets over 756d window."""
    res = _z(assets, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_liquidity_coverage_quick_ratio_fin_z_756d_v124_signal(cashneq, liabilitiesc):
    """Z-score of Quick liquidity ratio over 756d window."""
    res = _z(_ratio(cashneq, liabilitiesc), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_liquidity_coverage_cashneq_z_1008d_v125_signal(cashneq):
    """Z-score of Raw level of cashneq over 1008d window."""
    res = _z(cashneq, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_liquidity_coverage_liabilitiesc_z_1008d_v126_signal(liabilitiesc):
    """Z-score of Raw level of liabilitiesc over 1008d window."""
    res = _z(liabilitiesc, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_liquidity_coverage_assets_z_1008d_v127_signal(assets):
    """Z-score of Raw level of assets over 1008d window."""
    res = _z(assets, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_liquidity_coverage_quick_ratio_fin_z_1008d_v128_signal(cashneq, liabilitiesc):
    """Z-score of Quick liquidity ratio over 1008d window."""
    res = _z(_ratio(cashneq, liabilitiesc), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_liquidity_coverage_cashneq_z_1260d_v129_signal(cashneq):
    """Z-score of Raw level of cashneq over 1260d window."""
    res = _z(cashneq, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_liquidity_coverage_liabilitiesc_z_1260d_v130_signal(liabilitiesc):
    """Z-score of Raw level of liabilitiesc over 1260d window."""
    res = _z(liabilitiesc, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_liquidity_coverage_assets_z_1260d_v131_signal(assets):
    """Z-score of Raw level of assets over 1260d window."""
    res = _z(assets, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_liquidity_coverage_quick_ratio_fin_z_1260d_v132_signal(cashneq, liabilitiesc):
    """Z-score of Quick liquidity ratio over 1260d window."""
    res = _z(_ratio(cashneq, liabilitiesc), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_liquidity_coverage_cashneq_dd_5d_v133_signal(cashneq):
    """Drawdown of Raw level of cashneq over 5d window."""
    res = _drawdown(cashneq, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_liquidity_coverage_liabilitiesc_dd_5d_v134_signal(liabilitiesc):
    """Drawdown of Raw level of liabilitiesc over 5d window."""
    res = _drawdown(liabilitiesc, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_liquidity_coverage_assets_dd_5d_v135_signal(assets):
    """Drawdown of Raw level of assets over 5d window."""
    res = _drawdown(assets, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_liquidity_coverage_quick_ratio_fin_dd_5d_v136_signal(cashneq, liabilitiesc):
    """Drawdown of Quick liquidity ratio over 5d window."""
    res = _drawdown(_ratio(cashneq, liabilitiesc), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_liquidity_coverage_cashneq_dd_10d_v137_signal(cashneq):
    """Drawdown of Raw level of cashneq over 10d window."""
    res = _drawdown(cashneq, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_liquidity_coverage_liabilitiesc_dd_10d_v138_signal(liabilitiesc):
    """Drawdown of Raw level of liabilitiesc over 10d window."""
    res = _drawdown(liabilitiesc, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_liquidity_coverage_assets_dd_10d_v139_signal(assets):
    """Drawdown of Raw level of assets over 10d window."""
    res = _drawdown(assets, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_liquidity_coverage_quick_ratio_fin_dd_10d_v140_signal(cashneq, liabilitiesc):
    """Drawdown of Quick liquidity ratio over 10d window."""
    res = _drawdown(_ratio(cashneq, liabilitiesc), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_liquidity_coverage_cashneq_dd_21d_v141_signal(cashneq):
    """Drawdown of Raw level of cashneq over 21d window."""
    res = _drawdown(cashneq, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_liquidity_coverage_liabilitiesc_dd_21d_v142_signal(liabilitiesc):
    """Drawdown of Raw level of liabilitiesc over 21d window."""
    res = _drawdown(liabilitiesc, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_liquidity_coverage_assets_dd_21d_v143_signal(assets):
    """Drawdown of Raw level of assets over 21d window."""
    res = _drawdown(assets, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_liquidity_coverage_quick_ratio_fin_dd_21d_v144_signal(cashneq, liabilitiesc):
    """Drawdown of Quick liquidity ratio over 21d window."""
    res = _drawdown(_ratio(cashneq, liabilitiesc), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_liquidity_coverage_cashneq_dd_42d_v145_signal(cashneq):
    """Drawdown of Raw level of cashneq over 42d window."""
    res = _drawdown(cashneq, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_liquidity_coverage_liabilitiesc_dd_42d_v146_signal(liabilitiesc):
    """Drawdown of Raw level of liabilitiesc over 42d window."""
    res = _drawdown(liabilitiesc, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_liquidity_coverage_assets_dd_42d_v147_signal(assets):
    """Drawdown of Raw level of assets over 42d window."""
    res = _drawdown(assets, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_liquidity_coverage_quick_ratio_fin_dd_42d_v148_signal(cashneq, liabilitiesc):
    """Drawdown of Quick liquidity ratio over 42d window."""
    res = _drawdown(_ratio(cashneq, liabilitiesc), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_liquidity_coverage_cashneq_dd_63d_v149_signal(cashneq):
    """Drawdown of Raw level of cashneq over 63d window."""
    res = _drawdown(cashneq, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_liquidity_coverage_liabilitiesc_dd_63d_v150_signal(liabilitiesc):
    """Drawdown of Raw level of liabilitiesc over 63d window."""
    res = _drawdown(liabilitiesc, 63)
    return res.replace([np.inf, -np.inf], np.nan)


# ===== Feature Registry =====
REGISTRY = {
    "f34_liquidity_coverage_quick_ratio_fin_ewma_504d_v076_signal": {"func": f34_liquidity_coverage_quick_ratio_fin_ewma_504d_v076_signal},
    "f34_liquidity_coverage_cashneq_ewma_756d_v077_signal": {"func": f34_liquidity_coverage_cashneq_ewma_756d_v077_signal},
    "f34_liquidity_coverage_liabilitiesc_ewma_756d_v078_signal": {"func": f34_liquidity_coverage_liabilitiesc_ewma_756d_v078_signal},
    "f34_liquidity_coverage_assets_ewma_756d_v079_signal": {"func": f34_liquidity_coverage_assets_ewma_756d_v079_signal},
    "f34_liquidity_coverage_quick_ratio_fin_ewma_756d_v080_signal": {"func": f34_liquidity_coverage_quick_ratio_fin_ewma_756d_v080_signal},
    "f34_liquidity_coverage_cashneq_ewma_1008d_v081_signal": {"func": f34_liquidity_coverage_cashneq_ewma_1008d_v081_signal},
    "f34_liquidity_coverage_liabilitiesc_ewma_1008d_v082_signal": {"func": f34_liquidity_coverage_liabilitiesc_ewma_1008d_v082_signal},
    "f34_liquidity_coverage_assets_ewma_1008d_v083_signal": {"func": f34_liquidity_coverage_assets_ewma_1008d_v083_signal},
    "f34_liquidity_coverage_quick_ratio_fin_ewma_1008d_v084_signal": {"func": f34_liquidity_coverage_quick_ratio_fin_ewma_1008d_v084_signal},
    "f34_liquidity_coverage_cashneq_ewma_1260d_v085_signal": {"func": f34_liquidity_coverage_cashneq_ewma_1260d_v085_signal},
    "f34_liquidity_coverage_liabilitiesc_ewma_1260d_v086_signal": {"func": f34_liquidity_coverage_liabilitiesc_ewma_1260d_v086_signal},
    "f34_liquidity_coverage_assets_ewma_1260d_v087_signal": {"func": f34_liquidity_coverage_assets_ewma_1260d_v087_signal},
    "f34_liquidity_coverage_quick_ratio_fin_ewma_1260d_v088_signal": {"func": f34_liquidity_coverage_quick_ratio_fin_ewma_1260d_v088_signal},
    "f34_liquidity_coverage_cashneq_z_5d_v089_signal": {"func": f34_liquidity_coverage_cashneq_z_5d_v089_signal},
    "f34_liquidity_coverage_liabilitiesc_z_5d_v090_signal": {"func": f34_liquidity_coverage_liabilitiesc_z_5d_v090_signal},
    "f34_liquidity_coverage_assets_z_5d_v091_signal": {"func": f34_liquidity_coverage_assets_z_5d_v091_signal},
    "f34_liquidity_coverage_quick_ratio_fin_z_5d_v092_signal": {"func": f34_liquidity_coverage_quick_ratio_fin_z_5d_v092_signal},
    "f34_liquidity_coverage_cashneq_z_10d_v093_signal": {"func": f34_liquidity_coverage_cashneq_z_10d_v093_signal},
    "f34_liquidity_coverage_liabilitiesc_z_10d_v094_signal": {"func": f34_liquidity_coverage_liabilitiesc_z_10d_v094_signal},
    "f34_liquidity_coverage_assets_z_10d_v095_signal": {"func": f34_liquidity_coverage_assets_z_10d_v095_signal},
    "f34_liquidity_coverage_quick_ratio_fin_z_10d_v096_signal": {"func": f34_liquidity_coverage_quick_ratio_fin_z_10d_v096_signal},
    "f34_liquidity_coverage_cashneq_z_21d_v097_signal": {"func": f34_liquidity_coverage_cashneq_z_21d_v097_signal},
    "f34_liquidity_coverage_liabilitiesc_z_21d_v098_signal": {"func": f34_liquidity_coverage_liabilitiesc_z_21d_v098_signal},
    "f34_liquidity_coverage_assets_z_21d_v099_signal": {"func": f34_liquidity_coverage_assets_z_21d_v099_signal},
    "f34_liquidity_coverage_quick_ratio_fin_z_21d_v100_signal": {"func": f34_liquidity_coverage_quick_ratio_fin_z_21d_v100_signal},
    "f34_liquidity_coverage_cashneq_z_42d_v101_signal": {"func": f34_liquidity_coverage_cashneq_z_42d_v101_signal},
    "f34_liquidity_coverage_liabilitiesc_z_42d_v102_signal": {"func": f34_liquidity_coverage_liabilitiesc_z_42d_v102_signal},
    "f34_liquidity_coverage_assets_z_42d_v103_signal": {"func": f34_liquidity_coverage_assets_z_42d_v103_signal},
    "f34_liquidity_coverage_quick_ratio_fin_z_42d_v104_signal": {"func": f34_liquidity_coverage_quick_ratio_fin_z_42d_v104_signal},
    "f34_liquidity_coverage_cashneq_z_63d_v105_signal": {"func": f34_liquidity_coverage_cashneq_z_63d_v105_signal},
    "f34_liquidity_coverage_liabilitiesc_z_63d_v106_signal": {"func": f34_liquidity_coverage_liabilitiesc_z_63d_v106_signal},
    "f34_liquidity_coverage_assets_z_63d_v107_signal": {"func": f34_liquidity_coverage_assets_z_63d_v107_signal},
    "f34_liquidity_coverage_quick_ratio_fin_z_63d_v108_signal": {"func": f34_liquidity_coverage_quick_ratio_fin_z_63d_v108_signal},
    "f34_liquidity_coverage_cashneq_z_126d_v109_signal": {"func": f34_liquidity_coverage_cashneq_z_126d_v109_signal},
    "f34_liquidity_coverage_liabilitiesc_z_126d_v110_signal": {"func": f34_liquidity_coverage_liabilitiesc_z_126d_v110_signal},
    "f34_liquidity_coverage_assets_z_126d_v111_signal": {"func": f34_liquidity_coverage_assets_z_126d_v111_signal},
    "f34_liquidity_coverage_quick_ratio_fin_z_126d_v112_signal": {"func": f34_liquidity_coverage_quick_ratio_fin_z_126d_v112_signal},
    "f34_liquidity_coverage_cashneq_z_252d_v113_signal": {"func": f34_liquidity_coverage_cashneq_z_252d_v113_signal},
    "f34_liquidity_coverage_liabilitiesc_z_252d_v114_signal": {"func": f34_liquidity_coverage_liabilitiesc_z_252d_v114_signal},
    "f34_liquidity_coverage_assets_z_252d_v115_signal": {"func": f34_liquidity_coverage_assets_z_252d_v115_signal},
    "f34_liquidity_coverage_quick_ratio_fin_z_252d_v116_signal": {"func": f34_liquidity_coverage_quick_ratio_fin_z_252d_v116_signal},
    "f34_liquidity_coverage_cashneq_z_504d_v117_signal": {"func": f34_liquidity_coverage_cashneq_z_504d_v117_signal},
    "f34_liquidity_coverage_liabilitiesc_z_504d_v118_signal": {"func": f34_liquidity_coverage_liabilitiesc_z_504d_v118_signal},
    "f34_liquidity_coverage_assets_z_504d_v119_signal": {"func": f34_liquidity_coverage_assets_z_504d_v119_signal},
    "f34_liquidity_coverage_quick_ratio_fin_z_504d_v120_signal": {"func": f34_liquidity_coverage_quick_ratio_fin_z_504d_v120_signal},
    "f34_liquidity_coverage_cashneq_z_756d_v121_signal": {"func": f34_liquidity_coverage_cashneq_z_756d_v121_signal},
    "f34_liquidity_coverage_liabilitiesc_z_756d_v122_signal": {"func": f34_liquidity_coverage_liabilitiesc_z_756d_v122_signal},
    "f34_liquidity_coverage_assets_z_756d_v123_signal": {"func": f34_liquidity_coverage_assets_z_756d_v123_signal},
    "f34_liquidity_coverage_quick_ratio_fin_z_756d_v124_signal": {"func": f34_liquidity_coverage_quick_ratio_fin_z_756d_v124_signal},
    "f34_liquidity_coverage_cashneq_z_1008d_v125_signal": {"func": f34_liquidity_coverage_cashneq_z_1008d_v125_signal},
    "f34_liquidity_coverage_liabilitiesc_z_1008d_v126_signal": {"func": f34_liquidity_coverage_liabilitiesc_z_1008d_v126_signal},
    "f34_liquidity_coverage_assets_z_1008d_v127_signal": {"func": f34_liquidity_coverage_assets_z_1008d_v127_signal},
    "f34_liquidity_coverage_quick_ratio_fin_z_1008d_v128_signal": {"func": f34_liquidity_coverage_quick_ratio_fin_z_1008d_v128_signal},
    "f34_liquidity_coverage_cashneq_z_1260d_v129_signal": {"func": f34_liquidity_coverage_cashneq_z_1260d_v129_signal},
    "f34_liquidity_coverage_liabilitiesc_z_1260d_v130_signal": {"func": f34_liquidity_coverage_liabilitiesc_z_1260d_v130_signal},
    "f34_liquidity_coverage_assets_z_1260d_v131_signal": {"func": f34_liquidity_coverage_assets_z_1260d_v131_signal},
    "f34_liquidity_coverage_quick_ratio_fin_z_1260d_v132_signal": {"func": f34_liquidity_coverage_quick_ratio_fin_z_1260d_v132_signal},
    "f34_liquidity_coverage_cashneq_dd_5d_v133_signal": {"func": f34_liquidity_coverage_cashneq_dd_5d_v133_signal},
    "f34_liquidity_coverage_liabilitiesc_dd_5d_v134_signal": {"func": f34_liquidity_coverage_liabilitiesc_dd_5d_v134_signal},
    "f34_liquidity_coverage_assets_dd_5d_v135_signal": {"func": f34_liquidity_coverage_assets_dd_5d_v135_signal},
    "f34_liquidity_coverage_quick_ratio_fin_dd_5d_v136_signal": {"func": f34_liquidity_coverage_quick_ratio_fin_dd_5d_v136_signal},
    "f34_liquidity_coverage_cashneq_dd_10d_v137_signal": {"func": f34_liquidity_coverage_cashneq_dd_10d_v137_signal},
    "f34_liquidity_coverage_liabilitiesc_dd_10d_v138_signal": {"func": f34_liquidity_coverage_liabilitiesc_dd_10d_v138_signal},
    "f34_liquidity_coverage_assets_dd_10d_v139_signal": {"func": f34_liquidity_coverage_assets_dd_10d_v139_signal},
    "f34_liquidity_coverage_quick_ratio_fin_dd_10d_v140_signal": {"func": f34_liquidity_coverage_quick_ratio_fin_dd_10d_v140_signal},
    "f34_liquidity_coverage_cashneq_dd_21d_v141_signal": {"func": f34_liquidity_coverage_cashneq_dd_21d_v141_signal},
    "f34_liquidity_coverage_liabilitiesc_dd_21d_v142_signal": {"func": f34_liquidity_coverage_liabilitiesc_dd_21d_v142_signal},
    "f34_liquidity_coverage_assets_dd_21d_v143_signal": {"func": f34_liquidity_coverage_assets_dd_21d_v143_signal},
    "f34_liquidity_coverage_quick_ratio_fin_dd_21d_v144_signal": {"func": f34_liquidity_coverage_quick_ratio_fin_dd_21d_v144_signal},
    "f34_liquidity_coverage_cashneq_dd_42d_v145_signal": {"func": f34_liquidity_coverage_cashneq_dd_42d_v145_signal},
    "f34_liquidity_coverage_liabilitiesc_dd_42d_v146_signal": {"func": f34_liquidity_coverage_liabilitiesc_dd_42d_v146_signal},
    "f34_liquidity_coverage_assets_dd_42d_v147_signal": {"func": f34_liquidity_coverage_assets_dd_42d_v147_signal},
    "f34_liquidity_coverage_quick_ratio_fin_dd_42d_v148_signal": {"func": f34_liquidity_coverage_quick_ratio_fin_dd_42d_v148_signal},
    "f34_liquidity_coverage_cashneq_dd_63d_v149_signal": {"func": f34_liquidity_coverage_cashneq_dd_63d_v149_signal},
    "f34_liquidity_coverage_liabilitiesc_dd_63d_v150_signal": {"func": f34_liquidity_coverage_liabilitiesc_dd_63d_v150_signal},
}

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "deferredrev": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "equity": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "deposits": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "divyield": np.random.normal(100, 10, n).cumsum(), "bvps": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "tangibles": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "grossmargin": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "liabilitiesc": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum()
    })
    print(f"Verifying {len(REGISTRY)} functions for family 34...")
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
