"""
95_95_forced_selling_proxy — Base Features 376-450
Domain: 95_forced_selling_proxy
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

def fsel_376_voladj_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 95 forced selling proxy for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = inst_buy_value
    return _safe_div(base, _rolling_std(base, 5))

def fsel_377_voladj_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 95 forced selling proxy for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = inst_buy_value
    return _safe_div(base, _rolling_std(base, 21))

def fsel_378_voladj_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 95 forced selling proxy for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = inst_buy_value
    return _safe_div(base, _rolling_std(base, 63))

def fsel_379_voladj_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 95 forced selling proxy for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = inst_buy_value
    return _safe_div(base, _rolling_std(base, 126))

def fsel_380_voladj_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 95 forced selling proxy for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = inst_buy_value
    return _safe_div(base, _rolling_std(base, 252))

def fsel_381_lognorm_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 95 forced selling proxy over 5d to stabilize variance and capture exponential shifts.
    """
    base = inst_buy_value
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def fsel_382_lognorm_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 95 forced selling proxy over 21d to stabilize variance and capture exponential shifts.
    """
    base = inst_buy_value
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def fsel_383_lognorm_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 95 forced selling proxy over 63d to stabilize variance and capture exponential shifts.
    """
    base = inst_buy_value
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def fsel_384_lognorm_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 95 forced selling proxy over 126d to stabilize variance and capture exponential shifts.
    """
    base = inst_buy_value
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def fsel_385_lognorm_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 95 forced selling proxy over 252d to stabilize variance and capture exponential shifts.
    """
    base = inst_buy_value
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def fsel_386_lvl_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 95 forced selling proxy over a 5d horizon to identify extreme regimes.
    """
    base = inst_sell_value
    return _rolling_mean(base, 5)

def fsel_387_lvl_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 95 forced selling proxy over a 21d horizon to identify extreme regimes.
    """
    base = inst_sell_value
    return _rolling_mean(base, 21)

def fsel_388_lvl_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 95 forced selling proxy over a 63d horizon to identify extreme regimes.
    """
    base = inst_sell_value
    return _rolling_mean(base, 63)

def fsel_389_lvl_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 95 forced selling proxy over a 126d horizon to identify extreme regimes.
    """
    base = inst_sell_value
    return _rolling_mean(base, 126)

def fsel_390_lvl_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 95 forced selling proxy over a 252d horizon to identify extreme regimes.
    """
    base = inst_sell_value
    return _rolling_mean(base, 252)

def fsel_391_zscore_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 95 forced selling proxy by measuring deviations from the 5d mean.
    """
    base = inst_sell_value
    return _zscore_rolling(base, 5)

def fsel_392_zscore_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 95 forced selling proxy by measuring deviations from the 21d mean.
    """
    base = inst_sell_value
    return _zscore_rolling(base, 21)

def fsel_393_zscore_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 95 forced selling proxy by measuring deviations from the 63d mean.
    """
    base = inst_sell_value
    return _zscore_rolling(base, 63)

def fsel_394_zscore_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 95 forced selling proxy by measuring deviations from the 126d mean.
    """
    base = inst_sell_value
    return _zscore_rolling(base, 126)

def fsel_395_zscore_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 95 forced selling proxy by measuring deviations from the 252d mean.
    """
    base = inst_sell_value
    return _zscore_rolling(base, 252)

def fsel_396_rank_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 95 forced selling proxy to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = inst_sell_value
    return _rank_pct(base, 5)

def fsel_397_rank_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 95 forced selling proxy to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = inst_sell_value
    return _rank_pct(base, 21)

def fsel_398_rank_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 95 forced selling proxy to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = inst_sell_value
    return _rank_pct(base, 63)

def fsel_399_rank_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 95 forced selling proxy to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = inst_sell_value
    return _rank_pct(base, 126)

def fsel_400_rank_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 95 forced selling proxy to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = inst_sell_value
    return _rank_pct(base, 252)

def fsel_401_skew_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 95 forced selling proxy distribution over 5d to detect tail risk or exhaustion.
    """
    base = inst_sell_value
    return _rolling_skew(base, 5)

def fsel_402_skew_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 95 forced selling proxy distribution over 21d to detect tail risk or exhaustion.
    """
    base = inst_sell_value
    return _rolling_skew(base, 21)

