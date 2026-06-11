"""
18_18_volume_dryup — Base Features 376-450
Domain: 18_volume_dryup
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

def vdry_376_voladj_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 18 volume dryup for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(11).rolling(55).mean())
    return _safe_div(base, _rolling_std(base, 5))

def vdry_377_voladj_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 18 volume dryup for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(11).rolling(55).mean())
    return _safe_div(base, _rolling_std(base, 21))

def vdry_378_voladj_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 18 volume dryup for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(11).rolling(55).mean())
    return _safe_div(base, _rolling_std(base, 63))

def vdry_379_voladj_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 18 volume dryup for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(11).rolling(55).mean())
    return _safe_div(base, _rolling_std(base, 126))

def vdry_380_voladj_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 18 volume dryup for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(11).rolling(55).mean())
    return _safe_div(base, _rolling_std(base, 252))

def vdry_381_lognorm_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 18 volume dryup over 5d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(11).rolling(55).mean())
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def vdry_382_lognorm_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 18 volume dryup over 21d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(11).rolling(55).mean())
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def vdry_383_lognorm_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 18 volume dryup over 63d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(11).rolling(55).mean())
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def vdry_384_lognorm_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 18 volume dryup over 126d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(11).rolling(55).mean())
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def vdry_385_lognorm_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 18 volume dryup over 252d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(11).rolling(55).mean())
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def vdry_386_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 18 volume dryup over a 5d horizon to identify extreme regimes.
    """
    base = (close.pct_change(12).rolling(60).mean())
    return _rolling_mean(base, 5)

def vdry_387_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 18 volume dryup over a 21d horizon to identify extreme regimes.
    """
    base = (close.pct_change(12).rolling(60).mean())
    return _rolling_mean(base, 21)

def vdry_388_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 18 volume dryup over a 63d horizon to identify extreme regimes.
    """
    base = (close.pct_change(12).rolling(60).mean())
    return _rolling_mean(base, 63)

def vdry_389_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 18 volume dryup over a 126d horizon to identify extreme regimes.
    """
    base = (close.pct_change(12).rolling(60).mean())
    return _rolling_mean(base, 126)

def vdry_390_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 18 volume dryup over a 252d horizon to identify extreme regimes.
    """
    base = (close.pct_change(12).rolling(60).mean())
    return _rolling_mean(base, 252)

def vdry_391_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 18 volume dryup by measuring deviations from the 5d mean.
    """
    base = (close.pct_change(12).rolling(60).mean())
    return _zscore_rolling(base, 5)

def vdry_392_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 18 volume dryup by measuring deviations from the 21d mean.
    """
    base = (close.pct_change(12).rolling(60).mean())
    return _zscore_rolling(base, 21)

def vdry_393_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 18 volume dryup by measuring deviations from the 63d mean.
    """
    base = (close.pct_change(12).rolling(60).mean())
    return _zscore_rolling(base, 63)

def vdry_394_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 18 volume dryup by measuring deviations from the 126d mean.
    """
    base = (close.pct_change(12).rolling(60).mean())
    return _zscore_rolling(base, 126)

def vdry_395_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 18 volume dryup by measuring deviations from the 252d mean.
    """
    base = (close.pct_change(12).rolling(60).mean())
    return _zscore_rolling(base, 252)

def vdry_396_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 18 volume dryup to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = (close.pct_change(12).rolling(60).mean())
    return _rank_pct(base, 5)

def vdry_397_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 18 volume dryup to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = (close.pct_change(12).rolling(60).mean())
    return _rank_pct(base, 21)

def vdry_398_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 18 volume dryup to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = (close.pct_change(12).rolling(60).mean())
    return _rank_pct(base, 63)

def vdry_399_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 18 volume dryup to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = (close.pct_change(12).rolling(60).mean())
    return _rank_pct(base, 126)

def vdry_400_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 18 volume dryup to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = (close.pct_change(12).rolling(60).mean())
    return _rank_pct(base, 252)

def vdry_401_skew_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 18 volume dryup distribution over 5d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(12).rolling(60).mean())
    return _rolling_skew(base, 5)

def vdry_402_skew_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 18 volume dryup distribution over 21d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(12).rolling(60).mean())
    return _rolling_skew(base, 21)

def vdry_403_skew_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 18 volume dryup distribution over 63d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(12).rolling(60).mean())
    return _rolling_skew(base, 63)

def vdry_404_skew_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 18 volume dryup distribution over 126d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(12).rolling(60).mean())
    return _rolling_skew(base, 126)

def vdry_405_skew_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 18 volume dryup distribution over 252d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(12).rolling(60).mean())
    return _rolling_skew(base, 252)

def vdry_406_kurt_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 18 volume dryup over 5d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(12).rolling(60).mean())
    return _rolling_kurt(base, 5)

def vdry_407_kurt_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 18 volume dryup over 21d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(12).rolling(60).mean())
    return _rolling_kurt(base, 21)

def vdry_408_kurt_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 18 volume dryup over 63d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(12).rolling(60).mean())
    return _rolling_kurt(base, 63)

def vdry_409_kurt_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 18 volume dryup over 126d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(12).rolling(60).mean())
    return _rolling_kurt(base, 126)

def vdry_410_kurt_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 18 volume dryup over 252d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(12).rolling(60).mean())
    return _rolling_kurt(base, 252)

def vdry_411_voladj_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 18 volume dryup for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(12).rolling(60).mean())
    return _safe_div(base, _rolling_std(base, 5))

def vdry_412_voladj_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 18 volume dryup for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(12).rolling(60).mean())
    return _safe_div(base, _rolling_std(base, 21))

def vdry_413_voladj_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 18 volume dryup for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(12).rolling(60).mean())
    return _safe_div(base, _rolling_std(base, 63))

def vdry_414_voladj_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 18 volume dryup for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(12).rolling(60).mean())
    return _safe_div(base, _rolling_std(base, 126))

def vdry_415_voladj_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 18 volume dryup for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(12).rolling(60).mean())
    return _safe_div(base, _rolling_std(base, 252))

def vdry_416_lognorm_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 18 volume dryup over 5d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(12).rolling(60).mean())
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def vdry_417_lognorm_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 18 volume dryup over 21d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(12).rolling(60).mean())
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def vdry_418_lognorm_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 18 volume dryup over 63d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(12).rolling(60).mean())
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def vdry_419_lognorm_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 18 volume dryup over 126d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(12).rolling(60).mean())
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def vdry_420_lognorm_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 18 volume dryup over 252d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(12).rolling(60).mean())
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def vdry_421_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 18 volume dryup over a 5d horizon to identify extreme regimes.
    """
    base = (close.pct_change(13).rolling(65).mean())
    return _rolling_mean(base, 5)

