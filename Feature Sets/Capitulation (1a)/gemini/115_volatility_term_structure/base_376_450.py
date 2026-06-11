"""
115_115_volatility_term_structure — Base Features 376-450
Domain: 115_volatility_term_structure
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

def vts_376_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 115 volatility term structure for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(55).std()
    return _safe_div(base, _rolling_std(base, 5))

def vts_377_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 115 volatility term structure for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(55).std()
    return _safe_div(base, _rolling_std(base, 21))

def vts_378_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 115 volatility term structure for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(55).std()
    return _safe_div(base, _rolling_std(base, 63))

def vts_379_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 115 volatility term structure for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(55).std()
    return _safe_div(base, _rolling_std(base, 126))

def vts_380_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 115 volatility term structure for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(55).std()
    return _safe_div(base, _rolling_std(base, 252))

def vts_381_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 115 volatility term structure over 5d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(55).std()
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def vts_382_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 115 volatility term structure over 21d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(55).std()
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def vts_383_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 115 volatility term structure over 63d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(55).std()
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def vts_384_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 115 volatility term structure over 126d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(55).std()
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def vts_385_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 115 volatility term structure over 252d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(55).std()
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def vts_386_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 115 volatility term structure over a 5d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(60).std()
    return _rolling_mean(base, 5)

def vts_387_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 115 volatility term structure over a 21d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(60).std()
    return _rolling_mean(base, 21)

def vts_388_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 115 volatility term structure over a 63d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(60).std()
    return _rolling_mean(base, 63)

def vts_389_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 115 volatility term structure over a 126d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(60).std()
    return _rolling_mean(base, 126)

def vts_390_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 115 volatility term structure over a 252d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(60).std()
    return _rolling_mean(base, 252)

def vts_391_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 115 volatility term structure by measuring deviations from the 5d mean.
    """
    base = close.pct_change().rolling(60).std()
    return _zscore_rolling(base, 5)

def vts_392_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 115 volatility term structure by measuring deviations from the 21d mean.
    """
    base = close.pct_change().rolling(60).std()
    return _zscore_rolling(base, 21)

def vts_393_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 115 volatility term structure by measuring deviations from the 63d mean.
    """
    base = close.pct_change().rolling(60).std()
    return _zscore_rolling(base, 63)

def vts_394_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 115 volatility term structure by measuring deviations from the 126d mean.
    """
    base = close.pct_change().rolling(60).std()
    return _zscore_rolling(base, 126)

def vts_395_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 115 volatility term structure by measuring deviations from the 252d mean.
    """
    base = close.pct_change().rolling(60).std()
    return _zscore_rolling(base, 252)

def vts_396_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 115 volatility term structure to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(60).std()
    return _rank_pct(base, 5)

def vts_397_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 115 volatility term structure to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(60).std()
    return _rank_pct(base, 21)

def vts_398_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 115 volatility term structure to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(60).std()
    return _rank_pct(base, 63)

def vts_399_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 115 volatility term structure to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(60).std()
    return _rank_pct(base, 126)

def vts_400_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 115 volatility term structure to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(60).std()
    return _rank_pct(base, 252)

def vts_401_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 115 volatility term structure distribution over 5d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(60).std()
    return _rolling_skew(base, 5)

def vts_402_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 115 volatility term structure distribution over 21d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(60).std()
    return _rolling_skew(base, 21)

def vts_403_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 115 volatility term structure distribution over 63d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(60).std()
    return _rolling_skew(base, 63)

def vts_404_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 115 volatility term structure distribution over 126d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(60).std()
    return _rolling_skew(base, 126)

def vts_405_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 115 volatility term structure distribution over 252d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(60).std()
    return _rolling_skew(base, 252)

def vts_406_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 115 volatility term structure over 5d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(60).std()
    return _rolling_kurt(base, 5)

def vts_407_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 115 volatility term structure over 21d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(60).std()
    return _rolling_kurt(base, 21)

def vts_408_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 115 volatility term structure over 63d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(60).std()
    return _rolling_kurt(base, 63)

def vts_409_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 115 volatility term structure over 126d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(60).std()
    return _rolling_kurt(base, 126)

def vts_410_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 115 volatility term structure over 252d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(60).std()
    return _rolling_kurt(base, 252)

def vts_411_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 115 volatility term structure for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(60).std()
    return _safe_div(base, _rolling_std(base, 5))

