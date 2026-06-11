"""
Family: f46_cinema_exhibition_box_office_momentum
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

def f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v001_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 252d of _comm_opex_drag with 126d lookback."""
    raw = _comm_opex_drag(opex, marketcap, volume, 126).diff(5).diff(5)
    result = _rank(raw, 252)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v001_signal)

def f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v002_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 20d of _comm_revenue_velocity with 10d lookback."""
    raw = _comm_revenue_velocity(revenue, assets, closeadj, 10).diff(5).diff(5)
    result = _rank(raw, 20)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v002_signal)

def f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v003_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 126d of _comm_revenue_velocity with 63d lookback."""
    raw = _comm_revenue_velocity(revenue, assets, closeadj, 63).diff(5).diff(5)
    result = _rank(raw, 126)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v003_signal)

def f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v004_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 126d of _comm_revenue_velocity with 63d lookback."""
    raw = _comm_revenue_velocity(revenue, assets, closeadj, 63).diff(5).diff(5)
    result = _rank(raw, 126)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v004_signal)

def f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v005_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 252d of _comm_revenue_velocity with 126d lookback."""
    raw = _comm_revenue_velocity(revenue, assets, closeadj, 126).diff(5).diff(5)
    result = _rank(raw, 252)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v005_signal)

def f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v006_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 20d of _comm_revenue_velocity with 10d lookback."""
    raw = _comm_revenue_velocity(revenue, assets, closeadj, 10).diff(5).diff(5)
    result = _rank(raw, 20)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v006_signal)

def f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v007_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 20d of _comm_revenue_velocity with 10d lookback."""
    raw = _comm_revenue_velocity(revenue, assets, closeadj, 10).diff(5).diff(5)
    result = _rank(raw, 20)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v007_signal)

def f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v008_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 252d of _comm_leverage_convexity with 126d lookback."""
    raw = _comm_leverage_convexity(ebitda, debt, closeadj, 126).diff(5).diff(5)
    result = _rank(raw, 252)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v008_signal)

def f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v009_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 20d of _comm_leverage_convexity with 10d lookback."""
    raw = _comm_leverage_convexity(ebitda, debt, closeadj, 10).diff(5).diff(5)
    result = _rank(raw, 20)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v009_signal)

def f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v010_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 504d of _comm_revenue_velocity with 252d lookback."""
    raw = _comm_revenue_velocity(revenue, assets, closeadj, 252).diff(5).diff(5)
    result = _rank(raw, 504)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v010_signal)

def f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v011_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 126d of _comm_opex_drag with 63d lookback."""
    raw = _comm_opex_drag(opex, marketcap, volume, 63).diff(5).diff(5)
    result = _rank(raw, 126)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v011_signal)

def f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v012_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 10d of _comm_revenue_velocity with 5d lookback."""
    raw = _comm_revenue_velocity(revenue, assets, closeadj, 5).diff(5).diff(5)
    result = _rank(raw, 10)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v012_signal)

def f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v013_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 42d of _comm_leverage_convexity with 21d lookback."""
    raw = _comm_leverage_convexity(ebitda, debt, closeadj, 21).diff(5).diff(5)
    result = _rank(raw, 42)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v013_signal)

def f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v014_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 252d of _comm_revenue_velocity with 126d lookback."""
    raw = _comm_revenue_velocity(revenue, assets, closeadj, 126).diff(5).diff(5)
    result = _rank(raw, 252)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v014_signal)

def f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v015_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 126d of _comm_leverage_convexity with 63d lookback."""
    raw = _comm_leverage_convexity(ebitda, debt, closeadj, 63).diff(5).diff(5)
    result = _rank(raw, 126)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v015_signal)

def f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v016_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 10d of _comm_opex_drag with 5d lookback."""
    raw = _comm_opex_drag(opex, marketcap, volume, 5).diff(5).diff(5)
    result = _rank(raw, 10)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v016_signal)

def f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v017_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 252d of _comm_leverage_convexity with 126d lookback."""
    raw = _comm_leverage_convexity(ebitda, debt, closeadj, 126).diff(5).diff(5)
    result = _rank(raw, 252)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v017_signal)

def f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v018_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 20d of _comm_revenue_velocity with 10d lookback."""
    raw = _comm_revenue_velocity(revenue, assets, closeadj, 10).diff(5).diff(5)
    result = _rank(raw, 20)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v018_signal)

def f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v019_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 504d of _comm_leverage_convexity with 252d lookback."""
    raw = _comm_leverage_convexity(ebitda, debt, closeadj, 252).diff(5).diff(5)
    result = _rank(raw, 504)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v019_signal)

