"""
84_mfid_dynamics — Base Features 001-075
Domain: mfid_dynamics
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

def mfid_001_tp_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_001_tp_lvl_5d"""
    base = (high + low + close) / 3
    return _rolling_mean(base, 5)

def mfid_002_tp_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_002_tp_zscore_5d"""
    base = (high + low + close) / 3
    return _zscore_rolling(base, 5)

def mfid_003_tp_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_003_tp_rank_5d"""
    base = (high + low + close) / 3
    return _rank_pct(base, 5)

def mfid_004_tp_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_004_tp_lvl_21d"""
    base = (high + low + close) / 3
    return _rolling_mean(base, 21)

def mfid_005_tp_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_005_tp_zscore_21d"""
    base = (high + low + close) / 3
    return _zscore_rolling(base, 21)

def mfid_006_tp_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_006_tp_rank_21d"""
    base = (high + low + close) / 3
    return _rank_pct(base, 21)

def mfid_007_tp_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_007_tp_lvl_63d"""
    base = (high + low + close) / 3
    return _rolling_mean(base, 63)

def mfid_008_tp_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_008_tp_zscore_63d"""
    base = (high + low + close) / 3
    return _zscore_rolling(base, 63)

def mfid_009_tp_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_009_tp_rank_63d"""
    base = (high + low + close) / 3
    return _rank_pct(base, 63)

def mfid_010_tp_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_010_tp_lvl_126d"""
    base = (high + low + close) / 3
    return _rolling_mean(base, 126)

def mfid_011_tp_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_011_tp_zscore_126d"""
    base = (high + low + close) / 3
    return _zscore_rolling(base, 126)

def mfid_012_tp_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_012_tp_rank_126d"""
    base = (high + low + close) / 3
    return _rank_pct(base, 126)

def mfid_013_tp_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_013_tp_lvl_252d"""
    base = (high + low + close) / 3
    return _rolling_mean(base, 252)

def mfid_014_tp_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_014_tp_zscore_252d"""
    base = (high + low + close) / 3
    return _zscore_rolling(base, 252)

def mfid_015_tp_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_015_tp_rank_252d"""
    base = (high + low + close) / 3
    return _rank_pct(base, 252)

def mfid_016_rmf_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_016_rmf_lvl_5d"""
    base = ((high + low + close) / 3) * volume
    return _rolling_mean(base, 5)

def mfid_017_rmf_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_017_rmf_zscore_5d"""
    base = ((high + low + close) / 3) * volume
    return _zscore_rolling(base, 5)

def mfid_018_rmf_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_018_rmf_rank_5d"""
    base = ((high + low + close) / 3) * volume
    return _rank_pct(base, 5)

def mfid_019_rmf_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_019_rmf_lvl_21d"""
    base = ((high + low + close) / 3) * volume
    return _rolling_mean(base, 21)

def mfid_020_rmf_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_020_rmf_zscore_21d"""
    base = ((high + low + close) / 3) * volume
    return _zscore_rolling(base, 21)

def mfid_021_rmf_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_021_rmf_rank_21d"""
    base = ((high + low + close) / 3) * volume
    return _rank_pct(base, 21)

def mfid_022_rmf_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_022_rmf_lvl_63d"""
    base = ((high + low + close) / 3) * volume
    return _rolling_mean(base, 63)

def mfid_023_rmf_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_023_rmf_zscore_63d"""
    base = ((high + low + close) / 3) * volume
    return _zscore_rolling(base, 63)

def mfid_024_rmf_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_024_rmf_rank_63d"""
    base = ((high + low + close) / 3) * volume
    return _rank_pct(base, 63)

def mfid_025_rmf_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_025_rmf_lvl_126d"""
    base = ((high + low + close) / 3) * volume
    return _rolling_mean(base, 126)

def mfid_026_rmf_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_026_rmf_zscore_126d"""
    base = ((high + low + close) / 3) * volume
    return _zscore_rolling(base, 126)

def mfid_027_rmf_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_027_rmf_rank_126d"""
    base = ((high + low + close) / 3) * volume
    return _rank_pct(base, 126)

def mfid_028_rmf_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_028_rmf_lvl_252d"""
    base = ((high + low + close) / 3) * volume
    return _rolling_mean(base, 252)

def mfid_029_rmf_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_029_rmf_zscore_252d"""
    base = ((high + low + close) / 3) * volume
    return _zscore_rolling(base, 252)

