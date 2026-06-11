"""
94_aroo_dynamics — Base Features 001-075
Domain: aroo_dynamics
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

def aroo_001_aroon_up_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_001_aroon_up_lvl_5d"""
    base = 100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmax(x), raw=True)) / 25
    return _rolling_mean(base, 5)

def aroo_002_aroon_up_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_002_aroon_up_zscore_5d"""
    base = 100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmax(x), raw=True)) / 25
    return _zscore_rolling(base, 5)

def aroo_003_aroon_up_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_003_aroon_up_rank_5d"""
    base = 100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmax(x), raw=True)) / 25
    return _rank_pct(base, 5)

def aroo_004_aroon_up_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_004_aroon_up_lvl_21d"""
    base = 100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmax(x), raw=True)) / 25
    return _rolling_mean(base, 21)

def aroo_005_aroon_up_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_005_aroon_up_zscore_21d"""
    base = 100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmax(x), raw=True)) / 25
    return _zscore_rolling(base, 21)

def aroo_006_aroon_up_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_006_aroon_up_rank_21d"""
    base = 100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmax(x), raw=True)) / 25
    return _rank_pct(base, 21)

def aroo_007_aroon_up_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_007_aroon_up_lvl_63d"""
    base = 100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmax(x), raw=True)) / 25
    return _rolling_mean(base, 63)

def aroo_008_aroon_up_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_008_aroon_up_zscore_63d"""
    base = 100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmax(x), raw=True)) / 25
    return _zscore_rolling(base, 63)

def aroo_009_aroon_up_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_009_aroon_up_rank_63d"""
    base = 100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmax(x), raw=True)) / 25
    return _rank_pct(base, 63)

def aroo_010_aroon_up_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_010_aroon_up_lvl_126d"""
    base = 100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmax(x), raw=True)) / 25
    return _rolling_mean(base, 126)

def aroo_011_aroon_up_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_011_aroon_up_zscore_126d"""
    base = 100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmax(x), raw=True)) / 25
    return _zscore_rolling(base, 126)

def aroo_012_aroon_up_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_012_aroon_up_rank_126d"""
    base = 100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmax(x), raw=True)) / 25
    return _rank_pct(base, 126)

def aroo_013_aroon_up_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_013_aroon_up_lvl_252d"""
    base = 100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmax(x), raw=True)) / 25
    return _rolling_mean(base, 252)

def aroo_014_aroon_up_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_014_aroon_up_zscore_252d"""
    base = 100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmax(x), raw=True)) / 25
    return _zscore_rolling(base, 252)

def aroo_015_aroon_up_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_015_aroon_up_rank_252d"""
    base = 100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmax(x), raw=True)) / 25
    return _rank_pct(base, 252)

def aroo_016_aroon_dn_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_016_aroon_dn_lvl_5d"""
    base = 100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmin(x), raw=True)) / 25
    return _rolling_mean(base, 5)

def aroo_017_aroon_dn_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_017_aroon_dn_zscore_5d"""
    base = 100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmin(x), raw=True)) / 25
    return _zscore_rolling(base, 5)

def aroo_018_aroon_dn_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_018_aroon_dn_rank_5d"""
    base = 100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmin(x), raw=True)) / 25
    return _rank_pct(base, 5)

def aroo_019_aroon_dn_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_019_aroon_dn_lvl_21d"""
    base = 100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmin(x), raw=True)) / 25
    return _rolling_mean(base, 21)

def aroo_020_aroon_dn_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_020_aroon_dn_zscore_21d"""
    base = 100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmin(x), raw=True)) / 25
    return _zscore_rolling(base, 21)

def aroo_021_aroon_dn_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_021_aroon_dn_rank_21d"""
    base = 100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmin(x), raw=True)) / 25
    return _rank_pct(base, 21)