def f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v020_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 10d of _comm_leverage_convexity with 5d lookback."""
    raw = _comm_leverage_convexity(ebitda, debt, closeadj, 5).diff(5).diff(5)
    result = _rank(raw, 10)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v020_signal)

def f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v021_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 10d of _comm_revenue_velocity with 5d lookback."""
    raw = _comm_revenue_velocity(revenue, assets, closeadj, 5).diff(5).diff(5)
    result = _rank(raw, 10)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v021_signal)

def f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v022_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 20d of _comm_leverage_convexity with 10d lookback."""
    raw = _comm_leverage_convexity(ebitda, debt, closeadj, 10).diff(5).diff(5)
    result = _rank(raw, 20)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v022_signal)

def f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v023_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 10d of _comm_revenue_velocity with 5d lookback."""
    raw = _comm_revenue_velocity(revenue, assets, closeadj, 5).diff(5).diff(5)
    result = _rank(raw, 10)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v023_signal)

def f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v024_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 504d of _comm_revenue_velocity with 252d lookback."""
    raw = _comm_revenue_velocity(revenue, assets, closeadj, 252).diff(5).diff(5)
    result = _rank(raw, 504)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v024_signal)

def f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v025_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 20d of _comm_revenue_velocity with 10d lookback."""
    raw = _comm_revenue_velocity(revenue, assets, closeadj, 10).diff(5).diff(5)
    result = _rank(raw, 20)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v025_signal)

def f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v026_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 20d of _comm_leverage_convexity with 10d lookback."""
    raw = _comm_leverage_convexity(ebitda, debt, closeadj, 10).diff(5).diff(5)
    result = _rank(raw, 20)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v026_signal)

def f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v027_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 252d of _comm_leverage_convexity with 126d lookback."""
    raw = _comm_leverage_convexity(ebitda, debt, closeadj, 126).diff(5).diff(5)
    result = _rank(raw, 252)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v027_signal)

def f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v028_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 10d of _comm_leverage_convexity with 5d lookback."""
    raw = _comm_leverage_convexity(ebitda, debt, closeadj, 5).diff(5).diff(5)
    result = _rank(raw, 10)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v028_signal)

def f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v029_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 504d of _comm_leverage_convexity with 252d lookback."""
    raw = _comm_leverage_convexity(ebitda, debt, closeadj, 252).diff(5).diff(5)
    result = _rank(raw, 504)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v029_signal)

def f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v030_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 42d of _comm_leverage_convexity with 21d lookback."""
    raw = _comm_leverage_convexity(ebitda, debt, closeadj, 21).diff(5).diff(5)
    result = _rank(raw, 42)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v030_signal)

def f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v031_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 42d of _comm_opex_drag with 21d lookback."""
    raw = _comm_opex_drag(opex, marketcap, volume, 21).diff(5).diff(5)
    result = _rank(raw, 42)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v031_signal)

def f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v032_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 504d of _comm_opex_drag with 252d lookback."""
    raw = _comm_opex_drag(opex, marketcap, volume, 252).diff(5).diff(5)
    result = _rank(raw, 504)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v032_signal)

def f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v033_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 42d of _comm_leverage_convexity with 21d lookback."""
    raw = _comm_leverage_convexity(ebitda, debt, closeadj, 21).diff(5).diff(5)
    result = _rank(raw, 42)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v033_signal)

def f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v034_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 504d of _comm_opex_drag with 252d lookback."""
    raw = _comm_opex_drag(opex, marketcap, volume, 252).diff(5).diff(5)
    result = _rank(raw, 504)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v034_signal)

def f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v035_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 20d of _comm_opex_drag with 10d lookback."""
    raw = _comm_opex_drag(opex, marketcap, volume, 10).diff(5).diff(5)
    result = _rank(raw, 20)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v035_signal)

def f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v036_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 504d of _comm_opex_drag with 252d lookback."""
    raw = _comm_opex_drag(opex, marketcap, volume, 252).diff(5).diff(5)
    result = _rank(raw, 504)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v036_signal)

def f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v037_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 504d of _comm_opex_drag with 252d lookback."""
    raw = _comm_opex_drag(opex, marketcap, volume, 252).diff(5).diff(5)
    result = _rank(raw, 504)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v037_signal)

