"""
81_adxd_dynamics — Base Features 001-075
Domain: adxd_dynamics
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

def adxd_001_tr_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_001_tr_lvl_5d"""
    base = _rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0]
    return _rolling_mean(base, 5)

def adxd_002_tr_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_002_tr_zscore_5d"""
    base = _rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0]
    return _zscore_rolling(base, 5)

def adxd_003_tr_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_003_tr_rank_5d"""
    base = _rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0]
    return _rank_pct(base, 5)

def adxd_004_tr_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_004_tr_lvl_21d"""
    base = _rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0]
    return _rolling_mean(base, 21)

def adxd_005_tr_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_005_tr_zscore_21d"""
    base = _rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0]
    return _zscore_rolling(base, 21)

def adxd_006_tr_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_006_tr_rank_21d"""
    base = _rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0]
    return _rank_pct(base, 21)

def adxd_007_tr_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_007_tr_lvl_63d"""
    base = _rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0]
    return _rolling_mean(base, 63)

def adxd_008_tr_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_008_tr_zscore_63d"""
    base = _rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0]
    return _zscore_rolling(base, 63)

def adxd_009_tr_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_009_tr_rank_63d"""
    base = _rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0]
    return _rank_pct(base, 63)

def adxd_010_tr_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_010_tr_lvl_126d"""
    base = _rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0]
    return _rolling_mean(base, 126)

def adxd_011_tr_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_011_tr_zscore_126d"""
    base = _rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0]
    return _zscore_rolling(base, 126)

def adxd_012_tr_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_012_tr_rank_126d"""
    base = _rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0]
    return _rank_pct(base, 126)

def adxd_013_tr_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_013_tr_lvl_252d"""
    base = _rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0]
    return _rolling_mean(base, 252)

def adxd_014_tr_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_014_tr_zscore_252d"""
    base = _rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0]
    return _zscore_rolling(base, 252)

def adxd_015_tr_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_015_tr_rank_252d"""
    base = _rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0]
    return _rank_pct(base, 252)

def adxd_016_pdm_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_016_pdm_lvl_5d"""
    base = (high - high.shift(1)).where((high - high.shift(1)) > (low.shift(1) - low), 0).where((high - high.shift(1)) > 0, 0)
    return _rolling_mean(base, 5)

def adxd_017_pdm_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_017_pdm_zscore_5d"""
    base = (high - high.shift(1)).where((high - high.shift(1)) > (low.shift(1) - low), 0).where((high - high.shift(1)) > 0, 0)
    return _zscore_rolling(base, 5)

def adxd_018_pdm_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_018_pdm_rank_5d"""
    base = (high - high.shift(1)).where((high - high.shift(1)) > (low.shift(1) - low), 0).where((high - high.shift(1)) > 0, 0)
    return _rank_pct(base, 5)

def adxd_019_pdm_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_019_pdm_lvl_21d"""
    base = (high - high.shift(1)).where((high - high.shift(1)) > (low.shift(1) - low), 0).where((high - high.shift(1)) > 0, 0)
    return _rolling_mean(base, 21)

def adxd_020_pdm_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_020_pdm_zscore_21d"""
    base = (high - high.shift(1)).where((high - high.shift(1)) > (low.shift(1) - low), 0).where((high - high.shift(1)) > 0, 0)
    return _zscore_rolling(base, 21)

def adxd_021_pdm_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_021_pdm_rank_21d"""
    base = (high - high.shift(1)).where((high - high.shift(1)) > (low.shift(1) - low), 0).where((high - high.shift(1)) > 0, 0)
    return _rank_pct(base, 21)

def adxd_022_pdm_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_022_pdm_lvl_63d"""
    base = (high - high.shift(1)).where((high - high.shift(1)) > (low.shift(1) - low), 0).where((high - high.shift(1)) > 0, 0)
    return _rolling_mean(base, 63)

def adxd_023_pdm_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_023_pdm_zscore_63d"""
    base = (high - high.shift(1)).where((high - high.shift(1)) > (low.shift(1) - low), 0).where((high - high.shift(1)) > 0, 0)
    return _zscore_rolling(base, 63)

