"""
118_118_drawdown_recovery_asymmetry — 3rd Derivatives 026-050
Domain: 118_drawdown_recovery_asymmetry
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

def dras_d3_026_accel_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Acceleration of 118_drawdown_recovery_asymmetry over 5d to detect blow-off or exhaustion.
    """
    base = close.pct_change().rolling(60).skew()
    return base.diff(5).diff(5)

def dras_d3_027_accel_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Acceleration of 118_drawdown_recovery_asymmetry over 21d to detect blow-off or exhaustion.
    """
    base = close.pct_change().rolling(60).skew()
    return base.diff(21).diff(21)

def dras_d3_028_accel_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Acceleration of 118_drawdown_recovery_asymmetry over 63d to detect blow-off or exhaustion.
    """
    base = close.pct_change().rolling(60).skew()
    return base.diff(63).diff(63)

def dras_d3_029_accel_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Acceleration of 118_drawdown_recovery_asymmetry over 126d to detect blow-off or exhaustion.
    """
    base = close.pct_change().rolling(60).skew()
    return base.diff(126).diff(126)

def dras_d3_030_accel_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Acceleration of 118_drawdown_recovery_asymmetry over 252d to detect blow-off or exhaustion.
    """
    base = close.pct_change().rolling(60).skew()
    return base.diff(252).diff(252)

def dras_d3_031_accel_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Acceleration of 118_drawdown_recovery_asymmetry over 5d to detect blow-off or exhaustion.
    """
    base = close.pct_change().rolling(70).skew()
    return base.diff(5).diff(5)

def dras_d3_032_accel_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Acceleration of 118_drawdown_recovery_asymmetry over 21d to detect blow-off or exhaustion.
    """
    base = close.pct_change().rolling(70).skew()
    return base.diff(21).diff(21)

def dras_d3_033_accel_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Acceleration of 118_drawdown_recovery_asymmetry over 63d to detect blow-off or exhaustion.
    """
    base = close.pct_change().rolling(70).skew()
    return base.diff(63).diff(63)

def dras_d3_034_accel_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Acceleration of 118_drawdown_recovery_asymmetry over 126d to detect blow-off or exhaustion.
    """
    base = close.pct_change().rolling(70).skew()
    return base.diff(126).diff(126)

def dras_d3_035_accel_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Acceleration of 118_drawdown_recovery_asymmetry over 252d to detect blow-off or exhaustion.
    """
    base = close.pct_change().rolling(70).skew()
    return base.diff(252).diff(252)

def dras_d3_036_accel_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Acceleration of 118_drawdown_recovery_asymmetry over 5d to detect blow-off or exhaustion.
    """
    base = close.pct_change().rolling(80).skew()
    return base.diff(5).diff(5)

def dras_d3_037_accel_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Acceleration of 118_drawdown_recovery_asymmetry over 21d to detect blow-off or exhaustion.
    """
    base = close.pct_change().rolling(80).skew()
    return base.diff(21).diff(21)

def dras_d3_038_accel_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Acceleration of 118_drawdown_recovery_asymmetry over 63d to detect blow-off or exhaustion.
    """
    base = close.pct_change().rolling(80).skew()
    return base.diff(63).diff(63)

def dras_d3_039_accel_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Acceleration of 118_drawdown_recovery_asymmetry over 126d to detect blow-off or exhaustion.
    """
    base = close.pct_change().rolling(80).skew()
    return base.diff(126).diff(126)

def dras_d3_040_accel_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Acceleration of 118_drawdown_recovery_asymmetry over 252d to detect blow-off or exhaustion.
    """
    base = close.pct_change().rolling(80).skew()
    return base.diff(252).diff(252)

def dras_d3_041_accel_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Acceleration of 118_drawdown_recovery_asymmetry over 5d to detect blow-off or exhaustion.
    """
    base = close.pct_change().rolling(90).skew()
    return base.diff(5).diff(5)

def dras_d3_042_accel_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Acceleration of 118_drawdown_recovery_asymmetry over 21d to detect blow-off or exhaustion.
    """
    base = close.pct_change().rolling(90).skew()
    return base.diff(21).diff(21)

def dras_d3_043_accel_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Acceleration of 118_drawdown_recovery_asymmetry over 63d to detect blow-off or exhaustion.
    """
    base = close.pct_change().rolling(90).skew()
    return base.diff(63).diff(63)

def dras_d3_044_accel_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Acceleration of 118_drawdown_recovery_asymmetry over 126d to detect blow-off or exhaustion.
    """
    base = close.pct_change().rolling(90).skew()
    return base.diff(126).diff(126)

def dras_d3_045_accel_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Acceleration of 118_drawdown_recovery_asymmetry over 252d to detect blow-off or exhaustion.
    """
    base = close.pct_change().rolling(90).skew()
    return base.diff(252).diff(252)

def dras_d3_046_accel_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Acceleration of 118_drawdown_recovery_asymmetry over 5d to detect blow-off or exhaustion.
    """
    base = close.pct_change().rolling(100).skew()
    return base.diff(5).diff(5)

def dras_d3_047_accel_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Acceleration of 118_drawdown_recovery_asymmetry over 21d to detect blow-off or exhaustion.
    """
    base = close.pct_change().rolling(100).skew()
    return base.diff(21).diff(21)

def dras_d3_048_accel_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Acceleration of 118_drawdown_recovery_asymmetry over 63d to detect blow-off or exhaustion.
    """
    base = close.pct_change().rolling(100).skew()
    return base.diff(63).diff(63)

def dras_d3_049_accel_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Acceleration of 118_drawdown_recovery_asymmetry over 126d to detect blow-off or exhaustion.
    """
    base = close.pct_change().rolling(100).skew()
    return base.diff(126).diff(126)

def dras_d3_050_accel_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Acceleration of 118_drawdown_recovery_asymmetry over 252d to detect blow-off or exhaustion.
    """
    base = close.pct_change().rolling(100).skew()
    return base.diff(252).diff(252)
