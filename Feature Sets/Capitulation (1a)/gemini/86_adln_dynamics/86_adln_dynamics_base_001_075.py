"""
86_adln_dynamics — Base Features 001-075
Domain: adln_dynamics
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

def adln_001_adl_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_001_adl_lvl_5d"""
    base = ((close - low) - (high - close)) / (high - low).replace(0, _EPS) * volume
    return _rolling_mean(base, 5)

def adln_002_adl_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_002_adl_zscore_5d"""
    base = ((close - low) - (high - close)) / (high - low).replace(0, _EPS) * volume
    return _zscore_rolling(base, 5)

def adln_003_adl_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_003_adl_rank_5d"""
    base = ((close - low) - (high - close)) / (high - low).replace(0, _EPS) * volume
    return _rank_pct(base, 5)

def adln_004_adl_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_004_adl_lvl_21d"""
    base = ((close - low) - (high - close)) / (high - low).replace(0, _EPS) * volume
    return _rolling_mean(base, 21)

def adln_005_adl_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_005_adl_zscore_21d"""
    base = ((close - low) - (high - close)) / (high - low).replace(0, _EPS) * volume
    return _zscore_rolling(base, 21)

def adln_006_adl_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_006_adl_rank_21d"""
    base = ((close - low) - (high - close)) / (high - low).replace(0, _EPS) * volume
    return _rank_pct(base, 21)

def adln_007_adl_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_007_adl_lvl_63d"""
    base = ((close - low) - (high - close)) / (high - low).replace(0, _EPS) * volume
    return _rolling_mean(base, 63)

def adln_008_adl_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_008_adl_zscore_63d"""
    base = ((close - low) - (high - close)) / (high - low).replace(0, _EPS) * volume
    return _zscore_rolling(base, 63)

def adln_009_adl_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_009_adl_rank_63d"""
    base = ((close - low) - (high - close)) / (high - low).replace(0, _EPS) * volume
    return _rank_pct(base, 63)

def adln_010_adl_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_010_adl_lvl_126d"""
    base = ((close - low) - (high - close)) / (high - low).replace(0, _EPS) * volume
    return _rolling_mean(base, 126)

def adln_011_adl_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_011_adl_zscore_126d"""
    base = ((close - low) - (high - close)) / (high - low).replace(0, _EPS) * volume
    return _zscore_rolling(base, 126)

def adln_012_adl_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_012_adl_rank_126d"""
    base = ((close - low) - (high - close)) / (high - low).replace(0, _EPS) * volume
    return _rank_pct(base, 126)

def adln_013_adl_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_013_adl_lvl_252d"""
    base = ((close - low) - (high - close)) / (high - low).replace(0, _EPS) * volume
    return _rolling_mean(base, 252)

def adln_014_adl_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_014_adl_zscore_252d"""
    base = ((close - low) - (high - close)) / (high - low).replace(0, _EPS) * volume
    return _zscore_rolling(base, 252)

def adln_015_adl_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_015_adl_rank_252d"""
    base = ((close - low) - (high - close)) / (high - low).replace(0, _EPS) * volume
    return _rank_pct(base, 252)

def adln_016_adl_ps_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_016_adl_ps_lvl_5d"""
    base = (((close - low) - (high - close)) / (high - low).replace(0, _EPS) * volume).cumsum()
    return _rolling_mean(base, 5)

def adln_017_adl_ps_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_017_adl_ps_zscore_5d"""
    base = (((close - low) - (high - close)) / (high - low).replace(0, _EPS) * volume).cumsum()
    return _zscore_rolling(base, 5)

def adln_018_adl_ps_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_018_adl_ps_rank_5d"""
    base = (((close - low) - (high - close)) / (high - low).replace(0, _EPS) * volume).cumsum()
    return _rank_pct(base, 5)

def adln_019_adl_ps_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_019_adl_ps_lvl_21d"""
    base = (((close - low) - (high - close)) / (high - low).replace(0, _EPS) * volume).cumsum()
    return _rolling_mean(base, 21)

