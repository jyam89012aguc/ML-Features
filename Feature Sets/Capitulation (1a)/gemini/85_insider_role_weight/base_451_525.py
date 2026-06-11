"""
85_85_insider_role_weight — Base Features 451-525
Domain: 85_insider_role_weight
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

def irwt_451_lognorm_5d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 85 insider role weight over 5d to stabilize variance and capture exponential shifts.
    """
    base = ceo_buy_value + cfo_buy_value
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def irwt_452_lognorm_21d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 85 insider role weight over 21d to stabilize variance and capture exponential shifts.
    """
    base = ceo_buy_value + cfo_buy_value
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def irwt_453_lognorm_63d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 85 insider role weight over 63d to stabilize variance and capture exponential shifts.
    """
    base = ceo_buy_value + cfo_buy_value
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def irwt_454_lognorm_126d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 85 insider role weight over 126d to stabilize variance and capture exponential shifts.
    """
    base = ceo_buy_value + cfo_buy_value
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def irwt_455_lognorm_252d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 85 insider role weight over 252d to stabilize variance and capture exponential shifts.
    """
    base = ceo_buy_value + cfo_buy_value
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def irwt_456_lvl_5d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 85 insider role weight over a 5d horizon to identify extreme regimes.
    """
    base = _safe_div(insider_buy_shares, insider_shares_held)
    return _rolling_mean(base, 5)

def irwt_457_lvl_21d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 85 insider role weight over a 21d horizon to identify extreme regimes.
    """
    base = _safe_div(insider_buy_shares, insider_shares_held)
    return _rolling_mean(base, 21)

def irwt_458_lvl_63d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 85 insider role weight over a 63d horizon to identify extreme regimes.
    """
    base = _safe_div(insider_buy_shares, insider_shares_held)
    return _rolling_mean(base, 63)

def irwt_459_lvl_126d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 85 insider role weight over a 126d horizon to identify extreme regimes.
    """
    base = _safe_div(insider_buy_shares, insider_shares_held)
    return _rolling_mean(base, 126)

def irwt_460_lvl_252d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 85 insider role weight over a 252d horizon to identify extreme regimes.
    """
    base = _safe_div(insider_buy_shares, insider_shares_held)
    return _rolling_mean(base, 252)

def irwt_461_zscore_5d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 85 insider role weight by measuring deviations from the 5d mean.
    """
    base = _safe_div(insider_buy_shares, insider_shares_held)
    return _zscore_rolling(base, 5)

def irwt_462_zscore_21d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 85 insider role weight by measuring deviations from the 21d mean.
    """
    base = _safe_div(insider_buy_shares, insider_shares_held)
    return _zscore_rolling(base, 21)

def irwt_463_zscore_63d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 85 insider role weight by measuring deviations from the 63d mean.
    """
    base = _safe_div(insider_buy_shares, insider_shares_held)
    return _zscore_rolling(base, 63)

def irwt_464_zscore_126d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 85 insider role weight by measuring deviations from the 126d mean.
    """
    base = _safe_div(insider_buy_shares, insider_shares_held)
    return _zscore_rolling(base, 126)

def irwt_465_zscore_252d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 85 insider role weight by measuring deviations from the 252d mean.
    """
    base = _safe_div(insider_buy_shares, insider_shares_held)
    return _zscore_rolling(base, 252)

def irwt_466_rank_5d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 85 insider role weight to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = _safe_div(insider_buy_shares, insider_shares_held)
    return _rank_pct(base, 5)

def irwt_467_rank_21d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 85 insider role weight to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = _safe_div(insider_buy_shares, insider_shares_held)
    return _rank_pct(base, 21)

def irwt_468_rank_63d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 85 insider role weight to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = _safe_div(insider_buy_shares, insider_shares_held)
    return _rank_pct(base, 63)

def irwt_469_rank_126d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 85 insider role weight to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = _safe_div(insider_buy_shares, insider_shares_held)
    return _rank_pct(base, 126)

def irwt_470_rank_252d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 85 insider role weight to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = _safe_div(insider_buy_shares, insider_shares_held)
    return _rank_pct(base, 252)

def irwt_471_skew_5d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 85 insider role weight distribution over 5d to detect tail risk or exhaustion.
    """
    base = _safe_div(insider_buy_shares, insider_shares_held)
    return _rolling_skew(base, 5)

def irwt_472_skew_21d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 85 insider role weight distribution over 21d to detect tail risk or exhaustion.
    """
    base = _safe_div(insider_buy_shares, insider_shares_held)
    return _rolling_skew(base, 21)

