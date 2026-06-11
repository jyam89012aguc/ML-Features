"""
77_bolp_dynamics — Base Features 001-075
Domain: bolp_dynamics
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

def bolp_001_bb_upper_lvl_5d(close: pd.Series) -> pd.Series:
    """bolp_001_bb_upper_lvl_5d"""
    base = _rolling_mean(close, 20) + 2 * _rolling_std(close, 20)
    return _rolling_mean(base, 5)

def bolp_002_bb_upper_zscore_5d(close: pd.Series) -> pd.Series:
    """bolp_002_bb_upper_zscore_5d"""
    base = _rolling_mean(close, 20) + 2 * _rolling_std(close, 20)
    return _zscore_rolling(base, 5)

def bolp_003_bb_upper_rank_5d(close: pd.Series) -> pd.Series:
    """bolp_003_bb_upper_rank_5d"""
    base = _rolling_mean(close, 20) + 2 * _rolling_std(close, 20)
    return _rank_pct(base, 5)

def bolp_004_bb_upper_lvl_21d(close: pd.Series) -> pd.Series:
    """bolp_004_bb_upper_lvl_21d"""
    base = _rolling_mean(close, 20) + 2 * _rolling_std(close, 20)
    return _rolling_mean(base, 21)

def bolp_005_bb_upper_zscore_21d(close: pd.Series) -> pd.Series:
    """bolp_005_bb_upper_zscore_21d"""
    base = _rolling_mean(close, 20) + 2 * _rolling_std(close, 20)
    return _zscore_rolling(base, 21)

def bolp_006_bb_upper_rank_21d(close: pd.Series) -> pd.Series:
    """bolp_006_bb_upper_rank_21d"""
    base = _rolling_mean(close, 20) + 2 * _rolling_std(close, 20)
    return _rank_pct(base, 21)

def bolp_007_bb_upper_lvl_63d(close: pd.Series) -> pd.Series:
    """bolp_007_bb_upper_lvl_63d"""
    base = _rolling_mean(close, 20) + 2 * _rolling_std(close, 20)
    return _rolling_mean(base, 63)

def bolp_008_bb_upper_zscore_63d(close: pd.Series) -> pd.Series:
    """bolp_008_bb_upper_zscore_63d"""
    base = _rolling_mean(close, 20) + 2 * _rolling_std(close, 20)
    return _zscore_rolling(base, 63)

def bolp_009_bb_upper_rank_63d(close: pd.Series) -> pd.Series:
    """bolp_009_bb_upper_rank_63d"""
    base = _rolling_mean(close, 20) + 2 * _rolling_std(close, 20)
    return _rank_pct(base, 63)

def bolp_010_bb_upper_lvl_126d(close: pd.Series) -> pd.Series:
    """bolp_010_bb_upper_lvl_126d"""
    base = _rolling_mean(close, 20) + 2 * _rolling_std(close, 20)
    return _rolling_mean(base, 126)

def bolp_011_bb_upper_zscore_126d(close: pd.Series) -> pd.Series:
    """bolp_011_bb_upper_zscore_126d"""
    base = _rolling_mean(close, 20) + 2 * _rolling_std(close, 20)
    return _zscore_rolling(base, 126)

def bolp_012_bb_upper_rank_126d(close: pd.Series) -> pd.Series:
    """bolp_012_bb_upper_rank_126d"""
    base = _rolling_mean(close, 20) + 2 * _rolling_std(close, 20)
    return _rank_pct(base, 126)

def bolp_013_bb_upper_lvl_252d(close: pd.Series) -> pd.Series:
    """bolp_013_bb_upper_lvl_252d"""
    base = _rolling_mean(close, 20) + 2 * _rolling_std(close, 20)
    return _rolling_mean(base, 252)

def bolp_014_bb_upper_zscore_252d(close: pd.Series) -> pd.Series:
    """bolp_014_bb_upper_zscore_252d"""
    base = _rolling_mean(close, 20) + 2 * _rolling_std(close, 20)
    return _zscore_rolling(base, 252)

def bolp_015_bb_upper_rank_252d(close: pd.Series) -> pd.Series:
    """bolp_015_bb_upper_rank_252d"""
    base = _rolling_mean(close, 20) + 2 * _rolling_std(close, 20)
    return _rank_pct(base, 252)

def bolp_016_bb_lower_lvl_5d(close: pd.Series) -> pd.Series:
    """bolp_016_bb_lower_lvl_5d"""
    base = _rolling_mean(close, 20) - 2 * _rolling_std(close, 20)
    return _rolling_mean(base, 5)

def bolp_017_bb_lower_zscore_5d(close: pd.Series) -> pd.Series:
    """bolp_017_bb_lower_zscore_5d"""
    base = _rolling_mean(close, 20) - 2 * _rolling_std(close, 20)
    return _zscore_rolling(base, 5)

def bolp_018_bb_lower_rank_5d(close: pd.Series) -> pd.Series:
    """bolp_018_bb_lower_rank_5d"""
    base = _rolling_mean(close, 20) - 2 * _rolling_std(close, 20)
    return _rank_pct(base, 5)

def bolp_019_bb_lower_lvl_21d(close: pd.Series) -> pd.Series:
    """bolp_019_bb_lower_lvl_21d"""
    base = _rolling_mean(close, 20) - 2 * _rolling_std(close, 20)
    return _rolling_mean(base, 21)

def bolp_020_bb_lower_zscore_21d(close: pd.Series) -> pd.Series:
    """bolp_020_bb_lower_zscore_21d"""
    base = _rolling_mean(close, 20) - 2 * _rolling_std(close, 20)
    return _zscore_rolling(base, 21)

def bolp_021_bb_lower_rank_21d(close: pd.Series) -> pd.Series:
    """bolp_021_bb_lower_rank_21d"""
    base = _rolling_mean(close, 20) - 2 * _rolling_std(close, 20)
    return _rank_pct(base, 21)

def bolp_022_bb_lower_lvl_63d(close: pd.Series) -> pd.Series:
    """bolp_022_bb_lower_lvl_63d"""
    base = _rolling_mean(close, 20) - 2 * _rolling_std(close, 20)
    return _rolling_mean(base, 63)

def bolp_023_bb_lower_zscore_63d(close: pd.Series) -> pd.Series:
    """bolp_023_bb_lower_zscore_63d"""
    base = _rolling_mean(close, 20) - 2 * _rolling_std(close, 20)
    return _zscore_rolling(base, 63)

def bolp_024_bb_lower_rank_63d(close: pd.Series) -> pd.Series:
    """bolp_024_bb_lower_rank_63d"""
    base = _rolling_mean(close, 20) - 2 * _rolling_std(close, 20)
    return _rank_pct(base, 63)

def bolp_025_bb_lower_lvl_126d(close: pd.Series) -> pd.Series:
    """bolp_025_bb_lower_lvl_126d"""
    base = _rolling_mean(close, 20) - 2 * _rolling_std(close, 20)
    return _rolling_mean(base, 126)

def bolp_026_bb_lower_zscore_126d(close: pd.Series) -> pd.Series:
    """bolp_026_bb_lower_zscore_126d"""
    base = _rolling_mean(close, 20) - 2 * _rolling_std(close, 20)
    return _zscore_rolling(base, 126)

def bolp_027_bb_lower_rank_126d(close: pd.Series) -> pd.Series:
    """bolp_027_bb_lower_rank_126d"""
    base = _rolling_mean(close, 20) - 2 * _rolling_std(close, 20)
    return _rank_pct(base, 126)

def bolp_028_bb_lower_lvl_252d(close: pd.Series) -> pd.Series:
    """bolp_028_bb_lower_lvl_252d"""
    base = _rolling_mean(close, 20) - 2 * _rolling_std(close, 20)
    return _rolling_mean(base, 252)

def bolp_029_bb_lower_zscore_252d(close: pd.Series) -> pd.Series:
    """bolp_029_bb_lower_zscore_252d"""
    base = _rolling_mean(close, 20) - 2 * _rolling_std(close, 20)
    return _zscore_rolling(base, 252)

def bolp_030_bb_lower_rank_252d(close: pd.Series) -> pd.Series:
    """bolp_030_bb_lower_rank_252d"""
    base = _rolling_mean(close, 20) - 2 * _rolling_std(close, 20)
    return _rank_pct(base, 252)

def bolp_031_bb_width_lvl_5d(close: pd.Series) -> pd.Series:
    """bolp_031_bb_width_lvl_5d"""
    base = _safe_div(4 * _rolling_std(close, 20), _rolling_mean(close, 20))
    return _rolling_mean(base, 5)

def bolp_032_bb_width_zscore_5d(close: pd.Series) -> pd.Series:
    """bolp_032_bb_width_zscore_5d"""
    base = _safe_div(4 * _rolling_std(close, 20), _rolling_mean(close, 20))
    return _zscore_rolling(base, 5)

def bolp_033_bb_width_rank_5d(close: pd.Series) -> pd.Series:
    """bolp_033_bb_width_rank_5d"""
    base = _safe_div(4 * _rolling_std(close, 20), _rolling_mean(close, 20))
    return _rank_pct(base, 5)

def bolp_034_bb_width_lvl_21d(close: pd.Series) -> pd.Series:
    """bolp_034_bb_width_lvl_21d"""
    base = _safe_div(4 * _rolling_std(close, 20), _rolling_mean(close, 20))
    return _rolling_mean(base, 21)

def bolp_035_bb_width_zscore_21d(close: pd.Series) -> pd.Series:
    """bolp_035_bb_width_zscore_21d"""
    base = _safe_div(4 * _rolling_std(close, 20), _rolling_mean(close, 20))
    return _zscore_rolling(base, 21)

def bolp_036_bb_width_rank_21d(close: pd.Series) -> pd.Series:
    """bolp_036_bb_width_rank_21d"""
    base = _safe_div(4 * _rolling_std(close, 20), _rolling_mean(close, 20))
    return _rank_pct(base, 21)

def bolp_037_bb_width_lvl_63d(close: pd.Series) -> pd.Series:
    """bolp_037_bb_width_lvl_63d"""
    base = _safe_div(4 * _rolling_std(close, 20), _rolling_mean(close, 20))
    return _rolling_mean(base, 63)

def bolp_038_bb_width_zscore_63d(close: pd.Series) -> pd.Series:
    """bolp_038_bb_width_zscore_63d"""
    base = _safe_div(4 * _rolling_std(close, 20), _rolling_mean(close, 20))
    return _zscore_rolling(base, 63)

def bolp_039_bb_width_rank_63d(close: pd.Series) -> pd.Series:
    """bolp_039_bb_width_rank_63d"""
    base = _safe_div(4 * _rolling_std(close, 20), _rolling_mean(close, 20))
    return _rank_pct(base, 63)

def bolp_040_bb_width_lvl_126d(close: pd.Series) -> pd.Series:
    """bolp_040_bb_width_lvl_126d"""
    base = _safe_div(4 * _rolling_std(close, 20), _rolling_mean(close, 20))
    return _rolling_mean(base, 126)

def bolp_041_bb_width_zscore_126d(close: pd.Series) -> pd.Series:
    """bolp_041_bb_width_zscore_126d"""
    base = _safe_div(4 * _rolling_std(close, 20), _rolling_mean(close, 20))
    return _zscore_rolling(base, 126)

def bolp_042_bb_width_rank_126d(close: pd.Series) -> pd.Series:
    """bolp_042_bb_width_rank_126d"""
    base = _safe_div(4 * _rolling_std(close, 20), _rolling_mean(close, 20))
    return _rank_pct(base, 126)

def bolp_043_bb_width_lvl_252d(close: pd.Series) -> pd.Series:
    """bolp_043_bb_width_lvl_252d"""
    base = _safe_div(4 * _rolling_std(close, 20), _rolling_mean(close, 20))
    return _rolling_mean(base, 252)

def bolp_044_bb_width_zscore_252d(close: pd.Series) -> pd.Series:
    """bolp_044_bb_width_zscore_252d"""
    base = _safe_div(4 * _rolling_std(close, 20), _rolling_mean(close, 20))
    return _zscore_rolling(base, 252)

def bolp_045_bb_width_rank_252d(close: pd.Series) -> pd.Series:
    """bolp_045_bb_width_rank_252d"""
    base = _safe_div(4 * _rolling_std(close, 20), _rolling_mean(close, 20))
    return _rank_pct(base, 252)

def bolp_046_bb_pctb_lvl_5d(close: pd.Series) -> pd.Series:
    """bolp_046_bb_pctb_lvl_5d"""
    base = _safe_div(close - (_rolling_mean(close, 20) - 2 * _rolling_std(close, 20)), 4 * _rolling_std(close, 20))
    return _rolling_mean(base, 5)

def bolp_047_bb_pctb_zscore_5d(close: pd.Series) -> pd.Series:
    """bolp_047_bb_pctb_zscore_5d"""
    base = _safe_div(close - (_rolling_mean(close, 20) - 2 * _rolling_std(close, 20)), 4 * _rolling_std(close, 20))
    return _zscore_rolling(base, 5)

def bolp_048_bb_pctb_rank_5d(close: pd.Series) -> pd.Series:
    """bolp_048_bb_pctb_rank_5d"""
    base = _safe_div(close - (_rolling_mean(close, 20) - 2 * _rolling_std(close, 20)), 4 * _rolling_std(close, 20))
    return _rank_pct(base, 5)

def bolp_049_bb_pctb_lvl_21d(close: pd.Series) -> pd.Series:
    """bolp_049_bb_pctb_lvl_21d"""
    base = _safe_div(close - (_rolling_mean(close, 20) - 2 * _rolling_std(close, 20)), 4 * _rolling_std(close, 20))
    return _rolling_mean(base, 21)

def bolp_050_bb_pctb_zscore_21d(close: pd.Series) -> pd.Series:
    """bolp_050_bb_pctb_zscore_21d"""
    base = _safe_div(close - (_rolling_mean(close, 20) - 2 * _rolling_std(close, 20)), 4 * _rolling_std(close, 20))
    return _zscore_rolling(base, 21)

def bolp_051_bb_pctb_rank_21d(close: pd.Series) -> pd.Series:
    """bolp_051_bb_pctb_rank_21d"""
    base = _safe_div(close - (_rolling_mean(close, 20) - 2 * _rolling_std(close, 20)), 4 * _rolling_std(close, 20))
    return _rank_pct(base, 21)

def bolp_052_bb_pctb_lvl_63d(close: pd.Series) -> pd.Series:
    """bolp_052_bb_pctb_lvl_63d"""
    base = _safe_div(close - (_rolling_mean(close, 20) - 2 * _rolling_std(close, 20)), 4 * _rolling_std(close, 20))
    return _rolling_mean(base, 63)

def bolp_053_bb_pctb_zscore_63d(close: pd.Series) -> pd.Series:
    """bolp_053_bb_pctb_zscore_63d"""
    base = _safe_div(close - (_rolling_mean(close, 20) - 2 * _rolling_std(close, 20)), 4 * _rolling_std(close, 20))
    return _zscore_rolling(base, 63)

def bolp_054_bb_pctb_rank_63d(close: pd.Series) -> pd.Series:
    """bolp_054_bb_pctb_rank_63d"""
    base = _safe_div(close - (_rolling_mean(close, 20) - 2 * _rolling_std(close, 20)), 4 * _rolling_std(close, 20))
    return _rank_pct(base, 63)

def bolp_055_bb_pctb_lvl_126d(close: pd.Series) -> pd.Series:
    """bolp_055_bb_pctb_lvl_126d"""
    base = _safe_div(close - (_rolling_mean(close, 20) - 2 * _rolling_std(close, 20)), 4 * _rolling_std(close, 20))
    return _rolling_mean(base, 126)

def bolp_056_bb_pctb_zscore_126d(close: pd.Series) -> pd.Series:
    """bolp_056_bb_pctb_zscore_126d"""
    base = _safe_div(close - (_rolling_mean(close, 20) - 2 * _rolling_std(close, 20)), 4 * _rolling_std(close, 20))
    return _zscore_rolling(base, 126)

def bolp_057_bb_pctb_rank_126d(close: pd.Series) -> pd.Series:
    """bolp_057_bb_pctb_rank_126d"""
    base = _safe_div(close - (_rolling_mean(close, 20) - 2 * _rolling_std(close, 20)), 4 * _rolling_std(close, 20))
    return _rank_pct(base, 126)

def bolp_058_bb_pctb_lvl_252d(close: pd.Series) -> pd.Series:
    """bolp_058_bb_pctb_lvl_252d"""
    base = _safe_div(close - (_rolling_mean(close, 20) - 2 * _rolling_std(close, 20)), 4 * _rolling_std(close, 20))
    return _rolling_mean(base, 252)

def bolp_059_bb_pctb_zscore_252d(close: pd.Series) -> pd.Series:
    """bolp_059_bb_pctb_zscore_252d"""
    base = _safe_div(close - (_rolling_mean(close, 20) - 2 * _rolling_std(close, 20)), 4 * _rolling_std(close, 20))
    return _zscore_rolling(base, 252)

def bolp_060_bb_pctb_rank_252d(close: pd.Series) -> pd.Series:
    """bolp_060_bb_pctb_rank_252d"""
    base = _safe_div(close - (_rolling_mean(close, 20) - 2 * _rolling_std(close, 20)), 4 * _rolling_std(close, 20))
    return _rank_pct(base, 252)

def bolp_061_bb_dist_u_lvl_5d(close: pd.Series) -> pd.Series:
    """bolp_061_bb_dist_u_lvl_5d"""
    base = _safe_div(close, _rolling_mean(close, 20) + 2 * _rolling_std(close, 20))
    return _rolling_mean(base, 5)

def bolp_062_bb_dist_u_zscore_5d(close: pd.Series) -> pd.Series:
    """bolp_062_bb_dist_u_zscore_5d"""
    base = _safe_div(close, _rolling_mean(close, 20) + 2 * _rolling_std(close, 20))
    return _zscore_rolling(base, 5)

def bolp_063_bb_dist_u_rank_5d(close: pd.Series) -> pd.Series:
    """bolp_063_bb_dist_u_rank_5d"""
    base = _safe_div(close, _rolling_mean(close, 20) + 2 * _rolling_std(close, 20))
    return _rank_pct(base, 5)

def bolp_064_bb_dist_u_lvl_21d(close: pd.Series) -> pd.Series:
    """bolp_064_bb_dist_u_lvl_21d"""
    base = _safe_div(close, _rolling_mean(close, 20) + 2 * _rolling_std(close, 20))
    return _rolling_mean(base, 21)

def bolp_065_bb_dist_u_zscore_21d(close: pd.Series) -> pd.Series:
    """bolp_065_bb_dist_u_zscore_21d"""
    base = _safe_div(close, _rolling_mean(close, 20) + 2 * _rolling_std(close, 20))
    return _zscore_rolling(base, 21)

def bolp_066_bb_dist_u_rank_21d(close: pd.Series) -> pd.Series:
    """bolp_066_bb_dist_u_rank_21d"""
    base = _safe_div(close, _rolling_mean(close, 20) + 2 * _rolling_std(close, 20))
    return _rank_pct(base, 21)

def bolp_067_bb_dist_u_lvl_63d(close: pd.Series) -> pd.Series:
    """bolp_067_bb_dist_u_lvl_63d"""
    base = _safe_div(close, _rolling_mean(close, 20) + 2 * _rolling_std(close, 20))
    return _rolling_mean(base, 63)

def bolp_068_bb_dist_u_zscore_63d(close: pd.Series) -> pd.Series:
    """bolp_068_bb_dist_u_zscore_63d"""
    base = _safe_div(close, _rolling_mean(close, 20) + 2 * _rolling_std(close, 20))
    return _zscore_rolling(base, 63)

def bolp_069_bb_dist_u_rank_63d(close: pd.Series) -> pd.Series:
    """bolp_069_bb_dist_u_rank_63d"""
    base = _safe_div(close, _rolling_mean(close, 20) + 2 * _rolling_std(close, 20))
    return _rank_pct(base, 63)

def bolp_070_bb_dist_u_lvl_126d(close: pd.Series) -> pd.Series:
    """bolp_070_bb_dist_u_lvl_126d"""
    base = _safe_div(close, _rolling_mean(close, 20) + 2 * _rolling_std(close, 20))
    return _rolling_mean(base, 126)

def bolp_071_bb_dist_u_zscore_126d(close: pd.Series) -> pd.Series:
    """bolp_071_bb_dist_u_zscore_126d"""
    base = _safe_div(close, _rolling_mean(close, 20) + 2 * _rolling_std(close, 20))
    return _zscore_rolling(base, 126)

def bolp_072_bb_dist_u_rank_126d(close: pd.Series) -> pd.Series:
    """bolp_072_bb_dist_u_rank_126d"""
    base = _safe_div(close, _rolling_mean(close, 20) + 2 * _rolling_std(close, 20))
    return _rank_pct(base, 126)

def bolp_073_bb_dist_u_lvl_252d(close: pd.Series) -> pd.Series:
    """bolp_073_bb_dist_u_lvl_252d"""
    base = _safe_div(close, _rolling_mean(close, 20) + 2 * _rolling_std(close, 20))
    return _rolling_mean(base, 252)

def bolp_074_bb_dist_u_zscore_252d(close: pd.Series) -> pd.Series:
    """bolp_074_bb_dist_u_zscore_252d"""
    base = _safe_div(close, _rolling_mean(close, 20) + 2 * _rolling_std(close, 20))
    return _zscore_rolling(base, 252)

def bolp_075_bb_dist_u_rank_252d(close: pd.Series) -> pd.Series:
    """bolp_075_bb_dist_u_rank_252d"""
    base = _safe_div(close, _rolling_mean(close, 20) + 2 * _rolling_std(close, 20))
    return _rank_pct(base, 252)

# ── Registry ──────────────────────────────────────────────────────────────────
V77_REGISTRY = {
    "bolp_001_bb_upper_lvl_5d": {"inputs": ["close"], "func": bolp_001_bb_upper_lvl_5d},
    "bolp_002_bb_upper_zscore_5d": {"inputs": ["close"], "func": bolp_002_bb_upper_zscore_5d},
    "bolp_003_bb_upper_rank_5d": {"inputs": ["close"], "func": bolp_003_bb_upper_rank_5d},
    "bolp_004_bb_upper_lvl_21d": {"inputs": ["close"], "func": bolp_004_bb_upper_lvl_21d},
    "bolp_005_bb_upper_zscore_21d": {"inputs": ["close"], "func": bolp_005_bb_upper_zscore_21d},
    "bolp_006_bb_upper_rank_21d": {"inputs": ["close"], "func": bolp_006_bb_upper_rank_21d},
    "bolp_007_bb_upper_lvl_63d": {"inputs": ["close"], "func": bolp_007_bb_upper_lvl_63d},
    "bolp_008_bb_upper_zscore_63d": {"inputs": ["close"], "func": bolp_008_bb_upper_zscore_63d},
    "bolp_009_bb_upper_rank_63d": {"inputs": ["close"], "func": bolp_009_bb_upper_rank_63d},
    "bolp_010_bb_upper_lvl_126d": {"inputs": ["close"], "func": bolp_010_bb_upper_lvl_126d},
    "bolp_011_bb_upper_zscore_126d": {"inputs": ["close"], "func": bolp_011_bb_upper_zscore_126d},
    "bolp_012_bb_upper_rank_126d": {"inputs": ["close"], "func": bolp_012_bb_upper_rank_126d},
    "bolp_013_bb_upper_lvl_252d": {"inputs": ["close"], "func": bolp_013_bb_upper_lvl_252d},
    "bolp_014_bb_upper_zscore_252d": {"inputs": ["close"], "func": bolp_014_bb_upper_zscore_252d},
    "bolp_015_bb_upper_rank_252d": {"inputs": ["close"], "func": bolp_015_bb_upper_rank_252d},
    "bolp_016_bb_lower_lvl_5d": {"inputs": ["close"], "func": bolp_016_bb_lower_lvl_5d},
    "bolp_017_bb_lower_zscore_5d": {"inputs": ["close"], "func": bolp_017_bb_lower_zscore_5d},
    "bolp_018_bb_lower_rank_5d": {"inputs": ["close"], "func": bolp_018_bb_lower_rank_5d},
    "bolp_019_bb_lower_lvl_21d": {"inputs": ["close"], "func": bolp_019_bb_lower_lvl_21d},
    "bolp_020_bb_lower_zscore_21d": {"inputs": ["close"], "func": bolp_020_bb_lower_zscore_21d},
    "bolp_021_bb_lower_rank_21d": {"inputs": ["close"], "func": bolp_021_bb_lower_rank_21d},
    "bolp_022_bb_lower_lvl_63d": {"inputs": ["close"], "func": bolp_022_bb_lower_lvl_63d},
    "bolp_023_bb_lower_zscore_63d": {"inputs": ["close"], "func": bolp_023_bb_lower_zscore_63d},
    "bolp_024_bb_lower_rank_63d": {"inputs": ["close"], "func": bolp_024_bb_lower_rank_63d},
    "bolp_025_bb_lower_lvl_126d": {"inputs": ["close"], "func": bolp_025_bb_lower_lvl_126d},
    "bolp_026_bb_lower_zscore_126d": {"inputs": ["close"], "func": bolp_026_bb_lower_zscore_126d},
    "bolp_027_bb_lower_rank_126d": {"inputs": ["close"], "func": bolp_027_bb_lower_rank_126d},
    "bolp_028_bb_lower_lvl_252d": {"inputs": ["close"], "func": bolp_028_bb_lower_lvl_252d},
    "bolp_029_bb_lower_zscore_252d": {"inputs": ["close"], "func": bolp_029_bb_lower_zscore_252d},
    "bolp_030_bb_lower_rank_252d": {"inputs": ["close"], "func": bolp_030_bb_lower_rank_252d},
    "bolp_031_bb_width_lvl_5d": {"inputs": ["close"], "func": bolp_031_bb_width_lvl_5d},
    "bolp_032_bb_width_zscore_5d": {"inputs": ["close"], "func": bolp_032_bb_width_zscore_5d},
    "bolp_033_bb_width_rank_5d": {"inputs": ["close"], "func": bolp_033_bb_width_rank_5d},
    "bolp_034_bb_width_lvl_21d": {"inputs": ["close"], "func": bolp_034_bb_width_lvl_21d},
    "bolp_035_bb_width_zscore_21d": {"inputs": ["close"], "func": bolp_035_bb_width_zscore_21d},
    "bolp_036_bb_width_rank_21d": {"inputs": ["close"], "func": bolp_036_bb_width_rank_21d},
    "bolp_037_bb_width_lvl_63d": {"inputs": ["close"], "func": bolp_037_bb_width_lvl_63d},
    "bolp_038_bb_width_zscore_63d": {"inputs": ["close"], "func": bolp_038_bb_width_zscore_63d},
    "bolp_039_bb_width_rank_63d": {"inputs": ["close"], "func": bolp_039_bb_width_rank_63d},
    "bolp_040_bb_width_lvl_126d": {"inputs": ["close"], "func": bolp_040_bb_width_lvl_126d},
    "bolp_041_bb_width_zscore_126d": {"inputs": ["close"], "func": bolp_041_bb_width_zscore_126d},
    "bolp_042_bb_width_rank_126d": {"inputs": ["close"], "func": bolp_042_bb_width_rank_126d},
    "bolp_043_bb_width_lvl_252d": {"inputs": ["close"], "func": bolp_043_bb_width_lvl_252d},
    "bolp_044_bb_width_zscore_252d": {"inputs": ["close"], "func": bolp_044_bb_width_zscore_252d},
    "bolp_045_bb_width_rank_252d": {"inputs": ["close"], "func": bolp_045_bb_width_rank_252d},
    "bolp_046_bb_pctb_lvl_5d": {"inputs": ["close"], "func": bolp_046_bb_pctb_lvl_5d},
    "bolp_047_bb_pctb_zscore_5d": {"inputs": ["close"], "func": bolp_047_bb_pctb_zscore_5d},
    "bolp_048_bb_pctb_rank_5d": {"inputs": ["close"], "func": bolp_048_bb_pctb_rank_5d},
    "bolp_049_bb_pctb_lvl_21d": {"inputs": ["close"], "func": bolp_049_bb_pctb_lvl_21d},
    "bolp_050_bb_pctb_zscore_21d": {"inputs": ["close"], "func": bolp_050_bb_pctb_zscore_21d},
    "bolp_051_bb_pctb_rank_21d": {"inputs": ["close"], "func": bolp_051_bb_pctb_rank_21d},
    "bolp_052_bb_pctb_lvl_63d": {"inputs": ["close"], "func": bolp_052_bb_pctb_lvl_63d},
    "bolp_053_bb_pctb_zscore_63d": {"inputs": ["close"], "func": bolp_053_bb_pctb_zscore_63d},
    "bolp_054_bb_pctb_rank_63d": {"inputs": ["close"], "func": bolp_054_bb_pctb_rank_63d},
    "bolp_055_bb_pctb_lvl_126d": {"inputs": ["close"], "func": bolp_055_bb_pctb_lvl_126d},
    "bolp_056_bb_pctb_zscore_126d": {"inputs": ["close"], "func": bolp_056_bb_pctb_zscore_126d},
    "bolp_057_bb_pctb_rank_126d": {"inputs": ["close"], "func": bolp_057_bb_pctb_rank_126d},
    "bolp_058_bb_pctb_lvl_252d": {"inputs": ["close"], "func": bolp_058_bb_pctb_lvl_252d},
    "bolp_059_bb_pctb_zscore_252d": {"inputs": ["close"], "func": bolp_059_bb_pctb_zscore_252d},
    "bolp_060_bb_pctb_rank_252d": {"inputs": ["close"], "func": bolp_060_bb_pctb_rank_252d},
    "bolp_061_bb_dist_u_lvl_5d": {"inputs": ["close"], "func": bolp_061_bb_dist_u_lvl_5d},
    "bolp_062_bb_dist_u_zscore_5d": {"inputs": ["close"], "func": bolp_062_bb_dist_u_zscore_5d},
    "bolp_063_bb_dist_u_rank_5d": {"inputs": ["close"], "func": bolp_063_bb_dist_u_rank_5d},
    "bolp_064_bb_dist_u_lvl_21d": {"inputs": ["close"], "func": bolp_064_bb_dist_u_lvl_21d},
    "bolp_065_bb_dist_u_zscore_21d": {"inputs": ["close"], "func": bolp_065_bb_dist_u_zscore_21d},
    "bolp_066_bb_dist_u_rank_21d": {"inputs": ["close"], "func": bolp_066_bb_dist_u_rank_21d},
    "bolp_067_bb_dist_u_lvl_63d": {"inputs": ["close"], "func": bolp_067_bb_dist_u_lvl_63d},
    "bolp_068_bb_dist_u_zscore_63d": {"inputs": ["close"], "func": bolp_068_bb_dist_u_zscore_63d},
    "bolp_069_bb_dist_u_rank_63d": {"inputs": ["close"], "func": bolp_069_bb_dist_u_rank_63d},
    "bolp_070_bb_dist_u_lvl_126d": {"inputs": ["close"], "func": bolp_070_bb_dist_u_lvl_126d},
    "bolp_071_bb_dist_u_zscore_126d": {"inputs": ["close"], "func": bolp_071_bb_dist_u_zscore_126d},
    "bolp_072_bb_dist_u_rank_126d": {"inputs": ["close"], "func": bolp_072_bb_dist_u_rank_126d},
    "bolp_073_bb_dist_u_lvl_252d": {"inputs": ["close"], "func": bolp_073_bb_dist_u_lvl_252d},
    "bolp_074_bb_dist_u_zscore_252d": {"inputs": ["close"], "func": bolp_074_bb_dist_u_zscore_252d},
    "bolp_075_bb_dist_u_rank_252d": {"inputs": ["close"], "func": bolp_075_bb_dist_u_rank_252d},
}
