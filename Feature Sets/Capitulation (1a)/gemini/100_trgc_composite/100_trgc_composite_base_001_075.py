"""
100_trgc_composite — Base Features 001-075
Domain: trgc_composite
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

def trgc_001_comp_mom_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_001_comp_mom_lvl_5d"""
    base = close.pct_change(21) + close.pct_change(63) + close.pct_change(252)
    return _rolling_mean(base, 5)

def trgc_002_comp_mom_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_002_comp_mom_zscore_5d"""
    base = close.pct_change(21) + close.pct_change(63) + close.pct_change(252)
    return _zscore_rolling(base, 5)

def trgc_003_comp_mom_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_003_comp_mom_rank_5d"""
    base = close.pct_change(21) + close.pct_change(63) + close.pct_change(252)
    return _rank_pct(base, 5)

def trgc_004_comp_mom_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_004_comp_mom_lvl_21d"""
    base = close.pct_change(21) + close.pct_change(63) + close.pct_change(252)
    return _rolling_mean(base, 21)

def trgc_005_comp_mom_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_005_comp_mom_zscore_21d"""
    base = close.pct_change(21) + close.pct_change(63) + close.pct_change(252)
    return _zscore_rolling(base, 21)

def trgc_006_comp_mom_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_006_comp_mom_rank_21d"""
    base = close.pct_change(21) + close.pct_change(63) + close.pct_change(252)
    return _rank_pct(base, 21)

def trgc_007_comp_mom_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_007_comp_mom_lvl_63d"""
    base = close.pct_change(21) + close.pct_change(63) + close.pct_change(252)
    return _rolling_mean(base, 63)

def trgc_008_comp_mom_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_008_comp_mom_zscore_63d"""
    base = close.pct_change(21) + close.pct_change(63) + close.pct_change(252)
    return _zscore_rolling(base, 63)

def trgc_009_comp_mom_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_009_comp_mom_rank_63d"""
    base = close.pct_change(21) + close.pct_change(63) + close.pct_change(252)
    return _rank_pct(base, 63)

def trgc_010_comp_mom_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_010_comp_mom_lvl_126d"""
    base = close.pct_change(21) + close.pct_change(63) + close.pct_change(252)
    return _rolling_mean(base, 126)

def trgc_011_comp_mom_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_011_comp_mom_zscore_126d"""
    base = close.pct_change(21) + close.pct_change(63) + close.pct_change(252)
    return _zscore_rolling(base, 126)

def trgc_012_comp_mom_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_012_comp_mom_rank_126d"""
    base = close.pct_change(21) + close.pct_change(63) + close.pct_change(252)
    return _rank_pct(base, 126)

def trgc_013_comp_mom_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_013_comp_mom_lvl_252d"""
    base = close.pct_change(21) + close.pct_change(63) + close.pct_change(252)
    return _rolling_mean(base, 252)

def trgc_014_comp_mom_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_014_comp_mom_zscore_252d"""
    base = close.pct_change(21) + close.pct_change(63) + close.pct_change(252)
    return _zscore_rolling(base, 252)

def trgc_015_comp_mom_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_015_comp_mom_rank_252d"""
    base = close.pct_change(21) + close.pct_change(63) + close.pct_change(252)
    return _rank_pct(base, 252)

def trgc_016_comp_vol_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_016_comp_vol_lvl_5d"""
    base = _rolling_std(close.pct_change(), 21) + _rolling_std(close.pct_change(), 63)
    return _rolling_mean(base, 5)

def trgc_017_comp_vol_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_017_comp_vol_zscore_5d"""
    base = _rolling_std(close.pct_change(), 21) + _rolling_std(close.pct_change(), 63)
    return _zscore_rolling(base, 5)

def trgc_018_comp_vol_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_018_comp_vol_rank_5d"""
    base = _rolling_std(close.pct_change(), 21) + _rolling_std(close.pct_change(), 63)
    return _rank_pct(base, 5)

def trgc_019_comp_vol_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_019_comp_vol_lvl_21d"""
    base = _rolling_std(close.pct_change(), 21) + _rolling_std(close.pct_change(), 63)
    return _rolling_mean(base, 21)