def adxd_024_pdm_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_024_pdm_rank_63d"""
    base = (high - high.shift(1)).where((high - high.shift(1)) > (low.shift(1) - low), 0).where((high - high.shift(1)) > 0, 0)
    return _rank_pct(base, 63)

def adxd_025_pdm_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_025_pdm_lvl_126d"""
    base = (high - high.shift(1)).where((high - high.shift(1)) > (low.shift(1) - low), 0).where((high - high.shift(1)) > 0, 0)
    return _rolling_mean(base, 126)

def adxd_026_pdm_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_026_pdm_zscore_126d"""
    base = (high - high.shift(1)).where((high - high.shift(1)) > (low.shift(1) - low), 0).where((high - high.shift(1)) > 0, 0)
    return _zscore_rolling(base, 126)

def adxd_027_pdm_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_027_pdm_rank_126d"""
    base = (high - high.shift(1)).where((high - high.shift(1)) > (low.shift(1) - low), 0).where((high - high.shift(1)) > 0, 0)
    return _rank_pct(base, 126)

def adxd_028_pdm_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_028_pdm_lvl_252d"""
    base = (high - high.shift(1)).where((high - high.shift(1)) > (low.shift(1) - low), 0).where((high - high.shift(1)) > 0, 0)
    return _rolling_mean(base, 252)

def adxd_029_pdm_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_029_pdm_zscore_252d"""
    base = (high - high.shift(1)).where((high - high.shift(1)) > (low.shift(1) - low), 0).where((high - high.shift(1)) > 0, 0)
    return _zscore_rolling(base, 252)

def adxd_030_pdm_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_030_pdm_rank_252d"""
    base = (high - high.shift(1)).where((high - high.shift(1)) > (low.shift(1) - low), 0).where((high - high.shift(1)) > 0, 0)
    return _rank_pct(base, 252)

def adxd_031_mdm_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_031_mdm_lvl_5d"""
    base = (low.shift(1) - low).where((low.shift(1) - low) > (high - high.shift(1)), 0).where((low.shift(1) - low) > 0, 0)
    return _rolling_mean(base, 5)

def adxd_032_mdm_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_032_mdm_zscore_5d"""
    base = (low.shift(1) - low).where((low.shift(1) - low) > (high - high.shift(1)), 0).where((low.shift(1) - low) > 0, 0)
    return _zscore_rolling(base, 5)

def adxd_033_mdm_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_033_mdm_rank_5d"""
    base = (low.shift(1) - low).where((low.shift(1) - low) > (high - high.shift(1)), 0).where((low.shift(1) - low) > 0, 0)
    return _rank_pct(base, 5)

def adxd_034_mdm_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_034_mdm_lvl_21d"""
    base = (low.shift(1) - low).where((low.shift(1) - low) > (high - high.shift(1)), 0).where((low.shift(1) - low) > 0, 0)
    return _rolling_mean(base, 21)

def adxd_035_mdm_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_035_mdm_zscore_21d"""
    base = (low.shift(1) - low).where((low.shift(1) - low) > (high - high.shift(1)), 0).where((low.shift(1) - low) > 0, 0)
    return _zscore_rolling(base, 21)

def adxd_036_mdm_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_036_mdm_rank_21d"""
    base = (low.shift(1) - low).where((low.shift(1) - low) > (high - high.shift(1)), 0).where((low.shift(1) - low) > 0, 0)
    return _rank_pct(base, 21)

def adxd_037_mdm_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_037_mdm_lvl_63d"""
    base = (low.shift(1) - low).where((low.shift(1) - low) > (high - high.shift(1)), 0).where((low.shift(1) - low) > 0, 0)
    return _rolling_mean(base, 63)

def adxd_038_mdm_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_038_mdm_zscore_63d"""
    base = (low.shift(1) - low).where((low.shift(1) - low) > (high - high.shift(1)), 0).where((low.shift(1) - low) > 0, 0)
    return _zscore_rolling(base, 63)

def adxd_039_mdm_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_039_mdm_rank_63d"""
    base = (low.shift(1) - low).where((low.shift(1) - low) > (high - high.shift(1)), 0).where((low.shift(1) - low) > 0, 0)
    return _rank_pct(base, 63)

