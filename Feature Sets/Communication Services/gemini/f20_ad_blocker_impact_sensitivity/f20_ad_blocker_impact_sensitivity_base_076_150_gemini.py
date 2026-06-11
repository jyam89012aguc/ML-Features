"""
Family: f20_ad_blocker_impact_sensitivity
Sector: Communication Services
Mathematical Approach: Domain-Specific Fundamentals & Pricing
"""

import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252

def _z(s, w):
    m = s.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = s.rolling(w, min_periods=max(1, w // 2)).std()
    return (s - m) / sd.replace(0, np.nan)

def _rank(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).rank(pct=True) - 0.5

# --- Sophisticated Domain Primitives ---
def _comm_revenue_velocity(revenue, assets, closeadj, w):
    """Velocity of asset turnover adjusted for price momentum. Captures user growth efficiency."""
    return (revenue / assets.replace(0, np.nan)).diff(w) * closeadj.pct_change(w)

def _comm_opex_drag(opex, marketcap, volume, w):
    """Operating expense drag relative to market valuation and volume shock. Proxies talent/content cost inflation."""
    return (opex / marketcap.replace(0, np.nan)) * _z(volume, w)

def _comm_leverage_convexity(ebitda, debt, closeadj, w):
    """Leverage convexity mapping EBITDA generation against debt loads. Ideal for telecom/infrastructure."""
    return np.log((ebitda.replace(0, np.nan) / debt.replace(0, np.nan)).abs() + 1) * closeadj.pct_change(w)

_FEATURES = []

def f20cs_f20_ad_blocker_impact_sensitivity_base_076_150_gemini_v001_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 252d of _comm_leverage_convexity with 126d lookback."""
    raw = _comm_leverage_convexity(ebitda, debt, closeadj, 126)
    result = _rank(raw, 252)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f20cs_f20_ad_blocker_impact_sensitivity_base_076_150_gemini_v001_signal)

def f20cs_f20_ad_blocker_impact_sensitivity_base_076_150_gemini_v002_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 126d of _comm_leverage_convexity with 63d lookback."""
    raw = _comm_leverage_convexity(ebitda, debt, closeadj, 63)
    result = _rank(raw, 126)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f20cs_f20_ad_blocker_impact_sensitivity_base_076_150_gemini_v002_signal)

def f20cs_f20_ad_blocker_impact_sensitivity_base_076_150_gemini_v003_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 20d of _comm_leverage_convexity with 10d lookback."""
    raw = _comm_leverage_convexity(ebitda, debt, closeadj, 10)
    result = _rank(raw, 20)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f20cs_f20_ad_blocker_impact_sensitivity_base_076_150_gemini_v003_signal)

def f20cs_f20_ad_blocker_impact_sensitivity_base_076_150_gemini_v004_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _z over 20d of _comm_leverage_convexity with 10d lookback."""
    raw = _comm_leverage_convexity(ebitda, debt, closeadj, 10)
    result = _z(raw, 20)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f20cs_f20_ad_blocker_impact_sensitivity_base_076_150_gemini_v004_signal)

def f20cs_f20_ad_blocker_impact_sensitivity_base_076_150_gemini_v005_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _z over 42d of _comm_leverage_convexity with 21d lookback."""
    raw = _comm_leverage_convexity(ebitda, debt, closeadj, 21)
    result = _z(raw, 42)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f20cs_f20_ad_blocker_impact_sensitivity_base_076_150_gemini_v005_signal)

def f20cs_f20_ad_blocker_impact_sensitivity_base_076_150_gemini_v006_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _z over 10d of _comm_leverage_convexity with 5d lookback."""
    raw = _comm_leverage_convexity(ebitda, debt, closeadj, 5)
    result = _z(raw, 10)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f20cs_f20_ad_blocker_impact_sensitivity_base_076_150_gemini_v006_signal)

