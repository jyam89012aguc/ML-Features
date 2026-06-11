"""
28_28_return_distribution — Base Features 301-375
Domain: 28_return_distribution
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

def rdis_301_kurt_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 28 return distribution over 5d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(9).rolling(45).mean())
    return _rolling_kurt(base, 5)

def rdis_302_kurt_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 28 return distribution over 21d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(9).rolling(45).mean())
    return _rolling_kurt(base, 21)

def rdis_303_kurt_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 28 return distribution over 63d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(9).rolling(45).mean())
    return _rolling_kurt(base, 63)

def rdis_304_kurt_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 28 return distribution over 126d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(9).rolling(45).mean())
    return _rolling_kurt(base, 126)

def rdis_305_kurt_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 28 return distribution over 252d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(9).rolling(45).mean())
    return _rolling_kurt(base, 252)

def rdis_306_voladj_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 28 return distribution for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(9).rolling(45).mean())
    return _safe_div(base, _rolling_std(base, 5))

def rdis_307_voladj_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 28 return distribution for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(9).rolling(45).mean())
    return _safe_div(base, _rolling_std(base, 21))

def rdis_308_voladj_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 28 return distribution for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(9).rolling(45).mean())
    return _safe_div(base, _rolling_std(base, 63))

def rdis_309_voladj_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 28 return distribution for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(9).rolling(45).mean())
    return _safe_div(base, _rolling_std(base, 126))

def rdis_310_voladj_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 28 return distribution for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(9).rolling(45).mean())
    return _safe_div(base, _rolling_std(base, 252))

def rdis_311_lognorm_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 28 return distribution over 5d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(9).rolling(45).mean())
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def rdis_312_lognorm_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 28 return distribution over 21d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(9).rolling(45).mean())
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def rdis_313_lognorm_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 28 return distribution over 63d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(9).rolling(45).mean())
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def rdis_314_lognorm_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 28 return distribution over 126d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(9).rolling(45).mean())
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def rdis_315_lognorm_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 28 return distribution over 252d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(9).rolling(45).mean())
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def rdis_316_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 28 return distribution over a 5d horizon to identify extreme regimes.
    """
    base = (close.pct_change(10).rolling(50).mean())
    return _rolling_mean(base, 5)

def rdis_317_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 28 return distribution over a 21d horizon to identify extreme regimes.
    """
    base = (close.pct_change(10).rolling(50).mean())
    return _rolling_mean(base, 21)

def rdis_318_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 28 return distribution over a 63d horizon to identify extreme regimes.
    """
    base = (close.pct_change(10).rolling(50).mean())
    return _rolling_mean(base, 63)

def rdis_319_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 28 return distribution over a 126d horizon to identify extreme regimes.
    """
    base = (close.pct_change(10).rolling(50).mean())
    return _rolling_mean(base, 126)

def rdis_320_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 28 return distribution over a 252d horizon to identify extreme regimes.
    """
    base = (close.pct_change(10).rolling(50).mean())
    return _rolling_mean(base, 252)

def rdis_321_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 28 return distribution by measuring deviations from the 5d mean.
    """
    base = (close.pct_change(10).rolling(50).mean())
    return _zscore_rolling(base, 5)

def rdis_322_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 28 return distribution by measuring deviations from the 21d mean.
    """
    base = (close.pct_change(10).rolling(50).mean())
    return _zscore_rolling(base, 21)

def rdis_323_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 28 return distribution by measuring deviations from the 63d mean.
    """
    base = (close.pct_change(10).rolling(50).mean())
    return _zscore_rolling(base, 63)

def rdis_324_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 28 return distribution by measuring deviations from the 126d mean.
    """
    base = (close.pct_change(10).rolling(50).mean())
    return _zscore_rolling(base, 126)

