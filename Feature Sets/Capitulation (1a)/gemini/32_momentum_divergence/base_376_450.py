"""
32_32_momentum_divergence — Base Features 376-450
Domain: 32_momentum_divergence
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

def mdiv_376_voladj_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 32 momentum divergence for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(11).rolling(55).mean())
    return _safe_div(base, _rolling_std(base, 5))

def mdiv_377_voladj_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 32 momentum divergence for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(11).rolling(55).mean())
    return _safe_div(base, _rolling_std(base, 21))

def mdiv_378_voladj_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 32 momentum divergence for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(11).rolling(55).mean())
    return _safe_div(base, _rolling_std(base, 63))

def mdiv_379_voladj_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 32 momentum divergence for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(11).rolling(55).mean())
    return _safe_div(base, _rolling_std(base, 126))

def mdiv_380_voladj_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 32 momentum divergence for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(11).rolling(55).mean())
    return _safe_div(base, _rolling_std(base, 252))

def mdiv_381_lognorm_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 32 momentum divergence over 5d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(11).rolling(55).mean())
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def mdiv_382_lognorm_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 32 momentum divergence over 21d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(11).rolling(55).mean())
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def mdiv_383_lognorm_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 32 momentum divergence over 63d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(11).rolling(55).mean())
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def mdiv_384_lognorm_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 32 momentum divergence over 126d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(11).rolling(55).mean())
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def mdiv_385_lognorm_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 32 momentum divergence over 252d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(11).rolling(55).mean())
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def mdiv_386_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 32 momentum divergence over a 5d horizon to identify extreme regimes.
    """
    base = (close.pct_change(12).rolling(60).mean())
    return _rolling_mean(base, 5)

def mdiv_387_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 32 momentum divergence over a 21d horizon to identify extreme regimes.
    """
    base = (close.pct_change(12).rolling(60).mean())
    return _rolling_mean(base, 21)

def mdiv_388_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 32 momentum divergence over a 63d horizon to identify extreme regimes.
    """
    base = (close.pct_change(12).rolling(60).mean())
    return _rolling_mean(base, 63)

def mdiv_389_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 32 momentum divergence over a 126d horizon to identify extreme regimes.
    """
    base = (close.pct_change(12).rolling(60).mean())
    return _rolling_mean(base, 126)

def mdiv_390_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 32 momentum divergence over a 252d horizon to identify extreme regimes.
    """
    base = (close.pct_change(12).rolling(60).mean())
    return _rolling_mean(base, 252)

def mdiv_391_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 32 momentum divergence by measuring deviations from the 5d mean.
    """
    base = (close.pct_change(12).rolling(60).mean())
    return _zscore_rolling(base, 5)

def mdiv_392_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 32 momentum divergence by measuring deviations from the 21d mean.
    """
    base = (close.pct_change(12).rolling(60).mean())
    return _zscore_rolling(base, 21)

def mdiv_393_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 32 momentum divergence by measuring deviations from the 63d mean.
    """
    base = (close.pct_change(12).rolling(60).mean())
    return _zscore_rolling(base, 63)

def mdiv_394_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 32 momentum divergence by measuring deviations from the 126d mean.
    """
    base = (close.pct_change(12).rolling(60).mean())
    return _zscore_rolling(base, 126)

