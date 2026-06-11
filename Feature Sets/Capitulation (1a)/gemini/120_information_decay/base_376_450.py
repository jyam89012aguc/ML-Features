"""
120_120_information_decay — Base Features 376-450
Domain: 120_information_decay
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

def idec_376_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 120 information decay for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = close.diff().abs().rolling(55).sum()
    return _safe_div(base, _rolling_std(base, 5))

def idec_377_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 120 information decay for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = close.diff().abs().rolling(55).sum()
    return _safe_div(base, _rolling_std(base, 21))

def idec_378_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 120 information decay for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = close.diff().abs().rolling(55).sum()
    return _safe_div(base, _rolling_std(base, 63))

def idec_379_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 120 information decay for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = close.diff().abs().rolling(55).sum()
    return _safe_div(base, _rolling_std(base, 126))

def idec_380_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 120 information decay for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = close.diff().abs().rolling(55).sum()
    return _safe_div(base, _rolling_std(base, 252))

def idec_381_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 120 information decay over 5d to stabilize variance and capture exponential shifts.
    """
    base = close.diff().abs().rolling(55).sum()
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def idec_382_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 120 information decay over 21d to stabilize variance and capture exponential shifts.
    """
    base = close.diff().abs().rolling(55).sum()
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def idec_383_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 120 information decay over 63d to stabilize variance and capture exponential shifts.
    """
    base = close.diff().abs().rolling(55).sum()
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def idec_384_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 120 information decay over 126d to stabilize variance and capture exponential shifts.
    """
    base = close.diff().abs().rolling(55).sum()
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def idec_385_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 120 information decay over 252d to stabilize variance and capture exponential shifts.
    """
    base = close.diff().abs().rolling(55).sum()
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def idec_386_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 120 information decay over a 5d horizon to identify extreme regimes.
    """
    base = close.diff().abs().rolling(60).sum()
    return _rolling_mean(base, 5)

def idec_387_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 120 information decay over a 21d horizon to identify extreme regimes.
    """
    base = close.diff().abs().rolling(60).sum()
    return _rolling_mean(base, 21)

def idec_388_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 120 information decay over a 63d horizon to identify extreme regimes.
    """
    base = close.diff().abs().rolling(60).sum()
    return _rolling_mean(base, 63)

def idec_389_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 120 information decay over a 126d horizon to identify extreme regimes.
    """
    base = close.diff().abs().rolling(60).sum()
    return _rolling_mean(base, 126)

def idec_390_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 120 information decay over a 252d horizon to identify extreme regimes.
    """
    base = close.diff().abs().rolling(60).sum()
    return _rolling_mean(base, 252)

def idec_391_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 120 information decay by measuring deviations from the 5d mean.
    """
    base = close.diff().abs().rolling(60).sum()
    return _zscore_rolling(base, 5)

def idec_392_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 120 information decay by measuring deviations from the 21d mean.
    """
    base = close.diff().abs().rolling(60).sum()
    return _zscore_rolling(base, 21)

def idec_393_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 120 information decay by measuring deviations from the 63d mean.
    """
    base = close.diff().abs().rolling(60).sum()
    return _zscore_rolling(base, 63)

def idec_394_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 120 information decay by measuring deviations from the 126d mean.
    """
    base = close.diff().abs().rolling(60).sum()
    return _zscore_rolling(base, 126)

def idec_395_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 120 information decay by measuring deviations from the 252d mean.
    """
    base = close.diff().abs().rolling(60).sum()
    return _zscore_rolling(base, 252)

def idec_396_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 120 information decay to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = close.diff().abs().rolling(60).sum()
    return _rank_pct(base, 5)

def idec_397_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 120 information decay to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = close.diff().abs().rolling(60).sum()
    return _rank_pct(base, 21)

def idec_398_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 120 information decay to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = close.diff().abs().rolling(60).sum()
    return _rank_pct(base, 63)

def idec_399_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 120 information decay to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = close.diff().abs().rolling(60).sum()
    return _rank_pct(base, 126)

def idec_400_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 120 information decay to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = close.diff().abs().rolling(60).sum()
    return _rank_pct(base, 252)

