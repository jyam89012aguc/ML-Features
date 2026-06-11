"""
46_46_gap_structure — Base Features 301-375
Domain: 46_gap_structure
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

def gaps_301_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 46 gap structure over 5d to capture explosive breakdown or reversal points.
    """
    base = ((close - open).abs().rolling(45).mean())
    return _rolling_kurt(base, 5)

def gaps_302_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 46 gap structure over 21d to capture explosive breakdown or reversal points.
    """
    base = ((close - open).abs().rolling(45).mean())
    return _rolling_kurt(base, 21)

def gaps_303_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 46 gap structure over 63d to capture explosive breakdown or reversal points.
    """
    base = ((close - open).abs().rolling(45).mean())
    return _rolling_kurt(base, 63)

def gaps_304_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 46 gap structure over 126d to capture explosive breakdown or reversal points.
    """
    base = ((close - open).abs().rolling(45).mean())
    return _rolling_kurt(base, 126)

def gaps_305_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 46 gap structure over 252d to capture explosive breakdown or reversal points.
    """
    base = ((close - open).abs().rolling(45).mean())
    return _rolling_kurt(base, 252)

def gaps_306_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 46 gap structure for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = ((close - open).abs().rolling(45).mean())
    return _safe_div(base, _rolling_std(base, 5))

def gaps_307_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 46 gap structure for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = ((close - open).abs().rolling(45).mean())
    return _safe_div(base, _rolling_std(base, 21))

def gaps_308_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 46 gap structure for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = ((close - open).abs().rolling(45).mean())
    return _safe_div(base, _rolling_std(base, 63))

def gaps_309_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 46 gap structure for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = ((close - open).abs().rolling(45).mean())
    return _safe_div(base, _rolling_std(base, 126))

def gaps_310_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 46 gap structure for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = ((close - open).abs().rolling(45).mean())
    return _safe_div(base, _rolling_std(base, 252))

def gaps_311_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 46 gap structure over 5d to stabilize variance and capture exponential shifts.
    """
    base = ((close - open).abs().rolling(45).mean())
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def gaps_312_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 46 gap structure over 21d to stabilize variance and capture exponential shifts.
    """
    base = ((close - open).abs().rolling(45).mean())
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def gaps_313_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 46 gap structure over 63d to stabilize variance and capture exponential shifts.
    """
    base = ((close - open).abs().rolling(45).mean())
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def gaps_314_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 46 gap structure over 126d to stabilize variance and capture exponential shifts.
    """
    base = ((close - open).abs().rolling(45).mean())
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def gaps_315_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 46 gap structure over 252d to stabilize variance and capture exponential shifts.
    """
    base = ((close - open).abs().rolling(45).mean())
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def gaps_316_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 46 gap structure over a 5d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(50).mean())
    return _rolling_mean(base, 5)

def gaps_317_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 46 gap structure over a 21d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(50).mean())
    return _rolling_mean(base, 21)

def gaps_318_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 46 gap structure over a 63d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(50).mean())
    return _rolling_mean(base, 63)

def gaps_319_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 46 gap structure over a 126d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(50).mean())
    return _rolling_mean(base, 126)

def gaps_320_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 46 gap structure over a 252d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(50).mean())
    return _rolling_mean(base, 252)

def gaps_321_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 46 gap structure by measuring deviations from the 5d mean.
    """
    base = ((close - open).abs().rolling(50).mean())
    return _zscore_rolling(base, 5)

def gaps_322_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 46 gap structure by measuring deviations from the 21d mean.
    """
    base = ((close - open).abs().rolling(50).mean())
    return _zscore_rolling(base, 21)

def gaps_323_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 46 gap structure by measuring deviations from the 63d mean.
    """
    base = ((close - open).abs().rolling(50).mean())
    return _zscore_rolling(base, 63)

def gaps_324_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 46 gap structure by measuring deviations from the 126d mean.
    """
    base = ((close - open).abs().rolling(50).mean())
    return _zscore_rolling(base, 126)

def gaps_325_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 46 gap structure by measuring deviations from the 252d mean.
    """
    base = ((close - open).abs().rolling(50).mean())
    return _zscore_rolling(base, 252)

