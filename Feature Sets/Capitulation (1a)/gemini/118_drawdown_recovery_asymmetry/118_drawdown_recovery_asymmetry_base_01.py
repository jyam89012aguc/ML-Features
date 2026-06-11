"""
118_drawdown_recovery_asymmetry — Base Features Part 1
Domain: drawdown_recovery_asymmetry
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

def dras_001_downside_speed_lvl_5d(close: pd.Series) -> pd.Series:
    """
    dras_001_downside_speed_lvl_5d
    ECONOMIC RATIONALE: Average speed of price drops.
    """
    base = close.diff(21).clip(upper=0).abs() / 21
    return _rolling_mean(base, 5)

def dras_002_downside_speed_zscore_5d(close: pd.Series) -> pd.Series:
    """
    dras_002_downside_speed_zscore_5d
    ECONOMIC RATIONALE: Average speed of price drops.
    """
    base = close.diff(21).clip(upper=0).abs() / 21
    return _zscore_rolling(base, 5)

def dras_003_downside_speed_rank_5d(close: pd.Series) -> pd.Series:
    """
    dras_003_downside_speed_rank_5d
    ECONOMIC RATIONALE: Average speed of price drops.
    """
    base = close.diff(21).clip(upper=0).abs() / 21
    return _rank_pct(base, 5)

def dras_004_downside_speed_lvl_21d(close: pd.Series) -> pd.Series:
    """
    dras_004_downside_speed_lvl_21d
    ECONOMIC RATIONALE: Average speed of price drops.
    """
    base = close.diff(21).clip(upper=0).abs() / 21
    return _rolling_mean(base, 21)

def dras_005_downside_speed_zscore_21d(close: pd.Series) -> pd.Series:
    """
    dras_005_downside_speed_zscore_21d
    ECONOMIC RATIONALE: Average speed of price drops.
    """
    base = close.diff(21).clip(upper=0).abs() / 21
    return _zscore_rolling(base, 21)

def dras_006_downside_speed_rank_21d(close: pd.Series) -> pd.Series:
    """
    dras_006_downside_speed_rank_21d
    ECONOMIC RATIONALE: Average speed of price drops.
    """
    base = close.diff(21).clip(upper=0).abs() / 21
    return _rank_pct(base, 21)

def dras_007_downside_speed_lvl_63d(close: pd.Series) -> pd.Series:
    """
    dras_007_downside_speed_lvl_63d
    ECONOMIC RATIONALE: Average speed of price drops.
    """
    base = close.diff(21).clip(upper=0).abs() / 21
    return _rolling_mean(base, 63)

def dras_008_downside_speed_zscore_63d(close: pd.Series) -> pd.Series:
    """
    dras_008_downside_speed_zscore_63d
    ECONOMIC RATIONALE: Average speed of price drops.
    """
    base = close.diff(21).clip(upper=0).abs() / 21
    return _zscore_rolling(base, 63)

def dras_009_downside_speed_rank_63d(close: pd.Series) -> pd.Series:
    """
    dras_009_downside_speed_rank_63d
    ECONOMIC RATIONALE: Average speed of price drops.
    """
    base = close.diff(21).clip(upper=0).abs() / 21
    return _rank_pct(base, 63)

def dras_010_downside_speed_lvl_126d(close: pd.Series) -> pd.Series:
    """
    dras_010_downside_speed_lvl_126d
    ECONOMIC RATIONALE: Average speed of price drops.
    """
    base = close.diff(21).clip(upper=0).abs() / 21
    return _rolling_mean(base, 126)

def dras_011_downside_speed_zscore_126d(close: pd.Series) -> pd.Series:
    """
    dras_011_downside_speed_zscore_126d
    ECONOMIC RATIONALE: Average speed of price drops.
    """
    base = close.diff(21).clip(upper=0).abs() / 21
    return _zscore_rolling(base, 126)

def dras_012_downside_speed_rank_126d(close: pd.Series) -> pd.Series:
    """
    dras_012_downside_speed_rank_126d
    ECONOMIC RATIONALE: Average speed of price drops.
    """
    base = close.diff(21).clip(upper=0).abs() / 21
    return _rank_pct(base, 126)

def dras_013_downside_speed_lvl_252d(close: pd.Series) -> pd.Series:
    """
    dras_013_downside_speed_lvl_252d
    ECONOMIC RATIONALE: Average speed of price drops.
    """
    base = close.diff(21).clip(upper=0).abs() / 21
    return _rolling_mean(base, 252)

def dras_014_downside_speed_zscore_252d(close: pd.Series) -> pd.Series:
    """
    dras_014_downside_speed_zscore_252d
    ECONOMIC RATIONALE: Average speed of price drops.
    """
    base = close.diff(21).clip(upper=0).abs() / 21
    return _zscore_rolling(base, 252)

def dras_015_downside_speed_rank_252d(close: pd.Series) -> pd.Series:
    """
    dras_015_downside_speed_rank_252d
    ECONOMIC RATIONALE: Average speed of price drops.
    """
    base = close.diff(21).clip(upper=0).abs() / 21
    return _rank_pct(base, 252)

def dras_016_upside_speed_lvl_5d(close: pd.Series) -> pd.Series:
    """
    dras_016_upside_speed_lvl_5d
    ECONOMIC RATIONALE: Average speed of price rallies.
    """
    base = close.diff(21).clip(lower=0) / 21
    return _rolling_mean(base, 5)

def dras_017_upside_speed_zscore_5d(close: pd.Series) -> pd.Series:
    """
    dras_017_upside_speed_zscore_5d
    ECONOMIC RATIONALE: Average speed of price rallies.
    """
    base = close.diff(21).clip(lower=0) / 21
    return _zscore_rolling(base, 5)

def dras_018_upside_speed_rank_5d(close: pd.Series) -> pd.Series:
    """
    dras_018_upside_speed_rank_5d
    ECONOMIC RATIONALE: Average speed of price rallies.
    """
    base = close.diff(21).clip(lower=0) / 21
    return _rank_pct(base, 5)

def dras_019_upside_speed_lvl_21d(close: pd.Series) -> pd.Series:
    """
    dras_019_upside_speed_lvl_21d
    ECONOMIC RATIONALE: Average speed of price rallies.
    """
    base = close.diff(21).clip(lower=0) / 21
    return _rolling_mean(base, 21)

def dras_020_upside_speed_zscore_21d(close: pd.Series) -> pd.Series:
    """
    dras_020_upside_speed_zscore_21d
    ECONOMIC RATIONALE: Average speed of price rallies.
    """
    base = close.diff(21).clip(lower=0) / 21
    return _zscore_rolling(base, 21)

def dras_021_upside_speed_rank_21d(close: pd.Series) -> pd.Series:
    """
    dras_021_upside_speed_rank_21d
    ECONOMIC RATIONALE: Average speed of price rallies.
    """
    base = close.diff(21).clip(lower=0) / 21
    return _rank_pct(base, 21)

def dras_022_upside_speed_lvl_63d(close: pd.Series) -> pd.Series:
    """
    dras_022_upside_speed_lvl_63d
    ECONOMIC RATIONALE: Average speed of price rallies.
    """
    base = close.diff(21).clip(lower=0) / 21
    return _rolling_mean(base, 63)

def dras_023_upside_speed_zscore_63d(close: pd.Series) -> pd.Series:
    """
    dras_023_upside_speed_zscore_63d
    ECONOMIC RATIONALE: Average speed of price rallies.
    """
    base = close.diff(21).clip(lower=0) / 21
    return _zscore_rolling(base, 63)

def dras_024_upside_speed_rank_63d(close: pd.Series) -> pd.Series:
    """
    dras_024_upside_speed_rank_63d
    ECONOMIC RATIONALE: Average speed of price rallies.
    """
    base = close.diff(21).clip(lower=0) / 21
    return _rank_pct(base, 63)

def dras_025_upside_speed_lvl_126d(close: pd.Series) -> pd.Series:
    """
    dras_025_upside_speed_lvl_126d
    ECONOMIC RATIONALE: Average speed of price rallies.
    """
    base = close.diff(21).clip(lower=0) / 21
    return _rolling_mean(base, 126)

def dras_026_upside_speed_zscore_126d(close: pd.Series) -> pd.Series:
    """
    dras_026_upside_speed_zscore_126d
    ECONOMIC RATIONALE: Average speed of price rallies.
    """
    base = close.diff(21).clip(lower=0) / 21
    return _zscore_rolling(base, 126)

def dras_027_upside_speed_rank_126d(close: pd.Series) -> pd.Series:
    """
    dras_027_upside_speed_rank_126d
    ECONOMIC RATIONALE: Average speed of price rallies.
    """
    base = close.diff(21).clip(lower=0) / 21
    return _rank_pct(base, 126)

def dras_028_upside_speed_lvl_252d(close: pd.Series) -> pd.Series:
    """
    dras_028_upside_speed_lvl_252d
    ECONOMIC RATIONALE: Average speed of price rallies.
    """
    base = close.diff(21).clip(lower=0) / 21
    return _rolling_mean(base, 252)

def dras_029_upside_speed_zscore_252d(close: pd.Series) -> pd.Series:
    """
    dras_029_upside_speed_zscore_252d
    ECONOMIC RATIONALE: Average speed of price rallies.
    """
    base = close.diff(21).clip(lower=0) / 21
    return _zscore_rolling(base, 252)

def dras_030_upside_speed_rank_252d(close: pd.Series) -> pd.Series:
    """
    dras_030_upside_speed_rank_252d
    ECONOMIC RATIONALE: Average speed of price rallies.
    """
    base = close.diff(21).clip(lower=0) / 21
    return _rank_pct(base, 252)

def dras_031_recovery_asymmetry_ratio_lvl_5d(close: pd.Series) -> pd.Series:
    """
    dras_031_recovery_asymmetry_ratio_lvl_5d
    ECONOMIC RATIONALE: Ratio of recovery speed to drawdown speed.
    """
    base = (close.diff(21).clip(lower=0).rolling(63).mean()) / (close.diff(21).clip(upper=0).abs().rolling(63).mean()).replace(0, 1e-9)
    return _rolling_mean(base, 5)

def dras_032_recovery_asymmetry_ratio_zscore_5d(close: pd.Series) -> pd.Series:
    """
    dras_032_recovery_asymmetry_ratio_zscore_5d
    ECONOMIC RATIONALE: Ratio of recovery speed to drawdown speed.
    """
    base = (close.diff(21).clip(lower=0).rolling(63).mean()) / (close.diff(21).clip(upper=0).abs().rolling(63).mean()).replace(0, 1e-9)
    return _zscore_rolling(base, 5)

def dras_033_recovery_asymmetry_ratio_rank_5d(close: pd.Series) -> pd.Series:
    """
    dras_033_recovery_asymmetry_ratio_rank_5d
    ECONOMIC RATIONALE: Ratio of recovery speed to drawdown speed.
    """
    base = (close.diff(21).clip(lower=0).rolling(63).mean()) / (close.diff(21).clip(upper=0).abs().rolling(63).mean()).replace(0, 1e-9)
    return _rank_pct(base, 5)

def dras_034_recovery_asymmetry_ratio_lvl_21d(close: pd.Series) -> pd.Series:
    """
    dras_034_recovery_asymmetry_ratio_lvl_21d
    ECONOMIC RATIONALE: Ratio of recovery speed to drawdown speed.
    """
    base = (close.diff(21).clip(lower=0).rolling(63).mean()) / (close.diff(21).clip(upper=0).abs().rolling(63).mean()).replace(0, 1e-9)
    return _rolling_mean(base, 21)

def dras_035_recovery_asymmetry_ratio_zscore_21d(close: pd.Series) -> pd.Series:
    """
    dras_035_recovery_asymmetry_ratio_zscore_21d
    ECONOMIC RATIONALE: Ratio of recovery speed to drawdown speed.
    """
    base = (close.diff(21).clip(lower=0).rolling(63).mean()) / (close.diff(21).clip(upper=0).abs().rolling(63).mean()).replace(0, 1e-9)
    return _zscore_rolling(base, 21)

def dras_036_recovery_asymmetry_ratio_rank_21d(close: pd.Series) -> pd.Series:
    """
    dras_036_recovery_asymmetry_ratio_rank_21d
    ECONOMIC RATIONALE: Ratio of recovery speed to drawdown speed.
    """
    base = (close.diff(21).clip(lower=0).rolling(63).mean()) / (close.diff(21).clip(upper=0).abs().rolling(63).mean()).replace(0, 1e-9)
    return _rank_pct(base, 21)

def dras_037_recovery_asymmetry_ratio_lvl_63d(close: pd.Series) -> pd.Series:
    """
    dras_037_recovery_asymmetry_ratio_lvl_63d
    ECONOMIC RATIONALE: Ratio of recovery speed to drawdown speed.
    """
    base = (close.diff(21).clip(lower=0).rolling(63).mean()) / (close.diff(21).clip(upper=0).abs().rolling(63).mean()).replace(0, 1e-9)
    return _rolling_mean(base, 63)

def dras_038_recovery_asymmetry_ratio_zscore_63d(close: pd.Series) -> pd.Series:
    """
    dras_038_recovery_asymmetry_ratio_zscore_63d
    ECONOMIC RATIONALE: Ratio of recovery speed to drawdown speed.
    """
    base = (close.diff(21).clip(lower=0).rolling(63).mean()) / (close.diff(21).clip(upper=0).abs().rolling(63).mean()).replace(0, 1e-9)
    return _zscore_rolling(base, 63)

def dras_039_recovery_asymmetry_ratio_rank_63d(close: pd.Series) -> pd.Series:
    """
    dras_039_recovery_asymmetry_ratio_rank_63d
    ECONOMIC RATIONALE: Ratio of recovery speed to drawdown speed.
    """
    base = (close.diff(21).clip(lower=0).rolling(63).mean()) / (close.diff(21).clip(upper=0).abs().rolling(63).mean()).replace(0, 1e-9)
    return _rank_pct(base, 63)

def dras_040_recovery_asymmetry_ratio_lvl_126d(close: pd.Series) -> pd.Series:
    """
    dras_040_recovery_asymmetry_ratio_lvl_126d
    ECONOMIC RATIONALE: Ratio of recovery speed to drawdown speed.
    """
    base = (close.diff(21).clip(lower=0).rolling(63).mean()) / (close.diff(21).clip(upper=0).abs().rolling(63).mean()).replace(0, 1e-9)
    return _rolling_mean(base, 126)

def dras_041_recovery_asymmetry_ratio_zscore_126d(close: pd.Series) -> pd.Series:
    """
    dras_041_recovery_asymmetry_ratio_zscore_126d
    ECONOMIC RATIONALE: Ratio of recovery speed to drawdown speed.
    """
    base = (close.diff(21).clip(lower=0).rolling(63).mean()) / (close.diff(21).clip(upper=0).abs().rolling(63).mean()).replace(0, 1e-9)
    return _zscore_rolling(base, 126)

def dras_042_recovery_asymmetry_ratio_rank_126d(close: pd.Series) -> pd.Series:
    """
    dras_042_recovery_asymmetry_ratio_rank_126d
    ECONOMIC RATIONALE: Ratio of recovery speed to drawdown speed.
    """
    base = (close.diff(21).clip(lower=0).rolling(63).mean()) / (close.diff(21).clip(upper=0).abs().rolling(63).mean()).replace(0, 1e-9)
    return _rank_pct(base, 126)

def dras_043_recovery_asymmetry_ratio_lvl_252d(close: pd.Series) -> pd.Series:
    """
    dras_043_recovery_asymmetry_ratio_lvl_252d
    ECONOMIC RATIONALE: Ratio of recovery speed to drawdown speed.
    """
    base = (close.diff(21).clip(lower=0).rolling(63).mean()) / (close.diff(21).clip(upper=0).abs().rolling(63).mean()).replace(0, 1e-9)
    return _rolling_mean(base, 252)

def dras_044_recovery_asymmetry_ratio_zscore_252d(close: pd.Series) -> pd.Series:
    """
    dras_044_recovery_asymmetry_ratio_zscore_252d
    ECONOMIC RATIONALE: Ratio of recovery speed to drawdown speed.
    """
    base = (close.diff(21).clip(lower=0).rolling(63).mean()) / (close.diff(21).clip(upper=0).abs().rolling(63).mean()).replace(0, 1e-9)
    return _zscore_rolling(base, 252)

def dras_045_recovery_asymmetry_ratio_rank_252d(close: pd.Series) -> pd.Series:
    """
    dras_045_recovery_asymmetry_ratio_rank_252d
    ECONOMIC RATIONALE: Ratio of recovery speed to drawdown speed.
    """
    base = (close.diff(21).clip(lower=0).rolling(63).mean()) / (close.diff(21).clip(upper=0).abs().rolling(63).mean()).replace(0, 1e-9)
    return _rank_pct(base, 252)

def dras_046_drawdown_recovery_lag_lvl_5d(close: pd.Series) -> pd.Series:
    """
    dras_046_drawdown_recovery_lag_lvl_5d
    ECONOMIC RATIONALE: Time spent in drawdown vs time spent in recovery.
    """
    base = (close.rolling(252).max().shift(1) > close).rolling(252).sum()
    return _rolling_mean(base, 5)

def dras_047_drawdown_recovery_lag_zscore_5d(close: pd.Series) -> pd.Series:
    """
    dras_047_drawdown_recovery_lag_zscore_5d
    ECONOMIC RATIONALE: Time spent in drawdown vs time spent in recovery.
    """
    base = (close.rolling(252).max().shift(1) > close).rolling(252).sum()
    return _zscore_rolling(base, 5)

def dras_048_drawdown_recovery_lag_rank_5d(close: pd.Series) -> pd.Series:
    """
    dras_048_drawdown_recovery_lag_rank_5d
    ECONOMIC RATIONALE: Time spent in drawdown vs time spent in recovery.
    """
    base = (close.rolling(252).max().shift(1) > close).rolling(252).sum()
    return _rank_pct(base, 5)

def dras_049_drawdown_recovery_lag_lvl_21d(close: pd.Series) -> pd.Series:
    """
    dras_049_drawdown_recovery_lag_lvl_21d
    ECONOMIC RATIONALE: Time spent in drawdown vs time spent in recovery.
    """
    base = (close.rolling(252).max().shift(1) > close).rolling(252).sum()
    return _rolling_mean(base, 21)

def dras_050_drawdown_recovery_lag_zscore_21d(close: pd.Series) -> pd.Series:
    """
    dras_050_drawdown_recovery_lag_zscore_21d
    ECONOMIC RATIONALE: Time spent in drawdown vs time spent in recovery.
    """
    base = (close.rolling(252).max().shift(1) > close).rolling(252).sum()
    return _zscore_rolling(base, 21)

def dras_051_drawdown_recovery_lag_rank_21d(close: pd.Series) -> pd.Series:
    """
    dras_051_drawdown_recovery_lag_rank_21d
    ECONOMIC RATIONALE: Time spent in drawdown vs time spent in recovery.
    """
    base = (close.rolling(252).max().shift(1) > close).rolling(252).sum()
    return _rank_pct(base, 21)

def dras_052_drawdown_recovery_lag_lvl_63d(close: pd.Series) -> pd.Series:
    """
    dras_052_drawdown_recovery_lag_lvl_63d
    ECONOMIC RATIONALE: Time spent in drawdown vs time spent in recovery.
    """
    base = (close.rolling(252).max().shift(1) > close).rolling(252).sum()
    return _rolling_mean(base, 63)

def dras_053_drawdown_recovery_lag_zscore_63d(close: pd.Series) -> pd.Series:
    """
    dras_053_drawdown_recovery_lag_zscore_63d
    ECONOMIC RATIONALE: Time spent in drawdown vs time spent in recovery.
    """
    base = (close.rolling(252).max().shift(1) > close).rolling(252).sum()
    return _zscore_rolling(base, 63)

def dras_054_drawdown_recovery_lag_rank_63d(close: pd.Series) -> pd.Series:
    """
    dras_054_drawdown_recovery_lag_rank_63d
    ECONOMIC RATIONALE: Time spent in drawdown vs time spent in recovery.
    """
    base = (close.rolling(252).max().shift(1) > close).rolling(252).sum()
    return _rank_pct(base, 63)

def dras_055_drawdown_recovery_lag_lvl_126d(close: pd.Series) -> pd.Series:
    """
    dras_055_drawdown_recovery_lag_lvl_126d
    ECONOMIC RATIONALE: Time spent in drawdown vs time spent in recovery.
    """
    base = (close.rolling(252).max().shift(1) > close).rolling(252).sum()
    return _rolling_mean(base, 126)

def dras_056_drawdown_recovery_lag_zscore_126d(close: pd.Series) -> pd.Series:
    """
    dras_056_drawdown_recovery_lag_zscore_126d
    ECONOMIC RATIONALE: Time spent in drawdown vs time spent in recovery.
    """
    base = (close.rolling(252).max().shift(1) > close).rolling(252).sum()
    return _zscore_rolling(base, 126)

def dras_057_drawdown_recovery_lag_rank_126d(close: pd.Series) -> pd.Series:
    """
    dras_057_drawdown_recovery_lag_rank_126d
    ECONOMIC RATIONALE: Time spent in drawdown vs time spent in recovery.
    """
    base = (close.rolling(252).max().shift(1) > close).rolling(252).sum()
    return _rank_pct(base, 126)

def dras_058_drawdown_recovery_lag_lvl_252d(close: pd.Series) -> pd.Series:
    """
    dras_058_drawdown_recovery_lag_lvl_252d
    ECONOMIC RATIONALE: Time spent in drawdown vs time spent in recovery.
    """
    base = (close.rolling(252).max().shift(1) > close).rolling(252).sum()
    return _rolling_mean(base, 252)

def dras_059_drawdown_recovery_lag_zscore_252d(close: pd.Series) -> pd.Series:
    """
    dras_059_drawdown_recovery_lag_zscore_252d
    ECONOMIC RATIONALE: Time spent in drawdown vs time spent in recovery.
    """
    base = (close.rolling(252).max().shift(1) > close).rolling(252).sum()
    return _zscore_rolling(base, 252)

def dras_060_drawdown_recovery_lag_rank_252d(close: pd.Series) -> pd.Series:
    """
    dras_060_drawdown_recovery_lag_rank_252d
    ECONOMIC RATIONALE: Time spent in drawdown vs time spent in recovery.
    """
    base = (close.rolling(252).max().shift(1) > close).rolling(252).sum()
    return _rank_pct(base, 252)

def dras_061_asymmetry_zscore_lvl_5d(close: pd.Series) -> pd.Series:
    """
    dras_061_asymmetry_zscore_lvl_5d
    ECONOMIC RATIONALE: Anomaly in return symmetry.
    """
    base = _zscore_rolling((close.diff(1).clip(lower=0).mean() / close.diff(1).clip(upper=0).abs().mean()), 252)
    return _rolling_mean(base, 5)

def dras_062_asymmetry_zscore_zscore_5d(close: pd.Series) -> pd.Series:
    """
    dras_062_asymmetry_zscore_zscore_5d
    ECONOMIC RATIONALE: Anomaly in return symmetry.
    """
    base = _zscore_rolling((close.diff(1).clip(lower=0).mean() / close.diff(1).clip(upper=0).abs().mean()), 252)
    return _zscore_rolling(base, 5)

def dras_063_asymmetry_zscore_rank_5d(close: pd.Series) -> pd.Series:
    """
    dras_063_asymmetry_zscore_rank_5d
    ECONOMIC RATIONALE: Anomaly in return symmetry.
    """
    base = _zscore_rolling((close.diff(1).clip(lower=0).mean() / close.diff(1).clip(upper=0).abs().mean()), 252)
    return _rank_pct(base, 5)

def dras_064_asymmetry_zscore_lvl_21d(close: pd.Series) -> pd.Series:
    """
    dras_064_asymmetry_zscore_lvl_21d
    ECONOMIC RATIONALE: Anomaly in return symmetry.
    """
    base = _zscore_rolling((close.diff(1).clip(lower=0).mean() / close.diff(1).clip(upper=0).abs().mean()), 252)
    return _rolling_mean(base, 21)

def dras_065_asymmetry_zscore_zscore_21d(close: pd.Series) -> pd.Series:
    """
    dras_065_asymmetry_zscore_zscore_21d
    ECONOMIC RATIONALE: Anomaly in return symmetry.
    """
    base = _zscore_rolling((close.diff(1).clip(lower=0).mean() / close.diff(1).clip(upper=0).abs().mean()), 252)
    return _zscore_rolling(base, 21)

def dras_066_asymmetry_zscore_rank_21d(close: pd.Series) -> pd.Series:
    """
    dras_066_asymmetry_zscore_rank_21d
    ECONOMIC RATIONALE: Anomaly in return symmetry.
    """
    base = _zscore_rolling((close.diff(1).clip(lower=0).mean() / close.diff(1).clip(upper=0).abs().mean()), 252)
    return _rank_pct(base, 21)

def dras_067_asymmetry_zscore_lvl_63d(close: pd.Series) -> pd.Series:
    """
    dras_067_asymmetry_zscore_lvl_63d
    ECONOMIC RATIONALE: Anomaly in return symmetry.
    """
    base = _zscore_rolling((close.diff(1).clip(lower=0).mean() / close.diff(1).clip(upper=0).abs().mean()), 252)
    return _rolling_mean(base, 63)

def dras_068_asymmetry_zscore_zscore_63d(close: pd.Series) -> pd.Series:
    """
    dras_068_asymmetry_zscore_zscore_63d
    ECONOMIC RATIONALE: Anomaly in return symmetry.
    """
    base = _zscore_rolling((close.diff(1).clip(lower=0).mean() / close.diff(1).clip(upper=0).abs().mean()), 252)
    return _zscore_rolling(base, 63)

def dras_069_asymmetry_zscore_rank_63d(close: pd.Series) -> pd.Series:
    """
    dras_069_asymmetry_zscore_rank_63d
    ECONOMIC RATIONALE: Anomaly in return symmetry.
    """
    base = _zscore_rolling((close.diff(1).clip(lower=0).mean() / close.diff(1).clip(upper=0).abs().mean()), 252)
    return _rank_pct(base, 63)

def dras_070_asymmetry_zscore_lvl_126d(close: pd.Series) -> pd.Series:
    """
    dras_070_asymmetry_zscore_lvl_126d
    ECONOMIC RATIONALE: Anomaly in return symmetry.
    """
    base = _zscore_rolling((close.diff(1).clip(lower=0).mean() / close.diff(1).clip(upper=0).abs().mean()), 252)
    return _rolling_mean(base, 126)

def dras_071_asymmetry_zscore_zscore_126d(close: pd.Series) -> pd.Series:
    """
    dras_071_asymmetry_zscore_zscore_126d
    ECONOMIC RATIONALE: Anomaly in return symmetry.
    """
    base = _zscore_rolling((close.diff(1).clip(lower=0).mean() / close.diff(1).clip(upper=0).abs().mean()), 252)
    return _zscore_rolling(base, 126)

def dras_072_asymmetry_zscore_rank_126d(close: pd.Series) -> pd.Series:
    """
    dras_072_asymmetry_zscore_rank_126d
    ECONOMIC RATIONALE: Anomaly in return symmetry.
    """
    base = _zscore_rolling((close.diff(1).clip(lower=0).mean() / close.diff(1).clip(upper=0).abs().mean()), 252)
    return _rank_pct(base, 126)

def dras_073_asymmetry_zscore_lvl_252d(close: pd.Series) -> pd.Series:
    """
    dras_073_asymmetry_zscore_lvl_252d
    ECONOMIC RATIONALE: Anomaly in return symmetry.
    """
    base = _zscore_rolling((close.diff(1).clip(lower=0).mean() / close.diff(1).clip(upper=0).abs().mean()), 252)
    return _rolling_mean(base, 252)

def dras_074_asymmetry_zscore_zscore_252d(close: pd.Series) -> pd.Series:
    """
    dras_074_asymmetry_zscore_zscore_252d
    ECONOMIC RATIONALE: Anomaly in return symmetry.
    """
    base = _zscore_rolling((close.diff(1).clip(lower=0).mean() / close.diff(1).clip(upper=0).abs().mean()), 252)
    return _zscore_rolling(base, 252)

def dras_075_asymmetry_zscore_rank_252d(close: pd.Series) -> pd.Series:
    """
    dras_075_asymmetry_zscore_rank_252d
    ECONOMIC RATIONALE: Anomaly in return symmetry.
    """
    base = _zscore_rolling((close.diff(1).clip(lower=0).mean() / close.diff(1).clip(upper=0).abs().mean()), 252)
    return _rank_pct(base, 252)

def dras_076_drawdown_severity_skew_lvl_5d(close: pd.Series) -> pd.Series:
    """
    dras_076_drawdown_severity_skew_lvl_5d
    ECONOMIC RATIONALE: Skewness of negative returns only.
    """
    base = close.pct_change(1).rolling(252).apply(lambda x: x[x < 0].skew())
    return _rolling_mean(base, 5)

def dras_077_drawdown_severity_skew_zscore_5d(close: pd.Series) -> pd.Series:
    """
    dras_077_drawdown_severity_skew_zscore_5d
    ECONOMIC RATIONALE: Skewness of negative returns only.
    """
    base = close.pct_change(1).rolling(252).apply(lambda x: x[x < 0].skew())
    return _zscore_rolling(base, 5)

def dras_078_drawdown_severity_skew_rank_5d(close: pd.Series) -> pd.Series:
    """
    dras_078_drawdown_severity_skew_rank_5d
    ECONOMIC RATIONALE: Skewness of negative returns only.
    """
    base = close.pct_change(1).rolling(252).apply(lambda x: x[x < 0].skew())
    return _rank_pct(base, 5)

def dras_079_drawdown_severity_skew_lvl_21d(close: pd.Series) -> pd.Series:
    """
    dras_079_drawdown_severity_skew_lvl_21d
    ECONOMIC RATIONALE: Skewness of negative returns only.
    """
    base = close.pct_change(1).rolling(252).apply(lambda x: x[x < 0].skew())
    return _rolling_mean(base, 21)

def dras_080_drawdown_severity_skew_zscore_21d(close: pd.Series) -> pd.Series:
    """
    dras_080_drawdown_severity_skew_zscore_21d
    ECONOMIC RATIONALE: Skewness of negative returns only.
    """
    base = close.pct_change(1).rolling(252).apply(lambda x: x[x < 0].skew())
    return _zscore_rolling(base, 21)

def dras_081_drawdown_severity_skew_rank_21d(close: pd.Series) -> pd.Series:
    """
    dras_081_drawdown_severity_skew_rank_21d
    ECONOMIC RATIONALE: Skewness of negative returns only.
    """
    base = close.pct_change(1).rolling(252).apply(lambda x: x[x < 0].skew())
    return _rank_pct(base, 21)

def dras_082_drawdown_severity_skew_lvl_63d(close: pd.Series) -> pd.Series:
    """
    dras_082_drawdown_severity_skew_lvl_63d
    ECONOMIC RATIONALE: Skewness of negative returns only.
    """
    base = close.pct_change(1).rolling(252).apply(lambda x: x[x < 0].skew())
    return _rolling_mean(base, 63)

def dras_083_drawdown_severity_skew_zscore_63d(close: pd.Series) -> pd.Series:
    """
    dras_083_drawdown_severity_skew_zscore_63d
    ECONOMIC RATIONALE: Skewness of negative returns only.
    """
    base = close.pct_change(1).rolling(252).apply(lambda x: x[x < 0].skew())
    return _zscore_rolling(base, 63)

def dras_084_drawdown_severity_skew_rank_63d(close: pd.Series) -> pd.Series:
    """
    dras_084_drawdown_severity_skew_rank_63d
    ECONOMIC RATIONALE: Skewness of negative returns only.
    """
    base = close.pct_change(1).rolling(252).apply(lambda x: x[x < 0].skew())
    return _rank_pct(base, 63)

def dras_085_drawdown_severity_skew_lvl_126d(close: pd.Series) -> pd.Series:
    """
    dras_085_drawdown_severity_skew_lvl_126d
    ECONOMIC RATIONALE: Skewness of negative returns only.
    """
    base = close.pct_change(1).rolling(252).apply(lambda x: x[x < 0].skew())
    return _rolling_mean(base, 126)

def dras_086_drawdown_severity_skew_zscore_126d(close: pd.Series) -> pd.Series:
    """
    dras_086_drawdown_severity_skew_zscore_126d
    ECONOMIC RATIONALE: Skewness of negative returns only.
    """
    base = close.pct_change(1).rolling(252).apply(lambda x: x[x < 0].skew())
    return _zscore_rolling(base, 126)

def dras_087_drawdown_severity_skew_rank_126d(close: pd.Series) -> pd.Series:
    """
    dras_087_drawdown_severity_skew_rank_126d
    ECONOMIC RATIONALE: Skewness of negative returns only.
    """
    base = close.pct_change(1).rolling(252).apply(lambda x: x[x < 0].skew())
    return _rank_pct(base, 126)

def dras_088_drawdown_severity_skew_lvl_252d(close: pd.Series) -> pd.Series:
    """
    dras_088_drawdown_severity_skew_lvl_252d
    ECONOMIC RATIONALE: Skewness of negative returns only.
    """
    base = close.pct_change(1).rolling(252).apply(lambda x: x[x < 0].skew())
    return _rolling_mean(base, 252)

def dras_089_drawdown_severity_skew_zscore_252d(close: pd.Series) -> pd.Series:
    """
    dras_089_drawdown_severity_skew_zscore_252d
    ECONOMIC RATIONALE: Skewness of negative returns only.
    """
    base = close.pct_change(1).rolling(252).apply(lambda x: x[x < 0].skew())
    return _zscore_rolling(base, 252)

def dras_090_drawdown_severity_skew_rank_252d(close: pd.Series) -> pd.Series:
    """
    dras_090_drawdown_severity_skew_rank_252d
    ECONOMIC RATIONALE: Skewness of negative returns only.
    """
    base = close.pct_change(1).rolling(252).apply(lambda x: x[x < 0].skew())
    return _rank_pct(base, 252)

def dras_091_recovery_strength_index_lvl_5d(close: pd.Series) -> pd.Series:
    """
    dras_091_recovery_strength_index_lvl_5d
    ECONOMIC RATIONALE: Recent rally relative to annual range.
    """
    base = close.pct_change(21) / (close.rolling(252).max() - close.rolling(252).min()).replace(0, 1e-9)
    return _rolling_mean(base, 5)

def dras_092_recovery_strength_index_zscore_5d(close: pd.Series) -> pd.Series:
    """
    dras_092_recovery_strength_index_zscore_5d
    ECONOMIC RATIONALE: Recent rally relative to annual range.
    """
    base = close.pct_change(21) / (close.rolling(252).max() - close.rolling(252).min()).replace(0, 1e-9)
    return _zscore_rolling(base, 5)

def dras_093_recovery_strength_index_rank_5d(close: pd.Series) -> pd.Series:
    """
    dras_093_recovery_strength_index_rank_5d
    ECONOMIC RATIONALE: Recent rally relative to annual range.
    """
    base = close.pct_change(21) / (close.rolling(252).max() - close.rolling(252).min()).replace(0, 1e-9)
    return _rank_pct(base, 5)

def dras_094_recovery_strength_index_lvl_21d(close: pd.Series) -> pd.Series:
    """
    dras_094_recovery_strength_index_lvl_21d
    ECONOMIC RATIONALE: Recent rally relative to annual range.
    """
    base = close.pct_change(21) / (close.rolling(252).max() - close.rolling(252).min()).replace(0, 1e-9)
    return _rolling_mean(base, 21)

def dras_095_recovery_strength_index_zscore_21d(close: pd.Series) -> pd.Series:
    """
    dras_095_recovery_strength_index_zscore_21d
    ECONOMIC RATIONALE: Recent rally relative to annual range.
    """
    base = close.pct_change(21) / (close.rolling(252).max() - close.rolling(252).min()).replace(0, 1e-9)
    return _zscore_rolling(base, 21)

def dras_096_recovery_strength_index_rank_21d(close: pd.Series) -> pd.Series:
    """
    dras_096_recovery_strength_index_rank_21d
    ECONOMIC RATIONALE: Recent rally relative to annual range.
    """
    base = close.pct_change(21) / (close.rolling(252).max() - close.rolling(252).min()).replace(0, 1e-9)
    return _rank_pct(base, 21)

def dras_097_recovery_strength_index_lvl_63d(close: pd.Series) -> pd.Series:
    """
    dras_097_recovery_strength_index_lvl_63d
    ECONOMIC RATIONALE: Recent rally relative to annual range.
    """
    base = close.pct_change(21) / (close.rolling(252).max() - close.rolling(252).min()).replace(0, 1e-9)
    return _rolling_mean(base, 63)

def dras_098_recovery_strength_index_zscore_63d(close: pd.Series) -> pd.Series:
    """
    dras_098_recovery_strength_index_zscore_63d
    ECONOMIC RATIONALE: Recent rally relative to annual range.
    """
    base = close.pct_change(21) / (close.rolling(252).max() - close.rolling(252).min()).replace(0, 1e-9)
    return _zscore_rolling(base, 63)

def dras_099_recovery_strength_index_rank_63d(close: pd.Series) -> pd.Series:
    """
    dras_099_recovery_strength_index_rank_63d
    ECONOMIC RATIONALE: Recent rally relative to annual range.
    """
    base = close.pct_change(21) / (close.rolling(252).max() - close.rolling(252).min()).replace(0, 1e-9)
    return _rank_pct(base, 63)

def dras_100_recovery_strength_index_lvl_126d(close: pd.Series) -> pd.Series:
    """
    dras_100_recovery_strength_index_lvl_126d
    ECONOMIC RATIONALE: Recent rally relative to annual range.
    """
    base = close.pct_change(21) / (close.rolling(252).max() - close.rolling(252).min()).replace(0, 1e-9)
    return _rolling_mean(base, 126)

def dras_101_recovery_strength_index_zscore_126d(close: pd.Series) -> pd.Series:
    """
    dras_101_recovery_strength_index_zscore_126d
    ECONOMIC RATIONALE: Recent rally relative to annual range.
    """
    base = close.pct_change(21) / (close.rolling(252).max() - close.rolling(252).min()).replace(0, 1e-9)
    return _zscore_rolling(base, 126)

def dras_102_recovery_strength_index_rank_126d(close: pd.Series) -> pd.Series:
    """
    dras_102_recovery_strength_index_rank_126d
    ECONOMIC RATIONALE: Recent rally relative to annual range.
    """
    base = close.pct_change(21) / (close.rolling(252).max() - close.rolling(252).min()).replace(0, 1e-9)
    return _rank_pct(base, 126)

def dras_103_recovery_strength_index_lvl_252d(close: pd.Series) -> pd.Series:
    """
    dras_103_recovery_strength_index_lvl_252d
    ECONOMIC RATIONALE: Recent rally relative to annual range.
    """
    base = close.pct_change(21) / (close.rolling(252).max() - close.rolling(252).min()).replace(0, 1e-9)
    return _rolling_mean(base, 252)

def dras_104_recovery_strength_index_zscore_252d(close: pd.Series) -> pd.Series:
    """
    dras_104_recovery_strength_index_zscore_252d
    ECONOMIC RATIONALE: Recent rally relative to annual range.
    """
    base = close.pct_change(21) / (close.rolling(252).max() - close.rolling(252).min()).replace(0, 1e-9)
    return _zscore_rolling(base, 252)

def dras_105_recovery_strength_index_rank_252d(close: pd.Series) -> pd.Series:
    """
    dras_105_recovery_strength_index_rank_252d
    ECONOMIC RATIONALE: Recent rally relative to annual range.
    """
    base = close.pct_change(21) / (close.rolling(252).max() - close.rolling(252).min()).replace(0, 1e-9)
    return _rank_pct(base, 252)

def dras_106_asymmetry_momentum_lvl_5d(close: pd.Series) -> pd.Series:
    """
    dras_106_asymmetry_momentum_lvl_5d
    ECONOMIC RATIONALE: Change in the recovery/drawdown balance.
    """
    base = (recovery_asymmetry_ratio).diff(21)
    return _rolling_mean(base, 5)

def dras_107_asymmetry_momentum_zscore_5d(close: pd.Series) -> pd.Series:
    """
    dras_107_asymmetry_momentum_zscore_5d
    ECONOMIC RATIONALE: Change in the recovery/drawdown balance.
    """
    base = (recovery_asymmetry_ratio).diff(21)
    return _zscore_rolling(base, 5)

def dras_108_asymmetry_momentum_rank_5d(close: pd.Series) -> pd.Series:
    """
    dras_108_asymmetry_momentum_rank_5d
    ECONOMIC RATIONALE: Change in the recovery/drawdown balance.
    """
    base = (recovery_asymmetry_ratio).diff(21)
    return _rank_pct(base, 5)

def dras_109_asymmetry_momentum_lvl_21d(close: pd.Series) -> pd.Series:
    """
    dras_109_asymmetry_momentum_lvl_21d
    ECONOMIC RATIONALE: Change in the recovery/drawdown balance.
    """
    base = (recovery_asymmetry_ratio).diff(21)
    return _rolling_mean(base, 21)

def dras_110_asymmetry_momentum_zscore_21d(close: pd.Series) -> pd.Series:
    """
    dras_110_asymmetry_momentum_zscore_21d
    ECONOMIC RATIONALE: Change in the recovery/drawdown balance.
    """
    base = (recovery_asymmetry_ratio).diff(21)
    return _zscore_rolling(base, 21)

def dras_111_asymmetry_momentum_rank_21d(close: pd.Series) -> pd.Series:
    """
    dras_111_asymmetry_momentum_rank_21d
    ECONOMIC RATIONALE: Change in the recovery/drawdown balance.
    """
    base = (recovery_asymmetry_ratio).diff(21)
    return _rank_pct(base, 21)

def dras_112_asymmetry_momentum_lvl_63d(close: pd.Series) -> pd.Series:
    """
    dras_112_asymmetry_momentum_lvl_63d
    ECONOMIC RATIONALE: Change in the recovery/drawdown balance.
    """
    base = (recovery_asymmetry_ratio).diff(21)
    return _rolling_mean(base, 63)

def dras_113_asymmetry_momentum_zscore_63d(close: pd.Series) -> pd.Series:
    """
    dras_113_asymmetry_momentum_zscore_63d
    ECONOMIC RATIONALE: Change in the recovery/drawdown balance.
    """
    base = (recovery_asymmetry_ratio).diff(21)
    return _zscore_rolling(base, 63)

def dras_114_asymmetry_momentum_rank_63d(close: pd.Series) -> pd.Series:
    """
    dras_114_asymmetry_momentum_rank_63d
    ECONOMIC RATIONALE: Change in the recovery/drawdown balance.
    """
    base = (recovery_asymmetry_ratio).diff(21)
    return _rank_pct(base, 63)

def dras_115_asymmetry_momentum_lvl_126d(close: pd.Series) -> pd.Series:
    """
    dras_115_asymmetry_momentum_lvl_126d
    ECONOMIC RATIONALE: Change in the recovery/drawdown balance.
    """
    base = (recovery_asymmetry_ratio).diff(21)
    return _rolling_mean(base, 126)

def dras_116_asymmetry_momentum_zscore_126d(close: pd.Series) -> pd.Series:
    """
    dras_116_asymmetry_momentum_zscore_126d
    ECONOMIC RATIONALE: Change in the recovery/drawdown balance.
    """
    base = (recovery_asymmetry_ratio).diff(21)
    return _zscore_rolling(base, 126)

def dras_117_asymmetry_momentum_rank_126d(close: pd.Series) -> pd.Series:
    """
    dras_117_asymmetry_momentum_rank_126d
    ECONOMIC RATIONALE: Change in the recovery/drawdown balance.
    """
    base = (recovery_asymmetry_ratio).diff(21)
    return _rank_pct(base, 126)

def dras_118_asymmetry_momentum_lvl_252d(close: pd.Series) -> pd.Series:
    """
    dras_118_asymmetry_momentum_lvl_252d
    ECONOMIC RATIONALE: Change in the recovery/drawdown balance.
    """
    base = (recovery_asymmetry_ratio).diff(21)
    return _rolling_mean(base, 252)

def dras_119_asymmetry_momentum_zscore_252d(close: pd.Series) -> pd.Series:
    """
    dras_119_asymmetry_momentum_zscore_252d
    ECONOMIC RATIONALE: Change in the recovery/drawdown balance.
    """
    base = (recovery_asymmetry_ratio).diff(21)
    return _zscore_rolling(base, 252)

def dras_120_asymmetry_momentum_rank_252d(close: pd.Series) -> pd.Series:
    """
    dras_120_asymmetry_momentum_rank_252d
    ECONOMIC RATIONALE: Change in the recovery/drawdown balance.
    """
    base = (recovery_asymmetry_ratio).diff(21)
    return _rank_pct(base, 252)

# ── Registry ──────────────────────────────────────────────────────────────────
V118_REGISTRY_1 = {
    "dras_001_downside_speed_lvl_5d": {"inputs": ["close"], "func": dras_001_downside_speed_lvl_5d},
    "dras_002_downside_speed_zscore_5d": {"inputs": ["close"], "func": dras_002_downside_speed_zscore_5d},
    "dras_003_downside_speed_rank_5d": {"inputs": ["close"], "func": dras_003_downside_speed_rank_5d},
    "dras_004_downside_speed_lvl_21d": {"inputs": ["close"], "func": dras_004_downside_speed_lvl_21d},
    "dras_005_downside_speed_zscore_21d": {"inputs": ["close"], "func": dras_005_downside_speed_zscore_21d},
    "dras_006_downside_speed_rank_21d": {"inputs": ["close"], "func": dras_006_downside_speed_rank_21d},
    "dras_007_downside_speed_lvl_63d": {"inputs": ["close"], "func": dras_007_downside_speed_lvl_63d},
    "dras_008_downside_speed_zscore_63d": {"inputs": ["close"], "func": dras_008_downside_speed_zscore_63d},
    "dras_009_downside_speed_rank_63d": {"inputs": ["close"], "func": dras_009_downside_speed_rank_63d},
    "dras_010_downside_speed_lvl_126d": {"inputs": ["close"], "func": dras_010_downside_speed_lvl_126d},
    "dras_011_downside_speed_zscore_126d": {"inputs": ["close"], "func": dras_011_downside_speed_zscore_126d},
    "dras_012_downside_speed_rank_126d": {"inputs": ["close"], "func": dras_012_downside_speed_rank_126d},
    "dras_013_downside_speed_lvl_252d": {"inputs": ["close"], "func": dras_013_downside_speed_lvl_252d},
    "dras_014_downside_speed_zscore_252d": {"inputs": ["close"], "func": dras_014_downside_speed_zscore_252d},
    "dras_015_downside_speed_rank_252d": {"inputs": ["close"], "func": dras_015_downside_speed_rank_252d},
    "dras_016_upside_speed_lvl_5d": {"inputs": ["close"], "func": dras_016_upside_speed_lvl_5d},
    "dras_017_upside_speed_zscore_5d": {"inputs": ["close"], "func": dras_017_upside_speed_zscore_5d},
    "dras_018_upside_speed_rank_5d": {"inputs": ["close"], "func": dras_018_upside_speed_rank_5d},
    "dras_019_upside_speed_lvl_21d": {"inputs": ["close"], "func": dras_019_upside_speed_lvl_21d},
    "dras_020_upside_speed_zscore_21d": {"inputs": ["close"], "func": dras_020_upside_speed_zscore_21d},
    "dras_021_upside_speed_rank_21d": {"inputs": ["close"], "func": dras_021_upside_speed_rank_21d},
    "dras_022_upside_speed_lvl_63d": {"inputs": ["close"], "func": dras_022_upside_speed_lvl_63d},
    "dras_023_upside_speed_zscore_63d": {"inputs": ["close"], "func": dras_023_upside_speed_zscore_63d},
    "dras_024_upside_speed_rank_63d": {"inputs": ["close"], "func": dras_024_upside_speed_rank_63d},
    "dras_025_upside_speed_lvl_126d": {"inputs": ["close"], "func": dras_025_upside_speed_lvl_126d},
    "dras_026_upside_speed_zscore_126d": {"inputs": ["close"], "func": dras_026_upside_speed_zscore_126d},
    "dras_027_upside_speed_rank_126d": {"inputs": ["close"], "func": dras_027_upside_speed_rank_126d},
    "dras_028_upside_speed_lvl_252d": {"inputs": ["close"], "func": dras_028_upside_speed_lvl_252d},
    "dras_029_upside_speed_zscore_252d": {"inputs": ["close"], "func": dras_029_upside_speed_zscore_252d},
    "dras_030_upside_speed_rank_252d": {"inputs": ["close"], "func": dras_030_upside_speed_rank_252d},
    "dras_031_recovery_asymmetry_ratio_lvl_5d": {"inputs": ["close"], "func": dras_031_recovery_asymmetry_ratio_lvl_5d},
    "dras_032_recovery_asymmetry_ratio_zscore_5d": {"inputs": ["close"], "func": dras_032_recovery_asymmetry_ratio_zscore_5d},
    "dras_033_recovery_asymmetry_ratio_rank_5d": {"inputs": ["close"], "func": dras_033_recovery_asymmetry_ratio_rank_5d},
    "dras_034_recovery_asymmetry_ratio_lvl_21d": {"inputs": ["close"], "func": dras_034_recovery_asymmetry_ratio_lvl_21d},
    "dras_035_recovery_asymmetry_ratio_zscore_21d": {"inputs": ["close"], "func": dras_035_recovery_asymmetry_ratio_zscore_21d},
    "dras_036_recovery_asymmetry_ratio_rank_21d": {"inputs": ["close"], "func": dras_036_recovery_asymmetry_ratio_rank_21d},
    "dras_037_recovery_asymmetry_ratio_lvl_63d": {"inputs": ["close"], "func": dras_037_recovery_asymmetry_ratio_lvl_63d},
    "dras_038_recovery_asymmetry_ratio_zscore_63d": {"inputs": ["close"], "func": dras_038_recovery_asymmetry_ratio_zscore_63d},
    "dras_039_recovery_asymmetry_ratio_rank_63d": {"inputs": ["close"], "func": dras_039_recovery_asymmetry_ratio_rank_63d},
    "dras_040_recovery_asymmetry_ratio_lvl_126d": {"inputs": ["close"], "func": dras_040_recovery_asymmetry_ratio_lvl_126d},
    "dras_041_recovery_asymmetry_ratio_zscore_126d": {"inputs": ["close"], "func": dras_041_recovery_asymmetry_ratio_zscore_126d},
    "dras_042_recovery_asymmetry_ratio_rank_126d": {"inputs": ["close"], "func": dras_042_recovery_asymmetry_ratio_rank_126d},
    "dras_043_recovery_asymmetry_ratio_lvl_252d": {"inputs": ["close"], "func": dras_043_recovery_asymmetry_ratio_lvl_252d},
    "dras_044_recovery_asymmetry_ratio_zscore_252d": {"inputs": ["close"], "func": dras_044_recovery_asymmetry_ratio_zscore_252d},
    "dras_045_recovery_asymmetry_ratio_rank_252d": {"inputs": ["close"], "func": dras_045_recovery_asymmetry_ratio_rank_252d},
    "dras_046_drawdown_recovery_lag_lvl_5d": {"inputs": ["close"], "func": dras_046_drawdown_recovery_lag_lvl_5d},
    "dras_047_drawdown_recovery_lag_zscore_5d": {"inputs": ["close"], "func": dras_047_drawdown_recovery_lag_zscore_5d},
    "dras_048_drawdown_recovery_lag_rank_5d": {"inputs": ["close"], "func": dras_048_drawdown_recovery_lag_rank_5d},
    "dras_049_drawdown_recovery_lag_lvl_21d": {"inputs": ["close"], "func": dras_049_drawdown_recovery_lag_lvl_21d},
    "dras_050_drawdown_recovery_lag_zscore_21d": {"inputs": ["close"], "func": dras_050_drawdown_recovery_lag_zscore_21d},
    "dras_051_drawdown_recovery_lag_rank_21d": {"inputs": ["close"], "func": dras_051_drawdown_recovery_lag_rank_21d},
    "dras_052_drawdown_recovery_lag_lvl_63d": {"inputs": ["close"], "func": dras_052_drawdown_recovery_lag_lvl_63d},
    "dras_053_drawdown_recovery_lag_zscore_63d": {"inputs": ["close"], "func": dras_053_drawdown_recovery_lag_zscore_63d},
    "dras_054_drawdown_recovery_lag_rank_63d": {"inputs": ["close"], "func": dras_054_drawdown_recovery_lag_rank_63d},
    "dras_055_drawdown_recovery_lag_lvl_126d": {"inputs": ["close"], "func": dras_055_drawdown_recovery_lag_lvl_126d},
    "dras_056_drawdown_recovery_lag_zscore_126d": {"inputs": ["close"], "func": dras_056_drawdown_recovery_lag_zscore_126d},
    "dras_057_drawdown_recovery_lag_rank_126d": {"inputs": ["close"], "func": dras_057_drawdown_recovery_lag_rank_126d},
    "dras_058_drawdown_recovery_lag_lvl_252d": {"inputs": ["close"], "func": dras_058_drawdown_recovery_lag_lvl_252d},
    "dras_059_drawdown_recovery_lag_zscore_252d": {"inputs": ["close"], "func": dras_059_drawdown_recovery_lag_zscore_252d},
    "dras_060_drawdown_recovery_lag_rank_252d": {"inputs": ["close"], "func": dras_060_drawdown_recovery_lag_rank_252d},
    "dras_061_asymmetry_zscore_lvl_5d": {"inputs": ["close"], "func": dras_061_asymmetry_zscore_lvl_5d},
    "dras_062_asymmetry_zscore_zscore_5d": {"inputs": ["close"], "func": dras_062_asymmetry_zscore_zscore_5d},
    "dras_063_asymmetry_zscore_rank_5d": {"inputs": ["close"], "func": dras_063_asymmetry_zscore_rank_5d},
    "dras_064_asymmetry_zscore_lvl_21d": {"inputs": ["close"], "func": dras_064_asymmetry_zscore_lvl_21d},
    "dras_065_asymmetry_zscore_zscore_21d": {"inputs": ["close"], "func": dras_065_asymmetry_zscore_zscore_21d},
    "dras_066_asymmetry_zscore_rank_21d": {"inputs": ["close"], "func": dras_066_asymmetry_zscore_rank_21d},
    "dras_067_asymmetry_zscore_lvl_63d": {"inputs": ["close"], "func": dras_067_asymmetry_zscore_lvl_63d},
    "dras_068_asymmetry_zscore_zscore_63d": {"inputs": ["close"], "func": dras_068_asymmetry_zscore_zscore_63d},
    "dras_069_asymmetry_zscore_rank_63d": {"inputs": ["close"], "func": dras_069_asymmetry_zscore_rank_63d},
    "dras_070_asymmetry_zscore_lvl_126d": {"inputs": ["close"], "func": dras_070_asymmetry_zscore_lvl_126d},
    "dras_071_asymmetry_zscore_zscore_126d": {"inputs": ["close"], "func": dras_071_asymmetry_zscore_zscore_126d},
    "dras_072_asymmetry_zscore_rank_126d": {"inputs": ["close"], "func": dras_072_asymmetry_zscore_rank_126d},
    "dras_073_asymmetry_zscore_lvl_252d": {"inputs": ["close"], "func": dras_073_asymmetry_zscore_lvl_252d},
    "dras_074_asymmetry_zscore_zscore_252d": {"inputs": ["close"], "func": dras_074_asymmetry_zscore_zscore_252d},
    "dras_075_asymmetry_zscore_rank_252d": {"inputs": ["close"], "func": dras_075_asymmetry_zscore_rank_252d},
    "dras_076_drawdown_severity_skew_lvl_5d": {"inputs": ["close"], "func": dras_076_drawdown_severity_skew_lvl_5d},
    "dras_077_drawdown_severity_skew_zscore_5d": {"inputs": ["close"], "func": dras_077_drawdown_severity_skew_zscore_5d},
    "dras_078_drawdown_severity_skew_rank_5d": {"inputs": ["close"], "func": dras_078_drawdown_severity_skew_rank_5d},
    "dras_079_drawdown_severity_skew_lvl_21d": {"inputs": ["close"], "func": dras_079_drawdown_severity_skew_lvl_21d},
    "dras_080_drawdown_severity_skew_zscore_21d": {"inputs": ["close"], "func": dras_080_drawdown_severity_skew_zscore_21d},
    "dras_081_drawdown_severity_skew_rank_21d": {"inputs": ["close"], "func": dras_081_drawdown_severity_skew_rank_21d},
    "dras_082_drawdown_severity_skew_lvl_63d": {"inputs": ["close"], "func": dras_082_drawdown_severity_skew_lvl_63d},
    "dras_083_drawdown_severity_skew_zscore_63d": {"inputs": ["close"], "func": dras_083_drawdown_severity_skew_zscore_63d},
    "dras_084_drawdown_severity_skew_rank_63d": {"inputs": ["close"], "func": dras_084_drawdown_severity_skew_rank_63d},
    "dras_085_drawdown_severity_skew_lvl_126d": {"inputs": ["close"], "func": dras_085_drawdown_severity_skew_lvl_126d},
    "dras_086_drawdown_severity_skew_zscore_126d": {"inputs": ["close"], "func": dras_086_drawdown_severity_skew_zscore_126d},
    "dras_087_drawdown_severity_skew_rank_126d": {"inputs": ["close"], "func": dras_087_drawdown_severity_skew_rank_126d},
    "dras_088_drawdown_severity_skew_lvl_252d": {"inputs": ["close"], "func": dras_088_drawdown_severity_skew_lvl_252d},
    "dras_089_drawdown_severity_skew_zscore_252d": {"inputs": ["close"], "func": dras_089_drawdown_severity_skew_zscore_252d},
    "dras_090_drawdown_severity_skew_rank_252d": {"inputs": ["close"], "func": dras_090_drawdown_severity_skew_rank_252d},
    "dras_091_recovery_strength_index_lvl_5d": {"inputs": ["close"], "func": dras_091_recovery_strength_index_lvl_5d},
    "dras_092_recovery_strength_index_zscore_5d": {"inputs": ["close"], "func": dras_092_recovery_strength_index_zscore_5d},
    "dras_093_recovery_strength_index_rank_5d": {"inputs": ["close"], "func": dras_093_recovery_strength_index_rank_5d},
    "dras_094_recovery_strength_index_lvl_21d": {"inputs": ["close"], "func": dras_094_recovery_strength_index_lvl_21d},
    "dras_095_recovery_strength_index_zscore_21d": {"inputs": ["close"], "func": dras_095_recovery_strength_index_zscore_21d},
    "dras_096_recovery_strength_index_rank_21d": {"inputs": ["close"], "func": dras_096_recovery_strength_index_rank_21d},
    "dras_097_recovery_strength_index_lvl_63d": {"inputs": ["close"], "func": dras_097_recovery_strength_index_lvl_63d},
    "dras_098_recovery_strength_index_zscore_63d": {"inputs": ["close"], "func": dras_098_recovery_strength_index_zscore_63d},
    "dras_099_recovery_strength_index_rank_63d": {"inputs": ["close"], "func": dras_099_recovery_strength_index_rank_63d},
    "dras_100_recovery_strength_index_lvl_126d": {"inputs": ["close"], "func": dras_100_recovery_strength_index_lvl_126d},
    "dras_101_recovery_strength_index_zscore_126d": {"inputs": ["close"], "func": dras_101_recovery_strength_index_zscore_126d},
    "dras_102_recovery_strength_index_rank_126d": {"inputs": ["close"], "func": dras_102_recovery_strength_index_rank_126d},
    "dras_103_recovery_strength_index_lvl_252d": {"inputs": ["close"], "func": dras_103_recovery_strength_index_lvl_252d},
    "dras_104_recovery_strength_index_zscore_252d": {"inputs": ["close"], "func": dras_104_recovery_strength_index_zscore_252d},
    "dras_105_recovery_strength_index_rank_252d": {"inputs": ["close"], "func": dras_105_recovery_strength_index_rank_252d},
    "dras_106_asymmetry_momentum_lvl_5d": {"inputs": ["close"], "func": dras_106_asymmetry_momentum_lvl_5d},
    "dras_107_asymmetry_momentum_zscore_5d": {"inputs": ["close"], "func": dras_107_asymmetry_momentum_zscore_5d},
    "dras_108_asymmetry_momentum_rank_5d": {"inputs": ["close"], "func": dras_108_asymmetry_momentum_rank_5d},
    "dras_109_asymmetry_momentum_lvl_21d": {"inputs": ["close"], "func": dras_109_asymmetry_momentum_lvl_21d},
    "dras_110_asymmetry_momentum_zscore_21d": {"inputs": ["close"], "func": dras_110_asymmetry_momentum_zscore_21d},
    "dras_111_asymmetry_momentum_rank_21d": {"inputs": ["close"], "func": dras_111_asymmetry_momentum_rank_21d},
    "dras_112_asymmetry_momentum_lvl_63d": {"inputs": ["close"], "func": dras_112_asymmetry_momentum_lvl_63d},
    "dras_113_asymmetry_momentum_zscore_63d": {"inputs": ["close"], "func": dras_113_asymmetry_momentum_zscore_63d},
    "dras_114_asymmetry_momentum_rank_63d": {"inputs": ["close"], "func": dras_114_asymmetry_momentum_rank_63d},
    "dras_115_asymmetry_momentum_lvl_126d": {"inputs": ["close"], "func": dras_115_asymmetry_momentum_lvl_126d},
    "dras_116_asymmetry_momentum_zscore_126d": {"inputs": ["close"], "func": dras_116_asymmetry_momentum_zscore_126d},
    "dras_117_asymmetry_momentum_rank_126d": {"inputs": ["close"], "func": dras_117_asymmetry_momentum_rank_126d},
    "dras_118_asymmetry_momentum_lvl_252d": {"inputs": ["close"], "func": dras_118_asymmetry_momentum_lvl_252d},
    "dras_119_asymmetry_momentum_zscore_252d": {"inputs": ["close"], "func": dras_119_asymmetry_momentum_zscore_252d},
    "dras_120_asymmetry_momentum_rank_252d": {"inputs": ["close"], "func": dras_120_asymmetry_momentum_rank_252d},
}