def irwt_473_skew_63d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 85 insider role weight distribution over 63d to detect tail risk or exhaustion.
    """
    base = _safe_div(insider_buy_shares, insider_shares_held)
    return _rolling_skew(base, 63)

def irwt_474_skew_126d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 85 insider role weight distribution over 126d to detect tail risk or exhaustion.
    """
    base = _safe_div(insider_buy_shares, insider_shares_held)
    return _rolling_skew(base, 126)

def irwt_475_skew_252d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 85 insider role weight distribution over 252d to detect tail risk or exhaustion.
    """
    base = _safe_div(insider_buy_shares, insider_shares_held)
    return _rolling_skew(base, 252)

def irwt_476_kurt_5d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 85 insider role weight over 5d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(insider_buy_shares, insider_shares_held)
    return _rolling_kurt(base, 5)

def irwt_477_kurt_21d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 85 insider role weight over 21d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(insider_buy_shares, insider_shares_held)
    return _rolling_kurt(base, 21)

def irwt_478_kurt_63d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 85 insider role weight over 63d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(insider_buy_shares, insider_shares_held)
    return _rolling_kurt(base, 63)

def irwt_479_kurt_126d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 85 insider role weight over 126d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(insider_buy_shares, insider_shares_held)
    return _rolling_kurt(base, 126)

def irwt_480_kurt_252d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 85 insider role weight over 252d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(insider_buy_shares, insider_shares_held)
    return _rolling_kurt(base, 252)

def irwt_481_voladj_5d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 85 insider role weight for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(insider_buy_shares, insider_shares_held)
    return _safe_div(base, _rolling_std(base, 5))

def irwt_482_voladj_21d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 85 insider role weight for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(insider_buy_shares, insider_shares_held)
    return _safe_div(base, _rolling_std(base, 21))

def irwt_483_voladj_63d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 85 insider role weight for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(insider_buy_shares, insider_shares_held)
    return _safe_div(base, _rolling_std(base, 63))

def irwt_484_voladj_126d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 85 insider role weight for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(insider_buy_shares, insider_shares_held)
    return _safe_div(base, _rolling_std(base, 126))

def irwt_485_voladj_252d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 85 insider role weight for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(insider_buy_shares, insider_shares_held)
    return _safe_div(base, _rolling_std(base, 252))

def irwt_486_lognorm_5d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 85 insider role weight over 5d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(insider_buy_shares, insider_shares_held)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def irwt_487_lognorm_21d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 85 insider role weight over 21d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(insider_buy_shares, insider_shares_held)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def irwt_488_lognorm_63d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 85 insider role weight over 63d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(insider_buy_shares, insider_shares_held)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def irwt_489_lognorm_126d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 85 insider role weight over 126d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(insider_buy_shares, insider_shares_held)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def irwt_490_lognorm_252d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 85 insider role weight over 252d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(insider_buy_shares, insider_shares_held)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def irwt_491_lvl_5d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 85 insider role weight over a 5d horizon to identify extreme regimes.
    """
    base = insider_buy_shares
    return _rolling_mean(base, 5)

def irwt_492_lvl_21d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 85 insider role weight over a 21d horizon to identify extreme regimes.
    """
    base = insider_buy_shares
    return _rolling_mean(base, 21)

def irwt_493_lvl_63d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 85 insider role weight over a 63d horizon to identify extreme regimes.
    """
    base = insider_buy_shares
    return _rolling_mean(base, 63)

def irwt_494_lvl_126d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 85 insider role weight over a 126d horizon to identify extreme regimes.
    """
    base = insider_buy_shares
    return _rolling_mean(base, 126)

def irwt_495_lvl_252d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 85 insider role weight over a 252d horizon to identify extreme regimes.
    """
    base = insider_buy_shares
    return _rolling_mean(base, 252)

def irwt_496_zscore_5d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 85 insider role weight by measuring deviations from the 5d mean.
    """
    base = insider_buy_shares
    return _zscore_rolling(base, 5)

def irwt_497_zscore_21d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 85 insider role weight by measuring deviations from the 21d mean.
    """
    base = insider_buy_shares
    return _zscore_rolling(base, 21)

