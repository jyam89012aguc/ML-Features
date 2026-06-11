"""
03_03_drawdown_shape — 2nd Derivatives 001-025
Domain: 03_drawdown_shape
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

def dsh_d2_001_vel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Velocity of 03_drawdown_shape over 5d to detect acceleration in trend.
    """
    base = (close / close.rolling(252).max() - 1.0).abs()
    return base.diff(5)

def dsh_d2_002_vel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Velocity of 03_drawdown_shape over 21d to detect acceleration in trend.
    """
    base = (close / close.rolling(252).max() - 1.0).abs()
    return base.diff(21)

def dsh_d2_003_vel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Velocity of 03_drawdown_shape over 63d to detect acceleration in trend.
    """
    base = (close / close.rolling(252).max() - 1.0).abs()
    return base.diff(63)

def dsh_d2_004_vel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Velocity of 03_drawdown_shape over 126d to detect acceleration in trend.
    """
    base = (close / close.rolling(252).max() - 1.0).abs()
    return base.diff(126)

def dsh_d2_005_vel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Velocity of 03_drawdown_shape over 252d to detect acceleration in trend.
    """
    base = (close / close.rolling(252).max() - 1.0).abs()
    return base.diff(252)

def dsh_d2_006_vel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Velocity of 03_drawdown_shape over 5d to detect acceleration in trend.
    """
    base = (close.diff(5).abs() / close.rolling(5).std())
    return base.diff(5)

def dsh_d2_007_vel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Velocity of 03_drawdown_shape over 21d to detect acceleration in trend.
    """
    base = (close.diff(5).abs() / close.rolling(5).std())
    return base.diff(21)

def dsh_d2_008_vel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Velocity of 03_drawdown_shape over 63d to detect acceleration in trend.
    """
    base = (close.diff(5).abs() / close.rolling(5).std())
    return base.diff(63)

def dsh_d2_009_vel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Velocity of 03_drawdown_shape over 126d to detect acceleration in trend.
    """
    base = (close.diff(5).abs() / close.rolling(5).std())
    return base.diff(126)

def dsh_d2_010_vel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Velocity of 03_drawdown_shape over 252d to detect acceleration in trend.
    """
    base = (close.diff(5).abs() / close.rolling(5).std())
    return base.diff(252)

def dsh_d2_011_vel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Velocity of 03_drawdown_shape over 5d to detect acceleration in trend.
    """
    base = (close.rolling(21).max() - close) / close.rolling(21).std().replace(0, 1e-9)
    return base.diff(5)

def dsh_d2_012_vel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Velocity of 03_drawdown_shape over 21d to detect acceleration in trend.
    """
    base = (close.rolling(21).max() - close) / close.rolling(21).std().replace(0, 1e-9)
    return base.diff(21)

def dsh_d2_013_vel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Velocity of 03_drawdown_shape over 63d to detect acceleration in trend.
    """
    base = (close.rolling(21).max() - close) / close.rolling(21).std().replace(0, 1e-9)
    return base.diff(63)

def dsh_d2_014_vel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Velocity of 03_drawdown_shape over 126d to detect acceleration in trend.
    """
    base = (close.rolling(21).max() - close) / close.rolling(21).std().replace(0, 1e-9)
    return base.diff(126)

def dsh_d2_015_vel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Velocity of 03_drawdown_shape over 252d to detect acceleration in trend.
    """
    base = (close.rolling(21).max() - close) / close.rolling(21).std().replace(0, 1e-9)
    return base.diff(252)

def dsh_d2_016_vel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Velocity of 03_drawdown_shape over 5d to detect acceleration in trend.
    """
    base = (close.pct_change(4).rolling(20).mean())
    return base.diff(5)

def dsh_d2_017_vel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Velocity of 03_drawdown_shape over 21d to detect acceleration in trend.
    """
    base = (close.pct_change(4).rolling(20).mean())
    return base.diff(21)

def dsh_d2_018_vel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Velocity of 03_drawdown_shape over 63d to detect acceleration in trend.
    """
    base = (close.pct_change(4).rolling(20).mean())
    return base.diff(63)

def dsh_d2_019_vel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Velocity of 03_drawdown_shape over 126d to detect acceleration in trend.
    """
    base = (close.pct_change(4).rolling(20).mean())
    return base.diff(126)

def dsh_d2_020_vel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Velocity of 03_drawdown_shape over 252d to detect acceleration in trend.
    """
    base = (close.pct_change(4).rolling(20).mean())
    return base.diff(252)

def dsh_d2_021_vel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Velocity of 03_drawdown_shape over 5d to detect acceleration in trend.
    """
    base = (close.pct_change(5).rolling(25).mean())
    return base.diff(5)

def dsh_d2_022_vel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Velocity of 03_drawdown_shape over 21d to detect acceleration in trend.
    """
    base = (close.pct_change(5).rolling(25).mean())
    return base.diff(21)

def dsh_d2_023_vel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Velocity of 03_drawdown_shape over 63d to detect acceleration in trend.
    """
    base = (close.pct_change(5).rolling(25).mean())
    return base.diff(63)

def dsh_d2_024_vel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Velocity of 03_drawdown_shape over 126d to detect acceleration in trend.
    """
    base = (close.pct_change(5).rolling(25).mean())
    return base.diff(126)

def dsh_d2_025_vel_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Velocity of 03_drawdown_shape over 252d to detect acceleration in trend.
    """
    base = (close.pct_change(5).rolling(25).mean())
    return base.diff(252)
