"""
87_87_insider_timing — Base Features 376-450
Domain: 87_insider_timing
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

def itm_376_voladj_5d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 87 insider timing for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = insider_buy_value
    return _safe_div(base, _rolling_std(base, 5))

def itm_377_voladj_21d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 87 insider timing for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = insider_buy_value
    return _safe_div(base, _rolling_std(base, 21))

def itm_378_voladj_63d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 87 insider timing for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = insider_buy_value
    return _safe_div(base, _rolling_std(base, 63))

def itm_379_voladj_126d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 87 insider timing for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = insider_buy_value
    return _safe_div(base, _rolling_std(base, 126))

def itm_380_voladj_252d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 87 insider timing for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = insider_buy_value
    return _safe_div(base, _rolling_std(base, 252))

def itm_381_lognorm_5d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 87 insider timing over 5d to stabilize variance and capture exponential shifts.
    """
    base = insider_buy_value
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def itm_382_lognorm_21d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 87 insider timing over 21d to stabilize variance and capture exponential shifts.
    """
    base = insider_buy_value
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def itm_383_lognorm_63d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 87 insider timing over 63d to stabilize variance and capture exponential shifts.
    """
    base = insider_buy_value
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def itm_384_lognorm_126d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 87 insider timing over 126d to stabilize variance and capture exponential shifts.
    """
    base = insider_buy_value
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def itm_385_lognorm_252d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 87 insider timing over 252d to stabilize variance and capture exponential shifts.
    """
    base = insider_buy_value
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def itm_386_lvl_5d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 87 insider timing over a 5d horizon to identify extreme regimes.
    """
    base = _safe_div(insider_buy_value, insider_buy_value + insider_sell_value)
    return _rolling_mean(base, 5)

def itm_387_lvl_21d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 87 insider timing over a 21d horizon to identify extreme regimes.
    """
    base = _safe_div(insider_buy_value, insider_buy_value + insider_sell_value)
    return _rolling_mean(base, 21)

def itm_388_lvl_63d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 87 insider timing over a 63d horizon to identify extreme regimes.
    """
    base = _safe_div(insider_buy_value, insider_buy_value + insider_sell_value)
    return _rolling_mean(base, 63)

def itm_389_lvl_126d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 87 insider timing over a 126d horizon to identify extreme regimes.
    """
    base = _safe_div(insider_buy_value, insider_buy_value + insider_sell_value)
    return _rolling_mean(base, 126)

def itm_390_lvl_252d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 87 insider timing over a 252d horizon to identify extreme regimes.
    """
    base = _safe_div(insider_buy_value, insider_buy_value + insider_sell_value)
    return _rolling_mean(base, 252)

def itm_391_zscore_5d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 87 insider timing by measuring deviations from the 5d mean.
    """
    base = _safe_div(insider_buy_value, insider_buy_value + insider_sell_value)
    return _zscore_rolling(base, 5)

def itm_392_zscore_21d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 87 insider timing by measuring deviations from the 21d mean.
    """
    base = _safe_div(insider_buy_value, insider_buy_value + insider_sell_value)
    return _zscore_rolling(base, 21)

def itm_393_zscore_63d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 87 insider timing by measuring deviations from the 63d mean.
    """
    base = _safe_div(insider_buy_value, insider_buy_value + insider_sell_value)
    return _zscore_rolling(base, 63)

def itm_394_zscore_126d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 87 insider timing by measuring deviations from the 126d mean.
    """
    base = _safe_div(insider_buy_value, insider_buy_value + insider_sell_value)
    return _zscore_rolling(base, 126)

def itm_395_zscore_252d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 87 insider timing by measuring deviations from the 252d mean.
    """
    base = _safe_div(insider_buy_value, insider_buy_value + insider_sell_value)
    return _zscore_rolling(base, 252)

def itm_396_rank_5d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 87 insider timing to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = _safe_div(insider_buy_value, insider_buy_value + insider_sell_value)
    return _rank_pct(base, 5)

def itm_397_rank_21d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 87 insider timing to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = _safe_div(insider_buy_value, insider_buy_value + insider_sell_value)
    return _rank_pct(base, 21)

def itm_398_rank_63d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 87 insider timing to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = _safe_div(insider_buy_value, insider_buy_value + insider_sell_value)
    return _rank_pct(base, 63)

def itm_399_rank_126d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 87 insider timing to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = _safe_div(insider_buy_value, insider_buy_value + insider_sell_value)
    return _rank_pct(base, 126)

def itm_400_rank_252d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 87 insider timing to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = _safe_div(insider_buy_value, insider_buy_value + insider_sell_value)
    return _rank_pct(base, 252)

