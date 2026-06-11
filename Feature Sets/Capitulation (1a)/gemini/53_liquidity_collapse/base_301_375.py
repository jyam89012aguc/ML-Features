"""
53_53_liquidity_collapse — Base Features 301-375
Domain: 53_liquidity_collapse
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

def lcol_301_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 53 liquidity collapse over 5d to capture explosive breakdown or reversal points.
    """
    base = (volume.pct_change(9).rolling(45).mean())
    return _rolling_kurt(base, 5)

def lcol_302_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 53 liquidity collapse over 21d to capture explosive breakdown or reversal points.
    """
    base = (volume.pct_change(9).rolling(45).mean())
    return _rolling_kurt(base, 21)

def lcol_303_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 53 liquidity collapse over 63d to capture explosive breakdown or reversal points.
    """
    base = (volume.pct_change(9).rolling(45).mean())
    return _rolling_kurt(base, 63)

def lcol_304_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 53 liquidity collapse over 126d to capture explosive breakdown or reversal points.
    """
    base = (volume.pct_change(9).rolling(45).mean())
    return _rolling_kurt(base, 126)

def lcol_305_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 53 liquidity collapse over 252d to capture explosive breakdown or reversal points.
    """
    base = (volume.pct_change(9).rolling(45).mean())
    return _rolling_kurt(base, 252)

def lcol_306_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 53 liquidity collapse for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = (volume.pct_change(9).rolling(45).mean())
    return _safe_div(base, _rolling_std(base, 5))

def lcol_307_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 53 liquidity collapse for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = (volume.pct_change(9).rolling(45).mean())
    return _safe_div(base, _rolling_std(base, 21))

def lcol_308_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 53 liquidity collapse for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = (volume.pct_change(9).rolling(45).mean())
    return _safe_div(base, _rolling_std(base, 63))

def lcol_309_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 53 liquidity collapse for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = (volume.pct_change(9).rolling(45).mean())
    return _safe_div(base, _rolling_std(base, 126))

def lcol_310_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 53 liquidity collapse for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = (volume.pct_change(9).rolling(45).mean())
    return _safe_div(base, _rolling_std(base, 252))

def lcol_311_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 53 liquidity collapse over 5d to stabilize variance and capture exponential shifts.
    """
    base = (volume.pct_change(9).rolling(45).mean())
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def lcol_312_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 53 liquidity collapse over 21d to stabilize variance and capture exponential shifts.
    """
    base = (volume.pct_change(9).rolling(45).mean())
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def lcol_313_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 53 liquidity collapse over 63d to stabilize variance and capture exponential shifts.
    """
    base = (volume.pct_change(9).rolling(45).mean())
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def lcol_314_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 53 liquidity collapse over 126d to stabilize variance and capture exponential shifts.
    """
    base = (volume.pct_change(9).rolling(45).mean())
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def lcol_315_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 53 liquidity collapse over 252d to stabilize variance and capture exponential shifts.
    """
    base = (volume.pct_change(9).rolling(45).mean())
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def lcol_316_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 53 liquidity collapse over a 5d horizon to identify extreme regimes.
    """
    base = (volume.pct_change(10).rolling(50).mean())
    return _rolling_mean(base, 5)

def lcol_317_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 53 liquidity collapse over a 21d horizon to identify extreme regimes.
    """
    base = (volume.pct_change(10).rolling(50).mean())
    return _rolling_mean(base, 21)

def lcol_318_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 53 liquidity collapse over a 63d horizon to identify extreme regimes.
    """
    base = (volume.pct_change(10).rolling(50).mean())
    return _rolling_mean(base, 63)

def lcol_319_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 53 liquidity collapse over a 126d horizon to identify extreme regimes.
    """
    base = (volume.pct_change(10).rolling(50).mean())
    return _rolling_mean(base, 126)

def lcol_320_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 53 liquidity collapse over a 252d horizon to identify extreme regimes.
    """
    base = (volume.pct_change(10).rolling(50).mean())
    return _rolling_mean(base, 252)

def lcol_321_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 53 liquidity collapse by measuring deviations from the 5d mean.
    """
    base = (volume.pct_change(10).rolling(50).mean())
    return _zscore_rolling(base, 5)

def lcol_322_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 53 liquidity collapse by measuring deviations from the 21d mean.
    """
    base = (volume.pct_change(10).rolling(50).mean())
    return _zscore_rolling(base, 21)

def lcol_323_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 53 liquidity collapse by measuring deviations from the 63d mean.
    """
    base = (volume.pct_change(10).rolling(50).mean())
    return _zscore_rolling(base, 63)

def lcol_324_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 53 liquidity collapse by measuring deviations from the 126d mean.
    """
    base = (volume.pct_change(10).rolling(50).mean())
    return _zscore_rolling(base, 126)

