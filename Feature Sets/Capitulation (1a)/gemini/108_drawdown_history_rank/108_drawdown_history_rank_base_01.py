"""
108_drawdown_history_rank — Base Features Part 1
Domain: drawdown_history_rank
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

def dhrk_001_current_drawdown_lvl_5d(close: pd.Series) -> pd.Series:
    """
    dhrk_001_current_drawdown_lvl_5d
    ECONOMIC RATIONALE: Drawdown from the 52-week high.
    """
    base = close / close.rolling(252).max() - 1
    return _rolling_mean(base, 5)

def dhrk_002_current_drawdown_zscore_5d(close: pd.Series) -> pd.Series:
    """
    dhrk_002_current_drawdown_zscore_5d
    ECONOMIC RATIONALE: Drawdown from the 52-week high.
    """
    base = close / close.rolling(252).max() - 1
    return _zscore_rolling(base, 5)

def dhrk_003_current_drawdown_rank_5d(close: pd.Series) -> pd.Series:
    """
    dhrk_003_current_drawdown_rank_5d
    ECONOMIC RATIONALE: Drawdown from the 52-week high.
    """
    base = close / close.rolling(252).max() - 1
    return _rank_pct(base, 5)

def dhrk_004_current_drawdown_lvl_21d(close: pd.Series) -> pd.Series:
    """
    dhrk_004_current_drawdown_lvl_21d
    ECONOMIC RATIONALE: Drawdown from the 52-week high.
    """
    base = close / close.rolling(252).max() - 1
    return _rolling_mean(base, 21)

def dhrk_005_current_drawdown_zscore_21d(close: pd.Series) -> pd.Series:
    """
    dhrk_005_current_drawdown_zscore_21d
    ECONOMIC RATIONALE: Drawdown from the 52-week high.
    """
    base = close / close.rolling(252).max() - 1
    return _zscore_rolling(base, 21)

def dhrk_006_current_drawdown_rank_21d(close: pd.Series) -> pd.Series:
    """
    dhrk_006_current_drawdown_rank_21d
    ECONOMIC RATIONALE: Drawdown from the 52-week high.
    """
    base = close / close.rolling(252).max() - 1
    return _rank_pct(base, 21)

def dhrk_007_current_drawdown_lvl_63d(close: pd.Series) -> pd.Series:
    """
    dhrk_007_current_drawdown_lvl_63d
    ECONOMIC RATIONALE: Drawdown from the 52-week high.
    """
    base = close / close.rolling(252).max() - 1
    return _rolling_mean(base, 63)

def dhrk_008_current_drawdown_zscore_63d(close: pd.Series) -> pd.Series:
    """
    dhrk_008_current_drawdown_zscore_63d
    ECONOMIC RATIONALE: Drawdown from the 52-week high.
    """
    base = close / close.rolling(252).max() - 1
    return _zscore_rolling(base, 63)

def dhrk_009_current_drawdown_rank_63d(close: pd.Series) -> pd.Series:
    """
    dhrk_009_current_drawdown_rank_63d
    ECONOMIC RATIONALE: Drawdown from the 52-week high.
    """
    base = close / close.rolling(252).max() - 1
    return _rank_pct(base, 63)

def dhrk_010_current_drawdown_lvl_126d(close: pd.Series) -> pd.Series:
    """
    dhrk_010_current_drawdown_lvl_126d
    ECONOMIC RATIONALE: Drawdown from the 52-week high.
    """
    base = close / close.rolling(252).max() - 1
    return _rolling_mean(base, 126)

def dhrk_011_current_drawdown_zscore_126d(close: pd.Series) -> pd.Series:
    """
    dhrk_011_current_drawdown_zscore_126d
    ECONOMIC RATIONALE: Drawdown from the 52-week high.
    """
    base = close / close.rolling(252).max() - 1
    return _zscore_rolling(base, 126)

def dhrk_012_current_drawdown_rank_126d(close: pd.Series) -> pd.Series:
    """
    dhrk_012_current_drawdown_rank_126d
    ECONOMIC RATIONALE: Drawdown from the 52-week high.
    """
    base = close / close.rolling(252).max() - 1
    return _rank_pct(base, 126)

def dhrk_013_current_drawdown_lvl_252d(close: pd.Series) -> pd.Series:
    """
    dhrk_013_current_drawdown_lvl_252d
    ECONOMIC RATIONALE: Drawdown from the 52-week high.
    """
    base = close / close.rolling(252).max() - 1
    return _rolling_mean(base, 252)

def dhrk_014_current_drawdown_zscore_252d(close: pd.Series) -> pd.Series:
    """
    dhrk_014_current_drawdown_zscore_252d
    ECONOMIC RATIONALE: Drawdown from the 52-week high.
    """
    base = close / close.rolling(252).max() - 1
    return _zscore_rolling(base, 252)

def dhrk_015_current_drawdown_rank_252d(close: pd.Series) -> pd.Series:
    """
    dhrk_015_current_drawdown_rank_252d
    ECONOMIC RATIONALE: Drawdown from the 52-week high.
    """
    base = close / close.rolling(252).max() - 1
    return _rank_pct(base, 252)

def dhrk_016_drawdown_rank_252d_lvl_5d(close: pd.Series) -> pd.Series:
    """
    dhrk_016_drawdown_rank_252d_lvl_5d
    ECONOMIC RATIONALE: Historical rank of the current drawdown level.
    """
    base = _rank_pct(close / close.rolling(252).max() - 1, 252)
    return _rolling_mean(base, 5)

def dhrk_017_drawdown_rank_252d_zscore_5d(close: pd.Series) -> pd.Series:
    """
    dhrk_017_drawdown_rank_252d_zscore_5d
    ECONOMIC RATIONALE: Historical rank of the current drawdown level.
    """
    base = _rank_pct(close / close.rolling(252).max() - 1, 252)
    return _zscore_rolling(base, 5)

def dhrk_018_drawdown_rank_252d_rank_5d(close: pd.Series) -> pd.Series:
    """
    dhrk_018_drawdown_rank_252d_rank_5d
    ECONOMIC RATIONALE: Historical rank of the current drawdown level.
    """
    base = _rank_pct(close / close.rolling(252).max() - 1, 252)
    return _rank_pct(base, 5)

def dhrk_019_drawdown_rank_252d_lvl_21d(close: pd.Series) -> pd.Series:
    """
    dhrk_019_drawdown_rank_252d_lvl_21d
    ECONOMIC RATIONALE: Historical rank of the current drawdown level.
    """
    base = _rank_pct(close / close.rolling(252).max() - 1, 252)
    return _rolling_mean(base, 21)

def dhrk_020_drawdown_rank_252d_zscore_21d(close: pd.Series) -> pd.Series:
    """
    dhrk_020_drawdown_rank_252d_zscore_21d
    ECONOMIC RATIONALE: Historical rank of the current drawdown level.
    """
    base = _rank_pct(close / close.rolling(252).max() - 1, 252)
    return _zscore_rolling(base, 21)

def dhrk_021_drawdown_rank_252d_rank_21d(close: pd.Series) -> pd.Series:
    """
    dhrk_021_drawdown_rank_252d_rank_21d
    ECONOMIC RATIONALE: Historical rank of the current drawdown level.
    """
    base = _rank_pct(close / close.rolling(252).max() - 1, 252)
    return _rank_pct(base, 21)

def dhrk_022_drawdown_rank_252d_lvl_63d(close: pd.Series) -> pd.Series:
    """
    dhrk_022_drawdown_rank_252d_lvl_63d
    ECONOMIC RATIONALE: Historical rank of the current drawdown level.
    """
    base = _rank_pct(close / close.rolling(252).max() - 1, 252)
    return _rolling_mean(base, 63)

def dhrk_023_drawdown_rank_252d_zscore_63d(close: pd.Series) -> pd.Series:
    """
    dhrk_023_drawdown_rank_252d_zscore_63d
    ECONOMIC RATIONALE: Historical rank of the current drawdown level.
    """
    base = _rank_pct(close / close.rolling(252).max() - 1, 252)
    return _zscore_rolling(base, 63)

def dhrk_024_drawdown_rank_252d_rank_63d(close: pd.Series) -> pd.Series:
    """
    dhrk_024_drawdown_rank_252d_rank_63d
    ECONOMIC RATIONALE: Historical rank of the current drawdown level.
    """
    base = _rank_pct(close / close.rolling(252).max() - 1, 252)
    return _rank_pct(base, 63)

def dhrk_025_drawdown_rank_252d_lvl_126d(close: pd.Series) -> pd.Series:
    """
    dhrk_025_drawdown_rank_252d_lvl_126d
    ECONOMIC RATIONALE: Historical rank of the current drawdown level.
    """
    base = _rank_pct(close / close.rolling(252).max() - 1, 252)
    return _rolling_mean(base, 126)

def dhrk_026_drawdown_rank_252d_zscore_126d(close: pd.Series) -> pd.Series:
    """
    dhrk_026_drawdown_rank_252d_zscore_126d
    ECONOMIC RATIONALE: Historical rank of the current drawdown level.
    """
    base = _rank_pct(close / close.rolling(252).max() - 1, 252)
    return _zscore_rolling(base, 126)

def dhrk_027_drawdown_rank_252d_rank_126d(close: pd.Series) -> pd.Series:
    """
    dhrk_027_drawdown_rank_252d_rank_126d
    ECONOMIC RATIONALE: Historical rank of the current drawdown level.
    """
    base = _rank_pct(close / close.rolling(252).max() - 1, 252)
    return _rank_pct(base, 126)

def dhrk_028_drawdown_rank_252d_lvl_252d(close: pd.Series) -> pd.Series:
    """
    dhrk_028_drawdown_rank_252d_lvl_252d
    ECONOMIC RATIONALE: Historical rank of the current drawdown level.
    """
    base = _rank_pct(close / close.rolling(252).max() - 1, 252)
    return _rolling_mean(base, 252)

def dhrk_029_drawdown_rank_252d_zscore_252d(close: pd.Series) -> pd.Series:
    """
    dhrk_029_drawdown_rank_252d_zscore_252d
    ECONOMIC RATIONALE: Historical rank of the current drawdown level.
    """
    base = _rank_pct(close / close.rolling(252).max() - 1, 252)
    return _zscore_rolling(base, 252)

def dhrk_030_drawdown_rank_252d_rank_252d(close: pd.Series) -> pd.Series:
    """
    dhrk_030_drawdown_rank_252d_rank_252d
    ECONOMIC RATIONALE: Historical rank of the current drawdown level.
    """
    base = _rank_pct(close / close.rolling(252).max() - 1, 252)
    return _rank_pct(base, 252)

def dhrk_031_drawdown_severity_z_lvl_5d(close: pd.Series) -> pd.Series:
    """
    dhrk_031_drawdown_severity_z_lvl_5d
    ECONOMIC RATIONALE: Z-score of current drawdown vs historical drawdowns.
    """
    base = _zscore_rolling(close / close.rolling(252).max() - 1, 252)
    return _rolling_mean(base, 5)

def dhrk_032_drawdown_severity_z_zscore_5d(close: pd.Series) -> pd.Series:
    """
    dhrk_032_drawdown_severity_z_zscore_5d
    ECONOMIC RATIONALE: Z-score of current drawdown vs historical drawdowns.
    """
    base = _zscore_rolling(close / close.rolling(252).max() - 1, 252)
    return _zscore_rolling(base, 5)

def dhrk_033_drawdown_severity_z_rank_5d(close: pd.Series) -> pd.Series:
    """
    dhrk_033_drawdown_severity_z_rank_5d
    ECONOMIC RATIONALE: Z-score of current drawdown vs historical drawdowns.
    """
    base = _zscore_rolling(close / close.rolling(252).max() - 1, 252)
    return _rank_pct(base, 5)

def dhrk_034_drawdown_severity_z_lvl_21d(close: pd.Series) -> pd.Series:
    """
    dhrk_034_drawdown_severity_z_lvl_21d
    ECONOMIC RATIONALE: Z-score of current drawdown vs historical drawdowns.
    """
    base = _zscore_rolling(close / close.rolling(252).max() - 1, 252)
    return _rolling_mean(base, 21)

def dhrk_035_drawdown_severity_z_zscore_21d(close: pd.Series) -> pd.Series:
    """
    dhrk_035_drawdown_severity_z_zscore_21d
    ECONOMIC RATIONALE: Z-score of current drawdown vs historical drawdowns.
    """
    base = _zscore_rolling(close / close.rolling(252).max() - 1, 252)
    return _zscore_rolling(base, 21)

def dhrk_036_drawdown_severity_z_rank_21d(close: pd.Series) -> pd.Series:
    """
    dhrk_036_drawdown_severity_z_rank_21d
    ECONOMIC RATIONALE: Z-score of current drawdown vs historical drawdowns.
    """
    base = _zscore_rolling(close / close.rolling(252).max() - 1, 252)
    return _rank_pct(base, 21)

def dhrk_037_drawdown_severity_z_lvl_63d(close: pd.Series) -> pd.Series:
    """
    dhrk_037_drawdown_severity_z_lvl_63d
    ECONOMIC RATIONALE: Z-score of current drawdown vs historical drawdowns.
    """
    base = _zscore_rolling(close / close.rolling(252).max() - 1, 252)
    return _rolling_mean(base, 63)

def dhrk_038_drawdown_severity_z_zscore_63d(close: pd.Series) -> pd.Series:
    """
    dhrk_038_drawdown_severity_z_zscore_63d
    ECONOMIC RATIONALE: Z-score of current drawdown vs historical drawdowns.
    """
    base = _zscore_rolling(close / close.rolling(252).max() - 1, 252)
    return _zscore_rolling(base, 63)

def dhrk_039_drawdown_severity_z_rank_63d(close: pd.Series) -> pd.Series:
    """
    dhrk_039_drawdown_severity_z_rank_63d
    ECONOMIC RATIONALE: Z-score of current drawdown vs historical drawdowns.
    """
    base = _zscore_rolling(close / close.rolling(252).max() - 1, 252)
    return _rank_pct(base, 63)

def dhrk_040_drawdown_severity_z_lvl_126d(close: pd.Series) -> pd.Series:
    """
    dhrk_040_drawdown_severity_z_lvl_126d
    ECONOMIC RATIONALE: Z-score of current drawdown vs historical drawdowns.
    """
    base = _zscore_rolling(close / close.rolling(252).max() - 1, 252)
    return _rolling_mean(base, 126)

def dhrk_041_drawdown_severity_z_zscore_126d(close: pd.Series) -> pd.Series:
    """
    dhrk_041_drawdown_severity_z_zscore_126d
    ECONOMIC RATIONALE: Z-score of current drawdown vs historical drawdowns.
    """
    base = _zscore_rolling(close / close.rolling(252).max() - 1, 252)
    return _zscore_rolling(base, 126)

def dhrk_042_drawdown_severity_z_rank_126d(close: pd.Series) -> pd.Series:
    """
    dhrk_042_drawdown_severity_z_rank_126d
    ECONOMIC RATIONALE: Z-score of current drawdown vs historical drawdowns.
    """
    base = _zscore_rolling(close / close.rolling(252).max() - 1, 252)
    return _rank_pct(base, 126)

def dhrk_043_drawdown_severity_z_lvl_252d(close: pd.Series) -> pd.Series:
    """
    dhrk_043_drawdown_severity_z_lvl_252d
    ECONOMIC RATIONALE: Z-score of current drawdown vs historical drawdowns.
    """
    base = _zscore_rolling(close / close.rolling(252).max() - 1, 252)
    return _rolling_mean(base, 252)

def dhrk_044_drawdown_severity_z_zscore_252d(close: pd.Series) -> pd.Series:
    """
    dhrk_044_drawdown_severity_z_zscore_252d
    ECONOMIC RATIONALE: Z-score of current drawdown vs historical drawdowns.
    """
    base = _zscore_rolling(close / close.rolling(252).max() - 1, 252)
    return _zscore_rolling(base, 252)

def dhrk_045_drawdown_severity_z_rank_252d(close: pd.Series) -> pd.Series:
    """
    dhrk_045_drawdown_severity_z_rank_252d
    ECONOMIC RATIONALE: Z-score of current drawdown vs historical drawdowns.
    """
    base = _zscore_rolling(close / close.rolling(252).max() - 1, 252)
    return _rank_pct(base, 252)

def dhrk_046_drawdown_duration_lvl_5d(close: pd.Series) -> pd.Series:
    """
    dhrk_046_drawdown_duration_lvl_5d
    ECONOMIC RATIONALE: Number of days since the last 52-week high.
    """
    base = (close < close.rolling(252).max()).rolling(252).sum()
    return _rolling_mean(base, 5)

def dhrk_047_drawdown_duration_zscore_5d(close: pd.Series) -> pd.Series:
    """
    dhrk_047_drawdown_duration_zscore_5d
    ECONOMIC RATIONALE: Number of days since the last 52-week high.
    """
    base = (close < close.rolling(252).max()).rolling(252).sum()
    return _zscore_rolling(base, 5)

def dhrk_048_drawdown_duration_rank_5d(close: pd.Series) -> pd.Series:
    """
    dhrk_048_drawdown_duration_rank_5d
    ECONOMIC RATIONALE: Number of days since the last 52-week high.
    """
    base = (close < close.rolling(252).max()).rolling(252).sum()
    return _rank_pct(base, 5)

def dhrk_049_drawdown_duration_lvl_21d(close: pd.Series) -> pd.Series:
    """
    dhrk_049_drawdown_duration_lvl_21d
    ECONOMIC RATIONALE: Number of days since the last 52-week high.
    """
    base = (close < close.rolling(252).max()).rolling(252).sum()
    return _rolling_mean(base, 21)

def dhrk_050_drawdown_duration_zscore_21d(close: pd.Series) -> pd.Series:
    """
    dhrk_050_drawdown_duration_zscore_21d
    ECONOMIC RATIONALE: Number of days since the last 52-week high.
    """
    base = (close < close.rolling(252).max()).rolling(252).sum()
    return _zscore_rolling(base, 21)

def dhrk_051_drawdown_duration_rank_21d(close: pd.Series) -> pd.Series:
    """
    dhrk_051_drawdown_duration_rank_21d
    ECONOMIC RATIONALE: Number of days since the last 52-week high.
    """
    base = (close < close.rolling(252).max()).rolling(252).sum()
    return _rank_pct(base, 21)

def dhrk_052_drawdown_duration_lvl_63d(close: pd.Series) -> pd.Series:
    """
    dhrk_052_drawdown_duration_lvl_63d
    ECONOMIC RATIONALE: Number of days since the last 52-week high.
    """
    base = (close < close.rolling(252).max()).rolling(252).sum()
    return _rolling_mean(base, 63)

def dhrk_053_drawdown_duration_zscore_63d(close: pd.Series) -> pd.Series:
    """
    dhrk_053_drawdown_duration_zscore_63d
    ECONOMIC RATIONALE: Number of days since the last 52-week high.
    """
    base = (close < close.rolling(252).max()).rolling(252).sum()
    return _zscore_rolling(base, 63)

def dhrk_054_drawdown_duration_rank_63d(close: pd.Series) -> pd.Series:
    """
    dhrk_054_drawdown_duration_rank_63d
    ECONOMIC RATIONALE: Number of days since the last 52-week high.
    """
    base = (close < close.rolling(252).max()).rolling(252).sum()
    return _rank_pct(base, 63)

def dhrk_055_drawdown_duration_lvl_126d(close: pd.Series) -> pd.Series:
    """
    dhrk_055_drawdown_duration_lvl_126d
    ECONOMIC RATIONALE: Number of days since the last 52-week high.
    """
    base = (close < close.rolling(252).max()).rolling(252).sum()
    return _rolling_mean(base, 126)

def dhrk_056_drawdown_duration_zscore_126d(close: pd.Series) -> pd.Series:
    """
    dhrk_056_drawdown_duration_zscore_126d
    ECONOMIC RATIONALE: Number of days since the last 52-week high.
    """
    base = (close < close.rolling(252).max()).rolling(252).sum()
    return _zscore_rolling(base, 126)

def dhrk_057_drawdown_duration_rank_126d(close: pd.Series) -> pd.Series:
    """
    dhrk_057_drawdown_duration_rank_126d
    ECONOMIC RATIONALE: Number of days since the last 52-week high.
    """
    base = (close < close.rolling(252).max()).rolling(252).sum()
    return _rank_pct(base, 126)

def dhrk_058_drawdown_duration_lvl_252d(close: pd.Series) -> pd.Series:
    """
    dhrk_058_drawdown_duration_lvl_252d
    ECONOMIC RATIONALE: Number of days since the last 52-week high.
    """
    base = (close < close.rolling(252).max()).rolling(252).sum()
    return _rolling_mean(base, 252)

def dhrk_059_drawdown_duration_zscore_252d(close: pd.Series) -> pd.Series:
    """
    dhrk_059_drawdown_duration_zscore_252d
    ECONOMIC RATIONALE: Number of days since the last 52-week high.
    """
    base = (close < close.rolling(252).max()).rolling(252).sum()
    return _zscore_rolling(base, 252)

def dhrk_060_drawdown_duration_rank_252d(close: pd.Series) -> pd.Series:
    """
    dhrk_060_drawdown_duration_rank_252d
    ECONOMIC RATIONALE: Number of days since the last 52-week high.
    """
    base = (close < close.rolling(252).max()).rolling(252).sum()
    return _rank_pct(base, 252)

def dhrk_061_peak_to_trough_momentum_lvl_5d(close: pd.Series) -> pd.Series:
    """
    dhrk_061_peak_to_trough_momentum_lvl_5d
    ECONOMIC RATIONALE: Average rate of wealth destruction from peak.
    """
    base = (close.rolling(252).max() - close) / 252
    return _rolling_mean(base, 5)

def dhrk_062_peak_to_trough_momentum_zscore_5d(close: pd.Series) -> pd.Series:
    """
    dhrk_062_peak_to_trough_momentum_zscore_5d
    ECONOMIC RATIONALE: Average rate of wealth destruction from peak.
    """
    base = (close.rolling(252).max() - close) / 252
    return _zscore_rolling(base, 5)

def dhrk_063_peak_to_trough_momentum_rank_5d(close: pd.Series) -> pd.Series:
    """
    dhrk_063_peak_to_trough_momentum_rank_5d
    ECONOMIC RATIONALE: Average rate of wealth destruction from peak.
    """
    base = (close.rolling(252).max() - close) / 252
    return _rank_pct(base, 5)

def dhrk_064_peak_to_trough_momentum_lvl_21d(close: pd.Series) -> pd.Series:
    """
    dhrk_064_peak_to_trough_momentum_lvl_21d
    ECONOMIC RATIONALE: Average rate of wealth destruction from peak.
    """
    base = (close.rolling(252).max() - close) / 252
    return _rolling_mean(base, 21)

def dhrk_065_peak_to_trough_momentum_zscore_21d(close: pd.Series) -> pd.Series:
    """
    dhrk_065_peak_to_trough_momentum_zscore_21d
    ECONOMIC RATIONALE: Average rate of wealth destruction from peak.
    """
    base = (close.rolling(252).max() - close) / 252
    return _zscore_rolling(base, 21)

def dhrk_066_peak_to_trough_momentum_rank_21d(close: pd.Series) -> pd.Series:
    """
    dhrk_066_peak_to_trough_momentum_rank_21d
    ECONOMIC RATIONALE: Average rate of wealth destruction from peak.
    """
    base = (close.rolling(252).max() - close) / 252
    return _rank_pct(base, 21)

def dhrk_067_peak_to_trough_momentum_lvl_63d(close: pd.Series) -> pd.Series:
    """
    dhrk_067_peak_to_trough_momentum_lvl_63d
    ECONOMIC RATIONALE: Average rate of wealth destruction from peak.
    """
    base = (close.rolling(252).max() - close) / 252
    return _rolling_mean(base, 63)

def dhrk_068_peak_to_trough_momentum_zscore_63d(close: pd.Series) -> pd.Series:
    """
    dhrk_068_peak_to_trough_momentum_zscore_63d
    ECONOMIC RATIONALE: Average rate of wealth destruction from peak.
    """
    base = (close.rolling(252).max() - close) / 252
    return _zscore_rolling(base, 63)

def dhrk_069_peak_to_trough_momentum_rank_63d(close: pd.Series) -> pd.Series:
    """
    dhrk_069_peak_to_trough_momentum_rank_63d
    ECONOMIC RATIONALE: Average rate of wealth destruction from peak.
    """
    base = (close.rolling(252).max() - close) / 252
    return _rank_pct(base, 63)

def dhrk_070_peak_to_trough_momentum_lvl_126d(close: pd.Series) -> pd.Series:
    """
    dhrk_070_peak_to_trough_momentum_lvl_126d
    ECONOMIC RATIONALE: Average rate of wealth destruction from peak.
    """
    base = (close.rolling(252).max() - close) / 252
    return _rolling_mean(base, 126)

def dhrk_071_peak_to_trough_momentum_zscore_126d(close: pd.Series) -> pd.Series:
    """
    dhrk_071_peak_to_trough_momentum_zscore_126d
    ECONOMIC RATIONALE: Average rate of wealth destruction from peak.
    """
    base = (close.rolling(252).max() - close) / 252
    return _zscore_rolling(base, 126)

def dhrk_072_peak_to_trough_momentum_rank_126d(close: pd.Series) -> pd.Series:
    """
    dhrk_072_peak_to_trough_momentum_rank_126d
    ECONOMIC RATIONALE: Average rate of wealth destruction from peak.
    """
    base = (close.rolling(252).max() - close) / 252
    return _rank_pct(base, 126)

def dhrk_073_peak_to_trough_momentum_lvl_252d(close: pd.Series) -> pd.Series:
    """
    dhrk_073_peak_to_trough_momentum_lvl_252d
    ECONOMIC RATIONALE: Average rate of wealth destruction from peak.
    """
    base = (close.rolling(252).max() - close) / 252
    return _rolling_mean(base, 252)

def dhrk_074_peak_to_trough_momentum_zscore_252d(close: pd.Series) -> pd.Series:
    """
    dhrk_074_peak_to_trough_momentum_zscore_252d
    ECONOMIC RATIONALE: Average rate of wealth destruction from peak.
    """
    base = (close.rolling(252).max() - close) / 252
    return _zscore_rolling(base, 252)

def dhrk_075_peak_to_trough_momentum_rank_252d(close: pd.Series) -> pd.Series:
    """
    dhrk_075_peak_to_trough_momentum_rank_252d
    ECONOMIC RATIONALE: Average rate of wealth destruction from peak.
    """
    base = (close.rolling(252).max() - close) / 252
    return _rank_pct(base, 252)

def dhrk_076_drawdown_acceleration_lvl_5d(close: pd.Series) -> pd.Series:
    """
    dhrk_076_drawdown_acceleration_lvl_5d
    ECONOMIC RATIONALE: Speed at which the drawdown is deepening.
    """
    base = (close / close.rolling(252).max() - 1).diff(21)
    return _rolling_mean(base, 5)

def dhrk_077_drawdown_acceleration_zscore_5d(close: pd.Series) -> pd.Series:
    """
    dhrk_077_drawdown_acceleration_zscore_5d
    ECONOMIC RATIONALE: Speed at which the drawdown is deepening.
    """
    base = (close / close.rolling(252).max() - 1).diff(21)
    return _zscore_rolling(base, 5)

def dhrk_078_drawdown_acceleration_rank_5d(close: pd.Series) -> pd.Series:
    """
    dhrk_078_drawdown_acceleration_rank_5d
    ECONOMIC RATIONALE: Speed at which the drawdown is deepening.
    """
    base = (close / close.rolling(252).max() - 1).diff(21)
    return _rank_pct(base, 5)

def dhrk_079_drawdown_acceleration_lvl_21d(close: pd.Series) -> pd.Series:
    """
    dhrk_079_drawdown_acceleration_lvl_21d
    ECONOMIC RATIONALE: Speed at which the drawdown is deepening.
    """
    base = (close / close.rolling(252).max() - 1).diff(21)
    return _rolling_mean(base, 21)

def dhrk_080_drawdown_acceleration_zscore_21d(close: pd.Series) -> pd.Series:
    """
    dhrk_080_drawdown_acceleration_zscore_21d
    ECONOMIC RATIONALE: Speed at which the drawdown is deepening.
    """
    base = (close / close.rolling(252).max() - 1).diff(21)
    return _zscore_rolling(base, 21)

def dhrk_081_drawdown_acceleration_rank_21d(close: pd.Series) -> pd.Series:
    """
    dhrk_081_drawdown_acceleration_rank_21d
    ECONOMIC RATIONALE: Speed at which the drawdown is deepening.
    """
    base = (close / close.rolling(252).max() - 1).diff(21)
    return _rank_pct(base, 21)

def dhrk_082_drawdown_acceleration_lvl_63d(close: pd.Series) -> pd.Series:
    """
    dhrk_082_drawdown_acceleration_lvl_63d
    ECONOMIC RATIONALE: Speed at which the drawdown is deepening.
    """
    base = (close / close.rolling(252).max() - 1).diff(21)
    return _rolling_mean(base, 63)

def dhrk_083_drawdown_acceleration_zscore_63d(close: pd.Series) -> pd.Series:
    """
    dhrk_083_drawdown_acceleration_zscore_63d
    ECONOMIC RATIONALE: Speed at which the drawdown is deepening.
    """
    base = (close / close.rolling(252).max() - 1).diff(21)
    return _zscore_rolling(base, 63)

def dhrk_084_drawdown_acceleration_rank_63d(close: pd.Series) -> pd.Series:
    """
    dhrk_084_drawdown_acceleration_rank_63d
    ECONOMIC RATIONALE: Speed at which the drawdown is deepening.
    """
    base = (close / close.rolling(252).max() - 1).diff(21)
    return _rank_pct(base, 63)

def dhrk_085_drawdown_acceleration_lvl_126d(close: pd.Series) -> pd.Series:
    """
    dhrk_085_drawdown_acceleration_lvl_126d
    ECONOMIC RATIONALE: Speed at which the drawdown is deepening.
    """
    base = (close / close.rolling(252).max() - 1).diff(21)
    return _rolling_mean(base, 126)

def dhrk_086_drawdown_acceleration_zscore_126d(close: pd.Series) -> pd.Series:
    """
    dhrk_086_drawdown_acceleration_zscore_126d
    ECONOMIC RATIONALE: Speed at which the drawdown is deepening.
    """
    base = (close / close.rolling(252).max() - 1).diff(21)
    return _zscore_rolling(base, 126)

def dhrk_087_drawdown_acceleration_rank_126d(close: pd.Series) -> pd.Series:
    """
    dhrk_087_drawdown_acceleration_rank_126d
    ECONOMIC RATIONALE: Speed at which the drawdown is deepening.
    """
    base = (close / close.rolling(252).max() - 1).diff(21)
    return _rank_pct(base, 126)

def dhrk_088_drawdown_acceleration_lvl_252d(close: pd.Series) -> pd.Series:
    """
    dhrk_088_drawdown_acceleration_lvl_252d
    ECONOMIC RATIONALE: Speed at which the drawdown is deepening.
    """
    base = (close / close.rolling(252).max() - 1).diff(21)
    return _rolling_mean(base, 252)

def dhrk_089_drawdown_acceleration_zscore_252d(close: pd.Series) -> pd.Series:
    """
    dhrk_089_drawdown_acceleration_zscore_252d
    ECONOMIC RATIONALE: Speed at which the drawdown is deepening.
    """
    base = (close / close.rolling(252).max() - 1).diff(21)
    return _zscore_rolling(base, 252)

def dhrk_090_drawdown_acceleration_rank_252d(close: pd.Series) -> pd.Series:
    """
    dhrk_090_drawdown_acceleration_rank_252d
    ECONOMIC RATIONALE: Speed at which the drawdown is deepening.
    """
    base = (close / close.rolling(252).max() - 1).diff(21)
    return _rank_pct(base, 252)

def dhrk_091_drawdown_vol_ratio_lvl_5d(close: pd.Series) -> pd.Series:
    """
    dhrk_091_drawdown_vol_ratio_lvl_5d
    ECONOMIC RATIONALE: Drawdown depth normalized by volatility.
    """
    base = (close / close.rolling(252).max() - 1) / close.rolling(252).std()
    return _rolling_mean(base, 5)

def dhrk_092_drawdown_vol_ratio_zscore_5d(close: pd.Series) -> pd.Series:
    """
    dhrk_092_drawdown_vol_ratio_zscore_5d
    ECONOMIC RATIONALE: Drawdown depth normalized by volatility.
    """
    base = (close / close.rolling(252).max() - 1) / close.rolling(252).std()
    return _zscore_rolling(base, 5)

def dhrk_093_drawdown_vol_ratio_rank_5d(close: pd.Series) -> pd.Series:
    """
    dhrk_093_drawdown_vol_ratio_rank_5d
    ECONOMIC RATIONALE: Drawdown depth normalized by volatility.
    """
    base = (close / close.rolling(252).max() - 1) / close.rolling(252).std()
    return _rank_pct(base, 5)

def dhrk_094_drawdown_vol_ratio_lvl_21d(close: pd.Series) -> pd.Series:
    """
    dhrk_094_drawdown_vol_ratio_lvl_21d
    ECONOMIC RATIONALE: Drawdown depth normalized by volatility.
    """
    base = (close / close.rolling(252).max() - 1) / close.rolling(252).std()
    return _rolling_mean(base, 21)

def dhrk_095_drawdown_vol_ratio_zscore_21d(close: pd.Series) -> pd.Series:
    """
    dhrk_095_drawdown_vol_ratio_zscore_21d
    ECONOMIC RATIONALE: Drawdown depth normalized by volatility.
    """
    base = (close / close.rolling(252).max() - 1) / close.rolling(252).std()
    return _zscore_rolling(base, 21)

def dhrk_096_drawdown_vol_ratio_rank_21d(close: pd.Series) -> pd.Series:
    """
    dhrk_096_drawdown_vol_ratio_rank_21d
    ECONOMIC RATIONALE: Drawdown depth normalized by volatility.
    """
    base = (close / close.rolling(252).max() - 1) / close.rolling(252).std()
    return _rank_pct(base, 21)

def dhrk_097_drawdown_vol_ratio_lvl_63d(close: pd.Series) -> pd.Series:
    """
    dhrk_097_drawdown_vol_ratio_lvl_63d
    ECONOMIC RATIONALE: Drawdown depth normalized by volatility.
    """
    base = (close / close.rolling(252).max() - 1) / close.rolling(252).std()
    return _rolling_mean(base, 63)

def dhrk_098_drawdown_vol_ratio_zscore_63d(close: pd.Series) -> pd.Series:
    """
    dhrk_098_drawdown_vol_ratio_zscore_63d
    ECONOMIC RATIONALE: Drawdown depth normalized by volatility.
    """
    base = (close / close.rolling(252).max() - 1) / close.rolling(252).std()
    return _zscore_rolling(base, 63)

def dhrk_099_drawdown_vol_ratio_rank_63d(close: pd.Series) -> pd.Series:
    """
    dhrk_099_drawdown_vol_ratio_rank_63d
    ECONOMIC RATIONALE: Drawdown depth normalized by volatility.
    """
    base = (close / close.rolling(252).max() - 1) / close.rolling(252).std()
    return _rank_pct(base, 63)

def dhrk_100_drawdown_vol_ratio_lvl_126d(close: pd.Series) -> pd.Series:
    """
    dhrk_100_drawdown_vol_ratio_lvl_126d
    ECONOMIC RATIONALE: Drawdown depth normalized by volatility.
    """
    base = (close / close.rolling(252).max() - 1) / close.rolling(252).std()
    return _rolling_mean(base, 126)

def dhrk_101_drawdown_vol_ratio_zscore_126d(close: pd.Series) -> pd.Series:
    """
    dhrk_101_drawdown_vol_ratio_zscore_126d
    ECONOMIC RATIONALE: Drawdown depth normalized by volatility.
    """
    base = (close / close.rolling(252).max() - 1) / close.rolling(252).std()
    return _zscore_rolling(base, 126)

def dhrk_102_drawdown_vol_ratio_rank_126d(close: pd.Series) -> pd.Series:
    """
    dhrk_102_drawdown_vol_ratio_rank_126d
    ECONOMIC RATIONALE: Drawdown depth normalized by volatility.
    """
    base = (close / close.rolling(252).max() - 1) / close.rolling(252).std()
    return _rank_pct(base, 126)

def dhrk_103_drawdown_vol_ratio_lvl_252d(close: pd.Series) -> pd.Series:
    """
    dhrk_103_drawdown_vol_ratio_lvl_252d
    ECONOMIC RATIONALE: Drawdown depth normalized by volatility.
    """
    base = (close / close.rolling(252).max() - 1) / close.rolling(252).std()
    return _rolling_mean(base, 252)

def dhrk_104_drawdown_vol_ratio_zscore_252d(close: pd.Series) -> pd.Series:
    """
    dhrk_104_drawdown_vol_ratio_zscore_252d
    ECONOMIC RATIONALE: Drawdown depth normalized by volatility.
    """
    base = (close / close.rolling(252).max() - 1) / close.rolling(252).std()
    return _zscore_rolling(base, 252)

def dhrk_105_drawdown_vol_ratio_rank_252d(close: pd.Series) -> pd.Series:
    """
    dhrk_105_drawdown_vol_ratio_rank_252d
    ECONOMIC RATIONALE: Drawdown depth normalized by volatility.
    """
    base = (close / close.rolling(252).max() - 1) / close.rolling(252).std()
    return _rank_pct(base, 252)

def dhrk_106_recovery_from_lows_lvl_5d(close: pd.Series) -> pd.Series:
    """
    dhrk_106_recovery_from_lows_lvl_5d
    ECONOMIC RATIONALE: Percentage rally from the 52-week low.
    """
    base = close / close.rolling(252).min() - 1
    return _rolling_mean(base, 5)

def dhrk_107_recovery_from_lows_zscore_5d(close: pd.Series) -> pd.Series:
    """
    dhrk_107_recovery_from_lows_zscore_5d
    ECONOMIC RATIONALE: Percentage rally from the 52-week low.
    """
    base = close / close.rolling(252).min() - 1
    return _zscore_rolling(base, 5)

def dhrk_108_recovery_from_lows_rank_5d(close: pd.Series) -> pd.Series:
    """
    dhrk_108_recovery_from_lows_rank_5d
    ECONOMIC RATIONALE: Percentage rally from the 52-week low.
    """
    base = close / close.rolling(252).min() - 1
    return _rank_pct(base, 5)

def dhrk_109_recovery_from_lows_lvl_21d(close: pd.Series) -> pd.Series:
    """
    dhrk_109_recovery_from_lows_lvl_21d
    ECONOMIC RATIONALE: Percentage rally from the 52-week low.
    """
    base = close / close.rolling(252).min() - 1
    return _rolling_mean(base, 21)

def dhrk_110_recovery_from_lows_zscore_21d(close: pd.Series) -> pd.Series:
    """
    dhrk_110_recovery_from_lows_zscore_21d
    ECONOMIC RATIONALE: Percentage rally from the 52-week low.
    """
    base = close / close.rolling(252).min() - 1
    return _zscore_rolling(base, 21)

def dhrk_111_recovery_from_lows_rank_21d(close: pd.Series) -> pd.Series:
    """
    dhrk_111_recovery_from_lows_rank_21d
    ECONOMIC RATIONALE: Percentage rally from the 52-week low.
    """
    base = close / close.rolling(252).min() - 1
    return _rank_pct(base, 21)

def dhrk_112_recovery_from_lows_lvl_63d(close: pd.Series) -> pd.Series:
    """
    dhrk_112_recovery_from_lows_lvl_63d
    ECONOMIC RATIONALE: Percentage rally from the 52-week low.
    """
    base = close / close.rolling(252).min() - 1
    return _rolling_mean(base, 63)

def dhrk_113_recovery_from_lows_zscore_63d(close: pd.Series) -> pd.Series:
    """
    dhrk_113_recovery_from_lows_zscore_63d
    ECONOMIC RATIONALE: Percentage rally from the 52-week low.
    """
    base = close / close.rolling(252).min() - 1
    return _zscore_rolling(base, 63)

def dhrk_114_recovery_from_lows_rank_63d(close: pd.Series) -> pd.Series:
    """
    dhrk_114_recovery_from_lows_rank_63d
    ECONOMIC RATIONALE: Percentage rally from the 52-week low.
    """
    base = close / close.rolling(252).min() - 1
    return _rank_pct(base, 63)

def dhrk_115_recovery_from_lows_lvl_126d(close: pd.Series) -> pd.Series:
    """
    dhrk_115_recovery_from_lows_lvl_126d
    ECONOMIC RATIONALE: Percentage rally from the 52-week low.
    """
    base = close / close.rolling(252).min() - 1
    return _rolling_mean(base, 126)

def dhrk_116_recovery_from_lows_zscore_126d(close: pd.Series) -> pd.Series:
    """
    dhrk_116_recovery_from_lows_zscore_126d
    ECONOMIC RATIONALE: Percentage rally from the 52-week low.
    """
    base = close / close.rolling(252).min() - 1
    return _zscore_rolling(base, 126)

def dhrk_117_recovery_from_lows_rank_126d(close: pd.Series) -> pd.Series:
    """
    dhrk_117_recovery_from_lows_rank_126d
    ECONOMIC RATIONALE: Percentage rally from the 52-week low.
    """
    base = close / close.rolling(252).min() - 1
    return _rank_pct(base, 126)

def dhrk_118_recovery_from_lows_lvl_252d(close: pd.Series) -> pd.Series:
    """
    dhrk_118_recovery_from_lows_lvl_252d
    ECONOMIC RATIONALE: Percentage rally from the 52-week low.
    """
    base = close / close.rolling(252).min() - 1
    return _rolling_mean(base, 252)

def dhrk_119_recovery_from_lows_zscore_252d(close: pd.Series) -> pd.Series:
    """
    dhrk_119_recovery_from_lows_zscore_252d
    ECONOMIC RATIONALE: Percentage rally from the 52-week low.
    """
    base = close / close.rolling(252).min() - 1
    return _zscore_rolling(base, 252)

def dhrk_120_recovery_from_lows_rank_252d(close: pd.Series) -> pd.Series:
    """
    dhrk_120_recovery_from_lows_rank_252d
    ECONOMIC RATIONALE: Percentage rally from the 52-week low.
    """
    base = close / close.rolling(252).min() - 1
    return _rank_pct(base, 252)

# ── Registry ──────────────────────────────────────────────────────────────────
V108_REGISTRY_1 = {
    "dhrk_001_current_drawdown_lvl_5d": {"inputs": ["close"], "func": dhrk_001_current_drawdown_lvl_5d},
    "dhrk_002_current_drawdown_zscore_5d": {"inputs": ["close"], "func": dhrk_002_current_drawdown_zscore_5d},
    "dhrk_003_current_drawdown_rank_5d": {"inputs": ["close"], "func": dhrk_003_current_drawdown_rank_5d},
    "dhrk_004_current_drawdown_lvl_21d": {"inputs": ["close"], "func": dhrk_004_current_drawdown_lvl_21d},
    "dhrk_005_current_drawdown_zscore_21d": {"inputs": ["close"], "func": dhrk_005_current_drawdown_zscore_21d},
    "dhrk_006_current_drawdown_rank_21d": {"inputs": ["close"], "func": dhrk_006_current_drawdown_rank_21d},
    "dhrk_007_current_drawdown_lvl_63d": {"inputs": ["close"], "func": dhrk_007_current_drawdown_lvl_63d},
    "dhrk_008_current_drawdown_zscore_63d": {"inputs": ["close"], "func": dhrk_008_current_drawdown_zscore_63d},
    "dhrk_009_current_drawdown_rank_63d": {"inputs": ["close"], "func": dhrk_009_current_drawdown_rank_63d},
    "dhrk_010_current_drawdown_lvl_126d": {"inputs": ["close"], "func": dhrk_010_current_drawdown_lvl_126d},
    "dhrk_011_current_drawdown_zscore_126d": {"inputs": ["close"], "func": dhrk_011_current_drawdown_zscore_126d},
    "dhrk_012_current_drawdown_rank_126d": {"inputs": ["close"], "func": dhrk_012_current_drawdown_rank_126d},
    "dhrk_013_current_drawdown_lvl_252d": {"inputs": ["close"], "func": dhrk_013_current_drawdown_lvl_252d},
    "dhrk_014_current_drawdown_zscore_252d": {"inputs": ["close"], "func": dhrk_014_current_drawdown_zscore_252d},
    "dhrk_015_current_drawdown_rank_252d": {"inputs": ["close"], "func": dhrk_015_current_drawdown_rank_252d},
    "dhrk_016_drawdown_rank_252d_lvl_5d": {"inputs": ["close"], "func": dhrk_016_drawdown_rank_252d_lvl_5d},
    "dhrk_017_drawdown_rank_252d_zscore_5d": {"inputs": ["close"], "func": dhrk_017_drawdown_rank_252d_zscore_5d},
    "dhrk_018_drawdown_rank_252d_rank_5d": {"inputs": ["close"], "func": dhrk_018_drawdown_rank_252d_rank_5d},
    "dhrk_019_drawdown_rank_252d_lvl_21d": {"inputs": ["close"], "func": dhrk_019_drawdown_rank_252d_lvl_21d},
    "dhrk_020_drawdown_rank_252d_zscore_21d": {"inputs": ["close"], "func": dhrk_020_drawdown_rank_252d_zscore_21d},
    "dhrk_021_drawdown_rank_252d_rank_21d": {"inputs": ["close"], "func": dhrk_021_drawdown_rank_252d_rank_21d},
    "dhrk_022_drawdown_rank_252d_lvl_63d": {"inputs": ["close"], "func": dhrk_022_drawdown_rank_252d_lvl_63d},
    "dhrk_023_drawdown_rank_252d_zscore_63d": {"inputs": ["close"], "func": dhrk_023_drawdown_rank_252d_zscore_63d},
    "dhrk_024_drawdown_rank_252d_rank_63d": {"inputs": ["close"], "func": dhrk_024_drawdown_rank_252d_rank_63d},
    "dhrk_025_drawdown_rank_252d_lvl_126d": {"inputs": ["close"], "func": dhrk_025_drawdown_rank_252d_lvl_126d},
    "dhrk_026_drawdown_rank_252d_zscore_126d": {"inputs": ["close"], "func": dhrk_026_drawdown_rank_252d_zscore_126d},
    "dhrk_027_drawdown_rank_252d_rank_126d": {"inputs": ["close"], "func": dhrk_027_drawdown_rank_252d_rank_126d},
    "dhrk_028_drawdown_rank_252d_lvl_252d": {"inputs": ["close"], "func": dhrk_028_drawdown_rank_252d_lvl_252d},
    "dhrk_029_drawdown_rank_252d_zscore_252d": {"inputs": ["close"], "func": dhrk_029_drawdown_rank_252d_zscore_252d},
    "dhrk_030_drawdown_rank_252d_rank_252d": {"inputs": ["close"], "func": dhrk_030_drawdown_rank_252d_rank_252d},
    "dhrk_031_drawdown_severity_z_lvl_5d": {"inputs": ["close"], "func": dhrk_031_drawdown_severity_z_lvl_5d},
    "dhrk_032_drawdown_severity_z_zscore_5d": {"inputs": ["close"], "func": dhrk_032_drawdown_severity_z_zscore_5d},
    "dhrk_033_drawdown_severity_z_rank_5d": {"inputs": ["close"], "func": dhrk_033_drawdown_severity_z_rank_5d},
    "dhrk_034_drawdown_severity_z_lvl_21d": {"inputs": ["close"], "func": dhrk_034_drawdown_severity_z_lvl_21d},
    "dhrk_035_drawdown_severity_z_zscore_21d": {"inputs": ["close"], "func": dhrk_035_drawdown_severity_z_zscore_21d},
    "dhrk_036_drawdown_severity_z_rank_21d": {"inputs": ["close"], "func": dhrk_036_drawdown_severity_z_rank_21d},
    "dhrk_037_drawdown_severity_z_lvl_63d": {"inputs": ["close"], "func": dhrk_037_drawdown_severity_z_lvl_63d},
    "dhrk_038_drawdown_severity_z_zscore_63d": {"inputs": ["close"], "func": dhrk_038_drawdown_severity_z_zscore_63d},
    "dhrk_039_drawdown_severity_z_rank_63d": {"inputs": ["close"], "func": dhrk_039_drawdown_severity_z_rank_63d},
    "dhrk_040_drawdown_severity_z_lvl_126d": {"inputs": ["close"], "func": dhrk_040_drawdown_severity_z_lvl_126d},
    "dhrk_041_drawdown_severity_z_zscore_126d": {"inputs": ["close"], "func": dhrk_041_drawdown_severity_z_zscore_126d},
    "dhrk_042_drawdown_severity_z_rank_126d": {"inputs": ["close"], "func": dhrk_042_drawdown_severity_z_rank_126d},
    "dhrk_043_drawdown_severity_z_lvl_252d": {"inputs": ["close"], "func": dhrk_043_drawdown_severity_z_lvl_252d},
    "dhrk_044_drawdown_severity_z_zscore_252d": {"inputs": ["close"], "func": dhrk_044_drawdown_severity_z_zscore_252d},
    "dhrk_045_drawdown_severity_z_rank_252d": {"inputs": ["close"], "func": dhrk_045_drawdown_severity_z_rank_252d},
    "dhrk_046_drawdown_duration_lvl_5d": {"inputs": ["close"], "func": dhrk_046_drawdown_duration_lvl_5d},
    "dhrk_047_drawdown_duration_zscore_5d": {"inputs": ["close"], "func": dhrk_047_drawdown_duration_zscore_5d},
    "dhrk_048_drawdown_duration_rank_5d": {"inputs": ["close"], "func": dhrk_048_drawdown_duration_rank_5d},
    "dhrk_049_drawdown_duration_lvl_21d": {"inputs": ["close"], "func": dhrk_049_drawdown_duration_lvl_21d},
    "dhrk_050_drawdown_duration_zscore_21d": {"inputs": ["close"], "func": dhrk_050_drawdown_duration_zscore_21d},
    "dhrk_051_drawdown_duration_rank_21d": {"inputs": ["close"], "func": dhrk_051_drawdown_duration_rank_21d},
    "dhrk_052_drawdown_duration_lvl_63d": {"inputs": ["close"], "func": dhrk_052_drawdown_duration_lvl_63d},
    "dhrk_053_drawdown_duration_zscore_63d": {"inputs": ["close"], "func": dhrk_053_drawdown_duration_zscore_63d},
    "dhrk_054_drawdown_duration_rank_63d": {"inputs": ["close"], "func": dhrk_054_drawdown_duration_rank_63d},
    "dhrk_055_drawdown_duration_lvl_126d": {"inputs": ["close"], "func": dhrk_055_drawdown_duration_lvl_126d},
    "dhrk_056_drawdown_duration_zscore_126d": {"inputs": ["close"], "func": dhrk_056_drawdown_duration_zscore_126d},
    "dhrk_057_drawdown_duration_rank_126d": {"inputs": ["close"], "func": dhrk_057_drawdown_duration_rank_126d},
    "dhrk_058_drawdown_duration_lvl_252d": {"inputs": ["close"], "func": dhrk_058_drawdown_duration_lvl_252d},
    "dhrk_059_drawdown_duration_zscore_252d": {"inputs": ["close"], "func": dhrk_059_drawdown_duration_zscore_252d},
    "dhrk_060_drawdown_duration_rank_252d": {"inputs": ["close"], "func": dhrk_060_drawdown_duration_rank_252d},
    "dhrk_061_peak_to_trough_momentum_lvl_5d": {"inputs": ["close"], "func": dhrk_061_peak_to_trough_momentum_lvl_5d},
    "dhrk_062_peak_to_trough_momentum_zscore_5d": {"inputs": ["close"], "func": dhrk_062_peak_to_trough_momentum_zscore_5d},
    "dhrk_063_peak_to_trough_momentum_rank_5d": {"inputs": ["close"], "func": dhrk_063_peak_to_trough_momentum_rank_5d},
    "dhrk_064_peak_to_trough_momentum_lvl_21d": {"inputs": ["close"], "func": dhrk_064_peak_to_trough_momentum_lvl_21d},
    "dhrk_065_peak_to_trough_momentum_zscore_21d": {"inputs": ["close"], "func": dhrk_065_peak_to_trough_momentum_zscore_21d},
    "dhrk_066_peak_to_trough_momentum_rank_21d": {"inputs": ["close"], "func": dhrk_066_peak_to_trough_momentum_rank_21d},
    "dhrk_067_peak_to_trough_momentum_lvl_63d": {"inputs": ["close"], "func": dhrk_067_peak_to_trough_momentum_lvl_63d},
    "dhrk_068_peak_to_trough_momentum_zscore_63d": {"inputs": ["close"], "func": dhrk_068_peak_to_trough_momentum_zscore_63d},
    "dhrk_069_peak_to_trough_momentum_rank_63d": {"inputs": ["close"], "func": dhrk_069_peak_to_trough_momentum_rank_63d},
    "dhrk_070_peak_to_trough_momentum_lvl_126d": {"inputs": ["close"], "func": dhrk_070_peak_to_trough_momentum_lvl_126d},
    "dhrk_071_peak_to_trough_momentum_zscore_126d": {"inputs": ["close"], "func": dhrk_071_peak_to_trough_momentum_zscore_126d},
    "dhrk_072_peak_to_trough_momentum_rank_126d": {"inputs": ["close"], "func": dhrk_072_peak_to_trough_momentum_rank_126d},
    "dhrk_073_peak_to_trough_momentum_lvl_252d": {"inputs": ["close"], "func": dhrk_073_peak_to_trough_momentum_lvl_252d},
    "dhrk_074_peak_to_trough_momentum_zscore_252d": {"inputs": ["close"], "func": dhrk_074_peak_to_trough_momentum_zscore_252d},
    "dhrk_075_peak_to_trough_momentum_rank_252d": {"inputs": ["close"], "func": dhrk_075_peak_to_trough_momentum_rank_252d},
    "dhrk_076_drawdown_acceleration_lvl_5d": {"inputs": ["close"], "func": dhrk_076_drawdown_acceleration_lvl_5d},
    "dhrk_077_drawdown_acceleration_zscore_5d": {"inputs": ["close"], "func": dhrk_077_drawdown_acceleration_zscore_5d},
    "dhrk_078_drawdown_acceleration_rank_5d": {"inputs": ["close"], "func": dhrk_078_drawdown_acceleration_rank_5d},
    "dhrk_079_drawdown_acceleration_lvl_21d": {"inputs": ["close"], "func": dhrk_079_drawdown_acceleration_lvl_21d},
    "dhrk_080_drawdown_acceleration_zscore_21d": {"inputs": ["close"], "func": dhrk_080_drawdown_acceleration_zscore_21d},
    "dhrk_081_drawdown_acceleration_rank_21d": {"inputs": ["close"], "func": dhrk_081_drawdown_acceleration_rank_21d},
    "dhrk_082_drawdown_acceleration_lvl_63d": {"inputs": ["close"], "func": dhrk_082_drawdown_acceleration_lvl_63d},
    "dhrk_083_drawdown_acceleration_zscore_63d": {"inputs": ["close"], "func": dhrk_083_drawdown_acceleration_zscore_63d},
    "dhrk_084_drawdown_acceleration_rank_63d": {"inputs": ["close"], "func": dhrk_084_drawdown_acceleration_rank_63d},
    "dhrk_085_drawdown_acceleration_lvl_126d": {"inputs": ["close"], "func": dhrk_085_drawdown_acceleration_lvl_126d},
    "dhrk_086_drawdown_acceleration_zscore_126d": {"inputs": ["close"], "func": dhrk_086_drawdown_acceleration_zscore_126d},
    "dhrk_087_drawdown_acceleration_rank_126d": {"inputs": ["close"], "func": dhrk_087_drawdown_acceleration_rank_126d},
    "dhrk_088_drawdown_acceleration_lvl_252d": {"inputs": ["close"], "func": dhrk_088_drawdown_acceleration_lvl_252d},
    "dhrk_089_drawdown_acceleration_zscore_252d": {"inputs": ["close"], "func": dhrk_089_drawdown_acceleration_zscore_252d},
    "dhrk_090_drawdown_acceleration_rank_252d": {"inputs": ["close"], "func": dhrk_090_drawdown_acceleration_rank_252d},
    "dhrk_091_drawdown_vol_ratio_lvl_5d": {"inputs": ["close"], "func": dhrk_091_drawdown_vol_ratio_lvl_5d},
    "dhrk_092_drawdown_vol_ratio_zscore_5d": {"inputs": ["close"], "func": dhrk_092_drawdown_vol_ratio_zscore_5d},
    "dhrk_093_drawdown_vol_ratio_rank_5d": {"inputs": ["close"], "func": dhrk_093_drawdown_vol_ratio_rank_5d},
    "dhrk_094_drawdown_vol_ratio_lvl_21d": {"inputs": ["close"], "func": dhrk_094_drawdown_vol_ratio_lvl_21d},
    "dhrk_095_drawdown_vol_ratio_zscore_21d": {"inputs": ["close"], "func": dhrk_095_drawdown_vol_ratio_zscore_21d},
    "dhrk_096_drawdown_vol_ratio_rank_21d": {"inputs": ["close"], "func": dhrk_096_drawdown_vol_ratio_rank_21d},
    "dhrk_097_drawdown_vol_ratio_lvl_63d": {"inputs": ["close"], "func": dhrk_097_drawdown_vol_ratio_lvl_63d},
    "dhrk_098_drawdown_vol_ratio_zscore_63d": {"inputs": ["close"], "func": dhrk_098_drawdown_vol_ratio_zscore_63d},
    "dhrk_099_drawdown_vol_ratio_rank_63d": {"inputs": ["close"], "func": dhrk_099_drawdown_vol_ratio_rank_63d},
    "dhrk_100_drawdown_vol_ratio_lvl_126d": {"inputs": ["close"], "func": dhrk_100_drawdown_vol_ratio_lvl_126d},
    "dhrk_101_drawdown_vol_ratio_zscore_126d": {"inputs": ["close"], "func": dhrk_101_drawdown_vol_ratio_zscore_126d},
    "dhrk_102_drawdown_vol_ratio_rank_126d": {"inputs": ["close"], "func": dhrk_102_drawdown_vol_ratio_rank_126d},
    "dhrk_103_drawdown_vol_ratio_lvl_252d": {"inputs": ["close"], "func": dhrk_103_drawdown_vol_ratio_lvl_252d},
    "dhrk_104_drawdown_vol_ratio_zscore_252d": {"inputs": ["close"], "func": dhrk_104_drawdown_vol_ratio_zscore_252d},
    "dhrk_105_drawdown_vol_ratio_rank_252d": {"inputs": ["close"], "func": dhrk_105_drawdown_vol_ratio_rank_252d},
    "dhrk_106_recovery_from_lows_lvl_5d": {"inputs": ["close"], "func": dhrk_106_recovery_from_lows_lvl_5d},
    "dhrk_107_recovery_from_lows_zscore_5d": {"inputs": ["close"], "func": dhrk_107_recovery_from_lows_zscore_5d},
    "dhrk_108_recovery_from_lows_rank_5d": {"inputs": ["close"], "func": dhrk_108_recovery_from_lows_rank_5d},
    "dhrk_109_recovery_from_lows_lvl_21d": {"inputs": ["close"], "func": dhrk_109_recovery_from_lows_lvl_21d},
    "dhrk_110_recovery_from_lows_zscore_21d": {"inputs": ["close"], "func": dhrk_110_recovery_from_lows_zscore_21d},
    "dhrk_111_recovery_from_lows_rank_21d": {"inputs": ["close"], "func": dhrk_111_recovery_from_lows_rank_21d},
    "dhrk_112_recovery_from_lows_lvl_63d": {"inputs": ["close"], "func": dhrk_112_recovery_from_lows_lvl_63d},
    "dhrk_113_recovery_from_lows_zscore_63d": {"inputs": ["close"], "func": dhrk_113_recovery_from_lows_zscore_63d},
    "dhrk_114_recovery_from_lows_rank_63d": {"inputs": ["close"], "func": dhrk_114_recovery_from_lows_rank_63d},
    "dhrk_115_recovery_from_lows_lvl_126d": {"inputs": ["close"], "func": dhrk_115_recovery_from_lows_lvl_126d},
    "dhrk_116_recovery_from_lows_zscore_126d": {"inputs": ["close"], "func": dhrk_116_recovery_from_lows_zscore_126d},
    "dhrk_117_recovery_from_lows_rank_126d": {"inputs": ["close"], "func": dhrk_117_recovery_from_lows_rank_126d},
    "dhrk_118_recovery_from_lows_lvl_252d": {"inputs": ["close"], "func": dhrk_118_recovery_from_lows_lvl_252d},
    "dhrk_119_recovery_from_lows_zscore_252d": {"inputs": ["close"], "func": dhrk_119_recovery_from_lows_zscore_252d},
    "dhrk_120_recovery_from_lows_rank_252d": {"inputs": ["close"], "func": dhrk_120_recovery_from_lows_rank_252d},
}
