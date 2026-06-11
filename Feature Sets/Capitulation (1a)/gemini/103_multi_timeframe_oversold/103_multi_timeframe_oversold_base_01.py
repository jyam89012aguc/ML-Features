"""
103_multi_timeframe_oversold — Base Features Part 1
Domain: multi_timeframe_oversold
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

def mtfo_001_daily_rsi_lvl_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_001_daily_rsi_lvl_5d
    ECONOMIC RATIONALE: 14-day Relative Strength Index.
    """
    base = 100 - (100 / (1 + close.diff(1).clip(lower=0).rolling(14).mean() / close.diff(1).clip(upper=0).abs().rolling(14).mean().replace(0, 1e-9)))
    return _rolling_mean(base, 5)

def mtfo_002_daily_rsi_zscore_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_002_daily_rsi_zscore_5d
    ECONOMIC RATIONALE: 14-day Relative Strength Index.
    """
    base = 100 - (100 / (1 + close.diff(1).clip(lower=0).rolling(14).mean() / close.diff(1).clip(upper=0).abs().rolling(14).mean().replace(0, 1e-9)))
    return _zscore_rolling(base, 5)

def mtfo_003_daily_rsi_rank_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_003_daily_rsi_rank_5d
    ECONOMIC RATIONALE: 14-day Relative Strength Index.
    """
    base = 100 - (100 / (1 + close.diff(1).clip(lower=0).rolling(14).mean() / close.diff(1).clip(upper=0).abs().rolling(14).mean().replace(0, 1e-9)))
    return _rank_pct(base, 5)

def mtfo_004_daily_rsi_lvl_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_004_daily_rsi_lvl_21d
    ECONOMIC RATIONALE: 14-day Relative Strength Index.
    """
    base = 100 - (100 / (1 + close.diff(1).clip(lower=0).rolling(14).mean() / close.diff(1).clip(upper=0).abs().rolling(14).mean().replace(0, 1e-9)))
    return _rolling_mean(base, 21)

def mtfo_005_daily_rsi_zscore_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_005_daily_rsi_zscore_21d
    ECONOMIC RATIONALE: 14-day Relative Strength Index.
    """
    base = 100 - (100 / (1 + close.diff(1).clip(lower=0).rolling(14).mean() / close.diff(1).clip(upper=0).abs().rolling(14).mean().replace(0, 1e-9)))
    return _zscore_rolling(base, 21)

def mtfo_006_daily_rsi_rank_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_006_daily_rsi_rank_21d
    ECONOMIC RATIONALE: 14-day Relative Strength Index.
    """
    base = 100 - (100 / (1 + close.diff(1).clip(lower=0).rolling(14).mean() / close.diff(1).clip(upper=0).abs().rolling(14).mean().replace(0, 1e-9)))
    return _rank_pct(base, 21)

def mtfo_007_daily_rsi_lvl_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_007_daily_rsi_lvl_63d
    ECONOMIC RATIONALE: 14-day Relative Strength Index.
    """
    base = 100 - (100 / (1 + close.diff(1).clip(lower=0).rolling(14).mean() / close.diff(1).clip(upper=0).abs().rolling(14).mean().replace(0, 1e-9)))
    return _rolling_mean(base, 63)

def mtfo_008_daily_rsi_zscore_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_008_daily_rsi_zscore_63d
    ECONOMIC RATIONALE: 14-day Relative Strength Index.
    """
    base = 100 - (100 / (1 + close.diff(1).clip(lower=0).rolling(14).mean() / close.diff(1).clip(upper=0).abs().rolling(14).mean().replace(0, 1e-9)))
    return _zscore_rolling(base, 63)

def mtfo_009_daily_rsi_rank_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_009_daily_rsi_rank_63d
    ECONOMIC RATIONALE: 14-day Relative Strength Index.
    """
    base = 100 - (100 / (1 + close.diff(1).clip(lower=0).rolling(14).mean() / close.diff(1).clip(upper=0).abs().rolling(14).mean().replace(0, 1e-9)))
    return _rank_pct(base, 63)

def mtfo_010_daily_rsi_lvl_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_010_daily_rsi_lvl_126d
    ECONOMIC RATIONALE: 14-day Relative Strength Index.
    """
    base = 100 - (100 / (1 + close.diff(1).clip(lower=0).rolling(14).mean() / close.diff(1).clip(upper=0).abs().rolling(14).mean().replace(0, 1e-9)))
    return _rolling_mean(base, 126)

def mtfo_011_daily_rsi_zscore_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_011_daily_rsi_zscore_126d
    ECONOMIC RATIONALE: 14-day Relative Strength Index.
    """
    base = 100 - (100 / (1 + close.diff(1).clip(lower=0).rolling(14).mean() / close.diff(1).clip(upper=0).abs().rolling(14).mean().replace(0, 1e-9)))
    return _zscore_rolling(base, 126)

def mtfo_012_daily_rsi_rank_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_012_daily_rsi_rank_126d
    ECONOMIC RATIONALE: 14-day Relative Strength Index.
    """
    base = 100 - (100 / (1 + close.diff(1).clip(lower=0).rolling(14).mean() / close.diff(1).clip(upper=0).abs().rolling(14).mean().replace(0, 1e-9)))
    return _rank_pct(base, 126)

def mtfo_013_daily_rsi_lvl_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_013_daily_rsi_lvl_252d
    ECONOMIC RATIONALE: 14-day Relative Strength Index.
    """
    base = 100 - (100 / (1 + close.diff(1).clip(lower=0).rolling(14).mean() / close.diff(1).clip(upper=0).abs().rolling(14).mean().replace(0, 1e-9)))
    return _rolling_mean(base, 252)

def mtfo_014_daily_rsi_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_014_daily_rsi_zscore_252d
    ECONOMIC RATIONALE: 14-day Relative Strength Index.
    """
    base = 100 - (100 / (1 + close.diff(1).clip(lower=0).rolling(14).mean() / close.diff(1).clip(upper=0).abs().rolling(14).mean().replace(0, 1e-9)))
    return _zscore_rolling(base, 252)

def mtfo_015_daily_rsi_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_015_daily_rsi_rank_252d
    ECONOMIC RATIONALE: 14-day Relative Strength Index.
    """
    base = 100 - (100 / (1 + close.diff(1).clip(lower=0).rolling(14).mean() / close.diff(1).clip(upper=0).abs().rolling(14).mean().replace(0, 1e-9)))
    return _rank_pct(base, 252)

def mtfo_016_weekly_rsi_lvl_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_016_weekly_rsi_lvl_5d
    ECONOMIC RATIONALE: Weekly-equivalent RSI.
    """
    base = 100 - (100 / (1 + close.diff(5).clip(lower=0).rolling(14).mean() / close.diff(5).clip(upper=0).abs().rolling(14).mean().replace(0, 1e-9)))
    return _rolling_mean(base, 5)

def mtfo_017_weekly_rsi_zscore_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_017_weekly_rsi_zscore_5d
    ECONOMIC RATIONALE: Weekly-equivalent RSI.
    """
    base = 100 - (100 / (1 + close.diff(5).clip(lower=0).rolling(14).mean() / close.diff(5).clip(upper=0).abs().rolling(14).mean().replace(0, 1e-9)))
    return _zscore_rolling(base, 5)

