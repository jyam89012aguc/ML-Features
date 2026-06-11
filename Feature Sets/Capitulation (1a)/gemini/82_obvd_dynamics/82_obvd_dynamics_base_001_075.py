"""
82_obvd_dynamics — Base Features 001-075
Domain: obvd_dynamics
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

def obvd_001_obv_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_001_obv_lvl_5d"""
    base = (volume * np.sign(close.diff()).fillna(0)).cumsum()
    return _rolling_mean(base, 5)

def obvd_002_obv_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_002_obv_zscore_5d"""
    base = (volume * np.sign(close.diff()).fillna(0)).cumsum()
    return _zscore_rolling(base, 5)

def obvd_003_obv_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_003_obv_rank_5d"""
    base = (volume * np.sign(close.diff()).fillna(0)).cumsum()
    return _rank_pct(base, 5)

def obvd_004_obv_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_004_obv_lvl_21d"""
    base = (volume * np.sign(close.diff()).fillna(0)).cumsum()
    return _rolling_mean(base, 21)

def obvd_005_obv_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_005_obv_zscore_21d"""
    base = (volume * np.sign(close.diff()).fillna(0)).cumsum()
    return _zscore_rolling(base, 21)

def obvd_006_obv_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_006_obv_rank_21d"""
    base = (volume * np.sign(close.diff()).fillna(0)).cumsum()
    return _rank_pct(base, 21)

def obvd_007_obv_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_007_obv_lvl_63d"""
    base = (volume * np.sign(close.diff()).fillna(0)).cumsum()
    return _rolling_mean(base, 63)

def obvd_008_obv_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_008_obv_zscore_63d"""
    base = (volume * np.sign(close.diff()).fillna(0)).cumsum()
    return _zscore_rolling(base, 63)

def obvd_009_obv_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_009_obv_rank_63d"""
    base = (volume * np.sign(close.diff()).fillna(0)).cumsum()
    return _rank_pct(base, 63)

def obvd_010_obv_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_010_obv_lvl_126d"""
    base = (volume * np.sign(close.diff()).fillna(0)).cumsum()
    return _rolling_mean(base, 126)

def obvd_011_obv_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_011_obv_zscore_126d"""
    base = (volume * np.sign(close.diff()).fillna(0)).cumsum()
    return _zscore_rolling(base, 126)

def obvd_012_obv_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_012_obv_rank_126d"""
    base = (volume * np.sign(close.diff()).fillna(0)).cumsum()
    return _rank_pct(base, 126)

def obvd_013_obv_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_013_obv_lvl_252d"""
    base = (volume * np.sign(close.diff()).fillna(0)).cumsum()
    return _rolling_mean(base, 252)

def obvd_014_obv_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_014_obv_zscore_252d"""
    base = (volume * np.sign(close.diff()).fillna(0)).cumsum()
    return _zscore_rolling(base, 252)

def obvd_015_obv_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_015_obv_rank_252d"""
    base = (volume * np.sign(close.diff()).fillna(0)).cumsum()
    return _rank_pct(base, 252)

def obvd_016_obv_sma_rat_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_016_obv_sma_rat_lvl_5d"""
    base = _safe_div((volume * np.sign(close.diff()).fillna(0)).cumsum(), _rolling_mean((volume * np.sign(close.diff()).fillna(0)).cumsum(), 20))
    return _rolling_mean(base, 5)

def obvd_017_obv_sma_rat_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_017_obv_sma_rat_zscore_5d"""
    base = _safe_div((volume * np.sign(close.diff()).fillna(0)).cumsum(), _rolling_mean((volume * np.sign(close.diff()).fillna(0)).cumsum(), 20))
    return _zscore_rolling(base, 5)

def obvd_018_obv_sma_rat_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_018_obv_sma_rat_rank_5d"""
    base = _safe_div((volume * np.sign(close.diff()).fillna(0)).cumsum(), _rolling_mean((volume * np.sign(close.diff()).fillna(0)).cumsum(), 20))
    return _rank_pct(base, 5)

def obvd_019_obv_sma_rat_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_019_obv_sma_rat_lvl_21d"""
    base = _safe_div((volume * np.sign(close.diff()).fillna(0)).cumsum(), _rolling_mean((volume * np.sign(close.diff()).fillna(0)).cumsum(), 20))
    return _rolling_mean(base, 21)

