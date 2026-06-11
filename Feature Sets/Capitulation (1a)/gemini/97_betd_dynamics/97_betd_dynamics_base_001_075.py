"""
97_betd_dynamics — Base Features 001-075
Domain: betd_dynamics
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

def betd_001_beta_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_001_beta_lvl_5d"""
    base = _safe_div(close.pct_change().rolling(252).cov(mkt_close.pct_change()), mkt_close.pct_change().rolling(252).var())
    return _rolling_mean(base, 5)

def betd_002_beta_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_002_beta_zscore_5d"""
    base = _safe_div(close.pct_change().rolling(252).cov(mkt_close.pct_change()), mkt_close.pct_change().rolling(252).var())
    return _zscore_rolling(base, 5)

def betd_003_beta_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_003_beta_rank_5d"""
    base = _safe_div(close.pct_change().rolling(252).cov(mkt_close.pct_change()), mkt_close.pct_change().rolling(252).var())
    return _rank_pct(base, 5)

def betd_004_beta_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_004_beta_lvl_21d"""
    base = _safe_div(close.pct_change().rolling(252).cov(mkt_close.pct_change()), mkt_close.pct_change().rolling(252).var())
    return _rolling_mean(base, 21)

def betd_005_beta_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_005_beta_zscore_21d"""
    base = _safe_div(close.pct_change().rolling(252).cov(mkt_close.pct_change()), mkt_close.pct_change().rolling(252).var())
    return _zscore_rolling(base, 21)

def betd_006_beta_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_006_beta_rank_21d"""
    base = _safe_div(close.pct_change().rolling(252).cov(mkt_close.pct_change()), mkt_close.pct_change().rolling(252).var())
    return _rank_pct(base, 21)

def betd_007_beta_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_007_beta_lvl_63d"""
    base = _safe_div(close.pct_change().rolling(252).cov(mkt_close.pct_change()), mkt_close.pct_change().rolling(252).var())
    return _rolling_mean(base, 63)

def betd_008_beta_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_008_beta_zscore_63d"""
    base = _safe_div(close.pct_change().rolling(252).cov(mkt_close.pct_change()), mkt_close.pct_change().rolling(252).var())
    return _zscore_rolling(base, 63)

def betd_009_beta_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_009_beta_rank_63d"""
    base = _safe_div(close.pct_change().rolling(252).cov(mkt_close.pct_change()), mkt_close.pct_change().rolling(252).var())
    return _rank_pct(base, 63)

def betd_010_beta_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_010_beta_lvl_126d"""
    base = _safe_div(close.pct_change().rolling(252).cov(mkt_close.pct_change()), mkt_close.pct_change().rolling(252).var())
    return _rolling_mean(base, 126)

def betd_011_beta_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_011_beta_zscore_126d"""
    base = _safe_div(close.pct_change().rolling(252).cov(mkt_close.pct_change()), mkt_close.pct_change().rolling(252).var())
    return _zscore_rolling(base, 126)

def betd_012_beta_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_012_beta_rank_126d"""
    base = _safe_div(close.pct_change().rolling(252).cov(mkt_close.pct_change()), mkt_close.pct_change().rolling(252).var())
    return _rank_pct(base, 126)

def betd_013_beta_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_013_beta_lvl_252d"""
    base = _safe_div(close.pct_change().rolling(252).cov(mkt_close.pct_change()), mkt_close.pct_change().rolling(252).var())
    return _rolling_mean(base, 252)

def betd_014_beta_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_014_beta_zscore_252d"""
    base = _safe_div(close.pct_change().rolling(252).cov(mkt_close.pct_change()), mkt_close.pct_change().rolling(252).var())
    return _zscore_rolling(base, 252)

def betd_015_beta_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_015_beta_rank_252d"""
    base = _safe_div(close.pct_change().rolling(252).cov(mkt_close.pct_change()), mkt_close.pct_change().rolling(252).var())
    return _rank_pct(base, 252)

def betd_016_corr_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_016_corr_lvl_5d"""
    base = close.pct_change().rolling(252).corr(mkt_close.pct_change())
    return _rolling_mean(base, 5)

def betd_017_corr_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_017_corr_zscore_5d"""
    base = close.pct_change().rolling(252).corr(mkt_close.pct_change())
    return _zscore_rolling(base, 5)