def mtfo_018_weekly_rsi_rank_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_018_weekly_rsi_rank_5d
    ECONOMIC RATIONALE: Weekly-equivalent RSI.
    """
    base = 100 - (100 / (1 + close.diff(5).clip(lower=0).rolling(14).mean() / close.diff(5).clip(upper=0).abs().rolling(14).mean().replace(0, 1e-9)))
    return _rank_pct(base, 5)

def mtfo_019_weekly_rsi_lvl_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_019_weekly_rsi_lvl_21d
    ECONOMIC RATIONALE: Weekly-equivalent RSI.
    """
    base = 100 - (100 / (1 + close.diff(5).clip(lower=0).rolling(14).mean() / close.diff(5).clip(upper=0).abs().rolling(14).mean().replace(0, 1e-9)))
    return _rolling_mean(base, 21)

def mtfo_020_weekly_rsi_zscore_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_020_weekly_rsi_zscore_21d
    ECONOMIC RATIONALE: Weekly-equivalent RSI.
    """
    base = 100 - (100 / (1 + close.diff(5).clip(lower=0).rolling(14).mean() / close.diff(5).clip(upper=0).abs().rolling(14).mean().replace(0, 1e-9)))
    return _zscore_rolling(base, 21)

def mtfo_021_weekly_rsi_rank_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_021_weekly_rsi_rank_21d
    ECONOMIC RATIONALE: Weekly-equivalent RSI.
    """
    base = 100 - (100 / (1 + close.diff(5).clip(lower=0).rolling(14).mean() / close.diff(5).clip(upper=0).abs().rolling(14).mean().replace(0, 1e-9)))
    return _rank_pct(base, 21)

def mtfo_022_weekly_rsi_lvl_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_022_weekly_rsi_lvl_63d
    ECONOMIC RATIONALE: Weekly-equivalent RSI.
    """
    base = 100 - (100 / (1 + close.diff(5).clip(lower=0).rolling(14).mean() / close.diff(5).clip(upper=0).abs().rolling(14).mean().replace(0, 1e-9)))
    return _rolling_mean(base, 63)

def mtfo_023_weekly_rsi_zscore_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_023_weekly_rsi_zscore_63d
    ECONOMIC RATIONALE: Weekly-equivalent RSI.
    """
    base = 100 - (100 / (1 + close.diff(5).clip(lower=0).rolling(14).mean() / close.diff(5).clip(upper=0).abs().rolling(14).mean().replace(0, 1e-9)))
    return _zscore_rolling(base, 63)

def mtfo_024_weekly_rsi_rank_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_024_weekly_rsi_rank_63d
    ECONOMIC RATIONALE: Weekly-equivalent RSI.
    """
    base = 100 - (100 / (1 + close.diff(5).clip(lower=0).rolling(14).mean() / close.diff(5).clip(upper=0).abs().rolling(14).mean().replace(0, 1e-9)))
    return _rank_pct(base, 63)

def mtfo_025_weekly_rsi_lvl_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_025_weekly_rsi_lvl_126d
    ECONOMIC RATIONALE: Weekly-equivalent RSI.
    """
    base = 100 - (100 / (1 + close.diff(5).clip(lower=0).rolling(14).mean() / close.diff(5).clip(upper=0).abs().rolling(14).mean().replace(0, 1e-9)))
    return _rolling_mean(base, 126)

def mtfo_026_weekly_rsi_zscore_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_026_weekly_rsi_zscore_126d
    ECONOMIC RATIONALE: Weekly-equivalent RSI.
    """
    base = 100 - (100 / (1 + close.diff(5).clip(lower=0).rolling(14).mean() / close.diff(5).clip(upper=0).abs().rolling(14).mean().replace(0, 1e-9)))
    return _zscore_rolling(base, 126)

def mtfo_027_weekly_rsi_rank_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_027_weekly_rsi_rank_126d
    ECONOMIC RATIONALE: Weekly-equivalent RSI.
    """
    base = 100 - (100 / (1 + close.diff(5).clip(lower=0).rolling(14).mean() / close.diff(5).clip(upper=0).abs().rolling(14).mean().replace(0, 1e-9)))
    return _rank_pct(base, 126)

def mtfo_028_weekly_rsi_lvl_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_028_weekly_rsi_lvl_252d
    ECONOMIC RATIONALE: Weekly-equivalent RSI.
    """
    base = 100 - (100 / (1 + close.diff(5).clip(lower=0).rolling(14).mean() / close.diff(5).clip(upper=0).abs().rolling(14).mean().replace(0, 1e-9)))
    return _rolling_mean(base, 252)

def mtfo_029_weekly_rsi_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_029_weekly_rsi_zscore_252d
    ECONOMIC RATIONALE: Weekly-equivalent RSI.
    """
    base = 100 - (100 / (1 + close.diff(5).clip(lower=0).rolling(14).mean() / close.diff(5).clip(upper=0).abs().rolling(14).mean().replace(0, 1e-9)))
    return _zscore_rolling(base, 252)

def mtfo_030_weekly_rsi_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_030_weekly_rsi_rank_252d
    ECONOMIC RATIONALE: Weekly-equivalent RSI.
    """
    base = 100 - (100 / (1 + close.diff(5).clip(lower=0).rolling(14).mean() / close.diff(5).clip(upper=0).abs().rolling(14).mean().replace(0, 1e-9)))
    return _rank_pct(base, 252)

def mtfo_031_monthly_rsi_lvl_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_031_monthly_rsi_lvl_5d
    ECONOMIC RATIONALE: Monthly-equivalent RSI.
    """
    base = 100 - (100 / (1 + close.diff(21).clip(lower=0).rolling(14).mean() / close.diff(21).clip(upper=0).abs().rolling(14).mean().replace(0, 1e-9)))
    return _rolling_mean(base, 5)

def mtfo_032_monthly_rsi_zscore_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_032_monthly_rsi_zscore_5d
    ECONOMIC RATIONALE: Monthly-equivalent RSI.
    """
    base = 100 - (100 / (1 + close.diff(21).clip(lower=0).rolling(14).mean() / close.diff(21).clip(upper=0).abs().rolling(14).mean().replace(0, 1e-9)))
    return _zscore_rolling(base, 5)

def mtfo_033_monthly_rsi_rank_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_033_monthly_rsi_rank_5d
    ECONOMIC RATIONALE: Monthly-equivalent RSI.
    """
    base = 100 - (100 / (1 + close.diff(21).clip(lower=0).rolling(14).mean() / close.diff(21).clip(upper=0).abs().rolling(14).mean().replace(0, 1e-9)))
    return _rank_pct(base, 5)