def obvd_020_obv_sma_rat_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_020_obv_sma_rat_zscore_21d"""
    base = _safe_div((volume * np.sign(close.diff()).fillna(0)).cumsum(), _rolling_mean((volume * np.sign(close.diff()).fillna(0)).cumsum(), 20))
    return _zscore_rolling(base, 21)

def obvd_021_obv_sma_rat_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_021_obv_sma_rat_rank_21d"""
    base = _safe_div((volume * np.sign(close.diff()).fillna(0)).cumsum(), _rolling_mean((volume * np.sign(close.diff()).fillna(0)).cumsum(), 20))
    return _rank_pct(base, 21)

def obvd_022_obv_sma_rat_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_022_obv_sma_rat_lvl_63d"""
    base = _safe_div((volume * np.sign(close.diff()).fillna(0)).cumsum(), _rolling_mean((volume * np.sign(close.diff()).fillna(0)).cumsum(), 20))
    return _rolling_mean(base, 63)

def obvd_023_obv_sma_rat_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_023_obv_sma_rat_zscore_63d"""
    base = _safe_div((volume * np.sign(close.diff()).fillna(0)).cumsum(), _rolling_mean((volume * np.sign(close.diff()).fillna(0)).cumsum(), 20))
    return _zscore_rolling(base, 63)

def obvd_024_obv_sma_rat_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_024_obv_sma_rat_rank_63d"""
    base = _safe_div((volume * np.sign(close.diff()).fillna(0)).cumsum(), _rolling_mean((volume * np.sign(close.diff()).fillna(0)).cumsum(), 20))
    return _rank_pct(base, 63)

def obvd_025_obv_sma_rat_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_025_obv_sma_rat_lvl_126d"""
    base = _safe_div((volume * np.sign(close.diff()).fillna(0)).cumsum(), _rolling_mean((volume * np.sign(close.diff()).fillna(0)).cumsum(), 20))
    return _rolling_mean(base, 126)

def obvd_026_obv_sma_rat_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_026_obv_sma_rat_zscore_126d"""
    base = _safe_div((volume * np.sign(close.diff()).fillna(0)).cumsum(), _rolling_mean((volume * np.sign(close.diff()).fillna(0)).cumsum(), 20))
    return _zscore_rolling(base, 126)

def obvd_027_obv_sma_rat_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_027_obv_sma_rat_rank_126d"""
    base = _safe_div((volume * np.sign(close.diff()).fillna(0)).cumsum(), _rolling_mean((volume * np.sign(close.diff()).fillna(0)).cumsum(), 20))
    return _rank_pct(base, 126)

def obvd_028_obv_sma_rat_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_028_obv_sma_rat_lvl_252d"""
    base = _safe_div((volume * np.sign(close.diff()).fillna(0)).cumsum(), _rolling_mean((volume * np.sign(close.diff()).fillna(0)).cumsum(), 20))
    return _rolling_mean(base, 252)

def obvd_029_obv_sma_rat_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_029_obv_sma_rat_zscore_252d"""
    base = _safe_div((volume * np.sign(close.diff()).fillna(0)).cumsum(), _rolling_mean((volume * np.sign(close.diff()).fillna(0)).cumsum(), 20))
    return _zscore_rolling(base, 252)

def obvd_030_obv_sma_rat_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_030_obv_sma_rat_rank_252d"""
    base = _safe_div((volume * np.sign(close.diff()).fillna(0)).cumsum(), _rolling_mean((volume * np.sign(close.diff()).fillna(0)).cumsum(), 20))
    return _rank_pct(base, 252)

def obvd_031_obv_z_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_031_obv_z_lvl_5d"""
    base = _zscore_rolling((volume * np.sign(close.diff()).fillna(0)).cumsum(), 63)
    return _rolling_mean(base, 5)