def gaps_326_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 46 gap structure to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = ((close - open).abs().rolling(50).mean())
    return _rank_pct(base, 5)

def gaps_327_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 46 gap structure to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = ((close - open).abs().rolling(50).mean())
    return _rank_pct(base, 21)

def gaps_328_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 46 gap structure to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = ((close - open).abs().rolling(50).mean())
    return _rank_pct(base, 63)

def gaps_329_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 46 gap structure to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = ((close - open).abs().rolling(50).mean())
    return _rank_pct(base, 126)

def gaps_330_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 46 gap structure to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = ((close - open).abs().rolling(50).mean())
    return _rank_pct(base, 252)

def gaps_331_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 46 gap structure distribution over 5d to detect tail risk or exhaustion.
    """
    base = ((close - open).abs().rolling(50).mean())
    return _rolling_skew(base, 5)

def gaps_332_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 46 gap structure distribution over 21d to detect tail risk or exhaustion.
    """
    base = ((close - open).abs().rolling(50).mean())
    return _rolling_skew(base, 21)

def gaps_333_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 46 gap structure distribution over 63d to detect tail risk or exhaustion.
    """
    base = ((close - open).abs().rolling(50).mean())
    return _rolling_skew(base, 63)

def gaps_334_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 46 gap structure distribution over 126d to detect tail risk or exhaustion.
    """
    base = ((close - open).abs().rolling(50).mean())
    return _rolling_skew(base, 126)

def gaps_335_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 46 gap structure distribution over 252d to detect tail risk or exhaustion.
    """
    base = ((close - open).abs().rolling(50).mean())
    return _rolling_skew(base, 252)

def gaps_336_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 46 gap structure over 5d to capture explosive breakdown or reversal points.
    """
    base = ((close - open).abs().rolling(50).mean())
    return _rolling_kurt(base, 5)

def gaps_337_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 46 gap structure over 21d to capture explosive breakdown or reversal points.
    """
    base = ((close - open).abs().rolling(50).mean())
    return _rolling_kurt(base, 21)

def gaps_338_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 46 gap structure over 63d to capture explosive breakdown or reversal points.
    """
    base = ((close - open).abs().rolling(50).mean())
    return _rolling_kurt(base, 63)

def gaps_339_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 46 gap structure over 126d to capture explosive breakdown or reversal points.
    """
    base = ((close - open).abs().rolling(50).mean())
    return _rolling_kurt(base, 126)

def gaps_340_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 46 gap structure over 252d to capture explosive breakdown or reversal points.
    """
    base = ((close - open).abs().rolling(50).mean())
    return _rolling_kurt(base, 252)

def gaps_341_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 46 gap structure for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = ((close - open).abs().rolling(50).mean())
    return _safe_div(base, _rolling_std(base, 5))

def gaps_342_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 46 gap structure for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = ((close - open).abs().rolling(50).mean())
    return _safe_div(base, _rolling_std(base, 21))

def gaps_343_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 46 gap structure for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = ((close - open).abs().rolling(50).mean())
    return _safe_div(base, _rolling_std(base, 63))

def gaps_344_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 46 gap structure for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = ((close - open).abs().rolling(50).mean())
    return _safe_div(base, _rolling_std(base, 126))

def gaps_345_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 46 gap structure for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = ((close - open).abs().rolling(50).mean())
    return _safe_div(base, _rolling_std(base, 252))

