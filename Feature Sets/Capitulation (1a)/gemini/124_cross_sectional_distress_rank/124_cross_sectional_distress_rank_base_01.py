"""
124_cross_sectional_distress_rank — Base Features Part 1
Domain: cross_sectional_distress_rank
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

def csdr_001_price_rank_xs_lvl_5d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_001_price_rank_xs_lvl_5d
    ECONOMIC RATIONALE: Rank of price drawdown vs history (proxy for cross-sectional rank).
    """
    base = _rank_pct(close / close.rolling(252).max(), 252)
    return _rolling_mean(base, 5)

def csdr_002_price_rank_xs_zscore_5d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_002_price_rank_xs_zscore_5d
    ECONOMIC RATIONALE: Rank of price drawdown vs history (proxy for cross-sectional rank).
    """
    base = _rank_pct(close / close.rolling(252).max(), 252)
    return _zscore_rolling(base, 5)

def csdr_003_price_rank_xs_rank_5d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_003_price_rank_xs_rank_5d
    ECONOMIC RATIONALE: Rank of price drawdown vs history (proxy for cross-sectional rank).
    """
    base = _rank_pct(close / close.rolling(252).max(), 252)
    return _rank_pct(base, 5)

def csdr_004_price_rank_xs_lvl_21d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_004_price_rank_xs_lvl_21d
    ECONOMIC RATIONALE: Rank of price drawdown vs history (proxy for cross-sectional rank).
    """
    base = _rank_pct(close / close.rolling(252).max(), 252)
    return _rolling_mean(base, 21)

def csdr_005_price_rank_xs_zscore_21d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_005_price_rank_xs_zscore_21d
    ECONOMIC RATIONALE: Rank of price drawdown vs history (proxy for cross-sectional rank).
    """
    base = _rank_pct(close / close.rolling(252).max(), 252)
    return _zscore_rolling(base, 21)

def csdr_006_price_rank_xs_rank_21d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_006_price_rank_xs_rank_21d
    ECONOMIC RATIONALE: Rank of price drawdown vs history (proxy for cross-sectional rank).
    """
    base = _rank_pct(close / close.rolling(252).max(), 252)
    return _rank_pct(base, 21)

def csdr_007_price_rank_xs_lvl_63d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_007_price_rank_xs_lvl_63d
    ECONOMIC RATIONALE: Rank of price drawdown vs history (proxy for cross-sectional rank).
    """
    base = _rank_pct(close / close.rolling(252).max(), 252)
    return _rolling_mean(base, 63)

def csdr_008_price_rank_xs_zscore_63d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_008_price_rank_xs_zscore_63d
    ECONOMIC RATIONALE: Rank of price drawdown vs history (proxy for cross-sectional rank).
    """
    base = _rank_pct(close / close.rolling(252).max(), 252)
    return _zscore_rolling(base, 63)

def csdr_009_price_rank_xs_rank_63d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_009_price_rank_xs_rank_63d
    ECONOMIC RATIONALE: Rank of price drawdown vs history (proxy for cross-sectional rank).
    """
    base = _rank_pct(close / close.rolling(252).max(), 252)
    return _rank_pct(base, 63)

def csdr_010_price_rank_xs_lvl_126d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_010_price_rank_xs_lvl_126d
    ECONOMIC RATIONALE: Rank of price drawdown vs history (proxy for cross-sectional rank).
    """
    base = _rank_pct(close / close.rolling(252).max(), 252)
    return _rolling_mean(base, 126)

def csdr_011_price_rank_xs_zscore_126d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_011_price_rank_xs_zscore_126d
    ECONOMIC RATIONALE: Rank of price drawdown vs history (proxy for cross-sectional rank).
    """
    base = _rank_pct(close / close.rolling(252).max(), 252)
    return _zscore_rolling(base, 126)

def csdr_012_price_rank_xs_rank_126d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_012_price_rank_xs_rank_126d
    ECONOMIC RATIONALE: Rank of price drawdown vs history (proxy for cross-sectional rank).
    """
    base = _rank_pct(close / close.rolling(252).max(), 252)
    return _rank_pct(base, 126)

def csdr_013_price_rank_xs_lvl_252d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_013_price_rank_xs_lvl_252d
    ECONOMIC RATIONALE: Rank of price drawdown vs history (proxy for cross-sectional rank).
    """
    base = _rank_pct(close / close.rolling(252).max(), 252)
    return _rolling_mean(base, 252)

def csdr_014_price_rank_xs_zscore_252d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_014_price_rank_xs_zscore_252d
    ECONOMIC RATIONALE: Rank of price drawdown vs history (proxy for cross-sectional rank).
    """
    base = _rank_pct(close / close.rolling(252).max(), 252)
    return _zscore_rolling(base, 252)

def csdr_015_price_rank_xs_rank_252d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_015_price_rank_xs_rank_252d
    ECONOMIC RATIONALE: Rank of price drawdown vs history (proxy for cross-sectional rank).
    """
    base = _rank_pct(close / close.rolling(252).max(), 252)
    return _rank_pct(base, 252)

def csdr_016_volume_rank_xs_lvl_5d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_016_volume_rank_xs_lvl_5d
    ECONOMIC RATIONALE: Rank of volume intensity vs history.
    """
    base = _rank_pct(volume / volume.rolling(252).mean(), 252)
    return _rolling_mean(base, 5)

def csdr_017_volume_rank_xs_zscore_5d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_017_volume_rank_xs_zscore_5d
    ECONOMIC RATIONALE: Rank of volume intensity vs history.
    """
    base = _rank_pct(volume / volume.rolling(252).mean(), 252)
    return _zscore_rolling(base, 5)

def csdr_018_volume_rank_xs_rank_5d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_018_volume_rank_xs_rank_5d
    ECONOMIC RATIONALE: Rank of volume intensity vs history.
    """
    base = _rank_pct(volume / volume.rolling(252).mean(), 252)
    return _rank_pct(base, 5)

def csdr_019_volume_rank_xs_lvl_21d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_019_volume_rank_xs_lvl_21d
    ECONOMIC RATIONALE: Rank of volume intensity vs history.
    """
    base = _rank_pct(volume / volume.rolling(252).mean(), 252)
    return _rolling_mean(base, 21)

