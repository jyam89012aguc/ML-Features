"""
103_103_multi_timeframe_oversold — Base Features 376-450
Domain: 103_multi_timeframe_oversold
Asset class: Equities
Target context: Capitulation
"""
import numpy as np
import pandas as pd

# ── Utility helpers ──────────────────────────────────────────────────────────
_EPS = 1e-9

def _safe_div(a: pd.Series, b: pd.Series) -> pd.Series:
    return a / b.replace(0, _EPS)

def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=1).mean()

def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=1).std().fillna(0)

def _zscore_rolling(s: pd.Series, w: int) -> pd.Series:
    m = _rolling_mean(s, w)
    sd = _rolling_std(s, w)
    return _safe_div((s - m), sd)

def _rank_pct(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=1).rank(pct=True)

def _rolling_skew(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=1).skew().fillna(0)

def _rolling_kurt(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=1).kurt().fillna(0)

# ── Feature functions ────────────────────────────────────────────────────────

def mtfo_376_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 103 multi timeframe oversold for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = _zscore_rolling(close, 105)
    return _safe_div(base, _rolling_std(base, 5))

def mtfo_377_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 103 multi timeframe oversold for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = _zscore_rolling(close, 105)
    return _safe_div(base, _rolling_std(base, 21))

def mtfo_378_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 103 multi timeframe oversold for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = _zscore_rolling(close, 105)
    return _safe_div(base, _rolling_std(base, 63))

def mtfo_379_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 103 multi timeframe oversold for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = _zscore_rolling(close, 105)
    return _safe_div(base, _rolling_std(base, 126))

def mtfo_380_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 103 multi timeframe oversold for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = _zscore_rolling(close, 105)
    return _safe_div(base, _rolling_std(base, 252))

def mtfo_381_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 103 multi timeframe oversold over 5d to stabilize variance and capture exponential shifts.
    """
    base = _zscore_rolling(close, 105)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def mtfo_382_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 103 multi timeframe oversold over 21d to stabilize variance and capture exponential shifts.
    """
    base = _zscore_rolling(close, 105)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def mtfo_383_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 103 multi timeframe oversold over 63d to stabilize variance and capture exponential shifts.
    """
    base = _zscore_rolling(close, 105)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def mtfo_384_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 103 multi timeframe oversold over 126d to stabilize variance and capture exponential shifts.
    """
    base = _zscore_rolling(close, 105)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def mtfo_385_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 103 multi timeframe oversold over 252d to stabilize variance and capture exponential shifts.
    """
    base = _zscore_rolling(close, 105)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def mtfo_386_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 103 multi timeframe oversold over a 5d horizon to identify extreme regimes.
    """
    base = _zscore_rolling(close, 115)
    return _rolling_mean(base, 5)

def mtfo_387_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 103 multi timeframe oversold over a 21d horizon to identify extreme regimes.
    """
    base = _zscore_rolling(close, 115)
    return _rolling_mean(base, 21)

def mtfo_388_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 103 multi timeframe oversold over a 63d horizon to identify extreme regimes.
    """
    base = _zscore_rolling(close, 115)
    return _rolling_mean(base, 63)

def mtfo_389_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 103 multi timeframe oversold over a 126d horizon to identify extreme regimes.
    """
    base = _zscore_rolling(close, 115)
    return _rolling_mean(base, 126)

def mtfo_390_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 103 multi timeframe oversold over a 252d horizon to identify extreme regimes.
    """
    base = _zscore_rolling(close, 115)
    return _rolling_mean(base, 252)

def mtfo_391_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 103 multi timeframe oversold by measuring deviations from the 5d mean.
    """
    base = _zscore_rolling(close, 115)
    return _zscore_rolling(base, 5)

def mtfo_392_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 103 multi timeframe oversold by measuring deviations from the 21d mean.
    """
    base = _zscore_rolling(close, 115)
    return _zscore_rolling(base, 21)

def mtfo_393_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 103 multi timeframe oversold by measuring deviations from the 63d mean.
    """
    base = _zscore_rolling(close, 115)
    return _zscore_rolling(base, 63)

def mtfo_394_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 103 multi timeframe oversold by measuring deviations from the 126d mean.
    """
    base = _zscore_rolling(close, 115)
    return _zscore_rolling(base, 126)