def vts_412_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 115 volatility term structure for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(60).std()
    return _safe_div(base, _rolling_std(base, 21))

def vts_413_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 115 volatility term structure for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(60).std()
    return _safe_div(base, _rolling_std(base, 63))

def vts_414_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 115 volatility term structure for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(60).std()
    return _safe_div(base, _rolling_std(base, 126))

def vts_415_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 115 volatility term structure for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(60).std()
    return _safe_div(base, _rolling_std(base, 252))

def vts_416_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 115 volatility term structure over 5d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(60).std()
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def vts_417_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 115 volatility term structure over 21d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(60).std()
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def vts_418_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 115 volatility term structure over 63d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(60).std()
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def vts_419_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 115 volatility term structure over 126d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(60).std()
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def vts_420_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 115 volatility term structure over 252d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(60).std()
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def vts_421_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 115 volatility term structure over a 5d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(65).std()
    return _rolling_mean(base, 5)

def vts_422_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 115 volatility term structure over a 21d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(65).std()
    return _rolling_mean(base, 21)

def vts_423_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 115 volatility term structure over a 63d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(65).std()
    return _rolling_mean(base, 63)

def vts_424_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 115 volatility term structure over a 126d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(65).std()
    return _rolling_mean(base, 126)

def vts_425_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 115 volatility term structure over a 252d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(65).std()
    return _rolling_mean(base, 252)

def vts_426_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 115 volatility term structure by measuring deviations from the 5d mean.
    """
    base = close.pct_change().rolling(65).std()
    return _zscore_rolling(base, 5)

def vts_427_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 115 volatility term structure by measuring deviations from the 21d mean.
    """
    base = close.pct_change().rolling(65).std()
    return _zscore_rolling(base, 21)

def vts_428_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 115 volatility term structure by measuring deviations from the 63d mean.
    """
    base = close.pct_change().rolling(65).std()
    return _zscore_rolling(base, 63)

def vts_429_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 115 volatility term structure by measuring deviations from the 126d mean.
    """
    base = close.pct_change().rolling(65).std()
    return _zscore_rolling(base, 126)

def vts_430_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 115 volatility term structure by measuring deviations from the 252d mean.
    """
    base = close.pct_change().rolling(65).std()
    return _zscore_rolling(base, 252)

def vts_431_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 115 volatility term structure to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(65).std()
    return _rank_pct(base, 5)

def vts_432_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 115 volatility term structure to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(65).std()
    return _rank_pct(base, 21)

def vts_433_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 115 volatility term structure to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(65).std()
    return _rank_pct(base, 63)

def vts_434_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 115 volatility term structure to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(65).std()
    return _rank_pct(base, 126)

def vts_435_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 115 volatility term structure to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(65).std()
    return _rank_pct(base, 252)

def vts_436_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 115 volatility term structure distribution over 5d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(65).std()
    return _rolling_skew(base, 5)

def vts_437_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 115 volatility term structure distribution over 21d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(65).std()
    return _rolling_skew(base, 21)

def vts_438_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 115 volatility term structure distribution over 63d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(65).std()
    return _rolling_skew(base, 63)

def vts_439_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 115 volatility term structure distribution over 126d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(65).std()
    return _rolling_skew(base, 126)

def vts_440_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 115 volatility term structure distribution over 252d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(65).std()
    return _rolling_skew(base, 252)

def vts_441_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 115 volatility term structure over 5d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(65).std()
    return _rolling_kurt(base, 5)

def vts_442_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 115 volatility term structure over 21d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(65).std()
    return _rolling_kurt(base, 21)

def vts_443_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 115 volatility term structure over 63d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(65).std()
    return _rolling_kurt(base, 63)

def vts_444_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 115 volatility term structure over 126d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(65).std()
    return _rolling_kurt(base, 126)

def vts_445_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 115 volatility term structure over 252d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(65).std()
    return _rolling_kurt(base, 252)

def vts_446_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 115 volatility term structure for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(65).std()
    return _safe_div(base, _rolling_std(base, 5))

def vts_447_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 115 volatility term structure for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(65).std()
    return _safe_div(base, _rolling_std(base, 21))

def vts_448_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 115 volatility term structure for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(65).std()
    return _safe_div(base, _rolling_std(base, 63))

def vts_449_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 115 volatility term structure for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(65).std()
    return _safe_div(base, _rolling_std(base, 126))

def vts_450_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 115 volatility term structure for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(65).std()
    return _safe_div(base, _rolling_std(base, 252))