def csdr_020_volume_rank_xs_zscore_21d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_020_volume_rank_xs_zscore_21d
    ECONOMIC RATIONALE: Rank of volume intensity vs history.
    """
    base = _rank_pct(volume / volume.rolling(252).mean(), 252)
    return _zscore_rolling(base, 21)

def csdr_021_volume_rank_xs_rank_21d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_021_volume_rank_xs_rank_21d
    ECONOMIC RATIONALE: Rank of volume intensity vs history.
    """
    base = _rank_pct(volume / volume.rolling(252).mean(), 252)
    return _rank_pct(base, 21)

def csdr_022_volume_rank_xs_lvl_63d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_022_volume_rank_xs_lvl_63d
    ECONOMIC RATIONALE: Rank of volume intensity vs history.
    """
    base = _rank_pct(volume / volume.rolling(252).mean(), 252)
    return _rolling_mean(base, 63)

def csdr_023_volume_rank_xs_zscore_63d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_023_volume_rank_xs_zscore_63d
    ECONOMIC RATIONALE: Rank of volume intensity vs history.
    """
    base = _rank_pct(volume / volume.rolling(252).mean(), 252)
    return _zscore_rolling(base, 63)

def csdr_024_volume_rank_xs_rank_63d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_024_volume_rank_xs_rank_63d
    ECONOMIC RATIONALE: Rank of volume intensity vs history.
    """
    base = _rank_pct(volume / volume.rolling(252).mean(), 252)
    return _rank_pct(base, 63)

def csdr_025_volume_rank_xs_lvl_126d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_025_volume_rank_xs_lvl_126d
    ECONOMIC RATIONALE: Rank of volume intensity vs history.
    """
    base = _rank_pct(volume / volume.rolling(252).mean(), 252)
    return _rolling_mean(base, 126)

def csdr_026_volume_rank_xs_zscore_126d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_026_volume_rank_xs_zscore_126d
    ECONOMIC RATIONALE: Rank of volume intensity vs history.
    """
    base = _rank_pct(volume / volume.rolling(252).mean(), 252)
    return _zscore_rolling(base, 126)

def csdr_027_volume_rank_xs_rank_126d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_027_volume_rank_xs_rank_126d
    ECONOMIC RATIONALE: Rank of volume intensity vs history.
    """
    base = _rank_pct(volume / volume.rolling(252).mean(), 252)
    return _rank_pct(base, 126)

def csdr_028_volume_rank_xs_lvl_252d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_028_volume_rank_xs_lvl_252d
    ECONOMIC RATIONALE: Rank of volume intensity vs history.
    """
    base = _rank_pct(volume / volume.rolling(252).mean(), 252)
    return _rolling_mean(base, 252)

def csdr_029_volume_rank_xs_zscore_252d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_029_volume_rank_xs_zscore_252d
    ECONOMIC RATIONALE: Rank of volume intensity vs history.
    """
    base = _rank_pct(volume / volume.rolling(252).mean(), 252)
    return _zscore_rolling(base, 252)

def csdr_030_volume_rank_xs_rank_252d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_030_volume_rank_xs_rank_252d
    ECONOMIC RATIONALE: Rank of volume intensity vs history.
    """
    base = _rank_pct(volume / volume.rolling(252).mean(), 252)
    return _rank_pct(base, 252)

def csdr_031_relative_distress_rank_lvl_5d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_031_relative_distress_rank_lvl_5d
    ECONOMIC RATIONALE: Historical rank of relative underperformance.
    """
    base = _rank_pct(close.pct_change(63) - mkt_close.pct_change(63), 252)
    return _rolling_mean(base, 5)

def csdr_032_relative_distress_rank_zscore_5d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_032_relative_distress_rank_zscore_5d
    ECONOMIC RATIONALE: Historical rank of relative underperformance.
    """
    base = _rank_pct(close.pct_change(63) - mkt_close.pct_change(63), 252)
    return _zscore_rolling(base, 5)

def csdr_033_relative_distress_rank_rank_5d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_033_relative_distress_rank_rank_5d
    ECONOMIC RATIONALE: Historical rank of relative underperformance.
    """
    base = _rank_pct(close.pct_change(63) - mkt_close.pct_change(63), 252)
    return _rank_pct(base, 5)

def csdr_034_relative_distress_rank_lvl_21d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_034_relative_distress_rank_lvl_21d
    ECONOMIC RATIONALE: Historical rank of relative underperformance.
    """
    base = _rank_pct(close.pct_change(63) - mkt_close.pct_change(63), 252)
    return _rolling_mean(base, 21)

def csdr_035_relative_distress_rank_zscore_21d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_035_relative_distress_rank_zscore_21d
    ECONOMIC RATIONALE: Historical rank of relative underperformance.
    """
    base = _rank_pct(close.pct_change(63) - mkt_close.pct_change(63), 252)
    return _zscore_rolling(base, 21)

def csdr_036_relative_distress_rank_rank_21d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_036_relative_distress_rank_rank_21d
    ECONOMIC RATIONALE: Historical rank of relative underperformance.
    """
    base = _rank_pct(close.pct_change(63) - mkt_close.pct_change(63), 252)
    return _rank_pct(base, 21)

def csdr_037_relative_distress_rank_lvl_63d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_037_relative_distress_rank_lvl_63d
    ECONOMIC RATIONALE: Historical rank of relative underperformance.
    """
    base = _rank_pct(close.pct_change(63) - mkt_close.pct_change(63), 252)
    return _rolling_mean(base, 63)

def csdr_038_relative_distress_rank_zscore_63d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_038_relative_distress_rank_zscore_63d
    ECONOMIC RATIONALE: Historical rank of relative underperformance.
    """
    base = _rank_pct(close.pct_change(63) - mkt_close.pct_change(63), 252)
    return _zscore_rolling(base, 63)

def csdr_039_relative_distress_rank_rank_63d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_039_relative_distress_rank_rank_63d
    ECONOMIC RATIONALE: Historical rank of relative underperformance.
    """
    base = _rank_pct(close.pct_change(63) - mkt_close.pct_change(63), 252)
    return _rank_pct(base, 63)