def betd_018_corr_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_018_corr_rank_5d"""
    base = close.pct_change().rolling(252).corr(mkt_close.pct_change())
    return _rank_pct(base, 5)

def betd_019_corr_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_019_corr_lvl_21d"""
    base = close.pct_change().rolling(252).corr(mkt_close.pct_change())
    return _rolling_mean(base, 21)

def betd_020_corr_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_020_corr_zscore_21d"""
    base = close.pct_change().rolling(252).corr(mkt_close.pct_change())
    return _zscore_rolling(base, 21)

def betd_021_corr_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_021_corr_rank_21d"""
    base = close.pct_change().rolling(252).corr(mkt_close.pct_change())
    return _rank_pct(base, 21)

def betd_022_corr_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_022_corr_lvl_63d"""
    base = close.pct_change().rolling(252).corr(mkt_close.pct_change())
    return _rolling_mean(base, 63)

def betd_023_corr_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_023_corr_zscore_63d"""
    base = close.pct_change().rolling(252).corr(mkt_close.pct_change())
    return _zscore_rolling(base, 63)

def betd_024_corr_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_024_corr_rank_63d"""
    base = close.pct_change().rolling(252).corr(mkt_close.pct_change())
    return _rank_pct(base, 63)

def betd_025_corr_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_025_corr_lvl_126d"""
    base = close.pct_change().rolling(252).corr(mkt_close.pct_change())
    return _rolling_mean(base, 126)

def betd_026_corr_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_026_corr_zscore_126d"""
    base = close.pct_change().rolling(252).corr(mkt_close.pct_change())
    return _zscore_rolling(base, 126)

def betd_027_corr_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_027_corr_rank_126d"""
    base = close.pct_change().rolling(252).corr(mkt_close.pct_change())
    return _rank_pct(base, 126)

def betd_028_corr_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_028_corr_lvl_252d"""
    base = close.pct_change().rolling(252).corr(mkt_close.pct_change())
    return _rolling_mean(base, 252)

def betd_029_corr_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_029_corr_zscore_252d"""
    base = close.pct_change().rolling(252).corr(mkt_close.pct_change())
    return _zscore_rolling(base, 252)

def betd_030_corr_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_030_corr_rank_252d"""
    base = close.pct_change().rolling(252).corr(mkt_close.pct_change())
    return _rank_pct(base, 252)

def betd_031_idio_vol_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_031_idio_vol_lvl_5d"""
    base = _rolling_std(close.pct_change(), 252) - _safe_div(close.pct_change().rolling(252).cov(mkt_close.pct_change()), mkt_close.pct_change().rolling(252).var()) * _rolling_std(mkt_close.pct_change(), 252)
    return _rolling_mean(base, 5)

def betd_032_idio_vol_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_032_idio_vol_zscore_5d"""
    base = _rolling_std(close.pct_change(), 252) - _safe_div(close.pct_change().rolling(252).cov(mkt_close.pct_change()), mkt_close.pct_change().rolling(252).var()) * _rolling_std(mkt_close.pct_change(), 252)
    return _zscore_rolling(base, 5)

def betd_033_idio_vol_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_033_idio_vol_rank_5d"""
    base = _rolling_std(close.pct_change(), 252) - _safe_div(close.pct_change().rolling(252).cov(mkt_close.pct_change()), mkt_close.pct_change().rolling(252).var()) * _rolling_std(mkt_close.pct_change(), 252)
    return _rank_pct(base, 5)

def betd_034_idio_vol_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_034_idio_vol_lvl_21d"""
    base = _rolling_std(close.pct_change(), 252) - _safe_div(close.pct_change().rolling(252).cov(mkt_close.pct_change()), mkt_close.pct_change().rolling(252).var()) * _rolling_std(mkt_close.pct_change(), 252)
    return _rolling_mean(base, 21)

def betd_035_idio_vol_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_035_idio_vol_zscore_21d"""
    base = _rolling_std(close.pct_change(), 252) - _safe_div(close.pct_change().rolling(252).cov(mkt_close.pct_change()), mkt_close.pct_change().rolling(252).var()) * _rolling_std(mkt_close.pct_change(), 252)
    return _zscore_rolling(base, 21)

