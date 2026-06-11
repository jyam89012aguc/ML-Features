"""
17_17_volume_climax — Base Features 301-375
Domain: 17_volume_climax
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

def vcl_301_kurt_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 17 volume climax over 5d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(9).rolling(45).mean())
    return _rolling_kurt(base, 5)

def vcl_302_kurt_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 17 volume climax over 21d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(9).rolling(45).mean())
    return _rolling_kurt(base, 21)

def vcl_303_kurt_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 17 volume climax over 63d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(9).rolling(45).mean())
    return _rolling_kurt(base, 63)

def vcl_304_kurt_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 17 volume climax over 126d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(9).rolling(45).mean())
    return _rolling_kurt(base, 126)

def vcl_305_kurt_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 17 volume climax over 252d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(9).rolling(45).mean())
    return _rolling_kurt(base, 252)

def vcl_306_voladj_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 17 volume climax for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(9).rolling(45).mean())
    return _safe_div(base, _rolling_std(base, 5))

def vcl_307_voladj_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 17 volume climax for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(9).rolling(45).mean())
    return _safe_div(base, _rolling_std(base, 21))

def vcl_308_voladj_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 17 volume climax for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(9).rolling(45).mean())
    return _safe_div(base, _rolling_std(base, 63))

def vcl_309_voladj_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 17 volume climax for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(9).rolling(45).mean())
    return _safe_div(base, _rolling_std(base, 126))

def vcl_310_voladj_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 17 volume climax for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(9).rolling(45).mean())
    return _safe_div(base, _rolling_std(base, 252))

def vcl_311_lognorm_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 17 volume climax over 5d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(9).rolling(45).mean())
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def vcl_312_lognorm_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 17 volume climax over 21d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(9).rolling(45).mean())
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def vcl_313_lognorm_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 17 volume climax over 63d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(9).rolling(45).mean())
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def vcl_314_lognorm_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 17 volume climax over 126d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(9).rolling(45).mean())
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def vcl_315_lognorm_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 17 volume climax over 252d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(9).rolling(45).mean())
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def vcl_316_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 17 volume climax over a 5d horizon to identify extreme regimes.
    """
    base = (close.pct_change(10).rolling(50).mean())
    return _rolling_mean(base, 5)

def vcl_317_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 17 volume climax over a 21d horizon to identify extreme regimes.
    """
    base = (close.pct_change(10).rolling(50).mean())
    return _rolling_mean(base, 21)

def vcl_318_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 17 volume climax over a 63d horizon to identify extreme regimes.
    """
    base = (close.pct_change(10).rolling(50).mean())
    return _rolling_mean(base, 63)

def vcl_319_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 17 volume climax over a 126d horizon to identify extreme regimes.
    """
    base = (close.pct_change(10).rolling(50).mean())
    return _rolling_mean(base, 126)

def vcl_320_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 17 volume climax over a 252d horizon to identify extreme regimes.
    """
    base = (close.pct_change(10).rolling(50).mean())
    return _rolling_mean(base, 252)

def vcl_321_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 17 volume climax by measuring deviations from the 5d mean.
    """
    base = (close.pct_change(10).rolling(50).mean())
    return _zscore_rolling(base, 5)

def vcl_322_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 17 volume climax by measuring deviations from the 21d mean.
    """
    base = (close.pct_change(10).rolling(50).mean())
    return _zscore_rolling(base, 21)

def vcl_323_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 17 volume climax by measuring deviations from the 63d mean.
    """
    base = (close.pct_change(10).rolling(50).mean())
    return _zscore_rolling(base, 63)

def vcl_324_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 17 volume climax by measuring deviations from the 126d mean.
    """
    base = (close.pct_change(10).rolling(50).mean())
    return _zscore_rolling(base, 126)