def csdr_040_relative_distress_rank_lvl_126d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_040_relative_distress_rank_lvl_126d
    ECONOMIC RATIONALE: Historical rank of relative underperformance.
    """
    base = _rank_pct(close.pct_change(63) - mkt_close.pct_change(63), 252)
    return _rolling_mean(base, 126)

def csdr_041_relative_distress_rank_zscore_126d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_041_relative_distress_rank_zscore_126d
    ECONOMIC RATIONALE: Historical rank of relative underperformance.
    """
    base = _rank_pct(close.pct_change(63) - mkt_close.pct_change(63), 252)
    return _zscore_rolling(base, 126)

def csdr_042_relative_distress_rank_rank_126d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_042_relative_distress_rank_rank_126d
    ECONOMIC RATIONALE: Historical rank of relative underperformance.
    """
    base = _rank_pct(close.pct_change(63) - mkt_close.pct_change(63), 252)
    return _rank_pct(base, 126)

def csdr_043_relative_distress_rank_lvl_252d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_043_relative_distress_rank_lvl_252d
    ECONOMIC RATIONALE: Historical rank of relative underperformance.
    """
    base = _rank_pct(close.pct_change(63) - mkt_close.pct_change(63), 252)
    return _rolling_mean(base, 252)

def csdr_044_relative_distress_rank_zscore_252d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_044_relative_distress_rank_zscore_252d
    ECONOMIC RATIONALE: Historical rank of relative underperformance.
    """
    base = _rank_pct(close.pct_change(63) - mkt_close.pct_change(63), 252)
    return _zscore_rolling(base, 252)

def csdr_045_relative_distress_rank_rank_252d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_045_relative_distress_rank_rank_252d
    ECONOMIC RATIONALE: Historical rank of relative underperformance.
    """
    base = _rank_pct(close.pct_change(63) - mkt_close.pct_change(63), 252)
    return _rank_pct(base, 252)

def csdr_046_xs_volatility_rank_lvl_5d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_046_xs_volatility_rank_lvl_5d
    ECONOMIC RATIONALE: Historical rank of realized volatility.
    """
    base = _rank_pct(close.rolling(21).std(), 252)
    return _rolling_mean(base, 5)

def csdr_047_xs_volatility_rank_zscore_5d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_047_xs_volatility_rank_zscore_5d
    ECONOMIC RATIONALE: Historical rank of realized volatility.
    """
    base = _rank_pct(close.rolling(21).std(), 252)
    return _zscore_rolling(base, 5)

def csdr_048_xs_volatility_rank_rank_5d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_048_xs_volatility_rank_rank_5d
    ECONOMIC RATIONALE: Historical rank of realized volatility.
    """
    base = _rank_pct(close.rolling(21).std(), 252)
    return _rank_pct(base, 5)

def csdr_049_xs_volatility_rank_lvl_21d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_049_xs_volatility_rank_lvl_21d
    ECONOMIC RATIONALE: Historical rank of realized volatility.
    """
    base = _rank_pct(close.rolling(21).std(), 252)
    return _rolling_mean(base, 21)

def csdr_050_xs_volatility_rank_zscore_21d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_050_xs_volatility_rank_zscore_21d
    ECONOMIC RATIONALE: Historical rank of realized volatility.
    """
    base = _rank_pct(close.rolling(21).std(), 252)
    return _zscore_rolling(base, 21)

def csdr_051_xs_volatility_rank_rank_21d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_051_xs_volatility_rank_rank_21d
    ECONOMIC RATIONALE: Historical rank of realized volatility.
    """
    base = _rank_pct(close.rolling(21).std(), 252)
    return _rank_pct(base, 21)

def csdr_052_xs_volatility_rank_lvl_63d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_052_xs_volatility_rank_lvl_63d
    ECONOMIC RATIONALE: Historical rank of realized volatility.
    """
    base = _rank_pct(close.rolling(21).std(), 252)
    return _rolling_mean(base, 63)

def csdr_053_xs_volatility_rank_zscore_63d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_053_xs_volatility_rank_zscore_63d
    ECONOMIC RATIONALE: Historical rank of realized volatility.
    """
    base = _rank_pct(close.rolling(21).std(), 252)
    return _zscore_rolling(base, 63)

def csdr_054_xs_volatility_rank_rank_63d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_054_xs_volatility_rank_rank_63d
    ECONOMIC RATIONALE: Historical rank of realized volatility.
    """
    base = _rank_pct(close.rolling(21).std(), 252)
    return _rank_pct(base, 63)

def csdr_055_xs_volatility_rank_lvl_126d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_055_xs_volatility_rank_lvl_126d
    ECONOMIC RATIONALE: Historical rank of realized volatility.
    """
    base = _rank_pct(close.rolling(21).std(), 252)
    return _rolling_mean(base, 126)

def csdr_056_xs_volatility_rank_zscore_126d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_056_xs_volatility_rank_zscore_126d
    ECONOMIC RATIONALE: Historical rank of realized volatility.
    """
    base = _rank_pct(close.rolling(21).std(), 252)
    return _zscore_rolling(base, 126)

def csdr_057_xs_volatility_rank_rank_126d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_057_xs_volatility_rank_rank_126d
    ECONOMIC RATIONALE: Historical rank of realized volatility.
    """
    base = _rank_pct(close.rolling(21).std(), 252)
    return _rank_pct(base, 126)

def csdr_058_xs_volatility_rank_lvl_252d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_058_xs_volatility_rank_lvl_252d
    ECONOMIC RATIONALE: Historical rank of realized volatility.
    """
    base = _rank_pct(close.rolling(21).std(), 252)
    return _rolling_mean(base, 252)

def csdr_059_xs_volatility_rank_zscore_252d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_059_xs_volatility_rank_zscore_252d
    ECONOMIC RATIONALE: Historical rank of realized volatility.
    """
    base = _rank_pct(close.rolling(21).std(), 252)
    return _zscore_rolling(base, 252)

def csdr_060_xs_volatility_rank_rank_252d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_060_xs_volatility_rank_rank_252d
    ECONOMIC RATIONALE: Historical rank of realized volatility.
    """
    base = _rank_pct(close.rolling(21).std(), 252)
    return _rank_pct(base, 252)

def csdr_061_xs_drawdown_rank_lvl_5d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_061_xs_drawdown_rank_lvl_5d
    ECONOMIC RATIONALE: Historical rank of drawdown severity.
    """
    base = _rank_pct(close / close.rolling(252).max() - 1, 252)
    return _rolling_mean(base, 5)