def betd_036_idio_vol_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_036_idio_vol_rank_21d"""
    base = _rolling_std(close.pct_change(), 252) - _safe_div(close.pct_change().rolling(252).cov(mkt_close.pct_change()), mkt_close.pct_change().rolling(252).var()) * _rolling_std(mkt_close.pct_change(), 252)
    return _rank_pct(base, 21)

def betd_037_idio_vol_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_037_idio_vol_lvl_63d"""
    base = _rolling_std(close.pct_change(), 252) - _safe_div(close.pct_change().rolling(252).cov(mkt_close.pct_change()), mkt_close.pct_change().rolling(252).var()) * _rolling_std(mkt_close.pct_change(), 252)
    return _rolling_mean(base, 63)

def betd_038_idio_vol_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_038_idio_vol_zscore_63d"""
    base = _rolling_std(close.pct_change(), 252) - _safe_div(close.pct_change().rolling(252).cov(mkt_close.pct_change()), mkt_close.pct_change().rolling(252).var()) * _rolling_std(mkt_close.pct_change(), 252)
    return _zscore_rolling(base, 63)

def betd_039_idio_vol_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_039_idio_vol_rank_63d"""
    base = _rolling_std(close.pct_change(), 252) - _safe_div(close.pct_change().rolling(252).cov(mkt_close.pct_change()), mkt_close.pct_change().rolling(252).var()) * _rolling_std(mkt_close.pct_change(), 252)
    return _rank_pct(base, 63)

def betd_040_idio_vol_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_040_idio_vol_lvl_126d"""
    base = _rolling_std(close.pct_change(), 252) - _safe_div(close.pct_change().rolling(252).cov(mkt_close.pct_change()), mkt_close.pct_change().rolling(252).var()) * _rolling_std(mkt_close.pct_change(), 252)
    return _rolling_mean(base, 126)

def betd_041_idio_vol_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_041_idio_vol_zscore_126d"""
    base = _rolling_std(close.pct_change(), 252) - _safe_div(close.pct_change().rolling(252).cov(mkt_close.pct_change()), mkt_close.pct_change().rolling(252).var()) * _rolling_std(mkt_close.pct_change(), 252)
    return _zscore_rolling(base, 126)

def betd_042_idio_vol_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_042_idio_vol_rank_126d"""
    base = _rolling_std(close.pct_change(), 252) - _safe_div(close.pct_change().rolling(252).cov(mkt_close.pct_change()), mkt_close.pct_change().rolling(252).var()) * _rolling_std(mkt_close.pct_change(), 252)
    return _rank_pct(base, 126)

def betd_043_idio_vol_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_043_idio_vol_lvl_252d"""
    base = _rolling_std(close.pct_change(), 252) - _safe_div(close.pct_change().rolling(252).cov(mkt_close.pct_change()), mkt_close.pct_change().rolling(252).var()) * _rolling_std(mkt_close.pct_change(), 252)
    return _rolling_mean(base, 252)

def betd_044_idio_vol_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_044_idio_vol_zscore_252d"""
    base = _rolling_std(close.pct_change(), 252) - _safe_div(close.pct_change().rolling(252).cov(mkt_close.pct_change()), mkt_close.pct_change().rolling(252).var()) * _rolling_std(mkt_close.pct_change(), 252)
    return _zscore_rolling(base, 252)

def betd_045_idio_vol_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_045_idio_vol_rank_252d"""
    base = _rolling_std(close.pct_change(), 252) - _safe_div(close.pct_change().rolling(252).cov(mkt_close.pct_change()), mkt_close.pct_change().rolling(252).var()) * _rolling_std(mkt_close.pct_change(), 252)
    return _rank_pct(base, 252)

def betd_046_beta_63_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_046_beta_63_lvl_5d"""
    base = _safe_div(close.pct_change().rolling(63).cov(mkt_close.pct_change()), mkt_close.pct_change().rolling(63).var())
    return _rolling_mean(base, 5)

def betd_047_beta_63_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_047_beta_63_zscore_5d"""
    base = _safe_div(close.pct_change().rolling(63).cov(mkt_close.pct_change()), mkt_close.pct_change().rolling(63).var())
    return _zscore_rolling(base, 5)

