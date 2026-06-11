"""
119_volume_shock_aftermath — Base Features Part 1
Domain: volume_shock_aftermath
Asset class: Equities
Target context: Capitulation
"""
import numpy as np
import pandas as pd

# ── Utility helpers ──────────────────────────────────────────────────────────
_TD_YEAR = 252
_TD_HALF = 126
_TD_QTR = 63
_TD_MON = 21
_TD_WEEK = 5
_EPS = 1e-9

def _safe_div(a: pd.Series, b: pd.Series) -> pd.Series:
    return a / b.replace(0, _EPS)

def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=1).mean()

def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=1).max()

def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=1).min()

def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=1).std().fillna(0)

def _zscore_rolling(s: pd.Series, w: int) -> pd.Series:
    m = _rolling_mean(s, w)
    sd = _rolling_std(s, w)
    return _safe_div((s - m), sd)

def _rank_pct(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=1).rank(pct=True)

# ── Feature functions ────────────────────────────────────────────────────────

def vsha_001_volume_shock_mag_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_001_volume_shock_mag_lvl_5d
    ECONOMIC RATIONALE: Magnitude of the current volume shock.
    """
    base = volume / volume.rolling(63).mean()
    return _rolling_mean(base, 5)

def vsha_002_volume_shock_mag_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_002_volume_shock_mag_zscore_5d
    ECONOMIC RATIONALE: Magnitude of the current volume shock.
    """
    base = volume / volume.rolling(63).mean()
    return _zscore_rolling(base, 5)

def vsha_003_volume_shock_mag_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_003_volume_shock_mag_rank_5d
    ECONOMIC RATIONALE: Magnitude of the current volume shock.
    """
    base = volume / volume.rolling(63).mean()
    return _rank_pct(base, 5)

def vsha_004_volume_shock_mag_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_004_volume_shock_mag_lvl_21d
    ECONOMIC RATIONALE: Magnitude of the current volume shock.
    """
    base = volume / volume.rolling(63).mean()
    return _rolling_mean(base, 21)

def vsha_005_volume_shock_mag_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_005_volume_shock_mag_zscore_21d
    ECONOMIC RATIONALE: Magnitude of the current volume shock.
    """
    base = volume / volume.rolling(63).mean()
    return _zscore_rolling(base, 21)

def vsha_006_volume_shock_mag_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_006_volume_shock_mag_rank_21d
    ECONOMIC RATIONALE: Magnitude of the current volume shock.
    """
    base = volume / volume.rolling(63).mean()
    return _rank_pct(base, 21)

def vsha_007_volume_shock_mag_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_007_volume_shock_mag_lvl_63d
    ECONOMIC RATIONALE: Magnitude of the current volume shock.
    """
    base = volume / volume.rolling(63).mean()
    return _rolling_mean(base, 63)

def vsha_008_volume_shock_mag_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_008_volume_shock_mag_zscore_63d
    ECONOMIC RATIONALE: Magnitude of the current volume shock.
    """
    base = volume / volume.rolling(63).mean()
    return _zscore_rolling(base, 63)

def vsha_009_volume_shock_mag_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_009_volume_shock_mag_rank_63d
    ECONOMIC RATIONALE: Magnitude of the current volume shock.
    """
    base = volume / volume.rolling(63).mean()
    return _rank_pct(base, 63)

def vsha_010_volume_shock_mag_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_010_volume_shock_mag_lvl_126d
    ECONOMIC RATIONALE: Magnitude of the current volume shock.
    """
    base = volume / volume.rolling(63).mean()
    return _rolling_mean(base, 126)

def vsha_011_volume_shock_mag_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_011_volume_shock_mag_zscore_126d
    ECONOMIC RATIONALE: Magnitude of the current volume shock.
    """
    base = volume / volume.rolling(63).mean()
    return _zscore_rolling(base, 126)

def vsha_012_volume_shock_mag_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_012_volume_shock_mag_rank_126d
    ECONOMIC RATIONALE: Magnitude of the current volume shock.
    """
    base = volume / volume.rolling(63).mean()
    return _rank_pct(base, 126)

def vsha_013_volume_shock_mag_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_013_volume_shock_mag_lvl_252d
    ECONOMIC RATIONALE: Magnitude of the current volume shock.
    """
    base = volume / volume.rolling(63).mean()
    return _rolling_mean(base, 252)

def vsha_014_volume_shock_mag_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_014_volume_shock_mag_zscore_252d
    ECONOMIC RATIONALE: Magnitude of the current volume shock.
    """
    base = volume / volume.rolling(63).mean()
    return _zscore_rolling(base, 252)

def vsha_015_volume_shock_mag_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_015_volume_shock_mag_rank_252d
    ECONOMIC RATIONALE: Magnitude of the current volume shock.
    """
    base = volume / volume.rolling(63).mean()
    return _rank_pct(base, 252)

def vsha_016_post_shock_drift_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_016_post_shock_drift_lvl_5d
    ECONOMIC RATIONALE: Price drift following major volume shocks.
    """
    base = close.pct_change(21) * (volume.shift(21) > volume.rolling(63).mean().shift(21)*2).astype(float)
    return _rolling_mean(base, 5)

def vsha_017_post_shock_drift_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_017_post_shock_drift_zscore_5d
    ECONOMIC RATIONALE: Price drift following major volume shocks.
    """
    base = close.pct_change(21) * (volume.shift(21) > volume.rolling(63).mean().shift(21)*2).astype(float)
    return _zscore_rolling(base, 5)

def vsha_018_post_shock_drift_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_018_post_shock_drift_rank_5d
    ECONOMIC RATIONALE: Price drift following major volume shocks.
    """
    base = close.pct_change(21) * (volume.shift(21) > volume.rolling(63).mean().shift(21)*2).astype(float)
    return _rank_pct(base, 5)

def vsha_019_post_shock_drift_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_019_post_shock_drift_lvl_21d
    ECONOMIC RATIONALE: Price drift following major volume shocks.
    """
    base = close.pct_change(21) * (volume.shift(21) > volume.rolling(63).mean().shift(21)*2).astype(float)
    return _rolling_mean(base, 21)

def vsha_020_post_shock_drift_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_020_post_shock_drift_zscore_21d
    ECONOMIC RATIONALE: Price drift following major volume shocks.
    """
    base = close.pct_change(21) * (volume.shift(21) > volume.rolling(63).mean().shift(21)*2).astype(float)
    return _zscore_rolling(base, 21)

def vsha_021_post_shock_drift_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_021_post_shock_drift_rank_21d
    ECONOMIC RATIONALE: Price drift following major volume shocks.
    """
    base = close.pct_change(21) * (volume.shift(21) > volume.rolling(63).mean().shift(21)*2).astype(float)
    return _rank_pct(base, 21)

def vsha_022_post_shock_drift_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_022_post_shock_drift_lvl_63d
    ECONOMIC RATIONALE: Price drift following major volume shocks.
    """
    base = close.pct_change(21) * (volume.shift(21) > volume.rolling(63).mean().shift(21)*2).astype(float)
    return _rolling_mean(base, 63)