def csdr_062_xs_drawdown_rank_zscore_5d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_062_xs_drawdown_rank_zscore_5d
    ECONOMIC RATIONALE: Historical rank of drawdown severity.
    """
    base = _rank_pct(close / close.rolling(252).max() - 1, 252)
    return _zscore_rolling(base, 5)

def csdr_063_xs_drawdown_rank_rank_5d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_063_xs_drawdown_rank_rank_5d
    ECONOMIC RATIONALE: Historical rank of drawdown severity.
    """
    base = _rank_pct(close / close.rolling(252).max() - 1, 252)
    return _rank_pct(base, 5)

def csdr_064_xs_drawdown_rank_lvl_21d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_064_xs_drawdown_rank_lvl_21d
    ECONOMIC RATIONALE: Historical rank of drawdown severity.
    """
    base = _rank_pct(close / close.rolling(252).max() - 1, 252)
    return _rolling_mean(base, 21)

def csdr_065_xs_drawdown_rank_zscore_21d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_065_xs_drawdown_rank_zscore_21d
    ECONOMIC RATIONALE: Historical rank of drawdown severity.
    """
    base = _rank_pct(close / close.rolling(252).max() - 1, 252)
    return _zscore_rolling(base, 21)

def csdr_066_xs_drawdown_rank_rank_21d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_066_xs_drawdown_rank_rank_21d
    ECONOMIC RATIONALE: Historical rank of drawdown severity.
    """
    base = _rank_pct(close / close.rolling(252).max() - 1, 252)
    return _rank_pct(base, 21)

def csdr_067_xs_drawdown_rank_lvl_63d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_067_xs_drawdown_rank_lvl_63d
    ECONOMIC RATIONALE: Historical rank of drawdown severity.
    """
    base = _rank_pct(close / close.rolling(252).max() - 1, 252)
    return _rolling_mean(base, 63)

def csdr_068_xs_drawdown_rank_zscore_63d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_068_xs_drawdown_rank_zscore_63d
    ECONOMIC RATIONALE: Historical rank of drawdown severity.
    """
    base = _rank_pct(close / close.rolling(252).max() - 1, 252)
    return _zscore_rolling(base, 63)

def csdr_069_xs_drawdown_rank_rank_63d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_069_xs_drawdown_rank_rank_63d
    ECONOMIC RATIONALE: Historical rank of drawdown severity.
    """
    base = _rank_pct(close / close.rolling(252).max() - 1, 252)
    return _rank_pct(base, 63)

def csdr_070_xs_drawdown_rank_lvl_126d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_070_xs_drawdown_rank_lvl_126d
    ECONOMIC RATIONALE: Historical rank of drawdown severity.
    """
    base = _rank_pct(close / close.rolling(252).max() - 1, 252)
    return _rolling_mean(base, 126)

def csdr_071_xs_drawdown_rank_zscore_126d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_071_xs_drawdown_rank_zscore_126d
    ECONOMIC RATIONALE: Historical rank of drawdown severity.
    """
    base = _rank_pct(close / close.rolling(252).max() - 1, 252)
    return _zscore_rolling(base, 126)

def csdr_072_xs_drawdown_rank_rank_126d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_072_xs_drawdown_rank_rank_126d
    ECONOMIC RATIONALE: Historical rank of drawdown severity.
    """
    base = _rank_pct(close / close.rolling(252).max() - 1, 252)
    return _rank_pct(base, 126)

def csdr_073_xs_drawdown_rank_lvl_252d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_073_xs_drawdown_rank_lvl_252d
    ECONOMIC RATIONALE: Historical rank of drawdown severity.
    """
    base = _rank_pct(close / close.rolling(252).max() - 1, 252)
    return _rolling_mean(base, 252)

def csdr_074_xs_drawdown_rank_zscore_252d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_074_xs_drawdown_rank_zscore_252d
    ECONOMIC RATIONALE: Historical rank of drawdown severity.
    """
    base = _rank_pct(close / close.rolling(252).max() - 1, 252)
    return _zscore_rolling(base, 252)

def csdr_075_xs_drawdown_rank_rank_252d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_075_xs_drawdown_rank_rank_252d
    ECONOMIC RATIONALE: Historical rank of drawdown severity.
    """
    base = _rank_pct(close / close.rolling(252).max() - 1, 252)
    return _rank_pct(base, 252)

def csdr_076_relative_volume_rank_lvl_5d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_076_relative_volume_rank_lvl_5d
    ECONOMIC RATIONALE: Rank of volume relative to market volume.
    """
    base = _rank_pct(volume / mkt_volume.replace(0, 1e-9), 252)
    return _rolling_mean(base, 5)

def csdr_077_relative_volume_rank_zscore_5d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_077_relative_volume_rank_zscore_5d
    ECONOMIC RATIONALE: Rank of volume relative to market volume.
    """
    base = _rank_pct(volume / mkt_volume.replace(0, 1e-9), 252)
    return _zscore_rolling(base, 5)

def csdr_078_relative_volume_rank_rank_5d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_078_relative_volume_rank_rank_5d
    ECONOMIC RATIONALE: Rank of volume relative to market volume.
    """
    base = _rank_pct(volume / mkt_volume.replace(0, 1e-9), 252)
    return _rank_pct(base, 5)

def csdr_079_relative_volume_rank_lvl_21d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_079_relative_volume_rank_lvl_21d
    ECONOMIC RATIONALE: Rank of volume relative to market volume.
    """
    base = _rank_pct(volume / mkt_volume.replace(0, 1e-9), 252)
    return _rolling_mean(base, 21)

def csdr_080_relative_volume_rank_zscore_21d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_080_relative_volume_rank_zscore_21d
    ECONOMIC RATIONALE: Rank of volume relative to market volume.
    """
    base = _rank_pct(volume / mkt_volume.replace(0, 1e-9), 252)
    return _zscore_rolling(base, 21)

def csdr_081_relative_volume_rank_rank_21d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_081_relative_volume_rank_rank_21d
    ECONOMIC RATIONALE: Rank of volume relative to market volume.
    """
    base = _rank_pct(volume / mkt_volume.replace(0, 1e-9), 252)
    return _rank_pct(base, 21)