def betd_048_beta_63_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_048_beta_63_rank_5d"""
    base = _safe_div(close.pct_change().rolling(63).cov(mkt_close.pct_change()), mkt_close.pct_change().rolling(63).var())
    return _rank_pct(base, 5)

def betd_049_beta_63_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_049_beta_63_lvl_21d"""
    base = _safe_div(close.pct_change().rolling(63).cov(mkt_close.pct_change()), mkt_close.pct_change().rolling(63).var())
    return _rolling_mean(base, 21)

def betd_050_beta_63_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_050_beta_63_zscore_21d"""
    base = _safe_div(close.pct_change().rolling(63).cov(mkt_close.pct_change()), mkt_close.pct_change().rolling(63).var())
    return _zscore_rolling(base, 21)

def betd_051_beta_63_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_051_beta_63_rank_21d"""
    base = _safe_div(close.pct_change().rolling(63).cov(mkt_close.pct_change()), mkt_close.pct_change().rolling(63).var())
    return _rank_pct(base, 21)

def betd_052_beta_63_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_052_beta_63_lvl_63d"""
    base = _safe_div(close.pct_change().rolling(63).cov(mkt_close.pct_change()), mkt_close.pct_change().rolling(63).var())
    return _rolling_mean(base, 63)

def betd_053_beta_63_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_053_beta_63_zscore_63d"""
    base = _safe_div(close.pct_change().rolling(63).cov(mkt_close.pct_change()), mkt_close.pct_change().rolling(63).var())
    return _zscore_rolling(base, 63)

def betd_054_beta_63_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_054_beta_63_rank_63d"""
    base = _safe_div(close.pct_change().rolling(63).cov(mkt_close.pct_change()), mkt_close.pct_change().rolling(63).var())
    return _rank_pct(base, 63)

def betd_055_beta_63_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_055_beta_63_lvl_126d"""
    base = _safe_div(close.pct_change().rolling(63).cov(mkt_close.pct_change()), mkt_close.pct_change().rolling(63).var())
    return _rolling_mean(base, 126)

def betd_056_beta_63_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_056_beta_63_zscore_126d"""
    base = _safe_div(close.pct_change().rolling(63).cov(mkt_close.pct_change()), mkt_close.pct_change().rolling(63).var())
    return _zscore_rolling(base, 126)

def betd_057_beta_63_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_057_beta_63_rank_126d"""
    base = _safe_div(close.pct_change().rolling(63).cov(mkt_close.pct_change()), mkt_close.pct_change().rolling(63).var())
    return _rank_pct(base, 126)

def betd_058_beta_63_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_058_beta_63_lvl_252d"""
    base = _safe_div(close.pct_change().rolling(63).cov(mkt_close.pct_change()), mkt_close.pct_change().rolling(63).var())
    return _rolling_mean(base, 252)

def betd_059_beta_63_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_059_beta_63_zscore_252d"""
    base = _safe_div(close.pct_change().rolling(63).cov(mkt_close.pct_change()), mkt_close.pct_change().rolling(63).var())
    return _zscore_rolling(base, 252)

def betd_060_beta_63_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_060_beta_63_rank_252d"""
    base = _safe_div(close.pct_change().rolling(63).cov(mkt_close.pct_change()), mkt_close.pct_change().rolling(63).var())
    return _rank_pct(base, 252)

def betd_061_corr_63_lvl_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_061_corr_63_lvl_5d"""
    base = close.pct_change().rolling(63).corr(mkt_close.pct_change())
    return _rolling_mean(base, 5)

def betd_062_corr_63_zscore_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_062_corr_63_zscore_5d"""
    base = close.pct_change().rolling(63).corr(mkt_close.pct_change())
    return _zscore_rolling(base, 5)

def betd_063_corr_63_rank_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_063_corr_63_rank_5d"""
    base = close.pct_change().rolling(63).corr(mkt_close.pct_change())
    return _rank_pct(base, 5)

def betd_064_corr_63_lvl_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_064_corr_63_lvl_21d"""
    base = close.pct_change().rolling(63).corr(mkt_close.pct_change())
    return _rolling_mean(base, 21)

def betd_065_corr_63_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_065_corr_63_zscore_21d"""
    base = close.pct_change().rolling(63).corr(mkt_close.pct_change())
    return _zscore_rolling(base, 21)

