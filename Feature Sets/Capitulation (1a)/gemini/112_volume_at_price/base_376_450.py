"""
112_112_volume_at_price — Base Features 376-450
Domain: 112_volume_at_price
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

def vapr_376_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 112 volume at price for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = volume * close.pct_change(11)
    return _safe_div(base, _rolling_std(base, 5))

def vapr_377_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 112 volume at price for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = volume * close.pct_change(11)
    return _safe_div(base, _rolling_std(base, 21))

def vapr_378_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 112 volume at price for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = volume * close.pct_change(11)
    return _safe_div(base, _rolling_std(base, 63))

def vapr_379_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 112 volume at price for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = volume * close.pct_change(11)
    return _safe_div(base, _rolling_std(base, 126))

def vapr_380_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 112 volume at price for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = volume * close.pct_change(11)
    return _safe_div(base, _rolling_std(base, 252))

def vapr_381_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 112 volume at price over 5d to stabilize variance and capture exponential shifts.
    """
    base = volume * close.pct_change(11)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def vapr_382_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 112 volume at price over 21d to stabilize variance and capture exponential shifts.
    """
    base = volume * close.pct_change(11)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def vapr_383_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 112 volume at price over 63d to stabilize variance and capture exponential shifts.
    """
    base = volume * close.pct_change(11)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def vapr_384_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 112 volume at price over 126d to stabilize variance and capture exponential shifts.
    """
    base = volume * close.pct_change(11)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def vapr_385_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 112 volume at price over 252d to stabilize variance and capture exponential shifts.
    """
    base = volume * close.pct_change(11)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def vapr_386_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 112 volume at price over a 5d horizon to identify extreme regimes.
    """
    base = volume * close.pct_change(12)
    return _rolling_mean(base, 5)

def vapr_387_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 112 volume at price over a 21d horizon to identify extreme regimes.
    """
    base = volume * close.pct_change(12)
    return _rolling_mean(base, 21)

def vapr_388_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 112 volume at price over a 63d horizon to identify extreme regimes.
    """
    base = volume * close.pct_change(12)
    return _rolling_mean(base, 63)

def vapr_389_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 112 volume at price over a 126d horizon to identify extreme regimes.
    """
    base = volume * close.pct_change(12)
    return _rolling_mean(base, 126)

def vapr_390_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 112 volume at price over a 252d horizon to identify extreme regimes.
    """
    base = volume * close.pct_change(12)
    return _rolling_mean(base, 252)

def vapr_391_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 112 volume at price by measuring deviations from the 5d mean.
    """
    base = volume * close.pct_change(12)
    return _zscore_rolling(base, 5)

def vapr_392_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 112 volume at price by measuring deviations from the 21d mean.
    """
    base = volume * close.pct_change(12)
    return _zscore_rolling(base, 21)

def vapr_393_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 112 volume at price by measuring deviations from the 63d mean.
    """
    base = volume * close.pct_change(12)
    return _zscore_rolling(base, 63)

def vapr_394_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 112 volume at price by measuring deviations from the 126d mean.
    """
    base = volume * close.pct_change(12)
    return _zscore_rolling(base, 126)

def vapr_395_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 112 volume at price by measuring deviations from the 252d mean.
    """
    base = volume * close.pct_change(12)
    return _zscore_rolling(base, 252)

def vapr_396_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 112 volume at price to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = volume * close.pct_change(12)
    return _rank_pct(base, 5)

def vapr_397_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 112 volume at price to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = volume * close.pct_change(12)
    return _rank_pct(base, 21)

def vapr_398_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 112 volume at price to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = volume * close.pct_change(12)
    return _rank_pct(base, 63)

def vapr_399_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 112 volume at price to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = volume * close.pct_change(12)
    return _rank_pct(base, 126)

def vapr_400_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 112 volume at price to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = volume * close.pct_change(12)
    return _rank_pct(base, 252)

