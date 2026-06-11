"""
83_cmfd_dynamics — Base Features 001-075
Domain: cmfd_dynamics
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

def cmfd_001_mf_mult_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_001_mf_mult_lvl_5d"""
    base = _safe_div((close - low) - (high - close), high - low)
    return _rolling_mean(base, 5)

def cmfd_002_mf_mult_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_002_mf_mult_zscore_5d"""
    base = _safe_div((close - low) - (high - close), high - low)
    return _zscore_rolling(base, 5)

def cmfd_003_mf_mult_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_003_mf_mult_rank_5d"""
    base = _safe_div((close - low) - (high - close), high - low)
    return _rank_pct(base, 5)

def cmfd_004_mf_mult_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_004_mf_mult_lvl_21d"""
    base = _safe_div((close - low) - (high - close), high - low)
    return _rolling_mean(base, 21)

def cmfd_005_mf_mult_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_005_mf_mult_zscore_21d"""
    base = _safe_div((close - low) - (high - close), high - low)
    return _zscore_rolling(base, 21)

def cmfd_006_mf_mult_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_006_mf_mult_rank_21d"""
    base = _safe_div((close - low) - (high - close), high - low)
    return _rank_pct(base, 21)

def cmfd_007_mf_mult_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_007_mf_mult_lvl_63d"""
    base = _safe_div((close - low) - (high - close), high - low)
    return _rolling_mean(base, 63)

def cmfd_008_mf_mult_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_008_mf_mult_zscore_63d"""
    base = _safe_div((close - low) - (high - close), high - low)
    return _zscore_rolling(base, 63)

def cmfd_009_mf_mult_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_009_mf_mult_rank_63d"""
    base = _safe_div((close - low) - (high - close), high - low)
    return _rank_pct(base, 63)

def cmfd_010_mf_mult_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_010_mf_mult_lvl_126d"""
    base = _safe_div((close - low) - (high - close), high - low)
    return _rolling_mean(base, 126)

def cmfd_011_mf_mult_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_011_mf_mult_zscore_126d"""
    base = _safe_div((close - low) - (high - close), high - low)
    return _zscore_rolling(base, 126)

def cmfd_012_mf_mult_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_012_mf_mult_rank_126d"""
    base = _safe_div((close - low) - (high - close), high - low)
    return _rank_pct(base, 126)

def cmfd_013_mf_mult_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_013_mf_mult_lvl_252d"""
    base = _safe_div((close - low) - (high - close), high - low)
    return _rolling_mean(base, 252)

def cmfd_014_mf_mult_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_014_mf_mult_zscore_252d"""
    base = _safe_div((close - low) - (high - close), high - low)
    return _zscore_rolling(base, 252)

def cmfd_015_mf_mult_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_015_mf_mult_rank_252d"""
    base = _safe_div((close - low) - (high - close), high - low)
    return _rank_pct(base, 252)

def cmfd_016_mf_vol_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_016_mf_vol_lvl_5d"""
    base = _safe_div((close - low) - (high - close), high - low) * volume
    return _rolling_mean(base, 5)

def cmfd_017_mf_vol_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_017_mf_vol_zscore_5d"""
    base = _safe_div((close - low) - (high - close), high - low) * volume
    return _zscore_rolling(base, 5)

def cmfd_018_mf_vol_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_018_mf_vol_rank_5d"""
    base = _safe_div((close - low) - (high - close), high - low) * volume
    return _rank_pct(base, 5)

def cmfd_019_mf_vol_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_019_mf_vol_lvl_21d"""
    base = _safe_div((close - low) - (high - close), high - low) * volume
    return _rolling_mean(base, 21)

def cmfd_020_mf_vol_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_020_mf_vol_zscore_21d"""
    base = _safe_div((close - low) - (high - close), high - low) * volume
    return _zscore_rolling(base, 21)

def cmfd_021_mf_vol_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_021_mf_vol_rank_21d"""
    base = _safe_div((close - low) - (high - close), high - low) * volume
    return _rank_pct(base, 21)

def cmfd_022_mf_vol_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_022_mf_vol_lvl_63d"""
    base = _safe_div((close - low) - (high - close), high - low) * volume
    return _rolling_mean(base, 63)

def cmfd_023_mf_vol_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_023_mf_vol_zscore_63d"""
    base = _safe_div((close - low) - (high - close), high - low) * volume
    return _zscore_rolling(base, 63)

