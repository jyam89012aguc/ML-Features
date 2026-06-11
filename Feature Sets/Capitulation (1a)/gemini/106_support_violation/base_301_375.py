"""
106_106_support_violation — Base Features 301-375
Domain: 106_support_violation
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

def supv_301_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 106 support violation over 5d to capture explosive breakdown or reversal points.
    """
    base = close / low.rolling(90).min() - 1
    return _rolling_kurt(base, 5)

def supv_302_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 106 support violation over 21d to capture explosive breakdown or reversal points.
    """
    base = close / low.rolling(90).min() - 1
    return _rolling_kurt(base, 21)

def supv_303_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 106 support violation over 63d to capture explosive breakdown or reversal points.
    """
    base = close / low.rolling(90).min() - 1
    return _rolling_kurt(base, 63)

def supv_304_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 106 support violation over 126d to capture explosive breakdown or reversal points.
    """
    base = close / low.rolling(90).min() - 1
    return _rolling_kurt(base, 126)

def supv_305_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 106 support violation over 252d to capture explosive breakdown or reversal points.
    """
    base = close / low.rolling(90).min() - 1
    return _rolling_kurt(base, 252)

def supv_306_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 106 support violation for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = close / low.rolling(90).min() - 1
    return _safe_div(base, _rolling_std(base, 5))

def supv_307_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 106 support violation for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = close / low.rolling(90).min() - 1
    return _safe_div(base, _rolling_std(base, 21))

def supv_308_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 106 support violation for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = close / low.rolling(90).min() - 1
    return _safe_div(base, _rolling_std(base, 63))

def supv_309_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 106 support violation for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = close / low.rolling(90).min() - 1
    return _safe_div(base, _rolling_std(base, 126))

def supv_310_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 106 support violation for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = close / low.rolling(90).min() - 1
    return _safe_div(base, _rolling_std(base, 252))

def supv_311_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 106 support violation over 5d to stabilize variance and capture exponential shifts.
    """
    base = close / low.rolling(90).min() - 1
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def supv_312_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 106 support violation over 21d to stabilize variance and capture exponential shifts.
    """
    base = close / low.rolling(90).min() - 1
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def supv_313_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 106 support violation over 63d to stabilize variance and capture exponential shifts.
    """
    base = close / low.rolling(90).min() - 1
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def supv_314_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 106 support violation over 126d to stabilize variance and capture exponential shifts.
    """
    base = close / low.rolling(90).min() - 1
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def supv_315_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 106 support violation over 252d to stabilize variance and capture exponential shifts.
    """
    base = close / low.rolling(90).min() - 1
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def supv_316_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 106 support violation over a 5d horizon to identify extreme regimes.
    """
    base = close / low.rolling(100).min() - 1
    return _rolling_mean(base, 5)

def supv_317_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 106 support violation over a 21d horizon to identify extreme regimes.
    """
    base = close / low.rolling(100).min() - 1
    return _rolling_mean(base, 21)

def supv_318_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 106 support violation over a 63d horizon to identify extreme regimes.
    """
    base = close / low.rolling(100).min() - 1
    return _rolling_mean(base, 63)

def supv_319_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 106 support violation over a 126d horizon to identify extreme regimes.
    """
    base = close / low.rolling(100).min() - 1
    return _rolling_mean(base, 126)

def supv_320_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 106 support violation over a 252d horizon to identify extreme regimes.
    """
    base = close / low.rolling(100).min() - 1
    return _rolling_mean(base, 252)

def supv_321_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 106 support violation by measuring deviations from the 5d mean.
    """
    base = close / low.rolling(100).min() - 1
    return _zscore_rolling(base, 5)

def supv_322_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 106 support violation by measuring deviations from the 21d mean.
    """
    base = close / low.rolling(100).min() - 1
    return _zscore_rolling(base, 21)

def supv_323_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 106 support violation by measuring deviations from the 63d mean.
    """
    base = close / low.rolling(100).min() - 1
    return _zscore_rolling(base, 63)

def supv_324_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 106 support violation by measuring deviations from the 126d mean.
    """
    base = close / low.rolling(100).min() - 1
    return _zscore_rolling(base, 126)

