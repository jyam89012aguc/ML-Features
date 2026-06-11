"""
85_frcd_dynamics — Base Features 001-075
Domain: frcd_dynamics
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
    return s.rolling(w, min_periods=max(1, w // 2)).mean()

def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).std().fillna(0)

def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).max()

def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).min()

def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).sum()

def _ewm_mean(s: pd.Series, w: int) -> pd.Series:
    return s.ewm(span=w, min_periods=max(1, w // 2)).mean()

def _zscore_rolling(s: pd.Series, w: int) -> pd.Series:
    m = _rolling_mean(s, w)
    sd = _rolling_std(s, w)
    return _safe_div((s - m), sd)

def _rank_pct(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).rank(pct=True)

def _rsi(s: pd.Series, w: int) -> pd.Series:
    delta = s.diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=w).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=w).mean()
    rs = _safe_div(gain, loss)
    return 100 - (100 / (1 + rs))

# ── Feature functions ────────────────────────────────────────────────────────

def frcd_001_fi_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_001_fi_lvl_5d"""
    base = (close - close.shift(1)) * volume
    return _rolling_mean(base, 5)

def frcd_002_fi_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_002_fi_zscore_5d"""
    base = (close - close.shift(1)) * volume
    return _zscore_rolling(base, 5)

def frcd_003_fi_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_003_fi_rank_5d"""
    base = (close - close.shift(1)) * volume
    return _rank_pct(base, 5)

def frcd_004_fi_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_004_fi_lvl_21d"""
    base = (close - close.shift(1)) * volume
    return _rolling_mean(base, 21)

def frcd_005_fi_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_005_fi_zscore_21d"""
    base = (close - close.shift(1)) * volume
    return _zscore_rolling(base, 21)

def frcd_006_fi_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_006_fi_rank_21d"""
    base = (close - close.shift(1)) * volume
    return _rank_pct(base, 21)

def frcd_007_fi_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_007_fi_lvl_63d"""
    base = (close - close.shift(1)) * volume
    return _rolling_mean(base, 63)

def frcd_008_fi_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_008_fi_zscore_63d"""
    base = (close - close.shift(1)) * volume
    return _zscore_rolling(base, 63)

def frcd_009_fi_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_009_fi_rank_63d"""
    base = (close - close.shift(1)) * volume
    return _rank_pct(base, 63)

def frcd_010_fi_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_010_fi_lvl_126d"""
    base = (close - close.shift(1)) * volume
    return _rolling_mean(base, 126)

def frcd_011_fi_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_011_fi_zscore_126d"""
    base = (close - close.shift(1)) * volume
    return _zscore_rolling(base, 126)

def frcd_012_fi_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_012_fi_rank_126d"""
    base = (close - close.shift(1)) * volume
    return _rank_pct(base, 126)

def frcd_013_fi_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_013_fi_lvl_252d"""
    base = (close - close.shift(1)) * volume
    return _rolling_mean(base, 252)

def frcd_014_fi_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_014_fi_zscore_252d"""
    base = (close - close.shift(1)) * volume
    return _zscore_rolling(base, 252)

def frcd_015_fi_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_015_fi_rank_252d"""
    base = (close - close.shift(1)) * volume
    return _rank_pct(base, 252)

def frcd_016_fi_ema13_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_016_fi_ema13_lvl_5d"""
    base = _ewm_mean((close - close.shift(1)) * volume, 13)
    return _rolling_mean(base, 5)

def frcd_017_fi_ema13_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_017_fi_ema13_zscore_5d"""
    base = _ewm_mean((close - close.shift(1)) * volume, 13)
    return _zscore_rolling(base, 5)

def frcd_018_fi_ema13_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_018_fi_ema13_rank_5d"""
    base = _ewm_mean((close - close.shift(1)) * volume, 13)
    return _rank_pct(base, 5)

def frcd_019_fi_ema13_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_019_fi_ema13_lvl_21d"""
    base = _ewm_mean((close - close.shift(1)) * volume, 13)
    return _rolling_mean(base, 21)

def frcd_020_fi_ema13_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_020_fi_ema13_zscore_21d"""
    base = _ewm_mean((close - close.shift(1)) * volume, 13)
    return _zscore_rolling(base, 21)

def frcd_021_fi_ema13_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_021_fi_ema13_rank_21d"""
    base = _ewm_mean((close - close.shift(1)) * volume, 13)
    return _rank_pct(base, 21)