def obvd_032_obv_z_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_032_obv_z_zscore_5d"""
    base = _zscore_rolling((volume * np.sign(close.diff()).fillna(0)).cumsum(), 63)
    return _zscore_rolling(base, 5)

def obvd_033_obv_z_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_033_obv_z_rank_5d"""
    base = _zscore_rolling((volume * np.sign(close.diff()).fillna(0)).cumsum(), 63)
    return _rank_pct(base, 5)

def obvd_034_obv_z_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_034_obv_z_lvl_21d"""
    base = _zscore_rolling((volume * np.sign(close.diff()).fillna(0)).cumsum(), 63)
    return _rolling_mean(base, 21)

def obvd_035_obv_z_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_035_obv_z_zscore_21d"""
    base = _zscore_rolling((volume * np.sign(close.diff()).fillna(0)).cumsum(), 63)
    return _zscore_rolling(base, 21)

def obvd_036_obv_z_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_036_obv_z_rank_21d"""
    base = _zscore_rolling((volume * np.sign(close.diff()).fillna(0)).cumsum(), 63)
    return _rank_pct(base, 21)

def obvd_037_obv_z_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_037_obv_z_lvl_63d"""
    base = _zscore_rolling((volume * np.sign(close.diff()).fillna(0)).cumsum(), 63)
    return _rolling_mean(base, 63)

def obvd_038_obv_z_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_038_obv_z_zscore_63d"""
    base = _zscore_rolling((volume * np.sign(close.diff()).fillna(0)).cumsum(), 63)
    return _zscore_rolling(base, 63)

def obvd_039_obv_z_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_039_obv_z_rank_63d"""
    base = _zscore_rolling((volume * np.sign(close.diff()).fillna(0)).cumsum(), 63)
    return _rank_pct(base, 63)

def obvd_040_obv_z_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_040_obv_z_lvl_126d"""
    base = _zscore_rolling((volume * np.sign(close.diff()).fillna(0)).cumsum(), 63)
    return _rolling_mean(base, 126)

def obvd_041_obv_z_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_041_obv_z_zscore_126d"""
    base = _zscore_rolling((volume * np.sign(close.diff()).fillna(0)).cumsum(), 63)
    return _zscore_rolling(base, 126)

def obvd_042_obv_z_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_042_obv_z_rank_126d"""
    base = _zscore_rolling((volume * np.sign(close.diff()).fillna(0)).cumsum(), 63)
    return _rank_pct(base, 126)

def obvd_043_obv_z_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_043_obv_z_lvl_252d"""
    base = _zscore_rolling((volume * np.sign(close.diff()).fillna(0)).cumsum(), 63)
    return _rolling_mean(base, 252)

def obvd_044_obv_z_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_044_obv_z_zscore_252d"""
    base = _zscore_rolling((volume * np.sign(close.diff()).fillna(0)).cumsum(), 63)
    return _zscore_rolling(base, 252)

def obvd_045_obv_z_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_045_obv_z_rank_252d"""
    base = _zscore_rolling((volume * np.sign(close.diff()).fillna(0)).cumsum(), 63)
    return _rank_pct(base, 252)

def obvd_046_obv_slope_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_046_obv_slope_lvl_5d"""
    base = (volume * np.sign(close.diff()).fillna(0)).cumsum().diff(5)
    return _rolling_mean(base, 5)

def obvd_047_obv_slope_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_047_obv_slope_zscore_5d"""
    base = (volume * np.sign(close.diff()).fillna(0)).cumsum().diff(5)
    return _zscore_rolling(base, 5)

def obvd_048_obv_slope_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_048_obv_slope_rank_5d"""
    base = (volume * np.sign(close.diff()).fillna(0)).cumsum().diff(5)
    return _rank_pct(base, 5)

def obvd_049_obv_slope_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_049_obv_slope_lvl_21d"""
    base = (volume * np.sign(close.diff()).fillna(0)).cumsum().diff(5)
    return _rolling_mean(base, 21)

def obvd_050_obv_slope_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_050_obv_slope_zscore_21d"""
    base = (volume * np.sign(close.diff()).fillna(0)).cumsum().diff(5)
    return _zscore_rolling(base, 21)

def obvd_051_obv_slope_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_051_obv_slope_rank_21d"""
    base = (volume * np.sign(close.diff()).fillna(0)).cumsum().diff(5)
    return _rank_pct(base, 21)