def mdiv_395_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 32 momentum divergence by measuring deviations from the 252d mean.
    """
    base = (close.pct_change(12).rolling(60).mean())
    return _zscore_rolling(base, 252)

def mdiv_396_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 32 momentum divergence to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = (close.pct_change(12).rolling(60).mean())
    return _rank_pct(base, 5)

def mdiv_397_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 32 momentum divergence to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = (close.pct_change(12).rolling(60).mean())
    return _rank_pct(base, 21)

def mdiv_398_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 32 momentum divergence to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = (close.pct_change(12).rolling(60).mean())
    return _rank_pct(base, 63)

def mdiv_399_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 32 momentum divergence to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = (close.pct_change(12).rolling(60).mean())
    return _rank_pct(base, 126)

def mdiv_400_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 32 momentum divergence to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = (close.pct_change(12).rolling(60).mean())
    return _rank_pct(base, 252)

def mdiv_401_skew_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 32 momentum divergence distribution over 5d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(12).rolling(60).mean())
    return _rolling_skew(base, 5)

def mdiv_402_skew_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 32 momentum divergence distribution over 21d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(12).rolling(60).mean())
    return _rolling_skew(base, 21)

def mdiv_403_skew_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 32 momentum divergence distribution over 63d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(12).rolling(60).mean())
    return _rolling_skew(base, 63)

def mdiv_404_skew_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 32 momentum divergence distribution over 126d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(12).rolling(60).mean())
    return _rolling_skew(base, 126)

def mdiv_405_skew_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 32 momentum divergence distribution over 252d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(12).rolling(60).mean())
    return _rolling_skew(base, 252)

def mdiv_406_kurt_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 32 momentum divergence over 5d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(12).rolling(60).mean())
    return _rolling_kurt(base, 5)

def mdiv_407_kurt_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 32 momentum divergence over 21d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(12).rolling(60).mean())
    return _rolling_kurt(base, 21)

def mdiv_408_kurt_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 32 momentum divergence over 63d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(12).rolling(60).mean())
    return _rolling_kurt(base, 63)

def mdiv_409_kurt_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 32 momentum divergence over 126d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(12).rolling(60).mean())
    return _rolling_kurt(base, 126)

def mdiv_410_kurt_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 32 momentum divergence over 252d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(12).rolling(60).mean())
    return _rolling_kurt(base, 252)

def mdiv_411_voladj_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 32 momentum divergence for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(12).rolling(60).mean())
    return _safe_div(base, _rolling_std(base, 5))

def mdiv_412_voladj_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 32 momentum divergence for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(12).rolling(60).mean())
    return _safe_div(base, _rolling_std(base, 21))

def mdiv_413_voladj_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 32 momentum divergence for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(12).rolling(60).mean())
    return _safe_div(base, _rolling_std(base, 63))

def mdiv_414_voladj_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 32 momentum divergence for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(12).rolling(60).mean())
    return _safe_div(base, _rolling_std(base, 126))

def mdiv_415_voladj_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 32 momentum divergence for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(12).rolling(60).mean())
    return _safe_div(base, _rolling_std(base, 252))

def mdiv_416_lognorm_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 32 momentum divergence over 5d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(12).rolling(60).mean())
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def mdiv_417_lognorm_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 32 momentum divergence over 21d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(12).rolling(60).mean())
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def mdiv_418_lognorm_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 32 momentum divergence over 63d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(12).rolling(60).mean())
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def mdiv_419_lognorm_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 32 momentum divergence over 126d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(12).rolling(60).mean())
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def mdiv_420_lognorm_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 32 momentum divergence over 252d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(12).rolling(60).mean())
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def mdiv_421_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 32 momentum divergence over a 5d horizon to identify extreme regimes.
    """
    base = (close.pct_change(13).rolling(65).mean())
    return _rolling_mean(base, 5)

def mdiv_422_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 32 momentum divergence over a 21d horizon to identify extreme regimes.
    """
    base = (close.pct_change(13).rolling(65).mean())
    return _rolling_mean(base, 21)

def mdiv_423_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 32 momentum divergence over a 63d horizon to identify extreme regimes.
    """
    base = (close.pct_change(13).rolling(65).mean())
    return _rolling_mean(base, 63)

def mdiv_424_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 32 momentum divergence over a 126d horizon to identify extreme regimes.
    """
    base = (close.pct_change(13).rolling(65).mean())
    return _rolling_mean(base, 126)

def mdiv_425_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 32 momentum divergence over a 252d horizon to identify extreme regimes.
    """
    base = (close.pct_change(13).rolling(65).mean())
    return _rolling_mean(base, 252)