def vsha_023_post_shock_drift_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_023_post_shock_drift_zscore_63d
    ECONOMIC RATIONALE: Price drift following major volume shocks.
    """
    base = close.pct_change(21) * (volume.shift(21) > volume.rolling(63).mean().shift(21)*2).astype(float)
    return _zscore_rolling(base, 63)

def vsha_024_post_shock_drift_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_024_post_shock_drift_rank_63d
    ECONOMIC RATIONALE: Price drift following major volume shocks.
    """
    base = close.pct_change(21) * (volume.shift(21) > volume.rolling(63).mean().shift(21)*2).astype(float)
    return _rank_pct(base, 63)

def vsha_025_post_shock_drift_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_025_post_shock_drift_lvl_126d
    ECONOMIC RATIONALE: Price drift following major volume shocks.
    """
    base = close.pct_change(21) * (volume.shift(21) > volume.rolling(63).mean().shift(21)*2).astype(float)
    return _rolling_mean(base, 126)

def vsha_026_post_shock_drift_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_026_post_shock_drift_zscore_126d
    ECONOMIC RATIONALE: Price drift following major volume shocks.
    """
    base = close.pct_change(21) * (volume.shift(21) > volume.rolling(63).mean().shift(21)*2).astype(float)
    return _zscore_rolling(base, 126)

def vsha_027_post_shock_drift_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_027_post_shock_drift_rank_126d
    ECONOMIC RATIONALE: Price drift following major volume shocks.
    """
    base = close.pct_change(21) * (volume.shift(21) > volume.rolling(63).mean().shift(21)*2).astype(float)
    return _rank_pct(base, 126)

def vsha_028_post_shock_drift_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_028_post_shock_drift_lvl_252d
    ECONOMIC RATIONALE: Price drift following major volume shocks.
    """
    base = close.pct_change(21) * (volume.shift(21) > volume.rolling(63).mean().shift(21)*2).astype(float)
    return _rolling_mean(base, 252)

def vsha_029_post_shock_drift_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_029_post_shock_drift_zscore_252d
    ECONOMIC RATIONALE: Price drift following major volume shocks.
    """
    base = close.pct_change(21) * (volume.shift(21) > volume.rolling(63).mean().shift(21)*2).astype(float)
    return _zscore_rolling(base, 252)

def vsha_030_post_shock_drift_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_030_post_shock_drift_rank_252d
    ECONOMIC RATIONALE: Price drift following major volume shocks.
    """
    base = close.pct_change(21) * (volume.shift(21) > volume.rolling(63).mean().shift(21)*2).astype(float)
    return _rank_pct(base, 252)

def vsha_031_shock_volatility_expansion_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_031_shock_volatility_expansion_lvl_5d
    ECONOMIC RATIONALE: Volatility expansion associated with volume shocks.
    """
    base = close.rolling(21).std() / close.rolling(252).std() * (volume > volume.rolling(63).mean()*2).astype(float)
    return _rolling_mean(base, 5)

def vsha_032_shock_volatility_expansion_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_032_shock_volatility_expansion_zscore_5d
    ECONOMIC RATIONALE: Volatility expansion associated with volume shocks.
    """
    base = close.rolling(21).std() / close.rolling(252).std() * (volume > volume.rolling(63).mean()*2).astype(float)
    return _zscore_rolling(base, 5)

def vsha_033_shock_volatility_expansion_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_033_shock_volatility_expansion_rank_5d
    ECONOMIC RATIONALE: Volatility expansion associated with volume shocks.
    """
    base = close.rolling(21).std() / close.rolling(252).std() * (volume > volume.rolling(63).mean()*2).astype(float)
    return _rank_pct(base, 5)

def vsha_034_shock_volatility_expansion_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_034_shock_volatility_expansion_lvl_21d
    ECONOMIC RATIONALE: Volatility expansion associated with volume shocks.
    """
    base = close.rolling(21).std() / close.rolling(252).std() * (volume > volume.rolling(63).mean()*2).astype(float)
    return _rolling_mean(base, 21)

def vsha_035_shock_volatility_expansion_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_035_shock_volatility_expansion_zscore_21d
    ECONOMIC RATIONALE: Volatility expansion associated with volume shocks.
    """
    base = close.rolling(21).std() / close.rolling(252).std() * (volume > volume.rolling(63).mean()*2).astype(float)
    return _zscore_rolling(base, 21)

def vsha_036_shock_volatility_expansion_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_036_shock_volatility_expansion_rank_21d
    ECONOMIC RATIONALE: Volatility expansion associated with volume shocks.
    """
    base = close.rolling(21).std() / close.rolling(252).std() * (volume > volume.rolling(63).mean()*2).astype(float)
    return _rank_pct(base, 21)

def vsha_037_shock_volatility_expansion_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_037_shock_volatility_expansion_lvl_63d
    ECONOMIC RATIONALE: Volatility expansion associated with volume shocks.
    """
    base = close.rolling(21).std() / close.rolling(252).std() * (volume > volume.rolling(63).mean()*2).astype(float)
    return _rolling_mean(base, 63)

def vsha_038_shock_volatility_expansion_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_038_shock_volatility_expansion_zscore_63d
    ECONOMIC RATIONALE: Volatility expansion associated with volume shocks.
    """
    base = close.rolling(21).std() / close.rolling(252).std() * (volume > volume.rolling(63).mean()*2).astype(float)
    return _zscore_rolling(base, 63)

def vsha_039_shock_volatility_expansion_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_039_shock_volatility_expansion_rank_63d
    ECONOMIC RATIONALE: Volatility expansion associated with volume shocks.
    """
    base = close.rolling(21).std() / close.rolling(252).std() * (volume > volume.rolling(63).mean()*2).astype(float)
    return _rank_pct(base, 63)

def vsha_040_shock_volatility_expansion_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_040_shock_volatility_expansion_lvl_126d
    ECONOMIC RATIONALE: Volatility expansion associated with volume shocks.
    """
    base = close.rolling(21).std() / close.rolling(252).std() * (volume > volume.rolling(63).mean()*2).astype(float)
    return _rolling_mean(base, 126)

def vsha_041_shock_volatility_expansion_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_041_shock_volatility_expansion_zscore_126d
    ECONOMIC RATIONALE: Volatility expansion associated with volume shocks.
    """
    base = close.rolling(21).std() / close.rolling(252).std() * (volume > volume.rolling(63).mean()*2).astype(float)
    return _zscore_rolling(base, 126)

def vsha_042_shock_volatility_expansion_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_042_shock_volatility_expansion_rank_126d
    ECONOMIC RATIONALE: Volatility expansion associated with volume shocks.
    """
    base = close.rolling(21).std() / close.rolling(252).std() * (volume > volume.rolling(63).mean()*2).astype(float)
    return _rank_pct(base, 126)

def vsha_043_shock_volatility_expansion_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_043_shock_volatility_expansion_lvl_252d
    ECONOMIC RATIONALE: Volatility expansion associated with volume shocks.
    """
    base = close.rolling(21).std() / close.rolling(252).std() * (volume > volume.rolling(63).mean()*2).astype(float)
    return _rolling_mean(base, 252)

def vsha_044_shock_volatility_expansion_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_044_shock_volatility_expansion_zscore_252d
    ECONOMIC RATIONALE: Volatility expansion associated with volume shocks.
    """
    base = close.rolling(21).std() / close.rolling(252).std() * (volume > volume.rolling(63).mean()*2).astype(float)
    return _zscore_rolling(base, 252)

