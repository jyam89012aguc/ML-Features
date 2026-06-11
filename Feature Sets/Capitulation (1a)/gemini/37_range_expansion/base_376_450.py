"""
37_37_range_expansion — Base Features 376-450
Domain: 37_range_expansion
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

def rexp_376_voladj_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 37 range expansion for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(11).rolling(55).mean())
    return _safe_div(base, _rolling_std(base, 5))

def rexp_377_voladj_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 37 range expansion for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(11).rolling(55).mean())
    return _safe_div(base, _rolling_std(base, 21))

def rexp_378_voladj_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 37 range expansion for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(11).rolling(55).mean())
    return _safe_div(base, _rolling_std(base, 63))

def rexp_379_voladj_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 37 range expansion for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(11).rolling(55).mean())
    return _safe_div(base, _rolling_std(base, 126))

def rexp_380_voladj_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 37 range expansion for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(11).rolling(55).mean())
    return _safe_div(base, _rolling_std(base, 252))

def rexp_381_lognorm_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 37 range expansion over 5d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(11).rolling(55).mean())
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def rexp_382_lognorm_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 37 range expansion over 21d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(11).rolling(55).mean())
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def rexp_383_lognorm_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 37 range expansion over 63d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(11).rolling(55).mean())
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def rexp_384_lognorm_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 37 range expansion over 126d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(11).rolling(55).mean())
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def rexp_385_lognorm_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 37 range expansion over 252d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(11).rolling(55).mean())
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def rexp_386_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 37 range expansion over a 5d horizon to identify extreme regimes.
    """
    base = (close.pct_change(12).rolling(60).mean())
    return _rolling_mean(base, 5)

def rexp_387_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 37 range expansion over a 21d horizon to identify extreme regimes.
    """
    base = (close.pct_change(12).rolling(60).mean())
    return _rolling_mean(base, 21)

def rexp_388_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 37 range expansion over a 63d horizon to identify extreme regimes.
    """
    base = (close.pct_change(12).rolling(60).mean())
    return _rolling_mean(base, 63)

def rexp_389_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 37 range expansion over a 126d horizon to identify extreme regimes.
    """
    base = (close.pct_change(12).rolling(60).mean())
    return _rolling_mean(base, 126)

def rexp_390_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 37 range expansion over a 252d horizon to identify extreme regimes.
    """
    base = (close.pct_change(12).rolling(60).mean())
    return _rolling_mean(base, 252)

def rexp_391_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 37 range expansion by measuring deviations from the 5d mean.
    """
    base = (close.pct_change(12).rolling(60).mean())
    return _zscore_rolling(base, 5)

def rexp_392_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 37 range expansion by measuring deviations from the 21d mean.
    """
    base = (close.pct_change(12).rolling(60).mean())
    return _zscore_rolling(base, 21)

def rexp_393_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 37 range expansion by measuring deviations from the 63d mean.
    """
    base = (close.pct_change(12).rolling(60).mean())
    return _zscore_rolling(base, 63)

def rexp_394_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 37 range expansion by measuring deviations from the 126d mean.
    """
    base = (close.pct_change(12).rolling(60).mean())
    return _zscore_rolling(base, 126)

def rexp_395_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 37 range expansion by measuring deviations from the 252d mean.
    """
    base = (close.pct_change(12).rolling(60).mean())
    return _zscore_rolling(base, 252)

def rexp_396_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 37 range expansion to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = (close.pct_change(12).rolling(60).mean())
    return _rank_pct(base, 5)

def rexp_397_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 37 range expansion to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = (close.pct_change(12).rolling(60).mean())
    return _rank_pct(base, 21)

def rexp_398_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 37 range expansion to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = (close.pct_change(12).rolling(60).mean())
    return _rank_pct(base, 63)

def rexp_399_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 37 range expansion to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = (close.pct_change(12).rolling(60).mean())
    return _rank_pct(base, 126)

def rexp_400_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 37 range expansion to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = (close.pct_change(12).rolling(60).mean())
    return _rank_pct(base, 252)

def rexp_401_skew_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 37 range expansion distribution over 5d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(12).rolling(60).mean())
    return _rolling_skew(base, 5)

def rexp_402_skew_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 37 range expansion distribution over 21d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(12).rolling(60).mean())
    return _rolling_skew(base, 21)

def rexp_403_skew_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 37 range expansion distribution over 63d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(12).rolling(60).mean())
    return _rolling_skew(base, 63)

def rexp_404_skew_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 37 range expansion distribution over 126d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(12).rolling(60).mean())
    return _rolling_skew(base, 126)

def rexp_405_skew_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 37 range expansion distribution over 252d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(12).rolling(60).mean())
    return _rolling_skew(base, 252)

def rexp_406_kurt_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 37 range expansion over 5d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(12).rolling(60).mean())
    return _rolling_kurt(base, 5)

def rexp_407_kurt_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 37 range expansion over 21d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(12).rolling(60).mean())
    return _rolling_kurt(base, 21)

def rexp_408_kurt_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 37 range expansion over 63d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(12).rolling(60).mean())
    return _rolling_kurt(base, 63)

def rexp_409_kurt_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 37 range expansion over 126d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(12).rolling(60).mean())
    return _rolling_kurt(base, 126)

def rexp_410_kurt_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 37 range expansion over 252d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(12).rolling(60).mean())
    return _rolling_kurt(base, 252)

def rexp_411_voladj_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 37 range expansion for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(12).rolling(60).mean())
    return _safe_div(base, _rolling_std(base, 5))

def rexp_412_voladj_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 37 range expansion for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(12).rolling(60).mean())
    return _safe_div(base, _rolling_std(base, 21))

def rexp_413_voladj_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 37 range expansion for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(12).rolling(60).mean())
    return _safe_div(base, _rolling_std(base, 63))

def rexp_414_voladj_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 37 range expansion for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(12).rolling(60).mean())
    return _safe_div(base, _rolling_std(base, 126))

def rexp_415_voladj_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 37 range expansion for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(12).rolling(60).mean())
    return _safe_div(base, _rolling_std(base, 252))

def rexp_416_lognorm_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 37 range expansion over 5d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(12).rolling(60).mean())
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def rexp_417_lognorm_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 37 range expansion over 21d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(12).rolling(60).mean())
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def rexp_418_lognorm_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 37 range expansion over 63d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(12).rolling(60).mean())
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def rexp_419_lognorm_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 37 range expansion over 126d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(12).rolling(60).mean())
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def rexp_420_lognorm_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 37 range expansion over 252d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(12).rolling(60).mean())
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def rexp_421_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 37 range expansion over a 5d horizon to identify extreme regimes.
    """
    base = (close.pct_change(13).rolling(65).mean())
    return _rolling_mean(base, 5)

