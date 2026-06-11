"""
45_45_panic_bar_signatures — Base Features 301-375
Domain: 45_panic_bar_signatures
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

def pans_301_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 45 panic bar signatures over 5d to capture explosive breakdown or reversal points.
    """
    base = ((close - open).abs().rolling(45).mean())
    return _rolling_kurt(base, 5)

def pans_302_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 45 panic bar signatures over 21d to capture explosive breakdown or reversal points.
    """
    base = ((close - open).abs().rolling(45).mean())
    return _rolling_kurt(base, 21)

def pans_303_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 45 panic bar signatures over 63d to capture explosive breakdown or reversal points.
    """
    base = ((close - open).abs().rolling(45).mean())
    return _rolling_kurt(base, 63)

def pans_304_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 45 panic bar signatures over 126d to capture explosive breakdown or reversal points.
    """
    base = ((close - open).abs().rolling(45).mean())
    return _rolling_kurt(base, 126)

def pans_305_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 45 panic bar signatures over 252d to capture explosive breakdown or reversal points.
    """
    base = ((close - open).abs().rolling(45).mean())
    return _rolling_kurt(base, 252)

def pans_306_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 45 panic bar signatures for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = ((close - open).abs().rolling(45).mean())
    return _safe_div(base, _rolling_std(base, 5))

def pans_307_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 45 panic bar signatures for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = ((close - open).abs().rolling(45).mean())
    return _safe_div(base, _rolling_std(base, 21))

def pans_308_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 45 panic bar signatures for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = ((close - open).abs().rolling(45).mean())
    return _safe_div(base, _rolling_std(base, 63))

def pans_309_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 45 panic bar signatures for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = ((close - open).abs().rolling(45).mean())
    return _safe_div(base, _rolling_std(base, 126))

def pans_310_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 45 panic bar signatures for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = ((close - open).abs().rolling(45).mean())
    return _safe_div(base, _rolling_std(base, 252))

def pans_311_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 45 panic bar signatures over 5d to stabilize variance and capture exponential shifts.
    """
    base = ((close - open).abs().rolling(45).mean())
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def pans_312_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 45 panic bar signatures over 21d to stabilize variance and capture exponential shifts.
    """
    base = ((close - open).abs().rolling(45).mean())
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def pans_313_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 45 panic bar signatures over 63d to stabilize variance and capture exponential shifts.
    """
    base = ((close - open).abs().rolling(45).mean())
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def pans_314_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 45 panic bar signatures over 126d to stabilize variance and capture exponential shifts.
    """
    base = ((close - open).abs().rolling(45).mean())
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def pans_315_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 45 panic bar signatures over 252d to stabilize variance and capture exponential shifts.
    """
    base = ((close - open).abs().rolling(45).mean())
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def pans_316_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 45 panic bar signatures over a 5d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(50).mean())
    return _rolling_mean(base, 5)

def pans_317_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 45 panic bar signatures over a 21d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(50).mean())
    return _rolling_mean(base, 21)

def pans_318_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 45 panic bar signatures over a 63d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(50).mean())
    return _rolling_mean(base, 63)

def pans_319_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 45 panic bar signatures over a 126d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(50).mean())
    return _rolling_mean(base, 126)

def pans_320_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 45 panic bar signatures over a 252d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(50).mean())
    return _rolling_mean(base, 252)

def pans_321_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 45 panic bar signatures by measuring deviations from the 5d mean.
    """
    base = ((close - open).abs().rolling(50).mean())
    return _zscore_rolling(base, 5)

def pans_322_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 45 panic bar signatures by measuring deviations from the 21d mean.
    """
    base = ((close - open).abs().rolling(50).mean())
    return _zscore_rolling(base, 21)

def pans_323_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 45 panic bar signatures by measuring deviations from the 63d mean.
    """
    base = ((close - open).abs().rolling(50).mean())
    return _zscore_rolling(base, 63)

def pans_324_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 45 panic bar signatures by measuring deviations from the 126d mean.
    """
    base = ((close - open).abs().rolling(50).mean())
    return _zscore_rolling(base, 126)

def pans_325_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 45 panic bar signatures by measuring deviations from the 252d mean.
    """
    base = ((close - open).abs().rolling(50).mean())
    return _zscore_rolling(base, 252)

