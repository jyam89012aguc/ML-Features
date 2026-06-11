"""
75_75_guidance_distress — Base Features 301-375
Domain: 75_guidance_distress
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

def guid_301_kurt_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 75 guidance distress over 5d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(45)
    return _rolling_kurt(base, 5)

def guid_302_kurt_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 75 guidance distress over 21d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(45)
    return _rolling_kurt(base, 21)

def guid_303_kurt_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 75 guidance distress over 63d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(45)
    return _rolling_kurt(base, 63)

def guid_304_kurt_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 75 guidance distress over 126d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(45)
    return _rolling_kurt(base, 126)

def guid_305_kurt_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 75 guidance distress over 252d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(45)
    return _rolling_kurt(base, 252)

def guid_306_voladj_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 75 guidance distress for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(45)
    return _safe_div(base, _rolling_std(base, 5))

def guid_307_voladj_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 75 guidance distress for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(45)
    return _safe_div(base, _rolling_std(base, 21))

def guid_308_voladj_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 75 guidance distress for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(45)
    return _safe_div(base, _rolling_std(base, 63))

def guid_309_voladj_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 75 guidance distress for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(45)
    return _safe_div(base, _rolling_std(base, 126))

def guid_310_voladj_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 75 guidance distress for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(45)
    return _safe_div(base, _rolling_std(base, 252))

def guid_311_lognorm_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 75 guidance distress over 5d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(45)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def guid_312_lognorm_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 75 guidance distress over 21d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(45)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def guid_313_lognorm_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 75 guidance distress over 63d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(45)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def guid_314_lognorm_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 75 guidance distress over 126d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(45)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def guid_315_lognorm_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 75 guidance distress over 252d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(45)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def guid_316_lvl_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 75 guidance distress over a 5d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(50)
    return _rolling_mean(base, 5)

def guid_317_lvl_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 75 guidance distress over a 21d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(50)
    return _rolling_mean(base, 21)

def guid_318_lvl_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 75 guidance distress over a 63d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(50)
    return _rolling_mean(base, 63)

def guid_319_lvl_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 75 guidance distress over a 126d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(50)
    return _rolling_mean(base, 126)

def guid_320_lvl_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 75 guidance distress over a 252d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(50)
    return _rolling_mean(base, 252)

def guid_321_zscore_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 75 guidance distress by measuring deviations from the 5d mean.
    """
    base = marketcap.pct_change(50)
    return _zscore_rolling(base, 5)

def guid_322_zscore_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 75 guidance distress by measuring deviations from the 21d mean.
    """
    base = marketcap.pct_change(50)
    return _zscore_rolling(base, 21)

def guid_323_zscore_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 75 guidance distress by measuring deviations from the 63d mean.
    """
    base = marketcap.pct_change(50)
    return _zscore_rolling(base, 63)

def guid_324_zscore_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 75 guidance distress by measuring deviations from the 126d mean.
    """
    base = marketcap.pct_change(50)
    return _zscore_rolling(base, 126)

def guid_325_zscore_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 75 guidance distress by measuring deviations from the 252d mean.
    """
    base = marketcap.pct_change(50)
    return _zscore_rolling(base, 252)

def guid_326_rank_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 75 guidance distress to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(50)
    return _rank_pct(base, 5)

def guid_327_rank_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 75 guidance distress to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(50)
    return _rank_pct(base, 21)

def guid_328_rank_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 75 guidance distress to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(50)
    return _rank_pct(base, 63)

def guid_329_rank_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 75 guidance distress to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(50)
    return _rank_pct(base, 126)

def guid_330_rank_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 75 guidance distress to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(50)
    return _rank_pct(base, 252)

def guid_331_skew_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 75 guidance distress distribution over 5d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(50)
    return _rolling_skew(base, 5)

def guid_332_skew_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 75 guidance distress distribution over 21d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(50)
    return _rolling_skew(base, 21)

def guid_333_skew_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 75 guidance distress distribution over 63d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(50)
    return _rolling_skew(base, 63)

def guid_334_skew_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 75 guidance distress distribution over 126d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(50)
    return _rolling_skew(base, 126)

def guid_335_skew_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 75 guidance distress distribution over 252d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(50)
    return _rolling_skew(base, 252)

def guid_336_kurt_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 75 guidance distress over 5d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(50)
    return _rolling_kurt(base, 5)

def guid_337_kurt_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 75 guidance distress over 21d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(50)
    return _rolling_kurt(base, 21)

