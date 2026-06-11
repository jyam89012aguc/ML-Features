"""
80_ccid_dynamics — Base Features 001-075
Domain: ccid_dynamics
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

def ccid_001_tp_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_001_tp_lvl_5d"""
    base = (high + low + close) / 3
    return _rolling_mean(base, 5)

def ccid_002_tp_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_002_tp_zscore_5d"""
    base = (high + low + close) / 3
    return _zscore_rolling(base, 5)

def ccid_003_tp_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_003_tp_rank_5d"""
    base = (high + low + close) / 3
    return _rank_pct(base, 5)

def ccid_004_tp_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_004_tp_lvl_21d"""
    base = (high + low + close) / 3
    return _rolling_mean(base, 21)

def ccid_005_tp_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_005_tp_zscore_21d"""
    base = (high + low + close) / 3
    return _zscore_rolling(base, 21)

def ccid_006_tp_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_006_tp_rank_21d"""
    base = (high + low + close) / 3
    return _rank_pct(base, 21)

def ccid_007_tp_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_007_tp_lvl_63d"""
    base = (high + low + close) / 3
    return _rolling_mean(base, 63)

def ccid_008_tp_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_008_tp_zscore_63d"""
    base = (high + low + close) / 3
    return _zscore_rolling(base, 63)

def ccid_009_tp_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_009_tp_rank_63d"""
    base = (high + low + close) / 3
    return _rank_pct(base, 63)

def ccid_010_tp_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_010_tp_lvl_126d"""
    base = (high + low + close) / 3
    return _rolling_mean(base, 126)

def ccid_011_tp_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_011_tp_zscore_126d"""
    base = (high + low + close) / 3
    return _zscore_rolling(base, 126)

def ccid_012_tp_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_012_tp_rank_126d"""
    base = (high + low + close) / 3
    return _rank_pct(base, 126)

def ccid_013_tp_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_013_tp_lvl_252d"""
    base = (high + low + close) / 3
    return _rolling_mean(base, 252)

def ccid_014_tp_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_014_tp_zscore_252d"""
    base = (high + low + close) / 3
    return _zscore_rolling(base, 252)

def ccid_015_tp_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_015_tp_rank_252d"""
    base = (high + low + close) / 3
    return _rank_pct(base, 252)

def ccid_016_cci20_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_016_cci20_lvl_5d"""
    base = _safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True))
    return _rolling_mean(base, 5)

def ccid_017_cci20_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_017_cci20_zscore_5d"""
    base = _safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True))
    return _zscore_rolling(base, 5)

def ccid_018_cci20_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_018_cci20_rank_5d"""
    base = _safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True))
    return _rank_pct(base, 5)

def ccid_019_cci20_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_019_cci20_lvl_21d"""
    base = _safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True))
    return _rolling_mean(base, 21)

def ccid_020_cci20_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_020_cci20_zscore_21d"""
    base = _safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True))
    return _zscore_rolling(base, 21)

def ccid_021_cci20_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_021_cci20_rank_21d"""
    base = _safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True))
    return _rank_pct(base, 21)

def ccid_022_cci20_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_022_cci20_lvl_63d"""
    base = _safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True))
    return _rolling_mean(base, 63)

def ccid_023_cci20_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_023_cci20_zscore_63d"""
    base = _safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True))
    return _zscore_rolling(base, 63)

def ccid_024_cci20_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_024_cci20_rank_63d"""
    base = _safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True))
    return _rank_pct(base, 63)

def ccid_025_cci20_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_025_cci20_lvl_126d"""
    base = _safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True))
    return _rolling_mean(base, 126)

def ccid_026_cci20_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_026_cci20_zscore_126d"""
    base = _safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True))
    return _zscore_rolling(base, 126)

def ccid_027_cci20_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_027_cci20_rank_126d"""
    base = _safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True))
    return _rank_pct(base, 126)

def ccid_028_cci20_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_028_cci20_lvl_252d"""
    base = _safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True))
    return _rolling_mean(base, 252)

def ccid_029_cci20_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_029_cci20_zscore_252d"""
    base = _safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True))
    return _zscore_rolling(base, 252)

def ccid_030_cci20_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_030_cci20_rank_252d"""
    base = _safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True))
    return _rank_pct(base, 252)

def ccid_031_cci_dist_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_031_cci_dist_lvl_5d"""
    base = _safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True)) - 100
    return _rolling_mean(base, 5)