def pans_326_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 45 panic bar signatures to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = ((close - open).abs().rolling(50).mean())
    return _rank_pct(base, 5)

def pans_327_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 45 panic bar signatures to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = ((close - open).abs().rolling(50).mean())
    return _rank_pct(base, 21)

def pans_328_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 45 panic bar signatures to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = ((close - open).abs().rolling(50).mean())
    return _rank_pct(base, 63)

def pans_329_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 45 panic bar signatures to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = ((close - open).abs().rolling(50).mean())
    return _rank_pct(base, 126)

def pans_330_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 45 panic bar signatures to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = ((close - open).abs().rolling(50).mean())
    return _rank_pct(base, 252)

def pans_331_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 45 panic bar signatures distribution over 5d to detect tail risk or exhaustion.
    """
    base = ((close - open).abs().rolling(50).mean())
    return _rolling_skew(base, 5)

def pans_332_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 45 panic bar signatures distribution over 21d to detect tail risk or exhaustion.
    """
    base = ((close - open).abs().rolling(50).mean())
    return _rolling_skew(base, 21)

def pans_333_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 45 panic bar signatures distribution over 63d to detect tail risk or exhaustion.
    """
    base = ((close - open).abs().rolling(50).mean())
    return _rolling_skew(base, 63)

def pans_334_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 45 panic bar signatures distribution over 126d to detect tail risk or exhaustion.
    """
    base = ((close - open).abs().rolling(50).mean())
    return _rolling_skew(base, 126)

def pans_335_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 45 panic bar signatures distribution over 252d to detect tail risk or exhaustion.
    """
    base = ((close - open).abs().rolling(50).mean())
    return _rolling_skew(base, 252)

def pans_336_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 45 panic bar signatures over 5d to capture explosive breakdown or reversal points.
    """
    base = ((close - open).abs().rolling(50).mean())
    return _rolling_kurt(base, 5)

def pans_337_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 45 panic bar signatures over 21d to capture explosive breakdown or reversal points.
    """
    base = ((close - open).abs().rolling(50).mean())
    return _rolling_kurt(base, 21)

def pans_338_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 45 panic bar signatures over 63d to capture explosive breakdown or reversal points.
    """
    base = ((close - open).abs().rolling(50).mean())
    return _rolling_kurt(base, 63)

def pans_339_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 45 panic bar signatures over 126d to capture explosive breakdown or reversal points.
    """
    base = ((close - open).abs().rolling(50).mean())
    return _rolling_kurt(base, 126)

def pans_340_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 45 panic bar signatures over 252d to capture explosive breakdown or reversal points.
    """
    base = ((close - open).abs().rolling(50).mean())
    return _rolling_kurt(base, 252)

def pans_341_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 45 panic bar signatures for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = ((close - open).abs().rolling(50).mean())
    return _safe_div(base, _rolling_std(base, 5))

def pans_342_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 45 panic bar signatures for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = ((close - open).abs().rolling(50).mean())
    return _safe_div(base, _rolling_std(base, 21))

def pans_343_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 45 panic bar signatures for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = ((close - open).abs().rolling(50).mean())
    return _safe_div(base, _rolling_std(base, 63))

def pans_344_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 45 panic bar signatures for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = ((close - open).abs().rolling(50).mean())
    return _safe_div(base, _rolling_std(base, 126))

def pans_345_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 45 panic bar signatures for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = ((close - open).abs().rolling(50).mean())
    return _safe_div(base, _rolling_std(base, 252))