def aroo_022_aroon_dn_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_022_aroon_dn_lvl_63d"""
    base = 100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmin(x), raw=True)) / 25
    return _rolling_mean(base, 63)

def aroo_023_aroon_dn_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_023_aroon_dn_zscore_63d"""
    base = 100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmin(x), raw=True)) / 25
    return _zscore_rolling(base, 63)

def aroo_024_aroon_dn_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_024_aroon_dn_rank_63d"""
    base = 100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmin(x), raw=True)) / 25
    return _rank_pct(base, 63)

def aroo_025_aroon_dn_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_025_aroon_dn_lvl_126d"""
    base = 100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmin(x), raw=True)) / 25
    return _rolling_mean(base, 126)

def aroo_026_aroon_dn_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_026_aroon_dn_zscore_126d"""
    base = 100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmin(x), raw=True)) / 25
    return _zscore_rolling(base, 126)

def aroo_027_aroon_dn_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_027_aroon_dn_rank_126d"""
    base = 100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmin(x), raw=True)) / 25
    return _rank_pct(base, 126)

def aroo_028_aroon_dn_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_028_aroon_dn_lvl_252d"""
    base = 100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmin(x), raw=True)) / 25
    return _rolling_mean(base, 252)

def aroo_029_aroon_dn_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_029_aroon_dn_zscore_252d"""
    base = 100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmin(x), raw=True)) / 25
    return _zscore_rolling(base, 252)

def aroo_030_aroon_dn_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_030_aroon_dn_rank_252d"""
    base = 100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmin(x), raw=True)) / 25
    return _rank_pct(base, 252)

def aroo_031_aroon_osc_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_031_aroon_osc_lvl_5d"""
    base = 100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmax(x), raw=True)) / 25 - 100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmin(x), raw=True)) / 25
    return _rolling_mean(base, 5)

def aroo_032_aroon_osc_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_032_aroon_osc_zscore_5d"""
    base = 100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmax(x), raw=True)) / 25 - 100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmin(x), raw=True)) / 25
    return _zscore_rolling(base, 5)

def aroo_033_aroon_osc_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_033_aroon_osc_rank_5d"""
    base = 100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmax(x), raw=True)) / 25 - 100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmin(x), raw=True)) / 25
    return _rank_pct(base, 5)

def aroo_034_aroon_osc_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_034_aroon_osc_lvl_21d"""
    base = 100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmax(x), raw=True)) / 25 - 100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmin(x), raw=True)) / 25
    return _rolling_mean(base, 21)

def aroo_035_aroon_osc_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_035_aroon_osc_zscore_21d"""
    base = 100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmax(x), raw=True)) / 25 - 100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmin(x), raw=True)) / 25
    return _zscore_rolling(base, 21)

def aroo_036_aroon_osc_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_036_aroon_osc_rank_21d"""
    base = 100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmax(x), raw=True)) / 25 - 100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmin(x), raw=True)) / 25
    return _rank_pct(base, 21)

def aroo_037_aroon_osc_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_037_aroon_osc_lvl_63d"""
    base = 100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmax(x), raw=True)) / 25 - 100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmin(x), raw=True)) / 25
    return _rolling_mean(base, 63)

def aroo_038_aroon_osc_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_038_aroon_osc_zscore_63d"""
    base = 100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmax(x), raw=True)) / 25 - 100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmin(x), raw=True)) / 25
    return _zscore_rolling(base, 63)

def aroo_039_aroon_osc_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_039_aroon_osc_rank_63d"""
    base = 100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmax(x), raw=True)) / 25 - 100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmin(x), raw=True)) / 25
    return _rank_pct(base, 63)

def aroo_040_aroon_osc_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_040_aroon_osc_lvl_126d"""
    base = 100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmax(x), raw=True)) / 25 - 100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmin(x), raw=True)) / 25
    return _rolling_mean(base, 126)

def aroo_041_aroon_osc_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_041_aroon_osc_zscore_126d"""
    base = 100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmax(x), raw=True)) / 25 - 100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmin(x), raw=True)) / 25
    return _zscore_rolling(base, 126)

