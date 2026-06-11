"""
87_atrd_dynamics — Base Features 001-075
Domain: atrd_dynamics
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

def atrd_001_tr_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_001_tr_lvl_5d"""
    base = pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1)
    return _rolling_mean(base, 5)

def atrd_002_tr_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_002_tr_zscore_5d"""
    base = pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1)
    return _zscore_rolling(base, 5)

def atrd_003_tr_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_003_tr_rank_5d"""
    base = pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1)
    return _rank_pct(base, 5)

def atrd_004_tr_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_004_tr_lvl_21d"""
    base = pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1)
    return _rolling_mean(base, 21)

def atrd_005_tr_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_005_tr_zscore_21d"""
    base = pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1)
    return _zscore_rolling(base, 21)

def atrd_006_tr_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_006_tr_rank_21d"""
    base = pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1)
    return _rank_pct(base, 21)

def atrd_007_tr_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_007_tr_lvl_63d"""
    base = pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1)
    return _rolling_mean(base, 63)

def atrd_008_tr_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_008_tr_zscore_63d"""
    base = pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1)
    return _zscore_rolling(base, 63)

def atrd_009_tr_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_009_tr_rank_63d"""
    base = pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1)
    return _rank_pct(base, 63)

def atrd_010_tr_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_010_tr_lvl_126d"""
    base = pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1)
    return _rolling_mean(base, 126)

def atrd_011_tr_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_011_tr_zscore_126d"""
    base = pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1)
    return _zscore_rolling(base, 126)

def atrd_012_tr_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_012_tr_rank_126d"""
    base = pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1)
    return _rank_pct(base, 126)

def atrd_013_tr_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_013_tr_lvl_252d"""
    base = pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1)
    return _rolling_mean(base, 252)

def atrd_014_tr_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_014_tr_zscore_252d"""
    base = pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1)
    return _zscore_rolling(base, 252)

def atrd_015_tr_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_015_tr_rank_252d"""
    base = pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1)
    return _rank_pct(base, 252)

def atrd_016_atr_rat_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_016_atr_rat_lvl_5d"""
    base = _safe_div(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), close)
    return _rolling_mean(base, 5)

def atrd_017_atr_rat_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_017_atr_rat_zscore_5d"""
    base = _safe_div(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), close)
    return _zscore_rolling(base, 5)

def atrd_018_atr_rat_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_018_atr_rat_rank_5d"""
    base = _safe_div(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), close)
    return _rank_pct(base, 5)

def atrd_019_atr_rat_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_019_atr_rat_lvl_21d"""
    base = _safe_div(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), close)
    return _rolling_mean(base, 21)

def atrd_020_atr_rat_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_020_atr_rat_zscore_21d"""
    base = _safe_div(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), close)
    return _zscore_rolling(base, 21)

def atrd_021_atr_rat_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_021_atr_rat_rank_21d"""
    base = _safe_div(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), close)
    return _rank_pct(base, 21)

def atrd_022_atr_rat_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_022_atr_rat_lvl_63d"""
    base = _safe_div(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), close)
    return _rolling_mean(base, 63)

def atrd_023_atr_rat_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_023_atr_rat_zscore_63d"""
    base = _safe_div(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), close)
    return _zscore_rolling(base, 63)

def atrd_024_atr_rat_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_024_atr_rat_rank_63d"""
    base = _safe_div(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), close)
    return _rank_pct(base, 63)

def atrd_025_atr_rat_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_025_atr_rat_lvl_126d"""
    base = _safe_div(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), close)
    return _rolling_mean(base, 126)

def atrd_026_atr_rat_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_026_atr_rat_zscore_126d"""
    base = _safe_div(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), close)
    return _zscore_rolling(base, 126)

def atrd_027_atr_rat_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_027_atr_rat_rank_126d"""
    base = _safe_div(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), close)
    return _rank_pct(base, 126)

def atrd_028_atr_rat_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_028_atr_rat_lvl_252d"""
    base = _safe_div(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), close)
    return _rolling_mean(base, 252)

def atrd_029_atr_rat_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_029_atr_rat_zscore_252d"""
    base = _safe_div(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), close)
    return _zscore_rolling(base, 252)

def atrd_030_atr_rat_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_030_atr_rat_rank_252d"""
    base = _safe_div(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), close)
    return _rank_pct(base, 252)

def atrd_031_natr_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_031_natr_lvl_5d"""
    base = _safe_div(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), close) * 100
    return _rolling_mean(base, 5)