def vsha_045_shock_volatility_expansion_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_045_shock_volatility_expansion_rank_252d
    ECONOMIC RATIONALE: Volatility expansion associated with volume shocks.
    """
    base = close.rolling(21).std() / close.rolling(252).std() * (volume > volume.rolling(63).mean()*2).astype(float)
    return _rank_pct(base, 252)

def vsha_046_volume_shock_reversal_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_046_volume_shock_reversal_lvl_5d
    ECONOMIC RATIONALE: Reversal of price direction after a volume shock.
    """
    base = (close.diff(5) * close.diff(5).shift(5) < 0) * (volume > volume.rolling(63).mean()*2).astype(float)
    return _rolling_mean(base, 5)

def vsha_047_volume_shock_reversal_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_047_volume_shock_reversal_zscore_5d
    ECONOMIC RATIONALE: Reversal of price direction after a volume shock.
    """
    base = (close.diff(5) * close.diff(5).shift(5) < 0) * (volume > volume.rolling(63).mean()*2).astype(float)
    return _zscore_rolling(base, 5)

def vsha_048_volume_shock_reversal_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_048_volume_shock_reversal_rank_5d
    ECONOMIC RATIONALE: Reversal of price direction after a volume shock.
    """
    base = (close.diff(5) * close.diff(5).shift(5) < 0) * (volume > volume.rolling(63).mean()*2).astype(float)
    return _rank_pct(base, 5)

def vsha_049_volume_shock_reversal_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_049_volume_shock_reversal_lvl_21d
    ECONOMIC RATIONALE: Reversal of price direction after a volume shock.
    """
    base = (close.diff(5) * close.diff(5).shift(5) < 0) * (volume > volume.rolling(63).mean()*2).astype(float)
    return _rolling_mean(base, 21)

def vsha_050_volume_shock_reversal_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_050_volume_shock_reversal_zscore_21d
    ECONOMIC RATIONALE: Reversal of price direction after a volume shock.
    """
    base = (close.diff(5) * close.diff(5).shift(5) < 0) * (volume > volume.rolling(63).mean()*2).astype(float)
    return _zscore_rolling(base, 21)

def vsha_051_volume_shock_reversal_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_051_volume_shock_reversal_rank_21d
    ECONOMIC RATIONALE: Reversal of price direction after a volume shock.
    """
    base = (close.diff(5) * close.diff(5).shift(5) < 0) * (volume > volume.rolling(63).mean()*2).astype(float)
    return _rank_pct(base, 21)

def vsha_052_volume_shock_reversal_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_052_volume_shock_reversal_lvl_63d
    ECONOMIC RATIONALE: Reversal of price direction after a volume shock.
    """
    base = (close.diff(5) * close.diff(5).shift(5) < 0) * (volume > volume.rolling(63).mean()*2).astype(float)
    return _rolling_mean(base, 63)

def vsha_053_volume_shock_reversal_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_053_volume_shock_reversal_zscore_63d
    ECONOMIC RATIONALE: Reversal of price direction after a volume shock.
    """
    base = (close.diff(5) * close.diff(5).shift(5) < 0) * (volume > volume.rolling(63).mean()*2).astype(float)
    return _zscore_rolling(base, 63)

def vsha_054_volume_shock_reversal_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_054_volume_shock_reversal_rank_63d
    ECONOMIC RATIONALE: Reversal of price direction after a volume shock.
    """
    base = (close.diff(5) * close.diff(5).shift(5) < 0) * (volume > volume.rolling(63).mean()*2).astype(float)
    return _rank_pct(base, 63)

def vsha_055_volume_shock_reversal_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_055_volume_shock_reversal_lvl_126d
    ECONOMIC RATIONALE: Reversal of price direction after a volume shock.
    """
    base = (close.diff(5) * close.diff(5).shift(5) < 0) * (volume > volume.rolling(63).mean()*2).astype(float)
    return _rolling_mean(base, 126)

def vsha_056_volume_shock_reversal_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_056_volume_shock_reversal_zscore_126d
    ECONOMIC RATIONALE: Reversal of price direction after a volume shock.
    """
    base = (close.diff(5) * close.diff(5).shift(5) < 0) * (volume > volume.rolling(63).mean()*2).astype(float)
    return _zscore_rolling(base, 126)

def vsha_057_volume_shock_reversal_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_057_volume_shock_reversal_rank_126d
    ECONOMIC RATIONALE: Reversal of price direction after a volume shock.
    """
    base = (close.diff(5) * close.diff(5).shift(5) < 0) * (volume > volume.rolling(63).mean()*2).astype(float)
    return _rank_pct(base, 126)

def vsha_058_volume_shock_reversal_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_058_volume_shock_reversal_lvl_252d
    ECONOMIC RATIONALE: Reversal of price direction after a volume shock.
    """
    base = (close.diff(5) * close.diff(5).shift(5) < 0) * (volume > volume.rolling(63).mean()*2).astype(float)
    return _rolling_mean(base, 252)

def vsha_059_volume_shock_reversal_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_059_volume_shock_reversal_zscore_252d
    ECONOMIC RATIONALE: Reversal of price direction after a volume shock.
    """
    base = (close.diff(5) * close.diff(5).shift(5) < 0) * (volume > volume.rolling(63).mean()*2).astype(float)
    return _zscore_rolling(base, 252)

def vsha_060_volume_shock_reversal_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_060_volume_shock_reversal_rank_252d
    ECONOMIC RATIONALE: Reversal of price direction after a volume shock.
    """
    base = (close.diff(5) * close.diff(5).shift(5) < 0) * (volume > volume.rolling(63).mean()*2).astype(float)
    return _rank_pct(base, 252)

def vsha_061_shock_persistence_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_061_shock_persistence_lvl_5d
    ECONOMIC RATIONALE: Duration of a high-volume regime.
    """
    base = (volume > volume.rolling(63).mean()*2).rolling(10).sum()
    return _rolling_mean(base, 5)

def vsha_062_shock_persistence_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_062_shock_persistence_zscore_5d
    ECONOMIC RATIONALE: Duration of a high-volume regime.
    """
    base = (volume > volume.rolling(63).mean()*2).rolling(10).sum()
    return _zscore_rolling(base, 5)

def vsha_063_shock_persistence_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_063_shock_persistence_rank_5d
    ECONOMIC RATIONALE: Duration of a high-volume regime.
    """
    base = (volume > volume.rolling(63).mean()*2).rolling(10).sum()
    return _rank_pct(base, 5)

def vsha_064_shock_persistence_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_064_shock_persistence_lvl_21d
    ECONOMIC RATIONALE: Duration of a high-volume regime.
    """
    base = (volume > volume.rolling(63).mean()*2).rolling(10).sum()
    return _rolling_mean(base, 21)

def vsha_065_shock_persistence_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_065_shock_persistence_zscore_21d
    ECONOMIC RATIONALE: Duration of a high-volume regime.
    """
    base = (volume > volume.rolling(63).mean()*2).rolling(10).sum()
    return _zscore_rolling(base, 21)

def vsha_066_shock_persistence_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_066_shock_persistence_rank_21d
    ECONOMIC RATIONALE: Duration of a high-volume regime.
    """
    base = (volume > volume.rolling(63).mean()*2).rolling(10).sum()
    return _rank_pct(base, 21)

