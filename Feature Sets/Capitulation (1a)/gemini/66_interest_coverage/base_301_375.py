"""
66_66_interest_coverage — Base Features 301-375
Domain: 66_interest_coverage
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

def icov_301_kurt_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 66 interest coverage over 5d to capture explosive breakdown or reversal points.
    """
    base = opinc.pct_change(45)
    return _rolling_kurt(base, 5)

def icov_302_kurt_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 66 interest coverage over 21d to capture explosive breakdown or reversal points.
    """
    base = opinc.pct_change(45)
    return _rolling_kurt(base, 21)

def icov_303_kurt_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 66 interest coverage over 63d to capture explosive breakdown or reversal points.
    """
    base = opinc.pct_change(45)
    return _rolling_kurt(base, 63)

def icov_304_kurt_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 66 interest coverage over 126d to capture explosive breakdown or reversal points.
    """
    base = opinc.pct_change(45)
    return _rolling_kurt(base, 126)

def icov_305_kurt_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 66 interest coverage over 252d to capture explosive breakdown or reversal points.
    """
    base = opinc.pct_change(45)
    return _rolling_kurt(base, 252)

def icov_306_voladj_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 66 interest coverage for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = opinc.pct_change(45)
    return _safe_div(base, _rolling_std(base, 5))

def icov_307_voladj_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 66 interest coverage for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = opinc.pct_change(45)
    return _safe_div(base, _rolling_std(base, 21))

def icov_308_voladj_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 66 interest coverage for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = opinc.pct_change(45)
    return _safe_div(base, _rolling_std(base, 63))

def icov_309_voladj_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 66 interest coverage for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = opinc.pct_change(45)
    return _safe_div(base, _rolling_std(base, 126))

def icov_310_voladj_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 66 interest coverage for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = opinc.pct_change(45)
    return _safe_div(base, _rolling_std(base, 252))

def icov_311_lognorm_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 66 interest coverage over 5d to stabilize variance and capture exponential shifts.
    """
    base = opinc.pct_change(45)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def icov_312_lognorm_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 66 interest coverage over 21d to stabilize variance and capture exponential shifts.
    """
    base = opinc.pct_change(45)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def icov_313_lognorm_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 66 interest coverage over 63d to stabilize variance and capture exponential shifts.
    """
    base = opinc.pct_change(45)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def icov_314_lognorm_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 66 interest coverage over 126d to stabilize variance and capture exponential shifts.
    """
    base = opinc.pct_change(45)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def icov_315_lognorm_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 66 interest coverage over 252d to stabilize variance and capture exponential shifts.
    """
    base = opinc.pct_change(45)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def icov_316_lvl_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 66 interest coverage over a 5d horizon to identify extreme regimes.
    """
    base = opinc.pct_change(50)
    return _rolling_mean(base, 5)

def icov_317_lvl_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 66 interest coverage over a 21d horizon to identify extreme regimes.
    """
    base = opinc.pct_change(50)
    return _rolling_mean(base, 21)

def icov_318_lvl_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 66 interest coverage over a 63d horizon to identify extreme regimes.
    """
    base = opinc.pct_change(50)
    return _rolling_mean(base, 63)

def icov_319_lvl_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 66 interest coverage over a 126d horizon to identify extreme regimes.
    """
    base = opinc.pct_change(50)
    return _rolling_mean(base, 126)

def icov_320_lvl_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 66 interest coverage over a 252d horizon to identify extreme regimes.
    """
    base = opinc.pct_change(50)
    return _rolling_mean(base, 252)

def icov_321_zscore_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 66 interest coverage by measuring deviations from the 5d mean.
    """
    base = opinc.pct_change(50)
    return _zscore_rolling(base, 5)

def icov_322_zscore_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 66 interest coverage by measuring deviations from the 21d mean.
    """
    base = opinc.pct_change(50)
    return _zscore_rolling(base, 21)

def icov_323_zscore_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 66 interest coverage by measuring deviations from the 63d mean.
    """
    base = opinc.pct_change(50)
    return _zscore_rolling(base, 63)

def icov_324_zscore_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 66 interest coverage by measuring deviations from the 126d mean.
    """
    base = opinc.pct_change(50)
    return _zscore_rolling(base, 126)

