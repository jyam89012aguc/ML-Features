"""
105_105_fractal_structure — Base Features 376-450
Domain: 105_fractal_structure
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

def frac_376_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 105 fractal structure for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = close.diff().abs().rolling(55).sum()
    return _safe_div(base, _rolling_std(base, 5))

def frac_377_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 105 fractal structure for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = close.diff().abs().rolling(55).sum()
    return _safe_div(base, _rolling_std(base, 21))

def frac_378_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 105 fractal structure for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = close.diff().abs().rolling(55).sum()
    return _safe_div(base, _rolling_std(base, 63))

def frac_379_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 105 fractal structure for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = close.diff().abs().rolling(55).sum()
    return _safe_div(base, _rolling_std(base, 126))

def frac_380_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 105 fractal structure for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = close.diff().abs().rolling(55).sum()
    return _safe_div(base, _rolling_std(base, 252))

def frac_381_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 105 fractal structure over 5d to stabilize variance and capture exponential shifts.
    """
    base = close.diff().abs().rolling(55).sum()
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def frac_382_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 105 fractal structure over 21d to stabilize variance and capture exponential shifts.
    """
    base = close.diff().abs().rolling(55).sum()
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def frac_383_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 105 fractal structure over 63d to stabilize variance and capture exponential shifts.
    """
    base = close.diff().abs().rolling(55).sum()
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def frac_384_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 105 fractal structure over 126d to stabilize variance and capture exponential shifts.
    """
    base = close.diff().abs().rolling(55).sum()
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def frac_385_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 105 fractal structure over 252d to stabilize variance and capture exponential shifts.
    """
    base = close.diff().abs().rolling(55).sum()
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def frac_386_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 105 fractal structure over a 5d horizon to identify extreme regimes.
    """
    base = close.diff().abs().rolling(60).sum()
    return _rolling_mean(base, 5)

def frac_387_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 105 fractal structure over a 21d horizon to identify extreme regimes.
    """
    base = close.diff().abs().rolling(60).sum()
    return _rolling_mean(base, 21)

def frac_388_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 105 fractal structure over a 63d horizon to identify extreme regimes.
    """
    base = close.diff().abs().rolling(60).sum()
    return _rolling_mean(base, 63)

def frac_389_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 105 fractal structure over a 126d horizon to identify extreme regimes.
    """
    base = close.diff().abs().rolling(60).sum()
    return _rolling_mean(base, 126)

def frac_390_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 105 fractal structure over a 252d horizon to identify extreme regimes.
    """
    base = close.diff().abs().rolling(60).sum()
    return _rolling_mean(base, 252)

def frac_391_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 105 fractal structure by measuring deviations from the 5d mean.
    """
    base = close.diff().abs().rolling(60).sum()
    return _zscore_rolling(base, 5)

def frac_392_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 105 fractal structure by measuring deviations from the 21d mean.
    """
    base = close.diff().abs().rolling(60).sum()
    return _zscore_rolling(base, 21)

def frac_393_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 105 fractal structure by measuring deviations from the 63d mean.
    """
    base = close.diff().abs().rolling(60).sum()
    return _zscore_rolling(base, 63)

def frac_394_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 105 fractal structure by measuring deviations from the 126d mean.
    """
    base = close.diff().abs().rolling(60).sum()
    return _zscore_rolling(base, 126)

def frac_395_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 105 fractal structure by measuring deviations from the 252d mean.
    """
    base = close.diff().abs().rolling(60).sum()
    return _zscore_rolling(base, 252)

def frac_396_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 105 fractal structure to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = close.diff().abs().rolling(60).sum()
    return _rank_pct(base, 5)

def frac_397_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 105 fractal structure to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = close.diff().abs().rolling(60).sum()
    return _rank_pct(base, 21)

def frac_398_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 105 fractal structure to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = close.diff().abs().rolling(60).sum()
    return _rank_pct(base, 63)

def frac_399_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 105 fractal structure to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = close.diff().abs().rolling(60).sum()
    return _rank_pct(base, 126)

def frac_400_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 105 fractal structure to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = close.diff().abs().rolling(60).sum()
    return _rank_pct(base, 252)

