"""
120_information_decay — Base Features Part 1
Domain: information_decay
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

def idec_001_price_impact_decay_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_001_price_impact_decay_lvl_5d
    ECONOMIC RATIONALE: Decaying magnitude of recent price impacts.
    """
    base = close.diff(1).abs().ewm(halflife=5).mean()
    return _rolling_mean(base, 5)

def idec_002_price_impact_decay_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_002_price_impact_decay_zscore_5d
    ECONOMIC RATIONALE: Decaying magnitude of recent price impacts.
    """
    base = close.diff(1).abs().ewm(halflife=5).mean()
    return _zscore_rolling(base, 5)

def idec_003_price_impact_decay_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_003_price_impact_decay_rank_5d
    ECONOMIC RATIONALE: Decaying magnitude of recent price impacts.
    """
    base = close.diff(1).abs().ewm(halflife=5).mean()
    return _rank_pct(base, 5)

def idec_004_price_impact_decay_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_004_price_impact_decay_lvl_21d
    ECONOMIC RATIONALE: Decaying magnitude of recent price impacts.
    """
    base = close.diff(1).abs().ewm(halflife=5).mean()
    return _rolling_mean(base, 21)

def idec_005_price_impact_decay_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_005_price_impact_decay_zscore_21d
    ECONOMIC RATIONALE: Decaying magnitude of recent price impacts.
    """
    base = close.diff(1).abs().ewm(halflife=5).mean()
    return _zscore_rolling(base, 21)

def idec_006_price_impact_decay_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_006_price_impact_decay_rank_21d
    ECONOMIC RATIONALE: Decaying magnitude of recent price impacts.
    """
    base = close.diff(1).abs().ewm(halflife=5).mean()
    return _rank_pct(base, 21)

def idec_007_price_impact_decay_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_007_price_impact_decay_lvl_63d
    ECONOMIC RATIONALE: Decaying magnitude of recent price impacts.
    """
    base = close.diff(1).abs().ewm(halflife=5).mean()
    return _rolling_mean(base, 63)

def idec_008_price_impact_decay_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_008_price_impact_decay_zscore_63d
    ECONOMIC RATIONALE: Decaying magnitude of recent price impacts.
    """
    base = close.diff(1).abs().ewm(halflife=5).mean()
    return _zscore_rolling(base, 63)

def idec_009_price_impact_decay_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_009_price_impact_decay_rank_63d
    ECONOMIC RATIONALE: Decaying magnitude of recent price impacts.
    """
    base = close.diff(1).abs().ewm(halflife=5).mean()
    return _rank_pct(base, 63)

def idec_010_price_impact_decay_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_010_price_impact_decay_lvl_126d
    ECONOMIC RATIONALE: Decaying magnitude of recent price impacts.
    """
    base = close.diff(1).abs().ewm(halflife=5).mean()
    return _rolling_mean(base, 126)

def idec_011_price_impact_decay_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_011_price_impact_decay_zscore_126d
    ECONOMIC RATIONALE: Decaying magnitude of recent price impacts.
    """
    base = close.diff(1).abs().ewm(halflife=5).mean()
    return _zscore_rolling(base, 126)

def idec_012_price_impact_decay_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_012_price_impact_decay_rank_126d
    ECONOMIC RATIONALE: Decaying magnitude of recent price impacts.
    """
    base = close.diff(1).abs().ewm(halflife=5).mean()
    return _rank_pct(base, 126)

def idec_013_price_impact_decay_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_013_price_impact_decay_lvl_252d
    ECONOMIC RATIONALE: Decaying magnitude of recent price impacts.
    """
    base = close.diff(1).abs().ewm(halflife=5).mean()
    return _rolling_mean(base, 252)

def idec_014_price_impact_decay_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_014_price_impact_decay_zscore_252d
    ECONOMIC RATIONALE: Decaying magnitude of recent price impacts.
    """
    base = close.diff(1).abs().ewm(halflife=5).mean()
    return _zscore_rolling(base, 252)

def idec_015_price_impact_decay_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_015_price_impact_decay_rank_252d
    ECONOMIC RATIONALE: Decaying magnitude of recent price impacts.
    """
    base = close.diff(1).abs().ewm(halflife=5).mean()
    return _rank_pct(base, 252)

def idec_016_volume_impact_decay_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_016_volume_impact_decay_lvl_5d
    ECONOMIC RATIONALE: Decaying intensity of recent volume spikes.
    """
    base = volume.ewm(halflife=5).mean() / volume.rolling(63).mean()
    return _rolling_mean(base, 5)

def idec_017_volume_impact_decay_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_017_volume_impact_decay_zscore_5d
    ECONOMIC RATIONALE: Decaying intensity of recent volume spikes.
    """
    base = volume.ewm(halflife=5).mean() / volume.rolling(63).mean()
    return _zscore_rolling(base, 5)

def idec_018_volume_impact_decay_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_018_volume_impact_decay_rank_5d
    ECONOMIC RATIONALE: Decaying intensity of recent volume spikes.
    """
    base = volume.ewm(halflife=5).mean() / volume.rolling(63).mean()
    return _rank_pct(base, 5)

def idec_019_volume_impact_decay_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_019_volume_impact_decay_lvl_21d
    ECONOMIC RATIONALE: Decaying intensity of recent volume spikes.
    """
    base = volume.ewm(halflife=5).mean() / volume.rolling(63).mean()
    return _rolling_mean(base, 21)

def idec_020_volume_impact_decay_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_020_volume_impact_decay_zscore_21d
    ECONOMIC RATIONALE: Decaying intensity of recent volume spikes.
    """
    base = volume.ewm(halflife=5).mean() / volume.rolling(63).mean()
    return _zscore_rolling(base, 21)

def idec_021_volume_impact_decay_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_021_volume_impact_decay_rank_21d
    ECONOMIC RATIONALE: Decaying intensity of recent volume spikes.
    """
    base = volume.ewm(halflife=5).mean() / volume.rolling(63).mean()
    return _rank_pct(base, 21)

def idec_022_volume_impact_decay_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_022_volume_impact_decay_lvl_63d
    ECONOMIC RATIONALE: Decaying intensity of recent volume spikes.
    """
    base = volume.ewm(halflife=5).mean() / volume.rolling(63).mean()
    return _rolling_mean(base, 63)

def idec_023_volume_impact_decay_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_023_volume_impact_decay_zscore_63d
    ECONOMIC RATIONALE: Decaying intensity of recent volume spikes.
    """
    base = volume.ewm(halflife=5).mean() / volume.rolling(63).mean()
    return _zscore_rolling(base, 63)