def csdr_082_relative_volume_rank_lvl_63d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_082_relative_volume_rank_lvl_63d
    ECONOMIC RATIONALE: Rank of volume relative to market volume.
    """
    base = _rank_pct(volume / mkt_volume.replace(0, 1e-9), 252)
    return _rolling_mean(base, 63)

def csdr_083_relative_volume_rank_zscore_63d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_083_relative_volume_rank_zscore_63d
    ECONOMIC RATIONALE: Rank of volume relative to market volume.
    """
    base = _rank_pct(volume / mkt_volume.replace(0, 1e-9), 252)
    return _zscore_rolling(base, 63)

def csdr_084_relative_volume_rank_rank_63d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_084_relative_volume_rank_rank_63d
    ECONOMIC RATIONALE: Rank of volume relative to market volume.
    """
    base = _rank_pct(volume / mkt_volume.replace(0, 1e-9), 252)
    return _rank_pct(base, 63)

def csdr_085_relative_volume_rank_lvl_126d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_085_relative_volume_rank_lvl_126d
    ECONOMIC RATIONALE: Rank of volume relative to market volume.
    """
    base = _rank_pct(volume / mkt_volume.replace(0, 1e-9), 252)
    return _rolling_mean(base, 126)

def csdr_086_relative_volume_rank_zscore_126d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_086_relative_volume_rank_zscore_126d
    ECONOMIC RATIONALE: Rank of volume relative to market volume.
    """
    base = _rank_pct(volume / mkt_volume.replace(0, 1e-9), 252)
    return _zscore_rolling(base, 126)

def csdr_087_relative_volume_rank_rank_126d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_087_relative_volume_rank_rank_126d
    ECONOMIC RATIONALE: Rank of volume relative to market volume.
    """
    base = _rank_pct(volume / mkt_volume.replace(0, 1e-9), 252)
    return _rank_pct(base, 126)

def csdr_088_relative_volume_rank_lvl_252d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_088_relative_volume_rank_lvl_252d
    ECONOMIC RATIONALE: Rank of volume relative to market volume.
    """
    base = _rank_pct(volume / mkt_volume.replace(0, 1e-9), 252)
    return _rolling_mean(base, 252)

def csdr_089_relative_volume_rank_zscore_252d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_089_relative_volume_rank_zscore_252d
    ECONOMIC RATIONALE: Rank of volume relative to market volume.
    """
    base = _rank_pct(volume / mkt_volume.replace(0, 1e-9), 252)
    return _zscore_rolling(base, 252)

def csdr_090_relative_volume_rank_rank_252d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_090_relative_volume_rank_rank_252d
    ECONOMIC RATIONALE: Rank of volume relative to market volume.
    """
    base = _rank_pct(volume / mkt_volume.replace(0, 1e-9), 252)
    return _rank_pct(base, 252)

def csdr_091_xs_momentum_rank_lvl_5d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_091_xs_momentum_rank_lvl_5d
    ECONOMIC RATIONALE: Rank of long-term annual momentum.
    """
    base = _rank_pct(close.pct_change(252), 252)
    return _rolling_mean(base, 5)

def csdr_092_xs_momentum_rank_zscore_5d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_092_xs_momentum_rank_zscore_5d
    ECONOMIC RATIONALE: Rank of long-term annual momentum.
    """
    base = _rank_pct(close.pct_change(252), 252)
    return _zscore_rolling(base, 5)

def csdr_093_xs_momentum_rank_rank_5d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_093_xs_momentum_rank_rank_5d
    ECONOMIC RATIONALE: Rank of long-term annual momentum.
    """
    base = _rank_pct(close.pct_change(252), 252)
    return _rank_pct(base, 5)

def csdr_094_xs_momentum_rank_lvl_21d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_094_xs_momentum_rank_lvl_21d
    ECONOMIC RATIONALE: Rank of long-term annual momentum.
    """
    base = _rank_pct(close.pct_change(252), 252)
    return _rolling_mean(base, 21)

def csdr_095_xs_momentum_rank_zscore_21d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_095_xs_momentum_rank_zscore_21d
    ECONOMIC RATIONALE: Rank of long-term annual momentum.
    """
    base = _rank_pct(close.pct_change(252), 252)
    return _zscore_rolling(base, 21)

def csdr_096_xs_momentum_rank_rank_21d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_096_xs_momentum_rank_rank_21d
    ECONOMIC RATIONALE: Rank of long-term annual momentum.
    """
    base = _rank_pct(close.pct_change(252), 252)
    return _rank_pct(base, 21)

def csdr_097_xs_momentum_rank_lvl_63d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_097_xs_momentum_rank_lvl_63d
    ECONOMIC RATIONALE: Rank of long-term annual momentum.
    """
    base = _rank_pct(close.pct_change(252), 252)
    return _rolling_mean(base, 63)

def csdr_098_xs_momentum_rank_zscore_63d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_098_xs_momentum_rank_zscore_63d
    ECONOMIC RATIONALE: Rank of long-term annual momentum.
    """
    base = _rank_pct(close.pct_change(252), 252)
    return _zscore_rolling(base, 63)

def csdr_099_xs_momentum_rank_rank_63d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_099_xs_momentum_rank_rank_63d
    ECONOMIC RATIONALE: Rank of long-term annual momentum.
    """
    base = _rank_pct(close.pct_change(252), 252)
    return _rank_pct(base, 63)

def csdr_100_xs_momentum_rank_lvl_126d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_100_xs_momentum_rank_lvl_126d
    ECONOMIC RATIONALE: Rank of long-term annual momentum.
    """
    base = _rank_pct(close.pct_change(252), 252)
    return _rolling_mean(base, 126)

def csdr_101_xs_momentum_rank_zscore_126d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_101_xs_momentum_rank_zscore_126d
    ECONOMIC RATIONALE: Rank of long-term annual momentum.
    """
    base = _rank_pct(close.pct_change(252), 252)
    return _zscore_rolling(base, 126)

def csdr_102_xs_momentum_rank_rank_126d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_102_xs_momentum_rank_rank_126d
    ECONOMIC RATIONALE: Rank of long-term annual momentum.
    """
    base = _rank_pct(close.pct_change(252), 252)
    return _rank_pct(base, 126)

def csdr_103_xs_momentum_rank_lvl_252d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_103_xs_momentum_rank_lvl_252d
    ECONOMIC RATIONALE: Rank of long-term annual momentum.
    """
    base = _rank_pct(close.pct_change(252), 252)
    return _rolling_mean(base, 252)