def atrd_032_natr_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_032_natr_zscore_5d"""
    base = _safe_div(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), close) * 100
    return _zscore_rolling(base, 5)

def atrd_033_natr_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_033_natr_rank_5d"""
    base = _safe_div(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), close) * 100
    return _rank_pct(base, 5)

def atrd_034_natr_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_034_natr_lvl_21d"""
    base = _safe_div(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), close) * 100
    return _rolling_mean(base, 21)

def atrd_035_natr_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_035_natr_zscore_21d"""
    base = _safe_div(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), close) * 100
    return _zscore_rolling(base, 21)

def atrd_036_natr_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_036_natr_rank_21d"""
    base = _safe_div(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), close) * 100
    return _rank_pct(base, 21)

def atrd_037_natr_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_037_natr_lvl_63d"""
    base = _safe_div(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), close) * 100
    return _rolling_mean(base, 63)

def atrd_038_natr_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_038_natr_zscore_63d"""
    base = _safe_div(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), close) * 100
    return _zscore_rolling(base, 63)

def atrd_039_natr_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_039_natr_rank_63d"""
    base = _safe_div(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), close) * 100
    return _rank_pct(base, 63)

def atrd_040_natr_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_040_natr_lvl_126d"""
    base = _safe_div(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), close) * 100
    return _rolling_mean(base, 126)

def atrd_041_natr_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_041_natr_zscore_126d"""
    base = _safe_div(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), close) * 100
    return _zscore_rolling(base, 126)

def atrd_042_natr_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_042_natr_rank_126d"""
    base = _safe_div(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), close) * 100
    return _rank_pct(base, 126)

def atrd_043_natr_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_043_natr_lvl_252d"""
    base = _safe_div(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), close) * 100
    return _rolling_mean(base, 252)

def atrd_044_natr_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_044_natr_zscore_252d"""
    base = _safe_div(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), close) * 100
    return _zscore_rolling(base, 252)

def atrd_045_natr_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_045_natr_rank_252d"""
    base = _safe_div(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), close) * 100
    return _rank_pct(base, 252)

def atrd_046_tr_vol_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_046_tr_vol_lvl_5d"""
    base = _safe_div(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), volume)
    return _rolling_mean(base, 5)

def atrd_047_tr_vol_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_047_tr_vol_zscore_5d"""
    base = _safe_div(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), volume)
    return _zscore_rolling(base, 5)

def atrd_048_tr_vol_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_048_tr_vol_rank_5d"""
    base = _safe_div(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), volume)
    return _rank_pct(base, 5)

def atrd_049_tr_vol_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_049_tr_vol_lvl_21d"""
    base = _safe_div(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), volume)
    return _rolling_mean(base, 21)

def atrd_050_tr_vol_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_050_tr_vol_zscore_21d"""
    base = _safe_div(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), volume)
    return _zscore_rolling(base, 21)

def atrd_051_tr_vol_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_051_tr_vol_rank_21d"""
    base = _safe_div(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), volume)
    return _rank_pct(base, 21)

def atrd_052_tr_vol_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_052_tr_vol_lvl_63d"""
    base = _safe_div(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), volume)
    return _rolling_mean(base, 63)

def atrd_053_tr_vol_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_053_tr_vol_zscore_63d"""
    base = _safe_div(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), volume)
    return _zscore_rolling(base, 63)

def atrd_054_tr_vol_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_054_tr_vol_rank_63d"""
    base = _safe_div(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), volume)
    return _rank_pct(base, 63)

def atrd_055_tr_vol_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_055_tr_vol_lvl_126d"""
    base = _safe_div(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), volume)
    return _rolling_mean(base, 126)

def atrd_056_tr_vol_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_056_tr_vol_zscore_126d"""
    base = _safe_div(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), volume)
    return _zscore_rolling(base, 126)

def atrd_057_tr_vol_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_057_tr_vol_rank_126d"""
    base = _safe_div(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), volume)
    return _rank_pct(base, 126)

def atrd_058_tr_vol_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_058_tr_vol_lvl_252d"""
    base = _safe_div(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), volume)
    return _rolling_mean(base, 252)

def atrd_059_tr_vol_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_059_tr_vol_zscore_252d"""
    base = _safe_div(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), volume)
    return _zscore_rolling(base, 252)

def atrd_060_tr_vol_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_060_tr_vol_rank_252d"""
    base = _safe_div(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1), volume)
    return _rank_pct(base, 252)

def atrd_061_tr_log_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_061_tr_log_lvl_5d"""
    base = np.log(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1).clip(lower=_EPS))
    return _rolling_mean(base, 5)

