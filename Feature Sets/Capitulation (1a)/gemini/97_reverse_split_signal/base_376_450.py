"""
97_97_reverse_split_signal — Base Features 376-450
Domain: 97_reverse_split_signal
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

def rvrs_376_voladj_5d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 97 reverse split signal for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(ocf, debt)
    return _safe_div(base, _rolling_std(base, 5))

def rvrs_377_voladj_21d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 97 reverse split signal for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(ocf, debt)
    return _safe_div(base, _rolling_std(base, 21))

def rvrs_378_voladj_63d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 97 reverse split signal for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(ocf, debt)
    return _safe_div(base, _rolling_std(base, 63))

def rvrs_379_voladj_126d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 97 reverse split signal for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(ocf, debt)
    return _safe_div(base, _rolling_std(base, 126))

def rvrs_380_voladj_252d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 97 reverse split signal for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(ocf, debt)
    return _safe_div(base, _rolling_std(base, 252))

def rvrs_381_lognorm_5d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 97 reverse split signal over 5d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(ocf, debt)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def rvrs_382_lognorm_21d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 97 reverse split signal over 21d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(ocf, debt)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def rvrs_383_lognorm_63d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 97 reverse split signal over 63d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(ocf, debt)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def rvrs_384_lognorm_126d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 97 reverse split signal over 126d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(ocf, debt)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def rvrs_385_lognorm_252d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 97 reverse split signal over 252d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(ocf, debt)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def rvrs_386_lvl_5d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 97 reverse split signal over a 5d horizon to identify extreme regimes.
    """
    base = _safe_div(netinc, equity)
    return _rolling_mean(base, 5)

def rvrs_387_lvl_21d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 97 reverse split signal over a 21d horizon to identify extreme regimes.
    """
    base = _safe_div(netinc, equity)
    return _rolling_mean(base, 21)

def rvrs_388_lvl_63d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 97 reverse split signal over a 63d horizon to identify extreme regimes.
    """
    base = _safe_div(netinc, equity)
    return _rolling_mean(base, 63)

def rvrs_389_lvl_126d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 97 reverse split signal over a 126d horizon to identify extreme regimes.
    """
    base = _safe_div(netinc, equity)
    return _rolling_mean(base, 126)

def rvrs_390_lvl_252d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 97 reverse split signal over a 252d horizon to identify extreme regimes.
    """
    base = _safe_div(netinc, equity)
    return _rolling_mean(base, 252)

def rvrs_391_zscore_5d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 97 reverse split signal by measuring deviations from the 5d mean.
    """
    base = _safe_div(netinc, equity)
    return _zscore_rolling(base, 5)

def rvrs_392_zscore_21d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 97 reverse split signal by measuring deviations from the 21d mean.
    """
    base = _safe_div(netinc, equity)
    return _zscore_rolling(base, 21)

def rvrs_393_zscore_63d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 97 reverse split signal by measuring deviations from the 63d mean.
    """
    base = _safe_div(netinc, equity)
    return _zscore_rolling(base, 63)

def rvrs_394_zscore_126d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 97 reverse split signal by measuring deviations from the 126d mean.
    """
    base = _safe_div(netinc, equity)
    return _zscore_rolling(base, 126)

def rvrs_395_zscore_252d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 97 reverse split signal by measuring deviations from the 252d mean.
    """
    base = _safe_div(netinc, equity)
    return _zscore_rolling(base, 252)

def rvrs_396_rank_5d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 97 reverse split signal to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = _safe_div(netinc, equity)
    return _rank_pct(base, 5)

def rvrs_397_rank_21d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 97 reverse split signal to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = _safe_div(netinc, equity)
    return _rank_pct(base, 21)

def rvrs_398_rank_63d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 97 reverse split signal to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = _safe_div(netinc, equity)
    return _rank_pct(base, 63)

def rvrs_399_rank_126d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 97 reverse split signal to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = _safe_div(netinc, equity)
    return _rank_pct(base, 126)

def rvrs_400_rank_252d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 97 reverse split signal to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = _safe_div(netinc, equity)
    return _rank_pct(base, 252)

def rvrs_401_skew_5d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 97 reverse split signal distribution over 5d to detect tail risk or exhaustion.
    """
    base = _safe_div(netinc, equity)
    return _rolling_skew(base, 5)