def cmfd_024_mf_vol_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_024_mf_vol_rank_63d"""
    base = _safe_div((close - low) - (high - close), high - low) * volume
    return _rank_pct(base, 63)

def cmfd_025_mf_vol_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_025_mf_vol_lvl_126d"""
    base = _safe_div((close - low) - (high - close), high - low) * volume
    return _rolling_mean(base, 126)

def cmfd_026_mf_vol_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_026_mf_vol_zscore_126d"""
    base = _safe_div((close - low) - (high - close), high - low) * volume
    return _zscore_rolling(base, 126)

def cmfd_027_mf_vol_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_027_mf_vol_rank_126d"""
    base = _safe_div((close - low) - (high - close), high - low) * volume
    return _rank_pct(base, 126)

def cmfd_028_mf_vol_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_028_mf_vol_lvl_252d"""
    base = _safe_div((close - low) - (high - close), high - low) * volume
    return _rolling_mean(base, 252)

def cmfd_029_mf_vol_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_029_mf_vol_zscore_252d"""
    base = _safe_div((close - low) - (high - close), high - low) * volume
    return _zscore_rolling(base, 252)

def cmfd_030_mf_vol_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_030_mf_vol_rank_252d"""
    base = _safe_div((close - low) - (high - close), high - low) * volume
    return _rank_pct(base, 252)

def cmfd_031_cmf20_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_031_cmf20_lvl_5d"""
    base = _safe_div(_rolling_sum(_safe_div((close - low) - (high - close), high - low) * volume, 20), _rolling_sum(volume, 20))
    return _rolling_mean(base, 5)

def cmfd_032_cmf20_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_032_cmf20_zscore_5d"""
    base = _safe_div(_rolling_sum(_safe_div((close - low) - (high - close), high - low) * volume, 20), _rolling_sum(volume, 20))
    return _zscore_rolling(base, 5)

def cmfd_033_cmf20_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_033_cmf20_rank_5d"""
    base = _safe_div(_rolling_sum(_safe_div((close - low) - (high - close), high - low) * volume, 20), _rolling_sum(volume, 20))
    return _rank_pct(base, 5)

def cmfd_034_cmf20_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_034_cmf20_lvl_21d"""
    base = _safe_div(_rolling_sum(_safe_div((close - low) - (high - close), high - low) * volume, 20), _rolling_sum(volume, 20))
    return _rolling_mean(base, 21)

def cmfd_035_cmf20_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_035_cmf20_zscore_21d"""
    base = _safe_div(_rolling_sum(_safe_div((close - low) - (high - close), high - low) * volume, 20), _rolling_sum(volume, 20))
    return _zscore_rolling(base, 21)

def cmfd_036_cmf20_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_036_cmf20_rank_21d"""
    base = _safe_div(_rolling_sum(_safe_div((close - low) - (high - close), high - low) * volume, 20), _rolling_sum(volume, 20))
    return _rank_pct(base, 21)

def cmfd_037_cmf20_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_037_cmf20_lvl_63d"""
    base = _safe_div(_rolling_sum(_safe_div((close - low) - (high - close), high - low) * volume, 20), _rolling_sum(volume, 20))
    return _rolling_mean(base, 63)

def cmfd_038_cmf20_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_038_cmf20_zscore_63d"""
    base = _safe_div(_rolling_sum(_safe_div((close - low) - (high - close), high - low) * volume, 20), _rolling_sum(volume, 20))
    return _zscore_rolling(base, 63)

def cmfd_039_cmf20_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_039_cmf20_rank_63d"""
    base = _safe_div(_rolling_sum(_safe_div((close - low) - (high - close), high - low) * volume, 20), _rolling_sum(volume, 20))
    return _rank_pct(base, 63)

def cmfd_040_cmf20_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_040_cmf20_lvl_126d"""
    base = _safe_div(_rolling_sum(_safe_div((close - low) - (high - close), high - low) * volume, 20), _rolling_sum(volume, 20))
    return _rolling_mean(base, 126)

def cmfd_041_cmf20_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_041_cmf20_zscore_126d"""
    base = _safe_div(_rolling_sum(_safe_div((close - low) - (high - close), high - low) * volume, 20), _rolling_sum(volume, 20))
    return _zscore_rolling(base, 126)