def f20cs_f20_ad_blocker_impact_sensitivity_base_076_150_gemini_v007_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _z over 252d of _comm_leverage_convexity with 126d lookback."""
    raw = _comm_leverage_convexity(ebitda, debt, closeadj, 126)
    result = _z(raw, 252)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f20cs_f20_ad_blocker_impact_sensitivity_base_076_150_gemini_v007_signal)

def f20cs_f20_ad_blocker_impact_sensitivity_base_076_150_gemini_v008_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _z over 10d of _comm_leverage_convexity with 5d lookback."""
    raw = _comm_leverage_convexity(ebitda, debt, closeadj, 5)
    result = _z(raw, 10)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f20cs_f20_ad_blocker_impact_sensitivity_base_076_150_gemini_v008_signal)

def f20cs_f20_ad_blocker_impact_sensitivity_base_076_150_gemini_v009_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _z over 126d of _comm_leverage_convexity with 63d lookback."""
    raw = _comm_leverage_convexity(ebitda, debt, closeadj, 63)
    result = _z(raw, 126)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f20cs_f20_ad_blocker_impact_sensitivity_base_076_150_gemini_v009_signal)

def f20cs_f20_ad_blocker_impact_sensitivity_base_076_150_gemini_v010_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 42d of _comm_leverage_convexity with 21d lookback."""
    raw = _comm_leverage_convexity(ebitda, debt, closeadj, 21)
    result = _rank(raw, 42)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f20cs_f20_ad_blocker_impact_sensitivity_base_076_150_gemini_v010_signal)

def f20cs_f20_ad_blocker_impact_sensitivity_base_076_150_gemini_v011_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _z over 20d of _comm_leverage_convexity with 10d lookback."""
    raw = _comm_leverage_convexity(ebitda, debt, closeadj, 10)
    result = _z(raw, 20)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f20cs_f20_ad_blocker_impact_sensitivity_base_076_150_gemini_v011_signal)

def f20cs_f20_ad_blocker_impact_sensitivity_base_076_150_gemini_v012_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 42d of _comm_leverage_convexity with 21d lookback."""
    raw = _comm_leverage_convexity(ebitda, debt, closeadj, 21)
    result = _rank(raw, 42)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f20cs_f20_ad_blocker_impact_sensitivity_base_076_150_gemini_v012_signal)

def f20cs_f20_ad_blocker_impact_sensitivity_base_076_150_gemini_v013_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _z over 126d of _comm_leverage_convexity with 63d lookback."""
    raw = _comm_leverage_convexity(ebitda, debt, closeadj, 63)
    result = _z(raw, 126)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f20cs_f20_ad_blocker_impact_sensitivity_base_076_150_gemini_v013_signal)

def f20cs_f20_ad_blocker_impact_sensitivity_base_076_150_gemini_v014_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 42d of _comm_leverage_convexity with 21d lookback."""
    raw = _comm_leverage_convexity(ebitda, debt, closeadj, 21)
    result = _rank(raw, 42)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f20cs_f20_ad_blocker_impact_sensitivity_base_076_150_gemini_v014_signal)

def f20cs_f20_ad_blocker_impact_sensitivity_base_076_150_gemini_v015_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 504d of _comm_leverage_convexity with 252d lookback."""
    raw = _comm_leverage_convexity(ebitda, debt, closeadj, 252)
    result = _rank(raw, 504)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f20cs_f20_ad_blocker_impact_sensitivity_base_076_150_gemini_v015_signal)

def f20cs_f20_ad_blocker_impact_sensitivity_base_076_150_gemini_v016_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _z over 10d of _comm_leverage_convexity with 5d lookback."""
    raw = _comm_leverage_convexity(ebitda, debt, closeadj, 5)
    result = _z(raw, 10)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f20cs_f20_ad_blocker_impact_sensitivity_base_076_150_gemini_v016_signal)