def rvrs_402_skew_21d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 97 reverse split signal distribution over 21d to detect tail risk or exhaustion.
    """
    base = _safe_div(netinc, equity)
    return _rolling_skew(base, 21)

def rvrs_403_skew_63d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 97 reverse split signal distribution over 63d to detect tail risk or exhaustion.
    """
    base = _safe_div(netinc, equity)
    return _rolling_skew(base, 63)

def rvrs_404_skew_126d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 97 reverse split signal distribution over 126d to detect tail risk or exhaustion.
    """
    base = _safe_div(netinc, equity)
    return _rolling_skew(base, 126)

def rvrs_405_skew_252d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 97 reverse split signal distribution over 252d to detect tail risk or exhaustion.
    """
    base = _safe_div(netinc, equity)
    return _rolling_skew(base, 252)

def rvrs_406_kurt_5d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 97 reverse split signal over 5d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(netinc, equity)
    return _rolling_kurt(base, 5)

def rvrs_407_kurt_21d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 97 reverse split signal over 21d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(netinc, equity)
    return _rolling_kurt(base, 21)

def rvrs_408_kurt_63d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 97 reverse split signal over 63d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(netinc, equity)
    return _rolling_kurt(base, 63)

def rvrs_409_kurt_126d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 97 reverse split signal over 126d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(netinc, equity)
    return _rolling_kurt(base, 126)

def rvrs_410_kurt_252d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 97 reverse split signal over 252d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(netinc, equity)
    return _rolling_kurt(base, 252)

def rvrs_411_voladj_5d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 97 reverse split signal for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(netinc, equity)
    return _safe_div(base, _rolling_std(base, 5))

def rvrs_412_voladj_21d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 97 reverse split signal for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(netinc, equity)
    return _safe_div(base, _rolling_std(base, 21))

def rvrs_413_voladj_63d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 97 reverse split signal for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(netinc, equity)
    return _safe_div(base, _rolling_std(base, 63))

def rvrs_414_voladj_126d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 97 reverse split signal for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(netinc, equity)
    return _safe_div(base, _rolling_std(base, 126))

def rvrs_415_voladj_252d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 97 reverse split signal for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(netinc, equity)
    return _safe_div(base, _rolling_std(base, 252))

def rvrs_416_lognorm_5d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 97 reverse split signal over 5d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(netinc, equity)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def rvrs_417_lognorm_21d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 97 reverse split signal over 21d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(netinc, equity)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def rvrs_418_lognorm_63d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 97 reverse split signal over 63d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(netinc, equity)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def rvrs_419_lognorm_126d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 97 reverse split signal over 126d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(netinc, equity)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def rvrs_420_lognorm_252d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 97 reverse split signal over 252d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(netinc, equity)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def rvrs_421_lvl_5d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 97 reverse split signal over a 5d horizon to identify extreme regimes.
    """
    base = _safe_div(assets - liabs, assets)
    return _rolling_mean(base, 5)

def rvrs_422_lvl_21d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 97 reverse split signal over a 21d horizon to identify extreme regimes.
    """
    base = _safe_div(assets - liabs, assets)
    return _rolling_mean(base, 21)

def rvrs_423_lvl_63d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 97 reverse split signal over a 63d horizon to identify extreme regimes.
    """
    base = _safe_div(assets - liabs, assets)
    return _rolling_mean(base, 63)

def rvrs_424_lvl_126d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 97 reverse split signal over a 126d horizon to identify extreme regimes.
    """
    base = _safe_div(assets - liabs, assets)
    return _rolling_mean(base, 126)

def rvrs_425_lvl_252d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 97 reverse split signal over a 252d horizon to identify extreme regimes.
    """
    base = _safe_div(assets - liabs, assets)
    return _rolling_mean(base, 252)

def rvrs_426_zscore_5d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 97 reverse split signal by measuring deviations from the 5d mean.
    """
    base = _safe_div(assets - liabs, assets)
    return _zscore_rolling(base, 5)