def supv_325_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 106 support violation by measuring deviations from the 252d mean.
    """
    base = close / low.rolling(100).min() - 1
    return _zscore_rolling(base, 252)

def supv_326_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 106 support violation to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = close / low.rolling(100).min() - 1
    return _rank_pct(base, 5)

def supv_327_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 106 support violation to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = close / low.rolling(100).min() - 1
    return _rank_pct(base, 21)

def supv_328_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 106 support violation to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = close / low.rolling(100).min() - 1
    return _rank_pct(base, 63)

def supv_329_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 106 support violation to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = close / low.rolling(100).min() - 1
    return _rank_pct(base, 126)

def supv_330_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 106 support violation to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = close / low.rolling(100).min() - 1
    return _rank_pct(base, 252)

def supv_331_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 106 support violation distribution over 5d to detect tail risk or exhaustion.
    """
    base = close / low.rolling(100).min() - 1
    return _rolling_skew(base, 5)

def supv_332_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 106 support violation distribution over 21d to detect tail risk or exhaustion.
    """
    base = close / low.rolling(100).min() - 1
    return _rolling_skew(base, 21)

def supv_333_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 106 support violation distribution over 63d to detect tail risk or exhaustion.
    """
    base = close / low.rolling(100).min() - 1
    return _rolling_skew(base, 63)

def supv_334_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 106 support violation distribution over 126d to detect tail risk or exhaustion.
    """
    base = close / low.rolling(100).min() - 1
    return _rolling_skew(base, 126)

def supv_335_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 106 support violation distribution over 252d to detect tail risk or exhaustion.
    """
    base = close / low.rolling(100).min() - 1
    return _rolling_skew(base, 252)

def supv_336_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 106 support violation over 5d to capture explosive breakdown or reversal points.
    """
    base = close / low.rolling(100).min() - 1
    return _rolling_kurt(base, 5)

def supv_337_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 106 support violation over 21d to capture explosive breakdown or reversal points.
    """
    base = close / low.rolling(100).min() - 1
    return _rolling_kurt(base, 21)

def supv_338_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 106 support violation over 63d to capture explosive breakdown or reversal points.
    """
    base = close / low.rolling(100).min() - 1
    return _rolling_kurt(base, 63)

def supv_339_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 106 support violation over 126d to capture explosive breakdown or reversal points.
    """
    base = close / low.rolling(100).min() - 1
    return _rolling_kurt(base, 126)

def supv_340_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 106 support violation over 252d to capture explosive breakdown or reversal points.
    """
    base = close / low.rolling(100).min() - 1
    return _rolling_kurt(base, 252)

def supv_341_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 106 support violation for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = close / low.rolling(100).min() - 1
    return _safe_div(base, _rolling_std(base, 5))

def supv_342_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 106 support violation for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = close / low.rolling(100).min() - 1
    return _safe_div(base, _rolling_std(base, 21))

def supv_343_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 106 support violation for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = close / low.rolling(100).min() - 1
    return _safe_div(base, _rolling_std(base, 63))

def supv_344_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 106 support violation for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = close / low.rolling(100).min() - 1
    return _safe_div(base, _rolling_std(base, 126))

def supv_345_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 106 support violation for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = close / low.rolling(100).min() - 1
    return _safe_div(base, _rolling_std(base, 252))

def supv_346_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 106 support violation over 5d to stabilize variance and capture exponential shifts.
    """
    base = close / low.rolling(100).min() - 1
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def supv_347_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 106 support violation over 21d to stabilize variance and capture exponential shifts.
    """
    base = close / low.rolling(100).min() - 1
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def supv_348_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 106 support violation over 63d to stabilize variance and capture exponential shifts.
    """
    base = close / low.rolling(100).min() - 1
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def supv_349_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 106 support violation over 126d to stabilize variance and capture exponential shifts.
    """
    base = close / low.rolling(100).min() - 1
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def supv_350_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 106 support violation over 252d to stabilize variance and capture exponential shifts.
    """
    base = close / low.rolling(100).min() - 1
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def supv_351_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 106 support violation over a 5d horizon to identify extreme regimes.
    """
    base = close / low.rolling(110).min() - 1
    return _rolling_mean(base, 5)

def supv_352_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 106 support violation over a 21d horizon to identify extreme regimes.
    """
    base = close / low.rolling(110).min() - 1
    return _rolling_mean(base, 21)

