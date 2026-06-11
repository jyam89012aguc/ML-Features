"""
61_61_revenue_deterioration — Base Features 301-375
Domain: 61_revenue_deterioration
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

def rdet_301_kurt_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 61 revenue deterioration over 5d to capture explosive breakdown or reversal points.
    """
    base = revenue.pct_change(45)
    return _rolling_kurt(base, 5)

def rdet_302_kurt_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 61 revenue deterioration over 21d to capture explosive breakdown or reversal points.
    """
    base = revenue.pct_change(45)
    return _rolling_kurt(base, 21)

def rdet_303_kurt_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 61 revenue deterioration over 63d to capture explosive breakdown or reversal points.
    """
    base = revenue.pct_change(45)
    return _rolling_kurt(base, 63)

def rdet_304_kurt_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 61 revenue deterioration over 126d to capture explosive breakdown or reversal points.
    """
    base = revenue.pct_change(45)
    return _rolling_kurt(base, 126)

def rdet_305_kurt_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 61 revenue deterioration over 252d to capture explosive breakdown or reversal points.
    """
    base = revenue.pct_change(45)
    return _rolling_kurt(base, 252)

def rdet_306_voladj_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 61 revenue deterioration for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = revenue.pct_change(45)
    return _safe_div(base, _rolling_std(base, 5))

def rdet_307_voladj_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 61 revenue deterioration for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = revenue.pct_change(45)
    return _safe_div(base, _rolling_std(base, 21))

def rdet_308_voladj_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 61 revenue deterioration for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = revenue.pct_change(45)
    return _safe_div(base, _rolling_std(base, 63))

def rdet_309_voladj_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 61 revenue deterioration for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = revenue.pct_change(45)
    return _safe_div(base, _rolling_std(base, 126))

def rdet_310_voladj_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 61 revenue deterioration for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = revenue.pct_change(45)
    return _safe_div(base, _rolling_std(base, 252))

def rdet_311_lognorm_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 61 revenue deterioration over 5d to stabilize variance and capture exponential shifts.
    """
    base = revenue.pct_change(45)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def rdet_312_lognorm_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 61 revenue deterioration over 21d to stabilize variance and capture exponential shifts.
    """
    base = revenue.pct_change(45)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def rdet_313_lognorm_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 61 revenue deterioration over 63d to stabilize variance and capture exponential shifts.
    """
    base = revenue.pct_change(45)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def rdet_314_lognorm_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 61 revenue deterioration over 126d to stabilize variance and capture exponential shifts.
    """
    base = revenue.pct_change(45)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def rdet_315_lognorm_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 61 revenue deterioration over 252d to stabilize variance and capture exponential shifts.
    """
    base = revenue.pct_change(45)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def rdet_316_lvl_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 61 revenue deterioration over a 5d horizon to identify extreme regimes.
    """
    base = revenue.pct_change(50)
    return _rolling_mean(base, 5)

def rdet_317_lvl_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 61 revenue deterioration over a 21d horizon to identify extreme regimes.
    """
    base = revenue.pct_change(50)
    return _rolling_mean(base, 21)

def rdet_318_lvl_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 61 revenue deterioration over a 63d horizon to identify extreme regimes.
    """
    base = revenue.pct_change(50)
    return _rolling_mean(base, 63)

def rdet_319_lvl_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 61 revenue deterioration over a 126d horizon to identify extreme regimes.
    """
    base = revenue.pct_change(50)
    return _rolling_mean(base, 126)

def rdet_320_lvl_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 61 revenue deterioration over a 252d horizon to identify extreme regimes.
    """
    base = revenue.pct_change(50)
    return _rolling_mean(base, 252)

def rdet_321_zscore_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 61 revenue deterioration by measuring deviations from the 5d mean.
    """
    base = revenue.pct_change(50)
    return _zscore_rolling(base, 5)

def rdet_322_zscore_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 61 revenue deterioration by measuring deviations from the 21d mean.
    """
    base = revenue.pct_change(50)
    return _zscore_rolling(base, 21)

def rdet_323_zscore_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 61 revenue deterioration by measuring deviations from the 63d mean.
    """
    base = revenue.pct_change(50)
    return _zscore_rolling(base, 63)

def rdet_324_zscore_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 61 revenue deterioration by measuring deviations from the 126d mean.
    """
    base = revenue.pct_change(50)
    return _zscore_rolling(base, 126)