def aroo_042_aroon_osc_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_042_aroon_osc_rank_126d"""
    base = 100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmax(x), raw=True)) / 25 - 100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmin(x), raw=True)) / 25
    return _rank_pct(base, 126)

def aroo_043_aroon_osc_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_043_aroon_osc_lvl_252d"""
    base = 100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmax(x), raw=True)) / 25 - 100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmin(x), raw=True)) / 25
    return _rolling_mean(base, 252)

def aroo_044_aroon_osc_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_044_aroon_osc_zscore_252d"""
    base = 100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmax(x), raw=True)) / 25 - 100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmin(x), raw=True)) / 25
    return _zscore_rolling(base, 252)

def aroo_045_aroon_osc_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_045_aroon_osc_rank_252d"""
    base = 100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmax(x), raw=True)) / 25 - 100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmin(x), raw=True)) / 25
    return _rank_pct(base, 252)

def aroo_046_aroo_z_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_046_aroo_z_lvl_5d"""
    base = _zscore_rolling(100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmax(x), raw=True)) / 25 - 100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmin(x), raw=True)) / 25, 63)
    return _rolling_mean(base, 5)

def aroo_047_aroo_z_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_047_aroo_z_zscore_5d"""
    base = _zscore_rolling(100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmax(x), raw=True)) / 25 - 100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmin(x), raw=True)) / 25, 63)
    return _zscore_rolling(base, 5)

def aroo_048_aroo_z_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_048_aroo_z_rank_5d"""
    base = _zscore_rolling(100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmax(x), raw=True)) / 25 - 100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmin(x), raw=True)) / 25, 63)
    return _rank_pct(base, 5)

def aroo_049_aroo_z_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_049_aroo_z_lvl_21d"""
    base = _zscore_rolling(100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmax(x), raw=True)) / 25 - 100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmin(x), raw=True)) / 25, 63)
    return _rolling_mean(base, 21)

def aroo_050_aroo_z_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_050_aroo_z_zscore_21d"""
    base = _zscore_rolling(100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmax(x), raw=True)) / 25 - 100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmin(x), raw=True)) / 25, 63)
    return _zscore_rolling(base, 21)

def aroo_051_aroo_z_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_051_aroo_z_rank_21d"""
    base = _zscore_rolling(100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmax(x), raw=True)) / 25 - 100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmin(x), raw=True)) / 25, 63)
    return _rank_pct(base, 21)

def aroo_052_aroo_z_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_052_aroo_z_lvl_63d"""
    base = _zscore_rolling(100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmax(x), raw=True)) / 25 - 100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmin(x), raw=True)) / 25, 63)
    return _rolling_mean(base, 63)

def aroo_053_aroo_z_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_053_aroo_z_zscore_63d"""
    base = _zscore_rolling(100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmax(x), raw=True)) / 25 - 100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmin(x), raw=True)) / 25, 63)
    return _zscore_rolling(base, 63)

def aroo_054_aroo_z_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_054_aroo_z_rank_63d"""
    base = _zscore_rolling(100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmax(x), raw=True)) / 25 - 100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmin(x), raw=True)) / 25, 63)
    return _rank_pct(base, 63)

def aroo_055_aroo_z_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_055_aroo_z_lvl_126d"""
    base = _zscore_rolling(100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmax(x), raw=True)) / 25 - 100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmin(x), raw=True)) / 25, 63)
    return _rolling_mean(base, 126)

def aroo_056_aroo_z_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_056_aroo_z_zscore_126d"""
    base = _zscore_rolling(100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmax(x), raw=True)) / 25 - 100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmin(x), raw=True)) / 25, 63)
    return _zscore_rolling(base, 126)

def aroo_057_aroo_z_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_057_aroo_z_rank_126d"""
    base = _zscore_rolling(100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmax(x), raw=True)) / 25 - 100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmin(x), raw=True)) / 25, 63)
    return _rank_pct(base, 126)