def vapr_401_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 112 volume at price distribution over 5d to detect tail risk or exhaustion.
    """
    base = volume * close.pct_change(12)
    return _rolling_skew(base, 5)

def vapr_402_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 112 volume at price distribution over 21d to detect tail risk or exhaustion.
    """
    base = volume * close.pct_change(12)
    return _rolling_skew(base, 21)

def vapr_403_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 112 volume at price distribution over 63d to detect tail risk or exhaustion.
    """
    base = volume * close.pct_change(12)
    return _rolling_skew(base, 63)

def vapr_404_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 112 volume at price distribution over 126d to detect tail risk or exhaustion.
    """
    base = volume * close.pct_change(12)
    return _rolling_skew(base, 126)

def vapr_405_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 112 volume at price distribution over 252d to detect tail risk or exhaustion.
    """
    base = volume * close.pct_change(12)
    return _rolling_skew(base, 252)

def vapr_406_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 112 volume at price over 5d to capture explosive breakdown or reversal points.
    """
    base = volume * close.pct_change(12)
    return _rolling_kurt(base, 5)

def vapr_407_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 112 volume at price over 21d to capture explosive breakdown or reversal points.
    """
    base = volume * close.pct_change(12)
    return _rolling_kurt(base, 21)

def vapr_408_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 112 volume at price over 63d to capture explosive breakdown or reversal points.
    """
    base = volume * close.pct_change(12)
    return _rolling_kurt(base, 63)

def vapr_409_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 112 volume at price over 126d to capture explosive breakdown or reversal points.
    """
    base = volume * close.pct_change(12)
    return _rolling_kurt(base, 126)

def vapr_410_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 112 volume at price over 252d to capture explosive breakdown or reversal points.
    """
    base = volume * close.pct_change(12)
    return _rolling_kurt(base, 252)

def vapr_411_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 112 volume at price for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = volume * close.pct_change(12)
    return _safe_div(base, _rolling_std(base, 5))

def vapr_412_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 112 volume at price for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = volume * close.pct_change(12)
    return _safe_div(base, _rolling_std(base, 21))

def vapr_413_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 112 volume at price for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = volume * close.pct_change(12)
    return _safe_div(base, _rolling_std(base, 63))

def vapr_414_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 112 volume at price for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = volume * close.pct_change(12)
    return _safe_div(base, _rolling_std(base, 126))

def vapr_415_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 112 volume at price for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = volume * close.pct_change(12)
    return _safe_div(base, _rolling_std(base, 252))

def vapr_416_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 112 volume at price over 5d to stabilize variance and capture exponential shifts.
    """
    base = volume * close.pct_change(12)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def vapr_417_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 112 volume at price over 21d to stabilize variance and capture exponential shifts.
    """
    base = volume * close.pct_change(12)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def vapr_418_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 112 volume at price over 63d to stabilize variance and capture exponential shifts.
    """
    base = volume * close.pct_change(12)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def vapr_419_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 112 volume at price over 126d to stabilize variance and capture exponential shifts.
    """
    base = volume * close.pct_change(12)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def vapr_420_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 112 volume at price over 252d to stabilize variance and capture exponential shifts.
    """
    base = volume * close.pct_change(12)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def vapr_421_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 112 volume at price over a 5d horizon to identify extreme regimes.
    """
    base = volume * close.pct_change(13)
    return _rolling_mean(base, 5)

def vapr_422_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 112 volume at price over a 21d horizon to identify extreme regimes.
    """
    base = volume * close.pct_change(13)
    return _rolling_mean(base, 21)

def vapr_423_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 112 volume at price over a 63d horizon to identify extreme regimes.
    """
    base = volume * close.pct_change(13)
    return _rolling_mean(base, 63)

def vapr_424_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 112 volume at price over a 126d horizon to identify extreme regimes.
    """
    base = volume * close.pct_change(13)
    return _rolling_mean(base, 126)

def vapr_425_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 112 volume at price over a 252d horizon to identify extreme regimes.
    """
    base = volume * close.pct_change(13)
    return _rolling_mean(base, 252)

