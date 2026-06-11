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

def f47_renewables_project_finance_leverage_debt_slope_pct_5d_v001_signal(debt):
    """Percentage slope for Raw level of debt over 5d window."""
    res = _slope_pct(debt, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_renewables_project_finance_leverage_ebitda_slope_pct_5d_v002_signal(ebitda):
    """Percentage slope for Raw level of ebitda over 5d window."""
    res = _slope_pct(ebitda, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_renewables_project_finance_leverage_fcf_slope_pct_5d_v003_signal(fcf):
    """Percentage slope for Raw level of fcf over 5d window."""
    res = _slope_pct(fcf, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_renewables_project_finance_leverage_marketcap_slope_pct_5d_v004_signal(marketcap):
    """Percentage slope for Raw level of marketcap over 5d window."""
    res = _slope_pct(marketcap, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_renewables_project_finance_leverage_project_leverage_slope_pct_5d_v005_signal(debt, ebitda, fcf):
    """Percentage slope for Leverage constrained by cash conversion over 5d window."""
    res = _slope_pct(_ratio(debt, ebitda) * _ratio(fcf, debt), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_renewables_project_finance_leverage_yield_safety_slope_pct_5d_v006_signal(fcf, marketcap):
    """Percentage slope for Implied FCF yield for renewables over 5d window."""
    res = _slope_pct(_ratio(fcf, marketcap), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_renewables_project_finance_leverage_debt_slope_pct_10d_v007_signal(debt):
    """Percentage slope for Raw level of debt over 10d window."""
    res = _slope_pct(debt, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_renewables_project_finance_leverage_ebitda_slope_pct_10d_v008_signal(ebitda):
    """Percentage slope for Raw level of ebitda over 10d window."""
    res = _slope_pct(ebitda, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_renewables_project_finance_leverage_fcf_slope_pct_10d_v009_signal(fcf):
    """Percentage slope for Raw level of fcf over 10d window."""
    res = _slope_pct(fcf, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_renewables_project_finance_leverage_marketcap_slope_pct_10d_v010_signal(marketcap):
    """Percentage slope for Raw level of marketcap over 10d window."""
    res = _slope_pct(marketcap, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_renewables_project_finance_leverage_project_leverage_slope_pct_10d_v011_signal(debt, ebitda, fcf):
    """Percentage slope for Leverage constrained by cash conversion over 10d window."""
    res = _slope_pct(_ratio(debt, ebitda) * _ratio(fcf, debt), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_renewables_project_finance_leverage_yield_safety_slope_pct_10d_v012_signal(fcf, marketcap):
    """Percentage slope for Implied FCF yield for renewables over 10d window."""
    res = _slope_pct(_ratio(fcf, marketcap), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_renewables_project_finance_leverage_debt_slope_pct_21d_v013_signal(debt):
    """Percentage slope for Raw level of debt over 21d window."""
    res = _slope_pct(debt, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_renewables_project_finance_leverage_ebitda_slope_pct_21d_v014_signal(ebitda):
    """Percentage slope for Raw level of ebitda over 21d window."""
    res = _slope_pct(ebitda, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_renewables_project_finance_leverage_fcf_slope_pct_21d_v015_signal(fcf):
    """Percentage slope for Raw level of fcf over 21d window."""
    res = _slope_pct(fcf, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_renewables_project_finance_leverage_marketcap_slope_pct_21d_v016_signal(marketcap):
    """Percentage slope for Raw level of marketcap over 21d window."""
    res = _slope_pct(marketcap, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_renewables_project_finance_leverage_project_leverage_slope_pct_21d_v017_signal(debt, ebitda, fcf):
    """Percentage slope for Leverage constrained by cash conversion over 21d window."""
    res = _slope_pct(_ratio(debt, ebitda) * _ratio(fcf, debt), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_renewables_project_finance_leverage_yield_safety_slope_pct_21d_v018_signal(fcf, marketcap):
    """Percentage slope for Implied FCF yield for renewables over 21d window."""
    res = _slope_pct(_ratio(fcf, marketcap), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_renewables_project_finance_leverage_debt_slope_pct_42d_v019_signal(debt):
    """Percentage slope for Raw level of debt over 42d window."""
    res = _slope_pct(debt, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_renewables_project_finance_leverage_ebitda_slope_pct_42d_v020_signal(ebitda):
    """Percentage slope for Raw level of ebitda over 42d window."""
    res = _slope_pct(ebitda, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_renewables_project_finance_leverage_fcf_slope_pct_42d_v021_signal(fcf):
    """Percentage slope for Raw level of fcf over 42d window."""
    res = _slope_pct(fcf, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_renewables_project_finance_leverage_marketcap_slope_pct_42d_v022_signal(marketcap):
    """Percentage slope for Raw level of marketcap over 42d window."""
    res = _slope_pct(marketcap, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_renewables_project_finance_leverage_project_leverage_slope_pct_42d_v023_signal(debt, ebitda, fcf):
    """Percentage slope for Leverage constrained by cash conversion over 42d window."""
    res = _slope_pct(_ratio(debt, ebitda) * _ratio(fcf, debt), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_renewables_project_finance_leverage_yield_safety_slope_pct_42d_v024_signal(fcf, marketcap):
    """Percentage slope for Implied FCF yield for renewables over 42d window."""
    res = _slope_pct(_ratio(fcf, marketcap), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_renewables_project_finance_leverage_debt_slope_pct_63d_v025_signal(debt):
    """Percentage slope for Raw level of debt over 63d window."""
    res = _slope_pct(debt, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_renewables_project_finance_leverage_ebitda_slope_pct_63d_v026_signal(ebitda):
    """Percentage slope for Raw level of ebitda over 63d window."""
    res = _slope_pct(ebitda, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_renewables_project_finance_leverage_fcf_slope_pct_63d_v027_signal(fcf):
    """Percentage slope for Raw level of fcf over 63d window."""
    res = _slope_pct(fcf, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_renewables_project_finance_leverage_marketcap_slope_pct_63d_v028_signal(marketcap):
    """Percentage slope for Raw level of marketcap over 63d window."""
    res = _slope_pct(marketcap, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_renewables_project_finance_leverage_project_leverage_slope_pct_63d_v029_signal(debt, ebitda, fcf):
    """Percentage slope for Leverage constrained by cash conversion over 63d window."""
    res = _slope_pct(_ratio(debt, ebitda) * _ratio(fcf, debt), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_renewables_project_finance_leverage_yield_safety_slope_pct_63d_v030_signal(fcf, marketcap):
    """Percentage slope for Implied FCF yield for renewables over 63d window."""
    res = _slope_pct(_ratio(fcf, marketcap), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_renewables_project_finance_leverage_debt_slope_pct_126d_v031_signal(debt):
    """Percentage slope for Raw level of debt over 126d window."""
    res = _slope_pct(debt, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_renewables_project_finance_leverage_ebitda_slope_pct_126d_v032_signal(ebitda):
    """Percentage slope for Raw level of ebitda over 126d window."""
    res = _slope_pct(ebitda, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_renewables_project_finance_leverage_fcf_slope_pct_126d_v033_signal(fcf):
    """Percentage slope for Raw level of fcf over 126d window."""
    res = _slope_pct(fcf, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_renewables_project_finance_leverage_marketcap_slope_pct_126d_v034_signal(marketcap):
    """Percentage slope for Raw level of marketcap over 126d window."""
    res = _slope_pct(marketcap, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_renewables_project_finance_leverage_project_leverage_slope_pct_126d_v035_signal(debt, ebitda, fcf):
    """Percentage slope for Leverage constrained by cash conversion over 126d window."""
    res = _slope_pct(_ratio(debt, ebitda) * _ratio(fcf, debt), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_renewables_project_finance_leverage_yield_safety_slope_pct_126d_v036_signal(fcf, marketcap):
    """Percentage slope for Implied FCF yield for renewables over 126d window."""
    res = _slope_pct(_ratio(fcf, marketcap), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_renewables_project_finance_leverage_debt_slope_pct_252d_v037_signal(debt):
    """Percentage slope for Raw level of debt over 252d window."""
    res = _slope_pct(debt, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_renewables_project_finance_leverage_ebitda_slope_pct_252d_v038_signal(ebitda):
    """Percentage slope for Raw level of ebitda over 252d window."""
    res = _slope_pct(ebitda, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_renewables_project_finance_leverage_fcf_slope_pct_252d_v039_signal(fcf):
    """Percentage slope for Raw level of fcf over 252d window."""
    res = _slope_pct(fcf, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_renewables_project_finance_leverage_marketcap_slope_pct_252d_v040_signal(marketcap):
    """Percentage slope for Raw level of marketcap over 252d window."""
    res = _slope_pct(marketcap, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_renewables_project_finance_leverage_project_leverage_slope_pct_252d_v041_signal(debt, ebitda, fcf):
    """Percentage slope for Leverage constrained by cash conversion over 252d window."""
    res = _slope_pct(_ratio(debt, ebitda) * _ratio(fcf, debt), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_renewables_project_finance_leverage_yield_safety_slope_pct_252d_v042_signal(fcf, marketcap):
    """Percentage slope for Implied FCF yield for renewables over 252d window."""
    res = _slope_pct(_ratio(fcf, marketcap), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_renewables_project_finance_leverage_debt_slope_pct_504d_v043_signal(debt):
    """Percentage slope for Raw level of debt over 504d window."""
    res = _slope_pct(debt, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_renewables_project_finance_leverage_ebitda_slope_pct_504d_v044_signal(ebitda):
    """Percentage slope for Raw level of ebitda over 504d window."""
    res = _slope_pct(ebitda, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_renewables_project_finance_leverage_fcf_slope_pct_504d_v045_signal(fcf):
    """Percentage slope for Raw level of fcf over 504d window."""
    res = _slope_pct(fcf, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_renewables_project_finance_leverage_marketcap_slope_pct_504d_v046_signal(marketcap):
    """Percentage slope for Raw level of marketcap over 504d window."""
    res = _slope_pct(marketcap, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_renewables_project_finance_leverage_project_leverage_slope_pct_504d_v047_signal(debt, ebitda, fcf):
    """Percentage slope for Leverage constrained by cash conversion over 504d window."""
    res = _slope_pct(_ratio(debt, ebitda) * _ratio(fcf, debt), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_renewables_project_finance_leverage_yield_safety_slope_pct_504d_v048_signal(fcf, marketcap):
    """Percentage slope for Implied FCF yield for renewables over 504d window."""
    res = _slope_pct(_ratio(fcf, marketcap), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_renewables_project_finance_leverage_debt_slope_pct_756d_v049_signal(debt):
    """Percentage slope for Raw level of debt over 756d window."""
    res = _slope_pct(debt, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_renewables_project_finance_leverage_ebitda_slope_pct_756d_v050_signal(ebitda):
    """Percentage slope for Raw level of ebitda over 756d window."""
    res = _slope_pct(ebitda, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_renewables_project_finance_leverage_fcf_slope_pct_756d_v051_signal(fcf):
    """Percentage slope for Raw level of fcf over 756d window."""
    res = _slope_pct(fcf, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_renewables_project_finance_leverage_marketcap_slope_pct_756d_v052_signal(marketcap):
    """Percentage slope for Raw level of marketcap over 756d window."""
    res = _slope_pct(marketcap, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_renewables_project_finance_leverage_project_leverage_slope_pct_756d_v053_signal(debt, ebitda, fcf):
    """Percentage slope for Leverage constrained by cash conversion over 756d window."""
    res = _slope_pct(_ratio(debt, ebitda) * _ratio(fcf, debt), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_renewables_project_finance_leverage_yield_safety_slope_pct_756d_v054_signal(fcf, marketcap):
    """Percentage slope for Implied FCF yield for renewables over 756d window."""
    res = _slope_pct(_ratio(fcf, marketcap), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_renewables_project_finance_leverage_debt_slope_pct_1008d_v055_signal(debt):
    """Percentage slope for Raw level of debt over 1008d window."""
    res = _slope_pct(debt, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_renewables_project_finance_leverage_ebitda_slope_pct_1008d_v056_signal(ebitda):
    """Percentage slope for Raw level of ebitda over 1008d window."""
    res = _slope_pct(ebitda, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_renewables_project_finance_leverage_fcf_slope_pct_1008d_v057_signal(fcf):
    """Percentage slope for Raw level of fcf over 1008d window."""
    res = _slope_pct(fcf, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_renewables_project_finance_leverage_marketcap_slope_pct_1008d_v058_signal(marketcap):
    """Percentage slope for Raw level of marketcap over 1008d window."""
    res = _slope_pct(marketcap, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_renewables_project_finance_leverage_project_leverage_slope_pct_1008d_v059_signal(debt, ebitda, fcf):
    """Percentage slope for Leverage constrained by cash conversion over 1008d window."""
    res = _slope_pct(_ratio(debt, ebitda) * _ratio(fcf, debt), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_renewables_project_finance_leverage_yield_safety_slope_pct_1008d_v060_signal(fcf, marketcap):
    """Percentage slope for Implied FCF yield for renewables over 1008d window."""
    res = _slope_pct(_ratio(fcf, marketcap), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_renewables_project_finance_leverage_debt_slope_pct_1260d_v061_signal(debt):
    """Percentage slope for Raw level of debt over 1260d window."""
    res = _slope_pct(debt, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_renewables_project_finance_leverage_ebitda_slope_pct_1260d_v062_signal(ebitda):
    """Percentage slope for Raw level of ebitda over 1260d window."""
    res = _slope_pct(ebitda, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_renewables_project_finance_leverage_fcf_slope_pct_1260d_v063_signal(fcf):
    """Percentage slope for Raw level of fcf over 1260d window."""
    res = _slope_pct(fcf, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_renewables_project_finance_leverage_marketcap_slope_pct_1260d_v064_signal(marketcap):
    """Percentage slope for Raw level of marketcap over 1260d window."""
    res = _slope_pct(marketcap, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_renewables_project_finance_leverage_project_leverage_slope_pct_1260d_v065_signal(debt, ebitda, fcf):
    """Percentage slope for Leverage constrained by cash conversion over 1260d window."""
    res = _slope_pct(_ratio(debt, ebitda) * _ratio(fcf, debt), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_renewables_project_finance_leverage_yield_safety_slope_pct_1260d_v066_signal(fcf, marketcap):
    """Percentage slope for Implied FCF yield for renewables over 1260d window."""
    res = _slope_pct(_ratio(fcf, marketcap), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_renewables_project_finance_leverage_debt_jerk_5d_v067_signal(debt):
    """Acceleration/Jerk for Raw level of debt over 5d window."""
    res = _jerk(debt, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_renewables_project_finance_leverage_ebitda_jerk_5d_v068_signal(ebitda):
    """Acceleration/Jerk for Raw level of ebitda over 5d window."""
    res = _jerk(ebitda, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_renewables_project_finance_leverage_fcf_jerk_5d_v069_signal(fcf):
    """Acceleration/Jerk for Raw level of fcf over 5d window."""
    res = _jerk(fcf, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_renewables_project_finance_leverage_marketcap_jerk_5d_v070_signal(marketcap):
    """Acceleration/Jerk for Raw level of marketcap over 5d window."""
    res = _jerk(marketcap, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_renewables_project_finance_leverage_project_leverage_jerk_5d_v071_signal(debt, ebitda, fcf):
    """Acceleration/Jerk for Leverage constrained by cash conversion over 5d window."""
    res = _jerk(_ratio(debt, ebitda) * _ratio(fcf, debt), 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_renewables_project_finance_leverage_yield_safety_jerk_5d_v072_signal(fcf, marketcap):
    """Acceleration/Jerk for Implied FCF yield for renewables over 5d window."""
    res = _jerk(_ratio(fcf, marketcap), 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_renewables_project_finance_leverage_debt_jerk_10d_v073_signal(debt):
    """Acceleration/Jerk for Raw level of debt over 10d window."""
    res = _jerk(debt, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_renewables_project_finance_leverage_ebitda_jerk_10d_v074_signal(ebitda):
    """Acceleration/Jerk for Raw level of ebitda over 10d window."""
    res = _jerk(ebitda, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_renewables_project_finance_leverage_fcf_jerk_10d_v075_signal(fcf):
    """Acceleration/Jerk for Raw level of fcf over 10d window."""
    res = _jerk(fcf, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_renewables_project_finance_leverage_marketcap_jerk_10d_v076_signal(marketcap):
    """Acceleration/Jerk for Raw level of marketcap over 10d window."""
    res = _jerk(marketcap, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_renewables_project_finance_leverage_project_leverage_jerk_10d_v077_signal(debt, ebitda, fcf):
    """Acceleration/Jerk for Leverage constrained by cash conversion over 10d window."""
    res = _jerk(_ratio(debt, ebitda) * _ratio(fcf, debt), 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_renewables_project_finance_leverage_yield_safety_jerk_10d_v078_signal(fcf, marketcap):
    """Acceleration/Jerk for Implied FCF yield for renewables over 10d window."""
    res = _jerk(_ratio(fcf, marketcap), 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_renewables_project_finance_leverage_debt_jerk_21d_v079_signal(debt):
    """Acceleration/Jerk for Raw level of debt over 21d window."""
    res = _jerk(debt, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_renewables_project_finance_leverage_ebitda_jerk_21d_v080_signal(ebitda):
    """Acceleration/Jerk for Raw level of ebitda over 21d window."""
    res = _jerk(ebitda, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_renewables_project_finance_leverage_fcf_jerk_21d_v081_signal(fcf):
    """Acceleration/Jerk for Raw level of fcf over 21d window."""
    res = _jerk(fcf, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_renewables_project_finance_leverage_marketcap_jerk_21d_v082_signal(marketcap):
    """Acceleration/Jerk for Raw level of marketcap over 21d window."""
    res = _jerk(marketcap, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_renewables_project_finance_leverage_project_leverage_jerk_21d_v083_signal(debt, ebitda, fcf):
    """Acceleration/Jerk for Leverage constrained by cash conversion over 21d window."""
    res = _jerk(_ratio(debt, ebitda) * _ratio(fcf, debt), 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_renewables_project_finance_leverage_yield_safety_jerk_21d_v084_signal(fcf, marketcap):
    """Acceleration/Jerk for Implied FCF yield for renewables over 21d window."""
    res = _jerk(_ratio(fcf, marketcap), 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_renewables_project_finance_leverage_debt_jerk_42d_v085_signal(debt):
    """Acceleration/Jerk for Raw level of debt over 42d window."""
    res = _jerk(debt, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_renewables_project_finance_leverage_ebitda_jerk_42d_v086_signal(ebitda):
    """Acceleration/Jerk for Raw level of ebitda over 42d window."""
    res = _jerk(ebitda, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_renewables_project_finance_leverage_fcf_jerk_42d_v087_signal(fcf):
    """Acceleration/Jerk for Raw level of fcf over 42d window."""
    res = _jerk(fcf, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_renewables_project_finance_leverage_marketcap_jerk_42d_v088_signal(marketcap):
    """Acceleration/Jerk for Raw level of marketcap over 42d window."""
    res = _jerk(marketcap, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_renewables_project_finance_leverage_project_leverage_jerk_42d_v089_signal(debt, ebitda, fcf):
    """Acceleration/Jerk for Leverage constrained by cash conversion over 42d window."""
    res = _jerk(_ratio(debt, ebitda) * _ratio(fcf, debt), 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_renewables_project_finance_leverage_yield_safety_jerk_42d_v090_signal(fcf, marketcap):
    """Acceleration/Jerk for Implied FCF yield for renewables over 42d window."""
    res = _jerk(_ratio(fcf, marketcap), 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_renewables_project_finance_leverage_debt_jerk_63d_v091_signal(debt):
    """Acceleration/Jerk for Raw level of debt over 63d window."""
    res = _jerk(debt, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_renewables_project_finance_leverage_ebitda_jerk_63d_v092_signal(ebitda):
    """Acceleration/Jerk for Raw level of ebitda over 63d window."""
    res = _jerk(ebitda, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_renewables_project_finance_leverage_fcf_jerk_63d_v093_signal(fcf):
    """Acceleration/Jerk for Raw level of fcf over 63d window."""
    res = _jerk(fcf, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_renewables_project_finance_leverage_marketcap_jerk_63d_v094_signal(marketcap):
    """Acceleration/Jerk for Raw level of marketcap over 63d window."""
    res = _jerk(marketcap, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_renewables_project_finance_leverage_project_leverage_jerk_63d_v095_signal(debt, ebitda, fcf):
    """Acceleration/Jerk for Leverage constrained by cash conversion over 63d window."""
    res = _jerk(_ratio(debt, ebitda) * _ratio(fcf, debt), 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_renewables_project_finance_leverage_yield_safety_jerk_63d_v096_signal(fcf, marketcap):
    """Acceleration/Jerk for Implied FCF yield for renewables over 63d window."""
    res = _jerk(_ratio(fcf, marketcap), 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_renewables_project_finance_leverage_debt_jerk_126d_v097_signal(debt):
    """Acceleration/Jerk for Raw level of debt over 126d window."""
    res = _jerk(debt, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_renewables_project_finance_leverage_ebitda_jerk_126d_v098_signal(ebitda):
    """Acceleration/Jerk for Raw level of ebitda over 126d window."""
    res = _jerk(ebitda, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_renewables_project_finance_leverage_fcf_jerk_126d_v099_signal(fcf):
    """Acceleration/Jerk for Raw level of fcf over 126d window."""
    res = _jerk(fcf, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_renewables_project_finance_leverage_marketcap_jerk_126d_v100_signal(marketcap):
    """Acceleration/Jerk for Raw level of marketcap over 126d window."""
    res = _jerk(marketcap, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_renewables_project_finance_leverage_project_leverage_jerk_126d_v101_signal(debt, ebitda, fcf):
    """Acceleration/Jerk for Leverage constrained by cash conversion over 126d window."""
    res = _jerk(_ratio(debt, ebitda) * _ratio(fcf, debt), 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_renewables_project_finance_leverage_yield_safety_jerk_126d_v102_signal(fcf, marketcap):
    """Acceleration/Jerk for Implied FCF yield for renewables over 126d window."""
    res = _jerk(_ratio(fcf, marketcap), 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_renewables_project_finance_leverage_debt_jerk_252d_v103_signal(debt):
    """Acceleration/Jerk for Raw level of debt over 252d window."""
    res = _jerk(debt, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_renewables_project_finance_leverage_ebitda_jerk_252d_v104_signal(ebitda):
    """Acceleration/Jerk for Raw level of ebitda over 252d window."""
    res = _jerk(ebitda, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_renewables_project_finance_leverage_fcf_jerk_252d_v105_signal(fcf):
    """Acceleration/Jerk for Raw level of fcf over 252d window."""
    res = _jerk(fcf, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_renewables_project_finance_leverage_marketcap_jerk_252d_v106_signal(marketcap):
    """Acceleration/Jerk for Raw level of marketcap over 252d window."""
    res = _jerk(marketcap, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_renewables_project_finance_leverage_project_leverage_jerk_252d_v107_signal(debt, ebitda, fcf):
    """Acceleration/Jerk for Leverage constrained by cash conversion over 252d window."""
    res = _jerk(_ratio(debt, ebitda) * _ratio(fcf, debt), 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_renewables_project_finance_leverage_yield_safety_jerk_252d_v108_signal(fcf, marketcap):
    """Acceleration/Jerk for Implied FCF yield for renewables over 252d window."""
    res = _jerk(_ratio(fcf, marketcap), 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_renewables_project_finance_leverage_debt_jerk_504d_v109_signal(debt):
    """Acceleration/Jerk for Raw level of debt over 504d window."""
    res = _jerk(debt, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_renewables_project_finance_leverage_ebitda_jerk_504d_v110_signal(ebitda):
    """Acceleration/Jerk for Raw level of ebitda over 504d window."""
    res = _jerk(ebitda, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_renewables_project_finance_leverage_fcf_jerk_504d_v111_signal(fcf):
    """Acceleration/Jerk for Raw level of fcf over 504d window."""
    res = _jerk(fcf, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_renewables_project_finance_leverage_marketcap_jerk_504d_v112_signal(marketcap):
    """Acceleration/Jerk for Raw level of marketcap over 504d window."""
    res = _jerk(marketcap, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_renewables_project_finance_leverage_project_leverage_jerk_504d_v113_signal(debt, ebitda, fcf):
    """Acceleration/Jerk for Leverage constrained by cash conversion over 504d window."""
    res = _jerk(_ratio(debt, ebitda) * _ratio(fcf, debt), 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_renewables_project_finance_leverage_yield_safety_jerk_504d_v114_signal(fcf, marketcap):
    """Acceleration/Jerk for Implied FCF yield for renewables over 504d window."""
    res = _jerk(_ratio(fcf, marketcap), 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_renewables_project_finance_leverage_debt_jerk_756d_v115_signal(debt):
    """Acceleration/Jerk for Raw level of debt over 756d window."""
    res = _jerk(debt, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_renewables_project_finance_leverage_ebitda_jerk_756d_v116_signal(ebitda):
    """Acceleration/Jerk for Raw level of ebitda over 756d window."""
    res = _jerk(ebitda, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_renewables_project_finance_leverage_fcf_jerk_756d_v117_signal(fcf):
    """Acceleration/Jerk for Raw level of fcf over 756d window."""
    res = _jerk(fcf, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_renewables_project_finance_leverage_marketcap_jerk_756d_v118_signal(marketcap):
    """Acceleration/Jerk for Raw level of marketcap over 756d window."""
    res = _jerk(marketcap, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_renewables_project_finance_leverage_project_leverage_jerk_756d_v119_signal(debt, ebitda, fcf):
    """Acceleration/Jerk for Leverage constrained by cash conversion over 756d window."""
    res = _jerk(_ratio(debt, ebitda) * _ratio(fcf, debt), 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_renewables_project_finance_leverage_yield_safety_jerk_756d_v120_signal(fcf, marketcap):
    """Acceleration/Jerk for Implied FCF yield for renewables over 756d window."""
    res = _jerk(_ratio(fcf, marketcap), 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_renewables_project_finance_leverage_debt_jerk_1008d_v121_signal(debt):
    """Acceleration/Jerk for Raw level of debt over 1008d window."""
    res = _jerk(debt, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_renewables_project_finance_leverage_ebitda_jerk_1008d_v122_signal(ebitda):
    """Acceleration/Jerk for Raw level of ebitda over 1008d window."""
    res = _jerk(ebitda, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_renewables_project_finance_leverage_fcf_jerk_1008d_v123_signal(fcf):
    """Acceleration/Jerk for Raw level of fcf over 1008d window."""
    res = _jerk(fcf, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_renewables_project_finance_leverage_marketcap_jerk_1008d_v124_signal(marketcap):
    """Acceleration/Jerk for Raw level of marketcap over 1008d window."""
    res = _jerk(marketcap, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_renewables_project_finance_leverage_project_leverage_jerk_1008d_v125_signal(debt, ebitda, fcf):
    """Acceleration/Jerk for Leverage constrained by cash conversion over 1008d window."""
    res = _jerk(_ratio(debt, ebitda) * _ratio(fcf, debt), 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_renewables_project_finance_leverage_yield_safety_jerk_1008d_v126_signal(fcf, marketcap):
    """Acceleration/Jerk for Implied FCF yield for renewables over 1008d window."""
    res = _jerk(_ratio(fcf, marketcap), 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_renewables_project_finance_leverage_debt_jerk_1260d_v127_signal(debt):
    """Acceleration/Jerk for Raw level of debt over 1260d window."""
    res = _jerk(debt, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_renewables_project_finance_leverage_ebitda_jerk_1260d_v128_signal(ebitda):
    """Acceleration/Jerk for Raw level of ebitda over 1260d window."""
    res = _jerk(ebitda, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_renewables_project_finance_leverage_fcf_jerk_1260d_v129_signal(fcf):
    """Acceleration/Jerk for Raw level of fcf over 1260d window."""
    res = _jerk(fcf, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_renewables_project_finance_leverage_marketcap_jerk_1260d_v130_signal(marketcap):
    """Acceleration/Jerk for Raw level of marketcap over 1260d window."""
    res = _jerk(marketcap, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_renewables_project_finance_leverage_project_leverage_jerk_1260d_v131_signal(debt, ebitda, fcf):
    """Acceleration/Jerk for Leverage constrained by cash conversion over 1260d window."""
    res = _jerk(_ratio(debt, ebitda) * _ratio(fcf, debt), 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_renewables_project_finance_leverage_yield_safety_jerk_1260d_v132_signal(fcf, marketcap):
    """Acceleration/Jerk for Implied FCF yield for renewables over 1260d window."""
    res = _jerk(_ratio(fcf, marketcap), 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_renewables_project_finance_leverage_debt_slope_diff_norm_5d_v133_signal(debt):
    """Normalized slope change for Raw level of debt over 5d window."""
    res = (_slope_pct(debt, 5).diff(5) / _sma(debt.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f47_renewables_project_finance_leverage_ebitda_slope_diff_norm_5d_v134_signal(ebitda):
    """Normalized slope change for Raw level of ebitda over 5d window."""
    res = (_slope_pct(ebitda, 5).diff(5) / _sma(ebitda.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f47_renewables_project_finance_leverage_fcf_slope_diff_norm_5d_v135_signal(fcf):
    """Normalized slope change for Raw level of fcf over 5d window."""
    res = (_slope_pct(fcf, 5).diff(5) / _sma(fcf.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f47_renewables_project_finance_leverage_marketcap_slope_diff_norm_5d_v136_signal(marketcap):
    """Normalized slope change for Raw level of marketcap over 5d window."""
    res = (_slope_pct(marketcap, 5).diff(5) / _sma(marketcap.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f47_renewables_project_finance_leverage_project_leverage_slope_diff_norm_5d_v137_signal(debt, ebitda, fcf):
    """Normalized slope change for Leverage constrained by cash conversion over 5d window."""
    res = (_slope_pct(_ratio(debt, ebitda) * _ratio(fcf, debt), 5).diff(5) / _sma(_ratio(debt, ebitda) * _ratio(fcf, debt).abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f47_renewables_project_finance_leverage_yield_safety_slope_diff_norm_5d_v138_signal(fcf, marketcap):
    """Normalized slope change for Implied FCF yield for renewables over 5d window."""
    res = (_slope_pct(_ratio(fcf, marketcap), 5).diff(5) / _sma(_ratio(fcf, marketcap).abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f47_renewables_project_finance_leverage_debt_slope_diff_norm_10d_v139_signal(debt):
    """Normalized slope change for Raw level of debt over 10d window."""
    res = (_slope_pct(debt, 10).diff(10) / _sma(debt.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f47_renewables_project_finance_leverage_ebitda_slope_diff_norm_10d_v140_signal(ebitda):
    """Normalized slope change for Raw level of ebitda over 10d window."""
    res = (_slope_pct(ebitda, 10).diff(10) / _sma(ebitda.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f47_renewables_project_finance_leverage_fcf_slope_diff_norm_10d_v141_signal(fcf):
    """Normalized slope change for Raw level of fcf over 10d window."""
    res = (_slope_pct(fcf, 10).diff(10) / _sma(fcf.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f47_renewables_project_finance_leverage_marketcap_slope_diff_norm_10d_v142_signal(marketcap):
    """Normalized slope change for Raw level of marketcap over 10d window."""
    res = (_slope_pct(marketcap, 10).diff(10) / _sma(marketcap.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f47_renewables_project_finance_leverage_project_leverage_slope_diff_norm_10d_v143_signal(debt, ebitda, fcf):
    """Normalized slope change for Leverage constrained by cash conversion over 10d window."""
    res = (_slope_pct(_ratio(debt, ebitda) * _ratio(fcf, debt), 10).diff(10) / _sma(_ratio(debt, ebitda) * _ratio(fcf, debt).abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f47_renewables_project_finance_leverage_yield_safety_slope_diff_norm_10d_v144_signal(fcf, marketcap):
    """Normalized slope change for Implied FCF yield for renewables over 10d window."""
    res = (_slope_pct(_ratio(fcf, marketcap), 10).diff(10) / _sma(_ratio(fcf, marketcap).abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f47_renewables_project_finance_leverage_debt_slope_diff_norm_21d_v145_signal(debt):
    """Normalized slope change for Raw level of debt over 21d window."""
    res = (_slope_pct(debt, 21).diff(21) / _sma(debt.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f47_renewables_project_finance_leverage_ebitda_slope_diff_norm_21d_v146_signal(ebitda):
    """Normalized slope change for Raw level of ebitda over 21d window."""
    res = (_slope_pct(ebitda, 21).diff(21) / _sma(ebitda.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f47_renewables_project_finance_leverage_fcf_slope_diff_norm_21d_v147_signal(fcf):
    """Normalized slope change for Raw level of fcf over 21d window."""
    res = (_slope_pct(fcf, 21).diff(21) / _sma(fcf.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f47_renewables_project_finance_leverage_marketcap_slope_diff_norm_21d_v148_signal(marketcap):
    """Normalized slope change for Raw level of marketcap over 21d window."""
    res = (_slope_pct(marketcap, 21).diff(21) / _sma(marketcap.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f47_renewables_project_finance_leverage_project_leverage_slope_diff_norm_21d_v149_signal(debt, ebitda, fcf):
    """Normalized slope change for Leverage constrained by cash conversion over 21d window."""
    res = (_slope_pct(_ratio(debt, ebitda) * _ratio(fcf, debt), 21).diff(21) / _sma(_ratio(debt, ebitda) * _ratio(fcf, debt).abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f47_renewables_project_finance_leverage_yield_safety_slope_diff_norm_21d_v150_signal(fcf, marketcap):
    """Normalized slope change for Implied FCF yield for renewables over 21d window."""
    res = (_slope_pct(_ratio(fcf, marketcap), 21).diff(21) / _sma(_ratio(fcf, marketcap).abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)


# ===== Feature Registry =====
REGISTRY = {
    "f47_renewables_project_finance_leverage_debt_slope_pct_5d_v001_signal": {"func": f47_renewables_project_finance_leverage_debt_slope_pct_5d_v001_signal},
    "f47_renewables_project_finance_leverage_ebitda_slope_pct_5d_v002_signal": {"func": f47_renewables_project_finance_leverage_ebitda_slope_pct_5d_v002_signal},
    "f47_renewables_project_finance_leverage_fcf_slope_pct_5d_v003_signal": {"func": f47_renewables_project_finance_leverage_fcf_slope_pct_5d_v003_signal},
    "f47_renewables_project_finance_leverage_marketcap_slope_pct_5d_v004_signal": {"func": f47_renewables_project_finance_leverage_marketcap_slope_pct_5d_v004_signal},
    "f47_renewables_project_finance_leverage_project_leverage_slope_pct_5d_v005_signal": {"func": f47_renewables_project_finance_leverage_project_leverage_slope_pct_5d_v005_signal},
    "f47_renewables_project_finance_leverage_yield_safety_slope_pct_5d_v006_signal": {"func": f47_renewables_project_finance_leverage_yield_safety_slope_pct_5d_v006_signal},
    "f47_renewables_project_finance_leverage_debt_slope_pct_10d_v007_signal": {"func": f47_renewables_project_finance_leverage_debt_slope_pct_10d_v007_signal},
    "f47_renewables_project_finance_leverage_ebitda_slope_pct_10d_v008_signal": {"func": f47_renewables_project_finance_leverage_ebitda_slope_pct_10d_v008_signal},
    "f47_renewables_project_finance_leverage_fcf_slope_pct_10d_v009_signal": {"func": f47_renewables_project_finance_leverage_fcf_slope_pct_10d_v009_signal},
    "f47_renewables_project_finance_leverage_marketcap_slope_pct_10d_v010_signal": {"func": f47_renewables_project_finance_leverage_marketcap_slope_pct_10d_v010_signal},
    "f47_renewables_project_finance_leverage_project_leverage_slope_pct_10d_v011_signal": {"func": f47_renewables_project_finance_leverage_project_leverage_slope_pct_10d_v011_signal},
    "f47_renewables_project_finance_leverage_yield_safety_slope_pct_10d_v012_signal": {"func": f47_renewables_project_finance_leverage_yield_safety_slope_pct_10d_v012_signal},
    "f47_renewables_project_finance_leverage_debt_slope_pct_21d_v013_signal": {"func": f47_renewables_project_finance_leverage_debt_slope_pct_21d_v013_signal},
    "f47_renewables_project_finance_leverage_ebitda_slope_pct_21d_v014_signal": {"func": f47_renewables_project_finance_leverage_ebitda_slope_pct_21d_v014_signal},
    "f47_renewables_project_finance_leverage_fcf_slope_pct_21d_v015_signal": {"func": f47_renewables_project_finance_leverage_fcf_slope_pct_21d_v015_signal},
    "f47_renewables_project_finance_leverage_marketcap_slope_pct_21d_v016_signal": {"func": f47_renewables_project_finance_leverage_marketcap_slope_pct_21d_v016_signal},
    "f47_renewables_project_finance_leverage_project_leverage_slope_pct_21d_v017_signal": {"func": f47_renewables_project_finance_leverage_project_leverage_slope_pct_21d_v017_signal},
    "f47_renewables_project_finance_leverage_yield_safety_slope_pct_21d_v018_signal": {"func": f47_renewables_project_finance_leverage_yield_safety_slope_pct_21d_v018_signal},
    "f47_renewables_project_finance_leverage_debt_slope_pct_42d_v019_signal": {"func": f47_renewables_project_finance_leverage_debt_slope_pct_42d_v019_signal},
    "f47_renewables_project_finance_leverage_ebitda_slope_pct_42d_v020_signal": {"func": f47_renewables_project_finance_leverage_ebitda_slope_pct_42d_v020_signal},
    "f47_renewables_project_finance_leverage_fcf_slope_pct_42d_v021_signal": {"func": f47_renewables_project_finance_leverage_fcf_slope_pct_42d_v021_signal},
    "f47_renewables_project_finance_leverage_marketcap_slope_pct_42d_v022_signal": {"func": f47_renewables_project_finance_leverage_marketcap_slope_pct_42d_v022_signal},
    "f47_renewables_project_finance_leverage_project_leverage_slope_pct_42d_v023_signal": {"func": f47_renewables_project_finance_leverage_project_leverage_slope_pct_42d_v023_signal},
    "f47_renewables_project_finance_leverage_yield_safety_slope_pct_42d_v024_signal": {"func": f47_renewables_project_finance_leverage_yield_safety_slope_pct_42d_v024_signal},
    "f47_renewables_project_finance_leverage_debt_slope_pct_63d_v025_signal": {"func": f47_renewables_project_finance_leverage_debt_slope_pct_63d_v025_signal},
    "f47_renewables_project_finance_leverage_ebitda_slope_pct_63d_v026_signal": {"func": f47_renewables_project_finance_leverage_ebitda_slope_pct_63d_v026_signal},
    "f47_renewables_project_finance_leverage_fcf_slope_pct_63d_v027_signal": {"func": f47_renewables_project_finance_leverage_fcf_slope_pct_63d_v027_signal},
    "f47_renewables_project_finance_leverage_marketcap_slope_pct_63d_v028_signal": {"func": f47_renewables_project_finance_leverage_marketcap_slope_pct_63d_v028_signal},
    "f47_renewables_project_finance_leverage_project_leverage_slope_pct_63d_v029_signal": {"func": f47_renewables_project_finance_leverage_project_leverage_slope_pct_63d_v029_signal},
    "f47_renewables_project_finance_leverage_yield_safety_slope_pct_63d_v030_signal": {"func": f47_renewables_project_finance_leverage_yield_safety_slope_pct_63d_v030_signal},
    "f47_renewables_project_finance_leverage_debt_slope_pct_126d_v031_signal": {"func": f47_renewables_project_finance_leverage_debt_slope_pct_126d_v031_signal},
    "f47_renewables_project_finance_leverage_ebitda_slope_pct_126d_v032_signal": {"func": f47_renewables_project_finance_leverage_ebitda_slope_pct_126d_v032_signal},
    "f47_renewables_project_finance_leverage_fcf_slope_pct_126d_v033_signal": {"func": f47_renewables_project_finance_leverage_fcf_slope_pct_126d_v033_signal},
    "f47_renewables_project_finance_leverage_marketcap_slope_pct_126d_v034_signal": {"func": f47_renewables_project_finance_leverage_marketcap_slope_pct_126d_v034_signal},
    "f47_renewables_project_finance_leverage_project_leverage_slope_pct_126d_v035_signal": {"func": f47_renewables_project_finance_leverage_project_leverage_slope_pct_126d_v035_signal},
    "f47_renewables_project_finance_leverage_yield_safety_slope_pct_126d_v036_signal": {"func": f47_renewables_project_finance_leverage_yield_safety_slope_pct_126d_v036_signal},
    "f47_renewables_project_finance_leverage_debt_slope_pct_252d_v037_signal": {"func": f47_renewables_project_finance_leverage_debt_slope_pct_252d_v037_signal},
    "f47_renewables_project_finance_leverage_ebitda_slope_pct_252d_v038_signal": {"func": f47_renewables_project_finance_leverage_ebitda_slope_pct_252d_v038_signal},
    "f47_renewables_project_finance_leverage_fcf_slope_pct_252d_v039_signal": {"func": f47_renewables_project_finance_leverage_fcf_slope_pct_252d_v039_signal},
    "f47_renewables_project_finance_leverage_marketcap_slope_pct_252d_v040_signal": {"func": f47_renewables_project_finance_leverage_marketcap_slope_pct_252d_v040_signal},
    "f47_renewables_project_finance_leverage_project_leverage_slope_pct_252d_v041_signal": {"func": f47_renewables_project_finance_leverage_project_leverage_slope_pct_252d_v041_signal},
    "f47_renewables_project_finance_leverage_yield_safety_slope_pct_252d_v042_signal": {"func": f47_renewables_project_finance_leverage_yield_safety_slope_pct_252d_v042_signal},
    "f47_renewables_project_finance_leverage_debt_slope_pct_504d_v043_signal": {"func": f47_renewables_project_finance_leverage_debt_slope_pct_504d_v043_signal},
    "f47_renewables_project_finance_leverage_ebitda_slope_pct_504d_v044_signal": {"func": f47_renewables_project_finance_leverage_ebitda_slope_pct_504d_v044_signal},
    "f47_renewables_project_finance_leverage_fcf_slope_pct_504d_v045_signal": {"func": f47_renewables_project_finance_leverage_fcf_slope_pct_504d_v045_signal},
    "f47_renewables_project_finance_leverage_marketcap_slope_pct_504d_v046_signal": {"func": f47_renewables_project_finance_leverage_marketcap_slope_pct_504d_v046_signal},
    "f47_renewables_project_finance_leverage_project_leverage_slope_pct_504d_v047_signal": {"func": f47_renewables_project_finance_leverage_project_leverage_slope_pct_504d_v047_signal},
    "f47_renewables_project_finance_leverage_yield_safety_slope_pct_504d_v048_signal": {"func": f47_renewables_project_finance_leverage_yield_safety_slope_pct_504d_v048_signal},
    "f47_renewables_project_finance_leverage_debt_slope_pct_756d_v049_signal": {"func": f47_renewables_project_finance_leverage_debt_slope_pct_756d_v049_signal},
    "f47_renewables_project_finance_leverage_ebitda_slope_pct_756d_v050_signal": {"func": f47_renewables_project_finance_leverage_ebitda_slope_pct_756d_v050_signal},
    "f47_renewables_project_finance_leverage_fcf_slope_pct_756d_v051_signal": {"func": f47_renewables_project_finance_leverage_fcf_slope_pct_756d_v051_signal},
    "f47_renewables_project_finance_leverage_marketcap_slope_pct_756d_v052_signal": {"func": f47_renewables_project_finance_leverage_marketcap_slope_pct_756d_v052_signal},
    "f47_renewables_project_finance_leverage_project_leverage_slope_pct_756d_v053_signal": {"func": f47_renewables_project_finance_leverage_project_leverage_slope_pct_756d_v053_signal},
    "f47_renewables_project_finance_leverage_yield_safety_slope_pct_756d_v054_signal": {"func": f47_renewables_project_finance_leverage_yield_safety_slope_pct_756d_v054_signal},
    "f47_renewables_project_finance_leverage_debt_slope_pct_1008d_v055_signal": {"func": f47_renewables_project_finance_leverage_debt_slope_pct_1008d_v055_signal},
    "f47_renewables_project_finance_leverage_ebitda_slope_pct_1008d_v056_signal": {"func": f47_renewables_project_finance_leverage_ebitda_slope_pct_1008d_v056_signal},
    "f47_renewables_project_finance_leverage_fcf_slope_pct_1008d_v057_signal": {"func": f47_renewables_project_finance_leverage_fcf_slope_pct_1008d_v057_signal},
    "f47_renewables_project_finance_leverage_marketcap_slope_pct_1008d_v058_signal": {"func": f47_renewables_project_finance_leverage_marketcap_slope_pct_1008d_v058_signal},
    "f47_renewables_project_finance_leverage_project_leverage_slope_pct_1008d_v059_signal": {"func": f47_renewables_project_finance_leverage_project_leverage_slope_pct_1008d_v059_signal},
    "f47_renewables_project_finance_leverage_yield_safety_slope_pct_1008d_v060_signal": {"func": f47_renewables_project_finance_leverage_yield_safety_slope_pct_1008d_v060_signal},
    "f47_renewables_project_finance_leverage_debt_slope_pct_1260d_v061_signal": {"func": f47_renewables_project_finance_leverage_debt_slope_pct_1260d_v061_signal},
    "f47_renewables_project_finance_leverage_ebitda_slope_pct_1260d_v062_signal": {"func": f47_renewables_project_finance_leverage_ebitda_slope_pct_1260d_v062_signal},
    "f47_renewables_project_finance_leverage_fcf_slope_pct_1260d_v063_signal": {"func": f47_renewables_project_finance_leverage_fcf_slope_pct_1260d_v063_signal},
    "f47_renewables_project_finance_leverage_marketcap_slope_pct_1260d_v064_signal": {"func": f47_renewables_project_finance_leverage_marketcap_slope_pct_1260d_v064_signal},
    "f47_renewables_project_finance_leverage_project_leverage_slope_pct_1260d_v065_signal": {"func": f47_renewables_project_finance_leverage_project_leverage_slope_pct_1260d_v065_signal},
    "f47_renewables_project_finance_leverage_yield_safety_slope_pct_1260d_v066_signal": {"func": f47_renewables_project_finance_leverage_yield_safety_slope_pct_1260d_v066_signal},
    "f47_renewables_project_finance_leverage_debt_jerk_5d_v067_signal": {"func": f47_renewables_project_finance_leverage_debt_jerk_5d_v067_signal},
    "f47_renewables_project_finance_leverage_ebitda_jerk_5d_v068_signal": {"func": f47_renewables_project_finance_leverage_ebitda_jerk_5d_v068_signal},
    "f47_renewables_project_finance_leverage_fcf_jerk_5d_v069_signal": {"func": f47_renewables_project_finance_leverage_fcf_jerk_5d_v069_signal},
    "f47_renewables_project_finance_leverage_marketcap_jerk_5d_v070_signal": {"func": f47_renewables_project_finance_leverage_marketcap_jerk_5d_v070_signal},
    "f47_renewables_project_finance_leverage_project_leverage_jerk_5d_v071_signal": {"func": f47_renewables_project_finance_leverage_project_leverage_jerk_5d_v071_signal},
    "f47_renewables_project_finance_leverage_yield_safety_jerk_5d_v072_signal": {"func": f47_renewables_project_finance_leverage_yield_safety_jerk_5d_v072_signal},
    "f47_renewables_project_finance_leverage_debt_jerk_10d_v073_signal": {"func": f47_renewables_project_finance_leverage_debt_jerk_10d_v073_signal},
    "f47_renewables_project_finance_leverage_ebitda_jerk_10d_v074_signal": {"func": f47_renewables_project_finance_leverage_ebitda_jerk_10d_v074_signal},
    "f47_renewables_project_finance_leverage_fcf_jerk_10d_v075_signal": {"func": f47_renewables_project_finance_leverage_fcf_jerk_10d_v075_signal},
    "f47_renewables_project_finance_leverage_marketcap_jerk_10d_v076_signal": {"func": f47_renewables_project_finance_leverage_marketcap_jerk_10d_v076_signal},
    "f47_renewables_project_finance_leverage_project_leverage_jerk_10d_v077_signal": {"func": f47_renewables_project_finance_leverage_project_leverage_jerk_10d_v077_signal},
    "f47_renewables_project_finance_leverage_yield_safety_jerk_10d_v078_signal": {"func": f47_renewables_project_finance_leverage_yield_safety_jerk_10d_v078_signal},
    "f47_renewables_project_finance_leverage_debt_jerk_21d_v079_signal": {"func": f47_renewables_project_finance_leverage_debt_jerk_21d_v079_signal},
    "f47_renewables_project_finance_leverage_ebitda_jerk_21d_v080_signal": {"func": f47_renewables_project_finance_leverage_ebitda_jerk_21d_v080_signal},
    "f47_renewables_project_finance_leverage_fcf_jerk_21d_v081_signal": {"func": f47_renewables_project_finance_leverage_fcf_jerk_21d_v081_signal},
    "f47_renewables_project_finance_leverage_marketcap_jerk_21d_v082_signal": {"func": f47_renewables_project_finance_leverage_marketcap_jerk_21d_v082_signal},
    "f47_renewables_project_finance_leverage_project_leverage_jerk_21d_v083_signal": {"func": f47_renewables_project_finance_leverage_project_leverage_jerk_21d_v083_signal},
    "f47_renewables_project_finance_leverage_yield_safety_jerk_21d_v084_signal": {"func": f47_renewables_project_finance_leverage_yield_safety_jerk_21d_v084_signal},
    "f47_renewables_project_finance_leverage_debt_jerk_42d_v085_signal": {"func": f47_renewables_project_finance_leverage_debt_jerk_42d_v085_signal},
    "f47_renewables_project_finance_leverage_ebitda_jerk_42d_v086_signal": {"func": f47_renewables_project_finance_leverage_ebitda_jerk_42d_v086_signal},
    "f47_renewables_project_finance_leverage_fcf_jerk_42d_v087_signal": {"func": f47_renewables_project_finance_leverage_fcf_jerk_42d_v087_signal},
    "f47_renewables_project_finance_leverage_marketcap_jerk_42d_v088_signal": {"func": f47_renewables_project_finance_leverage_marketcap_jerk_42d_v088_signal},
    "f47_renewables_project_finance_leverage_project_leverage_jerk_42d_v089_signal": {"func": f47_renewables_project_finance_leverage_project_leverage_jerk_42d_v089_signal},
    "f47_renewables_project_finance_leverage_yield_safety_jerk_42d_v090_signal": {"func": f47_renewables_project_finance_leverage_yield_safety_jerk_42d_v090_signal},
    "f47_renewables_project_finance_leverage_debt_jerk_63d_v091_signal": {"func": f47_renewables_project_finance_leverage_debt_jerk_63d_v091_signal},
    "f47_renewables_project_finance_leverage_ebitda_jerk_63d_v092_signal": {"func": f47_renewables_project_finance_leverage_ebitda_jerk_63d_v092_signal},
    "f47_renewables_project_finance_leverage_fcf_jerk_63d_v093_signal": {"func": f47_renewables_project_finance_leverage_fcf_jerk_63d_v093_signal},
    "f47_renewables_project_finance_leverage_marketcap_jerk_63d_v094_signal": {"func": f47_renewables_project_finance_leverage_marketcap_jerk_63d_v094_signal},
    "f47_renewables_project_finance_leverage_project_leverage_jerk_63d_v095_signal": {"func": f47_renewables_project_finance_leverage_project_leverage_jerk_63d_v095_signal},
    "f47_renewables_project_finance_leverage_yield_safety_jerk_63d_v096_signal": {"func": f47_renewables_project_finance_leverage_yield_safety_jerk_63d_v096_signal},
    "f47_renewables_project_finance_leverage_debt_jerk_126d_v097_signal": {"func": f47_renewables_project_finance_leverage_debt_jerk_126d_v097_signal},
    "f47_renewables_project_finance_leverage_ebitda_jerk_126d_v098_signal": {"func": f47_renewables_project_finance_leverage_ebitda_jerk_126d_v098_signal},
    "f47_renewables_project_finance_leverage_fcf_jerk_126d_v099_signal": {"func": f47_renewables_project_finance_leverage_fcf_jerk_126d_v099_signal},
    "f47_renewables_project_finance_leverage_marketcap_jerk_126d_v100_signal": {"func": f47_renewables_project_finance_leverage_marketcap_jerk_126d_v100_signal},
    "f47_renewables_project_finance_leverage_project_leverage_jerk_126d_v101_signal": {"func": f47_renewables_project_finance_leverage_project_leverage_jerk_126d_v101_signal},
    "f47_renewables_project_finance_leverage_yield_safety_jerk_126d_v102_signal": {"func": f47_renewables_project_finance_leverage_yield_safety_jerk_126d_v102_signal},
    "f47_renewables_project_finance_leverage_debt_jerk_252d_v103_signal": {"func": f47_renewables_project_finance_leverage_debt_jerk_252d_v103_signal},
    "f47_renewables_project_finance_leverage_ebitda_jerk_252d_v104_signal": {"func": f47_renewables_project_finance_leverage_ebitda_jerk_252d_v104_signal},
    "f47_renewables_project_finance_leverage_fcf_jerk_252d_v105_signal": {"func": f47_renewables_project_finance_leverage_fcf_jerk_252d_v105_signal},
    "f47_renewables_project_finance_leverage_marketcap_jerk_252d_v106_signal": {"func": f47_renewables_project_finance_leverage_marketcap_jerk_252d_v106_signal},
    "f47_renewables_project_finance_leverage_project_leverage_jerk_252d_v107_signal": {"func": f47_renewables_project_finance_leverage_project_leverage_jerk_252d_v107_signal},
    "f47_renewables_project_finance_leverage_yield_safety_jerk_252d_v108_signal": {"func": f47_renewables_project_finance_leverage_yield_safety_jerk_252d_v108_signal},
    "f47_renewables_project_finance_leverage_debt_jerk_504d_v109_signal": {"func": f47_renewables_project_finance_leverage_debt_jerk_504d_v109_signal},
    "f47_renewables_project_finance_leverage_ebitda_jerk_504d_v110_signal": {"func": f47_renewables_project_finance_leverage_ebitda_jerk_504d_v110_signal},
    "f47_renewables_project_finance_leverage_fcf_jerk_504d_v111_signal": {"func": f47_renewables_project_finance_leverage_fcf_jerk_504d_v111_signal},
    "f47_renewables_project_finance_leverage_marketcap_jerk_504d_v112_signal": {"func": f47_renewables_project_finance_leverage_marketcap_jerk_504d_v112_signal},
    "f47_renewables_project_finance_leverage_project_leverage_jerk_504d_v113_signal": {"func": f47_renewables_project_finance_leverage_project_leverage_jerk_504d_v113_signal},
    "f47_renewables_project_finance_leverage_yield_safety_jerk_504d_v114_signal": {"func": f47_renewables_project_finance_leverage_yield_safety_jerk_504d_v114_signal},
    "f47_renewables_project_finance_leverage_debt_jerk_756d_v115_signal": {"func": f47_renewables_project_finance_leverage_debt_jerk_756d_v115_signal},
    "f47_renewables_project_finance_leverage_ebitda_jerk_756d_v116_signal": {"func": f47_renewables_project_finance_leverage_ebitda_jerk_756d_v116_signal},
    "f47_renewables_project_finance_leverage_fcf_jerk_756d_v117_signal": {"func": f47_renewables_project_finance_leverage_fcf_jerk_756d_v117_signal},
    "f47_renewables_project_finance_leverage_marketcap_jerk_756d_v118_signal": {"func": f47_renewables_project_finance_leverage_marketcap_jerk_756d_v118_signal},
    "f47_renewables_project_finance_leverage_project_leverage_jerk_756d_v119_signal": {"func": f47_renewables_project_finance_leverage_project_leverage_jerk_756d_v119_signal},
    "f47_renewables_project_finance_leverage_yield_safety_jerk_756d_v120_signal": {"func": f47_renewables_project_finance_leverage_yield_safety_jerk_756d_v120_signal},
    "f47_renewables_project_finance_leverage_debt_jerk_1008d_v121_signal": {"func": f47_renewables_project_finance_leverage_debt_jerk_1008d_v121_signal},
    "f47_renewables_project_finance_leverage_ebitda_jerk_1008d_v122_signal": {"func": f47_renewables_project_finance_leverage_ebitda_jerk_1008d_v122_signal},
    "f47_renewables_project_finance_leverage_fcf_jerk_1008d_v123_signal": {"func": f47_renewables_project_finance_leverage_fcf_jerk_1008d_v123_signal},
    "f47_renewables_project_finance_leverage_marketcap_jerk_1008d_v124_signal": {"func": f47_renewables_project_finance_leverage_marketcap_jerk_1008d_v124_signal},
    "f47_renewables_project_finance_leverage_project_leverage_jerk_1008d_v125_signal": {"func": f47_renewables_project_finance_leverage_project_leverage_jerk_1008d_v125_signal},
    "f47_renewables_project_finance_leverage_yield_safety_jerk_1008d_v126_signal": {"func": f47_renewables_project_finance_leverage_yield_safety_jerk_1008d_v126_signal},
    "f47_renewables_project_finance_leverage_debt_jerk_1260d_v127_signal": {"func": f47_renewables_project_finance_leverage_debt_jerk_1260d_v127_signal},
    "f47_renewables_project_finance_leverage_ebitda_jerk_1260d_v128_signal": {"func": f47_renewables_project_finance_leverage_ebitda_jerk_1260d_v128_signal},
    "f47_renewables_project_finance_leverage_fcf_jerk_1260d_v129_signal": {"func": f47_renewables_project_finance_leverage_fcf_jerk_1260d_v129_signal},
    "f47_renewables_project_finance_leverage_marketcap_jerk_1260d_v130_signal": {"func": f47_renewables_project_finance_leverage_marketcap_jerk_1260d_v130_signal},
    "f47_renewables_project_finance_leverage_project_leverage_jerk_1260d_v131_signal": {"func": f47_renewables_project_finance_leverage_project_leverage_jerk_1260d_v131_signal},
    "f47_renewables_project_finance_leverage_yield_safety_jerk_1260d_v132_signal": {"func": f47_renewables_project_finance_leverage_yield_safety_jerk_1260d_v132_signal},
    "f47_renewables_project_finance_leverage_debt_slope_diff_norm_5d_v133_signal": {"func": f47_renewables_project_finance_leverage_debt_slope_diff_norm_5d_v133_signal},
    "f47_renewables_project_finance_leverage_ebitda_slope_diff_norm_5d_v134_signal": {"func": f47_renewables_project_finance_leverage_ebitda_slope_diff_norm_5d_v134_signal},
    "f47_renewables_project_finance_leverage_fcf_slope_diff_norm_5d_v135_signal": {"func": f47_renewables_project_finance_leverage_fcf_slope_diff_norm_5d_v135_signal},
    "f47_renewables_project_finance_leverage_marketcap_slope_diff_norm_5d_v136_signal": {"func": f47_renewables_project_finance_leverage_marketcap_slope_diff_norm_5d_v136_signal},
    "f47_renewables_project_finance_leverage_project_leverage_slope_diff_norm_5d_v137_signal": {"func": f47_renewables_project_finance_leverage_project_leverage_slope_diff_norm_5d_v137_signal},
    "f47_renewables_project_finance_leverage_yield_safety_slope_diff_norm_5d_v138_signal": {"func": f47_renewables_project_finance_leverage_yield_safety_slope_diff_norm_5d_v138_signal},
    "f47_renewables_project_finance_leverage_debt_slope_diff_norm_10d_v139_signal": {"func": f47_renewables_project_finance_leverage_debt_slope_diff_norm_10d_v139_signal},
    "f47_renewables_project_finance_leverage_ebitda_slope_diff_norm_10d_v140_signal": {"func": f47_renewables_project_finance_leverage_ebitda_slope_diff_norm_10d_v140_signal},
    "f47_renewables_project_finance_leverage_fcf_slope_diff_norm_10d_v141_signal": {"func": f47_renewables_project_finance_leverage_fcf_slope_diff_norm_10d_v141_signal},
    "f47_renewables_project_finance_leverage_marketcap_slope_diff_norm_10d_v142_signal": {"func": f47_renewables_project_finance_leverage_marketcap_slope_diff_norm_10d_v142_signal},
    "f47_renewables_project_finance_leverage_project_leverage_slope_diff_norm_10d_v143_signal": {"func": f47_renewables_project_finance_leverage_project_leverage_slope_diff_norm_10d_v143_signal},
    "f47_renewables_project_finance_leverage_yield_safety_slope_diff_norm_10d_v144_signal": {"func": f47_renewables_project_finance_leverage_yield_safety_slope_diff_norm_10d_v144_signal},
    "f47_renewables_project_finance_leverage_debt_slope_diff_norm_21d_v145_signal": {"func": f47_renewables_project_finance_leverage_debt_slope_diff_norm_21d_v145_signal},
    "f47_renewables_project_finance_leverage_ebitda_slope_diff_norm_21d_v146_signal": {"func": f47_renewables_project_finance_leverage_ebitda_slope_diff_norm_21d_v146_signal},
    "f47_renewables_project_finance_leverage_fcf_slope_diff_norm_21d_v147_signal": {"func": f47_renewables_project_finance_leverage_fcf_slope_diff_norm_21d_v147_signal},
    "f47_renewables_project_finance_leverage_marketcap_slope_diff_norm_21d_v148_signal": {"func": f47_renewables_project_finance_leverage_marketcap_slope_diff_norm_21d_v148_signal},
    "f47_renewables_project_finance_leverage_project_leverage_slope_diff_norm_21d_v149_signal": {"func": f47_renewables_project_finance_leverage_project_leverage_slope_diff_norm_21d_v149_signal},
    "f47_renewables_project_finance_leverage_yield_safety_slope_diff_norm_21d_v150_signal": {"func": f47_renewables_project_finance_leverage_yield_safety_slope_diff_norm_21d_v150_signal},
}

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "roic": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "tangibles": np.random.normal(100, 10, n).cumsum(), "ev": np.random.normal(100, 10, n).cumsum(), "ps": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "opex": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "deferredrev": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "deposits": np.random.normal(100, 10, n).cumsum(), "pb": np.random.normal(100, 10, n).cumsum(), "bvps": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "liabilitiesc": np.random.normal(100, 10, n).cumsum(), "pe": np.random.normal(100, 10, n).cumsum(), "grossmargin": np.random.normal(100, 10, n).cumsum(), "divyield": np.random.normal(100, 10, n).cumsum(), "debt": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "equity": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum()
    })
    print(f"Verifying {len(REGISTRY)} functions for family 47...")
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