def lcol_325_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 53 liquidity collapse by measuring deviations from the 252d mean.
    """
    base = (volume.pct_change(10).rolling(50).mean())
    return _zscore_rolling(base, 252)

def lcol_326_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 53 liquidity collapse to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = (volume.pct_change(10).rolling(50).mean())
    return _rank_pct(base, 5)

def lcol_327_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 53 liquidity collapse to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = (volume.pct_change(10).rolling(50).mean())
    return _rank_pct(base, 21)

def lcol_328_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 53 liquidity collapse to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = (volume.pct_change(10).rolling(50).mean())
    return _rank_pct(base, 63)

def lcol_329_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 53 liquidity collapse to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = (volume.pct_change(10).rolling(50).mean())
    return _rank_pct(base, 126)

def lcol_330_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 53 liquidity collapse to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = (volume.pct_change(10).rolling(50).mean())
    return _rank_pct(base, 252)

def lcol_331_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 53 liquidity collapse distribution over 5d to detect tail risk or exhaustion.
    """
    base = (volume.pct_change(10).rolling(50).mean())
    return _rolling_skew(base, 5)

def lcol_332_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 53 liquidity collapse distribution over 21d to detect tail risk or exhaustion.
    """
    base = (volume.pct_change(10).rolling(50).mean())
    return _rolling_skew(base, 21)

def lcol_333_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 53 liquidity collapse distribution over 63d to detect tail risk or exhaustion.
    """
    base = (volume.pct_change(10).rolling(50).mean())
    return _rolling_skew(base, 63)

def lcol_334_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 53 liquidity collapse distribution over 126d to detect tail risk or exhaustion.
    """
    base = (volume.pct_change(10).rolling(50).mean())
    return _rolling_skew(base, 126)

def lcol_335_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 53 liquidity collapse distribution over 252d to detect tail risk or exhaustion.
    """
    base = (volume.pct_change(10).rolling(50).mean())
    return _rolling_skew(base, 252)

def lcol_336_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 53 liquidity collapse over 5d to capture explosive breakdown or reversal points.
    """
    base = (volume.pct_change(10).rolling(50).mean())
    return _rolling_kurt(base, 5)

def lcol_337_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 53 liquidity collapse over 21d to capture explosive breakdown or reversal points.
    """
    base = (volume.pct_change(10).rolling(50).mean())
    return _rolling_kurt(base, 21)

def lcol_338_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 53 liquidity collapse over 63d to capture explosive breakdown or reversal points.
    """
    base = (volume.pct_change(10).rolling(50).mean())
    return _rolling_kurt(base, 63)

def lcol_339_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 53 liquidity collapse over 126d to capture explosive breakdown or reversal points.
    """
    base = (volume.pct_change(10).rolling(50).mean())
    return _rolling_kurt(base, 126)

def lcol_340_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 53 liquidity collapse over 252d to capture explosive breakdown or reversal points.
    """
    base = (volume.pct_change(10).rolling(50).mean())
    return _rolling_kurt(base, 252)

def lcol_341_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 53 liquidity collapse for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = (volume.pct_change(10).rolling(50).mean())
    return _safe_div(base, _rolling_std(base, 5))

def lcol_342_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 53 liquidity collapse for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = (volume.pct_change(10).rolling(50).mean())
    return _safe_div(base, _rolling_std(base, 21))

def lcol_343_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 53 liquidity collapse for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = (volume.pct_change(10).rolling(50).mean())
    return _safe_div(base, _rolling_std(base, 63))

def lcol_344_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 53 liquidity collapse for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = (volume.pct_change(10).rolling(50).mean())
    return _safe_div(base, _rolling_std(base, 126))

def lcol_345_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 53 liquidity collapse for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = (volume.pct_change(10).rolling(50).mean())
    return _safe_div(base, _rolling_std(base, 252))

def lcol_346_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 53 liquidity collapse over 5d to stabilize variance and capture exponential shifts.
    """
    base = (volume.pct_change(10).rolling(50).mean())
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def lcol_347_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 53 liquidity collapse over 21d to stabilize variance and capture exponential shifts.
    """
    base = (volume.pct_change(10).rolling(50).mean())
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def lcol_348_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 53 liquidity collapse over 63d to stabilize variance and capture exponential shifts.
    """
    base = (volume.pct_change(10).rolling(50).mean())
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def lcol_349_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 53 liquidity collapse over 126d to stabilize variance and capture exponential shifts.
    """
    base = (volume.pct_change(10).rolling(50).mean())
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def lcol_350_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 53 liquidity collapse over 252d to stabilize variance and capture exponential shifts.
    """
    base = (volume.pct_change(10).rolling(50).mean())
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def lcol_351_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 53 liquidity collapse over a 5d horizon to identify extreme regimes.
    """
    base = (volume.pct_change(11).rolling(55).mean())
    return _rolling_mean(base, 5)

def lcol_352_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 53 liquidity collapse over a 21d horizon to identify extreme regimes.
    """
    base = (volume.pct_change(11).rolling(55).mean())
    return _rolling_mean(base, 21)

