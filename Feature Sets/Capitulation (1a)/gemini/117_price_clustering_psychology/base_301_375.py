"""
117_117_price_clustering_psychology — Base Features 301-375
Domain: 117_price_clustering_psychology
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

def ppsy_301_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 117 price clustering psychology over 5d to capture explosive breakdown or reversal points.
    """
    base = np.abs(close - close.rolling(45).mean())
    return _rolling_kurt(base, 5)

def ppsy_302_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 117 price clustering psychology over 21d to capture explosive breakdown or reversal points.
    """
    base = np.abs(close - close.rolling(45).mean())
    return _rolling_kurt(base, 21)

def ppsy_303_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 117 price clustering psychology over 63d to capture explosive breakdown or reversal points.
    """
    base = np.abs(close - close.rolling(45).mean())
    return _rolling_kurt(base, 63)

def ppsy_304_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 117 price clustering psychology over 126d to capture explosive breakdown or reversal points.
    """
    base = np.abs(close - close.rolling(45).mean())
    return _rolling_kurt(base, 126)

def ppsy_305_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 117 price clustering psychology over 252d to capture explosive breakdown or reversal points.
    """
    base = np.abs(close - close.rolling(45).mean())
    return _rolling_kurt(base, 252)

def ppsy_306_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 117 price clustering psychology for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = np.abs(close - close.rolling(45).mean())
    return _safe_div(base, _rolling_std(base, 5))

def ppsy_307_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 117 price clustering psychology for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = np.abs(close - close.rolling(45).mean())
    return _safe_div(base, _rolling_std(base, 21))

def ppsy_308_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 117 price clustering psychology for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = np.abs(close - close.rolling(45).mean())
    return _safe_div(base, _rolling_std(base, 63))

def ppsy_309_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 117 price clustering psychology for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = np.abs(close - close.rolling(45).mean())
    return _safe_div(base, _rolling_std(base, 126))

def ppsy_310_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 117 price clustering psychology for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = np.abs(close - close.rolling(45).mean())
    return _safe_div(base, _rolling_std(base, 252))

def ppsy_311_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 117 price clustering psychology over 5d to stabilize variance and capture exponential shifts.
    """
    base = np.abs(close - close.rolling(45).mean())
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def ppsy_312_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 117 price clustering psychology over 21d to stabilize variance and capture exponential shifts.
    """
    base = np.abs(close - close.rolling(45).mean())
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def ppsy_313_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 117 price clustering psychology over 63d to stabilize variance and capture exponential shifts.
    """
    base = np.abs(close - close.rolling(45).mean())
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def ppsy_314_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 117 price clustering psychology over 126d to stabilize variance and capture exponential shifts.
    """
    base = np.abs(close - close.rolling(45).mean())
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def ppsy_315_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 117 price clustering psychology over 252d to stabilize variance and capture exponential shifts.
    """
    base = np.abs(close - close.rolling(45).mean())
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def ppsy_316_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 117 price clustering psychology over a 5d horizon to identify extreme regimes.
    """
    base = np.abs(close - close.rolling(50).mean())
    return _rolling_mean(base, 5)

def ppsy_317_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 117 price clustering psychology over a 21d horizon to identify extreme regimes.
    """
    base = np.abs(close - close.rolling(50).mean())
    return _rolling_mean(base, 21)

def ppsy_318_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 117 price clustering psychology over a 63d horizon to identify extreme regimes.
    """
    base = np.abs(close - close.rolling(50).mean())
    return _rolling_mean(base, 63)

def ppsy_319_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 117 price clustering psychology over a 126d horizon to identify extreme regimes.
    """
    base = np.abs(close - close.rolling(50).mean())
    return _rolling_mean(base, 126)

def ppsy_320_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 117 price clustering psychology over a 252d horizon to identify extreme regimes.
    """
    base = np.abs(close - close.rolling(50).mean())
    return _rolling_mean(base, 252)

def ppsy_321_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 117 price clustering psychology by measuring deviations from the 5d mean.
    """
    base = np.abs(close - close.rolling(50).mean())
    return _zscore_rolling(base, 5)

def ppsy_322_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 117 price clustering psychology by measuring deviations from the 21d mean.
    """
    base = np.abs(close - close.rolling(50).mean())
    return _zscore_rolling(base, 21)

def ppsy_323_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 117 price clustering psychology by measuring deviations from the 63d mean.
    """
    base = np.abs(close - close.rolling(50).mean())
    return _zscore_rolling(base, 63)

def ppsy_324_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 117 price clustering psychology by measuring deviations from the 126d mean.
    """
    base = np.abs(close - close.rolling(50).mean())
    return _zscore_rolling(base, 126)