def f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v038_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 126d of _comm_leverage_convexity with 63d lookback."""
    raw = _comm_leverage_convexity(ebitda, debt, closeadj, 63).diff(5).diff(5)
    result = _rank(raw, 126)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v038_signal)

def f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v039_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 126d of _comm_opex_drag with 63d lookback."""
    raw = _comm_opex_drag(opex, marketcap, volume, 63).diff(5).diff(5)
    result = _rank(raw, 126)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v039_signal)

def f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v040_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 504d of _comm_leverage_convexity with 252d lookback."""
    raw = _comm_leverage_convexity(ebitda, debt, closeadj, 252).diff(5).diff(5)
    result = _rank(raw, 504)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v040_signal)

def f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v041_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 126d of _comm_opex_drag with 63d lookback."""
    raw = _comm_opex_drag(opex, marketcap, volume, 63).diff(5).diff(5)
    result = _rank(raw, 126)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v041_signal)

def f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v042_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 126d of _comm_revenue_velocity with 63d lookback."""
    raw = _comm_revenue_velocity(revenue, assets, closeadj, 63).diff(5).diff(5)
    result = _rank(raw, 126)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v042_signal)

def f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v043_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 10d of _comm_revenue_velocity with 5d lookback."""
    raw = _comm_revenue_velocity(revenue, assets, closeadj, 5).diff(5).diff(5)
    result = _rank(raw, 10)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v043_signal)

def f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v044_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 20d of _comm_revenue_velocity with 10d lookback."""
    raw = _comm_revenue_velocity(revenue, assets, closeadj, 10).diff(5).diff(5)
    result = _rank(raw, 20)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v044_signal)

def f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v045_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 126d of _comm_revenue_velocity with 63d lookback."""
    raw = _comm_revenue_velocity(revenue, assets, closeadj, 63).diff(5).diff(5)
    result = _rank(raw, 126)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v045_signal)

def f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v046_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 252d of _comm_revenue_velocity with 126d lookback."""
    raw = _comm_revenue_velocity(revenue, assets, closeadj, 126).diff(5).diff(5)
    result = _rank(raw, 252)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v046_signal)

def f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v047_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 504d of _comm_opex_drag with 252d lookback."""
    raw = _comm_opex_drag(opex, marketcap, volume, 252).diff(5).diff(5)
    result = _rank(raw, 504)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v047_signal)

def f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v048_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 252d of _comm_revenue_velocity with 126d lookback."""
    raw = _comm_revenue_velocity(revenue, assets, closeadj, 126).diff(5).diff(5)
    result = _rank(raw, 252)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v048_signal)

def f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v049_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 20d of _comm_opex_drag with 10d lookback."""
    raw = _comm_opex_drag(opex, marketcap, volume, 10).diff(5).diff(5)
    result = _rank(raw, 20)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v049_signal)

def f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v050_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 126d of _comm_opex_drag with 63d lookback."""
    raw = _comm_opex_drag(opex, marketcap, volume, 63).diff(5).diff(5)
    result = _rank(raw, 126)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v050_signal)

def f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v051_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 252d of _comm_revenue_velocity with 126d lookback."""
    raw = _comm_revenue_velocity(revenue, assets, closeadj, 126).diff(5).diff(5)
    result = _rank(raw, 252)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v051_signal)

def f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v052_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 252d of _comm_opex_drag with 126d lookback."""
    raw = _comm_opex_drag(opex, marketcap, volume, 126).diff(5).diff(5)
    result = _rank(raw, 252)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v052_signal)

def f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v053_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 252d of _comm_opex_drag with 126d lookback."""
    raw = _comm_opex_drag(opex, marketcap, volume, 126).diff(5).diff(5)
    result = _rank(raw, 252)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v053_signal)

def f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v054_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 504d of _comm_revenue_velocity with 252d lookback."""
    raw = _comm_revenue_velocity(revenue, assets, closeadj, 252).diff(5).diff(5)
    result = _rank(raw, 504)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v054_signal)

def f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v055_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 504d of _comm_opex_drag with 252d lookback."""
    raw = _comm_opex_drag(opex, marketcap, volume, 252).diff(5).diff(5)
    result = _rank(raw, 504)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v055_signal)

def f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v056_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 42d of _comm_leverage_convexity with 21d lookback."""
    raw = _comm_leverage_convexity(ebitda, debt, closeadj, 21).diff(5).diff(5)
    result = _rank(raw, 42)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v056_signal)

def f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v057_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 10d of _comm_opex_drag with 5d lookback."""
    raw = _comm_opex_drag(opex, marketcap, volume, 5).diff(5).diff(5)
    result = _rank(raw, 10)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v057_signal)

