"""
101_101_wyckoff_capitulation_structure — Base Features 301-375
Domain: 101_wyckoff_capitulation_structure
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

def wyck_301_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 101 wyckoff capitulation structure over 5d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change(9)
    return _rolling_kurt(base, 5)

def wyck_302_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 101 wyckoff capitulation structure over 21d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change(9)
    return _rolling_kurt(base, 21)

def wyck_303_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 101 wyckoff capitulation structure over 63d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change(9)
    return _rolling_kurt(base, 63)

def wyck_304_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 101 wyckoff capitulation structure over 126d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change(9)
    return _rolling_kurt(base, 126)

def wyck_305_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 101 wyckoff capitulation structure over 252d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change(9)
    return _rolling_kurt(base, 252)

def wyck_306_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 101 wyckoff capitulation structure for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change(9)
    return _safe_div(base, _rolling_std(base, 5))

def wyck_307_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 101 wyckoff capitulation structure for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change(9)
    return _safe_div(base, _rolling_std(base, 21))

def wyck_308_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 101 wyckoff capitulation structure for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change(9)
    return _safe_div(base, _rolling_std(base, 63))

def wyck_309_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 101 wyckoff capitulation structure for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change(9)
    return _safe_div(base, _rolling_std(base, 126))

def wyck_310_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 101 wyckoff capitulation structure for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change(9)
    return _safe_div(base, _rolling_std(base, 252))

def wyck_311_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 101 wyckoff capitulation structure over 5d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change(9)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def wyck_312_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 101 wyckoff capitulation structure over 21d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change(9)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def wyck_313_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 101 wyckoff capitulation structure over 63d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change(9)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def wyck_314_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 101 wyckoff capitulation structure over 126d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change(9)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def wyck_315_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 101 wyckoff capitulation structure over 252d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change(9)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def wyck_316_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 101 wyckoff capitulation structure over a 5d horizon to identify extreme regimes.
    """
    base = close.pct_change(10)
    return _rolling_mean(base, 5)

def wyck_317_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 101 wyckoff capitulation structure over a 21d horizon to identify extreme regimes.
    """
    base = close.pct_change(10)
    return _rolling_mean(base, 21)

def wyck_318_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 101 wyckoff capitulation structure over a 63d horizon to identify extreme regimes.
    """
    base = close.pct_change(10)
    return _rolling_mean(base, 63)

def wyck_319_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 101 wyckoff capitulation structure over a 126d horizon to identify extreme regimes.
    """
    base = close.pct_change(10)
    return _rolling_mean(base, 126)

def wyck_320_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 101 wyckoff capitulation structure over a 252d horizon to identify extreme regimes.
    """
    base = close.pct_change(10)
    return _rolling_mean(base, 252)

def wyck_321_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 101 wyckoff capitulation structure by measuring deviations from the 5d mean.
    """
    base = close.pct_change(10)
    return _zscore_rolling(base, 5)

def wyck_322_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 101 wyckoff capitulation structure by measuring deviations from the 21d mean.
    """
    base = close.pct_change(10)
    return _zscore_rolling(base, 21)

def wyck_323_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 101 wyckoff capitulation structure by measuring deviations from the 63d mean.
    """
    base = close.pct_change(10)
    return _zscore_rolling(base, 63)

def wyck_324_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 101 wyckoff capitulation structure by measuring deviations from the 126d mean.
    """
    base = close.pct_change(10)
    return _zscore_rolling(base, 126)

def wyck_325_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 101 wyckoff capitulation structure by measuring deviations from the 252d mean.
    """
    base = close.pct_change(10)
    return _zscore_rolling(base, 252)

def wyck_326_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 101 wyckoff capitulation structure to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = close.pct_change(10)
    return _rank_pct(base, 5)

def wyck_327_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 101 wyckoff capitulation structure to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = close.pct_change(10)
    return _rank_pct(base, 21)

def wyck_328_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 101 wyckoff capitulation structure to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = close.pct_change(10)
    return _rank_pct(base, 63)

def wyck_329_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 101 wyckoff capitulation structure to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = close.pct_change(10)
    return _rank_pct(base, 126)

def wyck_330_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 101 wyckoff capitulation structure to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = close.pct_change(10)
    return _rank_pct(base, 252)

def wyck_331_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 101 wyckoff capitulation structure distribution over 5d to detect tail risk or exhaustion.
    """
    base = close.pct_change(10)
    return _rolling_skew(base, 5)

def wyck_332_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 101 wyckoff capitulation structure distribution over 21d to detect tail risk or exhaustion.
    """
    base = close.pct_change(10)
    return _rolling_skew(base, 21)

def wyck_333_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 101 wyckoff capitulation structure distribution over 63d to detect tail risk or exhaustion.
    """
    base = close.pct_change(10)
    return _rolling_skew(base, 63)

def wyck_334_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 101 wyckoff capitulation structure distribution over 126d to detect tail risk or exhaustion.
    """
    base = close.pct_change(10)
    return _rolling_skew(base, 126)

def wyck_335_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 101 wyckoff capitulation structure distribution over 252d to detect tail risk or exhaustion.
    """
    base = close.pct_change(10)
    return _rolling_skew(base, 252)

def wyck_336_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 101 wyckoff capitulation structure over 5d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change(10)
    return _rolling_kurt(base, 5)

def wyck_337_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 101 wyckoff capitulation structure over 21d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change(10)
    return _rolling_kurt(base, 21)

