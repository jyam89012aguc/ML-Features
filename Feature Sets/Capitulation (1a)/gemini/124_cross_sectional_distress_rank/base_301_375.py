"""
124_124_cross_sectional_distress_rank — Base Features 301-375
Domain: 124_cross_sectional_distress_rank
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

def csdr_301_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 124 cross sectional distress rank over 5d to capture explosive breakdown or reversal points.
    """
    base = _rank_pct(close.pct_change(90), 252)
    return _rolling_kurt(base, 5)

def csdr_302_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 124 cross sectional distress rank over 21d to capture explosive breakdown or reversal points.
    """
    base = _rank_pct(close.pct_change(90), 252)
    return _rolling_kurt(base, 21)

def csdr_303_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 124 cross sectional distress rank over 63d to capture explosive breakdown or reversal points.
    """
    base = _rank_pct(close.pct_change(90), 252)
    return _rolling_kurt(base, 63)

def csdr_304_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 124 cross sectional distress rank over 126d to capture explosive breakdown or reversal points.
    """
    base = _rank_pct(close.pct_change(90), 252)
    return _rolling_kurt(base, 126)

def csdr_305_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 124 cross sectional distress rank over 252d to capture explosive breakdown or reversal points.
    """
    base = _rank_pct(close.pct_change(90), 252)
    return _rolling_kurt(base, 252)

def csdr_306_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 124 cross sectional distress rank for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = _rank_pct(close.pct_change(90), 252)
    return _safe_div(base, _rolling_std(base, 5))

def csdr_307_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 124 cross sectional distress rank for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = _rank_pct(close.pct_change(90), 252)
    return _safe_div(base, _rolling_std(base, 21))

def csdr_308_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 124 cross sectional distress rank for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = _rank_pct(close.pct_change(90), 252)
    return _safe_div(base, _rolling_std(base, 63))

def csdr_309_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 124 cross sectional distress rank for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = _rank_pct(close.pct_change(90), 252)
    return _safe_div(base, _rolling_std(base, 126))

def csdr_310_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 124 cross sectional distress rank for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = _rank_pct(close.pct_change(90), 252)
    return _safe_div(base, _rolling_std(base, 252))

def csdr_311_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 124 cross sectional distress rank over 5d to stabilize variance and capture exponential shifts.
    """
    base = _rank_pct(close.pct_change(90), 252)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def csdr_312_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 124 cross sectional distress rank over 21d to stabilize variance and capture exponential shifts.
    """
    base = _rank_pct(close.pct_change(90), 252)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def csdr_313_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 124 cross sectional distress rank over 63d to stabilize variance and capture exponential shifts.
    """
    base = _rank_pct(close.pct_change(90), 252)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def csdr_314_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 124 cross sectional distress rank over 126d to stabilize variance and capture exponential shifts.
    """
    base = _rank_pct(close.pct_change(90), 252)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def csdr_315_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 124 cross sectional distress rank over 252d to stabilize variance and capture exponential shifts.
    """
    base = _rank_pct(close.pct_change(90), 252)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def csdr_316_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 124 cross sectional distress rank over a 5d horizon to identify extreme regimes.
    """
    base = _rank_pct(close.pct_change(100), 252)
    return _rolling_mean(base, 5)

def csdr_317_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 124 cross sectional distress rank over a 21d horizon to identify extreme regimes.
    """
    base = _rank_pct(close.pct_change(100), 252)
    return _rolling_mean(base, 21)

def csdr_318_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 124 cross sectional distress rank over a 63d horizon to identify extreme regimes.
    """
    base = _rank_pct(close.pct_change(100), 252)
    return _rolling_mean(base, 63)

def csdr_319_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 124 cross sectional distress rank over a 126d horizon to identify extreme regimes.
    """
    base = _rank_pct(close.pct_change(100), 252)
    return _rolling_mean(base, 126)

def csdr_320_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 124 cross sectional distress rank over a 252d horizon to identify extreme regimes.
    """
    base = _rank_pct(close.pct_change(100), 252)
    return _rolling_mean(base, 252)

def csdr_321_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 124 cross sectional distress rank by measuring deviations from the 5d mean.
    """
    base = _rank_pct(close.pct_change(100), 252)
    return _zscore_rolling(base, 5)

def csdr_322_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 124 cross sectional distress rank by measuring deviations from the 21d mean.
    """
    base = _rank_pct(close.pct_change(100), 252)
    return _zscore_rolling(base, 21)

def csdr_323_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 124 cross sectional distress rank by measuring deviations from the 63d mean.
    """
    base = _rank_pct(close.pct_change(100), 252)
    return _zscore_rolling(base, 63)

def csdr_324_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 124 cross sectional distress rank by measuring deviations from the 126d mean.
    """
    base = _rank_pct(close.pct_change(100), 252)
    return _zscore_rolling(base, 126)