def vsha_067_shock_persistence_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_067_shock_persistence_lvl_63d
    ECONOMIC RATIONALE: Duration of a high-volume regime.
    """
    base = (volume > volume.rolling(63).mean()*2).rolling(10).sum()
    return _rolling_mean(base, 63)

def vsha_068_shock_persistence_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_068_shock_persistence_zscore_63d
    ECONOMIC RATIONALE: Duration of a high-volume regime.
    """
    base = (volume > volume.rolling(63).mean()*2).rolling(10).sum()
    return _zscore_rolling(base, 63)

def vsha_069_shock_persistence_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_069_shock_persistence_rank_63d
    ECONOMIC RATIONALE: Duration of a high-volume regime.
    """
    base = (volume > volume.rolling(63).mean()*2).rolling(10).sum()
    return _rank_pct(base, 63)

def vsha_070_shock_persistence_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_070_shock_persistence_lvl_126d
    ECONOMIC RATIONALE: Duration of a high-volume regime.
    """
    base = (volume > volume.rolling(63).mean()*2).rolling(10).sum()
    return _rolling_mean(base, 126)

def vsha_071_shock_persistence_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_071_shock_persistence_zscore_126d
    ECONOMIC RATIONALE: Duration of a high-volume regime.
    """
    base = (volume > volume.rolling(63).mean()*2).rolling(10).sum()
    return _zscore_rolling(base, 126)

def vsha_072_shock_persistence_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_072_shock_persistence_rank_126d
    ECONOMIC RATIONALE: Duration of a high-volume regime.
    """
    base = (volume > volume.rolling(63).mean()*2).rolling(10).sum()
    return _rank_pct(base, 126)

def vsha_073_shock_persistence_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_073_shock_persistence_lvl_252d
    ECONOMIC RATIONALE: Duration of a high-volume regime.
    """
    base = (volume > volume.rolling(63).mean()*2).rolling(10).sum()
    return _rolling_mean(base, 252)

def vsha_074_shock_persistence_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_074_shock_persistence_zscore_252d
    ECONOMIC RATIONALE: Duration of a high-volume regime.
    """
    base = (volume > volume.rolling(63).mean()*2).rolling(10).sum()
    return _zscore_rolling(base, 252)

def vsha_075_shock_persistence_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_075_shock_persistence_rank_252d
    ECONOMIC RATIONALE: Duration of a high-volume regime.
    """
    base = (volume > volume.rolling(63).mean()*2).rolling(10).sum()
    return _rank_pct(base, 252)

def vsha_076_volume_shock_z_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_076_volume_shock_z_lvl_5d
    ECONOMIC RATIONALE: Z-score of volume relative to annual history.
    """
    base = _zscore_rolling(volume, 252)
    return _rolling_mean(base, 5)

def vsha_077_volume_shock_z_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_077_volume_shock_z_zscore_5d
    ECONOMIC RATIONALE: Z-score of volume relative to annual history.
    """
    base = _zscore_rolling(volume, 252)
    return _zscore_rolling(base, 5)

def vsha_078_volume_shock_z_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_078_volume_shock_z_rank_5d
    ECONOMIC RATIONALE: Z-score of volume relative to annual history.
    """
    base = _zscore_rolling(volume, 252)
    return _rank_pct(base, 5)

def vsha_079_volume_shock_z_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_079_volume_shock_z_lvl_21d
    ECONOMIC RATIONALE: Z-score of volume relative to annual history.
    """
    base = _zscore_rolling(volume, 252)
    return _rolling_mean(base, 21)

def vsha_080_volume_shock_z_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_080_volume_shock_z_zscore_21d
    ECONOMIC RATIONALE: Z-score of volume relative to annual history.
    """
    base = _zscore_rolling(volume, 252)
    return _zscore_rolling(base, 21)

def vsha_081_volume_shock_z_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_081_volume_shock_z_rank_21d
    ECONOMIC RATIONALE: Z-score of volume relative to annual history.
    """
    base = _zscore_rolling(volume, 252)
    return _rank_pct(base, 21)

def vsha_082_volume_shock_z_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_082_volume_shock_z_lvl_63d
    ECONOMIC RATIONALE: Z-score of volume relative to annual history.
    """
    base = _zscore_rolling(volume, 252)
    return _rolling_mean(base, 63)

def vsha_083_volume_shock_z_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_083_volume_shock_z_zscore_63d
    ECONOMIC RATIONALE: Z-score of volume relative to annual history.
    """
    base = _zscore_rolling(volume, 252)
    return _zscore_rolling(base, 63)

def vsha_084_volume_shock_z_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_084_volume_shock_z_rank_63d
    ECONOMIC RATIONALE: Z-score of volume relative to annual history.
    """
    base = _zscore_rolling(volume, 252)
    return _rank_pct(base, 63)

def vsha_085_volume_shock_z_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_085_volume_shock_z_lvl_126d
    ECONOMIC RATIONALE: Z-score of volume relative to annual history.
    """
    base = _zscore_rolling(volume, 252)
    return _rolling_mean(base, 126)

def vsha_086_volume_shock_z_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_086_volume_shock_z_zscore_126d
    ECONOMIC RATIONALE: Z-score of volume relative to annual history.
    """
    base = _zscore_rolling(volume, 252)
    return _zscore_rolling(base, 126)

def vsha_087_volume_shock_z_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_087_volume_shock_z_rank_126d
    ECONOMIC RATIONALE: Z-score of volume relative to annual history.
    """
    base = _zscore_rolling(volume, 252)
    return _rank_pct(base, 126)

def vsha_088_volume_shock_z_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_088_volume_shock_z_lvl_252d
    ECONOMIC RATIONALE: Z-score of volume relative to annual history.
    """
    base = _zscore_rolling(volume, 252)
    return _rolling_mean(base, 252)

def vsha_089_volume_shock_z_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_089_volume_shock_z_zscore_252d
    ECONOMIC RATIONALE: Z-score of volume relative to annual history.
    """
    base = _zscore_rolling(volume, 252)
    return _zscore_rolling(base, 252)

def vsha_090_volume_shock_z_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_090_volume_shock_z_rank_252d
    ECONOMIC RATIONALE: Z-score of volume relative to annual history.
    """
    base = _zscore_rolling(volume, 252)
    return _rank_pct(base, 252)

def vsha_091_shock_price_impact_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_091_shock_price_impact_lvl_5d
    ECONOMIC RATIONALE: Price change weighted by the volume shock magnitude.
    """
    base = close.diff(1) * (volume / volume.rolling(63).mean())
    return _rolling_mean(base, 5)

def vsha_092_shock_price_impact_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_092_shock_price_impact_zscore_5d
    ECONOMIC RATIONALE: Price change weighted by the volume shock magnitude.
    """
    base = close.diff(1) * (volume / volume.rolling(63).mean())
    return _zscore_rolling(base, 5)