def mtfo_034_monthly_rsi_lvl_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_034_monthly_rsi_lvl_21d
    ECONOMIC RATIONALE: Monthly-equivalent RSI.
    """
    base = 100 - (100 / (1 + close.diff(21).clip(lower=0).rolling(14).mean() / close.diff(21).clip(upper=0).abs().rolling(14).mean().replace(0, 1e-9)))
    return _rolling_mean(base, 21)

def mtfo_035_monthly_rsi_zscore_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_035_monthly_rsi_zscore_21d
    ECONOMIC RATIONALE: Monthly-equivalent RSI.
    """
    base = 100 - (100 / (1 + close.diff(21).clip(lower=0).rolling(14).mean() / close.diff(21).clip(upper=0).abs().rolling(14).mean().replace(0, 1e-9)))
    return _zscore_rolling(base, 21)

def mtfo_036_monthly_rsi_rank_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_036_monthly_rsi_rank_21d
    ECONOMIC RATIONALE: Monthly-equivalent RSI.
    """
    base = 100 - (100 / (1 + close.diff(21).clip(lower=0).rolling(14).mean() / close.diff(21).clip(upper=0).abs().rolling(14).mean().replace(0, 1e-9)))
    return _rank_pct(base, 21)

def mtfo_037_monthly_rsi_lvl_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_037_monthly_rsi_lvl_63d
    ECONOMIC RATIONALE: Monthly-equivalent RSI.
    """
    base = 100 - (100 / (1 + close.diff(21).clip(lower=0).rolling(14).mean() / close.diff(21).clip(upper=0).abs().rolling(14).mean().replace(0, 1e-9)))
    return _rolling_mean(base, 63)

def mtfo_038_monthly_rsi_zscore_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_038_monthly_rsi_zscore_63d
    ECONOMIC RATIONALE: Monthly-equivalent RSI.
    """
    base = 100 - (100 / (1 + close.diff(21).clip(lower=0).rolling(14).mean() / close.diff(21).clip(upper=0).abs().rolling(14).mean().replace(0, 1e-9)))
    return _zscore_rolling(base, 63)

def mtfo_039_monthly_rsi_rank_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_039_monthly_rsi_rank_63d
    ECONOMIC RATIONALE: Monthly-equivalent RSI.
    """
    base = 100 - (100 / (1 + close.diff(21).clip(lower=0).rolling(14).mean() / close.diff(21).clip(upper=0).abs().rolling(14).mean().replace(0, 1e-9)))
    return _rank_pct(base, 63)

def mtfo_040_monthly_rsi_lvl_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_040_monthly_rsi_lvl_126d
    ECONOMIC RATIONALE: Monthly-equivalent RSI.
    """
    base = 100 - (100 / (1 + close.diff(21).clip(lower=0).rolling(14).mean() / close.diff(21).clip(upper=0).abs().rolling(14).mean().replace(0, 1e-9)))
    return _rolling_mean(base, 126)

def mtfo_041_monthly_rsi_zscore_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_041_monthly_rsi_zscore_126d
    ECONOMIC RATIONALE: Monthly-equivalent RSI.
    """
    base = 100 - (100 / (1 + close.diff(21).clip(lower=0).rolling(14).mean() / close.diff(21).clip(upper=0).abs().rolling(14).mean().replace(0, 1e-9)))
    return _zscore_rolling(base, 126)

def mtfo_042_monthly_rsi_rank_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_042_monthly_rsi_rank_126d
    ECONOMIC RATIONALE: Monthly-equivalent RSI.
    """
    base = 100 - (100 / (1 + close.diff(21).clip(lower=0).rolling(14).mean() / close.diff(21).clip(upper=0).abs().rolling(14).mean().replace(0, 1e-9)))
    return _rank_pct(base, 126)

def mtfo_043_monthly_rsi_lvl_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_043_monthly_rsi_lvl_252d
    ECONOMIC RATIONALE: Monthly-equivalent RSI.
    """
    base = 100 - (100 / (1 + close.diff(21).clip(lower=0).rolling(14).mean() / close.diff(21).clip(upper=0).abs().rolling(14).mean().replace(0, 1e-9)))
    return _rolling_mean(base, 252)

def mtfo_044_monthly_rsi_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_044_monthly_rsi_zscore_252d
    ECONOMIC RATIONALE: Monthly-equivalent RSI.
    """
    base = 100 - (100 / (1 + close.diff(21).clip(lower=0).rolling(14).mean() / close.diff(21).clip(upper=0).abs().rolling(14).mean().replace(0, 1e-9)))
    return _zscore_rolling(base, 252)

def mtfo_045_monthly_rsi_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_045_monthly_rsi_rank_252d
    ECONOMIC RATIONALE: Monthly-equivalent RSI.
    """
    base = 100 - (100 / (1 + close.diff(21).clip(lower=0).rolling(14).mean() / close.diff(21).clip(upper=0).abs().rolling(14).mean().replace(0, 1e-9)))
    return _rank_pct(base, 252)

def mtfo_046_stoch_k_lvl_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_046_stoch_k_lvl_5d
    ECONOMIC RATIONALE: Fast Stochastic %K.
    """
    base = 100 * (close - low.rolling(14).min()) / (high.rolling(14).max() - low.rolling(14).min()).replace(0, 1e-9)
    return _rolling_mean(base, 5)

def mtfo_047_stoch_k_zscore_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_047_stoch_k_zscore_5d
    ECONOMIC RATIONALE: Fast Stochastic %K.
    """
    base = 100 * (close - low.rolling(14).min()) / (high.rolling(14).max() - low.rolling(14).min()).replace(0, 1e-9)
    return _zscore_rolling(base, 5)

def mtfo_048_stoch_k_rank_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_048_stoch_k_rank_5d
    ECONOMIC RATIONALE: Fast Stochastic %K.
    """
    base = 100 * (close - low.rolling(14).min()) / (high.rolling(14).max() - low.rolling(14).min()).replace(0, 1e-9)
    return _rank_pct(base, 5)

def mtfo_049_stoch_k_lvl_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_049_stoch_k_lvl_21d
    ECONOMIC RATIONALE: Fast Stochastic %K.
    """
    base = 100 * (close - low.rolling(14).min()) / (high.rolling(14).max() - low.rolling(14).min()).replace(0, 1e-9)
    return _rolling_mean(base, 21)

def mtfo_050_stoch_k_zscore_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_050_stoch_k_zscore_21d
    ECONOMIC RATIONALE: Fast Stochastic %K.
    """
    base = 100 * (close - low.rolling(14).min()) / (high.rolling(14).max() - low.rolling(14).min()).replace(0, 1e-9)
    return _zscore_rolling(base, 21)

def mtfo_051_stoch_k_rank_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_051_stoch_k_rank_21d
    ECONOMIC RATIONALE: Fast Stochastic %K.
    """
    base = 100 * (close - low.rolling(14).min()) / (high.rolling(14).max() - low.rolling(14).min()).replace(0, 1e-9)
    return _rank_pct(base, 21)

