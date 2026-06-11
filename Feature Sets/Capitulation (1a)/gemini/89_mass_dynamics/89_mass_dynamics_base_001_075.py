"""
89_mass_dynamics — Base Features 001-075
Domain: mass_dynamics
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

def mass_001_range_ema_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_001_range_ema_lvl_5d"""
    base = (high - low).ewm(span=9).mean()
    return _rolling_mean(base, 5)

def mass_002_range_ema_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_002_range_ema_zscore_5d"""
    base = (high - low).ewm(span=9).mean()
    return _zscore_rolling(base, 5)

def mass_003_range_ema_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_003_range_ema_rank_5d"""
    base = (high - low).ewm(span=9).mean()
    return _rank_pct(base, 5)

def mass_004_range_ema_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_004_range_ema_lvl_21d"""
    base = (high - low).ewm(span=9).mean()
    return _rolling_mean(base, 21)

def mass_005_range_ema_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_005_range_ema_zscore_21d"""
    base = (high - low).ewm(span=9).mean()
    return _zscore_rolling(base, 21)

def mass_006_range_ema_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_006_range_ema_rank_21d"""
    base = (high - low).ewm(span=9).mean()
    return _rank_pct(base, 21)

def mass_007_range_ema_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_007_range_ema_lvl_63d"""
    base = (high - low).ewm(span=9).mean()
    return _rolling_mean(base, 63)

def mass_008_range_ema_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_008_range_ema_zscore_63d"""
    base = (high - low).ewm(span=9).mean()
    return _zscore_rolling(base, 63)

def mass_009_range_ema_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_009_range_ema_rank_63d"""
    base = (high - low).ewm(span=9).mean()
    return _rank_pct(base, 63)

def mass_010_range_ema_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_010_range_ema_lvl_126d"""
    base = (high - low).ewm(span=9).mean()
    return _rolling_mean(base, 126)

def mass_011_range_ema_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_011_range_ema_zscore_126d"""
    base = (high - low).ewm(span=9).mean()
    return _zscore_rolling(base, 126)

def mass_012_range_ema_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_012_range_ema_rank_126d"""
    base = (high - low).ewm(span=9).mean()
    return _rank_pct(base, 126)

def mass_013_range_ema_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_013_range_ema_lvl_252d"""
    base = (high - low).ewm(span=9).mean()
    return _rolling_mean(base, 252)

def mass_014_range_ema_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_014_range_ema_zscore_252d"""
    base = (high - low).ewm(span=9).mean()
    return _zscore_rolling(base, 252)

def mass_015_range_ema_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_015_range_ema_rank_252d"""
    base = (high - low).ewm(span=9).mean()
    return _rank_pct(base, 252)

def mass_016_range_dema_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_016_range_dema_lvl_5d"""
    base = (high - low).ewm(span=9).mean().ewm(span=9).mean()
    return _rolling_mean(base, 5)

def mass_017_range_dema_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_017_range_dema_zscore_5d"""
    base = (high - low).ewm(span=9).mean().ewm(span=9).mean()
    return _zscore_rolling(base, 5)

def mass_018_range_dema_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_018_range_dema_rank_5d"""
    base = (high - low).ewm(span=9).mean().ewm(span=9).mean()
    return _rank_pct(base, 5)

def mass_019_range_dema_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_019_range_dema_lvl_21d"""
    base = (high - low).ewm(span=9).mean().ewm(span=9).mean()
    return _rolling_mean(base, 21)

def mass_020_range_dema_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_020_range_dema_zscore_21d"""
    base = (high - low).ewm(span=9).mean().ewm(span=9).mean()
    return _zscore_rolling(base, 21)

def mass_021_range_dema_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_021_range_dema_rank_21d"""
    base = (high - low).ewm(span=9).mean().ewm(span=9).mean()
    return _rank_pct(base, 21)

def mass_022_range_dema_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_022_range_dema_lvl_63d"""
    base = (high - low).ewm(span=9).mean().ewm(span=9).mean()
    return _rolling_mean(base, 63)

def mass_023_range_dema_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_023_range_dema_zscore_63d"""
    base = (high - low).ewm(span=9).mean().ewm(span=9).mean()
    return _zscore_rolling(base, 63)