def f20cs_f20_ad_blocker_impact_sensitivity_base_076_150_gemini_v017_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _z over 504d of _comm_leverage_convexity with 252d lookback."""
    raw = _comm_leverage_convexity(ebitda, debt, closeadj, 252)
    result = _z(raw, 504)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f20cs_f20_ad_blocker_impact_sensitivity_base_076_150_gemini_v017_signal)

def f20cs_f20_ad_blocker_impact_sensitivity_base_076_150_gemini_v018_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _z over 504d of _comm_leverage_convexity with 252d lookback."""
    raw = _comm_leverage_convexity(ebitda, debt, closeadj, 252)
    result = _z(raw, 504)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f20cs_f20_ad_blocker_impact_sensitivity_base_076_150_gemini_v018_signal)

def f20cs_f20_ad_blocker_impact_sensitivity_base_076_150_gemini_v019_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 504d of _comm_leverage_convexity with 252d lookback."""
    raw = _comm_leverage_convexity(ebitda, debt, closeadj, 252)
    result = _rank(raw, 504)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f20cs_f20_ad_blocker_impact_sensitivity_base_076_150_gemini_v019_signal)

def f20cs_f20_ad_blocker_impact_sensitivity_base_076_150_gemini_v020_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _z over 126d of _comm_leverage_convexity with 63d lookback."""
    raw = _comm_leverage_convexity(ebitda, debt, closeadj, 63)
    result = _z(raw, 126)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f20cs_f20_ad_blocker_impact_sensitivity_base_076_150_gemini_v020_signal)

def f20cs_f20_ad_blocker_impact_sensitivity_base_076_150_gemini_v021_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 10d of _comm_leverage_convexity with 5d lookback."""
    raw = _comm_leverage_convexity(ebitda, debt, closeadj, 5)
    result = _rank(raw, 10)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f20cs_f20_ad_blocker_impact_sensitivity_base_076_150_gemini_v021_signal)

def f20cs_f20_ad_blocker_impact_sensitivity_base_076_150_gemini_v022_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _z over 126d of _comm_leverage_convexity with 63d lookback."""
    raw = _comm_leverage_convexity(ebitda, debt, closeadj, 63)
    result = _z(raw, 126)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f20cs_f20_ad_blocker_impact_sensitivity_base_076_150_gemini_v022_signal)

def f20cs_f20_ad_blocker_impact_sensitivity_base_076_150_gemini_v023_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _z over 10d of _comm_leverage_convexity with 5d lookback."""
    raw = _comm_leverage_convexity(ebitda, debt, closeadj, 5)
    result = _z(raw, 10)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f20cs_f20_ad_blocker_impact_sensitivity_base_076_150_gemini_v023_signal)

def f20cs_f20_ad_blocker_impact_sensitivity_base_076_150_gemini_v024_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 42d of _comm_leverage_convexity with 21d lookback."""
    raw = _comm_leverage_convexity(ebitda, debt, closeadj, 21)
    result = _rank(raw, 42)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f20cs_f20_ad_blocker_impact_sensitivity_base_076_150_gemini_v024_signal)

def f20cs_f20_ad_blocker_impact_sensitivity_base_076_150_gemini_v025_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 10d of _comm_leverage_convexity with 5d lookback."""
    raw = _comm_leverage_convexity(ebitda, debt, closeadj, 5)
    result = _rank(raw, 10)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f20cs_f20_ad_blocker_impact_sensitivity_base_076_150_gemini_v025_signal)

def f20cs_f20_ad_blocker_impact_sensitivity_base_076_150_gemini_v026_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 42d of _comm_leverage_convexity with 21d lookback."""
    raw = _comm_leverage_convexity(ebitda, debt, closeadj, 21)
    result = _rank(raw, 42)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f20cs_f20_ad_blocker_impact_sensitivity_base_076_150_gemini_v026_signal)

