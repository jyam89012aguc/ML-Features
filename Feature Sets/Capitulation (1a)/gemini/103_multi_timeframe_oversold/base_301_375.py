"""
103_103_multi_timeframe_oversold — Base Features 301-375
Domain: 103_multi_timeframe_oversold
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

def mtfo_301_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 103 multi timeframe oversold over 5d to capture explosive breakdown or reversal points.
    """
    base = _zscore_rolling(close, 85)
    return _rolling_kurt(base, 5)

def mtfo_302_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 103 multi timeframe oversold over 21d to capture explosive breakdown or reversal points.
    """
    base = _zscore_rolling(close, 85)
    return _rolling_kurt(base, 21)

def mtfo_303_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 103 multi timeframe oversold over 63d to capture explosive breakdown or reversal points.
    """
    base = _zscore_rolling(close, 85)
    return _rolling_kurt(base, 63)

def mtfo_304_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 103 multi timeframe oversold over 126d to capture explosive breakdown or reversal points.
    """
    base = _zscore_rolling(close, 85)
    return _rolling_kurt(base, 126)

def mtfo_305_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 103 multi timeframe oversold over 252d to capture explosive breakdown or reversal points.
    """
    base = _zscore_rolling(close, 85)
    return _rolling_kurt(base, 252)

def mtfo_306_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 103 multi timeframe oversold for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = _zscore_rolling(close, 85)
    return _safe_div(base, _rolling_std(base, 5))

def mtfo_307_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 103 multi timeframe oversold for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = _zscore_rolling(close, 85)
    return _safe_div(base, _rolling_std(base, 21))

def mtfo_308_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 103 multi timeframe oversold for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = _zscore_rolling(close, 85)
    return _safe_div(base, _rolling_std(base, 63))

def mtfo_309_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 103 multi timeframe oversold for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = _zscore_rolling(close, 85)
    return _safe_div(base, _rolling_std(base, 126))

def mtfo_310_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 103 multi timeframe oversold for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = _zscore_rolling(close, 85)
    return _safe_div(base, _rolling_std(base, 252))

def mtfo_311_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 103 multi timeframe oversold over 5d to stabilize variance and capture exponential shifts.
    """
    base = _zscore_rolling(close, 85)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def mtfo_312_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 103 multi timeframe oversold over 21d to stabilize variance and capture exponential shifts.
    """
    base = _zscore_rolling(close, 85)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def mtfo_313_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 103 multi timeframe oversold over 63d to stabilize variance and capture exponential shifts.
    """
    base = _zscore_rolling(close, 85)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def mtfo_314_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 103 multi timeframe oversold over 126d to stabilize variance and capture exponential shifts.
    """
    base = _zscore_rolling(close, 85)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def mtfo_315_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 103 multi timeframe oversold over 252d to stabilize variance and capture exponential shifts.
    """
    base = _zscore_rolling(close, 85)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def mtfo_316_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 103 multi timeframe oversold over a 5d horizon to identify extreme regimes.
    """
    base = _zscore_rolling(close, 95)
    return _rolling_mean(base, 5)

def mtfo_317_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 103 multi timeframe oversold over a 21d horizon to identify extreme regimes.
    """
    base = _zscore_rolling(close, 95)
    return _rolling_mean(base, 21)

def mtfo_318_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 103 multi timeframe oversold over a 63d horizon to identify extreme regimes.
    """
    base = _zscore_rolling(close, 95)
    return _rolling_mean(base, 63)

def mtfo_319_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 103 multi timeframe oversold over a 126d horizon to identify extreme regimes.
    """
    base = _zscore_rolling(close, 95)
    return _rolling_mean(base, 126)

def mtfo_320_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 103 multi timeframe oversold over a 252d horizon to identify extreme regimes.
    """
    base = _zscore_rolling(close, 95)
    return _rolling_mean(base, 252)

def mtfo_321_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 103 multi timeframe oversold by measuring deviations from the 5d mean.
    """
    base = _zscore_rolling(close, 95)
    return _zscore_rolling(base, 5)

def mtfo_322_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 103 multi timeframe oversold by measuring deviations from the 21d mean.
    """
    base = _zscore_rolling(close, 95)
    return _zscore_rolling(base, 21)

def mtfo_323_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 103 multi timeframe oversold by measuring deviations from the 63d mean.
    """
    base = _zscore_rolling(close, 95)
    return _zscore_rolling(base, 63)

def mtfo_324_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 103 multi timeframe oversold by measuring deviations from the 126d mean.
    """
    base = _zscore_rolling(close, 95)
    return _zscore_rolling(base, 126)