def mtfo_395_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 103 multi timeframe oversold by measuring deviations from the 252d mean.
    """
    base = _zscore_rolling(close, 115)
    return _zscore_rolling(base, 252)

def mtfo_396_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 103 multi timeframe oversold to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = _zscore_rolling(close, 115)
    return _rank_pct(base, 5)

def mtfo_397_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 103 multi timeframe oversold to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = _zscore_rolling(close, 115)
    return _rank_pct(base, 21)

def mtfo_398_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 103 multi timeframe oversold to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = _zscore_rolling(close, 115)
    return _rank_pct(base, 63)

def mtfo_399_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 103 multi timeframe oversold to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = _zscore_rolling(close, 115)
    return _rank_pct(base, 126)

def mtfo_400_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 103 multi timeframe oversold to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = _zscore_rolling(close, 115)
    return _rank_pct(base, 252)

def mtfo_401_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 103 multi timeframe oversold distribution over 5d to detect tail risk or exhaustion.
    """
    base = _zscore_rolling(close, 115)
    return _rolling_skew(base, 5)

def mtfo_402_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 103 multi timeframe oversold distribution over 21d to detect tail risk or exhaustion.
    """
    base = _zscore_rolling(close, 115)
    return _rolling_skew(base, 21)

def mtfo_403_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 103 multi timeframe oversold distribution over 63d to detect tail risk or exhaustion.
    """
    base = _zscore_rolling(close, 115)
    return _rolling_skew(base, 63)

def mtfo_404_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 103 multi timeframe oversold distribution over 126d to detect tail risk or exhaustion.
    """
    base = _zscore_rolling(close, 115)
    return _rolling_skew(base, 126)

def mtfo_405_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 103 multi timeframe oversold distribution over 252d to detect tail risk or exhaustion.
    """
    base = _zscore_rolling(close, 115)
    return _rolling_skew(base, 252)

def mtfo_406_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 103 multi timeframe oversold over 5d to capture explosive breakdown or reversal points.
    """
    base = _zscore_rolling(close, 115)
    return _rolling_kurt(base, 5)

def mtfo_407_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 103 multi timeframe oversold over 21d to capture explosive breakdown or reversal points.
    """
    base = _zscore_rolling(close, 115)
    return _rolling_kurt(base, 21)

def mtfo_408_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 103 multi timeframe oversold over 63d to capture explosive breakdown or reversal points.
    """
    base = _zscore_rolling(close, 115)
    return _rolling_kurt(base, 63)

def mtfo_409_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 103 multi timeframe oversold over 126d to capture explosive breakdown or reversal points.
    """
    base = _zscore_rolling(close, 115)
    return _rolling_kurt(base, 126)

def mtfo_410_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 103 multi timeframe oversold over 252d to capture explosive breakdown or reversal points.
    """
    base = _zscore_rolling(close, 115)
    return _rolling_kurt(base, 252)

def mtfo_411_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 103 multi timeframe oversold for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = _zscore_rolling(close, 115)
    return _safe_div(base, _rolling_std(base, 5))

def mtfo_412_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 103 multi timeframe oversold for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = _zscore_rolling(close, 115)
    return _safe_div(base, _rolling_std(base, 21))

def mtfo_413_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 103 multi timeframe oversold for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = _zscore_rolling(close, 115)
    return _safe_div(base, _rolling_std(base, 63))

def mtfo_414_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 103 multi timeframe oversold for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = _zscore_rolling(close, 115)
    return _safe_div(base, _rolling_std(base, 126))

def mtfo_415_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 103 multi timeframe oversold for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = _zscore_rolling(close, 115)
    return _safe_div(base, _rolling_std(base, 252))

def mtfo_416_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 103 multi timeframe oversold over 5d to stabilize variance and capture exponential shifts.
    """
    base = _zscore_rolling(close, 115)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def mtfo_417_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 103 multi timeframe oversold over 21d to stabilize variance and capture exponential shifts.
    """
    base = _zscore_rolling(close, 115)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def mtfo_418_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 103 multi timeframe oversold over 63d to stabilize variance and capture exponential shifts.
    """
    base = _zscore_rolling(close, 115)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def mtfo_419_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 103 multi timeframe oversold over 126d to stabilize variance and capture exponential shifts.
    """
    base = _zscore_rolling(close, 115)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def mtfo_420_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 103 multi timeframe oversold over 252d to stabilize variance and capture exponential shifts.
    """
    base = _zscore_rolling(close, 115)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def mtfo_421_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 103 multi timeframe oversold over a 5d horizon to identify extreme regimes.
    """
    base = _zscore_rolling(close, 125)
    return _rolling_mean(base, 5)

def mtfo_422_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 103 multi timeframe oversold over a 21d horizon to identify extreme regimes.
    """
    base = _zscore_rolling(close, 125)
    return _rolling_mean(base, 21)

def mtfo_423_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 103 multi timeframe oversold over a 63d horizon to identify extreme regimes.
    """
    base = _zscore_rolling(close, 125)
    return _rolling_mean(base, 63)

def mtfo_424_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 103 multi timeframe oversold over a 126d horizon to identify extreme regimes.
    """
    base = _zscore_rolling(close, 125)
    return _rolling_mean(base, 126)