def obvd_052_obv_slope_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_052_obv_slope_lvl_63d"""
    base = (volume * np.sign(close.diff()).fillna(0)).cumsum().diff(5)
    return _rolling_mean(base, 63)

def obvd_053_obv_slope_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_053_obv_slope_zscore_63d"""
    base = (volume * np.sign(close.diff()).fillna(0)).cumsum().diff(5)
    return _zscore_rolling(base, 63)

def obvd_054_obv_slope_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_054_obv_slope_rank_63d"""
    base = (volume * np.sign(close.diff()).fillna(0)).cumsum().diff(5)
    return _rank_pct(base, 63)

def obvd_055_obv_slope_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_055_obv_slope_lvl_126d"""
    base = (volume * np.sign(close.diff()).fillna(0)).cumsum().diff(5)
    return _rolling_mean(base, 126)

def obvd_056_obv_slope_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_056_obv_slope_zscore_126d"""
    base = (volume * np.sign(close.diff()).fillna(0)).cumsum().diff(5)
    return _zscore_rolling(base, 126)

def obvd_057_obv_slope_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_057_obv_slope_rank_126d"""
    base = (volume * np.sign(close.diff()).fillna(0)).cumsum().diff(5)
    return _rank_pct(base, 126)

def obvd_058_obv_slope_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_058_obv_slope_lvl_252d"""
    base = (volume * np.sign(close.diff()).fillna(0)).cumsum().diff(5)
    return _rolling_mean(base, 252)

def obvd_059_obv_slope_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_059_obv_slope_zscore_252d"""
    base = (volume * np.sign(close.diff()).fillna(0)).cumsum().diff(5)
    return _zscore_rolling(base, 252)

def obvd_060_obv_slope_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_060_obv_slope_rank_252d"""
    base = (volume * np.sign(close.diff()).fillna(0)).cumsum().diff(5)
    return _rank_pct(base, 252)

def obvd_061_obv_vol_rat_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_061_obv_vol_rat_lvl_5d"""
    base = _safe_div(volume, _rolling_mean(volume, 20))
    return _rolling_mean(base, 5)

def obvd_062_obv_vol_rat_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_062_obv_vol_rat_zscore_5d"""
    base = _safe_div(volume, _rolling_mean(volume, 20))
    return _zscore_rolling(base, 5)

def obvd_063_obv_vol_rat_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_063_obv_vol_rat_rank_5d"""
    base = _safe_div(volume, _rolling_mean(volume, 20))
    return _rank_pct(base, 5)

def obvd_064_obv_vol_rat_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_064_obv_vol_rat_lvl_21d"""
    base = _safe_div(volume, _rolling_mean(volume, 20))
    return _rolling_mean(base, 21)

def obvd_065_obv_vol_rat_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_065_obv_vol_rat_zscore_21d"""
    base = _safe_div(volume, _rolling_mean(volume, 20))
    return _zscore_rolling(base, 21)

def obvd_066_obv_vol_rat_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_066_obv_vol_rat_rank_21d"""
    base = _safe_div(volume, _rolling_mean(volume, 20))
    return _rank_pct(base, 21)

def obvd_067_obv_vol_rat_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_067_obv_vol_rat_lvl_63d"""
    base = _safe_div(volume, _rolling_mean(volume, 20))
    return _rolling_mean(base, 63)

def obvd_068_obv_vol_rat_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_068_obv_vol_rat_zscore_63d"""
    base = _safe_div(volume, _rolling_mean(volume, 20))
    return _zscore_rolling(base, 63)

def obvd_069_obv_vol_rat_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_069_obv_vol_rat_rank_63d"""
    base = _safe_div(volume, _rolling_mean(volume, 20))
    return _rank_pct(base, 63)