def cmfd_042_cmf20_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_042_cmf20_rank_126d"""
    base = _safe_div(_rolling_sum(_safe_div((close - low) - (high - close), high - low) * volume, 20), _rolling_sum(volume, 20))
    return _rank_pct(base, 126)

def cmfd_043_cmf20_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_043_cmf20_lvl_252d"""
    base = _safe_div(_rolling_sum(_safe_div((close - low) - (high - close), high - low) * volume, 20), _rolling_sum(volume, 20))
    return _rolling_mean(base, 252)

def cmfd_044_cmf20_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_044_cmf20_zscore_252d"""
    base = _safe_div(_rolling_sum(_safe_div((close - low) - (high - close), high - low) * volume, 20), _rolling_sum(volume, 20))
    return _zscore_rolling(base, 252)

def cmfd_045_cmf20_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_045_cmf20_rank_252d"""
    base = _safe_div(_rolling_sum(_safe_div((close - low) - (high - close), high - low) * volume, 20), _rolling_sum(volume, 20))
    return _rank_pct(base, 252)

def cmfd_046_cmf_z_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_046_cmf_z_lvl_5d"""
    base = _zscore_rolling(_safe_div(_rolling_sum(_safe_div((close - low) - (high - close), high - low) * volume, 20), _rolling_sum(volume, 20)), 63)
    return _rolling_mean(base, 5)

def cmfd_047_cmf_z_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_047_cmf_z_zscore_5d"""
    base = _zscore_rolling(_safe_div(_rolling_sum(_safe_div((close - low) - (high - close), high - low) * volume, 20), _rolling_sum(volume, 20)), 63)
    return _zscore_rolling(base, 5)

def cmfd_048_cmf_z_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_048_cmf_z_rank_5d"""
    base = _zscore_rolling(_safe_div(_rolling_sum(_safe_div((close - low) - (high - close), high - low) * volume, 20), _rolling_sum(volume, 20)), 63)
    return _rank_pct(base, 5)

def cmfd_049_cmf_z_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_049_cmf_z_lvl_21d"""
    base = _zscore_rolling(_safe_div(_rolling_sum(_safe_div((close - low) - (high - close), high - low) * volume, 20), _rolling_sum(volume, 20)), 63)
    return _rolling_mean(base, 21)

def cmfd_050_cmf_z_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_050_cmf_z_zscore_21d"""
    base = _zscore_rolling(_safe_div(_rolling_sum(_safe_div((close - low) - (high - close), high - low) * volume, 20), _rolling_sum(volume, 20)), 63)
    return _zscore_rolling(base, 21)

def cmfd_051_cmf_z_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_051_cmf_z_rank_21d"""
    base = _zscore_rolling(_safe_div(_rolling_sum(_safe_div((close - low) - (high - close), high - low) * volume, 20), _rolling_sum(volume, 20)), 63)
    return _rank_pct(base, 21)

def cmfd_052_cmf_z_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_052_cmf_z_lvl_63d"""
    base = _zscore_rolling(_safe_div(_rolling_sum(_safe_div((close - low) - (high - close), high - low) * volume, 20), _rolling_sum(volume, 20)), 63)
    return _rolling_mean(base, 63)

def cmfd_053_cmf_z_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_053_cmf_z_zscore_63d"""
    base = _zscore_rolling(_safe_div(_rolling_sum(_safe_div((close - low) - (high - close), high - low) * volume, 20), _rolling_sum(volume, 20)), 63)
    return _zscore_rolling(base, 63)

def cmfd_054_cmf_z_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_054_cmf_z_rank_63d"""
    base = _zscore_rolling(_safe_div(_rolling_sum(_safe_div((close - low) - (high - close), high - low) * volume, 20), _rolling_sum(volume, 20)), 63)
    return _rank_pct(base, 63)

def cmfd_055_cmf_z_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_055_cmf_z_lvl_126d"""
    base = _zscore_rolling(_safe_div(_rolling_sum(_safe_div((close - low) - (high - close), high - low) * volume, 20), _rolling_sum(volume, 20)), 63)
    return _rolling_mean(base, 126)

