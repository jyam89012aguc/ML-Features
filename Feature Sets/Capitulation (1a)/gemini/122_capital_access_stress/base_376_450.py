"""
122_122_capital_access_stress — Base Features 376-450
Domain: 122_capital_access_stress
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

def cast_376_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 122 capital access stress for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(55).std()
    return _safe_div(base, _rolling_std(base, 5))

def cast_377_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 122 capital access stress for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(55).std()
    return _safe_div(base, _rolling_std(base, 21))

def cast_378_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 122 capital access stress for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(55).std()
    return _safe_div(base, _rolling_std(base, 63))

def cast_379_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 122 capital access stress for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(55).std()
    return _safe_div(base, _rolling_std(base, 126))

def cast_380_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 122 capital access stress for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(55).std()
    return _safe_div(base, _rolling_std(base, 252))

def cast_381_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 122 capital access stress over 5d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(55).std()
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def cast_382_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 122 capital access stress over 21d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(55).std()
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def cast_383_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 122 capital access stress over 63d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(55).std()
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def cast_384_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 122 capital access stress over 126d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(55).std()
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def cast_385_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 122 capital access stress over 252d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(55).std()
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def cast_386_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 122 capital access stress over a 5d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(60).std()
    return _rolling_mean(base, 5)

def cast_387_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 122 capital access stress over a 21d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(60).std()
    return _rolling_mean(base, 21)

def cast_388_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 122 capital access stress over a 63d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(60).std()
    return _rolling_mean(base, 63)

def cast_389_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 122 capital access stress over a 126d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(60).std()
    return _rolling_mean(base, 126)

def cast_390_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 122 capital access stress over a 252d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(60).std()
    return _rolling_mean(base, 252)

def cast_391_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 122 capital access stress by measuring deviations from the 5d mean.
    """
    base = close.pct_change().rolling(60).std()
    return _zscore_rolling(base, 5)

def cast_392_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 122 capital access stress by measuring deviations from the 21d mean.
    """
    base = close.pct_change().rolling(60).std()
    return _zscore_rolling(base, 21)

def cast_393_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 122 capital access stress by measuring deviations from the 63d mean.
    """
    base = close.pct_change().rolling(60).std()
    return _zscore_rolling(base, 63)

def cast_394_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 122 capital access stress by measuring deviations from the 126d mean.
    """
    base = close.pct_change().rolling(60).std()
    return _zscore_rolling(base, 126)

def cast_395_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 122 capital access stress by measuring deviations from the 252d mean.
    """
    base = close.pct_change().rolling(60).std()
    return _zscore_rolling(base, 252)

def cast_396_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 122 capital access stress to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(60).std()
    return _rank_pct(base, 5)

def cast_397_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 122 capital access stress to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(60).std()
    return _rank_pct(base, 21)

def cast_398_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 122 capital access stress to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(60).std()
    return _rank_pct(base, 63)

def cast_399_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 122 capital access stress to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(60).std()
    return _rank_pct(base, 126)

def cast_400_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 122 capital access stress to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(60).std()
    return _rank_pct(base, 252)

def cast_401_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 122 capital access stress distribution over 5d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(60).std()
    return _rolling_skew(base, 5)

def cast_402_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 122 capital access stress distribution over 21d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(60).std()
    return _rolling_skew(base, 21)

def cast_403_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 122 capital access stress distribution over 63d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(60).std()
    return _rolling_skew(base, 63)

def cast_404_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 122 capital access stress distribution over 126d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(60).std()
    return _rolling_skew(base, 126)

def cast_405_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 122 capital access stress distribution over 252d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(60).std()
    return _rolling_skew(base, 252)

def cast_406_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 122 capital access stress over 5d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(60).std()
    return _rolling_kurt(base, 5)

def cast_407_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 122 capital access stress over 21d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(60).std()
    return _rolling_kurt(base, 21)

def cast_408_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 122 capital access stress over 63d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(60).std()
    return _rolling_kurt(base, 63)

def cast_409_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 122 capital access stress over 126d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(60).std()
    return _rolling_kurt(base, 126)

def cast_410_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 122 capital access stress over 252d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(60).std()
    return _rolling_kurt(base, 252)

def cast_411_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 122 capital access stress for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(60).std()
    return _safe_div(base, _rolling_std(base, 5))