def supv_353_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 106 support violation over a 63d horizon to identify extreme regimes.
    """
    base = close / low.rolling(110).min() - 1
    return _rolling_mean(base, 63)

def supv_354_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 106 support violation over a 126d horizon to identify extreme regimes.
    """
    base = close / low.rolling(110).min() - 1
    return _rolling_mean(base, 126)

def supv_355_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 106 support violation over a 252d horizon to identify extreme regimes.
    """
    base = close / low.rolling(110).min() - 1
    return _rolling_mean(base, 252)

def supv_356_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 106 support violation by measuring deviations from the 5d mean.
    """
    base = close / low.rolling(110).min() - 1
    return _zscore_rolling(base, 5)

def supv_357_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 106 support violation by measuring deviations from the 21d mean.
    """
    base = close / low.rolling(110).min() - 1
    return _zscore_rolling(base, 21)

def supv_358_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 106 support violation by measuring deviations from the 63d mean.
    """
    base = close / low.rolling(110).min() - 1
    return _zscore_rolling(base, 63)

def supv_359_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 106 support violation by measuring deviations from the 126d mean.
    """
    base = close / low.rolling(110).min() - 1
    return _zscore_rolling(base, 126)

def supv_360_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 106 support violation by measuring deviations from the 252d mean.
    """
    base = close / low.rolling(110).min() - 1
    return _zscore_rolling(base, 252)

def supv_361_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 106 support violation to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = close / low.rolling(110).min() - 1
    return _rank_pct(base, 5)

def supv_362_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 106 support violation to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = close / low.rolling(110).min() - 1
    return _rank_pct(base, 21)

def supv_363_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 106 support violation to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = close / low.rolling(110).min() - 1
    return _rank_pct(base, 63)

def supv_364_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 106 support violation to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = close / low.rolling(110).min() - 1
    return _rank_pct(base, 126)

def supv_365_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 106 support violation to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = close / low.rolling(110).min() - 1
    return _rank_pct(base, 252)

def supv_366_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 106 support violation distribution over 5d to detect tail risk or exhaustion.
    """
    base = close / low.rolling(110).min() - 1
    return _rolling_skew(base, 5)

def supv_367_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 106 support violation distribution over 21d to detect tail risk or exhaustion.
    """
    base = close / low.rolling(110).min() - 1
    return _rolling_skew(base, 21)

def supv_368_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 106 support violation distribution over 63d to detect tail risk or exhaustion.
    """
    base = close / low.rolling(110).min() - 1
    return _rolling_skew(base, 63)

def supv_369_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 106 support violation distribution over 126d to detect tail risk or exhaustion.
    """
    base = close / low.rolling(110).min() - 1
    return _rolling_skew(base, 126)

def supv_370_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 106 support violation distribution over 252d to detect tail risk or exhaustion.
    """
    base = close / low.rolling(110).min() - 1
    return _rolling_skew(base, 252)

def supv_371_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 106 support violation over 5d to capture explosive breakdown or reversal points.
    """
    base = close / low.rolling(110).min() - 1
    return _rolling_kurt(base, 5)

def supv_372_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 106 support violation over 21d to capture explosive breakdown or reversal points.
    """
    base = close / low.rolling(110).min() - 1
    return _rolling_kurt(base, 21)

def supv_373_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 106 support violation over 63d to capture explosive breakdown or reversal points.
    """
    base = close / low.rolling(110).min() - 1
    return _rolling_kurt(base, 63)

def supv_374_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 106 support violation over 126d to capture explosive breakdown or reversal points.
    """
    base = close / low.rolling(110).min() - 1
    return _rolling_kurt(base, 126)

def supv_375_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 106 support violation over 252d to capture explosive breakdown or reversal points.
    """
    base = close / low.rolling(110).min() - 1
    return _rolling_kurt(base, 252)