def frcd_022_fi_ema13_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_022_fi_ema13_lvl_63d"""
    base = _ewm_mean((close - close.shift(1)) * volume, 13)
    return _rolling_mean(base, 63)

def frcd_023_fi_ema13_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_023_fi_ema13_zscore_63d"""
    base = _ewm_mean((close - close.shift(1)) * volume, 13)
    return _zscore_rolling(base, 63)

def frcd_024_fi_ema13_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_024_fi_ema13_rank_63d"""
    base = _ewm_mean((close - close.shift(1)) * volume, 13)
    return _rank_pct(base, 63)

def frcd_025_fi_ema13_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_025_fi_ema13_lvl_126d"""
    base = _ewm_mean((close - close.shift(1)) * volume, 13)
    return _rolling_mean(base, 126)

def frcd_026_fi_ema13_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_026_fi_ema13_zscore_126d"""
    base = _ewm_mean((close - close.shift(1)) * volume, 13)
    return _zscore_rolling(base, 126)

def frcd_027_fi_ema13_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_027_fi_ema13_rank_126d"""
    base = _ewm_mean((close - close.shift(1)) * volume, 13)
    return _rank_pct(base, 126)

def frcd_028_fi_ema13_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_028_fi_ema13_lvl_252d"""
    base = _ewm_mean((close - close.shift(1)) * volume, 13)
    return _rolling_mean(base, 252)

def frcd_029_fi_ema13_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_029_fi_ema13_zscore_252d"""
    base = _ewm_mean((close - close.shift(1)) * volume, 13)
    return _zscore_rolling(base, 252)

def frcd_030_fi_ema13_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_030_fi_ema13_rank_252d"""
    base = _ewm_mean((close - close.shift(1)) * volume, 13)
    return _rank_pct(base, 252)

def frcd_031_fi_ema50_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_031_fi_ema50_lvl_5d"""
    base = _ewm_mean((close - close.shift(1)) * volume, 50)
    return _rolling_mean(base, 5)

def frcd_032_fi_ema50_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_032_fi_ema50_zscore_5d"""
    base = _ewm_mean((close - close.shift(1)) * volume, 50)
    return _zscore_rolling(base, 5)

def frcd_033_fi_ema50_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_033_fi_ema50_rank_5d"""
    base = _ewm_mean((close - close.shift(1)) * volume, 50)
    return _rank_pct(base, 5)

def frcd_034_fi_ema50_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_034_fi_ema50_lvl_21d"""
    base = _ewm_mean((close - close.shift(1)) * volume, 50)
    return _rolling_mean(base, 21)

def frcd_035_fi_ema50_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_035_fi_ema50_zscore_21d"""
    base = _ewm_mean((close - close.shift(1)) * volume, 50)
    return _zscore_rolling(base, 21)

def frcd_036_fi_ema50_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_036_fi_ema50_rank_21d"""
    base = _ewm_mean((close - close.shift(1)) * volume, 50)
    return _rank_pct(base, 21)

def frcd_037_fi_ema50_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_037_fi_ema50_lvl_63d"""
    base = _ewm_mean((close - close.shift(1)) * volume, 50)
    return _rolling_mean(base, 63)

def frcd_038_fi_ema50_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_038_fi_ema50_zscore_63d"""
    base = _ewm_mean((close - close.shift(1)) * volume, 50)
    return _zscore_rolling(base, 63)

def frcd_039_fi_ema50_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_039_fi_ema50_rank_63d"""
    base = _ewm_mean((close - close.shift(1)) * volume, 50)
    return _rank_pct(base, 63)

def frcd_040_fi_ema50_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_040_fi_ema50_lvl_126d"""
    base = _ewm_mean((close - close.shift(1)) * volume, 50)
    return _rolling_mean(base, 126)

def frcd_041_fi_ema50_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_041_fi_ema50_zscore_126d"""
    base = _ewm_mean((close - close.shift(1)) * volume, 50)
    return _zscore_rolling(base, 126)

def frcd_042_fi_ema50_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_042_fi_ema50_rank_126d"""
    base = _ewm_mean((close - close.shift(1)) * volume, 50)
    return _rank_pct(base, 126)

def frcd_043_fi_ema50_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_043_fi_ema50_lvl_252d"""
    base = _ewm_mean((close - close.shift(1)) * volume, 50)
    return _rolling_mean(base, 252)