def f20cs_f20_ad_blocker_impact_sensitivity_base_076_150_gemini_v027_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _z over 42d of _comm_leverage_convexity with 21d lookback."""
    raw = _comm_leverage_convexity(ebitda, debt, closeadj, 21)
    result = _z(raw, 42)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f20cs_f20_ad_blocker_impact_sensitivity_base_076_150_gemini_v027_signal)

def f20cs_f20_ad_blocker_impact_sensitivity_base_076_150_gemini_v028_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _z over 126d of _comm_leverage_convexity with 63d lookback."""
    raw = _comm_leverage_convexity(ebitda, debt, closeadj, 63)
    result = _z(raw, 126)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f20cs_f20_ad_blocker_impact_sensitivity_base_076_150_gemini_v028_signal)

def f20cs_f20_ad_blocker_impact_sensitivity_base_076_150_gemini_v029_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 504d of _comm_leverage_convexity with 252d lookback."""
    raw = _comm_leverage_convexity(ebitda, debt, closeadj, 252)
    result = _rank(raw, 504)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f20cs_f20_ad_blocker_impact_sensitivity_base_076_150_gemini_v029_signal)

def f20cs_f20_ad_blocker_impact_sensitivity_base_076_150_gemini_v030_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 504d of _comm_leverage_convexity with 252d lookback."""
    raw = _comm_leverage_convexity(ebitda, debt, closeadj, 252)
    result = _rank(raw, 504)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f20cs_f20_ad_blocker_impact_sensitivity_base_076_150_gemini_v030_signal)

def f20cs_f20_ad_blocker_impact_sensitivity_base_076_150_gemini_v031_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 10d of _comm_leverage_convexity with 5d lookback."""
    raw = _comm_leverage_convexity(ebitda, debt, closeadj, 5)
    result = _rank(raw, 10)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f20cs_f20_ad_blocker_impact_sensitivity_base_076_150_gemini_v031_signal)

def f20cs_f20_ad_blocker_impact_sensitivity_base_076_150_gemini_v032_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _z over 126d of _comm_leverage_convexity with 63d lookback."""
    raw = _comm_leverage_convexity(ebitda, debt, closeadj, 63)
    result = _z(raw, 126)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f20cs_f20_ad_blocker_impact_sensitivity_base_076_150_gemini_v032_signal)

def f20cs_f20_ad_blocker_impact_sensitivity_base_076_150_gemini_v033_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 252d of _comm_leverage_convexity with 126d lookback."""
    raw = _comm_leverage_convexity(ebitda, debt, closeadj, 126)
    result = _rank(raw, 252)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f20cs_f20_ad_blocker_impact_sensitivity_base_076_150_gemini_v033_signal)

def f20cs_f20_ad_blocker_impact_sensitivity_base_076_150_gemini_v034_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 42d of _comm_leverage_convexity with 21d lookback."""
    raw = _comm_leverage_convexity(ebitda, debt, closeadj, 21)
    result = _rank(raw, 42)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f20cs_f20_ad_blocker_impact_sensitivity_base_076_150_gemini_v034_signal)

def f20cs_f20_ad_blocker_impact_sensitivity_base_076_150_gemini_v035_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 252d of _comm_leverage_convexity with 126d lookback."""
    raw = _comm_leverage_convexity(ebitda, debt, closeadj, 126)
    result = _rank(raw, 252)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f20cs_f20_ad_blocker_impact_sensitivity_base_076_150_gemini_v035_signal)

def f20cs_f20_ad_blocker_impact_sensitivity_base_076_150_gemini_v036_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _z over 42d of _comm_leverage_convexity with 21d lookback."""
    raw = _comm_leverage_convexity(ebitda, debt, closeadj, 21)
    result = _z(raw, 42)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f20cs_f20_ad_blocker_impact_sensitivity_base_076_150_gemini_v036_signal)

