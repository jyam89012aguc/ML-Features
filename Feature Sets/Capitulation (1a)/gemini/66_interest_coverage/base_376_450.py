"""
66_66_interest_coverage — Base Features 376-450
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

def icov_376_voladj_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 66 interest coverage for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = opinc.pct_change(55)
    return _safe_div(base, _rolling_std(base, 5))

def icov_377_voladj_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 66 interest coverage for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = opinc.pct_change(55)
    return _safe_div(base, _rolling_std(base, 21))

def icov_378_voladj_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 66 interest coverage for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = opinc.pct_change(55)
    return _safe_div(base, _rolling_std(base, 63))

def icov_379_voladj_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 66 interest coverage for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = opinc.pct_change(55)
    return _safe_div(base, _rolling_std(base, 126))

def icov_380_voladj_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 66 interest coverage for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = opinc.pct_change(55)
    return _safe_div(base, _rolling_std(base, 252))

def icov_381_lognorm_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 66 interest coverage over 5d to stabilize variance and capture exponential shifts.
    """
    base = opinc.pct_change(55)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def icov_382_lognorm_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 66 interest coverage over 21d to stabilize variance and capture exponential shifts.
    """
    base = opinc.pct_change(55)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def icov_383_lognorm_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 66 interest coverage over 63d to stabilize variance and capture exponential shifts.
    """
    base = opinc.pct_change(55)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def icov_384_lognorm_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 66 interest coverage over 126d to stabilize variance and capture exponential shifts.
    """
    base = opinc.pct_change(55)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def icov_385_lognorm_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 66 interest coverage over 252d to stabilize variance and capture exponential shifts.
    """
    base = opinc.pct_change(55)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def icov_386_lvl_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 66 interest coverage over a 5d horizon to identify extreme regimes.
    """
    base = opinc.pct_change(60)
    return _rolling_mean(base, 5)

def icov_387_lvl_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 66 interest coverage over a 21d horizon to identify extreme regimes.
    """
    base = opinc.pct_change(60)
    return _rolling_mean(base, 21)

def icov_388_lvl_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 66 interest coverage over a 63d horizon to identify extreme regimes.
    """
    base = opinc.pct_change(60)
    return _rolling_mean(base, 63)

def icov_389_lvl_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 66 interest coverage over a 126d horizon to identify extreme regimes.
    """
    base = opinc.pct_change(60)
    return _rolling_mean(base, 126)

def icov_390_lvl_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 66 interest coverage over a 252d horizon to identify extreme regimes.
    """
    base = opinc.pct_change(60)
    return _rolling_mean(base, 252)

def icov_391_zscore_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 66 interest coverage by measuring deviations from the 5d mean.
    """
    base = opinc.pct_change(60)
    return _zscore_rolling(base, 5)

def icov_392_zscore_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 66 interest coverage by measuring deviations from the 21d mean.
    """
    base = opinc.pct_change(60)
    return _zscore_rolling(base, 21)

def icov_393_zscore_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 66 interest coverage by measuring deviations from the 63d mean.
    """
    base = opinc.pct_change(60)
    return _zscore_rolling(base, 63)

def icov_394_zscore_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 66 interest coverage by measuring deviations from the 126d mean.
    """
    base = opinc.pct_change(60)
    return _zscore_rolling(base, 126)

def icov_395_zscore_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 66 interest coverage by measuring deviations from the 252d mean.
    """
    base = opinc.pct_change(60)
    return _zscore_rolling(base, 252)

def icov_396_rank_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 66 interest coverage to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = opinc.pct_change(60)
    return _rank_pct(base, 5)

def icov_397_rank_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 66 interest coverage to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = opinc.pct_change(60)
    return _rank_pct(base, 21)

def icov_398_rank_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 66 interest coverage to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = opinc.pct_change(60)
    return _rank_pct(base, 63)

def icov_399_rank_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 66 interest coverage to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = opinc.pct_change(60)
    return _rank_pct(base, 126)

def icov_400_rank_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 66 interest coverage to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = opinc.pct_change(60)
    return _rank_pct(base, 252)

