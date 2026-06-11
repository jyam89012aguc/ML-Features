"""
47_47_gap_down_clustering — Base Features 301-375
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

def gapc_301_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 47 gap down clustering over 5d to capture explosive breakdown or reversal points.
    """
    base = ((close - open).abs().rolling(45).mean())
    return _rolling_kurt(base, 5)

def gapc_302_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 47 gap down clustering over 21d to capture explosive breakdown or reversal points.
    """
    base = ((close - open).abs().rolling(45).mean())
    return _rolling_kurt(base, 21)

def gapc_303_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 47 gap down clustering over 63d to capture explosive breakdown or reversal points.
    """
    base = ((close - open).abs().rolling(45).mean())
    return _rolling_kurt(base, 63)

def gapc_304_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 47 gap down clustering over 126d to capture explosive breakdown or reversal points.
    """
    base = ((close - open).abs().rolling(45).mean())
    return _rolling_kurt(base, 126)

def gapc_305_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 47 gap down clustering over 252d to capture explosive breakdown or reversal points.
    """
    base = ((close - open).abs().rolling(45).mean())
    return _rolling_kurt(base, 252)

def gapc_306_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 47 gap down clustering for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = ((close - open).abs().rolling(45).mean())
    return _safe_div(base, _rolling_std(base, 5))

def gapc_307_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 47 gap down clustering for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = ((close - open).abs().rolling(45).mean())
    return _safe_div(base, _rolling_std(base, 21))

def gapc_308_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 47 gap down clustering for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = ((close - open).abs().rolling(45).mean())
    return _safe_div(base, _rolling_std(base, 63))

def gapc_309_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 47 gap down clustering for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = ((close - open).abs().rolling(45).mean())
    return _safe_div(base, _rolling_std(base, 126))

def gapc_310_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 47 gap down clustering for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = ((close - open).abs().rolling(45).mean())
    return _safe_div(base, _rolling_std(base, 252))

def gapc_311_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 47 gap down clustering over 5d to stabilize variance and capture exponential shifts.
    """
    base = ((close - open).abs().rolling(45).mean())
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def gapc_312_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 47 gap down clustering over 21d to stabilize variance and capture exponential shifts.
    """
    base = ((close - open).abs().rolling(45).mean())
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def gapc_313_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 47 gap down clustering over 63d to stabilize variance and capture exponential shifts.
    """
    base = ((close - open).abs().rolling(45).mean())
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def gapc_314_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 47 gap down clustering over 126d to stabilize variance and capture exponential shifts.
    """
    base = ((close - open).abs().rolling(45).mean())
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def gapc_315_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 47 gap down clustering over 252d to stabilize variance and capture exponential shifts.
    """
    base = ((close - open).abs().rolling(45).mean())
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def gapc_316_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 47 gap down clustering over a 5d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(50).mean())
    return _rolling_mean(base, 5)

def gapc_317_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 47 gap down clustering over a 21d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(50).mean())
    return _rolling_mean(base, 21)

def gapc_318_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 47 gap down clustering over a 63d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(50).mean())
    return _rolling_mean(base, 63)

def gapc_319_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 47 gap down clustering over a 126d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(50).mean())
    return _rolling_mean(base, 126)

def gapc_320_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 47 gap down clustering over a 252d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(50).mean())
    return _rolling_mean(base, 252)

def gapc_321_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 47 gap down clustering by measuring deviations from the 5d mean.
    """
    base = ((close - open).abs().rolling(50).mean())
    return _zscore_rolling(base, 5)

def gapc_322_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 47 gap down clustering by measuring deviations from the 21d mean.
    """
    base = ((close - open).abs().rolling(50).mean())
    return _zscore_rolling(base, 21)

def gapc_323_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 47 gap down clustering by measuring deviations from the 63d mean.
    """
    base = ((close - open).abs().rolling(50).mean())
    return _zscore_rolling(base, 63)

def gapc_324_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 47 gap down clustering by measuring deviations from the 126d mean.
    """
    base = ((close - open).abs().rolling(50).mean())
    return _zscore_rolling(base, 126)

def gapc_325_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 47 gap down clustering by measuring deviations from the 252d mean.
    """
    base = ((close - open).abs().rolling(50).mean())
    return _zscore_rolling(base, 252)