def mtfo_325_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 103 multi timeframe oversold by measuring deviations from the 252d mean.
    """
    base = _zscore_rolling(close, 95)
    return _zscore_rolling(base, 252)

def mtfo_326_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 103 multi timeframe oversold to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = _zscore_rolling(close, 95)
    return _rank_pct(base, 5)

def mtfo_327_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 103 multi timeframe oversold to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = _zscore_rolling(close, 95)
    return _rank_pct(base, 21)

def mtfo_328_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 103 multi timeframe oversold to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = _zscore_rolling(close, 95)
    return _rank_pct(base, 63)

def mtfo_329_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 103 multi timeframe oversold to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = _zscore_rolling(close, 95)
    return _rank_pct(base, 126)

def mtfo_330_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 103 multi timeframe oversold to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = _zscore_rolling(close, 95)
    return _rank_pct(base, 252)

def mtfo_331_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 103 multi timeframe oversold distribution over 5d to detect tail risk or exhaustion.
    """
    base = _zscore_rolling(close, 95)
    return _rolling_skew(base, 5)

def mtfo_332_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 103 multi timeframe oversold distribution over 21d to detect tail risk or exhaustion.
    """
    base = _zscore_rolling(close, 95)
    return _rolling_skew(base, 21)

def mtfo_333_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 103 multi timeframe oversold distribution over 63d to detect tail risk or exhaustion.
    """
    base = _zscore_rolling(close, 95)
    return _rolling_skew(base, 63)

def mtfo_334_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 103 multi timeframe oversold distribution over 126d to detect tail risk or exhaustion.
    """
    base = _zscore_rolling(close, 95)
    return _rolling_skew(base, 126)

def mtfo_335_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 103 multi timeframe oversold distribution over 252d to detect tail risk or exhaustion.
    """
    base = _zscore_rolling(close, 95)
    return _rolling_skew(base, 252)

def mtfo_336_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 103 multi timeframe oversold over 5d to capture explosive breakdown or reversal points.
    """
    base = _zscore_rolling(close, 95)
    return _rolling_kurt(base, 5)

def mtfo_337_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 103 multi timeframe oversold over 21d to capture explosive breakdown or reversal points.
    """
    base = _zscore_rolling(close, 95)
    return _rolling_kurt(base, 21)

def mtfo_338_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 103 multi timeframe oversold over 63d to capture explosive breakdown or reversal points.
    """
    base = _zscore_rolling(close, 95)
    return _rolling_kurt(base, 63)

def mtfo_339_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 103 multi timeframe oversold over 126d to capture explosive breakdown or reversal points.
    """
    base = _zscore_rolling(close, 95)
    return _rolling_kurt(base, 126)

def mtfo_340_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 103 multi timeframe oversold over 252d to capture explosive breakdown or reversal points.
    """
    base = _zscore_rolling(close, 95)
    return _rolling_kurt(base, 252)

def mtfo_341_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 103 multi timeframe oversold for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = _zscore_rolling(close, 95)
    return _safe_div(base, _rolling_std(base, 5))

def mtfo_342_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 103 multi timeframe oversold for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = _zscore_rolling(close, 95)
    return _safe_div(base, _rolling_std(base, 21))

def mtfo_343_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 103 multi timeframe oversold for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = _zscore_rolling(close, 95)
    return _safe_div(base, _rolling_std(base, 63))

def mtfo_344_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 103 multi timeframe oversold for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = _zscore_rolling(close, 95)
    return _safe_div(base, _rolling_std(base, 126))

def mtfo_345_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 103 multi timeframe oversold for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = _zscore_rolling(close, 95)
    return _safe_div(base, _rolling_std(base, 252))

def mtfo_346_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 103 multi timeframe oversold over 5d to stabilize variance and capture exponential shifts.
    """
    base = _zscore_rolling(close, 95)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def mtfo_347_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 103 multi timeframe oversold over 21d to stabilize variance and capture exponential shifts.
    """
    base = _zscore_rolling(close, 95)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def mtfo_348_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 103 multi timeframe oversold over 63d to stabilize variance and capture exponential shifts.
    """
    base = _zscore_rolling(close, 95)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def mtfo_349_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 103 multi timeframe oversold over 126d to stabilize variance and capture exponential shifts.
    """
    base = _zscore_rolling(close, 95)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def mtfo_350_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 103 multi timeframe oversold over 252d to stabilize variance and capture exponential shifts.
    """
    base = _zscore_rolling(close, 95)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def mtfo_351_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 103 multi timeframe oversold over a 5d horizon to identify extreme regimes.
    """
    base = _zscore_rolling(close, 105)
    return _rolling_mean(base, 5)

def mtfo_352_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 103 multi timeframe oversold over a 21d horizon to identify extreme regimes.
    """
    base = _zscore_rolling(close, 105)
    return _rolling_mean(base, 21)