def fsel_403_skew_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 95 forced selling proxy distribution over 63d to detect tail risk or exhaustion.
    """
    base = inst_sell_value
    return _rolling_skew(base, 63)

def fsel_404_skew_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 95 forced selling proxy distribution over 126d to detect tail risk or exhaustion.
    """
    base = inst_sell_value
    return _rolling_skew(base, 126)

def fsel_405_skew_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 95 forced selling proxy distribution over 252d to detect tail risk or exhaustion.
    """
    base = inst_sell_value
    return _rolling_skew(base, 252)

def fsel_406_kurt_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 95 forced selling proxy over 5d to capture explosive breakdown or reversal points.
    """
    base = inst_sell_value
    return _rolling_kurt(base, 5)

def fsel_407_kurt_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 95 forced selling proxy over 21d to capture explosive breakdown or reversal points.
    """
    base = inst_sell_value
    return _rolling_kurt(base, 21)

def fsel_408_kurt_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 95 forced selling proxy over 63d to capture explosive breakdown or reversal points.
    """
    base = inst_sell_value
    return _rolling_kurt(base, 63)

def fsel_409_kurt_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 95 forced selling proxy over 126d to capture explosive breakdown or reversal points.
    """
    base = inst_sell_value
    return _rolling_kurt(base, 126)

def fsel_410_kurt_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 95 forced selling proxy over 252d to capture explosive breakdown or reversal points.
    """
    base = inst_sell_value
    return _rolling_kurt(base, 252)

def fsel_411_voladj_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 95 forced selling proxy for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = inst_sell_value
    return _safe_div(base, _rolling_std(base, 5))

def fsel_412_voladj_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 95 forced selling proxy for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = inst_sell_value
    return _safe_div(base, _rolling_std(base, 21))

def fsel_413_voladj_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 95 forced selling proxy for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = inst_sell_value
    return _safe_div(base, _rolling_std(base, 63))

def fsel_414_voladj_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 95 forced selling proxy for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = inst_sell_value
    return _safe_div(base, _rolling_std(base, 126))

def fsel_415_voladj_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 95 forced selling proxy for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = inst_sell_value
    return _safe_div(base, _rolling_std(base, 252))

def fsel_416_lognorm_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 95 forced selling proxy over 5d to stabilize variance and capture exponential shifts.
    """
    base = inst_sell_value
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def fsel_417_lognorm_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 95 forced selling proxy over 21d to stabilize variance and capture exponential shifts.
    """
    base = inst_sell_value
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def fsel_418_lognorm_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 95 forced selling proxy over 63d to stabilize variance and capture exponential shifts.
    """
    base = inst_sell_value
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def fsel_419_lognorm_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 95 forced selling proxy over 126d to stabilize variance and capture exponential shifts.
    """
    base = inst_sell_value
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def fsel_420_lognorm_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 95 forced selling proxy over 252d to stabilize variance and capture exponential shifts.
    """
    base = inst_sell_value
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def fsel_421_lvl_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 95 forced selling proxy over a 5d horizon to identify extreme regimes.
    """
    base = inst_buy_value - inst_sell_value
    return _rolling_mean(base, 5)

def fsel_422_lvl_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 95 forced selling proxy over a 21d horizon to identify extreme regimes.
    """
    base = inst_buy_value - inst_sell_value
    return _rolling_mean(base, 21)

def fsel_423_lvl_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 95 forced selling proxy over a 63d horizon to identify extreme regimes.
    """
    base = inst_buy_value - inst_sell_value
    return _rolling_mean(base, 63)

def fsel_424_lvl_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 95 forced selling proxy over a 126d horizon to identify extreme regimes.
    """
    base = inst_buy_value - inst_sell_value
    return _rolling_mean(base, 126)

def fsel_425_lvl_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 95 forced selling proxy over a 252d horizon to identify extreme regimes.
    """
    base = inst_buy_value - inst_sell_value
    return _rolling_mean(base, 252)

def fsel_426_zscore_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 95 forced selling proxy by measuring deviations from the 5d mean.
    """
    base = inst_buy_value - inst_sell_value
    return _zscore_rolling(base, 5)

def fsel_427_zscore_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 95 forced selling proxy by measuring deviations from the 21d mean.
    """
    base = inst_buy_value - inst_sell_value
    return _zscore_rolling(base, 21)

