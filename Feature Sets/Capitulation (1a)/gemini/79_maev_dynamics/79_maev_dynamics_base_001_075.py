"""
79_maev_dynamics — Base Features 001-075
Domain: maev_dynamics
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

def maev_001_sma20_rat_lvl_5d(close: pd.Series) -> pd.Series:
    """maev_001_sma20_rat_lvl_5d"""
    base = _safe_div(close, _rolling_mean(close, 20))
    return _rolling_mean(base, 5)

def maev_002_sma20_rat_zscore_5d(close: pd.Series) -> pd.Series:
    """maev_002_sma20_rat_zscore_5d"""
    base = _safe_div(close, _rolling_mean(close, 20))
    return _zscore_rolling(base, 5)

def maev_003_sma20_rat_rank_5d(close: pd.Series) -> pd.Series:
    """maev_003_sma20_rat_rank_5d"""
    base = _safe_div(close, _rolling_mean(close, 20))
    return _rank_pct(base, 5)

def maev_004_sma20_rat_lvl_21d(close: pd.Series) -> pd.Series:
    """maev_004_sma20_rat_lvl_21d"""
    base = _safe_div(close, _rolling_mean(close, 20))
    return _rolling_mean(base, 21)

def maev_005_sma20_rat_zscore_21d(close: pd.Series) -> pd.Series:
    """maev_005_sma20_rat_zscore_21d"""
    base = _safe_div(close, _rolling_mean(close, 20))
    return _zscore_rolling(base, 21)

def maev_006_sma20_rat_rank_21d(close: pd.Series) -> pd.Series:
    """maev_006_sma20_rat_rank_21d"""
    base = _safe_div(close, _rolling_mean(close, 20))
    return _rank_pct(base, 21)

def maev_007_sma20_rat_lvl_63d(close: pd.Series) -> pd.Series:
    """maev_007_sma20_rat_lvl_63d"""
    base = _safe_div(close, _rolling_mean(close, 20))
    return _rolling_mean(base, 63)

def maev_008_sma20_rat_zscore_63d(close: pd.Series) -> pd.Series:
    """maev_008_sma20_rat_zscore_63d"""
    base = _safe_div(close, _rolling_mean(close, 20))
    return _zscore_rolling(base, 63)

def maev_009_sma20_rat_rank_63d(close: pd.Series) -> pd.Series:
    """maev_009_sma20_rat_rank_63d"""
    base = _safe_div(close, _rolling_mean(close, 20))
    return _rank_pct(base, 63)

def maev_010_sma20_rat_lvl_126d(close: pd.Series) -> pd.Series:
    """maev_010_sma20_rat_lvl_126d"""
    base = _safe_div(close, _rolling_mean(close, 20))
    return _rolling_mean(base, 126)

def maev_011_sma20_rat_zscore_126d(close: pd.Series) -> pd.Series:
    """maev_011_sma20_rat_zscore_126d"""
    base = _safe_div(close, _rolling_mean(close, 20))
    return _zscore_rolling(base, 126)

def maev_012_sma20_rat_rank_126d(close: pd.Series) -> pd.Series:
    """maev_012_sma20_rat_rank_126d"""
    base = _safe_div(close, _rolling_mean(close, 20))
    return _rank_pct(base, 126)

def maev_013_sma20_rat_lvl_252d(close: pd.Series) -> pd.Series:
    """maev_013_sma20_rat_lvl_252d"""
    base = _safe_div(close, _rolling_mean(close, 20))
    return _rolling_mean(base, 252)

def maev_014_sma20_rat_zscore_252d(close: pd.Series) -> pd.Series:
    """maev_014_sma20_rat_zscore_252d"""
    base = _safe_div(close, _rolling_mean(close, 20))
    return _zscore_rolling(base, 252)

def maev_015_sma20_rat_rank_252d(close: pd.Series) -> pd.Series:
    """maev_015_sma20_rat_rank_252d"""
    base = _safe_div(close, _rolling_mean(close, 20))
    return _rank_pct(base, 252)

def maev_016_ema20_rat_lvl_5d(close: pd.Series) -> pd.Series:
    """maev_016_ema20_rat_lvl_5d"""
    base = _safe_div(close, _ewm_mean(close, 20))
    return _rolling_mean(base, 5)

def maev_017_ema20_rat_zscore_5d(close: pd.Series) -> pd.Series:
    """maev_017_ema20_rat_zscore_5d"""
    base = _safe_div(close, _ewm_mean(close, 20))
    return _zscore_rolling(base, 5)

def maev_018_ema20_rat_rank_5d(close: pd.Series) -> pd.Series:
    """maev_018_ema20_rat_rank_5d"""
    base = _safe_div(close, _ewm_mean(close, 20))
    return _rank_pct(base, 5)

def maev_019_ema20_rat_lvl_21d(close: pd.Series) -> pd.Series:
    """maev_019_ema20_rat_lvl_21d"""
    base = _safe_div(close, _ewm_mean(close, 20))
    return _rolling_mean(base, 21)

def maev_020_ema20_rat_zscore_21d(close: pd.Series) -> pd.Series:
    """maev_020_ema20_rat_zscore_21d"""
    base = _safe_div(close, _ewm_mean(close, 20))
    return _zscore_rolling(base, 21)

def maev_021_ema20_rat_rank_21d(close: pd.Series) -> pd.Series:
    """maev_021_ema20_rat_rank_21d"""
    base = _safe_div(close, _ewm_mean(close, 20))
    return _rank_pct(base, 21)

def maev_022_ema20_rat_lvl_63d(close: pd.Series) -> pd.Series:
    """maev_022_ema20_rat_lvl_63d"""
    base = _safe_div(close, _ewm_mean(close, 20))
    return _rolling_mean(base, 63)

def maev_023_ema20_rat_zscore_63d(close: pd.Series) -> pd.Series:
    """maev_023_ema20_rat_zscore_63d"""
    base = _safe_div(close, _ewm_mean(close, 20))
    return _zscore_rolling(base, 63)

def maev_024_ema20_rat_rank_63d(close: pd.Series) -> pd.Series:
    """maev_024_ema20_rat_rank_63d"""
    base = _safe_div(close, _ewm_mean(close, 20))
    return _rank_pct(base, 63)

def maev_025_ema20_rat_lvl_126d(close: pd.Series) -> pd.Series:
    """maev_025_ema20_rat_lvl_126d"""
    base = _safe_div(close, _ewm_mean(close, 20))
    return _rolling_mean(base, 126)

def maev_026_ema20_rat_zscore_126d(close: pd.Series) -> pd.Series:
    """maev_026_ema20_rat_zscore_126d"""
    base = _safe_div(close, _ewm_mean(close, 20))
    return _zscore_rolling(base, 126)

def maev_027_ema20_rat_rank_126d(close: pd.Series) -> pd.Series:
    """maev_027_ema20_rat_rank_126d"""
    base = _safe_div(close, _ewm_mean(close, 20))
    return _rank_pct(base, 126)

def maev_028_ema20_rat_lvl_252d(close: pd.Series) -> pd.Series:
    """maev_028_ema20_rat_lvl_252d"""
    base = _safe_div(close, _ewm_mean(close, 20))
    return _rolling_mean(base, 252)

def maev_029_ema20_rat_zscore_252d(close: pd.Series) -> pd.Series:
    """maev_029_ema20_rat_zscore_252d"""
    base = _safe_div(close, _ewm_mean(close, 20))
    return _zscore_rolling(base, 252)

def maev_030_ema20_rat_rank_252d(close: pd.Series) -> pd.Series:
    """maev_030_ema20_rat_rank_252d"""
    base = _safe_div(close, _ewm_mean(close, 20))
    return _rank_pct(base, 252)

def maev_031_sma50_rat_lvl_5d(close: pd.Series) -> pd.Series:
    """maev_031_sma50_rat_lvl_5d"""
    base = _safe_div(close, _rolling_mean(close, 50))
    return _rolling_mean(base, 5)

def maev_032_sma50_rat_zscore_5d(close: pd.Series) -> pd.Series:
    """maev_032_sma50_rat_zscore_5d"""
    base = _safe_div(close, _rolling_mean(close, 50))
    return _zscore_rolling(base, 5)

def maev_033_sma50_rat_rank_5d(close: pd.Series) -> pd.Series:
    """maev_033_sma50_rat_rank_5d"""
    base = _safe_div(close, _rolling_mean(close, 50))
    return _rank_pct(base, 5)

def maev_034_sma50_rat_lvl_21d(close: pd.Series) -> pd.Series:
    """maev_034_sma50_rat_lvl_21d"""
    base = _safe_div(close, _rolling_mean(close, 50))
    return _rolling_mean(base, 21)

def maev_035_sma50_rat_zscore_21d(close: pd.Series) -> pd.Series:
    """maev_035_sma50_rat_zscore_21d"""
    base = _safe_div(close, _rolling_mean(close, 50))
    return _zscore_rolling(base, 21)

def maev_036_sma50_rat_rank_21d(close: pd.Series) -> pd.Series:
    """maev_036_sma50_rat_rank_21d"""
    base = _safe_div(close, _rolling_mean(close, 50))
    return _rank_pct(base, 21)

def maev_037_sma50_rat_lvl_63d(close: pd.Series) -> pd.Series:
    """maev_037_sma50_rat_lvl_63d"""
    base = _safe_div(close, _rolling_mean(close, 50))
    return _rolling_mean(base, 63)

def maev_038_sma50_rat_zscore_63d(close: pd.Series) -> pd.Series:
    """maev_038_sma50_rat_zscore_63d"""
    base = _safe_div(close, _rolling_mean(close, 50))
    return _zscore_rolling(base, 63)

def maev_039_sma50_rat_rank_63d(close: pd.Series) -> pd.Series:
    """maev_039_sma50_rat_rank_63d"""
    base = _safe_div(close, _rolling_mean(close, 50))
    return _rank_pct(base, 63)

def maev_040_sma50_rat_lvl_126d(close: pd.Series) -> pd.Series:
    """maev_040_sma50_rat_lvl_126d"""
    base = _safe_div(close, _rolling_mean(close, 50))
    return _rolling_mean(base, 126)

def maev_041_sma50_rat_zscore_126d(close: pd.Series) -> pd.Series:
    """maev_041_sma50_rat_zscore_126d"""
    base = _safe_div(close, _rolling_mean(close, 50))
    return _zscore_rolling(base, 126)

def maev_042_sma50_rat_rank_126d(close: pd.Series) -> pd.Series:
    """maev_042_sma50_rat_rank_126d"""
    base = _safe_div(close, _rolling_mean(close, 50))
    return _rank_pct(base, 126)

def maev_043_sma50_rat_lvl_252d(close: pd.Series) -> pd.Series:
    """maev_043_sma50_rat_lvl_252d"""
    base = _safe_div(close, _rolling_mean(close, 50))
    return _rolling_mean(base, 252)

def maev_044_sma50_rat_zscore_252d(close: pd.Series) -> pd.Series:
    """maev_044_sma50_rat_zscore_252d"""
    base = _safe_div(close, _rolling_mean(close, 50))
    return _zscore_rolling(base, 252)

def maev_045_sma50_rat_rank_252d(close: pd.Series) -> pd.Series:
    """maev_045_sma50_rat_rank_252d"""
    base = _safe_div(close, _rolling_mean(close, 50))
    return _rank_pct(base, 252)

def maev_046_sma200_rat_lvl_5d(close: pd.Series) -> pd.Series:
    """maev_046_sma200_rat_lvl_5d"""
    base = _safe_div(close, _rolling_mean(close, 200))
    return _rolling_mean(base, 5)

def maev_047_sma200_rat_zscore_5d(close: pd.Series) -> pd.Series:
    """maev_047_sma200_rat_zscore_5d"""
    base = _safe_div(close, _rolling_mean(close, 200))
    return _zscore_rolling(base, 5)

def maev_048_sma200_rat_rank_5d(close: pd.Series) -> pd.Series:
    """maev_048_sma200_rat_rank_5d"""
    base = _safe_div(close, _rolling_mean(close, 200))
    return _rank_pct(base, 5)

def maev_049_sma200_rat_lvl_21d(close: pd.Series) -> pd.Series:
    """maev_049_sma200_rat_lvl_21d"""
    base = _safe_div(close, _rolling_mean(close, 200))
    return _rolling_mean(base, 21)

def maev_050_sma200_rat_zscore_21d(close: pd.Series) -> pd.Series:
    """maev_050_sma200_rat_zscore_21d"""
    base = _safe_div(close, _rolling_mean(close, 200))
    return _zscore_rolling(base, 21)

def maev_051_sma200_rat_rank_21d(close: pd.Series) -> pd.Series:
    """maev_051_sma200_rat_rank_21d"""
    base = _safe_div(close, _rolling_mean(close, 200))
    return _rank_pct(base, 21)

def maev_052_sma200_rat_lvl_63d(close: pd.Series) -> pd.Series:
    """maev_052_sma200_rat_lvl_63d"""
    base = _safe_div(close, _rolling_mean(close, 200))
    return _rolling_mean(base, 63)

def maev_053_sma200_rat_zscore_63d(close: pd.Series) -> pd.Series:
    """maev_053_sma200_rat_zscore_63d"""
    base = _safe_div(close, _rolling_mean(close, 200))
    return _zscore_rolling(base, 63)

def maev_054_sma200_rat_rank_63d(close: pd.Series) -> pd.Series:
    """maev_054_sma200_rat_rank_63d"""
    base = _safe_div(close, _rolling_mean(close, 200))
    return _rank_pct(base, 63)

def maev_055_sma200_rat_lvl_126d(close: pd.Series) -> pd.Series:
    """maev_055_sma200_rat_lvl_126d"""
    base = _safe_div(close, _rolling_mean(close, 200))
    return _rolling_mean(base, 126)

def maev_056_sma200_rat_zscore_126d(close: pd.Series) -> pd.Series:
    """maev_056_sma200_rat_zscore_126d"""
    base = _safe_div(close, _rolling_mean(close, 200))
    return _zscore_rolling(base, 126)

def maev_057_sma200_rat_rank_126d(close: pd.Series) -> pd.Series:
    """maev_057_sma200_rat_rank_126d"""
    base = _safe_div(close, _rolling_mean(close, 200))
    return _rank_pct(base, 126)

def maev_058_sma200_rat_lvl_252d(close: pd.Series) -> pd.Series:
    """maev_058_sma200_rat_lvl_252d"""
    base = _safe_div(close, _rolling_mean(close, 200))
    return _rolling_mean(base, 252)

def maev_059_sma200_rat_zscore_252d(close: pd.Series) -> pd.Series:
    """maev_059_sma200_rat_zscore_252d"""
    base = _safe_div(close, _rolling_mean(close, 200))
    return _zscore_rolling(base, 252)

def maev_060_sma200_rat_rank_252d(close: pd.Series) -> pd.Series:
    """maev_060_sma200_rat_rank_252d"""
    base = _safe_div(close, _rolling_mean(close, 200))
    return _rank_pct(base, 252)

def maev_061_cross_rat_lvl_5d(close: pd.Series) -> pd.Series:
    """maev_061_cross_rat_lvl_5d"""
    base = _safe_div(_rolling_mean(close, 20), _rolling_mean(close, 50))
    return _rolling_mean(base, 5)

def maev_062_cross_rat_zscore_5d(close: pd.Series) -> pd.Series:
    """maev_062_cross_rat_zscore_5d"""
    base = _safe_div(_rolling_mean(close, 20), _rolling_mean(close, 50))
    return _zscore_rolling(base, 5)

def maev_063_cross_rat_rank_5d(close: pd.Series) -> pd.Series:
    """maev_063_cross_rat_rank_5d"""
    base = _safe_div(_rolling_mean(close, 20), _rolling_mean(close, 50))
    return _rank_pct(base, 5)

def maev_064_cross_rat_lvl_21d(close: pd.Series) -> pd.Series:
    """maev_064_cross_rat_lvl_21d"""
    base = _safe_div(_rolling_mean(close, 20), _rolling_mean(close, 50))
    return _rolling_mean(base, 21)

def maev_065_cross_rat_zscore_21d(close: pd.Series) -> pd.Series:
    """maev_065_cross_rat_zscore_21d"""
    base = _safe_div(_rolling_mean(close, 20), _rolling_mean(close, 50))
    return _zscore_rolling(base, 21)

def maev_066_cross_rat_rank_21d(close: pd.Series) -> pd.Series:
    """maev_066_cross_rat_rank_21d"""
    base = _safe_div(_rolling_mean(close, 20), _rolling_mean(close, 50))
    return _rank_pct(base, 21)

def maev_067_cross_rat_lvl_63d(close: pd.Series) -> pd.Series:
    """maev_067_cross_rat_lvl_63d"""
    base = _safe_div(_rolling_mean(close, 20), _rolling_mean(close, 50))
    return _rolling_mean(base, 63)

def maev_068_cross_rat_zscore_63d(close: pd.Series) -> pd.Series:
    """maev_068_cross_rat_zscore_63d"""
    base = _safe_div(_rolling_mean(close, 20), _rolling_mean(close, 50))
    return _zscore_rolling(base, 63)

def maev_069_cross_rat_rank_63d(close: pd.Series) -> pd.Series:
    """maev_069_cross_rat_rank_63d"""
    base = _safe_div(_rolling_mean(close, 20), _rolling_mean(close, 50))
    return _rank_pct(base, 63)

def maev_070_cross_rat_lvl_126d(close: pd.Series) -> pd.Series:
    """maev_070_cross_rat_lvl_126d"""
    base = _safe_div(_rolling_mean(close, 20), _rolling_mean(close, 50))
    return _rolling_mean(base, 126)

def maev_071_cross_rat_zscore_126d(close: pd.Series) -> pd.Series:
    """maev_071_cross_rat_zscore_126d"""
    base = _safe_div(_rolling_mean(close, 20), _rolling_mean(close, 50))
    return _zscore_rolling(base, 126)

def maev_072_cross_rat_rank_126d(close: pd.Series) -> pd.Series:
    """maev_072_cross_rat_rank_126d"""
    base = _safe_div(_rolling_mean(close, 20), _rolling_mean(close, 50))
    return _rank_pct(base, 126)

def maev_073_cross_rat_lvl_252d(close: pd.Series) -> pd.Series:
    """maev_073_cross_rat_lvl_252d"""
    base = _safe_div(_rolling_mean(close, 20), _rolling_mean(close, 50))
    return _rolling_mean(base, 252)

def maev_074_cross_rat_zscore_252d(close: pd.Series) -> pd.Series:
    """maev_074_cross_rat_zscore_252d"""
    base = _safe_div(_rolling_mean(close, 20), _rolling_mean(close, 50))
    return _zscore_rolling(base, 252)

def maev_075_cross_rat_rank_252d(close: pd.Series) -> pd.Series:
    """maev_075_cross_rat_rank_252d"""
    base = _safe_div(_rolling_mean(close, 20), _rolling_mean(close, 50))
    return _rank_pct(base, 252)

# ── Registry ──────────────────────────────────────────────────────────────────
V79_REGISTRY = {
    "maev_001_sma20_rat_lvl_5d": {"inputs": ["close"], "func": maev_001_sma20_rat_lvl_5d},
    "maev_002_sma20_rat_zscore_5d": {"inputs": ["close"], "func": maev_002_sma20_rat_zscore_5d},
    "maev_003_sma20_rat_rank_5d": {"inputs": ["close"], "func": maev_003_sma20_rat_rank_5d},
    "maev_004_sma20_rat_lvl_21d": {"inputs": ["close"], "func": maev_004_sma20_rat_lvl_21d},
    "maev_005_sma20_rat_zscore_21d": {"inputs": ["close"], "func": maev_005_sma20_rat_zscore_21d},
    "maev_006_sma20_rat_rank_21d": {"inputs": ["close"], "func": maev_006_sma20_rat_rank_21d},
    "maev_007_sma20_rat_lvl_63d": {"inputs": ["close"], "func": maev_007_sma20_rat_lvl_63d},
    "maev_008_sma20_rat_zscore_63d": {"inputs": ["close"], "func": maev_008_sma20_rat_zscore_63d},
    "maev_009_sma20_rat_rank_63d": {"inputs": ["close"], "func": maev_009_sma20_rat_rank_63d},
    "maev_010_sma20_rat_lvl_126d": {"inputs": ["close"], "func": maev_010_sma20_rat_lvl_126d},
    "maev_011_sma20_rat_zscore_126d": {"inputs": ["close"], "func": maev_011_sma20_rat_zscore_126d},
    "maev_012_sma20_rat_rank_126d": {"inputs": ["close"], "func": maev_012_sma20_rat_rank_126d},
    "maev_013_sma20_rat_lvl_252d": {"inputs": ["close"], "func": maev_013_sma20_rat_lvl_252d},
    "maev_014_sma20_rat_zscore_252d": {"inputs": ["close"], "func": maev_014_sma20_rat_zscore_252d},
    "maev_015_sma20_rat_rank_252d": {"inputs": ["close"], "func": maev_015_sma20_rat_rank_252d},
    "maev_016_ema20_rat_lvl_5d": {"inputs": ["close"], "func": maev_016_ema20_rat_lvl_5d},
    "maev_017_ema20_rat_zscore_5d": {"inputs": ["close"], "func": maev_017_ema20_rat_zscore_5d},
    "maev_018_ema20_rat_rank_5d": {"inputs": ["close"], "func": maev_018_ema20_rat_rank_5d},
    "maev_019_ema20_rat_lvl_21d": {"inputs": ["close"], "func": maev_019_ema20_rat_lvl_21d},
    "maev_020_ema20_rat_zscore_21d": {"inputs": ["close"], "func": maev_020_ema20_rat_zscore_21d},
    "maev_021_ema20_rat_rank_21d": {"inputs": ["close"], "func": maev_021_ema20_rat_rank_21d},
    "maev_022_ema20_rat_lvl_63d": {"inputs": ["close"], "func": maev_022_ema20_rat_lvl_63d},
    "maev_023_ema20_rat_zscore_63d": {"inputs": ["close"], "func": maev_023_ema20_rat_zscore_63d},
    "maev_024_ema20_rat_rank_63d": {"inputs": ["close"], "func": maev_024_ema20_rat_rank_63d},
    "maev_025_ema20_rat_lvl_126d": {"inputs": ["close"], "func": maev_025_ema20_rat_lvl_126d},
    "maev_026_ema20_rat_zscore_126d": {"inputs": ["close"], "func": maev_026_ema20_rat_zscore_126d},
    "maev_027_ema20_rat_rank_126d": {"inputs": ["close"], "func": maev_027_ema20_rat_rank_126d},
    "maev_028_ema20_rat_lvl_252d": {"inputs": ["close"], "func": maev_028_ema20_rat_lvl_252d},
    "maev_029_ema20_rat_zscore_252d": {"inputs": ["close"], "func": maev_029_ema20_rat_zscore_252d},
    "maev_030_ema20_rat_rank_252d": {"inputs": ["close"], "func": maev_030_ema20_rat_rank_252d},
    "maev_031_sma50_rat_lvl_5d": {"inputs": ["close"], "func": maev_031_sma50_rat_lvl_5d},
    "maev_032_sma50_rat_zscore_5d": {"inputs": ["close"], "func": maev_032_sma50_rat_zscore_5d},
    "maev_033_sma50_rat_rank_5d": {"inputs": ["close"], "func": maev_033_sma50_rat_rank_5d},
    "maev_034_sma50_rat_lvl_21d": {"inputs": ["close"], "func": maev_034_sma50_rat_lvl_21d},
    "maev_035_sma50_rat_zscore_21d": {"inputs": ["close"], "func": maev_035_sma50_rat_zscore_21d},
    "maev_036_sma50_rat_rank_21d": {"inputs": ["close"], "func": maev_036_sma50_rat_rank_21d},
    "maev_037_sma50_rat_lvl_63d": {"inputs": ["close"], "func": maev_037_sma50_rat_lvl_63d},
    "maev_038_sma50_rat_zscore_63d": {"inputs": ["close"], "func": maev_038_sma50_rat_zscore_63d},
    "maev_039_sma50_rat_rank_63d": {"inputs": ["close"], "func": maev_039_sma50_rat_rank_63d},
    "maev_040_sma50_rat_lvl_126d": {"inputs": ["close"], "func": maev_040_sma50_rat_lvl_126d},
    "maev_041_sma50_rat_zscore_126d": {"inputs": ["close"], "func": maev_041_sma50_rat_zscore_126d},
    "maev_042_sma50_rat_rank_126d": {"inputs": ["close"], "func": maev_042_sma50_rat_rank_126d},
    "maev_043_sma50_rat_lvl_252d": {"inputs": ["close"], "func": maev_043_sma50_rat_lvl_252d},
    "maev_044_sma50_rat_zscore_252d": {"inputs": ["close"], "func": maev_044_sma50_rat_zscore_252d},
    "maev_045_sma50_rat_rank_252d": {"inputs": ["close"], "func": maev_045_sma50_rat_rank_252d},
    "maev_046_sma200_rat_lvl_5d": {"inputs": ["close"], "func": maev_046_sma200_rat_lvl_5d},
    "maev_047_sma200_rat_zscore_5d": {"inputs": ["close"], "func": maev_047_sma200_rat_zscore_5d},
    "maev_048_sma200_rat_rank_5d": {"inputs": ["close"], "func": maev_048_sma200_rat_rank_5d},
    "maev_049_sma200_rat_lvl_21d": {"inputs": ["close"], "func": maev_049_sma200_rat_lvl_21d},
    "maev_050_sma200_rat_zscore_21d": {"inputs": ["close"], "func": maev_050_sma200_rat_zscore_21d},
    "maev_051_sma200_rat_rank_21d": {"inputs": ["close"], "func": maev_051_sma200_rat_rank_21d},
    "maev_052_sma200_rat_lvl_63d": {"inputs": ["close"], "func": maev_052_sma200_rat_lvl_63d},
    "maev_053_sma200_rat_zscore_63d": {"inputs": ["close"], "func": maev_053_sma200_rat_zscore_63d},
    "maev_054_sma200_rat_rank_63d": {"inputs": ["close"], "func": maev_054_sma200_rat_rank_63d},
    "maev_055_sma200_rat_lvl_126d": {"inputs": ["close"], "func": maev_055_sma200_rat_lvl_126d},
    "maev_056_sma200_rat_zscore_126d": {"inputs": ["close"], "func": maev_056_sma200_rat_zscore_126d},
    "maev_057_sma200_rat_rank_126d": {"inputs": ["close"], "func": maev_057_sma200_rat_rank_126d},
    "maev_058_sma200_rat_lvl_252d": {"inputs": ["close"], "func": maev_058_sma200_rat_lvl_252d},
    "maev_059_sma200_rat_zscore_252d": {"inputs": ["close"], "func": maev_059_sma200_rat_zscore_252d},
    "maev_060_sma200_rat_rank_252d": {"inputs": ["close"], "func": maev_060_sma200_rat_rank_252d},
    "maev_061_cross_rat_lvl_5d": {"inputs": ["close"], "func": maev_061_cross_rat_lvl_5d},
    "maev_062_cross_rat_zscore_5d": {"inputs": ["close"], "func": maev_062_cross_rat_zscore_5d},
    "maev_063_cross_rat_rank_5d": {"inputs": ["close"], "func": maev_063_cross_rat_rank_5d},
    "maev_064_cross_rat_lvl_21d": {"inputs": ["close"], "func": maev_064_cross_rat_lvl_21d},
    "maev_065_cross_rat_zscore_21d": {"inputs": ["close"], "func": maev_065_cross_rat_zscore_21d},
    "maev_066_cross_rat_rank_21d": {"inputs": ["close"], "func": maev_066_cross_rat_rank_21d},
    "maev_067_cross_rat_lvl_63d": {"inputs": ["close"], "func": maev_067_cross_rat_lvl_63d},
    "maev_068_cross_rat_zscore_63d": {"inputs": ["close"], "func": maev_068_cross_rat_zscore_63d},
    "maev_069_cross_rat_rank_63d": {"inputs": ["close"], "func": maev_069_cross_rat_rank_63d},
    "maev_070_cross_rat_lvl_126d": {"inputs": ["close"], "func": maev_070_cross_rat_lvl_126d},
    "maev_071_cross_rat_zscore_126d": {"inputs": ["close"], "func": maev_071_cross_rat_zscore_126d},
    "maev_072_cross_rat_rank_126d": {"inputs": ["close"], "func": maev_072_cross_rat_rank_126d},
    "maev_073_cross_rat_lvl_252d": {"inputs": ["close"], "func": maev_073_cross_rat_lvl_252d},
    "maev_074_cross_rat_zscore_252d": {"inputs": ["close"], "func": maev_074_cross_rat_zscore_252d},
    "maev_075_cross_rat_rank_252d": {"inputs": ["close"], "func": maev_075_cross_rat_rank_252d},
}