def f20cs_f20_ad_blocker_impact_sensitivity_base_076_150_gemini_v037_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _z over 20d of _comm_leverage_convexity with 10d lookback."""
    raw = _comm_leverage_convexity(ebitda, debt, closeadj, 10)
    result = _z(raw, 20)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f20cs_f20_ad_blocker_impact_sensitivity_base_076_150_gemini_v037_signal)

def f20cs_f20_ad_blocker_impact_sensitivity_base_076_150_gemini_v038_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 504d of _comm_leverage_convexity with 252d lookback."""
    raw = _comm_leverage_convexity(ebitda, debt, closeadj, 252)
    result = _rank(raw, 504)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f20cs_f20_ad_blocker_impact_sensitivity_base_076_150_gemini_v038_signal)

def f20cs_f20_ad_blocker_impact_sensitivity_base_076_150_gemini_v039_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _z over 252d of _comm_leverage_convexity with 126d lookback."""
    raw = _comm_leverage_convexity(ebitda, debt, closeadj, 126)
    result = _z(raw, 252)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f20cs_f20_ad_blocker_impact_sensitivity_base_076_150_gemini_v039_signal)

def f20cs_f20_ad_blocker_impact_sensitivity_base_076_150_gemini_v040_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 10d of _comm_leverage_convexity with 5d lookback."""
    raw = _comm_leverage_convexity(ebitda, debt, closeadj, 5)
    result = _rank(raw, 10)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f20cs_f20_ad_blocker_impact_sensitivity_base_076_150_gemini_v040_signal)

def f20cs_f20_ad_blocker_impact_sensitivity_base_076_150_gemini_v041_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _z over 20d of _comm_leverage_convexity with 10d lookback."""
    raw = _comm_leverage_convexity(ebitda, debt, closeadj, 10)
    result = _z(raw, 20)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f20cs_f20_ad_blocker_impact_sensitivity_base_076_150_gemini_v041_signal)

def f20cs_f20_ad_blocker_impact_sensitivity_base_076_150_gemini_v042_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _z over 126d of _comm_leverage_convexity with 63d lookback."""
    raw = _comm_leverage_convexity(ebitda, debt, closeadj, 63)
    result = _z(raw, 126)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f20cs_f20_ad_blocker_impact_sensitivity_base_076_150_gemini_v042_signal)

def f20cs_f20_ad_blocker_impact_sensitivity_base_076_150_gemini_v043_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 42d of _comm_leverage_convexity with 21d lookback."""
    raw = _comm_leverage_convexity(ebitda, debt, closeadj, 21)
    result = _rank(raw, 42)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f20cs_f20_ad_blocker_impact_sensitivity_base_076_150_gemini_v043_signal)

def f20cs_f20_ad_blocker_impact_sensitivity_base_076_150_gemini_v044_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 126d of _comm_leverage_convexity with 63d lookback."""
    raw = _comm_leverage_convexity(ebitda, debt, closeadj, 63)
    result = _rank(raw, 126)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f20cs_f20_ad_blocker_impact_sensitivity_base_076_150_gemini_v044_signal)

def f20cs_f20_ad_blocker_impact_sensitivity_base_076_150_gemini_v045_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 252d of _comm_leverage_convexity with 126d lookback."""
    raw = _comm_leverage_convexity(ebitda, debt, closeadj, 126)
    result = _rank(raw, 252)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f20cs_f20_ad_blocker_impact_sensitivity_base_076_150_gemini_v045_signal)

def f20cs_f20_ad_blocker_impact_sensitivity_base_076_150_gemini_v046_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 20d of _comm_leverage_convexity with 10d lookback."""
    raw = _comm_leverage_convexity(ebitda, debt, closeadj, 10)
    result = _rank(raw, 20)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f20cs_f20_ad_blocker_impact_sensitivity_base_076_150_gemini_v046_signal)

def f20cs_f20_ad_blocker_impact_sensitivity_base_076_150_gemini_v047_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 42d of _comm_leverage_convexity with 21d lookback."""
    raw = _comm_leverage_convexity(ebitda, debt, closeadj, 21)
    result = _rank(raw, 42)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f20cs_f20_ad_blocker_impact_sensitivity_base_076_150_gemini_v047_signal)

def f20cs_f20_ad_blocker_impact_sensitivity_base_076_150_gemini_v048_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _z over 252d of _comm_leverage_convexity with 126d lookback."""
    raw = _comm_leverage_convexity(ebitda, debt, closeadj, 126)
    result = _z(raw, 252)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f20cs_f20_ad_blocker_impact_sensitivity_base_076_150_gemini_v048_signal)

