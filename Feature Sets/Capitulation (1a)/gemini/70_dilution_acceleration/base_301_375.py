"""
70_70_dilution_acceleration — Base Features 301-375
Domain: 70_dilution_acceleration
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

def dilacc_301_kurt_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 70 dilution acceleration over 5d to capture explosive breakdown or reversal points.
    """
    base = opinc.pct_change(45)
    return _rolling_kurt(base, 5)

def dilacc_302_kurt_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 70 dilution acceleration over 21d to capture explosive breakdown or reversal points.
    """
    base = opinc.pct_change(45)
    return _rolling_kurt(base, 21)

def dilacc_303_kurt_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 70 dilution acceleration over 63d to capture explosive breakdown or reversal points.
    """
    base = opinc.pct_change(45)
    return _rolling_kurt(base, 63)

def dilacc_304_kurt_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 70 dilution acceleration over 126d to capture explosive breakdown or reversal points.
    """
    base = opinc.pct_change(45)
    return _rolling_kurt(base, 126)

def dilacc_305_kurt_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 70 dilution acceleration over 252d to capture explosive breakdown or reversal points.
    """
    base = opinc.pct_change(45)
    return _rolling_kurt(base, 252)

def dilacc_306_voladj_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 70 dilution acceleration for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = opinc.pct_change(45)
    return _safe_div(base, _rolling_std(base, 5))

def dilacc_307_voladj_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 70 dilution acceleration for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = opinc.pct_change(45)
    return _safe_div(base, _rolling_std(base, 21))

def dilacc_308_voladj_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 70 dilution acceleration for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = opinc.pct_change(45)
    return _safe_div(base, _rolling_std(base, 63))

def dilacc_309_voladj_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 70 dilution acceleration for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = opinc.pct_change(45)
    return _safe_div(base, _rolling_std(base, 126))

def dilacc_310_voladj_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 70 dilution acceleration for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = opinc.pct_change(45)
    return _safe_div(base, _rolling_std(base, 252))

def dilacc_311_lognorm_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 70 dilution acceleration over 5d to stabilize variance and capture exponential shifts.
    """
    base = opinc.pct_change(45)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def dilacc_312_lognorm_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 70 dilution acceleration over 21d to stabilize variance and capture exponential shifts.
    """
    base = opinc.pct_change(45)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def dilacc_313_lognorm_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 70 dilution acceleration over 63d to stabilize variance and capture exponential shifts.
    """
    base = opinc.pct_change(45)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def dilacc_314_lognorm_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 70 dilution acceleration over 126d to stabilize variance and capture exponential shifts.
    """
    base = opinc.pct_change(45)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def dilacc_315_lognorm_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 70 dilution acceleration over 252d to stabilize variance and capture exponential shifts.
    """
    base = opinc.pct_change(45)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def dilacc_316_lvl_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 70 dilution acceleration over a 5d horizon to identify extreme regimes.
    """
    base = opinc.pct_change(50)
    return _rolling_mean(base, 5)

def dilacc_317_lvl_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 70 dilution acceleration over a 21d horizon to identify extreme regimes.
    """
    base = opinc.pct_change(50)
    return _rolling_mean(base, 21)

def dilacc_318_lvl_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 70 dilution acceleration over a 63d horizon to identify extreme regimes.
    """
    base = opinc.pct_change(50)
    return _rolling_mean(base, 63)

def dilacc_319_lvl_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 70 dilution acceleration over a 126d horizon to identify extreme regimes.
    """
    base = opinc.pct_change(50)
    return _rolling_mean(base, 126)

def dilacc_320_lvl_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 70 dilution acceleration over a 252d horizon to identify extreme regimes.
    """
    base = opinc.pct_change(50)
    return _rolling_mean(base, 252)

def dilacc_321_zscore_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 70 dilution acceleration by measuring deviations from the 5d mean.
    """
    base = opinc.pct_change(50)
    return _zscore_rolling(base, 5)

def dilacc_322_zscore_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 70 dilution acceleration by measuring deviations from the 21d mean.
    """
    base = opinc.pct_change(50)
    return _zscore_rolling(base, 21)

def dilacc_323_zscore_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 70 dilution acceleration by measuring deviations from the 63d mean.
    """
    base = opinc.pct_change(50)
    return _zscore_rolling(base, 63)

def dilacc_324_zscore_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 70 dilution acceleration by measuring deviations from the 126d mean.
    """
    base = opinc.pct_change(50)
    return _zscore_rolling(base, 126)

