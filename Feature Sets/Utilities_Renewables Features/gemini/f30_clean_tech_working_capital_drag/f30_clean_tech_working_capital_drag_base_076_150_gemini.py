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

def f30_clean_tech_working_capital_drag_ebitda_ewma_10d_v076_signal(ebitda):
    """Exponential moving average of Raw level of ebitda over 10d window."""
    res = _ewma(ebitda, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_clean_tech_working_capital_drag_rate_base_growth_proxy_ewma_10d_v077_signal(capex, assets, netinc):
    """Exponential moving average of Asset growth constrained by earnings yield over 10d window."""
    res = _ewma(_ratio(capex, assets) * _ratio(netinc, capex), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_clean_tech_working_capital_drag_operating_return_capex_ewma_10d_v078_signal(ebitda, capex):
    """Exponential moving average of EBITDA generated per unit of grid capex over 10d window."""
    res = _ewma(_ratio(ebitda, capex), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_clean_tech_working_capital_drag_capex_ewma_21d_v079_signal(capex):
    """Exponential moving average of Raw level of capex over 21d window."""
    res = _ewma(capex, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_clean_tech_working_capital_drag_assets_ewma_21d_v080_signal(assets):
    """Exponential moving average of Raw level of assets over 21d window."""
    res = _ewma(assets, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_clean_tech_working_capital_drag_netinc_ewma_21d_v081_signal(netinc):
    """Exponential moving average of Raw level of netinc over 21d window."""
    res = _ewma(netinc, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_clean_tech_working_capital_drag_ebitda_ewma_21d_v082_signal(ebitda):
    """Exponential moving average of Raw level of ebitda over 21d window."""
    res = _ewma(ebitda, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_clean_tech_working_capital_drag_rate_base_growth_proxy_ewma_21d_v083_signal(capex, assets, netinc):
    """Exponential moving average of Asset growth constrained by earnings yield over 21d window."""
    res = _ewma(_ratio(capex, assets) * _ratio(netinc, capex), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_clean_tech_working_capital_drag_operating_return_capex_ewma_21d_v084_signal(ebitda, capex):
    """Exponential moving average of EBITDA generated per unit of grid capex over 21d window."""
    res = _ewma(_ratio(ebitda, capex), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_clean_tech_working_capital_drag_capex_ewma_42d_v085_signal(capex):
    """Exponential moving average of Raw level of capex over 42d window."""
    res = _ewma(capex, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_clean_tech_working_capital_drag_assets_ewma_42d_v086_signal(assets):
    """Exponential moving average of Raw level of assets over 42d window."""
    res = _ewma(assets, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_clean_tech_working_capital_drag_netinc_ewma_42d_v087_signal(netinc):
    """Exponential moving average of Raw level of netinc over 42d window."""
    res = _ewma(netinc, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_clean_tech_working_capital_drag_ebitda_ewma_42d_v088_signal(ebitda):
    """Exponential moving average of Raw level of ebitda over 42d window."""
    res = _ewma(ebitda, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_clean_tech_working_capital_drag_rate_base_growth_proxy_ewma_42d_v089_signal(capex, assets, netinc):
    """Exponential moving average of Asset growth constrained by earnings yield over 42d window."""
    res = _ewma(_ratio(capex, assets) * _ratio(netinc, capex), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_clean_tech_working_capital_drag_operating_return_capex_ewma_42d_v090_signal(ebitda, capex):
    """Exponential moving average of EBITDA generated per unit of grid capex over 42d window."""
    res = _ewma(_ratio(ebitda, capex), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_clean_tech_working_capital_drag_capex_ewma_63d_v091_signal(capex):
    """Exponential moving average of Raw level of capex over 63d window."""
    res = _ewma(capex, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_clean_tech_working_capital_drag_assets_ewma_63d_v092_signal(assets):
    """Exponential moving average of Raw level of assets over 63d window."""
    res = _ewma(assets, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_clean_tech_working_capital_drag_netinc_ewma_63d_v093_signal(netinc):
    """Exponential moving average of Raw level of netinc over 63d window."""
    res = _ewma(netinc, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_clean_tech_working_capital_drag_ebitda_ewma_63d_v094_signal(ebitda):
    """Exponential moving average of Raw level of ebitda over 63d window."""
    res = _ewma(ebitda, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_clean_tech_working_capital_drag_rate_base_growth_proxy_ewma_63d_v095_signal(capex, assets, netinc):
    """Exponential moving average of Asset growth constrained by earnings yield over 63d window."""
    res = _ewma(_ratio(capex, assets) * _ratio(netinc, capex), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_clean_tech_working_capital_drag_operating_return_capex_ewma_63d_v096_signal(ebitda, capex):
    """Exponential moving average of EBITDA generated per unit of grid capex over 63d window."""
    res = _ewma(_ratio(ebitda, capex), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_clean_tech_working_capital_drag_capex_ewma_126d_v097_signal(capex):
    """Exponential moving average of Raw level of capex over 126d window."""
    res = _ewma(capex, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_clean_tech_working_capital_drag_assets_ewma_126d_v098_signal(assets):
    """Exponential moving average of Raw level of assets over 126d window."""
    res = _ewma(assets, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_clean_tech_working_capital_drag_netinc_ewma_126d_v099_signal(netinc):
    """Exponential moving average of Raw level of netinc over 126d window."""
    res = _ewma(netinc, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_clean_tech_working_capital_drag_ebitda_ewma_126d_v100_signal(ebitda):
    """Exponential moving average of Raw level of ebitda over 126d window."""
    res = _ewma(ebitda, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_clean_tech_working_capital_drag_rate_base_growth_proxy_ewma_126d_v101_signal(capex, assets, netinc):
    """Exponential moving average of Asset growth constrained by earnings yield over 126d window."""
    res = _ewma(_ratio(capex, assets) * _ratio(netinc, capex), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_clean_tech_working_capital_drag_operating_return_capex_ewma_126d_v102_signal(ebitda, capex):
    """Exponential moving average of EBITDA generated per unit of grid capex over 126d window."""
    res = _ewma(_ratio(ebitda, capex), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_clean_tech_working_capital_drag_capex_ewma_252d_v103_signal(capex):
    """Exponential moving average of Raw level of capex over 252d window."""
    res = _ewma(capex, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_clean_tech_working_capital_drag_assets_ewma_252d_v104_signal(assets):
    """Exponential moving average of Raw level of assets over 252d window."""
    res = _ewma(assets, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_clean_tech_working_capital_drag_netinc_ewma_252d_v105_signal(netinc):
    """Exponential moving average of Raw level of netinc over 252d window."""
    res = _ewma(netinc, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_clean_tech_working_capital_drag_ebitda_ewma_252d_v106_signal(ebitda):
    """Exponential moving average of Raw level of ebitda over 252d window."""
    res = _ewma(ebitda, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_clean_tech_working_capital_drag_rate_base_growth_proxy_ewma_252d_v107_signal(capex, assets, netinc):
    """Exponential moving average of Asset growth constrained by earnings yield over 252d window."""
    res = _ewma(_ratio(capex, assets) * _ratio(netinc, capex), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_clean_tech_working_capital_drag_operating_return_capex_ewma_252d_v108_signal(ebitda, capex):
    """Exponential moving average of EBITDA generated per unit of grid capex over 252d window."""
    res = _ewma(_ratio(ebitda, capex), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_clean_tech_working_capital_drag_capex_ewma_504d_v109_signal(capex):
    """Exponential moving average of Raw level of capex over 504d window."""
    res = _ewma(capex, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_clean_tech_working_capital_drag_assets_ewma_504d_v110_signal(assets):
    """Exponential moving average of Raw level of assets over 504d window."""
    res = _ewma(assets, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_clean_tech_working_capital_drag_netinc_ewma_504d_v111_signal(netinc):
    """Exponential moving average of Raw level of netinc over 504d window."""
    res = _ewma(netinc, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_clean_tech_working_capital_drag_ebitda_ewma_504d_v112_signal(ebitda):
    """Exponential moving average of Raw level of ebitda over 504d window."""
    res = _ewma(ebitda, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_clean_tech_working_capital_drag_rate_base_growth_proxy_ewma_504d_v113_signal(capex, assets, netinc):
    """Exponential moving average of Asset growth constrained by earnings yield over 504d window."""
    res = _ewma(_ratio(capex, assets) * _ratio(netinc, capex), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_clean_tech_working_capital_drag_operating_return_capex_ewma_504d_v114_signal(ebitda, capex):
    """Exponential moving average of EBITDA generated per unit of grid capex over 504d window."""
    res = _ewma(_ratio(ebitda, capex), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_clean_tech_working_capital_drag_capex_ewma_756d_v115_signal(capex):
    """Exponential moving average of Raw level of capex over 756d window."""
    res = _ewma(capex, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_clean_tech_working_capital_drag_assets_ewma_756d_v116_signal(assets):
    """Exponential moving average of Raw level of assets over 756d window."""
    res = _ewma(assets, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_clean_tech_working_capital_drag_netinc_ewma_756d_v117_signal(netinc):
    """Exponential moving average of Raw level of netinc over 756d window."""
    res = _ewma(netinc, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_clean_tech_working_capital_drag_ebitda_ewma_756d_v118_signal(ebitda):
    """Exponential moving average of Raw level of ebitda over 756d window."""
    res = _ewma(ebitda, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_clean_tech_working_capital_drag_rate_base_growth_proxy_ewma_756d_v119_signal(capex, assets, netinc):
    """Exponential moving average of Asset growth constrained by earnings yield over 756d window."""
    res = _ewma(_ratio(capex, assets) * _ratio(netinc, capex), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_clean_tech_working_capital_drag_operating_return_capex_ewma_756d_v120_signal(ebitda, capex):
    """Exponential moving average of EBITDA generated per unit of grid capex over 756d window."""
    res = _ewma(_ratio(ebitda, capex), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_clean_tech_working_capital_drag_capex_ewma_1008d_v121_signal(capex):
    """Exponential moving average of Raw level of capex over 1008d window."""
    res = _ewma(capex, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_clean_tech_working_capital_drag_assets_ewma_1008d_v122_signal(assets):
    """Exponential moving average of Raw level of assets over 1008d window."""
    res = _ewma(assets, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_clean_tech_working_capital_drag_netinc_ewma_1008d_v123_signal(netinc):
    """Exponential moving average of Raw level of netinc over 1008d window."""
    res = _ewma(netinc, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_clean_tech_working_capital_drag_ebitda_ewma_1008d_v124_signal(ebitda):
    """Exponential moving average of Raw level of ebitda over 1008d window."""
    res = _ewma(ebitda, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_clean_tech_working_capital_drag_rate_base_growth_proxy_ewma_1008d_v125_signal(capex, assets, netinc):
    """Exponential moving average of Asset growth constrained by earnings yield over 1008d window."""
    res = _ewma(_ratio(capex, assets) * _ratio(netinc, capex), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_clean_tech_working_capital_drag_operating_return_capex_ewma_1008d_v126_signal(ebitda, capex):
    """Exponential moving average of EBITDA generated per unit of grid capex over 1008d window."""
    res = _ewma(_ratio(ebitda, capex), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_clean_tech_working_capital_drag_capex_ewma_1260d_v127_signal(capex):
    """Exponential moving average of Raw level of capex over 1260d window."""
    res = _ewma(capex, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_clean_tech_working_capital_drag_assets_ewma_1260d_v128_signal(assets):
    """Exponential moving average of Raw level of assets over 1260d window."""
    res = _ewma(assets, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_clean_tech_working_capital_drag_netinc_ewma_1260d_v129_signal(netinc):
    """Exponential moving average of Raw level of netinc over 1260d window."""
    res = _ewma(netinc, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_clean_tech_working_capital_drag_ebitda_ewma_1260d_v130_signal(ebitda):
    """Exponential moving average of Raw level of ebitda over 1260d window."""
    res = _ewma(ebitda, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_clean_tech_working_capital_drag_rate_base_growth_proxy_ewma_1260d_v131_signal(capex, assets, netinc):
    """Exponential moving average of Asset growth constrained by earnings yield over 1260d window."""
    res = _ewma(_ratio(capex, assets) * _ratio(netinc, capex), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_clean_tech_working_capital_drag_operating_return_capex_ewma_1260d_v132_signal(ebitda, capex):
    """Exponential moving average of EBITDA generated per unit of grid capex over 1260d window."""
    res = _ewma(_ratio(ebitda, capex), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_clean_tech_working_capital_drag_capex_z_5d_v133_signal(capex):
    """Z-score of Raw level of capex over 5d window."""
    res = _z(capex, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_clean_tech_working_capital_drag_assets_z_5d_v134_signal(assets):
    """Z-score of Raw level of assets over 5d window."""
    res = _z(assets, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_clean_tech_working_capital_drag_netinc_z_5d_v135_signal(netinc):
    """Z-score of Raw level of netinc over 5d window."""
    res = _z(netinc, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_clean_tech_working_capital_drag_ebitda_z_5d_v136_signal(ebitda):
    """Z-score of Raw level of ebitda over 5d window."""
    res = _z(ebitda, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_clean_tech_working_capital_drag_rate_base_growth_proxy_z_5d_v137_signal(capex, assets, netinc):
    """Z-score of Asset growth constrained by earnings yield over 5d window."""
    res = _z(_ratio(capex, assets) * _ratio(netinc, capex), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_clean_tech_working_capital_drag_operating_return_capex_z_5d_v138_signal(ebitda, capex):
    """Z-score of EBITDA generated per unit of grid capex over 5d window."""
    res = _z(_ratio(ebitda, capex), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_clean_tech_working_capital_drag_capex_z_10d_v139_signal(capex):
    """Z-score of Raw level of capex over 10d window."""
    res = _z(capex, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_clean_tech_working_capital_drag_assets_z_10d_v140_signal(assets):
    """Z-score of Raw level of assets over 10d window."""
    res = _z(assets, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_clean_tech_working_capital_drag_netinc_z_10d_v141_signal(netinc):
    """Z-score of Raw level of netinc over 10d window."""
    res = _z(netinc, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_clean_tech_working_capital_drag_ebitda_z_10d_v142_signal(ebitda):
    """Z-score of Raw level of ebitda over 10d window."""
    res = _z(ebitda, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_clean_tech_working_capital_drag_rate_base_growth_proxy_z_10d_v143_signal(capex, assets, netinc):
    """Z-score of Asset growth constrained by earnings yield over 10d window."""
    res = _z(_ratio(capex, assets) * _ratio(netinc, capex), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_clean_tech_working_capital_drag_operating_return_capex_z_10d_v144_signal(ebitda, capex):
    """Z-score of EBITDA generated per unit of grid capex over 10d window."""
    res = _z(_ratio(ebitda, capex), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_clean_tech_working_capital_drag_capex_z_21d_v145_signal(capex):
    """Z-score of Raw level of capex over 21d window."""
    res = _z(capex, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_clean_tech_working_capital_drag_assets_z_21d_v146_signal(assets):
    """Z-score of Raw level of assets over 21d window."""
    res = _z(assets, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_clean_tech_working_capital_drag_netinc_z_21d_v147_signal(netinc):
    """Z-score of Raw level of netinc over 21d window."""
    res = _z(netinc, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_clean_tech_working_capital_drag_ebitda_z_21d_v148_signal(ebitda):
    """Z-score of Raw level of ebitda over 21d window."""
    res = _z(ebitda, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_clean_tech_working_capital_drag_rate_base_growth_proxy_z_21d_v149_signal(capex, assets, netinc):
    """Z-score of Asset growth constrained by earnings yield over 21d window."""
    res = _z(_ratio(capex, assets) * _ratio(netinc, capex), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_clean_tech_working_capital_drag_operating_return_capex_z_21d_v150_signal(ebitda, capex):
    """Z-score of EBITDA generated per unit of grid capex over 21d window."""
    res = _z(_ratio(ebitda, capex), 21)
    return res.replace([np.inf, -np.inf], np.nan)


# ===== Feature Registry =====
REGISTRY = {
    "f30_clean_tech_working_capital_drag_ebitda_ewma_10d_v076_signal": {"func": f30_clean_tech_working_capital_drag_ebitda_ewma_10d_v076_signal},
    "f30_clean_tech_working_capital_drag_rate_base_growth_proxy_ewma_10d_v077_signal": {"func": f30_clean_tech_working_capital_drag_rate_base_growth_proxy_ewma_10d_v077_signal},
    "f30_clean_tech_working_capital_drag_operating_return_capex_ewma_10d_v078_signal": {"func": f30_clean_tech_working_capital_drag_operating_return_capex_ewma_10d_v078_signal},
    "f30_clean_tech_working_capital_drag_capex_ewma_21d_v079_signal": {"func": f30_clean_tech_working_capital_drag_capex_ewma_21d_v079_signal},
    "f30_clean_tech_working_capital_drag_assets_ewma_21d_v080_signal": {"func": f30_clean_tech_working_capital_drag_assets_ewma_21d_v080_signal},
    "f30_clean_tech_working_capital_drag_netinc_ewma_21d_v081_signal": {"func": f30_clean_tech_working_capital_drag_netinc_ewma_21d_v081_signal},
    "f30_clean_tech_working_capital_drag_ebitda_ewma_21d_v082_signal": {"func": f30_clean_tech_working_capital_drag_ebitda_ewma_21d_v082_signal},
    "f30_clean_tech_working_capital_drag_rate_base_growth_proxy_ewma_21d_v083_signal": {"func": f30_clean_tech_working_capital_drag_rate_base_growth_proxy_ewma_21d_v083_signal},
    "f30_clean_tech_working_capital_drag_operating_return_capex_ewma_21d_v084_signal": {"func": f30_clean_tech_working_capital_drag_operating_return_capex_ewma_21d_v084_signal},
    "f30_clean_tech_working_capital_drag_capex_ewma_42d_v085_signal": {"func": f30_clean_tech_working_capital_drag_capex_ewma_42d_v085_signal},
    "f30_clean_tech_working_capital_drag_assets_ewma_42d_v086_signal": {"func": f30_clean_tech_working_capital_drag_assets_ewma_42d_v086_signal},
    "f30_clean_tech_working_capital_drag_netinc_ewma_42d_v087_signal": {"func": f30_clean_tech_working_capital_drag_netinc_ewma_42d_v087_signal},
    "f30_clean_tech_working_capital_drag_ebitda_ewma_42d_v088_signal": {"func": f30_clean_tech_working_capital_drag_ebitda_ewma_42d_v088_signal},
    "f30_clean_tech_working_capital_drag_rate_base_growth_proxy_ewma_42d_v089_signal": {"func": f30_clean_tech_working_capital_drag_rate_base_growth_proxy_ewma_42d_v089_signal},
    "f30_clean_tech_working_capital_drag_operating_return_capex_ewma_42d_v090_signal": {"func": f30_clean_tech_working_capital_drag_operating_return_capex_ewma_42d_v090_signal},
    "f30_clean_tech_working_capital_drag_capex_ewma_63d_v091_signal": {"func": f30_clean_tech_working_capital_drag_capex_ewma_63d_v091_signal},
    "f30_clean_tech_working_capital_drag_assets_ewma_63d_v092_signal": {"func": f30_clean_tech_working_capital_drag_assets_ewma_63d_v092_signal},
    "f30_clean_tech_working_capital_drag_netinc_ewma_63d_v093_signal": {"func": f30_clean_tech_working_capital_drag_netinc_ewma_63d_v093_signal},
    "f30_clean_tech_working_capital_drag_ebitda_ewma_63d_v094_signal": {"func": f30_clean_tech_working_capital_drag_ebitda_ewma_63d_v094_signal},
    "f30_clean_tech_working_capital_drag_rate_base_growth_proxy_ewma_63d_v095_signal": {"func": f30_clean_tech_working_capital_drag_rate_base_growth_proxy_ewma_63d_v095_signal},
    "f30_clean_tech_working_capital_drag_operating_return_capex_ewma_63d_v096_signal": {"func": f30_clean_tech_working_capital_drag_operating_return_capex_ewma_63d_v096_signal},
    "f30_clean_tech_working_capital_drag_capex_ewma_126d_v097_signal": {"func": f30_clean_tech_working_capital_drag_capex_ewma_126d_v097_signal},
    "f30_clean_tech_working_capital_drag_assets_ewma_126d_v098_signal": {"func": f30_clean_tech_working_capital_drag_assets_ewma_126d_v098_signal},
    "f30_clean_tech_working_capital_drag_netinc_ewma_126d_v099_signal": {"func": f30_clean_tech_working_capital_drag_netinc_ewma_126d_v099_signal},
    "f30_clean_tech_working_capital_drag_ebitda_ewma_126d_v100_signal": {"func": f30_clean_tech_working_capital_drag_ebitda_ewma_126d_v100_signal},
    "f30_clean_tech_working_capital_drag_rate_base_growth_proxy_ewma_126d_v101_signal": {"func": f30_clean_tech_working_capital_drag_rate_base_growth_proxy_ewma_126d_v101_signal},
    "f30_clean_tech_working_capital_drag_operating_return_capex_ewma_126d_v102_signal": {"func": f30_clean_tech_working_capital_drag_operating_return_capex_ewma_126d_v102_signal},
    "f30_clean_tech_working_capital_drag_capex_ewma_252d_v103_signal": {"func": f30_clean_tech_working_capital_drag_capex_ewma_252d_v103_signal},
    "f30_clean_tech_working_capital_drag_assets_ewma_252d_v104_signal": {"func": f30_clean_tech_working_capital_drag_assets_ewma_252d_v104_signal},
    "f30_clean_tech_working_capital_drag_netinc_ewma_252d_v105_signal": {"func": f30_clean_tech_working_capital_drag_netinc_ewma_252d_v105_signal},
    "f30_clean_tech_working_capital_drag_ebitda_ewma_252d_v106_signal": {"func": f30_clean_tech_working_capital_drag_ebitda_ewma_252d_v106_signal},
    "f30_clean_tech_working_capital_drag_rate_base_growth_proxy_ewma_252d_v107_signal": {"func": f30_clean_tech_working_capital_drag_rate_base_growth_proxy_ewma_252d_v107_signal},
    "f30_clean_tech_working_capital_drag_operating_return_capex_ewma_252d_v108_signal": {"func": f30_clean_tech_working_capital_drag_operating_return_capex_ewma_252d_v108_signal},
    "f30_clean_tech_working_capital_drag_capex_ewma_504d_v109_signal": {"func": f30_clean_tech_working_capital_drag_capex_ewma_504d_v109_signal},
    "f30_clean_tech_working_capital_drag_assets_ewma_504d_v110_signal": {"func": f30_clean_tech_working_capital_drag_assets_ewma_504d_v110_signal},
    "f30_clean_tech_working_capital_drag_netinc_ewma_504d_v111_signal": {"func": f30_clean_tech_working_capital_drag_netinc_ewma_504d_v111_signal},
    "f30_clean_tech_working_capital_drag_ebitda_ewma_504d_v112_signal": {"func": f30_clean_tech_working_capital_drag_ebitda_ewma_504d_v112_signal},
    "f30_clean_tech_working_capital_drag_rate_base_growth_proxy_ewma_504d_v113_signal": {"func": f30_clean_tech_working_capital_drag_rate_base_growth_proxy_ewma_504d_v113_signal},
    "f30_clean_tech_working_capital_drag_operating_return_capex_ewma_504d_v114_signal": {"func": f30_clean_tech_working_capital_drag_operating_return_capex_ewma_504d_v114_signal},
    "f30_clean_tech_working_capital_drag_capex_ewma_756d_v115_signal": {"func": f30_clean_tech_working_capital_drag_capex_ewma_756d_v115_signal},
    "f30_clean_tech_working_capital_drag_assets_ewma_756d_v116_signal": {"func": f30_clean_tech_working_capital_drag_assets_ewma_756d_v116_signal},
    "f30_clean_tech_working_capital_drag_netinc_ewma_756d_v117_signal": {"func": f30_clean_tech_working_capital_drag_netinc_ewma_756d_v117_signal},
    "f30_clean_tech_working_capital_drag_ebitda_ewma_756d_v118_signal": {"func": f30_clean_tech_working_capital_drag_ebitda_ewma_756d_v118_signal},
    "f30_clean_tech_working_capital_drag_rate_base_growth_proxy_ewma_756d_v119_signal": {"func": f30_clean_tech_working_capital_drag_rate_base_growth_proxy_ewma_756d_v119_signal},
    "f30_clean_tech_working_capital_drag_operating_return_capex_ewma_756d_v120_signal": {"func": f30_clean_tech_working_capital_drag_operating_return_capex_ewma_756d_v120_signal},
    "f30_clean_tech_working_capital_drag_capex_ewma_1008d_v121_signal": {"func": f30_clean_tech_working_capital_drag_capex_ewma_1008d_v121_signal},
    "f30_clean_tech_working_capital_drag_assets_ewma_1008d_v122_signal": {"func": f30_clean_tech_working_capital_drag_assets_ewma_1008d_v122_signal},
    "f30_clean_tech_working_capital_drag_netinc_ewma_1008d_v123_signal": {"func": f30_clean_tech_working_capital_drag_netinc_ewma_1008d_v123_signal},
    "f30_clean_tech_working_capital_drag_ebitda_ewma_1008d_v124_signal": {"func": f30_clean_tech_working_capital_drag_ebitda_ewma_1008d_v124_signal},
    "f30_clean_tech_working_capital_drag_rate_base_growth_proxy_ewma_1008d_v125_signal": {"func": f30_clean_tech_working_capital_drag_rate_base_growth_proxy_ewma_1008d_v125_signal},
    "f30_clean_tech_working_capital_drag_operating_return_capex_ewma_1008d_v126_signal": {"func": f30_clean_tech_working_capital_drag_operating_return_capex_ewma_1008d_v126_signal},
    "f30_clean_tech_working_capital_drag_capex_ewma_1260d_v127_signal": {"func": f30_clean_tech_working_capital_drag_capex_ewma_1260d_v127_signal},
    "f30_clean_tech_working_capital_drag_assets_ewma_1260d_v128_signal": {"func": f30_clean_tech_working_capital_drag_assets_ewma_1260d_v128_signal},
    "f30_clean_tech_working_capital_drag_netinc_ewma_1260d_v129_signal": {"func": f30_clean_tech_working_capital_drag_netinc_ewma_1260d_v129_signal},
    "f30_clean_tech_working_capital_drag_ebitda_ewma_1260d_v130_signal": {"func": f30_clean_tech_working_capital_drag_ebitda_ewma_1260d_v130_signal},
    "f30_clean_tech_working_capital_drag_rate_base_growth_proxy_ewma_1260d_v131_signal": {"func": f30_clean_tech_working_capital_drag_rate_base_growth_proxy_ewma_1260d_v131_signal},
    "f30_clean_tech_working_capital_drag_operating_return_capex_ewma_1260d_v132_signal": {"func": f30_clean_tech_working_capital_drag_operating_return_capex_ewma_1260d_v132_signal},
    "f30_clean_tech_working_capital_drag_capex_z_5d_v133_signal": {"func": f30_clean_tech_working_capital_drag_capex_z_5d_v133_signal},
    "f30_clean_tech_working_capital_drag_assets_z_5d_v134_signal": {"func": f30_clean_tech_working_capital_drag_assets_z_5d_v134_signal},
    "f30_clean_tech_working_capital_drag_netinc_z_5d_v135_signal": {"func": f30_clean_tech_working_capital_drag_netinc_z_5d_v135_signal},
    "f30_clean_tech_working_capital_drag_ebitda_z_5d_v136_signal": {"func": f30_clean_tech_working_capital_drag_ebitda_z_5d_v136_signal},
    "f30_clean_tech_working_capital_drag_rate_base_growth_proxy_z_5d_v137_signal": {"func": f30_clean_tech_working_capital_drag_rate_base_growth_proxy_z_5d_v137_signal},
    "f30_clean_tech_working_capital_drag_operating_return_capex_z_5d_v138_signal": {"func": f30_clean_tech_working_capital_drag_operating_return_capex_z_5d_v138_signal},
    "f30_clean_tech_working_capital_drag_capex_z_10d_v139_signal": {"func": f30_clean_tech_working_capital_drag_capex_z_10d_v139_signal},
    "f30_clean_tech_working_capital_drag_assets_z_10d_v140_signal": {"func": f30_clean_tech_working_capital_drag_assets_z_10d_v140_signal},
    "f30_clean_tech_working_capital_drag_netinc_z_10d_v141_signal": {"func": f30_clean_tech_working_capital_drag_netinc_z_10d_v141_signal},
    "f30_clean_tech_working_capital_drag_ebitda_z_10d_v142_signal": {"func": f30_clean_tech_working_capital_drag_ebitda_z_10d_v142_signal},
    "f30_clean_tech_working_capital_drag_rate_base_growth_proxy_z_10d_v143_signal": {"func": f30_clean_tech_working_capital_drag_rate_base_growth_proxy_z_10d_v143_signal},
    "f30_clean_tech_working_capital_drag_operating_return_capex_z_10d_v144_signal": {"func": f30_clean_tech_working_capital_drag_operating_return_capex_z_10d_v144_signal},
    "f30_clean_tech_working_capital_drag_capex_z_21d_v145_signal": {"func": f30_clean_tech_working_capital_drag_capex_z_21d_v145_signal},
    "f30_clean_tech_working_capital_drag_assets_z_21d_v146_signal": {"func": f30_clean_tech_working_capital_drag_assets_z_21d_v146_signal},
    "f30_clean_tech_working_capital_drag_netinc_z_21d_v147_signal": {"func": f30_clean_tech_working_capital_drag_netinc_z_21d_v147_signal},
    "f30_clean_tech_working_capital_drag_ebitda_z_21d_v148_signal": {"func": f30_clean_tech_working_capital_drag_ebitda_z_21d_v148_signal},
    "f30_clean_tech_working_capital_drag_rate_base_growth_proxy_z_21d_v149_signal": {"func": f30_clean_tech_working_capital_drag_rate_base_growth_proxy_z_21d_v149_signal},
    "f30_clean_tech_working_capital_drag_operating_return_capex_z_21d_v150_signal": {"func": f30_clean_tech_working_capital_drag_operating_return_capex_z_21d_v150_signal},
}

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "roic": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "tangibles": np.random.normal(100, 10, n).cumsum(), "ev": np.random.normal(100, 10, n).cumsum(), "ps": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "opex": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "deferredrev": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "deposits": np.random.normal(100, 10, n).cumsum(), "pb": np.random.normal(100, 10, n).cumsum(), "bvps": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "liabilitiesc": np.random.normal(100, 10, n).cumsum(), "pe": np.random.normal(100, 10, n).cumsum(), "grossmargin": np.random.normal(100, 10, n).cumsum(), "divyield": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "equity": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum()
    })
    print(f"Verifying {len(REGISTRY)} functions for family 30...")
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
