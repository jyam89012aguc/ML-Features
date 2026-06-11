"""
74_74_fundamental_momentum — Base Features 376-450
Domain: 74_fundamental_momentum
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

def fmom_376_voladj_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 74 fundamental momentum for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(55)
    return _safe_div(base, _rolling_std(base, 5))

def fmom_377_voladj_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 74 fundamental momentum for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(55)
    return _safe_div(base, _rolling_std(base, 21))

def fmom_378_voladj_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 74 fundamental momentum for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(55)
    return _safe_div(base, _rolling_std(base, 63))

def fmom_379_voladj_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 74 fundamental momentum for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(55)
    return _safe_div(base, _rolling_std(base, 126))

def fmom_380_voladj_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 74 fundamental momentum for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(55)
    return _safe_div(base, _rolling_std(base, 252))

def fmom_381_lognorm_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 74 fundamental momentum over 5d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(55)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def fmom_382_lognorm_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 74 fundamental momentum over 21d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(55)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def fmom_383_lognorm_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 74 fundamental momentum over 63d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(55)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def fmom_384_lognorm_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 74 fundamental momentum over 126d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(55)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def fmom_385_lognorm_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 74 fundamental momentum over 252d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(55)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def fmom_386_lvl_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 74 fundamental momentum over a 5d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(60)
    return _rolling_mean(base, 5)

def fmom_387_lvl_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 74 fundamental momentum over a 21d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(60)
    return _rolling_mean(base, 21)

def fmom_388_lvl_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 74 fundamental momentum over a 63d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(60)
    return _rolling_mean(base, 63)

def fmom_389_lvl_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 74 fundamental momentum over a 126d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(60)
    return _rolling_mean(base, 126)

def fmom_390_lvl_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 74 fundamental momentum over a 252d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(60)
    return _rolling_mean(base, 252)

def fmom_391_zscore_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 74 fundamental momentum by measuring deviations from the 5d mean.
    """
    base = marketcap.pct_change(60)
    return _zscore_rolling(base, 5)

def fmom_392_zscore_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 74 fundamental momentum by measuring deviations from the 21d mean.
    """
    base = marketcap.pct_change(60)
    return _zscore_rolling(base, 21)

def fmom_393_zscore_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 74 fundamental momentum by measuring deviations from the 63d mean.
    """
    base = marketcap.pct_change(60)
    return _zscore_rolling(base, 63)

def fmom_394_zscore_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 74 fundamental momentum by measuring deviations from the 126d mean.
    """
    base = marketcap.pct_change(60)
    return _zscore_rolling(base, 126)

def fmom_395_zscore_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 74 fundamental momentum by measuring deviations from the 252d mean.
    """
    base = marketcap.pct_change(60)
    return _zscore_rolling(base, 252)

def fmom_396_rank_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 74 fundamental momentum to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(60)
    return _rank_pct(base, 5)

def fmom_397_rank_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 74 fundamental momentum to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(60)
    return _rank_pct(base, 21)

def fmom_398_rank_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 74 fundamental momentum to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(60)
    return _rank_pct(base, 63)

def fmom_399_rank_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 74 fundamental momentum to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(60)
    return _rank_pct(base, 126)

def fmom_400_rank_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 74 fundamental momentum to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(60)
    return _rank_pct(base, 252)

def fmom_401_skew_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 74 fundamental momentum distribution over 5d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(60)
    return _rolling_skew(base, 5)

def fmom_402_skew_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 74 fundamental momentum distribution over 21d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(60)
    return _rolling_skew(base, 21)

def fmom_403_skew_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 74 fundamental momentum distribution over 63d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(60)
    return _rolling_skew(base, 63)

def fmom_404_skew_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 74 fundamental momentum distribution over 126d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(60)
    return _rolling_skew(base, 126)

def fmom_405_skew_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 74 fundamental momentum distribution over 252d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(60)
    return _rolling_skew(base, 252)

def fmom_406_kurt_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 74 fundamental momentum over 5d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(60)
    return _rolling_kurt(base, 5)

def fmom_407_kurt_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 74 fundamental momentum over 21d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(60)
    return _rolling_kurt(base, 21)

def fmom_408_kurt_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 74 fundamental momentum over 63d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(60)
    return _rolling_kurt(base, 63)

def fmom_409_kurt_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 74 fundamental momentum over 126d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(60)
    return _rolling_kurt(base, 126)

def fmom_410_kurt_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 74 fundamental momentum over 252d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(60)
    return _rolling_kurt(base, 252)

def fmom_411_voladj_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 74 fundamental momentum for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(60)
    return _safe_div(base, _rolling_std(base, 5))

def fmom_412_voladj_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 74 fundamental momentum for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(60)
    return _safe_div(base, _rolling_std(base, 21))

