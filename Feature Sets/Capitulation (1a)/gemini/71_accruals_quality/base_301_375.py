"""
71_71_accruals_quality — Base Features 301-375
Domain: 71_accruals_quality
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

def accq_301_kurt_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 71 accruals quality over 5d to capture explosive breakdown or reversal points.
    """
    base = opinc.pct_change(45)
    return _rolling_kurt(base, 5)

def accq_302_kurt_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 71 accruals quality over 21d to capture explosive breakdown or reversal points.
    """
    base = opinc.pct_change(45)
    return _rolling_kurt(base, 21)

def accq_303_kurt_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 71 accruals quality over 63d to capture explosive breakdown or reversal points.
    """
    base = opinc.pct_change(45)
    return _rolling_kurt(base, 63)

def accq_304_kurt_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 71 accruals quality over 126d to capture explosive breakdown or reversal points.
    """
    base = opinc.pct_change(45)
    return _rolling_kurt(base, 126)

def accq_305_kurt_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 71 accruals quality over 252d to capture explosive breakdown or reversal points.
    """
    base = opinc.pct_change(45)
    return _rolling_kurt(base, 252)

def accq_306_voladj_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 71 accruals quality for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = opinc.pct_change(45)
    return _safe_div(base, _rolling_std(base, 5))

def accq_307_voladj_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 71 accruals quality for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = opinc.pct_change(45)
    return _safe_div(base, _rolling_std(base, 21))

def accq_308_voladj_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 71 accruals quality for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = opinc.pct_change(45)
    return _safe_div(base, _rolling_std(base, 63))

def accq_309_voladj_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 71 accruals quality for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = opinc.pct_change(45)
    return _safe_div(base, _rolling_std(base, 126))

def accq_310_voladj_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 71 accruals quality for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = opinc.pct_change(45)
    return _safe_div(base, _rolling_std(base, 252))

def accq_311_lognorm_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 71 accruals quality over 5d to stabilize variance and capture exponential shifts.
    """
    base = opinc.pct_change(45)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def accq_312_lognorm_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 71 accruals quality over 21d to stabilize variance and capture exponential shifts.
    """
    base = opinc.pct_change(45)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def accq_313_lognorm_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 71 accruals quality over 63d to stabilize variance and capture exponential shifts.
    """
    base = opinc.pct_change(45)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def accq_314_lognorm_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 71 accruals quality over 126d to stabilize variance and capture exponential shifts.
    """
    base = opinc.pct_change(45)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def accq_315_lognorm_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 71 accruals quality over 252d to stabilize variance and capture exponential shifts.
    """
    base = opinc.pct_change(45)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def accq_316_lvl_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 71 accruals quality over a 5d horizon to identify extreme regimes.
    """
    base = opinc.pct_change(50)
    return _rolling_mean(base, 5)

def accq_317_lvl_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 71 accruals quality over a 21d horizon to identify extreme regimes.
    """
    base = opinc.pct_change(50)
    return _rolling_mean(base, 21)

def accq_318_lvl_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 71 accruals quality over a 63d horizon to identify extreme regimes.
    """
    base = opinc.pct_change(50)
    return _rolling_mean(base, 63)

def accq_319_lvl_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 71 accruals quality over a 126d horizon to identify extreme regimes.
    """
    base = opinc.pct_change(50)
    return _rolling_mean(base, 126)

def accq_320_lvl_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 71 accruals quality over a 252d horizon to identify extreme regimes.
    """
    base = opinc.pct_change(50)
    return _rolling_mean(base, 252)

def accq_321_zscore_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 71 accruals quality by measuring deviations from the 5d mean.
    """
    base = opinc.pct_change(50)
    return _zscore_rolling(base, 5)

def accq_322_zscore_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 71 accruals quality by measuring deviations from the 21d mean.
    """
    base = opinc.pct_change(50)
    return _zscore_rolling(base, 21)

def accq_323_zscore_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 71 accruals quality by measuring deviations from the 63d mean.
    """
    base = opinc.pct_change(50)
    return _zscore_rolling(base, 63)

def accq_324_zscore_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 71 accruals quality by measuring deviations from the 126d mean.
    """
    base = opinc.pct_change(50)
    return _zscore_rolling(base, 126)