def frac_401_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 105 fractal structure distribution over 5d to detect tail risk or exhaustion.
    """
    base = close.diff().abs().rolling(60).sum()
    return _rolling_skew(base, 5)

def frac_402_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 105 fractal structure distribution over 21d to detect tail risk or exhaustion.
    """
    base = close.diff().abs().rolling(60).sum()
    return _rolling_skew(base, 21)

def frac_403_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 105 fractal structure distribution over 63d to detect tail risk or exhaustion.
    """
    base = close.diff().abs().rolling(60).sum()
    return _rolling_skew(base, 63)

def frac_404_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 105 fractal structure distribution over 126d to detect tail risk or exhaustion.
    """
    base = close.diff().abs().rolling(60).sum()
    return _rolling_skew(base, 126)

def frac_405_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 105 fractal structure distribution over 252d to detect tail risk or exhaustion.
    """
    base = close.diff().abs().rolling(60).sum()
    return _rolling_skew(base, 252)

def frac_406_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 105 fractal structure over 5d to capture explosive breakdown or reversal points.
    """
    base = close.diff().abs().rolling(60).sum()
    return _rolling_kurt(base, 5)

def frac_407_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 105 fractal structure over 21d to capture explosive breakdown or reversal points.
    """
    base = close.diff().abs().rolling(60).sum()
    return _rolling_kurt(base, 21)

def frac_408_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 105 fractal structure over 63d to capture explosive breakdown or reversal points.
    """
    base = close.diff().abs().rolling(60).sum()
    return _rolling_kurt(base, 63)

def frac_409_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 105 fractal structure over 126d to capture explosive breakdown or reversal points.
    """
    base = close.diff().abs().rolling(60).sum()
    return _rolling_kurt(base, 126)

def frac_410_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 105 fractal structure over 252d to capture explosive breakdown or reversal points.
    """
    base = close.diff().abs().rolling(60).sum()
    return _rolling_kurt(base, 252)

def frac_411_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 105 fractal structure for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = close.diff().abs().rolling(60).sum()
    return _safe_div(base, _rolling_std(base, 5))

def frac_412_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 105 fractal structure for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = close.diff().abs().rolling(60).sum()
    return _safe_div(base, _rolling_std(base, 21))

def frac_413_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 105 fractal structure for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = close.diff().abs().rolling(60).sum()
    return _safe_div(base, _rolling_std(base, 63))

def frac_414_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 105 fractal structure for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = close.diff().abs().rolling(60).sum()
    return _safe_div(base, _rolling_std(base, 126))

def frac_415_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 105 fractal structure for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = close.diff().abs().rolling(60).sum()
    return _safe_div(base, _rolling_std(base, 252))

def frac_416_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 105 fractal structure over 5d to stabilize variance and capture exponential shifts.
    """
    base = close.diff().abs().rolling(60).sum()
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def frac_417_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 105 fractal structure over 21d to stabilize variance and capture exponential shifts.
    """
    base = close.diff().abs().rolling(60).sum()
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def frac_418_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 105 fractal structure over 63d to stabilize variance and capture exponential shifts.
    """
    base = close.diff().abs().rolling(60).sum()
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def frac_419_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 105 fractal structure over 126d to stabilize variance and capture exponential shifts.
    """
    base = close.diff().abs().rolling(60).sum()
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def frac_420_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 105 fractal structure over 252d to stabilize variance and capture exponential shifts.
    """
    base = close.diff().abs().rolling(60).sum()
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def frac_421_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 105 fractal structure over a 5d horizon to identify extreme regimes.
    """
    base = close.diff().abs().rolling(65).sum()
    return _rolling_mean(base, 5)

def frac_422_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 105 fractal structure over a 21d horizon to identify extreme regimes.
    """
    base = close.diff().abs().rolling(65).sum()
    return _rolling_mean(base, 21)

def frac_423_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 105 fractal structure over a 63d horizon to identify extreme regimes.
    """
    base = close.diff().abs().rolling(65).sum()
    return _rolling_mean(base, 63)

def frac_424_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 105 fractal structure over a 126d horizon to identify extreme regimes.
    """
    base = close.diff().abs().rolling(65).sum()
    return _rolling_mean(base, 126)

def frac_425_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 105 fractal structure over a 252d horizon to identify extreme regimes.
    """
    base = close.diff().abs().rolling(65).sum()
    return _rolling_mean(base, 252)