def vsha_093_shock_price_impact_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_093_shock_price_impact_rank_5d
    ECONOMIC RATIONALE: Price change weighted by the volume shock magnitude.
    """
    base = close.diff(1) * (volume / volume.rolling(63).mean())
    return _rank_pct(base, 5)

def vsha_094_shock_price_impact_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_094_shock_price_impact_lvl_21d
    ECONOMIC RATIONALE: Price change weighted by the volume shock magnitude.
    """
    base = close.diff(1) * (volume / volume.rolling(63).mean())
    return _rolling_mean(base, 21)

def vsha_095_shock_price_impact_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_095_shock_price_impact_zscore_21d
    ECONOMIC RATIONALE: Price change weighted by the volume shock magnitude.
    """
    base = close.diff(1) * (volume / volume.rolling(63).mean())
    return _zscore_rolling(base, 21)

def vsha_096_shock_price_impact_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_096_shock_price_impact_rank_21d
    ECONOMIC RATIONALE: Price change weighted by the volume shock magnitude.
    """
    base = close.diff(1) * (volume / volume.rolling(63).mean())
    return _rank_pct(base, 21)

def vsha_097_shock_price_impact_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_097_shock_price_impact_lvl_63d
    ECONOMIC RATIONALE: Price change weighted by the volume shock magnitude.
    """
    base = close.diff(1) * (volume / volume.rolling(63).mean())
    return _rolling_mean(base, 63)

def vsha_098_shock_price_impact_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_098_shock_price_impact_zscore_63d
    ECONOMIC RATIONALE: Price change weighted by the volume shock magnitude.
    """
    base = close.diff(1) * (volume / volume.rolling(63).mean())
    return _zscore_rolling(base, 63)

def vsha_099_shock_price_impact_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_099_shock_price_impact_rank_63d
    ECONOMIC RATIONALE: Price change weighted by the volume shock magnitude.
    """
    base = close.diff(1) * (volume / volume.rolling(63).mean())
    return _rank_pct(base, 63)

def vsha_100_shock_price_impact_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_100_shock_price_impact_lvl_126d
    ECONOMIC RATIONALE: Price change weighted by the volume shock magnitude.
    """
    base = close.diff(1) * (volume / volume.rolling(63).mean())
    return _rolling_mean(base, 126)

def vsha_101_shock_price_impact_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_101_shock_price_impact_zscore_126d
    ECONOMIC RATIONALE: Price change weighted by the volume shock magnitude.
    """
    base = close.diff(1) * (volume / volume.rolling(63).mean())
    return _zscore_rolling(base, 126)

def vsha_102_shock_price_impact_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_102_shock_price_impact_rank_126d
    ECONOMIC RATIONALE: Price change weighted by the volume shock magnitude.
    """
    base = close.diff(1) * (volume / volume.rolling(63).mean())
    return _rank_pct(base, 126)

def vsha_103_shock_price_impact_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_103_shock_price_impact_lvl_252d
    ECONOMIC RATIONALE: Price change weighted by the volume shock magnitude.
    """
    base = close.diff(1) * (volume / volume.rolling(63).mean())
    return _rolling_mean(base, 252)

def vsha_104_shock_price_impact_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_104_shock_price_impact_zscore_252d
    ECONOMIC RATIONALE: Price change weighted by the volume shock magnitude.
    """
    base = close.diff(1) * (volume / volume.rolling(63).mean())
    return _zscore_rolling(base, 252)

def vsha_105_shock_price_impact_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_105_shock_price_impact_rank_252d
    ECONOMIC RATIONALE: Price change weighted by the volume shock magnitude.
    """
    base = close.diff(1) * (volume / volume.rolling(63).mean())
    return _rank_pct(base, 252)

def vsha_106_post_shock_liquidity_drain_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_106_post_shock_liquidity_drain_lvl_5d
    ECONOMIC RATIONALE: Liquidity dry-up following a massive shock.
    """
    base = (volume.rolling(5).mean() / volume.rolling(63).mean()) * (volume.shift(21) > volume.rolling(63).mean().shift(21)*3).astype(float)
    return _rolling_mean(base, 5)

def vsha_107_post_shock_liquidity_drain_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_107_post_shock_liquidity_drain_zscore_5d
    ECONOMIC RATIONALE: Liquidity dry-up following a massive shock.
    """
    base = (volume.rolling(5).mean() / volume.rolling(63).mean()) * (volume.shift(21) > volume.rolling(63).mean().shift(21)*3).astype(float)
    return _zscore_rolling(base, 5)

def vsha_108_post_shock_liquidity_drain_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_108_post_shock_liquidity_drain_rank_5d
    ECONOMIC RATIONALE: Liquidity dry-up following a massive shock.
    """
    base = (volume.rolling(5).mean() / volume.rolling(63).mean()) * (volume.shift(21) > volume.rolling(63).mean().shift(21)*3).astype(float)
    return _rank_pct(base, 5)

def vsha_109_post_shock_liquidity_drain_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_109_post_shock_liquidity_drain_lvl_21d
    ECONOMIC RATIONALE: Liquidity dry-up following a massive shock.
    """
    base = (volume.rolling(5).mean() / volume.rolling(63).mean()) * (volume.shift(21) > volume.rolling(63).mean().shift(21)*3).astype(float)
    return _rolling_mean(base, 21)

def vsha_110_post_shock_liquidity_drain_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_110_post_shock_liquidity_drain_zscore_21d
    ECONOMIC RATIONALE: Liquidity dry-up following a massive shock.
    """
    base = (volume.rolling(5).mean() / volume.rolling(63).mean()) * (volume.shift(21) > volume.rolling(63).mean().shift(21)*3).astype(float)
    return _zscore_rolling(base, 21)

def vsha_111_post_shock_liquidity_drain_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_111_post_shock_liquidity_drain_rank_21d
    ECONOMIC RATIONALE: Liquidity dry-up following a massive shock.
    """
    base = (volume.rolling(5).mean() / volume.rolling(63).mean()) * (volume.shift(21) > volume.rolling(63).mean().shift(21)*3).astype(float)
    return _rank_pct(base, 21)

def vsha_112_post_shock_liquidity_drain_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_112_post_shock_liquidity_drain_lvl_63d
    ECONOMIC RATIONALE: Liquidity dry-up following a massive shock.
    """
    base = (volume.rolling(5).mean() / volume.rolling(63).mean()) * (volume.shift(21) > volume.rolling(63).mean().shift(21)*3).astype(float)
    return _rolling_mean(base, 63)

def vsha_113_post_shock_liquidity_drain_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_113_post_shock_liquidity_drain_zscore_63d
    ECONOMIC RATIONALE: Liquidity dry-up following a massive shock.
    """
    base = (volume.rolling(5).mean() / volume.rolling(63).mean()) * (volume.shift(21) > volume.rolling(63).mean().shift(21)*3).astype(float)
    return _zscore_rolling(base, 63)

def vsha_114_post_shock_liquidity_drain_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_114_post_shock_liquidity_drain_rank_63d
    ECONOMIC RATIONALE: Liquidity dry-up following a massive shock.
    """
    base = (volume.rolling(5).mean() / volume.rolling(63).mean()) * (volume.shift(21) > volume.rolling(63).mean().shift(21)*3).astype(float)
    return _rank_pct(base, 63)

