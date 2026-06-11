"""
114_overnight_intraday_split — Base Features Part 1
Domain: overnight_intraday_split
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

def onid_001_overnight_return_lvl_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_001_overnight_return_lvl_5d
    ECONOMIC RATIONALE: Returns from previous close to current open.
    """
    base = open / close.shift(1) - 1
    return _rolling_mean(base, 5)

def onid_002_overnight_return_zscore_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_002_overnight_return_zscore_5d
    ECONOMIC RATIONALE: Returns from previous close to current open.
    """
    base = open / close.shift(1) - 1
    return _zscore_rolling(base, 5)

def onid_003_overnight_return_rank_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_003_overnight_return_rank_5d
    ECONOMIC RATIONALE: Returns from previous close to current open.
    """
    base = open / close.shift(1) - 1
    return _rank_pct(base, 5)

def onid_004_overnight_return_lvl_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_004_overnight_return_lvl_21d
    ECONOMIC RATIONALE: Returns from previous close to current open.
    """
    base = open / close.shift(1) - 1
    return _rolling_mean(base, 21)

def onid_005_overnight_return_zscore_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_005_overnight_return_zscore_21d
    ECONOMIC RATIONALE: Returns from previous close to current open.
    """
    base = open / close.shift(1) - 1
    return _zscore_rolling(base, 21)

def onid_006_overnight_return_rank_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_006_overnight_return_rank_21d
    ECONOMIC RATIONALE: Returns from previous close to current open.
    """
    base = open / close.shift(1) - 1
    return _rank_pct(base, 21)

def onid_007_overnight_return_lvl_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_007_overnight_return_lvl_63d
    ECONOMIC RATIONALE: Returns from previous close to current open.
    """
    base = open / close.shift(1) - 1
    return _rolling_mean(base, 63)

def onid_008_overnight_return_zscore_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_008_overnight_return_zscore_63d
    ECONOMIC RATIONALE: Returns from previous close to current open.
    """
    base = open / close.shift(1) - 1
    return _zscore_rolling(base, 63)

def onid_009_overnight_return_rank_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_009_overnight_return_rank_63d
    ECONOMIC RATIONALE: Returns from previous close to current open.
    """
    base = open / close.shift(1) - 1
    return _rank_pct(base, 63)

def onid_010_overnight_return_lvl_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_010_overnight_return_lvl_126d
    ECONOMIC RATIONALE: Returns from previous close to current open.
    """
    base = open / close.shift(1) - 1
    return _rolling_mean(base, 126)

def onid_011_overnight_return_zscore_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_011_overnight_return_zscore_126d
    ECONOMIC RATIONALE: Returns from previous close to current open.
    """
    base = open / close.shift(1) - 1
    return _zscore_rolling(base, 126)

def onid_012_overnight_return_rank_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_012_overnight_return_rank_126d
    ECONOMIC RATIONALE: Returns from previous close to current open.
    """
    base = open / close.shift(1) - 1
    return _rank_pct(base, 126)

def onid_013_overnight_return_lvl_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_013_overnight_return_lvl_252d
    ECONOMIC RATIONALE: Returns from previous close to current open.
    """
    base = open / close.shift(1) - 1
    return _rolling_mean(base, 252)

def onid_014_overnight_return_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_014_overnight_return_zscore_252d
    ECONOMIC RATIONALE: Returns from previous close to current open.
    """
    base = open / close.shift(1) - 1
    return _zscore_rolling(base, 252)

def onid_015_overnight_return_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_015_overnight_return_rank_252d
    ECONOMIC RATIONALE: Returns from previous close to current open.
    """
    base = open / close.shift(1) - 1
    return _rank_pct(base, 252)

def onid_016_intraday_return_lvl_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_016_intraday_return_lvl_5d
    ECONOMIC RATIONALE: Returns from current open to current close.
    """
    base = close / open - 1
    return _rolling_mean(base, 5)

def onid_017_intraday_return_zscore_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_017_intraday_return_zscore_5d
    ECONOMIC RATIONALE: Returns from current open to current close.
    """
    base = close / open - 1
    return _zscore_rolling(base, 5)

def onid_018_intraday_return_rank_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_018_intraday_return_rank_5d
    ECONOMIC RATIONALE: Returns from current open to current close.
    """
    base = close / open - 1
    return _rank_pct(base, 5)

def onid_019_intraday_return_lvl_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_019_intraday_return_lvl_21d
    ECONOMIC RATIONALE: Returns from current open to current close.
    """
    base = close / open - 1
    return _rolling_mean(base, 21)

def onid_020_intraday_return_zscore_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_020_intraday_return_zscore_21d
    ECONOMIC RATIONALE: Returns from current open to current close.
    """
    base = close / open - 1
    return _zscore_rolling(base, 21)

def onid_021_intraday_return_rank_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_021_intraday_return_rank_21d
    ECONOMIC RATIONALE: Returns from current open to current close.
    """
    base = close / open - 1
    return _rank_pct(base, 21)

def onid_022_intraday_return_lvl_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_022_intraday_return_lvl_63d
    ECONOMIC RATIONALE: Returns from current open to current close.
    """
    base = close / open - 1
    return _rolling_mean(base, 63)

def onid_023_intraday_return_zscore_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_023_intraday_return_zscore_63d
    ECONOMIC RATIONALE: Returns from current open to current close.
    """
    base = close / open - 1
    return _zscore_rolling(base, 63)

def onid_024_intraday_return_rank_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_024_intraday_return_rank_63d
    ECONOMIC RATIONALE: Returns from current open to current close.
    """
    base = close / open - 1
    return _rank_pct(base, 63)

def onid_025_intraday_return_lvl_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_025_intraday_return_lvl_126d
    ECONOMIC RATIONALE: Returns from current open to current close.
    """
    base = close / open - 1
    return _rolling_mean(base, 126)

def onid_026_intraday_return_zscore_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_026_intraday_return_zscore_126d
    ECONOMIC RATIONALE: Returns from current open to current close.
    """
    base = close / open - 1
    return _zscore_rolling(base, 126)

def onid_027_intraday_return_rank_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_027_intraday_return_rank_126d
    ECONOMIC RATIONALE: Returns from current open to current close.
    """
    base = close / open - 1
    return _rank_pct(base, 126)