def gapc_326_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 47 gap down clustering to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = ((close - open).abs().rolling(50).mean())
    return _rank_pct(base, 5)

def gapc_327_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 47 gap down clustering to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = ((close - open).abs().rolling(50).mean())
    return _rank_pct(base, 21)

def gapc_328_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 47 gap down clustering to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = ((close - open).abs().rolling(50).mean())
    return _rank_pct(base, 63)

def gapc_329_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 47 gap down clustering to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = ((close - open).abs().rolling(50).mean())
    return _rank_pct(base, 126)

def gapc_330_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 47 gap down clustering to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = ((close - open).abs().rolling(50).mean())
    return _rank_pct(base, 252)

def gapc_331_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 47 gap down clustering distribution over 5d to detect tail risk or exhaustion.
    """
    base = ((close - open).abs().rolling(50).mean())
    return _rolling_skew(base, 5)

def gapc_332_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 47 gap down clustering distribution over 21d to detect tail risk or exhaustion.
    """
    base = ((close - open).abs().rolling(50).mean())
    return _rolling_skew(base, 21)

def gapc_333_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 47 gap down clustering distribution over 63d to detect tail risk or exhaustion.
    """
    base = ((close - open).abs().rolling(50).mean())
    return _rolling_skew(base, 63)

def gapc_334_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 47 gap down clustering distribution over 126d to detect tail risk or exhaustion.
    """
    base = ((close - open).abs().rolling(50).mean())
    return _rolling_skew(base, 126)

def gapc_335_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 47 gap down clustering distribution over 252d to detect tail risk or exhaustion.
    """
    base = ((close - open).abs().rolling(50).mean())
    return _rolling_skew(base, 252)

def gapc_336_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 47 gap down clustering over 5d to capture explosive breakdown or reversal points.
    """
    base = ((close - open).abs().rolling(50).mean())
    return _rolling_kurt(base, 5)

def gapc_337_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 47 gap down clustering over 21d to capture explosive breakdown or reversal points.
    """
    base = ((close - open).abs().rolling(50).mean())
    return _rolling_kurt(base, 21)

def gapc_338_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 47 gap down clustering over 63d to capture explosive breakdown or reversal points.
    """
    base = ((close - open).abs().rolling(50).mean())
    return _rolling_kurt(base, 63)

def gapc_339_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 47 gap down clustering over 126d to capture explosive breakdown or reversal points.
    """
    base = ((close - open).abs().rolling(50).mean())
    return _rolling_kurt(base, 126)

def gapc_340_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 47 gap down clustering over 252d to capture explosive breakdown or reversal points.
    """
    base = ((close - open).abs().rolling(50).mean())
    return _rolling_kurt(base, 252)

def gapc_341_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 47 gap down clustering for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = ((close - open).abs().rolling(50).mean())
    return _safe_div(base, _rolling_std(base, 5))

def gapc_342_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 47 gap down clustering for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = ((close - open).abs().rolling(50).mean())
    return _safe_div(base, _rolling_std(base, 21))

def gapc_343_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 47 gap down clustering for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = ((close - open).abs().rolling(50).mean())
    return _safe_div(base, _rolling_std(base, 63))

def gapc_344_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 47 gap down clustering for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = ((close - open).abs().rolling(50).mean())
    return _safe_div(base, _rolling_std(base, 126))

def gapc_345_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 47 gap down clustering for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = ((close - open).abs().rolling(50).mean())
    return _safe_div(base, _rolling_std(base, 252))