def accq_325_zscore_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 71 accruals quality by measuring deviations from the 252d mean.
    """
    base = opinc.pct_change(50)
    return _zscore_rolling(base, 252)

def accq_326_rank_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 71 accruals quality to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = opinc.pct_change(50)
    return _rank_pct(base, 5)

def accq_327_rank_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 71 accruals quality to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = opinc.pct_change(50)
    return _rank_pct(base, 21)

def accq_328_rank_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 71 accruals quality to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = opinc.pct_change(50)
    return _rank_pct(base, 63)

def accq_329_rank_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 71 accruals quality to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = opinc.pct_change(50)
    return _rank_pct(base, 126)

def accq_330_rank_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 71 accruals quality to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = opinc.pct_change(50)
    return _rank_pct(base, 252)

def accq_331_skew_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 71 accruals quality distribution over 5d to detect tail risk or exhaustion.
    """
    base = opinc.pct_change(50)
    return _rolling_skew(base, 5)

def accq_332_skew_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 71 accruals quality distribution over 21d to detect tail risk or exhaustion.
    """
    base = opinc.pct_change(50)
    return _rolling_skew(base, 21)

def accq_333_skew_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 71 accruals quality distribution over 63d to detect tail risk or exhaustion.
    """
    base = opinc.pct_change(50)
    return _rolling_skew(base, 63)

def accq_334_skew_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 71 accruals quality distribution over 126d to detect tail risk or exhaustion.
    """
    base = opinc.pct_change(50)
    return _rolling_skew(base, 126)

def accq_335_skew_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 71 accruals quality distribution over 252d to detect tail risk or exhaustion.
    """
    base = opinc.pct_change(50)
    return _rolling_skew(base, 252)

def accq_336_kurt_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 71 accruals quality over 5d to capture explosive breakdown or reversal points.
    """
    base = opinc.pct_change(50)
    return _rolling_kurt(base, 5)

def accq_337_kurt_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 71 accruals quality over 21d to capture explosive breakdown or reversal points.
    """
    base = opinc.pct_change(50)
    return _rolling_kurt(base, 21)

def accq_338_kurt_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 71 accruals quality over 63d to capture explosive breakdown or reversal points.
    """
    base = opinc.pct_change(50)
    return _rolling_kurt(base, 63)

def accq_339_kurt_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 71 accruals quality over 126d to capture explosive breakdown or reversal points.
    """
    base = opinc.pct_change(50)
    return _rolling_kurt(base, 126)

def accq_340_kurt_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 71 accruals quality over 252d to capture explosive breakdown or reversal points.
    """
    base = opinc.pct_change(50)
    return _rolling_kurt(base, 252)

def accq_341_voladj_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 71 accruals quality for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = opinc.pct_change(50)
    return _safe_div(base, _rolling_std(base, 5))

def accq_342_voladj_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 71 accruals quality for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = opinc.pct_change(50)
    return _safe_div(base, _rolling_std(base, 21))

def accq_343_voladj_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 71 accruals quality for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = opinc.pct_change(50)
    return _safe_div(base, _rolling_std(base, 63))

def accq_344_voladj_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 71 accruals quality for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = opinc.pct_change(50)
    return _safe_div(base, _rolling_std(base, 126))

def accq_345_voladj_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 71 accruals quality for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = opinc.pct_change(50)
    return _safe_div(base, _rolling_std(base, 252))

def accq_346_lognorm_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 71 accruals quality over 5d to stabilize variance and capture exponential shifts.
    """
    base = opinc.pct_change(50)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def accq_347_lognorm_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 71 accruals quality over 21d to stabilize variance and capture exponential shifts.
    """
    base = opinc.pct_change(50)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def accq_348_lognorm_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 71 accruals quality over 63d to stabilize variance and capture exponential shifts.
    """
    base = opinc.pct_change(50)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def accq_349_lognorm_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 71 accruals quality over 126d to stabilize variance and capture exponential shifts.
    """
    base = opinc.pct_change(50)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def accq_350_lognorm_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 71 accruals quality over 252d to stabilize variance and capture exponential shifts.
    """
    base = opinc.pct_change(50)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def accq_351_lvl_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 71 accruals quality over a 5d horizon to identify extreme regimes.
    """
    base = opinc.pct_change(55)
    return _rolling_mean(base, 5)

def accq_352_lvl_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 71 accruals quality over a 21d horizon to identify extreme regimes.
    """
    base = opinc.pct_change(55)
    return _rolling_mean(base, 21)