def csdr_104_xs_momentum_rank_zscore_252d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_104_xs_momentum_rank_zscore_252d
    ECONOMIC RATIONALE: Rank of long-term annual momentum.
    """
    base = _rank_pct(close.pct_change(252), 252)
    return _zscore_rolling(base, 252)

def csdr_105_xs_momentum_rank_rank_252d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_105_xs_momentum_rank_rank_252d
    ECONOMIC RATIONALE: Rank of long-term annual momentum.
    """
    base = _rank_pct(close.pct_change(252), 252)
    return _rank_pct(base, 252)

def csdr_106_distress_rank_z_lvl_5d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_106_distress_rank_z_lvl_5d
    ECONOMIC RATIONALE: Z-score of the current momentum rank.
    """
    base = _zscore_rolling(_rank_pct(close.pct_change(21), 252), 252)
    return _rolling_mean(base, 5)

def csdr_107_distress_rank_z_zscore_5d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_107_distress_rank_z_zscore_5d
    ECONOMIC RATIONALE: Z-score of the current momentum rank.
    """
    base = _zscore_rolling(_rank_pct(close.pct_change(21), 252), 252)
    return _zscore_rolling(base, 5)

def csdr_108_distress_rank_z_rank_5d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_108_distress_rank_z_rank_5d
    ECONOMIC RATIONALE: Z-score of the current momentum rank.
    """
    base = _zscore_rolling(_rank_pct(close.pct_change(21), 252), 252)
    return _rank_pct(base, 5)

def csdr_109_distress_rank_z_lvl_21d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_109_distress_rank_z_lvl_21d
    ECONOMIC RATIONALE: Z-score of the current momentum rank.
    """
    base = _zscore_rolling(_rank_pct(close.pct_change(21), 252), 252)
    return _rolling_mean(base, 21)

def csdr_110_distress_rank_z_zscore_21d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_110_distress_rank_z_zscore_21d
    ECONOMIC RATIONALE: Z-score of the current momentum rank.
    """
    base = _zscore_rolling(_rank_pct(close.pct_change(21), 252), 252)
    return _zscore_rolling(base, 21)

def csdr_111_distress_rank_z_rank_21d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_111_distress_rank_z_rank_21d
    ECONOMIC RATIONALE: Z-score of the current momentum rank.
    """
    base = _zscore_rolling(_rank_pct(close.pct_change(21), 252), 252)
    return _rank_pct(base, 21)

def csdr_112_distress_rank_z_lvl_63d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_112_distress_rank_z_lvl_63d
    ECONOMIC RATIONALE: Z-score of the current momentum rank.
    """
    base = _zscore_rolling(_rank_pct(close.pct_change(21), 252), 252)
    return _rolling_mean(base, 63)

def csdr_113_distress_rank_z_zscore_63d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_113_distress_rank_z_zscore_63d
    ECONOMIC RATIONALE: Z-score of the current momentum rank.
    """
    base = _zscore_rolling(_rank_pct(close.pct_change(21), 252), 252)
    return _zscore_rolling(base, 63)

def csdr_114_distress_rank_z_rank_63d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_114_distress_rank_z_rank_63d
    ECONOMIC RATIONALE: Z-score of the current momentum rank.
    """
    base = _zscore_rolling(_rank_pct(close.pct_change(21), 252), 252)
    return _rank_pct(base, 63)

def csdr_115_distress_rank_z_lvl_126d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_115_distress_rank_z_lvl_126d
    ECONOMIC RATIONALE: Z-score of the current momentum rank.
    """
    base = _zscore_rolling(_rank_pct(close.pct_change(21), 252), 252)
    return _rolling_mean(base, 126)

def csdr_116_distress_rank_z_zscore_126d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_116_distress_rank_z_zscore_126d
    ECONOMIC RATIONALE: Z-score of the current momentum rank.
    """
    base = _zscore_rolling(_rank_pct(close.pct_change(21), 252), 252)
    return _zscore_rolling(base, 126)

def csdr_117_distress_rank_z_rank_126d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_117_distress_rank_z_rank_126d
    ECONOMIC RATIONALE: Z-score of the current momentum rank.
    """
    base = _zscore_rolling(_rank_pct(close.pct_change(21), 252), 252)
    return _rank_pct(base, 126)

def csdr_118_distress_rank_z_lvl_252d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_118_distress_rank_z_lvl_252d
    ECONOMIC RATIONALE: Z-score of the current momentum rank.
    """
    base = _zscore_rolling(_rank_pct(close.pct_change(21), 252), 252)
    return _rolling_mean(base, 252)

def csdr_119_distress_rank_z_zscore_252d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_119_distress_rank_z_zscore_252d
    ECONOMIC RATIONALE: Z-score of the current momentum rank.
    """
    base = _zscore_rolling(_rank_pct(close.pct_change(21), 252), 252)
    return _zscore_rolling(base, 252)