def ccid_032_cci_dist_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_032_cci_dist_zscore_5d"""
    base = _safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True)) - 100
    return _zscore_rolling(base, 5)

def ccid_033_cci_dist_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_033_cci_dist_rank_5d"""
    base = _safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True)) - 100
    return _rank_pct(base, 5)

def ccid_034_cci_dist_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_034_cci_dist_lvl_21d"""
    base = _safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True)) - 100
    return _rolling_mean(base, 21)

def ccid_035_cci_dist_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_035_cci_dist_zscore_21d"""
    base = _safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True)) - 100
    return _zscore_rolling(base, 21)

def ccid_036_cci_dist_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_036_cci_dist_rank_21d"""
    base = _safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True)) - 100
    return _rank_pct(base, 21)

def ccid_037_cci_dist_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_037_cci_dist_lvl_63d"""
    base = _safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True)) - 100
    return _rolling_mean(base, 63)

def ccid_038_cci_dist_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_038_cci_dist_zscore_63d"""
    base = _safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True)) - 100
    return _zscore_rolling(base, 63)

def ccid_039_cci_dist_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_039_cci_dist_rank_63d"""
    base = _safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True)) - 100
    return _rank_pct(base, 63)

def ccid_040_cci_dist_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_040_cci_dist_lvl_126d"""
    base = _safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True)) - 100
    return _rolling_mean(base, 126)

def ccid_041_cci_dist_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_041_cci_dist_zscore_126d"""
    base = _safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True)) - 100
    return _zscore_rolling(base, 126)

def ccid_042_cci_dist_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_042_cci_dist_rank_126d"""
    base = _safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True)) - 100
    return _rank_pct(base, 126)

def ccid_043_cci_dist_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_043_cci_dist_lvl_252d"""
    base = _safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True)) - 100
    return _rolling_mean(base, 252)

def ccid_044_cci_dist_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_044_cci_dist_zscore_252d"""
    base = _safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True)) - 100
    return _zscore_rolling(base, 252)

def ccid_045_cci_dist_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_045_cci_dist_rank_252d"""
    base = _safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True)) - 100
    return _rank_pct(base, 252)

def ccid_046_cci_z_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_046_cci_z_lvl_5d"""
    base = _zscore_rolling(_safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True)), 63)
    return _rolling_mean(base, 5)

def ccid_047_cci_z_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_047_cci_z_zscore_5d"""
    base = _zscore_rolling(_safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True)), 63)
    return _zscore_rolling(base, 5)

def ccid_048_cci_z_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_048_cci_z_rank_5d"""
    base = _zscore_rolling(_safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True)), 63)
    return _rank_pct(base, 5)

def ccid_049_cci_z_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_049_cci_z_lvl_21d"""
    base = _zscore_rolling(_safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True)), 63)
    return _rolling_mean(base, 21)

def ccid_050_cci_z_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_050_cci_z_zscore_21d"""
    base = _zscore_rolling(_safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True)), 63)
    return _zscore_rolling(base, 21)

def ccid_051_cci_z_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_051_cci_z_rank_21d"""
    base = _zscore_rolling(_safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True)), 63)
    return _rank_pct(base, 21)

def ccid_052_cci_z_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_052_cci_z_lvl_63d"""
    base = _zscore_rolling(_safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True)), 63)
    return _rolling_mean(base, 63)

def ccid_053_cci_z_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_053_cci_z_zscore_63d"""
    base = _zscore_rolling(_safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True)), 63)
    return _zscore_rolling(base, 63)

def ccid_054_cci_z_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_054_cci_z_rank_63d"""
    base = _zscore_rolling(_safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True)), 63)
    return _rank_pct(base, 63)

def ccid_055_cci_z_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_055_cci_z_lvl_126d"""
    base = _zscore_rolling(_safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True)), 63)
    return _rolling_mean(base, 126)

def ccid_056_cci_z_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_056_cci_z_zscore_126d"""
    base = _zscore_rolling(_safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True)), 63)
    return _zscore_rolling(base, 126)

def ccid_057_cci_z_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_057_cci_z_rank_126d"""
    base = _zscore_rolling(_safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True)), 63)
    return _rank_pct(base, 126)

def ccid_058_cci_z_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_058_cci_z_lvl_252d"""
    base = _zscore_rolling(_safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True)), 63)
    return _rolling_mean(base, 252)

def ccid_059_cci_z_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_059_cci_z_zscore_252d"""
    base = _zscore_rolling(_safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True)), 63)
    return _zscore_rolling(base, 252)

