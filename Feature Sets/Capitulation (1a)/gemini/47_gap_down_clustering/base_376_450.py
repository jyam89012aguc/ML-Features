"""
47_47_gap_down_clustering — Base Features 376-450
Domain: 47_gap_down_clustering
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

def gapc_376_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 47 gap down clustering for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = ((close - open).abs().rolling(55).mean())
    return _safe_div(base, _rolling_std(base, 5))

def gapc_377_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 47 gap down clustering for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = ((close - open).abs().rolling(55).mean())
    return _safe_div(base, _rolling_std(base, 21))

def gapc_378_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 47 gap down clustering for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = ((close - open).abs().rolling(55).mean())
    return _safe_div(base, _rolling_std(base, 63))

def gapc_379_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 47 gap down clustering for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = ((close - open).abs().rolling(55).mean())
    return _safe_div(base, _rolling_std(base, 126))

def gapc_380_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 47 gap down clustering for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = ((close - open).abs().rolling(55).mean())
    return _safe_div(base, _rolling_std(base, 252))

def gapc_381_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 47 gap down clustering over 5d to stabilize variance and capture exponential shifts.
    """
    base = ((close - open).abs().rolling(55).mean())
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def gapc_382_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 47 gap down clustering over 21d to stabilize variance and capture exponential shifts.
    """
    base = ((close - open).abs().rolling(55).mean())
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def gapc_383_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 47 gap down clustering over 63d to stabilize variance and capture exponential shifts.
    """
    base = ((close - open).abs().rolling(55).mean())
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def gapc_384_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 47 gap down clustering over 126d to stabilize variance and capture exponential shifts.
    """
    base = ((close - open).abs().rolling(55).mean())
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def gapc_385_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 47 gap down clustering over 252d to stabilize variance and capture exponential shifts.
    """
    base = ((close - open).abs().rolling(55).mean())
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def gapc_386_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 47 gap down clustering over a 5d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(60).mean())
    return _rolling_mean(base, 5)

def gapc_387_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 47 gap down clustering over a 21d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(60).mean())
    return _rolling_mean(base, 21)

def gapc_388_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 47 gap down clustering over a 63d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(60).mean())
    return _rolling_mean(base, 63)

def gapc_389_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 47 gap down clustering over a 126d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(60).mean())
    return _rolling_mean(base, 126)

def gapc_390_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 47 gap down clustering over a 252d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(60).mean())
    return _rolling_mean(base, 252)

def gapc_391_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 47 gap down clustering by measuring deviations from the 5d mean.
    """
    base = ((close - open).abs().rolling(60).mean())
    return _zscore_rolling(base, 5)

def gapc_392_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 47 gap down clustering by measuring deviations from the 21d mean.
    """
    base = ((close - open).abs().rolling(60).mean())
    return _zscore_rolling(base, 21)

def gapc_393_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 47 gap down clustering by measuring deviations from the 63d mean.
    """
    base = ((close - open).abs().rolling(60).mean())
    return _zscore_rolling(base, 63)

def gapc_394_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 47 gap down clustering by measuring deviations from the 126d mean.
    """
    base = ((close - open).abs().rolling(60).mean())
    return _zscore_rolling(base, 126)

def gapc_395_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 47 gap down clustering by measuring deviations from the 252d mean.
    """
    base = ((close - open).abs().rolling(60).mean())
    return _zscore_rolling(base, 252)

def gapc_396_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 47 gap down clustering to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = ((close - open).abs().rolling(60).mean())
    return _rank_pct(base, 5)

def gapc_397_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 47 gap down clustering to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = ((close - open).abs().rolling(60).mean())
    return _rank_pct(base, 21)

def gapc_398_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 47 gap down clustering to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = ((close - open).abs().rolling(60).mean())
    return _rank_pct(base, 63)

def gapc_399_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 47 gap down clustering to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = ((close - open).abs().rolling(60).mean())
    return _rank_pct(base, 126)

def gapc_400_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 47 gap down clustering to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = ((close - open).abs().rolling(60).mean())
    return _rank_pct(base, 252)

def gapc_401_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 47 gap down clustering distribution over 5d to detect tail risk or exhaustion.
    """
    base = ((close - open).abs().rolling(60).mean())
    return _rolling_skew(base, 5)