def icov_401_skew_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 66 interest coverage distribution over 5d to detect tail risk or exhaustion.
    """
    base = opinc.pct_change(60)
    return _rolling_skew(base, 5)

def icov_402_skew_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 66 interest coverage distribution over 21d to detect tail risk or exhaustion.
    """
    base = opinc.pct_change(60)
    return _rolling_skew(base, 21)

def icov_403_skew_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 66 interest coverage distribution over 63d to detect tail risk or exhaustion.
    """
    base = opinc.pct_change(60)
    return _rolling_skew(base, 63)

def icov_404_skew_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 66 interest coverage distribution over 126d to detect tail risk or exhaustion.
    """
    base = opinc.pct_change(60)
    return _rolling_skew(base, 126)

def icov_405_skew_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 66 interest coverage distribution over 252d to detect tail risk or exhaustion.
    """
    base = opinc.pct_change(60)
    return _rolling_skew(base, 252)

def icov_406_kurt_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 66 interest coverage over 5d to capture explosive breakdown or reversal points.
    """
    base = opinc.pct_change(60)
    return _rolling_kurt(base, 5)

def icov_407_kurt_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 66 interest coverage over 21d to capture explosive breakdown or reversal points.
    """
    base = opinc.pct_change(60)
    return _rolling_kurt(base, 21)

def icov_408_kurt_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 66 interest coverage over 63d to capture explosive breakdown or reversal points.
    """
    base = opinc.pct_change(60)
    return _rolling_kurt(base, 63)

def icov_409_kurt_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 66 interest coverage over 126d to capture explosive breakdown or reversal points.
    """
    base = opinc.pct_change(60)
    return _rolling_kurt(base, 126)

def icov_410_kurt_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 66 interest coverage over 252d to capture explosive breakdown or reversal points.
    """
    base = opinc.pct_change(60)
    return _rolling_kurt(base, 252)

def icov_411_voladj_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 66 interest coverage for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = opinc.pct_change(60)
    return _safe_div(base, _rolling_std(base, 5))

def icov_412_voladj_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 66 interest coverage for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = opinc.pct_change(60)
    return _safe_div(base, _rolling_std(base, 21))

def icov_413_voladj_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 66 interest coverage for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = opinc.pct_change(60)
    return _safe_div(base, _rolling_std(base, 63))

def icov_414_voladj_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 66 interest coverage for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = opinc.pct_change(60)
    return _safe_div(base, _rolling_std(base, 126))

def icov_415_voladj_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 66 interest coverage for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = opinc.pct_change(60)
    return _safe_div(base, _rolling_std(base, 252))

def icov_416_lognorm_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 66 interest coverage over 5d to stabilize variance and capture exponential shifts.
    """
    base = opinc.pct_change(60)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def icov_417_lognorm_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 66 interest coverage over 21d to stabilize variance and capture exponential shifts.
    """
    base = opinc.pct_change(60)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def icov_418_lognorm_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 66 interest coverage over 63d to stabilize variance and capture exponential shifts.
    """
    base = opinc.pct_change(60)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def icov_419_lognorm_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 66 interest coverage over 126d to stabilize variance and capture exponential shifts.
    """
    base = opinc.pct_change(60)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def icov_420_lognorm_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 66 interest coverage over 252d to stabilize variance and capture exponential shifts.
    """
    base = opinc.pct_change(60)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def icov_421_lvl_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 66 interest coverage over a 5d horizon to identify extreme regimes.
    """
    base = opinc.pct_change(65)
    return _rolling_mean(base, 5)

def icov_422_lvl_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 66 interest coverage over a 21d horizon to identify extreme regimes.
    """
    base = opinc.pct_change(65)
    return _rolling_mean(base, 21)

def icov_423_lvl_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 66 interest coverage over a 63d horizon to identify extreme regimes.
    """
    base = opinc.pct_change(65)
    return _rolling_mean(base, 63)

def icov_424_lvl_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 66 interest coverage over a 126d horizon to identify extreme regimes.
    """
    base = opinc.pct_change(65)
    return _rolling_mean(base, 126)

def icov_425_lvl_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 66 interest coverage over a 252d horizon to identify extreme regimes.
    """
    base = opinc.pct_change(65)
    return _rolling_mean(base, 252)