def f20cs_f20_ad_blocker_impact_sensitivity_base_076_150_gemini_v049_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _z over 126d of _comm_leverage_convexity with 63d lookback."""
    raw = _comm_leverage_convexity(ebitda, debt, closeadj, 63)
    result = _z(raw, 126)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f20cs_f20_ad_blocker_impact_sensitivity_base_076_150_gemini_v049_signal)

def f20cs_f20_ad_blocker_impact_sensitivity_base_076_150_gemini_v050_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 20d of _comm_leverage_convexity with 10d lookback."""
    raw = _comm_leverage_convexity(ebitda, debt, closeadj, 10)
    result = _rank(raw, 20)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f20cs_f20_ad_blocker_impact_sensitivity_base_076_150_gemini_v050_signal)

def f20cs_f20_ad_blocker_impact_sensitivity_base_076_150_gemini_v051_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _z over 252d of _comm_leverage_convexity with 126d lookback."""
    raw = _comm_leverage_convexity(ebitda, debt, closeadj, 126)
    result = _z(raw, 252)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f20cs_f20_ad_blocker_impact_sensitivity_base_076_150_gemini_v051_signal)

def f20cs_f20_ad_blocker_impact_sensitivity_base_076_150_gemini_v052_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 42d of _comm_leverage_convexity with 21d lookback."""
    raw = _comm_leverage_convexity(ebitda, debt, closeadj, 21)
    result = _rank(raw, 42)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f20cs_f20_ad_blocker_impact_sensitivity_base_076_150_gemini_v052_signal)

def f20cs_f20_ad_blocker_impact_sensitivity_base_076_150_gemini_v053_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _z over 10d of _comm_leverage_convexity with 5d lookback."""
    raw = _comm_leverage_convexity(ebitda, debt, closeadj, 5)
    result = _z(raw, 10)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f20cs_f20_ad_blocker_impact_sensitivity_base_076_150_gemini_v053_signal)

def f20cs_f20_ad_blocker_impact_sensitivity_base_076_150_gemini_v054_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _z over 42d of _comm_leverage_convexity with 21d lookback."""
    raw = _comm_leverage_convexity(ebitda, debt, closeadj, 21)
    result = _z(raw, 42)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f20cs_f20_ad_blocker_impact_sensitivity_base_076_150_gemini_v054_signal)

def f20cs_f20_ad_blocker_impact_sensitivity_base_076_150_gemini_v055_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 42d of _comm_leverage_convexity with 21d lookback."""
    raw = _comm_leverage_convexity(ebitda, debt, closeadj, 21)
    result = _rank(raw, 42)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f20cs_f20_ad_blocker_impact_sensitivity_base_076_150_gemini_v055_signal)

def f20cs_f20_ad_blocker_impact_sensitivity_base_076_150_gemini_v056_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 126d of _comm_leverage_convexity with 63d lookback."""
    raw = _comm_leverage_convexity(ebitda, debt, closeadj, 63)
    result = _rank(raw, 126)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f20cs_f20_ad_blocker_impact_sensitivity_base_076_150_gemini_v056_signal)

def f20cs_f20_ad_blocker_impact_sensitivity_base_076_150_gemini_v057_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _z over 126d of _comm_leverage_convexity with 63d lookback."""
    raw = _comm_leverage_convexity(ebitda, debt, closeadj, 63)
    result = _z(raw, 126)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f20cs_f20_ad_blocker_impact_sensitivity_base_076_150_gemini_v057_signal)

def f20cs_f20_ad_blocker_impact_sensitivity_base_076_150_gemini_v058_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _z over 504d of _comm_leverage_convexity with 252d lookback."""
    raw = _comm_leverage_convexity(ebitda, debt, closeadj, 252)
    result = _z(raw, 504)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f20cs_f20_ad_blocker_impact_sensitivity_base_076_150_gemini_v058_signal)

