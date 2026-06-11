"""
78_78_marketcap_destruction — Base Features 376-450
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

def mdes_376_voladj_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 78 marketcap destruction for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(55)
    return _safe_div(base, _rolling_std(base, 5))

def mdes_377_voladj_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 78 marketcap destruction for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(55)
    return _safe_div(base, _rolling_std(base, 21))

def mdes_378_voladj_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 78 marketcap destruction for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(55)
    return _safe_div(base, _rolling_std(base, 63))

def mdes_379_voladj_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 78 marketcap destruction for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(55)
    return _safe_div(base, _rolling_std(base, 126))

def mdes_380_voladj_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 78 marketcap destruction for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(55)
    return _safe_div(base, _rolling_std(base, 252))

def mdes_381_lognorm_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 78 marketcap destruction over 5d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(55)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def mdes_382_lognorm_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 78 marketcap destruction over 21d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(55)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def mdes_383_lognorm_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 78 marketcap destruction over 63d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(55)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def mdes_384_lognorm_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 78 marketcap destruction over 126d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(55)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def mdes_385_lognorm_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 78 marketcap destruction over 252d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(55)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def mdes_386_lvl_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 78 marketcap destruction over a 5d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(60)
    return _rolling_mean(base, 5)

def mdes_387_lvl_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 78 marketcap destruction over a 21d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(60)
    return _rolling_mean(base, 21)

def mdes_388_lvl_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 78 marketcap destruction over a 63d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(60)
    return _rolling_mean(base, 63)

def mdes_389_lvl_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 78 marketcap destruction over a 126d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(60)
    return _rolling_mean(base, 126)

def mdes_390_lvl_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 78 marketcap destruction over a 252d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(60)
    return _rolling_mean(base, 252)

def mdes_391_zscore_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 78 marketcap destruction by measuring deviations from the 5d mean.
    """
    base = marketcap.pct_change(60)
    return _zscore_rolling(base, 5)

def mdes_392_zscore_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 78 marketcap destruction by measuring deviations from the 21d mean.
    """
    base = marketcap.pct_change(60)
    return _zscore_rolling(base, 21)

def mdes_393_zscore_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 78 marketcap destruction by measuring deviations from the 63d mean.
    """
    base = marketcap.pct_change(60)
    return _zscore_rolling(base, 63)

def mdes_394_zscore_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 78 marketcap destruction by measuring deviations from the 126d mean.
    """
    base = marketcap.pct_change(60)
    return _zscore_rolling(base, 126)

def mdes_395_zscore_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 78 marketcap destruction by measuring deviations from the 252d mean.
    """
    base = marketcap.pct_change(60)
    return _zscore_rolling(base, 252)

def mdes_396_rank_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 78 marketcap destruction to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(60)
    return _rank_pct(base, 5)

def mdes_397_rank_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 78 marketcap destruction to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(60)
    return _rank_pct(base, 21)

def mdes_398_rank_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 78 marketcap destruction to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(60)
    return _rank_pct(base, 63)

def mdes_399_rank_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 78 marketcap destruction to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(60)
    return _rank_pct(base, 126)

def mdes_400_rank_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 78 marketcap destruction to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(60)
    return _rank_pct(base, 252)

def mdes_401_skew_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 78 marketcap destruction distribution over 5d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(60)
    return _rolling_skew(base, 5)

def mdes_402_skew_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 78 marketcap destruction distribution over 21d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(60)
    return _rolling_skew(base, 21)

def mdes_403_skew_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 78 marketcap destruction distribution over 63d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(60)
    return _rolling_skew(base, 63)

def mdes_404_skew_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 78 marketcap destruction distribution over 126d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(60)
    return _rolling_skew(base, 126)

def mdes_405_skew_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 78 marketcap destruction distribution over 252d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(60)
    return _rolling_skew(base, 252)

def mdes_406_kurt_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 78 marketcap destruction over 5d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(60)
    return _rolling_kurt(base, 5)

def mdes_407_kurt_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 78 marketcap destruction over 21d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(60)
    return _rolling_kurt(base, 21)

def mdes_408_kurt_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 78 marketcap destruction over 63d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(60)
    return _rolling_kurt(base, 63)

def mdes_409_kurt_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 78 marketcap destruction over 126d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(60)
    return _rolling_kurt(base, 126)

def mdes_410_kurt_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 78 marketcap destruction over 252d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(60)
    return _rolling_kurt(base, 252)

def mdes_411_voladj_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 78 marketcap destruction for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(60)
    return _safe_div(base, _rolling_std(base, 5))

def mdes_412_voladj_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 78 marketcap destruction for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(60)
    return _safe_div(base, _rolling_std(base, 21))