def ccid_060_cci_z_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_060_cci_z_rank_252d"""
    base = _zscore_rolling(_safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True)), 63)
    return _rank_pct(base, 252)

def ccid_061_cci_slope_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_061_cci_slope_lvl_5d"""
    base = (_safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True))).diff(5)
    return _rolling_mean(base, 5)

def ccid_062_cci_slope_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_062_cci_slope_zscore_5d"""
    base = (_safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True))).diff(5)
    return _zscore_rolling(base, 5)

def ccid_063_cci_slope_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_063_cci_slope_rank_5d"""
    base = (_safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True))).diff(5)
    return _rank_pct(base, 5)

def ccid_064_cci_slope_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_064_cci_slope_lvl_21d"""
    base = (_safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True))).diff(5)
    return _rolling_mean(base, 21)

def ccid_065_cci_slope_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_065_cci_slope_zscore_21d"""
    base = (_safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True))).diff(5)
    return _zscore_rolling(base, 21)

def ccid_066_cci_slope_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_066_cci_slope_rank_21d"""
    base = (_safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True))).diff(5)
    return _rank_pct(base, 21)

def ccid_067_cci_slope_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_067_cci_slope_lvl_63d"""
    base = (_safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True))).diff(5)
    return _rolling_mean(base, 63)

def ccid_068_cci_slope_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_068_cci_slope_zscore_63d"""
    base = (_safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True))).diff(5)
    return _zscore_rolling(base, 63)

def ccid_069_cci_slope_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_069_cci_slope_rank_63d"""
    base = (_safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True))).diff(5)
    return _rank_pct(base, 63)

def ccid_070_cci_slope_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_070_cci_slope_lvl_126d"""
    base = (_safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True))).diff(5)
    return _rolling_mean(base, 126)

def ccid_071_cci_slope_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_071_cci_slope_zscore_126d"""
    base = (_safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True))).diff(5)
    return _zscore_rolling(base, 126)

def ccid_072_cci_slope_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_072_cci_slope_rank_126d"""
    base = (_safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True))).diff(5)
    return _rank_pct(base, 126)

def ccid_073_cci_slope_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_073_cci_slope_lvl_252d"""
    base = (_safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True))).diff(5)
    return _rolling_mean(base, 252)

def ccid_074_cci_slope_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_074_cci_slope_zscore_252d"""
    base = (_safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True))).diff(5)
    return _zscore_rolling(base, 252)

def ccid_075_cci_slope_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ccid_075_cci_slope_rank_252d"""
    base = (_safe_div(((high + low + close) / 3) - _rolling_mean((high + low + close) / 3, 20), 0.015 * ((high + low + close) / 3).rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True))).diff(5)
    return _rank_pct(base, 252)