def adxd_040_mdm_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_040_mdm_lvl_126d"""
    base = (low.shift(1) - low).where((low.shift(1) - low) > (high - high.shift(1)), 0).where((low.shift(1) - low) > 0, 0)
    return _rolling_mean(base, 126)

def adxd_041_mdm_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_041_mdm_zscore_126d"""
    base = (low.shift(1) - low).where((low.shift(1) - low) > (high - high.shift(1)), 0).where((low.shift(1) - low) > 0, 0)
    return _zscore_rolling(base, 126)

def adxd_042_mdm_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_042_mdm_rank_126d"""
    base = (low.shift(1) - low).where((low.shift(1) - low) > (high - high.shift(1)), 0).where((low.shift(1) - low) > 0, 0)
    return _rank_pct(base, 126)

def adxd_043_mdm_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_043_mdm_lvl_252d"""
    base = (low.shift(1) - low).where((low.shift(1) - low) > (high - high.shift(1)), 0).where((low.shift(1) - low) > 0, 0)
    return _rolling_mean(base, 252)

def adxd_044_mdm_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_044_mdm_zscore_252d"""
    base = (low.shift(1) - low).where((low.shift(1) - low) > (high - high.shift(1)), 0).where((low.shift(1) - low) > 0, 0)
    return _zscore_rolling(base, 252)

def adxd_045_mdm_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_045_mdm_rank_252d"""
    base = (low.shift(1) - low).where((low.shift(1) - low) > (high - high.shift(1)), 0).where((low.shift(1) - low) > 0, 0)
    return _rank_pct(base, 252)