def wyck_338_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 101 wyckoff capitulation structure over 63d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change(10)
    return _rolling_kurt(base, 63)

def wyck_339_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 101 wyckoff capitulation structure over 126d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change(10)
    return _rolling_kurt(base, 126)

def wyck_340_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 101 wyckoff capitulation structure over 252d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change(10)
    return _rolling_kurt(base, 252)

def wyck_341_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 101 wyckoff capitulation structure for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change(10)
    return _safe_div(base, _rolling_std(base, 5))

def wyck_342_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 101 wyckoff capitulation structure for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change(10)
    return _safe_div(base, _rolling_std(base, 21))

def wyck_343_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 101 wyckoff capitulation structure for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change(10)
    return _safe_div(base, _rolling_std(base, 63))

def wyck_344_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 101 wyckoff capitulation structure for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change(10)
    return _safe_div(base, _rolling_std(base, 126))

def wyck_345_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 101 wyckoff capitulation structure for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change(10)
    return _safe_div(base, _rolling_std(base, 252))

def wyck_346_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 101 wyckoff capitulation structure over 5d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change(10)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def wyck_347_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 101 wyckoff capitulation structure over 21d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change(10)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def wyck_348_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 101 wyckoff capitulation structure over 63d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change(10)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def wyck_349_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 101 wyckoff capitulation structure over 126d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change(10)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def wyck_350_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 101 wyckoff capitulation structure over 252d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change(10)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def wyck_351_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 101 wyckoff capitulation structure over a 5d horizon to identify extreme regimes.
    """
    base = close.pct_change(11)
    return _rolling_mean(base, 5)

def wyck_352_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 101 wyckoff capitulation structure over a 21d horizon to identify extreme regimes.
    """
    base = close.pct_change(11)
    return _rolling_mean(base, 21)

def wyck_353_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 101 wyckoff capitulation structure over a 63d horizon to identify extreme regimes.
    """
    base = close.pct_change(11)
    return _rolling_mean(base, 63)

def wyck_354_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 101 wyckoff capitulation structure over a 126d horizon to identify extreme regimes.
    """
    base = close.pct_change(11)
    return _rolling_mean(base, 126)

def wyck_355_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 101 wyckoff capitulation structure over a 252d horizon to identify extreme regimes.
    """
    base = close.pct_change(11)
    return _rolling_mean(base, 252)

def wyck_356_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 101 wyckoff capitulation structure by measuring deviations from the 5d mean.
    """
    base = close.pct_change(11)
    return _zscore_rolling(base, 5)

def wyck_357_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 101 wyckoff capitulation structure by measuring deviations from the 21d mean.
    """
    base = close.pct_change(11)
    return _zscore_rolling(base, 21)

def wyck_358_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 101 wyckoff capitulation structure by measuring deviations from the 63d mean.
    """
    base = close.pct_change(11)
    return _zscore_rolling(base, 63)

def wyck_359_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 101 wyckoff capitulation structure by measuring deviations from the 126d mean.
    """
    base = close.pct_change(11)
    return _zscore_rolling(base, 126)

def wyck_360_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 101 wyckoff capitulation structure by measuring deviations from the 252d mean.
    """
    base = close.pct_change(11)
    return _zscore_rolling(base, 252)

def wyck_361_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 101 wyckoff capitulation structure to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = close.pct_change(11)
    return _rank_pct(base, 5)

def wyck_362_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 101 wyckoff capitulation structure to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = close.pct_change(11)
    return _rank_pct(base, 21)

def wyck_363_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 101 wyckoff capitulation structure to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = close.pct_change(11)
    return _rank_pct(base, 63)

def wyck_364_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 101 wyckoff capitulation structure to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = close.pct_change(11)
    return _rank_pct(base, 126)

def wyck_365_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 101 wyckoff capitulation structure to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = close.pct_change(11)
    return _rank_pct(base, 252)

def wyck_366_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 101 wyckoff capitulation structure distribution over 5d to detect tail risk or exhaustion.
    """
    base = close.pct_change(11)
    return _rolling_skew(base, 5)

def wyck_367_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 101 wyckoff capitulation structure distribution over 21d to detect tail risk or exhaustion.
    """
    base = close.pct_change(11)
    return _rolling_skew(base, 21)

def wyck_368_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 101 wyckoff capitulation structure distribution over 63d to detect tail risk or exhaustion.
    """
    base = close.pct_change(11)
    return _rolling_skew(base, 63)

def wyck_369_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 101 wyckoff capitulation structure distribution over 126d to detect tail risk or exhaustion.
    """
    base = close.pct_change(11)
    return _rolling_skew(base, 126)

def wyck_370_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 101 wyckoff capitulation structure distribution over 252d to detect tail risk or exhaustion.
    """
    base = close.pct_change(11)
    return _rolling_skew(base, 252)

def wyck_371_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 101 wyckoff capitulation structure over 5d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change(11)
    return _rolling_kurt(base, 5)

def wyck_372_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 101 wyckoff capitulation structure over 21d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change(11)
    return _rolling_kurt(base, 21)

def wyck_373_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 101 wyckoff capitulation structure over 63d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change(11)
    return _rolling_kurt(base, 63)

def wyck_374_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 101 wyckoff capitulation structure over 126d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change(11)
    return _rolling_kurt(base, 126)

def wyck_375_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 101 wyckoff capitulation structure over 252d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change(11)
    return _rolling_kurt(base, 252)