def idec_401_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 120 information decay distribution over 5d to detect tail risk or exhaustion.
    """
    base = close.diff().abs().rolling(60).sum()
    return _rolling_skew(base, 5)

def idec_402_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 120 information decay distribution over 21d to detect tail risk or exhaustion.
    """
    base = close.diff().abs().rolling(60).sum()
    return _rolling_skew(base, 21)

def idec_403_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 120 information decay distribution over 63d to detect tail risk or exhaustion.
    """
    base = close.diff().abs().rolling(60).sum()
    return _rolling_skew(base, 63)

def idec_404_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 120 information decay distribution over 126d to detect tail risk or exhaustion.
    """
    base = close.diff().abs().rolling(60).sum()
    return _rolling_skew(base, 126)

def idec_405_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 120 information decay distribution over 252d to detect tail risk or exhaustion.
    """
    base = close.diff().abs().rolling(60).sum()
    return _rolling_skew(base, 252)

def idec_406_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 120 information decay over 5d to capture explosive breakdown or reversal points.
    """
    base = close.diff().abs().rolling(60).sum()
    return _rolling_kurt(base, 5)

def idec_407_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 120 information decay over 21d to capture explosive breakdown or reversal points.
    """
    base = close.diff().abs().rolling(60).sum()
    return _rolling_kurt(base, 21)

def idec_408_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 120 information decay over 63d to capture explosive breakdown or reversal points.
    """
    base = close.diff().abs().rolling(60).sum()
    return _rolling_kurt(base, 63)

def idec_409_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 120 information decay over 126d to capture explosive breakdown or reversal points.
    """
    base = close.diff().abs().rolling(60).sum()
    return _rolling_kurt(base, 126)

def idec_410_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 120 information decay over 252d to capture explosive breakdown or reversal points.
    """
    base = close.diff().abs().rolling(60).sum()
    return _rolling_kurt(base, 252)

def idec_411_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 120 information decay for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = close.diff().abs().rolling(60).sum()
    return _safe_div(base, _rolling_std(base, 5))

def idec_412_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 120 information decay for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = close.diff().abs().rolling(60).sum()
    return _safe_div(base, _rolling_std(base, 21))

def idec_413_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 120 information decay for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = close.diff().abs().rolling(60).sum()
    return _safe_div(base, _rolling_std(base, 63))

def idec_414_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 120 information decay for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = close.diff().abs().rolling(60).sum()
    return _safe_div(base, _rolling_std(base, 126))

def idec_415_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 120 information decay for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = close.diff().abs().rolling(60).sum()
    return _safe_div(base, _rolling_std(base, 252))

def idec_416_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 120 information decay over 5d to stabilize variance and capture exponential shifts.
    """
    base = close.diff().abs().rolling(60).sum()
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def idec_417_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 120 information decay over 21d to stabilize variance and capture exponential shifts.
    """
    base = close.diff().abs().rolling(60).sum()
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def idec_418_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 120 information decay over 63d to stabilize variance and capture exponential shifts.
    """
    base = close.diff().abs().rolling(60).sum()
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def idec_419_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 120 information decay over 126d to stabilize variance and capture exponential shifts.
    """
    base = close.diff().abs().rolling(60).sum()
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def idec_420_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 120 information decay over 252d to stabilize variance and capture exponential shifts.
    """
    base = close.diff().abs().rolling(60).sum()
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def idec_421_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 120 information decay over a 5d horizon to identify extreme regimes.
    """
    base = close.diff().abs().rolling(65).sum()
    return _rolling_mean(base, 5)

def idec_422_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 120 information decay over a 21d horizon to identify extreme regimes.
    """
    base = close.diff().abs().rolling(65).sum()
    return _rolling_mean(base, 21)

def idec_423_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 120 information decay over a 63d horizon to identify extreme regimes.
    """
    base = close.diff().abs().rolling(65).sum()
    return _rolling_mean(base, 63)

def idec_424_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 120 information decay over a 126d horizon to identify extreme regimes.
    """
    base = close.diff().abs().rolling(65).sum()
    return _rolling_mean(base, 126)

def idec_425_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 120 information decay over a 252d horizon to identify extreme regimes.
    """
    base = close.diff().abs().rolling(65).sum()
    return _rolling_mean(base, 252)