def mdiv_426_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 32 momentum divergence by measuring deviations from the 5d mean.
    """
    base = (close.pct_change(13).rolling(65).mean())
    return _zscore_rolling(base, 5)

def mdiv_427_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 32 momentum divergence by measuring deviations from the 21d mean.
    """
    base = (close.pct_change(13).rolling(65).mean())
    return _zscore_rolling(base, 21)

def mdiv_428_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 32 momentum divergence by measuring deviations from the 63d mean.
    """
    base = (close.pct_change(13).rolling(65).mean())
    return _zscore_rolling(base, 63)

def mdiv_429_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 32 momentum divergence by measuring deviations from the 126d mean.
    """
    base = (close.pct_change(13).rolling(65).mean())
    return _zscore_rolling(base, 126)

def mdiv_430_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 32 momentum divergence by measuring deviations from the 252d mean.
    """
    base = (close.pct_change(13).rolling(65).mean())
    return _zscore_rolling(base, 252)

def mdiv_431_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 32 momentum divergence to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = (close.pct_change(13).rolling(65).mean())
    return _rank_pct(base, 5)

def mdiv_432_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 32 momentum divergence to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = (close.pct_change(13).rolling(65).mean())
    return _rank_pct(base, 21)

def mdiv_433_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 32 momentum divergence to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = (close.pct_change(13).rolling(65).mean())
    return _rank_pct(base, 63)

def mdiv_434_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 32 momentum divergence to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = (close.pct_change(13).rolling(65).mean())
    return _rank_pct(base, 126)

def mdiv_435_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 32 momentum divergence to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = (close.pct_change(13).rolling(65).mean())
    return _rank_pct(base, 252)

def mdiv_436_skew_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 32 momentum divergence distribution over 5d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(13).rolling(65).mean())
    return _rolling_skew(base, 5)

def mdiv_437_skew_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 32 momentum divergence distribution over 21d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(13).rolling(65).mean())
    return _rolling_skew(base, 21)

def mdiv_438_skew_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 32 momentum divergence distribution over 63d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(13).rolling(65).mean())
    return _rolling_skew(base, 63)

def mdiv_439_skew_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 32 momentum divergence distribution over 126d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(13).rolling(65).mean())
    return _rolling_skew(base, 126)

def mdiv_440_skew_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 32 momentum divergence distribution over 252d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(13).rolling(65).mean())
    return _rolling_skew(base, 252)

def mdiv_441_kurt_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 32 momentum divergence over 5d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(13).rolling(65).mean())
    return _rolling_kurt(base, 5)

def mdiv_442_kurt_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 32 momentum divergence over 21d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(13).rolling(65).mean())
    return _rolling_kurt(base, 21)

def mdiv_443_kurt_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 32 momentum divergence over 63d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(13).rolling(65).mean())
    return _rolling_kurt(base, 63)

def mdiv_444_kurt_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 32 momentum divergence over 126d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(13).rolling(65).mean())
    return _rolling_kurt(base, 126)

def mdiv_445_kurt_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 32 momentum divergence over 252d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(13).rolling(65).mean())
    return _rolling_kurt(base, 252)

def mdiv_446_voladj_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 32 momentum divergence for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(13).rolling(65).mean())
    return _safe_div(base, _rolling_std(base, 5))

def mdiv_447_voladj_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 32 momentum divergence for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(13).rolling(65).mean())
    return _safe_div(base, _rolling_std(base, 21))

def mdiv_448_voladj_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 32 momentum divergence for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(13).rolling(65).mean())
    return _safe_div(base, _rolling_std(base, 63))

def mdiv_449_voladj_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 32 momentum divergence for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(13).rolling(65).mean())
    return _safe_div(base, _rolling_std(base, 126))

def mdiv_450_voladj_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 32 momentum divergence for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(13).rolling(65).mean())
    return _safe_div(base, _rolling_std(base, 252))
