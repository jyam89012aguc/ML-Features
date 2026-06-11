"""
111_111_jump_discontinuity — Base Features 301-375
Domain: 111_jump_discontinuity
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

def jump_301_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 111 jump discontinuity over 5d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().abs().rolling(45).max()
    return _rolling_kurt(base, 5)

def jump_302_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 111 jump discontinuity over 21d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().abs().rolling(45).max()
    return _rolling_kurt(base, 21)

def jump_303_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 111 jump discontinuity over 63d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().abs().rolling(45).max()
    return _rolling_kurt(base, 63)

def jump_304_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 111 jump discontinuity over 126d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().abs().rolling(45).max()
    return _rolling_kurt(base, 126)

def jump_305_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 111 jump discontinuity over 252d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().abs().rolling(45).max()
    return _rolling_kurt(base, 252)

def jump_306_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 111 jump discontinuity for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().abs().rolling(45).max()
    return _safe_div(base, _rolling_std(base, 5))

def jump_307_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 111 jump discontinuity for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().abs().rolling(45).max()
    return _safe_div(base, _rolling_std(base, 21))

def jump_308_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 111 jump discontinuity for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().abs().rolling(45).max()
    return _safe_div(base, _rolling_std(base, 63))

def jump_309_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 111 jump discontinuity for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().abs().rolling(45).max()
    return _safe_div(base, _rolling_std(base, 126))

def jump_310_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 111 jump discontinuity for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().abs().rolling(45).max()
    return _safe_div(base, _rolling_std(base, 252))

def jump_311_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 111 jump discontinuity over 5d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().abs().rolling(45).max()
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def jump_312_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 111 jump discontinuity over 21d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().abs().rolling(45).max()
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def jump_313_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 111 jump discontinuity over 63d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().abs().rolling(45).max()
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def jump_314_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 111 jump discontinuity over 126d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().abs().rolling(45).max()
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def jump_315_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 111 jump discontinuity over 252d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().abs().rolling(45).max()
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def jump_316_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 111 jump discontinuity over a 5d horizon to identify extreme regimes.
    """
    base = close.pct_change().abs().rolling(50).max()
    return _rolling_mean(base, 5)

def jump_317_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 111 jump discontinuity over a 21d horizon to identify extreme regimes.
    """
    base = close.pct_change().abs().rolling(50).max()
    return _rolling_mean(base, 21)

def jump_318_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 111 jump discontinuity over a 63d horizon to identify extreme regimes.
    """
    base = close.pct_change().abs().rolling(50).max()
    return _rolling_mean(base, 63)

def jump_319_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 111 jump discontinuity over a 126d horizon to identify extreme regimes.
    """
    base = close.pct_change().abs().rolling(50).max()
    return _rolling_mean(base, 126)

def jump_320_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 111 jump discontinuity over a 252d horizon to identify extreme regimes.
    """
    base = close.pct_change().abs().rolling(50).max()
    return _rolling_mean(base, 252)

def jump_321_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 111 jump discontinuity by measuring deviations from the 5d mean.
    """
    base = close.pct_change().abs().rolling(50).max()
    return _zscore_rolling(base, 5)

def jump_322_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 111 jump discontinuity by measuring deviations from the 21d mean.
    """
    base = close.pct_change().abs().rolling(50).max()
    return _zscore_rolling(base, 21)

def jump_323_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 111 jump discontinuity by measuring deviations from the 63d mean.
    """
    base = close.pct_change().abs().rolling(50).max()
    return _zscore_rolling(base, 63)

def jump_324_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 111 jump discontinuity by measuring deviations from the 126d mean.
    """
    base = close.pct_change().abs().rolling(50).max()
    return _zscore_rolling(base, 126)