def f20cs_f20_ad_blocker_impact_sensitivity_base_076_150_gemini_v059_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _z over 252d of _comm_leverage_convexity with 126d lookback."""
    raw = _comm_leverage_convexity(ebitda, debt, closeadj, 126)
    result = _z(raw, 252)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f20cs_f20_ad_blocker_impact_sensitivity_base_076_150_gemini_v059_signal)

def f20cs_f20_ad_blocker_impact_sensitivity_base_076_150_gemini_v060_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 42d of _comm_leverage_convexity with 21d lookback."""
    raw = _comm_leverage_convexity(ebitda, debt, closeadj, 21)
    result = _rank(raw, 42)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f20cs_f20_ad_blocker_impact_sensitivity_base_076_150_gemini_v060_signal)

def f20cs_f20_ad_blocker_impact_sensitivity_base_076_150_gemini_v061_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _z over 20d of _comm_leverage_convexity with 10d lookback."""
    raw = _comm_leverage_convexity(ebitda, debt, closeadj, 10)
    result = _z(raw, 20)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f20cs_f20_ad_blocker_impact_sensitivity_base_076_150_gemini_v061_signal)

def f20cs_f20_ad_blocker_impact_sensitivity_base_076_150_gemini_v062_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _z over 42d of _comm_leverage_convexity with 21d lookback."""
    raw = _comm_leverage_convexity(ebitda, debt, closeadj, 21)
    result = _z(raw, 42)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f20cs_f20_ad_blocker_impact_sensitivity_base_076_150_gemini_v062_signal)

def f20cs_f20_ad_blocker_impact_sensitivity_base_076_150_gemini_v063_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 20d of _comm_leverage_convexity with 10d lookback."""
    raw = _comm_leverage_convexity(ebitda, debt, closeadj, 10)
    result = _rank(raw, 20)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f20cs_f20_ad_blocker_impact_sensitivity_base_076_150_gemini_v063_signal)

def f20cs_f20_ad_blocker_impact_sensitivity_base_076_150_gemini_v064_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 126d of _comm_leverage_convexity with 63d lookback."""
    raw = _comm_leverage_convexity(ebitda, debt, closeadj, 63)
    result = _rank(raw, 126)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f20cs_f20_ad_blocker_impact_sensitivity_base_076_150_gemini_v064_signal)

def f20cs_f20_ad_blocker_impact_sensitivity_base_076_150_gemini_v065_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _z over 126d of _comm_leverage_convexity with 63d lookback."""
    raw = _comm_leverage_convexity(ebitda, debt, closeadj, 63)
    result = _z(raw, 126)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f20cs_f20_ad_blocker_impact_sensitivity_base_076_150_gemini_v065_signal)

def f20cs_f20_ad_blocker_impact_sensitivity_base_076_150_gemini_v066_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _z over 42d of _comm_leverage_convexity with 21d lookback."""
    raw = _comm_leverage_convexity(ebitda, debt, closeadj, 21)
    result = _z(raw, 42)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f20cs_f20_ad_blocker_impact_sensitivity_base_076_150_gemini_v066_signal)

def f20cs_f20_ad_blocker_impact_sensitivity_base_076_150_gemini_v067_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 126d of _comm_leverage_convexity with 63d lookback."""
    raw = _comm_leverage_convexity(ebitda, debt, closeadj, 63)
    result = _rank(raw, 126)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f20cs_f20_ad_blocker_impact_sensitivity_base_076_150_gemini_v067_signal)

def f20cs_f20_ad_blocker_impact_sensitivity_base_076_150_gemini_v068_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 10d of _comm_leverage_convexity with 5d lookback."""
    raw = _comm_leverage_convexity(ebitda, debt, closeadj, 5)
    result = _rank(raw, 10)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f20cs_f20_ad_blocker_impact_sensitivity_base_076_150_gemini_v068_signal)

