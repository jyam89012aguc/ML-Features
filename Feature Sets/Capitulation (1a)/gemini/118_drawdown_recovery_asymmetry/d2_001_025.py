"""
118_118_drawdown_recovery_asymmetry — 2nd Derivatives 001-025
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

def dras_d2_001_vel_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Velocity of 118_drawdown_recovery_asymmetry over 5d to detect acceleration in trend.
    """
    base = (close / close.rolling(252).max() - 1).abs() / (close / close.rolling(252).min() - 1).abs()
    return base.diff(5)

def dras_d2_002_vel_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Velocity of 118_drawdown_recovery_asymmetry over 21d to detect acceleration in trend.
    """
    base = (close / close.rolling(252).max() - 1).abs() / (close / close.rolling(252).min() - 1).abs()
    return base.diff(21)

def dras_d2_003_vel_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Velocity of 118_drawdown_recovery_asymmetry over 63d to detect acceleration in trend.
    """
    base = (close / close.rolling(252).max() - 1).abs() / (close / close.rolling(252).min() - 1).abs()
    return base.diff(63)

def dras_d2_004_vel_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Velocity of 118_drawdown_recovery_asymmetry over 126d to detect acceleration in trend.
    """
    base = (close / close.rolling(252).max() - 1).abs() / (close / close.rolling(252).min() - 1).abs()
    return base.diff(126)

def dras_d2_005_vel_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Velocity of 118_drawdown_recovery_asymmetry over 252d to detect acceleration in trend.
    """
    base = (close / close.rolling(252).max() - 1).abs() / (close / close.rolling(252).min() - 1).abs()
    return base.diff(252)

def dras_d2_006_vel_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Velocity of 118_drawdown_recovery_asymmetry over 5d to detect acceleration in trend.
    """
    base = close.diff().clip(lower=0).rolling(21).sum() / close.diff().clip(upper=0).abs().rolling(21).sum()
    return base.diff(5)

def dras_d2_007_vel_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Velocity of 118_drawdown_recovery_asymmetry over 21d to detect acceleration in trend.
    """
    base = close.diff().clip(lower=0).rolling(21).sum() / close.diff().clip(upper=0).abs().rolling(21).sum()
    return base.diff(21)

def dras_d2_008_vel_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Velocity of 118_drawdown_recovery_asymmetry over 63d to detect acceleration in trend.
    """
    base = close.diff().clip(lower=0).rolling(21).sum() / close.diff().clip(upper=0).abs().rolling(21).sum()
    return base.diff(63)

def dras_d2_009_vel_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Velocity of 118_drawdown_recovery_asymmetry over 126d to detect acceleration in trend.
    """
    base = close.diff().clip(lower=0).rolling(21).sum() / close.diff().clip(upper=0).abs().rolling(21).sum()
    return base.diff(126)

def dras_d2_010_vel_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Velocity of 118_drawdown_recovery_asymmetry over 252d to detect acceleration in trend.
    """
    base = close.diff().clip(lower=0).rolling(21).sum() / close.diff().clip(upper=0).abs().rolling(21).sum()
    return base.diff(252)

def dras_d2_011_vel_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Velocity of 118_drawdown_recovery_asymmetry over 5d to detect acceleration in trend.
    """
    base = close.pct_change().rolling(21).skew()
    return base.diff(5)

def dras_d2_012_vel_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Velocity of 118_drawdown_recovery_asymmetry over 21d to detect acceleration in trend.
    """
    base = close.pct_change().rolling(21).skew()
    return base.diff(21)

def dras_d2_013_vel_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Velocity of 118_drawdown_recovery_asymmetry over 63d to detect acceleration in trend.
    """
    base = close.pct_change().rolling(21).skew()
    return base.diff(63)

def dras_d2_014_vel_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Velocity of 118_drawdown_recovery_asymmetry over 126d to detect acceleration in trend.
    """
    base = close.pct_change().rolling(21).skew()
    return base.diff(126)

def dras_d2_015_vel_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Velocity of 118_drawdown_recovery_asymmetry over 252d to detect acceleration in trend.
    """
    base = close.pct_change().rolling(21).skew()
    return base.diff(252)

def dras_d2_016_vel_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Velocity of 118_drawdown_recovery_asymmetry over 5d to detect acceleration in trend.
    """
    base = close.pct_change().rolling(40).skew()
    return base.diff(5)

def dras_d2_017_vel_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Velocity of 118_drawdown_recovery_asymmetry over 21d to detect acceleration in trend.
    """
    base = close.pct_change().rolling(40).skew()
    return base.diff(21)

def dras_d2_018_vel_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Velocity of 118_drawdown_recovery_asymmetry over 63d to detect acceleration in trend.
    """
    base = close.pct_change().rolling(40).skew()
    return base.diff(63)

def dras_d2_019_vel_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Velocity of 118_drawdown_recovery_asymmetry over 126d to detect acceleration in trend.
    """
    base = close.pct_change().rolling(40).skew()
    return base.diff(126)

def dras_d2_020_vel_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Velocity of 118_drawdown_recovery_asymmetry over 252d to detect acceleration in trend.
    """
    base = close.pct_change().rolling(40).skew()
    return base.diff(252)

def dras_d2_021_vel_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Velocity of 118_drawdown_recovery_asymmetry over 5d to detect acceleration in trend.
    """
    base = close.pct_change().rolling(50).skew()
    return base.diff(5)

def dras_d2_022_vel_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Velocity of 118_drawdown_recovery_asymmetry over 21d to detect acceleration in trend.
    """
    base = close.pct_change().rolling(50).skew()
    return base.diff(21)

def dras_d2_023_vel_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Velocity of 118_drawdown_recovery_asymmetry over 63d to detect acceleration in trend.
    """
    base = close.pct_change().rolling(50).skew()
    return base.diff(63)

def dras_d2_024_vel_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Velocity of 118_drawdown_recovery_asymmetry over 126d to detect acceleration in trend.
    """
    base = close.pct_change().rolling(50).skew()
    return base.diff(126)

def dras_d2_025_vel_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Velocity of 118_drawdown_recovery_asymmetry over 252d to detect acceleration in trend.
    """
    base = close.pct_change().rolling(50).skew()
    return base.diff(252)