def guid_338_kurt_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 75 guidance distress over 63d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(50)
    return _rolling_kurt(base, 63)

def guid_339_kurt_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 75 guidance distress over 126d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(50)
    return _rolling_kurt(base, 126)

def guid_340_kurt_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 75 guidance distress over 252d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(50)
    return _rolling_kurt(base, 252)

def guid_341_voladj_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 75 guidance distress for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(50)
    return _safe_div(base, _rolling_std(base, 5))

def guid_342_voladj_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 75 guidance distress for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(50)
    return _safe_div(base, _rolling_std(base, 21))

def guid_343_voladj_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 75 guidance distress for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(50)
    return _safe_div(base, _rolling_std(base, 63))

def guid_344_voladj_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 75 guidance distress for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(50)
    return _safe_div(base, _rolling_std(base, 126))

def guid_345_voladj_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 75 guidance distress for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(50)
    return _safe_div(base, _rolling_std(base, 252))

def guid_346_lognorm_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 75 guidance distress over 5d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(50)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def guid_347_lognorm_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 75 guidance distress over 21d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(50)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def guid_348_lognorm_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 75 guidance distress over 63d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(50)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def guid_349_lognorm_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 75 guidance distress over 126d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(50)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def guid_350_lognorm_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 75 guidance distress over 252d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(50)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def guid_351_lvl_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 75 guidance distress over a 5d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(55)
    return _rolling_mean(base, 5)

def guid_352_lvl_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 75 guidance distress over a 21d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(55)
    return _rolling_mean(base, 21)

def guid_353_lvl_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 75 guidance distress over a 63d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(55)
    return _rolling_mean(base, 63)

def guid_354_lvl_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 75 guidance distress over a 126d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(55)
    return _rolling_mean(base, 126)

def guid_355_lvl_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 75 guidance distress over a 252d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(55)
    return _rolling_mean(base, 252)

def guid_356_zscore_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 75 guidance distress by measuring deviations from the 5d mean.
    """
    base = marketcap.pct_change(55)
    return _zscore_rolling(base, 5)

def guid_357_zscore_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 75 guidance distress by measuring deviations from the 21d mean.
    """
    base = marketcap.pct_change(55)
    return _zscore_rolling(base, 21)

def guid_358_zscore_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 75 guidance distress by measuring deviations from the 63d mean.
    """
    base = marketcap.pct_change(55)
    return _zscore_rolling(base, 63)

def guid_359_zscore_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 75 guidance distress by measuring deviations from the 126d mean.
    """
    base = marketcap.pct_change(55)
    return _zscore_rolling(base, 126)

def guid_360_zscore_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 75 guidance distress by measuring deviations from the 252d mean.
    """
    base = marketcap.pct_change(55)
    return _zscore_rolling(base, 252)

def guid_361_rank_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 75 guidance distress to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(55)
    return _rank_pct(base, 5)

def guid_362_rank_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 75 guidance distress to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(55)
    return _rank_pct(base, 21)

def guid_363_rank_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 75 guidance distress to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(55)
    return _rank_pct(base, 63)

def guid_364_rank_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 75 guidance distress to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(55)
    return _rank_pct(base, 126)

def guid_365_rank_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 75 guidance distress to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(55)
    return _rank_pct(base, 252)

def guid_366_skew_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 75 guidance distress distribution over 5d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(55)
    return _rolling_skew(base, 5)

def guid_367_skew_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 75 guidance distress distribution over 21d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(55)
    return _rolling_skew(base, 21)

def guid_368_skew_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 75 guidance distress distribution over 63d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(55)
    return _rolling_skew(base, 63)

def guid_369_skew_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 75 guidance distress distribution over 126d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(55)
    return _rolling_skew(base, 126)

def guid_370_skew_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 75 guidance distress distribution over 252d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(55)
    return _rolling_skew(base, 252)

def guid_371_kurt_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 75 guidance distress over 5d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(55)
    return _rolling_kurt(base, 5)

def guid_372_kurt_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 75 guidance distress over 21d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(55)
    return _rolling_kurt(base, 21)

def guid_373_kurt_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 75 guidance distress over 63d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(55)
    return _rolling_kurt(base, 63)

def guid_374_kurt_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 75 guidance distress over 126d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(55)
    return _rolling_kurt(base, 126)

def guid_375_kurt_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 75 guidance distress over 252d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(55)
    return _rolling_kurt(base, 252)