def frcd_044_fi_ema50_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_044_fi_ema50_zscore_252d"""
    base = _ewm_mean((close - close.shift(1)) * volume, 50)
    return _zscore_rolling(base, 252)

def frcd_045_fi_ema50_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_045_fi_ema50_rank_252d"""
    base = _ewm_mean((close - close.shift(1)) * volume, 50)
    return _rank_pct(base, 252)

def frcd_046_fi_z_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_046_fi_z_lvl_5d"""
    base = _zscore_rolling(_ewm_mean((close - close.shift(1)) * volume, 13), 63)
    return _rolling_mean(base, 5)

def frcd_047_fi_z_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_047_fi_z_zscore_5d"""
    base = _zscore_rolling(_ewm_mean((close - close.shift(1)) * volume, 13), 63)
    return _zscore_rolling(base, 5)

def frcd_048_fi_z_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_048_fi_z_rank_5d"""
    base = _zscore_rolling(_ewm_mean((close - close.shift(1)) * volume, 13), 63)
    return _rank_pct(base, 5)

def frcd_049_fi_z_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_049_fi_z_lvl_21d"""
    base = _zscore_rolling(_ewm_mean((close - close.shift(1)) * volume, 13), 63)
    return _rolling_mean(base, 21)

def frcd_050_fi_z_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_050_fi_z_zscore_21d"""
    base = _zscore_rolling(_ewm_mean((close - close.shift(1)) * volume, 13), 63)
    return _zscore_rolling(base, 21)

def frcd_051_fi_z_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_051_fi_z_rank_21d"""
    base = _zscore_rolling(_ewm_mean((close - close.shift(1)) * volume, 13), 63)
    return _rank_pct(base, 21)

def frcd_052_fi_z_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_052_fi_z_lvl_63d"""
    base = _zscore_rolling(_ewm_mean((close - close.shift(1)) * volume, 13), 63)
    return _rolling_mean(base, 63)

def frcd_053_fi_z_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_053_fi_z_zscore_63d"""
    base = _zscore_rolling(_ewm_mean((close - close.shift(1)) * volume, 13), 63)
    return _zscore_rolling(base, 63)

def frcd_054_fi_z_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_054_fi_z_rank_63d"""
    base = _zscore_rolling(_ewm_mean((close - close.shift(1)) * volume, 13), 63)
    return _rank_pct(base, 63)

def frcd_055_fi_z_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_055_fi_z_lvl_126d"""
    base = _zscore_rolling(_ewm_mean((close - close.shift(1)) * volume, 13), 63)
    return _rolling_mean(base, 126)

def frcd_056_fi_z_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_056_fi_z_zscore_126d"""
    base = _zscore_rolling(_ewm_mean((close - close.shift(1)) * volume, 13), 63)
    return _zscore_rolling(base, 126)

def frcd_057_fi_z_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_057_fi_z_rank_126d"""
    base = _zscore_rolling(_ewm_mean((close - close.shift(1)) * volume, 13), 63)
    return _rank_pct(base, 126)

def frcd_058_fi_z_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_058_fi_z_lvl_252d"""
    base = _zscore_rolling(_ewm_mean((close - close.shift(1)) * volume, 13), 63)
    return _rolling_mean(base, 252)

def frcd_059_fi_z_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_059_fi_z_zscore_252d"""
    base = _zscore_rolling(_ewm_mean((close - close.shift(1)) * volume, 13), 63)
    return _zscore_rolling(base, 252)

def frcd_060_fi_z_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_060_fi_z_rank_252d"""
    base = _zscore_rolling(_ewm_mean((close - close.shift(1)) * volume, 13), 63)
    return _rank_pct(base, 252)

def frcd_061_fi_slope_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_061_fi_slope_lvl_5d"""
    base = (_ewm_mean((close - close.shift(1)) * volume, 13)).diff(5)
    return _rolling_mean(base, 5)

def frcd_062_fi_slope_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_062_fi_slope_zscore_5d"""
    base = (_ewm_mean((close - close.shift(1)) * volume, 13)).diff(5)
    return _zscore_rolling(base, 5)

def frcd_063_fi_slope_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_063_fi_slope_rank_5d"""
    base = (_ewm_mean((close - close.shift(1)) * volume, 13)).diff(5)
    return _rank_pct(base, 5)

