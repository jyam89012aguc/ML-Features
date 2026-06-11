"""
76_76_balance_sheet_decay — Base Features 376-450
Domain: 76_balance_sheet_decay
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

def bdec_376_voladj_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 76 balance sheet decay for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(55)
    return _safe_div(base, _rolling_std(base, 5))

def bdec_377_voladj_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 76 balance sheet decay for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(55)
    return _safe_div(base, _rolling_std(base, 21))

def bdec_378_voladj_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 76 balance sheet decay for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(55)
    return _safe_div(base, _rolling_std(base, 63))

def bdec_379_voladj_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 76 balance sheet decay for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(55)
    return _safe_div(base, _rolling_std(base, 126))

def bdec_380_voladj_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 76 balance sheet decay for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(55)
    return _safe_div(base, _rolling_std(base, 252))

def bdec_381_lognorm_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 76 balance sheet decay over 5d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(55)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def bdec_382_lognorm_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 76 balance sheet decay over 21d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(55)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def bdec_383_lognorm_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 76 balance sheet decay over 63d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(55)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def bdec_384_lognorm_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 76 balance sheet decay over 126d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(55)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def bdec_385_lognorm_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 76 balance sheet decay over 252d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(55)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def bdec_386_lvl_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 76 balance sheet decay over a 5d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(60)
    return _rolling_mean(base, 5)

def bdec_387_lvl_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 76 balance sheet decay over a 21d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(60)
    return _rolling_mean(base, 21)

def bdec_388_lvl_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 76 balance sheet decay over a 63d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(60)
    return _rolling_mean(base, 63)

def bdec_389_lvl_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 76 balance sheet decay over a 126d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(60)
    return _rolling_mean(base, 126)

def bdec_390_lvl_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 76 balance sheet decay over a 252d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(60)
    return _rolling_mean(base, 252)

def bdec_391_zscore_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 76 balance sheet decay by measuring deviations from the 5d mean.
    """
    base = marketcap.pct_change(60)
    return _zscore_rolling(base, 5)

def bdec_392_zscore_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 76 balance sheet decay by measuring deviations from the 21d mean.
    """
    base = marketcap.pct_change(60)
    return _zscore_rolling(base, 21)

def bdec_393_zscore_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 76 balance sheet decay by measuring deviations from the 63d mean.
    """
    base = marketcap.pct_change(60)
    return _zscore_rolling(base, 63)

def bdec_394_zscore_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 76 balance sheet decay by measuring deviations from the 126d mean.
    """
    base = marketcap.pct_change(60)
    return _zscore_rolling(base, 126)

def bdec_395_zscore_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 76 balance sheet decay by measuring deviations from the 252d mean.
    """
    base = marketcap.pct_change(60)
    return _zscore_rolling(base, 252)

def bdec_396_rank_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 76 balance sheet decay to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(60)
    return _rank_pct(base, 5)

def bdec_397_rank_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 76 balance sheet decay to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(60)
    return _rank_pct(base, 21)

def bdec_398_rank_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 76 balance sheet decay to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(60)
    return _rank_pct(base, 63)

def bdec_399_rank_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 76 balance sheet decay to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(60)
    return _rank_pct(base, 126)

def bdec_400_rank_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 76 balance sheet decay to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(60)
    return _rank_pct(base, 252)

def bdec_401_skew_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 76 balance sheet decay distribution over 5d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(60)
    return _rolling_skew(base, 5)

def bdec_402_skew_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 76 balance sheet decay distribution over 21d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(60)
    return _rolling_skew(base, 21)

def bdec_403_skew_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 76 balance sheet decay distribution over 63d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(60)
    return _rolling_skew(base, 63)

def bdec_404_skew_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 76 balance sheet decay distribution over 126d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(60)
    return _rolling_skew(base, 126)

def bdec_405_skew_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 76 balance sheet decay distribution over 252d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(60)
    return _rolling_skew(base, 252)

def bdec_406_kurt_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 76 balance sheet decay over 5d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(60)
    return _rolling_kurt(base, 5)

def bdec_407_kurt_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 76 balance sheet decay over 21d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(60)
    return _rolling_kurt(base, 21)

def bdec_408_kurt_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 76 balance sheet decay over 63d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(60)
    return _rolling_kurt(base, 63)

def bdec_409_kurt_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 76 balance sheet decay over 126d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(60)
    return _rolling_kurt(base, 126)

def bdec_410_kurt_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 76 balance sheet decay over 252d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(60)
    return _rolling_kurt(base, 252)

def bdec_411_voladj_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 76 balance sheet decay for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(60)
    return _safe_div(base, _rolling_std(base, 5))

def bdec_412_voladj_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 76 balance sheet decay for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(60)
    return _safe_div(base, _rolling_std(base, 21))