def cmfd_056_cmf_z_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_056_cmf_z_zscore_126d"""
    base = _zscore_rolling(_safe_div(_rolling_sum(_safe_div((close - low) - (high - close), high - low) * volume, 20), _rolling_sum(volume, 20)), 63)
    return _zscore_rolling(base, 126)

def cmfd_057_cmf_z_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_057_cmf_z_rank_126d"""
    base = _zscore_rolling(_safe_div(_rolling_sum(_safe_div((close - low) - (high - close), high - low) * volume, 20), _rolling_sum(volume, 20)), 63)
    return _rank_pct(base, 126)

def cmfd_058_cmf_z_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_058_cmf_z_lvl_252d"""
    base = _zscore_rolling(_safe_div(_rolling_sum(_safe_div((close - low) - (high - close), high - low) * volume, 20), _rolling_sum(volume, 20)), 63)
    return _rolling_mean(base, 252)

def cmfd_059_cmf_z_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_059_cmf_z_zscore_252d"""
    base = _zscore_rolling(_safe_div(_rolling_sum(_safe_div((close - low) - (high - close), high - low) * volume, 20), _rolling_sum(volume, 20)), 63)
    return _zscore_rolling(base, 252)

def cmfd_060_cmf_z_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_060_cmf_z_rank_252d"""
    base = _zscore_rolling(_safe_div(_rolling_sum(_safe_div((close - low) - (high - close), high - low) * volume, 20), _rolling_sum(volume, 20)), 63)
    return _rank_pct(base, 252)

def cmfd_061_cmf_slope_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_061_cmf_slope_lvl_5d"""
    base = (_safe_div(_rolling_sum(_safe_div((close - low) - (high - close), high - low) * volume, 20), _rolling_sum(volume, 20))).diff(5)
    return _rolling_mean(base, 5)

def cmfd_062_cmf_slope_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_062_cmf_slope_zscore_5d"""
    base = (_safe_div(_rolling_sum(_safe_div((close - low) - (high - close), high - low) * volume, 20), _rolling_sum(volume, 20))).diff(5)
    return _zscore_rolling(base, 5)

def cmfd_063_cmf_slope_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_063_cmf_slope_rank_5d"""
    base = (_safe_div(_rolling_sum(_safe_div((close - low) - (high - close), high - low) * volume, 20), _rolling_sum(volume, 20))).diff(5)
    return _rank_pct(base, 5)

def cmfd_064_cmf_slope_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_064_cmf_slope_lvl_21d"""
    base = (_safe_div(_rolling_sum(_safe_div((close - low) - (high - close), high - low) * volume, 20), _rolling_sum(volume, 20))).diff(5)
    return _rolling_mean(base, 21)

def cmfd_065_cmf_slope_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_065_cmf_slope_zscore_21d"""
    base = (_safe_div(_rolling_sum(_safe_div((close - low) - (high - close), high - low) * volume, 20), _rolling_sum(volume, 20))).diff(5)
    return _zscore_rolling(base, 21)

def cmfd_066_cmf_slope_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_066_cmf_slope_rank_21d"""
    base = (_safe_div(_rolling_sum(_safe_div((close - low) - (high - close), high - low) * volume, 20), _rolling_sum(volume, 20))).diff(5)
    return _rank_pct(base, 21)

def cmfd_067_cmf_slope_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_067_cmf_slope_lvl_63d"""
    base = (_safe_div(_rolling_sum(_safe_div((close - low) - (high - close), high - low) * volume, 20), _rolling_sum(volume, 20))).diff(5)
    return _rolling_mean(base, 63)

def cmfd_068_cmf_slope_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_068_cmf_slope_zscore_63d"""
    base = (_safe_div(_rolling_sum(_safe_div((close - low) - (high - close), high - low) * volume, 20), _rolling_sum(volume, 20))).diff(5)
    return _zscore_rolling(base, 63)

def cmfd_069_cmf_slope_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_069_cmf_slope_rank_63d"""
    base = (_safe_div(_rolling_sum(_safe_div((close - low) - (high - close), high - low) * volume, 20), _rolling_sum(volume, 20))).diff(5)
    return _rank_pct(base, 63)

def cmfd_070_cmf_slope_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_070_cmf_slope_lvl_126d"""
    base = (_safe_div(_rolling_sum(_safe_div((close - low) - (high - close), high - low) * volume, 20), _rolling_sum(volume, 20))).diff(5)
    return _rolling_mean(base, 126)

def cmfd_071_cmf_slope_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_071_cmf_slope_zscore_126d"""
    base = (_safe_div(_rolling_sum(_safe_div((close - low) - (high - close), high - low) * volume, 20), _rolling_sum(volume, 20))).diff(5)
    return _zscore_rolling(base, 126)