def csdr_325_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 124 cross sectional distress rank by measuring deviations from the 252d mean.
    """
    base = _rank_pct(close.pct_change(100), 252)
    return _zscore_rolling(base, 252)

def csdr_326_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 124 cross sectional distress rank to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = _rank_pct(close.pct_change(100), 252)
    return _rank_pct(base, 5)

def csdr_327_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 124 cross sectional distress rank to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = _rank_pct(close.pct_change(100), 252)
    return _rank_pct(base, 21)

def csdr_328_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 124 cross sectional distress rank to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = _rank_pct(close.pct_change(100), 252)
    return _rank_pct(base, 63)

def csdr_329_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 124 cross sectional distress rank to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = _rank_pct(close.pct_change(100), 252)
    return _rank_pct(base, 126)

def csdr_330_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 124 cross sectional distress rank to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = _rank_pct(close.pct_change(100), 252)
    return _rank_pct(base, 252)

def csdr_331_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 124 cross sectional distress rank distribution over 5d to detect tail risk or exhaustion.
    """
    base = _rank_pct(close.pct_change(100), 252)
    return _rolling_skew(base, 5)

def csdr_332_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 124 cross sectional distress rank distribution over 21d to detect tail risk or exhaustion.
    """
    base = _rank_pct(close.pct_change(100), 252)
    return _rolling_skew(base, 21)

def csdr_333_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 124 cross sectional distress rank distribution over 63d to detect tail risk or exhaustion.
    """
    base = _rank_pct(close.pct_change(100), 252)
    return _rolling_skew(base, 63)

def csdr_334_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 124 cross sectional distress rank distribution over 126d to detect tail risk or exhaustion.
    """
    base = _rank_pct(close.pct_change(100), 252)
    return _rolling_skew(base, 126)

def csdr_335_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 124 cross sectional distress rank distribution over 252d to detect tail risk or exhaustion.
    """
    base = _rank_pct(close.pct_change(100), 252)
    return _rolling_skew(base, 252)

def csdr_336_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 124 cross sectional distress rank over 5d to capture explosive breakdown or reversal points.
    """
    base = _rank_pct(close.pct_change(100), 252)
    return _rolling_kurt(base, 5)

def csdr_337_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 124 cross sectional distress rank over 21d to capture explosive breakdown or reversal points.
    """
    base = _rank_pct(close.pct_change(100), 252)
    return _rolling_kurt(base, 21)

def csdr_338_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 124 cross sectional distress rank over 63d to capture explosive breakdown or reversal points.
    """
    base = _rank_pct(close.pct_change(100), 252)
    return _rolling_kurt(base, 63)

def csdr_339_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 124 cross sectional distress rank over 126d to capture explosive breakdown or reversal points.
    """
    base = _rank_pct(close.pct_change(100), 252)
    return _rolling_kurt(base, 126)

def csdr_340_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 124 cross sectional distress rank over 252d to capture explosive breakdown or reversal points.
    """
    base = _rank_pct(close.pct_change(100), 252)
    return _rolling_kurt(base, 252)

def csdr_341_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 124 cross sectional distress rank for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = _rank_pct(close.pct_change(100), 252)
    return _safe_div(base, _rolling_std(base, 5))

def csdr_342_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 124 cross sectional distress rank for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = _rank_pct(close.pct_change(100), 252)
    return _safe_div(base, _rolling_std(base, 21))

def csdr_343_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 124 cross sectional distress rank for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = _rank_pct(close.pct_change(100), 252)
    return _safe_div(base, _rolling_std(base, 63))

def csdr_344_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 124 cross sectional distress rank for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = _rank_pct(close.pct_change(100), 252)
    return _safe_div(base, _rolling_std(base, 126))

def csdr_345_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 124 cross sectional distress rank for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = _rank_pct(close.pct_change(100), 252)
    return _safe_div(base, _rolling_std(base, 252))

def csdr_346_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 124 cross sectional distress rank over 5d to stabilize variance and capture exponential shifts.
    """
    base = _rank_pct(close.pct_change(100), 252)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def csdr_347_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 124 cross sectional distress rank over 21d to stabilize variance and capture exponential shifts.
    """
    base = _rank_pct(close.pct_change(100), 252)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def csdr_348_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 124 cross sectional distress rank over 63d to stabilize variance and capture exponential shifts.
    """
    base = _rank_pct(close.pct_change(100), 252)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def csdr_349_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 124 cross sectional distress rank over 126d to stabilize variance and capture exponential shifts.
    """
    base = _rank_pct(close.pct_change(100), 252)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def csdr_350_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 124 cross sectional distress rank over 252d to stabilize variance and capture exponential shifts.
    """
    base = _rank_pct(close.pct_change(100), 252)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def csdr_351_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 124 cross sectional distress rank over a 5d horizon to identify extreme regimes.
    """
    base = _rank_pct(close.pct_change(110), 252)
    return _rolling_mean(base, 5)

def csdr_352_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 124 cross sectional distress rank over a 21d horizon to identify extreme regimes.
    """
    base = _rank_pct(close.pct_change(110), 252)
    return _rolling_mean(base, 21)