def f20cs_f20_ad_blocker_impact_sensitivity_base_076_150_gemini_v069_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 20d of _comm_leverage_convexity with 10d lookback."""
    raw = _comm_leverage_convexity(ebitda, debt, closeadj, 10)
    result = _rank(raw, 20)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f20cs_f20_ad_blocker_impact_sensitivity_base_076_150_gemini_v069_signal)

def f20cs_f20_ad_blocker_impact_sensitivity_base_076_150_gemini_v070_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _z over 126d of _comm_leverage_convexity with 63d lookback."""
    raw = _comm_leverage_convexity(ebitda, debt, closeadj, 63)
    result = _z(raw, 126)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f20cs_f20_ad_blocker_impact_sensitivity_base_076_150_gemini_v070_signal)

def f20cs_f20_ad_blocker_impact_sensitivity_base_076_150_gemini_v071_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _z over 10d of _comm_leverage_convexity with 5d lookback."""
    raw = _comm_leverage_convexity(ebitda, debt, closeadj, 5)
    result = _z(raw, 10)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f20cs_f20_ad_blocker_impact_sensitivity_base_076_150_gemini_v071_signal)

def f20cs_f20_ad_blocker_impact_sensitivity_base_076_150_gemini_v072_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 10d of _comm_leverage_convexity with 5d lookback."""
    raw = _comm_leverage_convexity(ebitda, debt, closeadj, 5)
    result = _rank(raw, 10)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f20cs_f20_ad_blocker_impact_sensitivity_base_076_150_gemini_v072_signal)

def f20cs_f20_ad_blocker_impact_sensitivity_base_076_150_gemini_v073_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 252d of _comm_leverage_convexity with 126d lookback."""
    raw = _comm_leverage_convexity(ebitda, debt, closeadj, 126)
    result = _rank(raw, 252)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f20cs_f20_ad_blocker_impact_sensitivity_base_076_150_gemini_v073_signal)

def f20cs_f20_ad_blocker_impact_sensitivity_base_076_150_gemini_v074_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 10d of _comm_leverage_convexity with 5d lookback."""
    raw = _comm_leverage_convexity(ebitda, debt, closeadj, 5)
    result = _rank(raw, 10)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f20cs_f20_ad_blocker_impact_sensitivity_base_076_150_gemini_v074_signal)

def f20cs_f20_ad_blocker_impact_sensitivity_base_076_150_gemini_v075_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _z over 42d of _comm_leverage_convexity with 21d lookback."""
    raw = _comm_leverage_convexity(ebitda, debt, closeadj, 21)
    result = _z(raw, 42)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f20cs_f20_ad_blocker_impact_sensitivity_base_076_150_gemini_v075_signal)


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]

REGISTRY = {fn.__name__: {'inputs': _inputs_for(fn), 'func': fn} for fn in _FEATURES}

if __name__ == '__main__':
    n = 1000
    cols = {
        'revenue': pd.Series(np.random.normal(100, 10, n), name='revenue'),
        'assets': pd.Series(np.random.normal(100, 10, n), name='assets'),
        'closeadj': pd.Series(np.random.normal(100, 10, n), name='closeadj'),
        'opex': pd.Series(np.random.normal(100, 10, n), name='opex'),
        'marketcap': pd.Series(np.random.normal(100, 10, n), name='marketcap'),
        'volume': pd.Series(np.random.normal(100, 10, n), name='volume'),
        'ebitda': pd.Series(np.random.normal(100, 10, n), name='ebitda'),
        'debt': pd.Series(np.random.normal(100, 10, n), name='debt')
    }
    n_features = 0
    for name, meta in REGISTRY.items():
        fn = meta['func']
        args = [cols[c] for c in meta['inputs']]
        y = fn(*args)
        if not y.isna().all():
            n_features += 1
    print(f'OK: {n_features} features pass')
