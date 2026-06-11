"""
64_64_liquidity_distress — Base Features 376-450
Domain: 64_liquidity_distress
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

def ldis_376_voladj_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 64 liquidity distress for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = revenue.pct_change(55)
    return _safe_div(base, _rolling_std(base, 5))

def ldis_377_voladj_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 64 liquidity distress for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = revenue.pct_change(55)
    return _safe_div(base, _rolling_std(base, 21))

def ldis_378_voladj_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 64 liquidity distress for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = revenue.pct_change(55)
    return _safe_div(base, _rolling_std(base, 63))

def ldis_379_voladj_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 64 liquidity distress for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = revenue.pct_change(55)
    return _safe_div(base, _rolling_std(base, 126))

def ldis_380_voladj_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 64 liquidity distress for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = revenue.pct_change(55)
    return _safe_div(base, _rolling_std(base, 252))

def ldis_381_lognorm_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 64 liquidity distress over 5d to stabilize variance and capture exponential shifts.
    """
    base = revenue.pct_change(55)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def ldis_382_lognorm_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 64 liquidity distress over 21d to stabilize variance and capture exponential shifts.
    """
    base = revenue.pct_change(55)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def ldis_383_lognorm_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 64 liquidity distress over 63d to stabilize variance and capture exponential shifts.
    """
    base = revenue.pct_change(55)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def ldis_384_lognorm_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 64 liquidity distress over 126d to stabilize variance and capture exponential shifts.
    """
    base = revenue.pct_change(55)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def ldis_385_lognorm_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 64 liquidity distress over 252d to stabilize variance and capture exponential shifts.
    """
    base = revenue.pct_change(55)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def ldis_386_lvl_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 64 liquidity distress over a 5d horizon to identify extreme regimes.
    """
    base = revenue.pct_change(60)
    return _rolling_mean(base, 5)

def ldis_387_lvl_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 64 liquidity distress over a 21d horizon to identify extreme regimes.
    """
    base = revenue.pct_change(60)
    return _rolling_mean(base, 21)

def ldis_388_lvl_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 64 liquidity distress over a 63d horizon to identify extreme regimes.
    """
    base = revenue.pct_change(60)
    return _rolling_mean(base, 63)

def ldis_389_lvl_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 64 liquidity distress over a 126d horizon to identify extreme regimes.
    """
    base = revenue.pct_change(60)
    return _rolling_mean(base, 126)

def ldis_390_lvl_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 64 liquidity distress over a 252d horizon to identify extreme regimes.
    """
    base = revenue.pct_change(60)
    return _rolling_mean(base, 252)

def ldis_391_zscore_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 64 liquidity distress by measuring deviations from the 5d mean.
    """
    base = revenue.pct_change(60)
    return _zscore_rolling(base, 5)

def ldis_392_zscore_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 64 liquidity distress by measuring deviations from the 21d mean.
    """
    base = revenue.pct_change(60)
    return _zscore_rolling(base, 21)

def ldis_393_zscore_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 64 liquidity distress by measuring deviations from the 63d mean.
    """
    base = revenue.pct_change(60)
    return _zscore_rolling(base, 63)

def ldis_394_zscore_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 64 liquidity distress by measuring deviations from the 126d mean.
    """
    base = revenue.pct_change(60)
    return _zscore_rolling(base, 126)

def ldis_395_zscore_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 64 liquidity distress by measuring deviations from the 252d mean.
    """
    base = revenue.pct_change(60)
    return _zscore_rolling(base, 252)

def ldis_396_rank_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 64 liquidity distress to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = revenue.pct_change(60)
    return _rank_pct(base, 5)

def ldis_397_rank_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 64 liquidity distress to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = revenue.pct_change(60)
    return _rank_pct(base, 21)

def ldis_398_rank_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 64 liquidity distress to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = revenue.pct_change(60)
    return _rank_pct(base, 63)

def ldis_399_rank_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 64 liquidity distress to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = revenue.pct_change(60)
    return _rank_pct(base, 126)

def ldis_400_rank_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 64 liquidity distress to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = revenue.pct_change(60)
    return _rank_pct(base, 252)