def atrd_062_tr_log_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_062_tr_log_zscore_5d"""
    base = np.log(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1).clip(lower=_EPS))
    return _zscore_rolling(base, 5)

def atrd_063_tr_log_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_063_tr_log_rank_5d"""
    base = np.log(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1).clip(lower=_EPS))
    return _rank_pct(base, 5)

def atrd_064_tr_log_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_064_tr_log_lvl_21d"""
    base = np.log(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1).clip(lower=_EPS))
    return _rolling_mean(base, 21)

def atrd_065_tr_log_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_065_tr_log_zscore_21d"""
    base = np.log(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1).clip(lower=_EPS))
    return _zscore_rolling(base, 21)

def atrd_066_tr_log_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_066_tr_log_rank_21d"""
    base = np.log(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1).clip(lower=_EPS))
    return _rank_pct(base, 21)

def atrd_067_tr_log_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_067_tr_log_lvl_63d"""
    base = np.log(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1).clip(lower=_EPS))
    return _rolling_mean(base, 63)

def atrd_068_tr_log_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_068_tr_log_zscore_63d"""
    base = np.log(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1).clip(lower=_EPS))
    return _zscore_rolling(base, 63)

def atrd_069_tr_log_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_069_tr_log_rank_63d"""
    base = np.log(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1).clip(lower=_EPS))
    return _rank_pct(base, 63)

def atrd_070_tr_log_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_070_tr_log_lvl_126d"""
    base = np.log(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1).clip(lower=_EPS))
    return _rolling_mean(base, 126)

def atrd_071_tr_log_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_071_tr_log_zscore_126d"""
    base = np.log(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1).clip(lower=_EPS))
    return _zscore_rolling(base, 126)

def atrd_072_tr_log_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_072_tr_log_rank_126d"""
    base = np.log(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1).clip(lower=_EPS))
    return _rank_pct(base, 126)

def atrd_073_tr_log_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_073_tr_log_lvl_252d"""
    base = np.log(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1).clip(lower=_EPS))
    return _rolling_mean(base, 252)