# ── Registry ──────────────────────────────────────────────────────────────────
V80_REGISTRY = {
    "ccid_001_tp_lvl_5d": {"inputs": ["high", "low", "close"], "func": ccid_001_tp_lvl_5d},
    "ccid_002_tp_zscore_5d": {"inputs": ["high", "low", "close"], "func": ccid_002_tp_zscore_5d},
    "ccid_003_tp_rank_5d": {"inputs": ["high", "low", "close"], "func": ccid_003_tp_rank_5d},
    "ccid_004_tp_lvl_21d": {"inputs": ["high", "low", "close"], "func": ccid_004_tp_lvl_21d},
    "ccid_005_tp_zscore_21d": {"inputs": ["high", "low", "close"], "func": ccid_005_tp_zscore_21d},
    "ccid_006_tp_rank_21d": {"inputs": ["high", "low", "close"], "func": ccid_006_tp_rank_21d},
    "ccid_007_tp_lvl_63d": {"inputs": ["high", "low", "close"], "func": ccid_007_tp_lvl_63d},
    "ccid_008_tp_zscore_63d": {"inputs": ["high", "low", "close"], "func": ccid_008_tp_zscore_63d},
    "ccid_009_tp_rank_63d": {"inputs": ["high", "low", "close"], "func": ccid_009_tp_rank_63d},
    "ccid_010_tp_lvl_126d": {"inputs": ["high", "low", "close"], "func": ccid_010_tp_lvl_126d},
    "ccid_011_tp_zscore_126d": {"inputs": ["high", "low", "close"], "func": ccid_011_tp_zscore_126d},
    "ccid_012_tp_rank_126d": {"inputs": ["high", "low", "close"], "func": ccid_012_tp_rank_126d},
    "ccid_013_tp_lvl_252d": {"inputs": ["high", "low", "close"], "func": ccid_013_tp_lvl_252d},
    "ccid_014_tp_zscore_252d": {"inputs": ["high", "low", "close"], "func": ccid_014_tp_zscore_252d},
    "ccid_015_tp_rank_252d": {"inputs": ["high", "low", "close"], "func": ccid_015_tp_rank_252d},
    "ccid_016_cci20_lvl_5d": {"inputs": ["high", "low", "close"], "func": ccid_016_cci20_lvl_5d},
    "ccid_017_cci20_zscore_5d": {"inputs": ["high", "low", "close"], "func": ccid_017_cci20_zscore_5d},
    "ccid_018_cci20_rank_5d": {"inputs": ["high", "low", "close"], "func": ccid_018_cci20_rank_5d},
    "ccid_019_cci20_lvl_21d": {"inputs": ["high", "low", "close"], "func": ccid_019_cci20_lvl_21d},
    "ccid_020_cci20_zscore_21d": {"inputs": ["high", "low", "close"], "func": ccid_020_cci20_zscore_21d},
    "ccid_021_cci20_rank_21d": {"inputs": ["high", "low", "close"], "func": ccid_021_cci20_rank_21d},
    "ccid_022_cci20_lvl_63d": {"inputs": ["high", "low", "close"], "func": ccid_022_cci20_lvl_63d},
    "ccid_023_cci20_zscore_63d": {"inputs": ["high", "low", "close"], "func": ccid_023_cci20_zscore_63d},
    "ccid_024_cci20_rank_63d": {"inputs": ["high", "low", "close"], "func": ccid_024_cci20_rank_63d},
    "ccid_025_cci20_lvl_126d": {"inputs": ["high", "low", "close"], "func": ccid_025_cci20_lvl_126d},
    "ccid_026_cci20_zscore_126d": {"inputs": ["high", "low", "close"], "func": ccid_026_cci20_zscore_126d},
    "ccid_027_cci20_rank_126d": {"inputs": ["high", "low", "close"], "func": ccid_027_cci20_rank_126d},
    "ccid_028_cci20_lvl_252d": {"inputs": ["high", "low", "close"], "func": ccid_028_cci20_lvl_252d},
    "ccid_029_cci20_zscore_252d": {"inputs": ["high", "low", "close"], "func": ccid_029_cci20_zscore_252d},
    "ccid_030_cci20_rank_252d": {"inputs": ["high", "low", "close"], "func": ccid_030_cci20_rank_252d},
    "ccid_031_cci_dist_lvl_5d": {"inputs": ["high", "low", "close"], "func": ccid_031_cci_dist_lvl_5d},
    "ccid_032_cci_dist_zscore_5d": {"inputs": ["high", "low", "close"], "func": ccid_032_cci_dist_zscore_5d},
    "ccid_033_cci_dist_rank_5d": {"inputs": ["high", "low", "close"], "func": ccid_033_cci_dist_rank_5d},
    "ccid_034_cci_dist_lvl_21d": {"inputs": ["high", "low", "close"], "func": ccid_034_cci_dist_lvl_21d},
    "ccid_035_cci_dist_zscore_21d": {"inputs": ["high", "low", "close"], "func": ccid_035_cci_dist_zscore_21d},
    "ccid_036_cci_dist_rank_21d": {"inputs": ["high", "low", "close"], "func": ccid_036_cci_dist_rank_21d},
    "ccid_037_cci_dist_lvl_63d": {"inputs": ["high", "low", "close"], "func": ccid_037_cci_dist_lvl_63d},
    "ccid_038_cci_dist_zscore_63d": {"inputs": ["high", "low", "close"], "func": ccid_038_cci_dist_zscore_63d},
    "ccid_039_cci_dist_rank_63d": {"inputs": ["high", "low", "close"], "func": ccid_039_cci_dist_rank_63d},
    "ccid_040_cci_dist_lvl_126d": {"inputs": ["high", "low", "close"], "func": ccid_040_cci_dist_lvl_126d},
    "ccid_041_cci_dist_zscore_126d": {"inputs": ["high", "low", "close"], "func": ccid_041_cci_dist_zscore_126d},
    "ccid_042_cci_dist_rank_126d": {"inputs": ["high", "low", "close"], "func": ccid_042_cci_dist_rank_126d},
    "ccid_043_cci_dist_lvl_252d": {"inputs": ["high", "low", "close"], "func": ccid_043_cci_dist_lvl_252d},
    "ccid_044_cci_dist_zscore_252d": {"inputs": ["high", "low", "close"], "func": ccid_044_cci_dist_zscore_252d},
    "ccid_045_cci_dist_rank_252d": {"inputs": ["high", "low", "close"], "func": ccid_045_cci_dist_rank_252d},
    "ccid_046_cci_z_lvl_5d": {"inputs": ["high", "low", "close"], "func": ccid_046_cci_z_lvl_5d},
    "ccid_047_cci_z_zscore_5d": {"inputs": ["high", "low", "close"], "func": ccid_047_cci_z_zscore_5d},
    "ccid_048_cci_z_rank_5d": {"inputs": ["high", "low", "close"], "func": ccid_048_cci_z_rank_5d},
    "ccid_049_cci_z_lvl_21d": {"inputs": ["high", "low", "close"], "func": ccid_049_cci_z_lvl_21d},
    "ccid_050_cci_z_zscore_21d": {"inputs": ["high", "low", "close"], "func": ccid_050_cci_z_zscore_21d},
    "ccid_051_cci_z_rank_21d": {"inputs": ["high", "low", "close"], "func": ccid_051_cci_z_rank_21d},
    "ccid_052_cci_z_lvl_63d": {"inputs": ["high", "low", "close"], "func": ccid_052_cci_z_lvl_63d},
    "ccid_053_cci_z_zscore_63d": {"inputs": ["high", "low", "close"], "func": ccid_053_cci_z_zscore_63d},
    "ccid_054_cci_z_rank_63d": {"inputs": ["high", "low", "close"], "func": ccid_054_cci_z_rank_63d},
    "ccid_055_cci_z_lvl_126d": {"inputs": ["high", "low", "close"], "func": ccid_055_cci_z_lvl_126d},
    "ccid_056_cci_z_zscore_126d": {"inputs": ["high", "low", "close"], "func": ccid_056_cci_z_zscore_126d},
    "ccid_057_cci_z_rank_126d": {"inputs": ["high", "low", "close"], "func": ccid_057_cci_z_rank_126d},
    "ccid_058_cci_z_lvl_252d": {"inputs": ["high", "low", "close"], "func": ccid_058_cci_z_lvl_252d},
    "ccid_059_cci_z_zscore_252d": {"inputs": ["high", "low", "close"], "func": ccid_059_cci_z_zscore_252d},
    "ccid_060_cci_z_rank_252d": {"inputs": ["high", "low", "close"], "func": ccid_060_cci_z_rank_252d},
    "ccid_061_cci_slope_lvl_5d": {"inputs": ["high", "low", "close"], "func": ccid_061_cci_slope_lvl_5d},
    "ccid_062_cci_slope_zscore_5d": {"inputs": ["high", "low", "close"], "func": ccid_062_cci_slope_zscore_5d},
    "ccid_063_cci_slope_rank_5d": {"inputs": ["high", "low", "close"], "func": ccid_063_cci_slope_rank_5d},
    "ccid_064_cci_slope_lvl_21d": {"inputs": ["high", "low", "close"], "func": ccid_064_cci_slope_lvl_21d},
    "ccid_065_cci_slope_zscore_21d": {"inputs": ["high", "low", "close"], "func": ccid_065_cci_slope_zscore_21d},
    "ccid_066_cci_slope_rank_21d": {"inputs": ["high", "low", "close"], "func": ccid_066_cci_slope_rank_21d},
    "ccid_067_cci_slope_lvl_63d": {"inputs": ["high", "low", "close"], "func": ccid_067_cci_slope_lvl_63d},
    "ccid_068_cci_slope_zscore_63d": {"inputs": ["high", "low", "close"], "func": ccid_068_cci_slope_zscore_63d},
    "ccid_069_cci_slope_rank_63d": {"inputs": ["high", "low", "close"], "func": ccid_069_cci_slope_rank_63d},
    "ccid_070_cci_slope_lvl_126d": {"inputs": ["high", "low", "close"], "func": ccid_070_cci_slope_lvl_126d},
    "ccid_071_cci_slope_zscore_126d": {"inputs": ["high", "low", "close"], "func": ccid_071_cci_slope_zscore_126d},
    "ccid_072_cci_slope_rank_126d": {"inputs": ["high", "low", "close"], "func": ccid_072_cci_slope_rank_126d},
    "ccid_073_cci_slope_lvl_252d": {"inputs": ["high", "low", "close"], "func": ccid_073_cci_slope_lvl_252d},
    "ccid_074_cci_slope_zscore_252d": {"inputs": ["high", "low", "close"], "func": ccid_074_cci_slope_zscore_252d},
    "ccid_075_cci_slope_rank_252d": {"inputs": ["high", "low", "close"], "func": ccid_075_cci_slope_rank_252d},
}