def adxd_046_pdi_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_046_pdi_lvl_5d"""
    base = 100 * _safe_div(_rolling_mean((high - high.shift(1)).where((high - high.shift(1)) > (low.shift(1) - low), 0).where((high - high.shift(1)) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14))
    return _rolling_mean(base, 5)

def adxd_047_pdi_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_047_pdi_zscore_5d"""
    base = 100 * _safe_div(_rolling_mean((high - high.shift(1)).where((high - high.shift(1)) > (low.shift(1) - low), 0).where((high - high.shift(1)) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14))
    return _zscore_rolling(base, 5)

def adxd_048_pdi_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_048_pdi_rank_5d"""
    base = 100 * _safe_div(_rolling_mean((high - high.shift(1)).where((high - high.shift(1)) > (low.shift(1) - low), 0).where((high - high.shift(1)) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14))
    return _rank_pct(base, 5)

def adxd_049_pdi_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_049_pdi_lvl_21d"""
    base = 100 * _safe_div(_rolling_mean((high - high.shift(1)).where((high - high.shift(1)) > (low.shift(1) - low), 0).where((high - high.shift(1)) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14))
    return _rolling_mean(base, 21)

def adxd_050_pdi_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_050_pdi_zscore_21d"""
    base = 100 * _safe_div(_rolling_mean((high - high.shift(1)).where((high - high.shift(1)) > (low.shift(1) - low), 0).where((high - high.shift(1)) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14))
    return _zscore_rolling(base, 21)

def adxd_051_pdi_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_051_pdi_rank_21d"""
    base = 100 * _safe_div(_rolling_mean((high - high.shift(1)).where((high - high.shift(1)) > (low.shift(1) - low), 0).where((high - high.shift(1)) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14))
    return _rank_pct(base, 21)

def adxd_052_pdi_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_052_pdi_lvl_63d"""
    base = 100 * _safe_div(_rolling_mean((high - high.shift(1)).where((high - high.shift(1)) > (low.shift(1) - low), 0).where((high - high.shift(1)) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14))
    return _rolling_mean(base, 63)

def adxd_053_pdi_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_053_pdi_zscore_63d"""
    base = 100 * _safe_div(_rolling_mean((high - high.shift(1)).where((high - high.shift(1)) > (low.shift(1) - low), 0).where((high - high.shift(1)) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14))
    return _zscore_rolling(base, 63)

def adxd_054_pdi_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_054_pdi_rank_63d"""
    base = 100 * _safe_div(_rolling_mean((high - high.shift(1)).where((high - high.shift(1)) > (low.shift(1) - low), 0).where((high - high.shift(1)) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14))
    return _rank_pct(base, 63)

def adxd_055_pdi_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_055_pdi_lvl_126d"""
    base = 100 * _safe_div(_rolling_mean((high - high.shift(1)).where((high - high.shift(1)) > (low.shift(1) - low), 0).where((high - high.shift(1)) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14))
    return _rolling_mean(base, 126)

def adxd_056_pdi_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_056_pdi_zscore_126d"""
    base = 100 * _safe_div(_rolling_mean((high - high.shift(1)).where((high - high.shift(1)) > (low.shift(1) - low), 0).where((high - high.shift(1)) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14))
    return _zscore_rolling(base, 126)

def adxd_057_pdi_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_057_pdi_rank_126d"""
    base = 100 * _safe_div(_rolling_mean((high - high.shift(1)).where((high - high.shift(1)) > (low.shift(1) - low), 0).where((high - high.shift(1)) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14))
    return _rank_pct(base, 126)

def adxd_058_pdi_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_058_pdi_lvl_252d"""
    base = 100 * _safe_div(_rolling_mean((high - high.shift(1)).where((high - high.shift(1)) > (low.shift(1) - low), 0).where((high - high.shift(1)) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14))
    return _rolling_mean(base, 252)

def adxd_059_pdi_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_059_pdi_zscore_252d"""
    base = 100 * _safe_div(_rolling_mean((high - high.shift(1)).where((high - high.shift(1)) > (low.shift(1) - low), 0).where((high - high.shift(1)) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14))
    return _zscore_rolling(base, 252)

def adxd_060_pdi_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_060_pdi_rank_252d"""
    base = 100 * _safe_div(_rolling_mean((high - high.shift(1)).where((high - high.shift(1)) > (low.shift(1) - low), 0).where((high - high.shift(1)) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14))
    return _rank_pct(base, 252)

def adxd_061_mdi_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_061_mdi_lvl_5d"""
    base = 100 * _safe_div(_rolling_mean((low.shift(1) - low).where((low.shift(1) - low) > (high - high.shift(1)), 0).where((low.shift(1) - low) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14))
    return _rolling_mean(base, 5)

def adxd_062_mdi_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_062_mdi_zscore_5d"""
    base = 100 * _safe_div(_rolling_mean((low.shift(1) - low).where((low.shift(1) - low) > (high - high.shift(1)), 0).where((low.shift(1) - low) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14))
    return _zscore_rolling(base, 5)

def adxd_063_mdi_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_063_mdi_rank_5d"""
    base = 100 * _safe_div(_rolling_mean((low.shift(1) - low).where((low.shift(1) - low) > (high - high.shift(1)), 0).where((low.shift(1) - low) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14))
    return _rank_pct(base, 5)

def adxd_064_mdi_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_064_mdi_lvl_21d"""
    base = 100 * _safe_div(_rolling_mean((low.shift(1) - low).where((low.shift(1) - low) > (high - high.shift(1)), 0).where((low.shift(1) - low) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14))
    return _rolling_mean(base, 21)

def adxd_065_mdi_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_065_mdi_zscore_21d"""
    base = 100 * _safe_div(_rolling_mean((low.shift(1) - low).where((low.shift(1) - low) > (high - high.shift(1)), 0).where((low.shift(1) - low) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14))
    return _zscore_rolling(base, 21)

def adxd_066_mdi_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_066_mdi_rank_21d"""
    base = 100 * _safe_div(_rolling_mean((low.shift(1) - low).where((low.shift(1) - low) > (high - high.shift(1)), 0).where((low.shift(1) - low) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14))
    return _rank_pct(base, 21)

def adxd_067_mdi_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_067_mdi_lvl_63d"""
    base = 100 * _safe_div(_rolling_mean((low.shift(1) - low).where((low.shift(1) - low) > (high - high.shift(1)), 0).where((low.shift(1) - low) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14))
    return _rolling_mean(base, 63)

def adxd_068_mdi_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_068_mdi_zscore_63d"""
    base = 100 * _safe_div(_rolling_mean((low.shift(1) - low).where((low.shift(1) - low) > (high - high.shift(1)), 0).where((low.shift(1) - low) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14))
    return _zscore_rolling(base, 63)

def adxd_069_mdi_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_069_mdi_rank_63d"""
    base = 100 * _safe_div(_rolling_mean((low.shift(1) - low).where((low.shift(1) - low) > (high - high.shift(1)), 0).where((low.shift(1) - low) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14))
    return _rank_pct(base, 63)

def adxd_070_mdi_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_070_mdi_lvl_126d"""
    base = 100 * _safe_div(_rolling_mean((low.shift(1) - low).where((low.shift(1) - low) > (high - high.shift(1)), 0).where((low.shift(1) - low) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14))
    return _rolling_mean(base, 126)

def adxd_071_mdi_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_071_mdi_zscore_126d"""
    base = 100 * _safe_div(_rolling_mean((low.shift(1) - low).where((low.shift(1) - low) > (high - high.shift(1)), 0).where((low.shift(1) - low) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14))
    return _zscore_rolling(base, 126)

def adxd_072_mdi_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_072_mdi_rank_126d"""
    base = 100 * _safe_div(_rolling_mean((low.shift(1) - low).where((low.shift(1) - low) > (high - high.shift(1)), 0).where((low.shift(1) - low) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14))
    return _rank_pct(base, 126)

def adxd_073_mdi_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_073_mdi_lvl_252d"""
    base = 100 * _safe_div(_rolling_mean((low.shift(1) - low).where((low.shift(1) - low) > (high - high.shift(1)), 0).where((low.shift(1) - low) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14))
    return _rolling_mean(base, 252)

def adxd_074_mdi_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_074_mdi_zscore_252d"""
    base = 100 * _safe_div(_rolling_mean((low.shift(1) - low).where((low.shift(1) - low) > (high - high.shift(1)), 0).where((low.shift(1) - low) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14))
    return _zscore_rolling(base, 252)

def adxd_075_mdi_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """adxd_075_mdi_rank_252d"""
    base = 100 * _safe_div(_rolling_mean((low.shift(1) - low).where((low.shift(1) - low) > (high - high.shift(1)), 0).where((low.shift(1) - low) > 0, 0), 14), _rolling_mean(_rolling_max(pd.concat([high-low, (high-close.shift(1)).abs(), (low-close.shift(1)).abs()], axis=1), 1).iloc[:,0], 14))
    return _rank_pct(base, 252)

# ── Registry ──────────────────────────────────────────────────────────────────
V81_REGISTRY = {
    "adxd_001_tr_lvl_5d": {"inputs": ["high", "low", "close"], "func": adxd_001_tr_lvl_5d},
    "adxd_002_tr_zscore_5d": {"inputs": ["high", "low", "close"], "func": adxd_002_tr_zscore_5d},
    "adxd_003_tr_rank_5d": {"inputs": ["high", "low", "close"], "func": adxd_003_tr_rank_5d},
    "adxd_004_tr_lvl_21d": {"inputs": ["high", "low", "close"], "func": adxd_004_tr_lvl_21d},
    "adxd_005_tr_zscore_21d": {"inputs": ["high", "low", "close"], "func": adxd_005_tr_zscore_21d},
    "adxd_006_tr_rank_21d": {"inputs": ["high", "low", "close"], "func": adxd_006_tr_rank_21d},
    "adxd_007_tr_lvl_63d": {"inputs": ["high", "low", "close"], "func": adxd_007_tr_lvl_63d},
    "adxd_008_tr_zscore_63d": {"inputs": ["high", "low", "close"], "func": adxd_008_tr_zscore_63d},
    "adxd_009_tr_rank_63d": {"inputs": ["high", "low", "close"], "func": adxd_009_tr_rank_63d},
    "adxd_010_tr_lvl_126d": {"inputs": ["high", "low", "close"], "func": adxd_010_tr_lvl_126d},
    "adxd_011_tr_zscore_126d": {"inputs": ["high", "low", "close"], "func": adxd_011_tr_zscore_126d},
    "adxd_012_tr_rank_126d": {"inputs": ["high", "low", "close"], "func": adxd_012_tr_rank_126d},
    "adxd_013_tr_lvl_252d": {"inputs": ["high", "low", "close"], "func": adxd_013_tr_lvl_252d},
    "adxd_014_tr_zscore_252d": {"inputs": ["high", "low", "close"], "func": adxd_014_tr_zscore_252d},
    "adxd_015_tr_rank_252d": {"inputs": ["high", "low", "close"], "func": adxd_015_tr_rank_252d},
    "adxd_016_pdm_lvl_5d": {"inputs": ["high", "low", "close"], "func": adxd_016_pdm_lvl_5d},
    "adxd_017_pdm_zscore_5d": {"inputs": ["high", "low", "close"], "func": adxd_017_pdm_zscore_5d},
    "adxd_018_pdm_rank_5d": {"inputs": ["high", "low", "close"], "func": adxd_018_pdm_rank_5d},
    "adxd_019_pdm_lvl_21d": {"inputs": ["high", "low", "close"], "func": adxd_019_pdm_lvl_21d},
    "adxd_020_pdm_zscore_21d": {"inputs": ["high", "low", "close"], "func": adxd_020_pdm_zscore_21d},
    "adxd_021_pdm_rank_21d": {"inputs": ["high", "low", "close"], "func": adxd_021_pdm_rank_21d},
    "adxd_022_pdm_lvl_63d": {"inputs": ["high", "low", "close"], "func": adxd_022_pdm_lvl_63d},
    "adxd_023_pdm_zscore_63d": {"inputs": ["high", "low", "close"], "func": adxd_023_pdm_zscore_63d},
    "adxd_024_pdm_rank_63d": {"inputs": ["high", "low", "close"], "func": adxd_024_pdm_rank_63d},
    "adxd_025_pdm_lvl_126d": {"inputs": ["high", "low", "close"], "func": adxd_025_pdm_lvl_126d},
    "adxd_026_pdm_zscore_126d": {"inputs": ["high", "low", "close"], "func": adxd_026_pdm_zscore_126d},
    "adxd_027_pdm_rank_126d": {"inputs": ["high", "low", "close"], "func": adxd_027_pdm_rank_126d},
    "adxd_028_pdm_lvl_252d": {"inputs": ["high", "low", "close"], "func": adxd_028_pdm_lvl_252d},
    "adxd_029_pdm_zscore_252d": {"inputs": ["high", "low", "close"], "func": adxd_029_pdm_zscore_252d},
    "adxd_030_pdm_rank_252d": {"inputs": ["high", "low", "close"], "func": adxd_030_pdm_rank_252d},
    "adxd_031_mdm_lvl_5d": {"inputs": ["high", "low", "close"], "func": adxd_031_mdm_lvl_5d},
    "adxd_032_mdm_zscore_5d": {"inputs": ["high", "low", "close"], "func": adxd_032_mdm_zscore_5d},
    "adxd_033_mdm_rank_5d": {"inputs": ["high", "low", "close"], "func": adxd_033_mdm_rank_5d},
    "adxd_034_mdm_lvl_21d": {"inputs": ["high", "low", "close"], "func": adxd_034_mdm_lvl_21d},
    "adxd_035_mdm_zscore_21d": {"inputs": ["high", "low", "close"], "func": adxd_035_mdm_zscore_21d},
    "adxd_036_mdm_rank_21d": {"inputs": ["high", "low", "close"], "func": adxd_036_mdm_rank_21d},
    "adxd_037_mdm_lvl_63d": {"inputs": ["high", "low", "close"], "func": adxd_037_mdm_lvl_63d},
    "adxd_038_mdm_zscore_63d": {"inputs": ["high", "low", "close"], "func": adxd_038_mdm_zscore_63d},
    "adxd_039_mdm_rank_63d": {"inputs": ["high", "low", "close"], "func": adxd_039_mdm_rank_63d},
    "adxd_040_mdm_lvl_126d": {"inputs": ["high", "low", "close"], "func": adxd_040_mdm_lvl_126d},
    "adxd_041_mdm_zscore_126d": {"inputs": ["high", "low", "close"], "func": adxd_041_mdm_zscore_126d},
    "adxd_042_mdm_rank_126d": {"inputs": ["high", "low", "close"], "func": adxd_042_mdm_rank_126d},
    "adxd_043_mdm_lvl_252d": {"inputs": ["high", "low", "close"], "func": adxd_043_mdm_lvl_252d},
    "adxd_044_mdm_zscore_252d": {"inputs": ["high", "low", "close"], "func": adxd_044_mdm_zscore_252d},
    "adxd_045_mdm_rank_252d": {"inputs": ["high", "low", "close"], "func": adxd_045_mdm_rank_252d},
    "adxd_046_pdi_lvl_5d": {"inputs": ["high", "low", "close"], "func": adxd_046_pdi_lvl_5d},
    "adxd_047_pdi_zscore_5d": {"inputs": ["high", "low", "close"], "func": adxd_047_pdi_zscore_5d},
    "adxd_048_pdi_rank_5d": {"inputs": ["high", "low", "close"], "func": adxd_048_pdi_rank_5d},
    "adxd_049_pdi_lvl_21d": {"inputs": ["high", "low", "close"], "func": adxd_049_pdi_lvl_21d},
    "adxd_050_pdi_zscore_21d": {"inputs": ["high", "low", "close"], "func": adxd_050_pdi_zscore_21d},
    "adxd_051_pdi_rank_21d": {"inputs": ["high", "low", "close"], "func": adxd_051_pdi_rank_21d},
    "adxd_052_pdi_lvl_63d": {"inputs": ["high", "low", "close"], "func": adxd_052_pdi_lvl_63d},
    "adxd_053_pdi_zscore_63d": {"inputs": ["high", "low", "close"], "func": adxd_053_pdi_zscore_63d},
    "adxd_054_pdi_rank_63d": {"inputs": ["high", "low", "close"], "func": adxd_054_pdi_rank_63d},
    "adxd_055_pdi_lvl_126d": {"inputs": ["high", "low", "close"], "func": adxd_055_pdi_lvl_126d},
    "adxd_056_pdi_zscore_126d": {"inputs": ["high", "low", "close"], "func": adxd_056_pdi_zscore_126d},
    "adxd_057_pdi_rank_126d": {"inputs": ["high", "low", "close"], "func": adxd_057_pdi_rank_126d},
    "adxd_058_pdi_lvl_252d": {"inputs": ["high", "low", "close"], "func": adxd_058_pdi_lvl_252d},
    "adxd_059_pdi_zscore_252d": {"inputs": ["high", "low", "close"], "func": adxd_059_pdi_zscore_252d},
    "adxd_060_pdi_rank_252d": {"inputs": ["high", "low", "close"], "func": adxd_060_pdi_rank_252d},
    "adxd_061_mdi_lvl_5d": {"inputs": ["high", "low", "close"], "func": adxd_061_mdi_lvl_5d},
    "adxd_062_mdi_zscore_5d": {"inputs": ["high", "low", "close"], "func": adxd_062_mdi_zscore_5d},
    "adxd_063_mdi_rank_5d": {"inputs": ["high", "low", "close"], "func": adxd_063_mdi_rank_5d},
    "adxd_064_mdi_lvl_21d": {"inputs": ["high", "low", "close"], "func": adxd_064_mdi_lvl_21d},
    "adxd_065_mdi_zscore_21d": {"inputs": ["high", "low", "close"], "func": adxd_065_mdi_zscore_21d},
    "adxd_066_mdi_rank_21d": {"inputs": ["high", "low", "close"], "func": adxd_066_mdi_rank_21d},
    "adxd_067_mdi_lvl_63d": {"inputs": ["high", "low", "close"], "func": adxd_067_mdi_lvl_63d},
    "adxd_068_mdi_zscore_63d": {"inputs": ["high", "low", "close"], "func": adxd_068_mdi_zscore_63d},
    "adxd_069_mdi_rank_63d": {"inputs": ["high", "low", "close"], "func": adxd_069_mdi_rank_63d},
    "adxd_070_mdi_lvl_126d": {"inputs": ["high", "low", "close"], "func": adxd_070_mdi_lvl_126d},
    "adxd_071_mdi_zscore_126d": {"inputs": ["high", "low", "close"], "func": adxd_071_mdi_zscore_126d},
    "adxd_072_mdi_rank_126d": {"inputs": ["high", "low", "close"], "func": adxd_072_mdi_rank_126d},
    "adxd_073_mdi_lvl_252d": {"inputs": ["high", "low", "close"], "func": adxd_073_mdi_lvl_252d},
    "adxd_074_mdi_zscore_252d": {"inputs": ["high", "low", "close"], "func": adxd_074_mdi_zscore_252d},
    "adxd_075_mdi_rank_252d": {"inputs": ["high", "low", "close"], "func": adxd_075_mdi_rank_252d},
}