def mfid_030_rmf_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_030_rmf_rank_252d"""
    base = ((high + low + close) / 3) * volume
    return _rank_pct(base, 252)

def mfid_031_mfi14_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_031_mfi14_lvl_5d"""
    base = 100 - (100 / (1 + _safe_div(_rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) > ((high + low + close) / 3).shift(1), 0), 14), _rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) < ((high + low + close) / 3).shift(1), 0), 14))))
    return _rolling_mean(base, 5)

def mfid_032_mfi14_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_032_mfi14_zscore_5d"""
    base = 100 - (100 / (1 + _safe_div(_rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) > ((high + low + close) / 3).shift(1), 0), 14), _rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) < ((high + low + close) / 3).shift(1), 0), 14))))
    return _zscore_rolling(base, 5)

def mfid_033_mfi14_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_033_mfi14_rank_5d"""
    base = 100 - (100 / (1 + _safe_div(_rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) > ((high + low + close) / 3).shift(1), 0), 14), _rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) < ((high + low + close) / 3).shift(1), 0), 14))))
    return _rank_pct(base, 5)

def mfid_034_mfi14_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_034_mfi14_lvl_21d"""
    base = 100 - (100 / (1 + _safe_div(_rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) > ((high + low + close) / 3).shift(1), 0), 14), _rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) < ((high + low + close) / 3).shift(1), 0), 14))))
    return _rolling_mean(base, 21)

def mfid_035_mfi14_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_035_mfi14_zscore_21d"""
    base = 100 - (100 / (1 + _safe_div(_rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) > ((high + low + close) / 3).shift(1), 0), 14), _rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) < ((high + low + close) / 3).shift(1), 0), 14))))
    return _zscore_rolling(base, 21)

def mfid_036_mfi14_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_036_mfi14_rank_21d"""
    base = 100 - (100 / (1 + _safe_div(_rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) > ((high + low + close) / 3).shift(1), 0), 14), _rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) < ((high + low + close) / 3).shift(1), 0), 14))))
    return _rank_pct(base, 21)

def mfid_037_mfi14_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_037_mfi14_lvl_63d"""
    base = 100 - (100 / (1 + _safe_div(_rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) > ((high + low + close) / 3).shift(1), 0), 14), _rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) < ((high + low + close) / 3).shift(1), 0), 14))))
    return _rolling_mean(base, 63)

def mfid_038_mfi14_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_038_mfi14_zscore_63d"""
    base = 100 - (100 / (1 + _safe_div(_rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) > ((high + low + close) / 3).shift(1), 0), 14), _rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) < ((high + low + close) / 3).shift(1), 0), 14))))
    return _zscore_rolling(base, 63)

def mfid_039_mfi14_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_039_mfi14_rank_63d"""
    base = 100 - (100 / (1 + _safe_div(_rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) > ((high + low + close) / 3).shift(1), 0), 14), _rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) < ((high + low + close) / 3).shift(1), 0), 14))))
    return _rank_pct(base, 63)

def mfid_040_mfi14_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_040_mfi14_lvl_126d"""
    base = 100 - (100 / (1 + _safe_div(_rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) > ((high + low + close) / 3).shift(1), 0), 14), _rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) < ((high + low + close) / 3).shift(1), 0), 14))))
    return _rolling_mean(base, 126)

def mfid_041_mfi14_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_041_mfi14_zscore_126d"""
    base = 100 - (100 / (1 + _safe_div(_rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) > ((high + low + close) / 3).shift(1), 0), 14), _rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) < ((high + low + close) / 3).shift(1), 0), 14))))
    return _zscore_rolling(base, 126)

def mfid_042_mfi14_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_042_mfi14_rank_126d"""
    base = 100 - (100 / (1 + _safe_div(_rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) > ((high + low + close) / 3).shift(1), 0), 14), _rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) < ((high + low + close) / 3).shift(1), 0), 14))))
    return _rank_pct(base, 126)

def mfid_043_mfi14_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_043_mfi14_lvl_252d"""
    base = 100 - (100 / (1 + _safe_div(_rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) > ((high + low + close) / 3).shift(1), 0), 14), _rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) < ((high + low + close) / 3).shift(1), 0), 14))))
    return _rolling_mean(base, 252)