def atrd_074_tr_log_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_074_tr_log_zscore_252d"""
    base = np.log(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1).clip(lower=_EPS))
    return _zscore_rolling(base, 252)

def atrd_075_tr_log_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """atrd_075_tr_log_rank_252d"""
    base = np.log(pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1).clip(lower=_EPS))
    return _rank_pct(base, 252)

# ── Registry ──────────────────────────────────────────────────────────────────
V87_REGISTRY = {
    "atrd_001_tr_lvl_5d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_001_tr_lvl_5d},
    "atrd_002_tr_zscore_5d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_002_tr_zscore_5d},
    "atrd_003_tr_rank_5d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_003_tr_rank_5d},
    "atrd_004_tr_lvl_21d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_004_tr_lvl_21d},
    "atrd_005_tr_zscore_21d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_005_tr_zscore_21d},
    "atrd_006_tr_rank_21d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_006_tr_rank_21d},
    "atrd_007_tr_lvl_63d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_007_tr_lvl_63d},
    "atrd_008_tr_zscore_63d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_008_tr_zscore_63d},
    "atrd_009_tr_rank_63d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_009_tr_rank_63d},
    "atrd_010_tr_lvl_126d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_010_tr_lvl_126d},
    "atrd_011_tr_zscore_126d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_011_tr_zscore_126d},
    "atrd_012_tr_rank_126d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_012_tr_rank_126d},
    "atrd_013_tr_lvl_252d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_013_tr_lvl_252d},
    "atrd_014_tr_zscore_252d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_014_tr_zscore_252d},
    "atrd_015_tr_rank_252d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_015_tr_rank_252d},
    "atrd_016_atr_rat_lvl_5d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_016_atr_rat_lvl_5d},
    "atrd_017_atr_rat_zscore_5d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_017_atr_rat_zscore_5d},
    "atrd_018_atr_rat_rank_5d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_018_atr_rat_rank_5d},
    "atrd_019_atr_rat_lvl_21d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_019_atr_rat_lvl_21d},
    "atrd_020_atr_rat_zscore_21d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_020_atr_rat_zscore_21d},
    "atrd_021_atr_rat_rank_21d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_021_atr_rat_rank_21d},
    "atrd_022_atr_rat_lvl_63d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_022_atr_rat_lvl_63d},
    "atrd_023_atr_rat_zscore_63d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_023_atr_rat_zscore_63d},
    "atrd_024_atr_rat_rank_63d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_024_atr_rat_rank_63d},
    "atrd_025_atr_rat_lvl_126d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_025_atr_rat_lvl_126d},
    "atrd_026_atr_rat_zscore_126d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_026_atr_rat_zscore_126d},
    "atrd_027_atr_rat_rank_126d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_027_atr_rat_rank_126d},
    "atrd_028_atr_rat_lvl_252d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_028_atr_rat_lvl_252d},
    "atrd_029_atr_rat_zscore_252d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_029_atr_rat_zscore_252d},
    "atrd_030_atr_rat_rank_252d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_030_atr_rat_rank_252d},
    "atrd_031_natr_lvl_5d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_031_natr_lvl_5d},
    "atrd_032_natr_zscore_5d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_032_natr_zscore_5d},
    "atrd_033_natr_rank_5d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_033_natr_rank_5d},
    "atrd_034_natr_lvl_21d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_034_natr_lvl_21d},
    "atrd_035_natr_zscore_21d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_035_natr_zscore_21d},
    "atrd_036_natr_rank_21d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_036_natr_rank_21d},
    "atrd_037_natr_lvl_63d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_037_natr_lvl_63d},
    "atrd_038_natr_zscore_63d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_038_natr_zscore_63d},
    "atrd_039_natr_rank_63d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_039_natr_rank_63d},
    "atrd_040_natr_lvl_126d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_040_natr_lvl_126d},
    "atrd_041_natr_zscore_126d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_041_natr_zscore_126d},
    "atrd_042_natr_rank_126d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_042_natr_rank_126d},
    "atrd_043_natr_lvl_252d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_043_natr_lvl_252d},
    "atrd_044_natr_zscore_252d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_044_natr_zscore_252d},
    "atrd_045_natr_rank_252d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_045_natr_rank_252d},
    "atrd_046_tr_vol_lvl_5d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_046_tr_vol_lvl_5d},
    "atrd_047_tr_vol_zscore_5d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_047_tr_vol_zscore_5d},
    "atrd_048_tr_vol_rank_5d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_048_tr_vol_rank_5d},
    "atrd_049_tr_vol_lvl_21d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_049_tr_vol_lvl_21d},
    "atrd_050_tr_vol_zscore_21d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_050_tr_vol_zscore_21d},
    "atrd_051_tr_vol_rank_21d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_051_tr_vol_rank_21d},
    "atrd_052_tr_vol_lvl_63d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_052_tr_vol_lvl_63d},
    "atrd_053_tr_vol_zscore_63d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_053_tr_vol_zscore_63d},
    "atrd_054_tr_vol_rank_63d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_054_tr_vol_rank_63d},
    "atrd_055_tr_vol_lvl_126d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_055_tr_vol_lvl_126d},
    "atrd_056_tr_vol_zscore_126d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_056_tr_vol_zscore_126d},
    "atrd_057_tr_vol_rank_126d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_057_tr_vol_rank_126d},
    "atrd_058_tr_vol_lvl_252d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_058_tr_vol_lvl_252d},
    "atrd_059_tr_vol_zscore_252d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_059_tr_vol_zscore_252d},
    "atrd_060_tr_vol_rank_252d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_060_tr_vol_rank_252d},
    "atrd_061_tr_log_lvl_5d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_061_tr_log_lvl_5d},
    "atrd_062_tr_log_zscore_5d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_062_tr_log_zscore_5d},
    "atrd_063_tr_log_rank_5d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_063_tr_log_rank_5d},
    "atrd_064_tr_log_lvl_21d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_064_tr_log_lvl_21d},
    "atrd_065_tr_log_zscore_21d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_065_tr_log_zscore_21d},
    "atrd_066_tr_log_rank_21d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_066_tr_log_rank_21d},
    "atrd_067_tr_log_lvl_63d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_067_tr_log_lvl_63d},
    "atrd_068_tr_log_zscore_63d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_068_tr_log_zscore_63d},
    "atrd_069_tr_log_rank_63d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_069_tr_log_rank_63d},
    "atrd_070_tr_log_lvl_126d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_070_tr_log_lvl_126d},
    "atrd_071_tr_log_zscore_126d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_071_tr_log_zscore_126d},
    "atrd_072_tr_log_rank_126d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_072_tr_log_rank_126d},
    "atrd_073_tr_log_lvl_252d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_073_tr_log_lvl_252d},
    "atrd_074_tr_log_zscore_252d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_074_tr_log_zscore_252d},
    "atrd_075_tr_log_rank_252d": {"inputs": ["high", "low", "close", "volume"], "func": atrd_075_tr_log_rank_252d},
}