def gapc_346_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 47 gap down clustering over 5d to stabilize variance and capture exponential shifts.
    """
    base = ((close - open).abs().rolling(50).mean())
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def gapc_347_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 47 gap down clustering over 21d to stabilize variance and capture exponential shifts.
    """
    base = ((close - open).abs().rolling(50).mean())
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def gapc_348_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 47 gap down clustering over 63d to stabilize variance and capture exponential shifts.
    """
    base = ((close - open).abs().rolling(50).mean())
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def gapc_349_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 47 gap down clustering over 126d to stabilize variance and capture exponential shifts.
    """
    base = ((close - open).abs().rolling(50).mean())
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def gapc_350_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 47 gap down clustering over 252d to stabilize variance and capture exponential shifts.
    """
    base = ((close - open).abs().rolling(50).mean())
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def gapc_351_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 47 gap down clustering over a 5d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(55).mean())
    return _rolling_mean(base, 5)

def gapc_352_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 47 gap down clustering over a 21d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(55).mean())
    return _rolling_mean(base, 21)

def gapc_353_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 47 gap down clustering over a 63d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(55).mean())
    return _rolling_mean(base, 63)

def gapc_354_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 47 gap down clustering over a 126d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(55).mean())
    return _rolling_mean(base, 126)

def gapc_355_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 47 gap down clustering over a 252d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(55).mean())
    return _rolling_mean(base, 252)

def gapc_356_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 47 gap down clustering by measuring deviations from the 5d mean.
    """
    base = ((close - open).abs().rolling(55).mean())
    return _zscore_rolling(base, 5)

def gapc_357_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 47 gap down clustering by measuring deviations from the 21d mean.
    """
    base = ((close - open).abs().rolling(55).mean())
    return _zscore_rolling(base, 21)

def gapc_358_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 47 gap down clustering by measuring deviations from the 63d mean.
    """
    base = ((close - open).abs().rolling(55).mean())
    return _zscore_rolling(base, 63)

def gapc_359_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 47 gap down clustering by measuring deviations from the 126d mean.
    """
    base = ((close - open).abs().rolling(55).mean())
    return _zscore_rolling(base, 126)

def gapc_360_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 47 gap down clustering by measuring deviations from the 252d mean.
    """
    base = ((close - open).abs().rolling(55).mean())
    return _zscore_rolling(base, 252)

def gapc_361_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 47 gap down clustering to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = ((close - open).abs().rolling(55).mean())
    return _rank_pct(base, 5)

def gapc_362_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 47 gap down clustering to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = ((close - open).abs().rolling(55).mean())
    return _rank_pct(base, 21)

def gapc_363_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 47 gap down clustering to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = ((close - open).abs().rolling(55).mean())
    return _rank_pct(base, 63)

def gapc_364_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 47 gap down clustering to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = ((close - open).abs().rolling(55).mean())
    return _rank_pct(base, 126)

def gapc_365_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 47 gap down clustering to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = ((close - open).abs().rolling(55).mean())
    return _rank_pct(base, 252)

def gapc_366_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 47 gap down clustering distribution over 5d to detect tail risk or exhaustion.
    """
    base = ((close - open).abs().rolling(55).mean())
    return _rolling_skew(base, 5)

def gapc_367_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 47 gap down clustering distribution over 21d to detect tail risk or exhaustion.
    """
    base = ((close - open).abs().rolling(55).mean())
    return _rolling_skew(base, 21)

def gapc_368_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 47 gap down clustering distribution over 63d to detect tail risk or exhaustion.
    """
    base = ((close - open).abs().rolling(55).mean())
    return _rolling_skew(base, 63)

def gapc_369_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 47 gap down clustering distribution over 126d to detect tail risk or exhaustion.
    """
    base = ((close - open).abs().rolling(55).mean())
    return _rolling_skew(base, 126)

def gapc_370_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 47 gap down clustering distribution over 252d to detect tail risk or exhaustion.
    """
    base = ((close - open).abs().rolling(55).mean())
    return _rolling_skew(base, 252)

def gapc_371_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 47 gap down clustering over 5d to capture explosive breakdown or reversal points.
    """
    base = ((close - open).abs().rolling(55).mean())
    return _rolling_kurt(base, 5)

def gapc_372_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 47 gap down clustering over 21d to capture explosive breakdown or reversal points.
    """
    base = ((close - open).abs().rolling(55).mean())
    return _rolling_kurt(base, 21)

def gapc_373_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 47 gap down clustering over 63d to capture explosive breakdown or reversal points.
    """
    base = ((close - open).abs().rolling(55).mean())
    return _rolling_kurt(base, 63)

def gapc_374_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 47 gap down clustering over 126d to capture explosive breakdown or reversal points.
    """
    base = ((close - open).abs().rolling(55).mean())
    return _rolling_kurt(base, 126)

def gapc_375_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 47 gap down clustering over 252d to capture explosive breakdown or reversal points.
    """
    base = ((close - open).abs().rolling(55).mean())
    return _rolling_kurt(base, 252)