def onid_028_intraday_return_lvl_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_028_intraday_return_lvl_252d
    ECONOMIC RATIONALE: Returns from current open to current close.
    """
    base = close / open - 1
    return _rolling_mean(base, 252)

def onid_029_intraday_return_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_029_intraday_return_zscore_252d
    ECONOMIC RATIONALE: Returns from current open to current close.
    """
    base = close / open - 1
    return _zscore_rolling(base, 252)

def onid_030_intraday_return_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_030_intraday_return_rank_252d
    ECONOMIC RATIONALE: Returns from current open to current close.
    """
    base = close / open - 1
    return _rank_pct(base, 252)

def onid_031_on_id_divergence_lvl_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_031_on_id_divergence_lvl_5d
    ECONOMIC RATIONALE: Divergence between overnight and intraday performance.
    """
    base = (open / close.shift(1) - 1) - (close / open - 1)
    return _rolling_mean(base, 5)

def onid_032_on_id_divergence_zscore_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_032_on_id_divergence_zscore_5d
    ECONOMIC RATIONALE: Divergence between overnight and intraday performance.
    """
    base = (open / close.shift(1) - 1) - (close / open - 1)
    return _zscore_rolling(base, 5)

def onid_033_on_id_divergence_rank_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_033_on_id_divergence_rank_5d
    ECONOMIC RATIONALE: Divergence between overnight and intraday performance.
    """
    base = (open / close.shift(1) - 1) - (close / open - 1)
    return _rank_pct(base, 5)

def onid_034_on_id_divergence_lvl_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_034_on_id_divergence_lvl_21d
    ECONOMIC RATIONALE: Divergence between overnight and intraday performance.
    """
    base = (open / close.shift(1) - 1) - (close / open - 1)
    return _rolling_mean(base, 21)

def onid_035_on_id_divergence_zscore_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_035_on_id_divergence_zscore_21d
    ECONOMIC RATIONALE: Divergence between overnight and intraday performance.
    """
    base = (open / close.shift(1) - 1) - (close / open - 1)
    return _zscore_rolling(base, 21)

def onid_036_on_id_divergence_rank_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_036_on_id_divergence_rank_21d
    ECONOMIC RATIONALE: Divergence between overnight and intraday performance.
    """
    base = (open / close.shift(1) - 1) - (close / open - 1)
    return _rank_pct(base, 21)

def onid_037_on_id_divergence_lvl_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_037_on_id_divergence_lvl_63d
    ECONOMIC RATIONALE: Divergence between overnight and intraday performance.
    """
    base = (open / close.shift(1) - 1) - (close / open - 1)
    return _rolling_mean(base, 63)

def onid_038_on_id_divergence_zscore_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_038_on_id_divergence_zscore_63d
    ECONOMIC RATIONALE: Divergence between overnight and intraday performance.
    """
    base = (open / close.shift(1) - 1) - (close / open - 1)
    return _zscore_rolling(base, 63)

def onid_039_on_id_divergence_rank_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_039_on_id_divergence_rank_63d
    ECONOMIC RATIONALE: Divergence between overnight and intraday performance.
    """
    base = (open / close.shift(1) - 1) - (close / open - 1)
    return _rank_pct(base, 63)

def onid_040_on_id_divergence_lvl_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_040_on_id_divergence_lvl_126d
    ECONOMIC RATIONALE: Divergence between overnight and intraday performance.
    """
    base = (open / close.shift(1) - 1) - (close / open - 1)
    return _rolling_mean(base, 126)

def onid_041_on_id_divergence_zscore_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_041_on_id_divergence_zscore_126d
    ECONOMIC RATIONALE: Divergence between overnight and intraday performance.
    """
    base = (open / close.shift(1) - 1) - (close / open - 1)
    return _zscore_rolling(base, 126)

def onid_042_on_id_divergence_rank_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_042_on_id_divergence_rank_126d
    ECONOMIC RATIONALE: Divergence between overnight and intraday performance.
    """
    base = (open / close.shift(1) - 1) - (close / open - 1)
    return _rank_pct(base, 126)

def onid_043_on_id_divergence_lvl_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_043_on_id_divergence_lvl_252d
    ECONOMIC RATIONALE: Divergence between overnight and intraday performance.
    """
    base = (open / close.shift(1) - 1) - (close / open - 1)
    return _rolling_mean(base, 252)

def onid_044_on_id_divergence_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_044_on_id_divergence_zscore_252d
    ECONOMIC RATIONALE: Divergence between overnight and intraday performance.
    """
    base = (open / close.shift(1) - 1) - (close / open - 1)
    return _zscore_rolling(base, 252)

def onid_045_on_id_divergence_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_045_on_id_divergence_rank_252d
    ECONOMIC RATIONALE: Divergence between overnight and intraday performance.
    """
    base = (open / close.shift(1) - 1) - (close / open - 1)
    return _rank_pct(base, 252)

def onid_046_overnight_vol_lvl_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_046_overnight_vol_lvl_5d
    ECONOMIC RATIONALE: Volatility of overnight returns.
    """
    base = (open / close.shift(1) - 1).rolling(21).std()
    return _rolling_mean(base, 5)

def onid_047_overnight_vol_zscore_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_047_overnight_vol_zscore_5d
    ECONOMIC RATIONALE: Volatility of overnight returns.
    """
    base = (open / close.shift(1) - 1).rolling(21).std()
    return _zscore_rolling(base, 5)

def onid_048_overnight_vol_rank_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_048_overnight_vol_rank_5d
    ECONOMIC RATIONALE: Volatility of overnight returns.
    """
    base = (open / close.shift(1) - 1).rolling(21).std()
    return _rank_pct(base, 5)

def onid_049_overnight_vol_lvl_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_049_overnight_vol_lvl_21d
    ECONOMIC RATIONALE: Volatility of overnight returns.
    """
    base = (open / close.shift(1) - 1).rolling(21).std()
    return _rolling_mean(base, 21)

def onid_050_overnight_vol_zscore_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_050_overnight_vol_zscore_21d
    ECONOMIC RATIONALE: Volatility of overnight returns.
    """
    base = (open / close.shift(1) - 1).rolling(21).std()
    return _zscore_rolling(base, 21)

def onid_051_overnight_vol_rank_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_051_overnight_vol_rank_21d
    ECONOMIC RATIONALE: Volatility of overnight returns.
    """
    base = (open / close.shift(1) - 1).rolling(21).std()
    return _rank_pct(base, 21)