def rdet_325_zscore_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 61 revenue deterioration by measuring deviations from the 252d mean.
    """
    base = revenue.pct_change(50)
    return _zscore_rolling(base, 252)

def rdet_326_rank_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 61 revenue deterioration to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = revenue.pct_change(50)
    return _rank_pct(base, 5)

def rdet_327_rank_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 61 revenue deterioration to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = revenue.pct_change(50)
    return _rank_pct(base, 21)

def rdet_328_rank_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 61 revenue deterioration to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = revenue.pct_change(50)
    return _rank_pct(base, 63)

def rdet_329_rank_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 61 revenue deterioration to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = revenue.pct_change(50)
    return _rank_pct(base, 126)

def rdet_330_rank_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 61 revenue deterioration to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = revenue.pct_change(50)
    return _rank_pct(base, 252)

def rdet_331_skew_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 61 revenue deterioration distribution over 5d to detect tail risk or exhaustion.
    """
    base = revenue.pct_change(50)
    return _rolling_skew(base, 5)

def rdet_332_skew_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 61 revenue deterioration distribution over 21d to detect tail risk or exhaustion.
    """
    base = revenue.pct_change(50)
    return _rolling_skew(base, 21)

def rdet_333_skew_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 61 revenue deterioration distribution over 63d to detect tail risk or exhaustion.
    """
    base = revenue.pct_change(50)
    return _rolling_skew(base, 63)

def rdet_334_skew_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 61 revenue deterioration distribution over 126d to detect tail risk or exhaustion.
    """
    base = revenue.pct_change(50)
    return _rolling_skew(base, 126)

def rdet_335_skew_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 61 revenue deterioration distribution over 252d to detect tail risk or exhaustion.
    """
    base = revenue.pct_change(50)
    return _rolling_skew(base, 252)

def rdet_336_kurt_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 61 revenue deterioration over 5d to capture explosive breakdown or reversal points.
    """
    base = revenue.pct_change(50)
    return _rolling_kurt(base, 5)

def rdet_337_kurt_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 61 revenue deterioration over 21d to capture explosive breakdown or reversal points.
    """
    base = revenue.pct_change(50)
    return _rolling_kurt(base, 21)

def rdet_338_kurt_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 61 revenue deterioration over 63d to capture explosive breakdown or reversal points.
    """
    base = revenue.pct_change(50)
    return _rolling_kurt(base, 63)

def rdet_339_kurt_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 61 revenue deterioration over 126d to capture explosive breakdown or reversal points.
    """
    base = revenue.pct_change(50)
    return _rolling_kurt(base, 126)

def rdet_340_kurt_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 61 revenue deterioration over 252d to capture explosive breakdown or reversal points.
    """
    base = revenue.pct_change(50)
    return _rolling_kurt(base, 252)

def rdet_341_voladj_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 61 revenue deterioration for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = revenue.pct_change(50)
    return _safe_div(base, _rolling_std(base, 5))

def rdet_342_voladj_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 61 revenue deterioration for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = revenue.pct_change(50)
    return _safe_div(base, _rolling_std(base, 21))

def rdet_343_voladj_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 61 revenue deterioration for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = revenue.pct_change(50)
    return _safe_div(base, _rolling_std(base, 63))

def rdet_344_voladj_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 61 revenue deterioration for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = revenue.pct_change(50)
    return _safe_div(base, _rolling_std(base, 126))

def rdet_345_voladj_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 61 revenue deterioration for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = revenue.pct_change(50)
    return _safe_div(base, _rolling_std(base, 252))

def rdet_346_lognorm_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 61 revenue deterioration over 5d to stabilize variance and capture exponential shifts.
    """
    base = revenue.pct_change(50)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def rdet_347_lognorm_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 61 revenue deterioration over 21d to stabilize variance and capture exponential shifts.
    """
    base = revenue.pct_change(50)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def rdet_348_lognorm_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 61 revenue deterioration over 63d to stabilize variance and capture exponential shifts.
    """
    base = revenue.pct_change(50)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def rdet_349_lognorm_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 61 revenue deterioration over 126d to stabilize variance and capture exponential shifts.
    """
    base = revenue.pct_change(50)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def rdet_350_lognorm_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 61 revenue deterioration over 252d to stabilize variance and capture exponential shifts.
    """
    base = revenue.pct_change(50)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def rdet_351_lvl_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 61 revenue deterioration over a 5d horizon to identify extreme regimes.
    """
    base = revenue.pct_change(55)
    return _rolling_mean(base, 5)

def rdet_352_lvl_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 61 revenue deterioration over a 21d horizon to identify extreme regimes.
    """
    base = revenue.pct_change(55)
    return _rolling_mean(base, 21)

