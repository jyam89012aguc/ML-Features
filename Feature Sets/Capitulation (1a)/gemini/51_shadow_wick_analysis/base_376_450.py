"""
51_51_shadow_wick_analysis — Base Features 376-450
Domain: 51_shadow_wick_analysis
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

def swik_376_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 51 shadow wick analysis for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = ((close - open).abs().rolling(55).mean())
    return _safe_div(base, _rolling_std(base, 5))

def swik_377_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 51 shadow wick analysis for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = ((close - open).abs().rolling(55).mean())
    return _safe_div(base, _rolling_std(base, 21))

def swik_378_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 51 shadow wick analysis for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = ((close - open).abs().rolling(55).mean())
    return _safe_div(base, _rolling_std(base, 63))

def swik_379_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 51 shadow wick analysis for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = ((close - open).abs().rolling(55).mean())
    return _safe_div(base, _rolling_std(base, 126))

def swik_380_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 51 shadow wick analysis for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = ((close - open).abs().rolling(55).mean())
    return _safe_div(base, _rolling_std(base, 252))

def swik_381_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 51 shadow wick analysis over 5d to stabilize variance and capture exponential shifts.
    """
    base = ((close - open).abs().rolling(55).mean())
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def swik_382_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 51 shadow wick analysis over 21d to stabilize variance and capture exponential shifts.
    """
    base = ((close - open).abs().rolling(55).mean())
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def swik_383_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 51 shadow wick analysis over 63d to stabilize variance and capture exponential shifts.
    """
    base = ((close - open).abs().rolling(55).mean())
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def swik_384_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 51 shadow wick analysis over 126d to stabilize variance and capture exponential shifts.
    """
    base = ((close - open).abs().rolling(55).mean())
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def swik_385_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 51 shadow wick analysis over 252d to stabilize variance and capture exponential shifts.
    """
    base = ((close - open).abs().rolling(55).mean())
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def swik_386_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 51 shadow wick analysis over a 5d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(60).mean())
    return _rolling_mean(base, 5)

def swik_387_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 51 shadow wick analysis over a 21d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(60).mean())
    return _rolling_mean(base, 21)

def swik_388_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 51 shadow wick analysis over a 63d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(60).mean())
    return _rolling_mean(base, 63)

def swik_389_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 51 shadow wick analysis over a 126d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(60).mean())
    return _rolling_mean(base, 126)

def swik_390_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 51 shadow wick analysis over a 252d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(60).mean())
    return _rolling_mean(base, 252)

def swik_391_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 51 shadow wick analysis by measuring deviations from the 5d mean.
    """
    base = ((close - open).abs().rolling(60).mean())
    return _zscore_rolling(base, 5)

def swik_392_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 51 shadow wick analysis by measuring deviations from the 21d mean.
    """
    base = ((close - open).abs().rolling(60).mean())
    return _zscore_rolling(base, 21)

def swik_393_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 51 shadow wick analysis by measuring deviations from the 63d mean.
    """
    base = ((close - open).abs().rolling(60).mean())
    return _zscore_rolling(base, 63)

def swik_394_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 51 shadow wick analysis by measuring deviations from the 126d mean.
    """
    base = ((close - open).abs().rolling(60).mean())
    return _zscore_rolling(base, 126)

def swik_395_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 51 shadow wick analysis by measuring deviations from the 252d mean.
    """
    base = ((close - open).abs().rolling(60).mean())
    return _zscore_rolling(base, 252)

def swik_396_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 51 shadow wick analysis to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = ((close - open).abs().rolling(60).mean())
    return _rank_pct(base, 5)

def swik_397_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 51 shadow wick analysis to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = ((close - open).abs().rolling(60).mean())
    return _rank_pct(base, 21)

def swik_398_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 51 shadow wick analysis to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = ((close - open).abs().rolling(60).mean())
    return _rank_pct(base, 63)

def swik_399_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 51 shadow wick analysis to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = ((close - open).abs().rolling(60).mean())
    return _rank_pct(base, 126)

def swik_400_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 51 shadow wick analysis to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = ((close - open).abs().rolling(60).mean())
    return _rank_pct(base, 252)

def swik_401_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 51 shadow wick analysis distribution over 5d to detect tail risk or exhaustion.
    """
    base = ((close - open).abs().rolling(60).mean())
    return _rolling_skew(base, 5)

