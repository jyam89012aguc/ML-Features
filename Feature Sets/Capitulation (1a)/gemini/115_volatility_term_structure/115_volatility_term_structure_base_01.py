"""
115_volatility_term_structure — Base Features Part 1
Domain: volatility_term_structure
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

def vts_001_vol_5d_lvl_5d(close: pd.Series) -> pd.Series:
    """
    vts_001_vol_5d_lvl_5d
    ECONOMIC RATIONALE: Short-term realized volatility.
    """
    base = close.pct_change(1).rolling(5).std()
    return _rolling_mean(base, 5)

def vts_002_vol_5d_zscore_5d(close: pd.Series) -> pd.Series:
    """
    vts_002_vol_5d_zscore_5d
    ECONOMIC RATIONALE: Short-term realized volatility.
    """
    base = close.pct_change(1).rolling(5).std()
    return _zscore_rolling(base, 5)

def vts_003_vol_5d_rank_5d(close: pd.Series) -> pd.Series:
    """
    vts_003_vol_5d_rank_5d
    ECONOMIC RATIONALE: Short-term realized volatility.
    """
    base = close.pct_change(1).rolling(5).std()
    return _rank_pct(base, 5)

def vts_004_vol_5d_lvl_21d(close: pd.Series) -> pd.Series:
    """
    vts_004_vol_5d_lvl_21d
    ECONOMIC RATIONALE: Short-term realized volatility.
    """
    base = close.pct_change(1).rolling(5).std()
    return _rolling_mean(base, 21)

def vts_005_vol_5d_zscore_21d(close: pd.Series) -> pd.Series:
    """
    vts_005_vol_5d_zscore_21d
    ECONOMIC RATIONALE: Short-term realized volatility.
    """
    base = close.pct_change(1).rolling(5).std()
    return _zscore_rolling(base, 21)

def vts_006_vol_5d_rank_21d(close: pd.Series) -> pd.Series:
    """
    vts_006_vol_5d_rank_21d
    ECONOMIC RATIONALE: Short-term realized volatility.
    """
    base = close.pct_change(1).rolling(5).std()
    return _rank_pct(base, 21)

def vts_007_vol_5d_lvl_63d(close: pd.Series) -> pd.Series:
    """
    vts_007_vol_5d_lvl_63d
    ECONOMIC RATIONALE: Short-term realized volatility.
    """
    base = close.pct_change(1).rolling(5).std()
    return _rolling_mean(base, 63)

def vts_008_vol_5d_zscore_63d(close: pd.Series) -> pd.Series:
    """
    vts_008_vol_5d_zscore_63d
    ECONOMIC RATIONALE: Short-term realized volatility.
    """
    base = close.pct_change(1).rolling(5).std()
    return _zscore_rolling(base, 63)

def vts_009_vol_5d_rank_63d(close: pd.Series) -> pd.Series:
    """
    vts_009_vol_5d_rank_63d
    ECONOMIC RATIONALE: Short-term realized volatility.
    """
    base = close.pct_change(1).rolling(5).std()
    return _rank_pct(base, 63)

def vts_010_vol_5d_lvl_126d(close: pd.Series) -> pd.Series:
    """
    vts_010_vol_5d_lvl_126d
    ECONOMIC RATIONALE: Short-term realized volatility.
    """
    base = close.pct_change(1).rolling(5).std()
    return _rolling_mean(base, 126)

def vts_011_vol_5d_zscore_126d(close: pd.Series) -> pd.Series:
    """
    vts_011_vol_5d_zscore_126d
    ECONOMIC RATIONALE: Short-term realized volatility.
    """
    base = close.pct_change(1).rolling(5).std()
    return _zscore_rolling(base, 126)

def vts_012_vol_5d_rank_126d(close: pd.Series) -> pd.Series:
    """
    vts_012_vol_5d_rank_126d
    ECONOMIC RATIONALE: Short-term realized volatility.
    """
    base = close.pct_change(1).rolling(5).std()
    return _rank_pct(base, 126)

def vts_013_vol_5d_lvl_252d(close: pd.Series) -> pd.Series:
    """
    vts_013_vol_5d_lvl_252d
    ECONOMIC RATIONALE: Short-term realized volatility.
    """
    base = close.pct_change(1).rolling(5).std()
    return _rolling_mean(base, 252)

def vts_014_vol_5d_zscore_252d(close: pd.Series) -> pd.Series:
    """
    vts_014_vol_5d_zscore_252d
    ECONOMIC RATIONALE: Short-term realized volatility.
    """
    base = close.pct_change(1).rolling(5).std()
    return _zscore_rolling(base, 252)

def vts_015_vol_5d_rank_252d(close: pd.Series) -> pd.Series:
    """
    vts_015_vol_5d_rank_252d
    ECONOMIC RATIONALE: Short-term realized volatility.
    """
    base = close.pct_change(1).rolling(5).std()
    return _rank_pct(base, 252)

def vts_016_vol_21d_lvl_5d(close: pd.Series) -> pd.Series:
    """
    vts_016_vol_21d_lvl_5d
    ECONOMIC RATIONALE: Monthly realized volatility.
    """
    base = close.pct_change(1).rolling(21).std()
    return _rolling_mean(base, 5)

def vts_017_vol_21d_zscore_5d(close: pd.Series) -> pd.Series:
    """
    vts_017_vol_21d_zscore_5d
    ECONOMIC RATIONALE: Monthly realized volatility.
    """
    base = close.pct_change(1).rolling(21).std()
    return _zscore_rolling(base, 5)

def vts_018_vol_21d_rank_5d(close: pd.Series) -> pd.Series:
    """
    vts_018_vol_21d_rank_5d
    ECONOMIC RATIONALE: Monthly realized volatility.
    """
    base = close.pct_change(1).rolling(21).std()
    return _rank_pct(base, 5)

def vts_019_vol_21d_lvl_21d(close: pd.Series) -> pd.Series:
    """
    vts_019_vol_21d_lvl_21d
    ECONOMIC RATIONALE: Monthly realized volatility.
    """
    base = close.pct_change(1).rolling(21).std()
    return _rolling_mean(base, 21)

def vts_020_vol_21d_zscore_21d(close: pd.Series) -> pd.Series:
    """
    vts_020_vol_21d_zscore_21d
    ECONOMIC RATIONALE: Monthly realized volatility.
    """
    base = close.pct_change(1).rolling(21).std()
    return _zscore_rolling(base, 21)

def vts_021_vol_21d_rank_21d(close: pd.Series) -> pd.Series:
    """
    vts_021_vol_21d_rank_21d
    ECONOMIC RATIONALE: Monthly realized volatility.
    """
    base = close.pct_change(1).rolling(21).std()
    return _rank_pct(base, 21)

def vts_022_vol_21d_lvl_63d(close: pd.Series) -> pd.Series:
    """
    vts_022_vol_21d_lvl_63d
    ECONOMIC RATIONALE: Monthly realized volatility.
    """
    base = close.pct_change(1).rolling(21).std()
    return _rolling_mean(base, 63)

def vts_023_vol_21d_zscore_63d(close: pd.Series) -> pd.Series:
    """
    vts_023_vol_21d_zscore_63d
    ECONOMIC RATIONALE: Monthly realized volatility.
    """
    base = close.pct_change(1).rolling(21).std()
    return _zscore_rolling(base, 63)

def vts_024_vol_21d_rank_63d(close: pd.Series) -> pd.Series:
    """
    vts_024_vol_21d_rank_63d
    ECONOMIC RATIONALE: Monthly realized volatility.
    """
    base = close.pct_change(1).rolling(21).std()
    return _rank_pct(base, 63)

def vts_025_vol_21d_lvl_126d(close: pd.Series) -> pd.Series:
    """
    vts_025_vol_21d_lvl_126d
    ECONOMIC RATIONALE: Monthly realized volatility.
    """
    base = close.pct_change(1).rolling(21).std()
    return _rolling_mean(base, 126)

def vts_026_vol_21d_zscore_126d(close: pd.Series) -> pd.Series:
    """
    vts_026_vol_21d_zscore_126d
    ECONOMIC RATIONALE: Monthly realized volatility.
    """
    base = close.pct_change(1).rolling(21).std()
    return _zscore_rolling(base, 126)

def vts_027_vol_21d_rank_126d(close: pd.Series) -> pd.Series:
    """
    vts_027_vol_21d_rank_126d
    ECONOMIC RATIONALE: Monthly realized volatility.
    """
    base = close.pct_change(1).rolling(21).std()
    return _rank_pct(base, 126)

def vts_028_vol_21d_lvl_252d(close: pd.Series) -> pd.Series:
    """
    vts_028_vol_21d_lvl_252d
    ECONOMIC RATIONALE: Monthly realized volatility.
    """
    base = close.pct_change(1).rolling(21).std()
    return _rolling_mean(base, 252)

def vts_029_vol_21d_zscore_252d(close: pd.Series) -> pd.Series:
    """
    vts_029_vol_21d_zscore_252d
    ECONOMIC RATIONALE: Monthly realized volatility.
    """
    base = close.pct_change(1).rolling(21).std()
    return _zscore_rolling(base, 252)

def vts_030_vol_21d_rank_252d(close: pd.Series) -> pd.Series:
    """
    vts_030_vol_21d_rank_252d
    ECONOMIC RATIONALE: Monthly realized volatility.
    """
    base = close.pct_change(1).rolling(21).std()
    return _rank_pct(base, 252)

def vts_031_vol_63d_lvl_5d(close: pd.Series) -> pd.Series:
    """
    vts_031_vol_63d_lvl_5d
    ECONOMIC RATIONALE: Quarterly realized volatility.
    """
    base = close.pct_change(1).rolling(63).std()
    return _rolling_mean(base, 5)

def vts_032_vol_63d_zscore_5d(close: pd.Series) -> pd.Series:
    """
    vts_032_vol_63d_zscore_5d
    ECONOMIC RATIONALE: Quarterly realized volatility.
    """
    base = close.pct_change(1).rolling(63).std()
    return _zscore_rolling(base, 5)

def vts_033_vol_63d_rank_5d(close: pd.Series) -> pd.Series:
    """
    vts_033_vol_63d_rank_5d
    ECONOMIC RATIONALE: Quarterly realized volatility.
    """
    base = close.pct_change(1).rolling(63).std()
    return _rank_pct(base, 5)

def vts_034_vol_63d_lvl_21d(close: pd.Series) -> pd.Series:
    """
    vts_034_vol_63d_lvl_21d
    ECONOMIC RATIONALE: Quarterly realized volatility.
    """
    base = close.pct_change(1).rolling(63).std()
    return _rolling_mean(base, 21)

def vts_035_vol_63d_zscore_21d(close: pd.Series) -> pd.Series:
    """
    vts_035_vol_63d_zscore_21d
    ECONOMIC RATIONALE: Quarterly realized volatility.
    """
    base = close.pct_change(1).rolling(63).std()
    return _zscore_rolling(base, 21)

def vts_036_vol_63d_rank_21d(close: pd.Series) -> pd.Series:
    """
    vts_036_vol_63d_rank_21d
    ECONOMIC RATIONALE: Quarterly realized volatility.
    """
    base = close.pct_change(1).rolling(63).std()
    return _rank_pct(base, 21)

def vts_037_vol_63d_lvl_63d(close: pd.Series) -> pd.Series:
    """
    vts_037_vol_63d_lvl_63d
    ECONOMIC RATIONALE: Quarterly realized volatility.
    """
    base = close.pct_change(1).rolling(63).std()
    return _rolling_mean(base, 63)

def vts_038_vol_63d_zscore_63d(close: pd.Series) -> pd.Series:
    """
    vts_038_vol_63d_zscore_63d
    ECONOMIC RATIONALE: Quarterly realized volatility.
    """
    base = close.pct_change(1).rolling(63).std()
    return _zscore_rolling(base, 63)

def vts_039_vol_63d_rank_63d(close: pd.Series) -> pd.Series:
    """
    vts_039_vol_63d_rank_63d
    ECONOMIC RATIONALE: Quarterly realized volatility.
    """
    base = close.pct_change(1).rolling(63).std()
    return _rank_pct(base, 63)

def vts_040_vol_63d_lvl_126d(close: pd.Series) -> pd.Series:
    """
    vts_040_vol_63d_lvl_126d
    ECONOMIC RATIONALE: Quarterly realized volatility.
    """
    base = close.pct_change(1).rolling(63).std()
    return _rolling_mean(base, 126)

def vts_041_vol_63d_zscore_126d(close: pd.Series) -> pd.Series:
    """
    vts_041_vol_63d_zscore_126d
    ECONOMIC RATIONALE: Quarterly realized volatility.
    """
    base = close.pct_change(1).rolling(63).std()
    return _zscore_rolling(base, 126)

def vts_042_vol_63d_rank_126d(close: pd.Series) -> pd.Series:
    """
    vts_042_vol_63d_rank_126d
    ECONOMIC RATIONALE: Quarterly realized volatility.
    """
    base = close.pct_change(1).rolling(63).std()
    return _rank_pct(base, 126)

def vts_043_vol_63d_lvl_252d(close: pd.Series) -> pd.Series:
    """
    vts_043_vol_63d_lvl_252d
    ECONOMIC RATIONALE: Quarterly realized volatility.
    """
    base = close.pct_change(1).rolling(63).std()
    return _rolling_mean(base, 252)

def vts_044_vol_63d_zscore_252d(close: pd.Series) -> pd.Series:
    """
    vts_044_vol_63d_zscore_252d
    ECONOMIC RATIONALE: Quarterly realized volatility.
    """
    base = close.pct_change(1).rolling(63).std()
    return _zscore_rolling(base, 252)

def vts_045_vol_63d_rank_252d(close: pd.Series) -> pd.Series:
    """
    vts_045_vol_63d_rank_252d
    ECONOMIC RATIONALE: Quarterly realized volatility.
    """
    base = close.pct_change(1).rolling(63).std()
    return _rank_pct(base, 252)

def vts_046_vol_spread_short_long_lvl_5d(close: pd.Series) -> pd.Series:
    """
    vts_046_vol_spread_short_long_lvl_5d
    ECONOMIC RATIONALE: Spread between short and long term volatility.
    """
    base = close.pct_change(1).rolling(5).std() / close.pct_change(1).rolling(252).std()
    return _rolling_mean(base, 5)

def vts_047_vol_spread_short_long_zscore_5d(close: pd.Series) -> pd.Series:
    """
    vts_047_vol_spread_short_long_zscore_5d
    ECONOMIC RATIONALE: Spread between short and long term volatility.
    """
    base = close.pct_change(1).rolling(5).std() / close.pct_change(1).rolling(252).std()
    return _zscore_rolling(base, 5)

def vts_048_vol_spread_short_long_rank_5d(close: pd.Series) -> pd.Series:
    """
    vts_048_vol_spread_short_long_rank_5d
    ECONOMIC RATIONALE: Spread between short and long term volatility.
    """
    base = close.pct_change(1).rolling(5).std() / close.pct_change(1).rolling(252).std()
    return _rank_pct(base, 5)

def vts_049_vol_spread_short_long_lvl_21d(close: pd.Series) -> pd.Series:
    """
    vts_049_vol_spread_short_long_lvl_21d
    ECONOMIC RATIONALE: Spread between short and long term volatility.
    """
    base = close.pct_change(1).rolling(5).std() / close.pct_change(1).rolling(252).std()
    return _rolling_mean(base, 21)

def vts_050_vol_spread_short_long_zscore_21d(close: pd.Series) -> pd.Series:
    """
    vts_050_vol_spread_short_long_zscore_21d
    ECONOMIC RATIONALE: Spread between short and long term volatility.
    """
    base = close.pct_change(1).rolling(5).std() / close.pct_change(1).rolling(252).std()
    return _zscore_rolling(base, 21)

def vts_051_vol_spread_short_long_rank_21d(close: pd.Series) -> pd.Series:
    """
    vts_051_vol_spread_short_long_rank_21d
    ECONOMIC RATIONALE: Spread between short and long term volatility.
    """
    base = close.pct_change(1).rolling(5).std() / close.pct_change(1).rolling(252).std()
    return _rank_pct(base, 21)

def vts_052_vol_spread_short_long_lvl_63d(close: pd.Series) -> pd.Series:
    """
    vts_052_vol_spread_short_long_lvl_63d
    ECONOMIC RATIONALE: Spread between short and long term volatility.
    """
    base = close.pct_change(1).rolling(5).std() / close.pct_change(1).rolling(252).std()
    return _rolling_mean(base, 63)

def vts_053_vol_spread_short_long_zscore_63d(close: pd.Series) -> pd.Series:
    """
    vts_053_vol_spread_short_long_zscore_63d
    ECONOMIC RATIONALE: Spread between short and long term volatility.
    """
    base = close.pct_change(1).rolling(5).std() / close.pct_change(1).rolling(252).std()
    return _zscore_rolling(base, 63)

def vts_054_vol_spread_short_long_rank_63d(close: pd.Series) -> pd.Series:
    """
    vts_054_vol_spread_short_long_rank_63d
    ECONOMIC RATIONALE: Spread between short and long term volatility.
    """
    base = close.pct_change(1).rolling(5).std() / close.pct_change(1).rolling(252).std()
    return _rank_pct(base, 63)

def vts_055_vol_spread_short_long_lvl_126d(close: pd.Series) -> pd.Series:
    """
    vts_055_vol_spread_short_long_lvl_126d
    ECONOMIC RATIONALE: Spread between short and long term volatility.
    """
    base = close.pct_change(1).rolling(5).std() / close.pct_change(1).rolling(252).std()
    return _rolling_mean(base, 126)

def vts_056_vol_spread_short_long_zscore_126d(close: pd.Series) -> pd.Series:
    """
    vts_056_vol_spread_short_long_zscore_126d
    ECONOMIC RATIONALE: Spread between short and long term volatility.
    """
    base = close.pct_change(1).rolling(5).std() / close.pct_change(1).rolling(252).std()
    return _zscore_rolling(base, 126)

def vts_057_vol_spread_short_long_rank_126d(close: pd.Series) -> pd.Series:
    """
    vts_057_vol_spread_short_long_rank_126d
    ECONOMIC RATIONALE: Spread between short and long term volatility.
    """
    base = close.pct_change(1).rolling(5).std() / close.pct_change(1).rolling(252).std()
    return _rank_pct(base, 126)

def vts_058_vol_spread_short_long_lvl_252d(close: pd.Series) -> pd.Series:
    """
    vts_058_vol_spread_short_long_lvl_252d
    ECONOMIC RATIONALE: Spread between short and long term volatility.
    """
    base = close.pct_change(1).rolling(5).std() / close.pct_change(1).rolling(252).std()
    return _rolling_mean(base, 252)

def vts_059_vol_spread_short_long_zscore_252d(close: pd.Series) -> pd.Series:
    """
    vts_059_vol_spread_short_long_zscore_252d
    ECONOMIC RATIONALE: Spread between short and long term volatility.
    """
    base = close.pct_change(1).rolling(5).std() / close.pct_change(1).rolling(252).std()
    return _zscore_rolling(base, 252)

def vts_060_vol_spread_short_long_rank_252d(close: pd.Series) -> pd.Series:
    """
    vts_060_vol_spread_short_long_rank_252d
    ECONOMIC RATIONALE: Spread between short and long term volatility.
    """
    base = close.pct_change(1).rolling(5).std() / close.pct_change(1).rolling(252).std()
    return _rank_pct(base, 252)

def vts_061_vol_term_slope_lvl_5d(close: pd.Series) -> pd.Series:
    """
    vts_061_vol_term_slope_lvl_5d
    ECONOMIC RATIONALE: Slope of the volatility term structure.
    """
    base = (close.pct_change(1).rolling(252).std() - close.pct_change(1).rolling(21).std()) / 231
    return _rolling_mean(base, 5)

def vts_062_vol_term_slope_zscore_5d(close: pd.Series) -> pd.Series:
    """
    vts_062_vol_term_slope_zscore_5d
    ECONOMIC RATIONALE: Slope of the volatility term structure.
    """
    base = (close.pct_change(1).rolling(252).std() - close.pct_change(1).rolling(21).std()) / 231
    return _zscore_rolling(base, 5)

def vts_063_vol_term_slope_rank_5d(close: pd.Series) -> pd.Series:
    """
    vts_063_vol_term_slope_rank_5d
    ECONOMIC RATIONALE: Slope of the volatility term structure.
    """
    base = (close.pct_change(1).rolling(252).std() - close.pct_change(1).rolling(21).std()) / 231
    return _rank_pct(base, 5)

def vts_064_vol_term_slope_lvl_21d(close: pd.Series) -> pd.Series:
    """
    vts_064_vol_term_slope_lvl_21d
    ECONOMIC RATIONALE: Slope of the volatility term structure.
    """
    base = (close.pct_change(1).rolling(252).std() - close.pct_change(1).rolling(21).std()) / 231
    return _rolling_mean(base, 21)

def vts_065_vol_term_slope_zscore_21d(close: pd.Series) -> pd.Series:
    """
    vts_065_vol_term_slope_zscore_21d
    ECONOMIC RATIONALE: Slope of the volatility term structure.
    """
    base = (close.pct_change(1).rolling(252).std() - close.pct_change(1).rolling(21).std()) / 231
    return _zscore_rolling(base, 21)

def vts_066_vol_term_slope_rank_21d(close: pd.Series) -> pd.Series:
    """
    vts_066_vol_term_slope_rank_21d
    ECONOMIC RATIONALE: Slope of the volatility term structure.
    """
    base = (close.pct_change(1).rolling(252).std() - close.pct_change(1).rolling(21).std()) / 231
    return _rank_pct(base, 21)

def vts_067_vol_term_slope_lvl_63d(close: pd.Series) -> pd.Series:
    """
    vts_067_vol_term_slope_lvl_63d
    ECONOMIC RATIONALE: Slope of the volatility term structure.
    """
    base = (close.pct_change(1).rolling(252).std() - close.pct_change(1).rolling(21).std()) / 231
    return _rolling_mean(base, 63)

def vts_068_vol_term_slope_zscore_63d(close: pd.Series) -> pd.Series:
    """
    vts_068_vol_term_slope_zscore_63d
    ECONOMIC RATIONALE: Slope of the volatility term structure.
    """
    base = (close.pct_change(1).rolling(252).std() - close.pct_change(1).rolling(21).std()) / 231
    return _zscore_rolling(base, 63)

def vts_069_vol_term_slope_rank_63d(close: pd.Series) -> pd.Series:
    """
    vts_069_vol_term_slope_rank_63d
    ECONOMIC RATIONALE: Slope of the volatility term structure.
    """
    base = (close.pct_change(1).rolling(252).std() - close.pct_change(1).rolling(21).std()) / 231
    return _rank_pct(base, 63)

def vts_070_vol_term_slope_lvl_126d(close: pd.Series) -> pd.Series:
    """
    vts_070_vol_term_slope_lvl_126d
    ECONOMIC RATIONALE: Slope of the volatility term structure.
    """
    base = (close.pct_change(1).rolling(252).std() - close.pct_change(1).rolling(21).std()) / 231
    return _rolling_mean(base, 126)

def vts_071_vol_term_slope_zscore_126d(close: pd.Series) -> pd.Series:
    """
    vts_071_vol_term_slope_zscore_126d
    ECONOMIC RATIONALE: Slope of the volatility term structure.
    """
    base = (close.pct_change(1).rolling(252).std() - close.pct_change(1).rolling(21).std()) / 231
    return _zscore_rolling(base, 126)

def vts_072_vol_term_slope_rank_126d(close: pd.Series) -> pd.Series:
    """
    vts_072_vol_term_slope_rank_126d
    ECONOMIC RATIONALE: Slope of the volatility term structure.
    """
    base = (close.pct_change(1).rolling(252).std() - close.pct_change(1).rolling(21).std()) / 231
    return _rank_pct(base, 126)

def vts_073_vol_term_slope_lvl_252d(close: pd.Series) -> pd.Series:
    """
    vts_073_vol_term_slope_lvl_252d
    ECONOMIC RATIONALE: Slope of the volatility term structure.
    """
    base = (close.pct_change(1).rolling(252).std() - close.pct_change(1).rolling(21).std()) / 231
    return _rolling_mean(base, 252)

def vts_074_vol_term_slope_zscore_252d(close: pd.Series) -> pd.Series:
    """
    vts_074_vol_term_slope_zscore_252d
    ECONOMIC RATIONALE: Slope of the volatility term structure.
    """
    base = (close.pct_change(1).rolling(252).std() - close.pct_change(1).rolling(21).std()) / 231
    return _zscore_rolling(base, 252)

def vts_075_vol_term_slope_rank_252d(close: pd.Series) -> pd.Series:
    """
    vts_075_vol_term_slope_rank_252d
    ECONOMIC RATIONALE: Slope of the volatility term structure.
    """
    base = (close.pct_change(1).rolling(252).std() - close.pct_change(1).rolling(21).std()) / 231
    return _rank_pct(base, 252)

def vts_076_vol_convexity_lvl_5d(close: pd.Series) -> pd.Series:
    """
    vts_076_vol_convexity_lvl_5d
    ECONOMIC RATIONALE: Change in the rate of volatility change.
    """
    base = close.pct_change(1).rolling(21).std().diff(1).diff(1)
    return _rolling_mean(base, 5)

def vts_077_vol_convexity_zscore_5d(close: pd.Series) -> pd.Series:
    """
    vts_077_vol_convexity_zscore_5d
    ECONOMIC RATIONALE: Change in the rate of volatility change.
    """
    base = close.pct_change(1).rolling(21).std().diff(1).diff(1)
    return _zscore_rolling(base, 5)

def vts_078_vol_convexity_rank_5d(close: pd.Series) -> pd.Series:
    """
    vts_078_vol_convexity_rank_5d
    ECONOMIC RATIONALE: Change in the rate of volatility change.
    """
    base = close.pct_change(1).rolling(21).std().diff(1).diff(1)
    return _rank_pct(base, 5)

def vts_079_vol_convexity_lvl_21d(close: pd.Series) -> pd.Series:
    """
    vts_079_vol_convexity_lvl_21d
    ECONOMIC RATIONALE: Change in the rate of volatility change.
    """
    base = close.pct_change(1).rolling(21).std().diff(1).diff(1)
    return _rolling_mean(base, 21)

def vts_080_vol_convexity_zscore_21d(close: pd.Series) -> pd.Series:
    """
    vts_080_vol_convexity_zscore_21d
    ECONOMIC RATIONALE: Change in the rate of volatility change.
    """
    base = close.pct_change(1).rolling(21).std().diff(1).diff(1)
    return _zscore_rolling(base, 21)

def vts_081_vol_convexity_rank_21d(close: pd.Series) -> pd.Series:
    """
    vts_081_vol_convexity_rank_21d
    ECONOMIC RATIONALE: Change in the rate of volatility change.
    """
    base = close.pct_change(1).rolling(21).std().diff(1).diff(1)
    return _rank_pct(base, 21)

def vts_082_vol_convexity_lvl_63d(close: pd.Series) -> pd.Series:
    """
    vts_082_vol_convexity_lvl_63d
    ECONOMIC RATIONALE: Change in the rate of volatility change.
    """
    base = close.pct_change(1).rolling(21).std().diff(1).diff(1)
    return _rolling_mean(base, 63)

def vts_083_vol_convexity_zscore_63d(close: pd.Series) -> pd.Series:
    """
    vts_083_vol_convexity_zscore_63d
    ECONOMIC RATIONALE: Change in the rate of volatility change.
    """
    base = close.pct_change(1).rolling(21).std().diff(1).diff(1)
    return _zscore_rolling(base, 63)

def vts_084_vol_convexity_rank_63d(close: pd.Series) -> pd.Series:
    """
    vts_084_vol_convexity_rank_63d
    ECONOMIC RATIONALE: Change in the rate of volatility change.
    """
    base = close.pct_change(1).rolling(21).std().diff(1).diff(1)
    return _rank_pct(base, 63)

def vts_085_vol_convexity_lvl_126d(close: pd.Series) -> pd.Series:
    """
    vts_085_vol_convexity_lvl_126d
    ECONOMIC RATIONALE: Change in the rate of volatility change.
    """
    base = close.pct_change(1).rolling(21).std().diff(1).diff(1)
    return _rolling_mean(base, 126)

def vts_086_vol_convexity_zscore_126d(close: pd.Series) -> pd.Series:
    """
    vts_086_vol_convexity_zscore_126d
    ECONOMIC RATIONALE: Change in the rate of volatility change.
    """
    base = close.pct_change(1).rolling(21).std().diff(1).diff(1)
    return _zscore_rolling(base, 126)

def vts_087_vol_convexity_rank_126d(close: pd.Series) -> pd.Series:
    """
    vts_087_vol_convexity_rank_126d
    ECONOMIC RATIONALE: Change in the rate of volatility change.
    """
    base = close.pct_change(1).rolling(21).std().diff(1).diff(1)
    return _rank_pct(base, 126)

def vts_088_vol_convexity_lvl_252d(close: pd.Series) -> pd.Series:
    """
    vts_088_vol_convexity_lvl_252d
    ECONOMIC RATIONALE: Change in the rate of volatility change.
    """
    base = close.pct_change(1).rolling(21).std().diff(1).diff(1)
    return _rolling_mean(base, 252)

def vts_089_vol_convexity_zscore_252d(close: pd.Series) -> pd.Series:
    """
    vts_089_vol_convexity_zscore_252d
    ECONOMIC RATIONALE: Change in the rate of volatility change.
    """
    base = close.pct_change(1).rolling(21).std().diff(1).diff(1)
    return _zscore_rolling(base, 252)

def vts_090_vol_convexity_rank_252d(close: pd.Series) -> pd.Series:
    """
    vts_090_vol_convexity_rank_252d
    ECONOMIC RATIONALE: Change in the rate of volatility change.
    """
    base = close.pct_change(1).rolling(21).std().diff(1).diff(1)
    return _rank_pct(base, 252)

def vts_091_vol_mean_reversion_speed_lvl_5d(close: pd.Series) -> pd.Series:
    """
    vts_091_vol_mean_reversion_speed_lvl_5d
    ECONOMIC RATIONALE: Distance from long-term volatility mean.
    """
    base = (close.pct_change(1).rolling(21).std() - close.pct_change(1).rolling(252).std()).abs()
    return _rolling_mean(base, 5)

def vts_092_vol_mean_reversion_speed_zscore_5d(close: pd.Series) -> pd.Series:
    """
    vts_092_vol_mean_reversion_speed_zscore_5d
    ECONOMIC RATIONALE: Distance from long-term volatility mean.
    """
    base = (close.pct_change(1).rolling(21).std() - close.pct_change(1).rolling(252).std()).abs()
    return _zscore_rolling(base, 5)

def vts_093_vol_mean_reversion_speed_rank_5d(close: pd.Series) -> pd.Series:
    """
    vts_093_vol_mean_reversion_speed_rank_5d
    ECONOMIC RATIONALE: Distance from long-term volatility mean.
    """
    base = (close.pct_change(1).rolling(21).std() - close.pct_change(1).rolling(252).std()).abs()
    return _rank_pct(base, 5)

def vts_094_vol_mean_reversion_speed_lvl_21d(close: pd.Series) -> pd.Series:
    """
    vts_094_vol_mean_reversion_speed_lvl_21d
    ECONOMIC RATIONALE: Distance from long-term volatility mean.
    """
    base = (close.pct_change(1).rolling(21).std() - close.pct_change(1).rolling(252).std()).abs()
    return _rolling_mean(base, 21)

def vts_095_vol_mean_reversion_speed_zscore_21d(close: pd.Series) -> pd.Series:
    """
    vts_095_vol_mean_reversion_speed_zscore_21d
    ECONOMIC RATIONALE: Distance from long-term volatility mean.
    """
    base = (close.pct_change(1).rolling(21).std() - close.pct_change(1).rolling(252).std()).abs()
    return _zscore_rolling(base, 21)

def vts_096_vol_mean_reversion_speed_rank_21d(close: pd.Series) -> pd.Series:
    """
    vts_096_vol_mean_reversion_speed_rank_21d
    ECONOMIC RATIONALE: Distance from long-term volatility mean.
    """
    base = (close.pct_change(1).rolling(21).std() - close.pct_change(1).rolling(252).std()).abs()
    return _rank_pct(base, 21)

def vts_097_vol_mean_reversion_speed_lvl_63d(close: pd.Series) -> pd.Series:
    """
    vts_097_vol_mean_reversion_speed_lvl_63d
    ECONOMIC RATIONALE: Distance from long-term volatility mean.
    """
    base = (close.pct_change(1).rolling(21).std() - close.pct_change(1).rolling(252).std()).abs()
    return _rolling_mean(base, 63)

def vts_098_vol_mean_reversion_speed_zscore_63d(close: pd.Series) -> pd.Series:
    """
    vts_098_vol_mean_reversion_speed_zscore_63d
    ECONOMIC RATIONALE: Distance from long-term volatility mean.
    """
    base = (close.pct_change(1).rolling(21).std() - close.pct_change(1).rolling(252).std()).abs()
    return _zscore_rolling(base, 63)

def vts_099_vol_mean_reversion_speed_rank_63d(close: pd.Series) -> pd.Series:
    """
    vts_099_vol_mean_reversion_speed_rank_63d
    ECONOMIC RATIONALE: Distance from long-term volatility mean.
    """
    base = (close.pct_change(1).rolling(21).std() - close.pct_change(1).rolling(252).std()).abs()
    return _rank_pct(base, 63)

def vts_100_vol_mean_reversion_speed_lvl_126d(close: pd.Series) -> pd.Series:
    """
    vts_100_vol_mean_reversion_speed_lvl_126d
    ECONOMIC RATIONALE: Distance from long-term volatility mean.
    """
    base = (close.pct_change(1).rolling(21).std() - close.pct_change(1).rolling(252).std()).abs()
    return _rolling_mean(base, 126)

def vts_101_vol_mean_reversion_speed_zscore_126d(close: pd.Series) -> pd.Series:
    """
    vts_101_vol_mean_reversion_speed_zscore_126d
    ECONOMIC RATIONALE: Distance from long-term volatility mean.
    """
    base = (close.pct_change(1).rolling(21).std() - close.pct_change(1).rolling(252).std()).abs()
    return _zscore_rolling(base, 126)

def vts_102_vol_mean_reversion_speed_rank_126d(close: pd.Series) -> pd.Series:
    """
    vts_102_vol_mean_reversion_speed_rank_126d
    ECONOMIC RATIONALE: Distance from long-term volatility mean.
    """
    base = (close.pct_change(1).rolling(21).std() - close.pct_change(1).rolling(252).std()).abs()
    return _rank_pct(base, 126)

def vts_103_vol_mean_reversion_speed_lvl_252d(close: pd.Series) -> pd.Series:
    """
    vts_103_vol_mean_reversion_speed_lvl_252d
    ECONOMIC RATIONALE: Distance from long-term volatility mean.
    """
    base = (close.pct_change(1).rolling(21).std() - close.pct_change(1).rolling(252).std()).abs()
    return _rolling_mean(base, 252)

def vts_104_vol_mean_reversion_speed_zscore_252d(close: pd.Series) -> pd.Series:
    """
    vts_104_vol_mean_reversion_speed_zscore_252d
    ECONOMIC RATIONALE: Distance from long-term volatility mean.
    """
    base = (close.pct_change(1).rolling(21).std() - close.pct_change(1).rolling(252).std()).abs()
    return _zscore_rolling(base, 252)

def vts_105_vol_mean_reversion_speed_rank_252d(close: pd.Series) -> pd.Series:
    """
    vts_105_vol_mean_reversion_speed_rank_252d
    ECONOMIC RATIONALE: Distance from long-term volatility mean.
    """
    base = (close.pct_change(1).rolling(21).std() - close.pct_change(1).rolling(252).std()).abs()
    return _rank_pct(base, 252)

def vts_106_vol_regime_z_lvl_5d(close: pd.Series) -> pd.Series:
    """
    vts_106_vol_regime_z_lvl_5d
    ECONOMIC RATIONALE: Z-score of current volatility regime.
    """
    base = _zscore_rolling(close.pct_change(1).rolling(21).std(), 252)
    return _rolling_mean(base, 5)

def vts_107_vol_regime_z_zscore_5d(close: pd.Series) -> pd.Series:
    """
    vts_107_vol_regime_z_zscore_5d
    ECONOMIC RATIONALE: Z-score of current volatility regime.
    """
    base = _zscore_rolling(close.pct_change(1).rolling(21).std(), 252)
    return _zscore_rolling(base, 5)

def vts_108_vol_regime_z_rank_5d(close: pd.Series) -> pd.Series:
    """
    vts_108_vol_regime_z_rank_5d
    ECONOMIC RATIONALE: Z-score of current volatility regime.
    """
    base = _zscore_rolling(close.pct_change(1).rolling(21).std(), 252)
    return _rank_pct(base, 5)

def vts_109_vol_regime_z_lvl_21d(close: pd.Series) -> pd.Series:
    """
    vts_109_vol_regime_z_lvl_21d
    ECONOMIC RATIONALE: Z-score of current volatility regime.
    """
    base = _zscore_rolling(close.pct_change(1).rolling(21).std(), 252)
    return _rolling_mean(base, 21)

def vts_110_vol_regime_z_zscore_21d(close: pd.Series) -> pd.Series:
    """
    vts_110_vol_regime_z_zscore_21d
    ECONOMIC RATIONALE: Z-score of current volatility regime.
    """
    base = _zscore_rolling(close.pct_change(1).rolling(21).std(), 252)
    return _zscore_rolling(base, 21)

def vts_111_vol_regime_z_rank_21d(close: pd.Series) -> pd.Series:
    """
    vts_111_vol_regime_z_rank_21d
    ECONOMIC RATIONALE: Z-score of current volatility regime.
    """
    base = _zscore_rolling(close.pct_change(1).rolling(21).std(), 252)
    return _rank_pct(base, 21)

def vts_112_vol_regime_z_lvl_63d(close: pd.Series) -> pd.Series:
    """
    vts_112_vol_regime_z_lvl_63d
    ECONOMIC RATIONALE: Z-score of current volatility regime.
    """
    base = _zscore_rolling(close.pct_change(1).rolling(21).std(), 252)
    return _rolling_mean(base, 63)

def vts_113_vol_regime_z_zscore_63d(close: pd.Series) -> pd.Series:
    """
    vts_113_vol_regime_z_zscore_63d
    ECONOMIC RATIONALE: Z-score of current volatility regime.
    """
    base = _zscore_rolling(close.pct_change(1).rolling(21).std(), 252)
    return _zscore_rolling(base, 63)

def vts_114_vol_regime_z_rank_63d(close: pd.Series) -> pd.Series:
    """
    vts_114_vol_regime_z_rank_63d
    ECONOMIC RATIONALE: Z-score of current volatility regime.
    """
    base = _zscore_rolling(close.pct_change(1).rolling(21).std(), 252)
    return _rank_pct(base, 63)

def vts_115_vol_regime_z_lvl_126d(close: pd.Series) -> pd.Series:
    """
    vts_115_vol_regime_z_lvl_126d
    ECONOMIC RATIONALE: Z-score of current volatility regime.
    """
    base = _zscore_rolling(close.pct_change(1).rolling(21).std(), 252)
    return _rolling_mean(base, 126)

def vts_116_vol_regime_z_zscore_126d(close: pd.Series) -> pd.Series:
    """
    vts_116_vol_regime_z_zscore_126d
    ECONOMIC RATIONALE: Z-score of current volatility regime.
    """
    base = _zscore_rolling(close.pct_change(1).rolling(21).std(), 252)
    return _zscore_rolling(base, 126)

def vts_117_vol_regime_z_rank_126d(close: pd.Series) -> pd.Series:
    """
    vts_117_vol_regime_z_rank_126d
    ECONOMIC RATIONALE: Z-score of current volatility regime.
    """
    base = _zscore_rolling(close.pct_change(1).rolling(21).std(), 252)
    return _rank_pct(base, 126)

def vts_118_vol_regime_z_lvl_252d(close: pd.Series) -> pd.Series:
    """
    vts_118_vol_regime_z_lvl_252d
    ECONOMIC RATIONALE: Z-score of current volatility regime.
    """
    base = _zscore_rolling(close.pct_change(1).rolling(21).std(), 252)
    return _rolling_mean(base, 252)

def vts_119_vol_regime_z_zscore_252d(close: pd.Series) -> pd.Series:
    """
    vts_119_vol_regime_z_zscore_252d
    ECONOMIC RATIONALE: Z-score of current volatility regime.
    """
    base = _zscore_rolling(close.pct_change(1).rolling(21).std(), 252)
    return _zscore_rolling(base, 252)

def vts_120_vol_regime_z_rank_252d(close: pd.Series) -> pd.Series:
    """
    vts_120_vol_regime_z_rank_252d
    ECONOMIC RATIONALE: Z-score of current volatility regime.
    """
    base = _zscore_rolling(close.pct_change(1).rolling(21).std(), 252)
    return _rank_pct(base, 252)

# ── Registry ──────────────────────────────────────────────────────────────────
V115_REGISTRY_1 = {
    "vts_001_vol_5d_lvl_5d": {"inputs": ["close"], "func": vts_001_vol_5d_lvl_5d},
    "vts_002_vol_5d_zscore_5d": {"inputs": ["close"], "func": vts_002_vol_5d_zscore_5d},
    "vts_003_vol_5d_rank_5d": {"inputs": ["close"], "func": vts_003_vol_5d_rank_5d},
    "vts_004_vol_5d_lvl_21d": {"inputs": ["close"], "func": vts_004_vol_5d_lvl_21d},
    "vts_005_vol_5d_zscore_21d": {"inputs": ["close"], "func": vts_005_vol_5d_zscore_21d},
    "vts_006_vol_5d_rank_21d": {"inputs": ["close"], "func": vts_006_vol_5d_rank_21d},
    "vts_007_vol_5d_lvl_63d": {"inputs": ["close"], "func": vts_007_vol_5d_lvl_63d},
    "vts_008_vol_5d_zscore_63d": {"inputs": ["close"], "func": vts_008_vol_5d_zscore_63d},
    "vts_009_vol_5d_rank_63d": {"inputs": ["close"], "func": vts_009_vol_5d_rank_63d},
    "vts_010_vol_5d_lvl_126d": {"inputs": ["close"], "func": vts_010_vol_5d_lvl_126d},
    "vts_011_vol_5d_zscore_126d": {"inputs": ["close"], "func": vts_011_vol_5d_zscore_126d},
    "vts_012_vol_5d_rank_126d": {"inputs": ["close"], "func": vts_012_vol_5d_rank_126d},
    "vts_013_vol_5d_lvl_252d": {"inputs": ["close"], "func": vts_013_vol_5d_lvl_252d},
    "vts_014_vol_5d_zscore_252d": {"inputs": ["close"], "func": vts_014_vol_5d_zscore_252d},
    "vts_015_vol_5d_rank_252d": {"inputs": ["close"], "func": vts_015_vol_5d_rank_252d},
    "vts_016_vol_21d_lvl_5d": {"inputs": ["close"], "func": vts_016_vol_21d_lvl_5d},
    "vts_017_vol_21d_zscore_5d": {"inputs": ["close"], "func": vts_017_vol_21d_zscore_5d},
    "vts_018_vol_21d_rank_5d": {"inputs": ["close"], "func": vts_018_vol_21d_rank_5d},
    "vts_019_vol_21d_lvl_21d": {"inputs": ["close"], "func": vts_019_vol_21d_lvl_21d},
    "vts_020_vol_21d_zscore_21d": {"inputs": ["close"], "func": vts_020_vol_21d_zscore_21d},
    "vts_021_vol_21d_rank_21d": {"inputs": ["close"], "func": vts_021_vol_21d_rank_21d},
    "vts_022_vol_21d_lvl_63d": {"inputs": ["close"], "func": vts_022_vol_21d_lvl_63d},
    "vts_023_vol_21d_zscore_63d": {"inputs": ["close"], "func": vts_023_vol_21d_zscore_63d},
    "vts_024_vol_21d_rank_63d": {"inputs": ["close"], "func": vts_024_vol_21d_rank_63d},
    "vts_025_vol_21d_lvl_126d": {"inputs": ["close"], "func": vts_025_vol_21d_lvl_126d},
    "vts_026_vol_21d_zscore_126d": {"inputs": ["close"], "func": vts_026_vol_21d_zscore_126d},
    "vts_027_vol_21d_rank_126d": {"inputs": ["close"], "func": vts_027_vol_21d_rank_126d},
    "vts_028_vol_21d_lvl_252d": {"inputs": ["close"], "func": vts_028_vol_21d_lvl_252d},
    "vts_029_vol_21d_zscore_252d": {"inputs": ["close"], "func": vts_029_vol_21d_zscore_252d},
    "vts_030_vol_21d_rank_252d": {"inputs": ["close"], "func": vts_030_vol_21d_rank_252d},
    "vts_031_vol_63d_lvl_5d": {"inputs": ["close"], "func": vts_031_vol_63d_lvl_5d},
    "vts_032_vol_63d_zscore_5d": {"inputs": ["close"], "func": vts_032_vol_63d_zscore_5d},
    "vts_033_vol_63d_rank_5d": {"inputs": ["close"], "func": vts_033_vol_63d_rank_5d},
    "vts_034_vol_63d_lvl_21d": {"inputs": ["close"], "func": vts_034_vol_63d_lvl_21d},
    "vts_035_vol_63d_zscore_21d": {"inputs": ["close"], "func": vts_035_vol_63d_zscore_21d},
    "vts_036_vol_63d_rank_21d": {"inputs": ["close"], "func": vts_036_vol_63d_rank_21d},
    "vts_037_vol_63d_lvl_63d": {"inputs": ["close"], "func": vts_037_vol_63d_lvl_63d},
    "vts_038_vol_63d_zscore_63d": {"inputs": ["close"], "func": vts_038_vol_63d_zscore_63d},
    "vts_039_vol_63d_rank_63d": {"inputs": ["close"], "func": vts_039_vol_63d_rank_63d},
    "vts_040_vol_63d_lvl_126d": {"inputs": ["close"], "func": vts_040_vol_63d_lvl_126d},
    "vts_041_vol_63d_zscore_126d": {"inputs": ["close"], "func": vts_041_vol_63d_zscore_126d},
    "vts_042_vol_63d_rank_126d": {"inputs": ["close"], "func": vts_042_vol_63d_rank_126d},
    "vts_043_vol_63d_lvl_252d": {"inputs": ["close"], "func": vts_043_vol_63d_lvl_252d},
    "vts_044_vol_63d_zscore_252d": {"inputs": ["close"], "func": vts_044_vol_63d_zscore_252d},
    "vts_045_vol_63d_rank_252d": {"inputs": ["close"], "func": vts_045_vol_63d_rank_252d},
    "vts_046_vol_spread_short_long_lvl_5d": {"inputs": ["close"], "func": vts_046_vol_spread_short_long_lvl_5d},
    "vts_047_vol_spread_short_long_zscore_5d": {"inputs": ["close"], "func": vts_047_vol_spread_short_long_zscore_5d},
    "vts_048_vol_spread_short_long_rank_5d": {"inputs": ["close"], "func": vts_048_vol_spread_short_long_rank_5d},
    "vts_049_vol_spread_short_long_lvl_21d": {"inputs": ["close"], "func": vts_049_vol_spread_short_long_lvl_21d},
    "vts_050_vol_spread_short_long_zscore_21d": {"inputs": ["close"], "func": vts_050_vol_spread_short_long_zscore_21d},
    "vts_051_vol_spread_short_long_rank_21d": {"inputs": ["close"], "func": vts_051_vol_spread_short_long_rank_21d},
    "vts_052_vol_spread_short_long_lvl_63d": {"inputs": ["close"], "func": vts_052_vol_spread_short_long_lvl_63d},
    "vts_053_vol_spread_short_long_zscore_63d": {"inputs": ["close"], "func": vts_053_vol_spread_short_long_zscore_63d},
    "vts_054_vol_spread_short_long_rank_63d": {"inputs": ["close"], "func": vts_054_vol_spread_short_long_rank_63d},
    "vts_055_vol_spread_short_long_lvl_126d": {"inputs": ["close"], "func": vts_055_vol_spread_short_long_lvl_126d},
    "vts_056_vol_spread_short_long_zscore_126d": {"inputs": ["close"], "func": vts_056_vol_spread_short_long_zscore_126d},
    "vts_057_vol_spread_short_long_rank_126d": {"inputs": ["close"], "func": vts_057_vol_spread_short_long_rank_126d},
    "vts_058_vol_spread_short_long_lvl_252d": {"inputs": ["close"], "func": vts_058_vol_spread_short_long_lvl_252d},
    "vts_059_vol_spread_short_long_zscore_252d": {"inputs": ["close"], "func": vts_059_vol_spread_short_long_zscore_252d},
    "vts_060_vol_spread_short_long_rank_252d": {"inputs": ["close"], "func": vts_060_vol_spread_short_long_rank_252d},
    "vts_061_vol_term_slope_lvl_5d": {"inputs": ["close"], "func": vts_061_vol_term_slope_lvl_5d},
    "vts_062_vol_term_slope_zscore_5d": {"inputs": ["close"], "func": vts_062_vol_term_slope_zscore_5d},
    "vts_063_vol_term_slope_rank_5d": {"inputs": ["close"], "func": vts_063_vol_term_slope_rank_5d},
    "vts_064_vol_term_slope_lvl_21d": {"inputs": ["close"], "func": vts_064_vol_term_slope_lvl_21d},
    "vts_065_vol_term_slope_zscore_21d": {"inputs": ["close"], "func": vts_065_vol_term_slope_zscore_21d},
    "vts_066_vol_term_slope_rank_21d": {"inputs": ["close"], "func": vts_066_vol_term_slope_rank_21d},
    "vts_067_vol_term_slope_lvl_63d": {"inputs": ["close"], "func": vts_067_vol_term_slope_lvl_63d},
    "vts_068_vol_term_slope_zscore_63d": {"inputs": ["close"], "func": vts_068_vol_term_slope_zscore_63d},
    "vts_069_vol_term_slope_rank_63d": {"inputs": ["close"], "func": vts_069_vol_term_slope_rank_63d},
    "vts_070_vol_term_slope_lvl_126d": {"inputs": ["close"], "func": vts_070_vol_term_slope_lvl_126d},
    "vts_071_vol_term_slope_zscore_126d": {"inputs": ["close"], "func": vts_071_vol_term_slope_zscore_126d},
    "vts_072_vol_term_slope_rank_126d": {"inputs": ["close"], "func": vts_072_vol_term_slope_rank_126d},
    "vts_073_vol_term_slope_lvl_252d": {"inputs": ["close"], "func": vts_073_vol_term_slope_lvl_252d},
    "vts_074_vol_term_slope_zscore_252d": {"inputs": ["close"], "func": vts_074_vol_term_slope_zscore_252d},
    "vts_075_vol_term_slope_rank_252d": {"inputs": ["close"], "func": vts_075_vol_term_slope_rank_252d},
    "vts_076_vol_convexity_lvl_5d": {"inputs": ["close"], "func": vts_076_vol_convexity_lvl_5d},
    "vts_077_vol_convexity_zscore_5d": {"inputs": ["close"], "func": vts_077_vol_convexity_zscore_5d},
    "vts_078_vol_convexity_rank_5d": {"inputs": ["close"], "func": vts_078_vol_convexity_rank_5d},
    "vts_079_vol_convexity_lvl_21d": {"inputs": ["close"], "func": vts_079_vol_convexity_lvl_21d},
    "vts_080_vol_convexity_zscore_21d": {"inputs": ["close"], "func": vts_080_vol_convexity_zscore_21d},
    "vts_081_vol_convexity_rank_21d": {"inputs": ["close"], "func": vts_081_vol_convexity_rank_21d},
    "vts_082_vol_convexity_lvl_63d": {"inputs": ["close"], "func": vts_082_vol_convexity_lvl_63d},
    "vts_083_vol_convexity_zscore_63d": {"inputs": ["close"], "func": vts_083_vol_convexity_zscore_63d},
    "vts_084_vol_convexity_rank_63d": {"inputs": ["close"], "func": vts_084_vol_convexity_rank_63d},
    "vts_085_vol_convexity_lvl_126d": {"inputs": ["close"], "func": vts_085_vol_convexity_lvl_126d},
    "vts_086_vol_convexity_zscore_126d": {"inputs": ["close"], "func": vts_086_vol_convexity_zscore_126d},
    "vts_087_vol_convexity_rank_126d": {"inputs": ["close"], "func": vts_087_vol_convexity_rank_126d},
    "vts_088_vol_convexity_lvl_252d": {"inputs": ["close"], "func": vts_088_vol_convexity_lvl_252d},
    "vts_089_vol_convexity_zscore_252d": {"inputs": ["close"], "func": vts_089_vol_convexity_zscore_252d},
    "vts_090_vol_convexity_rank_252d": {"inputs": ["close"], "func": vts_090_vol_convexity_rank_252d},
    "vts_091_vol_mean_reversion_speed_lvl_5d": {"inputs": ["close"], "func": vts_091_vol_mean_reversion_speed_lvl_5d},
    "vts_092_vol_mean_reversion_speed_zscore_5d": {"inputs": ["close"], "func": vts_092_vol_mean_reversion_speed_zscore_5d},
    "vts_093_vol_mean_reversion_speed_rank_5d": {"inputs": ["close"], "func": vts_093_vol_mean_reversion_speed_rank_5d},
    "vts_094_vol_mean_reversion_speed_lvl_21d": {"inputs": ["close"], "func": vts_094_vol_mean_reversion_speed_lvl_21d},
    "vts_095_vol_mean_reversion_speed_zscore_21d": {"inputs": ["close"], "func": vts_095_vol_mean_reversion_speed_zscore_21d},
    "vts_096_vol_mean_reversion_speed_rank_21d": {"inputs": ["close"], "func": vts_096_vol_mean_reversion_speed_rank_21d},
    "vts_097_vol_mean_reversion_speed_lvl_63d": {"inputs": ["close"], "func": vts_097_vol_mean_reversion_speed_lvl_63d},
    "vts_098_vol_mean_reversion_speed_zscore_63d": {"inputs": ["close"], "func": vts_098_vol_mean_reversion_speed_zscore_63d},
    "vts_099_vol_mean_reversion_speed_rank_63d": {"inputs": ["close"], "func": vts_099_vol_mean_reversion_speed_rank_63d},
    "vts_100_vol_mean_reversion_speed_lvl_126d": {"inputs": ["close"], "func": vts_100_vol_mean_reversion_speed_lvl_126d},
    "vts_101_vol_mean_reversion_speed_zscore_126d": {"inputs": ["close"], "func": vts_101_vol_mean_reversion_speed_zscore_126d},
    "vts_102_vol_mean_reversion_speed_rank_126d": {"inputs": ["close"], "func": vts_102_vol_mean_reversion_speed_rank_126d},
    "vts_103_vol_mean_reversion_speed_lvl_252d": {"inputs": ["close"], "func": vts_103_vol_mean_reversion_speed_lvl_252d},
    "vts_104_vol_mean_reversion_speed_zscore_252d": {"inputs": ["close"], "func": vts_104_vol_mean_reversion_speed_zscore_252d},
    "vts_105_vol_mean_reversion_speed_rank_252d": {"inputs": ["close"], "func": vts_105_vol_mean_reversion_speed_rank_252d},
    "vts_106_vol_regime_z_lvl_5d": {"inputs": ["close"], "func": vts_106_vol_regime_z_lvl_5d},
    "vts_107_vol_regime_z_zscore_5d": {"inputs": ["close"], "func": vts_107_vol_regime_z_zscore_5d},
    "vts_108_vol_regime_z_rank_5d": {"inputs": ["close"], "func": vts_108_vol_regime_z_rank_5d},
    "vts_109_vol_regime_z_lvl_21d": {"inputs": ["close"], "func": vts_109_vol_regime_z_lvl_21d},
    "vts_110_vol_regime_z_zscore_21d": {"inputs": ["close"], "func": vts_110_vol_regime_z_zscore_21d},
    "vts_111_vol_regime_z_rank_21d": {"inputs": ["close"], "func": vts_111_vol_regime_z_rank_21d},
    "vts_112_vol_regime_z_lvl_63d": {"inputs": ["close"], "func": vts_112_vol_regime_z_lvl_63d},
    "vts_113_vol_regime_z_zscore_63d": {"inputs": ["close"], "func": vts_113_vol_regime_z_zscore_63d},
    "vts_114_vol_regime_z_rank_63d": {"inputs": ["close"], "func": vts_114_vol_regime_z_rank_63d},
    "vts_115_vol_regime_z_lvl_126d": {"inputs": ["close"], "func": vts_115_vol_regime_z_lvl_126d},
    "vts_116_vol_regime_z_zscore_126d": {"inputs": ["close"], "func": vts_116_vol_regime_z_zscore_126d},
    "vts_117_vol_regime_z_rank_126d": {"inputs": ["close"], "func": vts_117_vol_regime_z_rank_126d},
    "vts_118_vol_regime_z_lvl_252d": {"inputs": ["close"], "func": vts_118_vol_regime_z_lvl_252d},
    "vts_119_vol_regime_z_zscore_252d": {"inputs": ["close"], "func": vts_119_vol_regime_z_zscore_252d},
    "vts_120_vol_regime_z_rank_252d": {"inputs": ["close"], "func": vts_120_vol_regime_z_rank_252d},
}