def irwt_498_zscore_63d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 85 insider role weight by measuring deviations from the 63d mean.
    """
    base = insider_buy_shares
    return _zscore_rolling(base, 63)

def irwt_499_zscore_126d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 85 insider role weight by measuring deviations from the 126d mean.
    """
    base = insider_buy_shares
    return _zscore_rolling(base, 126)

def irwt_500_zscore_252d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 85 insider role weight by measuring deviations from the 252d mean.
    """
    base = insider_buy_shares
    return _zscore_rolling(base, 252)

def irwt_501_rank_5d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 85 insider role weight to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = insider_buy_shares
    return _rank_pct(base, 5)

def irwt_502_rank_21d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 85 insider role weight to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = insider_buy_shares
    return _rank_pct(base, 21)

def irwt_503_rank_63d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 85 insider role weight to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = insider_buy_shares
    return _rank_pct(base, 63)

def irwt_504_rank_126d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 85 insider role weight to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = insider_buy_shares
    return _rank_pct(base, 126)

def irwt_505_rank_252d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 85 insider role weight to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = insider_buy_shares
    return _rank_pct(base, 252)

def irwt_506_skew_5d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 85 insider role weight distribution over 5d to detect tail risk or exhaustion.
    """
    base = insider_buy_shares
    return _rolling_skew(base, 5)

def irwt_507_skew_21d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 85 insider role weight distribution over 21d to detect tail risk or exhaustion.
    """
    base = insider_buy_shares
    return _rolling_skew(base, 21)

def irwt_508_skew_63d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 85 insider role weight distribution over 63d to detect tail risk or exhaustion.
    """
    base = insider_buy_shares
    return _rolling_skew(base, 63)

def irwt_509_skew_126d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 85 insider role weight distribution over 126d to detect tail risk or exhaustion.
    """
    base = insider_buy_shares
    return _rolling_skew(base, 126)

def irwt_510_skew_252d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 85 insider role weight distribution over 252d to detect tail risk or exhaustion.
    """
    base = insider_buy_shares
    return _rolling_skew(base, 252)

def irwt_511_kurt_5d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 85 insider role weight over 5d to capture explosive breakdown or reversal points.
    """
    base = insider_buy_shares
    return _rolling_kurt(base, 5)

def irwt_512_kurt_21d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 85 insider role weight over 21d to capture explosive breakdown or reversal points.
    """
    base = insider_buy_shares
    return _rolling_kurt(base, 21)

def irwt_513_kurt_63d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 85 insider role weight over 63d to capture explosive breakdown or reversal points.
    """
    base = insider_buy_shares
    return _rolling_kurt(base, 63)

def irwt_514_kurt_126d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 85 insider role weight over 126d to capture explosive breakdown or reversal points.
    """
    base = insider_buy_shares
    return _rolling_kurt(base, 126)

def irwt_515_kurt_252d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 85 insider role weight over 252d to capture explosive breakdown or reversal points.
    """
    base = insider_buy_shares
    return _rolling_kurt(base, 252)

def irwt_516_voladj_5d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 85 insider role weight for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = insider_buy_shares
    return _safe_div(base, _rolling_std(base, 5))

def irwt_517_voladj_21d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 85 insider role weight for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = insider_buy_shares
    return _safe_div(base, _rolling_std(base, 21))

def irwt_518_voladj_63d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 85 insider role weight for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = insider_buy_shares
    return _safe_div(base, _rolling_std(base, 63))

def irwt_519_voladj_126d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 85 insider role weight for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = insider_buy_shares
    return _safe_div(base, _rolling_std(base, 126))

def irwt_520_voladj_252d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 85 insider role weight for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = insider_buy_shares
    return _safe_div(base, _rolling_std(base, 252))

def irwt_521_lognorm_5d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 85 insider role weight over 5d to stabilize variance and capture exponential shifts.
    """
    base = insider_buy_shares
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def irwt_522_lognorm_21d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 85 insider role weight over 21d to stabilize variance and capture exponential shifts.
    """
    base = insider_buy_shares
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def irwt_523_lognorm_63d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 85 insider role weight over 63d to stabilize variance and capture exponential shifts.
    """
    base = insider_buy_shares
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def irwt_524_lognorm_126d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 85 insider role weight over 126d to stabilize variance and capture exponential shifts.
    """
    base = insider_buy_shares
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def irwt_525_lognorm_252d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 85 insider role weight over 252d to stabilize variance and capture exponential shifts.
    """
    base = insider_buy_shares
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))