def ldis_401_skew_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 64 liquidity distress distribution over 5d to detect tail risk or exhaustion.
    """
    base = revenue.pct_change(60)
    return _rolling_skew(base, 5)

def ldis_402_skew_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 64 liquidity distress distribution over 21d to detect tail risk or exhaustion.
    """
    base = revenue.pct_change(60)
    return _rolling_skew(base, 21)

def ldis_403_skew_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 64 liquidity distress distribution over 63d to detect tail risk or exhaustion.
    """
    base = revenue.pct_change(60)
    return _rolling_skew(base, 63)

def ldis_404_skew_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 64 liquidity distress distribution over 126d to detect tail risk or exhaustion.
    """
    base = revenue.pct_change(60)
    return _rolling_skew(base, 126)

def ldis_405_skew_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 64 liquidity distress distribution over 252d to detect tail risk or exhaustion.
    """
    base = revenue.pct_change(60)
    return _rolling_skew(base, 252)

def ldis_406_kurt_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 64 liquidity distress over 5d to capture explosive breakdown or reversal points.
    """
    base = revenue.pct_change(60)
    return _rolling_kurt(base, 5)

def ldis_407_kurt_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 64 liquidity distress over 21d to capture explosive breakdown or reversal points.
    """
    base = revenue.pct_change(60)
    return _rolling_kurt(base, 21)

def ldis_408_kurt_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 64 liquidity distress over 63d to capture explosive breakdown or reversal points.
    """
    base = revenue.pct_change(60)
    return _rolling_kurt(base, 63)

def ldis_409_kurt_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 64 liquidity distress over 126d to capture explosive breakdown or reversal points.
    """
    base = revenue.pct_change(60)
    return _rolling_kurt(base, 126)

def ldis_410_kurt_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 64 liquidity distress over 252d to capture explosive breakdown or reversal points.
    """
    base = revenue.pct_change(60)
    return _rolling_kurt(base, 252)

def ldis_411_voladj_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 64 liquidity distress for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = revenue.pct_change(60)
    return _safe_div(base, _rolling_std(base, 5))

def ldis_412_voladj_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 64 liquidity distress for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = revenue.pct_change(60)
    return _safe_div(base, _rolling_std(base, 21))

def ldis_413_voladj_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 64 liquidity distress for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = revenue.pct_change(60)
    return _safe_div(base, _rolling_std(base, 63))

def ldis_414_voladj_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 64 liquidity distress for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = revenue.pct_change(60)
    return _safe_div(base, _rolling_std(base, 126))

def ldis_415_voladj_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 64 liquidity distress for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = revenue.pct_change(60)
    return _safe_div(base, _rolling_std(base, 252))

def ldis_416_lognorm_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 64 liquidity distress over 5d to stabilize variance and capture exponential shifts.
    """
    base = revenue.pct_change(60)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def ldis_417_lognorm_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 64 liquidity distress over 21d to stabilize variance and capture exponential shifts.
    """
    base = revenue.pct_change(60)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def ldis_418_lognorm_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 64 liquidity distress over 63d to stabilize variance and capture exponential shifts.
    """
    base = revenue.pct_change(60)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def ldis_419_lognorm_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 64 liquidity distress over 126d to stabilize variance and capture exponential shifts.
    """
    base = revenue.pct_change(60)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def ldis_420_lognorm_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 64 liquidity distress over 252d to stabilize variance and capture exponential shifts.
    """
    base = revenue.pct_change(60)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def ldis_421_lvl_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 64 liquidity distress over a 5d horizon to identify extreme regimes.
    """
    base = revenue.pct_change(65)
    return _rolling_mean(base, 5)

def ldis_422_lvl_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 64 liquidity distress over a 21d horizon to identify extreme regimes.
    """
    base = revenue.pct_change(65)
    return _rolling_mean(base, 21)

def ldis_423_lvl_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 64 liquidity distress over a 63d horizon to identify extreme regimes.
    """
    base = revenue.pct_change(65)
    return _rolling_mean(base, 63)

def ldis_424_lvl_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 64 liquidity distress over a 126d horizon to identify extreme regimes.
    """
    base = revenue.pct_change(65)
    return _rolling_mean(base, 126)

def ldis_425_lvl_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 64 liquidity distress over a 252d horizon to identify extreme regimes.
    """
    base = revenue.pct_change(65)
    return _rolling_mean(base, 252)