def onid_052_overnight_vol_lvl_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_052_overnight_vol_lvl_63d
    ECONOMIC RATIONALE: Volatility of overnight returns.
    """
    base = (open / close.shift(1) - 1).rolling(21).std()
    return _rolling_mean(base, 63)

def onid_053_overnight_vol_zscore_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_053_overnight_vol_zscore_63d
    ECONOMIC RATIONALE: Volatility of overnight returns.
    """
    base = (open / close.shift(1) - 1).rolling(21).std()
    return _zscore_rolling(base, 63)

def onid_054_overnight_vol_rank_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_054_overnight_vol_rank_63d
    ECONOMIC RATIONALE: Volatility of overnight returns.
    """
    base = (open / close.shift(1) - 1).rolling(21).std()
    return _rank_pct(base, 63)

def onid_055_overnight_vol_lvl_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_055_overnight_vol_lvl_126d
    ECONOMIC RATIONALE: Volatility of overnight returns.
    """
    base = (open / close.shift(1) - 1).rolling(21).std()
    return _rolling_mean(base, 126)

def onid_056_overnight_vol_zscore_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_056_overnight_vol_zscore_126d
    ECONOMIC RATIONALE: Volatility of overnight returns.
    """
    base = (open / close.shift(1) - 1).rolling(21).std()
    return _zscore_rolling(base, 126)

def onid_057_overnight_vol_rank_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_057_overnight_vol_rank_126d
    ECONOMIC RATIONALE: Volatility of overnight returns.
    """
    base = (open / close.shift(1) - 1).rolling(21).std()
    return _rank_pct(base, 126)

def onid_058_overnight_vol_lvl_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_058_overnight_vol_lvl_252d
    ECONOMIC RATIONALE: Volatility of overnight returns.
    """
    base = (open / close.shift(1) - 1).rolling(21).std()
    return _rolling_mean(base, 252)

def onid_059_overnight_vol_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_059_overnight_vol_zscore_252d
    ECONOMIC RATIONALE: Volatility of overnight returns.
    """
    base = (open / close.shift(1) - 1).rolling(21).std()
    return _zscore_rolling(base, 252)

def onid_060_overnight_vol_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_060_overnight_vol_rank_252d
    ECONOMIC RATIONALE: Volatility of overnight returns.
    """
    base = (open / close.shift(1) - 1).rolling(21).std()
    return _rank_pct(base, 252)

def onid_061_intraday_vol_lvl_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_061_intraday_vol_lvl_5d
    ECONOMIC RATIONALE: Volatility of intraday returns.
    """
    base = (close / open - 1).rolling(21).std()
    return _rolling_mean(base, 5)

def onid_062_intraday_vol_zscore_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_062_intraday_vol_zscore_5d
    ECONOMIC RATIONALE: Volatility of intraday returns.
    """
    base = (close / open - 1).rolling(21).std()
    return _zscore_rolling(base, 5)

def onid_063_intraday_vol_rank_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_063_intraday_vol_rank_5d
    ECONOMIC RATIONALE: Volatility of intraday returns.
    """
    base = (close / open - 1).rolling(21).std()
    return _rank_pct(base, 5)

def onid_064_intraday_vol_lvl_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_064_intraday_vol_lvl_21d
    ECONOMIC RATIONALE: Volatility of intraday returns.
    """
    base = (close / open - 1).rolling(21).std()
    return _rolling_mean(base, 21)

def onid_065_intraday_vol_zscore_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_065_intraday_vol_zscore_21d
    ECONOMIC RATIONALE: Volatility of intraday returns.
    """
    base = (close / open - 1).rolling(21).std()
    return _zscore_rolling(base, 21)

def onid_066_intraday_vol_rank_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_066_intraday_vol_rank_21d
    ECONOMIC RATIONALE: Volatility of intraday returns.
    """
    base = (close / open - 1).rolling(21).std()
    return _rank_pct(base, 21)

def onid_067_intraday_vol_lvl_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_067_intraday_vol_lvl_63d
    ECONOMIC RATIONALE: Volatility of intraday returns.
    """
    base = (close / open - 1).rolling(21).std()
    return _rolling_mean(base, 63)

def onid_068_intraday_vol_zscore_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_068_intraday_vol_zscore_63d
    ECONOMIC RATIONALE: Volatility of intraday returns.
    """
    base = (close / open - 1).rolling(21).std()
    return _zscore_rolling(base, 63)

def onid_069_intraday_vol_rank_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_069_intraday_vol_rank_63d
    ECONOMIC RATIONALE: Volatility of intraday returns.
    """
    base = (close / open - 1).rolling(21).std()
    return _rank_pct(base, 63)

def onid_070_intraday_vol_lvl_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_070_intraday_vol_lvl_126d
    ECONOMIC RATIONALE: Volatility of intraday returns.
    """
    base = (close / open - 1).rolling(21).std()
    return _rolling_mean(base, 126)

def onid_071_intraday_vol_zscore_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_071_intraday_vol_zscore_126d
    ECONOMIC RATIONALE: Volatility of intraday returns.
    """
    base = (close / open - 1).rolling(21).std()
    return _zscore_rolling(base, 126)

def onid_072_intraday_vol_rank_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_072_intraday_vol_rank_126d
    ECONOMIC RATIONALE: Volatility of intraday returns.
    """
    base = (close / open - 1).rolling(21).std()
    return _rank_pct(base, 126)

def onid_073_intraday_vol_lvl_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_073_intraday_vol_lvl_252d
    ECONOMIC RATIONALE: Volatility of intraday returns.
    """
    base = (close / open - 1).rolling(21).std()
    return _rolling_mean(base, 252)

def onid_074_intraday_vol_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_074_intraday_vol_zscore_252d
    ECONOMIC RATIONALE: Volatility of intraday returns.
    """
    base = (close / open - 1).rolling(21).std()
    return _zscore_rolling(base, 252)

def onid_075_intraday_vol_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_075_intraday_vol_rank_252d
    ECONOMIC RATIONALE: Volatility of intraday returns.
    """
    base = (close / open - 1).rolling(21).std()
    return _rank_pct(base, 252)

def onid_076_on_id_vol_ratio_lvl_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_076_on_id_vol_ratio_lvl_5d
    ECONOMIC RATIONALE: Ratio of overnight to intraday volatility.
    """
    base = ((open / close.shift(1) - 1).rolling(21).std()) / ((close / open - 1).rolling(21).std()).replace(0, 1e-9)
    return _rolling_mean(base, 5)

def onid_077_on_id_vol_ratio_zscore_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_077_on_id_vol_ratio_zscore_5d
    ECONOMIC RATIONALE: Ratio of overnight to intraday volatility.
    """
    base = ((open / close.shift(1) - 1).rolling(21).std()) / ((close / open - 1).rolling(21).std()).replace(0, 1e-9)
    return _zscore_rolling(base, 5)