def fsel_428_zscore_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 95 forced selling proxy by measuring deviations from the 63d mean.
    """
    base = inst_buy_value - inst_sell_value
    return _zscore_rolling(base, 63)

def fsel_429_zscore_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 95 forced selling proxy by measuring deviations from the 126d mean.
    """
    base = inst_buy_value - inst_sell_value
    return _zscore_rolling(base, 126)

def fsel_430_zscore_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 95 forced selling proxy by measuring deviations from the 252d mean.
    """
    base = inst_buy_value - inst_sell_value
    return _zscore_rolling(base, 252)

def fsel_431_rank_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 95 forced selling proxy to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = inst_buy_value - inst_sell_value
    return _rank_pct(base, 5)

def fsel_432_rank_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 95 forced selling proxy to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = inst_buy_value - inst_sell_value
    return _rank_pct(base, 21)

def fsel_433_rank_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 95 forced selling proxy to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = inst_buy_value - inst_sell_value
    return _rank_pct(base, 63)

def fsel_434_rank_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 95 forced selling proxy to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = inst_buy_value - inst_sell_value
    return _rank_pct(base, 126)

def fsel_435_rank_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 95 forced selling proxy to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = inst_buy_value - inst_sell_value
    return _rank_pct(base, 252)

def fsel_436_skew_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 95 forced selling proxy distribution over 5d to detect tail risk or exhaustion.
    """
    base = inst_buy_value - inst_sell_value
    return _rolling_skew(base, 5)

def fsel_437_skew_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 95 forced selling proxy distribution over 21d to detect tail risk or exhaustion.
    """
    base = inst_buy_value - inst_sell_value
    return _rolling_skew(base, 21)

def fsel_438_skew_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 95 forced selling proxy distribution over 63d to detect tail risk or exhaustion.
    """
    base = inst_buy_value - inst_sell_value
    return _rolling_skew(base, 63)

def fsel_439_skew_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 95 forced selling proxy distribution over 126d to detect tail risk or exhaustion.
    """
    base = inst_buy_value - inst_sell_value
    return _rolling_skew(base, 126)

def fsel_440_skew_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 95 forced selling proxy distribution over 252d to detect tail risk or exhaustion.
    """
    base = inst_buy_value - inst_sell_value
    return _rolling_skew(base, 252)

def fsel_441_kurt_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 95 forced selling proxy over 5d to capture explosive breakdown or reversal points.
    """
    base = inst_buy_value - inst_sell_value
    return _rolling_kurt(base, 5)

def fsel_442_kurt_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 95 forced selling proxy over 21d to capture explosive breakdown or reversal points.
    """
    base = inst_buy_value - inst_sell_value
    return _rolling_kurt(base, 21)

def fsel_443_kurt_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 95 forced selling proxy over 63d to capture explosive breakdown or reversal points.
    """
    base = inst_buy_value - inst_sell_value
    return _rolling_kurt(base, 63)

def fsel_444_kurt_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 95 forced selling proxy over 126d to capture explosive breakdown or reversal points.
    """
    base = inst_buy_value - inst_sell_value
    return _rolling_kurt(base, 126)

def fsel_445_kurt_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 95 forced selling proxy over 252d to capture explosive breakdown or reversal points.
    """
    base = inst_buy_value - inst_sell_value
    return _rolling_kurt(base, 252)

def fsel_446_voladj_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 95 forced selling proxy for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = inst_buy_value - inst_sell_value
    return _safe_div(base, _rolling_std(base, 5))

def fsel_447_voladj_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 95 forced selling proxy for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = inst_buy_value - inst_sell_value
    return _safe_div(base, _rolling_std(base, 21))

def fsel_448_voladj_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 95 forced selling proxy for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = inst_buy_value - inst_sell_value
    return _safe_div(base, _rolling_std(base, 63))

def fsel_449_voladj_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 95 forced selling proxy for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = inst_buy_value - inst_sell_value
    return _safe_div(base, _rolling_std(base, 126))

def fsel_450_voladj_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 95 forced selling proxy for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = inst_buy_value - inst_sell_value
    return _safe_div(base, _rolling_std(base, 252))