def ldis_426_zscore_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 64 liquidity distress by measuring deviations from the 5d mean.
    """
    base = revenue.pct_change(65)
    return _zscore_rolling(base, 5)

def ldis_427_zscore_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 64 liquidity distress by measuring deviations from the 21d mean.
    """
    base = revenue.pct_change(65)
    return _zscore_rolling(base, 21)

def ldis_428_zscore_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 64 liquidity distress by measuring deviations from the 63d mean.
    """
    base = revenue.pct_change(65)
    return _zscore_rolling(base, 63)

def ldis_429_zscore_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 64 liquidity distress by measuring deviations from the 126d mean.
    """
    base = revenue.pct_change(65)
    return _zscore_rolling(base, 126)

def ldis_430_zscore_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 64 liquidity distress by measuring deviations from the 252d mean.
    """
    base = revenue.pct_change(65)
    return _zscore_rolling(base, 252)

def ldis_431_rank_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 64 liquidity distress to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = revenue.pct_change(65)
    return _rank_pct(base, 5)

def ldis_432_rank_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 64 liquidity distress to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = revenue.pct_change(65)
    return _rank_pct(base, 21)

def ldis_433_rank_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 64 liquidity distress to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = revenue.pct_change(65)
    return _rank_pct(base, 63)

def ldis_434_rank_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 64 liquidity distress to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = revenue.pct_change(65)
    return _rank_pct(base, 126)

def ldis_435_rank_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 64 liquidity distress to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = revenue.pct_change(65)
    return _rank_pct(base, 252)

def ldis_436_skew_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 64 liquidity distress distribution over 5d to detect tail risk or exhaustion.
    """
    base = revenue.pct_change(65)
    return _rolling_skew(base, 5)

def ldis_437_skew_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 64 liquidity distress distribution over 21d to detect tail risk or exhaustion.
    """
    base = revenue.pct_change(65)
    return _rolling_skew(base, 21)

def ldis_438_skew_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 64 liquidity distress distribution over 63d to detect tail risk or exhaustion.
    """
    base = revenue.pct_change(65)
    return _rolling_skew(base, 63)

def ldis_439_skew_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 64 liquidity distress distribution over 126d to detect tail risk or exhaustion.
    """
    base = revenue.pct_change(65)
    return _rolling_skew(base, 126)

def ldis_440_skew_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 64 liquidity distress distribution over 252d to detect tail risk or exhaustion.
    """
    base = revenue.pct_change(65)
    return _rolling_skew(base, 252)

def ldis_441_kurt_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 64 liquidity distress over 5d to capture explosive breakdown or reversal points.
    """
    base = revenue.pct_change(65)
    return _rolling_kurt(base, 5)

def ldis_442_kurt_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 64 liquidity distress over 21d to capture explosive breakdown or reversal points.
    """
    base = revenue.pct_change(65)
    return _rolling_kurt(base, 21)

def ldis_443_kurt_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 64 liquidity distress over 63d to capture explosive breakdown or reversal points.
    """
    base = revenue.pct_change(65)
    return _rolling_kurt(base, 63)

def ldis_444_kurt_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 64 liquidity distress over 126d to capture explosive breakdown or reversal points.
    """
    base = revenue.pct_change(65)
    return _rolling_kurt(base, 126)

def ldis_445_kurt_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 64 liquidity distress over 252d to capture explosive breakdown or reversal points.
    """
    base = revenue.pct_change(65)
    return _rolling_kurt(base, 252)

def ldis_446_voladj_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 64 liquidity distress for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = revenue.pct_change(65)
    return _safe_div(base, _rolling_std(base, 5))

def ldis_447_voladj_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 64 liquidity distress for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = revenue.pct_change(65)
    return _safe_div(base, _rolling_std(base, 21))

def ldis_448_voladj_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 64 liquidity distress for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = revenue.pct_change(65)
    return _safe_div(base, _rolling_std(base, 63))

def ldis_449_voladj_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 64 liquidity distress for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = revenue.pct_change(65)
    return _safe_div(base, _rolling_std(base, 126))

def ldis_450_voladj_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 64 liquidity distress for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = revenue.pct_change(65)
    return _safe_div(base, _rolling_std(base, 252))