def frcd_064_fi_slope_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_064_fi_slope_lvl_21d"""
    base = (_ewm_mean((close - close.shift(1)) * volume, 13)).diff(5)
    return _rolling_mean(base, 21)

def frcd_065_fi_slope_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_065_fi_slope_zscore_21d"""
    base = (_ewm_mean((close - close.shift(1)) * volume, 13)).diff(5)
    return _zscore_rolling(base, 21)

def frcd_066_fi_slope_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_066_fi_slope_rank_21d"""
    base = (_ewm_mean((close - close.shift(1)) * volume, 13)).diff(5)
    return _rank_pct(base, 21)

def frcd_067_fi_slope_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_067_fi_slope_lvl_63d"""
    base = (_ewm_mean((close - close.shift(1)) * volume, 13)).diff(5)
    return _rolling_mean(base, 63)

def frcd_068_fi_slope_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_068_fi_slope_zscore_63d"""
    base = (_ewm_mean((close - close.shift(1)) * volume, 13)).diff(5)
    return _zscore_rolling(base, 63)

def frcd_069_fi_slope_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_069_fi_slope_rank_63d"""
    base = (_ewm_mean((close - close.shift(1)) * volume, 13)).diff(5)
    return _rank_pct(base, 63)

def frcd_070_fi_slope_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_070_fi_slope_lvl_126d"""
    base = (_ewm_mean((close - close.shift(1)) * volume, 13)).diff(5)
    return _rolling_mean(base, 126)

def frcd_071_fi_slope_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_071_fi_slope_zscore_126d"""
    base = (_ewm_mean((close - close.shift(1)) * volume, 13)).diff(5)
    return _zscore_rolling(base, 126)

def frcd_072_fi_slope_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_072_fi_slope_rank_126d"""
    base = (_ewm_mean((close - close.shift(1)) * volume, 13)).diff(5)
    return _rank_pct(base, 126)

def frcd_073_fi_slope_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_073_fi_slope_lvl_252d"""
    base = (_ewm_mean((close - close.shift(1)) * volume, 13)).diff(5)
    return _rolling_mean(base, 252)