def idec_024_volume_impact_decay_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_024_volume_impact_decay_rank_63d
    ECONOMIC RATIONALE: Decaying intensity of recent volume spikes.
    """
    base = volume.ewm(halflife=5).mean() / volume.rolling(63).mean()
    return _rank_pct(base, 63)

def idec_025_volume_impact_decay_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_025_volume_impact_decay_lvl_126d
    ECONOMIC RATIONALE: Decaying intensity of recent volume spikes.
    """
    base = volume.ewm(halflife=5).mean() / volume.rolling(63).mean()
    return _rolling_mean(base, 126)

def idec_026_volume_impact_decay_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_026_volume_impact_decay_zscore_126d
    ECONOMIC RATIONALE: Decaying intensity of recent volume spikes.
    """
    base = volume.ewm(halflife=5).mean() / volume.rolling(63).mean()
    return _zscore_rolling(base, 126)

def idec_027_volume_impact_decay_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_027_volume_impact_decay_rank_126d
    ECONOMIC RATIONALE: Decaying intensity of recent volume spikes.
    """
    base = volume.ewm(halflife=5).mean() / volume.rolling(63).mean()
    return _rank_pct(base, 126)

def idec_028_volume_impact_decay_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_028_volume_impact_decay_lvl_252d
    ECONOMIC RATIONALE: Decaying intensity of recent volume spikes.
    """
    base = volume.ewm(halflife=5).mean() / volume.rolling(63).mean()
    return _rolling_mean(base, 252)

def idec_029_volume_impact_decay_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_029_volume_impact_decay_zscore_252d
    ECONOMIC RATIONALE: Decaying intensity of recent volume spikes.
    """
    base = volume.ewm(halflife=5).mean() / volume.rolling(63).mean()
    return _zscore_rolling(base, 252)

def idec_030_volume_impact_decay_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_030_volume_impact_decay_rank_252d
    ECONOMIC RATIONALE: Decaying intensity of recent volume spikes.
    """
    base = volume.ewm(halflife=5).mean() / volume.rolling(63).mean()
    return _rank_pct(base, 252)

def idec_031_information_horizon_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_031_information_horizon_lvl_5d
    ECONOMIC RATIONALE: Long-term memory of price levels.
    """
    base = close.rolling(21).corr(close.shift(21))
    return _rolling_mean(base, 5)

def idec_032_information_horizon_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_032_information_horizon_zscore_5d
    ECONOMIC RATIONALE: Long-term memory of price levels.
    """
    base = close.rolling(21).corr(close.shift(21))
    return _zscore_rolling(base, 5)

def idec_033_information_horizon_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_033_information_horizon_rank_5d
    ECONOMIC RATIONALE: Long-term memory of price levels.
    """
    base = close.rolling(21).corr(close.shift(21))
    return _rank_pct(base, 5)

def idec_034_information_horizon_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_034_information_horizon_lvl_21d
    ECONOMIC RATIONALE: Long-term memory of price levels.
    """
    base = close.rolling(21).corr(close.shift(21))
    return _rolling_mean(base, 21)

def idec_035_information_horizon_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_035_information_horizon_zscore_21d
    ECONOMIC RATIONALE: Long-term memory of price levels.
    """
    base = close.rolling(21).corr(close.shift(21))
    return _zscore_rolling(base, 21)

def idec_036_information_horizon_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_036_information_horizon_rank_21d
    ECONOMIC RATIONALE: Long-term memory of price levels.
    """
    base = close.rolling(21).corr(close.shift(21))
    return _rank_pct(base, 21)

def idec_037_information_horizon_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_037_information_horizon_lvl_63d
    ECONOMIC RATIONALE: Long-term memory of price levels.
    """
    base = close.rolling(21).corr(close.shift(21))
    return _rolling_mean(base, 63)

def idec_038_information_horizon_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_038_information_horizon_zscore_63d
    ECONOMIC RATIONALE: Long-term memory of price levels.
    """
    base = close.rolling(21).corr(close.shift(21))
    return _zscore_rolling(base, 63)

def idec_039_information_horizon_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_039_information_horizon_rank_63d
    ECONOMIC RATIONALE: Long-term memory of price levels.
    """
    base = close.rolling(21).corr(close.shift(21))
    return _rank_pct(base, 63)

def idec_040_information_horizon_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_040_information_horizon_lvl_126d
    ECONOMIC RATIONALE: Long-term memory of price levels.
    """
    base = close.rolling(21).corr(close.shift(21))
    return _rolling_mean(base, 126)

def idec_041_information_horizon_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_041_information_horizon_zscore_126d
    ECONOMIC RATIONALE: Long-term memory of price levels.
    """
    base = close.rolling(21).corr(close.shift(21))
    return _zscore_rolling(base, 126)

def idec_042_information_horizon_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_042_information_horizon_rank_126d
    ECONOMIC RATIONALE: Long-term memory of price levels.
    """
    base = close.rolling(21).corr(close.shift(21))
    return _rank_pct(base, 126)

def idec_043_information_horizon_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_043_information_horizon_lvl_252d
    ECONOMIC RATIONALE: Long-term memory of price levels.
    """
    base = close.rolling(21).corr(close.shift(21))
    return _rolling_mean(base, 252)

def idec_044_information_horizon_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_044_information_horizon_zscore_252d
    ECONOMIC RATIONALE: Long-term memory of price levels.
    """
    base = close.rolling(21).corr(close.shift(21))
    return _zscore_rolling(base, 252)

def idec_045_information_horizon_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_045_information_horizon_rank_252d
    ECONOMIC RATIONALE: Long-term memory of price levels.
    """
    base = close.rolling(21).corr(close.shift(21))
    return _rank_pct(base, 252)

def idec_046_news_response_decay_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_046_news_response_decay_lvl_5d
    ECONOMIC RATIONALE: Recent daily change relative to cumulative monthly change.
    """
    base = close.pct_change(1).abs() / close.pct_change(21).abs().shift(1).replace(0, 1e-9)
    return _rolling_mean(base, 5)

def idec_047_news_response_decay_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_047_news_response_decay_zscore_5d
    ECONOMIC RATIONALE: Recent daily change relative to cumulative monthly change.
    """
    base = close.pct_change(1).abs() / close.pct_change(21).abs().shift(1).replace(0, 1e-9)
    return _zscore_rolling(base, 5)

def idec_048_news_response_decay_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_048_news_response_decay_rank_5d
    ECONOMIC RATIONALE: Recent daily change relative to cumulative monthly change.
    """
    base = close.pct_change(1).abs() / close.pct_change(21).abs().shift(1).replace(0, 1e-9)
    return _rank_pct(base, 5)

def idec_049_news_response_decay_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_049_news_response_decay_lvl_21d
    ECONOMIC RATIONALE: Recent daily change relative to cumulative monthly change.
    """
    base = close.pct_change(1).abs() / close.pct_change(21).abs().shift(1).replace(0, 1e-9)
    return _rolling_mean(base, 21)