def betd_066_corr_63_rank_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_066_corr_63_rank_21d"""
    base = close.pct_change().rolling(63).corr(mkt_close.pct_change())
    return _rank_pct(base, 21)

def betd_067_corr_63_lvl_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_067_corr_63_lvl_63d"""
    base = close.pct_change().rolling(63).corr(mkt_close.pct_change())
    return _rolling_mean(base, 63)

def betd_068_corr_63_zscore_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_068_corr_63_zscore_63d"""
    base = close.pct_change().rolling(63).corr(mkt_close.pct_change())
    return _zscore_rolling(base, 63)

def betd_069_corr_63_rank_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_069_corr_63_rank_63d"""
    base = close.pct_change().rolling(63).corr(mkt_close.pct_change())
    return _rank_pct(base, 63)

def betd_070_corr_63_lvl_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_070_corr_63_lvl_126d"""
    base = close.pct_change().rolling(63).corr(mkt_close.pct_change())
    return _rolling_mean(base, 126)

def betd_071_corr_63_zscore_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_071_corr_63_zscore_126d"""
    base = close.pct_change().rolling(63).corr(mkt_close.pct_change())
    return _zscore_rolling(base, 126)

def betd_072_corr_63_rank_126d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_072_corr_63_rank_126d"""
    base = close.pct_change().rolling(63).corr(mkt_close.pct_change())
    return _rank_pct(base, 126)

def betd_073_corr_63_lvl_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_073_corr_63_lvl_252d"""
    base = close.pct_change().rolling(63).corr(mkt_close.pct_change())
    return _rolling_mean(base, 252)