def vsha_115_post_shock_liquidity_drain_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_115_post_shock_liquidity_drain_lvl_126d
    ECONOMIC RATIONALE: Liquidity dry-up following a massive shock.
    """
    base = (volume.rolling(5).mean() / volume.rolling(63).mean()) * (volume.shift(21) > volume.rolling(63).mean().shift(21)*3).astype(float)
    return _rolling_mean(base, 126)

def vsha_116_post_shock_liquidity_drain_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_116_post_shock_liquidity_drain_zscore_126d
    ECONOMIC RATIONALE: Liquidity dry-up following a massive shock.
    """
    base = (volume.rolling(5).mean() / volume.rolling(63).mean()) * (volume.shift(21) > volume.rolling(63).mean().shift(21)*3).astype(float)
    return _zscore_rolling(base, 126)

def vsha_117_post_shock_liquidity_drain_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_117_post_shock_liquidity_drain_rank_126d
    ECONOMIC RATIONALE: Liquidity dry-up following a massive shock.
    """
    base = (volume.rolling(5).mean() / volume.rolling(63).mean()) * (volume.shift(21) > volume.rolling(63).mean().shift(21)*3).astype(float)
    return _rank_pct(base, 126)

def vsha_118_post_shock_liquidity_drain_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_118_post_shock_liquidity_drain_lvl_252d
    ECONOMIC RATIONALE: Liquidity dry-up following a massive shock.
    """
    base = (volume.rolling(5).mean() / volume.rolling(63).mean()) * (volume.shift(21) > volume.rolling(63).mean().shift(21)*3).astype(float)
    return _rolling_mean(base, 252)

def vsha_119_post_shock_liquidity_drain_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_119_post_shock_liquidity_drain_zscore_252d
    ECONOMIC RATIONALE: Liquidity dry-up following a massive shock.
    """
    base = (volume.rolling(5).mean() / volume.rolling(63).mean()) * (volume.shift(21) > volume.rolling(63).mean().shift(21)*3).astype(float)
    return _zscore_rolling(base, 252)

def vsha_120_post_shock_liquidity_drain_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    vsha_120_post_shock_liquidity_drain_rank_252d
    ECONOMIC RATIONALE: Liquidity dry-up following a massive shock.
    """
    base = (volume.rolling(5).mean() / volume.rolling(63).mean()) * (volume.shift(21) > volume.rolling(63).mean().shift(21)*3).astype(float)
    return _rank_pct(base, 252)