def onid_078_on_id_vol_ratio_rank_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_078_on_id_vol_ratio_rank_5d
    ECONOMIC RATIONALE: Ratio of overnight to intraday volatility.
    """
    base = ((open / close.shift(1) - 1).rolling(21).std()) / ((close / open - 1).rolling(21).std()).replace(0, 1e-9)
    return _rank_pct(base, 5)

def onid_079_on_id_vol_ratio_lvl_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_079_on_id_vol_ratio_lvl_21d
    ECONOMIC RATIONALE: Ratio of overnight to intraday volatility.
    """
    base = ((open / close.shift(1) - 1).rolling(21).std()) / ((close / open - 1).rolling(21).std()).replace(0, 1e-9)
    return _rolling_mean(base, 21)

def onid_080_on_id_vol_ratio_zscore_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_080_on_id_vol_ratio_zscore_21d
    ECONOMIC RATIONALE: Ratio of overnight to intraday volatility.
    """
    base = ((open / close.shift(1) - 1).rolling(21).std()) / ((close / open - 1).rolling(21).std()).replace(0, 1e-9)
    return _zscore_rolling(base, 21)

def onid_081_on_id_vol_ratio_rank_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_081_on_id_vol_ratio_rank_21d
    ECONOMIC RATIONALE: Ratio of overnight to intraday volatility.
    """
    base = ((open / close.shift(1) - 1).rolling(21).std()) / ((close / open - 1).rolling(21).std()).replace(0, 1e-9)
    return _rank_pct(base, 21)

def onid_082_on_id_vol_ratio_lvl_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_082_on_id_vol_ratio_lvl_63d
    ECONOMIC RATIONALE: Ratio of overnight to intraday volatility.
    """
    base = ((open / close.shift(1) - 1).rolling(21).std()) / ((close / open - 1).rolling(21).std()).replace(0, 1e-9)
    return _rolling_mean(base, 63)

def onid_083_on_id_vol_ratio_zscore_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_083_on_id_vol_ratio_zscore_63d
    ECONOMIC RATIONALE: Ratio of overnight to intraday volatility.
    """
    base = ((open / close.shift(1) - 1).rolling(21).std()) / ((close / open - 1).rolling(21).std()).replace(0, 1e-9)
    return _zscore_rolling(base, 63)

def onid_084_on_id_vol_ratio_rank_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_084_on_id_vol_ratio_rank_63d
    ECONOMIC RATIONALE: Ratio of overnight to intraday volatility.
    """
    base = ((open / close.shift(1) - 1).rolling(21).std()) / ((close / open - 1).rolling(21).std()).replace(0, 1e-9)
    return _rank_pct(base, 63)

def onid_085_on_id_vol_ratio_lvl_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_085_on_id_vol_ratio_lvl_126d
    ECONOMIC RATIONALE: Ratio of overnight to intraday volatility.
    """
    base = ((open / close.shift(1) - 1).rolling(21).std()) / ((close / open - 1).rolling(21).std()).replace(0, 1e-9)
    return _rolling_mean(base, 126)

def onid_086_on_id_vol_ratio_zscore_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_086_on_id_vol_ratio_zscore_126d
    ECONOMIC RATIONALE: Ratio of overnight to intraday volatility.
    """
    base = ((open / close.shift(1) - 1).rolling(21).std()) / ((close / open - 1).rolling(21).std()).replace(0, 1e-9)
    return _zscore_rolling(base, 126)

def onid_087_on_id_vol_ratio_rank_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_087_on_id_vol_ratio_rank_126d
    ECONOMIC RATIONALE: Ratio of overnight to intraday volatility.
    """
    base = ((open / close.shift(1) - 1).rolling(21).std()) / ((close / open - 1).rolling(21).std()).replace(0, 1e-9)
    return _rank_pct(base, 126)

def onid_088_on_id_vol_ratio_lvl_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_088_on_id_vol_ratio_lvl_252d
    ECONOMIC RATIONALE: Ratio of overnight to intraday volatility.
    """
    base = ((open / close.shift(1) - 1).rolling(21).std()) / ((close / open - 1).rolling(21).std()).replace(0, 1e-9)
    return _rolling_mean(base, 252)

def onid_089_on_id_vol_ratio_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_089_on_id_vol_ratio_zscore_252d
    ECONOMIC RATIONALE: Ratio of overnight to intraday volatility.
    """
    base = ((open / close.shift(1) - 1).rolling(21).std()) / ((close / open - 1).rolling(21).std()).replace(0, 1e-9)
    return _zscore_rolling(base, 252)

def onid_090_on_id_vol_ratio_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_090_on_id_vol_ratio_rank_252d
    ECONOMIC RATIONALE: Ratio of overnight to intraday volatility.
    """
    base = ((open / close.shift(1) - 1).rolling(21).std()) / ((close / open - 1).rolling(21).std()).replace(0, 1e-9)
    return _rank_pct(base, 252)

def onid_091_overnight_bias_lvl_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_091_overnight_bias_lvl_5d
    ECONOMIC RATIONALE: Cumulative overnight return bias.
    """
    base = (open / close.shift(1) - 1).rolling(63).sum()
    return _rolling_mean(base, 5)

def onid_092_overnight_bias_zscore_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_092_overnight_bias_zscore_5d
    ECONOMIC RATIONALE: Cumulative overnight return bias.
    """
    base = (open / close.shift(1) - 1).rolling(63).sum()
    return _zscore_rolling(base, 5)

def onid_093_overnight_bias_rank_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_093_overnight_bias_rank_5d
    ECONOMIC RATIONALE: Cumulative overnight return bias.
    """
    base = (open / close.shift(1) - 1).rolling(63).sum()
    return _rank_pct(base, 5)

def onid_094_overnight_bias_lvl_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_094_overnight_bias_lvl_21d
    ECONOMIC RATIONALE: Cumulative overnight return bias.
    """
    base = (open / close.shift(1) - 1).rolling(63).sum()
    return _rolling_mean(base, 21)

def onid_095_overnight_bias_zscore_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_095_overnight_bias_zscore_21d
    ECONOMIC RATIONALE: Cumulative overnight return bias.
    """
    base = (open / close.shift(1) - 1).rolling(63).sum()
    return _zscore_rolling(base, 21)