def betd_074_corr_63_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_074_corr_63_zscore_252d"""
    base = close.pct_change().rolling(63).corr(mkt_close.pct_change())
    return _zscore_rolling(base, 252)

def betd_075_corr_63_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series) -> pd.Series:
    """betd_075_corr_63_rank_252d"""
    base = close.pct_change().rolling(63).corr(mkt_close.pct_change())
    return _rank_pct(base, 252)

# ── Registry ──────────────────────────────────────────────────────────────────
V97_REGISTRY = {
    "betd_001_beta_lvl_5d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_001_beta_lvl_5d},
    "betd_002_beta_zscore_5d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_002_beta_zscore_5d},
    "betd_003_beta_rank_5d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_003_beta_rank_5d},
    "betd_004_beta_lvl_21d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_004_beta_lvl_21d},
    "betd_005_beta_zscore_21d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_005_beta_zscore_21d},
    "betd_006_beta_rank_21d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_006_beta_rank_21d},
    "betd_007_beta_lvl_63d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_007_beta_lvl_63d},
    "betd_008_beta_zscore_63d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_008_beta_zscore_63d},
    "betd_009_beta_rank_63d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_009_beta_rank_63d},
    "betd_010_beta_lvl_126d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_010_beta_lvl_126d},
    "betd_011_beta_zscore_126d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_011_beta_zscore_126d},
    "betd_012_beta_rank_126d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_012_beta_rank_126d},
    "betd_013_beta_lvl_252d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_013_beta_lvl_252d},
    "betd_014_beta_zscore_252d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_014_beta_zscore_252d},
    "betd_015_beta_rank_252d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_015_beta_rank_252d},
    "betd_016_corr_lvl_5d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_016_corr_lvl_5d},
    "betd_017_corr_zscore_5d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_017_corr_zscore_5d},
    "betd_018_corr_rank_5d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_018_corr_rank_5d},
    "betd_019_corr_lvl_21d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_019_corr_lvl_21d},
    "betd_020_corr_zscore_21d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_020_corr_zscore_21d},
    "betd_021_corr_rank_21d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_021_corr_rank_21d},
    "betd_022_corr_lvl_63d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_022_corr_lvl_63d},
    "betd_023_corr_zscore_63d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_023_corr_zscore_63d},
    "betd_024_corr_rank_63d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_024_corr_rank_63d},
    "betd_025_corr_lvl_126d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_025_corr_lvl_126d},
    "betd_026_corr_zscore_126d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_026_corr_zscore_126d},
    "betd_027_corr_rank_126d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_027_corr_rank_126d},
    "betd_028_corr_lvl_252d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_028_corr_lvl_252d},
    "betd_029_corr_zscore_252d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_029_corr_zscore_252d},
    "betd_030_corr_rank_252d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_030_corr_rank_252d},
    "betd_031_idio_vol_lvl_5d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_031_idio_vol_lvl_5d},
    "betd_032_idio_vol_zscore_5d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_032_idio_vol_zscore_5d},
    "betd_033_idio_vol_rank_5d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_033_idio_vol_rank_5d},
    "betd_034_idio_vol_lvl_21d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_034_idio_vol_lvl_21d},
    "betd_035_idio_vol_zscore_21d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_035_idio_vol_zscore_21d},
    "betd_036_idio_vol_rank_21d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_036_idio_vol_rank_21d},
    "betd_037_idio_vol_lvl_63d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_037_idio_vol_lvl_63d},
    "betd_038_idio_vol_zscore_63d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_038_idio_vol_zscore_63d},
    "betd_039_idio_vol_rank_63d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_039_idio_vol_rank_63d},
    "betd_040_idio_vol_lvl_126d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_040_idio_vol_lvl_126d},
    "betd_041_idio_vol_zscore_126d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_041_idio_vol_zscore_126d},
    "betd_042_idio_vol_rank_126d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_042_idio_vol_rank_126d},
    "betd_043_idio_vol_lvl_252d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_043_idio_vol_lvl_252d},
    "betd_044_idio_vol_zscore_252d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_044_idio_vol_zscore_252d},
    "betd_045_idio_vol_rank_252d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_045_idio_vol_rank_252d},
    "betd_046_beta_63_lvl_5d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_046_beta_63_lvl_5d},
    "betd_047_beta_63_zscore_5d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_047_beta_63_zscore_5d},
    "betd_048_beta_63_rank_5d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_048_beta_63_rank_5d},
    "betd_049_beta_63_lvl_21d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_049_beta_63_lvl_21d},
    "betd_050_beta_63_zscore_21d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_050_beta_63_zscore_21d},
    "betd_051_beta_63_rank_21d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_051_beta_63_rank_21d},
    "betd_052_beta_63_lvl_63d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_052_beta_63_lvl_63d},
    "betd_053_beta_63_zscore_63d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_053_beta_63_zscore_63d},
    "betd_054_beta_63_rank_63d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_054_beta_63_rank_63d},
    "betd_055_beta_63_lvl_126d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_055_beta_63_lvl_126d},
    "betd_056_beta_63_zscore_126d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_056_beta_63_zscore_126d},
    "betd_057_beta_63_rank_126d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_057_beta_63_rank_126d},
    "betd_058_beta_63_lvl_252d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_058_beta_63_lvl_252d},
    "betd_059_beta_63_zscore_252d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_059_beta_63_zscore_252d},
    "betd_060_beta_63_rank_252d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_060_beta_63_rank_252d},
    "betd_061_corr_63_lvl_5d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_061_corr_63_lvl_5d},
    "betd_062_corr_63_zscore_5d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_062_corr_63_zscore_5d},
    "betd_063_corr_63_rank_5d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_063_corr_63_rank_5d},
    "betd_064_corr_63_lvl_21d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_064_corr_63_lvl_21d},
    "betd_065_corr_63_zscore_21d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_065_corr_63_zscore_21d},
    "betd_066_corr_63_rank_21d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_066_corr_63_rank_21d},
    "betd_067_corr_63_lvl_63d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_067_corr_63_lvl_63d},
    "betd_068_corr_63_zscore_63d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_068_corr_63_zscore_63d},
    "betd_069_corr_63_rank_63d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_069_corr_63_rank_63d},
    "betd_070_corr_63_lvl_126d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_070_corr_63_lvl_126d},
    "betd_071_corr_63_zscore_126d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_071_corr_63_zscore_126d},
    "betd_072_corr_63_rank_126d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_072_corr_63_rank_126d},
    "betd_073_corr_63_lvl_252d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_073_corr_63_lvl_252d},
    "betd_074_corr_63_zscore_252d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_074_corr_63_zscore_252d},
    "betd_075_corr_63_rank_252d": {"inputs": ["high", "low", "close", "volume", "mkt_close", "mkt_volume"], "func": betd_075_corr_63_rank_252d},
}
