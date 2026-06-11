"""
88_88_insider_transaction_freq — Base Features 376-450
Domain: 88_insider_transaction_freq
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

def itf_376_voladj_5d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 88 insider transaction freq for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = insider_buy_value
    return _safe_div(base, _rolling_std(base, 5))

def itf_377_voladj_21d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 88 insider transaction freq for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = insider_buy_value
    return _safe_div(base, _rolling_std(base, 21))

def itf_378_voladj_63d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 88 insider transaction freq for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = insider_buy_value
    return _safe_div(base, _rolling_std(base, 63))

def itf_379_voladj_126d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 88 insider transaction freq for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = insider_buy_value
    return _safe_div(base, _rolling_std(base, 126))

def itf_380_voladj_252d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 88 insider transaction freq for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = insider_buy_value
    return _safe_div(base, _rolling_std(base, 252))

def itf_381_lognorm_5d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 88 insider transaction freq over 5d to stabilize variance and capture exponential shifts.
    """
    base = insider_buy_value
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def itf_382_lognorm_21d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 88 insider transaction freq over 21d to stabilize variance and capture exponential shifts.
    """
    base = insider_buy_value
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def itf_383_lognorm_63d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 88 insider transaction freq over 63d to stabilize variance and capture exponential shifts.
    """
    base = insider_buy_value
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def itf_384_lognorm_126d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 88 insider transaction freq over 126d to stabilize variance and capture exponential shifts.
    """
    base = insider_buy_value
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def itf_385_lognorm_252d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 88 insider transaction freq over 252d to stabilize variance and capture exponential shifts.
    """
    base = insider_buy_value
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def itf_386_lvl_5d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 88 insider transaction freq over a 5d horizon to identify extreme regimes.
    """
    base = _safe_div(insider_buy_value, insider_buy_value + insider_sell_value)
    return _rolling_mean(base, 5)

def itf_387_lvl_21d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 88 insider transaction freq over a 21d horizon to identify extreme regimes.
    """
    base = _safe_div(insider_buy_value, insider_buy_value + insider_sell_value)
    return _rolling_mean(base, 21)

def itf_388_lvl_63d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 88 insider transaction freq over a 63d horizon to identify extreme regimes.
    """
    base = _safe_div(insider_buy_value, insider_buy_value + insider_sell_value)
    return _rolling_mean(base, 63)

def itf_389_lvl_126d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 88 insider transaction freq over a 126d horizon to identify extreme regimes.
    """
    base = _safe_div(insider_buy_value, insider_buy_value + insider_sell_value)
    return _rolling_mean(base, 126)

def itf_390_lvl_252d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 88 insider transaction freq over a 252d horizon to identify extreme regimes.
    """
    base = _safe_div(insider_buy_value, insider_buy_value + insider_sell_value)
    return _rolling_mean(base, 252)

def itf_391_zscore_5d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 88 insider transaction freq by measuring deviations from the 5d mean.
    """
    base = _safe_div(insider_buy_value, insider_buy_value + insider_sell_value)
    return _zscore_rolling(base, 5)

def itf_392_zscore_21d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 88 insider transaction freq by measuring deviations from the 21d mean.
    """
    base = _safe_div(insider_buy_value, insider_buy_value + insider_sell_value)
    return _zscore_rolling(base, 21)

def itf_393_zscore_63d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 88 insider transaction freq by measuring deviations from the 63d mean.
    """
    base = _safe_div(insider_buy_value, insider_buy_value + insider_sell_value)
    return _zscore_rolling(base, 63)

def itf_394_zscore_126d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 88 insider transaction freq by measuring deviations from the 126d mean.
    """
    base = _safe_div(insider_buy_value, insider_buy_value + insider_sell_value)
    return _zscore_rolling(base, 126)

def itf_395_zscore_252d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 88 insider transaction freq by measuring deviations from the 252d mean.
    """
    base = _safe_div(insider_buy_value, insider_buy_value + insider_sell_value)
    return _zscore_rolling(base, 252)

def itf_396_rank_5d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 88 insider transaction freq to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = _safe_div(insider_buy_value, insider_buy_value + insider_sell_value)
    return _rank_pct(base, 5)

def itf_397_rank_21d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 88 insider transaction freq to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = _safe_div(insider_buy_value, insider_buy_value + insider_sell_value)
    return _rank_pct(base, 21)

def itf_398_rank_63d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 88 insider transaction freq to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = _safe_div(insider_buy_value, insider_buy_value + insider_sell_value)
    return _rank_pct(base, 63)

def itf_399_rank_126d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 88 insider transaction freq to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = _safe_div(insider_buy_value, insider_buy_value + insider_sell_value)
    return _rank_pct(base, 126)