def icov_426_zscore_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 66 interest coverage by measuring deviations from the 5d mean.
    """
    base = opinc.pct_change(65)
    return _zscore_rolling(base, 5)

def icov_427_zscore_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 66 interest coverage by measuring deviations from the 21d mean.
    """
    base = opinc.pct_change(65)
    return _zscore_rolling(base, 21)

def icov_428_zscore_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 66 interest coverage by measuring deviations from the 63d mean.
    """
    base = opinc.pct_change(65)
    return _zscore_rolling(base, 63)

def icov_429_zscore_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 66 interest coverage by measuring deviations from the 126d mean.
    """
    base = opinc.pct_change(65)
    return _zscore_rolling(base, 126)

def icov_430_zscore_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 66 interest coverage by measuring deviations from the 252d mean.
    """
    base = opinc.pct_change(65)
    return _zscore_rolling(base, 252)

def icov_431_rank_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 66 interest coverage to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = opinc.pct_change(65)
    return _rank_pct(base, 5)

def icov_432_rank_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 66 interest coverage to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = opinc.pct_change(65)
    return _rank_pct(base, 21)

def icov_433_rank_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 66 interest coverage to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = opinc.pct_change(65)
    return _rank_pct(base, 63)

def icov_434_rank_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 66 interest coverage to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = opinc.pct_change(65)
    return _rank_pct(base, 126)

def icov_435_rank_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 66 interest coverage to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = opinc.pct_change(65)
    return _rank_pct(base, 252)

def icov_436_skew_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 66 interest coverage distribution over 5d to detect tail risk or exhaustion.
    """
    base = opinc.pct_change(65)
    return _rolling_skew(base, 5)

def icov_437_skew_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 66 interest coverage distribution over 21d to detect tail risk or exhaustion.
    """
    base = opinc.pct_change(65)
    return _rolling_skew(base, 21)

def icov_438_skew_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 66 interest coverage distribution over 63d to detect tail risk or exhaustion.
    """
    base = opinc.pct_change(65)
    return _rolling_skew(base, 63)

def icov_439_skew_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 66 interest coverage distribution over 126d to detect tail risk or exhaustion.
    """
    base = opinc.pct_change(65)
    return _rolling_skew(base, 126)

def icov_440_skew_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 66 interest coverage distribution over 252d to detect tail risk or exhaustion.
    """
    base = opinc.pct_change(65)
    return _rolling_skew(base, 252)

def icov_441_kurt_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 66 interest coverage over 5d to capture explosive breakdown or reversal points.
    """
    base = opinc.pct_change(65)
    return _rolling_kurt(base, 5)

def icov_442_kurt_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 66 interest coverage over 21d to capture explosive breakdown or reversal points.
    """
    base = opinc.pct_change(65)
    return _rolling_kurt(base, 21)

def icov_443_kurt_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 66 interest coverage over 63d to capture explosive breakdown or reversal points.
    """
    base = opinc.pct_change(65)
    return _rolling_kurt(base, 63)

def icov_444_kurt_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 66 interest coverage over 126d to capture explosive breakdown or reversal points.
    """
    base = opinc.pct_change(65)
    return _rolling_kurt(base, 126)

def icov_445_kurt_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 66 interest coverage over 252d to capture explosive breakdown or reversal points.
    """
    base = opinc.pct_change(65)
    return _rolling_kurt(base, 252)

def icov_446_voladj_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 66 interest coverage for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = opinc.pct_change(65)
    return _safe_div(base, _rolling_std(base, 5))

def icov_447_voladj_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 66 interest coverage for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = opinc.pct_change(65)
    return _safe_div(base, _rolling_std(base, 21))

def icov_448_voladj_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 66 interest coverage for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = opinc.pct_change(65)
    return _safe_div(base, _rolling_std(base, 63))

def icov_449_voladj_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 66 interest coverage for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = opinc.pct_change(65)
    return _safe_div(base, _rolling_std(base, 126))

def icov_450_voladj_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 66 interest coverage for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = opinc.pct_change(65)
    return _safe_div(base, _rolling_std(base, 252))