def adln_020_adl_ps_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_020_adl_ps_zscore_21d"""
    base = (((close - low) - (high - close)) / (high - low).replace(0, _EPS) * volume).cumsum()
    return _zscore_rolling(base, 21)

def adln_021_adl_ps_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_021_adl_ps_rank_21d"""
    base = (((close - low) - (high - close)) / (high - low).replace(0, _EPS) * volume).cumsum()
    return _rank_pct(base, 21)

def adln_022_adl_ps_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_022_adl_ps_lvl_63d"""
    base = (((close - low) - (high - close)) / (high - low).replace(0, _EPS) * volume).cumsum()
    return _rolling_mean(base, 63)

def adln_023_adl_ps_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_023_adl_ps_zscore_63d"""
    base = (((close - low) - (high - close)) / (high - low).replace(0, _EPS) * volume).cumsum()
    return _zscore_rolling(base, 63)

def adln_024_adl_ps_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_024_adl_ps_rank_63d"""
    base = (((close - low) - (high - close)) / (high - low).replace(0, _EPS) * volume).cumsum()
    return _rank_pct(base, 63)

def adln_025_adl_ps_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_025_adl_ps_lvl_126d"""
    base = (((close - low) - (high - close)) / (high - low).replace(0, _EPS) * volume).cumsum()
    return _rolling_mean(base, 126)

def adln_026_adl_ps_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_026_adl_ps_zscore_126d"""
    base = (((close - low) - (high - close)) / (high - low).replace(0, _EPS) * volume).cumsum()
    return _zscore_rolling(base, 126)

def adln_027_adl_ps_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_027_adl_ps_rank_126d"""
    base = (((close - low) - (high - close)) / (high - low).replace(0, _EPS) * volume).cumsum()
    return _rank_pct(base, 126)

def adln_028_adl_ps_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_028_adl_ps_lvl_252d"""
    base = (((close - low) - (high - close)) / (high - low).replace(0, _EPS) * volume).cumsum()
    return _rolling_mean(base, 252)

def adln_029_adl_ps_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_029_adl_ps_zscore_252d"""
    base = (((close - low) - (high - close)) / (high - low).replace(0, _EPS) * volume).cumsum()
    return _zscore_rolling(base, 252)

def adln_030_adl_ps_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_030_adl_ps_rank_252d"""
    base = (((close - low) - (high - close)) / (high - low).replace(0, _EPS) * volume).cumsum()
    return _rank_pct(base, 252)

def adln_031_chaikin_osc_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_031_chaikin_osc_lvl_5d"""
    base = close.ewm(span=3).mean() - close.ewm(span=10).mean()
    return _rolling_mean(base, 5)

def adln_032_chaikin_osc_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_032_chaikin_osc_zscore_5d"""
    base = close.ewm(span=3).mean() - close.ewm(span=10).mean()
    return _zscore_rolling(base, 5)

def adln_033_chaikin_osc_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_033_chaikin_osc_rank_5d"""
    base = close.ewm(span=3).mean() - close.ewm(span=10).mean()
    return _rank_pct(base, 5)

def adln_034_chaikin_osc_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_034_chaikin_osc_lvl_21d"""
    base = close.ewm(span=3).mean() - close.ewm(span=10).mean()
    return _rolling_mean(base, 21)

def adln_035_chaikin_osc_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_035_chaikin_osc_zscore_21d"""
    base = close.ewm(span=3).mean() - close.ewm(span=10).mean()
    return _zscore_rolling(base, 21)

def adln_036_chaikin_osc_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_036_chaikin_osc_rank_21d"""
    base = close.ewm(span=3).mean() - close.ewm(span=10).mean()
    return _rank_pct(base, 21)

def adln_037_chaikin_osc_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_037_chaikin_osc_lvl_63d"""
    base = close.ewm(span=3).mean() - close.ewm(span=10).mean()
    return _rolling_mean(base, 63)

