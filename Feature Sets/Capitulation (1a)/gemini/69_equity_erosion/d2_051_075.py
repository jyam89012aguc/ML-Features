"""
69_69_equity_erosion — 2nd Derivatives 051-075
Domain: 69_equity_erosion
Asset class: Equities
Target context: Capitulation
"""
import numpy as np
import pandas as pd

# ── Utility helpers ──────────────────────────────────────────────────────────
_EPS = 1e-9

def _safe_div(a: pd.Series, b: pd.Series) -> pd.Series:
    return a / b.replace(0, _EPS)

def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=1).mean()

def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=1).std().fillna(0)

def _zscore_rolling(s: pd.Series, w: int) -> pd.Series:
    m = _rolling_mean(s, w)
    sd = _rolling_std(s, w)
    return _safe_div((s - m), sd)

def _rank_pct(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=1).rank(pct=True)

def _rolling_skew(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=1).skew().fillna(0)

def _rolling_kurt(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=1).kurt().fillna(0)

# ── Feature functions ────────────────────────────────────────────────────────

def eqer_d2_051_vel_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Velocity of 69_equity_erosion over 5d to detect acceleration in trend.
    """
    base = opinc.pct_change(55)
    return base.diff(5)

def eqer_d2_052_vel_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Velocity of 69_equity_erosion over 21d to detect acceleration in trend.
    """
    base = opinc.pct_change(55)
    return base.diff(21)

def eqer_d2_053_vel_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Velocity of 69_equity_erosion over 63d to detect acceleration in trend.
    """
    base = opinc.pct_change(55)
    return base.diff(63)

def eqer_d2_054_vel_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Velocity of 69_equity_erosion over 126d to detect acceleration in trend.
    """
    base = opinc.pct_change(55)
    return base.diff(126)

def eqer_d2_055_vel_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Velocity of 69_equity_erosion over 252d to detect acceleration in trend.
    """
    base = opinc.pct_change(55)
    return base.diff(252)

def eqer_d2_056_vel_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Velocity of 69_equity_erosion over 5d to detect acceleration in trend.
    """
    base = opinc.pct_change(60)
    return base.diff(5)

def eqer_d2_057_vel_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Velocity of 69_equity_erosion over 21d to detect acceleration in trend.
    """
    base = opinc.pct_change(60)
    return base.diff(21)

def eqer_d2_058_vel_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Velocity of 69_equity_erosion over 63d to detect acceleration in trend.
    """
    base = opinc.pct_change(60)
    return base.diff(63)

def eqer_d2_059_vel_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Velocity of 69_equity_erosion over 126d to detect acceleration in trend.
    """
    base = opinc.pct_change(60)
    return base.diff(126)

def eqer_d2_060_vel_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Velocity of 69_equity_erosion over 252d to detect acceleration in trend.
    """
    base = opinc.pct_change(60)
    return base.diff(252)

def eqer_d2_061_vel_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Velocity of 69_equity_erosion over 5d to detect acceleration in trend.
    """
    base = opinc.pct_change(65)
    return base.diff(5)

def eqer_d2_062_vel_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Velocity of 69_equity_erosion over 21d to detect acceleration in trend.
    """
    base = opinc.pct_change(65)
    return base.diff(21)

def eqer_d2_063_vel_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Velocity of 69_equity_erosion over 63d to detect acceleration in trend.
    """
    base = opinc.pct_change(65)
    return base.diff(63)

def eqer_d2_064_vel_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Velocity of 69_equity_erosion over 126d to detect acceleration in trend.
    """
    base = opinc.pct_change(65)
    return base.diff(126)

def eqer_d2_065_vel_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Velocity of 69_equity_erosion over 252d to detect acceleration in trend.
    """
    base = opinc.pct_change(65)
    return base.diff(252)

def eqer_d2_066_vel_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Velocity of 69_equity_erosion over 5d to detect acceleration in trend.
    """
    base = opinc.pct_change(70)
    return base.diff(5)

def eqer_d2_067_vel_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Velocity of 69_equity_erosion over 21d to detect acceleration in trend.
    """
    base = opinc.pct_change(70)
    return base.diff(21)

def eqer_d2_068_vel_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Velocity of 69_equity_erosion over 63d to detect acceleration in trend.
    """
    base = opinc.pct_change(70)
    return base.diff(63)

def eqer_d2_069_vel_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Velocity of 69_equity_erosion over 126d to detect acceleration in trend.
    """
    base = opinc.pct_change(70)
    return base.diff(126)

def eqer_d2_070_vel_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Velocity of 69_equity_erosion over 252d to detect acceleration in trend.
    """
    base = opinc.pct_change(70)
    return base.diff(252)

def eqer_d2_071_vel_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Velocity of 69_equity_erosion over 5d to detect acceleration in trend.
    """
    base = opinc.pct_change(75)
    return base.diff(5)

def eqer_d2_072_vel_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Velocity of 69_equity_erosion over 21d to detect acceleration in trend.
    """
    base = opinc.pct_change(75)
    return base.diff(21)

def eqer_d2_073_vel_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Velocity of 69_equity_erosion over 63d to detect acceleration in trend.
    """
    base = opinc.pct_change(75)
    return base.diff(63)

def eqer_d2_074_vel_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Velocity of 69_equity_erosion over 126d to detect acceleration in trend.
    """
    base = opinc.pct_change(75)
    return base.diff(126)

def eqer_d2_075_vel_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Velocity of 69_equity_erosion over 252d to detect acceleration in trend.
    """
    base = opinc.pct_change(75)
    return base.diff(252)