def rdis_325_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 28 return distribution by measuring deviations from the 252d mean.
    """
    base = (close.pct_change(10).rolling(50).mean())
    return _zscore_rolling(base, 252)

def rdis_326_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 28 return distribution to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = (close.pct_change(10).rolling(50).mean())
    return _rank_pct(base, 5)

def rdis_327_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 28 return distribution to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = (close.pct_change(10).rolling(50).mean())
    return _rank_pct(base, 21)

def rdis_328_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 28 return distribution to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = (close.pct_change(10).rolling(50).mean())
    return _rank_pct(base, 63)

def rdis_329_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 28 return distribution to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = (close.pct_change(10).rolling(50).mean())
    return _rank_pct(base, 126)

def rdis_330_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 28 return distribution to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = (close.pct_change(10).rolling(50).mean())
    return _rank_pct(base, 252)

def rdis_331_skew_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 28 return distribution distribution over 5d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(10).rolling(50).mean())
    return _rolling_skew(base, 5)

def rdis_332_skew_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 28 return distribution distribution over 21d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(10).rolling(50).mean())
    return _rolling_skew(base, 21)

def rdis_333_skew_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 28 return distribution distribution over 63d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(10).rolling(50).mean())
    return _rolling_skew(base, 63)

def rdis_334_skew_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 28 return distribution distribution over 126d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(10).rolling(50).mean())
    return _rolling_skew(base, 126)

def rdis_335_skew_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 28 return distribution distribution over 252d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(10).rolling(50).mean())
    return _rolling_skew(base, 252)

def rdis_336_kurt_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 28 return distribution over 5d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(10).rolling(50).mean())
    return _rolling_kurt(base, 5)

def rdis_337_kurt_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 28 return distribution over 21d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(10).rolling(50).mean())
    return _rolling_kurt(base, 21)

def rdis_338_kurt_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 28 return distribution over 63d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(10).rolling(50).mean())
    return _rolling_kurt(base, 63)

def rdis_339_kurt_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 28 return distribution over 126d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(10).rolling(50).mean())
    return _rolling_kurt(base, 126)

def rdis_340_kurt_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 28 return distribution over 252d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(10).rolling(50).mean())
    return _rolling_kurt(base, 252)

def rdis_341_voladj_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 28 return distribution for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(10).rolling(50).mean())
    return _safe_div(base, _rolling_std(base, 5))

def rdis_342_voladj_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 28 return distribution for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(10).rolling(50).mean())
    return _safe_div(base, _rolling_std(base, 21))

def rdis_343_voladj_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 28 return distribution for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(10).rolling(50).mean())
    return _safe_div(base, _rolling_std(base, 63))

def rdis_344_voladj_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 28 return distribution for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(10).rolling(50).mean())
    return _safe_div(base, _rolling_std(base, 126))

def rdis_345_voladj_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 28 return distribution for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(10).rolling(50).mean())
    return _safe_div(base, _rolling_std(base, 252))

def rdis_346_lognorm_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 28 return distribution over 5d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(10).rolling(50).mean())
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def rdis_347_lognorm_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 28 return distribution over 21d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(10).rolling(50).mean())
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def rdis_348_lognorm_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 28 return distribution over 63d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(10).rolling(50).mean())
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def rdis_349_lognorm_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 28 return distribution over 126d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(10).rolling(50).mean())
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def rdis_350_lognorm_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 28 return distribution over 252d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(10).rolling(50).mean())
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def rdis_351_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 28 return distribution over a 5d horizon to identify extreme regimes.
    """
    base = (close.pct_change(11).rolling(55).mean())
    return _rolling_mean(base, 5)

def rdis_352_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 28 return distribution over a 21d horizon to identify extreme regimes.
    """
    base = (close.pct_change(11).rolling(55).mean())
    return _rolling_mean(base, 21)

def rdis_353_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 28 return distribution over a 63d horizon to identify extreme regimes.
    """
    base = (close.pct_change(11).rolling(55).mean())
    return _rolling_mean(base, 63)

def rdis_354_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 28 return distribution over a 126d horizon to identify extreme regimes.
    """
    base = (close.pct_change(11).rolling(55).mean())
    return _rolling_mean(base, 126)

def rdis_355_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 28 return distribution over a 252d horizon to identify extreme regimes.
    """
    base = (close.pct_change(11).rolling(55).mean())
    return _rolling_mean(base, 252)

def rdis_356_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 28 return distribution by measuring deviations from the 5d mean.
    """
    base = (close.pct_change(11).rolling(55).mean())
    return _zscore_rolling(base, 5)

def rdis_357_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 28 return distribution by measuring deviations from the 21d mean.
    """
    base = (close.pct_change(11).rolling(55).mean())
    return _zscore_rolling(base, 21)

def rdis_358_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 28 return distribution by measuring deviations from the 63d mean.
    """
    base = (close.pct_change(11).rolling(55).mean())
    return _zscore_rolling(base, 63)

def rdis_359_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 28 return distribution by measuring deviations from the 126d mean.
    """
    base = (close.pct_change(11).rolling(55).mean())
    return _zscore_rolling(base, 126)

def rdis_360_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 28 return distribution by measuring deviations from the 252d mean.
    """
    base = (close.pct_change(11).rolling(55).mean())
    return _zscore_rolling(base, 252)

def rdis_361_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 28 return distribution to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = (close.pct_change(11).rolling(55).mean())
    return _rank_pct(base, 5)

def rdis_362_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 28 return distribution to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = (close.pct_change(11).rolling(55).mean())
    return _rank_pct(base, 21)

def rdis_363_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 28 return distribution to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = (close.pct_change(11).rolling(55).mean())
    return _rank_pct(base, 63)

def rdis_364_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 28 return distribution to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = (close.pct_change(11).rolling(55).mean())
    return _rank_pct(base, 126)

def rdis_365_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 28 return distribution to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = (close.pct_change(11).rolling(55).mean())
    return _rank_pct(base, 252)

def rdis_366_skew_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 28 return distribution distribution over 5d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(11).rolling(55).mean())
    return _rolling_skew(base, 5)

def rdis_367_skew_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 28 return distribution distribution over 21d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(11).rolling(55).mean())
    return _rolling_skew(base, 21)

def rdis_368_skew_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 28 return distribution distribution over 63d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(11).rolling(55).mean())
    return _rolling_skew(base, 63)

def rdis_369_skew_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 28 return distribution distribution over 126d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(11).rolling(55).mean())
    return _rolling_skew(base, 126)

def rdis_370_skew_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 28 return distribution distribution over 252d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(11).rolling(55).mean())
    return _rolling_skew(base, 252)

def rdis_371_kurt_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 28 return distribution over 5d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(11).rolling(55).mean())
    return _rolling_kurt(base, 5)

def rdis_372_kurt_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 28 return distribution over 21d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(11).rolling(55).mean())
    return _rolling_kurt(base, 21)

def rdis_373_kurt_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 28 return distribution over 63d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(11).rolling(55).mean())
    return _rolling_kurt(base, 63)

def rdis_374_kurt_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 28 return distribution over 126d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(11).rolling(55).mean())
    return _rolling_kurt(base, 126)

def rdis_375_kurt_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 28 return distribution over 252d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(11).rolling(55).mean())
    return _rolling_kurt(base, 252)