def gaps_346_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 46 gap structure over 5d to stabilize variance and capture exponential shifts.
    """
    base = ((close - open).abs().rolling(50).mean())
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def gaps_347_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 46 gap structure over 21d to stabilize variance and capture exponential shifts.
    """
    base = ((close - open).abs().rolling(50).mean())
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def gaps_348_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 46 gap structure over 63d to stabilize variance and capture exponential shifts.
    """
    base = ((close - open).abs().rolling(50).mean())
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def gaps_349_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 46 gap structure over 126d to stabilize variance and capture exponential shifts.
    """
    base = ((close - open).abs().rolling(50).mean())
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def gaps_350_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 46 gap structure over 252d to stabilize variance and capture exponential shifts.
    """
    base = ((close - open).abs().rolling(50).mean())
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def gaps_351_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 46 gap structure over a 5d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(55).mean())
    return _rolling_mean(base, 5)

def gaps_352_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 46 gap structure over a 21d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(55).mean())
    return _rolling_mean(base, 21)

def gaps_353_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 46 gap structure over a 63d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(55).mean())
    return _rolling_mean(base, 63)

def gaps_354_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 46 gap structure over a 126d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(55).mean())
    return _rolling_mean(base, 126)

def gaps_355_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 46 gap structure over a 252d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(55).mean())
    return _rolling_mean(base, 252)

def gaps_356_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 46 gap structure by measuring deviations from the 5d mean.
    """
    base = ((close - open).abs().rolling(55).mean())
    return _zscore_rolling(base, 5)

def gaps_357_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 46 gap structure by measuring deviations from the 21d mean.
    """
    base = ((close - open).abs().rolling(55).mean())
    return _zscore_rolling(base, 21)

def gaps_358_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 46 gap structure by measuring deviations from the 63d mean.
    """
    base = ((close - open).abs().rolling(55).mean())
    return _zscore_rolling(base, 63)

def gaps_359_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 46 gap structure by measuring deviations from the 126d mean.
    """
    base = ((close - open).abs().rolling(55).mean())
    return _zscore_rolling(base, 126)

def gaps_360_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 46 gap structure by measuring deviations from the 252d mean.
    """
    base = ((close - open).abs().rolling(55).mean())
    return _zscore_rolling(base, 252)

def gaps_361_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 46 gap structure to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = ((close - open).abs().rolling(55).mean())
    return _rank_pct(base, 5)

def gaps_362_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 46 gap structure to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = ((close - open).abs().rolling(55).mean())
    return _rank_pct(base, 21)

def gaps_363_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 46 gap structure to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = ((close - open).abs().rolling(55).mean())
    return _rank_pct(base, 63)

def gaps_364_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 46 gap structure to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = ((close - open).abs().rolling(55).mean())
    return _rank_pct(base, 126)

def gaps_365_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 46 gap structure to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = ((close - open).abs().rolling(55).mean())
    return _rank_pct(base, 252)

def gaps_366_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 46 gap structure distribution over 5d to detect tail risk or exhaustion.
    """
    base = ((close - open).abs().rolling(55).mean())
    return _rolling_skew(base, 5)

def gaps_367_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 46 gap structure distribution over 21d to detect tail risk or exhaustion.
    """
    base = ((close - open).abs().rolling(55).mean())
    return _rolling_skew(base, 21)

def gaps_368_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 46 gap structure distribution over 63d to detect tail risk or exhaustion.
    """
    base = ((close - open).abs().rolling(55).mean())
    return _rolling_skew(base, 63)

def gaps_369_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 46 gap structure distribution over 126d to detect tail risk or exhaustion.
    """
    base = ((close - open).abs().rolling(55).mean())
    return _rolling_skew(base, 126)

def gaps_370_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 46 gap structure distribution over 252d to detect tail risk or exhaustion.
    """
    base = ((close - open).abs().rolling(55).mean())
    return _rolling_skew(base, 252)

def gaps_371_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 46 gap structure over 5d to capture explosive breakdown or reversal points.
    """
    base = ((close - open).abs().rolling(55).mean())
    return _rolling_kurt(base, 5)

def gaps_372_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 46 gap structure over 21d to capture explosive breakdown or reversal points.
    """
    base = ((close - open).abs().rolling(55).mean())
    return _rolling_kurt(base, 21)

def gaps_373_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 46 gap structure over 63d to capture explosive breakdown or reversal points.
    """
    base = ((close - open).abs().rolling(55).mean())
    return _rolling_kurt(base, 63)

def gaps_374_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 46 gap structure over 126d to capture explosive breakdown or reversal points.
    """
    base = ((close - open).abs().rolling(55).mean())
    return _rolling_kurt(base, 126)

def gaps_375_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 46 gap structure over 252d to capture explosive breakdown or reversal points.
    """
    base = ((close - open).abs().rolling(55).mean())
    return _rolling_kurt(base, 252)