def mtfo_052_stoch_k_lvl_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_052_stoch_k_lvl_63d
    ECONOMIC RATIONALE: Fast Stochastic %K.
    """
    base = 100 * (close - low.rolling(14).min()) / (high.rolling(14).max() - low.rolling(14).min()).replace(0, 1e-9)
    return _rolling_mean(base, 63)

def mtfo_053_stoch_k_zscore_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_053_stoch_k_zscore_63d
    ECONOMIC RATIONALE: Fast Stochastic %K.
    """
    base = 100 * (close - low.rolling(14).min()) / (high.rolling(14).max() - low.rolling(14).min()).replace(0, 1e-9)
    return _zscore_rolling(base, 63)

def mtfo_054_stoch_k_rank_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_054_stoch_k_rank_63d
    ECONOMIC RATIONALE: Fast Stochastic %K.
    """
    base = 100 * (close - low.rolling(14).min()) / (high.rolling(14).max() - low.rolling(14).min()).replace(0, 1e-9)
    return _rank_pct(base, 63)

def mtfo_055_stoch_k_lvl_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_055_stoch_k_lvl_126d
    ECONOMIC RATIONALE: Fast Stochastic %K.
    """
    base = 100 * (close - low.rolling(14).min()) / (high.rolling(14).max() - low.rolling(14).min()).replace(0, 1e-9)
    return _rolling_mean(base, 126)

def mtfo_056_stoch_k_zscore_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_056_stoch_k_zscore_126d
    ECONOMIC RATIONALE: Fast Stochastic %K.
    """
    base = 100 * (close - low.rolling(14).min()) / (high.rolling(14).max() - low.rolling(14).min()).replace(0, 1e-9)
    return _zscore_rolling(base, 126)

def mtfo_057_stoch_k_rank_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_057_stoch_k_rank_126d
    ECONOMIC RATIONALE: Fast Stochastic %K.
    """
    base = 100 * (close - low.rolling(14).min()) / (high.rolling(14).max() - low.rolling(14).min()).replace(0, 1e-9)
    return _rank_pct(base, 126)

def mtfo_058_stoch_k_lvl_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_058_stoch_k_lvl_252d
    ECONOMIC RATIONALE: Fast Stochastic %K.
    """
    base = 100 * (close - low.rolling(14).min()) / (high.rolling(14).max() - low.rolling(14).min()).replace(0, 1e-9)
    return _rolling_mean(base, 252)

def mtfo_059_stoch_k_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_059_stoch_k_zscore_252d
    ECONOMIC RATIONALE: Fast Stochastic %K.
    """
    base = 100 * (close - low.rolling(14).min()) / (high.rolling(14).max() - low.rolling(14).min()).replace(0, 1e-9)
    return _zscore_rolling(base, 252)

def mtfo_060_stoch_k_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_060_stoch_k_rank_252d
    ECONOMIC RATIONALE: Fast Stochastic %K.
    """
    base = 100 * (close - low.rolling(14).min()) / (high.rolling(14).max() - low.rolling(14).min()).replace(0, 1e-9)
    return _rank_pct(base, 252)

def mtfo_061_stoch_d_lvl_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_061_stoch_d_lvl_5d
    ECONOMIC RATIONALE: Slow Stochastic %D.
    """
    base = 100 * (close - low.rolling(14).min()).rolling(3).mean() / (high.rolling(14).max() - low.rolling(14).min()).rolling(3).mean().replace(0, 1e-9)
    return _rolling_mean(base, 5)

def mtfo_062_stoch_d_zscore_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_062_stoch_d_zscore_5d
    ECONOMIC RATIONALE: Slow Stochastic %D.
    """
    base = 100 * (close - low.rolling(14).min()).rolling(3).mean() / (high.rolling(14).max() - low.rolling(14).min()).rolling(3).mean().replace(0, 1e-9)
    return _zscore_rolling(base, 5)

def mtfo_063_stoch_d_rank_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_063_stoch_d_rank_5d
    ECONOMIC RATIONALE: Slow Stochastic %D.
    """
    base = 100 * (close - low.rolling(14).min()).rolling(3).mean() / (high.rolling(14).max() - low.rolling(14).min()).rolling(3).mean().replace(0, 1e-9)
    return _rank_pct(base, 5)

def mtfo_064_stoch_d_lvl_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_064_stoch_d_lvl_21d
    ECONOMIC RATIONALE: Slow Stochastic %D.
    """
    base = 100 * (close - low.rolling(14).min()).rolling(3).mean() / (high.rolling(14).max() - low.rolling(14).min()).rolling(3).mean().replace(0, 1e-9)
    return _rolling_mean(base, 21)

def mtfo_065_stoch_d_zscore_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_065_stoch_d_zscore_21d
    ECONOMIC RATIONALE: Slow Stochastic %D.
    """
    base = 100 * (close - low.rolling(14).min()).rolling(3).mean() / (high.rolling(14).max() - low.rolling(14).min()).rolling(3).mean().replace(0, 1e-9)
    return _zscore_rolling(base, 21)

def mtfo_066_stoch_d_rank_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_066_stoch_d_rank_21d
    ECONOMIC RATIONALE: Slow Stochastic %D.
    """
    base = 100 * (close - low.rolling(14).min()).rolling(3).mean() / (high.rolling(14).max() - low.rolling(14).min()).rolling(3).mean().replace(0, 1e-9)
    return _rank_pct(base, 21)

def mtfo_067_stoch_d_lvl_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_067_stoch_d_lvl_63d
    ECONOMIC RATIONALE: Slow Stochastic %D.
    """
    base = 100 * (close - low.rolling(14).min()).rolling(3).mean() / (high.rolling(14).max() - low.rolling(14).min()).rolling(3).mean().replace(0, 1e-9)
    return _rolling_mean(base, 63)

def mtfo_068_stoch_d_zscore_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_068_stoch_d_zscore_63d
    ECONOMIC RATIONALE: Slow Stochastic %D.
    """
    base = 100 * (close - low.rolling(14).min()).rolling(3).mean() / (high.rolling(14).max() - low.rolling(14).min()).rolling(3).mean().replace(0, 1e-9)
    return _zscore_rolling(base, 63)

def mtfo_069_stoch_d_rank_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_069_stoch_d_rank_63d
    ECONOMIC RATIONALE: Slow Stochastic %D.
    """
    base = 100 * (close - low.rolling(14).min()).rolling(3).mean() / (high.rolling(14).max() - low.rolling(14).min()).rolling(3).mean().replace(0, 1e-9)
    return _rank_pct(base, 63)

