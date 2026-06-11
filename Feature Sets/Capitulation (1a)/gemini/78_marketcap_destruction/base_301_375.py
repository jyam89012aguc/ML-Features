"""
78_78_marketcap_destruction — Base Features 301-375
Domain: 78_marketcap_destruction
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

def mdes_301_kurt_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 78 marketcap destruction over 5d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(45)
    return _rolling_kurt(base, 5)

def mdes_302_kurt_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 78 marketcap destruction over 21d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(45)
    return _rolling_kurt(base, 21)

def mdes_303_kurt_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 78 marketcap destruction over 63d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(45)
    return _rolling_kurt(base, 63)

def mdes_304_kurt_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 78 marketcap destruction over 126d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(45)
    return _rolling_kurt(base, 126)

def mdes_305_kurt_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 78 marketcap destruction over 252d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(45)
    return _rolling_kurt(base, 252)

def mdes_306_voladj_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 78 marketcap destruction for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(45)
    return _safe_div(base, _rolling_std(base, 5))

def mdes_307_voladj_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 78 marketcap destruction for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(45)
    return _safe_div(base, _rolling_std(base, 21))

def mdes_308_voladj_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 78 marketcap destruction for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(45)
    return _safe_div(base, _rolling_std(base, 63))

def mdes_309_voladj_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 78 marketcap destruction for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(45)
    return _safe_div(base, _rolling_std(base, 126))

def mdes_310_voladj_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 78 marketcap destruction for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(45)
    return _safe_div(base, _rolling_std(base, 252))

def mdes_311_lognorm_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 78 marketcap destruction over 5d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(45)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def mdes_312_lognorm_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 78 marketcap destruction over 21d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(45)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def mdes_313_lognorm_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 78 marketcap destruction over 63d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(45)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def mdes_314_lognorm_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 78 marketcap destruction over 126d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(45)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def mdes_315_lognorm_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 78 marketcap destruction over 252d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(45)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def mdes_316_lvl_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 78 marketcap destruction over a 5d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(50)
    return _rolling_mean(base, 5)

def mdes_317_lvl_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 78 marketcap destruction over a 21d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(50)
    return _rolling_mean(base, 21)

def mdes_318_lvl_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 78 marketcap destruction over a 63d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(50)
    return _rolling_mean(base, 63)

def mdes_319_lvl_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 78 marketcap destruction over a 126d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(50)
    return _rolling_mean(base, 126)

def mdes_320_lvl_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 78 marketcap destruction over a 252d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(50)
    return _rolling_mean(base, 252)

def mdes_321_zscore_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 78 marketcap destruction by measuring deviations from the 5d mean.
    """
    base = marketcap.pct_change(50)
    return _zscore_rolling(base, 5)

def mdes_322_zscore_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 78 marketcap destruction by measuring deviations from the 21d mean.
    """
    base = marketcap.pct_change(50)
    return _zscore_rolling(base, 21)

def mdes_323_zscore_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 78 marketcap destruction by measuring deviations from the 63d mean.
    """
    base = marketcap.pct_change(50)
    return _zscore_rolling(base, 63)

def mdes_324_zscore_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 78 marketcap destruction by measuring deviations from the 126d mean.
    """
    base = marketcap.pct_change(50)
    return _zscore_rolling(base, 126)

def mdes_325_zscore_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 78 marketcap destruction by measuring deviations from the 252d mean.
    """
    base = marketcap.pct_change(50)
    return _zscore_rolling(base, 252)

def mdes_326_rank_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 78 marketcap destruction to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(50)
    return _rank_pct(base, 5)

def mdes_327_rank_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 78 marketcap destruction to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(50)
    return _rank_pct(base, 21)

def mdes_328_rank_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 78 marketcap destruction to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(50)
    return _rank_pct(base, 63)

def mdes_329_rank_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 78 marketcap destruction to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(50)
    return _rank_pct(base, 126)

def mdes_330_rank_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 78 marketcap destruction to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(50)
    return _rank_pct(base, 252)

def mdes_331_skew_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 78 marketcap destruction distribution over 5d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(50)
    return _rolling_skew(base, 5)

def mdes_332_skew_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 78 marketcap destruction distribution over 21d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(50)
    return _rolling_skew(base, 21)

def mdes_333_skew_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 78 marketcap destruction distribution over 63d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(50)
    return _rolling_skew(base, 63)

def mdes_334_skew_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 78 marketcap destruction distribution over 126d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(50)
    return _rolling_skew(base, 126)

def mdes_335_skew_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 78 marketcap destruction distribution over 252d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(50)
    return _rolling_skew(base, 252)

def mdes_336_kurt_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 78 marketcap destruction over 5d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(50)
    return _rolling_kurt(base, 5)

