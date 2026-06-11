"""
75_rsi_dynamics — Base Features 001-075
Domain: rsi_dynamics
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

def rsid_001_rsi_14_lvl_5d(close: pd.Series) -> pd.Series:
    """rsid_001_rsi_14_lvl_5d"""
    base = _rsi(close, 14)
    return _rolling_mean(base, 5)

def rsid_002_rsi_14_zscore_5d(close: pd.Series) -> pd.Series:
    """rsid_002_rsi_14_zscore_5d"""
    base = _rsi(close, 14)
    return _zscore_rolling(base, 5)

def rsid_003_rsi_14_rank_5d(close: pd.Series) -> pd.Series:
    """rsid_003_rsi_14_rank_5d"""
    base = _rsi(close, 14)
    return _rank_pct(base, 5)

def rsid_004_rsi_14_lvl_21d(close: pd.Series) -> pd.Series:
    """rsid_004_rsi_14_lvl_21d"""
    base = _rsi(close, 14)
    return _rolling_mean(base, 21)

def rsid_005_rsi_14_zscore_21d(close: pd.Series) -> pd.Series:
    """rsid_005_rsi_14_zscore_21d"""
    base = _rsi(close, 14)
    return _zscore_rolling(base, 21)

def rsid_006_rsi_14_rank_21d(close: pd.Series) -> pd.Series:
    """rsid_006_rsi_14_rank_21d"""
    base = _rsi(close, 14)
    return _rank_pct(base, 21)

def rsid_007_rsi_14_lvl_63d(close: pd.Series) -> pd.Series:
    """rsid_007_rsi_14_lvl_63d"""
    base = _rsi(close, 14)
    return _rolling_mean(base, 63)

def rsid_008_rsi_14_zscore_63d(close: pd.Series) -> pd.Series:
    """rsid_008_rsi_14_zscore_63d"""
    base = _rsi(close, 14)
    return _zscore_rolling(base, 63)

def rsid_009_rsi_14_rank_63d(close: pd.Series) -> pd.Series:
    """rsid_009_rsi_14_rank_63d"""
    base = _rsi(close, 14)
    return _rank_pct(base, 63)

def rsid_010_rsi_14_lvl_126d(close: pd.Series) -> pd.Series:
    """rsid_010_rsi_14_lvl_126d"""
    base = _rsi(close, 14)
    return _rolling_mean(base, 126)

def rsid_011_rsi_14_zscore_126d(close: pd.Series) -> pd.Series:
    """rsid_011_rsi_14_zscore_126d"""
    base = _rsi(close, 14)
    return _zscore_rolling(base, 126)

def rsid_012_rsi_14_rank_126d(close: pd.Series) -> pd.Series:
    """rsid_012_rsi_14_rank_126d"""
    base = _rsi(close, 14)
    return _rank_pct(base, 126)

def rsid_013_rsi_14_lvl_252d(close: pd.Series) -> pd.Series:
    """rsid_013_rsi_14_lvl_252d"""
    base = _rsi(close, 14)
    return _rolling_mean(base, 252)

def rsid_014_rsi_14_zscore_252d(close: pd.Series) -> pd.Series:
    """rsid_014_rsi_14_zscore_252d"""
    base = _rsi(close, 14)
    return _zscore_rolling(base, 252)

def rsid_015_rsi_14_rank_252d(close: pd.Series) -> pd.Series:
    """rsid_015_rsi_14_rank_252d"""
    base = _rsi(close, 14)
    return _rank_pct(base, 252)

def rsid_016_rsi_5_lvl_5d(close: pd.Series) -> pd.Series:
    """rsid_016_rsi_5_lvl_5d"""
    base = _rsi(close, 5)
    return _rolling_mean(base, 5)

def rsid_017_rsi_5_zscore_5d(close: pd.Series) -> pd.Series:
    """rsid_017_rsi_5_zscore_5d"""
    base = _rsi(close, 5)
    return _zscore_rolling(base, 5)

def rsid_018_rsi_5_rank_5d(close: pd.Series) -> pd.Series:
    """rsid_018_rsi_5_rank_5d"""
    base = _rsi(close, 5)
    return _rank_pct(base, 5)

def rsid_019_rsi_5_lvl_21d(close: pd.Series) -> pd.Series:
    """rsid_019_rsi_5_lvl_21d"""
    base = _rsi(close, 5)
    return _rolling_mean(base, 21)

def rsid_020_rsi_5_zscore_21d(close: pd.Series) -> pd.Series:
    """rsid_020_rsi_5_zscore_21d"""
    base = _rsi(close, 5)
    return _zscore_rolling(base, 21)

def rsid_021_rsi_5_rank_21d(close: pd.Series) -> pd.Series:
    """rsid_021_rsi_5_rank_21d"""
    base = _rsi(close, 5)
    return _rank_pct(base, 21)

def rsid_022_rsi_5_lvl_63d(close: pd.Series) -> pd.Series:
    """rsid_022_rsi_5_lvl_63d"""
    base = _rsi(close, 5)
    return _rolling_mean(base, 63)

def rsid_023_rsi_5_zscore_63d(close: pd.Series) -> pd.Series:
    """rsid_023_rsi_5_zscore_63d"""
    base = _rsi(close, 5)
    return _zscore_rolling(base, 63)

def rsid_024_rsi_5_rank_63d(close: pd.Series) -> pd.Series:
    """rsid_024_rsi_5_rank_63d"""
    base = _rsi(close, 5)
    return _rank_pct(base, 63)

def rsid_025_rsi_5_lvl_126d(close: pd.Series) -> pd.Series:
    """rsid_025_rsi_5_lvl_126d"""
    base = _rsi(close, 5)
    return _rolling_mean(base, 126)

def rsid_026_rsi_5_zscore_126d(close: pd.Series) -> pd.Series:
    """rsid_026_rsi_5_zscore_126d"""
    base = _rsi(close, 5)
    return _zscore_rolling(base, 126)

def rsid_027_rsi_5_rank_126d(close: pd.Series) -> pd.Series:
    """rsid_027_rsi_5_rank_126d"""
    base = _rsi(close, 5)
    return _rank_pct(base, 126)

def rsid_028_rsi_5_lvl_252d(close: pd.Series) -> pd.Series:
    """rsid_028_rsi_5_lvl_252d"""
    base = _rsi(close, 5)
    return _rolling_mean(base, 252)

def rsid_029_rsi_5_zscore_252d(close: pd.Series) -> pd.Series:
    """rsid_029_rsi_5_zscore_252d"""
    base = _rsi(close, 5)
    return _zscore_rolling(base, 252)

def rsid_030_rsi_5_rank_252d(close: pd.Series) -> pd.Series:
    """rsid_030_rsi_5_rank_252d"""
    base = _rsi(close, 5)
    return _rank_pct(base, 252)

def rsid_031_rsi_21_lvl_5d(close: pd.Series) -> pd.Series:
    """rsid_031_rsi_21_lvl_5d"""
    base = _rsi(close, 21)
    return _rolling_mean(base, 5)

def rsid_032_rsi_21_zscore_5d(close: pd.Series) -> pd.Series:
    """rsid_032_rsi_21_zscore_5d"""
    base = _rsi(close, 21)
    return _zscore_rolling(base, 5)

def rsid_033_rsi_21_rank_5d(close: pd.Series) -> pd.Series:
    """rsid_033_rsi_21_rank_5d"""
    base = _rsi(close, 21)
    return _rank_pct(base, 5)

def rsid_034_rsi_21_lvl_21d(close: pd.Series) -> pd.Series:
    """rsid_034_rsi_21_lvl_21d"""
    base = _rsi(close, 21)
    return _rolling_mean(base, 21)

def rsid_035_rsi_21_zscore_21d(close: pd.Series) -> pd.Series:
    """rsid_035_rsi_21_zscore_21d"""
    base = _rsi(close, 21)
    return _zscore_rolling(base, 21)

def rsid_036_rsi_21_rank_21d(close: pd.Series) -> pd.Series:
    """rsid_036_rsi_21_rank_21d"""
    base = _rsi(close, 21)
    return _rank_pct(base, 21)

def rsid_037_rsi_21_lvl_63d(close: pd.Series) -> pd.Series:
    """rsid_037_rsi_21_lvl_63d"""
    base = _rsi(close, 21)
    return _rolling_mean(base, 63)

def rsid_038_rsi_21_zscore_63d(close: pd.Series) -> pd.Series:
    """rsid_038_rsi_21_zscore_63d"""
    base = _rsi(close, 21)
    return _zscore_rolling(base, 63)

def rsid_039_rsi_21_rank_63d(close: pd.Series) -> pd.Series:
    """rsid_039_rsi_21_rank_63d"""
    base = _rsi(close, 21)
    return _rank_pct(base, 63)

def rsid_040_rsi_21_lvl_126d(close: pd.Series) -> pd.Series:
    """rsid_040_rsi_21_lvl_126d"""
    base = _rsi(close, 21)
    return _rolling_mean(base, 126)

def rsid_041_rsi_21_zscore_126d(close: pd.Series) -> pd.Series:
    """rsid_041_rsi_21_zscore_126d"""
    base = _rsi(close, 21)
    return _zscore_rolling(base, 126)

def rsid_042_rsi_21_rank_126d(close: pd.Series) -> pd.Series:
    """rsid_042_rsi_21_rank_126d"""
    base = _rsi(close, 21)
    return _rank_pct(base, 126)

def rsid_043_rsi_21_lvl_252d(close: pd.Series) -> pd.Series:
    """rsid_043_rsi_21_lvl_252d"""
    base = _rsi(close, 21)
    return _rolling_mean(base, 252)

def rsid_044_rsi_21_zscore_252d(close: pd.Series) -> pd.Series:
    """rsid_044_rsi_21_zscore_252d"""
    base = _rsi(close, 21)
    return _zscore_rolling(base, 252)

def rsid_045_rsi_21_rank_252d(close: pd.Series) -> pd.Series:
    """rsid_045_rsi_21_rank_252d"""
    base = _rsi(close, 21)
    return _rank_pct(base, 252)

def rsid_046_rsi_dist_lvl_5d(close: pd.Series) -> pd.Series:
    """rsid_046_rsi_dist_lvl_5d"""
    base = _rsi(close, 14) - 50
    return _rolling_mean(base, 5)

def rsid_047_rsi_dist_zscore_5d(close: pd.Series) -> pd.Series:
    """rsid_047_rsi_dist_zscore_5d"""
    base = _rsi(close, 14) - 50
    return _zscore_rolling(base, 5)

def rsid_048_rsi_dist_rank_5d(close: pd.Series) -> pd.Series:
    """rsid_048_rsi_dist_rank_5d"""
    base = _rsi(close, 14) - 50
    return _rank_pct(base, 5)

def rsid_049_rsi_dist_lvl_21d(close: pd.Series) -> pd.Series:
    """rsid_049_rsi_dist_lvl_21d"""
    base = _rsi(close, 14) - 50
    return _rolling_mean(base, 21)

def rsid_050_rsi_dist_zscore_21d(close: pd.Series) -> pd.Series:
    """rsid_050_rsi_dist_zscore_21d"""
    base = _rsi(close, 14) - 50
    return _zscore_rolling(base, 21)

def rsid_051_rsi_dist_rank_21d(close: pd.Series) -> pd.Series:
    """rsid_051_rsi_dist_rank_21d"""
    base = _rsi(close, 14) - 50
    return _rank_pct(base, 21)

def rsid_052_rsi_dist_lvl_63d(close: pd.Series) -> pd.Series:
    """rsid_052_rsi_dist_lvl_63d"""
    base = _rsi(close, 14) - 50
    return _rolling_mean(base, 63)

def rsid_053_rsi_dist_zscore_63d(close: pd.Series) -> pd.Series:
    """rsid_053_rsi_dist_zscore_63d"""
    base = _rsi(close, 14) - 50
    return _zscore_rolling(base, 63)

def rsid_054_rsi_dist_rank_63d(close: pd.Series) -> pd.Series:
    """rsid_054_rsi_dist_rank_63d"""
    base = _rsi(close, 14) - 50
    return _rank_pct(base, 63)

def rsid_055_rsi_dist_lvl_126d(close: pd.Series) -> pd.Series:
    """rsid_055_rsi_dist_lvl_126d"""
    base = _rsi(close, 14) - 50
    return _rolling_mean(base, 126)

def rsid_056_rsi_dist_zscore_126d(close: pd.Series) -> pd.Series:
    """rsid_056_rsi_dist_zscore_126d"""
    base = _rsi(close, 14) - 50
    return _zscore_rolling(base, 126)

def rsid_057_rsi_dist_rank_126d(close: pd.Series) -> pd.Series:
    """rsid_057_rsi_dist_rank_126d"""
    base = _rsi(close, 14) - 50
    return _rank_pct(base, 126)

def rsid_058_rsi_dist_lvl_252d(close: pd.Series) -> pd.Series:
    """rsid_058_rsi_dist_lvl_252d"""
    base = _rsi(close, 14) - 50
    return _rolling_mean(base, 252)

def rsid_059_rsi_dist_zscore_252d(close: pd.Series) -> pd.Series:
    """rsid_059_rsi_dist_zscore_252d"""
    base = _rsi(close, 14) - 50
    return _zscore_rolling(base, 252)

def rsid_060_rsi_dist_rank_252d(close: pd.Series) -> pd.Series:
    """rsid_060_rsi_dist_rank_252d"""
    base = _rsi(close, 14) - 50
    return _rank_pct(base, 252)

def rsid_061_rsi_ob_lvl_5d(close: pd.Series) -> pd.Series:
    """rsid_061_rsi_ob_lvl_5d"""
    base = _rsi(close, 14) - 70
    return _rolling_mean(base, 5)

def rsid_062_rsi_ob_zscore_5d(close: pd.Series) -> pd.Series:
    """rsid_062_rsi_ob_zscore_5d"""
    base = _rsi(close, 14) - 70
    return _zscore_rolling(base, 5)

def rsid_063_rsi_ob_rank_5d(close: pd.Series) -> pd.Series:
    """rsid_063_rsi_ob_rank_5d"""
    base = _rsi(close, 14) - 70
    return _rank_pct(base, 5)

def rsid_064_rsi_ob_lvl_21d(close: pd.Series) -> pd.Series:
    """rsid_064_rsi_ob_lvl_21d"""
    base = _rsi(close, 14) - 70
    return _rolling_mean(base, 21)

def rsid_065_rsi_ob_zscore_21d(close: pd.Series) -> pd.Series:
    """rsid_065_rsi_ob_zscore_21d"""
    base = _rsi(close, 14) - 70
    return _zscore_rolling(base, 21)

def rsid_066_rsi_ob_rank_21d(close: pd.Series) -> pd.Series:
    """rsid_066_rsi_ob_rank_21d"""
    base = _rsi(close, 14) - 70
    return _rank_pct(base, 21)

def rsid_067_rsi_ob_lvl_63d(close: pd.Series) -> pd.Series:
    """rsid_067_rsi_ob_lvl_63d"""
    base = _rsi(close, 14) - 70
    return _rolling_mean(base, 63)

def rsid_068_rsi_ob_zscore_63d(close: pd.Series) -> pd.Series:
    """rsid_068_rsi_ob_zscore_63d"""
    base = _rsi(close, 14) - 70
    return _zscore_rolling(base, 63)

def rsid_069_rsi_ob_rank_63d(close: pd.Series) -> pd.Series:
    """rsid_069_rsi_ob_rank_63d"""
    base = _rsi(close, 14) - 70
    return _rank_pct(base, 63)

def rsid_070_rsi_ob_lvl_126d(close: pd.Series) -> pd.Series:
    """rsid_070_rsi_ob_lvl_126d"""
    base = _rsi(close, 14) - 70
    return _rolling_mean(base, 126)

def rsid_071_rsi_ob_zscore_126d(close: pd.Series) -> pd.Series:
    """rsid_071_rsi_ob_zscore_126d"""
    base = _rsi(close, 14) - 70
    return _zscore_rolling(base, 126)

def rsid_072_rsi_ob_rank_126d(close: pd.Series) -> pd.Series:
    """rsid_072_rsi_ob_rank_126d"""
    base = _rsi(close, 14) - 70
    return _rank_pct(base, 126)

def rsid_073_rsi_ob_lvl_252d(close: pd.Series) -> pd.Series:
    """rsid_073_rsi_ob_lvl_252d"""
    base = _rsi(close, 14) - 70
    return _rolling_mean(base, 252)

def rsid_074_rsi_ob_zscore_252d(close: pd.Series) -> pd.Series:
    """rsid_074_rsi_ob_zscore_252d"""
    base = _rsi(close, 14) - 70
    return _zscore_rolling(base, 252)

def rsid_075_rsi_ob_rank_252d(close: pd.Series) -> pd.Series:
    """rsid_075_rsi_ob_rank_252d"""
    base = _rsi(close, 14) - 70
    return _rank_pct(base, 252)

# ── Registry ──────────────────────────────────────────────────────────────────
V75_REGISTRY = {
    "rsid_001_rsi_14_lvl_5d": {"inputs": ["close"], "func": rsid_001_rsi_14_lvl_5d},
    "rsid_002_rsi_14_zscore_5d": {"inputs": ["close"], "func": rsid_002_rsi_14_zscore_5d},
    "rsid_003_rsi_14_rank_5d": {"inputs": ["close"], "func": rsid_003_rsi_14_rank_5d},
    "rsid_004_rsi_14_lvl_21d": {"inputs": ["close"], "func": rsid_004_rsi_14_lvl_21d},
    "rsid_005_rsi_14_zscore_21d": {"inputs": ["close"], "func": rsid_005_rsi_14_zscore_21d},
    "rsid_006_rsi_14_rank_21d": {"inputs": ["close"], "func": rsid_006_rsi_14_rank_21d},
    "rsid_007_rsi_14_lvl_63d": {"inputs": ["close"], "func": rsid_007_rsi_14_lvl_63d},
    "rsid_008_rsi_14_zscore_63d": {"inputs": ["close"], "func": rsid_008_rsi_14_zscore_63d},
    "rsid_009_rsi_14_rank_63d": {"inputs": ["close"], "func": rsid_009_rsi_14_rank_63d},
    "rsid_010_rsi_14_lvl_126d": {"inputs": ["close"], "func": rsid_010_rsi_14_lvl_126d},
    "rsid_011_rsi_14_zscore_126d": {"inputs": ["close"], "func": rsid_011_rsi_14_zscore_126d},
    "rsid_012_rsi_14_rank_126d": {"inputs": ["close"], "func": rsid_012_rsi_14_rank_126d},
    "rsid_013_rsi_14_lvl_252d": {"inputs": ["close"], "func": rsid_013_rsi_14_lvl_252d},
    "rsid_014_rsi_14_zscore_252d": {"inputs": ["close"], "func": rsid_014_rsi_14_zscore_252d},
    "rsid_015_rsi_14_rank_252d": {"inputs": ["close"], "func": rsid_015_rsi_14_rank_252d},
    "rsid_016_rsi_5_lvl_5d": {"inputs": ["close"], "func": rsid_016_rsi_5_lvl_5d},
    "rsid_017_rsi_5_zscore_5d": {"inputs": ["close"], "func": rsid_017_rsi_5_zscore_5d},
    "rsid_018_rsi_5_rank_5d": {"inputs": ["close"], "func": rsid_018_rsi_5_rank_5d},
    "rsid_019_rsi_5_lvl_21d": {"inputs": ["close"], "func": rsid_019_rsi_5_lvl_21d},
    "rsid_020_rsi_5_zscore_21d": {"inputs": ["close"], "func": rsid_020_rsi_5_zscore_21d},
    "rsid_021_rsi_5_rank_21d": {"inputs": ["close"], "func": rsid_021_rsi_5_rank_21d},
    "rsid_022_rsi_5_lvl_63d": {"inputs": ["close"], "func": rsid_022_rsi_5_lvl_63d},
    "rsid_023_rsi_5_zscore_63d": {"inputs": ["close"], "func": rsid_023_rsi_5_zscore_63d},
    "rsid_024_rsi_5_rank_63d": {"inputs": ["close"], "func": rsid_024_rsi_5_rank_63d},
    "rsid_025_rsi_5_lvl_126d": {"inputs": ["close"], "func": rsid_025_rsi_5_lvl_126d},
    "rsid_026_rsi_5_zscore_126d": {"inputs": ["close"], "func": rsid_026_rsi_5_zscore_126d},
    "rsid_027_rsi_5_rank_126d": {"inputs": ["close"], "func": rsid_027_rsi_5_rank_126d},
    "rsid_028_rsi_5_lvl_252d": {"inputs": ["close"], "func": rsid_028_rsi_5_lvl_252d},
    "rsid_029_rsi_5_zscore_252d": {"inputs": ["close"], "func": rsid_029_rsi_5_zscore_252d},
    "rsid_030_rsi_5_rank_252d": {"inputs": ["close"], "func": rsid_030_rsi_5_rank_252d},
    "rsid_031_rsi_21_lvl_5d": {"inputs": ["close"], "func": rsid_031_rsi_21_lvl_5d},
    "rsid_032_rsi_21_zscore_5d": {"inputs": ["close"], "func": rsid_032_rsi_21_zscore_5d},
    "rsid_033_rsi_21_rank_5d": {"inputs": ["close"], "func": rsid_033_rsi_21_rank_5d},
    "rsid_034_rsi_21_lvl_21d": {"inputs": ["close"], "func": rsid_034_rsi_21_lvl_21d},
    "rsid_035_rsi_21_zscore_21d": {"inputs": ["close"], "func": rsid_035_rsi_21_zscore_21d},
    "rsid_036_rsi_21_rank_21d": {"inputs": ["close"], "func": rsid_036_rsi_21_rank_21d},
    "rsid_037_rsi_21_lvl_63d": {"inputs": ["close"], "func": rsid_037_rsi_21_lvl_63d},
    "rsid_038_rsi_21_zscore_63d": {"inputs": ["close"], "func": rsid_038_rsi_21_zscore_63d},
    "rsid_039_rsi_21_rank_63d": {"inputs": ["close"], "func": rsid_039_rsi_21_rank_63d},
    "rsid_040_rsi_21_lvl_126d": {"inputs": ["close"], "func": rsid_040_rsi_21_lvl_126d},
    "rsid_041_rsi_21_zscore_126d": {"inputs": ["close"], "func": rsid_041_rsi_21_zscore_126d},
    "rsid_042_rsi_21_rank_126d": {"inputs": ["close"], "func": rsid_042_rsi_21_rank_126d},
    "rsid_043_rsi_21_lvl_252d": {"inputs": ["close"], "func": rsid_043_rsi_21_lvl_252d},
    "rsid_044_rsi_21_zscore_252d": {"inputs": ["close"], "func": rsid_044_rsi_21_zscore_252d},
    "rsid_045_rsi_21_rank_252d": {"inputs": ["close"], "func": rsid_045_rsi_21_rank_252d},
    "rsid_046_rsi_dist_lvl_5d": {"inputs": ["close"], "func": rsid_046_rsi_dist_lvl_5d},
    "rsid_047_rsi_dist_zscore_5d": {"inputs": ["close"], "func": rsid_047_rsi_dist_zscore_5d},
    "rsid_048_rsi_dist_rank_5d": {"inputs": ["close"], "func": rsid_048_rsi_dist_rank_5d},
    "rsid_049_rsi_dist_lvl_21d": {"inputs": ["close"], "func": rsid_049_rsi_dist_lvl_21d},
    "rsid_050_rsi_dist_zscore_21d": {"inputs": ["close"], "func": rsid_050_rsi_dist_zscore_21d},
    "rsid_051_rsi_dist_rank_21d": {"inputs": ["close"], "func": rsid_051_rsi_dist_rank_21d},
    "rsid_052_rsi_dist_lvl_63d": {"inputs": ["close"], "func": rsid_052_rsi_dist_lvl_63d},
    "rsid_053_rsi_dist_zscore_63d": {"inputs": ["close"], "func": rsid_053_rsi_dist_zscore_63d},
    "rsid_054_rsi_dist_rank_63d": {"inputs": ["close"], "func": rsid_054_rsi_dist_rank_63d},
    "rsid_055_rsi_dist_lvl_126d": {"inputs": ["close"], "func": rsid_055_rsi_dist_lvl_126d},
    "rsid_056_rsi_dist_zscore_126d": {"inputs": ["close"], "func": rsid_056_rsi_dist_zscore_126d},
    "rsid_057_rsi_dist_rank_126d": {"inputs": ["close"], "func": rsid_057_rsi_dist_rank_126d},
    "rsid_058_rsi_dist_lvl_252d": {"inputs": ["close"], "func": rsid_058_rsi_dist_lvl_252d},
    "rsid_059_rsi_dist_zscore_252d": {"inputs": ["close"], "func": rsid_059_rsi_dist_zscore_252d},
    "rsid_060_rsi_dist_rank_252d": {"inputs": ["close"], "func": rsid_060_rsi_dist_rank_252d},
    "rsid_061_rsi_ob_lvl_5d": {"inputs": ["close"], "func": rsid_061_rsi_ob_lvl_5d},
    "rsid_062_rsi_ob_zscore_5d": {"inputs": ["close"], "func": rsid_062_rsi_ob_zscore_5d},
    "rsid_063_rsi_ob_rank_5d": {"inputs": ["close"], "func": rsid_063_rsi_ob_rank_5d},
    "rsid_064_rsi_ob_lvl_21d": {"inputs": ["close"], "func": rsid_064_rsi_ob_lvl_21d},
    "rsid_065_rsi_ob_zscore_21d": {"inputs": ["close"], "func": rsid_065_rsi_ob_zscore_21d},
    "rsid_066_rsi_ob_rank_21d": {"inputs": ["close"], "func": rsid_066_rsi_ob_rank_21d},
    "rsid_067_rsi_ob_lvl_63d": {"inputs": ["close"], "func": rsid_067_rsi_ob_lvl_63d},
    "rsid_068_rsi_ob_zscore_63d": {"inputs": ["close"], "func": rsid_068_rsi_ob_zscore_63d},
    "rsid_069_rsi_ob_rank_63d": {"inputs": ["close"], "func": rsid_069_rsi_ob_rank_63d},
    "rsid_070_rsi_ob_lvl_126d": {"inputs": ["close"], "func": rsid_070_rsi_ob_lvl_126d},
    "rsid_071_rsi_ob_zscore_126d": {"inputs": ["close"], "func": rsid_071_rsi_ob_zscore_126d},
    "rsid_072_rsi_ob_rank_126d": {"inputs": ["close"], "func": rsid_072_rsi_ob_rank_126d},
    "rsid_073_rsi_ob_lvl_252d": {"inputs": ["close"], "func": rsid_073_rsi_ob_lvl_252d},
    "rsid_074_rsi_ob_zscore_252d": {"inputs": ["close"], "func": rsid_074_rsi_ob_zscore_252d},
    "rsid_075_rsi_ob_rank_252d": {"inputs": ["close"], "func": rsid_075_rsi_ob_rank_252d},
}