def f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v058_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 42d of _comm_leverage_convexity with 21d lookback."""
    raw = _comm_leverage_convexity(ebitda, debt, closeadj, 21).diff(5).diff(5)
    result = _rank(raw, 42)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v058_signal)

def f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v059_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 126d of _comm_revenue_velocity with 63d lookback."""
    raw = _comm_revenue_velocity(revenue, assets, closeadj, 63).diff(5).diff(5)
    result = _rank(raw, 126)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v059_signal)

def f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v060_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 10d of _comm_revenue_velocity with 5d lookback."""
    raw = _comm_revenue_velocity(revenue, assets, closeadj, 5).diff(5).diff(5)
    result = _rank(raw, 10)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v060_signal)

def f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v061_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 252d of _comm_leverage_convexity with 126d lookback."""
    raw = _comm_leverage_convexity(ebitda, debt, closeadj, 126).diff(5).diff(5)
    result = _rank(raw, 252)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v061_signal)

def f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v062_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 10d of _comm_leverage_convexity with 5d lookback."""
    raw = _comm_leverage_convexity(ebitda, debt, closeadj, 5).diff(5).diff(5)
    result = _rank(raw, 10)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v062_signal)

def f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v063_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 504d of _comm_revenue_velocity with 252d lookback."""
    raw = _comm_revenue_velocity(revenue, assets, closeadj, 252).diff(5).diff(5)
    result = _rank(raw, 504)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v063_signal)

def f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v064_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 20d of _comm_opex_drag with 10d lookback."""
    raw = _comm_opex_drag(opex, marketcap, volume, 10).diff(5).diff(5)
    result = _rank(raw, 20)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v064_signal)

def f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v065_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 252d of _comm_opex_drag with 126d lookback."""
    raw = _comm_opex_drag(opex, marketcap, volume, 126).diff(5).diff(5)
    result = _rank(raw, 252)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v065_signal)

def f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v066_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 42d of _comm_revenue_velocity with 21d lookback."""
    raw = _comm_revenue_velocity(revenue, assets, closeadj, 21).diff(5).diff(5)
    result = _rank(raw, 42)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v066_signal)

def f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v067_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 126d of _comm_revenue_velocity with 63d lookback."""
    raw = _comm_revenue_velocity(revenue, assets, closeadj, 63).diff(5).diff(5)
    result = _rank(raw, 126)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v067_signal)

def f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v068_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 20d of _comm_leverage_convexity with 10d lookback."""
    raw = _comm_leverage_convexity(ebitda, debt, closeadj, 10).diff(5).diff(5)
    result = _rank(raw, 20)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v068_signal)

def f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v069_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 42d of _comm_opex_drag with 21d lookback."""
    raw = _comm_opex_drag(opex, marketcap, volume, 21).diff(5).diff(5)
    result = _rank(raw, 42)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v069_signal)

def f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v070_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 252d of _comm_opex_drag with 126d lookback."""
    raw = _comm_opex_drag(opex, marketcap, volume, 126).diff(5).diff(5)
    result = _rank(raw, 252)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v070_signal)

def f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v071_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 20d of _comm_leverage_convexity with 10d lookback."""
    raw = _comm_leverage_convexity(ebitda, debt, closeadj, 10).diff(5).diff(5)
    result = _rank(raw, 20)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v071_signal)

def f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v072_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 504d of _comm_leverage_convexity with 252d lookback."""
    raw = _comm_leverage_convexity(ebitda, debt, closeadj, 252).diff(5).diff(5)
    result = _rank(raw, 504)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v072_signal)

def f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v073_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 252d of _comm_leverage_convexity with 126d lookback."""
    raw = _comm_leverage_convexity(ebitda, debt, closeadj, 126).diff(5).diff(5)
    result = _rank(raw, 252)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v073_signal)

def f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v074_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 10d of _comm_revenue_velocity with 5d lookback."""
    raw = _comm_revenue_velocity(revenue, assets, closeadj, 5).diff(5).diff(5)
    result = _rank(raw, 10)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v074_signal)

def f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v075_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 10d of _comm_leverage_convexity with 5d lookback."""
    raw = _comm_leverage_convexity(ebitda, debt, closeadj, 5).diff(5).diff(5)
    result = _rank(raw, 10)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v075_signal)