def mfid_044_mfi14_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_044_mfi14_zscore_252d"""
    base = 100 - (100 / (1 + _safe_div(_rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) > ((high + low + close) / 3).shift(1), 0), 14), _rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) < ((high + low + close) / 3).shift(1), 0), 14))))
    return _zscore_rolling(base, 252)

def mfid_045_mfi14_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_045_mfi14_rank_252d"""
    base = 100 - (100 / (1 + _safe_div(_rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) > ((high + low + close) / 3).shift(1), 0), 14), _rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) < ((high + low + close) / 3).shift(1), 0), 14))))
    return _rank_pct(base, 252)

def mfid_046_mfi_z_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_046_mfi_z_lvl_5d"""
    base = _zscore_rolling(100 - (100 / (1 + _safe_div(_rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) > ((high + low + close) / 3).shift(1), 0), 14), _rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) < ((high + low + close) / 3).shift(1), 0), 14)))), 63)
    return _rolling_mean(base, 5)

def mfid_047_mfi_z_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_047_mfi_z_zscore_5d"""
    base = _zscore_rolling(100 - (100 / (1 + _safe_div(_rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) > ((high + low + close) / 3).shift(1), 0), 14), _rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) < ((high + low + close) / 3).shift(1), 0), 14)))), 63)
    return _zscore_rolling(base, 5)

def mfid_048_mfi_z_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_048_mfi_z_rank_5d"""
    base = _zscore_rolling(100 - (100 / (1 + _safe_div(_rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) > ((high + low + close) / 3).shift(1), 0), 14), _rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) < ((high + low + close) / 3).shift(1), 0), 14)))), 63)
    return _rank_pct(base, 5)

def mfid_049_mfi_z_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_049_mfi_z_lvl_21d"""
    base = _zscore_rolling(100 - (100 / (1 + _safe_div(_rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) > ((high + low + close) / 3).shift(1), 0), 14), _rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) < ((high + low + close) / 3).shift(1), 0), 14)))), 63)
    return _rolling_mean(base, 21)

def mfid_050_mfi_z_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_050_mfi_z_zscore_21d"""
    base = _zscore_rolling(100 - (100 / (1 + _safe_div(_rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) > ((high + low + close) / 3).shift(1), 0), 14), _rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) < ((high + low + close) / 3).shift(1), 0), 14)))), 63)
    return _zscore_rolling(base, 21)

def mfid_051_mfi_z_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_051_mfi_z_rank_21d"""
    base = _zscore_rolling(100 - (100 / (1 + _safe_div(_rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) > ((high + low + close) / 3).shift(1), 0), 14), _rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) < ((high + low + close) / 3).shift(1), 0), 14)))), 63)
    return _rank_pct(base, 21)

def mfid_052_mfi_z_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_052_mfi_z_lvl_63d"""
    base = _zscore_rolling(100 - (100 / (1 + _safe_div(_rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) > ((high + low + close) / 3).shift(1), 0), 14), _rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) < ((high + low + close) / 3).shift(1), 0), 14)))), 63)
    return _rolling_mean(base, 63)

def mfid_053_mfi_z_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_053_mfi_z_zscore_63d"""
    base = _zscore_rolling(100 - (100 / (1 + _safe_div(_rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) > ((high + low + close) / 3).shift(1), 0), 14), _rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) < ((high + low + close) / 3).shift(1), 0), 14)))), 63)
    return _zscore_rolling(base, 63)

def mfid_054_mfi_z_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_054_mfi_z_rank_63d"""
    base = _zscore_rolling(100 - (100 / (1 + _safe_div(_rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) > ((high + low + close) / 3).shift(1), 0), 14), _rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) < ((high + low + close) / 3).shift(1), 0), 14)))), 63)
    return _rank_pct(base, 63)

def mfid_055_mfi_z_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_055_mfi_z_lvl_126d"""
    base = _zscore_rolling(100 - (100 / (1 + _safe_div(_rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) > ((high + low + close) / 3).shift(1), 0), 14), _rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) < ((high + low + close) / 3).shift(1), 0), 14)))), 63)
    return _rolling_mean(base, 126)

def mfid_056_mfi_z_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_056_mfi_z_zscore_126d"""
    base = _zscore_rolling(100 - (100 / (1 + _safe_div(_rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) > ((high + low + close) / 3).shift(1), 0), 14), _rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) < ((high + low + close) / 3).shift(1), 0), 14)))), 63)
    return _zscore_rolling(base, 126)

def mfid_057_mfi_z_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_057_mfi_z_rank_126d"""
    base = _zscore_rolling(100 - (100 / (1 + _safe_div(_rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) > ((high + low + close) / 3).shift(1), 0), 14), _rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) < ((high + low + close) / 3).shift(1), 0), 14)))), 63)
    return _rank_pct(base, 126)