def mtfo_070_stoch_d_lvl_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_070_stoch_d_lvl_126d
    ECONOMIC RATIONALE: Slow Stochastic %D.
    """
    base = 100 * (close - low.rolling(14).min()).rolling(3).mean() / (high.rolling(14).max() - low.rolling(14).min()).rolling(3).mean().replace(0, 1e-9)
    return _rolling_mean(base, 126)

def mtfo_071_stoch_d_zscore_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_071_stoch_d_zscore_126d
    ECONOMIC RATIONALE: Slow Stochastic %D.
    """
    base = 100 * (close - low.rolling(14).min()).rolling(3).mean() / (high.rolling(14).max() - low.rolling(14).min()).rolling(3).mean().replace(0, 1e-9)
    return _zscore_rolling(base, 126)

def mtfo_072_stoch_d_rank_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_072_stoch_d_rank_126d
    ECONOMIC RATIONALE: Slow Stochastic %D.
    """
    base = 100 * (close - low.rolling(14).min()).rolling(3).mean() / (high.rolling(14).max() - low.rolling(14).min()).rolling(3).mean().replace(0, 1e-9)
    return _rank_pct(base, 126)

def mtfo_073_stoch_d_lvl_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_073_stoch_d_lvl_252d
    ECONOMIC RATIONALE: Slow Stochastic %D.
    """
    base = 100 * (close - low.rolling(14).min()).rolling(3).mean() / (high.rolling(14).max() - low.rolling(14).min()).rolling(3).mean().replace(0, 1e-9)
    return _rolling_mean(base, 252)

def mtfo_074_stoch_d_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_074_stoch_d_zscore_252d
    ECONOMIC RATIONALE: Slow Stochastic %D.
    """
    base = 100 * (close - low.rolling(14).min()).rolling(3).mean() / (high.rolling(14).max() - low.rolling(14).min()).rolling(3).mean().replace(0, 1e-9)
    return _zscore_rolling(base, 252)

def mtfo_075_stoch_d_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_075_stoch_d_rank_252d
    ECONOMIC RATIONALE: Slow Stochastic %D.
    """
    base = 100 * (close - low.rolling(14).min()).rolling(3).mean() / (high.rolling(14).max() - low.rolling(14).min()).rolling(3).mean().replace(0, 1e-9)
    return _rank_pct(base, 252)

def mtfo_076_multi_tf_oversold_lvl_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_076_multi_tf_oversold_lvl_5d
    ECONOMIC RATIONALE: Convergence of oversold signals across timeframes.
    """
    base = ((daily_rsi < 30) & (weekly_rsi < 30)).astype(float)
    return _rolling_mean(base, 5)

def mtfo_077_multi_tf_oversold_zscore_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_077_multi_tf_oversold_zscore_5d
    ECONOMIC RATIONALE: Convergence of oversold signals across timeframes.
    """
    base = ((daily_rsi < 30) & (weekly_rsi < 30)).astype(float)
    return _zscore_rolling(base, 5)

def mtfo_078_multi_tf_oversold_rank_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_078_multi_tf_oversold_rank_5d
    ECONOMIC RATIONALE: Convergence of oversold signals across timeframes.
    """
    base = ((daily_rsi < 30) & (weekly_rsi < 30)).astype(float)
    return _rank_pct(base, 5)

def mtfo_079_multi_tf_oversold_lvl_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_079_multi_tf_oversold_lvl_21d
    ECONOMIC RATIONALE: Convergence of oversold signals across timeframes.
    """
    base = ((daily_rsi < 30) & (weekly_rsi < 30)).astype(float)
    return _rolling_mean(base, 21)

def mtfo_080_multi_tf_oversold_zscore_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_080_multi_tf_oversold_zscore_21d
    ECONOMIC RATIONALE: Convergence of oversold signals across timeframes.
    """
    base = ((daily_rsi < 30) & (weekly_rsi < 30)).astype(float)
    return _zscore_rolling(base, 21)

def mtfo_081_multi_tf_oversold_rank_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_081_multi_tf_oversold_rank_21d
    ECONOMIC RATIONALE: Convergence of oversold signals across timeframes.
    """
    base = ((daily_rsi < 30) & (weekly_rsi < 30)).astype(float)
    return _rank_pct(base, 21)

def mtfo_082_multi_tf_oversold_lvl_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_082_multi_tf_oversold_lvl_63d
    ECONOMIC RATIONALE: Convergence of oversold signals across timeframes.
    """
    base = ((daily_rsi < 30) & (weekly_rsi < 30)).astype(float)
    return _rolling_mean(base, 63)

def mtfo_083_multi_tf_oversold_zscore_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_083_multi_tf_oversold_zscore_63d
    ECONOMIC RATIONALE: Convergence of oversold signals across timeframes.
    """
    base = ((daily_rsi < 30) & (weekly_rsi < 30)).astype(float)
    return _zscore_rolling(base, 63)

def mtfo_084_multi_tf_oversold_rank_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_084_multi_tf_oversold_rank_63d
    ECONOMIC RATIONALE: Convergence of oversold signals across timeframes.
    """
    base = ((daily_rsi < 30) & (weekly_rsi < 30)).astype(float)
    return _rank_pct(base, 63)

def mtfo_085_multi_tf_oversold_lvl_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_085_multi_tf_oversold_lvl_126d
    ECONOMIC RATIONALE: Convergence of oversold signals across timeframes.
    """
    base = ((daily_rsi < 30) & (weekly_rsi < 30)).astype(float)
    return _rolling_mean(base, 126)

def mtfo_086_multi_tf_oversold_zscore_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_086_multi_tf_oversold_zscore_126d
    ECONOMIC RATIONALE: Convergence of oversold signals across timeframes.
    """
    base = ((daily_rsi < 30) & (weekly_rsi < 30)).astype(float)
    return _zscore_rolling(base, 126)

def mtfo_087_multi_tf_oversold_rank_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_087_multi_tf_oversold_rank_126d
    ECONOMIC RATIONALE: Convergence of oversold signals across timeframes.
    """
    base = ((daily_rsi < 30) & (weekly_rsi < 30)).astype(float)
    return _rank_pct(base, 126)

def mtfo_088_multi_tf_oversold_lvl_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_088_multi_tf_oversold_lvl_252d
    ECONOMIC RATIONALE: Convergence of oversold signals across timeframes.
    """
    base = ((daily_rsi < 30) & (weekly_rsi < 30)).astype(float)
    return _rolling_mean(base, 252)

def mtfo_089_multi_tf_oversold_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_089_multi_tf_oversold_zscore_252d
    ECONOMIC RATIONALE: Convergence of oversold signals across timeframes.
    """
    base = ((daily_rsi < 30) & (weekly_rsi < 30)).astype(float)
    return _zscore_rolling(base, 252)