def f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v076_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 42d of _comm_leverage_convexity with 21d lookback."""
    raw = _comm_leverage_convexity(ebitda, debt, closeadj, 21).diff(5).diff(5)
    result = _rank(raw, 42)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v076_signal)

def f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v077_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 126d of _comm_opex_drag with 63d lookback."""
    raw = _comm_opex_drag(opex, marketcap, volume, 63).diff(5).diff(5)
    result = _rank(raw, 126)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v077_signal)

def f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v078_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 42d of _comm_leverage_convexity with 21d lookback."""
    raw = _comm_leverage_convexity(ebitda, debt, closeadj, 21).diff(5).diff(5)
    result = _rank(raw, 42)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v078_signal)

def f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v079_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 42d of _comm_opex_drag with 21d lookback."""
    raw = _comm_opex_drag(opex, marketcap, volume, 21).diff(5).diff(5)
    result = _rank(raw, 42)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v079_signal)

def f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v080_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 252d of _comm_revenue_velocity with 126d lookback."""
    raw = _comm_revenue_velocity(revenue, assets, closeadj, 126).diff(5).diff(5)
    result = _rank(raw, 252)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v080_signal)

def f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v081_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 10d of _comm_leverage_convexity with 5d lookback."""
    raw = _comm_leverage_convexity(ebitda, debt, closeadj, 5).diff(5).diff(5)
    result = _rank(raw, 10)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v081_signal)

def f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v082_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 504d of _comm_leverage_convexity with 252d lookback."""
    raw = _comm_leverage_convexity(ebitda, debt, closeadj, 252).diff(5).diff(5)
    result = _rank(raw, 504)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v082_signal)

def f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v083_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 10d of _comm_leverage_convexity with 5d lookback."""
    raw = _comm_leverage_convexity(ebitda, debt, closeadj, 5).diff(5).diff(5)
    result = _rank(raw, 10)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v083_signal)

def f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v084_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 20d of _comm_leverage_convexity with 10d lookback."""
    raw = _comm_leverage_convexity(ebitda, debt, closeadj, 10).diff(5).diff(5)
    result = _rank(raw, 20)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v084_signal)

def f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v085_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 126d of _comm_leverage_convexity with 63d lookback."""
    raw = _comm_leverage_convexity(ebitda, debt, closeadj, 63).diff(5).diff(5)
    result = _rank(raw, 126)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v085_signal)

def f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v086_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 252d of _comm_leverage_convexity with 126d lookback."""
    raw = _comm_leverage_convexity(ebitda, debt, closeadj, 126).diff(5).diff(5)
    result = _rank(raw, 252)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v086_signal)

def f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v087_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 42d of _comm_leverage_convexity with 21d lookback."""
    raw = _comm_leverage_convexity(ebitda, debt, closeadj, 21).diff(5).diff(5)
    result = _rank(raw, 42)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v087_signal)

def f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v088_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 20d of _comm_revenue_velocity with 10d lookback."""
    raw = _comm_revenue_velocity(revenue, assets, closeadj, 10).diff(5).diff(5)
    result = _rank(raw, 20)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v088_signal)

def f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v089_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 252d of _comm_revenue_velocity with 126d lookback."""
    raw = _comm_revenue_velocity(revenue, assets, closeadj, 126).diff(5).diff(5)
    result = _rank(raw, 252)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v089_signal)

def f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v090_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 504d of _comm_opex_drag with 252d lookback."""
    raw = _comm_opex_drag(opex, marketcap, volume, 252).diff(5).diff(5)
    result = _rank(raw, 504)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v090_signal)

def f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v091_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 20d of _comm_leverage_convexity with 10d lookback."""
    raw = _comm_leverage_convexity(ebitda, debt, closeadj, 10).diff(5).diff(5)
    result = _rank(raw, 20)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v091_signal)

def f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v092_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 126d of _comm_opex_drag with 63d lookback."""
    raw = _comm_opex_drag(opex, marketcap, volume, 63).diff(5).diff(5)
    result = _rank(raw, 126)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v092_signal)

def f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v093_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 252d of _comm_revenue_velocity with 126d lookback."""
    raw = _comm_revenue_velocity(revenue, assets, closeadj, 126).diff(5).diff(5)
    result = _rank(raw, 252)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v093_signal)

def f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v094_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 126d of _comm_leverage_convexity with 63d lookback."""
    raw = _comm_leverage_convexity(ebitda, debt, closeadj, 63).diff(5).diff(5)
    result = _rank(raw, 126)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v094_signal)

def f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v095_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 126d of _comm_revenue_velocity with 63d lookback."""
    raw = _comm_revenue_velocity(revenue, assets, closeadj, 63).diff(5).diff(5)
    result = _rank(raw, 126)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v095_signal)