def icov_325_zscore_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 66 interest coverage by measuring deviations from the 252d mean.
    """
    base = opinc.pct_change(50)
    return _zscore_rolling(base, 252)

def icov_326_rank_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 66 interest coverage to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = opinc.pct_change(50)
    return _rank_pct(base, 5)

def icov_327_rank_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 66 interest coverage to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = opinc.pct_change(50)
    return _rank_pct(base, 21)

def icov_328_rank_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 66 interest coverage to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = opinc.pct_change(50)
    return _rank_pct(base, 63)

def icov_329_rank_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 66 interest coverage to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = opinc.pct_change(50)
    return _rank_pct(base, 126)

def icov_330_rank_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 66 interest coverage to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = opinc.pct_change(50)
    return _rank_pct(base, 252)

def icov_331_skew_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 66 interest coverage distribution over 5d to detect tail risk or exhaustion.
    """
    base = opinc.pct_change(50)
    return _rolling_skew(base, 5)

def icov_332_skew_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 66 interest coverage distribution over 21d to detect tail risk or exhaustion.
    """
    base = opinc.pct_change(50)
    return _rolling_skew(base, 21)

def icov_333_skew_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 66 interest coverage distribution over 63d to detect tail risk or exhaustion.
    """
    base = opinc.pct_change(50)
    return _rolling_skew(base, 63)

def icov_334_skew_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 66 interest coverage distribution over 126d to detect tail risk or exhaustion.
    """
    base = opinc.pct_change(50)
    return _rolling_skew(base, 126)

def icov_335_skew_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 66 interest coverage distribution over 252d to detect tail risk or exhaustion.
    """
    base = opinc.pct_change(50)
    return _rolling_skew(base, 252)

def icov_336_kurt_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 66 interest coverage over 5d to capture explosive breakdown or reversal points.
    """
    base = opinc.pct_change(50)
    return _rolling_kurt(base, 5)

def icov_337_kurt_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 66 interest coverage over 21d to capture explosive breakdown or reversal points.
    """
    base = opinc.pct_change(50)
    return _rolling_kurt(base, 21)

def icov_338_kurt_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 66 interest coverage over 63d to capture explosive breakdown or reversal points.
    """
    base = opinc.pct_change(50)
    return _rolling_kurt(base, 63)

def icov_339_kurt_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 66 interest coverage over 126d to capture explosive breakdown or reversal points.
    """
    base = opinc.pct_change(50)
    return _rolling_kurt(base, 126)

def icov_340_kurt_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 66 interest coverage over 252d to capture explosive breakdown or reversal points.
    """
    base = opinc.pct_change(50)
    return _rolling_kurt(base, 252)

def icov_341_voladj_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 66 interest coverage for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = opinc.pct_change(50)
    return _safe_div(base, _rolling_std(base, 5))

def icov_342_voladj_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 66 interest coverage for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = opinc.pct_change(50)
    return _safe_div(base, _rolling_std(base, 21))

def icov_343_voladj_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 66 interest coverage for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = opinc.pct_change(50)
    return _safe_div(base, _rolling_std(base, 63))

def icov_344_voladj_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 66 interest coverage for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = opinc.pct_change(50)
    return _safe_div(base, _rolling_std(base, 126))

def icov_345_voladj_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 66 interest coverage for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = opinc.pct_change(50)
    return _safe_div(base, _rolling_std(base, 252))

def icov_346_lognorm_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 66 interest coverage over 5d to stabilize variance and capture exponential shifts.
    """
    base = opinc.pct_change(50)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def icov_347_lognorm_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 66 interest coverage over 21d to stabilize variance and capture exponential shifts.
    """
    base = opinc.pct_change(50)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def icov_348_lognorm_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 66 interest coverage over 63d to stabilize variance and capture exponential shifts.
    """
    base = opinc.pct_change(50)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def icov_349_lognorm_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 66 interest coverage over 126d to stabilize variance and capture exponential shifts.
    """
    base = opinc.pct_change(50)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def icov_350_lognorm_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 66 interest coverage over 252d to stabilize variance and capture exponential shifts.
    """
    base = opinc.pct_change(50)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def icov_351_lvl_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 66 interest coverage over a 5d horizon to identify extreme regimes.
    """
    base = opinc.pct_change(55)
    return _rolling_mean(base, 5)

def icov_352_lvl_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 66 interest coverage over a 21d horizon to identify extreme regimes.
    """
    base = opinc.pct_change(55)
    return _rolling_mean(base, 21)

