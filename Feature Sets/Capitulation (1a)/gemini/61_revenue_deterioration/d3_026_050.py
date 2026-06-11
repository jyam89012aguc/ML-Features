"""
61_61_revenue_deterioration — 3rd Derivatives 026-050
Domain: 61_revenue_deterioration
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

def rdet_d3_026_accel_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Acceleration of 61_revenue_deterioration over 5d to detect blow-off or exhaustion.
    """
    base = revenue.pct_change(30)
    return base.diff(5).diff(5)

def rdet_d3_027_accel_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Acceleration of 61_revenue_deterioration over 21d to detect blow-off or exhaustion.
    """
    base = revenue.pct_change(30)
    return base.diff(21).diff(21)

def rdet_d3_028_accel_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Acceleration of 61_revenue_deterioration over 63d to detect blow-off or exhaustion.
    """
    base = revenue.pct_change(30)
    return base.diff(63).diff(63)

def rdet_d3_029_accel_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Acceleration of 61_revenue_deterioration over 126d to detect blow-off or exhaustion.
    """
    base = revenue.pct_change(30)
    return base.diff(126).diff(126)

def rdet_d3_030_accel_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Acceleration of 61_revenue_deterioration over 252d to detect blow-off or exhaustion.
    """
    base = revenue.pct_change(30)
    return base.diff(252).diff(252)

def rdet_d3_031_accel_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Acceleration of 61_revenue_deterioration over 5d to detect blow-off or exhaustion.
    """
    base = revenue.pct_change(35)
    return base.diff(5).diff(5)

def rdet_d3_032_accel_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Acceleration of 61_revenue_deterioration over 21d to detect blow-off or exhaustion.
    """
    base = revenue.pct_change(35)
    return base.diff(21).diff(21)

def rdet_d3_033_accel_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Acceleration of 61_revenue_deterioration over 63d to detect blow-off or exhaustion.
    """
    base = revenue.pct_change(35)
    return base.diff(63).diff(63)

def rdet_d3_034_accel_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Acceleration of 61_revenue_deterioration over 126d to detect blow-off or exhaustion.
    """
    base = revenue.pct_change(35)
    return base.diff(126).diff(126)

def rdet_d3_035_accel_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Acceleration of 61_revenue_deterioration over 252d to detect blow-off or exhaustion.
    """
    base = revenue.pct_change(35)
    return base.diff(252).diff(252)

def rdet_d3_036_accel_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Acceleration of 61_revenue_deterioration over 5d to detect blow-off or exhaustion.
    """
    base = revenue.pct_change(40)
    return base.diff(5).diff(5)

def rdet_d3_037_accel_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Acceleration of 61_revenue_deterioration over 21d to detect blow-off or exhaustion.
    """
    base = revenue.pct_change(40)
    return base.diff(21).diff(21)

def rdet_d3_038_accel_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Acceleration of 61_revenue_deterioration over 63d to detect blow-off or exhaustion.
    """
    base = revenue.pct_change(40)
    return base.diff(63).diff(63)

def rdet_d3_039_accel_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Acceleration of 61_revenue_deterioration over 126d to detect blow-off or exhaustion.
    """
    base = revenue.pct_change(40)
    return base.diff(126).diff(126)

def rdet_d3_040_accel_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Acceleration of 61_revenue_deterioration over 252d to detect blow-off or exhaustion.
    """
    base = revenue.pct_change(40)
    return base.diff(252).diff(252)

def rdet_d3_041_accel_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Acceleration of 61_revenue_deterioration over 5d to detect blow-off or exhaustion.
    """
    base = revenue.pct_change(45)
    return base.diff(5).diff(5)

def rdet_d3_042_accel_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Acceleration of 61_revenue_deterioration over 21d to detect blow-off or exhaustion.
    """
    base = revenue.pct_change(45)
    return base.diff(21).diff(21)

def rdet_d3_043_accel_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Acceleration of 61_revenue_deterioration over 63d to detect blow-off or exhaustion.
    """
    base = revenue.pct_change(45)
    return base.diff(63).diff(63)

def rdet_d3_044_accel_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Acceleration of 61_revenue_deterioration over 126d to detect blow-off or exhaustion.
    """
    base = revenue.pct_change(45)
    return base.diff(126).diff(126)

def rdet_d3_045_accel_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Acceleration of 61_revenue_deterioration over 252d to detect blow-off or exhaustion.
    """
    base = revenue.pct_change(45)
    return base.diff(252).diff(252)

def rdet_d3_046_accel_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Acceleration of 61_revenue_deterioration over 5d to detect blow-off or exhaustion.
    """
    base = revenue.pct_change(50)
    return base.diff(5).diff(5)

def rdet_d3_047_accel_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Acceleration of 61_revenue_deterioration over 21d to detect blow-off or exhaustion.
    """
    base = revenue.pct_change(50)
    return base.diff(21).diff(21)

def rdet_d3_048_accel_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Acceleration of 61_revenue_deterioration over 63d to detect blow-off or exhaustion.
    """
    base = revenue.pct_change(50)
    return base.diff(63).diff(63)

def rdet_d3_049_accel_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Acceleration of 61_revenue_deterioration over 126d to detect blow-off or exhaustion.
    """
    base = revenue.pct_change(50)
    return base.diff(126).diff(126)

def rdet_d3_050_accel_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Acceleration of 61_revenue_deterioration over 252d to detect blow-off or exhaustion.
    """
    base = revenue.pct_change(50)
    return base.diff(252).diff(252)