def mass_024_range_dema_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_024_range_dema_rank_63d"""
    base = (high - low).ewm(span=9).mean().ewm(span=9).mean()
    return _rank_pct(base, 63)

def mass_025_range_dema_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_025_range_dema_lvl_126d"""
    base = (high - low).ewm(span=9).mean().ewm(span=9).mean()
    return _rolling_mean(base, 126)

def mass_026_range_dema_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_026_range_dema_zscore_126d"""
    base = (high - low).ewm(span=9).mean().ewm(span=9).mean()
    return _zscore_rolling(base, 126)

def mass_027_range_dema_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_027_range_dema_rank_126d"""
    base = (high - low).ewm(span=9).mean().ewm(span=9).mean()
    return _rank_pct(base, 126)

def mass_028_range_dema_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_028_range_dema_lvl_252d"""
    base = (high - low).ewm(span=9).mean().ewm(span=9).mean()
    return _rolling_mean(base, 252)

def mass_029_range_dema_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_029_range_dema_zscore_252d"""
    base = (high - low).ewm(span=9).mean().ewm(span=9).mean()
    return _zscore_rolling(base, 252)

def mass_030_range_dema_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_030_range_dema_rank_252d"""
    base = (high - low).ewm(span=9).mean().ewm(span=9).mean()
    return _rank_pct(base, 252)

def mass_031_mass_idx_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_031_mass_idx_lvl_5d"""
    base = _safe_div((high - low).ewm(span=9).mean(), (high - low).ewm(span=9).mean().ewm(span=9).mean())
    return _rolling_mean(base, 5)

def mass_032_mass_idx_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_032_mass_idx_zscore_5d"""
    base = _safe_div((high - low).ewm(span=9).mean(), (high - low).ewm(span=9).mean().ewm(span=9).mean())
    return _zscore_rolling(base, 5)

def mass_033_mass_idx_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_033_mass_idx_rank_5d"""
    base = _safe_div((high - low).ewm(span=9).mean(), (high - low).ewm(span=9).mean().ewm(span=9).mean())
    return _rank_pct(base, 5)

def mass_034_mass_idx_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_034_mass_idx_lvl_21d"""
    base = _safe_div((high - low).ewm(span=9).mean(), (high - low).ewm(span=9).mean().ewm(span=9).mean())
    return _rolling_mean(base, 21)

def mass_035_mass_idx_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_035_mass_idx_zscore_21d"""
    base = _safe_div((high - low).ewm(span=9).mean(), (high - low).ewm(span=9).mean().ewm(span=9).mean())
    return _zscore_rolling(base, 21)

def mass_036_mass_idx_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_036_mass_idx_rank_21d"""
    base = _safe_div((high - low).ewm(span=9).mean(), (high - low).ewm(span=9).mean().ewm(span=9).mean())
    return _rank_pct(base, 21)

def mass_037_mass_idx_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_037_mass_idx_lvl_63d"""
    base = _safe_div((high - low).ewm(span=9).mean(), (high - low).ewm(span=9).mean().ewm(span=9).mean())
    return _rolling_mean(base, 63)

def mass_038_mass_idx_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_038_mass_idx_zscore_63d"""
    base = _safe_div((high - low).ewm(span=9).mean(), (high - low).ewm(span=9).mean().ewm(span=9).mean())
    return _zscore_rolling(base, 63)

def mass_039_mass_idx_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_039_mass_idx_rank_63d"""
    base = _safe_div((high - low).ewm(span=9).mean(), (high - low).ewm(span=9).mean().ewm(span=9).mean())
    return _rank_pct(base, 63)

def mass_040_mass_idx_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_040_mass_idx_lvl_126d"""
    base = _safe_div((high - low).ewm(span=9).mean(), (high - low).ewm(span=9).mean().ewm(span=9).mean())
    return _rolling_mean(base, 126)

def mass_041_mass_idx_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_041_mass_idx_zscore_126d"""
    base = _safe_div((high - low).ewm(span=9).mean(), (high - low).ewm(span=9).mean().ewm(span=9).mean())
    return _zscore_rolling(base, 126)

