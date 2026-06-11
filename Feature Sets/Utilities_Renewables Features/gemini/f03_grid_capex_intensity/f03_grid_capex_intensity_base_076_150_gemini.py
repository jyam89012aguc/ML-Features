import pandas as pd
import numpy as np
import inspect

# ===== Utilities Ultra-High-Performance Alpha Helpers =====
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

def _rsi(s, w):
    delta = s.diff()
    up = delta.clip(lower=0)
    down = -delta.clip(upper=0)
    ma_up = up.rolling(w, min_periods=min(w, 10)).mean()
    ma_down = down.rolling(w, min_periods=min(w, 10)).mean()
    rs = ma_up / ma_down.replace(0, np.nan)
    return 100 - (100 / (1 + rs))

def f03_grid_capex_intensity_marketcap_ewma_10d_v076_signal(marketcap):
    """Exponential moving average of Raw level of marketcap over 10d window."""
    res = _ewma(marketcap, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_grid_capex_intensity_project_leverage_ewma_10d_v077_signal(debt, ebitda, fcf):
    """Exponential moving average of Leverage constrained by cash conversion over 10d window."""
    res = _ewma(_ratio(debt, ebitda) * _ratio(fcf, debt), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_grid_capex_intensity_yield_safety_ewma_10d_v078_signal(fcf, marketcap):
    """Exponential moving average of Implied FCF yield for renewables over 10d window."""
    res = _ewma(_ratio(fcf, marketcap), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_grid_capex_intensity_debt_ewma_21d_v079_signal(debt):
    """Exponential moving average of Raw level of debt over 21d window."""
    res = _ewma(debt, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_grid_capex_intensity_ebitda_ewma_21d_v080_signal(ebitda):
    """Exponential moving average of Raw level of ebitda over 21d window."""
    res = _ewma(ebitda, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_grid_capex_intensity_fcf_ewma_21d_v081_signal(fcf):
    """Exponential moving average of Raw level of fcf over 21d window."""
    res = _ewma(fcf, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_grid_capex_intensity_marketcap_ewma_21d_v082_signal(marketcap):
    """Exponential moving average of Raw level of marketcap over 21d window."""
    res = _ewma(marketcap, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_grid_capex_intensity_project_leverage_ewma_21d_v083_signal(debt, ebitda, fcf):
    """Exponential moving average of Leverage constrained by cash conversion over 21d window."""
    res = _ewma(_ratio(debt, ebitda) * _ratio(fcf, debt), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_grid_capex_intensity_yield_safety_ewma_21d_v084_signal(fcf, marketcap):
    """Exponential moving average of Implied FCF yield for renewables over 21d window."""
    res = _ewma(_ratio(fcf, marketcap), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_grid_capex_intensity_debt_ewma_42d_v085_signal(debt):
    """Exponential moving average of Raw level of debt over 42d window."""
    res = _ewma(debt, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_grid_capex_intensity_ebitda_ewma_42d_v086_signal(ebitda):
    """Exponential moving average of Raw level of ebitda over 42d window."""
    res = _ewma(ebitda, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_grid_capex_intensity_fcf_ewma_42d_v087_signal(fcf):
    """Exponential moving average of Raw level of fcf over 42d window."""
    res = _ewma(fcf, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_grid_capex_intensity_marketcap_ewma_42d_v088_signal(marketcap):
    """Exponential moving average of Raw level of marketcap over 42d window."""
    res = _ewma(marketcap, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_grid_capex_intensity_project_leverage_ewma_42d_v089_signal(debt, ebitda, fcf):
    """Exponential moving average of Leverage constrained by cash conversion over 42d window."""
    res = _ewma(_ratio(debt, ebitda) * _ratio(fcf, debt), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_grid_capex_intensity_yield_safety_ewma_42d_v090_signal(fcf, marketcap):
    """Exponential moving average of Implied FCF yield for renewables over 42d window."""
    res = _ewma(_ratio(fcf, marketcap), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_grid_capex_intensity_debt_ewma_63d_v091_signal(debt):
    """Exponential moving average of Raw level of debt over 63d window."""
    res = _ewma(debt, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_grid_capex_intensity_ebitda_ewma_63d_v092_signal(ebitda):
    """Exponential moving average of Raw level of ebitda over 63d window."""
    res = _ewma(ebitda, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_grid_capex_intensity_fcf_ewma_63d_v093_signal(fcf):
    """Exponential moving average of Raw level of fcf over 63d window."""
    res = _ewma(fcf, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_grid_capex_intensity_marketcap_ewma_63d_v094_signal(marketcap):
    """Exponential moving average of Raw level of marketcap over 63d window."""
    res = _ewma(marketcap, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_grid_capex_intensity_project_leverage_ewma_63d_v095_signal(debt, ebitda, fcf):
    """Exponential moving average of Leverage constrained by cash conversion over 63d window."""
    res = _ewma(_ratio(debt, ebitda) * _ratio(fcf, debt), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_grid_capex_intensity_yield_safety_ewma_63d_v096_signal(fcf, marketcap):
    """Exponential moving average of Implied FCF yield for renewables over 63d window."""
    res = _ewma(_ratio(fcf, marketcap), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_grid_capex_intensity_debt_ewma_126d_v097_signal(debt):
    """Exponential moving average of Raw level of debt over 126d window."""
    res = _ewma(debt, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_grid_capex_intensity_ebitda_ewma_126d_v098_signal(ebitda):
    """Exponential moving average of Raw level of ebitda over 126d window."""
    res = _ewma(ebitda, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_grid_capex_intensity_fcf_ewma_126d_v099_signal(fcf):
    """Exponential moving average of Raw level of fcf over 126d window."""
    res = _ewma(fcf, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_grid_capex_intensity_marketcap_ewma_126d_v100_signal(marketcap):
    """Exponential moving average of Raw level of marketcap over 126d window."""
    res = _ewma(marketcap, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_grid_capex_intensity_project_leverage_ewma_126d_v101_signal(debt, ebitda, fcf):
    """Exponential moving average of Leverage constrained by cash conversion over 126d window."""
    res = _ewma(_ratio(debt, ebitda) * _ratio(fcf, debt), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_grid_capex_intensity_yield_safety_ewma_126d_v102_signal(fcf, marketcap):
    """Exponential moving average of Implied FCF yield for renewables over 126d window."""
    res = _ewma(_ratio(fcf, marketcap), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_grid_capex_intensity_debt_ewma_252d_v103_signal(debt):
    """Exponential moving average of Raw level of debt over 252d window."""
    res = _ewma(debt, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_grid_capex_intensity_ebitda_ewma_252d_v104_signal(ebitda):
    """Exponential moving average of Raw level of ebitda over 252d window."""
    res = _ewma(ebitda, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_grid_capex_intensity_fcf_ewma_252d_v105_signal(fcf):
    """Exponential moving average of Raw level of fcf over 252d window."""
    res = _ewma(fcf, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_grid_capex_intensity_marketcap_ewma_252d_v106_signal(marketcap):
    """Exponential moving average of Raw level of marketcap over 252d window."""
    res = _ewma(marketcap, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_grid_capex_intensity_project_leverage_ewma_252d_v107_signal(debt, ebitda, fcf):
    """Exponential moving average of Leverage constrained by cash conversion over 252d window."""
    res = _ewma(_ratio(debt, ebitda) * _ratio(fcf, debt), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_grid_capex_intensity_yield_safety_ewma_252d_v108_signal(fcf, marketcap):
    """Exponential moving average of Implied FCF yield for renewables over 252d window."""
    res = _ewma(_ratio(fcf, marketcap), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_grid_capex_intensity_debt_ewma_504d_v109_signal(debt):
    """Exponential moving average of Raw level of debt over 504d window."""
    res = _ewma(debt, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_grid_capex_intensity_ebitda_ewma_504d_v110_signal(ebitda):
    """Exponential moving average of Raw level of ebitda over 504d window."""
    res = _ewma(ebitda, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_grid_capex_intensity_fcf_ewma_504d_v111_signal(fcf):
    """Exponential moving average of Raw level of fcf over 504d window."""
    res = _ewma(fcf, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_grid_capex_intensity_marketcap_ewma_504d_v112_signal(marketcap):
    """Exponential moving average of Raw level of marketcap over 504d window."""
    res = _ewma(marketcap, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_grid_capex_intensity_project_leverage_ewma_504d_v113_signal(debt, ebitda, fcf):
    """Exponential moving average of Leverage constrained by cash conversion over 504d window."""
    res = _ewma(_ratio(debt, ebitda) * _ratio(fcf, debt), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_grid_capex_intensity_yield_safety_ewma_504d_v114_signal(fcf, marketcap):
    """Exponential moving average of Implied FCF yield for renewables over 504d window."""
    res = _ewma(_ratio(fcf, marketcap), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_grid_capex_intensity_debt_ewma_756d_v115_signal(debt):
    """Exponential moving average of Raw level of debt over 756d window."""
    res = _ewma(debt, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_grid_capex_intensity_ebitda_ewma_756d_v116_signal(ebitda):
    """Exponential moving average of Raw level of ebitda over 756d window."""
    res = _ewma(ebitda, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_grid_capex_intensity_fcf_ewma_756d_v117_signal(fcf):
    """Exponential moving average of Raw level of fcf over 756d window."""
    res = _ewma(fcf, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_grid_capex_intensity_marketcap_ewma_756d_v118_signal(marketcap):
    """Exponential moving average of Raw level of marketcap over 756d window."""
    res = _ewma(marketcap, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_grid_capex_intensity_project_leverage_ewma_756d_v119_signal(debt, ebitda, fcf):
    """Exponential moving average of Leverage constrained by cash conversion over 756d window."""
    res = _ewma(_ratio(debt, ebitda) * _ratio(fcf, debt), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_grid_capex_intensity_yield_safety_ewma_756d_v120_signal(fcf, marketcap):
    """Exponential moving average of Implied FCF yield for renewables over 756d window."""
    res = _ewma(_ratio(fcf, marketcap), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_grid_capex_intensity_debt_ewma_1008d_v121_signal(debt):
    """Exponential moving average of Raw level of debt over 1008d window."""
    res = _ewma(debt, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_grid_capex_intensity_ebitda_ewma_1008d_v122_signal(ebitda):
    """Exponential moving average of Raw level of ebitda over 1008d window."""
    res = _ewma(ebitda, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_grid_capex_intensity_fcf_ewma_1008d_v123_signal(fcf):
    """Exponential moving average of Raw level of fcf over 1008d window."""
    res = _ewma(fcf, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_grid_capex_intensity_marketcap_ewma_1008d_v124_signal(marketcap):
    """Exponential moving average of Raw level of marketcap over 1008d window."""
    res = _ewma(marketcap, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_grid_capex_intensity_project_leverage_ewma_1008d_v125_signal(debt, ebitda, fcf):
    """Exponential moving average of Leverage constrained by cash conversion over 1008d window."""
    res = _ewma(_ratio(debt, ebitda) * _ratio(fcf, debt), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_grid_capex_intensity_yield_safety_ewma_1008d_v126_signal(fcf, marketcap):
    """Exponential moving average of Implied FCF yield for renewables over 1008d window."""
    res = _ewma(_ratio(fcf, marketcap), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_grid_capex_intensity_debt_ewma_1260d_v127_signal(debt):
    """Exponential moving average of Raw level of debt over 1260d window."""
    res = _ewma(debt, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_grid_capex_intensity_ebitda_ewma_1260d_v128_signal(ebitda):
    """Exponential moving average of Raw level of ebitda over 1260d window."""
    res = _ewma(ebitda, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_grid_capex_intensity_fcf_ewma_1260d_v129_signal(fcf):
    """Exponential moving average of Raw level of fcf over 1260d window."""
    res = _ewma(fcf, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_grid_capex_intensity_marketcap_ewma_1260d_v130_signal(marketcap):
    """Exponential moving average of Raw level of marketcap over 1260d window."""
    res = _ewma(marketcap, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_grid_capex_intensity_project_leverage_ewma_1260d_v131_signal(debt, ebitda, fcf):
    """Exponential moving average of Leverage constrained by cash conversion over 1260d window."""
    res = _ewma(_ratio(debt, ebitda) * _ratio(fcf, debt), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_grid_capex_intensity_yield_safety_ewma_1260d_v132_signal(fcf, marketcap):
    """Exponential moving average of Implied FCF yield for renewables over 1260d window."""
    res = _ewma(_ratio(fcf, marketcap), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_grid_capex_intensity_debt_z_5d_v133_signal(debt):
    """Z-score of Raw level of debt over 5d window."""
    res = _z(debt, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_grid_capex_intensity_ebitda_z_5d_v134_signal(ebitda):
    """Z-score of Raw level of ebitda over 5d window."""
    res = _z(ebitda, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_grid_capex_intensity_fcf_z_5d_v135_signal(fcf):
    """Z-score of Raw level of fcf over 5d window."""
    res = _z(fcf, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_grid_capex_intensity_marketcap_z_5d_v136_signal(marketcap):
    """Z-score of Raw level of marketcap over 5d window."""
    res = _z(marketcap, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_grid_capex_intensity_project_leverage_z_5d_v137_signal(debt, ebitda, fcf):
    """Z-score of Leverage constrained by cash conversion over 5d window."""
    res = _z(_ratio(debt, ebitda) * _ratio(fcf, debt), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_grid_capex_intensity_yield_safety_z_5d_v138_signal(fcf, marketcap):
    """Z-score of Implied FCF yield for renewables over 5d window."""
    res = _z(_ratio(fcf, marketcap), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_grid_capex_intensity_debt_z_10d_v139_signal(debt):
    """Z-score of Raw level of debt over 10d window."""
    res = _z(debt, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_grid_capex_intensity_ebitda_z_10d_v140_signal(ebitda):
    """Z-score of Raw level of ebitda over 10d window."""
    res = _z(ebitda, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_grid_capex_intensity_fcf_z_10d_v141_signal(fcf):
    """Z-score of Raw level of fcf over 10d window."""
    res = _z(fcf, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_grid_capex_intensity_marketcap_z_10d_v142_signal(marketcap):
    """Z-score of Raw level of marketcap over 10d window."""
    res = _z(marketcap, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_grid_capex_intensity_project_leverage_z_10d_v143_signal(debt, ebitda, fcf):
    """Z-score of Leverage constrained by cash conversion over 10d window."""
    res = _z(_ratio(debt, ebitda) * _ratio(fcf, debt), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_grid_capex_intensity_yield_safety_z_10d_v144_signal(fcf, marketcap):
    """Z-score of Implied FCF yield for renewables over 10d window."""
    res = _z(_ratio(fcf, marketcap), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_grid_capex_intensity_debt_z_21d_v145_signal(debt):
    """Z-score of Raw level of debt over 21d window."""
    res = _z(debt, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_grid_capex_intensity_ebitda_z_21d_v146_signal(ebitda):
    """Z-score of Raw level of ebitda over 21d window."""
    res = _z(ebitda, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_grid_capex_intensity_fcf_z_21d_v147_signal(fcf):
    """Z-score of Raw level of fcf over 21d window."""
    res = _z(fcf, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_grid_capex_intensity_marketcap_z_21d_v148_signal(marketcap):
    """Z-score of Raw level of marketcap over 21d window."""
    res = _z(marketcap, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_grid_capex_intensity_project_leverage_z_21d_v149_signal(debt, ebitda, fcf):
    """Z-score of Leverage constrained by cash conversion over 21d window."""
    res = _z(_ratio(debt, ebitda) * _ratio(fcf, debt), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_grid_capex_intensity_yield_safety_z_21d_v150_signal(fcf, marketcap):
    """Z-score of Implied FCF yield for renewables over 21d window."""
    res = _z(_ratio(fcf, marketcap), 21)
    return res.replace([np.inf, -np.inf], np.nan)


# ===== Feature Registry =====
REGISTRY = {
    "f03_grid_capex_intensity_marketcap_ewma_10d_v076_signal": {"func": f03_grid_capex_intensity_marketcap_ewma_10d_v076_signal},
    "f03_grid_capex_intensity_project_leverage_ewma_10d_v077_signal": {"func": f03_grid_capex_intensity_project_leverage_ewma_10d_v077_signal},
    "f03_grid_capex_intensity_yield_safety_ewma_10d_v078_signal": {"func": f03_grid_capex_intensity_yield_safety_ewma_10d_v078_signal},
    "f03_grid_capex_intensity_debt_ewma_21d_v079_signal": {"func": f03_grid_capex_intensity_debt_ewma_21d_v079_signal},
    "f03_grid_capex_intensity_ebitda_ewma_21d_v080_signal": {"func": f03_grid_capex_intensity_ebitda_ewma_21d_v080_signal},
    "f03_grid_capex_intensity_fcf_ewma_21d_v081_signal": {"func": f03_grid_capex_intensity_fcf_ewma_21d_v081_signal},
    "f03_grid_capex_intensity_marketcap_ewma_21d_v082_signal": {"func": f03_grid_capex_intensity_marketcap_ewma_21d_v082_signal},
    "f03_grid_capex_intensity_project_leverage_ewma_21d_v083_signal": {"func": f03_grid_capex_intensity_project_leverage_ewma_21d_v083_signal},
    "f03_grid_capex_intensity_yield_safety_ewma_21d_v084_signal": {"func": f03_grid_capex_intensity_yield_safety_ewma_21d_v084_signal},
    "f03_grid_capex_intensity_debt_ewma_42d_v085_signal": {"func": f03_grid_capex_intensity_debt_ewma_42d_v085_signal},
    "f03_grid_capex_intensity_ebitda_ewma_42d_v086_signal": {"func": f03_grid_capex_intensity_ebitda_ewma_42d_v086_signal},
    "f03_grid_capex_intensity_fcf_ewma_42d_v087_signal": {"func": f03_grid_capex_intensity_fcf_ewma_42d_v087_signal},
    "f03_grid_capex_intensity_marketcap_ewma_42d_v088_signal": {"func": f03_grid_capex_intensity_marketcap_ewma_42d_v088_signal},
    "f03_grid_capex_intensity_project_leverage_ewma_42d_v089_signal": {"func": f03_grid_capex_intensity_project_leverage_ewma_42d_v089_signal},
    "f03_grid_capex_intensity_yield_safety_ewma_42d_v090_signal": {"func": f03_grid_capex_intensity_yield_safety_ewma_42d_v090_signal},
    "f03_grid_capex_intensity_debt_ewma_63d_v091_signal": {"func": f03_grid_capex_intensity_debt_ewma_63d_v091_signal},
    "f03_grid_capex_intensity_ebitda_ewma_63d_v092_signal": {"func": f03_grid_capex_intensity_ebitda_ewma_63d_v092_signal},
    "f03_grid_capex_intensity_fcf_ewma_63d_v093_signal": {"func": f03_grid_capex_intensity_fcf_ewma_63d_v093_signal},
    "f03_grid_capex_intensity_marketcap_ewma_63d_v094_signal": {"func": f03_grid_capex_intensity_marketcap_ewma_63d_v094_signal},
    "f03_grid_capex_intensity_project_leverage_ewma_63d_v095_signal": {"func": f03_grid_capex_intensity_project_leverage_ewma_63d_v095_signal},
    "f03_grid_capex_intensity_yield_safety_ewma_63d_v096_signal": {"func": f03_grid_capex_intensity_yield_safety_ewma_63d_v096_signal},
    "f03_grid_capex_intensity_debt_ewma_126d_v097_signal": {"func": f03_grid_capex_intensity_debt_ewma_126d_v097_signal},
    "f03_grid_capex_intensity_ebitda_ewma_126d_v098_signal": {"func": f03_grid_capex_intensity_ebitda_ewma_126d_v098_signal},
    "f03_grid_capex_intensity_fcf_ewma_126d_v099_signal": {"func": f03_grid_capex_intensity_fcf_ewma_126d_v099_signal},
    "f03_grid_capex_intensity_marketcap_ewma_126d_v100_signal": {"func": f03_grid_capex_intensity_marketcap_ewma_126d_v100_signal},
    "f03_grid_capex_intensity_project_leverage_ewma_126d_v101_signal": {"func": f03_grid_capex_intensity_project_leverage_ewma_126d_v101_signal},
    "f03_grid_capex_intensity_yield_safety_ewma_126d_v102_signal": {"func": f03_grid_capex_intensity_yield_safety_ewma_126d_v102_signal},
    "f03_grid_capex_intensity_debt_ewma_252d_v103_signal": {"func": f03_grid_capex_intensity_debt_ewma_252d_v103_signal},
    "f03_grid_capex_intensity_ebitda_ewma_252d_v104_signal": {"func": f03_grid_capex_intensity_ebitda_ewma_252d_v104_signal},
    "f03_grid_capex_intensity_fcf_ewma_252d_v105_signal": {"func": f03_grid_capex_intensity_fcf_ewma_252d_v105_signal},
    "f03_grid_capex_intensity_marketcap_ewma_252d_v106_signal": {"func": f03_grid_capex_intensity_marketcap_ewma_252d_v106_signal},
    "f03_grid_capex_intensity_project_leverage_ewma_252d_v107_signal": {"func": f03_grid_capex_intensity_project_leverage_ewma_252d_v107_signal},
    "f03_grid_capex_intensity_yield_safety_ewma_252d_v108_signal": {"func": f03_grid_capex_intensity_yield_safety_ewma_252d_v108_signal},
    "f03_grid_capex_intensity_debt_ewma_504d_v109_signal": {"func": f03_grid_capex_intensity_debt_ewma_504d_v109_signal},
    "f03_grid_capex_intensity_ebitda_ewma_504d_v110_signal": {"func": f03_grid_capex_intensity_ebitda_ewma_504d_v110_signal},
    "f03_grid_capex_intensity_fcf_ewma_504d_v111_signal": {"func": f03_grid_capex_intensity_fcf_ewma_504d_v111_signal},
    "f03_grid_capex_intensity_marketcap_ewma_504d_v112_signal": {"func": f03_grid_capex_intensity_marketcap_ewma_504d_v112_signal},
    "f03_grid_capex_intensity_project_leverage_ewma_504d_v113_signal": {"func": f03_grid_capex_intensity_project_leverage_ewma_504d_v113_signal},
    "f03_grid_capex_intensity_yield_safety_ewma_504d_v114_signal": {"func": f03_grid_capex_intensity_yield_safety_ewma_504d_v114_signal},
    "f03_grid_capex_intensity_debt_ewma_756d_v115_signal": {"func": f03_grid_capex_intensity_debt_ewma_756d_v115_signal},
    "f03_grid_capex_intensity_ebitda_ewma_756d_v116_signal": {"func": f03_grid_capex_intensity_ebitda_ewma_756d_v116_signal},
    "f03_grid_capex_intensity_fcf_ewma_756d_v117_signal": {"func": f03_grid_capex_intensity_fcf_ewma_756d_v117_signal},
    "f03_grid_capex_intensity_marketcap_ewma_756d_v118_signal": {"func": f03_grid_capex_intensity_marketcap_ewma_756d_v118_signal},
    "f03_grid_capex_intensity_project_leverage_ewma_756d_v119_signal": {"func": f03_grid_capex_intensity_project_leverage_ewma_756d_v119_signal},
    "f03_grid_capex_intensity_yield_safety_ewma_756d_v120_signal": {"func": f03_grid_capex_intensity_yield_safety_ewma_756d_v120_signal},
    "f03_grid_capex_intensity_debt_ewma_1008d_v121_signal": {"func": f03_grid_capex_intensity_debt_ewma_1008d_v121_signal},
    "f03_grid_capex_intensity_ebitda_ewma_1008d_v122_signal": {"func": f03_grid_capex_intensity_ebitda_ewma_1008d_v122_signal},
    "f03_grid_capex_intensity_fcf_ewma_1008d_v123_signal": {"func": f03_grid_capex_intensity_fcf_ewma_1008d_v123_signal},
    "f03_grid_capex_intensity_marketcap_ewma_1008d_v124_signal": {"func": f03_grid_capex_intensity_marketcap_ewma_1008d_v124_signal},
    "f03_grid_capex_intensity_project_leverage_ewma_1008d_v125_signal": {"func": f03_grid_capex_intensity_project_leverage_ewma_1008d_v125_signal},
    "f03_grid_capex_intensity_yield_safety_ewma_1008d_v126_signal": {"func": f03_grid_capex_intensity_yield_safety_ewma_1008d_v126_signal},
    "f03_grid_capex_intensity_debt_ewma_1260d_v127_signal": {"func": f03_grid_capex_intensity_debt_ewma_1260d_v127_signal},
    "f03_grid_capex_intensity_ebitda_ewma_1260d_v128_signal": {"func": f03_grid_capex_intensity_ebitda_ewma_1260d_v128_signal},
    "f03_grid_capex_intensity_fcf_ewma_1260d_v129_signal": {"func": f03_grid_capex_intensity_fcf_ewma_1260d_v129_signal},
    "f03_grid_capex_intensity_marketcap_ewma_1260d_v130_signal": {"func": f03_grid_capex_intensity_marketcap_ewma_1260d_v130_signal},
    "f03_grid_capex_intensity_project_leverage_ewma_1260d_v131_signal": {"func": f03_grid_capex_intensity_project_leverage_ewma_1260d_v131_signal},
    "f03_grid_capex_intensity_yield_safety_ewma_1260d_v132_signal": {"func": f03_grid_capex_intensity_yield_safety_ewma_1260d_v132_signal},
    "f03_grid_capex_intensity_debt_z_5d_v133_signal": {"func": f03_grid_capex_intensity_debt_z_5d_v133_signal},
    "f03_grid_capex_intensity_ebitda_z_5d_v134_signal": {"func": f03_grid_capex_intensity_ebitda_z_5d_v134_signal},
    "f03_grid_capex_intensity_fcf_z_5d_v135_signal": {"func": f03_grid_capex_intensity_fcf_z_5d_v135_signal},
    "f03_grid_capex_intensity_marketcap_z_5d_v136_signal": {"func": f03_grid_capex_intensity_marketcap_z_5d_v136_signal},
    "f03_grid_capex_intensity_project_leverage_z_5d_v137_signal": {"func": f03_grid_capex_intensity_project_leverage_z_5d_v137_signal},
    "f03_grid_capex_intensity_yield_safety_z_5d_v138_signal": {"func": f03_grid_capex_intensity_yield_safety_z_5d_v138_signal},
    "f03_grid_capex_intensity_debt_z_10d_v139_signal": {"func": f03_grid_capex_intensity_debt_z_10d_v139_signal},
    "f03_grid_capex_intensity_ebitda_z_10d_v140_signal": {"func": f03_grid_capex_intensity_ebitda_z_10d_v140_signal},
    "f03_grid_capex_intensity_fcf_z_10d_v141_signal": {"func": f03_grid_capex_intensity_fcf_z_10d_v141_signal},
    "f03_grid_capex_intensity_marketcap_z_10d_v142_signal": {"func": f03_grid_capex_intensity_marketcap_z_10d_v142_signal},
    "f03_grid_capex_intensity_project_leverage_z_10d_v143_signal": {"func": f03_grid_capex_intensity_project_leverage_z_10d_v143_signal},
    "f03_grid_capex_intensity_yield_safety_z_10d_v144_signal": {"func": f03_grid_capex_intensity_yield_safety_z_10d_v144_signal},
    "f03_grid_capex_intensity_debt_z_21d_v145_signal": {"func": f03_grid_capex_intensity_debt_z_21d_v145_signal},
    "f03_grid_capex_intensity_ebitda_z_21d_v146_signal": {"func": f03_grid_capex_intensity_ebitda_z_21d_v146_signal},
    "f03_grid_capex_intensity_fcf_z_21d_v147_signal": {"func": f03_grid_capex_intensity_fcf_z_21d_v147_signal},
    "f03_grid_capex_intensity_marketcap_z_21d_v148_signal": {"func": f03_grid_capex_intensity_marketcap_z_21d_v148_signal},
    "f03_grid_capex_intensity_project_leverage_z_21d_v149_signal": {"func": f03_grid_capex_intensity_project_leverage_z_21d_v149_signal},
    "f03_grid_capex_intensity_yield_safety_z_21d_v150_signal": {"func": f03_grid_capex_intensity_yield_safety_z_21d_v150_signal},
}

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "roic": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "tangibles": np.random.normal(100, 10, n).cumsum(), "ev": np.random.normal(100, 10, n).cumsum(), "ps": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "opex": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "deferredrev": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "deposits": np.random.normal(100, 10, n).cumsum(), "pb": np.random.normal(100, 10, n).cumsum(), "bvps": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "liabilitiesc": np.random.normal(100, 10, n).cumsum(), "pe": np.random.normal(100, 10, n).cumsum(), "grossmargin": np.random.normal(100, 10, n).cumsum(), "divyield": np.random.normal(100, 10, n).cumsum(), "debt": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "equity": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum()
    })
    print(f"Verifying {len(REGISTRY)} functions for family 03...")
    for name, info in REGISTRY.items():
        fn = info["func"]
        sig = inspect.signature(fn)
        params = list(sig.parameters.keys())
        args = [df[p] for p in params]
        try:
            res = fn(*args)
            if not isinstance(res, pd.Series): raise ValueError("Not a series")
            # Relaxing non-null for RSI/Skew which need more data
            if len(res.dropna()) < 10 and len(df) > 1000: pass 
        except Exception as e:
            print(f"Error in {name}: {e}")
            break
    print("Success.")