def idec_050_news_response_decay_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_050_news_response_decay_zscore_21d
    ECONOMIC RATIONALE: Recent daily change relative to cumulative monthly change.
    """
    base = close.pct_change(1).abs() / close.pct_change(21).abs().shift(1).replace(0, 1e-9)
    return _zscore_rolling(base, 21)

def idec_051_news_response_decay_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_051_news_response_decay_rank_21d
    ECONOMIC RATIONALE: Recent daily change relative to cumulative monthly change.
    """
    base = close.pct_change(1).abs() / close.pct_change(21).abs().shift(1).replace(0, 1e-9)
    return _rank_pct(base, 21)

def idec_052_news_response_decay_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_052_news_response_decay_lvl_63d
    ECONOMIC RATIONALE: Recent daily change relative to cumulative monthly change.
    """
    base = close.pct_change(1).abs() / close.pct_change(21).abs().shift(1).replace(0, 1e-9)
    return _rolling_mean(base, 63)

def idec_053_news_response_decay_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_053_news_response_decay_zscore_63d
    ECONOMIC RATIONALE: Recent daily change relative to cumulative monthly change.
    """
    base = close.pct_change(1).abs() / close.pct_change(21).abs().shift(1).replace(0, 1e-9)
    return _zscore_rolling(base, 63)

def idec_054_news_response_decay_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_054_news_response_decay_rank_63d
    ECONOMIC RATIONALE: Recent daily change relative to cumulative monthly change.
    """
    base = close.pct_change(1).abs() / close.pct_change(21).abs().shift(1).replace(0, 1e-9)
    return _rank_pct(base, 63)

def idec_055_news_response_decay_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_055_news_response_decay_lvl_126d
    ECONOMIC RATIONALE: Recent daily change relative to cumulative monthly change.
    """
    base = close.pct_change(1).abs() / close.pct_change(21).abs().shift(1).replace(0, 1e-9)
    return _rolling_mean(base, 126)

def idec_056_news_response_decay_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_056_news_response_decay_zscore_126d
    ECONOMIC RATIONALE: Recent daily change relative to cumulative monthly change.
    """
    base = close.pct_change(1).abs() / close.pct_change(21).abs().shift(1).replace(0, 1e-9)
    return _zscore_rolling(base, 126)

def idec_057_news_response_decay_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_057_news_response_decay_rank_126d
    ECONOMIC RATIONALE: Recent daily change relative to cumulative monthly change.
    """
    base = close.pct_change(1).abs() / close.pct_change(21).abs().shift(1).replace(0, 1e-9)
    return _rank_pct(base, 126)

def idec_058_news_response_decay_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_058_news_response_decay_lvl_252d
    ECONOMIC RATIONALE: Recent daily change relative to cumulative monthly change.
    """
    base = close.pct_change(1).abs() / close.pct_change(21).abs().shift(1).replace(0, 1e-9)
    return _rolling_mean(base, 252)

def idec_059_news_response_decay_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_059_news_response_decay_zscore_252d
    ECONOMIC RATIONALE: Recent daily change relative to cumulative monthly change.
    """
    base = close.pct_change(1).abs() / close.pct_change(21).abs().shift(1).replace(0, 1e-9)
    return _zscore_rolling(base, 252)

def idec_060_news_response_decay_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_060_news_response_decay_rank_252d
    ECONOMIC RATIONALE: Recent daily change relative to cumulative monthly change.
    """
    base = close.pct_change(1).abs() / close.pct_change(21).abs().shift(1).replace(0, 1e-9)
    return _rank_pct(base, 252)

def idec_061_autocorr_decay_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_061_autocorr_decay_lvl_5d
    ECONOMIC RATIONALE: Decay in serial correlation across timeframes.
    """
    base = close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) / close.pct_change(1).rolling(63).apply(lambda x: x.autocorr(1)).replace(0, 1e-9)
    return _rolling_mean(base, 5)

def idec_062_autocorr_decay_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_062_autocorr_decay_zscore_5d
    ECONOMIC RATIONALE: Decay in serial correlation across timeframes.
    """
    base = close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) / close.pct_change(1).rolling(63).apply(lambda x: x.autocorr(1)).replace(0, 1e-9)
    return _zscore_rolling(base, 5)

def idec_063_autocorr_decay_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_063_autocorr_decay_rank_5d
    ECONOMIC RATIONALE: Decay in serial correlation across timeframes.
    """
    base = close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) / close.pct_change(1).rolling(63).apply(lambda x: x.autocorr(1)).replace(0, 1e-9)
    return _rank_pct(base, 5)

def idec_064_autocorr_decay_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_064_autocorr_decay_lvl_21d
    ECONOMIC RATIONALE: Decay in serial correlation across timeframes.
    """
    base = close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) / close.pct_change(1).rolling(63).apply(lambda x: x.autocorr(1)).replace(0, 1e-9)
    return _rolling_mean(base, 21)

def idec_065_autocorr_decay_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_065_autocorr_decay_zscore_21d
    ECONOMIC RATIONALE: Decay in serial correlation across timeframes.
    """
    base = close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) / close.pct_change(1).rolling(63).apply(lambda x: x.autocorr(1)).replace(0, 1e-9)
    return _zscore_rolling(base, 21)

def idec_066_autocorr_decay_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_066_autocorr_decay_rank_21d
    ECONOMIC RATIONALE: Decay in serial correlation across timeframes.
    """
    base = close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) / close.pct_change(1).rolling(63).apply(lambda x: x.autocorr(1)).replace(0, 1e-9)
    return _rank_pct(base, 21)

def idec_067_autocorr_decay_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_067_autocorr_decay_lvl_63d
    ECONOMIC RATIONALE: Decay in serial correlation across timeframes.
    """
    base = close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) / close.pct_change(1).rolling(63).apply(lambda x: x.autocorr(1)).replace(0, 1e-9)
    return _rolling_mean(base, 63)

def idec_068_autocorr_decay_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_068_autocorr_decay_zscore_63d
    ECONOMIC RATIONALE: Decay in serial correlation across timeframes.
    """
    base = close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) / close.pct_change(1).rolling(63).apply(lambda x: x.autocorr(1)).replace(0, 1e-9)
    return _zscore_rolling(base, 63)

def idec_069_autocorr_decay_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_069_autocorr_decay_rank_63d
    ECONOMIC RATIONALE: Decay in serial correlation across timeframes.
    """
    base = close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) / close.pct_change(1).rolling(63).apply(lambda x: x.autocorr(1)).replace(0, 1e-9)
    return _rank_pct(base, 63)