def bdec_413_voladj_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 76 balance sheet decay for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(60)
    return _safe_div(base, _rolling_std(base, 63))

def bdec_414_voladj_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 76 balance sheet decay for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(60)
    return _safe_div(base, _rolling_std(base, 126))

def bdec_415_voladj_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 76 balance sheet decay for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(60)
    return _safe_div(base, _rolling_std(base, 252))

def bdec_416_lognorm_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 76 balance sheet decay over 5d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(60)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def bdec_417_lognorm_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 76 balance sheet decay over 21d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(60)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def bdec_418_lognorm_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 76 balance sheet decay over 63d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(60)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def bdec_419_lognorm_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 76 balance sheet decay over 126d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(60)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def bdec_420_lognorm_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 76 balance sheet decay over 252d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(60)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def bdec_421_lvl_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 76 balance sheet decay over a 5d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(65)
    return _rolling_mean(base, 5)

def bdec_422_lvl_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 76 balance sheet decay over a 21d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(65)
    return _rolling_mean(base, 21)

def bdec_423_lvl_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 76 balance sheet decay over a 63d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(65)
    return _rolling_mean(base, 63)

def bdec_424_lvl_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 76 balance sheet decay over a 126d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(65)
    return _rolling_mean(base, 126)

def bdec_425_lvl_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 76 balance sheet decay over a 252d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(65)
    return _rolling_mean(base, 252)

def bdec_426_zscore_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 76 balance sheet decay by measuring deviations from the 5d mean.
    """
    base = marketcap.pct_change(65)
    return _zscore_rolling(base, 5)

def bdec_427_zscore_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 76 balance sheet decay by measuring deviations from the 21d mean.
    """
    base = marketcap.pct_change(65)
    return _zscore_rolling(base, 21)

def bdec_428_zscore_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 76 balance sheet decay by measuring deviations from the 63d mean.
    """
    base = marketcap.pct_change(65)
    return _zscore_rolling(base, 63)

def bdec_429_zscore_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 76 balance sheet decay by measuring deviations from the 126d mean.
    """
    base = marketcap.pct_change(65)
    return _zscore_rolling(base, 126)

def bdec_430_zscore_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 76 balance sheet decay by measuring deviations from the 252d mean.
    """
    base = marketcap.pct_change(65)
    return _zscore_rolling(base, 252)

def bdec_431_rank_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 76 balance sheet decay to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(65)
    return _rank_pct(base, 5)

def bdec_432_rank_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 76 balance sheet decay to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(65)
    return _rank_pct(base, 21)

def bdec_433_rank_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 76 balance sheet decay to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(65)
    return _rank_pct(base, 63)

def bdec_434_rank_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 76 balance sheet decay to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(65)
    return _rank_pct(base, 126)

def bdec_435_rank_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 76 balance sheet decay to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(65)
    return _rank_pct(base, 252)

def bdec_436_skew_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 76 balance sheet decay distribution over 5d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(65)
    return _rolling_skew(base, 5)

def bdec_437_skew_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 76 balance sheet decay distribution over 21d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(65)
    return _rolling_skew(base, 21)

def bdec_438_skew_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 76 balance sheet decay distribution over 63d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(65)
    return _rolling_skew(base, 63)

def bdec_439_skew_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 76 balance sheet decay distribution over 126d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(65)
    return _rolling_skew(base, 126)

def bdec_440_skew_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 76 balance sheet decay distribution over 252d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(65)
    return _rolling_skew(base, 252)

def bdec_441_kurt_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 76 balance sheet decay over 5d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(65)
    return _rolling_kurt(base, 5)

def bdec_442_kurt_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 76 balance sheet decay over 21d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(65)
    return _rolling_kurt(base, 21)

def bdec_443_kurt_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 76 balance sheet decay over 63d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(65)
    return _rolling_kurt(base, 63)

def bdec_444_kurt_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 76 balance sheet decay over 126d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(65)
    return _rolling_kurt(base, 126)

def bdec_445_kurt_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 76 balance sheet decay over 252d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(65)
    return _rolling_kurt(base, 252)

def bdec_446_voladj_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 76 balance sheet decay for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(65)
    return _safe_div(base, _rolling_std(base, 5))

def bdec_447_voladj_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 76 balance sheet decay for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(65)
    return _safe_div(base, _rolling_std(base, 21))

def bdec_448_voladj_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 76 balance sheet decay for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(65)
    return _safe_div(base, _rolling_std(base, 63))

def bdec_449_voladj_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 76 balance sheet decay for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(65)
    return _safe_div(base, _rolling_std(base, 126))

def bdec_450_voladj_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 76 balance sheet decay for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(65)
    return _safe_div(base, _rolling_std(base, 252))