def ppsy_325_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 117 price clustering psychology by measuring deviations from the 252d mean.
    """
    base = np.abs(close - close.rolling(50).mean())
    return _zscore_rolling(base, 252)

def ppsy_326_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 117 price clustering psychology to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = np.abs(close - close.rolling(50).mean())
    return _rank_pct(base, 5)

def ppsy_327_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 117 price clustering psychology to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = np.abs(close - close.rolling(50).mean())
    return _rank_pct(base, 21)

def ppsy_328_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 117 price clustering psychology to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = np.abs(close - close.rolling(50).mean())
    return _rank_pct(base, 63)

def ppsy_329_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 117 price clustering psychology to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = np.abs(close - close.rolling(50).mean())
    return _rank_pct(base, 126)

def ppsy_330_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 117 price clustering psychology to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = np.abs(close - close.rolling(50).mean())
    return _rank_pct(base, 252)

def ppsy_331_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 117 price clustering psychology distribution over 5d to detect tail risk or exhaustion.
    """
    base = np.abs(close - close.rolling(50).mean())
    return _rolling_skew(base, 5)

def ppsy_332_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 117 price clustering psychology distribution over 21d to detect tail risk or exhaustion.
    """
    base = np.abs(close - close.rolling(50).mean())
    return _rolling_skew(base, 21)

def ppsy_333_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 117 price clustering psychology distribution over 63d to detect tail risk or exhaustion.
    """
    base = np.abs(close - close.rolling(50).mean())
    return _rolling_skew(base, 63)

def ppsy_334_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 117 price clustering psychology distribution over 126d to detect tail risk or exhaustion.
    """
    base = np.abs(close - close.rolling(50).mean())
    return _rolling_skew(base, 126)

def ppsy_335_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 117 price clustering psychology distribution over 252d to detect tail risk or exhaustion.
    """
    base = np.abs(close - close.rolling(50).mean())
    return _rolling_skew(base, 252)

def ppsy_336_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 117 price clustering psychology over 5d to capture explosive breakdown or reversal points.
    """
    base = np.abs(close - close.rolling(50).mean())
    return _rolling_kurt(base, 5)

def ppsy_337_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 117 price clustering psychology over 21d to capture explosive breakdown or reversal points.
    """
    base = np.abs(close - close.rolling(50).mean())
    return _rolling_kurt(base, 21)

def ppsy_338_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 117 price clustering psychology over 63d to capture explosive breakdown or reversal points.
    """
    base = np.abs(close - close.rolling(50).mean())
    return _rolling_kurt(base, 63)

def ppsy_339_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 117 price clustering psychology over 126d to capture explosive breakdown or reversal points.
    """
    base = np.abs(close - close.rolling(50).mean())
    return _rolling_kurt(base, 126)

def ppsy_340_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 117 price clustering psychology over 252d to capture explosive breakdown or reversal points.
    """
    base = np.abs(close - close.rolling(50).mean())
    return _rolling_kurt(base, 252)

def ppsy_341_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 117 price clustering psychology for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = np.abs(close - close.rolling(50).mean())
    return _safe_div(base, _rolling_std(base, 5))

def ppsy_342_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 117 price clustering psychology for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = np.abs(close - close.rolling(50).mean())
    return _safe_div(base, _rolling_std(base, 21))

def ppsy_343_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 117 price clustering psychology for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = np.abs(close - close.rolling(50).mean())
    return _safe_div(base, _rolling_std(base, 63))

def ppsy_344_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 117 price clustering psychology for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = np.abs(close - close.rolling(50).mean())
    return _safe_div(base, _rolling_std(base, 126))

def ppsy_345_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 117 price clustering psychology for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = np.abs(close - close.rolling(50).mean())
    return _safe_div(base, _rolling_std(base, 252))

def ppsy_346_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 117 price clustering psychology over 5d to stabilize variance and capture exponential shifts.
    """
    base = np.abs(close - close.rolling(50).mean())
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def ppsy_347_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 117 price clustering psychology over 21d to stabilize variance and capture exponential shifts.
    """
    base = np.abs(close - close.rolling(50).mean())
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def ppsy_348_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 117 price clustering psychology over 63d to stabilize variance and capture exponential shifts.
    """
    base = np.abs(close - close.rolling(50).mean())
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def ppsy_349_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 117 price clustering psychology over 126d to stabilize variance and capture exponential shifts.
    """
    base = np.abs(close - close.rolling(50).mean())
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def ppsy_350_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 117 price clustering psychology over 252d to stabilize variance and capture exponential shifts.
    """
    base = np.abs(close - close.rolling(50).mean())
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def ppsy_351_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 117 price clustering psychology over a 5d horizon to identify extreme regimes.
    """
    base = np.abs(close - close.rolling(55).mean())
    return _rolling_mean(base, 5)

def ppsy_352_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 117 price clustering psychology over a 21d horizon to identify extreme regimes.
    """
    base = np.abs(close - close.rolling(55).mean())
    return _rolling_mean(base, 21)