def vapr_426_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 112 volume at price by measuring deviations from the 5d mean.
    """
    base = volume * close.pct_change(13)
    return _zscore_rolling(base, 5)

def vapr_427_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 112 volume at price by measuring deviations from the 21d mean.
    """
    base = volume * close.pct_change(13)
    return _zscore_rolling(base, 21)

def vapr_428_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 112 volume at price by measuring deviations from the 63d mean.
    """
    base = volume * close.pct_change(13)
    return _zscore_rolling(base, 63)

def vapr_429_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 112 volume at price by measuring deviations from the 126d mean.
    """
    base = volume * close.pct_change(13)
    return _zscore_rolling(base, 126)

def vapr_430_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 112 volume at price by measuring deviations from the 252d mean.
    """
    base = volume * close.pct_change(13)
    return _zscore_rolling(base, 252)

def vapr_431_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 112 volume at price to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = volume * close.pct_change(13)
    return _rank_pct(base, 5)

def vapr_432_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 112 volume at price to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = volume * close.pct_change(13)
    return _rank_pct(base, 21)

def vapr_433_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 112 volume at price to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = volume * close.pct_change(13)
    return _rank_pct(base, 63)

def vapr_434_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 112 volume at price to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = volume * close.pct_change(13)
    return _rank_pct(base, 126)

def vapr_435_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 112 volume at price to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = volume * close.pct_change(13)
    return _rank_pct(base, 252)

def vapr_436_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 112 volume at price distribution over 5d to detect tail risk or exhaustion.
    """
    base = volume * close.pct_change(13)
    return _rolling_skew(base, 5)

def vapr_437_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 112 volume at price distribution over 21d to detect tail risk or exhaustion.
    """
    base = volume * close.pct_change(13)
    return _rolling_skew(base, 21)

def vapr_438_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 112 volume at price distribution over 63d to detect tail risk or exhaustion.
    """
    base = volume * close.pct_change(13)
    return _rolling_skew(base, 63)

def vapr_439_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 112 volume at price distribution over 126d to detect tail risk or exhaustion.
    """
    base = volume * close.pct_change(13)
    return _rolling_skew(base, 126)

def vapr_440_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 112 volume at price distribution over 252d to detect tail risk or exhaustion.
    """
    base = volume * close.pct_change(13)
    return _rolling_skew(base, 252)

def vapr_441_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 112 volume at price over 5d to capture explosive breakdown or reversal points.
    """
    base = volume * close.pct_change(13)
    return _rolling_kurt(base, 5)

def vapr_442_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 112 volume at price over 21d to capture explosive breakdown or reversal points.
    """
    base = volume * close.pct_change(13)
    return _rolling_kurt(base, 21)

def vapr_443_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 112 volume at price over 63d to capture explosive breakdown or reversal points.
    """
    base = volume * close.pct_change(13)
    return _rolling_kurt(base, 63)

def vapr_444_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 112 volume at price over 126d to capture explosive breakdown or reversal points.
    """
    base = volume * close.pct_change(13)
    return _rolling_kurt(base, 126)

def vapr_445_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 112 volume at price over 252d to capture explosive breakdown or reversal points.
    """
    base = volume * close.pct_change(13)
    return _rolling_kurt(base, 252)

def vapr_446_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 112 volume at price for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = volume * close.pct_change(13)
    return _safe_div(base, _rolling_std(base, 5))

def vapr_447_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 112 volume at price for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = volume * close.pct_change(13)
    return _safe_div(base, _rolling_std(base, 21))

def vapr_448_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 112 volume at price for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = volume * close.pct_change(13)
    return _safe_div(base, _rolling_std(base, 63))

def vapr_449_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 112 volume at price for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = volume * close.pct_change(13)
    return _safe_div(base, _rolling_std(base, 126))

def vapr_450_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 112 volume at price for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = volume * close.pct_change(13)
    return _safe_div(base, _rolling_std(base, 252))