def f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v096_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 126d of _comm_opex_drag with 63d lookback."""
    raw = _comm_opex_drag(opex, marketcap, volume, 63).diff(5).diff(5)
    result = _rank(raw, 126)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v096_signal)

def f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v097_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 126d of _comm_opex_drag with 63d lookback."""
    raw = _comm_opex_drag(opex, marketcap, volume, 63).diff(5).diff(5)
    result = _rank(raw, 126)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v097_signal)

def f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v098_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 20d of _comm_opex_drag with 10d lookback."""
    raw = _comm_opex_drag(opex, marketcap, volume, 10).diff(5).diff(5)
    result = _rank(raw, 20)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v098_signal)

def f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v099_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 126d of _comm_leverage_convexity with 63d lookback."""
    raw = _comm_leverage_convexity(ebitda, debt, closeadj, 63).diff(5).diff(5)
    result = _rank(raw, 126)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v099_signal)

def f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v100_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 42d of _comm_revenue_velocity with 21d lookback."""
    raw = _comm_revenue_velocity(revenue, assets, closeadj, 21).diff(5).diff(5)
    result = _rank(raw, 42)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v100_signal)

def f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v101_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 504d of _comm_opex_drag with 252d lookback."""
    raw = _comm_opex_drag(opex, marketcap, volume, 252).diff(5).diff(5)
    result = _rank(raw, 504)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v101_signal)

def f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v102_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 504d of _comm_opex_drag with 252d lookback."""
    raw = _comm_opex_drag(opex, marketcap, volume, 252).diff(5).diff(5)
    result = _rank(raw, 504)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v102_signal)

def f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v103_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 10d of _comm_revenue_velocity with 5d lookback."""
    raw = _comm_revenue_velocity(revenue, assets, closeadj, 5).diff(5).diff(5)
    result = _rank(raw, 10)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v103_signal)

def f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v104_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 252d of _comm_revenue_velocity with 126d lookback."""
    raw = _comm_revenue_velocity(revenue, assets, closeadj, 126).diff(5).diff(5)
    result = _rank(raw, 252)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v104_signal)

def f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v105_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 252d of _comm_opex_drag with 126d lookback."""
    raw = _comm_opex_drag(opex, marketcap, volume, 126).diff(5).diff(5)
    result = _rank(raw, 252)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v105_signal)

def f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v106_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 126d of _comm_opex_drag with 63d lookback."""
    raw = _comm_opex_drag(opex, marketcap, volume, 63).diff(5).diff(5)
    result = _rank(raw, 126)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v106_signal)

def f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v107_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 252d of _comm_leverage_convexity with 126d lookback."""
    raw = _comm_leverage_convexity(ebitda, debt, closeadj, 126).diff(5).diff(5)
    result = _rank(raw, 252)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v107_signal)

def f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v108_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 10d of _comm_opex_drag with 5d lookback."""
    raw = _comm_opex_drag(opex, marketcap, volume, 5).diff(5).diff(5)
    result = _rank(raw, 10)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v108_signal)

def f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v109_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 126d of _comm_leverage_convexity with 63d lookback."""
    raw = _comm_leverage_convexity(ebitda, debt, closeadj, 63).diff(5).diff(5)
    result = _rank(raw, 126)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v109_signal)

def f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v110_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 252d of _comm_leverage_convexity with 126d lookback."""
    raw = _comm_leverage_convexity(ebitda, debt, closeadj, 126).diff(5).diff(5)
    result = _rank(raw, 252)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v110_signal)

def f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v111_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 504d of _comm_revenue_velocity with 252d lookback."""
    raw = _comm_revenue_velocity(revenue, assets, closeadj, 252).diff(5).diff(5)
    result = _rank(raw, 504)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v111_signal)

def f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v112_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 126d of _comm_opex_drag with 63d lookback."""
    raw = _comm_opex_drag(opex, marketcap, volume, 63).diff(5).diff(5)
    result = _rank(raw, 126)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v112_signal)

def f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v113_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 10d of _comm_opex_drag with 5d lookback."""
    raw = _comm_opex_drag(opex, marketcap, volume, 5).diff(5).diff(5)
    result = _rank(raw, 10)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v113_signal)