def rexp_422_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 37 range expansion over a 21d horizon to identify extreme regimes.
    """
    base = (close.pct_change(13).rolling(65).mean())
    return _rolling_mean(base, 21)

def rexp_423_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 37 range expansion over a 63d horizon to identify extreme regimes.
    """
    base = (close.pct_change(13).rolling(65).mean())
    return _rolling_mean(base, 63)

def rexp_424_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 37 range expansion over a 126d horizon to identify extreme regimes.
    """
    base = (close.pct_change(13).rolling(65).mean())
    return _rolling_mean(base, 126)

def rexp_425_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 37 range expansion over a 252d horizon to identify extreme regimes.
    """
    base = (close.pct_change(13).rolling(65).mean())
    return _rolling_mean(base, 252)

def rexp_426_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 37 range expansion by measuring deviations from the 5d mean.
    """
    base = (close.pct_change(13).rolling(65).mean())
    return _zscore_rolling(base, 5)

def rexp_427_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 37 range expansion by measuring deviations from the 21d mean.
    """
    base = (close.pct_change(13).rolling(65).mean())
    return _zscore_rolling(base, 21)

def rexp_428_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 37 range expansion by measuring deviations from the 63d mean.
    """
    base = (close.pct_change(13).rolling(65).mean())
    return _zscore_rolling(base, 63)

def rexp_429_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 37 range expansion by measuring deviations from the 126d mean.
    """
    base = (close.pct_change(13).rolling(65).mean())
    return _zscore_rolling(base, 126)

def rexp_430_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 37 range expansion by measuring deviations from the 252d mean.
    """
    base = (close.pct_change(13).rolling(65).mean())
    return _zscore_rolling(base, 252)

def rexp_431_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 37 range expansion to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = (close.pct_change(13).rolling(65).mean())
    return _rank_pct(base, 5)

def rexp_432_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 37 range expansion to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = (close.pct_change(13).rolling(65).mean())
    return _rank_pct(base, 21)

def rexp_433_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 37 range expansion to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = (close.pct_change(13).rolling(65).mean())
    return _rank_pct(base, 63)

def rexp_434_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 37 range expansion to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = (close.pct_change(13).rolling(65).mean())
    return _rank_pct(base, 126)

def rexp_435_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 37 range expansion to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = (close.pct_change(13).rolling(65).mean())
    return _rank_pct(base, 252)

def rexp_436_skew_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 37 range expansion distribution over 5d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(13).rolling(65).mean())
    return _rolling_skew(base, 5)

def rexp_437_skew_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 37 range expansion distribution over 21d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(13).rolling(65).mean())
    return _rolling_skew(base, 21)

def rexp_438_skew_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 37 range expansion distribution over 63d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(13).rolling(65).mean())
    return _rolling_skew(base, 63)

def rexp_439_skew_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 37 range expansion distribution over 126d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(13).rolling(65).mean())
    return _rolling_skew(base, 126)

def rexp_440_skew_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 37 range expansion distribution over 252d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(13).rolling(65).mean())
    return _rolling_skew(base, 252)

def rexp_441_kurt_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 37 range expansion over 5d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(13).rolling(65).mean())
    return _rolling_kurt(base, 5)

def rexp_442_kurt_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 37 range expansion over 21d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(13).rolling(65).mean())
    return _rolling_kurt(base, 21)

def rexp_443_kurt_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 37 range expansion over 63d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(13).rolling(65).mean())
    return _rolling_kurt(base, 63)

def rexp_444_kurt_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 37 range expansion over 126d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(13).rolling(65).mean())
    return _rolling_kurt(base, 126)

def rexp_445_kurt_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 37 range expansion over 252d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(13).rolling(65).mean())
    return _rolling_kurt(base, 252)

def rexp_446_voladj_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 37 range expansion for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(13).rolling(65).mean())
    return _safe_div(base, _rolling_std(base, 5))

def rexp_447_voladj_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 37 range expansion for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(13).rolling(65).mean())
    return _safe_div(base, _rolling_std(base, 21))

def rexp_448_voladj_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 37 range expansion for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(13).rolling(65).mean())
    return _safe_div(base, _rolling_std(base, 63))

def rexp_449_voladj_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 37 range expansion for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(13).rolling(65).mean())
    return _safe_div(base, _rolling_std(base, 126))

def rexp_450_voladj_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 37 range expansion for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(13).rolling(65).mean())
    return _safe_div(base, _rolling_std(base, 252))
