"""
109_109_return_autocorrelation — Base Features 376-450
Domain: 109_return_autocorrelation
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

def raut_376_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 109 return autocorrelation for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=11), raw=True)
    return _safe_div(base, _rolling_std(base, 5))

def raut_377_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 109 return autocorrelation for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=11), raw=True)
    return _safe_div(base, _rolling_std(base, 21))

def raut_378_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 109 return autocorrelation for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=11), raw=True)
    return _safe_div(base, _rolling_std(base, 63))

def raut_379_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 109 return autocorrelation for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=11), raw=True)
    return _safe_div(base, _rolling_std(base, 126))

def raut_380_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 109 return autocorrelation for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=11), raw=True)
    return _safe_div(base, _rolling_std(base, 252))

def raut_381_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 109 return autocorrelation over 5d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=11), raw=True)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def raut_382_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 109 return autocorrelation over 21d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=11), raw=True)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def raut_383_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 109 return autocorrelation over 63d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=11), raw=True)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def raut_384_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 109 return autocorrelation over 126d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=11), raw=True)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def raut_385_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 109 return autocorrelation over 252d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=11), raw=True)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def raut_386_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 109 return autocorrelation over a 5d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=12), raw=True)
    return _rolling_mean(base, 5)

def raut_387_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 109 return autocorrelation over a 21d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=12), raw=True)
    return _rolling_mean(base, 21)

def raut_388_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 109 return autocorrelation over a 63d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=12), raw=True)
    return _rolling_mean(base, 63)

def raut_389_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 109 return autocorrelation over a 126d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=12), raw=True)
    return _rolling_mean(base, 126)

def raut_390_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 109 return autocorrelation over a 252d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=12), raw=True)
    return _rolling_mean(base, 252)

def raut_391_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 109 return autocorrelation by measuring deviations from the 5d mean.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=12), raw=True)
    return _zscore_rolling(base, 5)

def raut_392_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 109 return autocorrelation by measuring deviations from the 21d mean.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=12), raw=True)
    return _zscore_rolling(base, 21)

def raut_393_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 109 return autocorrelation by measuring deviations from the 63d mean.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=12), raw=True)
    return _zscore_rolling(base, 63)

def raut_394_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 109 return autocorrelation by measuring deviations from the 126d mean.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=12), raw=True)
    return _zscore_rolling(base, 126)

def raut_395_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 109 return autocorrelation by measuring deviations from the 252d mean.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=12), raw=True)
    return _zscore_rolling(base, 252)

def raut_396_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 109 return autocorrelation to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=12), raw=True)
    return _rank_pct(base, 5)

def raut_397_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 109 return autocorrelation to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=12), raw=True)
    return _rank_pct(base, 21)

def raut_398_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 109 return autocorrelation to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=12), raw=True)
    return _rank_pct(base, 63)

def raut_399_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 109 return autocorrelation to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=12), raw=True)
    return _rank_pct(base, 126)

def raut_400_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 109 return autocorrelation to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=12), raw=True)
    return _rank_pct(base, 252)

def raut_401_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 109 return autocorrelation distribution over 5d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=12), raw=True)
    return _rolling_skew(base, 5)

def raut_402_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 109 return autocorrelation distribution over 21d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=12), raw=True)
    return _rolling_skew(base, 21)

def raut_403_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 109 return autocorrelation distribution over 63d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=12), raw=True)
    return _rolling_skew(base, 63)

def raut_404_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 109 return autocorrelation distribution over 126d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=12), raw=True)
    return _rolling_skew(base, 126)

def raut_405_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 109 return autocorrelation distribution over 252d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=12), raw=True)
    return _rolling_skew(base, 252)

def raut_406_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 109 return autocorrelation over 5d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=12), raw=True)
    return _rolling_kurt(base, 5)

def raut_407_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 109 return autocorrelation over 21d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=12), raw=True)
    return _rolling_kurt(base, 21)

def raut_408_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 109 return autocorrelation over 63d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=12), raw=True)
    return _rolling_kurt(base, 63)

def raut_409_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 109 return autocorrelation over 126d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=12), raw=True)
    return _rolling_kurt(base, 126)

def raut_410_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 109 return autocorrelation over 252d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=12), raw=True)
    return _rolling_kurt(base, 252)

def raut_411_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 109 return autocorrelation for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=12), raw=True)
    return _safe_div(base, _rolling_std(base, 5))

def raut_412_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 109 return autocorrelation for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=12), raw=True)
    return _safe_div(base, _rolling_std(base, 21))

def raut_413_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 109 return autocorrelation for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=12), raw=True)
    return _safe_div(base, _rolling_std(base, 63))

def raut_414_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 109 return autocorrelation for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=12), raw=True)
    return _safe_div(base, _rolling_std(base, 126))

def raut_415_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 109 return autocorrelation for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=12), raw=True)
    return _safe_div(base, _rolling_std(base, 252))

def raut_416_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 109 return autocorrelation over 5d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=12), raw=True)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def raut_417_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 109 return autocorrelation over 21d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=12), raw=True)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def raut_418_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 109 return autocorrelation over 63d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=12), raw=True)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def raut_419_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 109 return autocorrelation over 126d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=12), raw=True)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def raut_420_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 109 return autocorrelation over 252d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=12), raw=True)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def raut_421_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 109 return autocorrelation over a 5d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=13), raw=True)
    return _rolling_mean(base, 5)

def raut_422_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 109 return autocorrelation over a 21d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=13), raw=True)
    return _rolling_mean(base, 21)

def raut_423_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 109 return autocorrelation over a 63d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=13), raw=True)
    return _rolling_mean(base, 63)

def raut_424_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 109 return autocorrelation over a 126d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=13), raw=True)
    return _rolling_mean(base, 126)

def raut_425_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 109 return autocorrelation over a 252d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=13), raw=True)
    return _rolling_mean(base, 252)

def raut_426_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 109 return autocorrelation by measuring deviations from the 5d mean.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=13), raw=True)
    return _zscore_rolling(base, 5)

def raut_427_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 109 return autocorrelation by measuring deviations from the 21d mean.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=13), raw=True)
    return _zscore_rolling(base, 21)

def raut_428_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 109 return autocorrelation by measuring deviations from the 63d mean.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=13), raw=True)
    return _zscore_rolling(base, 63)

def raut_429_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 109 return autocorrelation by measuring deviations from the 126d mean.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=13), raw=True)
    return _zscore_rolling(base, 126)

def raut_430_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 109 return autocorrelation by measuring deviations from the 252d mean.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=13), raw=True)
    return _zscore_rolling(base, 252)

def raut_431_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 109 return autocorrelation to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=13), raw=True)
    return _rank_pct(base, 5)

def raut_432_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 109 return autocorrelation to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=13), raw=True)
    return _rank_pct(base, 21)

def raut_433_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 109 return autocorrelation to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=13), raw=True)
    return _rank_pct(base, 63)

def raut_434_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 109 return autocorrelation to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=13), raw=True)
    return _rank_pct(base, 126)

def raut_435_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 109 return autocorrelation to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=13), raw=True)
    return _rank_pct(base, 252)

def raut_436_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 109 return autocorrelation distribution over 5d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=13), raw=True)
    return _rolling_skew(base, 5)

def raut_437_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 109 return autocorrelation distribution over 21d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=13), raw=True)
    return _rolling_skew(base, 21)

def raut_438_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 109 return autocorrelation distribution over 63d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=13), raw=True)
    return _rolling_skew(base, 63)

def raut_439_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 109 return autocorrelation distribution over 126d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=13), raw=True)
    return _rolling_skew(base, 126)

def raut_440_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 109 return autocorrelation distribution over 252d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=13), raw=True)
    return _rolling_skew(base, 252)

def raut_441_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 109 return autocorrelation over 5d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=13), raw=True)
    return _rolling_kurt(base, 5)

def raut_442_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 109 return autocorrelation over 21d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=13), raw=True)
    return _rolling_kurt(base, 21)

def raut_443_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 109 return autocorrelation over 63d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=13), raw=True)
    return _rolling_kurt(base, 63)

def raut_444_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 109 return autocorrelation over 126d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=13), raw=True)
    return _rolling_kurt(base, 126)

def raut_445_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 109 return autocorrelation over 252d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=13), raw=True)
    return _rolling_kurt(base, 252)

def raut_446_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 109 return autocorrelation for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=13), raw=True)
    return _safe_div(base, _rolling_std(base, 5))

def raut_447_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 109 return autocorrelation for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=13), raw=True)
    return _safe_div(base, _rolling_std(base, 21))

def raut_448_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 109 return autocorrelation for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=13), raw=True)
    return _safe_div(base, _rolling_std(base, 63))

def raut_449_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 109 return autocorrelation for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=13), raw=True)
    return _safe_div(base, _rolling_std(base, 126))

def raut_450_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 109 return autocorrelation for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=13), raw=True)
    return _safe_div(base, _rolling_std(base, 252))