def lcol_353_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 53 liquidity collapse over a 63d horizon to identify extreme regimes.
    """
    base = (volume.pct_change(11).rolling(55).mean())
    return _rolling_mean(base, 63)

def lcol_354_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 53 liquidity collapse over a 126d horizon to identify extreme regimes.
    """
    base = (volume.pct_change(11).rolling(55).mean())
    return _rolling_mean(base, 126)

def lcol_355_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 53 liquidity collapse over a 252d horizon to identify extreme regimes.
    """
    base = (volume.pct_change(11).rolling(55).mean())
    return _rolling_mean(base, 252)

def lcol_356_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 53 liquidity collapse by measuring deviations from the 5d mean.
    """
    base = (volume.pct_change(11).rolling(55).mean())
    return _zscore_rolling(base, 5)

def lcol_357_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 53 liquidity collapse by measuring deviations from the 21d mean.
    """
    base = (volume.pct_change(11).rolling(55).mean())
    return _zscore_rolling(base, 21)

def lcol_358_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 53 liquidity collapse by measuring deviations from the 63d mean.
    """
    base = (volume.pct_change(11).rolling(55).mean())
    return _zscore_rolling(base, 63)

def lcol_359_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 53 liquidity collapse by measuring deviations from the 126d mean.
    """
    base = (volume.pct_change(11).rolling(55).mean())
    return _zscore_rolling(base, 126)

def lcol_360_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 53 liquidity collapse by measuring deviations from the 252d mean.
    """
    base = (volume.pct_change(11).rolling(55).mean())
    return _zscore_rolling(base, 252)

def lcol_361_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 53 liquidity collapse to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = (volume.pct_change(11).rolling(55).mean())
    return _rank_pct(base, 5)

def lcol_362_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 53 liquidity collapse to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = (volume.pct_change(11).rolling(55).mean())
    return _rank_pct(base, 21)

def lcol_363_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 53 liquidity collapse to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = (volume.pct_change(11).rolling(55).mean())
    return _rank_pct(base, 63)

def lcol_364_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 53 liquidity collapse to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = (volume.pct_change(11).rolling(55).mean())
    return _rank_pct(base, 126)

def lcol_365_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 53 liquidity collapse to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = (volume.pct_change(11).rolling(55).mean())
    return _rank_pct(base, 252)

def lcol_366_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 53 liquidity collapse distribution over 5d to detect tail risk or exhaustion.
    """
    base = (volume.pct_change(11).rolling(55).mean())
    return _rolling_skew(base, 5)

def lcol_367_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 53 liquidity collapse distribution over 21d to detect tail risk or exhaustion.
    """
    base = (volume.pct_change(11).rolling(55).mean())
    return _rolling_skew(base, 21)

def lcol_368_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 53 liquidity collapse distribution over 63d to detect tail risk or exhaustion.
    """
    base = (volume.pct_change(11).rolling(55).mean())
    return _rolling_skew(base, 63)

def lcol_369_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 53 liquidity collapse distribution over 126d to detect tail risk or exhaustion.
    """
    base = (volume.pct_change(11).rolling(55).mean())
    return _rolling_skew(base, 126)

def lcol_370_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 53 liquidity collapse distribution over 252d to detect tail risk or exhaustion.
    """
    base = (volume.pct_change(11).rolling(55).mean())
    return _rolling_skew(base, 252)

def lcol_371_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 53 liquidity collapse over 5d to capture explosive breakdown or reversal points.
    """
    base = (volume.pct_change(11).rolling(55).mean())
    return _rolling_kurt(base, 5)

def lcol_372_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 53 liquidity collapse over 21d to capture explosive breakdown or reversal points.
    """
    base = (volume.pct_change(11).rolling(55).mean())
    return _rolling_kurt(base, 21)

def lcol_373_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 53 liquidity collapse over 63d to capture explosive breakdown or reversal points.
    """
    base = (volume.pct_change(11).rolling(55).mean())
    return _rolling_kurt(base, 63)

def lcol_374_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 53 liquidity collapse over 126d to capture explosive breakdown or reversal points.
    """
    base = (volume.pct_change(11).rolling(55).mean())
    return _rolling_kurt(base, 126)

def lcol_375_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 53 liquidity collapse over 252d to capture explosive breakdown or reversal points.
    """
    base = (volume.pct_change(11).rolling(55).mean())
    return _rolling_kurt(base, 252)