def trgc_020_comp_vol_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_020_comp_vol_zscore_21d"""
    base = _rolling_std(close.pct_change(), 21) + _rolling_std(close.pct_change(), 63)
    return _zscore_rolling(base, 21)

def trgc_021_comp_vol_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_021_comp_vol_rank_21d"""
    base = _rolling_std(close.pct_change(), 21) + _rolling_std(close.pct_change(), 63)
    return _rank_pct(base, 21)

def trgc_022_comp_vol_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_022_comp_vol_lvl_63d"""
    base = _rolling_std(close.pct_change(), 21) + _rolling_std(close.pct_change(), 63)
    return _rolling_mean(base, 63)

def trgc_023_comp_vol_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_023_comp_vol_zscore_63d"""
    base = _rolling_std(close.pct_change(), 21) + _rolling_std(close.pct_change(), 63)
    return _zscore_rolling(base, 63)

def trgc_024_comp_vol_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_024_comp_vol_rank_63d"""
    base = _rolling_std(close.pct_change(), 21) + _rolling_std(close.pct_change(), 63)
    return _rank_pct(base, 63)

def trgc_025_comp_vol_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_025_comp_vol_lvl_126d"""
    base = _rolling_std(close.pct_change(), 21) + _rolling_std(close.pct_change(), 63)
    return _rolling_mean(base, 126)

def trgc_026_comp_vol_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_026_comp_vol_zscore_126d"""
    base = _rolling_std(close.pct_change(), 21) + _rolling_std(close.pct_change(), 63)
    return _zscore_rolling(base, 126)

def trgc_027_comp_vol_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_027_comp_vol_rank_126d"""
    base = _rolling_std(close.pct_change(), 21) + _rolling_std(close.pct_change(), 63)
    return _rank_pct(base, 126)

def trgc_028_comp_vol_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_028_comp_vol_lvl_252d"""
    base = _rolling_std(close.pct_change(), 21) + _rolling_std(close.pct_change(), 63)
    return _rolling_mean(base, 252)

def trgc_029_comp_vol_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_029_comp_vol_zscore_252d"""
    base = _rolling_std(close.pct_change(), 21) + _rolling_std(close.pct_change(), 63)
    return _zscore_rolling(base, 252)

def trgc_030_comp_vol_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_030_comp_vol_rank_252d"""
    base = _rolling_std(close.pct_change(), 21) + _rolling_std(close.pct_change(), 63)
    return _rank_pct(base, 252)

def trgc_031_comp_adv_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_031_comp_adv_lvl_5d"""
    base = _safe_div(volume * close, _rolling_mean(volume * close, 252))
    return _rolling_mean(base, 5)

def trgc_032_comp_adv_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_032_comp_adv_zscore_5d"""
    base = _safe_div(volume * close, _rolling_mean(volume * close, 252))
    return _zscore_rolling(base, 5)

def trgc_033_comp_adv_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_033_comp_adv_rank_5d"""
    base = _safe_div(volume * close, _rolling_mean(volume * close, 252))
    return _rank_pct(base, 5)

def trgc_034_comp_adv_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_034_comp_adv_lvl_21d"""
    base = _safe_div(volume * close, _rolling_mean(volume * close, 252))
    return _rolling_mean(base, 21)

def trgc_035_comp_adv_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_035_comp_adv_zscore_21d"""
    base = _safe_div(volume * close, _rolling_mean(volume * close, 252))
    return _zscore_rolling(base, 21)

def trgc_036_comp_adv_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_036_comp_adv_rank_21d"""
    base = _safe_div(volume * close, _rolling_mean(volume * close, 252))
    return _rank_pct(base, 21)

def trgc_037_comp_adv_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_037_comp_adv_lvl_63d"""
    base = _safe_div(volume * close, _rolling_mean(volume * close, 252))
    return _rolling_mean(base, 63)

def trgc_038_comp_adv_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_038_comp_adv_zscore_63d"""
    base = _safe_div(volume * close, _rolling_mean(volume * close, 252))
    return _zscore_rolling(base, 63)

def trgc_039_comp_adv_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_039_comp_adv_rank_63d"""
    base = _safe_div(volume * close, _rolling_mean(volume * close, 252))
    return _rank_pct(base, 63)

def trgc_040_comp_adv_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_040_comp_adv_lvl_126d"""
    base = _safe_div(volume * close, _rolling_mean(volume * close, 252))
    return _rolling_mean(base, 126)

def trgc_041_comp_adv_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_041_comp_adv_zscore_126d"""
    base = _safe_div(volume * close, _rolling_mean(volume * close, 252))
    return _zscore_rolling(base, 126)

