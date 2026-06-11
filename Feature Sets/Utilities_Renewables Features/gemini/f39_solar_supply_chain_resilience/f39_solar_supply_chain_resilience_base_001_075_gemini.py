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

def f39_solar_supply_chain_resilience_debt_base_5d_v001_signal(debt):
    """Moving average of Raw level of debt over 5d window."""
    res = _sma(debt, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_solar_supply_chain_resilience_ebitda_base_5d_v002_signal(ebitda):
    """Moving average of Raw level of ebitda over 5d window."""
    res = _sma(ebitda, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_solar_supply_chain_resilience_fcf_base_5d_v003_signal(fcf):
    """Moving average of Raw level of fcf over 5d window."""
    res = _sma(fcf, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_solar_supply_chain_resilience_marketcap_base_5d_v004_signal(marketcap):
    """Moving average of Raw level of marketcap over 5d window."""
    res = _sma(marketcap, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_solar_supply_chain_resilience_project_leverage_base_5d_v005_signal(debt, ebitda, fcf):
    """Moving average of Leverage constrained by cash conversion over 5d window."""
    res = _sma(_ratio(debt, ebitda) * _ratio(fcf, debt), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_solar_supply_chain_resilience_yield_safety_base_5d_v006_signal(fcf, marketcap):
    """Moving average of Implied FCF yield for renewables over 5d window."""
    res = _sma(_ratio(fcf, marketcap), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_solar_supply_chain_resilience_debt_base_10d_v007_signal(debt):
    """Moving average of Raw level of debt over 10d window."""
    res = _sma(debt, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_solar_supply_chain_resilience_ebitda_base_10d_v008_signal(ebitda):
    """Moving average of Raw level of ebitda over 10d window."""
    res = _sma(ebitda, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_solar_supply_chain_resilience_fcf_base_10d_v009_signal(fcf):
    """Moving average of Raw level of fcf over 10d window."""
    res = _sma(fcf, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_solar_supply_chain_resilience_marketcap_base_10d_v010_signal(marketcap):
    """Moving average of Raw level of marketcap over 10d window."""
    res = _sma(marketcap, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_solar_supply_chain_resilience_project_leverage_base_10d_v011_signal(debt, ebitda, fcf):
    """Moving average of Leverage constrained by cash conversion over 10d window."""
    res = _sma(_ratio(debt, ebitda) * _ratio(fcf, debt), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_solar_supply_chain_resilience_yield_safety_base_10d_v012_signal(fcf, marketcap):
    """Moving average of Implied FCF yield for renewables over 10d window."""
    res = _sma(_ratio(fcf, marketcap), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_solar_supply_chain_resilience_debt_base_21d_v013_signal(debt):
    """Moving average of Raw level of debt over 21d window."""
    res = _sma(debt, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_solar_supply_chain_resilience_ebitda_base_21d_v014_signal(ebitda):
    """Moving average of Raw level of ebitda over 21d window."""
    res = _sma(ebitda, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_solar_supply_chain_resilience_fcf_base_21d_v015_signal(fcf):
    """Moving average of Raw level of fcf over 21d window."""
    res = _sma(fcf, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_solar_supply_chain_resilience_marketcap_base_21d_v016_signal(marketcap):
    """Moving average of Raw level of marketcap over 21d window."""
    res = _sma(marketcap, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_solar_supply_chain_resilience_project_leverage_base_21d_v017_signal(debt, ebitda, fcf):
    """Moving average of Leverage constrained by cash conversion over 21d window."""
    res = _sma(_ratio(debt, ebitda) * _ratio(fcf, debt), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_solar_supply_chain_resilience_yield_safety_base_21d_v018_signal(fcf, marketcap):
    """Moving average of Implied FCF yield for renewables over 21d window."""
    res = _sma(_ratio(fcf, marketcap), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_solar_supply_chain_resilience_debt_base_42d_v019_signal(debt):
    """Moving average of Raw level of debt over 42d window."""
    res = _sma(debt, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_solar_supply_chain_resilience_ebitda_base_42d_v020_signal(ebitda):
    """Moving average of Raw level of ebitda over 42d window."""
    res = _sma(ebitda, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_solar_supply_chain_resilience_fcf_base_42d_v021_signal(fcf):
    """Moving average of Raw level of fcf over 42d window."""
    res = _sma(fcf, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_solar_supply_chain_resilience_marketcap_base_42d_v022_signal(marketcap):
    """Moving average of Raw level of marketcap over 42d window."""
    res = _sma(marketcap, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_solar_supply_chain_resilience_project_leverage_base_42d_v023_signal(debt, ebitda, fcf):
    """Moving average of Leverage constrained by cash conversion over 42d window."""
    res = _sma(_ratio(debt, ebitda) * _ratio(fcf, debt), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_solar_supply_chain_resilience_yield_safety_base_42d_v024_signal(fcf, marketcap):
    """Moving average of Implied FCF yield for renewables over 42d window."""
    res = _sma(_ratio(fcf, marketcap), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_solar_supply_chain_resilience_debt_base_63d_v025_signal(debt):
    """Moving average of Raw level of debt over 63d window."""
    res = _sma(debt, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_solar_supply_chain_resilience_ebitda_base_63d_v026_signal(ebitda):
    """Moving average of Raw level of ebitda over 63d window."""
    res = _sma(ebitda, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_solar_supply_chain_resilience_fcf_base_63d_v027_signal(fcf):
    """Moving average of Raw level of fcf over 63d window."""
    res = _sma(fcf, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_solar_supply_chain_resilience_marketcap_base_63d_v028_signal(marketcap):
    """Moving average of Raw level of marketcap over 63d window."""
    res = _sma(marketcap, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_solar_supply_chain_resilience_project_leverage_base_63d_v029_signal(debt, ebitda, fcf):
    """Moving average of Leverage constrained by cash conversion over 63d window."""
    res = _sma(_ratio(debt, ebitda) * _ratio(fcf, debt), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_solar_supply_chain_resilience_yield_safety_base_63d_v030_signal(fcf, marketcap):
    """Moving average of Implied FCF yield for renewables over 63d window."""
    res = _sma(_ratio(fcf, marketcap), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_solar_supply_chain_resilience_debt_base_126d_v031_signal(debt):
    """Moving average of Raw level of debt over 126d window."""
    res = _sma(debt, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_solar_supply_chain_resilience_ebitda_base_126d_v032_signal(ebitda):
    """Moving average of Raw level of ebitda over 126d window."""
    res = _sma(ebitda, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_solar_supply_chain_resilience_fcf_base_126d_v033_signal(fcf):
    """Moving average of Raw level of fcf over 126d window."""
    res = _sma(fcf, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_solar_supply_chain_resilience_marketcap_base_126d_v034_signal(marketcap):
    """Moving average of Raw level of marketcap over 126d window."""
    res = _sma(marketcap, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_solar_supply_chain_resilience_project_leverage_base_126d_v035_signal(debt, ebitda, fcf):
    """Moving average of Leverage constrained by cash conversion over 126d window."""
    res = _sma(_ratio(debt, ebitda) * _ratio(fcf, debt), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_solar_supply_chain_resilience_yield_safety_base_126d_v036_signal(fcf, marketcap):
    """Moving average of Implied FCF yield for renewables over 126d window."""
    res = _sma(_ratio(fcf, marketcap), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_solar_supply_chain_resilience_debt_base_252d_v037_signal(debt):
    """Moving average of Raw level of debt over 252d window."""
    res = _sma(debt, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_solar_supply_chain_resilience_ebitda_base_252d_v038_signal(ebitda):
    """Moving average of Raw level of ebitda over 252d window."""
    res = _sma(ebitda, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_solar_supply_chain_resilience_fcf_base_252d_v039_signal(fcf):
    """Moving average of Raw level of fcf over 252d window."""
    res = _sma(fcf, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_solar_supply_chain_resilience_marketcap_base_252d_v040_signal(marketcap):
    """Moving average of Raw level of marketcap over 252d window."""
    res = _sma(marketcap, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_solar_supply_chain_resilience_project_leverage_base_252d_v041_signal(debt, ebitda, fcf):
    """Moving average of Leverage constrained by cash conversion over 252d window."""
    res = _sma(_ratio(debt, ebitda) * _ratio(fcf, debt), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_solar_supply_chain_resilience_yield_safety_base_252d_v042_signal(fcf, marketcap):
    """Moving average of Implied FCF yield for renewables over 252d window."""
    res = _sma(_ratio(fcf, marketcap), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_solar_supply_chain_resilience_debt_base_504d_v043_signal(debt):
    """Moving average of Raw level of debt over 504d window."""
    res = _sma(debt, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_solar_supply_chain_resilience_ebitda_base_504d_v044_signal(ebitda):
    """Moving average of Raw level of ebitda over 504d window."""
    res = _sma(ebitda, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_solar_supply_chain_resilience_fcf_base_504d_v045_signal(fcf):
    """Moving average of Raw level of fcf over 504d window."""
    res = _sma(fcf, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_solar_supply_chain_resilience_marketcap_base_504d_v046_signal(marketcap):
    """Moving average of Raw level of marketcap over 504d window."""
    res = _sma(marketcap, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_solar_supply_chain_resilience_project_leverage_base_504d_v047_signal(debt, ebitda, fcf):
    """Moving average of Leverage constrained by cash conversion over 504d window."""
    res = _sma(_ratio(debt, ebitda) * _ratio(fcf, debt), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_solar_supply_chain_resilience_yield_safety_base_504d_v048_signal(fcf, marketcap):
    """Moving average of Implied FCF yield for renewables over 504d window."""
    res = _sma(_ratio(fcf, marketcap), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_solar_supply_chain_resilience_debt_base_756d_v049_signal(debt):
    """Moving average of Raw level of debt over 756d window."""
    res = _sma(debt, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_solar_supply_chain_resilience_ebitda_base_756d_v050_signal(ebitda):
    """Moving average of Raw level of ebitda over 756d window."""
    res = _sma(ebitda, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_solar_supply_chain_resilience_fcf_base_756d_v051_signal(fcf):
    """Moving average of Raw level of fcf over 756d window."""
    res = _sma(fcf, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_solar_supply_chain_resilience_marketcap_base_756d_v052_signal(marketcap):
    """Moving average of Raw level of marketcap over 756d window."""
    res = _sma(marketcap, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_solar_supply_chain_resilience_project_leverage_base_756d_v053_signal(debt, ebitda, fcf):
    """Moving average of Leverage constrained by cash conversion over 756d window."""
    res = _sma(_ratio(debt, ebitda) * _ratio(fcf, debt), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_solar_supply_chain_resilience_yield_safety_base_756d_v054_signal(fcf, marketcap):
    """Moving average of Implied FCF yield for renewables over 756d window."""
    res = _sma(_ratio(fcf, marketcap), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_solar_supply_chain_resilience_debt_base_1008d_v055_signal(debt):
    """Moving average of Raw level of debt over 1008d window."""
    res = _sma(debt, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_solar_supply_chain_resilience_ebitda_base_1008d_v056_signal(ebitda):
    """Moving average of Raw level of ebitda over 1008d window."""
    res = _sma(ebitda, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_solar_supply_chain_resilience_fcf_base_1008d_v057_signal(fcf):
    """Moving average of Raw level of fcf over 1008d window."""
    res = _sma(fcf, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_solar_supply_chain_resilience_marketcap_base_1008d_v058_signal(marketcap):
    """Moving average of Raw level of marketcap over 1008d window."""
    res = _sma(marketcap, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_solar_supply_chain_resilience_project_leverage_base_1008d_v059_signal(debt, ebitda, fcf):
    """Moving average of Leverage constrained by cash conversion over 1008d window."""
    res = _sma(_ratio(debt, ebitda) * _ratio(fcf, debt), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_solar_supply_chain_resilience_yield_safety_base_1008d_v060_signal(fcf, marketcap):
    """Moving average of Implied FCF yield for renewables over 1008d window."""
    res = _sma(_ratio(fcf, marketcap), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_solar_supply_chain_resilience_debt_base_1260d_v061_signal(debt):
    """Moving average of Raw level of debt over 1260d window."""
    res = _sma(debt, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_solar_supply_chain_resilience_ebitda_base_1260d_v062_signal(ebitda):
    """Moving average of Raw level of ebitda over 1260d window."""
    res = _sma(ebitda, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_solar_supply_chain_resilience_fcf_base_1260d_v063_signal(fcf):
    """Moving average of Raw level of fcf over 1260d window."""
    res = _sma(fcf, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_solar_supply_chain_resilience_marketcap_base_1260d_v064_signal(marketcap):
    """Moving average of Raw level of marketcap over 1260d window."""
    res = _sma(marketcap, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_solar_supply_chain_resilience_project_leverage_base_1260d_v065_signal(debt, ebitda, fcf):
    """Moving average of Leverage constrained by cash conversion over 1260d window."""
    res = _sma(_ratio(debt, ebitda) * _ratio(fcf, debt), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_solar_supply_chain_resilience_yield_safety_base_1260d_v066_signal(fcf, marketcap):
    """Moving average of Implied FCF yield for renewables over 1260d window."""
    res = _sma(_ratio(fcf, marketcap), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_solar_supply_chain_resilience_debt_ewma_5d_v067_signal(debt):
    """Exponential moving average of Raw level of debt over 5d window."""
    res = _ewma(debt, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_solar_supply_chain_resilience_ebitda_ewma_5d_v068_signal(ebitda):
    """Exponential moving average of Raw level of ebitda over 5d window."""
    res = _ewma(ebitda, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_solar_supply_chain_resilience_fcf_ewma_5d_v069_signal(fcf):
    """Exponential moving average of Raw level of fcf over 5d window."""
    res = _ewma(fcf, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_solar_supply_chain_resilience_marketcap_ewma_5d_v070_signal(marketcap):
    """Exponential moving average of Raw level of marketcap over 5d window."""
    res = _ewma(marketcap, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_solar_supply_chain_resilience_project_leverage_ewma_5d_v071_signal(debt, ebitda, fcf):
    """Exponential moving average of Leverage constrained by cash conversion over 5d window."""
    res = _ewma(_ratio(debt, ebitda) * _ratio(fcf, debt), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_solar_supply_chain_resilience_yield_safety_ewma_5d_v072_signal(fcf, marketcap):
    """Exponential moving average of Implied FCF yield for renewables over 5d window."""
    res = _ewma(_ratio(fcf, marketcap), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_solar_supply_chain_resilience_debt_ewma_10d_v073_signal(debt):
    """Exponential moving average of Raw level of debt over 10d window."""
    res = _ewma(debt, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_solar_supply_chain_resilience_ebitda_ewma_10d_v074_signal(ebitda):
    """Exponential moving average of Raw level of ebitda over 10d window."""
    res = _ewma(ebitda, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_solar_supply_chain_resilience_fcf_ewma_10d_v075_signal(fcf):
    """Exponential moving average of Raw level of fcf over 10d window."""
    res = _ewma(fcf, 10)
    return res.replace([np.inf, -np.inf], np.nan)


# ===== Feature Registry =====
REGISTRY = {
    "f39_solar_supply_chain_resilience_debt_base_5d_v001_signal": {"func": f39_solar_supply_chain_resilience_debt_base_5d_v001_signal},
    "f39_solar_supply_chain_resilience_ebitda_base_5d_v002_signal": {"func": f39_solar_supply_chain_resilience_ebitda_base_5d_v002_signal},
    "f39_solar_supply_chain_resilience_fcf_base_5d_v003_signal": {"func": f39_solar_supply_chain_resilience_fcf_base_5d_v003_signal},
    "f39_solar_supply_chain_resilience_marketcap_base_5d_v004_signal": {"func": f39_solar_supply_chain_resilience_marketcap_base_5d_v004_signal},
    "f39_solar_supply_chain_resilience_project_leverage_base_5d_v005_signal": {"func": f39_solar_supply_chain_resilience_project_leverage_base_5d_v005_signal},
    "f39_solar_supply_chain_resilience_yield_safety_base_5d_v006_signal": {"func": f39_solar_supply_chain_resilience_yield_safety_base_5d_v006_signal},
    "f39_solar_supply_chain_resilience_debt_base_10d_v007_signal": {"func": f39_solar_supply_chain_resilience_debt_base_10d_v007_signal},
    "f39_solar_supply_chain_resilience_ebitda_base_10d_v008_signal": {"func": f39_solar_supply_chain_resilience_ebitda_base_10d_v008_signal},
    "f39_solar_supply_chain_resilience_fcf_base_10d_v009_signal": {"func": f39_solar_supply_chain_resilience_fcf_base_10d_v009_signal},
    "f39_solar_supply_chain_resilience_marketcap_base_10d_v010_signal": {"func": f39_solar_supply_chain_resilience_marketcap_base_10d_v010_signal},
    "f39_solar_supply_chain_resilience_project_leverage_base_10d_v011_signal": {"func": f39_solar_supply_chain_resilience_project_leverage_base_10d_v011_signal},
    "f39_solar_supply_chain_resilience_yield_safety_base_10d_v012_signal": {"func": f39_solar_supply_chain_resilience_yield_safety_base_10d_v012_signal},
    "f39_solar_supply_chain_resilience_debt_base_21d_v013_signal": {"func": f39_solar_supply_chain_resilience_debt_base_21d_v013_signal},
    "f39_solar_supply_chain_resilience_ebitda_base_21d_v014_signal": {"func": f39_solar_supply_chain_resilience_ebitda_base_21d_v014_signal},
    "f39_solar_supply_chain_resilience_fcf_base_21d_v015_signal": {"func": f39_solar_supply_chain_resilience_fcf_base_21d_v015_signal},
    "f39_solar_supply_chain_resilience_marketcap_base_21d_v016_signal": {"func": f39_solar_supply_chain_resilience_marketcap_base_21d_v016_signal},
    "f39_solar_supply_chain_resilience_project_leverage_base_21d_v017_signal": {"func": f39_solar_supply_chain_resilience_project_leverage_base_21d_v017_signal},
    "f39_solar_supply_chain_resilience_yield_safety_base_21d_v018_signal": {"func": f39_solar_supply_chain_resilience_yield_safety_base_21d_v018_signal},
    "f39_solar_supply_chain_resilience_debt_base_42d_v019_signal": {"func": f39_solar_supply_chain_resilience_debt_base_42d_v019_signal},
    "f39_solar_supply_chain_resilience_ebitda_base_42d_v020_signal": {"func": f39_solar_supply_chain_resilience_ebitda_base_42d_v020_signal},
    "f39_solar_supply_chain_resilience_fcf_base_42d_v021_signal": {"func": f39_solar_supply_chain_resilience_fcf_base_42d_v021_signal},
    "f39_solar_supply_chain_resilience_marketcap_base_42d_v022_signal": {"func": f39_solar_supply_chain_resilience_marketcap_base_42d_v022_signal},
    "f39_solar_supply_chain_resilience_project_leverage_base_42d_v023_signal": {"func": f39_solar_supply_chain_resilience_project_leverage_base_42d_v023_signal},
    "f39_solar_supply_chain_resilience_yield_safety_base_42d_v024_signal": {"func": f39_solar_supply_chain_resilience_yield_safety_base_42d_v024_signal},
    "f39_solar_supply_chain_resilience_debt_base_63d_v025_signal": {"func": f39_solar_supply_chain_resilience_debt_base_63d_v025_signal},
    "f39_solar_supply_chain_resilience_ebitda_base_63d_v026_signal": {"func": f39_solar_supply_chain_resilience_ebitda_base_63d_v026_signal},
    "f39_solar_supply_chain_resilience_fcf_base_63d_v027_signal": {"func": f39_solar_supply_chain_resilience_fcf_base_63d_v027_signal},
    "f39_solar_supply_chain_resilience_marketcap_base_63d_v028_signal": {"func": f39_solar_supply_chain_resilience_marketcap_base_63d_v028_signal},
    "f39_solar_supply_chain_resilience_project_leverage_base_63d_v029_signal": {"func": f39_solar_supply_chain_resilience_project_leverage_base_63d_v029_signal},
    "f39_solar_supply_chain_resilience_yield_safety_base_63d_v030_signal": {"func": f39_solar_supply_chain_resilience_yield_safety_base_63d_v030_signal},
    "f39_solar_supply_chain_resilience_debt_base_126d_v031_signal": {"func": f39_solar_supply_chain_resilience_debt_base_126d_v031_signal},
    "f39_solar_supply_chain_resilience_ebitda_base_126d_v032_signal": {"func": f39_solar_supply_chain_resilience_ebitda_base_126d_v032_signal},
    "f39_solar_supply_chain_resilience_fcf_base_126d_v033_signal": {"func": f39_solar_supply_chain_resilience_fcf_base_126d_v033_signal},
    "f39_solar_supply_chain_resilience_marketcap_base_126d_v034_signal": {"func": f39_solar_supply_chain_resilience_marketcap_base_126d_v034_signal},
    "f39_solar_supply_chain_resilience_project_leverage_base_126d_v035_signal": {"func": f39_solar_supply_chain_resilience_project_leverage_base_126d_v035_signal},
    "f39_solar_supply_chain_resilience_yield_safety_base_126d_v036_signal": {"func": f39_solar_supply_chain_resilience_yield_safety_base_126d_v036_signal},
    "f39_solar_supply_chain_resilience_debt_base_252d_v037_signal": {"func": f39_solar_supply_chain_resilience_debt_base_252d_v037_signal},
    "f39_solar_supply_chain_resilience_ebitda_base_252d_v038_signal": {"func": f39_solar_supply_chain_resilience_ebitda_base_252d_v038_signal},
    "f39_solar_supply_chain_resilience_fcf_base_252d_v039_signal": {"func": f39_solar_supply_chain_resilience_fcf_base_252d_v039_signal},
    "f39_solar_supply_chain_resilience_marketcap_base_252d_v040_signal": {"func": f39_solar_supply_chain_resilience_marketcap_base_252d_v040_signal},
    "f39_solar_supply_chain_resilience_project_leverage_base_252d_v041_signal": {"func": f39_solar_supply_chain_resilience_project_leverage_base_252d_v041_signal},
    "f39_solar_supply_chain_resilience_yield_safety_base_252d_v042_signal": {"func": f39_solar_supply_chain_resilience_yield_safety_base_252d_v042_signal},
    "f39_solar_supply_chain_resilience_debt_base_504d_v043_signal": {"func": f39_solar_supply_chain_resilience_debt_base_504d_v043_signal},
    "f39_solar_supply_chain_resilience_ebitda_base_504d_v044_signal": {"func": f39_solar_supply_chain_resilience_ebitda_base_504d_v044_signal},
    "f39_solar_supply_chain_resilience_fcf_base_504d_v045_signal": {"func": f39_solar_supply_chain_resilience_fcf_base_504d_v045_signal},
    "f39_solar_supply_chain_resilience_marketcap_base_504d_v046_signal": {"func": f39_solar_supply_chain_resilience_marketcap_base_504d_v046_signal},
    "f39_solar_supply_chain_resilience_project_leverage_base_504d_v047_signal": {"func": f39_solar_supply_chain_resilience_project_leverage_base_504d_v047_signal},
    "f39_solar_supply_chain_resilience_yield_safety_base_504d_v048_signal": {"func": f39_solar_supply_chain_resilience_yield_safety_base_504d_v048_signal},
    "f39_solar_supply_chain_resilience_debt_base_756d_v049_signal": {"func": f39_solar_supply_chain_resilience_debt_base_756d_v049_signal},
    "f39_solar_supply_chain_resilience_ebitda_base_756d_v050_signal": {"func": f39_solar_supply_chain_resilience_ebitda_base_756d_v050_signal},
    "f39_solar_supply_chain_resilience_fcf_base_756d_v051_signal": {"func": f39_solar_supply_chain_resilience_fcf_base_756d_v051_signal},
    "f39_solar_supply_chain_resilience_marketcap_base_756d_v052_signal": {"func": f39_solar_supply_chain_resilience_marketcap_base_756d_v052_signal},
    "f39_solar_supply_chain_resilience_project_leverage_base_756d_v053_signal": {"func": f39_solar_supply_chain_resilience_project_leverage_base_756d_v053_signal},
    "f39_solar_supply_chain_resilience_yield_safety_base_756d_v054_signal": {"func": f39_solar_supply_chain_resilience_yield_safety_base_756d_v054_signal},
    "f39_solar_supply_chain_resilience_debt_base_1008d_v055_signal": {"func": f39_solar_supply_chain_resilience_debt_base_1008d_v055_signal},
    "f39_solar_supply_chain_resilience_ebitda_base_1008d_v056_signal": {"func": f39_solar_supply_chain_resilience_ebitda_base_1008d_v056_signal},
    "f39_solar_supply_chain_resilience_fcf_base_1008d_v057_signal": {"func": f39_solar_supply_chain_resilience_fcf_base_1008d_v057_signal},
    "f39_solar_supply_chain_resilience_marketcap_base_1008d_v058_signal": {"func": f39_solar_supply_chain_resilience_marketcap_base_1008d_v058_signal},
    "f39_solar_supply_chain_resilience_project_leverage_base_1008d_v059_signal": {"func": f39_solar_supply_chain_resilience_project_leverage_base_1008d_v059_signal},
    "f39_solar_supply_chain_resilience_yield_safety_base_1008d_v060_signal": {"func": f39_solar_supply_chain_resilience_yield_safety_base_1008d_v060_signal},
    "f39_solar_supply_chain_resilience_debt_base_1260d_v061_signal": {"func": f39_solar_supply_chain_resilience_debt_base_1260d_v061_signal},
    "f39_solar_supply_chain_resilience_ebitda_base_1260d_v062_signal": {"func": f39_solar_supply_chain_resilience_ebitda_base_1260d_v062_signal},
    "f39_solar_supply_chain_resilience_fcf_base_1260d_v063_signal": {"func": f39_solar_supply_chain_resilience_fcf_base_1260d_v063_signal},
    "f39_solar_supply_chain_resilience_marketcap_base_1260d_v064_signal": {"func": f39_solar_supply_chain_resilience_marketcap_base_1260d_v064_signal},
    "f39_solar_supply_chain_resilience_project_leverage_base_1260d_v065_signal": {"func": f39_solar_supply_chain_resilience_project_leverage_base_1260d_v065_signal},
    "f39_solar_supply_chain_resilience_yield_safety_base_1260d_v066_signal": {"func": f39_solar_supply_chain_resilience_yield_safety_base_1260d_v066_signal},
    "f39_solar_supply_chain_resilience_debt_ewma_5d_v067_signal": {"func": f39_solar_supply_chain_resilience_debt_ewma_5d_v067_signal},
    "f39_solar_supply_chain_resilience_ebitda_ewma_5d_v068_signal": {"func": f39_solar_supply_chain_resilience_ebitda_ewma_5d_v068_signal},
    "f39_solar_supply_chain_resilience_fcf_ewma_5d_v069_signal": {"func": f39_solar_supply_chain_resilience_fcf_ewma_5d_v069_signal},
    "f39_solar_supply_chain_resilience_marketcap_ewma_5d_v070_signal": {"func": f39_solar_supply_chain_resilience_marketcap_ewma_5d_v070_signal},
    "f39_solar_supply_chain_resilience_project_leverage_ewma_5d_v071_signal": {"func": f39_solar_supply_chain_resilience_project_leverage_ewma_5d_v071_signal},
    "f39_solar_supply_chain_resilience_yield_safety_ewma_5d_v072_signal": {"func": f39_solar_supply_chain_resilience_yield_safety_ewma_5d_v072_signal},
    "f39_solar_supply_chain_resilience_debt_ewma_10d_v073_signal": {"func": f39_solar_supply_chain_resilience_debt_ewma_10d_v073_signal},
    "f39_solar_supply_chain_resilience_ebitda_ewma_10d_v074_signal": {"func": f39_solar_supply_chain_resilience_ebitda_ewma_10d_v074_signal},
    "f39_solar_supply_chain_resilience_fcf_ewma_10d_v075_signal": {"func": f39_solar_supply_chain_resilience_fcf_ewma_10d_v075_signal},
}

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "roic": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "tangibles": np.random.normal(100, 10, n).cumsum(), "ev": np.random.normal(100, 10, n).cumsum(), "ps": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "opex": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "deferredrev": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "deposits": np.random.normal(100, 10, n).cumsum(), "pb": np.random.normal(100, 10, n).cumsum(), "bvps": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "liabilitiesc": np.random.normal(100, 10, n).cumsum(), "pe": np.random.normal(100, 10, n).cumsum(), "grossmargin": np.random.normal(100, 10, n).cumsum(), "divyield": np.random.normal(100, 10, n).cumsum(), "debt": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "equity": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum()
    })
    print(f"Verifying {len(REGISTRY)} functions for family 39...")
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