def mtfo_425_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 103 multi timeframe oversold over a 252d horizon to identify extreme regimes.
    """
    base = _zscore_rolling(close, 125)
    return _rolling_mean(base, 252)

def mtfo_426_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 103 multi timeframe oversold by measuring deviations from the 5d mean.
    """
    base = _zscore_rolling(close, 125)
    return _zscore_rolling(base, 5)

def mtfo_427_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 103 multi timeframe oversold by measuring deviations from the 21d mean.
    """
    base = _zscore_rolling(close, 125)
    return _zscore_rolling(base, 21)

def mtfo_428_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 103 multi timeframe oversold by measuring deviations from the 63d mean.
    """
    base = _zscore_rolling(close, 125)
    return _zscore_rolling(base, 63)

def mtfo_429_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 103 multi timeframe oversold by measuring deviations from the 126d mean.
    """
    base = _zscore_rolling(close, 125)
    return _zscore_rolling(base, 126)

def mtfo_430_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 103 multi timeframe oversold by measuring deviations from the 252d mean.
    """
    base = _zscore_rolling(close, 125)
    return _zscore_rolling(base, 252)

def mtfo_431_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 103 multi timeframe oversold to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = _zscore_rolling(close, 125)
    return _rank_pct(base, 5)

def mtfo_432_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 103 multi timeframe oversold to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = _zscore_rolling(close, 125)
    return _rank_pct(base, 21)

def mtfo_433_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 103 multi timeframe oversold to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = _zscore_rolling(close, 125)
    return _rank_pct(base, 63)

def mtfo_434_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 103 multi timeframe oversold to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = _zscore_rolling(close, 125)
    return _rank_pct(base, 126)

def mtfo_435_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 103 multi timeframe oversold to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = _zscore_rolling(close, 125)
    return _rank_pct(base, 252)

def mtfo_436_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 103 multi timeframe oversold distribution over 5d to detect tail risk or exhaustion.
    """
    base = _zscore_rolling(close, 125)
    return _rolling_skew(base, 5)

def mtfo_437_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 103 multi timeframe oversold distribution over 21d to detect tail risk or exhaustion.
    """
    base = _zscore_rolling(close, 125)
    return _rolling_skew(base, 21)

def mtfo_438_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 103 multi timeframe oversold distribution over 63d to detect tail risk or exhaustion.
    """
    base = _zscore_rolling(close, 125)
    return _rolling_skew(base, 63)

def mtfo_439_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 103 multi timeframe oversold distribution over 126d to detect tail risk or exhaustion.
    """
    base = _zscore_rolling(close, 125)
    return _rolling_skew(base, 126)

def mtfo_440_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 103 multi timeframe oversold distribution over 252d to detect tail risk or exhaustion.
    """
    base = _zscore_rolling(close, 125)
    return _rolling_skew(base, 252)

def mtfo_441_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 103 multi timeframe oversold over 5d to capture explosive breakdown or reversal points.
    """
    base = _zscore_rolling(close, 125)
    return _rolling_kurt(base, 5)

def mtfo_442_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 103 multi timeframe oversold over 21d to capture explosive breakdown or reversal points.
    """
    base = _zscore_rolling(close, 125)
    return _rolling_kurt(base, 21)

def mtfo_443_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 103 multi timeframe oversold over 63d to capture explosive breakdown or reversal points.
    """
    base = _zscore_rolling(close, 125)
    return _rolling_kurt(base, 63)

def mtfo_444_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 103 multi timeframe oversold over 126d to capture explosive breakdown or reversal points.
    """
    base = _zscore_rolling(close, 125)
    return _rolling_kurt(base, 126)

def mtfo_445_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 103 multi timeframe oversold over 252d to capture explosive breakdown or reversal points.
    """
    base = _zscore_rolling(close, 125)
    return _rolling_kurt(base, 252)

def mtfo_446_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 103 multi timeframe oversold for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = _zscore_rolling(close, 125)
    return _safe_div(base, _rolling_std(base, 5))

def mtfo_447_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 103 multi timeframe oversold for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = _zscore_rolling(close, 125)
    return _safe_div(base, _rolling_std(base, 21))

def mtfo_448_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 103 multi timeframe oversold for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = _zscore_rolling(close, 125)
    return _safe_div(base, _rolling_std(base, 63))

def mtfo_449_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 103 multi timeframe oversold for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = _zscore_rolling(close, 125)
    return _safe_div(base, _rolling_std(base, 126))

def mtfo_450_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 103 multi timeframe oversold for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = _zscore_rolling(close, 125)
    return _safe_div(base, _rolling_std(base, 252))