def onid_096_overnight_bias_rank_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_096_overnight_bias_rank_21d
    ECONOMIC RATIONALE: Cumulative overnight return bias.
    """
    base = (open / close.shift(1) - 1).rolling(63).sum()
    return _rank_pct(base, 21)

def onid_097_overnight_bias_lvl_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_097_overnight_bias_lvl_63d
    ECONOMIC RATIONALE: Cumulative overnight return bias.
    """
    base = (open / close.shift(1) - 1).rolling(63).sum()
    return _rolling_mean(base, 63)

def onid_098_overnight_bias_zscore_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_098_overnight_bias_zscore_63d
    ECONOMIC RATIONALE: Cumulative overnight return bias.
    """
    base = (open / close.shift(1) - 1).rolling(63).sum()
    return _zscore_rolling(base, 63)

def onid_099_overnight_bias_rank_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_099_overnight_bias_rank_63d
    ECONOMIC RATIONALE: Cumulative overnight return bias.
    """
    base = (open / close.shift(1) - 1).rolling(63).sum()
    return _rank_pct(base, 63)

def onid_100_overnight_bias_lvl_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_100_overnight_bias_lvl_126d
    ECONOMIC RATIONALE: Cumulative overnight return bias.
    """
    base = (open / close.shift(1) - 1).rolling(63).sum()
    return _rolling_mean(base, 126)

def onid_101_overnight_bias_zscore_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_101_overnight_bias_zscore_126d
    ECONOMIC RATIONALE: Cumulative overnight return bias.
    """
    base = (open / close.shift(1) - 1).rolling(63).sum()
    return _zscore_rolling(base, 126)

def onid_102_overnight_bias_rank_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_102_overnight_bias_rank_126d
    ECONOMIC RATIONALE: Cumulative overnight return bias.
    """
    base = (open / close.shift(1) - 1).rolling(63).sum()
    return _rank_pct(base, 126)

def onid_103_overnight_bias_lvl_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_103_overnight_bias_lvl_252d
    ECONOMIC RATIONALE: Cumulative overnight return bias.
    """
    base = (open / close.shift(1) - 1).rolling(63).sum()
    return _rolling_mean(base, 252)

def onid_104_overnight_bias_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_104_overnight_bias_zscore_252d
    ECONOMIC RATIONALE: Cumulative overnight return bias.
    """
    base = (open / close.shift(1) - 1).rolling(63).sum()
    return _zscore_rolling(base, 252)

def onid_105_overnight_bias_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_105_overnight_bias_rank_252d
    ECONOMIC RATIONALE: Cumulative overnight return bias.
    """
    base = (open / close.shift(1) - 1).rolling(63).sum()
    return _rank_pct(base, 252)

def onid_106_intraday_bias_lvl_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_106_intraday_bias_lvl_5d
    ECONOMIC RATIONALE: Cumulative intraday return bias.
    """
    base = (close / open - 1).rolling(63).sum()
    return _rolling_mean(base, 5)

def onid_107_intraday_bias_zscore_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_107_intraday_bias_zscore_5d
    ECONOMIC RATIONALE: Cumulative intraday return bias.
    """
    base = (close / open - 1).rolling(63).sum()
    return _zscore_rolling(base, 5)

def onid_108_intraday_bias_rank_5d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_108_intraday_bias_rank_5d
    ECONOMIC RATIONALE: Cumulative intraday return bias.
    """
    base = (close / open - 1).rolling(63).sum()
    return _rank_pct(base, 5)

def onid_109_intraday_bias_lvl_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_109_intraday_bias_lvl_21d
    ECONOMIC RATIONALE: Cumulative intraday return bias.
    """
    base = (close / open - 1).rolling(63).sum()
    return _rolling_mean(base, 21)

def onid_110_intraday_bias_zscore_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_110_intraday_bias_zscore_21d
    ECONOMIC RATIONALE: Cumulative intraday return bias.
    """
    base = (close / open - 1).rolling(63).sum()
    return _zscore_rolling(base, 21)

def onid_111_intraday_bias_rank_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_111_intraday_bias_rank_21d
    ECONOMIC RATIONALE: Cumulative intraday return bias.
    """
    base = (close / open - 1).rolling(63).sum()
    return _rank_pct(base, 21)

def onid_112_intraday_bias_lvl_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_112_intraday_bias_lvl_63d
    ECONOMIC RATIONALE: Cumulative intraday return bias.
    """
    base = (close / open - 1).rolling(63).sum()
    return _rolling_mean(base, 63)

def onid_113_intraday_bias_zscore_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_113_intraday_bias_zscore_63d
    ECONOMIC RATIONALE: Cumulative intraday return bias.
    """
    base = (close / open - 1).rolling(63).sum()
    return _zscore_rolling(base, 63)

def onid_114_intraday_bias_rank_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_114_intraday_bias_rank_63d
    ECONOMIC RATIONALE: Cumulative intraday return bias.
    """
    base = (close / open - 1).rolling(63).sum()
    return _rank_pct(base, 63)

def onid_115_intraday_bias_lvl_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_115_intraday_bias_lvl_126d
    ECONOMIC RATIONALE: Cumulative intraday return bias.
    """
    base = (close / open - 1).rolling(63).sum()
    return _rolling_mean(base, 126)

def onid_116_intraday_bias_zscore_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_116_intraday_bias_zscore_126d
    ECONOMIC RATIONALE: Cumulative intraday return bias.
    """
    base = (close / open - 1).rolling(63).sum()
    return _zscore_rolling(base, 126)

def onid_117_intraday_bias_rank_126d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_117_intraday_bias_rank_126d
    ECONOMIC RATIONALE: Cumulative intraday return bias.
    """
    base = (close / open - 1).rolling(63).sum()
    return _rank_pct(base, 126)

def onid_118_intraday_bias_lvl_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_118_intraday_bias_lvl_252d
    ECONOMIC RATIONALE: Cumulative intraday return bias.
    """
    base = (close / open - 1).rolling(63).sum()
    return _rolling_mean(base, 252)

def onid_119_intraday_bias_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_119_intraday_bias_zscore_252d
    ECONOMIC RATIONALE: Cumulative intraday return bias.
    """
    base = (close / open - 1).rolling(63).sum()
    return _zscore_rolling(base, 252)

def onid_120_intraday_bias_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """
    onid_120_intraday_bias_rank_252d
    ECONOMIC RATIONALE: Cumulative intraday return bias.
    """
    base = (close / open - 1).rolling(63).sum()
    return _rank_pct(base, 252)