def itm_401_skew_5d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 87 insider timing distribution over 5d to detect tail risk or exhaustion.
    """
    base = _safe_div(insider_buy_value, insider_buy_value + insider_sell_value)
    return _rolling_skew(base, 5)

def itm_402_skew_21d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 87 insider timing distribution over 21d to detect tail risk or exhaustion.
    """
    base = _safe_div(insider_buy_value, insider_buy_value + insider_sell_value)
    return _rolling_skew(base, 21)

def itm_403_skew_63d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 87 insider timing distribution over 63d to detect tail risk or exhaustion.
    """
    base = _safe_div(insider_buy_value, insider_buy_value + insider_sell_value)
    return _rolling_skew(base, 63)

def itm_404_skew_126d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 87 insider timing distribution over 126d to detect tail risk or exhaustion.
    """
    base = _safe_div(insider_buy_value, insider_buy_value + insider_sell_value)
    return _rolling_skew(base, 126)

def itm_405_skew_252d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 87 insider timing distribution over 252d to detect tail risk or exhaustion.
    """
    base = _safe_div(insider_buy_value, insider_buy_value + insider_sell_value)
    return _rolling_skew(base, 252)

def itm_406_kurt_5d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 87 insider timing over 5d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(insider_buy_value, insider_buy_value + insider_sell_value)
    return _rolling_kurt(base, 5)

def itm_407_kurt_21d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 87 insider timing over 21d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(insider_buy_value, insider_buy_value + insider_sell_value)
    return _rolling_kurt(base, 21)

def itm_408_kurt_63d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 87 insider timing over 63d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(insider_buy_value, insider_buy_value + insider_sell_value)
    return _rolling_kurt(base, 63)

def itm_409_kurt_126d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 87 insider timing over 126d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(insider_buy_value, insider_buy_value + insider_sell_value)
    return _rolling_kurt(base, 126)

def itm_410_kurt_252d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 87 insider timing over 252d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(insider_buy_value, insider_buy_value + insider_sell_value)
    return _rolling_kurt(base, 252)

def itm_411_voladj_5d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 87 insider timing for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(insider_buy_value, insider_buy_value + insider_sell_value)
    return _safe_div(base, _rolling_std(base, 5))

def itm_412_voladj_21d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 87 insider timing for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(insider_buy_value, insider_buy_value + insider_sell_value)
    return _safe_div(base, _rolling_std(base, 21))

def itm_413_voladj_63d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 87 insider timing for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(insider_buy_value, insider_buy_value + insider_sell_value)
    return _safe_div(base, _rolling_std(base, 63))

def itm_414_voladj_126d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 87 insider timing for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(insider_buy_value, insider_buy_value + insider_sell_value)
    return _safe_div(base, _rolling_std(base, 126))

def itm_415_voladj_252d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 87 insider timing for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(insider_buy_value, insider_buy_value + insider_sell_value)
    return _safe_div(base, _rolling_std(base, 252))

def itm_416_lognorm_5d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 87 insider timing over 5d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(insider_buy_value, insider_buy_value + insider_sell_value)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def itm_417_lognorm_21d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 87 insider timing over 21d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(insider_buy_value, insider_buy_value + insider_sell_value)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def itm_418_lognorm_63d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 87 insider timing over 63d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(insider_buy_value, insider_buy_value + insider_sell_value)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def itm_419_lognorm_126d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 87 insider timing over 126d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(insider_buy_value, insider_buy_value + insider_sell_value)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def itm_420_lognorm_252d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 87 insider timing over 252d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(insider_buy_value, insider_buy_value + insider_sell_value)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def itm_421_lvl_5d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 87 insider timing over a 5d horizon to identify extreme regimes.
    """
    base = ceo_buy_value + cfo_buy_value
    return _rolling_mean(base, 5)

def itm_422_lvl_21d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 87 insider timing over a 21d horizon to identify extreme regimes.
    """
    base = ceo_buy_value + cfo_buy_value
    return _rolling_mean(base, 21)

def itm_423_lvl_63d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 87 insider timing over a 63d horizon to identify extreme regimes.
    """
    base = ceo_buy_value + cfo_buy_value
    return _rolling_mean(base, 63)

def itm_424_lvl_126d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 87 insider timing over a 126d horizon to identify extreme regimes.
    """
    base = ceo_buy_value + cfo_buy_value
    return _rolling_mean(base, 126)

def itm_425_lvl_252d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 87 insider timing over a 252d horizon to identify extreme regimes.
    """
    base = ceo_buy_value + cfo_buy_value
    return _rolling_mean(base, 252)