def idec_070_autocorr_decay_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_070_autocorr_decay_lvl_126d
    ECONOMIC RATIONALE: Decay in serial correlation across timeframes.
    """
    base = close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) / close.pct_change(1).rolling(63).apply(lambda x: x.autocorr(1)).replace(0, 1e-9)
    return _rolling_mean(base, 126)

def idec_071_autocorr_decay_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_071_autocorr_decay_zscore_126d
    ECONOMIC RATIONALE: Decay in serial correlation across timeframes.
    """
    base = close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) / close.pct_change(1).rolling(63).apply(lambda x: x.autocorr(1)).replace(0, 1e-9)
    return _zscore_rolling(base, 126)

def idec_072_autocorr_decay_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_072_autocorr_decay_rank_126d
    ECONOMIC RATIONALE: Decay in serial correlation across timeframes.
    """
    base = close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) / close.pct_change(1).rolling(63).apply(lambda x: x.autocorr(1)).replace(0, 1e-9)
    return _rank_pct(base, 126)

def idec_073_autocorr_decay_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_073_autocorr_decay_lvl_252d
    ECONOMIC RATIONALE: Decay in serial correlation across timeframes.
    """
    base = close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) / close.pct_change(1).rolling(63).apply(lambda x: x.autocorr(1)).replace(0, 1e-9)
    return _rolling_mean(base, 252)

def idec_074_autocorr_decay_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_074_autocorr_decay_zscore_252d
    ECONOMIC RATIONALE: Decay in serial correlation across timeframes.
    """
    base = close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) / close.pct_change(1).rolling(63).apply(lambda x: x.autocorr(1)).replace(0, 1e-9)
    return _zscore_rolling(base, 252)

def idec_075_autocorr_decay_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_075_autocorr_decay_rank_252d
    ECONOMIC RATIONALE: Decay in serial correlation across timeframes.
    """
    base = close.pct_change(1).rolling(21).apply(lambda x: x.autocorr(1)) / close.pct_change(1).rolling(63).apply(lambda x: x.autocorr(1)).replace(0, 1e-9)
    return _rank_pct(base, 252)

def idec_076_volatility_mean_reversion_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_076_volatility_mean_reversion_lvl_5d
    ECONOMIC RATIONALE: Rate at which short-term vol returns to the long-term mean.
    """
    base = close.rolling(21).std() / close.rolling(252).std()
    return _rolling_mean(base, 5)

def idec_077_volatility_mean_reversion_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_077_volatility_mean_reversion_zscore_5d
    ECONOMIC RATIONALE: Rate at which short-term vol returns to the long-term mean.
    """
    base = close.rolling(21).std() / close.rolling(252).std()
    return _zscore_rolling(base, 5)

def idec_078_volatility_mean_reversion_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_078_volatility_mean_reversion_rank_5d
    ECONOMIC RATIONALE: Rate at which short-term vol returns to the long-term mean.
    """
    base = close.rolling(21).std() / close.rolling(252).std()
    return _rank_pct(base, 5)

def idec_079_volatility_mean_reversion_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_079_volatility_mean_reversion_lvl_21d
    ECONOMIC RATIONALE: Rate at which short-term vol returns to the long-term mean.
    """
    base = close.rolling(21).std() / close.rolling(252).std()
    return _rolling_mean(base, 21)

def idec_080_volatility_mean_reversion_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_080_volatility_mean_reversion_zscore_21d
    ECONOMIC RATIONALE: Rate at which short-term vol returns to the long-term mean.
    """
    base = close.rolling(21).std() / close.rolling(252).std()
    return _zscore_rolling(base, 21)

def idec_081_volatility_mean_reversion_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_081_volatility_mean_reversion_rank_21d
    ECONOMIC RATIONALE: Rate at which short-term vol returns to the long-term mean.
    """
    base = close.rolling(21).std() / close.rolling(252).std()
    return _rank_pct(base, 21)

def idec_082_volatility_mean_reversion_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_082_volatility_mean_reversion_lvl_63d
    ECONOMIC RATIONALE: Rate at which short-term vol returns to the long-term mean.
    """
    base = close.rolling(21).std() / close.rolling(252).std()
    return _rolling_mean(base, 63)

def idec_083_volatility_mean_reversion_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_083_volatility_mean_reversion_zscore_63d
    ECONOMIC RATIONALE: Rate at which short-term vol returns to the long-term mean.
    """
    base = close.rolling(21).std() / close.rolling(252).std()
    return _zscore_rolling(base, 63)

def idec_084_volatility_mean_reversion_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_084_volatility_mean_reversion_rank_63d
    ECONOMIC RATIONALE: Rate at which short-term vol returns to the long-term mean.
    """
    base = close.rolling(21).std() / close.rolling(252).std()
    return _rank_pct(base, 63)

def idec_085_volatility_mean_reversion_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_085_volatility_mean_reversion_lvl_126d
    ECONOMIC RATIONALE: Rate at which short-term vol returns to the long-term mean.
    """
    base = close.rolling(21).std() / close.rolling(252).std()
    return _rolling_mean(base, 126)

def idec_086_volatility_mean_reversion_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_086_volatility_mean_reversion_zscore_126d
    ECONOMIC RATIONALE: Rate at which short-term vol returns to the long-term mean.
    """
    base = close.rolling(21).std() / close.rolling(252).std()
    return _zscore_rolling(base, 126)

def idec_087_volatility_mean_reversion_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_087_volatility_mean_reversion_rank_126d
    ECONOMIC RATIONALE: Rate at which short-term vol returns to the long-term mean.
    """
    base = close.rolling(21).std() / close.rolling(252).std()
    return _rank_pct(base, 126)

def idec_088_volatility_mean_reversion_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_088_volatility_mean_reversion_lvl_252d
    ECONOMIC RATIONALE: Rate at which short-term vol returns to the long-term mean.
    """
    base = close.rolling(21).std() / close.rolling(252).std()
    return _rolling_mean(base, 252)

def idec_089_volatility_mean_reversion_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_089_volatility_mean_reversion_zscore_252d
    ECONOMIC RATIONALE: Rate at which short-term vol returns to the long-term mean.
    """
    base = close.rolling(21).std() / close.rolling(252).std()
    return _zscore_rolling(base, 252)

def idec_090_volatility_mean_reversion_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_090_volatility_mean_reversion_rank_252d
    ECONOMIC RATIONALE: Rate at which short-term vol returns to the long-term mean.
    """
    base = close.rolling(21).std() / close.rolling(252).std()
    return _rank_pct(base, 252)

def idec_091_information_efficiency_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_091_information_efficiency_lvl_5d
    ECONOMIC RATIONALE: Rate of information incorporation into price.
    """
    base = abs(close.diff(21)) / (close.diff(1).abs().rolling(21).sum()).replace(0, 1e-9)
    return _rolling_mean(base, 5)