def rvrs_427_zscore_21d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 97 reverse split signal by measuring deviations from the 21d mean.
    """
    base = _safe_div(assets - liabs, assets)
    return _zscore_rolling(base, 21)

def rvrs_428_zscore_63d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 97 reverse split signal by measuring deviations from the 63d mean.
    """
    base = _safe_div(assets - liabs, assets)
    return _zscore_rolling(base, 63)

def rvrs_429_zscore_126d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 97 reverse split signal by measuring deviations from the 126d mean.
    """
    base = _safe_div(assets - liabs, assets)
    return _zscore_rolling(base, 126)

def rvrs_430_zscore_252d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 97 reverse split signal by measuring deviations from the 252d mean.
    """
    base = _safe_div(assets - liabs, assets)
    return _zscore_rolling(base, 252)

def rvrs_431_rank_5d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 97 reverse split signal to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = _safe_div(assets - liabs, assets)
    return _rank_pct(base, 5)

def rvrs_432_rank_21d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 97 reverse split signal to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = _safe_div(assets - liabs, assets)
    return _rank_pct(base, 21)

def rvrs_433_rank_63d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 97 reverse split signal to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = _safe_div(assets - liabs, assets)
    return _rank_pct(base, 63)

def rvrs_434_rank_126d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 97 reverse split signal to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = _safe_div(assets - liabs, assets)
    return _rank_pct(base, 126)

def rvrs_435_rank_252d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 97 reverse split signal to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = _safe_div(assets - liabs, assets)
    return _rank_pct(base, 252)

def rvrs_436_skew_5d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 97 reverse split signal distribution over 5d to detect tail risk or exhaustion.
    """
    base = _safe_div(assets - liabs, assets)
    return _rolling_skew(base, 5)

def rvrs_437_skew_21d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 97 reverse split signal distribution over 21d to detect tail risk or exhaustion.
    """
    base = _safe_div(assets - liabs, assets)
    return _rolling_skew(base, 21)

def rvrs_438_skew_63d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 97 reverse split signal distribution over 63d to detect tail risk or exhaustion.
    """
    base = _safe_div(assets - liabs, assets)
    return _rolling_skew(base, 63)

def rvrs_439_skew_126d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 97 reverse split signal distribution over 126d to detect tail risk or exhaustion.
    """
    base = _safe_div(assets - liabs, assets)
    return _rolling_skew(base, 126)

def rvrs_440_skew_252d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 97 reverse split signal distribution over 252d to detect tail risk or exhaustion.
    """
    base = _safe_div(assets - liabs, assets)
    return _rolling_skew(base, 252)

def rvrs_441_kurt_5d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 97 reverse split signal over 5d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(assets - liabs, assets)
    return _rolling_kurt(base, 5)

def rvrs_442_kurt_21d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 97 reverse split signal over 21d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(assets - liabs, assets)
    return _rolling_kurt(base, 21)

def rvrs_443_kurt_63d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 97 reverse split signal over 63d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(assets - liabs, assets)
    return _rolling_kurt(base, 63)

def rvrs_444_kurt_126d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 97 reverse split signal over 126d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(assets - liabs, assets)
    return _rolling_kurt(base, 126)

def rvrs_445_kurt_252d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 97 reverse split signal over 252d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(assets - liabs, assets)
    return _rolling_kurt(base, 252)

def rvrs_446_voladj_5d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 97 reverse split signal for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(assets - liabs, assets)
    return _safe_div(base, _rolling_std(base, 5))

def rvrs_447_voladj_21d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 97 reverse split signal for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(assets - liabs, assets)
    return _safe_div(base, _rolling_std(base, 21))

def rvrs_448_voladj_63d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 97 reverse split signal for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(assets - liabs, assets)
    return _safe_div(base, _rolling_std(base, 63))

def rvrs_449_voladj_126d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 97 reverse split signal for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(assets - liabs, assets)
    return _safe_div(base, _rolling_std(base, 126))

def rvrs_450_voladj_252d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 97 reverse split signal for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(assets - liabs, assets)
    return _safe_div(base, _rolling_std(base, 252))