def adln_038_chaikin_osc_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_038_chaikin_osc_zscore_63d"""
    base = close.ewm(span=3).mean() - close.ewm(span=10).mean()
    return _zscore_rolling(base, 63)

def adln_039_chaikin_osc_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_039_chaikin_osc_rank_63d"""
    base = close.ewm(span=3).mean() - close.ewm(span=10).mean()
    return _rank_pct(base, 63)

def adln_040_chaikin_osc_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_040_chaikin_osc_lvl_126d"""
    base = close.ewm(span=3).mean() - close.ewm(span=10).mean()
    return _rolling_mean(base, 126)

def adln_041_chaikin_osc_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_041_chaikin_osc_zscore_126d"""
    base = close.ewm(span=3).mean() - close.ewm(span=10).mean()
    return _zscore_rolling(base, 126)

def adln_042_chaikin_osc_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_042_chaikin_osc_rank_126d"""
    base = close.ewm(span=3).mean() - close.ewm(span=10).mean()
    return _rank_pct(base, 126)

def adln_043_chaikin_osc_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_043_chaikin_osc_lvl_252d"""
    base = close.ewm(span=3).mean() - close.ewm(span=10).mean()
    return _rolling_mean(base, 252)

def adln_044_chaikin_osc_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_044_chaikin_osc_zscore_252d"""
    base = close.ewm(span=3).mean() - close.ewm(span=10).mean()
    return _zscore_rolling(base, 252)

def adln_045_chaikin_osc_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_045_chaikin_osc_rank_252d"""
    base = close.ewm(span=3).mean() - close.ewm(span=10).mean()
    return _rank_pct(base, 252)

def adln_046_adl_roc_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_046_adl_roc_lvl_5d"""
    base = (((close - low) - (high - close)) / (high - low).replace(0, _EPS) * volume).pct_change()
    return _rolling_mean(base, 5)

def adln_047_adl_roc_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_047_adl_roc_zscore_5d"""
    base = (((close - low) - (high - close)) / (high - low).replace(0, _EPS) * volume).pct_change()
    return _zscore_rolling(base, 5)

def adln_048_adl_roc_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_048_adl_roc_rank_5d"""
    base = (((close - low) - (high - close)) / (high - low).replace(0, _EPS) * volume).pct_change()
    return _rank_pct(base, 5)

def adln_049_adl_roc_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_049_adl_roc_lvl_21d"""
    base = (((close - low) - (high - close)) / (high - low).replace(0, _EPS) * volume).pct_change()
    return _rolling_mean(base, 21)

def adln_050_adl_roc_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_050_adl_roc_zscore_21d"""
    base = (((close - low) - (high - close)) / (high - low).replace(0, _EPS) * volume).pct_change()
    return _zscore_rolling(base, 21)

def adln_051_adl_roc_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_051_adl_roc_rank_21d"""
    base = (((close - low) - (high - close)) / (high - low).replace(0, _EPS) * volume).pct_change()
    return _rank_pct(base, 21)

def adln_052_adl_roc_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_052_adl_roc_lvl_63d"""
    base = (((close - low) - (high - close)) / (high - low).replace(0, _EPS) * volume).pct_change()
    return _rolling_mean(base, 63)

def adln_053_adl_roc_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_053_adl_roc_zscore_63d"""
    base = (((close - low) - (high - close)) / (high - low).replace(0, _EPS) * volume).pct_change()
    return _zscore_rolling(base, 63)

def adln_054_adl_roc_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_054_adl_roc_rank_63d"""
    base = (((close - low) - (high - close)) / (high - low).replace(0, _EPS) * volume).pct_change()
    return _rank_pct(base, 63)

def adln_055_adl_roc_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_055_adl_roc_lvl_126d"""
    base = (((close - low) - (high - close)) / (high - low).replace(0, _EPS) * volume).pct_change()
    return _rolling_mean(base, 126)

def adln_056_adl_roc_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_056_adl_roc_zscore_126d"""
    base = (((close - low) - (high - close)) / (high - low).replace(0, _EPS) * volume).pct_change()
    return _zscore_rolling(base, 126)

def adln_057_adl_roc_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_057_adl_roc_rank_126d"""
    base = (((close - low) - (high - close)) / (high - low).replace(0, _EPS) * volume).pct_change()
    return _rank_pct(base, 126)