def trgc_042_comp_adv_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_042_comp_adv_rank_126d"""
    base = _safe_div(volume * close, _rolling_mean(volume * close, 252))
    return _rank_pct(base, 126)

def trgc_043_comp_adv_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_043_comp_adv_lvl_252d"""
    base = _safe_div(volume * close, _rolling_mean(volume * close, 252))
    return _rolling_mean(base, 252)

def trgc_044_comp_adv_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_044_comp_adv_zscore_252d"""
    base = _safe_div(volume * close, _rolling_mean(volume * close, 252))
    return _zscore_rolling(base, 252)

def trgc_045_comp_adv_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_045_comp_adv_rank_252d"""
    base = _safe_div(volume * close, _rolling_mean(volume * close, 252))
    return _rank_pct(base, 252)

def trgc_046_comp_range_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_046_comp_range_lvl_5d"""
    base = _safe_div(high - low, close)
    return _rolling_mean(base, 5)

def trgc_047_comp_range_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_047_comp_range_zscore_5d"""
    base = _safe_div(high - low, close)
    return _zscore_rolling(base, 5)

def trgc_048_comp_range_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_048_comp_range_rank_5d"""
    base = _safe_div(high - low, close)
    return _rank_pct(base, 5)

def trgc_049_comp_range_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_049_comp_range_lvl_21d"""
    base = _safe_div(high - low, close)
    return _rolling_mean(base, 21)

def trgc_050_comp_range_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_050_comp_range_zscore_21d"""
    base = _safe_div(high - low, close)
    return _zscore_rolling(base, 21)

def trgc_051_comp_range_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_051_comp_range_rank_21d"""
    base = _safe_div(high - low, close)
    return _rank_pct(base, 21)

def trgc_052_comp_range_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_052_comp_range_lvl_63d"""
    base = _safe_div(high - low, close)
    return _rolling_mean(base, 63)

def trgc_053_comp_range_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_053_comp_range_zscore_63d"""
    base = _safe_div(high - low, close)
    return _zscore_rolling(base, 63)

def trgc_054_comp_range_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_054_comp_range_rank_63d"""
    base = _safe_div(high - low, close)
    return _rank_pct(base, 63)

def trgc_055_comp_range_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_055_comp_range_lvl_126d"""
    base = _safe_div(high - low, close)
    return _rolling_mean(base, 126)

def trgc_056_comp_range_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_056_comp_range_zscore_126d"""
    base = _safe_div(high - low, close)
    return _zscore_rolling(base, 126)

def trgc_057_comp_range_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_057_comp_range_rank_126d"""
    base = _safe_div(high - low, close)
    return _rank_pct(base, 126)

def trgc_058_comp_range_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_058_comp_range_lvl_252d"""
    base = _safe_div(high - low, close)
    return _rolling_mean(base, 252)

def trgc_059_comp_range_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_059_comp_range_zscore_252d"""
    base = _safe_div(high - low, close)
    return _zscore_rolling(base, 252)

def trgc_060_comp_range_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_060_comp_range_rank_252d"""
    base = _safe_div(high - low, close)
    return _rank_pct(base, 252)

def trgc_061_comp_trend_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_061_comp_trend_lvl_5d"""
    base = _safe_div(close, _rolling_mean(close, 252))
    return _rolling_mean(base, 5)

def trgc_062_comp_trend_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_062_comp_trend_zscore_5d"""
    base = _safe_div(close, _rolling_mean(close, 252))
    return _zscore_rolling(base, 5)

def trgc_063_comp_trend_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_063_comp_trend_rank_5d"""
    base = _safe_div(close, _rolling_mean(close, 252))
    return _rank_pct(base, 5)

def trgc_064_comp_trend_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_064_comp_trend_lvl_21d"""
    base = _safe_div(close, _rolling_mean(close, 252))
    return _rolling_mean(base, 21)

def trgc_065_comp_trend_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_065_comp_trend_zscore_21d"""
    base = _safe_div(close, _rolling_mean(close, 252))
    return _zscore_rolling(base, 21)

def trgc_066_comp_trend_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_066_comp_trend_rank_21d"""
    base = _safe_div(close, _rolling_mean(close, 252))
    return _rank_pct(base, 21)

def trgc_067_comp_trend_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_067_comp_trend_lvl_63d"""
    base = _safe_div(close, _rolling_mean(close, 252))
    return _rolling_mean(base, 63)