def jump_325_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 111 jump discontinuity by measuring deviations from the 252d mean.
    """
    base = close.pct_change().abs().rolling(50).max()
    return _zscore_rolling(base, 252)

def jump_326_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 111 jump discontinuity to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = close.pct_change().abs().rolling(50).max()
    return _rank_pct(base, 5)

def jump_327_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 111 jump discontinuity to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = close.pct_change().abs().rolling(50).max()
    return _rank_pct(base, 21)

def jump_328_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 111 jump discontinuity to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = close.pct_change().abs().rolling(50).max()
    return _rank_pct(base, 63)

def jump_329_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 111 jump discontinuity to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = close.pct_change().abs().rolling(50).max()
    return _rank_pct(base, 126)

def jump_330_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 111 jump discontinuity to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = close.pct_change().abs().rolling(50).max()
    return _rank_pct(base, 252)

def jump_331_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 111 jump discontinuity distribution over 5d to detect tail risk or exhaustion.
    """
    base = close.pct_change().abs().rolling(50).max()
    return _rolling_skew(base, 5)

def jump_332_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 111 jump discontinuity distribution over 21d to detect tail risk or exhaustion.
    """
    base = close.pct_change().abs().rolling(50).max()
    return _rolling_skew(base, 21)

def jump_333_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 111 jump discontinuity distribution over 63d to detect tail risk or exhaustion.
    """
    base = close.pct_change().abs().rolling(50).max()
    return _rolling_skew(base, 63)

def jump_334_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 111 jump discontinuity distribution over 126d to detect tail risk or exhaustion.
    """
    base = close.pct_change().abs().rolling(50).max()
    return _rolling_skew(base, 126)

def jump_335_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 111 jump discontinuity distribution over 252d to detect tail risk or exhaustion.
    """
    base = close.pct_change().abs().rolling(50).max()
    return _rolling_skew(base, 252)

def jump_336_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 111 jump discontinuity over 5d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().abs().rolling(50).max()
    return _rolling_kurt(base, 5)

def jump_337_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 111 jump discontinuity over 21d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().abs().rolling(50).max()
    return _rolling_kurt(base, 21)

def jump_338_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 111 jump discontinuity over 63d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().abs().rolling(50).max()
    return _rolling_kurt(base, 63)

def jump_339_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 111 jump discontinuity over 126d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().abs().rolling(50).max()
    return _rolling_kurt(base, 126)

def jump_340_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 111 jump discontinuity over 252d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().abs().rolling(50).max()
    return _rolling_kurt(base, 252)

def jump_341_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 111 jump discontinuity for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().abs().rolling(50).max()
    return _safe_div(base, _rolling_std(base, 5))

def jump_342_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 111 jump discontinuity for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().abs().rolling(50).max()
    return _safe_div(base, _rolling_std(base, 21))

def jump_343_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 111 jump discontinuity for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().abs().rolling(50).max()
    return _safe_div(base, _rolling_std(base, 63))

def jump_344_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 111 jump discontinuity for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().abs().rolling(50).max()
    return _safe_div(base, _rolling_std(base, 126))

def jump_345_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 111 jump discontinuity for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().abs().rolling(50).max()
    return _safe_div(base, _rolling_std(base, 252))

def jump_346_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 111 jump discontinuity over 5d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().abs().rolling(50).max()
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def jump_347_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 111 jump discontinuity over 21d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().abs().rolling(50).max()
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def jump_348_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 111 jump discontinuity over 63d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().abs().rolling(50).max()
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def jump_349_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 111 jump discontinuity over 126d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().abs().rolling(50).max()
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def jump_350_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 111 jump discontinuity over 252d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().abs().rolling(50).max()
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def jump_351_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 111 jump discontinuity over a 5d horizon to identify extreme regimes.
    """
    base = close.pct_change().abs().rolling(55).max()
    return _rolling_mean(base, 5)

def jump_352_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 111 jump discontinuity over a 21d horizon to identify extreme regimes.
    """
    base = close.pct_change().abs().rolling(55).max()
    return _rolling_mean(base, 21)