def adln_058_adl_roc_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_058_adl_roc_lvl_252d"""
    base = (((close - low) - (high - close)) / (high - low).replace(0, _EPS) * volume).pct_change()
    return _rolling_mean(base, 252)

def adln_059_adl_roc_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_059_adl_roc_zscore_252d"""
    base = (((close - low) - (high - close)) / (high - low).replace(0, _EPS) * volume).pct_change()
    return _zscore_rolling(base, 252)

def adln_060_adl_roc_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_060_adl_roc_rank_252d"""
    base = (((close - low) - (high - close)) / (high - low).replace(0, _EPS) * volume).pct_change()
    return _rank_pct(base, 252)

def adln_061_adl_mfi_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_061_adl_mfi_lvl_5d"""
    base = (((close - low) - (high - close)) / (high - low).replace(0, _EPS) * volume) * close
    return _rolling_mean(base, 5)

def adln_062_adl_mfi_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_062_adl_mfi_zscore_5d"""
    base = (((close - low) - (high - close)) / (high - low).replace(0, _EPS) * volume) * close
    return _zscore_rolling(base, 5)

def adln_063_adl_mfi_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_063_adl_mfi_rank_5d"""
    base = (((close - low) - (high - close)) / (high - low).replace(0, _EPS) * volume) * close
    return _rank_pct(base, 5)

def adln_064_adl_mfi_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_064_adl_mfi_lvl_21d"""
    base = (((close - low) - (high - close)) / (high - low).replace(0, _EPS) * volume) * close
    return _rolling_mean(base, 21)

def adln_065_adl_mfi_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_065_adl_mfi_zscore_21d"""
    base = (((close - low) - (high - close)) / (high - low).replace(0, _EPS) * volume) * close
    return _zscore_rolling(base, 21)

def adln_066_adl_mfi_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_066_adl_mfi_rank_21d"""
    base = (((close - low) - (high - close)) / (high - low).replace(0, _EPS) * volume) * close
    return _rank_pct(base, 21)

def adln_067_adl_mfi_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_067_adl_mfi_lvl_63d"""
    base = (((close - low) - (high - close)) / (high - low).replace(0, _EPS) * volume) * close
    return _rolling_mean(base, 63)

def adln_068_adl_mfi_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_068_adl_mfi_zscore_63d"""
    base = (((close - low) - (high - close)) / (high - low).replace(0, _EPS) * volume) * close
    return _zscore_rolling(base, 63)

def adln_069_adl_mfi_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_069_adl_mfi_rank_63d"""
    base = (((close - low) - (high - close)) / (high - low).replace(0, _EPS) * volume) * close
    return _rank_pct(base, 63)

def adln_070_adl_mfi_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_070_adl_mfi_lvl_126d"""
    base = (((close - low) - (high - close)) / (high - low).replace(0, _EPS) * volume) * close
    return _rolling_mean(base, 126)

def adln_071_adl_mfi_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_071_adl_mfi_zscore_126d"""
    base = (((close - low) - (high - close)) / (high - low).replace(0, _EPS) * volume) * close
    return _zscore_rolling(base, 126)

def adln_072_adl_mfi_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_072_adl_mfi_rank_126d"""
    base = (((close - low) - (high - close)) / (high - low).replace(0, _EPS) * volume) * close
    return _rank_pct(base, 126)

def adln_073_adl_mfi_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_073_adl_mfi_lvl_252d"""
    base = (((close - low) - (high - close)) / (high - low).replace(0, _EPS) * volume) * close
    return _rolling_mean(base, 252)