def rdet_353_lvl_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 61 revenue deterioration over a 63d horizon to identify extreme regimes.
    """
    base = revenue.pct_change(55)
    return _rolling_mean(base, 63)

def rdet_354_lvl_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 61 revenue deterioration over a 126d horizon to identify extreme regimes.
    """
    base = revenue.pct_change(55)
    return _rolling_mean(base, 126)

def rdet_355_lvl_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 61 revenue deterioration over a 252d horizon to identify extreme regimes.
    """
    base = revenue.pct_change(55)
    return _rolling_mean(base, 252)

def rdet_356_zscore_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 61 revenue deterioration by measuring deviations from the 5d mean.
    """
    base = revenue.pct_change(55)
    return _zscore_rolling(base, 5)

def rdet_357_zscore_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 61 revenue deterioration by measuring deviations from the 21d mean.
    """
    base = revenue.pct_change(55)
    return _zscore_rolling(base, 21)

def rdet_358_zscore_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 61 revenue deterioration by measuring deviations from the 63d mean.
    """
    base = revenue.pct_change(55)
    return _zscore_rolling(base, 63)

def rdet_359_zscore_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 61 revenue deterioration by measuring deviations from the 126d mean.
    """
    base = revenue.pct_change(55)
    return _zscore_rolling(base, 126)

def rdet_360_zscore_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 61 revenue deterioration by measuring deviations from the 252d mean.
    """
    base = revenue.pct_change(55)
    return _zscore_rolling(base, 252)

def rdet_361_rank_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 61 revenue deterioration to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = revenue.pct_change(55)
    return _rank_pct(base, 5)

def rdet_362_rank_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 61 revenue deterioration to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = revenue.pct_change(55)
    return _rank_pct(base, 21)

def rdet_363_rank_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 61 revenue deterioration to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = revenue.pct_change(55)
    return _rank_pct(base, 63)

def rdet_364_rank_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 61 revenue deterioration to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = revenue.pct_change(55)
    return _rank_pct(base, 126)

def rdet_365_rank_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 61 revenue deterioration to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = revenue.pct_change(55)
    return _rank_pct(base, 252)

def rdet_366_skew_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 61 revenue deterioration distribution over 5d to detect tail risk or exhaustion.
    """
    base = revenue.pct_change(55)
    return _rolling_skew(base, 5)

def rdet_367_skew_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 61 revenue deterioration distribution over 21d to detect tail risk or exhaustion.
    """
    base = revenue.pct_change(55)
    return _rolling_skew(base, 21)

def rdet_368_skew_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 61 revenue deterioration distribution over 63d to detect tail risk or exhaustion.
    """
    base = revenue.pct_change(55)
    return _rolling_skew(base, 63)

def rdet_369_skew_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 61 revenue deterioration distribution over 126d to detect tail risk or exhaustion.
    """
    base = revenue.pct_change(55)
    return _rolling_skew(base, 126)

def rdet_370_skew_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 61 revenue deterioration distribution over 252d to detect tail risk or exhaustion.
    """
    base = revenue.pct_change(55)
    return _rolling_skew(base, 252)

def rdet_371_kurt_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 61 revenue deterioration over 5d to capture explosive breakdown or reversal points.
    """
    base = revenue.pct_change(55)
    return _rolling_kurt(base, 5)

def rdet_372_kurt_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 61 revenue deterioration over 21d to capture explosive breakdown or reversal points.
    """
    base = revenue.pct_change(55)
    return _rolling_kurt(base, 21)

def rdet_373_kurt_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 61 revenue deterioration over 63d to capture explosive breakdown or reversal points.
    """
    base = revenue.pct_change(55)
    return _rolling_kurt(base, 63)

def rdet_374_kurt_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 61 revenue deterioration over 126d to capture explosive breakdown or reversal points.
    """
    base = revenue.pct_change(55)
    return _rolling_kurt(base, 126)

def rdet_375_kurt_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 61 revenue deterioration over 252d to capture explosive breakdown or reversal points.
    """
    base = revenue.pct_change(55)
    return _rolling_kurt(base, 252)
