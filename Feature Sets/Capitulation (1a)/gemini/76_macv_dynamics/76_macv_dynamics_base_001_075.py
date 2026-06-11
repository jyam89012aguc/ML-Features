"""
76_macv_dynamics — Base Features 001-075
Domain: macv_dynamics
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

def macv_001_macd_lvl_5d(close: pd.Series) -> pd.Series:
    """macv_001_macd_lvl_5d"""
    base = _ewm_mean(close, 12) - _ewm_mean(close, 26)
    return _rolling_mean(base, 5)

def macv_002_macd_zscore_5d(close: pd.Series) -> pd.Series:
    """macv_002_macd_zscore_5d"""
    base = _ewm_mean(close, 12) - _ewm_mean(close, 26)
    return _zscore_rolling(base, 5)

def macv_003_macd_rank_5d(close: pd.Series) -> pd.Series:
    """macv_003_macd_rank_5d"""
    base = _ewm_mean(close, 12) - _ewm_mean(close, 26)
    return _rank_pct(base, 5)

def macv_004_macd_lvl_21d(close: pd.Series) -> pd.Series:
    """macv_004_macd_lvl_21d"""
    base = _ewm_mean(close, 12) - _ewm_mean(close, 26)
    return _rolling_mean(base, 21)

def macv_005_macd_zscore_21d(close: pd.Series) -> pd.Series:
    """macv_005_macd_zscore_21d"""
    base = _ewm_mean(close, 12) - _ewm_mean(close, 26)
    return _zscore_rolling(base, 21)

def macv_006_macd_rank_21d(close: pd.Series) -> pd.Series:
    """macv_006_macd_rank_21d"""
    base = _ewm_mean(close, 12) - _ewm_mean(close, 26)
    return _rank_pct(base, 21)

def macv_007_macd_lvl_63d(close: pd.Series) -> pd.Series:
    """macv_007_macd_lvl_63d"""
    base = _ewm_mean(close, 12) - _ewm_mean(close, 26)
    return _rolling_mean(base, 63)

def macv_008_macd_zscore_63d(close: pd.Series) -> pd.Series:
    """macv_008_macd_zscore_63d"""
    base = _ewm_mean(close, 12) - _ewm_mean(close, 26)
    return _zscore_rolling(base, 63)

def macv_009_macd_rank_63d(close: pd.Series) -> pd.Series:
    """macv_009_macd_rank_63d"""
    base = _ewm_mean(close, 12) - _ewm_mean(close, 26)
    return _rank_pct(base, 63)

def macv_010_macd_lvl_126d(close: pd.Series) -> pd.Series:
    """macv_010_macd_lvl_126d"""
    base = _ewm_mean(close, 12) - _ewm_mean(close, 26)
    return _rolling_mean(base, 126)

def macv_011_macd_zscore_126d(close: pd.Series) -> pd.Series:
    """macv_011_macd_zscore_126d"""
    base = _ewm_mean(close, 12) - _ewm_mean(close, 26)
    return _zscore_rolling(base, 126)

def macv_012_macd_rank_126d(close: pd.Series) -> pd.Series:
    """macv_012_macd_rank_126d"""
    base = _ewm_mean(close, 12) - _ewm_mean(close, 26)
    return _rank_pct(base, 126)

def macv_013_macd_lvl_252d(close: pd.Series) -> pd.Series:
    """macv_013_macd_lvl_252d"""
    base = _ewm_mean(close, 12) - _ewm_mean(close, 26)
    return _rolling_mean(base, 252)

def macv_014_macd_zscore_252d(close: pd.Series) -> pd.Series:
    """macv_014_macd_zscore_252d"""
    base = _ewm_mean(close, 12) - _ewm_mean(close, 26)
    return _zscore_rolling(base, 252)

def macv_015_macd_rank_252d(close: pd.Series) -> pd.Series:
    """macv_015_macd_rank_252d"""
    base = _ewm_mean(close, 12) - _ewm_mean(close, 26)
    return _rank_pct(base, 252)

def macv_016_signal_lvl_5d(close: pd.Series) -> pd.Series:
    """macv_016_signal_lvl_5d"""
    base = _ewm_mean(_ewm_mean(close, 12) - _ewm_mean(close, 26), 9)
    return _rolling_mean(base, 5)

def macv_017_signal_zscore_5d(close: pd.Series) -> pd.Series:
    """macv_017_signal_zscore_5d"""
    base = _ewm_mean(_ewm_mean(close, 12) - _ewm_mean(close, 26), 9)
    return _zscore_rolling(base, 5)

def macv_018_signal_rank_5d(close: pd.Series) -> pd.Series:
    """macv_018_signal_rank_5d"""
    base = _ewm_mean(_ewm_mean(close, 12) - _ewm_mean(close, 26), 9)
    return _rank_pct(base, 5)

def macv_019_signal_lvl_21d(close: pd.Series) -> pd.Series:
    """macv_019_signal_lvl_21d"""
    base = _ewm_mean(_ewm_mean(close, 12) - _ewm_mean(close, 26), 9)
    return _rolling_mean(base, 21)

def macv_020_signal_zscore_21d(close: pd.Series) -> pd.Series:
    """macv_020_signal_zscore_21d"""
    base = _ewm_mean(_ewm_mean(close, 12) - _ewm_mean(close, 26), 9)
    return _zscore_rolling(base, 21)

def macv_021_signal_rank_21d(close: pd.Series) -> pd.Series:
    """macv_021_signal_rank_21d"""
    base = _ewm_mean(_ewm_mean(close, 12) - _ewm_mean(close, 26), 9)
    return _rank_pct(base, 21)

def macv_022_signal_lvl_63d(close: pd.Series) -> pd.Series:
    """macv_022_signal_lvl_63d"""
    base = _ewm_mean(_ewm_mean(close, 12) - _ewm_mean(close, 26), 9)
    return _rolling_mean(base, 63)

def macv_023_signal_zscore_63d(close: pd.Series) -> pd.Series:
    """macv_023_signal_zscore_63d"""
    base = _ewm_mean(_ewm_mean(close, 12) - _ewm_mean(close, 26), 9)
    return _zscore_rolling(base, 63)

def macv_024_signal_rank_63d(close: pd.Series) -> pd.Series:
    """macv_024_signal_rank_63d"""
    base = _ewm_mean(_ewm_mean(close, 12) - _ewm_mean(close, 26), 9)
    return _rank_pct(base, 63)

def macv_025_signal_lvl_126d(close: pd.Series) -> pd.Series:
    """macv_025_signal_lvl_126d"""
    base = _ewm_mean(_ewm_mean(close, 12) - _ewm_mean(close, 26), 9)
    return _rolling_mean(base, 126)

def macv_026_signal_zscore_126d(close: pd.Series) -> pd.Series:
    """macv_026_signal_zscore_126d"""
    base = _ewm_mean(_ewm_mean(close, 12) - _ewm_mean(close, 26), 9)
    return _zscore_rolling(base, 126)

def macv_027_signal_rank_126d(close: pd.Series) -> pd.Series:
    """macv_027_signal_rank_126d"""
    base = _ewm_mean(_ewm_mean(close, 12) - _ewm_mean(close, 26), 9)
    return _rank_pct(base, 126)

def macv_028_signal_lvl_252d(close: pd.Series) -> pd.Series:
    """macv_028_signal_lvl_252d"""
    base = _ewm_mean(_ewm_mean(close, 12) - _ewm_mean(close, 26), 9)
    return _rolling_mean(base, 252)

def macv_029_signal_zscore_252d(close: pd.Series) -> pd.Series:
    """macv_029_signal_zscore_252d"""
    base = _ewm_mean(_ewm_mean(close, 12) - _ewm_mean(close, 26), 9)
    return _zscore_rolling(base, 252)

def macv_030_signal_rank_252d(close: pd.Series) -> pd.Series:
    """macv_030_signal_rank_252d"""
    base = _ewm_mean(_ewm_mean(close, 12) - _ewm_mean(close, 26), 9)
    return _rank_pct(base, 252)

def macv_031_hist_lvl_5d(close: pd.Series) -> pd.Series:
    """macv_031_hist_lvl_5d"""
    base = (_ewm_mean(close, 12) - _ewm_mean(close, 26)) - _ewm_mean(_ewm_mean(close, 12) - _ewm_mean(close, 26), 9)
    return _rolling_mean(base, 5)

def macv_032_hist_zscore_5d(close: pd.Series) -> pd.Series:
    """macv_032_hist_zscore_5d"""
    base = (_ewm_mean(close, 12) - _ewm_mean(close, 26)) - _ewm_mean(_ewm_mean(close, 12) - _ewm_mean(close, 26), 9)
    return _zscore_rolling(base, 5)

def macv_033_hist_rank_5d(close: pd.Series) -> pd.Series:
    """macv_033_hist_rank_5d"""
    base = (_ewm_mean(close, 12) - _ewm_mean(close, 26)) - _ewm_mean(_ewm_mean(close, 12) - _ewm_mean(close, 26), 9)
    return _rank_pct(base, 5)

def macv_034_hist_lvl_21d(close: pd.Series) -> pd.Series:
    """macv_034_hist_lvl_21d"""
    base = (_ewm_mean(close, 12) - _ewm_mean(close, 26)) - _ewm_mean(_ewm_mean(close, 12) - _ewm_mean(close, 26), 9)
    return _rolling_mean(base, 21)

def macv_035_hist_zscore_21d(close: pd.Series) -> pd.Series:
    """macv_035_hist_zscore_21d"""
    base = (_ewm_mean(close, 12) - _ewm_mean(close, 26)) - _ewm_mean(_ewm_mean(close, 12) - _ewm_mean(close, 26), 9)
    return _zscore_rolling(base, 21)

def macv_036_hist_rank_21d(close: pd.Series) -> pd.Series:
    """macv_036_hist_rank_21d"""
    base = (_ewm_mean(close, 12) - _ewm_mean(close, 26)) - _ewm_mean(_ewm_mean(close, 12) - _ewm_mean(close, 26), 9)
    return _rank_pct(base, 21)

def macv_037_hist_lvl_63d(close: pd.Series) -> pd.Series:
    """macv_037_hist_lvl_63d"""
    base = (_ewm_mean(close, 12) - _ewm_mean(close, 26)) - _ewm_mean(_ewm_mean(close, 12) - _ewm_mean(close, 26), 9)
    return _rolling_mean(base, 63)

def macv_038_hist_zscore_63d(close: pd.Series) -> pd.Series:
    """macv_038_hist_zscore_63d"""
    base = (_ewm_mean(close, 12) - _ewm_mean(close, 26)) - _ewm_mean(_ewm_mean(close, 12) - _ewm_mean(close, 26), 9)
    return _zscore_rolling(base, 63)

def macv_039_hist_rank_63d(close: pd.Series) -> pd.Series:
    """macv_039_hist_rank_63d"""
    base = (_ewm_mean(close, 12) - _ewm_mean(close, 26)) - _ewm_mean(_ewm_mean(close, 12) - _ewm_mean(close, 26), 9)
    return _rank_pct(base, 63)

def macv_040_hist_lvl_126d(close: pd.Series) -> pd.Series:
    """macv_040_hist_lvl_126d"""
    base = (_ewm_mean(close, 12) - _ewm_mean(close, 26)) - _ewm_mean(_ewm_mean(close, 12) - _ewm_mean(close, 26), 9)
    return _rolling_mean(base, 126)

def macv_041_hist_zscore_126d(close: pd.Series) -> pd.Series:
    """macv_041_hist_zscore_126d"""
    base = (_ewm_mean(close, 12) - _ewm_mean(close, 26)) - _ewm_mean(_ewm_mean(close, 12) - _ewm_mean(close, 26), 9)
    return _zscore_rolling(base, 126)

def macv_042_hist_rank_126d(close: pd.Series) -> pd.Series:
    """macv_042_hist_rank_126d"""
    base = (_ewm_mean(close, 12) - _ewm_mean(close, 26)) - _ewm_mean(_ewm_mean(close, 12) - _ewm_mean(close, 26), 9)
    return _rank_pct(base, 126)

def macv_043_hist_lvl_252d(close: pd.Series) -> pd.Series:
    """macv_043_hist_lvl_252d"""
    base = (_ewm_mean(close, 12) - _ewm_mean(close, 26)) - _ewm_mean(_ewm_mean(close, 12) - _ewm_mean(close, 26), 9)
    return _rolling_mean(base, 252)

def macv_044_hist_zscore_252d(close: pd.Series) -> pd.Series:
    """macv_044_hist_zscore_252d"""
    base = (_ewm_mean(close, 12) - _ewm_mean(close, 26)) - _ewm_mean(_ewm_mean(close, 12) - _ewm_mean(close, 26), 9)
    return _zscore_rolling(base, 252)

def macv_045_hist_rank_252d(close: pd.Series) -> pd.Series:
    """macv_045_hist_rank_252d"""
    base = (_ewm_mean(close, 12) - _ewm_mean(close, 26)) - _ewm_mean(_ewm_mean(close, 12) - _ewm_mean(close, 26), 9)
    return _rank_pct(base, 252)

def macv_046_macd_rat_lvl_5d(close: pd.Series) -> pd.Series:
    """macv_046_macd_rat_lvl_5d"""
    base = _safe_div(_ewm_mean(close, 12) - _ewm_mean(close, 26), close)
    return _rolling_mean(base, 5)

def macv_047_macd_rat_zscore_5d(close: pd.Series) -> pd.Series:
    """macv_047_macd_rat_zscore_5d"""
    base = _safe_div(_ewm_mean(close, 12) - _ewm_mean(close, 26), close)
    return _zscore_rolling(base, 5)

def macv_048_macd_rat_rank_5d(close: pd.Series) -> pd.Series:
    """macv_048_macd_rat_rank_5d"""
    base = _safe_div(_ewm_mean(close, 12) - _ewm_mean(close, 26), close)
    return _rank_pct(base, 5)

def macv_049_macd_rat_lvl_21d(close: pd.Series) -> pd.Series:
    """macv_049_macd_rat_lvl_21d"""
    base = _safe_div(_ewm_mean(close, 12) - _ewm_mean(close, 26), close)
    return _rolling_mean(base, 21)

def macv_050_macd_rat_zscore_21d(close: pd.Series) -> pd.Series:
    """macv_050_macd_rat_zscore_21d"""
    base = _safe_div(_ewm_mean(close, 12) - _ewm_mean(close, 26), close)
    return _zscore_rolling(base, 21)

def macv_051_macd_rat_rank_21d(close: pd.Series) -> pd.Series:
    """macv_051_macd_rat_rank_21d"""
    base = _safe_div(_ewm_mean(close, 12) - _ewm_mean(close, 26), close)
    return _rank_pct(base, 21)

def macv_052_macd_rat_lvl_63d(close: pd.Series) -> pd.Series:
    """macv_052_macd_rat_lvl_63d"""
    base = _safe_div(_ewm_mean(close, 12) - _ewm_mean(close, 26), close)
    return _rolling_mean(base, 63)

def macv_053_macd_rat_zscore_63d(close: pd.Series) -> pd.Series:
    """macv_053_macd_rat_zscore_63d"""
    base = _safe_div(_ewm_mean(close, 12) - _ewm_mean(close, 26), close)
    return _zscore_rolling(base, 63)

def macv_054_macd_rat_rank_63d(close: pd.Series) -> pd.Series:
    """macv_054_macd_rat_rank_63d"""
    base = _safe_div(_ewm_mean(close, 12) - _ewm_mean(close, 26), close)
    return _rank_pct(base, 63)

def macv_055_macd_rat_lvl_126d(close: pd.Series) -> pd.Series:
    """macv_055_macd_rat_lvl_126d"""
    base = _safe_div(_ewm_mean(close, 12) - _ewm_mean(close, 26), close)
    return _rolling_mean(base, 126)

def macv_056_macd_rat_zscore_126d(close: pd.Series) -> pd.Series:
    """macv_056_macd_rat_zscore_126d"""
    base = _safe_div(_ewm_mean(close, 12) - _ewm_mean(close, 26), close)
    return _zscore_rolling(base, 126)

def macv_057_macd_rat_rank_126d(close: pd.Series) -> pd.Series:
    """macv_057_macd_rat_rank_126d"""
    base = _safe_div(_ewm_mean(close, 12) - _ewm_mean(close, 26), close)
    return _rank_pct(base, 126)

def macv_058_macd_rat_lvl_252d(close: pd.Series) -> pd.Series:
    """macv_058_macd_rat_lvl_252d"""
    base = _safe_div(_ewm_mean(close, 12) - _ewm_mean(close, 26), close)
    return _rolling_mean(base, 252)

def macv_059_macd_rat_zscore_252d(close: pd.Series) -> pd.Series:
    """macv_059_macd_rat_zscore_252d"""
    base = _safe_div(_ewm_mean(close, 12) - _ewm_mean(close, 26), close)
    return _zscore_rolling(base, 252)

def macv_060_macd_rat_rank_252d(close: pd.Series) -> pd.Series:
    """macv_060_macd_rat_rank_252d"""
    base = _safe_div(_ewm_mean(close, 12) - _ewm_mean(close, 26), close)
    return _rank_pct(base, 252)

def macv_061_macd_z_lvl_5d(close: pd.Series) -> pd.Series:
    """macv_061_macd_z_lvl_5d"""
    base = _zscore_rolling(_ewm_mean(close, 12) - _ewm_mean(close, 26), 63)
    return _rolling_mean(base, 5)

def macv_062_macd_z_zscore_5d(close: pd.Series) -> pd.Series:
    """macv_062_macd_z_zscore_5d"""
    base = _zscore_rolling(_ewm_mean(close, 12) - _ewm_mean(close, 26), 63)
    return _zscore_rolling(base, 5)

def macv_063_macd_z_rank_5d(close: pd.Series) -> pd.Series:
    """macv_063_macd_z_rank_5d"""
    base = _zscore_rolling(_ewm_mean(close, 12) - _ewm_mean(close, 26), 63)
    return _rank_pct(base, 5)

def macv_064_macd_z_lvl_21d(close: pd.Series) -> pd.Series:
    """macv_064_macd_z_lvl_21d"""
    base = _zscore_rolling(_ewm_mean(close, 12) - _ewm_mean(close, 26), 63)
    return _rolling_mean(base, 21)

def macv_065_macd_z_zscore_21d(close: pd.Series) -> pd.Series:
    """macv_065_macd_z_zscore_21d"""
    base = _zscore_rolling(_ewm_mean(close, 12) - _ewm_mean(close, 26), 63)
    return _zscore_rolling(base, 21)

def macv_066_macd_z_rank_21d(close: pd.Series) -> pd.Series:
    """macv_066_macd_z_rank_21d"""
    base = _zscore_rolling(_ewm_mean(close, 12) - _ewm_mean(close, 26), 63)
    return _rank_pct(base, 21)

def macv_067_macd_z_lvl_63d(close: pd.Series) -> pd.Series:
    """macv_067_macd_z_lvl_63d"""
    base = _zscore_rolling(_ewm_mean(close, 12) - _ewm_mean(close, 26), 63)
    return _rolling_mean(base, 63)

def macv_068_macd_z_zscore_63d(close: pd.Series) -> pd.Series:
    """macv_068_macd_z_zscore_63d"""
    base = _zscore_rolling(_ewm_mean(close, 12) - _ewm_mean(close, 26), 63)
    return _zscore_rolling(base, 63)

def macv_069_macd_z_rank_63d(close: pd.Series) -> pd.Series:
    """macv_069_macd_z_rank_63d"""
    base = _zscore_rolling(_ewm_mean(close, 12) - _ewm_mean(close, 26), 63)
    return _rank_pct(base, 63)

def macv_070_macd_z_lvl_126d(close: pd.Series) -> pd.Series:
    """macv_070_macd_z_lvl_126d"""
    base = _zscore_rolling(_ewm_mean(close, 12) - _ewm_mean(close, 26), 63)
    return _rolling_mean(base, 126)

def macv_071_macd_z_zscore_126d(close: pd.Series) -> pd.Series:
    """macv_071_macd_z_zscore_126d"""
    base = _zscore_rolling(_ewm_mean(close, 12) - _ewm_mean(close, 26), 63)
    return _zscore_rolling(base, 126)

def macv_072_macd_z_rank_126d(close: pd.Series) -> pd.Series:
    """macv_072_macd_z_rank_126d"""
    base = _zscore_rolling(_ewm_mean(close, 12) - _ewm_mean(close, 26), 63)
    return _rank_pct(base, 126)

def macv_073_macd_z_lvl_252d(close: pd.Series) -> pd.Series:
    """macv_073_macd_z_lvl_252d"""
    base = _zscore_rolling(_ewm_mean(close, 12) - _ewm_mean(close, 26), 63)
    return _rolling_mean(base, 252)

def macv_074_macd_z_zscore_252d(close: pd.Series) -> pd.Series:
    """macv_074_macd_z_zscore_252d"""
    base = _zscore_rolling(_ewm_mean(close, 12) - _ewm_mean(close, 26), 63)
    return _zscore_rolling(base, 252)

def macv_075_macd_z_rank_252d(close: pd.Series) -> pd.Series:
    """macv_075_macd_z_rank_252d"""
    base = _zscore_rolling(_ewm_mean(close, 12) - _ewm_mean(close, 26), 63)
    return _rank_pct(base, 252)

# ── Registry ──────────────────────────────────────────────────────────────────
V76_REGISTRY = {
    "macv_001_macd_lvl_5d": {"inputs": ["close"], "func": macv_001_macd_lvl_5d},
    "macv_002_macd_zscore_5d": {"inputs": ["close"], "func": macv_002_macd_zscore_5d},
    "macv_003_macd_rank_5d": {"inputs": ["close"], "func": macv_003_macd_rank_5d},
    "macv_004_macd_lvl_21d": {"inputs": ["close"], "func": macv_004_macd_lvl_21d},
    "macv_005_macd_zscore_21d": {"inputs": ["close"], "func": macv_005_macd_zscore_21d},
    "macv_006_macd_rank_21d": {"inputs": ["close"], "func": macv_006_macd_rank_21d},
    "macv_007_macd_lvl_63d": {"inputs": ["close"], "func": macv_007_macd_lvl_63d},
    "macv_008_macd_zscore_63d": {"inputs": ["close"], "func": macv_008_macd_zscore_63d},
    "macv_009_macd_rank_63d": {"inputs": ["close"], "func": macv_009_macd_rank_63d},
    "macv_010_macd_lvl_126d": {"inputs": ["close"], "func": macv_010_macd_lvl_126d},
    "macv_011_macd_zscore_126d": {"inputs": ["close"], "func": macv_011_macd_zscore_126d},
    "macv_012_macd_rank_126d": {"inputs": ["close"], "func": macv_012_macd_rank_126d},
    "macv_013_macd_lvl_252d": {"inputs": ["close"], "func": macv_013_macd_lvl_252d},
    "macv_014_macd_zscore_252d": {"inputs": ["close"], "func": macv_014_macd_zscore_252d},
    "macv_015_macd_rank_252d": {"inputs": ["close"], "func": macv_015_macd_rank_252d},
    "macv_016_signal_lvl_5d": {"inputs": ["close"], "func": macv_016_signal_lvl_5d},
    "macv_017_signal_zscore_5d": {"inputs": ["close"], "func": macv_017_signal_zscore_5d},
    "macv_018_signal_rank_5d": {"inputs": ["close"], "func": macv_018_signal_rank_5d},
    "macv_019_signal_lvl_21d": {"inputs": ["close"], "func": macv_019_signal_lvl_21d},
    "macv_020_signal_zscore_21d": {"inputs": ["close"], "func": macv_020_signal_zscore_21d},
    "macv_021_signal_rank_21d": {"inputs": ["close"], "func": macv_021_signal_rank_21d},
    "macv_022_signal_lvl_63d": {"inputs": ["close"], "func": macv_022_signal_lvl_63d},
    "macv_023_signal_zscore_63d": {"inputs": ["close"], "func": macv_023_signal_zscore_63d},
    "macv_024_signal_rank_63d": {"inputs": ["close"], "func": macv_024_signal_rank_63d},
    "macv_025_signal_lvl_126d": {"inputs": ["close"], "func": macv_025_signal_lvl_126d},
    "macv_026_signal_zscore_126d": {"inputs": ["close"], "func": macv_026_signal_zscore_126d},
    "macv_027_signal_rank_126d": {"inputs": ["close"], "func": macv_027_signal_rank_126d},
    "macv_028_signal_lvl_252d": {"inputs": ["close"], "func": macv_028_signal_lvl_252d},
    "macv_029_signal_zscore_252d": {"inputs": ["close"], "func": macv_029_signal_zscore_252d},
    "macv_030_signal_rank_252d": {"inputs": ["close"], "func": macv_030_signal_rank_252d},
    "macv_031_hist_lvl_5d": {"inputs": ["close"], "func": macv_031_hist_lvl_5d},
    "macv_032_hist_zscore_5d": {"inputs": ["close"], "func": macv_032_hist_zscore_5d},
    "macv_033_hist_rank_5d": {"inputs": ["close"], "func": macv_033_hist_rank_5d},
    "macv_034_hist_lvl_21d": {"inputs": ["close"], "func": macv_034_hist_lvl_21d},
    "macv_035_hist_zscore_21d": {"inputs": ["close"], "func": macv_035_hist_zscore_21d},
    "macv_036_hist_rank_21d": {"inputs": ["close"], "func": macv_036_hist_rank_21d},
    "macv_037_hist_lvl_63d": {"inputs": ["close"], "func": macv_037_hist_lvl_63d},
    "macv_038_hist_zscore_63d": {"inputs": ["close"], "func": macv_038_hist_zscore_63d},
    "macv_039_hist_rank_63d": {"inputs": ["close"], "func": macv_039_hist_rank_63d},
    "macv_040_hist_lvl_126d": {"inputs": ["close"], "func": macv_040_hist_lvl_126d},
    "macv_041_hist_zscore_126d": {"inputs": ["close"], "func": macv_041_hist_zscore_126d},
    "macv_042_hist_rank_126d": {"inputs": ["close"], "func": macv_042_hist_rank_126d},
    "macv_043_hist_lvl_252d": {"inputs": ["close"], "func": macv_043_hist_lvl_252d},
    "macv_044_hist_zscore_252d": {"inputs": ["close"], "func": macv_044_hist_zscore_252d},
    "macv_045_hist_rank_252d": {"inputs": ["close"], "func": macv_045_hist_rank_252d},
    "macv_046_macd_rat_lvl_5d": {"inputs": ["close"], "func": macv_046_macd_rat_lvl_5d},
    "macv_047_macd_rat_zscore_5d": {"inputs": ["close"], "func": macv_047_macd_rat_zscore_5d},
    "macv_048_macd_rat_rank_5d": {"inputs": ["close"], "func": macv_048_macd_rat_rank_5d},
    "macv_049_macd_rat_lvl_21d": {"inputs": ["close"], "func": macv_049_macd_rat_lvl_21d},
    "macv_050_macd_rat_zscore_21d": {"inputs": ["close"], "func": macv_050_macd_rat_zscore_21d},
    "macv_051_macd_rat_rank_21d": {"inputs": ["close"], "func": macv_051_macd_rat_rank_21d},
    "macv_052_macd_rat_lvl_63d": {"inputs": ["close"], "func": macv_052_macd_rat_lvl_63d},
    "macv_053_macd_rat_zscore_63d": {"inputs": ["close"], "func": macv_053_macd_rat_zscore_63d},
    "macv_054_macd_rat_rank_63d": {"inputs": ["close"], "func": macv_054_macd_rat_rank_63d},
    "macv_055_macd_rat_lvl_126d": {"inputs": ["close"], "func": macv_055_macd_rat_lvl_126d},
    "macv_056_macd_rat_zscore_126d": {"inputs": ["close"], "func": macv_056_macd_rat_zscore_126d},
    "macv_057_macd_rat_rank_126d": {"inputs": ["close"], "func": macv_057_macd_rat_rank_126d},
    "macv_058_macd_rat_lvl_252d": {"inputs": ["close"], "func": macv_058_macd_rat_lvl_252d},
    "macv_059_macd_rat_zscore_252d": {"inputs": ["close"], "func": macv_059_macd_rat_zscore_252d},
    "macv_060_macd_rat_rank_252d": {"inputs": ["close"], "func": macv_060_macd_rat_rank_252d},
    "macv_061_macd_z_lvl_5d": {"inputs": ["close"], "func": macv_061_macd_z_lvl_5d},
    "macv_062_macd_z_zscore_5d": {"inputs": ["close"], "func": macv_062_macd_z_zscore_5d},
    "macv_063_macd_z_rank_5d": {"inputs": ["close"], "func": macv_063_macd_z_rank_5d},
    "macv_064_macd_z_lvl_21d": {"inputs": ["close"], "func": macv_064_macd_z_lvl_21d},
    "macv_065_macd_z_zscore_21d": {"inputs": ["close"], "func": macv_065_macd_z_zscore_21d},
    "macv_066_macd_z_rank_21d": {"inputs": ["close"], "func": macv_066_macd_z_rank_21d},
    "macv_067_macd_z_lvl_63d": {"inputs": ["close"], "func": macv_067_macd_z_lvl_63d},
    "macv_068_macd_z_zscore_63d": {"inputs": ["close"], "func": macv_068_macd_z_zscore_63d},
    "macv_069_macd_z_rank_63d": {"inputs": ["close"], "func": macv_069_macd_z_rank_63d},
    "macv_070_macd_z_lvl_126d": {"inputs": ["close"], "func": macv_070_macd_z_lvl_126d},
    "macv_071_macd_z_zscore_126d": {"inputs": ["close"], "func": macv_071_macd_z_zscore_126d},
    "macv_072_macd_z_rank_126d": {"inputs": ["close"], "func": macv_072_macd_z_rank_126d},
    "macv_073_macd_z_lvl_252d": {"inputs": ["close"], "func": macv_073_macd_z_lvl_252d},
    "macv_074_macd_z_zscore_252d": {"inputs": ["close"], "func": macv_074_macd_z_zscore_252d},
    "macv_075_macd_z_rank_252d": {"inputs": ["close"], "func": macv_075_macd_z_rank_252d},
}