def mass_042_mass_idx_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_042_mass_idx_rank_126d"""
    base = _safe_div((high - low).ewm(span=9).mean(), (high - low).ewm(span=9).mean().ewm(span=9).mean())
    return _rank_pct(base, 126)

def mass_043_mass_idx_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_043_mass_idx_lvl_252d"""
    base = _safe_div((high - low).ewm(span=9).mean(), (high - low).ewm(span=9).mean().ewm(span=9).mean())
    return _rolling_mean(base, 252)

def mass_044_mass_idx_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_044_mass_idx_zscore_252d"""
    base = _safe_div((high - low).ewm(span=9).mean(), (high - low).ewm(span=9).mean().ewm(span=9).mean())
    return _zscore_rolling(base, 252)

def mass_045_mass_idx_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_045_mass_idx_rank_252d"""
    base = _safe_div((high - low).ewm(span=9).mean(), (high - low).ewm(span=9).mean().ewm(span=9).mean())
    return _rank_pct(base, 252)

def mass_046_range_std_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_046_range_std_lvl_5d"""
    base = _rolling_std(high - low, 9)
    return _rolling_mean(base, 5)

def mass_047_range_std_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_047_range_std_zscore_5d"""
    base = _rolling_std(high - low, 9)
    return _zscore_rolling(base, 5)

def mass_048_range_std_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_048_range_std_rank_5d"""
    base = _rolling_std(high - low, 9)
    return _rank_pct(base, 5)

def mass_049_range_std_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_049_range_std_lvl_21d"""
    base = _rolling_std(high - low, 9)
    return _rolling_mean(base, 21)

def mass_050_range_std_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_050_range_std_zscore_21d"""
    base = _rolling_std(high - low, 9)
    return _zscore_rolling(base, 21)

def mass_051_range_std_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_051_range_std_rank_21d"""
    base = _rolling_std(high - low, 9)
    return _rank_pct(base, 21)

def mass_052_range_std_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_052_range_std_lvl_63d"""
    base = _rolling_std(high - low, 9)
    return _rolling_mean(base, 63)

def mass_053_range_std_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_053_range_std_zscore_63d"""
    base = _rolling_std(high - low, 9)
    return _zscore_rolling(base, 63)

def mass_054_range_std_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_054_range_std_rank_63d"""
    base = _rolling_std(high - low, 9)
    return _rank_pct(base, 63)

def mass_055_range_std_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_055_range_std_lvl_126d"""
    base = _rolling_std(high - low, 9)
    return _rolling_mean(base, 126)

def mass_056_range_std_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_056_range_std_zscore_126d"""
    base = _rolling_std(high - low, 9)
    return _zscore_rolling(base, 126)

def mass_057_range_std_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_057_range_std_rank_126d"""
    base = _rolling_std(high - low, 9)
    return _rank_pct(base, 126)

def mass_058_range_std_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_058_range_std_lvl_252d"""
    base = _rolling_std(high - low, 9)
    return _rolling_mean(base, 252)

def mass_059_range_std_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_059_range_std_zscore_252d"""
    base = _rolling_std(high - low, 9)
    return _zscore_rolling(base, 252)

def mass_060_range_std_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_060_range_std_rank_252d"""
    base = _rolling_std(high - low, 9)
    return _rank_pct(base, 252)

def mass_061_range_lvl_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_061_range_lvl_lvl_5d"""
    base = high - low
    return _rolling_mean(base, 5)

def mass_062_range_lvl_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_062_range_lvl_zscore_5d"""
    base = high - low
    return _zscore_rolling(base, 5)

def mass_063_range_lvl_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_063_range_lvl_rank_5d"""
    base = high - low
    return _rank_pct(base, 5)

def mass_064_range_lvl_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_064_range_lvl_lvl_21d"""
    base = high - low
    return _rolling_mean(base, 21)

def mass_065_range_lvl_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_065_range_lvl_zscore_21d"""
    base = high - low
    return _zscore_rolling(base, 21)

def mass_066_range_lvl_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_066_range_lvl_rank_21d"""
    base = high - low
    return _rank_pct(base, 21)

def mass_067_range_lvl_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_067_range_lvl_lvl_63d"""
    base = high - low
    return _rolling_mean(base, 63)