def trgc_068_comp_trend_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_068_comp_trend_zscore_63d"""
    base = _safe_div(close, _rolling_mean(close, 252))
    return _zscore_rolling(base, 63)

def trgc_069_comp_trend_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_069_comp_trend_rank_63d"""
    base = _safe_div(close, _rolling_mean(close, 252))
    return _rank_pct(base, 63)

def trgc_070_comp_trend_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_070_comp_trend_lvl_126d"""
    base = _safe_div(close, _rolling_mean(close, 252))
    return _rolling_mean(base, 126)

def trgc_071_comp_trend_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_071_comp_trend_zscore_126d"""
    base = _safe_div(close, _rolling_mean(close, 252))
    return _zscore_rolling(base, 126)

def trgc_072_comp_trend_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_072_comp_trend_rank_126d"""
    base = _safe_div(close, _rolling_mean(close, 252))
    return _rank_pct(base, 126)

def trgc_073_comp_trend_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_073_comp_trend_lvl_252d"""
    base = _safe_div(close, _rolling_mean(close, 252))
    return _rolling_mean(base, 252)

def trgc_074_comp_trend_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_074_comp_trend_zscore_252d"""
    base = _safe_div(close, _rolling_mean(close, 252))
    return _zscore_rolling(base, 252)

def trgc_075_comp_trend_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """trgc_075_comp_trend_rank_252d"""
    base = _safe_div(close, _rolling_mean(close, 252))
    return _rank_pct(base, 252)

# ── Registry ──────────────────────────────────────────────────────────────────
V100_REGISTRY = {
    "trgc_001_comp_mom_lvl_5d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_001_comp_mom_lvl_5d},
    "trgc_002_comp_mom_zscore_5d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_002_comp_mom_zscore_5d},
    "trgc_003_comp_mom_rank_5d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_003_comp_mom_rank_5d},
    "trgc_004_comp_mom_lvl_21d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_004_comp_mom_lvl_21d},
    "trgc_005_comp_mom_zscore_21d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_005_comp_mom_zscore_21d},
    "trgc_006_comp_mom_rank_21d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_006_comp_mom_rank_21d},
    "trgc_007_comp_mom_lvl_63d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_007_comp_mom_lvl_63d},
    "trgc_008_comp_mom_zscore_63d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_008_comp_mom_zscore_63d},
    "trgc_009_comp_mom_rank_63d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_009_comp_mom_rank_63d},
    "trgc_010_comp_mom_lvl_126d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_010_comp_mom_lvl_126d},
    "trgc_011_comp_mom_zscore_126d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_011_comp_mom_zscore_126d},
    "trgc_012_comp_mom_rank_126d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_012_comp_mom_rank_126d},
    "trgc_013_comp_mom_lvl_252d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_013_comp_mom_lvl_252d},
    "trgc_014_comp_mom_zscore_252d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_014_comp_mom_zscore_252d},
    "trgc_015_comp_mom_rank_252d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_015_comp_mom_rank_252d},
    "trgc_016_comp_vol_lvl_5d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_016_comp_vol_lvl_5d},
    "trgc_017_comp_vol_zscore_5d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_017_comp_vol_zscore_5d},
    "trgc_018_comp_vol_rank_5d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_018_comp_vol_rank_5d},
    "trgc_019_comp_vol_lvl_21d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_019_comp_vol_lvl_21d},
    "trgc_020_comp_vol_zscore_21d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_020_comp_vol_zscore_21d},
    "trgc_021_comp_vol_rank_21d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_021_comp_vol_rank_21d},
    "trgc_022_comp_vol_lvl_63d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_022_comp_vol_lvl_63d},
    "trgc_023_comp_vol_zscore_63d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_023_comp_vol_zscore_63d},
    "trgc_024_comp_vol_rank_63d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_024_comp_vol_rank_63d},
    "trgc_025_comp_vol_lvl_126d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_025_comp_vol_lvl_126d},
    "trgc_026_comp_vol_zscore_126d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_026_comp_vol_zscore_126d},
    "trgc_027_comp_vol_rank_126d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_027_comp_vol_rank_126d},
    "trgc_028_comp_vol_lvl_252d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_028_comp_vol_lvl_252d},
    "trgc_029_comp_vol_zscore_252d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_029_comp_vol_zscore_252d},
    "trgc_030_comp_vol_rank_252d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_030_comp_vol_rank_252d},
    "trgc_031_comp_adv_lvl_5d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_031_comp_adv_lvl_5d},
    "trgc_032_comp_adv_zscore_5d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_032_comp_adv_zscore_5d},
    "trgc_033_comp_adv_rank_5d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_033_comp_adv_rank_5d},
    "trgc_034_comp_adv_lvl_21d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_034_comp_adv_lvl_21d},
    "trgc_035_comp_adv_zscore_21d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_035_comp_adv_zscore_21d},
    "trgc_036_comp_adv_rank_21d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_036_comp_adv_rank_21d},
    "trgc_037_comp_adv_lvl_63d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_037_comp_adv_lvl_63d},
    "trgc_038_comp_adv_zscore_63d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_038_comp_adv_zscore_63d},
    "trgc_039_comp_adv_rank_63d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_039_comp_adv_rank_63d},
    "trgc_040_comp_adv_lvl_126d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_040_comp_adv_lvl_126d},
    "trgc_041_comp_adv_zscore_126d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_041_comp_adv_zscore_126d},
    "trgc_042_comp_adv_rank_126d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_042_comp_adv_rank_126d},
    "trgc_043_comp_adv_lvl_252d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_043_comp_adv_lvl_252d},
    "trgc_044_comp_adv_zscore_252d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_044_comp_adv_zscore_252d},
    "trgc_045_comp_adv_rank_252d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_045_comp_adv_rank_252d},
    "trgc_046_comp_range_lvl_5d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_046_comp_range_lvl_5d},
    "trgc_047_comp_range_zscore_5d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_047_comp_range_zscore_5d},
    "trgc_048_comp_range_rank_5d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_048_comp_range_rank_5d},
    "trgc_049_comp_range_lvl_21d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_049_comp_range_lvl_21d},
    "trgc_050_comp_range_zscore_21d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_050_comp_range_zscore_21d},
    "trgc_051_comp_range_rank_21d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_051_comp_range_rank_21d},
    "trgc_052_comp_range_lvl_63d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_052_comp_range_lvl_63d},
    "trgc_053_comp_range_zscore_63d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_053_comp_range_zscore_63d},
    "trgc_054_comp_range_rank_63d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_054_comp_range_rank_63d},
    "trgc_055_comp_range_lvl_126d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_055_comp_range_lvl_126d},
    "trgc_056_comp_range_zscore_126d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_056_comp_range_zscore_126d},
    "trgc_057_comp_range_rank_126d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_057_comp_range_rank_126d},
    "trgc_058_comp_range_lvl_252d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_058_comp_range_lvl_252d},
    "trgc_059_comp_range_zscore_252d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_059_comp_range_zscore_252d},
    "trgc_060_comp_range_rank_252d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_060_comp_range_rank_252d},
    "trgc_061_comp_trend_lvl_5d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_061_comp_trend_lvl_5d},
    "trgc_062_comp_trend_zscore_5d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_062_comp_trend_zscore_5d},
    "trgc_063_comp_trend_rank_5d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_063_comp_trend_rank_5d},
    "trgc_064_comp_trend_lvl_21d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_064_comp_trend_lvl_21d},
    "trgc_065_comp_trend_zscore_21d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_065_comp_trend_zscore_21d},
    "trgc_066_comp_trend_rank_21d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_066_comp_trend_rank_21d},
    "trgc_067_comp_trend_lvl_63d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_067_comp_trend_lvl_63d},
    "trgc_068_comp_trend_zscore_63d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_068_comp_trend_zscore_63d},
    "trgc_069_comp_trend_rank_63d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_069_comp_trend_rank_63d},
    "trgc_070_comp_trend_lvl_126d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_070_comp_trend_lvl_126d},
    "trgc_071_comp_trend_zscore_126d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_071_comp_trend_zscore_126d},
    "trgc_072_comp_trend_rank_126d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_072_comp_trend_rank_126d},
    "trgc_073_comp_trend_lvl_252d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_073_comp_trend_lvl_252d},
    "trgc_074_comp_trend_zscore_252d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_074_comp_trend_zscore_252d},
    "trgc_075_comp_trend_rank_252d": {"inputs": ["high", "low", "close", "volume"], "func": trgc_075_comp_trend_rank_252d},
}