def cmfd_072_cmf_slope_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_072_cmf_slope_rank_126d"""
    base = (_safe_div(_rolling_sum(_safe_div((close - low) - (high - close), high - low) * volume, 20), _rolling_sum(volume, 20))).diff(5)
    return _rank_pct(base, 126)

def cmfd_073_cmf_slope_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_073_cmf_slope_lvl_252d"""
    base = (_safe_div(_rolling_sum(_safe_div((close - low) - (high - close), high - low) * volume, 20), _rolling_sum(volume, 20))).diff(5)
    return _rolling_mean(base, 252)

def cmfd_074_cmf_slope_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_074_cmf_slope_zscore_252d"""
    base = (_safe_div(_rolling_sum(_safe_div((close - low) - (high - close), high - low) * volume, 20), _rolling_sum(volume, 20))).diff(5)
    return _zscore_rolling(base, 252)

def cmfd_075_cmf_slope_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """cmfd_075_cmf_slope_rank_252d"""
    base = (_safe_div(_rolling_sum(_safe_div((close - low) - (high - close), high - low) * volume, 20), _rolling_sum(volume, 20))).diff(5)
    return _rank_pct(base, 252)

# ── Registry ──────────────────────────────────────────────────────────────────
V83_REGISTRY = {
    "cmfd_001_mf_mult_lvl_5d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_001_mf_mult_lvl_5d},
    "cmfd_002_mf_mult_zscore_5d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_002_mf_mult_zscore_5d},
    "cmfd_003_mf_mult_rank_5d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_003_mf_mult_rank_5d},
    "cmfd_004_mf_mult_lvl_21d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_004_mf_mult_lvl_21d},
    "cmfd_005_mf_mult_zscore_21d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_005_mf_mult_zscore_21d},
    "cmfd_006_mf_mult_rank_21d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_006_mf_mult_rank_21d},
    "cmfd_007_mf_mult_lvl_63d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_007_mf_mult_lvl_63d},
    "cmfd_008_mf_mult_zscore_63d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_008_mf_mult_zscore_63d},
    "cmfd_009_mf_mult_rank_63d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_009_mf_mult_rank_63d},
    "cmfd_010_mf_mult_lvl_126d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_010_mf_mult_lvl_126d},
    "cmfd_011_mf_mult_zscore_126d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_011_mf_mult_zscore_126d},
    "cmfd_012_mf_mult_rank_126d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_012_mf_mult_rank_126d},
    "cmfd_013_mf_mult_lvl_252d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_013_mf_mult_lvl_252d},
    "cmfd_014_mf_mult_zscore_252d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_014_mf_mult_zscore_252d},
    "cmfd_015_mf_mult_rank_252d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_015_mf_mult_rank_252d},
    "cmfd_016_mf_vol_lvl_5d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_016_mf_vol_lvl_5d},
    "cmfd_017_mf_vol_zscore_5d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_017_mf_vol_zscore_5d},
    "cmfd_018_mf_vol_rank_5d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_018_mf_vol_rank_5d},
    "cmfd_019_mf_vol_lvl_21d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_019_mf_vol_lvl_21d},
    "cmfd_020_mf_vol_zscore_21d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_020_mf_vol_zscore_21d},
    "cmfd_021_mf_vol_rank_21d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_021_mf_vol_rank_21d},
    "cmfd_022_mf_vol_lvl_63d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_022_mf_vol_lvl_63d},
    "cmfd_023_mf_vol_zscore_63d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_023_mf_vol_zscore_63d},
    "cmfd_024_mf_vol_rank_63d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_024_mf_vol_rank_63d},
    "cmfd_025_mf_vol_lvl_126d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_025_mf_vol_lvl_126d},
    "cmfd_026_mf_vol_zscore_126d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_026_mf_vol_zscore_126d},
    "cmfd_027_mf_vol_rank_126d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_027_mf_vol_rank_126d},
    "cmfd_028_mf_vol_lvl_252d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_028_mf_vol_lvl_252d},
    "cmfd_029_mf_vol_zscore_252d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_029_mf_vol_zscore_252d},
    "cmfd_030_mf_vol_rank_252d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_030_mf_vol_rank_252d},
    "cmfd_031_cmf20_lvl_5d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_031_cmf20_lvl_5d},
    "cmfd_032_cmf20_zscore_5d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_032_cmf20_zscore_5d},
    "cmfd_033_cmf20_rank_5d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_033_cmf20_rank_5d},
    "cmfd_034_cmf20_lvl_21d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_034_cmf20_lvl_21d},
    "cmfd_035_cmf20_zscore_21d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_035_cmf20_zscore_21d},
    "cmfd_036_cmf20_rank_21d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_036_cmf20_rank_21d},
    "cmfd_037_cmf20_lvl_63d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_037_cmf20_lvl_63d},
    "cmfd_038_cmf20_zscore_63d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_038_cmf20_zscore_63d},
    "cmfd_039_cmf20_rank_63d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_039_cmf20_rank_63d},
    "cmfd_040_cmf20_lvl_126d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_040_cmf20_lvl_126d},
    "cmfd_041_cmf20_zscore_126d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_041_cmf20_zscore_126d},
    "cmfd_042_cmf20_rank_126d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_042_cmf20_rank_126d},
    "cmfd_043_cmf20_lvl_252d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_043_cmf20_lvl_252d},
    "cmfd_044_cmf20_zscore_252d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_044_cmf20_zscore_252d},
    "cmfd_045_cmf20_rank_252d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_045_cmf20_rank_252d},
    "cmfd_046_cmf_z_lvl_5d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_046_cmf_z_lvl_5d},
    "cmfd_047_cmf_z_zscore_5d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_047_cmf_z_zscore_5d},
    "cmfd_048_cmf_z_rank_5d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_048_cmf_z_rank_5d},
    "cmfd_049_cmf_z_lvl_21d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_049_cmf_z_lvl_21d},
    "cmfd_050_cmf_z_zscore_21d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_050_cmf_z_zscore_21d},
    "cmfd_051_cmf_z_rank_21d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_051_cmf_z_rank_21d},
    "cmfd_052_cmf_z_lvl_63d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_052_cmf_z_lvl_63d},
    "cmfd_053_cmf_z_zscore_63d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_053_cmf_z_zscore_63d},
    "cmfd_054_cmf_z_rank_63d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_054_cmf_z_rank_63d},
    "cmfd_055_cmf_z_lvl_126d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_055_cmf_z_lvl_126d},
    "cmfd_056_cmf_z_zscore_126d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_056_cmf_z_zscore_126d},
    "cmfd_057_cmf_z_rank_126d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_057_cmf_z_rank_126d},
    "cmfd_058_cmf_z_lvl_252d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_058_cmf_z_lvl_252d},
    "cmfd_059_cmf_z_zscore_252d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_059_cmf_z_zscore_252d},
    "cmfd_060_cmf_z_rank_252d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_060_cmf_z_rank_252d},
    "cmfd_061_cmf_slope_lvl_5d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_061_cmf_slope_lvl_5d},
    "cmfd_062_cmf_slope_zscore_5d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_062_cmf_slope_zscore_5d},
    "cmfd_063_cmf_slope_rank_5d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_063_cmf_slope_rank_5d},
    "cmfd_064_cmf_slope_lvl_21d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_064_cmf_slope_lvl_21d},
    "cmfd_065_cmf_slope_zscore_21d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_065_cmf_slope_zscore_21d},
    "cmfd_066_cmf_slope_rank_21d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_066_cmf_slope_rank_21d},
    "cmfd_067_cmf_slope_lvl_63d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_067_cmf_slope_lvl_63d},
    "cmfd_068_cmf_slope_zscore_63d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_068_cmf_slope_zscore_63d},
    "cmfd_069_cmf_slope_rank_63d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_069_cmf_slope_rank_63d},
    "cmfd_070_cmf_slope_lvl_126d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_070_cmf_slope_lvl_126d},
    "cmfd_071_cmf_slope_zscore_126d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_071_cmf_slope_zscore_126d},
    "cmfd_072_cmf_slope_rank_126d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_072_cmf_slope_rank_126d},
    "cmfd_073_cmf_slope_lvl_252d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_073_cmf_slope_lvl_252d},
    "cmfd_074_cmf_slope_zscore_252d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_074_cmf_slope_zscore_252d},
    "cmfd_075_cmf_slope_rank_252d": {"inputs": ["high", "low", "close", "volume"], "func": cmfd_075_cmf_slope_rank_252d},
}