def obvd_070_obv_vol_rat_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_070_obv_vol_rat_lvl_126d"""
    base = _safe_div(volume, _rolling_mean(volume, 20))
    return _rolling_mean(base, 126)

def obvd_071_obv_vol_rat_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_071_obv_vol_rat_zscore_126d"""
    base = _safe_div(volume, _rolling_mean(volume, 20))
    return _zscore_rolling(base, 126)

def obvd_072_obv_vol_rat_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_072_obv_vol_rat_rank_126d"""
    base = _safe_div(volume, _rolling_mean(volume, 20))
    return _rank_pct(base, 126)

def obvd_073_obv_vol_rat_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_073_obv_vol_rat_lvl_252d"""
    base = _safe_div(volume, _rolling_mean(volume, 20))
    return _rolling_mean(base, 252)

def obvd_074_obv_vol_rat_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_074_obv_vol_rat_zscore_252d"""
    base = _safe_div(volume, _rolling_mean(volume, 20))
    return _zscore_rolling(base, 252)

def obvd_075_obv_vol_rat_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """obvd_075_obv_vol_rat_rank_252d"""
    base = _safe_div(volume, _rolling_mean(volume, 20))
    return _rank_pct(base, 252)

# ── Registry ──────────────────────────────────────────────────────────────────
V82_REGISTRY = {
    "obvd_001_obv_lvl_5d": {"inputs": ["close", "volume"], "func": obvd_001_obv_lvl_5d},
    "obvd_002_obv_zscore_5d": {"inputs": ["close", "volume"], "func": obvd_002_obv_zscore_5d},
    "obvd_003_obv_rank_5d": {"inputs": ["close", "volume"], "func": obvd_003_obv_rank_5d},
    "obvd_004_obv_lvl_21d": {"inputs": ["close", "volume"], "func": obvd_004_obv_lvl_21d},
    "obvd_005_obv_zscore_21d": {"inputs": ["close", "volume"], "func": obvd_005_obv_zscore_21d},
    "obvd_006_obv_rank_21d": {"inputs": ["close", "volume"], "func": obvd_006_obv_rank_21d},
    "obvd_007_obv_lvl_63d": {"inputs": ["close", "volume"], "func": obvd_007_obv_lvl_63d},
    "obvd_008_obv_zscore_63d": {"inputs": ["close", "volume"], "func": obvd_008_obv_zscore_63d},
    "obvd_009_obv_rank_63d": {"inputs": ["close", "volume"], "func": obvd_009_obv_rank_63d},
    "obvd_010_obv_lvl_126d": {"inputs": ["close", "volume"], "func": obvd_010_obv_lvl_126d},
    "obvd_011_obv_zscore_126d": {"inputs": ["close", "volume"], "func": obvd_011_obv_zscore_126d},
    "obvd_012_obv_rank_126d": {"inputs": ["close", "volume"], "func": obvd_012_obv_rank_126d},
    "obvd_013_obv_lvl_252d": {"inputs": ["close", "volume"], "func": obvd_013_obv_lvl_252d},
    "obvd_014_obv_zscore_252d": {"inputs": ["close", "volume"], "func": obvd_014_obv_zscore_252d},
    "obvd_015_obv_rank_252d": {"inputs": ["close", "volume"], "func": obvd_015_obv_rank_252d},
    "obvd_016_obv_sma_rat_lvl_5d": {"inputs": ["close", "volume"], "func": obvd_016_obv_sma_rat_lvl_5d},
    "obvd_017_obv_sma_rat_zscore_5d": {"inputs": ["close", "volume"], "func": obvd_017_obv_sma_rat_zscore_5d},
    "obvd_018_obv_sma_rat_rank_5d": {"inputs": ["close", "volume"], "func": obvd_018_obv_sma_rat_rank_5d},
    "obvd_019_obv_sma_rat_lvl_21d": {"inputs": ["close", "volume"], "func": obvd_019_obv_sma_rat_lvl_21d},
    "obvd_020_obv_sma_rat_zscore_21d": {"inputs": ["close", "volume"], "func": obvd_020_obv_sma_rat_zscore_21d},
    "obvd_021_obv_sma_rat_rank_21d": {"inputs": ["close", "volume"], "func": obvd_021_obv_sma_rat_rank_21d},
    "obvd_022_obv_sma_rat_lvl_63d": {"inputs": ["close", "volume"], "func": obvd_022_obv_sma_rat_lvl_63d},
    "obvd_023_obv_sma_rat_zscore_63d": {"inputs": ["close", "volume"], "func": obvd_023_obv_sma_rat_zscore_63d},
    "obvd_024_obv_sma_rat_rank_63d": {"inputs": ["close", "volume"], "func": obvd_024_obv_sma_rat_rank_63d},
    "obvd_025_obv_sma_rat_lvl_126d": {"inputs": ["close", "volume"], "func": obvd_025_obv_sma_rat_lvl_126d},
    "obvd_026_obv_sma_rat_zscore_126d": {"inputs": ["close", "volume"], "func": obvd_026_obv_sma_rat_zscore_126d},
    "obvd_027_obv_sma_rat_rank_126d": {"inputs": ["close", "volume"], "func": obvd_027_obv_sma_rat_rank_126d},
    "obvd_028_obv_sma_rat_lvl_252d": {"inputs": ["close", "volume"], "func": obvd_028_obv_sma_rat_lvl_252d},
    "obvd_029_obv_sma_rat_zscore_252d": {"inputs": ["close", "volume"], "func": obvd_029_obv_sma_rat_zscore_252d},
    "obvd_030_obv_sma_rat_rank_252d": {"inputs": ["close", "volume"], "func": obvd_030_obv_sma_rat_rank_252d},
    "obvd_031_obv_z_lvl_5d": {"inputs": ["close", "volume"], "func": obvd_031_obv_z_lvl_5d},
    "obvd_032_obv_z_zscore_5d": {"inputs": ["close", "volume"], "func": obvd_032_obv_z_zscore_5d},
    "obvd_033_obv_z_rank_5d": {"inputs": ["close", "volume"], "func": obvd_033_obv_z_rank_5d},
    "obvd_034_obv_z_lvl_21d": {"inputs": ["close", "volume"], "func": obvd_034_obv_z_lvl_21d},
    "obvd_035_obv_z_zscore_21d": {"inputs": ["close", "volume"], "func": obvd_035_obv_z_zscore_21d},
    "obvd_036_obv_z_rank_21d": {"inputs": ["close", "volume"], "func": obvd_036_obv_z_rank_21d},
    "obvd_037_obv_z_lvl_63d": {"inputs": ["close", "volume"], "func": obvd_037_obv_z_lvl_63d},
    "obvd_038_obv_z_zscore_63d": {"inputs": ["close", "volume"], "func": obvd_038_obv_z_zscore_63d},
    "obvd_039_obv_z_rank_63d": {"inputs": ["close", "volume"], "func": obvd_039_obv_z_rank_63d},
    "obvd_040_obv_z_lvl_126d": {"inputs": ["close", "volume"], "func": obvd_040_obv_z_lvl_126d},
    "obvd_041_obv_z_zscore_126d": {"inputs": ["close", "volume"], "func": obvd_041_obv_z_zscore_126d},
    "obvd_042_obv_z_rank_126d": {"inputs": ["close", "volume"], "func": obvd_042_obv_z_rank_126d},
    "obvd_043_obv_z_lvl_252d": {"inputs": ["close", "volume"], "func": obvd_043_obv_z_lvl_252d},
    "obvd_044_obv_z_zscore_252d": {"inputs": ["close", "volume"], "func": obvd_044_obv_z_zscore_252d},
    "obvd_045_obv_z_rank_252d": {"inputs": ["close", "volume"], "func": obvd_045_obv_z_rank_252d},
    "obvd_046_obv_slope_lvl_5d": {"inputs": ["close", "volume"], "func": obvd_046_obv_slope_lvl_5d},
    "obvd_047_obv_slope_zscore_5d": {"inputs": ["close", "volume"], "func": obvd_047_obv_slope_zscore_5d},
    "obvd_048_obv_slope_rank_5d": {"inputs": ["close", "volume"], "func": obvd_048_obv_slope_rank_5d},
    "obvd_049_obv_slope_lvl_21d": {"inputs": ["close", "volume"], "func": obvd_049_obv_slope_lvl_21d},
    "obvd_050_obv_slope_zscore_21d": {"inputs": ["close", "volume"], "func": obvd_050_obv_slope_zscore_21d},
    "obvd_051_obv_slope_rank_21d": {"inputs": ["close", "volume"], "func": obvd_051_obv_slope_rank_21d},
    "obvd_052_obv_slope_lvl_63d": {"inputs": ["close", "volume"], "func": obvd_052_obv_slope_lvl_63d},
    "obvd_053_obv_slope_zscore_63d": {"inputs": ["close", "volume"], "func": obvd_053_obv_slope_zscore_63d},
    "obvd_054_obv_slope_rank_63d": {"inputs": ["close", "volume"], "func": obvd_054_obv_slope_rank_63d},
    "obvd_055_obv_slope_lvl_126d": {"inputs": ["close", "volume"], "func": obvd_055_obv_slope_lvl_126d},
    "obvd_056_obv_slope_zscore_126d": {"inputs": ["close", "volume"], "func": obvd_056_obv_slope_zscore_126d},
    "obvd_057_obv_slope_rank_126d": {"inputs": ["close", "volume"], "func": obvd_057_obv_slope_rank_126d},
    "obvd_058_obv_slope_lvl_252d": {"inputs": ["close", "volume"], "func": obvd_058_obv_slope_lvl_252d},
    "obvd_059_obv_slope_zscore_252d": {"inputs": ["close", "volume"], "func": obvd_059_obv_slope_zscore_252d},
    "obvd_060_obv_slope_rank_252d": {"inputs": ["close", "volume"], "func": obvd_060_obv_slope_rank_252d},
    "obvd_061_obv_vol_rat_lvl_5d": {"inputs": ["close", "volume"], "func": obvd_061_obv_vol_rat_lvl_5d},
    "obvd_062_obv_vol_rat_zscore_5d": {"inputs": ["close", "volume"], "func": obvd_062_obv_vol_rat_zscore_5d},
    "obvd_063_obv_vol_rat_rank_5d": {"inputs": ["close", "volume"], "func": obvd_063_obv_vol_rat_rank_5d},
    "obvd_064_obv_vol_rat_lvl_21d": {"inputs": ["close", "volume"], "func": obvd_064_obv_vol_rat_lvl_21d},
    "obvd_065_obv_vol_rat_zscore_21d": {"inputs": ["close", "volume"], "func": obvd_065_obv_vol_rat_zscore_21d},
    "obvd_066_obv_vol_rat_rank_21d": {"inputs": ["close", "volume"], "func": obvd_066_obv_vol_rat_rank_21d},
    "obvd_067_obv_vol_rat_lvl_63d": {"inputs": ["close", "volume"], "func": obvd_067_obv_vol_rat_lvl_63d},
    "obvd_068_obv_vol_rat_zscore_63d": {"inputs": ["close", "volume"], "func": obvd_068_obv_vol_rat_zscore_63d},
    "obvd_069_obv_vol_rat_rank_63d": {"inputs": ["close", "volume"], "func": obvd_069_obv_vol_rat_rank_63d},
    "obvd_070_obv_vol_rat_lvl_126d": {"inputs": ["close", "volume"], "func": obvd_070_obv_vol_rat_lvl_126d},
    "obvd_071_obv_vol_rat_zscore_126d": {"inputs": ["close", "volume"], "func": obvd_071_obv_vol_rat_zscore_126d},
    "obvd_072_obv_vol_rat_rank_126d": {"inputs": ["close", "volume"], "func": obvd_072_obv_vol_rat_rank_126d},
    "obvd_073_obv_vol_rat_lvl_252d": {"inputs": ["close", "volume"], "func": obvd_073_obv_vol_rat_lvl_252d},
    "obvd_074_obv_vol_rat_zscore_252d": {"inputs": ["close", "volume"], "func": obvd_074_obv_vol_rat_zscore_252d},
    "obvd_075_obv_vol_rat_rank_252d": {"inputs": ["close", "volume"], "func": obvd_075_obv_vol_rat_rank_252d},
}
