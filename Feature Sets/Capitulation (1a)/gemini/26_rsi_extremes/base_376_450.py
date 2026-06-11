"""
26_26_rsi_extremes — Base Features 376-450
Domain: 26_rsi_extremes
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

def rsie_376_voladj_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 26 rsi extremes for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(11).rolling(55).mean())
    return _safe_div(base, _rolling_std(base, 5))

def rsie_377_voladj_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 26 rsi extremes for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(11).rolling(55).mean())
    return _safe_div(base, _rolling_std(base, 21))

def rsie_378_voladj_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 26 rsi extremes for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(11).rolling(55).mean())
    return _safe_div(base, _rolling_std(base, 63))

def rsie_379_voladj_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 26 rsi extremes for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(11).rolling(55).mean())
    return _safe_div(base, _rolling_std(base, 126))

def rsie_380_voladj_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 26 rsi extremes for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(11).rolling(55).mean())
    return _safe_div(base, _rolling_std(base, 252))

def rsie_381_lognorm_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 26 rsi extremes over 5d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(11).rolling(55).mean())
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def rsie_382_lognorm_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 26 rsi extremes over 21d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(11).rolling(55).mean())
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def rsie_383_lognorm_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 26 rsi extremes over 63d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(11).rolling(55).mean())
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def rsie_384_lognorm_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 26 rsi extremes over 126d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(11).rolling(55).mean())
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def rsie_385_lognorm_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 26 rsi extremes over 252d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(11).rolling(55).mean())
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def rsie_386_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 26 rsi extremes over a 5d horizon to identify extreme regimes.
    """
    base = (close.pct_change(12).rolling(60).mean())
    return _rolling_mean(base, 5)

def rsie_387_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 26 rsi extremes over a 21d horizon to identify extreme regimes.
    """
    base = (close.pct_change(12).rolling(60).mean())
    return _rolling_mean(base, 21)

def rsie_388_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 26 rsi extremes over a 63d horizon to identify extreme regimes.
    """
    base = (close.pct_change(12).rolling(60).mean())
    return _rolling_mean(base, 63)

def rsie_389_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 26 rsi extremes over a 126d horizon to identify extreme regimes.
    """
    base = (close.pct_change(12).rolling(60).mean())
    return _rolling_mean(base, 126)

def rsie_390_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 26 rsi extremes over a 252d horizon to identify extreme regimes.
    """
    base = (close.pct_change(12).rolling(60).mean())
    return _rolling_mean(base, 252)

def rsie_391_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 26 rsi extremes by measuring deviations from the 5d mean.
    """
    base = (close.pct_change(12).rolling(60).mean())
    return _zscore_rolling(base, 5)

def rsie_392_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 26 rsi extremes by measuring deviations from the 21d mean.
    """
    base = (close.pct_change(12).rolling(60).mean())
    return _zscore_rolling(base, 21)

def rsie_393_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 26 rsi extremes by measuring deviations from the 63d mean.
    """
    base = (close.pct_change(12).rolling(60).mean())
    return _zscore_rolling(base, 63)

def rsie_394_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 26 rsi extremes by measuring deviations from the 126d mean.
    """
    base = (close.pct_change(12).rolling(60).mean())
    return _zscore_rolling(base, 126)

def rsie_395_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 26 rsi extremes by measuring deviations from the 252d mean.
    """
    base = (close.pct_change(12).rolling(60).mean())
    return _zscore_rolling(base, 252)

def rsie_396_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 26 rsi extremes to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = (close.pct_change(12).rolling(60).mean())
    return _rank_pct(base, 5)

def rsie_397_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 26 rsi extremes to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = (close.pct_change(12).rolling(60).mean())
    return _rank_pct(base, 21)

def rsie_398_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 26 rsi extremes to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = (close.pct_change(12).rolling(60).mean())
    return _rank_pct(base, 63)

def rsie_399_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 26 rsi extremes to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = (close.pct_change(12).rolling(60).mean())
    return _rank_pct(base, 126)

def rsie_400_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 26 rsi extremes to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = (close.pct_change(12).rolling(60).mean())
    return _rank_pct(base, 252)

def rsie_401_skew_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 26 rsi extremes distribution over 5d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(12).rolling(60).mean())
    return _rolling_skew(base, 5)

def rsie_402_skew_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 26 rsi extremes distribution over 21d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(12).rolling(60).mean())
    return _rolling_skew(base, 21)

def rsie_403_skew_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 26 rsi extremes distribution over 63d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(12).rolling(60).mean())
    return _rolling_skew(base, 63)

def rsie_404_skew_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 26 rsi extremes distribution over 126d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(12).rolling(60).mean())
    return _rolling_skew(base, 126)

def rsie_405_skew_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 26 rsi extremes distribution over 252d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(12).rolling(60).mean())
    return _rolling_skew(base, 252)

def rsie_406_kurt_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 26 rsi extremes over 5d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(12).rolling(60).mean())
    return _rolling_kurt(base, 5)

def rsie_407_kurt_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 26 rsi extremes over 21d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(12).rolling(60).mean())
    return _rolling_kurt(base, 21)

def rsie_408_kurt_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 26 rsi extremes over 63d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(12).rolling(60).mean())
    return _rolling_kurt(base, 63)

def rsie_409_kurt_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 26 rsi extremes over 126d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(12).rolling(60).mean())
    return _rolling_kurt(base, 126)

def rsie_410_kurt_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 26 rsi extremes over 252d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(12).rolling(60).mean())
    return _rolling_kurt(base, 252)

def rsie_411_voladj_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 26 rsi extremes for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(12).rolling(60).mean())
    return _safe_div(base, _rolling_std(base, 5))

def rsie_412_voladj_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 26 rsi extremes for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(12).rolling(60).mean())
    return _safe_div(base, _rolling_std(base, 21))

def rsie_413_voladj_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 26 rsi extremes for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(12).rolling(60).mean())
    return _safe_div(base, _rolling_std(base, 63))

def rsie_414_voladj_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 26 rsi extremes for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(12).rolling(60).mean())
    return _safe_div(base, _rolling_std(base, 126))

def rsie_415_voladj_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 26 rsi extremes for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(12).rolling(60).mean())
    return _safe_div(base, _rolling_std(base, 252))

def rsie_416_lognorm_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 26 rsi extremes over 5d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(12).rolling(60).mean())
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def rsie_417_lognorm_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 26 rsi extremes over 21d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(12).rolling(60).mean())
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def rsie_418_lognorm_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 26 rsi extremes over 63d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(12).rolling(60).mean())
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def rsie_419_lognorm_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 26 rsi extremes over 126d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(12).rolling(60).mean())
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def rsie_420_lognorm_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 26 rsi extremes over 252d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(12).rolling(60).mean())
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def rsie_421_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 26 rsi extremes over a 5d horizon to identify extreme regimes.
    """
    base = (close.pct_change(13).rolling(65).mean())
    return _rolling_mean(base, 5)