def jump_353_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 111 jump discontinuity over a 63d horizon to identify extreme regimes.
    """
    base = close.pct_change().abs().rolling(55).max()
    return _rolling_mean(base, 63)

def jump_354_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 111 jump discontinuity over a 126d horizon to identify extreme regimes.
    """
    base = close.pct_change().abs().rolling(55).max()
    return _rolling_mean(base, 126)

def jump_355_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 111 jump discontinuity over a 252d horizon to identify extreme regimes.
    """
    base = close.pct_change().abs().rolling(55).max()
    return _rolling_mean(base, 252)

def jump_356_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 111 jump discontinuity by measuring deviations from the 5d mean.
    """
    base = close.pct_change().abs().rolling(55).max()
    return _zscore_rolling(base, 5)

def jump_357_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 111 jump discontinuity by measuring deviations from the 21d mean.
    """
    base = close.pct_change().abs().rolling(55).max()
    return _zscore_rolling(base, 21)

def jump_358_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 111 jump discontinuity by measuring deviations from the 63d mean.
    """
    base = close.pct_change().abs().rolling(55).max()
    return _zscore_rolling(base, 63)

def jump_359_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 111 jump discontinuity by measuring deviations from the 126d mean.
    """
    base = close.pct_change().abs().rolling(55).max()
    return _zscore_rolling(base, 126)

def jump_360_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 111 jump discontinuity by measuring deviations from the 252d mean.
    """
    base = close.pct_change().abs().rolling(55).max()
    return _zscore_rolling(base, 252)

def jump_361_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 111 jump discontinuity to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = close.pct_change().abs().rolling(55).max()
    return _rank_pct(base, 5)

def jump_362_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 111 jump discontinuity to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = close.pct_change().abs().rolling(55).max()
    return _rank_pct(base, 21)

def jump_363_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 111 jump discontinuity to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = close.pct_change().abs().rolling(55).max()
    return _rank_pct(base, 63)

def jump_364_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 111 jump discontinuity to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = close.pct_change().abs().rolling(55).max()
    return _rank_pct(base, 126)

def jump_365_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 111 jump discontinuity to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = close.pct_change().abs().rolling(55).max()
    return _rank_pct(base, 252)

def jump_366_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 111 jump discontinuity distribution over 5d to detect tail risk or exhaustion.
    """
    base = close.pct_change().abs().rolling(55).max()
    return _rolling_skew(base, 5)

def jump_367_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 111 jump discontinuity distribution over 21d to detect tail risk or exhaustion.
    """
    base = close.pct_change().abs().rolling(55).max()
    return _rolling_skew(base, 21)

def jump_368_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 111 jump discontinuity distribution over 63d to detect tail risk or exhaustion.
    """
    base = close.pct_change().abs().rolling(55).max()
    return _rolling_skew(base, 63)

def jump_369_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 111 jump discontinuity distribution over 126d to detect tail risk or exhaustion.
    """
    base = close.pct_change().abs().rolling(55).max()
    return _rolling_skew(base, 126)

def jump_370_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 111 jump discontinuity distribution over 252d to detect tail risk or exhaustion.
    """
    base = close.pct_change().abs().rolling(55).max()
    return _rolling_skew(base, 252)

def jump_371_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 111 jump discontinuity over 5d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().abs().rolling(55).max()
    return _rolling_kurt(base, 5)

def jump_372_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 111 jump discontinuity over 21d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().abs().rolling(55).max()
    return _rolling_kurt(base, 21)

def jump_373_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 111 jump discontinuity over 63d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().abs().rolling(55).max()
    return _rolling_kurt(base, 63)

def jump_374_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 111 jump discontinuity over 126d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().abs().rolling(55).max()
    return _rolling_kurt(base, 126)

def jump_375_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 111 jump discontinuity over 252d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().abs().rolling(55).max()
    return _rolling_kurt(base, 252)