def gapc_402_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 47 gap down clustering distribution over 21d to detect tail risk or exhaustion.
    """
    base = ((close - open).abs().rolling(60).mean())
    return _rolling_skew(base, 21)

def gapc_403_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 47 gap down clustering distribution over 63d to detect tail risk or exhaustion.
    """
    base = ((close - open).abs().rolling(60).mean())
    return _rolling_skew(base, 63)

def gapc_404_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 47 gap down clustering distribution over 126d to detect tail risk or exhaustion.
    """
    base = ((close - open).abs().rolling(60).mean())
    return _rolling_skew(base, 126)

def gapc_405_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 47 gap down clustering distribution over 252d to detect tail risk or exhaustion.
    """
    base = ((close - open).abs().rolling(60).mean())
    return _rolling_skew(base, 252)

def gapc_406_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 47 gap down clustering over 5d to capture explosive breakdown or reversal points.
    """
    base = ((close - open).abs().rolling(60).mean())
    return _rolling_kurt(base, 5)

def gapc_407_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 47 gap down clustering over 21d to capture explosive breakdown or reversal points.
    """
    base = ((close - open).abs().rolling(60).mean())
    return _rolling_kurt(base, 21)

def gapc_408_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 47 gap down clustering over 63d to capture explosive breakdown or reversal points.
    """
    base = ((close - open).abs().rolling(60).mean())
    return _rolling_kurt(base, 63)

def gapc_409_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 47 gap down clustering over 126d to capture explosive breakdown or reversal points.
    """
    base = ((close - open).abs().rolling(60).mean())
    return _rolling_kurt(base, 126)

def gapc_410_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 47 gap down clustering over 252d to capture explosive breakdown or reversal points.
    """
    base = ((close - open).abs().rolling(60).mean())
    return _rolling_kurt(base, 252)

def gapc_411_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 47 gap down clustering for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = ((close - open).abs().rolling(60).mean())
    return _safe_div(base, _rolling_std(base, 5))

def gapc_412_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 47 gap down clustering for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = ((close - open).abs().rolling(60).mean())
    return _safe_div(base, _rolling_std(base, 21))

def gapc_413_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 47 gap down clustering for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = ((close - open).abs().rolling(60).mean())
    return _safe_div(base, _rolling_std(base, 63))

def gapc_414_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 47 gap down clustering for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = ((close - open).abs().rolling(60).mean())
    return _safe_div(base, _rolling_std(base, 126))

def gapc_415_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 47 gap down clustering for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = ((close - open).abs().rolling(60).mean())
    return _safe_div(base, _rolling_std(base, 252))

def gapc_416_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 47 gap down clustering over 5d to stabilize variance and capture exponential shifts.
    """
    base = ((close - open).abs().rolling(60).mean())
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def gapc_417_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 47 gap down clustering over 21d to stabilize variance and capture exponential shifts.
    """
    base = ((close - open).abs().rolling(60).mean())
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def gapc_418_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 47 gap down clustering over 63d to stabilize variance and capture exponential shifts.
    """
    base = ((close - open).abs().rolling(60).mean())
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def gapc_419_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 47 gap down clustering over 126d to stabilize variance and capture exponential shifts.
    """
    base = ((close - open).abs().rolling(60).mean())
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def gapc_420_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 47 gap down clustering over 252d to stabilize variance and capture exponential shifts.
    """
    base = ((close - open).abs().rolling(60).mean())
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def gapc_421_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 47 gap down clustering over a 5d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(65).mean())
    return _rolling_mean(base, 5)

def gapc_422_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 47 gap down clustering over a 21d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(65).mean())
    return _rolling_mean(base, 21)

def gapc_423_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 47 gap down clustering over a 63d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(65).mean())
    return _rolling_mean(base, 63)

def gapc_424_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 47 gap down clustering over a 126d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(65).mean())
    return _rolling_mean(base, 126)

def gapc_425_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 47 gap down clustering over a 252d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(65).mean())
    return _rolling_mean(base, 252)

def gapc_426_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 47 gap down clustering by measuring deviations from the 5d mean.
    """
    base = ((close - open).abs().rolling(65).mean())
    return _zscore_rolling(base, 5)

def gapc_427_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 47 gap down clustering by measuring deviations from the 21d mean.
    """
    base = ((close - open).abs().rolling(65).mean())
    return _zscore_rolling(base, 21)