def mtfo_090_multi_tf_oversold_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_090_multi_tf_oversold_rank_252d
    ECONOMIC RATIONALE: Convergence of oversold signals across timeframes.
    """
    base = ((daily_rsi < 30) & (weekly_rsi < 30)).astype(float)
    return _rank_pct(base, 252)

def mtfo_091_rsi_divergence_lvl_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_091_rsi_divergence_lvl_5d
    ECONOMIC RATIONALE: Divergence between short and long term momentum.
    """
    base = daily_rsi - weekly_rsi
    return _rolling_mean(base, 5)

def mtfo_092_rsi_divergence_zscore_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_092_rsi_divergence_zscore_5d
    ECONOMIC RATIONALE: Divergence between short and long term momentum.
    """
    base = daily_rsi - weekly_rsi
    return _zscore_rolling(base, 5)

def mtfo_093_rsi_divergence_rank_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_093_rsi_divergence_rank_5d
    ECONOMIC RATIONALE: Divergence between short and long term momentum.
    """
    base = daily_rsi - weekly_rsi
    return _rank_pct(base, 5)

def mtfo_094_rsi_divergence_lvl_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_094_rsi_divergence_lvl_21d
    ECONOMIC RATIONALE: Divergence between short and long term momentum.
    """
    base = daily_rsi - weekly_rsi
    return _rolling_mean(base, 21)

def mtfo_095_rsi_divergence_zscore_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_095_rsi_divergence_zscore_21d
    ECONOMIC RATIONALE: Divergence between short and long term momentum.
    """
    base = daily_rsi - weekly_rsi
    return _zscore_rolling(base, 21)

def mtfo_096_rsi_divergence_rank_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_096_rsi_divergence_rank_21d
    ECONOMIC RATIONALE: Divergence between short and long term momentum.
    """
    base = daily_rsi - weekly_rsi
    return _rank_pct(base, 21)

def mtfo_097_rsi_divergence_lvl_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_097_rsi_divergence_lvl_63d
    ECONOMIC RATIONALE: Divergence between short and long term momentum.
    """
    base = daily_rsi - weekly_rsi
    return _rolling_mean(base, 63)

def mtfo_098_rsi_divergence_zscore_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_098_rsi_divergence_zscore_63d
    ECONOMIC RATIONALE: Divergence between short and long term momentum.
    """
    base = daily_rsi - weekly_rsi
    return _zscore_rolling(base, 63)

def mtfo_099_rsi_divergence_rank_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_099_rsi_divergence_rank_63d
    ECONOMIC RATIONALE: Divergence between short and long term momentum.
    """
    base = daily_rsi - weekly_rsi
    return _rank_pct(base, 63)

def mtfo_100_rsi_divergence_lvl_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_100_rsi_divergence_lvl_126d
    ECONOMIC RATIONALE: Divergence between short and long term momentum.
    """
    base = daily_rsi - weekly_rsi
    return _rolling_mean(base, 126)

def mtfo_101_rsi_divergence_zscore_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_101_rsi_divergence_zscore_126d
    ECONOMIC RATIONALE: Divergence between short and long term momentum.
    """
    base = daily_rsi - weekly_rsi
    return _zscore_rolling(base, 126)

def mtfo_102_rsi_divergence_rank_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_102_rsi_divergence_rank_126d
    ECONOMIC RATIONALE: Divergence between short and long term momentum.
    """
    base = daily_rsi - weekly_rsi
    return _rank_pct(base, 126)

def mtfo_103_rsi_divergence_lvl_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_103_rsi_divergence_lvl_252d
    ECONOMIC RATIONALE: Divergence between short and long term momentum.
    """
    base = daily_rsi - weekly_rsi
    return _rolling_mean(base, 252)

def mtfo_104_rsi_divergence_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_104_rsi_divergence_zscore_252d
    ECONOMIC RATIONALE: Divergence between short and long term momentum.
    """
    base = daily_rsi - weekly_rsi
    return _zscore_rolling(base, 252)

def mtfo_105_rsi_divergence_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_105_rsi_divergence_rank_252d
    ECONOMIC RATIONALE: Divergence between short and long term momentum.
    """
    base = daily_rsi - weekly_rsi
    return _rank_pct(base, 252)

def mtfo_106_oversold_persistence_lvl_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_106_oversold_persistence_lvl_5d
    ECONOMIC RATIONALE: Duration of extremely oversold conditions.
    """
    base = (daily_rsi < 30).rolling(10).sum()
    return _rolling_mean(base, 5)

def mtfo_107_oversold_persistence_zscore_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_107_oversold_persistence_zscore_5d
    ECONOMIC RATIONALE: Duration of extremely oversold conditions.
    """
    base = (daily_rsi < 30).rolling(10).sum()
    return _zscore_rolling(base, 5)

def mtfo_108_oversold_persistence_rank_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_108_oversold_persistence_rank_5d
    ECONOMIC RATIONALE: Duration of extremely oversold conditions.
    """
    base = (daily_rsi < 30).rolling(10).sum()
    return _rank_pct(base, 5)

def mtfo_109_oversold_persistence_lvl_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_109_oversold_persistence_lvl_21d
    ECONOMIC RATIONALE: Duration of extremely oversold conditions.
    """
    base = (daily_rsi < 30).rolling(10).sum()
    return _rolling_mean(base, 21)

def mtfo_110_oversold_persistence_zscore_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_110_oversold_persistence_zscore_21d
    ECONOMIC RATIONALE: Duration of extremely oversold conditions.
    """
    base = (daily_rsi < 30).rolling(10).sum()
    return _zscore_rolling(base, 21)

def mtfo_111_oversold_persistence_rank_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_111_oversold_persistence_rank_21d
    ECONOMIC RATIONALE: Duration of extremely oversold conditions.
    """
    base = (daily_rsi < 30).rolling(10).sum()
    return _rank_pct(base, 21)

def mtfo_112_oversold_persistence_lvl_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_112_oversold_persistence_lvl_63d
    ECONOMIC RATIONALE: Duration of extremely oversold conditions.
    """
    base = (daily_rsi < 30).rolling(10).sum()
    return _rolling_mean(base, 63)

def mtfo_113_oversold_persistence_zscore_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_113_oversold_persistence_zscore_63d
    ECONOMIC RATIONALE: Duration of extremely oversold conditions.
    """
    base = (daily_rsi < 30).rolling(10).sum()
    return _zscore_rolling(base, 63)

def mtfo_114_oversold_persistence_rank_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_114_oversold_persistence_rank_63d
    ECONOMIC RATIONALE: Duration of extremely oversold conditions.
    """
    base = (daily_rsi < 30).rolling(10).sum()
    return _rank_pct(base, 63)

def mtfo_115_oversold_persistence_lvl_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_115_oversold_persistence_lvl_126d
    ECONOMIC RATIONALE: Duration of extremely oversold conditions.
    """
    base = (daily_rsi < 30).rolling(10).sum()
    return _rolling_mean(base, 126)