def mass_068_range_lvl_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_068_range_lvl_zscore_63d"""
    base = high - low
    return _zscore_rolling(base, 63)

def mass_069_range_lvl_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_069_range_lvl_rank_63d"""
    base = high - low
    return _rank_pct(base, 63)

def mass_070_range_lvl_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_070_range_lvl_lvl_126d"""
    base = high - low
    return _rolling_mean(base, 126)

def mass_071_range_lvl_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_071_range_lvl_zscore_126d"""
    base = high - low
    return _zscore_rolling(base, 126)

def mass_072_range_lvl_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_072_range_lvl_rank_126d"""
    base = high - low
    return _rank_pct(base, 126)

def mass_073_range_lvl_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_073_range_lvl_lvl_252d"""
    base = high - low
    return _rolling_mean(base, 252)

def mass_074_range_lvl_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_074_range_lvl_zscore_252d"""
    base = high - low
    return _zscore_rolling(base, 252)

def mass_075_range_lvl_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mass_075_range_lvl_rank_252d"""
    base = high - low
    return _rank_pct(base, 252)

# ── Registry ──────────────────────────────────────────────────────────────────
V89_REGISTRY = {
    "mass_001_range_ema_lvl_5d": {"inputs": ["high", "low", "close", "volume"], "func": mass_001_range_ema_lvl_5d},
    "mass_002_range_ema_zscore_5d": {"inputs": ["high", "low", "close", "volume"], "func": mass_002_range_ema_zscore_5d},
    "mass_003_range_ema_rank_5d": {"inputs": ["high", "low", "close", "volume"], "func": mass_003_range_ema_rank_5d},
    "mass_004_range_ema_lvl_21d": {"inputs": ["high", "low", "close", "volume"], "func": mass_004_range_ema_lvl_21d},
    "mass_005_range_ema_zscore_21d": {"inputs": ["high", "low", "close", "volume"], "func": mass_005_range_ema_zscore_21d},
    "mass_006_range_ema_rank_21d": {"inputs": ["high", "low", "close", "volume"], "func": mass_006_range_ema_rank_21d},
    "mass_007_range_ema_lvl_63d": {"inputs": ["high", "low", "close", "volume"], "func": mass_007_range_ema_lvl_63d},
    "mass_008_range_ema_zscore_63d": {"inputs": ["high", "low", "close", "volume"], "func": mass_008_range_ema_zscore_63d},
    "mass_009_range_ema_rank_63d": {"inputs": ["high", "low", "close", "volume"], "func": mass_009_range_ema_rank_63d},
    "mass_010_range_ema_lvl_126d": {"inputs": ["high", "low", "close", "volume"], "func": mass_010_range_ema_lvl_126d},
    "mass_011_range_ema_zscore_126d": {"inputs": ["high", "low", "close", "volume"], "func": mass_011_range_ema_zscore_126d},
    "mass_012_range_ema_rank_126d": {"inputs": ["high", "low", "close", "volume"], "func": mass_012_range_ema_rank_126d},
    "mass_013_range_ema_lvl_252d": {"inputs": ["high", "low", "close", "volume"], "func": mass_013_range_ema_lvl_252d},
    "mass_014_range_ema_zscore_252d": {"inputs": ["high", "low", "close", "volume"], "func": mass_014_range_ema_zscore_252d},
    "mass_015_range_ema_rank_252d": {"inputs": ["high", "low", "close", "volume"], "func": mass_015_range_ema_rank_252d},
    "mass_016_range_dema_lvl_5d": {"inputs": ["high", "low", "close", "volume"], "func": mass_016_range_dema_lvl_5d},
    "mass_017_range_dema_zscore_5d": {"inputs": ["high", "low", "close", "volume"], "func": mass_017_range_dema_zscore_5d},
    "mass_018_range_dema_rank_5d": {"inputs": ["high", "low", "close", "volume"], "func": mass_018_range_dema_rank_5d},
    "mass_019_range_dema_lvl_21d": {"inputs": ["high", "low", "close", "volume"], "func": mass_019_range_dema_lvl_21d},
    "mass_020_range_dema_zscore_21d": {"inputs": ["high", "low", "close", "volume"], "func": mass_020_range_dema_zscore_21d},
    "mass_021_range_dema_rank_21d": {"inputs": ["high", "low", "close", "volume"], "func": mass_021_range_dema_rank_21d},
    "mass_022_range_dema_lvl_63d": {"inputs": ["high", "low", "close", "volume"], "func": mass_022_range_dema_lvl_63d},
    "mass_023_range_dema_zscore_63d": {"inputs": ["high", "low", "close", "volume"], "func": mass_023_range_dema_zscore_63d},
    "mass_024_range_dema_rank_63d": {"inputs": ["high", "low", "close", "volume"], "func": mass_024_range_dema_rank_63d},
    "mass_025_range_dema_lvl_126d": {"inputs": ["high", "low", "close", "volume"], "func": mass_025_range_dema_lvl_126d},
    "mass_026_range_dema_zscore_126d": {"inputs": ["high", "low", "close", "volume"], "func": mass_026_range_dema_zscore_126d},
    "mass_027_range_dema_rank_126d": {"inputs": ["high", "low", "close", "volume"], "func": mass_027_range_dema_rank_126d},
    "mass_028_range_dema_lvl_252d": {"inputs": ["high", "low", "close", "volume"], "func": mass_028_range_dema_lvl_252d},
    "mass_029_range_dema_zscore_252d": {"inputs": ["high", "low", "close", "volume"], "func": mass_029_range_dema_zscore_252d},
    "mass_030_range_dema_rank_252d": {"inputs": ["high", "low", "close", "volume"], "func": mass_030_range_dema_rank_252d},
    "mass_031_mass_idx_lvl_5d": {"inputs": ["high", "low", "close", "volume"], "func": mass_031_mass_idx_lvl_5d},
    "mass_032_mass_idx_zscore_5d": {"inputs": ["high", "low", "close", "volume"], "func": mass_032_mass_idx_zscore_5d},
    "mass_033_mass_idx_rank_5d": {"inputs": ["high", "low", "close", "volume"], "func": mass_033_mass_idx_rank_5d},
    "mass_034_mass_idx_lvl_21d": {"inputs": ["high", "low", "close", "volume"], "func": mass_034_mass_idx_lvl_21d},
    "mass_035_mass_idx_zscore_21d": {"inputs": ["high", "low", "close", "volume"], "func": mass_035_mass_idx_zscore_21d},
    "mass_036_mass_idx_rank_21d": {"inputs": ["high", "low", "close", "volume"], "func": mass_036_mass_idx_rank_21d},
    "mass_037_mass_idx_lvl_63d": {"inputs": ["high", "low", "close", "volume"], "func": mass_037_mass_idx_lvl_63d},
    "mass_038_mass_idx_zscore_63d": {"inputs": ["high", "low", "close", "volume"], "func": mass_038_mass_idx_zscore_63d},
    "mass_039_mass_idx_rank_63d": {"inputs": ["high", "low", "close", "volume"], "func": mass_039_mass_idx_rank_63d},
    "mass_040_mass_idx_lvl_126d": {"inputs": ["high", "low", "close", "volume"], "func": mass_040_mass_idx_lvl_126d},
    "mass_041_mass_idx_zscore_126d": {"inputs": ["high", "low", "close", "volume"], "func": mass_041_mass_idx_zscore_126d},
    "mass_042_mass_idx_rank_126d": {"inputs": ["high", "low", "close", "volume"], "func": mass_042_mass_idx_rank_126d},
    "mass_043_mass_idx_lvl_252d": {"inputs": ["high", "low", "close", "volume"], "func": mass_043_mass_idx_lvl_252d},
    "mass_044_mass_idx_zscore_252d": {"inputs": ["high", "low", "close", "volume"], "func": mass_044_mass_idx_zscore_252d},
    "mass_045_mass_idx_rank_252d": {"inputs": ["high", "low", "close", "volume"], "func": mass_045_mass_idx_rank_252d},
    "mass_046_range_std_lvl_5d": {"inputs": ["high", "low", "close", "volume"], "func": mass_046_range_std_lvl_5d},
    "mass_047_range_std_zscore_5d": {"inputs": ["high", "low", "close", "volume"], "func": mass_047_range_std_zscore_5d},
    "mass_048_range_std_rank_5d": {"inputs": ["high", "low", "close", "volume"], "func": mass_048_range_std_rank_5d},
    "mass_049_range_std_lvl_21d": {"inputs": ["high", "low", "close", "volume"], "func": mass_049_range_std_lvl_21d},
    "mass_050_range_std_zscore_21d": {"inputs": ["high", "low", "close", "volume"], "func": mass_050_range_std_zscore_21d},
    "mass_051_range_std_rank_21d": {"inputs": ["high", "low", "close", "volume"], "func": mass_051_range_std_rank_21d},
    "mass_052_range_std_lvl_63d": {"inputs": ["high", "low", "close", "volume"], "func": mass_052_range_std_lvl_63d},
    "mass_053_range_std_zscore_63d": {"inputs": ["high", "low", "close", "volume"], "func": mass_053_range_std_zscore_63d},
    "mass_054_range_std_rank_63d": {"inputs": ["high", "low", "close", "volume"], "func": mass_054_range_std_rank_63d},
    "mass_055_range_std_lvl_126d": {"inputs": ["high", "low", "close", "volume"], "func": mass_055_range_std_lvl_126d},
    "mass_056_range_std_zscore_126d": {"inputs": ["high", "low", "close", "volume"], "func": mass_056_range_std_zscore_126d},
    "mass_057_range_std_rank_126d": {"inputs": ["high", "low", "close", "volume"], "func": mass_057_range_std_rank_126d},
    "mass_058_range_std_lvl_252d": {"inputs": ["high", "low", "close", "volume"], "func": mass_058_range_std_lvl_252d},
    "mass_059_range_std_zscore_252d": {"inputs": ["high", "low", "close", "volume"], "func": mass_059_range_std_zscore_252d},
    "mass_060_range_std_rank_252d": {"inputs": ["high", "low", "close", "volume"], "func": mass_060_range_std_rank_252d},
    "mass_061_range_lvl_lvl_5d": {"inputs": ["high", "low", "close", "volume"], "func": mass_061_range_lvl_lvl_5d},
    "mass_062_range_lvl_zscore_5d": {"inputs": ["high", "low", "close", "volume"], "func": mass_062_range_lvl_zscore_5d},
    "mass_063_range_lvl_rank_5d": {"inputs": ["high", "low", "close", "volume"], "func": mass_063_range_lvl_rank_5d},
    "mass_064_range_lvl_lvl_21d": {"inputs": ["high", "low", "close", "volume"], "func": mass_064_range_lvl_lvl_21d},
    "mass_065_range_lvl_zscore_21d": {"inputs": ["high", "low", "close", "volume"], "func": mass_065_range_lvl_zscore_21d},
    "mass_066_range_lvl_rank_21d": {"inputs": ["high", "low", "close", "volume"], "func": mass_066_range_lvl_rank_21d},
    "mass_067_range_lvl_lvl_63d": {"inputs": ["high", "low", "close", "volume"], "func": mass_067_range_lvl_lvl_63d},
    "mass_068_range_lvl_zscore_63d": {"inputs": ["high", "low", "close", "volume"], "func": mass_068_range_lvl_zscore_63d},
    "mass_069_range_lvl_rank_63d": {"inputs": ["high", "low", "close", "volume"], "func": mass_069_range_lvl_rank_63d},
    "mass_070_range_lvl_lvl_126d": {"inputs": ["high", "low", "close", "volume"], "func": mass_070_range_lvl_lvl_126d},
    "mass_071_range_lvl_zscore_126d": {"inputs": ["high", "low", "close", "volume"], "func": mass_071_range_lvl_zscore_126d},
    "mass_072_range_lvl_rank_126d": {"inputs": ["high", "low", "close", "volume"], "func": mass_072_range_lvl_rank_126d},
    "mass_073_range_lvl_lvl_252d": {"inputs": ["high", "low", "close", "volume"], "func": mass_073_range_lvl_lvl_252d},
    "mass_074_range_lvl_zscore_252d": {"inputs": ["high", "low", "close", "volume"], "func": mass_074_range_lvl_zscore_252d},
    "mass_075_range_lvl_rank_252d": {"inputs": ["high", "low", "close", "volume"], "func": mass_075_range_lvl_rank_252d},
}