# ── Registry ──────────────────────────────────────────────────────────────────
V119_REGISTRY_1 = {
    "vsha_001_volume_shock_mag_lvl_5d": {"inputs": ["close", "volume"], "func": vsha_001_volume_shock_mag_lvl_5d},
    "vsha_002_volume_shock_mag_zscore_5d": {"inputs": ["close", "volume"], "func": vsha_002_volume_shock_mag_zscore_5d},
    "vsha_003_volume_shock_mag_rank_5d": {"inputs": ["close", "volume"], "func": vsha_003_volume_shock_mag_rank_5d},
    "vsha_004_volume_shock_mag_lvl_21d": {"inputs": ["close", "volume"], "func": vsha_004_volume_shock_mag_lvl_21d},
    "vsha_005_volume_shock_mag_zscore_21d": {"inputs": ["close", "volume"], "func": vsha_005_volume_shock_mag_zscore_21d},
    "vsha_006_volume_shock_mag_rank_21d": {"inputs": ["close", "volume"], "func": vsha_006_volume_shock_mag_rank_21d},
    "vsha_007_volume_shock_mag_lvl_63d": {"inputs": ["close", "volume"], "func": vsha_007_volume_shock_mag_lvl_63d},
    "vsha_008_volume_shock_mag_zscore_63d": {"inputs": ["close", "volume"], "func": vsha_008_volume_shock_mag_zscore_63d},
    "vsha_009_volume_shock_mag_rank_63d": {"inputs": ["close", "volume"], "func": vsha_009_volume_shock_mag_rank_63d},
    "vsha_010_volume_shock_mag_lvl_126d": {"inputs": ["close", "volume"], "func": vsha_010_volume_shock_mag_lvl_126d},
    "vsha_011_volume_shock_mag_zscore_126d": {"inputs": ["close", "volume"], "func": vsha_011_volume_shock_mag_zscore_126d},
    "vsha_012_volume_shock_mag_rank_126d": {"inputs": ["close", "volume"], "func": vsha_012_volume_shock_mag_rank_126d},
    "vsha_013_volume_shock_mag_lvl_252d": {"inputs": ["close", "volume"], "func": vsha_013_volume_shock_mag_lvl_252d},
    "vsha_014_volume_shock_mag_zscore_252d": {"inputs": ["close", "volume"], "func": vsha_014_volume_shock_mag_zscore_252d},
    "vsha_015_volume_shock_mag_rank_252d": {"inputs": ["close", "volume"], "func": vsha_015_volume_shock_mag_rank_252d},
    "vsha_016_post_shock_drift_lvl_5d": {"inputs": ["close", "volume"], "func": vsha_016_post_shock_drift_lvl_5d},
    "vsha_017_post_shock_drift_zscore_5d": {"inputs": ["close", "volume"], "func": vsha_017_post_shock_drift_zscore_5d},
    "vsha_018_post_shock_drift_rank_5d": {"inputs": ["close", "volume"], "func": vsha_018_post_shock_drift_rank_5d},
    "vsha_019_post_shock_drift_lvl_21d": {"inputs": ["close", "volume"], "func": vsha_019_post_shock_drift_lvl_21d},
    "vsha_020_post_shock_drift_zscore_21d": {"inputs": ["close", "volume"], "func": vsha_020_post_shock_drift_zscore_21d},
    "vsha_021_post_shock_drift_rank_21d": {"inputs": ["close", "volume"], "func": vsha_021_post_shock_drift_rank_21d},
    "vsha_022_post_shock_drift_lvl_63d": {"inputs": ["close", "volume"], "func": vsha_022_post_shock_drift_lvl_63d},
    "vsha_023_post_shock_drift_zscore_63d": {"inputs": ["close", "volume"], "func": vsha_023_post_shock_drift_zscore_63d},
    "vsha_024_post_shock_drift_rank_63d": {"inputs": ["close", "volume"], "func": vsha_024_post_shock_drift_rank_63d},
    "vsha_025_post_shock_drift_lvl_126d": {"inputs": ["close", "volume"], "func": vsha_025_post_shock_drift_lvl_126d},
    "vsha_026_post_shock_drift_zscore_126d": {"inputs": ["close", "volume"], "func": vsha_026_post_shock_drift_zscore_126d},
    "vsha_027_post_shock_drift_rank_126d": {"inputs": ["close", "volume"], "func": vsha_027_post_shock_drift_rank_126d},
    "vsha_028_post_shock_drift_lvl_252d": {"inputs": ["close", "volume"], "func": vsha_028_post_shock_drift_lvl_252d},
    "vsha_029_post_shock_drift_zscore_252d": {"inputs": ["close", "volume"], "func": vsha_029_post_shock_drift_zscore_252d},
    "vsha_030_post_shock_drift_rank_252d": {"inputs": ["close", "volume"], "func": vsha_030_post_shock_drift_rank_252d},
    "vsha_031_shock_volatility_expansion_lvl_5d": {"inputs": ["close", "volume"], "func": vsha_031_shock_volatility_expansion_lvl_5d},
    "vsha_032_shock_volatility_expansion_zscore_5d": {"inputs": ["close", "volume"], "func": vsha_032_shock_volatility_expansion_zscore_5d},
    "vsha_033_shock_volatility_expansion_rank_5d": {"inputs": ["close", "volume"], "func": vsha_033_shock_volatility_expansion_rank_5d},
    "vsha_034_shock_volatility_expansion_lvl_21d": {"inputs": ["close", "volume"], "func": vsha_034_shock_volatility_expansion_lvl_21d},
    "vsha_035_shock_volatility_expansion_zscore_21d": {"inputs": ["close", "volume"], "func": vsha_035_shock_volatility_expansion_zscore_21d},
    "vsha_036_shock_volatility_expansion_rank_21d": {"inputs": ["close", "volume"], "func": vsha_036_shock_volatility_expansion_rank_21d},
    "vsha_037_shock_volatility_expansion_lvl_63d": {"inputs": ["close", "volume"], "func": vsha_037_shock_volatility_expansion_lvl_63d},
    "vsha_038_shock_volatility_expansion_zscore_63d": {"inputs": ["close", "volume"], "func": vsha_038_shock_volatility_expansion_zscore_63d},
    "vsha_039_shock_volatility_expansion_rank_63d": {"inputs": ["close", "volume"], "func": vsha_039_shock_volatility_expansion_rank_63d},
    "vsha_040_shock_volatility_expansion_lvl_126d": {"inputs": ["close", "volume"], "func": vsha_040_shock_volatility_expansion_lvl_126d},
    "vsha_041_shock_volatility_expansion_zscore_126d": {"inputs": ["close", "volume"], "func": vsha_041_shock_volatility_expansion_zscore_126d},
    "vsha_042_shock_volatility_expansion_rank_126d": {"inputs": ["close", "volume"], "func": vsha_042_shock_volatility_expansion_rank_126d},
    "vsha_043_shock_volatility_expansion_lvl_252d": {"inputs": ["close", "volume"], "func": vsha_043_shock_volatility_expansion_lvl_252d},
    "vsha_044_shock_volatility_expansion_zscore_252d": {"inputs": ["close", "volume"], "func": vsha_044_shock_volatility_expansion_zscore_252d},
    "vsha_045_shock_volatility_expansion_rank_252d": {"inputs": ["close", "volume"], "func": vsha_045_shock_volatility_expansion_rank_252d},
    "vsha_046_volume_shock_reversal_lvl_5d": {"inputs": ["close", "volume"], "func": vsha_046_volume_shock_reversal_lvl_5d},
    "vsha_047_volume_shock_reversal_zscore_5d": {"inputs": ["close", "volume"], "func": vsha_047_volume_shock_reversal_zscore_5d},
    "vsha_048_volume_shock_reversal_rank_5d": {"inputs": ["close", "volume"], "func": vsha_048_volume_shock_reversal_rank_5d},
    "vsha_049_volume_shock_reversal_lvl_21d": {"inputs": ["close", "volume"], "func": vsha_049_volume_shock_reversal_lvl_21d},
    "vsha_050_volume_shock_reversal_zscore_21d": {"inputs": ["close", "volume"], "func": vsha_050_volume_shock_reversal_zscore_21d},
    "vsha_051_volume_shock_reversal_rank_21d": {"inputs": ["close", "volume"], "func": vsha_051_volume_shock_reversal_rank_21d},
    "vsha_052_volume_shock_reversal_lvl_63d": {"inputs": ["close", "volume"], "func": vsha_052_volume_shock_reversal_lvl_63d},
    "vsha_053_volume_shock_reversal_zscore_63d": {"inputs": ["close", "volume"], "func": vsha_053_volume_shock_reversal_zscore_63d},
    "vsha_054_volume_shock_reversal_rank_63d": {"inputs": ["close", "volume"], "func": vsha_054_volume_shock_reversal_rank_63d},
    "vsha_055_volume_shock_reversal_lvl_126d": {"inputs": ["close", "volume"], "func": vsha_055_volume_shock_reversal_lvl_126d},
    "vsha_056_volume_shock_reversal_zscore_126d": {"inputs": ["close", "volume"], "func": vsha_056_volume_shock_reversal_zscore_126d},
    "vsha_057_volume_shock_reversal_rank_126d": {"inputs": ["close", "volume"], "func": vsha_057_volume_shock_reversal_rank_126d},
    "vsha_058_volume_shock_reversal_lvl_252d": {"inputs": ["close", "volume"], "func": vsha_058_volume_shock_reversal_lvl_252d},
    "vsha_059_volume_shock_reversal_zscore_252d": {"inputs": ["close", "volume"], "func": vsha_059_volume_shock_reversal_zscore_252d},
    "vsha_060_volume_shock_reversal_rank_252d": {"inputs": ["close", "volume"], "func": vsha_060_volume_shock_reversal_rank_252d},
    "vsha_061_shock_persistence_lvl_5d": {"inputs": ["close", "volume"], "func": vsha_061_shock_persistence_lvl_5d},
    "vsha_062_shock_persistence_zscore_5d": {"inputs": ["close", "volume"], "func": vsha_062_shock_persistence_zscore_5d},
    "vsha_063_shock_persistence_rank_5d": {"inputs": ["close", "volume"], "func": vsha_063_shock_persistence_rank_5d},
    "vsha_064_shock_persistence_lvl_21d": {"inputs": ["close", "volume"], "func": vsha_064_shock_persistence_lvl_21d},
    "vsha_065_shock_persistence_zscore_21d": {"inputs": ["close", "volume"], "func": vsha_065_shock_persistence_zscore_21d},
    "vsha_066_shock_persistence_rank_21d": {"inputs": ["close", "volume"], "func": vsha_066_shock_persistence_rank_21d},
    "vsha_067_shock_persistence_lvl_63d": {"inputs": ["close", "volume"], "func": vsha_067_shock_persistence_lvl_63d},
    "vsha_068_shock_persistence_zscore_63d": {"inputs": ["close", "volume"], "func": vsha_068_shock_persistence_zscore_63d},
    "vsha_069_shock_persistence_rank_63d": {"inputs": ["close", "volume"], "func": vsha_069_shock_persistence_rank_63d},
    "vsha_070_shock_persistence_lvl_126d": {"inputs": ["close", "volume"], "func": vsha_070_shock_persistence_lvl_126d},
    "vsha_071_shock_persistence_zscore_126d": {"inputs": ["close", "volume"], "func": vsha_071_shock_persistence_zscore_126d},
    "vsha_072_shock_persistence_rank_126d": {"inputs": ["close", "volume"], "func": vsha_072_shock_persistence_rank_126d},
    "vsha_073_shock_persistence_lvl_252d": {"inputs": ["close", "volume"], "func": vsha_073_shock_persistence_lvl_252d},
    "vsha_074_shock_persistence_zscore_252d": {"inputs": ["close", "volume"], "func": vsha_074_shock_persistence_zscore_252d},
    "vsha_075_shock_persistence_rank_252d": {"inputs": ["close", "volume"], "func": vsha_075_shock_persistence_rank_252d},
    "vsha_076_volume_shock_z_lvl_5d": {"inputs": ["close", "volume"], "func": vsha_076_volume_shock_z_lvl_5d},
    "vsha_077_volume_shock_z_zscore_5d": {"inputs": ["close", "volume"], "func": vsha_077_volume_shock_z_zscore_5d},
    "vsha_078_volume_shock_z_rank_5d": {"inputs": ["close", "volume"], "func": vsha_078_volume_shock_z_rank_5d},
    "vsha_079_volume_shock_z_lvl_21d": {"inputs": ["close", "volume"], "func": vsha_079_volume_shock_z_lvl_21d},
    "vsha_080_volume_shock_z_zscore_21d": {"inputs": ["close", "volume"], "func": vsha_080_volume_shock_z_zscore_21d},
    "vsha_081_volume_shock_z_rank_21d": {"inputs": ["close", "volume"], "func": vsha_081_volume_shock_z_rank_21d},
    "vsha_082_volume_shock_z_lvl_63d": {"inputs": ["close", "volume"], "func": vsha_082_volume_shock_z_lvl_63d},
    "vsha_083_volume_shock_z_zscore_63d": {"inputs": ["close", "volume"], "func": vsha_083_volume_shock_z_zscore_63d},
    "vsha_084_volume_shock_z_rank_63d": {"inputs": ["close", "volume"], "func": vsha_084_volume_shock_z_rank_63d},
    "vsha_085_volume_shock_z_lvl_126d": {"inputs": ["close", "volume"], "func": vsha_085_volume_shock_z_lvl_126d},
    "vsha_086_volume_shock_z_zscore_126d": {"inputs": ["close", "volume"], "func": vsha_086_volume_shock_z_zscore_126d},
    "vsha_087_volume_shock_z_rank_126d": {"inputs": ["close", "volume"], "func": vsha_087_volume_shock_z_rank_126d},
    "vsha_088_volume_shock_z_lvl_252d": {"inputs": ["close", "volume"], "func": vsha_088_volume_shock_z_lvl_252d},
    "vsha_089_volume_shock_z_zscore_252d": {"inputs": ["close", "volume"], "func": vsha_089_volume_shock_z_zscore_252d},
    "vsha_090_volume_shock_z_rank_252d": {"inputs": ["close", "volume"], "func": vsha_090_volume_shock_z_rank_252d},
    "vsha_091_shock_price_impact_lvl_5d": {"inputs": ["close", "volume"], "func": vsha_091_shock_price_impact_lvl_5d},
    "vsha_092_shock_price_impact_zscore_5d": {"inputs": ["close", "volume"], "func": vsha_092_shock_price_impact_zscore_5d},
    "vsha_093_shock_price_impact_rank_5d": {"inputs": ["close", "volume"], "func": vsha_093_shock_price_impact_rank_5d},
    "vsha_094_shock_price_impact_lvl_21d": {"inputs": ["close", "volume"], "func": vsha_094_shock_price_impact_lvl_21d},
    "vsha_095_shock_price_impact_zscore_21d": {"inputs": ["close", "volume"], "func": vsha_095_shock_price_impact_zscore_21d},
    "vsha_096_shock_price_impact_rank_21d": {"inputs": ["close", "volume"], "func": vsha_096_shock_price_impact_rank_21d},
    "vsha_097_shock_price_impact_lvl_63d": {"inputs": ["close", "volume"], "func": vsha_097_shock_price_impact_lvl_63d},
    "vsha_098_shock_price_impact_zscore_63d": {"inputs": ["close", "volume"], "func": vsha_098_shock_price_impact_zscore_63d},
    "vsha_099_shock_price_impact_rank_63d": {"inputs": ["close", "volume"], "func": vsha_099_shock_price_impact_rank_63d},
    "vsha_100_shock_price_impact_lvl_126d": {"inputs": ["close", "volume"], "func": vsha_100_shock_price_impact_lvl_126d},
    "vsha_101_shock_price_impact_zscore_126d": {"inputs": ["close", "volume"], "func": vsha_101_shock_price_impact_zscore_126d},
    "vsha_102_shock_price_impact_rank_126d": {"inputs": ["close", "volume"], "func": vsha_102_shock_price_impact_rank_126d},
    "vsha_103_shock_price_impact_lvl_252d": {"inputs": ["close", "volume"], "func": vsha_103_shock_price_impact_lvl_252d},
    "vsha_104_shock_price_impact_zscore_252d": {"inputs": ["close", "volume"], "func": vsha_104_shock_price_impact_zscore_252d},
    "vsha_105_shock_price_impact_rank_252d": {"inputs": ["close", "volume"], "func": vsha_105_shock_price_impact_rank_252d},
    "vsha_106_post_shock_liquidity_drain_lvl_5d": {"inputs": ["close", "volume"], "func": vsha_106_post_shock_liquidity_drain_lvl_5d},
    "vsha_107_post_shock_liquidity_drain_zscore_5d": {"inputs": ["close", "volume"], "func": vsha_107_post_shock_liquidity_drain_zscore_5d},
    "vsha_108_post_shock_liquidity_drain_rank_5d": {"inputs": ["close", "volume"], "func": vsha_108_post_shock_liquidity_drain_rank_5d},
    "vsha_109_post_shock_liquidity_drain_lvl_21d": {"inputs": ["close", "volume"], "func": vsha_109_post_shock_liquidity_drain_lvl_21d},
    "vsha_110_post_shock_liquidity_drain_zscore_21d": {"inputs": ["close", "volume"], "func": vsha_110_post_shock_liquidity_drain_zscore_21d},
    "vsha_111_post_shock_liquidity_drain_rank_21d": {"inputs": ["close", "volume"], "func": vsha_111_post_shock_liquidity_drain_rank_21d},
    "vsha_112_post_shock_liquidity_drain_lvl_63d": {"inputs": ["close", "volume"], "func": vsha_112_post_shock_liquidity_drain_lvl_63d},
    "vsha_113_post_shock_liquidity_drain_zscore_63d": {"inputs": ["close", "volume"], "func": vsha_113_post_shock_liquidity_drain_zscore_63d},
    "vsha_114_post_shock_liquidity_drain_rank_63d": {"inputs": ["close", "volume"], "func": vsha_114_post_shock_liquidity_drain_rank_63d},
    "vsha_115_post_shock_liquidity_drain_lvl_126d": {"inputs": ["close", "volume"], "func": vsha_115_post_shock_liquidity_drain_lvl_126d},
    "vsha_116_post_shock_liquidity_drain_zscore_126d": {"inputs": ["close", "volume"], "func": vsha_116_post_shock_liquidity_drain_zscore_126d},
    "vsha_117_post_shock_liquidity_drain_rank_126d": {"inputs": ["close", "volume"], "func": vsha_117_post_shock_liquidity_drain_rank_126d},
    "vsha_118_post_shock_liquidity_drain_lvl_252d": {"inputs": ["close", "volume"], "func": vsha_118_post_shock_liquidity_drain_lvl_252d},
    "vsha_119_post_shock_liquidity_drain_zscore_252d": {"inputs": ["close", "volume"], "func": vsha_119_post_shock_liquidity_drain_zscore_252d},
    "vsha_120_post_shock_liquidity_drain_rank_252d": {"inputs": ["close", "volume"], "func": vsha_120_post_shock_liquidity_drain_rank_252d},
}