def gapc_428_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 47 gap down clustering by measuring deviations from the 63d mean.
    """
    base = ((close - open).abs().rolling(65).mean())
    return _zscore_rolling(base, 63)

def gapc_429_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 47 gap down clustering by measuring deviations from the 126d mean.
    """
    base = ((close - open).abs().rolling(65).mean())
    return _zscore_rolling(base, 126)

def gapc_430_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 47 gap down clustering by measuring deviations from the 252d mean.
    """
    base = ((close - open).abs().rolling(65).mean())
    return _zscore_rolling(base, 252)

def gapc_431_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 47 gap down clustering to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = ((close - open).abs().rolling(65).mean())
    return _rank_pct(base, 5)

def gapc_432_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 47 gap down clustering to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = ((close - open).abs().rolling(65).mean())
    return _rank_pct(base, 21)

def gapc_433_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 47 gap down clustering to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = ((close - open).abs().rolling(65).mean())
    return _rank_pct(base, 63)

def gapc_434_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 47 gap down clustering to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = ((close - open).abs().rolling(65).mean())
    return _rank_pct(base, 126)

def gapc_435_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 47 gap down clustering to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = ((close - open).abs().rolling(65).mean())
    return _rank_pct(base, 252)

def gapc_436_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 47 gap down clustering distribution over 5d to detect tail risk or exhaustion.
    """
    base = ((close - open).abs().rolling(65).mean())
    return _rolling_skew(base, 5)

def gapc_437_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 47 gap down clustering distribution over 21d to detect tail risk or exhaustion.
    """
    base = ((close - open).abs().rolling(65).mean())
    return _rolling_skew(base, 21)

def gapc_438_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 47 gap down clustering distribution over 63d to detect tail risk or exhaustion.
    """
    base = ((close - open).abs().rolling(65).mean())
    return _rolling_skew(base, 63)

def gapc_439_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 47 gap down clustering distribution over 126d to detect tail risk or exhaustion.
    """
    base = ((close - open).abs().rolling(65).mean())
    return _rolling_skew(base, 126)

def gapc_440_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 47 gap down clustering distribution over 252d to detect tail risk or exhaustion.
    """
    base = ((close - open).abs().rolling(65).mean())
    return _rolling_skew(base, 252)

def gapc_441_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 47 gap down clustering over 5d to capture explosive breakdown or reversal points.
    """
    base = ((close - open).abs().rolling(65).mean())
    return _rolling_kurt(base, 5)

def gapc_442_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 47 gap down clustering over 21d to capture explosive breakdown or reversal points.
    """
    base = ((close - open).abs().rolling(65).mean())
    return _rolling_kurt(base, 21)

def gapc_443_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 47 gap down clustering over 63d to capture explosive breakdown or reversal points.
    """
    base = ((close - open).abs().rolling(65).mean())
    return _rolling_kurt(base, 63)

def gapc_444_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 47 gap down clustering over 126d to capture explosive breakdown or reversal points.
    """
    base = ((close - open).abs().rolling(65).mean())
    return _rolling_kurt(base, 126)

def gapc_445_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 47 gap down clustering over 252d to capture explosive breakdown or reversal points.
    """
    base = ((close - open).abs().rolling(65).mean())
    return _rolling_kurt(base, 252)

def gapc_446_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 47 gap down clustering for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = ((close - open).abs().rolling(65).mean())
    return _safe_div(base, _rolling_std(base, 5))

def gapc_447_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 47 gap down clustering for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = ((close - open).abs().rolling(65).mean())
    return _safe_div(base, _rolling_std(base, 21))

def gapc_448_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 47 gap down clustering for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = ((close - open).abs().rolling(65).mean())
    return _safe_div(base, _rolling_std(base, 63))

def gapc_449_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 47 gap down clustering for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = ((close - open).abs().rolling(65).mean())
    return _safe_div(base, _rolling_std(base, 126))

def gapc_450_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 47 gap down clustering for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = ((close - open).abs().rolling(65).mean())
    return _safe_div(base, _rolling_std(base, 252))