def csdr_120_distress_rank_z_rank_252d(close: pd.Series, mkt_close: pd.Series, mkt_volume: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    csdr_120_distress_rank_z_rank_252d
    ECONOMIC RATIONALE: Z-score of the current momentum rank.
    """
    base = _zscore_rolling(_rank_pct(close.pct_change(21), 252), 252)
    return _rank_pct(base, 252)

# ── Registry ──────────────────────────────────────────────────────────────────
V124_REGISTRY_1 = {
    "csdr_001_price_rank_xs_lvl_5d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_001_price_rank_xs_lvl_5d},
    "csdr_002_price_rank_xs_zscore_5d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_002_price_rank_xs_zscore_5d},
    "csdr_003_price_rank_xs_rank_5d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_003_price_rank_xs_rank_5d},
    "csdr_004_price_rank_xs_lvl_21d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_004_price_rank_xs_lvl_21d},
    "csdr_005_price_rank_xs_zscore_21d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_005_price_rank_xs_zscore_21d},
    "csdr_006_price_rank_xs_rank_21d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_006_price_rank_xs_rank_21d},
    "csdr_007_price_rank_xs_lvl_63d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_007_price_rank_xs_lvl_63d},
    "csdr_008_price_rank_xs_zscore_63d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_008_price_rank_xs_zscore_63d},
    "csdr_009_price_rank_xs_rank_63d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_009_price_rank_xs_rank_63d},
    "csdr_010_price_rank_xs_lvl_126d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_010_price_rank_xs_lvl_126d},
    "csdr_011_price_rank_xs_zscore_126d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_011_price_rank_xs_zscore_126d},
    "csdr_012_price_rank_xs_rank_126d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_012_price_rank_xs_rank_126d},
    "csdr_013_price_rank_xs_lvl_252d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_013_price_rank_xs_lvl_252d},
    "csdr_014_price_rank_xs_zscore_252d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_014_price_rank_xs_zscore_252d},
    "csdr_015_price_rank_xs_rank_252d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_015_price_rank_xs_rank_252d},
    "csdr_016_volume_rank_xs_lvl_5d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_016_volume_rank_xs_lvl_5d},
    "csdr_017_volume_rank_xs_zscore_5d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_017_volume_rank_xs_zscore_5d},
    "csdr_018_volume_rank_xs_rank_5d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_018_volume_rank_xs_rank_5d},
    "csdr_019_volume_rank_xs_lvl_21d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_019_volume_rank_xs_lvl_21d},
    "csdr_020_volume_rank_xs_zscore_21d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_020_volume_rank_xs_zscore_21d},
    "csdr_021_volume_rank_xs_rank_21d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_021_volume_rank_xs_rank_21d},
    "csdr_022_volume_rank_xs_lvl_63d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_022_volume_rank_xs_lvl_63d},
    "csdr_023_volume_rank_xs_zscore_63d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_023_volume_rank_xs_zscore_63d},
    "csdr_024_volume_rank_xs_rank_63d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_024_volume_rank_xs_rank_63d},
    "csdr_025_volume_rank_xs_lvl_126d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_025_volume_rank_xs_lvl_126d},
    "csdr_026_volume_rank_xs_zscore_126d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_026_volume_rank_xs_zscore_126d},
    "csdr_027_volume_rank_xs_rank_126d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_027_volume_rank_xs_rank_126d},
    "csdr_028_volume_rank_xs_lvl_252d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_028_volume_rank_xs_lvl_252d},
    "csdr_029_volume_rank_xs_zscore_252d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_029_volume_rank_xs_zscore_252d},
    "csdr_030_volume_rank_xs_rank_252d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_030_volume_rank_xs_rank_252d},
    "csdr_031_relative_distress_rank_lvl_5d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_031_relative_distress_rank_lvl_5d},
    "csdr_032_relative_distress_rank_zscore_5d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_032_relative_distress_rank_zscore_5d},
    "csdr_033_relative_distress_rank_rank_5d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_033_relative_distress_rank_rank_5d},
    "csdr_034_relative_distress_rank_lvl_21d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_034_relative_distress_rank_lvl_21d},
    "csdr_035_relative_distress_rank_zscore_21d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_035_relative_distress_rank_zscore_21d},
    "csdr_036_relative_distress_rank_rank_21d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_036_relative_distress_rank_rank_21d},
    "csdr_037_relative_distress_rank_lvl_63d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_037_relative_distress_rank_lvl_63d},
    "csdr_038_relative_distress_rank_zscore_63d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_038_relative_distress_rank_zscore_63d},
    "csdr_039_relative_distress_rank_rank_63d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_039_relative_distress_rank_rank_63d},
    "csdr_040_relative_distress_rank_lvl_126d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_040_relative_distress_rank_lvl_126d},
    "csdr_041_relative_distress_rank_zscore_126d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_041_relative_distress_rank_zscore_126d},
    "csdr_042_relative_distress_rank_rank_126d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_042_relative_distress_rank_rank_126d},
    "csdr_043_relative_distress_rank_lvl_252d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_043_relative_distress_rank_lvl_252d},
    "csdr_044_relative_distress_rank_zscore_252d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_044_relative_distress_rank_zscore_252d},
    "csdr_045_relative_distress_rank_rank_252d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_045_relative_distress_rank_rank_252d},
    "csdr_046_xs_volatility_rank_lvl_5d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_046_xs_volatility_rank_lvl_5d},
    "csdr_047_xs_volatility_rank_zscore_5d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_047_xs_volatility_rank_zscore_5d},
    "csdr_048_xs_volatility_rank_rank_5d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_048_xs_volatility_rank_rank_5d},
    "csdr_049_xs_volatility_rank_lvl_21d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_049_xs_volatility_rank_lvl_21d},
    "csdr_050_xs_volatility_rank_zscore_21d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_050_xs_volatility_rank_zscore_21d},
    "csdr_051_xs_volatility_rank_rank_21d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_051_xs_volatility_rank_rank_21d},
    "csdr_052_xs_volatility_rank_lvl_63d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_052_xs_volatility_rank_lvl_63d},
    "csdr_053_xs_volatility_rank_zscore_63d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_053_xs_volatility_rank_zscore_63d},
    "csdr_054_xs_volatility_rank_rank_63d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_054_xs_volatility_rank_rank_63d},
    "csdr_055_xs_volatility_rank_lvl_126d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_055_xs_volatility_rank_lvl_126d},
    "csdr_056_xs_volatility_rank_zscore_126d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_056_xs_volatility_rank_zscore_126d},
    "csdr_057_xs_volatility_rank_rank_126d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_057_xs_volatility_rank_rank_126d},
    "csdr_058_xs_volatility_rank_lvl_252d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_058_xs_volatility_rank_lvl_252d},
    "csdr_059_xs_volatility_rank_zscore_252d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_059_xs_volatility_rank_zscore_252d},
    "csdr_060_xs_volatility_rank_rank_252d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_060_xs_volatility_rank_rank_252d},
    "csdr_061_xs_drawdown_rank_lvl_5d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_061_xs_drawdown_rank_lvl_5d},
    "csdr_062_xs_drawdown_rank_zscore_5d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_062_xs_drawdown_rank_zscore_5d},
    "csdr_063_xs_drawdown_rank_rank_5d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_063_xs_drawdown_rank_rank_5d},
    "csdr_064_xs_drawdown_rank_lvl_21d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_064_xs_drawdown_rank_lvl_21d},
    "csdr_065_xs_drawdown_rank_zscore_21d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_065_xs_drawdown_rank_zscore_21d},
    "csdr_066_xs_drawdown_rank_rank_21d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_066_xs_drawdown_rank_rank_21d},
    "csdr_067_xs_drawdown_rank_lvl_63d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_067_xs_drawdown_rank_lvl_63d},
    "csdr_068_xs_drawdown_rank_zscore_63d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_068_xs_drawdown_rank_zscore_63d},
    "csdr_069_xs_drawdown_rank_rank_63d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_069_xs_drawdown_rank_rank_63d},
    "csdr_070_xs_drawdown_rank_lvl_126d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_070_xs_drawdown_rank_lvl_126d},
    "csdr_071_xs_drawdown_rank_zscore_126d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_071_xs_drawdown_rank_zscore_126d},
    "csdr_072_xs_drawdown_rank_rank_126d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_072_xs_drawdown_rank_rank_126d},
    "csdr_073_xs_drawdown_rank_lvl_252d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_073_xs_drawdown_rank_lvl_252d},
    "csdr_074_xs_drawdown_rank_zscore_252d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_074_xs_drawdown_rank_zscore_252d},
    "csdr_075_xs_drawdown_rank_rank_252d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_075_xs_drawdown_rank_rank_252d},
    "csdr_076_relative_volume_rank_lvl_5d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_076_relative_volume_rank_lvl_5d},
    "csdr_077_relative_volume_rank_zscore_5d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_077_relative_volume_rank_zscore_5d},
    "csdr_078_relative_volume_rank_rank_5d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_078_relative_volume_rank_rank_5d},
    "csdr_079_relative_volume_rank_lvl_21d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_079_relative_volume_rank_lvl_21d},
    "csdr_080_relative_volume_rank_zscore_21d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_080_relative_volume_rank_zscore_21d},
    "csdr_081_relative_volume_rank_rank_21d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_081_relative_volume_rank_rank_21d},
    "csdr_082_relative_volume_rank_lvl_63d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_082_relative_volume_rank_lvl_63d},
    "csdr_083_relative_volume_rank_zscore_63d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_083_relative_volume_rank_zscore_63d},
    "csdr_084_relative_volume_rank_rank_63d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_084_relative_volume_rank_rank_63d},
    "csdr_085_relative_volume_rank_lvl_126d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_085_relative_volume_rank_lvl_126d},
    "csdr_086_relative_volume_rank_zscore_126d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_086_relative_volume_rank_zscore_126d},
    "csdr_087_relative_volume_rank_rank_126d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_087_relative_volume_rank_rank_126d},
    "csdr_088_relative_volume_rank_lvl_252d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_088_relative_volume_rank_lvl_252d},
    "csdr_089_relative_volume_rank_zscore_252d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_089_relative_volume_rank_zscore_252d},
    "csdr_090_relative_volume_rank_rank_252d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_090_relative_volume_rank_rank_252d},
    "csdr_091_xs_momentum_rank_lvl_5d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_091_xs_momentum_rank_lvl_5d},
    "csdr_092_xs_momentum_rank_zscore_5d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_092_xs_momentum_rank_zscore_5d},
    "csdr_093_xs_momentum_rank_rank_5d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_093_xs_momentum_rank_rank_5d},
    "csdr_094_xs_momentum_rank_lvl_21d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_094_xs_momentum_rank_lvl_21d},
    "csdr_095_xs_momentum_rank_zscore_21d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_095_xs_momentum_rank_zscore_21d},
    "csdr_096_xs_momentum_rank_rank_21d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_096_xs_momentum_rank_rank_21d},
    "csdr_097_xs_momentum_rank_lvl_63d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_097_xs_momentum_rank_lvl_63d},
    "csdr_098_xs_momentum_rank_zscore_63d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_098_xs_momentum_rank_zscore_63d},
    "csdr_099_xs_momentum_rank_rank_63d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_099_xs_momentum_rank_rank_63d},
    "csdr_100_xs_momentum_rank_lvl_126d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_100_xs_momentum_rank_lvl_126d},
    "csdr_101_xs_momentum_rank_zscore_126d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_101_xs_momentum_rank_zscore_126d},
    "csdr_102_xs_momentum_rank_rank_126d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_102_xs_momentum_rank_rank_126d},
    "csdr_103_xs_momentum_rank_lvl_252d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_103_xs_momentum_rank_lvl_252d},
    "csdr_104_xs_momentum_rank_zscore_252d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_104_xs_momentum_rank_zscore_252d},
    "csdr_105_xs_momentum_rank_rank_252d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_105_xs_momentum_rank_rank_252d},
    "csdr_106_distress_rank_z_lvl_5d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_106_distress_rank_z_lvl_5d},
    "csdr_107_distress_rank_z_zscore_5d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_107_distress_rank_z_zscore_5d},
    "csdr_108_distress_rank_z_rank_5d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_108_distress_rank_z_rank_5d},
    "csdr_109_distress_rank_z_lvl_21d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_109_distress_rank_z_lvl_21d},
    "csdr_110_distress_rank_z_zscore_21d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_110_distress_rank_z_zscore_21d},
    "csdr_111_distress_rank_z_rank_21d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_111_distress_rank_z_rank_21d},
    "csdr_112_distress_rank_z_lvl_63d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_112_distress_rank_z_lvl_63d},
    "csdr_113_distress_rank_z_zscore_63d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_113_distress_rank_z_zscore_63d},
    "csdr_114_distress_rank_z_rank_63d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_114_distress_rank_z_rank_63d},
    "csdr_115_distress_rank_z_lvl_126d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_115_distress_rank_z_lvl_126d},
    "csdr_116_distress_rank_z_zscore_126d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_116_distress_rank_z_zscore_126d},
    "csdr_117_distress_rank_z_rank_126d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_117_distress_rank_z_rank_126d},
    "csdr_118_distress_rank_z_lvl_252d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_118_distress_rank_z_lvl_252d},
    "csdr_119_distress_rank_z_zscore_252d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_119_distress_rank_z_zscore_252d},
    "csdr_120_distress_rank_z_rank_252d": {"inputs": ["close", "mkt_close", "mkt_volume", "open", "volume"], "func": csdr_120_distress_rank_z_rank_252d},
}