def ppsy_353_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 117 price clustering psychology over a 63d horizon to identify extreme regimes.
    """
    base = np.abs(close - close.rolling(55).mean())
    return _rolling_mean(base, 63)

def ppsy_354_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 117 price clustering psychology over a 126d horizon to identify extreme regimes.
    """
    base = np.abs(close - close.rolling(55).mean())
    return _rolling_mean(base, 126)

def ppsy_355_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 117 price clustering psychology over a 252d horizon to identify extreme regimes.
    """
    base = np.abs(close - close.rolling(55).mean())
    return _rolling_mean(base, 252)

def ppsy_356_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 117 price clustering psychology by measuring deviations from the 5d mean.
    """
    base = np.abs(close - close.rolling(55).mean())
    return _zscore_rolling(base, 5)

def ppsy_357_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 117 price clustering psychology by measuring deviations from the 21d mean.
    """
    base = np.abs(close - close.rolling(55).mean())
    return _zscore_rolling(base, 21)

def ppsy_358_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 117 price clustering psychology by measuring deviations from the 63d mean.
    """
    base = np.abs(close - close.rolling(55).mean())
    return _zscore_rolling(base, 63)

def ppsy_359_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 117 price clustering psychology by measuring deviations from the 126d mean.
    """
    base = np.abs(close - close.rolling(55).mean())
    return _zscore_rolling(base, 126)

def ppsy_360_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 117 price clustering psychology by measuring deviations from the 252d mean.
    """
    base = np.abs(close - close.rolling(55).mean())
    return _zscore_rolling(base, 252)

def ppsy_361_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 117 price clustering psychology to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = np.abs(close - close.rolling(55).mean())
    return _rank_pct(base, 5)

def ppsy_362_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 117 price clustering psychology to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = np.abs(close - close.rolling(55).mean())
    return _rank_pct(base, 21)

def ppsy_363_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 117 price clustering psychology to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = np.abs(close - close.rolling(55).mean())
    return _rank_pct(base, 63)

def ppsy_364_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 117 price clustering psychology to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = np.abs(close - close.rolling(55).mean())
    return _rank_pct(base, 126)

def ppsy_365_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 117 price clustering psychology to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = np.abs(close - close.rolling(55).mean())
    return _rank_pct(base, 252)

def ppsy_366_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 117 price clustering psychology distribution over 5d to detect tail risk or exhaustion.
    """
    base = np.abs(close - close.rolling(55).mean())
    return _rolling_skew(base, 5)

def ppsy_367_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 117 price clustering psychology distribution over 21d to detect tail risk or exhaustion.
    """
    base = np.abs(close - close.rolling(55).mean())
    return _rolling_skew(base, 21)

def ppsy_368_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 117 price clustering psychology distribution over 63d to detect tail risk or exhaustion.
    """
    base = np.abs(close - close.rolling(55).mean())
    return _rolling_skew(base, 63)

def ppsy_369_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 117 price clustering psychology distribution over 126d to detect tail risk or exhaustion.
    """
    base = np.abs(close - close.rolling(55).mean())
    return _rolling_skew(base, 126)

def ppsy_370_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 117 price clustering psychology distribution over 252d to detect tail risk or exhaustion.
    """
    base = np.abs(close - close.rolling(55).mean())
    return _rolling_skew(base, 252)

def ppsy_371_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 117 price clustering psychology over 5d to capture explosive breakdown or reversal points.
    """
    base = np.abs(close - close.rolling(55).mean())
    return _rolling_kurt(base, 5)

def ppsy_372_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 117 price clustering psychology over 21d to capture explosive breakdown or reversal points.
    """
    base = np.abs(close - close.rolling(55).mean())
    return _rolling_kurt(base, 21)

def ppsy_373_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 117 price clustering psychology over 63d to capture explosive breakdown or reversal points.
    """
    base = np.abs(close - close.rolling(55).mean())
    return _rolling_kurt(base, 63)

def ppsy_374_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 117 price clustering psychology over 126d to capture explosive breakdown or reversal points.
    """
    base = np.abs(close - close.rolling(55).mean())
    return _rolling_kurt(base, 126)

def ppsy_375_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 117 price clustering psychology over 252d to capture explosive breakdown or reversal points.
    """
    base = np.abs(close - close.rolling(55).mean())
    return _rolling_kurt(base, 252)