def accq_353_lvl_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 71 accruals quality over a 63d horizon to identify extreme regimes.
    """
    base = opinc.pct_change(55)
    return _rolling_mean(base, 63)

def accq_354_lvl_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 71 accruals quality over a 126d horizon to identify extreme regimes.
    """
    base = opinc.pct_change(55)
    return _rolling_mean(base, 126)

def accq_355_lvl_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 71 accruals quality over a 252d horizon to identify extreme regimes.
    """
    base = opinc.pct_change(55)
    return _rolling_mean(base, 252)

def accq_356_zscore_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 71 accruals quality by measuring deviations from the 5d mean.
    """
    base = opinc.pct_change(55)
    return _zscore_rolling(base, 5)

def accq_357_zscore_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 71 accruals quality by measuring deviations from the 21d mean.
    """
    base = opinc.pct_change(55)
    return _zscore_rolling(base, 21)

def accq_358_zscore_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 71 accruals quality by measuring deviations from the 63d mean.
    """
    base = opinc.pct_change(55)
    return _zscore_rolling(base, 63)

def accq_359_zscore_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 71 accruals quality by measuring deviations from the 126d mean.
    """
    base = opinc.pct_change(55)
    return _zscore_rolling(base, 126)

def accq_360_zscore_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 71 accruals quality by measuring deviations from the 252d mean.
    """
    base = opinc.pct_change(55)
    return _zscore_rolling(base, 252)

def accq_361_rank_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 71 accruals quality to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = opinc.pct_change(55)
    return _rank_pct(base, 5)

def accq_362_rank_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 71 accruals quality to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = opinc.pct_change(55)
    return _rank_pct(base, 21)

def accq_363_rank_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 71 accruals quality to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = opinc.pct_change(55)
    return _rank_pct(base, 63)

def accq_364_rank_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 71 accruals quality to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = opinc.pct_change(55)
    return _rank_pct(base, 126)

def accq_365_rank_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 71 accruals quality to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = opinc.pct_change(55)
    return _rank_pct(base, 252)

def accq_366_skew_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 71 accruals quality distribution over 5d to detect tail risk or exhaustion.
    """
    base = opinc.pct_change(55)
    return _rolling_skew(base, 5)

def accq_367_skew_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 71 accruals quality distribution over 21d to detect tail risk or exhaustion.
    """
    base = opinc.pct_change(55)
    return _rolling_skew(base, 21)

def accq_368_skew_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 71 accruals quality distribution over 63d to detect tail risk or exhaustion.
    """
    base = opinc.pct_change(55)
    return _rolling_skew(base, 63)

def accq_369_skew_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 71 accruals quality distribution over 126d to detect tail risk or exhaustion.
    """
    base = opinc.pct_change(55)
    return _rolling_skew(base, 126)

def accq_370_skew_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 71 accruals quality distribution over 252d to detect tail risk or exhaustion.
    """
    base = opinc.pct_change(55)
    return _rolling_skew(base, 252)

def accq_371_kurt_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 71 accruals quality over 5d to capture explosive breakdown or reversal points.
    """
    base = opinc.pct_change(55)
    return _rolling_kurt(base, 5)

def accq_372_kurt_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 71 accruals quality over 21d to capture explosive breakdown or reversal points.
    """
    base = opinc.pct_change(55)
    return _rolling_kurt(base, 21)

def accq_373_kurt_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 71 accruals quality over 63d to capture explosive breakdown or reversal points.
    """
    base = opinc.pct_change(55)
    return _rolling_kurt(base, 63)

def accq_374_kurt_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 71 accruals quality over 126d to capture explosive breakdown or reversal points.
    """
    base = opinc.pct_change(55)
    return _rolling_kurt(base, 126)

def accq_375_kurt_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 71 accruals quality over 252d to capture explosive breakdown or reversal points.
    """
    base = opinc.pct_change(55)
    return _rolling_kurt(base, 252)