def dilacc_325_zscore_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 70 dilution acceleration by measuring deviations from the 252d mean.
    """
    base = opinc.pct_change(50)
    return _zscore_rolling(base, 252)

def dilacc_326_rank_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 70 dilution acceleration to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = opinc.pct_change(50)
    return _rank_pct(base, 5)

def dilacc_327_rank_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 70 dilution acceleration to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = opinc.pct_change(50)
    return _rank_pct(base, 21)

def dilacc_328_rank_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 70 dilution acceleration to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = opinc.pct_change(50)
    return _rank_pct(base, 63)

def dilacc_329_rank_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 70 dilution acceleration to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = opinc.pct_change(50)
    return _rank_pct(base, 126)

def dilacc_330_rank_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 70 dilution acceleration to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = opinc.pct_change(50)
    return _rank_pct(base, 252)

def dilacc_331_skew_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 70 dilution acceleration distribution over 5d to detect tail risk or exhaustion.
    """
    base = opinc.pct_change(50)
    return _rolling_skew(base, 5)

def dilacc_332_skew_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 70 dilution acceleration distribution over 21d to detect tail risk or exhaustion.
    """
    base = opinc.pct_change(50)
    return _rolling_skew(base, 21)

def dilacc_333_skew_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 70 dilution acceleration distribution over 63d to detect tail risk or exhaustion.
    """
    base = opinc.pct_change(50)
    return _rolling_skew(base, 63)

def dilacc_334_skew_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 70 dilution acceleration distribution over 126d to detect tail risk or exhaustion.
    """
    base = opinc.pct_change(50)
    return _rolling_skew(base, 126)

def dilacc_335_skew_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 70 dilution acceleration distribution over 252d to detect tail risk or exhaustion.
    """
    base = opinc.pct_change(50)
    return _rolling_skew(base, 252)

def dilacc_336_kurt_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 70 dilution acceleration over 5d to capture explosive breakdown or reversal points.
    """
    base = opinc.pct_change(50)
    return _rolling_kurt(base, 5)

def dilacc_337_kurt_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 70 dilution acceleration over 21d to capture explosive breakdown or reversal points.
    """
    base = opinc.pct_change(50)
    return _rolling_kurt(base, 21)

def dilacc_338_kurt_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 70 dilution acceleration over 63d to capture explosive breakdown or reversal points.
    """
    base = opinc.pct_change(50)
    return _rolling_kurt(base, 63)

def dilacc_339_kurt_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 70 dilution acceleration over 126d to capture explosive breakdown or reversal points.
    """
    base = opinc.pct_change(50)
    return _rolling_kurt(base, 126)

def dilacc_340_kurt_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 70 dilution acceleration over 252d to capture explosive breakdown or reversal points.
    """
    base = opinc.pct_change(50)
    return _rolling_kurt(base, 252)

def dilacc_341_voladj_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 70 dilution acceleration for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = opinc.pct_change(50)
    return _safe_div(base, _rolling_std(base, 5))

def dilacc_342_voladj_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 70 dilution acceleration for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = opinc.pct_change(50)
    return _safe_div(base, _rolling_std(base, 21))

def dilacc_343_voladj_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 70 dilution acceleration for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = opinc.pct_change(50)
    return _safe_div(base, _rolling_std(base, 63))

def dilacc_344_voladj_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 70 dilution acceleration for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = opinc.pct_change(50)
    return _safe_div(base, _rolling_std(base, 126))

def dilacc_345_voladj_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 70 dilution acceleration for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = opinc.pct_change(50)
    return _safe_div(base, _rolling_std(base, 252))

def dilacc_346_lognorm_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 70 dilution acceleration over 5d to stabilize variance and capture exponential shifts.
    """
    base = opinc.pct_change(50)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def dilacc_347_lognorm_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 70 dilution acceleration over 21d to stabilize variance and capture exponential shifts.
    """
    base = opinc.pct_change(50)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def dilacc_348_lognorm_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 70 dilution acceleration over 63d to stabilize variance and capture exponential shifts.
    """
    base = opinc.pct_change(50)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def dilacc_349_lognorm_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 70 dilution acceleration over 126d to stabilize variance and capture exponential shifts.
    """
    base = opinc.pct_change(50)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def dilacc_350_lognorm_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 70 dilution acceleration over 252d to stabilize variance and capture exponential shifts.
    """
    base = opinc.pct_change(50)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def dilacc_351_lvl_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 70 dilution acceleration over a 5d horizon to identify extreme regimes.
    """
    base = opinc.pct_change(55)
    return _rolling_mean(base, 5)

def dilacc_352_lvl_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 70 dilution acceleration over a 21d horizon to identify extreme regimes.
    """
    base = opinc.pct_change(55)
    return _rolling_mean(base, 21)