def icov_353_lvl_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 66 interest coverage over a 63d horizon to identify extreme regimes.
    """
    base = opinc.pct_change(55)
    return _rolling_mean(base, 63)

def icov_354_lvl_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 66 interest coverage over a 126d horizon to identify extreme regimes.
    """
    base = opinc.pct_change(55)
    return _rolling_mean(base, 126)

def icov_355_lvl_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 66 interest coverage over a 252d horizon to identify extreme regimes.
    """
    base = opinc.pct_change(55)
    return _rolling_mean(base, 252)

def icov_356_zscore_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 66 interest coverage by measuring deviations from the 5d mean.
    """
    base = opinc.pct_change(55)
    return _zscore_rolling(base, 5)

def icov_357_zscore_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 66 interest coverage by measuring deviations from the 21d mean.
    """
    base = opinc.pct_change(55)
    return _zscore_rolling(base, 21)

def icov_358_zscore_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 66 interest coverage by measuring deviations from the 63d mean.
    """
    base = opinc.pct_change(55)
    return _zscore_rolling(base, 63)

def icov_359_zscore_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 66 interest coverage by measuring deviations from the 126d mean.
    """
    base = opinc.pct_change(55)
    return _zscore_rolling(base, 126)

def icov_360_zscore_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 66 interest coverage by measuring deviations from the 252d mean.
    """
    base = opinc.pct_change(55)
    return _zscore_rolling(base, 252)

def icov_361_rank_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 66 interest coverage to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = opinc.pct_change(55)
    return _rank_pct(base, 5)

def icov_362_rank_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 66 interest coverage to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = opinc.pct_change(55)
    return _rank_pct(base, 21)

def icov_363_rank_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 66 interest coverage to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = opinc.pct_change(55)
    return _rank_pct(base, 63)

def icov_364_rank_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 66 interest coverage to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = opinc.pct_change(55)
    return _rank_pct(base, 126)

def icov_365_rank_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 66 interest coverage to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = opinc.pct_change(55)
    return _rank_pct(base, 252)

def icov_366_skew_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 66 interest coverage distribution over 5d to detect tail risk or exhaustion.
    """
    base = opinc.pct_change(55)
    return _rolling_skew(base, 5)

def icov_367_skew_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 66 interest coverage distribution over 21d to detect tail risk or exhaustion.
    """
    base = opinc.pct_change(55)
    return _rolling_skew(base, 21)

def icov_368_skew_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 66 interest coverage distribution over 63d to detect tail risk or exhaustion.
    """
    base = opinc.pct_change(55)
    return _rolling_skew(base, 63)

def icov_369_skew_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 66 interest coverage distribution over 126d to detect tail risk or exhaustion.
    """
    base = opinc.pct_change(55)
    return _rolling_skew(base, 126)

def icov_370_skew_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 66 interest coverage distribution over 252d to detect tail risk or exhaustion.
    """
    base = opinc.pct_change(55)
    return _rolling_skew(base, 252)

def icov_371_kurt_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 66 interest coverage over 5d to capture explosive breakdown or reversal points.
    """
    base = opinc.pct_change(55)
    return _rolling_kurt(base, 5)

def icov_372_kurt_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 66 interest coverage over 21d to capture explosive breakdown or reversal points.
    """
    base = opinc.pct_change(55)
    return _rolling_kurt(base, 21)

def icov_373_kurt_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 66 interest coverage over 63d to capture explosive breakdown or reversal points.
    """
    base = opinc.pct_change(55)
    return _rolling_kurt(base, 63)

def icov_374_kurt_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 66 interest coverage over 126d to capture explosive breakdown or reversal points.
    """
    base = opinc.pct_change(55)
    return _rolling_kurt(base, 126)

def icov_375_kurt_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 66 interest coverage over 252d to capture explosive breakdown or reversal points.
    """
    base = opinc.pct_change(55)
    return _rolling_kurt(base, 252)