def frac_426_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 105 fractal structure by measuring deviations from the 5d mean.
    """
    base = close.diff().abs().rolling(65).sum()
    return _zscore_rolling(base, 5)

def frac_427_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 105 fractal structure by measuring deviations from the 21d mean.
    """
    base = close.diff().abs().rolling(65).sum()
    return _zscore_rolling(base, 21)

def frac_428_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 105 fractal structure by measuring deviations from the 63d mean.
    """
    base = close.diff().abs().rolling(65).sum()
    return _zscore_rolling(base, 63)

def frac_429_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 105 fractal structure by measuring deviations from the 126d mean.
    """
    base = close.diff().abs().rolling(65).sum()
    return _zscore_rolling(base, 126)

def frac_430_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 105 fractal structure by measuring deviations from the 252d mean.
    """
    base = close.diff().abs().rolling(65).sum()
    return _zscore_rolling(base, 252)

def frac_431_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 105 fractal structure to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = close.diff().abs().rolling(65).sum()
    return _rank_pct(base, 5)

def frac_432_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 105 fractal structure to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = close.diff().abs().rolling(65).sum()
    return _rank_pct(base, 21)

def frac_433_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 105 fractal structure to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = close.diff().abs().rolling(65).sum()
    return _rank_pct(base, 63)

def frac_434_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 105 fractal structure to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = close.diff().abs().rolling(65).sum()
    return _rank_pct(base, 126)

def frac_435_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 105 fractal structure to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = close.diff().abs().rolling(65).sum()
    return _rank_pct(base, 252)

def frac_436_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 105 fractal structure distribution over 5d to detect tail risk or exhaustion.
    """
    base = close.diff().abs().rolling(65).sum()
    return _rolling_skew(base, 5)

def frac_437_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 105 fractal structure distribution over 21d to detect tail risk or exhaustion.
    """
    base = close.diff().abs().rolling(65).sum()
    return _rolling_skew(base, 21)

def frac_438_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 105 fractal structure distribution over 63d to detect tail risk or exhaustion.
    """
    base = close.diff().abs().rolling(65).sum()
    return _rolling_skew(base, 63)

def frac_439_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 105 fractal structure distribution over 126d to detect tail risk or exhaustion.
    """
    base = close.diff().abs().rolling(65).sum()
    return _rolling_skew(base, 126)

def frac_440_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 105 fractal structure distribution over 252d to detect tail risk or exhaustion.
    """
    base = close.diff().abs().rolling(65).sum()
    return _rolling_skew(base, 252)

def frac_441_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 105 fractal structure over 5d to capture explosive breakdown or reversal points.
    """
    base = close.diff().abs().rolling(65).sum()
    return _rolling_kurt(base, 5)

def frac_442_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 105 fractal structure over 21d to capture explosive breakdown or reversal points.
    """
    base = close.diff().abs().rolling(65).sum()
    return _rolling_kurt(base, 21)

def frac_443_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 105 fractal structure over 63d to capture explosive breakdown or reversal points.
    """
    base = close.diff().abs().rolling(65).sum()
    return _rolling_kurt(base, 63)

def frac_444_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 105 fractal structure over 126d to capture explosive breakdown or reversal points.
    """
    base = close.diff().abs().rolling(65).sum()
    return _rolling_kurt(base, 126)

def frac_445_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 105 fractal structure over 252d to capture explosive breakdown or reversal points.
    """
    base = close.diff().abs().rolling(65).sum()
    return _rolling_kurt(base, 252)

def frac_446_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 105 fractal structure for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = close.diff().abs().rolling(65).sum()
    return _safe_div(base, _rolling_std(base, 5))

def frac_447_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 105 fractal structure for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = close.diff().abs().rolling(65).sum()
    return _safe_div(base, _rolling_std(base, 21))

def frac_448_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 105 fractal structure for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = close.diff().abs().rolling(65).sum()
    return _safe_div(base, _rolling_std(base, 63))

def frac_449_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 105 fractal structure for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = close.diff().abs().rolling(65).sum()
    return _safe_div(base, _rolling_std(base, 126))

def frac_450_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 105 fractal structure for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = close.diff().abs().rolling(65).sum()
    return _safe_div(base, _rolling_std(base, 252))