def f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v114_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 126d of _comm_revenue_velocity with 63d lookback."""
    raw = _comm_revenue_velocity(revenue, assets, closeadj, 63).diff(5).diff(5)
    result = _rank(raw, 126)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v114_signal)

def f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v115_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 126d of _comm_leverage_convexity with 63d lookback."""
    raw = _comm_leverage_convexity(ebitda, debt, closeadj, 63).diff(5).diff(5)
    result = _rank(raw, 126)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v115_signal)

def f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v116_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 126d of _comm_opex_drag with 63d lookback."""
    raw = _comm_opex_drag(opex, marketcap, volume, 63).diff(5).diff(5)
    result = _rank(raw, 126)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v116_signal)

def f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v117_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 126d of _comm_opex_drag with 63d lookback."""
    raw = _comm_opex_drag(opex, marketcap, volume, 63).diff(5).diff(5)
    result = _rank(raw, 126)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v117_signal)

def f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v118_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 126d of _comm_revenue_velocity with 63d lookback."""
    raw = _comm_revenue_velocity(revenue, assets, closeadj, 63).diff(5).diff(5)
    result = _rank(raw, 126)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v118_signal)

def f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v119_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 504d of _comm_revenue_velocity with 252d lookback."""
    raw = _comm_revenue_velocity(revenue, assets, closeadj, 252).diff(5).diff(5)
    result = _rank(raw, 504)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v119_signal)

def f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v120_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 10d of _comm_opex_drag with 5d lookback."""
    raw = _comm_opex_drag(opex, marketcap, volume, 5).diff(5).diff(5)
    result = _rank(raw, 10)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v120_signal)

def f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v121_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 20d of _comm_revenue_velocity with 10d lookback."""
    raw = _comm_revenue_velocity(revenue, assets, closeadj, 10).diff(5).diff(5)
    result = _rank(raw, 20)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v121_signal)

def f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v122_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 42d of _comm_opex_drag with 21d lookback."""
    raw = _comm_opex_drag(opex, marketcap, volume, 21).diff(5).diff(5)
    result = _rank(raw, 42)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v122_signal)

def f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v123_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 20d of _comm_leverage_convexity with 10d lookback."""
    raw = _comm_leverage_convexity(ebitda, debt, closeadj, 10).diff(5).diff(5)
    result = _rank(raw, 20)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v123_signal)

def f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v124_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 20d of _comm_opex_drag with 10d lookback."""
    raw = _comm_opex_drag(opex, marketcap, volume, 10).diff(5).diff(5)
    result = _rank(raw, 20)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v124_signal)

def f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v125_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 126d of _comm_opex_drag with 63d lookback."""
    raw = _comm_opex_drag(opex, marketcap, volume, 63).diff(5).diff(5)
    result = _rank(raw, 126)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v125_signal)

def f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v126_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 126d of _comm_opex_drag with 63d lookback."""
    raw = _comm_opex_drag(opex, marketcap, volume, 63).diff(5).diff(5)
    result = _rank(raw, 126)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v126_signal)

def f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v127_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 42d of _comm_opex_drag with 21d lookback."""
    raw = _comm_opex_drag(opex, marketcap, volume, 21).diff(5).diff(5)
    result = _rank(raw, 42)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v127_signal)

def f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v128_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 20d of _comm_leverage_convexity with 10d lookback."""
    raw = _comm_leverage_convexity(ebitda, debt, closeadj, 10).diff(5).diff(5)
    result = _rank(raw, 20)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v128_signal)

def f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v129_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 10d of _comm_leverage_convexity with 5d lookback."""
    raw = _comm_leverage_convexity(ebitda, debt, closeadj, 5).diff(5).diff(5)
    result = _rank(raw, 10)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v129_signal)

def f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v130_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 10d of _comm_opex_drag with 5d lookback."""
    raw = _comm_opex_drag(opex, marketcap, volume, 5).diff(5).diff(5)
    result = _rank(raw, 10)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v130_signal)

def f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v131_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 10d of _comm_revenue_velocity with 5d lookback."""
    raw = _comm_revenue_velocity(revenue, assets, closeadj, 5).diff(5).diff(5)
    result = _rank(raw, 10)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v131_signal)

def f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v132_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 20d of _comm_leverage_convexity with 10d lookback."""
    raw = _comm_leverage_convexity(ebitda, debt, closeadj, 10).diff(5).diff(5)
    result = _rank(raw, 20)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v132_signal)

def f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v133_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 126d of _comm_opex_drag with 63d lookback."""
    raw = _comm_opex_drag(opex, marketcap, volume, 63).diff(5).diff(5)
    result = _rank(raw, 126)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v133_signal)