def idec_092_information_efficiency_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_092_information_efficiency_zscore_5d
    ECONOMIC RATIONALE: Rate of information incorporation into price.
    """
    base = abs(close.diff(21)) / (close.diff(1).abs().rolling(21).sum()).replace(0, 1e-9)
    return _zscore_rolling(base, 5)

def idec_093_information_efficiency_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_093_information_efficiency_rank_5d
    ECONOMIC RATIONALE: Rate of information incorporation into price.
    """
    base = abs(close.diff(21)) / (close.diff(1).abs().rolling(21).sum()).replace(0, 1e-9)
    return _rank_pct(base, 5)

def idec_094_information_efficiency_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_094_information_efficiency_lvl_21d
    ECONOMIC RATIONALE: Rate of information incorporation into price.
    """
    base = abs(close.diff(21)) / (close.diff(1).abs().rolling(21).sum()).replace(0, 1e-9)
    return _rolling_mean(base, 21)

def idec_095_information_efficiency_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_095_information_efficiency_zscore_21d
    ECONOMIC RATIONALE: Rate of information incorporation into price.
    """
    base = abs(close.diff(21)) / (close.diff(1).abs().rolling(21).sum()).replace(0, 1e-9)
    return _zscore_rolling(base, 21)

def idec_096_information_efficiency_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_096_information_efficiency_rank_21d
    ECONOMIC RATIONALE: Rate of information incorporation into price.
    """
    base = abs(close.diff(21)) / (close.diff(1).abs().rolling(21).sum()).replace(0, 1e-9)
    return _rank_pct(base, 21)

def idec_097_information_efficiency_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_097_information_efficiency_lvl_63d
    ECONOMIC RATIONALE: Rate of information incorporation into price.
    """
    base = abs(close.diff(21)) / (close.diff(1).abs().rolling(21).sum()).replace(0, 1e-9)
    return _rolling_mean(base, 63)

def idec_098_information_efficiency_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_098_information_efficiency_zscore_63d
    ECONOMIC RATIONALE: Rate of information incorporation into price.
    """
    base = abs(close.diff(21)) / (close.diff(1).abs().rolling(21).sum()).replace(0, 1e-9)
    return _zscore_rolling(base, 63)

def idec_099_information_efficiency_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_099_information_efficiency_rank_63d
    ECONOMIC RATIONALE: Rate of information incorporation into price.
    """
    base = abs(close.diff(21)) / (close.diff(1).abs().rolling(21).sum()).replace(0, 1e-9)
    return _rank_pct(base, 63)

def idec_100_information_efficiency_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_100_information_efficiency_lvl_126d
    ECONOMIC RATIONALE: Rate of information incorporation into price.
    """
    base = abs(close.diff(21)) / (close.diff(1).abs().rolling(21).sum()).replace(0, 1e-9)
    return _rolling_mean(base, 126)

def idec_101_information_efficiency_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_101_information_efficiency_zscore_126d
    ECONOMIC RATIONALE: Rate of information incorporation into price.
    """
    base = abs(close.diff(21)) / (close.diff(1).abs().rolling(21).sum()).replace(0, 1e-9)
    return _zscore_rolling(base, 126)

def idec_102_information_efficiency_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_102_information_efficiency_rank_126d
    ECONOMIC RATIONALE: Rate of information incorporation into price.
    """
    base = abs(close.diff(21)) / (close.diff(1).abs().rolling(21).sum()).replace(0, 1e-9)
    return _rank_pct(base, 126)

def idec_103_information_efficiency_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_103_information_efficiency_lvl_252d
    ECONOMIC RATIONALE: Rate of information incorporation into price.
    """
    base = abs(close.diff(21)) / (close.diff(1).abs().rolling(21).sum()).replace(0, 1e-9)
    return _rolling_mean(base, 252)

def idec_104_information_efficiency_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_104_information_efficiency_zscore_252d
    ECONOMIC RATIONALE: Rate of information incorporation into price.
    """
    base = abs(close.diff(21)) / (close.diff(1).abs().rolling(21).sum()).replace(0, 1e-9)
    return _zscore_rolling(base, 252)

def idec_105_information_efficiency_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_105_information_efficiency_rank_252d
    ECONOMIC RATIONALE: Rate of information incorporation into price.
    """
    base = abs(close.diff(21)) / (close.diff(1).abs().rolling(21).sum()).replace(0, 1e-9)
    return _rank_pct(base, 252)

def idec_106_signal_noise_decay_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_106_signal_noise_decay_lvl_5d
    ECONOMIC RATIONALE: Decay of signal strength relative to noise.
    """
    base = close.rolling(21).mean().diff(5).abs() / close.rolling(21).std().replace(0, 1e-9)
    return _rolling_mean(base, 5)

def idec_107_signal_noise_decay_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_107_signal_noise_decay_zscore_5d
    ECONOMIC RATIONALE: Decay of signal strength relative to noise.
    """
    base = close.rolling(21).mean().diff(5).abs() / close.rolling(21).std().replace(0, 1e-9)
    return _zscore_rolling(base, 5)

def idec_108_signal_noise_decay_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_108_signal_noise_decay_rank_5d
    ECONOMIC RATIONALE: Decay of signal strength relative to noise.
    """
    base = close.rolling(21).mean().diff(5).abs() / close.rolling(21).std().replace(0, 1e-9)
    return _rank_pct(base, 5)

def idec_109_signal_noise_decay_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_109_signal_noise_decay_lvl_21d
    ECONOMIC RATIONALE: Decay of signal strength relative to noise.
    """
    base = close.rolling(21).mean().diff(5).abs() / close.rolling(21).std().replace(0, 1e-9)
    return _rolling_mean(base, 21)

def idec_110_signal_noise_decay_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_110_signal_noise_decay_zscore_21d
    ECONOMIC RATIONALE: Decay of signal strength relative to noise.
    """
    base = close.rolling(21).mean().diff(5).abs() / close.rolling(21).std().replace(0, 1e-9)
    return _zscore_rolling(base, 21)

def idec_111_signal_noise_decay_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_111_signal_noise_decay_rank_21d
    ECONOMIC RATIONALE: Decay of signal strength relative to noise.
    """
    base = close.rolling(21).mean().diff(5).abs() / close.rolling(21).std().replace(0, 1e-9)
    return _rank_pct(base, 21)

def idec_112_signal_noise_decay_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_112_signal_noise_decay_lvl_63d
    ECONOMIC RATIONALE: Decay of signal strength relative to noise.
    """
    base = close.rolling(21).mean().diff(5).abs() / close.rolling(21).std().replace(0, 1e-9)
    return _rolling_mean(base, 63)

def idec_113_signal_noise_decay_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_113_signal_noise_decay_zscore_63d
    ECONOMIC RATIONALE: Decay of signal strength relative to noise.
    """
    base = close.rolling(21).mean().diff(5).abs() / close.rolling(21).std().replace(0, 1e-9)
    return _zscore_rolling(base, 63)