def mdes_337_kurt_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 78 marketcap destruction over 21d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(50)
    return _rolling_kurt(base, 21)

def mdes_338_kurt_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 78 marketcap destruction over 63d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(50)
    return _rolling_kurt(base, 63)

def mdes_339_kurt_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 78 marketcap destruction over 126d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(50)
    return _rolling_kurt(base, 126)

def mdes_340_kurt_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 78 marketcap destruction over 252d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(50)
    return _rolling_kurt(base, 252)

def mdes_341_voladj_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 78 marketcap destruction for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(50)
    return _safe_div(base, _rolling_std(base, 5))

def mdes_342_voladj_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 78 marketcap destruction for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(50)
    return _safe_div(base, _rolling_std(base, 21))

def mdes_343_voladj_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 78 marketcap destruction for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(50)
    return _safe_div(base, _rolling_std(base, 63))

def mdes_344_voladj_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 78 marketcap destruction for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(50)
    return _safe_div(base, _rolling_std(base, 126))

def mdes_345_voladj_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 78 marketcap destruction for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(50)
    return _safe_div(base, _rolling_std(base, 252))

def mdes_346_lognorm_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 78 marketcap destruction over 5d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(50)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def mdes_347_lognorm_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 78 marketcap destruction over 21d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(50)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def mdes_348_lognorm_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 78 marketcap destruction over 63d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(50)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def mdes_349_lognorm_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 78 marketcap destruction over 126d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(50)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def mdes_350_lognorm_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 78 marketcap destruction over 252d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(50)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def mdes_351_lvl_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 78 marketcap destruction over a 5d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(55)
    return _rolling_mean(base, 5)

def mdes_352_lvl_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 78 marketcap destruction over a 21d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(55)
    return _rolling_mean(base, 21)

def mdes_353_lvl_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 78 marketcap destruction over a 63d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(55)
    return _rolling_mean(base, 63)

def mdes_354_lvl_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 78 marketcap destruction over a 126d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(55)
    return _rolling_mean(base, 126)

def mdes_355_lvl_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 78 marketcap destruction over a 252d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(55)
    return _rolling_mean(base, 252)

def mdes_356_zscore_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 78 marketcap destruction by measuring deviations from the 5d mean.
    """
    base = marketcap.pct_change(55)
    return _zscore_rolling(base, 5)

def mdes_357_zscore_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 78 marketcap destruction by measuring deviations from the 21d mean.
    """
    base = marketcap.pct_change(55)
    return _zscore_rolling(base, 21)

def mdes_358_zscore_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 78 marketcap destruction by measuring deviations from the 63d mean.
    """
    base = marketcap.pct_change(55)
    return _zscore_rolling(base, 63)

def mdes_359_zscore_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 78 marketcap destruction by measuring deviations from the 126d mean.
    """
    base = marketcap.pct_change(55)
    return _zscore_rolling(base, 126)

def mdes_360_zscore_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 78 marketcap destruction by measuring deviations from the 252d mean.
    """
    base = marketcap.pct_change(55)
    return _zscore_rolling(base, 252)

def mdes_361_rank_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 78 marketcap destruction to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(55)
    return _rank_pct(base, 5)

def mdes_362_rank_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 78 marketcap destruction to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(55)
    return _rank_pct(base, 21)

def mdes_363_rank_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 78 marketcap destruction to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(55)
    return _rank_pct(base, 63)

def mdes_364_rank_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 78 marketcap destruction to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(55)
    return _rank_pct(base, 126)

def mdes_365_rank_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 78 marketcap destruction to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(55)
    return _rank_pct(base, 252)

def mdes_366_skew_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 78 marketcap destruction distribution over 5d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(55)
    return _rolling_skew(base, 5)

def mdes_367_skew_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 78 marketcap destruction distribution over 21d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(55)
    return _rolling_skew(base, 21)

def mdes_368_skew_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 78 marketcap destruction distribution over 63d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(55)
    return _rolling_skew(base, 63)

def mdes_369_skew_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 78 marketcap destruction distribution over 126d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(55)
    return _rolling_skew(base, 126)

def mdes_370_skew_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 78 marketcap destruction distribution over 252d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(55)
    return _rolling_skew(base, 252)

def mdes_371_kurt_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 78 marketcap destruction over 5d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(55)
    return _rolling_kurt(base, 5)

def mdes_372_kurt_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 78 marketcap destruction over 21d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(55)
    return _rolling_kurt(base, 21)

def mdes_373_kurt_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 78 marketcap destruction over 63d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(55)
    return _rolling_kurt(base, 63)

def mdes_374_kurt_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 78 marketcap destruction over 126d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(55)
    return _rolling_kurt(base, 126)

def mdes_375_kurt_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 78 marketcap destruction over 252d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(55)
    return _rolling_kurt(base, 252)