def rsie_422_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 26 rsi extremes over a 21d horizon to identify extreme regimes.
    """
    base = (close.pct_change(13).rolling(65).mean())
    return _rolling_mean(base, 21)

def rsie_423_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 26 rsi extremes over a 63d horizon to identify extreme regimes.
    """
    base = (close.pct_change(13).rolling(65).mean())
    return _rolling_mean(base, 63)

def rsie_424_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 26 rsi extremes over a 126d horizon to identify extreme regimes.
    """
    base = (close.pct_change(13).rolling(65).mean())
    return _rolling_mean(base, 126)

def rsie_425_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 26 rsi extremes over a 252d horizon to identify extreme regimes.
    """
    base = (close.pct_change(13).rolling(65).mean())
    return _rolling_mean(base, 252)

def rsie_426_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 26 rsi extremes by measuring deviations from the 5d mean.
    """
    base = (close.pct_change(13).rolling(65).mean())
    return _zscore_rolling(base, 5)

def rsie_427_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 26 rsi extremes by measuring deviations from the 21d mean.
    """
    base = (close.pct_change(13).rolling(65).mean())
    return _zscore_rolling(base, 21)

def rsie_428_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 26 rsi extremes by measuring deviations from the 63d mean.
    """
    base = (close.pct_change(13).rolling(65).mean())
    return _zscore_rolling(base, 63)

def rsie_429_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 26 rsi extremes by measuring deviations from the 126d mean.
    """
    base = (close.pct_change(13).rolling(65).mean())
    return _zscore_rolling(base, 126)

def rsie_430_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 26 rsi extremes by measuring deviations from the 252d mean.
    """
    base = (close.pct_change(13).rolling(65).mean())
    return _zscore_rolling(base, 252)

def rsie_431_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 26 rsi extremes to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = (close.pct_change(13).rolling(65).mean())
    return _rank_pct(base, 5)

def rsie_432_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 26 rsi extremes to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = (close.pct_change(13).rolling(65).mean())
    return _rank_pct(base, 21)

def rsie_433_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 26 rsi extremes to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = (close.pct_change(13).rolling(65).mean())
    return _rank_pct(base, 63)

def rsie_434_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 26 rsi extremes to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = (close.pct_change(13).rolling(65).mean())
    return _rank_pct(base, 126)

def rsie_435_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 26 rsi extremes to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = (close.pct_change(13).rolling(65).mean())
    return _rank_pct(base, 252)

def rsie_436_skew_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 26 rsi extremes distribution over 5d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(13).rolling(65).mean())
    return _rolling_skew(base, 5)

def rsie_437_skew_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 26 rsi extremes distribution over 21d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(13).rolling(65).mean())
    return _rolling_skew(base, 21)

def rsie_438_skew_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 26 rsi extremes distribution over 63d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(13).rolling(65).mean())
    return _rolling_skew(base, 63)

def rsie_439_skew_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 26 rsi extremes distribution over 126d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(13).rolling(65).mean())
    return _rolling_skew(base, 126)

def rsie_440_skew_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 26 rsi extremes distribution over 252d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(13).rolling(65).mean())
    return _rolling_skew(base, 252)

def rsie_441_kurt_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 26 rsi extremes over 5d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(13).rolling(65).mean())
    return _rolling_kurt(base, 5)

def rsie_442_kurt_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 26 rsi extremes over 21d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(13).rolling(65).mean())
    return _rolling_kurt(base, 21)

def rsie_443_kurt_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 26 rsi extremes over 63d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(13).rolling(65).mean())
    return _rolling_kurt(base, 63)

def rsie_444_kurt_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 26 rsi extremes over 126d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(13).rolling(65).mean())
    return _rolling_kurt(base, 126)

def rsie_445_kurt_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 26 rsi extremes over 252d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(13).rolling(65).mean())
    return _rolling_kurt(base, 252)

def rsie_446_voladj_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 26 rsi extremes for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(13).rolling(65).mean())
    return _safe_div(base, _rolling_std(base, 5))

def rsie_447_voladj_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 26 rsi extremes for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(13).rolling(65).mean())
    return _safe_div(base, _rolling_std(base, 21))

def rsie_448_voladj_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 26 rsi extremes for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(13).rolling(65).mean())
    return _safe_div(base, _rolling_std(base, 63))

def rsie_449_voladj_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 26 rsi extremes for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(13).rolling(65).mean())
    return _safe_div(base, _rolling_std(base, 126))

def rsie_450_voladj_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 26 rsi extremes for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(13).rolling(65).mean())
    return _safe_div(base, _rolling_std(base, 252))
