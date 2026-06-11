"""
109_return_autocorrelation — Base Features Part 1
Domain: return_autocorrelation
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

def raut_001_lag1_autocorr_lvl_5d(close: pd.Series) -> pd.Series:
    """
    raut_001_lag1_autocorr_lvl_5d
    ECONOMIC RATIONALE: 21-day serial correlation of returns.
    """
    base = close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1))
    return _rolling_mean(base, 5)

def raut_002_lag1_autocorr_zscore_5d(close: pd.Series) -> pd.Series:
    """
    raut_002_lag1_autocorr_zscore_5d
    ECONOMIC RATIONALE: 21-day serial correlation of returns.
    """
    base = close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1))
    return _zscore_rolling(base, 5)

def raut_003_lag1_autocorr_rank_5d(close: pd.Series) -> pd.Series:
    """
    raut_003_lag1_autocorr_rank_5d
    ECONOMIC RATIONALE: 21-day serial correlation of returns.
    """
    base = close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1))
    return _rank_pct(base, 5)

def raut_004_lag1_autocorr_lvl_21d(close: pd.Series) -> pd.Series:
    """
    raut_004_lag1_autocorr_lvl_21d
    ECONOMIC RATIONALE: 21-day serial correlation of returns.
    """
    base = close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1))
    return _rolling_mean(base, 21)

def raut_005_lag1_autocorr_zscore_21d(close: pd.Series) -> pd.Series:
    """
    raut_005_lag1_autocorr_zscore_21d
    ECONOMIC RATIONALE: 21-day serial correlation of returns.
    """
    base = close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1))
    return _zscore_rolling(base, 21)

def raut_006_lag1_autocorr_rank_21d(close: pd.Series) -> pd.Series:
    """
    raut_006_lag1_autocorr_rank_21d
    ECONOMIC RATIONALE: 21-day serial correlation of returns.
    """
    base = close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1))
    return _rank_pct(base, 21)

def raut_007_lag1_autocorr_lvl_63d(close: pd.Series) -> pd.Series:
    """
    raut_007_lag1_autocorr_lvl_63d
    ECONOMIC RATIONALE: 21-day serial correlation of returns.
    """
    base = close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1))
    return _rolling_mean(base, 63)

def raut_008_lag1_autocorr_zscore_63d(close: pd.Series) -> pd.Series:
    """
    raut_008_lag1_autocorr_zscore_63d
    ECONOMIC RATIONALE: 21-day serial correlation of returns.
    """
    base = close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1))
    return _zscore_rolling(base, 63)

def raut_009_lag1_autocorr_rank_63d(close: pd.Series) -> pd.Series:
    """
    raut_009_lag1_autocorr_rank_63d
    ECONOMIC RATIONALE: 21-day serial correlation of returns.
    """
    base = close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1))
    return _rank_pct(base, 63)

def raut_010_lag1_autocorr_lvl_126d(close: pd.Series) -> pd.Series:
    """
    raut_010_lag1_autocorr_lvl_126d
    ECONOMIC RATIONALE: 21-day serial correlation of returns.
    """
    base = close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1))
    return _rolling_mean(base, 126)

def raut_011_lag1_autocorr_zscore_126d(close: pd.Series) -> pd.Series:
    """
    raut_011_lag1_autocorr_zscore_126d
    ECONOMIC RATIONALE: 21-day serial correlation of returns.
    """
    base = close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1))
    return _zscore_rolling(base, 126)

def raut_012_lag1_autocorr_rank_126d(close: pd.Series) -> pd.Series:
    """
    raut_012_lag1_autocorr_rank_126d
    ECONOMIC RATIONALE: 21-day serial correlation of returns.
    """
    base = close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1))
    return _rank_pct(base, 126)

def raut_013_lag1_autocorr_lvl_252d(close: pd.Series) -> pd.Series:
    """
    raut_013_lag1_autocorr_lvl_252d
    ECONOMIC RATIONALE: 21-day serial correlation of returns.
    """
    base = close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1))
    return _rolling_mean(base, 252)

def raut_014_lag1_autocorr_zscore_252d(close: pd.Series) -> pd.Series:
    """
    raut_014_lag1_autocorr_zscore_252d
    ECONOMIC RATIONALE: 21-day serial correlation of returns.
    """
    base = close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1))
    return _zscore_rolling(base, 252)

def raut_015_lag1_autocorr_rank_252d(close: pd.Series) -> pd.Series:
    """
    raut_015_lag1_autocorr_rank_252d
    ECONOMIC RATIONALE: 21-day serial correlation of returns.
    """
    base = close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1))
    return _rank_pct(base, 252)

def raut_016_lag5_autocorr_lvl_5d(close: pd.Series) -> pd.Series:
    """
    raut_016_lag5_autocorr_lvl_5d
    ECONOMIC RATIONALE: 63-day correlation with weekly-lagged returns.
    """
    base = close.pct_change(1).rolling(63).apply(lambda x: x.autocorr(5))
    return _rolling_mean(base, 5)

def raut_017_lag5_autocorr_zscore_5d(close: pd.Series) -> pd.Series:
    """
    raut_017_lag5_autocorr_zscore_5d
    ECONOMIC RATIONALE: 63-day correlation with weekly-lagged returns.
    """
    base = close.pct_change(1).rolling(63).apply(lambda x: x.autocorr(5))
    return _zscore_rolling(base, 5)

def raut_018_lag5_autocorr_rank_5d(close: pd.Series) -> pd.Series:
    """
    raut_018_lag5_autocorr_rank_5d
    ECONOMIC RATIONALE: 63-day correlation with weekly-lagged returns.
    """
    base = close.pct_change(1).rolling(63).apply(lambda x: x.autocorr(5))
    return _rank_pct(base, 5)

def raut_019_lag5_autocorr_lvl_21d(close: pd.Series) -> pd.Series:
    """
    raut_019_lag5_autocorr_lvl_21d
    ECONOMIC RATIONALE: 63-day correlation with weekly-lagged returns.
    """
    base = close.pct_change(1).rolling(63).apply(lambda x: x.autocorr(5))
    return _rolling_mean(base, 21)

def raut_020_lag5_autocorr_zscore_21d(close: pd.Series) -> pd.Series:
    """
    raut_020_lag5_autocorr_zscore_21d
    ECONOMIC RATIONALE: 63-day correlation with weekly-lagged returns.
    """
    base = close.pct_change(1).rolling(63).apply(lambda x: x.autocorr(5))
    return _zscore_rolling(base, 21)

def raut_021_lag5_autocorr_rank_21d(close: pd.Series) -> pd.Series:
    """
    raut_021_lag5_autocorr_rank_21d
    ECONOMIC RATIONALE: 63-day correlation with weekly-lagged returns.
    """
    base = close.pct_change(1).rolling(63).apply(lambda x: x.autocorr(5))
    return _rank_pct(base, 21)

def raut_022_lag5_autocorr_lvl_63d(close: pd.Series) -> pd.Series:
    """
    raut_022_lag5_autocorr_lvl_63d
    ECONOMIC RATIONALE: 63-day correlation with weekly-lagged returns.
    """
    base = close.pct_change(1).rolling(63).apply(lambda x: x.autocorr(5))
    return _rolling_mean(base, 63)

def raut_023_lag5_autocorr_zscore_63d(close: pd.Series) -> pd.Series:
    """
    raut_023_lag5_autocorr_zscore_63d
    ECONOMIC RATIONALE: 63-day correlation with weekly-lagged returns.
    """
    base = close.pct_change(1).rolling(63).apply(lambda x: x.autocorr(5))
    return _zscore_rolling(base, 63)

def raut_024_lag5_autocorr_rank_63d(close: pd.Series) -> pd.Series:
    """
    raut_024_lag5_autocorr_rank_63d
    ECONOMIC RATIONALE: 63-day correlation with weekly-lagged returns.
    """
    base = close.pct_change(1).rolling(63).apply(lambda x: x.autocorr(5))
    return _rank_pct(base, 63)

def raut_025_lag5_autocorr_lvl_126d(close: pd.Series) -> pd.Series:
    """
    raut_025_lag5_autocorr_lvl_126d
    ECONOMIC RATIONALE: 63-day correlation with weekly-lagged returns.
    """
    base = close.pct_change(1).rolling(63).apply(lambda x: x.autocorr(5))
    return _rolling_mean(base, 126)

def raut_026_lag5_autocorr_zscore_126d(close: pd.Series) -> pd.Series:
    """
    raut_026_lag5_autocorr_zscore_126d
    ECONOMIC RATIONALE: 63-day correlation with weekly-lagged returns.
    """
    base = close.pct_change(1).rolling(63).apply(lambda x: x.autocorr(5))
    return _zscore_rolling(base, 126)

def raut_027_lag5_autocorr_rank_126d(close: pd.Series) -> pd.Series:
    """
    raut_027_lag5_autocorr_rank_126d
    ECONOMIC RATIONALE: 63-day correlation with weekly-lagged returns.
    """
    base = close.pct_change(1).rolling(63).apply(lambda x: x.autocorr(5))
    return _rank_pct(base, 126)

def raut_028_lag5_autocorr_lvl_252d(close: pd.Series) -> pd.Series:
    """
    raut_028_lag5_autocorr_lvl_252d
    ECONOMIC RATIONALE: 63-day correlation with weekly-lagged returns.
    """
    base = close.pct_change(1).rolling(63).apply(lambda x: x.autocorr(5))
    return _rolling_mean(base, 252)

def raut_029_lag5_autocorr_zscore_252d(close: pd.Series) -> pd.Series:
    """
    raut_029_lag5_autocorr_zscore_252d
    ECONOMIC RATIONALE: 63-day correlation with weekly-lagged returns.
    """
    base = close.pct_change(1).rolling(63).apply(lambda x: x.autocorr(5))
    return _zscore_rolling(base, 252)

def raut_030_lag5_autocorr_rank_252d(close: pd.Series) -> pd.Series:
    """
    raut_030_lag5_autocorr_rank_252d
    ECONOMIC RATIONALE: 63-day correlation with weekly-lagged returns.
    """
    base = close.pct_change(1).rolling(63).apply(lambda x: x.autocorr(5))
    return _rank_pct(base, 252)

def raut_031_autocorr_zscore_lvl_5d(close: pd.Series) -> pd.Series:
    """
    raut_031_autocorr_zscore_lvl_5d
    ECONOMIC RATIONALE: Anomaly in return persistence.
    """
    base = _zscore_rolling(close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)
    return _rolling_mean(base, 5)

def raut_032_autocorr_zscore_zscore_5d(close: pd.Series) -> pd.Series:
    """
    raut_032_autocorr_zscore_zscore_5d
    ECONOMIC RATIONALE: Anomaly in return persistence.
    """
    base = _zscore_rolling(close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)
    return _zscore_rolling(base, 5)

def raut_033_autocorr_zscore_rank_5d(close: pd.Series) -> pd.Series:
    """
    raut_033_autocorr_zscore_rank_5d
    ECONOMIC RATIONALE: Anomaly in return persistence.
    """
    base = _zscore_rolling(close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)
    return _rank_pct(base, 5)

def raut_034_autocorr_zscore_lvl_21d(close: pd.Series) -> pd.Series:
    """
    raut_034_autocorr_zscore_lvl_21d
    ECONOMIC RATIONALE: Anomaly in return persistence.
    """
    base = _zscore_rolling(close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)
    return _rolling_mean(base, 21)

def raut_035_autocorr_zscore_zscore_21d(close: pd.Series) -> pd.Series:
    """
    raut_035_autocorr_zscore_zscore_21d
    ECONOMIC RATIONALE: Anomaly in return persistence.
    """
    base = _zscore_rolling(close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)
    return _zscore_rolling(base, 21)

def raut_036_autocorr_zscore_rank_21d(close: pd.Series) -> pd.Series:
    """
    raut_036_autocorr_zscore_rank_21d
    ECONOMIC RATIONALE: Anomaly in return persistence.
    """
    base = _zscore_rolling(close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)
    return _rank_pct(base, 21)

def raut_037_autocorr_zscore_lvl_63d(close: pd.Series) -> pd.Series:
    """
    raut_037_autocorr_zscore_lvl_63d
    ECONOMIC RATIONALE: Anomaly in return persistence.
    """
    base = _zscore_rolling(close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)
    return _rolling_mean(base, 63)

def raut_038_autocorr_zscore_zscore_63d(close: pd.Series) -> pd.Series:
    """
    raut_038_autocorr_zscore_zscore_63d
    ECONOMIC RATIONALE: Anomaly in return persistence.
    """
    base = _zscore_rolling(close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)
    return _zscore_rolling(base, 63)

def raut_039_autocorr_zscore_rank_63d(close: pd.Series) -> pd.Series:
    """
    raut_039_autocorr_zscore_rank_63d
    ECONOMIC RATIONALE: Anomaly in return persistence.
    """
    base = _zscore_rolling(close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)
    return _rank_pct(base, 63)

def raut_040_autocorr_zscore_lvl_126d(close: pd.Series) -> pd.Series:
    """
    raut_040_autocorr_zscore_lvl_126d
    ECONOMIC RATIONALE: Anomaly in return persistence.
    """
    base = _zscore_rolling(close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)
    return _rolling_mean(base, 126)

def raut_041_autocorr_zscore_zscore_126d(close: pd.Series) -> pd.Series:
    """
    raut_041_autocorr_zscore_zscore_126d
    ECONOMIC RATIONALE: Anomaly in return persistence.
    """
    base = _zscore_rolling(close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)
    return _zscore_rolling(base, 126)

def raut_042_autocorr_zscore_rank_126d(close: pd.Series) -> pd.Series:
    """
    raut_042_autocorr_zscore_rank_126d
    ECONOMIC RATIONALE: Anomaly in return persistence.
    """
    base = _zscore_rolling(close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)
    return _rank_pct(base, 126)

def raut_043_autocorr_zscore_lvl_252d(close: pd.Series) -> pd.Series:
    """
    raut_043_autocorr_zscore_lvl_252d
    ECONOMIC RATIONALE: Anomaly in return persistence.
    """
    base = _zscore_rolling(close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)
    return _rolling_mean(base, 252)

def raut_044_autocorr_zscore_zscore_252d(close: pd.Series) -> pd.Series:
    """
    raut_044_autocorr_zscore_zscore_252d
    ECONOMIC RATIONALE: Anomaly in return persistence.
    """
    base = _zscore_rolling(close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)
    return _zscore_rolling(base, 252)

def raut_045_autocorr_zscore_rank_252d(close: pd.Series) -> pd.Series:
    """
    raut_045_autocorr_zscore_rank_252d
    ECONOMIC RATIONALE: Anomaly in return persistence.
    """
    base = _zscore_rolling(close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)), 252)
    return _rank_pct(base, 252)

def raut_046_autocorr_trend_lvl_5d(close: pd.Series) -> pd.Series:
    """
    raut_046_autocorr_trend_lvl_5d
    ECONOMIC RATIONALE: Shift in return persistence trend.
    """
    base = close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(21)
    return _rolling_mean(base, 5)

def raut_047_autocorr_trend_zscore_5d(close: pd.Series) -> pd.Series:
    """
    raut_047_autocorr_trend_zscore_5d
    ECONOMIC RATIONALE: Shift in return persistence trend.
    """
    base = close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(21)
    return _zscore_rolling(base, 5)

def raut_048_autocorr_trend_rank_5d(close: pd.Series) -> pd.Series:
    """
    raut_048_autocorr_trend_rank_5d
    ECONOMIC RATIONALE: Shift in return persistence trend.
    """
    base = close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(21)
    return _rank_pct(base, 5)

def raut_049_autocorr_trend_lvl_21d(close: pd.Series) -> pd.Series:
    """
    raut_049_autocorr_trend_lvl_21d
    ECONOMIC RATIONALE: Shift in return persistence trend.
    """
    base = close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(21)
    return _rolling_mean(base, 21)

def raut_050_autocorr_trend_zscore_21d(close: pd.Series) -> pd.Series:
    """
    raut_050_autocorr_trend_zscore_21d
    ECONOMIC RATIONALE: Shift in return persistence trend.
    """
    base = close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(21)
    return _zscore_rolling(base, 21)

def raut_051_autocorr_trend_rank_21d(close: pd.Series) -> pd.Series:
    """
    raut_051_autocorr_trend_rank_21d
    ECONOMIC RATIONALE: Shift in return persistence trend.
    """
    base = close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(21)
    return _rank_pct(base, 21)

def raut_052_autocorr_trend_lvl_63d(close: pd.Series) -> pd.Series:
    """
    raut_052_autocorr_trend_lvl_63d
    ECONOMIC RATIONALE: Shift in return persistence trend.
    """
    base = close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(21)
    return _rolling_mean(base, 63)

def raut_053_autocorr_trend_zscore_63d(close: pd.Series) -> pd.Series:
    """
    raut_053_autocorr_trend_zscore_63d
    ECONOMIC RATIONALE: Shift in return persistence trend.
    """
    base = close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(21)
    return _zscore_rolling(base, 63)

def raut_054_autocorr_trend_rank_63d(close: pd.Series) -> pd.Series:
    """
    raut_054_autocorr_trend_rank_63d
    ECONOMIC RATIONALE: Shift in return persistence trend.
    """
    base = close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(21)
    return _rank_pct(base, 63)

def raut_055_autocorr_trend_lvl_126d(close: pd.Series) -> pd.Series:
    """
    raut_055_autocorr_trend_lvl_126d
    ECONOMIC RATIONALE: Shift in return persistence trend.
    """
    base = close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(21)
    return _rolling_mean(base, 126)

def raut_056_autocorr_trend_zscore_126d(close: pd.Series) -> pd.Series:
    """
    raut_056_autocorr_trend_zscore_126d
    ECONOMIC RATIONALE: Shift in return persistence trend.
    """
    base = close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(21)
    return _zscore_rolling(base, 126)

def raut_057_autocorr_trend_rank_126d(close: pd.Series) -> pd.Series:
    """
    raut_057_autocorr_trend_rank_126d
    ECONOMIC RATIONALE: Shift in return persistence trend.
    """
    base = close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(21)
    return _rank_pct(base, 126)

def raut_058_autocorr_trend_lvl_252d(close: pd.Series) -> pd.Series:
    """
    raut_058_autocorr_trend_lvl_252d
    ECONOMIC RATIONALE: Shift in return persistence trend.
    """
    base = close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(21)
    return _rolling_mean(base, 252)

def raut_059_autocorr_trend_zscore_252d(close: pd.Series) -> pd.Series:
    """
    raut_059_autocorr_trend_zscore_252d
    ECONOMIC RATIONALE: Shift in return persistence trend.
    """
    base = close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(21)
    return _zscore_rolling(base, 252)

def raut_060_autocorr_trend_rank_252d(close: pd.Series) -> pd.Series:
    """
    raut_060_autocorr_trend_rank_252d
    ECONOMIC RATIONALE: Shift in return persistence trend.
    """
    base = close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).diff(21)
    return _rank_pct(base, 252)

def raut_061_negative_autocorr_flag_lvl_5d(close: pd.Series) -> pd.Series:
    """
    raut_061_negative_autocorr_flag_lvl_5d
    ECONOMIC RATIONALE: Indication of mean-reverting regime.
    """
    base = (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) < -0.1).astype(float)
    return _rolling_mean(base, 5)

def raut_062_negative_autocorr_flag_zscore_5d(close: pd.Series) -> pd.Series:
    """
    raut_062_negative_autocorr_flag_zscore_5d
    ECONOMIC RATIONALE: Indication of mean-reverting regime.
    """
    base = (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) < -0.1).astype(float)
    return _zscore_rolling(base, 5)

def raut_063_negative_autocorr_flag_rank_5d(close: pd.Series) -> pd.Series:
    """
    raut_063_negative_autocorr_flag_rank_5d
    ECONOMIC RATIONALE: Indication of mean-reverting regime.
    """
    base = (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) < -0.1).astype(float)
    return _rank_pct(base, 5)

def raut_064_negative_autocorr_flag_lvl_21d(close: pd.Series) -> pd.Series:
    """
    raut_064_negative_autocorr_flag_lvl_21d
    ECONOMIC RATIONALE: Indication of mean-reverting regime.
    """
    base = (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) < -0.1).astype(float)
    return _rolling_mean(base, 21)

def raut_065_negative_autocorr_flag_zscore_21d(close: pd.Series) -> pd.Series:
    """
    raut_065_negative_autocorr_flag_zscore_21d
    ECONOMIC RATIONALE: Indication of mean-reverting regime.
    """
    base = (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) < -0.1).astype(float)
    return _zscore_rolling(base, 21)

def raut_066_negative_autocorr_flag_rank_21d(close: pd.Series) -> pd.Series:
    """
    raut_066_negative_autocorr_flag_rank_21d
    ECONOMIC RATIONALE: Indication of mean-reverting regime.
    """
    base = (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) < -0.1).astype(float)
    return _rank_pct(base, 21)

def raut_067_negative_autocorr_flag_lvl_63d(close: pd.Series) -> pd.Series:
    """
    raut_067_negative_autocorr_flag_lvl_63d
    ECONOMIC RATIONALE: Indication of mean-reverting regime.
    """
    base = (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) < -0.1).astype(float)
    return _rolling_mean(base, 63)

def raut_068_negative_autocorr_flag_zscore_63d(close: pd.Series) -> pd.Series:
    """
    raut_068_negative_autocorr_flag_zscore_63d
    ECONOMIC RATIONALE: Indication of mean-reverting regime.
    """
    base = (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) < -0.1).astype(float)
    return _zscore_rolling(base, 63)

def raut_069_negative_autocorr_flag_rank_63d(close: pd.Series) -> pd.Series:
    """
    raut_069_negative_autocorr_flag_rank_63d
    ECONOMIC RATIONALE: Indication of mean-reverting regime.
    """
    base = (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) < -0.1).astype(float)
    return _rank_pct(base, 63)

def raut_070_negative_autocorr_flag_lvl_126d(close: pd.Series) -> pd.Series:
    """
    raut_070_negative_autocorr_flag_lvl_126d
    ECONOMIC RATIONALE: Indication of mean-reverting regime.
    """
    base = (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) < -0.1).astype(float)
    return _rolling_mean(base, 126)

def raut_071_negative_autocorr_flag_zscore_126d(close: pd.Series) -> pd.Series:
    """
    raut_071_negative_autocorr_flag_zscore_126d
    ECONOMIC RATIONALE: Indication of mean-reverting regime.
    """
    base = (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) < -0.1).astype(float)
    return _zscore_rolling(base, 126)

def raut_072_negative_autocorr_flag_rank_126d(close: pd.Series) -> pd.Series:
    """
    raut_072_negative_autocorr_flag_rank_126d
    ECONOMIC RATIONALE: Indication of mean-reverting regime.
    """
    base = (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) < -0.1).astype(float)
    return _rank_pct(base, 126)

def raut_073_negative_autocorr_flag_lvl_252d(close: pd.Series) -> pd.Series:
    """
    raut_073_negative_autocorr_flag_lvl_252d
    ECONOMIC RATIONALE: Indication of mean-reverting regime.
    """
    base = (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) < -0.1).astype(float)
    return _rolling_mean(base, 252)

def raut_074_negative_autocorr_flag_zscore_252d(close: pd.Series) -> pd.Series:
    """
    raut_074_negative_autocorr_flag_zscore_252d
    ECONOMIC RATIONALE: Indication of mean-reverting regime.
    """
    base = (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) < -0.1).astype(float)
    return _zscore_rolling(base, 252)

def raut_075_negative_autocorr_flag_rank_252d(close: pd.Series) -> pd.Series:
    """
    raut_075_negative_autocorr_flag_rank_252d
    ECONOMIC RATIONALE: Indication of mean-reverting regime.
    """
    base = (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) < -0.1).astype(float)
    return _rank_pct(base, 252)

def raut_076_positive_autocorr_flag_lvl_5d(close: pd.Series) -> pd.Series:
    """
    raut_076_positive_autocorr_flag_lvl_5d
    ECONOMIC RATIONALE: Indication of trending regime.
    """
    base = (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) > 0.1).astype(float)
    return _rolling_mean(base, 5)

def raut_077_positive_autocorr_flag_zscore_5d(close: pd.Series) -> pd.Series:
    """
    raut_077_positive_autocorr_flag_zscore_5d
    ECONOMIC RATIONALE: Indication of trending regime.
    """
    base = (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) > 0.1).astype(float)
    return _zscore_rolling(base, 5)

def raut_078_positive_autocorr_flag_rank_5d(close: pd.Series) -> pd.Series:
    """
    raut_078_positive_autocorr_flag_rank_5d
    ECONOMIC RATIONALE: Indication of trending regime.
    """
    base = (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) > 0.1).astype(float)
    return _rank_pct(base, 5)

def raut_079_positive_autocorr_flag_lvl_21d(close: pd.Series) -> pd.Series:
    """
    raut_079_positive_autocorr_flag_lvl_21d
    ECONOMIC RATIONALE: Indication of trending regime.
    """
    base = (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) > 0.1).astype(float)
    return _rolling_mean(base, 21)

def raut_080_positive_autocorr_flag_zscore_21d(close: pd.Series) -> pd.Series:
    """
    raut_080_positive_autocorr_flag_zscore_21d
    ECONOMIC RATIONALE: Indication of trending regime.
    """
    base = (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) > 0.1).astype(float)
    return _zscore_rolling(base, 21)

def raut_081_positive_autocorr_flag_rank_21d(close: pd.Series) -> pd.Series:
    """
    raut_081_positive_autocorr_flag_rank_21d
    ECONOMIC RATIONALE: Indication of trending regime.
    """
    base = (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) > 0.1).astype(float)
    return _rank_pct(base, 21)

def raut_082_positive_autocorr_flag_lvl_63d(close: pd.Series) -> pd.Series:
    """
    raut_082_positive_autocorr_flag_lvl_63d
    ECONOMIC RATIONALE: Indication of trending regime.
    """
    base = (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) > 0.1).astype(float)
    return _rolling_mean(base, 63)

def raut_083_positive_autocorr_flag_zscore_63d(close: pd.Series) -> pd.Series:
    """
    raut_083_positive_autocorr_flag_zscore_63d
    ECONOMIC RATIONALE: Indication of trending regime.
    """
    base = (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) > 0.1).astype(float)
    return _zscore_rolling(base, 63)

def raut_084_positive_autocorr_flag_rank_63d(close: pd.Series) -> pd.Series:
    """
    raut_084_positive_autocorr_flag_rank_63d
    ECONOMIC RATIONALE: Indication of trending regime.
    """
    base = (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) > 0.1).astype(float)
    return _rank_pct(base, 63)

def raut_085_positive_autocorr_flag_lvl_126d(close: pd.Series) -> pd.Series:
    """
    raut_085_positive_autocorr_flag_lvl_126d
    ECONOMIC RATIONALE: Indication of trending regime.
    """
    base = (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) > 0.1).astype(float)
    return _rolling_mean(base, 126)

def raut_086_positive_autocorr_flag_zscore_126d(close: pd.Series) -> pd.Series:
    """
    raut_086_positive_autocorr_flag_zscore_126d
    ECONOMIC RATIONALE: Indication of trending regime.
    """
    base = (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) > 0.1).astype(float)
    return _zscore_rolling(base, 126)

def raut_087_positive_autocorr_flag_rank_126d(close: pd.Series) -> pd.Series:
    """
    raut_087_positive_autocorr_flag_rank_126d
    ECONOMIC RATIONALE: Indication of trending regime.
    """
    base = (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) > 0.1).astype(float)
    return _rank_pct(base, 126)

def raut_088_positive_autocorr_flag_lvl_252d(close: pd.Series) -> pd.Series:
    """
    raut_088_positive_autocorr_flag_lvl_252d
    ECONOMIC RATIONALE: Indication of trending regime.
    """
    base = (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) > 0.1).astype(float)
    return _rolling_mean(base, 252)

def raut_089_positive_autocorr_flag_zscore_252d(close: pd.Series) -> pd.Series:
    """
    raut_089_positive_autocorr_flag_zscore_252d
    ECONOMIC RATIONALE: Indication of trending regime.
    """
    base = (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) > 0.1).astype(float)
    return _zscore_rolling(base, 252)

def raut_090_positive_autocorr_flag_rank_252d(close: pd.Series) -> pd.Series:
    """
    raut_090_positive_autocorr_flag_rank_252d
    ECONOMIC RATIONALE: Indication of trending regime.
    """
    base = (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) > 0.1).astype(float)
    return _rank_pct(base, 252)

def raut_091_autocorr_vol_corr_lvl_5d(close: pd.Series) -> pd.Series:
    """
    raut_091_autocorr_vol_corr_lvl_5d
    ECONOMIC RATIONALE: Relationship between persistence and volatility.
    """
    base = close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).corr(close.rolling(21).std())
    return _rolling_mean(base, 5)

def raut_092_autocorr_vol_corr_zscore_5d(close: pd.Series) -> pd.Series:
    """
    raut_092_autocorr_vol_corr_zscore_5d
    ECONOMIC RATIONALE: Relationship between persistence and volatility.
    """
    base = close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).corr(close.rolling(21).std())
    return _zscore_rolling(base, 5)

def raut_093_autocorr_vol_corr_rank_5d(close: pd.Series) -> pd.Series:
    """
    raut_093_autocorr_vol_corr_rank_5d
    ECONOMIC RATIONALE: Relationship between persistence and volatility.
    """
    base = close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).corr(close.rolling(21).std())
    return _rank_pct(base, 5)

def raut_094_autocorr_vol_corr_lvl_21d(close: pd.Series) -> pd.Series:
    """
    raut_094_autocorr_vol_corr_lvl_21d
    ECONOMIC RATIONALE: Relationship between persistence and volatility.
    """
    base = close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).corr(close.rolling(21).std())
    return _rolling_mean(base, 21)

def raut_095_autocorr_vol_corr_zscore_21d(close: pd.Series) -> pd.Series:
    """
    raut_095_autocorr_vol_corr_zscore_21d
    ECONOMIC RATIONALE: Relationship between persistence and volatility.
    """
    base = close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).corr(close.rolling(21).std())
    return _zscore_rolling(base, 21)

def raut_096_autocorr_vol_corr_rank_21d(close: pd.Series) -> pd.Series:
    """
    raut_096_autocorr_vol_corr_rank_21d
    ECONOMIC RATIONALE: Relationship between persistence and volatility.
    """
    base = close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).corr(close.rolling(21).std())
    return _rank_pct(base, 21)

def raut_097_autocorr_vol_corr_lvl_63d(close: pd.Series) -> pd.Series:
    """
    raut_097_autocorr_vol_corr_lvl_63d
    ECONOMIC RATIONALE: Relationship between persistence and volatility.
    """
    base = close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).corr(close.rolling(21).std())
    return _rolling_mean(base, 63)

def raut_098_autocorr_vol_corr_zscore_63d(close: pd.Series) -> pd.Series:
    """
    raut_098_autocorr_vol_corr_zscore_63d
    ECONOMIC RATIONALE: Relationship between persistence and volatility.
    """
    base = close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).corr(close.rolling(21).std())
    return _zscore_rolling(base, 63)

def raut_099_autocorr_vol_corr_rank_63d(close: pd.Series) -> pd.Series:
    """
    raut_099_autocorr_vol_corr_rank_63d
    ECONOMIC RATIONALE: Relationship between persistence and volatility.
    """
    base = close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).corr(close.rolling(21).std())
    return _rank_pct(base, 63)

def raut_100_autocorr_vol_corr_lvl_126d(close: pd.Series) -> pd.Series:
    """
    raut_100_autocorr_vol_corr_lvl_126d
    ECONOMIC RATIONALE: Relationship between persistence and volatility.
    """
    base = close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).corr(close.rolling(21).std())
    return _rolling_mean(base, 126)

def raut_101_autocorr_vol_corr_zscore_126d(close: pd.Series) -> pd.Series:
    """
    raut_101_autocorr_vol_corr_zscore_126d
    ECONOMIC RATIONALE: Relationship between persistence and volatility.
    """
    base = close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).corr(close.rolling(21).std())
    return _zscore_rolling(base, 126)

def raut_102_autocorr_vol_corr_rank_126d(close: pd.Series) -> pd.Series:
    """
    raut_102_autocorr_vol_corr_rank_126d
    ECONOMIC RATIONALE: Relationship between persistence and volatility.
    """
    base = close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).corr(close.rolling(21).std())
    return _rank_pct(base, 126)

def raut_103_autocorr_vol_corr_lvl_252d(close: pd.Series) -> pd.Series:
    """
    raut_103_autocorr_vol_corr_lvl_252d
    ECONOMIC RATIONALE: Relationship between persistence and volatility.
    """
    base = close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).corr(close.rolling(21).std())
    return _rolling_mean(base, 252)

def raut_104_autocorr_vol_corr_zscore_252d(close: pd.Series) -> pd.Series:
    """
    raut_104_autocorr_vol_corr_zscore_252d
    ECONOMIC RATIONALE: Relationship between persistence and volatility.
    """
    base = close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).corr(close.rolling(21).std())
    return _zscore_rolling(base, 252)

def raut_105_autocorr_vol_corr_rank_252d(close: pd.Series) -> pd.Series:
    """
    raut_105_autocorr_vol_corr_rank_252d
    ECONOMIC RATIONALE: Relationship between persistence and volatility.
    """
    base = close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)).rolling(63).corr(close.rolling(21).std())
    return _rank_pct(base, 252)

def raut_106_multi_lag_autocorr_sum_lvl_5d(close: pd.Series) -> pd.Series:
    """
    raut_106_multi_lag_autocorr_sum_lvl_5d
    ECONOMIC RATIONALE: Average persistence across multiple lags.
    """
    base = (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) + close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(2))) / 2
    return _rolling_mean(base, 5)

def raut_107_multi_lag_autocorr_sum_zscore_5d(close: pd.Series) -> pd.Series:
    """
    raut_107_multi_lag_autocorr_sum_zscore_5d
    ECONOMIC RATIONALE: Average persistence across multiple lags.
    """
    base = (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) + close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(2))) / 2
    return _zscore_rolling(base, 5)

def raut_108_multi_lag_autocorr_sum_rank_5d(close: pd.Series) -> pd.Series:
    """
    raut_108_multi_lag_autocorr_sum_rank_5d
    ECONOMIC RATIONALE: Average persistence across multiple lags.
    """
    base = (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) + close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(2))) / 2
    return _rank_pct(base, 5)

def raut_109_multi_lag_autocorr_sum_lvl_21d(close: pd.Series) -> pd.Series:
    """
    raut_109_multi_lag_autocorr_sum_lvl_21d
    ECONOMIC RATIONALE: Average persistence across multiple lags.
    """
    base = (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) + close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(2))) / 2
    return _rolling_mean(base, 21)

def raut_110_multi_lag_autocorr_sum_zscore_21d(close: pd.Series) -> pd.Series:
    """
    raut_110_multi_lag_autocorr_sum_zscore_21d
    ECONOMIC RATIONALE: Average persistence across multiple lags.
    """
    base = (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) + close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(2))) / 2
    return _zscore_rolling(base, 21)

def raut_111_multi_lag_autocorr_sum_rank_21d(close: pd.Series) -> pd.Series:
    """
    raut_111_multi_lag_autocorr_sum_rank_21d
    ECONOMIC RATIONALE: Average persistence across multiple lags.
    """
    base = (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) + close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(2))) / 2
    return _rank_pct(base, 21)

def raut_112_multi_lag_autocorr_sum_lvl_63d(close: pd.Series) -> pd.Series:
    """
    raut_112_multi_lag_autocorr_sum_lvl_63d
    ECONOMIC RATIONALE: Average persistence across multiple lags.
    """
    base = (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) + close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(2))) / 2
    return _rolling_mean(base, 63)

def raut_113_multi_lag_autocorr_sum_zscore_63d(close: pd.Series) -> pd.Series:
    """
    raut_113_multi_lag_autocorr_sum_zscore_63d
    ECONOMIC RATIONALE: Average persistence across multiple lags.
    """
    base = (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) + close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(2))) / 2
    return _zscore_rolling(base, 63)

def raut_114_multi_lag_autocorr_sum_rank_63d(close: pd.Series) -> pd.Series:
    """
    raut_114_multi_lag_autocorr_sum_rank_63d
    ECONOMIC RATIONALE: Average persistence across multiple lags.
    """
    base = (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) + close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(2))) / 2
    return _rank_pct(base, 63)

def raut_115_multi_lag_autocorr_sum_lvl_126d(close: pd.Series) -> pd.Series:
    """
    raut_115_multi_lag_autocorr_sum_lvl_126d
    ECONOMIC RATIONALE: Average persistence across multiple lags.
    """
    base = (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) + close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(2))) / 2
    return _rolling_mean(base, 126)

def raut_116_multi_lag_autocorr_sum_zscore_126d(close: pd.Series) -> pd.Series:
    """
    raut_116_multi_lag_autocorr_sum_zscore_126d
    ECONOMIC RATIONALE: Average persistence across multiple lags.
    """
    base = (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) + close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(2))) / 2
    return _zscore_rolling(base, 126)

def raut_117_multi_lag_autocorr_sum_rank_126d(close: pd.Series) -> pd.Series:
    """
    raut_117_multi_lag_autocorr_sum_rank_126d
    ECONOMIC RATIONALE: Average persistence across multiple lags.
    """
    base = (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) + close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(2))) / 2
    return _rank_pct(base, 126)

def raut_118_multi_lag_autocorr_sum_lvl_252d(close: pd.Series) -> pd.Series:
    """
    raut_118_multi_lag_autocorr_sum_lvl_252d
    ECONOMIC RATIONALE: Average persistence across multiple lags.
    """
    base = (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) + close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(2))) / 2
    return _rolling_mean(base, 252)

def raut_119_multi_lag_autocorr_sum_zscore_252d(close: pd.Series) -> pd.Series:
    """
    raut_119_multi_lag_autocorr_sum_zscore_252d
    ECONOMIC RATIONALE: Average persistence across multiple lags.
    """
    base = (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) + close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(2))) / 2
    return _zscore_rolling(base, 252)

def raut_120_multi_lag_autocorr_sum_rank_252d(close: pd.Series) -> pd.Series:
    """
    raut_120_multi_lag_autocorr_sum_rank_252d
    ECONOMIC RATIONALE: Average persistence across multiple lags.
    """
    base = (close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) + close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(2))) / 2
    return _rank_pct(base, 252)

# ── Registry ──────────────────────────────────────────────────────────────────
V109_REGISTRY_1 = {
    "raut_001_lag1_autocorr_lvl_5d": {"inputs": ["close"], "func": raut_001_lag1_autocorr_lvl_5d},
    "raut_002_lag1_autocorr_zscore_5d": {"inputs": ["close"], "func": raut_002_lag1_autocorr_zscore_5d},
    "raut_003_lag1_autocorr_rank_5d": {"inputs": ["close"], "func": raut_003_lag1_autocorr_rank_5d},
    "raut_004_lag1_autocorr_lvl_21d": {"inputs": ["close"], "func": raut_004_lag1_autocorr_lvl_21d},
    "raut_005_lag1_autocorr_zscore_21d": {"inputs": ["close"], "func": raut_005_lag1_autocorr_zscore_21d},
    "raut_006_lag1_autocorr_rank_21d": {"inputs": ["close"], "func": raut_006_lag1_autocorr_rank_21d},
    "raut_007_lag1_autocorr_lvl_63d": {"inputs": ["close"], "func": raut_007_lag1_autocorr_lvl_63d},
    "raut_008_lag1_autocorr_zscore_63d": {"inputs": ["close"], "func": raut_008_lag1_autocorr_zscore_63d},
    "raut_009_lag1_autocorr_rank_63d": {"inputs": ["close"], "func": raut_009_lag1_autocorr_rank_63d},
    "raut_010_lag1_autocorr_lvl_126d": {"inputs": ["close"], "func": raut_010_lag1_autocorr_lvl_126d},
    "raut_011_lag1_autocorr_zscore_126d": {"inputs": ["close"], "func": raut_011_lag1_autocorr_zscore_126d},
    "raut_012_lag1_autocorr_rank_126d": {"inputs": ["close"], "func": raut_012_lag1_autocorr_rank_126d},
    "raut_013_lag1_autocorr_lvl_252d": {"inputs": ["close"], "func": raut_013_lag1_autocorr_lvl_252d},
    "raut_014_lag1_autocorr_zscore_252d": {"inputs": ["close"], "func": raut_014_lag1_autocorr_zscore_252d},
    "raut_015_lag1_autocorr_rank_252d": {"inputs": ["close"], "func": raut_015_lag1_autocorr_rank_252d},
    "raut_016_lag5_autocorr_lvl_5d": {"inputs": ["close"], "func": raut_016_lag5_autocorr_lvl_5d},
    "raut_017_lag5_autocorr_zscore_5d": {"inputs": ["close"], "func": raut_017_lag5_autocorr_zscore_5d},
    "raut_018_lag5_autocorr_rank_5d": {"inputs": ["close"], "func": raut_018_lag5_autocorr_rank_5d},
    "raut_019_lag5_autocorr_lvl_21d": {"inputs": ["close"], "func": raut_019_lag5_autocorr_lvl_21d},
    "raut_020_lag5_autocorr_zscore_21d": {"inputs": ["close"], "func": raut_020_lag5_autocorr_zscore_21d},
    "raut_021_lag5_autocorr_rank_21d": {"inputs": ["close"], "func": raut_021_lag5_autocorr_rank_21d},
    "raut_022_lag5_autocorr_lvl_63d": {"inputs": ["close"], "func": raut_022_lag5_autocorr_lvl_63d},
    "raut_023_lag5_autocorr_zscore_63d": {"inputs": ["close"], "func": raut_023_lag5_autocorr_zscore_63d},
    "raut_024_lag5_autocorr_rank_63d": {"inputs": ["close"], "func": raut_024_lag5_autocorr_rank_63d},
    "raut_025_lag5_autocorr_lvl_126d": {"inputs": ["close"], "func": raut_025_lag5_autocorr_lvl_126d},
    "raut_026_lag5_autocorr_zscore_126d": {"inputs": ["close"], "func": raut_026_lag5_autocorr_zscore_126d},
    "raut_027_lag5_autocorr_rank_126d": {"inputs": ["close"], "func": raut_027_lag5_autocorr_rank_126d},
    "raut_028_lag5_autocorr_lvl_252d": {"inputs": ["close"], "func": raut_028_lag5_autocorr_lvl_252d},
    "raut_029_lag5_autocorr_zscore_252d": {"inputs": ["close"], "func": raut_029_lag5_autocorr_zscore_252d},
    "raut_030_lag5_autocorr_rank_252d": {"inputs": ["close"], "func": raut_030_lag5_autocorr_rank_252d},
    "raut_031_autocorr_zscore_lvl_5d": {"inputs": ["close"], "func": raut_031_autocorr_zscore_lvl_5d},
    "raut_032_autocorr_zscore_zscore_5d": {"inputs": ["close"], "func": raut_032_autocorr_zscore_zscore_5d},
    "raut_033_autocorr_zscore_rank_5d": {"inputs": ["close"], "func": raut_033_autocorr_zscore_rank_5d},
    "raut_034_autocorr_zscore_lvl_21d": {"inputs": ["close"], "func": raut_034_autocorr_zscore_lvl_21d},
    "raut_035_autocorr_zscore_zscore_21d": {"inputs": ["close"], "func": raut_035_autocorr_zscore_zscore_21d},
    "raut_036_autocorr_zscore_rank_21d": {"inputs": ["close"], "func": raut_036_autocorr_zscore_rank_21d},
    "raut_037_autocorr_zscore_lvl_63d": {"inputs": ["close"], "func": raut_037_autocorr_zscore_lvl_63d},
    "raut_038_autocorr_zscore_zscore_63d": {"inputs": ["close"], "func": raut_038_autocorr_zscore_zscore_63d},
    "raut_039_autocorr_zscore_rank_63d": {"inputs": ["close"], "func": raut_039_autocorr_zscore_rank_63d},
    "raut_040_autocorr_zscore_lvl_126d": {"inputs": ["close"], "func": raut_040_autocorr_zscore_lvl_126d},
    "raut_041_autocorr_zscore_zscore_126d": {"inputs": ["close"], "func": raut_041_autocorr_zscore_zscore_126d},
    "raut_042_autocorr_zscore_rank_126d": {"inputs": ["close"], "func": raut_042_autocorr_zscore_rank_126d},
    "raut_043_autocorr_zscore_lvl_252d": {"inputs": ["close"], "func": raut_043_autocorr_zscore_lvl_252d},
    "raut_044_autocorr_zscore_zscore_252d": {"inputs": ["close"], "func": raut_044_autocorr_zscore_zscore_252d},
    "raut_045_autocorr_zscore_rank_252d": {"inputs": ["close"], "func": raut_045_autocorr_zscore_rank_252d},
    "raut_046_autocorr_trend_lvl_5d": {"inputs": ["close"], "func": raut_046_autocorr_trend_lvl_5d},
    "raut_047_autocorr_trend_zscore_5d": {"inputs": ["close"], "func": raut_047_autocorr_trend_zscore_5d},
    "raut_048_autocorr_trend_rank_5d": {"inputs": ["close"], "func": raut_048_autocorr_trend_rank_5d},
    "raut_049_autocorr_trend_lvl_21d": {"inputs": ["close"], "func": raut_049_autocorr_trend_lvl_21d},
    "raut_050_autocorr_trend_zscore_21d": {"inputs": ["close"], "func": raut_050_autocorr_trend_zscore_21d},
    "raut_051_autocorr_trend_rank_21d": {"inputs": ["close"], "func": raut_051_autocorr_trend_rank_21d},
    "raut_052_autocorr_trend_lvl_63d": {"inputs": ["close"], "func": raut_052_autocorr_trend_lvl_63d},
    "raut_053_autocorr_trend_zscore_63d": {"inputs": ["close"], "func": raut_053_autocorr_trend_zscore_63d},
    "raut_054_autocorr_trend_rank_63d": {"inputs": ["close"], "func": raut_054_autocorr_trend_rank_63d},
    "raut_055_autocorr_trend_lvl_126d": {"inputs": ["close"], "func": raut_055_autocorr_trend_lvl_126d},
    "raut_056_autocorr_trend_zscore_126d": {"inputs": ["close"], "func": raut_056_autocorr_trend_zscore_126d},
    "raut_057_autocorr_trend_rank_126d": {"inputs": ["close"], "func": raut_057_autocorr_trend_rank_126d},
    "raut_058_autocorr_trend_lvl_252d": {"inputs": ["close"], "func": raut_058_autocorr_trend_lvl_252d},
    "raut_059_autocorr_trend_zscore_252d": {"inputs": ["close"], "func": raut_059_autocorr_trend_zscore_252d},
    "raut_060_autocorr_trend_rank_252d": {"inputs": ["close"], "func": raut_060_autocorr_trend_rank_252d},
    "raut_061_negative_autocorr_flag_lvl_5d": {"inputs": ["close"], "func": raut_061_negative_autocorr_flag_lvl_5d},
    "raut_062_negative_autocorr_flag_zscore_5d": {"inputs": ["close"], "func": raut_062_negative_autocorr_flag_zscore_5d},
    "raut_063_negative_autocorr_flag_rank_5d": {"inputs": ["close"], "func": raut_063_negative_autocorr_flag_rank_5d},
    "raut_064_negative_autocorr_flag_lvl_21d": {"inputs": ["close"], "func": raut_064_negative_autocorr_flag_lvl_21d},
    "raut_065_negative_autocorr_flag_zscore_21d": {"inputs": ["close"], "func": raut_065_negative_autocorr_flag_zscore_21d},
    "raut_066_negative_autocorr_flag_rank_21d": {"inputs": ["close"], "func": raut_066_negative_autocorr_flag_rank_21d},
    "raut_067_negative_autocorr_flag_lvl_63d": {"inputs": ["close"], "func": raut_067_negative_autocorr_flag_lvl_63d},
    "raut_068_negative_autocorr_flag_zscore_63d": {"inputs": ["close"], "func": raut_068_negative_autocorr_flag_zscore_63d},
    "raut_069_negative_autocorr_flag_rank_63d": {"inputs": ["close"], "func": raut_069_negative_autocorr_flag_rank_63d},
    "raut_070_negative_autocorr_flag_lvl_126d": {"inputs": ["close"], "func": raut_070_negative_autocorr_flag_lvl_126d},
    "raut_071_negative_autocorr_flag_zscore_126d": {"inputs": ["close"], "func": raut_071_negative_autocorr_flag_zscore_126d},
    "raut_072_negative_autocorr_flag_rank_126d": {"inputs": ["close"], "func": raut_072_negative_autocorr_flag_rank_126d},
    "raut_073_negative_autocorr_flag_lvl_252d": {"inputs": ["close"], "func": raut_073_negative_autocorr_flag_lvl_252d},
    "raut_074_negative_autocorr_flag_zscore_252d": {"inputs": ["close"], "func": raut_074_negative_autocorr_flag_zscore_252d},
    "raut_075_negative_autocorr_flag_rank_252d": {"inputs": ["close"], "func": raut_075_negative_autocorr_flag_rank_252d},
    "raut_076_positive_autocorr_flag_lvl_5d": {"inputs": ["close"], "func": raut_076_positive_autocorr_flag_lvl_5d},
    "raut_077_positive_autocorr_flag_zscore_5d": {"inputs": ["close"], "func": raut_077_positive_autocorr_flag_zscore_5d},
    "raut_078_positive_autocorr_flag_rank_5d": {"inputs": ["close"], "func": raut_078_positive_autocorr_flag_rank_5d},
    "raut_079_positive_autocorr_flag_lvl_21d": {"inputs": ["close"], "func": raut_079_positive_autocorr_flag_lvl_21d},
    "raut_080_positive_autocorr_flag_zscore_21d": {"inputs": ["close"], "func": raut_080_positive_autocorr_flag_zscore_21d},
    "raut_081_positive_autocorr_flag_rank_21d": {"inputs": ["close"], "func": raut_081_positive_autocorr_flag_rank_21d},
    "raut_082_positive_autocorr_flag_lvl_63d": {"inputs": ["close"], "func": raut_082_positive_autocorr_flag_lvl_63d},
    "raut_083_positive_autocorr_flag_zscore_63d": {"inputs": ["close"], "func": raut_083_positive_autocorr_flag_zscore_63d},
    "raut_084_positive_autocorr_flag_rank_63d": {"inputs": ["close"], "func": raut_084_positive_autocorr_flag_rank_63d},
    "raut_085_positive_autocorr_flag_lvl_126d": {"inputs": ["close"], "func": raut_085_positive_autocorr_flag_lvl_126d},
    "raut_086_positive_autocorr_flag_zscore_126d": {"inputs": ["close"], "func": raut_086_positive_autocorr_flag_zscore_126d},
    "raut_087_positive_autocorr_flag_rank_126d": {"inputs": ["close"], "func": raut_087_positive_autocorr_flag_rank_126d},
    "raut_088_positive_autocorr_flag_lvl_252d": {"inputs": ["close"], "func": raut_088_positive_autocorr_flag_lvl_252d},
    "raut_089_positive_autocorr_flag_zscore_252d": {"inputs": ["close"], "func": raut_089_positive_autocorr_flag_zscore_252d},
    "raut_090_positive_autocorr_flag_rank_252d": {"inputs": ["close"], "func": raut_090_positive_autocorr_flag_rank_252d},
    "raut_091_autocorr_vol_corr_lvl_5d": {"inputs": ["close"], "func": raut_091_autocorr_vol_corr_lvl_5d},
    "raut_092_autocorr_vol_corr_zscore_5d": {"inputs": ["close"], "func": raut_092_autocorr_vol_corr_zscore_5d},
    "raut_093_autocorr_vol_corr_rank_5d": {"inputs": ["close"], "func": raut_093_autocorr_vol_corr_rank_5d},
    "raut_094_autocorr_vol_corr_lvl_21d": {"inputs": ["close"], "func": raut_094_autocorr_vol_corr_lvl_21d},
    "raut_095_autocorr_vol_corr_zscore_21d": {"inputs": ["close"], "func": raut_095_autocorr_vol_corr_zscore_21d},
    "raut_096_autocorr_vol_corr_rank_21d": {"inputs": ["close"], "func": raut_096_autocorr_vol_corr_rank_21d},
    "raut_097_autocorr_vol_corr_lvl_63d": {"inputs": ["close"], "func": raut_097_autocorr_vol_corr_lvl_63d},
    "raut_098_autocorr_vol_corr_zscore_63d": {"inputs": ["close"], "func": raut_098_autocorr_vol_corr_zscore_63d},
    "raut_099_autocorr_vol_corr_rank_63d": {"inputs": ["close"], "func": raut_099_autocorr_vol_corr_rank_63d},
    "raut_100_autocorr_vol_corr_lvl_126d": {"inputs": ["close"], "func": raut_100_autocorr_vol_corr_lvl_126d},
    "raut_101_autocorr_vol_corr_zscore_126d": {"inputs": ["close"], "func": raut_101_autocorr_vol_corr_zscore_126d},
    "raut_102_autocorr_vol_corr_rank_126d": {"inputs": ["close"], "func": raut_102_autocorr_vol_corr_rank_126d},
    "raut_103_autocorr_vol_corr_lvl_252d": {"inputs": ["close"], "func": raut_103_autocorr_vol_corr_lvl_252d},
    "raut_104_autocorr_vol_corr_zscore_252d": {"inputs": ["close"], "func": raut_104_autocorr_vol_corr_zscore_252d},
    "raut_105_autocorr_vol_corr_rank_252d": {"inputs": ["close"], "func": raut_105_autocorr_vol_corr_rank_252d},
    "raut_106_multi_lag_autocorr_sum_lvl_5d": {"inputs": ["close"], "func": raut_106_multi_lag_autocorr_sum_lvl_5d},
    "raut_107_multi_lag_autocorr_sum_zscore_5d": {"inputs": ["close"], "func": raut_107_multi_lag_autocorr_sum_zscore_5d},
    "raut_108_multi_lag_autocorr_sum_rank_5d": {"inputs": ["close"], "func": raut_108_multi_lag_autocorr_sum_rank_5d},
    "raut_109_multi_lag_autocorr_sum_lvl_21d": {"inputs": ["close"], "func": raut_109_multi_lag_autocorr_sum_lvl_21d},
    "raut_110_multi_lag_autocorr_sum_zscore_21d": {"inputs": ["close"], "func": raut_110_multi_lag_autocorr_sum_zscore_21d},
    "raut_111_multi_lag_autocorr_sum_rank_21d": {"inputs": ["close"], "func": raut_111_multi_lag_autocorr_sum_rank_21d},
    "raut_112_multi_lag_autocorr_sum_lvl_63d": {"inputs": ["close"], "func": raut_112_multi_lag_autocorr_sum_lvl_63d},
    "raut_113_multi_lag_autocorr_sum_zscore_63d": {"inputs": ["close"], "func": raut_113_multi_lag_autocorr_sum_zscore_63d},
    "raut_114_multi_lag_autocorr_sum_rank_63d": {"inputs": ["close"], "func": raut_114_multi_lag_autocorr_sum_rank_63d},
    "raut_115_multi_lag_autocorr_sum_lvl_126d": {"inputs": ["close"], "func": raut_115_multi_lag_autocorr_sum_lvl_126d},
    "raut_116_multi_lag_autocorr_sum_zscore_126d": {"inputs": ["close"], "func": raut_116_multi_lag_autocorr_sum_zscore_126d},
    "raut_117_multi_lag_autocorr_sum_rank_126d": {"inputs": ["close"], "func": raut_117_multi_lag_autocorr_sum_rank_126d},
    "raut_118_multi_lag_autocorr_sum_lvl_252d": {"inputs": ["close"], "func": raut_118_multi_lag_autocorr_sum_lvl_252d},
    "raut_119_multi_lag_autocorr_sum_zscore_252d": {"inputs": ["close"], "func": raut_119_multi_lag_autocorr_sum_zscore_252d},
    "raut_120_multi_lag_autocorr_sum_rank_252d": {"inputs": ["close"], "func": raut_120_multi_lag_autocorr_sum_rank_252d},
}