def idec_114_signal_noise_decay_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_114_signal_noise_decay_rank_63d
    ECONOMIC RATIONALE: Decay of signal strength relative to noise.
    """
    base = close.rolling(21).mean().diff(5).abs() / close.rolling(21).std().replace(0, 1e-9)
    return _rank_pct(base, 63)

def idec_115_signal_noise_decay_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_115_signal_noise_decay_lvl_126d
    ECONOMIC RATIONALE: Decay of signal strength relative to noise.
    """
    base = close.rolling(21).mean().diff(5).abs() / close.rolling(21).std().replace(0, 1e-9)
    return _rolling_mean(base, 126)

def idec_116_signal_noise_decay_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_116_signal_noise_decay_zscore_126d
    ECONOMIC RATIONALE: Decay of signal strength relative to noise.
    """
    base = close.rolling(21).mean().diff(5).abs() / close.rolling(21).std().replace(0, 1e-9)
    return _zscore_rolling(base, 126)

def idec_117_signal_noise_decay_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_117_signal_noise_decay_rank_126d
    ECONOMIC RATIONALE: Decay of signal strength relative to noise.
    """
    base = close.rolling(21).mean().diff(5).abs() / close.rolling(21).std().replace(0, 1e-9)
    return _rank_pct(base, 126)

def idec_118_signal_noise_decay_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_118_signal_noise_decay_lvl_252d
    ECONOMIC RATIONALE: Decay of signal strength relative to noise.
    """
    base = close.rolling(21).mean().diff(5).abs() / close.rolling(21).std().replace(0, 1e-9)
    return _rolling_mean(base, 252)

def idec_119_signal_noise_decay_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_119_signal_noise_decay_zscore_252d
    ECONOMIC RATIONALE: Decay of signal strength relative to noise.
    """
    base = close.rolling(21).mean().diff(5).abs() / close.rolling(21).std().replace(0, 1e-9)
    return _zscore_rolling(base, 252)