def mfid_058_mfi_z_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_058_mfi_z_lvl_252d"""
    base = _zscore_rolling(100 - (100 / (1 + _safe_div(_rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) > ((high + low + close) / 3).shift(1), 0), 14), _rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) < ((high + low + close) / 3).shift(1), 0), 14)))), 63)
    return _rolling_mean(base, 252)

def mfid_059_mfi_z_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_059_mfi_z_zscore_252d"""
    base = _zscore_rolling(100 - (100 / (1 + _safe_div(_rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) > ((high + low + close) / 3).shift(1), 0), 14), _rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) < ((high + low + close) / 3).shift(1), 0), 14)))), 63)
    return _zscore_rolling(base, 252)

def mfid_060_mfi_z_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_060_mfi_z_rank_252d"""
    base = _zscore_rolling(100 - (100 / (1 + _safe_div(_rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) > ((high + low + close) / 3).shift(1), 0), 14), _rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) < ((high + low + close) / 3).shift(1), 0), 14)))), 63)
    return _rank_pct(base, 252)

def mfid_061_mfi_dist_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_061_mfi_dist_lvl_5d"""
    base = (100 - (100 / (1 + _safe_div(_rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) > ((high + low + close) / 3).shift(1), 0), 14), _rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) < ((high + low + close) / 3).shift(1), 0), 14))))) - 50
    return _rolling_mean(base, 5)

def mfid_062_mfi_dist_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_062_mfi_dist_zscore_5d"""
    base = (100 - (100 / (1 + _safe_div(_rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) > ((high + low + close) / 3).shift(1), 0), 14), _rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) < ((high + low + close) / 3).shift(1), 0), 14))))) - 50
    return _zscore_rolling(base, 5)

def mfid_063_mfi_dist_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_063_mfi_dist_rank_5d"""
    base = (100 - (100 / (1 + _safe_div(_rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) > ((high + low + close) / 3).shift(1), 0), 14), _rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) < ((high + low + close) / 3).shift(1), 0), 14))))) - 50
    return _rank_pct(base, 5)

def mfid_064_mfi_dist_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_064_mfi_dist_lvl_21d"""
    base = (100 - (100 / (1 + _safe_div(_rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) > ((high + low + close) / 3).shift(1), 0), 14), _rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) < ((high + low + close) / 3).shift(1), 0), 14))))) - 50
    return _rolling_mean(base, 21)

def mfid_065_mfi_dist_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_065_mfi_dist_zscore_21d"""
    base = (100 - (100 / (1 + _safe_div(_rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) > ((high + low + close) / 3).shift(1), 0), 14), _rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) < ((high + low + close) / 3).shift(1), 0), 14))))) - 50
    return _zscore_rolling(base, 21)

def mfid_066_mfi_dist_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_066_mfi_dist_rank_21d"""
    base = (100 - (100 / (1 + _safe_div(_rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) > ((high + low + close) / 3).shift(1), 0), 14), _rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) < ((high + low + close) / 3).shift(1), 0), 14))))) - 50
    return _rank_pct(base, 21)

def mfid_067_mfi_dist_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_067_mfi_dist_lvl_63d"""
    base = (100 - (100 / (1 + _safe_div(_rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) > ((high + low + close) / 3).shift(1), 0), 14), _rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) < ((high + low + close) / 3).shift(1), 0), 14))))) - 50
    return _rolling_mean(base, 63)

def mfid_068_mfi_dist_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_068_mfi_dist_zscore_63d"""
    base = (100 - (100 / (1 + _safe_div(_rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) > ((high + low + close) / 3).shift(1), 0), 14), _rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) < ((high + low + close) / 3).shift(1), 0), 14))))) - 50
    return _zscore_rolling(base, 63)

def mfid_069_mfi_dist_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_069_mfi_dist_rank_63d"""
    base = (100 - (100 / (1 + _safe_div(_rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) > ((high + low + close) / 3).shift(1), 0), 14), _rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) < ((high + low + close) / 3).shift(1), 0), 14))))) - 50
    return _rank_pct(base, 63)