def frcd_074_fi_slope_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_074_fi_slope_zscore_252d"""
    base = (_ewm_mean((close - close.shift(1)) * volume, 13)).diff(5)
    return _zscore_rolling(base, 252)

def frcd_075_fi_slope_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """frcd_075_fi_slope_rank_252d"""
    base = (_ewm_mean((close - close.shift(1)) * volume, 13)).diff(5)
    return _rank_pct(base, 252)

# ── Registry ──────────────────────────────────────────────────────────────────
V85_REGISTRY = {
    "frcd_001_fi_lvl_5d": {"inputs": ["close", "volume"], "func": frcd_001_fi_lvl_5d},
    "frcd_002_fi_zscore_5d": {"inputs": ["close", "volume"], "func": frcd_002_fi_zscore_5d},
    "frcd_003_fi_rank_5d": {"inputs": ["close", "volume"], "func": frcd_003_fi_rank_5d},
    "frcd_004_fi_lvl_21d": {"inputs": ["close", "volume"], "func": frcd_004_fi_lvl_21d},
    "frcd_005_fi_zscore_21d": {"inputs": ["close", "volume"], "func": frcd_005_fi_zscore_21d},
    "frcd_006_fi_rank_21d": {"inputs": ["close", "volume"], "func": frcd_006_fi_rank_21d},
    "frcd_007_fi_lvl_63d": {"inputs": ["close", "volume"], "func": frcd_007_fi_lvl_63d},
    "frcd_008_fi_zscore_63d": {"inputs": ["close", "volume"], "func": frcd_008_fi_zscore_63d},
    "frcd_009_fi_rank_63d": {"inputs": ["close", "volume"], "func": frcd_009_fi_rank_63d},
    "frcd_010_fi_lvl_126d": {"inputs": ["close", "volume"], "func": frcd_010_fi_lvl_126d},
    "frcd_011_fi_zscore_126d": {"inputs": ["close", "volume"], "func": frcd_011_fi_zscore_126d},
    "frcd_012_fi_rank_126d": {"inputs": ["close", "volume"], "func": frcd_012_fi_rank_126d},
    "frcd_013_fi_lvl_252d": {"inputs": ["close", "volume"], "func": frcd_013_fi_lvl_252d},
    "frcd_014_fi_zscore_252d": {"inputs": ["close", "volume"], "func": frcd_014_fi_zscore_252d},
    "frcd_015_fi_rank_252d": {"inputs": ["close", "volume"], "func": frcd_015_fi_rank_252d},
    "frcd_016_fi_ema13_lvl_5d": {"inputs": ["close", "volume"], "func": frcd_016_fi_ema13_lvl_5d},
    "frcd_017_fi_ema13_zscore_5d": {"inputs": ["close", "volume"], "func": frcd_017_fi_ema13_zscore_5d},
    "frcd_018_fi_ema13_rank_5d": {"inputs": ["close", "volume"], "func": frcd_018_fi_ema13_rank_5d},
    "frcd_019_fi_ema13_lvl_21d": {"inputs": ["close", "volume"], "func": frcd_019_fi_ema13_lvl_21d},
    "frcd_020_fi_ema13_zscore_21d": {"inputs": ["close", "volume"], "func": frcd_020_fi_ema13_zscore_21d},
    "frcd_021_fi_ema13_rank_21d": {"inputs": ["close", "volume"], "func": frcd_021_fi_ema13_rank_21d},
    "frcd_022_fi_ema13_lvl_63d": {"inputs": ["close", "volume"], "func": frcd_022_fi_ema13_lvl_63d},
    "frcd_023_fi_ema13_zscore_63d": {"inputs": ["close", "volume"], "func": frcd_023_fi_ema13_zscore_63d},
    "frcd_024_fi_ema13_rank_63d": {"inputs": ["close", "volume"], "func": frcd_024_fi_ema13_rank_63d},
    "frcd_025_fi_ema13_lvl_126d": {"inputs": ["close", "volume"], "func": frcd_025_fi_ema13_lvl_126d},
    "frcd_026_fi_ema13_zscore_126d": {"inputs": ["close", "volume"], "func": frcd_026_fi_ema13_zscore_126d},
    "frcd_027_fi_ema13_rank_126d": {"inputs": ["close", "volume"], "func": frcd_027_fi_ema13_rank_126d},
    "frcd_028_fi_ema13_lvl_252d": {"inputs": ["close", "volume"], "func": frcd_028_fi_ema13_lvl_252d},
    "frcd_029_fi_ema13_zscore_252d": {"inputs": ["close", "volume"], "func": frcd_029_fi_ema13_zscore_252d},
    "frcd_030_fi_ema13_rank_252d": {"inputs": ["close", "volume"], "func": frcd_030_fi_ema13_rank_252d},
    "frcd_031_fi_ema50_lvl_5d": {"inputs": ["close", "volume"], "func": frcd_031_fi_ema50_lvl_5d},
    "frcd_032_fi_ema50_zscore_5d": {"inputs": ["close", "volume"], "func": frcd_032_fi_ema50_zscore_5d},
    "frcd_033_fi_ema50_rank_5d": {"inputs": ["close", "volume"], "func": frcd_033_fi_ema50_rank_5d},
    "frcd_034_fi_ema50_lvl_21d": {"inputs": ["close", "volume"], "func": frcd_034_fi_ema50_lvl_21d},
    "frcd_035_fi_ema50_zscore_21d": {"inputs": ["close", "volume"], "func": frcd_035_fi_ema50_zscore_21d},
    "frcd_036_fi_ema50_rank_21d": {"inputs": ["close", "volume"], "func": frcd_036_fi_ema50_rank_21d},
    "frcd_037_fi_ema50_lvl_63d": {"inputs": ["close", "volume"], "func": frcd_037_fi_ema50_lvl_63d},
    "frcd_038_fi_ema50_zscore_63d": {"inputs": ["close", "volume"], "func": frcd_038_fi_ema50_zscore_63d},
    "frcd_039_fi_ema50_rank_63d": {"inputs": ["close", "volume"], "func": frcd_039_fi_ema50_rank_63d},
    "frcd_040_fi_ema50_lvl_126d": {"inputs": ["close", "volume"], "func": frcd_040_fi_ema50_lvl_126d},
    "frcd_041_fi_ema50_zscore_126d": {"inputs": ["close", "volume"], "func": frcd_041_fi_ema50_zscore_126d},
    "frcd_042_fi_ema50_rank_126d": {"inputs": ["close", "volume"], "func": frcd_042_fi_ema50_rank_126d},
    "frcd_043_fi_ema50_lvl_252d": {"inputs": ["close", "volume"], "func": frcd_043_fi_ema50_lvl_252d},
    "frcd_044_fi_ema50_zscore_252d": {"inputs": ["close", "volume"], "func": frcd_044_fi_ema50_zscore_252d},
    "frcd_045_fi_ema50_rank_252d": {"inputs": ["close", "volume"], "func": frcd_045_fi_ema50_rank_252d},
    "frcd_046_fi_z_lvl_5d": {"inputs": ["close", "volume"], "func": frcd_046_fi_z_lvl_5d},
    "frcd_047_fi_z_zscore_5d": {"inputs": ["close", "volume"], "func": frcd_047_fi_z_zscore_5d},
    "frcd_048_fi_z_rank_5d": {"inputs": ["close", "volume"], "func": frcd_048_fi_z_rank_5d},
    "frcd_049_fi_z_lvl_21d": {"inputs": ["close", "volume"], "func": frcd_049_fi_z_lvl_21d},
    "frcd_050_fi_z_zscore_21d": {"inputs": ["close", "volume"], "func": frcd_050_fi_z_zscore_21d},
    "frcd_051_fi_z_rank_21d": {"inputs": ["close", "volume"], "func": frcd_051_fi_z_rank_21d},
    "frcd_052_fi_z_lvl_63d": {"inputs": ["close", "volume"], "func": frcd_052_fi_z_lvl_63d},
    "frcd_053_fi_z_zscore_63d": {"inputs": ["close", "volume"], "func": frcd_053_fi_z_zscore_63d},
    "frcd_054_fi_z_rank_63d": {"inputs": ["close", "volume"], "func": frcd_054_fi_z_rank_63d},
    "frcd_055_fi_z_lvl_126d": {"inputs": ["close", "volume"], "func": frcd_055_fi_z_lvl_126d},
    "frcd_056_fi_z_zscore_126d": {"inputs": ["close", "volume"], "func": frcd_056_fi_z_zscore_126d},
    "frcd_057_fi_z_rank_126d": {"inputs": ["close", "volume"], "func": frcd_057_fi_z_rank_126d},
    "frcd_058_fi_z_lvl_252d": {"inputs": ["close", "volume"], "func": frcd_058_fi_z_lvl_252d},
    "frcd_059_fi_z_zscore_252d": {"inputs": ["close", "volume"], "func": frcd_059_fi_z_zscore_252d},
    "frcd_060_fi_z_rank_252d": {"inputs": ["close", "volume"], "func": frcd_060_fi_z_rank_252d},
    "frcd_061_fi_slope_lvl_5d": {"inputs": ["close", "volume"], "func": frcd_061_fi_slope_lvl_5d},
    "frcd_062_fi_slope_zscore_5d": {"inputs": ["close", "volume"], "func": frcd_062_fi_slope_zscore_5d},
    "frcd_063_fi_slope_rank_5d": {"inputs": ["close", "volume"], "func": frcd_063_fi_slope_rank_5d},
    "frcd_064_fi_slope_lvl_21d": {"inputs": ["close", "volume"], "func": frcd_064_fi_slope_lvl_21d},
    "frcd_065_fi_slope_zscore_21d": {"inputs": ["close", "volume"], "func": frcd_065_fi_slope_zscore_21d},
    "frcd_066_fi_slope_rank_21d": {"inputs": ["close", "volume"], "func": frcd_066_fi_slope_rank_21d},
    "frcd_067_fi_slope_lvl_63d": {"inputs": ["close", "volume"], "func": frcd_067_fi_slope_lvl_63d},
    "frcd_068_fi_slope_zscore_63d": {"inputs": ["close", "volume"], "func": frcd_068_fi_slope_zscore_63d},
    "frcd_069_fi_slope_rank_63d": {"inputs": ["close", "volume"], "func": frcd_069_fi_slope_rank_63d},
    "frcd_070_fi_slope_lvl_126d": {"inputs": ["close", "volume"], "func": frcd_070_fi_slope_lvl_126d},
    "frcd_071_fi_slope_zscore_126d": {"inputs": ["close", "volume"], "func": frcd_071_fi_slope_zscore_126d},
    "frcd_072_fi_slope_rank_126d": {"inputs": ["close", "volume"], "func": frcd_072_fi_slope_rank_126d},
    "frcd_073_fi_slope_lvl_252d": {"inputs": ["close", "volume"], "func": frcd_073_fi_slope_lvl_252d},
    "frcd_074_fi_slope_zscore_252d": {"inputs": ["close", "volume"], "func": frcd_074_fi_slope_zscore_252d},
    "frcd_075_fi_slope_rank_252d": {"inputs": ["close", "volume"], "func": frcd_075_fi_slope_rank_252d},
}