def f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v134_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 10d of _comm_revenue_velocity with 5d lookback."""
    raw = _comm_revenue_velocity(revenue, assets, closeadj, 5).diff(5).diff(5)
    result = _rank(raw, 10)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v134_signal)

def f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v135_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 20d of _comm_opex_drag with 10d lookback."""
    raw = _comm_opex_drag(opex, marketcap, volume, 10).diff(5).diff(5)
    result = _rank(raw, 20)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v135_signal)

def f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v136_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 20d of _comm_opex_drag with 10d lookback."""
    raw = _comm_opex_drag(opex, marketcap, volume, 10).diff(5).diff(5)
    result = _rank(raw, 20)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v136_signal)

def f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v137_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 252d of _comm_opex_drag with 126d lookback."""
    raw = _comm_opex_drag(opex, marketcap, volume, 126).diff(5).diff(5)
    result = _rank(raw, 252)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v137_signal)

def f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v138_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 42d of _comm_revenue_velocity with 21d lookback."""
    raw = _comm_revenue_velocity(revenue, assets, closeadj, 21).diff(5).diff(5)
    result = _rank(raw, 42)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v138_signal)

def f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v139_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 20d of _comm_leverage_convexity with 10d lookback."""
    raw = _comm_leverage_convexity(ebitda, debt, closeadj, 10).diff(5).diff(5)
    result = _rank(raw, 20)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v139_signal)

def f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v140_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 504d of _comm_revenue_velocity with 252d lookback."""
    raw = _comm_revenue_velocity(revenue, assets, closeadj, 252).diff(5).diff(5)
    result = _rank(raw, 504)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v140_signal)

def f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v141_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 252d of _comm_leverage_convexity with 126d lookback."""
    raw = _comm_leverage_convexity(ebitda, debt, closeadj, 126).diff(5).diff(5)
    result = _rank(raw, 252)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v141_signal)

def f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v142_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 252d of _comm_leverage_convexity with 126d lookback."""
    raw = _comm_leverage_convexity(ebitda, debt, closeadj, 126).diff(5).diff(5)
    result = _rank(raw, 252)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v142_signal)

def f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v143_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 10d of _comm_revenue_velocity with 5d lookback."""
    raw = _comm_revenue_velocity(revenue, assets, closeadj, 5).diff(5).diff(5)
    result = _rank(raw, 10)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v143_signal)

def f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v144_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 504d of _comm_opex_drag with 252d lookback."""
    raw = _comm_opex_drag(opex, marketcap, volume, 252).diff(5).diff(5)
    result = _rank(raw, 504)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v144_signal)

def f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v145_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 504d of _comm_revenue_velocity with 252d lookback."""
    raw = _comm_revenue_velocity(revenue, assets, closeadj, 252).diff(5).diff(5)
    result = _rank(raw, 504)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v145_signal)

def f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v146_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 10d of _comm_opex_drag with 5d lookback."""
    raw = _comm_opex_drag(opex, marketcap, volume, 5).diff(5).diff(5)
    result = _rank(raw, 10)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v146_signal)

def f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v147_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 20d of _comm_leverage_convexity with 10d lookback."""
    raw = _comm_leverage_convexity(ebitda, debt, closeadj, 10).diff(5).diff(5)
    result = _rank(raw, 20)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v147_signal)

def f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v148_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 126d of _comm_opex_drag with 63d lookback."""
    raw = _comm_opex_drag(opex, marketcap, volume, 63).diff(5).diff(5)
    result = _rank(raw, 126)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v148_signal)

def f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v149_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 42d of _comm_revenue_velocity with 21d lookback."""
    raw = _comm_revenue_velocity(revenue, assets, closeadj, 21).diff(5).diff(5)
    result = _rank(raw, 42)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v149_signal)

def f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v150_signal(revenue, assets, closeadj, opex, marketcap, volume, ebitda, debt):
    """Computes _rank over 252d of _comm_leverage_convexity with 126d lookback."""
    raw = _comm_leverage_convexity(ebitda, debt, closeadj, 126).diff(5).diff(5)
    result = _rank(raw, 252)
    return result.replace([np.inf, -np.inf], np.nan)
_FEATURES.append(f46cs_f46_cinema_exhibition_box_office_momentum_3rd_derivatives_001_150_gemini_v150_signal)


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