def aroo_058_aroo_z_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_058_aroo_z_lvl_252d"""
    base = _zscore_rolling(100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmax(x), raw=True)) / 25 - 100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmin(x), raw=True)) / 25, 63)
    return _rolling_mean(base, 252)

def aroo_059_aroo_z_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_059_aroo_z_zscore_252d"""
    base = _zscore_rolling(100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmax(x), raw=True)) / 25 - 100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmin(x), raw=True)) / 25, 63)
    return _zscore_rolling(base, 252)

def aroo_060_aroo_z_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_060_aroo_z_rank_252d"""
    base = _zscore_rolling(100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmax(x), raw=True)) / 25 - 100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmin(x), raw=True)) / 25, 63)
    return _rank_pct(base, 252)

def aroo_061_aroo_roc_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_061_aroo_roc_lvl_5d"""
    base = (100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmax(x), raw=True)) / 25 - 100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmin(x), raw=True)) / 25).pct_change()
    return _rolling_mean(base, 5)

def aroo_062_aroo_roc_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_062_aroo_roc_zscore_5d"""
    base = (100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmax(x), raw=True)) / 25 - 100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmin(x), raw=True)) / 25).pct_change()
    return _zscore_rolling(base, 5)

def aroo_063_aroo_roc_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_063_aroo_roc_rank_5d"""
    base = (100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmax(x), raw=True)) / 25 - 100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmin(x), raw=True)) / 25).pct_change()
    return _rank_pct(base, 5)

def aroo_064_aroo_roc_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_064_aroo_roc_lvl_21d"""
    base = (100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmax(x), raw=True)) / 25 - 100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmin(x), raw=True)) / 25).pct_change()
    return _rolling_mean(base, 21)

def aroo_065_aroo_roc_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_065_aroo_roc_zscore_21d"""
    base = (100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmax(x), raw=True)) / 25 - 100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmin(x), raw=True)) / 25).pct_change()
    return _zscore_rolling(base, 21)

def aroo_066_aroo_roc_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_066_aroo_roc_rank_21d"""
    base = (100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmax(x), raw=True)) / 25 - 100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmin(x), raw=True)) / 25).pct_change()
    return _rank_pct(base, 21)

def aroo_067_aroo_roc_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_067_aroo_roc_lvl_63d"""
    base = (100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmax(x), raw=True)) / 25 - 100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmin(x), raw=True)) / 25).pct_change()
    return _rolling_mean(base, 63)

def aroo_068_aroo_roc_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_068_aroo_roc_zscore_63d"""
    base = (100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmax(x), raw=True)) / 25 - 100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmin(x), raw=True)) / 25).pct_change()
    return _zscore_rolling(base, 63)

def aroo_069_aroo_roc_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_069_aroo_roc_rank_63d"""
    base = (100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmax(x), raw=True)) / 25 - 100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmin(x), raw=True)) / 25).pct_change()
    return _rank_pct(base, 63)

def aroo_070_aroo_roc_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_070_aroo_roc_lvl_126d"""
    base = (100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmax(x), raw=True)) / 25 - 100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmin(x), raw=True)) / 25).pct_change()
    return _rolling_mean(base, 126)

def aroo_071_aroo_roc_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_071_aroo_roc_zscore_126d"""
    base = (100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmax(x), raw=True)) / 25 - 100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmin(x), raw=True)) / 25).pct_change()
    return _zscore_rolling(base, 126)

def aroo_072_aroo_roc_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_072_aroo_roc_rank_126d"""
    base = (100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmax(x), raw=True)) / 25 - 100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmin(x), raw=True)) / 25).pct_change()
    return _rank_pct(base, 126)

def aroo_073_aroo_roc_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_073_aroo_roc_lvl_252d"""
    base = (100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmax(x), raw=True)) / 25 - 100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmin(x), raw=True)) / 25).pct_change()
    return _rolling_mean(base, 252)