def swik_402_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 51 shadow wick analysis distribution over 21d to detect tail risk or exhaustion.
    """
    base = ((close - open).abs().rolling(60).mean())
    return _rolling_skew(base, 21)

def swik_403_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 51 shadow wick analysis distribution over 63d to detect tail risk or exhaustion.
    """
    base = ((close - open).abs().rolling(60).mean())
    return _rolling_skew(base, 63)

def swik_404_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 51 shadow wick analysis distribution over 126d to detect tail risk or exhaustion.
    """
    base = ((close - open).abs().rolling(60).mean())
    return _rolling_skew(base, 126)

def swik_405_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 51 shadow wick analysis distribution over 252d to detect tail risk or exhaustion.
    """
    base = ((close - open).abs().rolling(60).mean())
    return _rolling_skew(base, 252)

def swik_406_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 51 shadow wick analysis over 5d to capture explosive breakdown or reversal points.
    """
    base = ((close - open).abs().rolling(60).mean())
    return _rolling_kurt(base, 5)

def swik_407_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 51 shadow wick analysis over 21d to capture explosive breakdown or reversal points.
    """
    base = ((close - open).abs().rolling(60).mean())
    return _rolling_kurt(base, 21)

def swik_408_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 51 shadow wick analysis over 63d to capture explosive breakdown or reversal points.
    """
    base = ((close - open).abs().rolling(60).mean())
    return _rolling_kurt(base, 63)

def swik_409_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 51 shadow wick analysis over 126d to capture explosive breakdown or reversal points.
    """
    base = ((close - open).abs().rolling(60).mean())
    return _rolling_kurt(base, 126)

def swik_410_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 51 shadow wick analysis over 252d to capture explosive breakdown or reversal points.
    """
    base = ((close - open).abs().rolling(60).mean())
    return _rolling_kurt(base, 252)

def swik_411_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 51 shadow wick analysis for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = ((close - open).abs().rolling(60).mean())
    return _safe_div(base, _rolling_std(base, 5))

def swik_412_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 51 shadow wick analysis for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = ((close - open).abs().rolling(60).mean())
    return _safe_div(base, _rolling_std(base, 21))

def swik_413_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 51 shadow wick analysis for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = ((close - open).abs().rolling(60).mean())
    return _safe_div(base, _rolling_std(base, 63))

def swik_414_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 51 shadow wick analysis for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = ((close - open).abs().rolling(60).mean())
    return _safe_div(base, _rolling_std(base, 126))

def swik_415_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 51 shadow wick analysis for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = ((close - open).abs().rolling(60).mean())
    return _safe_div(base, _rolling_std(base, 252))

def swik_416_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 51 shadow wick analysis over 5d to stabilize variance and capture exponential shifts.
    """
    base = ((close - open).abs().rolling(60).mean())
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def swik_417_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 51 shadow wick analysis over 21d to stabilize variance and capture exponential shifts.
    """
    base = ((close - open).abs().rolling(60).mean())
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def swik_418_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 51 shadow wick analysis over 63d to stabilize variance and capture exponential shifts.
    """
    base = ((close - open).abs().rolling(60).mean())
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def swik_419_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 51 shadow wick analysis over 126d to stabilize variance and capture exponential shifts.
    """
    base = ((close - open).abs().rolling(60).mean())
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def swik_420_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 51 shadow wick analysis over 252d to stabilize variance and capture exponential shifts.
    """
    base = ((close - open).abs().rolling(60).mean())
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def swik_421_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 51 shadow wick analysis over a 5d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(65).mean())
    return _rolling_mean(base, 5)

def swik_422_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 51 shadow wick analysis over a 21d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(65).mean())
    return _rolling_mean(base, 21)

def swik_423_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 51 shadow wick analysis over a 63d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(65).mean())
    return _rolling_mean(base, 63)

def swik_424_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 51 shadow wick analysis over a 126d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(65).mean())
    return _rolling_mean(base, 126)

def swik_425_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 51 shadow wick analysis over a 252d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(65).mean())
    return _rolling_mean(base, 252)