# ── Registry ──────────────────────────────────────────────────────────────────
V114_REGISTRY_1 = {
    "onid_001_overnight_return_lvl_5d": {"inputs": ["close", "high", "low", "open"], "func": onid_001_overnight_return_lvl_5d},
    "onid_002_overnight_return_zscore_5d": {"inputs": ["close", "high", "low", "open"], "func": onid_002_overnight_return_zscore_5d},
    "onid_003_overnight_return_rank_5d": {"inputs": ["close", "high", "low", "open"], "func": onid_003_overnight_return_rank_5d},
    "onid_004_overnight_return_lvl_21d": {"inputs": ["close", "high", "low", "open"], "func": onid_004_overnight_return_lvl_21d},
    "onid_005_overnight_return_zscore_21d": {"inputs": ["close", "high", "low", "open"], "func": onid_005_overnight_return_zscore_21d},
    "onid_006_overnight_return_rank_21d": {"inputs": ["close", "high", "low", "open"], "func": onid_006_overnight_return_rank_21d},
    "onid_007_overnight_return_lvl_63d": {"inputs": ["close", "high", "low", "open"], "func": onid_007_overnight_return_lvl_63d},
    "onid_008_overnight_return_zscore_63d": {"inputs": ["close", "high", "low", "open"], "func": onid_008_overnight_return_zscore_63d},
    "onid_009_overnight_return_rank_63d": {"inputs": ["close", "high", "low", "open"], "func": onid_009_overnight_return_rank_63d},
    "onid_010_overnight_return_lvl_126d": {"inputs": ["close", "high", "low", "open"], "func": onid_010_overnight_return_lvl_126d},
    "onid_011_overnight_return_zscore_126d": {"inputs": ["close", "high", "low", "open"], "func": onid_011_overnight_return_zscore_126d},
    "onid_012_overnight_return_rank_126d": {"inputs": ["close", "high", "low", "open"], "func": onid_012_overnight_return_rank_126d},
    "onid_013_overnight_return_lvl_252d": {"inputs": ["close", "high", "low", "open"], "func": onid_013_overnight_return_lvl_252d},
    "onid_014_overnight_return_zscore_252d": {"inputs": ["close", "high", "low", "open"], "func": onid_014_overnight_return_zscore_252d},
    "onid_015_overnight_return_rank_252d": {"inputs": ["close", "high", "low", "open"], "func": onid_015_overnight_return_rank_252d},
    "onid_016_intraday_return_lvl_5d": {"inputs": ["close", "high", "low", "open"], "func": onid_016_intraday_return_lvl_5d},
    "onid_017_intraday_return_zscore_5d": {"inputs": ["close", "high", "low", "open"], "func": onid_017_intraday_return_zscore_5d},
    "onid_018_intraday_return_rank_5d": {"inputs": ["close", "high", "low", "open"], "func": onid_018_intraday_return_rank_5d},
    "onid_019_intraday_return_lvl_21d": {"inputs": ["close", "high", "low", "open"], "func": onid_019_intraday_return_lvl_21d},
    "onid_020_intraday_return_zscore_21d": {"inputs": ["close", "high", "low", "open"], "func": onid_020_intraday_return_zscore_21d},
    "onid_021_intraday_return_rank_21d": {"inputs": ["close", "high", "low", "open"], "func": onid_021_intraday_return_rank_21d},
    "onid_022_intraday_return_lvl_63d": {"inputs": ["close", "high", "low", "open"], "func": onid_022_intraday_return_lvl_63d},
    "onid_023_intraday_return_zscore_63d": {"inputs": ["close", "high", "low", "open"], "func": onid_023_intraday_return_zscore_63d},
    "onid_024_intraday_return_rank_63d": {"inputs": ["close", "high", "low", "open"], "func": onid_024_intraday_return_rank_63d},
    "onid_025_intraday_return_lvl_126d": {"inputs": ["close", "high", "low", "open"], "func": onid_025_intraday_return_lvl_126d},
    "onid_026_intraday_return_zscore_126d": {"inputs": ["close", "high", "low", "open"], "func": onid_026_intraday_return_zscore_126d},
    "onid_027_intraday_return_rank_126d": {"inputs": ["close", "high", "low", "open"], "func": onid_027_intraday_return_rank_126d},
    "onid_028_intraday_return_lvl_252d": {"inputs": ["close", "high", "low", "open"], "func": onid_028_intraday_return_lvl_252d},
    "onid_029_intraday_return_zscore_252d": {"inputs": ["close", "high", "low", "open"], "func": onid_029_intraday_return_zscore_252d},
    "onid_030_intraday_return_rank_252d": {"inputs": ["close", "high", "low", "open"], "func": onid_030_intraday_return_rank_252d},
    "onid_031_on_id_divergence_lvl_5d": {"inputs": ["close", "high", "low", "open"], "func": onid_031_on_id_divergence_lvl_5d},
    "onid_032_on_id_divergence_zscore_5d": {"inputs": ["close", "high", "low", "open"], "func": onid_032_on_id_divergence_zscore_5d},
    "onid_033_on_id_divergence_rank_5d": {"inputs": ["close", "high", "low", "open"], "func": onid_033_on_id_divergence_rank_5d},
    "onid_034_on_id_divergence_lvl_21d": {"inputs": ["close", "high", "low", "open"], "func": onid_034_on_id_divergence_lvl_21d},
    "onid_035_on_id_divergence_zscore_21d": {"inputs": ["close", "high", "low", "open"], "func": onid_035_on_id_divergence_zscore_21d},
    "onid_036_on_id_divergence_rank_21d": {"inputs": ["close", "high", "low", "open"], "func": onid_036_on_id_divergence_rank_21d},
    "onid_037_on_id_divergence_lvl_63d": {"inputs": ["close", "high", "low", "open"], "func": onid_037_on_id_divergence_lvl_63d},
    "onid_038_on_id_divergence_zscore_63d": {"inputs": ["close", "high", "low", "open"], "func": onid_038_on_id_divergence_zscore_63d},
    "onid_039_on_id_divergence_rank_63d": {"inputs": ["close", "high", "low", "open"], "func": onid_039_on_id_divergence_rank_63d},
    "onid_040_on_id_divergence_lvl_126d": {"inputs": ["close", "high", "low", "open"], "func": onid_040_on_id_divergence_lvl_126d},
    "onid_041_on_id_divergence_zscore_126d": {"inputs": ["close", "high", "low", "open"], "func": onid_041_on_id_divergence_zscore_126d},
    "onid_042_on_id_divergence_rank_126d": {"inputs": ["close", "high", "low", "open"], "func": onid_042_on_id_divergence_rank_126d},
    "onid_043_on_id_divergence_lvl_252d": {"inputs": ["close", "high", "low", "open"], "func": onid_043_on_id_divergence_lvl_252d},
    "onid_044_on_id_divergence_zscore_252d": {"inputs": ["close", "high", "low", "open"], "func": onid_044_on_id_divergence_zscore_252d},
    "onid_045_on_id_divergence_rank_252d": {"inputs": ["close", "high", "low", "open"], "func": onid_045_on_id_divergence_rank_252d},
    "onid_046_overnight_vol_lvl_5d": {"inputs": ["close", "high", "low", "open"], "func": onid_046_overnight_vol_lvl_5d},
    "onid_047_overnight_vol_zscore_5d": {"inputs": ["close", "high", "low", "open"], "func": onid_047_overnight_vol_zscore_5d},
    "onid_048_overnight_vol_rank_5d": {"inputs": ["close", "high", "low", "open"], "func": onid_048_overnight_vol_rank_5d},
    "onid_049_overnight_vol_lvl_21d": {"inputs": ["close", "high", "low", "open"], "func": onid_049_overnight_vol_lvl_21d},
    "onid_050_overnight_vol_zscore_21d": {"inputs": ["close", "high", "low", "open"], "func": onid_050_overnight_vol_zscore_21d},
    "onid_051_overnight_vol_rank_21d": {"inputs": ["close", "high", "low", "open"], "func": onid_051_overnight_vol_rank_21d},
    "onid_052_overnight_vol_lvl_63d": {"inputs": ["close", "high", "low", "open"], "func": onid_052_overnight_vol_lvl_63d},
    "onid_053_overnight_vol_zscore_63d": {"inputs": ["close", "high", "low", "open"], "func": onid_053_overnight_vol_zscore_63d},
    "onid_054_overnight_vol_rank_63d": {"inputs": ["close", "high", "low", "open"], "func": onid_054_overnight_vol_rank_63d},
    "onid_055_overnight_vol_lvl_126d": {"inputs": ["close", "high", "low", "open"], "func": onid_055_overnight_vol_lvl_126d},
    "onid_056_overnight_vol_zscore_126d": {"inputs": ["close", "high", "low", "open"], "func": onid_056_overnight_vol_zscore_126d},
    "onid_057_overnight_vol_rank_126d": {"inputs": ["close", "high", "low", "open"], "func": onid_057_overnight_vol_rank_126d},
    "onid_058_overnight_vol_lvl_252d": {"inputs": ["close", "high", "low", "open"], "func": onid_058_overnight_vol_lvl_252d},
    "onid_059_overnight_vol_zscore_252d": {"inputs": ["close", "high", "low", "open"], "func": onid_059_overnight_vol_zscore_252d},
    "onid_060_overnight_vol_rank_252d": {"inputs": ["close", "high", "low", "open"], "func": onid_060_overnight_vol_rank_252d},
    "onid_061_intraday_vol_lvl_5d": {"inputs": ["close", "high", "low", "open"], "func": onid_061_intraday_vol_lvl_5d},
    "onid_062_intraday_vol_zscore_5d": {"inputs": ["close", "high", "low", "open"], "func": onid_062_intraday_vol_zscore_5d},
    "onid_063_intraday_vol_rank_5d": {"inputs": ["close", "high", "low", "open"], "func": onid_063_intraday_vol_rank_5d},
    "onid_064_intraday_vol_lvl_21d": {"inputs": ["close", "high", "low", "open"], "func": onid_064_intraday_vol_lvl_21d},
    "onid_065_intraday_vol_zscore_21d": {"inputs": ["close", "high", "low", "open"], "func": onid_065_intraday_vol_zscore_21d},
    "onid_066_intraday_vol_rank_21d": {"inputs": ["close", "high", "low", "open"], "func": onid_066_intraday_vol_rank_21d},
    "onid_067_intraday_vol_lvl_63d": {"inputs": ["close", "high", "low", "open"], "func": onid_067_intraday_vol_lvl_63d},
    "onid_068_intraday_vol_zscore_63d": {"inputs": ["close", "high", "low", "open"], "func": onid_068_intraday_vol_zscore_63d},
    "onid_069_intraday_vol_rank_63d": {"inputs": ["close", "high", "low", "open"], "func": onid_069_intraday_vol_rank_63d},
    "onid_070_intraday_vol_lvl_126d": {"inputs": ["close", "high", "low", "open"], "func": onid_070_intraday_vol_lvl_126d},
    "onid_071_intraday_vol_zscore_126d": {"inputs": ["close", "high", "low", "open"], "func": onid_071_intraday_vol_zscore_126d},
    "onid_072_intraday_vol_rank_126d": {"inputs": ["close", "high", "low", "open"], "func": onid_072_intraday_vol_rank_126d},
    "onid_073_intraday_vol_lvl_252d": {"inputs": ["close", "high", "low", "open"], "func": onid_073_intraday_vol_lvl_252d},
    "onid_074_intraday_vol_zscore_252d": {"inputs": ["close", "high", "low", "open"], "func": onid_074_intraday_vol_zscore_252d},
    "onid_075_intraday_vol_rank_252d": {"inputs": ["close", "high", "low", "open"], "func": onid_075_intraday_vol_rank_252d},
    "onid_076_on_id_vol_ratio_lvl_5d": {"inputs": ["close", "high", "low", "open"], "func": onid_076_on_id_vol_ratio_lvl_5d},
    "onid_077_on_id_vol_ratio_zscore_5d": {"inputs": ["close", "high", "low", "open"], "func": onid_077_on_id_vol_ratio_zscore_5d},
    "onid_078_on_id_vol_ratio_rank_5d": {"inputs": ["close", "high", "low", "open"], "func": onid_078_on_id_vol_ratio_rank_5d},
    "onid_079_on_id_vol_ratio_lvl_21d": {"inputs": ["close", "high", "low", "open"], "func": onid_079_on_id_vol_ratio_lvl_21d},
    "onid_080_on_id_vol_ratio_zscore_21d": {"inputs": ["close", "high", "low", "open"], "func": onid_080_on_id_vol_ratio_zscore_21d},
    "onid_081_on_id_vol_ratio_rank_21d": {"inputs": ["close", "high", "low", "open"], "func": onid_081_on_id_vol_ratio_rank_21d},
    "onid_082_on_id_vol_ratio_lvl_63d": {"inputs": ["close", "high", "low", "open"], "func": onid_082_on_id_vol_ratio_lvl_63d},
    "onid_083_on_id_vol_ratio_zscore_63d": {"inputs": ["close", "high", "low", "open"], "func": onid_083_on_id_vol_ratio_zscore_63d},
    "onid_084_on_id_vol_ratio_rank_63d": {"inputs": ["close", "high", "low", "open"], "func": onid_084_on_id_vol_ratio_rank_63d},
    "onid_085_on_id_vol_ratio_lvl_126d": {"inputs": ["close", "high", "low", "open"], "func": onid_085_on_id_vol_ratio_lvl_126d},
    "onid_086_on_id_vol_ratio_zscore_126d": {"inputs": ["close", "high", "low", "open"], "func": onid_086_on_id_vol_ratio_zscore_126d},
    "onid_087_on_id_vol_ratio_rank_126d": {"inputs": ["close", "high", "low", "open"], "func": onid_087_on_id_vol_ratio_rank_126d},
    "onid_088_on_id_vol_ratio_lvl_252d": {"inputs": ["close", "high", "low", "open"], "func": onid_088_on_id_vol_ratio_lvl_252d},
    "onid_089_on_id_vol_ratio_zscore_252d": {"inputs": ["close", "high", "low", "open"], "func": onid_089_on_id_vol_ratio_zscore_252d},
    "onid_090_on_id_vol_ratio_rank_252d": {"inputs": ["close", "high", "low", "open"], "func": onid_090_on_id_vol_ratio_rank_252d},
    "onid_091_overnight_bias_lvl_5d": {"inputs": ["close", "high", "low", "open"], "func": onid_091_overnight_bias_lvl_5d},
    "onid_092_overnight_bias_zscore_5d": {"inputs": ["close", "high", "low", "open"], "func": onid_092_overnight_bias_zscore_5d},
    "onid_093_overnight_bias_rank_5d": {"inputs": ["close", "high", "low", "open"], "func": onid_093_overnight_bias_rank_5d},
    "onid_094_overnight_bias_lvl_21d": {"inputs": ["close", "high", "low", "open"], "func": onid_094_overnight_bias_lvl_21d},
    "onid_095_overnight_bias_zscore_21d": {"inputs": ["close", "high", "low", "open"], "func": onid_095_overnight_bias_zscore_21d},
    "onid_096_overnight_bias_rank_21d": {"inputs": ["close", "high", "low", "open"], "func": onid_096_overnight_bias_rank_21d},
    "onid_097_overnight_bias_lvl_63d": {"inputs": ["close", "high", "low", "open"], "func": onid_097_overnight_bias_lvl_63d},
    "onid_098_overnight_bias_zscore_63d": {"inputs": ["close", "high", "low", "open"], "func": onid_098_overnight_bias_zscore_63d},
    "onid_099_overnight_bias_rank_63d": {"inputs": ["close", "high", "low", "open"], "func": onid_099_overnight_bias_rank_63d},
    "onid_100_overnight_bias_lvl_126d": {"inputs": ["close", "high", "low", "open"], "func": onid_100_overnight_bias_lvl_126d},
    "onid_101_overnight_bias_zscore_126d": {"inputs": ["close", "high", "low", "open"], "func": onid_101_overnight_bias_zscore_126d},
    "onid_102_overnight_bias_rank_126d": {"inputs": ["close", "high", "low", "open"], "func": onid_102_overnight_bias_rank_126d},
    "onid_103_overnight_bias_lvl_252d": {"inputs": ["close", "high", "low", "open"], "func": onid_103_overnight_bias_lvl_252d},
    "onid_104_overnight_bias_zscore_252d": {"inputs": ["close", "high", "low", "open"], "func": onid_104_overnight_bias_zscore_252d},
    "onid_105_overnight_bias_rank_252d": {"inputs": ["close", "high", "low", "open"], "func": onid_105_overnight_bias_rank_252d},
    "onid_106_intraday_bias_lvl_5d": {"inputs": ["close", "high", "low", "open"], "func": onid_106_intraday_bias_lvl_5d},
    "onid_107_intraday_bias_zscore_5d": {"inputs": ["close", "high", "low", "open"], "func": onid_107_intraday_bias_zscore_5d},
    "onid_108_intraday_bias_rank_5d": {"inputs": ["close", "high", "low", "open"], "func": onid_108_intraday_bias_rank_5d},
    "onid_109_intraday_bias_lvl_21d": {"inputs": ["close", "high", "low", "open"], "func": onid_109_intraday_bias_lvl_21d},
    "onid_110_intraday_bias_zscore_21d": {"inputs": ["close", "high", "low", "open"], "func": onid_110_intraday_bias_zscore_21d},
    "onid_111_intraday_bias_rank_21d": {"inputs": ["close", "high", "low", "open"], "func": onid_111_intraday_bias_rank_21d},
    "onid_112_intraday_bias_lvl_63d": {"inputs": ["close", "high", "low", "open"], "func": onid_112_intraday_bias_lvl_63d},
    "onid_113_intraday_bias_zscore_63d": {"inputs": ["close", "high", "low", "open"], "func": onid_113_intraday_bias_zscore_63d},
    "onid_114_intraday_bias_rank_63d": {"inputs": ["close", "high", "low", "open"], "func": onid_114_intraday_bias_rank_63d},
    "onid_115_intraday_bias_lvl_126d": {"inputs": ["close", "high", "low", "open"], "func": onid_115_intraday_bias_lvl_126d},
    "onid_116_intraday_bias_zscore_126d": {"inputs": ["close", "high", "low", "open"], "func": onid_116_intraday_bias_zscore_126d},
    "onid_117_intraday_bias_rank_126d": {"inputs": ["close", "high", "low", "open"], "func": onid_117_intraday_bias_rank_126d},
    "onid_118_intraday_bias_lvl_252d": {"inputs": ["close", "high", "low", "open"], "func": onid_118_intraday_bias_lvl_252d},
    "onid_119_intraday_bias_zscore_252d": {"inputs": ["close", "high", "low", "open"], "func": onid_119_intraday_bias_zscore_252d},
    "onid_120_intraday_bias_rank_252d": {"inputs": ["close", "high", "low", "open"], "func": onid_120_intraday_bias_rank_252d},
}