def aroo_074_aroo_roc_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_074_aroo_roc_zscore_252d"""
    base = (100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmax(x), raw=True)) / 25 - 100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmin(x), raw=True)) / 25).pct_change()
    return _zscore_rolling(base, 252)

def aroo_075_aroo_roc_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """aroo_075_aroo_roc_rank_252d"""
    base = (100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmax(x), raw=True)) / 25 - 100 * (25 - close.rolling(25).apply(lambda x: 24 - np.argmin(x), raw=True)) / 25).pct_change()
    return _rank_pct(base, 252)

# ── Registry ──────────────────────────────────────────────────────────────────
V94_REGISTRY = {
    "aroo_001_aroon_up_lvl_5d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_001_aroon_up_lvl_5d},
    "aroo_002_aroon_up_zscore_5d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_002_aroon_up_zscore_5d},
    "aroo_003_aroon_up_rank_5d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_003_aroon_up_rank_5d},
    "aroo_004_aroon_up_lvl_21d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_004_aroon_up_lvl_21d},
    "aroo_005_aroon_up_zscore_21d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_005_aroon_up_zscore_21d},
    "aroo_006_aroon_up_rank_21d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_006_aroon_up_rank_21d},
    "aroo_007_aroon_up_lvl_63d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_007_aroon_up_lvl_63d},
    "aroo_008_aroon_up_zscore_63d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_008_aroon_up_zscore_63d},
    "aroo_009_aroon_up_rank_63d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_009_aroon_up_rank_63d},
    "aroo_010_aroon_up_lvl_126d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_010_aroon_up_lvl_126d},
    "aroo_011_aroon_up_zscore_126d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_011_aroon_up_zscore_126d},
    "aroo_012_aroon_up_rank_126d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_012_aroon_up_rank_126d},
    "aroo_013_aroon_up_lvl_252d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_013_aroon_up_lvl_252d},
    "aroo_014_aroon_up_zscore_252d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_014_aroon_up_zscore_252d},
    "aroo_015_aroon_up_rank_252d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_015_aroon_up_rank_252d},
    "aroo_016_aroon_dn_lvl_5d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_016_aroon_dn_lvl_5d},
    "aroo_017_aroon_dn_zscore_5d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_017_aroon_dn_zscore_5d},
    "aroo_018_aroon_dn_rank_5d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_018_aroon_dn_rank_5d},
    "aroo_019_aroon_dn_lvl_21d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_019_aroon_dn_lvl_21d},
    "aroo_020_aroon_dn_zscore_21d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_020_aroon_dn_zscore_21d},
    "aroo_021_aroon_dn_rank_21d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_021_aroon_dn_rank_21d},
    "aroo_022_aroon_dn_lvl_63d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_022_aroon_dn_lvl_63d},
    "aroo_023_aroon_dn_zscore_63d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_023_aroon_dn_zscore_63d},
    "aroo_024_aroon_dn_rank_63d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_024_aroon_dn_rank_63d},
    "aroo_025_aroon_dn_lvl_126d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_025_aroon_dn_lvl_126d},
    "aroo_026_aroon_dn_zscore_126d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_026_aroon_dn_zscore_126d},
    "aroo_027_aroon_dn_rank_126d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_027_aroon_dn_rank_126d},
    "aroo_028_aroon_dn_lvl_252d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_028_aroon_dn_lvl_252d},
    "aroo_029_aroon_dn_zscore_252d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_029_aroon_dn_zscore_252d},
    "aroo_030_aroon_dn_rank_252d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_030_aroon_dn_rank_252d},
    "aroo_031_aroon_osc_lvl_5d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_031_aroon_osc_lvl_5d},
    "aroo_032_aroon_osc_zscore_5d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_032_aroon_osc_zscore_5d},
    "aroo_033_aroon_osc_rank_5d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_033_aroon_osc_rank_5d},
    "aroo_034_aroon_osc_lvl_21d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_034_aroon_osc_lvl_21d},
    "aroo_035_aroon_osc_zscore_21d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_035_aroon_osc_zscore_21d},
    "aroo_036_aroon_osc_rank_21d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_036_aroon_osc_rank_21d},
    "aroo_037_aroon_osc_lvl_63d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_037_aroon_osc_lvl_63d},
    "aroo_038_aroon_osc_zscore_63d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_038_aroon_osc_zscore_63d},
    "aroo_039_aroon_osc_rank_63d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_039_aroon_osc_rank_63d},
    "aroo_040_aroon_osc_lvl_126d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_040_aroon_osc_lvl_126d},
    "aroo_041_aroon_osc_zscore_126d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_041_aroon_osc_zscore_126d},
    "aroo_042_aroon_osc_rank_126d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_042_aroon_osc_rank_126d},
    "aroo_043_aroon_osc_lvl_252d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_043_aroon_osc_lvl_252d},
    "aroo_044_aroon_osc_zscore_252d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_044_aroon_osc_zscore_252d},
    "aroo_045_aroon_osc_rank_252d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_045_aroon_osc_rank_252d},
    "aroo_046_aroo_z_lvl_5d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_046_aroo_z_lvl_5d},
    "aroo_047_aroo_z_zscore_5d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_047_aroo_z_zscore_5d},
    "aroo_048_aroo_z_rank_5d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_048_aroo_z_rank_5d},
    "aroo_049_aroo_z_lvl_21d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_049_aroo_z_lvl_21d},
    "aroo_050_aroo_z_zscore_21d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_050_aroo_z_zscore_21d},
    "aroo_051_aroo_z_rank_21d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_051_aroo_z_rank_21d},
    "aroo_052_aroo_z_lvl_63d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_052_aroo_z_lvl_63d},
    "aroo_053_aroo_z_zscore_63d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_053_aroo_z_zscore_63d},
    "aroo_054_aroo_z_rank_63d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_054_aroo_z_rank_63d},
    "aroo_055_aroo_z_lvl_126d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_055_aroo_z_lvl_126d},
    "aroo_056_aroo_z_zscore_126d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_056_aroo_z_zscore_126d},
    "aroo_057_aroo_z_rank_126d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_057_aroo_z_rank_126d},
    "aroo_058_aroo_z_lvl_252d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_058_aroo_z_lvl_252d},
    "aroo_059_aroo_z_zscore_252d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_059_aroo_z_zscore_252d},
    "aroo_060_aroo_z_rank_252d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_060_aroo_z_rank_252d},
    "aroo_061_aroo_roc_lvl_5d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_061_aroo_roc_lvl_5d},
    "aroo_062_aroo_roc_zscore_5d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_062_aroo_roc_zscore_5d},
    "aroo_063_aroo_roc_rank_5d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_063_aroo_roc_rank_5d},
    "aroo_064_aroo_roc_lvl_21d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_064_aroo_roc_lvl_21d},
    "aroo_065_aroo_roc_zscore_21d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_065_aroo_roc_zscore_21d},
    "aroo_066_aroo_roc_rank_21d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_066_aroo_roc_rank_21d},
    "aroo_067_aroo_roc_lvl_63d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_067_aroo_roc_lvl_63d},
    "aroo_068_aroo_roc_zscore_63d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_068_aroo_roc_zscore_63d},
    "aroo_069_aroo_roc_rank_63d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_069_aroo_roc_rank_63d},
    "aroo_070_aroo_roc_lvl_126d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_070_aroo_roc_lvl_126d},
    "aroo_071_aroo_roc_zscore_126d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_071_aroo_roc_zscore_126d},
    "aroo_072_aroo_roc_rank_126d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_072_aroo_roc_rank_126d},
    "aroo_073_aroo_roc_lvl_252d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_073_aroo_roc_lvl_252d},
    "aroo_074_aroo_roc_zscore_252d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_074_aroo_roc_zscore_252d},
    "aroo_075_aroo_roc_rank_252d": {"inputs": ["high", "low", "close", "volume"], "func": aroo_075_aroo_roc_rank_252d},
}
