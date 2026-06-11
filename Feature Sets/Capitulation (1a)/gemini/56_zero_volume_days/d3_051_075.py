"""
56_56_zero_volume_days — 3rd Derivatives 051-075
Domain: 56_zero_volume_days
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

def zvol_d3_051_accel_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Acceleration of 56_zero_volume_days over 5d to detect blow-off or exhaustion.
    """
    base = (volume.pct_change(11).rolling(55).mean())
    return base.diff(5).diff(5)

def zvol_d3_052_accel_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Acceleration of 56_zero_volume_days over 21d to detect blow-off or exhaustion.
    """
    base = (volume.pct_change(11).rolling(55).mean())
    return base.diff(21).diff(21)

def zvol_d3_053_accel_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Acceleration of 56_zero_volume_days over 63d to detect blow-off or exhaustion.
    """
    base = (volume.pct_change(11).rolling(55).mean())
    return base.diff(63).diff(63)

def zvol_d3_054_accel_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Acceleration of 56_zero_volume_days over 126d to detect blow-off or exhaustion.
    """
    base = (volume.pct_change(11).rolling(55).mean())
    return base.diff(126).diff(126)

def zvol_d3_055_accel_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Acceleration of 56_zero_volume_days over 252d to detect blow-off or exhaustion.
    """
    base = (volume.pct_change(11).rolling(55).mean())
    return base.diff(252).diff(252)

def zvol_d3_056_accel_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Acceleration of 56_zero_volume_days over 5d to detect blow-off or exhaustion.
    """
    base = (volume.pct_change(12).rolling(60).mean())
    return base.diff(5).diff(5)

def zvol_d3_057_accel_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Acceleration of 56_zero_volume_days over 21d to detect blow-off or exhaustion.
    """
    base = (volume.pct_change(12).rolling(60).mean())
    return base.diff(21).diff(21)

def zvol_d3_058_accel_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Acceleration of 56_zero_volume_days over 63d to detect blow-off or exhaustion.
    """
    base = (volume.pct_change(12).rolling(60).mean())
    return base.diff(63).diff(63)

def zvol_d3_059_accel_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Acceleration of 56_zero_volume_days over 126d to detect blow-off or exhaustion.
    """
    base = (volume.pct_change(12).rolling(60).mean())
    return base.diff(126).diff(126)

def zvol_d3_060_accel_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Acceleration of 56_zero_volume_days over 252d to detect blow-off or exhaustion.
    """
    base = (volume.pct_change(12).rolling(60).mean())
    return base.diff(252).diff(252)

def zvol_d3_061_accel_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Acceleration of 56_zero_volume_days over 5d to detect blow-off or exhaustion.
    """
    base = (volume.pct_change(13).rolling(65).mean())
    return base.diff(5).diff(5)

def zvol_d3_062_accel_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Acceleration of 56_zero_volume_days over 21d to detect blow-off or exhaustion.
    """
    base = (volume.pct_change(13).rolling(65).mean())
    return base.diff(21).diff(21)

def zvol_d3_063_accel_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Acceleration of 56_zero_volume_days over 63d to detect blow-off or exhaustion.
    """
    base = (volume.pct_change(13).rolling(65).mean())
    return base.diff(63).diff(63)

def zvol_d3_064_accel_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Acceleration of 56_zero_volume_days over 126d to detect blow-off or exhaustion.
    """
    base = (volume.pct_change(13).rolling(65).mean())
    return base.diff(126).diff(126)

def zvol_d3_065_accel_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Acceleration of 56_zero_volume_days over 252d to detect blow-off or exhaustion.
    """
    base = (volume.pct_change(13).rolling(65).mean())
    return base.diff(252).diff(252)

def zvol_d3_066_accel_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Acceleration of 56_zero_volume_days over 5d to detect blow-off or exhaustion.
    """
    base = (volume.pct_change(14).rolling(70).mean())
    return base.diff(5).diff(5)

def zvol_d3_067_accel_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Acceleration of 56_zero_volume_days over 21d to detect blow-off or exhaustion.
    """
    base = (volume.pct_change(14).rolling(70).mean())
    return base.diff(21).diff(21)

def zvol_d3_068_accel_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Acceleration of 56_zero_volume_days over 63d to detect blow-off or exhaustion.
    """
    base = (volume.pct_change(14).rolling(70).mean())
    return base.diff(63).diff(63)

def zvol_d3_069_accel_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Acceleration of 56_zero_volume_days over 126d to detect blow-off or exhaustion.
    """
    base = (volume.pct_change(14).rolling(70).mean())
    return base.diff(126).diff(126)

def zvol_d3_070_accel_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Acceleration of 56_zero_volume_days over 252d to detect blow-off or exhaustion.
    """
    base = (volume.pct_change(14).rolling(70).mean())
    return base.diff(252).diff(252)

def zvol_d3_071_accel_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Acceleration of 56_zero_volume_days over 5d to detect blow-off or exhaustion.
    """
    base = (volume.pct_change(15).rolling(75).mean())
    return base.diff(5).diff(5)

def zvol_d3_072_accel_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Acceleration of 56_zero_volume_days over 21d to detect blow-off or exhaustion.
    """
    base = (volume.pct_change(15).rolling(75).mean())
    return base.diff(21).diff(21)

def zvol_d3_073_accel_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Acceleration of 56_zero_volume_days over 63d to detect blow-off or exhaustion.
    """
    base = (volume.pct_change(15).rolling(75).mean())
    return base.diff(63).diff(63)

def zvol_d3_074_accel_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Acceleration of 56_zero_volume_days over 126d to detect blow-off or exhaustion.
    """
    base = (volume.pct_change(15).rolling(75).mean())
    return base.diff(126).diff(126)

def zvol_d3_075_accel_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Acceleration of 56_zero_volume_days over 252d to detect blow-off or exhaustion.
    """
    base = (volume.pct_change(15).rolling(75).mean())
    return base.diff(252).diff(252)
