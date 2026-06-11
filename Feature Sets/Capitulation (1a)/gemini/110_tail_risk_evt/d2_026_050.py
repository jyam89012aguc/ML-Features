"""
110_110_tail_risk_evt — 2nd Derivatives 026-050
Domain: 110_tail_risk_evt
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

def trev_d2_026_vel_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Velocity of 110_tail_risk_evt over 5d to detect acceleration in trend.
    """
    base = close.pct_change().rolling(300).quantile(0.01)
    return base.diff(5)

def trev_d2_027_vel_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Velocity of 110_tail_risk_evt over 21d to detect acceleration in trend.
    """
    base = close.pct_change().rolling(300).quantile(0.01)
    return base.diff(21)

def trev_d2_028_vel_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Velocity of 110_tail_risk_evt over 63d to detect acceleration in trend.
    """
    base = close.pct_change().rolling(300).quantile(0.01)
    return base.diff(63)

def trev_d2_029_vel_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Velocity of 110_tail_risk_evt over 126d to detect acceleration in trend.
    """
    base = close.pct_change().rolling(300).quantile(0.01)
    return base.diff(126)

def trev_d2_030_vel_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Velocity of 110_tail_risk_evt over 252d to detect acceleration in trend.
    """
    base = close.pct_change().rolling(300).quantile(0.01)
    return base.diff(252)

def trev_d2_031_vel_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Velocity of 110_tail_risk_evt over 5d to detect acceleration in trend.
    """
    base = close.pct_change().rolling(350).quantile(0.01)
    return base.diff(5)

def trev_d2_032_vel_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Velocity of 110_tail_risk_evt over 21d to detect acceleration in trend.
    """
    base = close.pct_change().rolling(350).quantile(0.01)
    return base.diff(21)

def trev_d2_033_vel_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Velocity of 110_tail_risk_evt over 63d to detect acceleration in trend.
    """
    base = close.pct_change().rolling(350).quantile(0.01)
    return base.diff(63)

def trev_d2_034_vel_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Velocity of 110_tail_risk_evt over 126d to detect acceleration in trend.
    """
    base = close.pct_change().rolling(350).quantile(0.01)
    return base.diff(126)

def trev_d2_035_vel_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Velocity of 110_tail_risk_evt over 252d to detect acceleration in trend.
    """
    base = close.pct_change().rolling(350).quantile(0.01)
    return base.diff(252)

def trev_d2_036_vel_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Velocity of 110_tail_risk_evt over 5d to detect acceleration in trend.
    """
    base = close.pct_change().rolling(400).quantile(0.01)
    return base.diff(5)

def trev_d2_037_vel_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Velocity of 110_tail_risk_evt over 21d to detect acceleration in trend.
    """
    base = close.pct_change().rolling(400).quantile(0.01)
    return base.diff(21)

def trev_d2_038_vel_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Velocity of 110_tail_risk_evt over 63d to detect acceleration in trend.
    """
    base = close.pct_change().rolling(400).quantile(0.01)
    return base.diff(63)

def trev_d2_039_vel_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Velocity of 110_tail_risk_evt over 126d to detect acceleration in trend.
    """
    base = close.pct_change().rolling(400).quantile(0.01)
    return base.diff(126)

def trev_d2_040_vel_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Velocity of 110_tail_risk_evt over 252d to detect acceleration in trend.
    """
    base = close.pct_change().rolling(400).quantile(0.01)
    return base.diff(252)

def trev_d2_041_vel_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Velocity of 110_tail_risk_evt over 5d to detect acceleration in trend.
    """
    base = close.pct_change().rolling(450).quantile(0.01)
    return base.diff(5)

def trev_d2_042_vel_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Velocity of 110_tail_risk_evt over 21d to detect acceleration in trend.
    """
    base = close.pct_change().rolling(450).quantile(0.01)
    return base.diff(21)

def trev_d2_043_vel_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Velocity of 110_tail_risk_evt over 63d to detect acceleration in trend.
    """
    base = close.pct_change().rolling(450).quantile(0.01)
    return base.diff(63)

def trev_d2_044_vel_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Velocity of 110_tail_risk_evt over 126d to detect acceleration in trend.
    """
    base = close.pct_change().rolling(450).quantile(0.01)
    return base.diff(126)

def trev_d2_045_vel_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Velocity of 110_tail_risk_evt over 252d to detect acceleration in trend.
    """
    base = close.pct_change().rolling(450).quantile(0.01)
    return base.diff(252)

def trev_d2_046_vel_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Velocity of 110_tail_risk_evt over 5d to detect acceleration in trend.
    """
    base = close.pct_change().rolling(500).quantile(0.01)
    return base.diff(5)

def trev_d2_047_vel_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Velocity of 110_tail_risk_evt over 21d to detect acceleration in trend.
    """
    base = close.pct_change().rolling(500).quantile(0.01)
    return base.diff(21)

def trev_d2_048_vel_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Velocity of 110_tail_risk_evt over 63d to detect acceleration in trend.
    """
    base = close.pct_change().rolling(500).quantile(0.01)
    return base.diff(63)

def trev_d2_049_vel_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Velocity of 110_tail_risk_evt over 126d to detect acceleration in trend.
    """
    base = close.pct_change().rolling(500).quantile(0.01)
    return base.diff(126)

def trev_d2_050_vel_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Velocity of 110_tail_risk_evt over 252d to detect acceleration in trend.
    """
    base = close.pct_change().rolling(500).quantile(0.01)
    return base.diff(252)