def dilacc_353_lvl_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 70 dilution acceleration over a 63d horizon to identify extreme regimes.
    """
    base = opinc.pct_change(55)
    return _rolling_mean(base, 63)

def dilacc_354_lvl_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 70 dilution acceleration over a 126d horizon to identify extreme regimes.
    """
    base = opinc.pct_change(55)
    return _rolling_mean(base, 126)

def dilacc_355_lvl_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 70 dilution acceleration over a 252d horizon to identify extreme regimes.
    """
    base = opinc.pct_change(55)
    return _rolling_mean(base, 252)

def dilacc_356_zscore_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 70 dilution acceleration by measuring deviations from the 5d mean.
    """
    base = opinc.pct_change(55)
    return _zscore_rolling(base, 5)

def dilacc_357_zscore_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 70 dilution acceleration by measuring deviations from the 21d mean.
    """
    base = opinc.pct_change(55)
    return _zscore_rolling(base, 21)

def dilacc_358_zscore_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 70 dilution acceleration by measuring deviations from the 63d mean.
    """
    base = opinc.pct_change(55)
    return _zscore_rolling(base, 63)

def dilacc_359_zscore_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 70 dilution acceleration by measuring deviations from the 126d mean.
    """
    base = opinc.pct_change(55)
    return _zscore_rolling(base, 126)

def dilacc_360_zscore_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 70 dilution acceleration by measuring deviations from the 252d mean.
    """
    base = opinc.pct_change(55)
    return _zscore_rolling(base, 252)

def dilacc_361_rank_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 70 dilution acceleration to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = opinc.pct_change(55)
    return _rank_pct(base, 5)

def dilacc_362_rank_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 70 dilution acceleration to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = opinc.pct_change(55)
    return _rank_pct(base, 21)

def dilacc_363_rank_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 70 dilution acceleration to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = opinc.pct_change(55)
    return _rank_pct(base, 63)

def dilacc_364_rank_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 70 dilution acceleration to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = opinc.pct_change(55)
    return _rank_pct(base, 126)

def dilacc_365_rank_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 70 dilution acceleration to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = opinc.pct_change(55)
    return _rank_pct(base, 252)

def dilacc_366_skew_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 70 dilution acceleration distribution over 5d to detect tail risk or exhaustion.
    """
    base = opinc.pct_change(55)
    return _rolling_skew(base, 5)

def dilacc_367_skew_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 70 dilution acceleration distribution over 21d to detect tail risk or exhaustion.
    """
    base = opinc.pct_change(55)
    return _rolling_skew(base, 21)

def dilacc_368_skew_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 70 dilution acceleration distribution over 63d to detect tail risk or exhaustion.
    """
    base = opinc.pct_change(55)
    return _rolling_skew(base, 63)

def dilacc_369_skew_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 70 dilution acceleration distribution over 126d to detect tail risk or exhaustion.
    """
    base = opinc.pct_change(55)
    return _rolling_skew(base, 126)

def dilacc_370_skew_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 70 dilution acceleration distribution over 252d to detect tail risk or exhaustion.
    """
    base = opinc.pct_change(55)
    return _rolling_skew(base, 252)

def dilacc_371_kurt_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 70 dilution acceleration over 5d to capture explosive breakdown or reversal points.
    """
    base = opinc.pct_change(55)
    return _rolling_kurt(base, 5)

def dilacc_372_kurt_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 70 dilution acceleration over 21d to capture explosive breakdown or reversal points.
    """
    base = opinc.pct_change(55)
    return _rolling_kurt(base, 21)

def dilacc_373_kurt_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 70 dilution acceleration over 63d to capture explosive breakdown or reversal points.
    """
    base = opinc.pct_change(55)
    return _rolling_kurt(base, 63)

def dilacc_374_kurt_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 70 dilution acceleration over 126d to capture explosive breakdown or reversal points.
    """
    base = opinc.pct_change(55)
    return _rolling_kurt(base, 126)

def dilacc_375_kurt_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 70 dilution acceleration over 252d to capture explosive breakdown or reversal points.
    """
    base = opinc.pct_change(55)
    return _rolling_kurt(base, 252)