def mtfo_116_oversold_persistence_zscore_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_116_oversold_persistence_zscore_126d
    ECONOMIC RATIONALE: Duration of extremely oversold conditions.
    """
    base = (daily_rsi < 30).rolling(10).sum()
    return _zscore_rolling(base, 126)

def mtfo_117_oversold_persistence_rank_126d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_117_oversold_persistence_rank_126d
    ECONOMIC RATIONALE: Duration of extremely oversold conditions.
    """
    base = (daily_rsi < 30).rolling(10).sum()
    return _rank_pct(base, 126)

def mtfo_118_oversold_persistence_lvl_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_118_oversold_persistence_lvl_252d
    ECONOMIC RATIONALE: Duration of extremely oversold conditions.
    """
    base = (daily_rsi < 30).rolling(10).sum()
    return _rolling_mean(base, 252)

def mtfo_119_oversold_persistence_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_119_oversold_persistence_zscore_252d
    ECONOMIC RATIONALE: Duration of extremely oversold conditions.
    """
    base = (daily_rsi < 30).rolling(10).sum()
    return _zscore_rolling(base, 252)

def mtfo_120_oversold_persistence_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    mtfo_120_oversold_persistence_rank_252d
    ECONOMIC RATIONALE: Duration of extremely oversold conditions.
    """
    base = (daily_rsi < 30).rolling(10).sum()
    return _rank_pct(base, 252)

# ── Registry ──────────────────────────────────────────────────────────────────
V103_REGISTRY_1 = {
    "mtfo_001_daily_rsi_lvl_5d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_001_daily_rsi_lvl_5d},
    "mtfo_002_daily_rsi_zscore_5d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_002_daily_rsi_zscore_5d},
    "mtfo_003_daily_rsi_rank_5d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_003_daily_rsi_rank_5d},
    "mtfo_004_daily_rsi_lvl_21d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_004_daily_rsi_lvl_21d},
    "mtfo_005_daily_rsi_zscore_21d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_005_daily_rsi_zscore_21d},
    "mtfo_006_daily_rsi_rank_21d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_006_daily_rsi_rank_21d},
    "mtfo_007_daily_rsi_lvl_63d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_007_daily_rsi_lvl_63d},
    "mtfo_008_daily_rsi_zscore_63d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_008_daily_rsi_zscore_63d},
    "mtfo_009_daily_rsi_rank_63d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_009_daily_rsi_rank_63d},
    "mtfo_010_daily_rsi_lvl_126d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_010_daily_rsi_lvl_126d},
    "mtfo_011_daily_rsi_zscore_126d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_011_daily_rsi_zscore_126d},
    "mtfo_012_daily_rsi_rank_126d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_012_daily_rsi_rank_126d},
    "mtfo_013_daily_rsi_lvl_252d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_013_daily_rsi_lvl_252d},
    "mtfo_014_daily_rsi_zscore_252d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_014_daily_rsi_zscore_252d},
    "mtfo_015_daily_rsi_rank_252d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_015_daily_rsi_rank_252d},
    "mtfo_016_weekly_rsi_lvl_5d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_016_weekly_rsi_lvl_5d},
    "mtfo_017_weekly_rsi_zscore_5d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_017_weekly_rsi_zscore_5d},
    "mtfo_018_weekly_rsi_rank_5d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_018_weekly_rsi_rank_5d},
    "mtfo_019_weekly_rsi_lvl_21d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_019_weekly_rsi_lvl_21d},
    "mtfo_020_weekly_rsi_zscore_21d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_020_weekly_rsi_zscore_21d},
    "mtfo_021_weekly_rsi_rank_21d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_021_weekly_rsi_rank_21d},
    "mtfo_022_weekly_rsi_lvl_63d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_022_weekly_rsi_lvl_63d},
    "mtfo_023_weekly_rsi_zscore_63d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_023_weekly_rsi_zscore_63d},
    "mtfo_024_weekly_rsi_rank_63d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_024_weekly_rsi_rank_63d},
    "mtfo_025_weekly_rsi_lvl_126d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_025_weekly_rsi_lvl_126d},
    "mtfo_026_weekly_rsi_zscore_126d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_026_weekly_rsi_zscore_126d},
    "mtfo_027_weekly_rsi_rank_126d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_027_weekly_rsi_rank_126d},
    "mtfo_028_weekly_rsi_lvl_252d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_028_weekly_rsi_lvl_252d},
    "mtfo_029_weekly_rsi_zscore_252d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_029_weekly_rsi_zscore_252d},
    "mtfo_030_weekly_rsi_rank_252d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_030_weekly_rsi_rank_252d},
    "mtfo_031_monthly_rsi_lvl_5d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_031_monthly_rsi_lvl_5d},
    "mtfo_032_monthly_rsi_zscore_5d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_032_monthly_rsi_zscore_5d},
    "mtfo_033_monthly_rsi_rank_5d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_033_monthly_rsi_rank_5d},
    "mtfo_034_monthly_rsi_lvl_21d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_034_monthly_rsi_lvl_21d},
    "mtfo_035_monthly_rsi_zscore_21d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_035_monthly_rsi_zscore_21d},
    "mtfo_036_monthly_rsi_rank_21d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_036_monthly_rsi_rank_21d},
    "mtfo_037_monthly_rsi_lvl_63d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_037_monthly_rsi_lvl_63d},
    "mtfo_038_monthly_rsi_zscore_63d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_038_monthly_rsi_zscore_63d},
    "mtfo_039_monthly_rsi_rank_63d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_039_monthly_rsi_rank_63d},
    "mtfo_040_monthly_rsi_lvl_126d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_040_monthly_rsi_lvl_126d},
    "mtfo_041_monthly_rsi_zscore_126d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_041_monthly_rsi_zscore_126d},
    "mtfo_042_monthly_rsi_rank_126d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_042_monthly_rsi_rank_126d},
    "mtfo_043_monthly_rsi_lvl_252d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_043_monthly_rsi_lvl_252d},
    "mtfo_044_monthly_rsi_zscore_252d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_044_monthly_rsi_zscore_252d},
    "mtfo_045_monthly_rsi_rank_252d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_045_monthly_rsi_rank_252d},
    "mtfo_046_stoch_k_lvl_5d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_046_stoch_k_lvl_5d},
    "mtfo_047_stoch_k_zscore_5d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_047_stoch_k_zscore_5d},
    "mtfo_048_stoch_k_rank_5d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_048_stoch_k_rank_5d},
    "mtfo_049_stoch_k_lvl_21d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_049_stoch_k_lvl_21d},
    "mtfo_050_stoch_k_zscore_21d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_050_stoch_k_zscore_21d},
    "mtfo_051_stoch_k_rank_21d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_051_stoch_k_rank_21d},
    "mtfo_052_stoch_k_lvl_63d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_052_stoch_k_lvl_63d},
    "mtfo_053_stoch_k_zscore_63d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_053_stoch_k_zscore_63d},
    "mtfo_054_stoch_k_rank_63d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_054_stoch_k_rank_63d},
    "mtfo_055_stoch_k_lvl_126d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_055_stoch_k_lvl_126d},
    "mtfo_056_stoch_k_zscore_126d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_056_stoch_k_zscore_126d},
    "mtfo_057_stoch_k_rank_126d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_057_stoch_k_rank_126d},
    "mtfo_058_stoch_k_lvl_252d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_058_stoch_k_lvl_252d},
    "mtfo_059_stoch_k_zscore_252d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_059_stoch_k_zscore_252d},
    "mtfo_060_stoch_k_rank_252d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_060_stoch_k_rank_252d},
    "mtfo_061_stoch_d_lvl_5d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_061_stoch_d_lvl_5d},
    "mtfo_062_stoch_d_zscore_5d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_062_stoch_d_zscore_5d},
    "mtfo_063_stoch_d_rank_5d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_063_stoch_d_rank_5d},
    "mtfo_064_stoch_d_lvl_21d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_064_stoch_d_lvl_21d},
    "mtfo_065_stoch_d_zscore_21d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_065_stoch_d_zscore_21d},
    "mtfo_066_stoch_d_rank_21d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_066_stoch_d_rank_21d},
    "mtfo_067_stoch_d_lvl_63d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_067_stoch_d_lvl_63d},
    "mtfo_068_stoch_d_zscore_63d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_068_stoch_d_zscore_63d},
    "mtfo_069_stoch_d_rank_63d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_069_stoch_d_rank_63d},
    "mtfo_070_stoch_d_lvl_126d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_070_stoch_d_lvl_126d},
    "mtfo_071_stoch_d_zscore_126d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_071_stoch_d_zscore_126d},
    "mtfo_072_stoch_d_rank_126d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_072_stoch_d_rank_126d},
    "mtfo_073_stoch_d_lvl_252d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_073_stoch_d_lvl_252d},
    "mtfo_074_stoch_d_zscore_252d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_074_stoch_d_zscore_252d},
    "mtfo_075_stoch_d_rank_252d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_075_stoch_d_rank_252d},
    "mtfo_076_multi_tf_oversold_lvl_5d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_076_multi_tf_oversold_lvl_5d},
    "mtfo_077_multi_tf_oversold_zscore_5d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_077_multi_tf_oversold_zscore_5d},
    "mtfo_078_multi_tf_oversold_rank_5d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_078_multi_tf_oversold_rank_5d},
    "mtfo_079_multi_tf_oversold_lvl_21d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_079_multi_tf_oversold_lvl_21d},
    "mtfo_080_multi_tf_oversold_zscore_21d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_080_multi_tf_oversold_zscore_21d},
    "mtfo_081_multi_tf_oversold_rank_21d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_081_multi_tf_oversold_rank_21d},
    "mtfo_082_multi_tf_oversold_lvl_63d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_082_multi_tf_oversold_lvl_63d},
    "mtfo_083_multi_tf_oversold_zscore_63d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_083_multi_tf_oversold_zscore_63d},
    "mtfo_084_multi_tf_oversold_rank_63d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_084_multi_tf_oversold_rank_63d},
    "mtfo_085_multi_tf_oversold_lvl_126d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_085_multi_tf_oversold_lvl_126d},
    "mtfo_086_multi_tf_oversold_zscore_126d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_086_multi_tf_oversold_zscore_126d},
    "mtfo_087_multi_tf_oversold_rank_126d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_087_multi_tf_oversold_rank_126d},
    "mtfo_088_multi_tf_oversold_lvl_252d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_088_multi_tf_oversold_lvl_252d},
    "mtfo_089_multi_tf_oversold_zscore_252d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_089_multi_tf_oversold_zscore_252d},
    "mtfo_090_multi_tf_oversold_rank_252d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_090_multi_tf_oversold_rank_252d},
    "mtfo_091_rsi_divergence_lvl_5d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_091_rsi_divergence_lvl_5d},
    "mtfo_092_rsi_divergence_zscore_5d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_092_rsi_divergence_zscore_5d},
    "mtfo_093_rsi_divergence_rank_5d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_093_rsi_divergence_rank_5d},
    "mtfo_094_rsi_divergence_lvl_21d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_094_rsi_divergence_lvl_21d},
    "mtfo_095_rsi_divergence_zscore_21d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_095_rsi_divergence_zscore_21d},
    "mtfo_096_rsi_divergence_rank_21d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_096_rsi_divergence_rank_21d},
    "mtfo_097_rsi_divergence_lvl_63d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_097_rsi_divergence_lvl_63d},
    "mtfo_098_rsi_divergence_zscore_63d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_098_rsi_divergence_zscore_63d},
    "mtfo_099_rsi_divergence_rank_63d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_099_rsi_divergence_rank_63d},
    "mtfo_100_rsi_divergence_lvl_126d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_100_rsi_divergence_lvl_126d},
    "mtfo_101_rsi_divergence_zscore_126d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_101_rsi_divergence_zscore_126d},
    "mtfo_102_rsi_divergence_rank_126d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_102_rsi_divergence_rank_126d},
    "mtfo_103_rsi_divergence_lvl_252d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_103_rsi_divergence_lvl_252d},
    "mtfo_104_rsi_divergence_zscore_252d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_104_rsi_divergence_zscore_252d},
    "mtfo_105_rsi_divergence_rank_252d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_105_rsi_divergence_rank_252d},
    "mtfo_106_oversold_persistence_lvl_5d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_106_oversold_persistence_lvl_5d},
    "mtfo_107_oversold_persistence_zscore_5d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_107_oversold_persistence_zscore_5d},
    "mtfo_108_oversold_persistence_rank_5d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_108_oversold_persistence_rank_5d},
    "mtfo_109_oversold_persistence_lvl_21d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_109_oversold_persistence_lvl_21d},
    "mtfo_110_oversold_persistence_zscore_21d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_110_oversold_persistence_zscore_21d},
    "mtfo_111_oversold_persistence_rank_21d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_111_oversold_persistence_rank_21d},
    "mtfo_112_oversold_persistence_lvl_63d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_112_oversold_persistence_lvl_63d},
    "mtfo_113_oversold_persistence_zscore_63d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_113_oversold_persistence_zscore_63d},
    "mtfo_114_oversold_persistence_rank_63d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_114_oversold_persistence_rank_63d},
    "mtfo_115_oversold_persistence_lvl_126d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_115_oversold_persistence_lvl_126d},
    "mtfo_116_oversold_persistence_zscore_126d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_116_oversold_persistence_zscore_126d},
    "mtfo_117_oversold_persistence_rank_126d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_117_oversold_persistence_rank_126d},
    "mtfo_118_oversold_persistence_lvl_252d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_118_oversold_persistence_lvl_252d},
    "mtfo_119_oversold_persistence_zscore_252d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_119_oversold_persistence_zscore_252d},
    "mtfo_120_oversold_persistence_rank_252d": {"inputs": ["close", "high", "low", "volume"], "func": mtfo_120_oversold_persistence_rank_252d},
}