def idec_426_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 120 information decay by measuring deviations from the 5d mean.
    """
    base = close.diff().abs().rolling(65).sum()
    return _zscore_rolling(base, 5)

def idec_427_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 120 information decay by measuring deviations from the 21d mean.
    """
    base = close.diff().abs().rolling(65).sum()
    return _zscore_rolling(base, 21)

def idec_428_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 120 information decay by measuring deviations from the 63d mean.
    """
    base = close.diff().abs().rolling(65).sum()
    return _zscore_rolling(base, 63)

def idec_429_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 120 information decay by measuring deviations from the 126d mean.
    """
    base = close.diff().abs().rolling(65).sum()
    return _zscore_rolling(base, 126)

def idec_430_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 120 information decay by measuring deviations from the 252d mean.
    """
    base = close.diff().abs().rolling(65).sum()
    return _zscore_rolling(base, 252)

def idec_431_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 120 information decay to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = close.diff().abs().rolling(65).sum()
    return _rank_pct(base, 5)

def idec_432_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 120 information decay to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = close.diff().abs().rolling(65).sum()
    return _rank_pct(base, 21)

def idec_433_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 120 information decay to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = close.diff().abs().rolling(65).sum()
    return _rank_pct(base, 63)

def idec_434_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 120 information decay to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = close.diff().abs().rolling(65).sum()
    return _rank_pct(base, 126)

def idec_435_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 120 information decay to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = close.diff().abs().rolling(65).sum()
    return _rank_pct(base, 252)

def idec_436_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 120 information decay distribution over 5d to detect tail risk or exhaustion.
    """
    base = close.diff().abs().rolling(65).sum()
    return _rolling_skew(base, 5)

def idec_437_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 120 information decay distribution over 21d to detect tail risk or exhaustion.
    """
    base = close.diff().abs().rolling(65).sum()
    return _rolling_skew(base, 21)

def idec_438_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 120 information decay distribution over 63d to detect tail risk or exhaustion.
    """
    base = close.diff().abs().rolling(65).sum()
    return _rolling_skew(base, 63)

def idec_439_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 120 information decay distribution over 126d to detect tail risk or exhaustion.
    """
    base = close.diff().abs().rolling(65).sum()
    return _rolling_skew(base, 126)

def idec_440_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 120 information decay distribution over 252d to detect tail risk or exhaustion.
    """
    base = close.diff().abs().rolling(65).sum()
    return _rolling_skew(base, 252)

def idec_441_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 120 information decay over 5d to capture explosive breakdown or reversal points.
    """
    base = close.diff().abs().rolling(65).sum()
    return _rolling_kurt(base, 5)

def idec_442_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 120 information decay over 21d to capture explosive breakdown or reversal points.
    """
    base = close.diff().abs().rolling(65).sum()
    return _rolling_kurt(base, 21)

def idec_443_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 120 information decay over 63d to capture explosive breakdown or reversal points.
    """
    base = close.diff().abs().rolling(65).sum()
    return _rolling_kurt(base, 63)

def idec_444_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 120 information decay over 126d to capture explosive breakdown or reversal points.
    """
    base = close.diff().abs().rolling(65).sum()
    return _rolling_kurt(base, 126)

def idec_445_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 120 information decay over 252d to capture explosive breakdown or reversal points.
    """
    base = close.diff().abs().rolling(65).sum()
    return _rolling_kurt(base, 252)

def idec_446_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 120 information decay for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = close.diff().abs().rolling(65).sum()
    return _safe_div(base, _rolling_std(base, 5))

def idec_447_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 120 information decay for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = close.diff().abs().rolling(65).sum()
    return _safe_div(base, _rolling_std(base, 21))

def idec_448_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 120 information decay for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = close.diff().abs().rolling(65).sum()
    return _safe_div(base, _rolling_std(base, 63))

def idec_449_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 120 information decay for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = close.diff().abs().rolling(65).sum()
    return _safe_div(base, _rolling_std(base, 126))

def idec_450_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 120 information decay for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = close.diff().abs().rolling(65).sum()
    return _safe_div(base, _rolling_std(base, 252))