def pans_346_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 45 panic bar signatures over 5d to stabilize variance and capture exponential shifts.
    """
    base = ((close - open).abs().rolling(50).mean())
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def pans_347_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 45 panic bar signatures over 21d to stabilize variance and capture exponential shifts.
    """
    base = ((close - open).abs().rolling(50).mean())
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def pans_348_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 45 panic bar signatures over 63d to stabilize variance and capture exponential shifts.
    """
    base = ((close - open).abs().rolling(50).mean())
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def pans_349_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 45 panic bar signatures over 126d to stabilize variance and capture exponential shifts.
    """
    base = ((close - open).abs().rolling(50).mean())
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def pans_350_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 45 panic bar signatures over 252d to stabilize variance and capture exponential shifts.
    """
    base = ((close - open).abs().rolling(50).mean())
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def pans_351_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 45 panic bar signatures over a 5d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(55).mean())
    return _rolling_mean(base, 5)

def pans_352_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 45 panic bar signatures over a 21d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(55).mean())
    return _rolling_mean(base, 21)

def pans_353_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 45 panic bar signatures over a 63d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(55).mean())
    return _rolling_mean(base, 63)

def pans_354_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 45 panic bar signatures over a 126d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(55).mean())
    return _rolling_mean(base, 126)

def pans_355_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 45 panic bar signatures over a 252d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(55).mean())
    return _rolling_mean(base, 252)

def pans_356_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 45 panic bar signatures by measuring deviations from the 5d mean.
    """
    base = ((close - open).abs().rolling(55).mean())
    return _zscore_rolling(base, 5)

def pans_357_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 45 panic bar signatures by measuring deviations from the 21d mean.
    """
    base = ((close - open).abs().rolling(55).mean())
    return _zscore_rolling(base, 21)

def pans_358_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 45 panic bar signatures by measuring deviations from the 63d mean.
    """
    base = ((close - open).abs().rolling(55).mean())
    return _zscore_rolling(base, 63)

def pans_359_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 45 panic bar signatures by measuring deviations from the 126d mean.
    """
    base = ((close - open).abs().rolling(55).mean())
    return _zscore_rolling(base, 126)

def pans_360_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 45 panic bar signatures by measuring deviations from the 252d mean.
    """
    base = ((close - open).abs().rolling(55).mean())
    return _zscore_rolling(base, 252)

def pans_361_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 45 panic bar signatures to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = ((close - open).abs().rolling(55).mean())
    return _rank_pct(base, 5)

def pans_362_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 45 panic bar signatures to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = ((close - open).abs().rolling(55).mean())
    return _rank_pct(base, 21)

def pans_363_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 45 panic bar signatures to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = ((close - open).abs().rolling(55).mean())
    return _rank_pct(base, 63)

def pans_364_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 45 panic bar signatures to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = ((close - open).abs().rolling(55).mean())
    return _rank_pct(base, 126)

def pans_365_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 45 panic bar signatures to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = ((close - open).abs().rolling(55).mean())
    return _rank_pct(base, 252)

def pans_366_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 45 panic bar signatures distribution over 5d to detect tail risk or exhaustion.
    """
    base = ((close - open).abs().rolling(55).mean())
    return _rolling_skew(base, 5)

def pans_367_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 45 panic bar signatures distribution over 21d to detect tail risk or exhaustion.
    """
    base = ((close - open).abs().rolling(55).mean())
    return _rolling_skew(base, 21)

def pans_368_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 45 panic bar signatures distribution over 63d to detect tail risk or exhaustion.
    """
    base = ((close - open).abs().rolling(55).mean())
    return _rolling_skew(base, 63)

def pans_369_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 45 panic bar signatures distribution over 126d to detect tail risk or exhaustion.
    """
    base = ((close - open).abs().rolling(55).mean())
    return _rolling_skew(base, 126)

def pans_370_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 45 panic bar signatures distribution over 252d to detect tail risk or exhaustion.
    """
    base = ((close - open).abs().rolling(55).mean())
    return _rolling_skew(base, 252)

def pans_371_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 45 panic bar signatures over 5d to capture explosive breakdown or reversal points.
    """
    base = ((close - open).abs().rolling(55).mean())
    return _rolling_kurt(base, 5)

def pans_372_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 45 panic bar signatures over 21d to capture explosive breakdown or reversal points.
    """
    base = ((close - open).abs().rolling(55).mean())
    return _rolling_kurt(base, 21)

def pans_373_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 45 panic bar signatures over 63d to capture explosive breakdown or reversal points.
    """
    base = ((close - open).abs().rolling(55).mean())
    return _rolling_kurt(base, 63)

def pans_374_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 45 panic bar signatures over 126d to capture explosive breakdown or reversal points.
    """
    base = ((close - open).abs().rolling(55).mean())
    return _rolling_kurt(base, 126)

def pans_375_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 45 panic bar signatures over 252d to capture explosive breakdown or reversal points.
    """
    base = ((close - open).abs().rolling(55).mean())
    return _rolling_kurt(base, 252)