def itf_400_rank_252d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 88 insider transaction freq to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = _safe_div(insider_buy_value, insider_buy_value + insider_sell_value)
    return _rank_pct(base, 252)

def itf_401_skew_5d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 88 insider transaction freq distribution over 5d to detect tail risk or exhaustion.
    """
    base = _safe_div(insider_buy_value, insider_buy_value + insider_sell_value)
    return _rolling_skew(base, 5)

def itf_402_skew_21d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 88 insider transaction freq distribution over 21d to detect tail risk or exhaustion.
    """
    base = _safe_div(insider_buy_value, insider_buy_value + insider_sell_value)
    return _rolling_skew(base, 21)

def itf_403_skew_63d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 88 insider transaction freq distribution over 63d to detect tail risk or exhaustion.
    """
    base = _safe_div(insider_buy_value, insider_buy_value + insider_sell_value)
    return _rolling_skew(base, 63)

def itf_404_skew_126d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 88 insider transaction freq distribution over 126d to detect tail risk or exhaustion.
    """
    base = _safe_div(insider_buy_value, insider_buy_value + insider_sell_value)
    return _rolling_skew(base, 126)

def itf_405_skew_252d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 88 insider transaction freq distribution over 252d to detect tail risk or exhaustion.
    """
    base = _safe_div(insider_buy_value, insider_buy_value + insider_sell_value)
    return _rolling_skew(base, 252)

def itf_406_kurt_5d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 88 insider transaction freq over 5d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(insider_buy_value, insider_buy_value + insider_sell_value)
    return _rolling_kurt(base, 5)

def itf_407_kurt_21d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 88 insider transaction freq over 21d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(insider_buy_value, insider_buy_value + insider_sell_value)
    return _rolling_kurt(base, 21)

def itf_408_kurt_63d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 88 insider transaction freq over 63d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(insider_buy_value, insider_buy_value + insider_sell_value)
    return _rolling_kurt(base, 63)

def itf_409_kurt_126d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 88 insider transaction freq over 126d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(insider_buy_value, insider_buy_value + insider_sell_value)
    return _rolling_kurt(base, 126)

def itf_410_kurt_252d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 88 insider transaction freq over 252d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(insider_buy_value, insider_buy_value + insider_sell_value)
    return _rolling_kurt(base, 252)

def itf_411_voladj_5d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 88 insider transaction freq for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(insider_buy_value, insider_buy_value + insider_sell_value)
    return _safe_div(base, _rolling_std(base, 5))

def itf_412_voladj_21d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 88 insider transaction freq for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(insider_buy_value, insider_buy_value + insider_sell_value)
    return _safe_div(base, _rolling_std(base, 21))

def itf_413_voladj_63d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 88 insider transaction freq for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(insider_buy_value, insider_buy_value + insider_sell_value)
    return _safe_div(base, _rolling_std(base, 63))

def itf_414_voladj_126d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 88 insider transaction freq for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(insider_buy_value, insider_buy_value + insider_sell_value)
    return _safe_div(base, _rolling_std(base, 126))

def itf_415_voladj_252d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 88 insider transaction freq for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(insider_buy_value, insider_buy_value + insider_sell_value)
    return _safe_div(base, _rolling_std(base, 252))

def itf_416_lognorm_5d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 88 insider transaction freq over 5d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(insider_buy_value, insider_buy_value + insider_sell_value)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def itf_417_lognorm_21d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 88 insider transaction freq over 21d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(insider_buy_value, insider_buy_value + insider_sell_value)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def itf_418_lognorm_63d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 88 insider transaction freq over 63d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(insider_buy_value, insider_buy_value + insider_sell_value)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def itf_419_lognorm_126d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 88 insider transaction freq over 126d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(insider_buy_value, insider_buy_value + insider_sell_value)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def itf_420_lognorm_252d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 88 insider transaction freq over 252d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(insider_buy_value, insider_buy_value + insider_sell_value)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def itf_421_lvl_5d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 88 insider transaction freq over a 5d horizon to identify extreme regimes.
    """
    base = ceo_buy_value + cfo_buy_value
    return _rolling_mean(base, 5)

def itf_422_lvl_21d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 88 insider transaction freq over a 21d horizon to identify extreme regimes.
    """
    base = ceo_buy_value + cfo_buy_value
    return _rolling_mean(base, 21)

def itf_423_lvl_63d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 88 insider transaction freq over a 63d horizon to identify extreme regimes.
    """
    base = ceo_buy_value + cfo_buy_value
    return _rolling_mean(base, 63)

def itf_424_lvl_126d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 88 insider transaction freq over a 126d horizon to identify extreme regimes.
    """
    base = ceo_buy_value + cfo_buy_value
    return _rolling_mean(base, 126)

def itf_425_lvl_252d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 88 insider transaction freq over a 252d horizon to identify extreme regimes.
    """
    base = ceo_buy_value + cfo_buy_value
    return _rolling_mean(base, 252)

