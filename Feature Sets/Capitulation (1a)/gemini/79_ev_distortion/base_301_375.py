"""
79_79_ev_distortion — Base Features 301-375
Domain: 79_ev_distortion
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

def evds_301_kurt_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 79 ev distortion over 5d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(45)
    return _rolling_kurt(base, 5)

def evds_302_kurt_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 79 ev distortion over 21d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(45)
    return _rolling_kurt(base, 21)

def evds_303_kurt_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 79 ev distortion over 63d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(45)
    return _rolling_kurt(base, 63)

def evds_304_kurt_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 79 ev distortion over 126d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(45)
    return _rolling_kurt(base, 126)

def evds_305_kurt_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 79 ev distortion over 252d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(45)
    return _rolling_kurt(base, 252)

def evds_306_voladj_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 79 ev distortion for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(45)
    return _safe_div(base, _rolling_std(base, 5))

def evds_307_voladj_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 79 ev distortion for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(45)
    return _safe_div(base, _rolling_std(base, 21))

def evds_308_voladj_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 79 ev distortion for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(45)
    return _safe_div(base, _rolling_std(base, 63))

def evds_309_voladj_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 79 ev distortion for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(45)
    return _safe_div(base, _rolling_std(base, 126))

def evds_310_voladj_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 79 ev distortion for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(45)
    return _safe_div(base, _rolling_std(base, 252))

def evds_311_lognorm_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 79 ev distortion over 5d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(45)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def evds_312_lognorm_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 79 ev distortion over 21d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(45)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def evds_313_lognorm_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 79 ev distortion over 63d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(45)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def evds_314_lognorm_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 79 ev distortion over 126d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(45)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def evds_315_lognorm_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 79 ev distortion over 252d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(45)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def evds_316_lvl_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 79 ev distortion over a 5d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(50)
    return _rolling_mean(base, 5)

def evds_317_lvl_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 79 ev distortion over a 21d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(50)
    return _rolling_mean(base, 21)

def evds_318_lvl_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 79 ev distortion over a 63d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(50)
    return _rolling_mean(base, 63)

def evds_319_lvl_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 79 ev distortion over a 126d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(50)
    return _rolling_mean(base, 126)

def evds_320_lvl_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 79 ev distortion over a 252d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(50)
    return _rolling_mean(base, 252)

def evds_321_zscore_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 79 ev distortion by measuring deviations from the 5d mean.
    """
    base = marketcap.pct_change(50)
    return _zscore_rolling(base, 5)

def evds_322_zscore_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 79 ev distortion by measuring deviations from the 21d mean.
    """
    base = marketcap.pct_change(50)
    return _zscore_rolling(base, 21)

def evds_323_zscore_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 79 ev distortion by measuring deviations from the 63d mean.
    """
    base = marketcap.pct_change(50)
    return _zscore_rolling(base, 63)

def evds_324_zscore_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 79 ev distortion by measuring deviations from the 126d mean.
    """
    base = marketcap.pct_change(50)
    return _zscore_rolling(base, 126)

def evds_325_zscore_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 79 ev distortion by measuring deviations from the 252d mean.
    """
    base = marketcap.pct_change(50)
    return _zscore_rolling(base, 252)

def evds_326_rank_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 79 ev distortion to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(50)
    return _rank_pct(base, 5)

def evds_327_rank_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 79 ev distortion to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(50)
    return _rank_pct(base, 21)

def evds_328_rank_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 79 ev distortion to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(50)
    return _rank_pct(base, 63)

def evds_329_rank_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 79 ev distortion to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(50)
    return _rank_pct(base, 126)

def evds_330_rank_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 79 ev distortion to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(50)
    return _rank_pct(base, 252)

def evds_331_skew_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 79 ev distortion distribution over 5d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(50)
    return _rolling_skew(base, 5)

def evds_332_skew_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 79 ev distortion distribution over 21d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(50)
    return _rolling_skew(base, 21)

def evds_333_skew_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 79 ev distortion distribution over 63d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(50)
    return _rolling_skew(base, 63)

def evds_334_skew_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 79 ev distortion distribution over 126d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(50)
    return _rolling_skew(base, 126)

def evds_335_skew_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 79 ev distortion distribution over 252d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(50)
    return _rolling_skew(base, 252)

def evds_336_kurt_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 79 ev distortion over 5d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(50)
    return _rolling_kurt(base, 5)

def evds_337_kurt_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 79 ev distortion over 21d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(50)
    return _rolling_kurt(base, 21)