def adln_074_adl_mfi_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_074_adl_mfi_zscore_252d"""
    base = (((close - low) - (high - close)) / (high - low).replace(0, _EPS) * volume) * close
    return _zscore_rolling(base, 252)

def adln_075_adl_mfi_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """adln_075_adl_mfi_rank_252d"""
    base = (((close - low) - (high - close)) / (high - low).replace(0, _EPS) * volume) * close
    return _rank_pct(base, 252)

# ── Registry ──────────────────────────────────────────────────────────────────
V86_REGISTRY = {
    "adln_001_adl_lvl_5d": {"inputs": ["high", "low", "close", "volume"], "func": adln_001_adl_lvl_5d},
    "adln_002_adl_zscore_5d": {"inputs": ["high", "low", "close", "volume"], "func": adln_002_adl_zscore_5d},
    "adln_003_adl_rank_5d": {"inputs": ["high", "low", "close", "volume"], "func": adln_003_adl_rank_5d},
    "adln_004_adl_lvl_21d": {"inputs": ["high", "low", "close", "volume"], "func": adln_004_adl_lvl_21d},
    "adln_005_adl_zscore_21d": {"inputs": ["high", "low", "close", "volume"], "func": adln_005_adl_zscore_21d},
    "adln_006_adl_rank_21d": {"inputs": ["high", "low", "close", "volume"], "func": adln_006_adl_rank_21d},
    "adln_007_adl_lvl_63d": {"inputs": ["high", "low", "close", "volume"], "func": adln_007_adl_lvl_63d},
    "adln_008_adl_zscore_63d": {"inputs": ["high", "low", "close", "volume"], "func": adln_008_adl_zscore_63d},
    "adln_009_adl_rank_63d": {"inputs": ["high", "low", "close", "volume"], "func": adln_009_adl_rank_63d},
    "adln_010_adl_lvl_126d": {"inputs": ["high", "low", "close", "volume"], "func": adln_010_adl_lvl_126d},
    "adln_011_adl_zscore_126d": {"inputs": ["high", "low", "close", "volume"], "func": adln_011_adl_zscore_126d},
    "adln_012_adl_rank_126d": {"inputs": ["high", "low", "close", "volume"], "func": adln_012_adl_rank_126d},
    "adln_013_adl_lvl_252d": {"inputs": ["high", "low", "close", "volume"], "func": adln_013_adl_lvl_252d},
    "adln_014_adl_zscore_252d": {"inputs": ["high", "low", "close", "volume"], "func": adln_014_adl_zscore_252d},
    "adln_015_adl_rank_252d": {"inputs": ["high", "low", "close", "volume"], "func": adln_015_adl_rank_252d},
    "adln_016_adl_ps_lvl_5d": {"inputs": ["high", "low", "close", "volume"], "func": adln_016_adl_ps_lvl_5d},
    "adln_017_adl_ps_zscore_5d": {"inputs": ["high", "low", "close", "volume"], "func": adln_017_adl_ps_zscore_5d},
    "adln_018_adl_ps_rank_5d": {"inputs": ["high", "low", "close", "volume"], "func": adln_018_adl_ps_rank_5d},
    "adln_019_adl_ps_lvl_21d": {"inputs": ["high", "low", "close", "volume"], "func": adln_019_adl_ps_lvl_21d},
    "adln_020_adl_ps_zscore_21d": {"inputs": ["high", "low", "close", "volume"], "func": adln_020_adl_ps_zscore_21d},
    "adln_021_adl_ps_rank_21d": {"inputs": ["high", "low", "close", "volume"], "func": adln_021_adl_ps_rank_21d},
    "adln_022_adl_ps_lvl_63d": {"inputs": ["high", "low", "close", "volume"], "func": adln_022_adl_ps_lvl_63d},
    "adln_023_adl_ps_zscore_63d": {"inputs": ["high", "low", "close", "volume"], "func": adln_023_adl_ps_zscore_63d},
    "adln_024_adl_ps_rank_63d": {"inputs": ["high", "low", "close", "volume"], "func": adln_024_adl_ps_rank_63d},
    "adln_025_adl_ps_lvl_126d": {"inputs": ["high", "low", "close", "volume"], "func": adln_025_adl_ps_lvl_126d},
    "adln_026_adl_ps_zscore_126d": {"inputs": ["high", "low", "close", "volume"], "func": adln_026_adl_ps_zscore_126d},
    "adln_027_adl_ps_rank_126d": {"inputs": ["high", "low", "close", "volume"], "func": adln_027_adl_ps_rank_126d},
    "adln_028_adl_ps_lvl_252d": {"inputs": ["high", "low", "close", "volume"], "func": adln_028_adl_ps_lvl_252d},
    "adln_029_adl_ps_zscore_252d": {"inputs": ["high", "low", "close", "volume"], "func": adln_029_adl_ps_zscore_252d},
    "adln_030_adl_ps_rank_252d": {"inputs": ["high", "low", "close", "volume"], "func": adln_030_adl_ps_rank_252d},
    "adln_031_chaikin_osc_lvl_5d": {"inputs": ["high", "low", "close", "volume"], "func": adln_031_chaikin_osc_lvl_5d},
    "adln_032_chaikin_osc_zscore_5d": {"inputs": ["high", "low", "close", "volume"], "func": adln_032_chaikin_osc_zscore_5d},
    "adln_033_chaikin_osc_rank_5d": {"inputs": ["high", "low", "close", "volume"], "func": adln_033_chaikin_osc_rank_5d},
    "adln_034_chaikin_osc_lvl_21d": {"inputs": ["high", "low", "close", "volume"], "func": adln_034_chaikin_osc_lvl_21d},
    "adln_035_chaikin_osc_zscore_21d": {"inputs": ["high", "low", "close", "volume"], "func": adln_035_chaikin_osc_zscore_21d},
    "adln_036_chaikin_osc_rank_21d": {"inputs": ["high", "low", "close", "volume"], "func": adln_036_chaikin_osc_rank_21d},
    "adln_037_chaikin_osc_lvl_63d": {"inputs": ["high", "low", "close", "volume"], "func": adln_037_chaikin_osc_lvl_63d},
    "adln_038_chaikin_osc_zscore_63d": {"inputs": ["high", "low", "close", "volume"], "func": adln_038_chaikin_osc_zscore_63d},
    "adln_039_chaikin_osc_rank_63d": {"inputs": ["high", "low", "close", "volume"], "func": adln_039_chaikin_osc_rank_63d},
    "adln_040_chaikin_osc_lvl_126d": {"inputs": ["high", "low", "close", "volume"], "func": adln_040_chaikin_osc_lvl_126d},
    "adln_041_chaikin_osc_zscore_126d": {"inputs": ["high", "low", "close", "volume"], "func": adln_041_chaikin_osc_zscore_126d},
    "adln_042_chaikin_osc_rank_126d": {"inputs": ["high", "low", "close", "volume"], "func": adln_042_chaikin_osc_rank_126d},
    "adln_043_chaikin_osc_lvl_252d": {"inputs": ["high", "low", "close", "volume"], "func": adln_043_chaikin_osc_lvl_252d},
    "adln_044_chaikin_osc_zscore_252d": {"inputs": ["high", "low", "close", "volume"], "func": adln_044_chaikin_osc_zscore_252d},
    "adln_045_chaikin_osc_rank_252d": {"inputs": ["high", "low", "close", "volume"], "func": adln_045_chaikin_osc_rank_252d},
    "adln_046_adl_roc_lvl_5d": {"inputs": ["high", "low", "close", "volume"], "func": adln_046_adl_roc_lvl_5d},
    "adln_047_adl_roc_zscore_5d": {"inputs": ["high", "low", "close", "volume"], "func": adln_047_adl_roc_zscore_5d},
    "adln_048_adl_roc_rank_5d": {"inputs": ["high", "low", "close", "volume"], "func": adln_048_adl_roc_rank_5d},
    "adln_049_adl_roc_lvl_21d": {"inputs": ["high", "low", "close", "volume"], "func": adln_049_adl_roc_lvl_21d},
    "adln_050_adl_roc_zscore_21d": {"inputs": ["high", "low", "close", "volume"], "func": adln_050_adl_roc_zscore_21d},
    "adln_051_adl_roc_rank_21d": {"inputs": ["high", "low", "close", "volume"], "func": adln_051_adl_roc_rank_21d},
    "adln_052_adl_roc_lvl_63d": {"inputs": ["high", "low", "close", "volume"], "func": adln_052_adl_roc_lvl_63d},
    "adln_053_adl_roc_zscore_63d": {"inputs": ["high", "low", "close", "volume"], "func": adln_053_adl_roc_zscore_63d},
    "adln_054_adl_roc_rank_63d": {"inputs": ["high", "low", "close", "volume"], "func": adln_054_adl_roc_rank_63d},
    "adln_055_adl_roc_lvl_126d": {"inputs": ["high", "low", "close", "volume"], "func": adln_055_adl_roc_lvl_126d},
    "adln_056_adl_roc_zscore_126d": {"inputs": ["high", "low", "close", "volume"], "func": adln_056_adl_roc_zscore_126d},
    "adln_057_adl_roc_rank_126d": {"inputs": ["high", "low", "close", "volume"], "func": adln_057_adl_roc_rank_126d},
    "adln_058_adl_roc_lvl_252d": {"inputs": ["high", "low", "close", "volume"], "func": adln_058_adl_roc_lvl_252d},
    "adln_059_adl_roc_zscore_252d": {"inputs": ["high", "low", "close", "volume"], "func": adln_059_adl_roc_zscore_252d},
    "adln_060_adl_roc_rank_252d": {"inputs": ["high", "low", "close", "volume"], "func": adln_060_adl_roc_rank_252d},
    "adln_061_adl_mfi_lvl_5d": {"inputs": ["high", "low", "close", "volume"], "func": adln_061_adl_mfi_lvl_5d},
    "adln_062_adl_mfi_zscore_5d": {"inputs": ["high", "low", "close", "volume"], "func": adln_062_adl_mfi_zscore_5d},
    "adln_063_adl_mfi_rank_5d": {"inputs": ["high", "low", "close", "volume"], "func": adln_063_adl_mfi_rank_5d},
    "adln_064_adl_mfi_lvl_21d": {"inputs": ["high", "low", "close", "volume"], "func": adln_064_adl_mfi_lvl_21d},
    "adln_065_adl_mfi_zscore_21d": {"inputs": ["high", "low", "close", "volume"], "func": adln_065_adl_mfi_zscore_21d},
    "adln_066_adl_mfi_rank_21d": {"inputs": ["high", "low", "close", "volume"], "func": adln_066_adl_mfi_rank_21d},
    "adln_067_adl_mfi_lvl_63d": {"inputs": ["high", "low", "close", "volume"], "func": adln_067_adl_mfi_lvl_63d},
    "adln_068_adl_mfi_zscore_63d": {"inputs": ["high", "low", "close", "volume"], "func": adln_068_adl_mfi_zscore_63d},
    "adln_069_adl_mfi_rank_63d": {"inputs": ["high", "low", "close", "volume"], "func": adln_069_adl_mfi_rank_63d},
    "adln_070_adl_mfi_lvl_126d": {"inputs": ["high", "low", "close", "volume"], "func": adln_070_adl_mfi_lvl_126d},
    "adln_071_adl_mfi_zscore_126d": {"inputs": ["high", "low", "close", "volume"], "func": adln_071_adl_mfi_zscore_126d},
    "adln_072_adl_mfi_rank_126d": {"inputs": ["high", "low", "close", "volume"], "func": adln_072_adl_mfi_rank_126d},
    "adln_073_adl_mfi_lvl_252d": {"inputs": ["high", "low", "close", "volume"], "func": adln_073_adl_mfi_lvl_252d},
    "adln_074_adl_mfi_zscore_252d": {"inputs": ["high", "low", "close", "volume"], "func": adln_074_adl_mfi_zscore_252d},
    "adln_075_adl_mfi_rank_252d": {"inputs": ["high", "low", "close", "volume"], "func": adln_075_adl_mfi_rank_252d},
}