def swik_426_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 51 shadow wick analysis by measuring deviations from the 5d mean.
    """
    base = ((close - open).abs().rolling(65).mean())
    return _zscore_rolling(base, 5)

def swik_427_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 51 shadow wick analysis by measuring deviations from the 21d mean.
    """
    base = ((close - open).abs().rolling(65).mean())
    return _zscore_rolling(base, 21)

def swik_428_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 51 shadow wick analysis by measuring deviations from the 63d mean.
    """
    base = ((close - open).abs().rolling(65).mean())
    return _zscore_rolling(base, 63)

def swik_429_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 51 shadow wick analysis by measuring deviations from the 126d mean.
    """
    base = ((close - open).abs().rolling(65).mean())
    return _zscore_rolling(base, 126)

def swik_430_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 51 shadow wick analysis by measuring deviations from the 252d mean.
    """
    base = ((close - open).abs().rolling(65).mean())
    return _zscore_rolling(base, 252)

def swik_431_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 51 shadow wick analysis to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = ((close - open).abs().rolling(65).mean())
    return _rank_pct(base, 5)

def swik_432_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 51 shadow wick analysis to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = ((close - open).abs().rolling(65).mean())
    return _rank_pct(base, 21)

def swik_433_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 51 shadow wick analysis to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = ((close - open).abs().rolling(65).mean())
    return _rank_pct(base, 63)

def swik_434_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 51 shadow wick analysis to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = ((close - open).abs().rolling(65).mean())
    return _rank_pct(base, 126)

def swik_435_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 51 shadow wick analysis to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = ((close - open).abs().rolling(65).mean())
    return _rank_pct(base, 252)

def swik_436_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 51 shadow wick analysis distribution over 5d to detect tail risk or exhaustion.
    """
    base = ((close - open).abs().rolling(65).mean())
    return _rolling_skew(base, 5)

def swik_437_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 51 shadow wick analysis distribution over 21d to detect tail risk or exhaustion.
    """
    base = ((close - open).abs().rolling(65).mean())
    return _rolling_skew(base, 21)

def swik_438_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 51 shadow wick analysis distribution over 63d to detect tail risk or exhaustion.
    """
    base = ((close - open).abs().rolling(65).mean())
    return _rolling_skew(base, 63)

def swik_439_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 51 shadow wick analysis distribution over 126d to detect tail risk or exhaustion.
    """
    base = ((close - open).abs().rolling(65).mean())
    return _rolling_skew(base, 126)

def swik_440_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 51 shadow wick analysis distribution over 252d to detect tail risk or exhaustion.
    """
    base = ((close - open).abs().rolling(65).mean())
    return _rolling_skew(base, 252)

def swik_441_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 51 shadow wick analysis over 5d to capture explosive breakdown or reversal points.
    """
    base = ((close - open).abs().rolling(65).mean())
    return _rolling_kurt(base, 5)

def swik_442_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 51 shadow wick analysis over 21d to capture explosive breakdown or reversal points.
    """
    base = ((close - open).abs().rolling(65).mean())
    return _rolling_kurt(base, 21)

def swik_443_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 51 shadow wick analysis over 63d to capture explosive breakdown or reversal points.
    """
    base = ((close - open).abs().rolling(65).mean())
    return _rolling_kurt(base, 63)

def swik_444_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 51 shadow wick analysis over 126d to capture explosive breakdown or reversal points.
    """
    base = ((close - open).abs().rolling(65).mean())
    return _rolling_kurt(base, 126)

def swik_445_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 51 shadow wick analysis over 252d to capture explosive breakdown or reversal points.
    """
    base = ((close - open).abs().rolling(65).mean())
    return _rolling_kurt(base, 252)

def swik_446_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 51 shadow wick analysis for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = ((close - open).abs().rolling(65).mean())
    return _safe_div(base, _rolling_std(base, 5))

def swik_447_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 51 shadow wick analysis for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = ((close - open).abs().rolling(65).mean())
    return _safe_div(base, _rolling_std(base, 21))

def swik_448_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 51 shadow wick analysis for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = ((close - open).abs().rolling(65).mean())
    return _safe_div(base, _rolling_std(base, 63))

def swik_449_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 51 shadow wick analysis for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = ((close - open).abs().rolling(65).mean())
    return _safe_div(base, _rolling_std(base, 126))

def swik_450_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 51 shadow wick analysis for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = ((close - open).abs().rolling(65).mean())
    return _safe_div(base, _rolling_std(base, 252))