def itm_426_zscore_5d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 87 insider timing by measuring deviations from the 5d mean.
    """
    base = ceo_buy_value + cfo_buy_value
    return _zscore_rolling(base, 5)

def itm_427_zscore_21d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 87 insider timing by measuring deviations from the 21d mean.
    """
    base = ceo_buy_value + cfo_buy_value
    return _zscore_rolling(base, 21)

def itm_428_zscore_63d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 87 insider timing by measuring deviations from the 63d mean.
    """
    base = ceo_buy_value + cfo_buy_value
    return _zscore_rolling(base, 63)

def itm_429_zscore_126d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 87 insider timing by measuring deviations from the 126d mean.
    """
    base = ceo_buy_value + cfo_buy_value
    return _zscore_rolling(base, 126)

def itm_430_zscore_252d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 87 insider timing by measuring deviations from the 252d mean.
    """
    base = ceo_buy_value + cfo_buy_value
    return _zscore_rolling(base, 252)

def itm_431_rank_5d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 87 insider timing to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = ceo_buy_value + cfo_buy_value
    return _rank_pct(base, 5)

def itm_432_rank_21d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 87 insider timing to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = ceo_buy_value + cfo_buy_value
    return _rank_pct(base, 21)

def itm_433_rank_63d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 87 insider timing to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = ceo_buy_value + cfo_buy_value
    return _rank_pct(base, 63)

def itm_434_rank_126d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 87 insider timing to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = ceo_buy_value + cfo_buy_value
    return _rank_pct(base, 126)

def itm_435_rank_252d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 87 insider timing to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = ceo_buy_value + cfo_buy_value
    return _rank_pct(base, 252)

def itm_436_skew_5d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 87 insider timing distribution over 5d to detect tail risk or exhaustion.
    """
    base = ceo_buy_value + cfo_buy_value
    return _rolling_skew(base, 5)

def itm_437_skew_21d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 87 insider timing distribution over 21d to detect tail risk or exhaustion.
    """
    base = ceo_buy_value + cfo_buy_value
    return _rolling_skew(base, 21)

def itm_438_skew_63d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 87 insider timing distribution over 63d to detect tail risk or exhaustion.
    """
    base = ceo_buy_value + cfo_buy_value
    return _rolling_skew(base, 63)

def itm_439_skew_126d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 87 insider timing distribution over 126d to detect tail risk or exhaustion.
    """
    base = ceo_buy_value + cfo_buy_value
    return _rolling_skew(base, 126)

def itm_440_skew_252d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 87 insider timing distribution over 252d to detect tail risk or exhaustion.
    """
    base = ceo_buy_value + cfo_buy_value
    return _rolling_skew(base, 252)

def itm_441_kurt_5d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 87 insider timing over 5d to capture explosive breakdown or reversal points.
    """
    base = ceo_buy_value + cfo_buy_value
    return _rolling_kurt(base, 5)

def itm_442_kurt_21d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 87 insider timing over 21d to capture explosive breakdown or reversal points.
    """
    base = ceo_buy_value + cfo_buy_value
    return _rolling_kurt(base, 21)

def itm_443_kurt_63d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 87 insider timing over 63d to capture explosive breakdown or reversal points.
    """
    base = ceo_buy_value + cfo_buy_value
    return _rolling_kurt(base, 63)

def itm_444_kurt_126d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 87 insider timing over 126d to capture explosive breakdown or reversal points.
    """
    base = ceo_buy_value + cfo_buy_value
    return _rolling_kurt(base, 126)

def itm_445_kurt_252d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 87 insider timing over 252d to capture explosive breakdown or reversal points.
    """
    base = ceo_buy_value + cfo_buy_value
    return _rolling_kurt(base, 252)

def itm_446_voladj_5d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 87 insider timing for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = ceo_buy_value + cfo_buy_value
    return _safe_div(base, _rolling_std(base, 5))

def itm_447_voladj_21d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 87 insider timing for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = ceo_buy_value + cfo_buy_value
    return _safe_div(base, _rolling_std(base, 21))

def itm_448_voladj_63d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 87 insider timing for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = ceo_buy_value + cfo_buy_value
    return _safe_div(base, _rolling_std(base, 63))

def itm_449_voladj_126d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 87 insider timing for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = ceo_buy_value + cfo_buy_value
    return _safe_div(base, _rolling_std(base, 126))

def itm_450_voladj_252d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 87 insider timing for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = ceo_buy_value + cfo_buy_value
    return _safe_div(base, _rolling_std(base, 252))