def csdr_353_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 124 cross sectional distress rank over a 63d horizon to identify extreme regimes.
    """
    base = _rank_pct(close.pct_change(110), 252)
    return _rolling_mean(base, 63)

def csdr_354_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 124 cross sectional distress rank over a 126d horizon to identify extreme regimes.
    """
    base = _rank_pct(close.pct_change(110), 252)
    return _rolling_mean(base, 126)

def csdr_355_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 124 cross sectional distress rank over a 252d horizon to identify extreme regimes.
    """
    base = _rank_pct(close.pct_change(110), 252)
    return _rolling_mean(base, 252)

def csdr_356_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 124 cross sectional distress rank by measuring deviations from the 5d mean.
    """
    base = _rank_pct(close.pct_change(110), 252)
    return _zscore_rolling(base, 5)

def csdr_357_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 124 cross sectional distress rank by measuring deviations from the 21d mean.
    """
    base = _rank_pct(close.pct_change(110), 252)
    return _zscore_rolling(base, 21)

def csdr_358_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 124 cross sectional distress rank by measuring deviations from the 63d mean.
    """
    base = _rank_pct(close.pct_change(110), 252)
    return _zscore_rolling(base, 63)

def csdr_359_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 124 cross sectional distress rank by measuring deviations from the 126d mean.
    """
    base = _rank_pct(close.pct_change(110), 252)
    return _zscore_rolling(base, 126)

def csdr_360_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 124 cross sectional distress rank by measuring deviations from the 252d mean.
    """
    base = _rank_pct(close.pct_change(110), 252)
    return _zscore_rolling(base, 252)

def csdr_361_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 124 cross sectional distress rank to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = _rank_pct(close.pct_change(110), 252)
    return _rank_pct(base, 5)

def csdr_362_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 124 cross sectional distress rank to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = _rank_pct(close.pct_change(110), 252)
    return _rank_pct(base, 21)

def csdr_363_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 124 cross sectional distress rank to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = _rank_pct(close.pct_change(110), 252)
    return _rank_pct(base, 63)

def csdr_364_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 124 cross sectional distress rank to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = _rank_pct(close.pct_change(110), 252)
    return _rank_pct(base, 126)

def csdr_365_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 124 cross sectional distress rank to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = _rank_pct(close.pct_change(110), 252)
    return _rank_pct(base, 252)

def csdr_366_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 124 cross sectional distress rank distribution over 5d to detect tail risk or exhaustion.
    """
    base = _rank_pct(close.pct_change(110), 252)
    return _rolling_skew(base, 5)

def csdr_367_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 124 cross sectional distress rank distribution over 21d to detect tail risk or exhaustion.
    """
    base = _rank_pct(close.pct_change(110), 252)
    return _rolling_skew(base, 21)

def csdr_368_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 124 cross sectional distress rank distribution over 63d to detect tail risk or exhaustion.
    """
    base = _rank_pct(close.pct_change(110), 252)
    return _rolling_skew(base, 63)

def csdr_369_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 124 cross sectional distress rank distribution over 126d to detect tail risk or exhaustion.
    """
    base = _rank_pct(close.pct_change(110), 252)
    return _rolling_skew(base, 126)

def csdr_370_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 124 cross sectional distress rank distribution over 252d to detect tail risk or exhaustion.
    """
    base = _rank_pct(close.pct_change(110), 252)
    return _rolling_skew(base, 252)

def csdr_371_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 124 cross sectional distress rank over 5d to capture explosive breakdown or reversal points.
    """
    base = _rank_pct(close.pct_change(110), 252)
    return _rolling_kurt(base, 5)

def csdr_372_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 124 cross sectional distress rank over 21d to capture explosive breakdown or reversal points.
    """
    base = _rank_pct(close.pct_change(110), 252)
    return _rolling_kurt(base, 21)

def csdr_373_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 124 cross sectional distress rank over 63d to capture explosive breakdown or reversal points.
    """
    base = _rank_pct(close.pct_change(110), 252)
    return _rolling_kurt(base, 63)

def csdr_374_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 124 cross sectional distress rank over 126d to capture explosive breakdown or reversal points.
    """
    base = _rank_pct(close.pct_change(110), 252)
    return _rolling_kurt(base, 126)

def csdr_375_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 124 cross sectional distress rank over 252d to capture explosive breakdown or reversal points.
    """
    base = _rank_pct(close.pct_change(110), 252)
    return _rolling_kurt(base, 252)