def idec_120_signal_noise_decay_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    idec_120_signal_noise_decay_rank_252d
    ECONOMIC RATIONALE: Decay of signal strength relative to noise.
    """
    base = close.rolling(21).mean().diff(5).abs() / close.rolling(21).std().replace(0, 1e-9)
    return _rank_pct(base, 252)

# ── Registry ──────────────────────────────────────────────────────────────────
V120_REGISTRY_1 = {
    "idec_001_price_impact_decay_lvl_5d": {"inputs": ["close", "volume"], "func": idec_001_price_impact_decay_lvl_5d},
    "idec_002_price_impact_decay_zscore_5d": {"inputs": ["close", "volume"], "func": idec_002_price_impact_decay_zscore_5d},
    "idec_003_price_impact_decay_rank_5d": {"inputs": ["close", "volume"], "func": idec_003_price_impact_decay_rank_5d},
    "idec_004_price_impact_decay_lvl_21d": {"inputs": ["close", "volume"], "func": idec_004_price_impact_decay_lvl_21d},
    "idec_005_price_impact_decay_zscore_21d": {"inputs": ["close", "volume"], "func": idec_005_price_impact_decay_zscore_21d},
    "idec_006_price_impact_decay_rank_21d": {"inputs": ["close", "volume"], "func": idec_006_price_impact_decay_rank_21d},
    "idec_007_price_impact_decay_lvl_63d": {"inputs": ["close", "volume"], "func": idec_007_price_impact_decay_lvl_63d},
    "idec_008_price_impact_decay_zscore_63d": {"inputs": ["close", "volume"], "func": idec_008_price_impact_decay_zscore_63d},
    "idec_009_price_impact_decay_rank_63d": {"inputs": ["close", "volume"], "func": idec_009_price_impact_decay_rank_63d},
    "idec_010_price_impact_decay_lvl_126d": {"inputs": ["close", "volume"], "func": idec_010_price_impact_decay_lvl_126d},
    "idec_011_price_impact_decay_zscore_126d": {"inputs": ["close", "volume"], "func": idec_011_price_impact_decay_zscore_126d},
    "idec_012_price_impact_decay_rank_126d": {"inputs": ["close", "volume"], "func": idec_012_price_impact_decay_rank_126d},
    "idec_013_price_impact_decay_lvl_252d": {"inputs": ["close", "volume"], "func": idec_013_price_impact_decay_lvl_252d},
    "idec_014_price_impact_decay_zscore_252d": {"inputs": ["close", "volume"], "func": idec_014_price_impact_decay_zscore_252d},
    "idec_015_price_impact_decay_rank_252d": {"inputs": ["close", "volume"], "func": idec_015_price_impact_decay_rank_252d},
    "idec_016_volume_impact_decay_lvl_5d": {"inputs": ["close", "volume"], "func": idec_016_volume_impact_decay_lvl_5d},
    "idec_017_volume_impact_decay_zscore_5d": {"inputs": ["close", "volume"], "func": idec_017_volume_impact_decay_zscore_5d},
    "idec_018_volume_impact_decay_rank_5d": {"inputs": ["close", "volume"], "func": idec_018_volume_impact_decay_rank_5d},
    "idec_019_volume_impact_decay_lvl_21d": {"inputs": ["close", "volume"], "func": idec_019_volume_impact_decay_lvl_21d},
    "idec_020_volume_impact_decay_zscore_21d": {"inputs": ["close", "volume"], "func": idec_020_volume_impact_decay_zscore_21d},
    "idec_021_volume_impact_decay_rank_21d": {"inputs": ["close", "volume"], "func": idec_021_volume_impact_decay_rank_21d},
    "idec_022_volume_impact_decay_lvl_63d": {"inputs": ["close", "volume"], "func": idec_022_volume_impact_decay_lvl_63d},
    "idec_023_volume_impact_decay_zscore_63d": {"inputs": ["close", "volume"], "func": idec_023_volume_impact_decay_zscore_63d},
    "idec_024_volume_impact_decay_rank_63d": {"inputs": ["close", "volume"], "func": idec_024_volume_impact_decay_rank_63d},
    "idec_025_volume_impact_decay_lvl_126d": {"inputs": ["close", "volume"], "func": idec_025_volume_impact_decay_lvl_126d},
    "idec_026_volume_impact_decay_zscore_126d": {"inputs": ["close", "volume"], "func": idec_026_volume_impact_decay_zscore_126d},
    "idec_027_volume_impact_decay_rank_126d": {"inputs": ["close", "volume"], "func": idec_027_volume_impact_decay_rank_126d},
    "idec_028_volume_impact_decay_lvl_252d": {"inputs": ["close", "volume"], "func": idec_028_volume_impact_decay_lvl_252d},
    "idec_029_volume_impact_decay_zscore_252d": {"inputs": ["close", "volume"], "func": idec_029_volume_impact_decay_zscore_252d},
    "idec_030_volume_impact_decay_rank_252d": {"inputs": ["close", "volume"], "func": idec_030_volume_impact_decay_rank_252d},
    "idec_031_information_horizon_lvl_5d": {"inputs": ["close", "volume"], "func": idec_031_information_horizon_lvl_5d},
    "idec_032_information_horizon_zscore_5d": {"inputs": ["close", "volume"], "func": idec_032_information_horizon_zscore_5d},
    "idec_033_information_horizon_rank_5d": {"inputs": ["close", "volume"], "func": idec_033_information_horizon_rank_5d},
    "idec_034_information_horizon_lvl_21d": {"inputs": ["close", "volume"], "func": idec_034_information_horizon_lvl_21d},
    "idec_035_information_horizon_zscore_21d": {"inputs": ["close", "volume"], "func": idec_035_information_horizon_zscore_21d},
    "idec_036_information_horizon_rank_21d": {"inputs": ["close", "volume"], "func": idec_036_information_horizon_rank_21d},
    "idec_037_information_horizon_lvl_63d": {"inputs": ["close", "volume"], "func": idec_037_information_horizon_lvl_63d},
    "idec_038_information_horizon_zscore_63d": {"inputs": ["close", "volume"], "func": idec_038_information_horizon_zscore_63d},
    "idec_039_information_horizon_rank_63d": {"inputs": ["close", "volume"], "func": idec_039_information_horizon_rank_63d},
    "idec_040_information_horizon_lvl_126d": {"inputs": ["close", "volume"], "func": idec_040_information_horizon_lvl_126d},
    "idec_041_information_horizon_zscore_126d": {"inputs": ["close", "volume"], "func": idec_041_information_horizon_zscore_126d},
    "idec_042_information_horizon_rank_126d": {"inputs": ["close", "volume"], "func": idec_042_information_horizon_rank_126d},
    "idec_043_information_horizon_lvl_252d": {"inputs": ["close", "volume"], "func": idec_043_information_horizon_lvl_252d},
    "idec_044_information_horizon_zscore_252d": {"inputs": ["close", "volume"], "func": idec_044_information_horizon_zscore_252d},
    "idec_045_information_horizon_rank_252d": {"inputs": ["close", "volume"], "func": idec_045_information_horizon_rank_252d},
    "idec_046_news_response_decay_lvl_5d": {"inputs": ["close", "volume"], "func": idec_046_news_response_decay_lvl_5d},
    "idec_047_news_response_decay_zscore_5d": {"inputs": ["close", "volume"], "func": idec_047_news_response_decay_zscore_5d},
    "idec_048_news_response_decay_rank_5d": {"inputs": ["close", "volume"], "func": idec_048_news_response_decay_rank_5d},
    "idec_049_news_response_decay_lvl_21d": {"inputs": ["close", "volume"], "func": idec_049_news_response_decay_lvl_21d},
    "idec_050_news_response_decay_zscore_21d": {"inputs": ["close", "volume"], "func": idec_050_news_response_decay_zscore_21d},
    "idec_051_news_response_decay_rank_21d": {"inputs": ["close", "volume"], "func": idec_051_news_response_decay_rank_21d},
    "idec_052_news_response_decay_lvl_63d": {"inputs": ["close", "volume"], "func": idec_052_news_response_decay_lvl_63d},
    "idec_053_news_response_decay_zscore_63d": {"inputs": ["close", "volume"], "func": idec_053_news_response_decay_zscore_63d},
    "idec_054_news_response_decay_rank_63d": {"inputs": ["close", "volume"], "func": idec_054_news_response_decay_rank_63d},
    "idec_055_news_response_decay_lvl_126d": {"inputs": ["close", "volume"], "func": idec_055_news_response_decay_lvl_126d},
    "idec_056_news_response_decay_zscore_126d": {"inputs": ["close", "volume"], "func": idec_056_news_response_decay_zscore_126d},
    "idec_057_news_response_decay_rank_126d": {"inputs": ["close", "volume"], "func": idec_057_news_response_decay_rank_126d},
    "idec_058_news_response_decay_lvl_252d": {"inputs": ["close", "volume"], "func": idec_058_news_response_decay_lvl_252d},
    "idec_059_news_response_decay_zscore_252d": {"inputs": ["close", "volume"], "func": idec_059_news_response_decay_zscore_252d},
    "idec_060_news_response_decay_rank_252d": {"inputs": ["close", "volume"], "func": idec_060_news_response_decay_rank_252d},
    "idec_061_autocorr_decay_lvl_5d": {"inputs": ["close", "volume"], "func": idec_061_autocorr_decay_lvl_5d},
    "idec_062_autocorr_decay_zscore_5d": {"inputs": ["close", "volume"], "func": idec_062_autocorr_decay_zscore_5d},
    "idec_063_autocorr_decay_rank_5d": {"inputs": ["close", "volume"], "func": idec_063_autocorr_decay_rank_5d},
    "idec_064_autocorr_decay_lvl_21d": {"inputs": ["close", "volume"], "func": idec_064_autocorr_decay_lvl_21d},
    "idec_065_autocorr_decay_zscore_21d": {"inputs": ["close", "volume"], "func": idec_065_autocorr_decay_zscore_21d},
    "idec_066_autocorr_decay_rank_21d": {"inputs": ["close", "volume"], "func": idec_066_autocorr_decay_rank_21d},
    "idec_067_autocorr_decay_lvl_63d": {"inputs": ["close", "volume"], "func": idec_067_autocorr_decay_lvl_63d},
    "idec_068_autocorr_decay_zscore_63d": {"inputs": ["close", "volume"], "func": idec_068_autocorr_decay_zscore_63d},
    "idec_069_autocorr_decay_rank_63d": {"inputs": ["close", "volume"], "func": idec_069_autocorr_decay_rank_63d},
    "idec_070_autocorr_decay_lvl_126d": {"inputs": ["close", "volume"], "func": idec_070_autocorr_decay_lvl_126d},
    "idec_071_autocorr_decay_zscore_126d": {"inputs": ["close", "volume"], "func": idec_071_autocorr_decay_zscore_126d},
    "idec_072_autocorr_decay_rank_126d": {"inputs": ["close", "volume"], "func": idec_072_autocorr_decay_rank_126d},
    "idec_073_autocorr_decay_lvl_252d": {"inputs": ["close", "volume"], "func": idec_073_autocorr_decay_lvl_252d},
    "idec_074_autocorr_decay_zscore_252d": {"inputs": ["close", "volume"], "func": idec_074_autocorr_decay_zscore_252d},
    "idec_075_autocorr_decay_rank_252d": {"inputs": ["close", "volume"], "func": idec_075_autocorr_decay_rank_252d},
    "idec_076_volatility_mean_reversion_lvl_5d": {"inputs": ["close", "volume"], "func": idec_076_volatility_mean_reversion_lvl_5d},
    "idec_077_volatility_mean_reversion_zscore_5d": {"inputs": ["close", "volume"], "func": idec_077_volatility_mean_reversion_zscore_5d},
    "idec_078_volatility_mean_reversion_rank_5d": {"inputs": ["close", "volume"], "func": idec_078_volatility_mean_reversion_rank_5d},
    "idec_079_volatility_mean_reversion_lvl_21d": {"inputs": ["close", "volume"], "func": idec_079_volatility_mean_reversion_lvl_21d},
    "idec_080_volatility_mean_reversion_zscore_21d": {"inputs": ["close", "volume"], "func": idec_080_volatility_mean_reversion_zscore_21d},
    "idec_081_volatility_mean_reversion_rank_21d": {"inputs": ["close", "volume"], "func": idec_081_volatility_mean_reversion_rank_21d},
    "idec_082_volatility_mean_reversion_lvl_63d": {"inputs": ["close", "volume"], "func": idec_082_volatility_mean_reversion_lvl_63d},
    "idec_083_volatility_mean_reversion_zscore_63d": {"inputs": ["close", "volume"], "func": idec_083_volatility_mean_reversion_zscore_63d},
    "idec_084_volatility_mean_reversion_rank_63d": {"inputs": ["close", "volume"], "func": idec_084_volatility_mean_reversion_rank_63d},
    "idec_085_volatility_mean_reversion_lvl_126d": {"inputs": ["close", "volume"], "func": idec_085_volatility_mean_reversion_lvl_126d},
    "idec_086_volatility_mean_reversion_zscore_126d": {"inputs": ["close", "volume"], "func": idec_086_volatility_mean_reversion_zscore_126d},
    "idec_087_volatility_mean_reversion_rank_126d": {"inputs": ["close", "volume"], "func": idec_087_volatility_mean_reversion_rank_126d},
    "idec_088_volatility_mean_reversion_lvl_252d": {"inputs": ["close", "volume"], "func": idec_088_volatility_mean_reversion_lvl_252d},
    "idec_089_volatility_mean_reversion_zscore_252d": {"inputs": ["close", "volume"], "func": idec_089_volatility_mean_reversion_zscore_252d},
    "idec_090_volatility_mean_reversion_rank_252d": {"inputs": ["close", "volume"], "func": idec_090_volatility_mean_reversion_rank_252d},
    "idec_091_information_efficiency_lvl_5d": {"inputs": ["close", "volume"], "func": idec_091_information_efficiency_lvl_5d},
    "idec_092_information_efficiency_zscore_5d": {"inputs": ["close", "volume"], "func": idec_092_information_efficiency_zscore_5d},
    "idec_093_information_efficiency_rank_5d": {"inputs": ["close", "volume"], "func": idec_093_information_efficiency_rank_5d},
    "idec_094_information_efficiency_lvl_21d": {"inputs": ["close", "volume"], "func": idec_094_information_efficiency_lvl_21d},
    "idec_095_information_efficiency_zscore_21d": {"inputs": ["close", "volume"], "func": idec_095_information_efficiency_zscore_21d},
    "idec_096_information_efficiency_rank_21d": {"inputs": ["close", "volume"], "func": idec_096_information_efficiency_rank_21d},
    "idec_097_information_efficiency_lvl_63d": {"inputs": ["close", "volume"], "func": idec_097_information_efficiency_lvl_63d},
    "idec_098_information_efficiency_zscore_63d": {"inputs": ["close", "volume"], "func": idec_098_information_efficiency_zscore_63d},
    "idec_099_information_efficiency_rank_63d": {"inputs": ["close", "volume"], "func": idec_099_information_efficiency_rank_63d},
    "idec_100_information_efficiency_lvl_126d": {"inputs": ["close", "volume"], "func": idec_100_information_efficiency_lvl_126d},
    "idec_101_information_efficiency_zscore_126d": {"inputs": ["close", "volume"], "func": idec_101_information_efficiency_zscore_126d},
    "idec_102_information_efficiency_rank_126d": {"inputs": ["close", "volume"], "func": idec_102_information_efficiency_rank_126d},
    "idec_103_information_efficiency_lvl_252d": {"inputs": ["close", "volume"], "func": idec_103_information_efficiency_lvl_252d},
    "idec_104_information_efficiency_zscore_252d": {"inputs": ["close", "volume"], "func": idec_104_information_efficiency_zscore_252d},
    "idec_105_information_efficiency_rank_252d": {"inputs": ["close", "volume"], "func": idec_105_information_efficiency_rank_252d},
    "idec_106_signal_noise_decay_lvl_5d": {"inputs": ["close", "volume"], "func": idec_106_signal_noise_decay_lvl_5d},
    "idec_107_signal_noise_decay_zscore_5d": {"inputs": ["close", "volume"], "func": idec_107_signal_noise_decay_zscore_5d},
    "idec_108_signal_noise_decay_rank_5d": {"inputs": ["close", "volume"], "func": idec_108_signal_noise_decay_rank_5d},
    "idec_109_signal_noise_decay_lvl_21d": {"inputs": ["close", "volume"], "func": idec_109_signal_noise_decay_lvl_21d},
    "idec_110_signal_noise_decay_zscore_21d": {"inputs": ["close", "volume"], "func": idec_110_signal_noise_decay_zscore_21d},
    "idec_111_signal_noise_decay_rank_21d": {"inputs": ["close", "volume"], "func": idec_111_signal_noise_decay_rank_21d},
    "idec_112_signal_noise_decay_lvl_63d": {"inputs": ["close", "volume"], "func": idec_112_signal_noise_decay_lvl_63d},
    "idec_113_signal_noise_decay_zscore_63d": {"inputs": ["close", "volume"], "func": idec_113_signal_noise_decay_zscore_63d},
    "idec_114_signal_noise_decay_rank_63d": {"inputs": ["close", "volume"], "func": idec_114_signal_noise_decay_rank_63d},
    "idec_115_signal_noise_decay_lvl_126d": {"inputs": ["close", "volume"], "func": idec_115_signal_noise_decay_lvl_126d},
    "idec_116_signal_noise_decay_zscore_126d": {"inputs": ["close", "volume"], "func": idec_116_signal_noise_decay_zscore_126d},
    "idec_117_signal_noise_decay_rank_126d": {"inputs": ["close", "volume"], "func": idec_117_signal_noise_decay_rank_126d},
    "idec_118_signal_noise_decay_lvl_252d": {"inputs": ["close", "volume"], "func": idec_118_signal_noise_decay_lvl_252d},
    "idec_119_signal_noise_decay_zscore_252d": {"inputs": ["close", "volume"], "func": idec_119_signal_noise_decay_zscore_252d},
    "idec_120_signal_noise_decay_rank_252d": {"inputs": ["close", "volume"], "func": idec_120_signal_noise_decay_rank_252d},
}