def fmom_413_voladj_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 74 fundamental momentum for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(60)
    return _safe_div(base, _rolling_std(base, 63))

def fmom_414_voladj_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 74 fundamental momentum for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(60)
    return _safe_div(base, _rolling_std(base, 126))

def fmom_415_voladj_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 74 fundamental momentum for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(60)
    return _safe_div(base, _rolling_std(base, 252))

def fmom_416_lognorm_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 74 fundamental momentum over 5d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(60)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def fmom_417_lognorm_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 74 fundamental momentum over 21d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(60)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def fmom_418_lognorm_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 74 fundamental momentum over 63d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(60)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def fmom_419_lognorm_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 74 fundamental momentum over 126d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(60)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def fmom_420_lognorm_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 74 fundamental momentum over 252d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(60)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def fmom_421_lvl_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 74 fundamental momentum over a 5d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(65)
    return _rolling_mean(base, 5)

def fmom_422_lvl_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 74 fundamental momentum over a 21d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(65)
    return _rolling_mean(base, 21)

def fmom_423_lvl_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 74 fundamental momentum over a 63d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(65)
    return _rolling_mean(base, 63)

def fmom_424_lvl_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 74 fundamental momentum over a 126d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(65)
    return _rolling_mean(base, 126)

def fmom_425_lvl_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 74 fundamental momentum over a 252d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(65)
    return _rolling_mean(base, 252)

def fmom_426_zscore_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 74 fundamental momentum by measuring deviations from the 5d mean.
    """
    base = marketcap.pct_change(65)
    return _zscore_rolling(base, 5)

def fmom_427_zscore_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 74 fundamental momentum by measuring deviations from the 21d mean.
    """
    base = marketcap.pct_change(65)
    return _zscore_rolling(base, 21)

def fmom_428_zscore_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 74 fundamental momentum by measuring deviations from the 63d mean.
    """
    base = marketcap.pct_change(65)
    return _zscore_rolling(base, 63)

def fmom_429_zscore_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 74 fundamental momentum by measuring deviations from the 126d mean.
    """
    base = marketcap.pct_change(65)
    return _zscore_rolling(base, 126)

def fmom_430_zscore_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 74 fundamental momentum by measuring deviations from the 252d mean.
    """
    base = marketcap.pct_change(65)
    return _zscore_rolling(base, 252)

def fmom_431_rank_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 74 fundamental momentum to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(65)
    return _rank_pct(base, 5)

def fmom_432_rank_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 74 fundamental momentum to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(65)
    return _rank_pct(base, 21)

def fmom_433_rank_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 74 fundamental momentum to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(65)
    return _rank_pct(base, 63)

def fmom_434_rank_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 74 fundamental momentum to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(65)
    return _rank_pct(base, 126)

def fmom_435_rank_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 74 fundamental momentum to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(65)
    return _rank_pct(base, 252)

def fmom_436_skew_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 74 fundamental momentum distribution over 5d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(65)
    return _rolling_skew(base, 5)

def fmom_437_skew_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 74 fundamental momentum distribution over 21d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(65)
    return _rolling_skew(base, 21)

def fmom_438_skew_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 74 fundamental momentum distribution over 63d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(65)
    return _rolling_skew(base, 63)

def fmom_439_skew_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 74 fundamental momentum distribution over 126d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(65)
    return _rolling_skew(base, 126)

def fmom_440_skew_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 74 fundamental momentum distribution over 252d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(65)
    return _rolling_skew(base, 252)

def fmom_441_kurt_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 74 fundamental momentum over 5d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(65)
    return _rolling_kurt(base, 5)

def fmom_442_kurt_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 74 fundamental momentum over 21d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(65)
    return _rolling_kurt(base, 21)

def fmom_443_kurt_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 74 fundamental momentum over 63d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(65)
    return _rolling_kurt(base, 63)

def fmom_444_kurt_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 74 fundamental momentum over 126d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(65)
    return _rolling_kurt(base, 126)

def fmom_445_kurt_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 74 fundamental momentum over 252d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(65)
    return _rolling_kurt(base, 252)

def fmom_446_voladj_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 74 fundamental momentum for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(65)
    return _safe_div(base, _rolling_std(base, 5))

def fmom_447_voladj_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 74 fundamental momentum for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(65)
    return _safe_div(base, _rolling_std(base, 21))

def fmom_448_voladj_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 74 fundamental momentum for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(65)
    return _safe_div(base, _rolling_std(base, 63))

def fmom_449_voladj_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 74 fundamental momentum for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(65)
    return _safe_div(base, _rolling_std(base, 126))

def fmom_450_voladj_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 74 fundamental momentum for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(65)
    return _safe_div(base, _rolling_std(base, 252))