def vcl_325_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 17 volume climax by measuring deviations from the 252d mean.
    """
    base = (close.pct_change(10).rolling(50).mean())
    return _zscore_rolling(base, 252)

def vcl_326_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 17 volume climax to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = (close.pct_change(10).rolling(50).mean())
    return _rank_pct(base, 5)

def vcl_327_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 17 volume climax to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = (close.pct_change(10).rolling(50).mean())
    return _rank_pct(base, 21)

def vcl_328_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 17 volume climax to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = (close.pct_change(10).rolling(50).mean())
    return _rank_pct(base, 63)

def vcl_329_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 17 volume climax to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = (close.pct_change(10).rolling(50).mean())
    return _rank_pct(base, 126)

def vcl_330_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 17 volume climax to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = (close.pct_change(10).rolling(50).mean())
    return _rank_pct(base, 252)

def vcl_331_skew_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 17 volume climax distribution over 5d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(10).rolling(50).mean())
    return _rolling_skew(base, 5)

def vcl_332_skew_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 17 volume climax distribution over 21d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(10).rolling(50).mean())
    return _rolling_skew(base, 21)

def vcl_333_skew_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 17 volume climax distribution over 63d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(10).rolling(50).mean())
    return _rolling_skew(base, 63)

def vcl_334_skew_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 17 volume climax distribution over 126d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(10).rolling(50).mean())
    return _rolling_skew(base, 126)

def vcl_335_skew_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 17 volume climax distribution over 252d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(10).rolling(50).mean())
    return _rolling_skew(base, 252)

def vcl_336_kurt_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 17 volume climax over 5d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(10).rolling(50).mean())
    return _rolling_kurt(base, 5)

def vcl_337_kurt_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 17 volume climax over 21d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(10).rolling(50).mean())
    return _rolling_kurt(base, 21)

def vcl_338_kurt_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 17 volume climax over 63d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(10).rolling(50).mean())
    return _rolling_kurt(base, 63)

def vcl_339_kurt_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 17 volume climax over 126d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(10).rolling(50).mean())
    return _rolling_kurt(base, 126)

def vcl_340_kurt_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 17 volume climax over 252d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(10).rolling(50).mean())
    return _rolling_kurt(base, 252)

def vcl_341_voladj_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 17 volume climax for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(10).rolling(50).mean())
    return _safe_div(base, _rolling_std(base, 5))

def vcl_342_voladj_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 17 volume climax for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(10).rolling(50).mean())
    return _safe_div(base, _rolling_std(base, 21))

def vcl_343_voladj_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 17 volume climax for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(10).rolling(50).mean())
    return _safe_div(base, _rolling_std(base, 63))

def vcl_344_voladj_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 17 volume climax for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(10).rolling(50).mean())
    return _safe_div(base, _rolling_std(base, 126))

def vcl_345_voladj_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 17 volume climax for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(10).rolling(50).mean())
    return _safe_div(base, _rolling_std(base, 252))

def vcl_346_lognorm_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 17 volume climax over 5d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(10).rolling(50).mean())
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def vcl_347_lognorm_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 17 volume climax over 21d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(10).rolling(50).mean())
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def vcl_348_lognorm_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 17 volume climax over 63d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(10).rolling(50).mean())
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def vcl_349_lognorm_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 17 volume climax over 126d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(10).rolling(50).mean())
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def vcl_350_lognorm_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 17 volume climax over 252d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(10).rolling(50).mean())
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def vcl_351_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 17 volume climax over a 5d horizon to identify extreme regimes.
    """
    base = (close.pct_change(11).rolling(55).mean())
    return _rolling_mean(base, 5)

def vcl_352_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 17 volume climax over a 21d horizon to identify extreme regimes.
    """
    base = (close.pct_change(11).rolling(55).mean())
    return _rolling_mean(base, 21)

def vcl_353_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 17 volume climax over a 63d horizon to identify extreme regimes.
    """
    base = (close.pct_change(11).rolling(55).mean())
    return _rolling_mean(base, 63)

def vcl_354_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 17 volume climax over a 126d horizon to identify extreme regimes.
    """
    base = (close.pct_change(11).rolling(55).mean())
    return _rolling_mean(base, 126)

def vcl_355_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 17 volume climax over a 252d horizon to identify extreme regimes.
    """
    base = (close.pct_change(11).rolling(55).mean())
    return _rolling_mean(base, 252)

def vcl_356_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 17 volume climax by measuring deviations from the 5d mean.
    """
    base = (close.pct_change(11).rolling(55).mean())
    return _zscore_rolling(base, 5)

def vcl_357_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 17 volume climax by measuring deviations from the 21d mean.
    """
    base = (close.pct_change(11).rolling(55).mean())
    return _zscore_rolling(base, 21)

def vcl_358_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 17 volume climax by measuring deviations from the 63d mean.
    """
    base = (close.pct_change(11).rolling(55).mean())
    return _zscore_rolling(base, 63)

def vcl_359_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 17 volume climax by measuring deviations from the 126d mean.
    """
    base = (close.pct_change(11).rolling(55).mean())
    return _zscore_rolling(base, 126)

def vcl_360_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 17 volume climax by measuring deviations from the 252d mean.
    """
    base = (close.pct_change(11).rolling(55).mean())
    return _zscore_rolling(base, 252)

def vcl_361_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 17 volume climax to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = (close.pct_change(11).rolling(55).mean())
    return _rank_pct(base, 5)

def vcl_362_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 17 volume climax to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = (close.pct_change(11).rolling(55).mean())
    return _rank_pct(base, 21)

def vcl_363_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 17 volume climax to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = (close.pct_change(11).rolling(55).mean())
    return _rank_pct(base, 63)

def vcl_364_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 17 volume climax to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = (close.pct_change(11).rolling(55).mean())
    return _rank_pct(base, 126)

def vcl_365_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 17 volume climax to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = (close.pct_change(11).rolling(55).mean())
    return _rank_pct(base, 252)

def vcl_366_skew_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 17 volume climax distribution over 5d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(11).rolling(55).mean())
    return _rolling_skew(base, 5)

def vcl_367_skew_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 17 volume climax distribution over 21d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(11).rolling(55).mean())
    return _rolling_skew(base, 21)

def vcl_368_skew_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 17 volume climax distribution over 63d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(11).rolling(55).mean())
    return _rolling_skew(base, 63)

def vcl_369_skew_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 17 volume climax distribution over 126d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(11).rolling(55).mean())
    return _rolling_skew(base, 126)

def vcl_370_skew_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 17 volume climax distribution over 252d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(11).rolling(55).mean())
    return _rolling_skew(base, 252)

def vcl_371_kurt_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 17 volume climax over 5d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(11).rolling(55).mean())
    return _rolling_kurt(base, 5)

def vcl_372_kurt_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 17 volume climax over 21d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(11).rolling(55).mean())
    return _rolling_kurt(base, 21)

def vcl_373_kurt_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 17 volume climax over 63d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(11).rolling(55).mean())
    return _rolling_kurt(base, 63)

def vcl_374_kurt_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 17 volume climax over 126d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(11).rolling(55).mean())
    return _rolling_kurt(base, 126)

def vcl_375_kurt_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 17 volume climax over 252d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(11).rolling(55).mean())
    return _rolling_kurt(base, 252)