def cast_412_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 122 capital access stress for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(60).std()
    return _safe_div(base, _rolling_std(base, 21))

def cast_413_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 122 capital access stress for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(60).std()
    return _safe_div(base, _rolling_std(base, 63))

def cast_414_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 122 capital access stress for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(60).std()
    return _safe_div(base, _rolling_std(base, 126))

def cast_415_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 122 capital access stress for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(60).std()
    return _safe_div(base, _rolling_std(base, 252))

def cast_416_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 122 capital access stress over 5d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(60).std()
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def cast_417_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 122 capital access stress over 21d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(60).std()
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def cast_418_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 122 capital access stress over 63d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(60).std()
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def cast_419_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 122 capital access stress over 126d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(60).std()
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def cast_420_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 122 capital access stress over 252d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(60).std()
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def cast_421_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 122 capital access stress over a 5d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(65).std()
    return _rolling_mean(base, 5)

def cast_422_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 122 capital access stress over a 21d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(65).std()
    return _rolling_mean(base, 21)

def cast_423_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 122 capital access stress over a 63d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(65).std()
    return _rolling_mean(base, 63)

def cast_424_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 122 capital access stress over a 126d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(65).std()
    return _rolling_mean(base, 126)

def cast_425_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 122 capital access stress over a 252d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(65).std()
    return _rolling_mean(base, 252)

def cast_426_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 122 capital access stress by measuring deviations from the 5d mean.
    """
    base = close.pct_change().rolling(65).std()
    return _zscore_rolling(base, 5)

def cast_427_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 122 capital access stress by measuring deviations from the 21d mean.
    """
    base = close.pct_change().rolling(65).std()
    return _zscore_rolling(base, 21)

def cast_428_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 122 capital access stress by measuring deviations from the 63d mean.
    """
    base = close.pct_change().rolling(65).std()
    return _zscore_rolling(base, 63)

def cast_429_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 122 capital access stress by measuring deviations from the 126d mean.
    """
    base = close.pct_change().rolling(65).std()
    return _zscore_rolling(base, 126)

def cast_430_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 122 capital access stress by measuring deviations from the 252d mean.
    """
    base = close.pct_change().rolling(65).std()
    return _zscore_rolling(base, 252)

def cast_431_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 122 capital access stress to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(65).std()
    return _rank_pct(base, 5)

def cast_432_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 122 capital access stress to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(65).std()
    return _rank_pct(base, 21)

def cast_433_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 122 capital access stress to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(65).std()
    return _rank_pct(base, 63)

def cast_434_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 122 capital access stress to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(65).std()
    return _rank_pct(base, 126)

def cast_435_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 122 capital access stress to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(65).std()
    return _rank_pct(base, 252)

def cast_436_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 122 capital access stress distribution over 5d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(65).std()
    return _rolling_skew(base, 5)

def cast_437_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 122 capital access stress distribution over 21d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(65).std()
    return _rolling_skew(base, 21)

def cast_438_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 122 capital access stress distribution over 63d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(65).std()
    return _rolling_skew(base, 63)

def cast_439_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 122 capital access stress distribution over 126d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(65).std()
    return _rolling_skew(base, 126)

def cast_440_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 122 capital access stress distribution over 252d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(65).std()
    return _rolling_skew(base, 252)

def cast_441_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 122 capital access stress over 5d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(65).std()
    return _rolling_kurt(base, 5)

def cast_442_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 122 capital access stress over 21d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(65).std()
    return _rolling_kurt(base, 21)

def cast_443_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 122 capital access stress over 63d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(65).std()
    return _rolling_kurt(base, 63)

def cast_444_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 122 capital access stress over 126d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(65).std()
    return _rolling_kurt(base, 126)

def cast_445_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 122 capital access stress over 252d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(65).std()
    return _rolling_kurt(base, 252)

def cast_446_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 122 capital access stress for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(65).std()
    return _safe_div(base, _rolling_std(base, 5))

def cast_447_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 122 capital access stress for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(65).std()
    return _safe_div(base, _rolling_std(base, 21))

def cast_448_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 122 capital access stress for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(65).std()
    return _safe_div(base, _rolling_std(base, 63))

def cast_449_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 122 capital access stress for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(65).std()
    return _safe_div(base, _rolling_std(base, 126))

def cast_450_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 122 capital access stress for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(65).std()
    return _safe_div(base, _rolling_std(base, 252))