def mtfo_353_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 103 multi timeframe oversold over a 63d horizon to identify extreme regimes.
    """
    base = _zscore_rolling(close, 105)
    return _rolling_mean(base, 63)

def mtfo_354_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 103 multi timeframe oversold over a 126d horizon to identify extreme regimes.
    """
    base = _zscore_rolling(close, 105)
    return _rolling_mean(base, 126)

def mtfo_355_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 103 multi timeframe oversold over a 252d horizon to identify extreme regimes.
    """
    base = _zscore_rolling(close, 105)
    return _rolling_mean(base, 252)

def mtfo_356_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 103 multi timeframe oversold by measuring deviations from the 5d mean.
    """
    base = _zscore_rolling(close, 105)
    return _zscore_rolling(base, 5)

def mtfo_357_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 103 multi timeframe oversold by measuring deviations from the 21d mean.
    """
    base = _zscore_rolling(close, 105)
    return _zscore_rolling(base, 21)

def mtfo_358_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 103 multi timeframe oversold by measuring deviations from the 63d mean.
    """
    base = _zscore_rolling(close, 105)
    return _zscore_rolling(base, 63)

def mtfo_359_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 103 multi timeframe oversold by measuring deviations from the 126d mean.
    """
    base = _zscore_rolling(close, 105)
    return _zscore_rolling(base, 126)

def mtfo_360_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 103 multi timeframe oversold by measuring deviations from the 252d mean.
    """
    base = _zscore_rolling(close, 105)
    return _zscore_rolling(base, 252)

def mtfo_361_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 103 multi timeframe oversold to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = _zscore_rolling(close, 105)
    return _rank_pct(base, 5)

def mtfo_362_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 103 multi timeframe oversold to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = _zscore_rolling(close, 105)
    return _rank_pct(base, 21)

def mtfo_363_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 103 multi timeframe oversold to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = _zscore_rolling(close, 105)
    return _rank_pct(base, 63)

def mtfo_364_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 103 multi timeframe oversold to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = _zscore_rolling(close, 105)
    return _rank_pct(base, 126)

def mtfo_365_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 103 multi timeframe oversold to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = _zscore_rolling(close, 105)
    return _rank_pct(base, 252)

def mtfo_366_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 103 multi timeframe oversold distribution over 5d to detect tail risk or exhaustion.
    """
    base = _zscore_rolling(close, 105)
    return _rolling_skew(base, 5)

def mtfo_367_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 103 multi timeframe oversold distribution over 21d to detect tail risk or exhaustion.
    """
    base = _zscore_rolling(close, 105)
    return _rolling_skew(base, 21)

def mtfo_368_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 103 multi timeframe oversold distribution over 63d to detect tail risk or exhaustion.
    """
    base = _zscore_rolling(close, 105)
    return _rolling_skew(base, 63)

def mtfo_369_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 103 multi timeframe oversold distribution over 126d to detect tail risk or exhaustion.
    """
    base = _zscore_rolling(close, 105)
    return _rolling_skew(base, 126)

def mtfo_370_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 103 multi timeframe oversold distribution over 252d to detect tail risk or exhaustion.
    """
    base = _zscore_rolling(close, 105)
    return _rolling_skew(base, 252)

def mtfo_371_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 103 multi timeframe oversold over 5d to capture explosive breakdown or reversal points.
    """
    base = _zscore_rolling(close, 105)
    return _rolling_kurt(base, 5)

def mtfo_372_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 103 multi timeframe oversold over 21d to capture explosive breakdown or reversal points.
    """
    base = _zscore_rolling(close, 105)
    return _rolling_kurt(base, 21)

def mtfo_373_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 103 multi timeframe oversold over 63d to capture explosive breakdown or reversal points.
    """
    base = _zscore_rolling(close, 105)
    return _rolling_kurt(base, 63)

def mtfo_374_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 103 multi timeframe oversold over 126d to capture explosive breakdown or reversal points.
    """
    base = _zscore_rolling(close, 105)
    return _rolling_kurt(base, 126)

def mtfo_375_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 103 multi timeframe oversold over 252d to capture explosive breakdown or reversal points.
    """
    base = _zscore_rolling(close, 105)
    return _rolling_kurt(base, 252)