def mfid_070_mfi_dist_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_070_mfi_dist_lvl_126d"""
    base = (100 - (100 / (1 + _safe_div(_rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) > ((high + low + close) / 3).shift(1), 0), 14), _rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) < ((high + low + close) / 3).shift(1), 0), 14))))) - 50
    return _rolling_mean(base, 126)

def mfid_071_mfi_dist_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_071_mfi_dist_zscore_126d"""
    base = (100 - (100 / (1 + _safe_div(_rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) > ((high + low + close) / 3).shift(1), 0), 14), _rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) < ((high + low + close) / 3).shift(1), 0), 14))))) - 50
    return _zscore_rolling(base, 126)

def mfid_072_mfi_dist_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_072_mfi_dist_rank_126d"""
    base = (100 - (100 / (1 + _safe_div(_rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) > ((high + low + close) / 3).shift(1), 0), 14), _rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) < ((high + low + close) / 3).shift(1), 0), 14))))) - 50
    return _rank_pct(base, 126)

def mfid_073_mfi_dist_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_073_mfi_dist_lvl_252d"""
    base = (100 - (100 / (1 + _safe_div(_rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) > ((high + low + close) / 3).shift(1), 0), 14), _rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) < ((high + low + close) / 3).shift(1), 0), 14))))) - 50
    return _rolling_mean(base, 252)