def vdry_422_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 18 volume dryup over a 21d horizon to identify extreme regimes.
    """
    base = (close.pct_change(13).rolling(65).mean())
    return _rolling_mean(base, 21)

def vdry_423_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 18 volume dryup over a 63d horizon to identify extreme regimes.
    """
    base = (close.pct_change(13).rolling(65).mean())
    return _rolling_mean(base, 63)

def vdry_424_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 18 volume dryup over a 126d horizon to identify extreme regimes.
    """
    base = (close.pct_change(13).rolling(65).mean())
    return _rolling_mean(base, 126)

def vdry_425_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 18 volume dryup over a 252d horizon to identify extreme regimes.
    """
    base = (close.pct_change(13).rolling(65).mean())
    return _rolling_mean(base, 252)

def vdry_426_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 18 volume dryup by measuring deviations from the 5d mean.
    """
    base = (close.pct_change(13).rolling(65).mean())
    return _zscore_rolling(base, 5)

def vdry_427_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 18 volume dryup by measuring deviations from the 21d mean.
    """
    base = (close.pct_change(13).rolling(65).mean())
    return _zscore_rolling(base, 21)

def vdry_428_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 18 volume dryup by measuring deviations from the 63d mean.
    """
    base = (close.pct_change(13).rolling(65).mean())
    return _zscore_rolling(base, 63)

def vdry_429_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 18 volume dryup by measuring deviations from the 126d mean.
    """
    base = (close.pct_change(13).rolling(65).mean())
    return _zscore_rolling(base, 126)

def vdry_430_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 18 volume dryup by measuring deviations from the 252d mean.
    """
    base = (close.pct_change(13).rolling(65).mean())
    return _zscore_rolling(base, 252)

def vdry_431_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 18 volume dryup to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = (close.pct_change(13).rolling(65).mean())
    return _rank_pct(base, 5)

def vdry_432_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 18 volume dryup to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = (close.pct_change(13).rolling(65).mean())
    return _rank_pct(base, 21)

def vdry_433_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 18 volume dryup to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = (close.pct_change(13).rolling(65).mean())
    return _rank_pct(base, 63)

def vdry_434_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 18 volume dryup to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = (close.pct_change(13).rolling(65).mean())
    return _rank_pct(base, 126)

def vdry_435_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 18 volume dryup to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = (close.pct_change(13).rolling(65).mean())
    return _rank_pct(base, 252)

def vdry_436_skew_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 18 volume dryup distribution over 5d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(13).rolling(65).mean())
    return _rolling_skew(base, 5)

def vdry_437_skew_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 18 volume dryup distribution over 21d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(13).rolling(65).mean())
    return _rolling_skew(base, 21)

def vdry_438_skew_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 18 volume dryup distribution over 63d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(13).rolling(65).mean())
    return _rolling_skew(base, 63)

def vdry_439_skew_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 18 volume dryup distribution over 126d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(13).rolling(65).mean())
    return _rolling_skew(base, 126)

def vdry_440_skew_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 18 volume dryup distribution over 252d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(13).rolling(65).mean())
    return _rolling_skew(base, 252)

def vdry_441_kurt_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 18 volume dryup over 5d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(13).rolling(65).mean())
    return _rolling_kurt(base, 5)

def vdry_442_kurt_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 18 volume dryup over 21d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(13).rolling(65).mean())
    return _rolling_kurt(base, 21)

def vdry_443_kurt_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 18 volume dryup over 63d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(13).rolling(65).mean())
    return _rolling_kurt(base, 63)

def vdry_444_kurt_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 18 volume dryup over 126d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(13).rolling(65).mean())
    return _rolling_kurt(base, 126)

def vdry_445_kurt_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 18 volume dryup over 252d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(13).rolling(65).mean())
    return _rolling_kurt(base, 252)

def vdry_446_voladj_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 18 volume dryup for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(13).rolling(65).mean())
    return _safe_div(base, _rolling_std(base, 5))

def vdry_447_voladj_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 18 volume dryup for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(13).rolling(65).mean())
    return _safe_div(base, _rolling_std(base, 21))

def vdry_448_voladj_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 18 volume dryup for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(13).rolling(65).mean())
    return _safe_div(base, _rolling_std(base, 63))

def vdry_449_voladj_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 18 volume dryup for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(13).rolling(65).mean())
    return _safe_div(base, _rolling_std(base, 126))

def vdry_450_voladj_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 18 volume dryup for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(13).rolling(65).mean())
    return _safe_div(base, _rolling_std(base, 252))