def evds_338_kurt_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 79 ev distortion over 63d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(50)
    return _rolling_kurt(base, 63)

def evds_339_kurt_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 79 ev distortion over 126d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(50)
    return _rolling_kurt(base, 126)

def evds_340_kurt_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 79 ev distortion over 252d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(50)
    return _rolling_kurt(base, 252)

def evds_341_voladj_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 79 ev distortion for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(50)
    return _safe_div(base, _rolling_std(base, 5))

def evds_342_voladj_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 79 ev distortion for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(50)
    return _safe_div(base, _rolling_std(base, 21))

def evds_343_voladj_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 79 ev distortion for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(50)
    return _safe_div(base, _rolling_std(base, 63))

def evds_344_voladj_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 79 ev distortion for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(50)
    return _safe_div(base, _rolling_std(base, 126))

def evds_345_voladj_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 79 ev distortion for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(50)
    return _safe_div(base, _rolling_std(base, 252))

def evds_346_lognorm_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 79 ev distortion over 5d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(50)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def evds_347_lognorm_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 79 ev distortion over 21d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(50)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def evds_348_lognorm_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 79 ev distortion over 63d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(50)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def evds_349_lognorm_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 79 ev distortion over 126d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(50)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def evds_350_lognorm_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 79 ev distortion over 252d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(50)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def evds_351_lvl_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 79 ev distortion over a 5d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(55)
    return _rolling_mean(base, 5)

def evds_352_lvl_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 79 ev distortion over a 21d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(55)
    return _rolling_mean(base, 21)

def evds_353_lvl_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 79 ev distortion over a 63d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(55)
    return _rolling_mean(base, 63)

def evds_354_lvl_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 79 ev distortion over a 126d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(55)
    return _rolling_mean(base, 126)

def evds_355_lvl_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 79 ev distortion over a 252d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(55)
    return _rolling_mean(base, 252)

def evds_356_zscore_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 79 ev distortion by measuring deviations from the 5d mean.
    """
    base = marketcap.pct_change(55)
    return _zscore_rolling(base, 5)

def evds_357_zscore_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 79 ev distortion by measuring deviations from the 21d mean.
    """
    base = marketcap.pct_change(55)
    return _zscore_rolling(base, 21)

def evds_358_zscore_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 79 ev distortion by measuring deviations from the 63d mean.
    """
    base = marketcap.pct_change(55)
    return _zscore_rolling(base, 63)

def evds_359_zscore_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 79 ev distortion by measuring deviations from the 126d mean.
    """
    base = marketcap.pct_change(55)
    return _zscore_rolling(base, 126)

def evds_360_zscore_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 79 ev distortion by measuring deviations from the 252d mean.
    """
    base = marketcap.pct_change(55)
    return _zscore_rolling(base, 252)

def evds_361_rank_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 79 ev distortion to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(55)
    return _rank_pct(base, 5)

def evds_362_rank_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 79 ev distortion to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(55)
    return _rank_pct(base, 21)

def evds_363_rank_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 79 ev distortion to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(55)
    return _rank_pct(base, 63)

def evds_364_rank_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 79 ev distortion to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(55)
    return _rank_pct(base, 126)

def evds_365_rank_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 79 ev distortion to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(55)
    return _rank_pct(base, 252)

def evds_366_skew_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 79 ev distortion distribution over 5d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(55)
    return _rolling_skew(base, 5)

def evds_367_skew_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 79 ev distortion distribution over 21d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(55)
    return _rolling_skew(base, 21)

def evds_368_skew_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 79 ev distortion distribution over 63d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(55)
    return _rolling_skew(base, 63)

def evds_369_skew_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 79 ev distortion distribution over 126d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(55)
    return _rolling_skew(base, 126)

def evds_370_skew_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 79 ev distortion distribution over 252d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(55)
    return _rolling_skew(base, 252)

def evds_371_kurt_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 79 ev distortion over 5d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(55)
    return _rolling_kurt(base, 5)

def evds_372_kurt_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 79 ev distortion over 21d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(55)
    return _rolling_kurt(base, 21)

def evds_373_kurt_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 79 ev distortion over 63d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(55)
    return _rolling_kurt(base, 63)

def evds_374_kurt_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 79 ev distortion over 126d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(55)
    return _rolling_kurt(base, 126)

def evds_375_kurt_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 79 ev distortion over 252d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(55)
    return _rolling_kurt(base, 252)