def mfid_074_mfi_dist_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_074_mfi_dist_zscore_252d"""
    base = (100 - (100 / (1 + _safe_div(_rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) > ((high + low + close) / 3).shift(1), 0), 14), _rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) < ((high + low + close) / 3).shift(1), 0), 14))))) - 50
    return _zscore_rolling(base, 252)

def mfid_075_mfi_dist_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """mfid_075_mfi_dist_rank_252d"""
    base = (100 - (100 / (1 + _safe_div(_rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) > ((high + low + close) / 3).shift(1), 0), 14), _rolling_sum((((high + low + close) / 3) * volume).where(((high + low + close) / 3) < ((high + low + close) / 3).shift(1), 0), 14))))) - 50
    return _rank_pct(base, 252)

# ── Registry ──────────────────────────────────────────────────────────────────
V84_REGISTRY = {
    "mfid_001_tp_lvl_5d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_001_tp_lvl_5d},
    "mfid_002_tp_zscore_5d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_002_tp_zscore_5d},
    "mfid_003_tp_rank_5d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_003_tp_rank_5d},
    "mfid_004_tp_lvl_21d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_004_tp_lvl_21d},
    "mfid_005_tp_zscore_21d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_005_tp_zscore_21d},
    "mfid_006_tp_rank_21d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_006_tp_rank_21d},
    "mfid_007_tp_lvl_63d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_007_tp_lvl_63d},
    "mfid_008_tp_zscore_63d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_008_tp_zscore_63d},
    "mfid_009_tp_rank_63d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_009_tp_rank_63d},
    "mfid_010_tp_lvl_126d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_010_tp_lvl_126d},
    "mfid_011_tp_zscore_126d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_011_tp_zscore_126d},
    "mfid_012_tp_rank_126d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_012_tp_rank_126d},
    "mfid_013_tp_lvl_252d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_013_tp_lvl_252d},
    "mfid_014_tp_zscore_252d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_014_tp_zscore_252d},
    "mfid_015_tp_rank_252d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_015_tp_rank_252d},
    "mfid_016_rmf_lvl_5d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_016_rmf_lvl_5d},
    "mfid_017_rmf_zscore_5d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_017_rmf_zscore_5d},
    "mfid_018_rmf_rank_5d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_018_rmf_rank_5d},
    "mfid_019_rmf_lvl_21d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_019_rmf_lvl_21d},
    "mfid_020_rmf_zscore_21d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_020_rmf_zscore_21d},
    "mfid_021_rmf_rank_21d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_021_rmf_rank_21d},
    "mfid_022_rmf_lvl_63d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_022_rmf_lvl_63d},
    "mfid_023_rmf_zscore_63d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_023_rmf_zscore_63d},
    "mfid_024_rmf_rank_63d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_024_rmf_rank_63d},
    "mfid_025_rmf_lvl_126d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_025_rmf_lvl_126d},
    "mfid_026_rmf_zscore_126d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_026_rmf_zscore_126d},
    "mfid_027_rmf_rank_126d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_027_rmf_rank_126d},
    "mfid_028_rmf_lvl_252d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_028_rmf_lvl_252d},
    "mfid_029_rmf_zscore_252d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_029_rmf_zscore_252d},
    "mfid_030_rmf_rank_252d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_030_rmf_rank_252d},
    "mfid_031_mfi14_lvl_5d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_031_mfi14_lvl_5d},
    "mfid_032_mfi14_zscore_5d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_032_mfi14_zscore_5d},
    "mfid_033_mfi14_rank_5d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_033_mfi14_rank_5d},
    "mfid_034_mfi14_lvl_21d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_034_mfi14_lvl_21d},
    "mfid_035_mfi14_zscore_21d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_035_mfi14_zscore_21d},
    "mfid_036_mfi14_rank_21d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_036_mfi14_rank_21d},
    "mfid_037_mfi14_lvl_63d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_037_mfi14_lvl_63d},
    "mfid_038_mfi14_zscore_63d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_038_mfi14_zscore_63d},
    "mfid_039_mfi14_rank_63d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_039_mfi14_rank_63d},
    "mfid_040_mfi14_lvl_126d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_040_mfi14_lvl_126d},
    "mfid_041_mfi14_zscore_126d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_041_mfi14_zscore_126d},
    "mfid_042_mfi14_rank_126d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_042_mfi14_rank_126d},
    "mfid_043_mfi14_lvl_252d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_043_mfi14_lvl_252d},
    "mfid_044_mfi14_zscore_252d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_044_mfi14_zscore_252d},
    "mfid_045_mfi14_rank_252d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_045_mfi14_rank_252d},
    "mfid_046_mfi_z_lvl_5d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_046_mfi_z_lvl_5d},
    "mfid_047_mfi_z_zscore_5d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_047_mfi_z_zscore_5d},
    "mfid_048_mfi_z_rank_5d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_048_mfi_z_rank_5d},
    "mfid_049_mfi_z_lvl_21d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_049_mfi_z_lvl_21d},
    "mfid_050_mfi_z_zscore_21d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_050_mfi_z_zscore_21d},
    "mfid_051_mfi_z_rank_21d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_051_mfi_z_rank_21d},
    "mfid_052_mfi_z_lvl_63d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_052_mfi_z_lvl_63d},
    "mfid_053_mfi_z_zscore_63d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_053_mfi_z_zscore_63d},
    "mfid_054_mfi_z_rank_63d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_054_mfi_z_rank_63d},
    "mfid_055_mfi_z_lvl_126d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_055_mfi_z_lvl_126d},
    "mfid_056_mfi_z_zscore_126d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_056_mfi_z_zscore_126d},
    "mfid_057_mfi_z_rank_126d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_057_mfi_z_rank_126d},
    "mfid_058_mfi_z_lvl_252d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_058_mfi_z_lvl_252d},
    "mfid_059_mfi_z_zscore_252d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_059_mfi_z_zscore_252d},
    "mfid_060_mfi_z_rank_252d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_060_mfi_z_rank_252d},
    "mfid_061_mfi_dist_lvl_5d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_061_mfi_dist_lvl_5d},
    "mfid_062_mfi_dist_zscore_5d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_062_mfi_dist_zscore_5d},
    "mfid_063_mfi_dist_rank_5d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_063_mfi_dist_rank_5d},
    "mfid_064_mfi_dist_lvl_21d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_064_mfi_dist_lvl_21d},
    "mfid_065_mfi_dist_zscore_21d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_065_mfi_dist_zscore_21d},
    "mfid_066_mfi_dist_rank_21d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_066_mfi_dist_rank_21d},
    "mfid_067_mfi_dist_lvl_63d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_067_mfi_dist_lvl_63d},
    "mfid_068_mfi_dist_zscore_63d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_068_mfi_dist_zscore_63d},
    "mfid_069_mfi_dist_rank_63d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_069_mfi_dist_rank_63d},
    "mfid_070_mfi_dist_lvl_126d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_070_mfi_dist_lvl_126d},
    "mfid_071_mfi_dist_zscore_126d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_071_mfi_dist_zscore_126d},
    "mfid_072_mfi_dist_rank_126d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_072_mfi_dist_rank_126d},
    "mfid_073_mfi_dist_lvl_252d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_073_mfi_dist_lvl_252d},
    "mfid_074_mfi_dist_zscore_252d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_074_mfi_dist_zscore_252d},
    "mfid_075_mfi_dist_rank_252d": {"inputs": ["high", "low", "close", "volume"], "func": mfid_075_mfi_dist_rank_252d},
}