def itf_426_zscore_5d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 88 insider transaction freq by measuring deviations from the 5d mean.
    """
    base = ceo_buy_value + cfo_buy_value
    return _zscore_rolling(base, 5)

def itf_427_zscore_21d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 88 insider transaction freq by measuring deviations from the 21d mean.
    """
    base = ceo_buy_value + cfo_buy_value
    return _zscore_rolling(base, 21)

def itf_428_zscore_63d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 88 insider transaction freq by measuring deviations from the 63d mean.
    """
    base = ceo_buy_value + cfo_buy_value
    return _zscore_rolling(base, 63)

def itf_429_zscore_126d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 88 insider transaction freq by measuring deviations from the 126d mean.
    """
    base = ceo_buy_value + cfo_buy_value
    return _zscore_rolling(base, 126)

def itf_430_zscore_252d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 88 insider transaction freq by measuring deviations from the 252d mean.
    """
    base = ceo_buy_value + cfo_buy_value
    return _zscore_rolling(base, 252)

def itf_431_rank_5d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 88 insider transaction freq to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = ceo_buy_value + cfo_buy_value
    return _rank_pct(base, 5)

def itf_432_rank_21d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 88 insider transaction freq to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = ceo_buy_value + cfo_buy_value
    return _rank_pct(base, 21)

def itf_433_rank_63d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 88 insider transaction freq to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = ceo_buy_value + cfo_buy_value
    return _rank_pct(base, 63)

def itf_434_rank_126d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 88 insider transaction freq to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = ceo_buy_value + cfo_buy_value
    return _rank_pct(base, 126)

def itf_435_rank_252d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 88 insider transaction freq to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = ceo_buy_value + cfo_buy_value
    return _rank_pct(base, 252)

def itf_436_skew_5d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 88 insider transaction freq distribution over 5d to detect tail risk or exhaustion.
    """
    base = ceo_buy_value + cfo_buy_value
    return _rolling_skew(base, 5)

def itf_437_skew_21d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 88 insider transaction freq distribution over 21d to detect tail risk or exhaustion.
    """
    base = ceo_buy_value + cfo_buy_value
    return _rolling_skew(base, 21)

def itf_438_skew_63d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 88 insider transaction freq distribution over 63d to detect tail risk or exhaustion.
    """
    base = ceo_buy_value + cfo_buy_value
    return _rolling_skew(base, 63)

def itf_439_skew_126d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 88 insider transaction freq distribution over 126d to detect tail risk or exhaustion.
    """
    base = ceo_buy_value + cfo_buy_value
    return _rolling_skew(base, 126)

def itf_440_skew_252d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 88 insider transaction freq distribution over 252d to detect tail risk or exhaustion.
    """
    base = ceo_buy_value + cfo_buy_value
    return _rolling_skew(base, 252)

def itf_441_kurt_5d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 88 insider transaction freq over 5d to capture explosive breakdown or reversal points.
    """
    base = ceo_buy_value + cfo_buy_value
    return _rolling_kurt(base, 5)

def itf_442_kurt_21d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 88 insider transaction freq over 21d to capture explosive breakdown or reversal points.
    """
    base = ceo_buy_value + cfo_buy_value
    return _rolling_kurt(base, 21)

def itf_443_kurt_63d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 88 insider transaction freq over 63d to capture explosive breakdown or reversal points.
    """
    base = ceo_buy_value + cfo_buy_value
    return _rolling_kurt(base, 63)

def itf_444_kurt_126d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 88 insider transaction freq over 126d to capture explosive breakdown or reversal points.
    """
    base = ceo_buy_value + cfo_buy_value
    return _rolling_kurt(base, 126)

def itf_445_kurt_252d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 88 insider transaction freq over 252d to capture explosive breakdown or reversal points.
    """
    base = ceo_buy_value + cfo_buy_value
    return _rolling_kurt(base, 252)

def itf_446_voladj_5d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 88 insider transaction freq for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = ceo_buy_value + cfo_buy_value
    return _safe_div(base, _rolling_std(base, 5))

def itf_447_voladj_21d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 88 insider transaction freq for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = ceo_buy_value + cfo_buy_value
    return _safe_div(base, _rolling_std(base, 21))

def itf_448_voladj_63d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 88 insider transaction freq for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = ceo_buy_value + cfo_buy_value
    return _safe_div(base, _rolling_std(base, 63))

def itf_449_voladj_126d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 88 insider transaction freq for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = ceo_buy_value + cfo_buy_value
    return _safe_div(base, _rolling_std(base, 126))

def itf_450_voladj_252d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 88 insider transaction freq for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = ceo_buy_value + cfo_buy_value
    return _safe_div(base, _rolling_std(base, 252))