def mdes_413_voladj_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 78 marketcap destruction for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(60)
    return _safe_div(base, _rolling_std(base, 63))

def mdes_414_voladj_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 78 marketcap destruction for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(60)
    return _safe_div(base, _rolling_std(base, 126))

def mdes_415_voladj_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 78 marketcap destruction for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(60)
    return _safe_div(base, _rolling_std(base, 252))

def mdes_416_lognorm_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 78 marketcap destruction over 5d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(60)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def mdes_417_lognorm_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 78 marketcap destruction over 21d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(60)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def mdes_418_lognorm_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 78 marketcap destruction over 63d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(60)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def mdes_419_lognorm_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 78 marketcap destruction over 126d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(60)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def mdes_420_lognorm_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 78 marketcap destruction over 252d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(60)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def mdes_421_lvl_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 78 marketcap destruction over a 5d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(65)
    return _rolling_mean(base, 5)

def mdes_422_lvl_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 78 marketcap destruction over a 21d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(65)
    return _rolling_mean(base, 21)

def mdes_423_lvl_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 78 marketcap destruction over a 63d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(65)
    return _rolling_mean(base, 63)

def mdes_424_lvl_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 78 marketcap destruction over a 126d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(65)
    return _rolling_mean(base, 126)

def mdes_425_lvl_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 78 marketcap destruction over a 252d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(65)
    return _rolling_mean(base, 252)

def mdes_426_zscore_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 78 marketcap destruction by measuring deviations from the 5d mean.
    """
    base = marketcap.pct_change(65)
    return _zscore_rolling(base, 5)

def mdes_427_zscore_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 78 marketcap destruction by measuring deviations from the 21d mean.
    """
    base = marketcap.pct_change(65)
    return _zscore_rolling(base, 21)

def mdes_428_zscore_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 78 marketcap destruction by measuring deviations from the 63d mean.
    """
    base = marketcap.pct_change(65)
    return _zscore_rolling(base, 63)

def mdes_429_zscore_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 78 marketcap destruction by measuring deviations from the 126d mean.
    """
    base = marketcap.pct_change(65)
    return _zscore_rolling(base, 126)

def mdes_430_zscore_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 78 marketcap destruction by measuring deviations from the 252d mean.
    """
    base = marketcap.pct_change(65)
    return _zscore_rolling(base, 252)

def mdes_431_rank_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 78 marketcap destruction to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(65)
    return _rank_pct(base, 5)

def mdes_432_rank_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 78 marketcap destruction to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(65)
    return _rank_pct(base, 21)

def mdes_433_rank_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 78 marketcap destruction to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(65)
    return _rank_pct(base, 63)

def mdes_434_rank_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 78 marketcap destruction to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(65)
    return _rank_pct(base, 126)

def mdes_435_rank_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 78 marketcap destruction to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(65)
    return _rank_pct(base, 252)

def mdes_436_skew_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 78 marketcap destruction distribution over 5d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(65)
    return _rolling_skew(base, 5)

def mdes_437_skew_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 78 marketcap destruction distribution over 21d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(65)
    return _rolling_skew(base, 21)

def mdes_438_skew_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 78 marketcap destruction distribution over 63d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(65)
    return _rolling_skew(base, 63)

def mdes_439_skew_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 78 marketcap destruction distribution over 126d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(65)
    return _rolling_skew(base, 126)

def mdes_440_skew_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 78 marketcap destruction distribution over 252d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(65)
    return _rolling_skew(base, 252)

def mdes_441_kurt_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 78 marketcap destruction over 5d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(65)
    return _rolling_kurt(base, 5)

def mdes_442_kurt_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 78 marketcap destruction over 21d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(65)
    return _rolling_kurt(base, 21)

def mdes_443_kurt_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 78 marketcap destruction over 63d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(65)
    return _rolling_kurt(base, 63)

def mdes_444_kurt_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 78 marketcap destruction over 126d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(65)
    return _rolling_kurt(base, 126)

def mdes_445_kurt_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 78 marketcap destruction over 252d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(65)
    return _rolling_kurt(base, 252)

def mdes_446_voladj_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 78 marketcap destruction for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(65)
    return _safe_div(base, _rolling_std(base, 5))

def mdes_447_voladj_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 78 marketcap destruction for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(65)
    return _safe_div(base, _rolling_std(base, 21))

def mdes_448_voladj_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 78 marketcap destruction for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(65)
    return _safe_div(base, _rolling_std(base, 63))

def mdes_449_voladj_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 78 marketcap destruction for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(65)
    return _safe_div(base, _rolling_std(base, 126))

def mdes_450_voladj_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 78 marketcap destruction for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(65)
    return _safe_div(base, _rolling_std(base, 252))
