"""
89_89_insider_conviction — Base Features 451-525
Domain: 89_insider_conviction
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

def icn_451_lognorm_5d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 89 insider conviction over 5d to stabilize variance and capture exponential shifts.
    """
    base = ceo_buy_value + cfo_buy_value
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def icn_452_lognorm_21d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 89 insider conviction over 21d to stabilize variance and capture exponential shifts.
    """
    base = ceo_buy_value + cfo_buy_value
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def icn_453_lognorm_63d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 89 insider conviction over 63d to stabilize variance and capture exponential shifts.
    """
    base = ceo_buy_value + cfo_buy_value
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def icn_454_lognorm_126d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 89 insider conviction over 126d to stabilize variance and capture exponential shifts.
    """
    base = ceo_buy_value + cfo_buy_value
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def icn_455_lognorm_252d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 89 insider conviction over 252d to stabilize variance and capture exponential shifts.
    """
    base = ceo_buy_value + cfo_buy_value
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def icn_456_lvl_5d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 89 insider conviction over a 5d horizon to identify extreme regimes.
    """
    base = _safe_div(insider_buy_shares, insider_shares_held)
    return _rolling_mean(base, 5)

def icn_457_lvl_21d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 89 insider conviction over a 21d horizon to identify extreme regimes.
    """
    base = _safe_div(insider_buy_shares, insider_shares_held)
    return _rolling_mean(base, 21)

def icn_458_lvl_63d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 89 insider conviction over a 63d horizon to identify extreme regimes.
    """
    base = _safe_div(insider_buy_shares, insider_shares_held)
    return _rolling_mean(base, 63)

def icn_459_lvl_126d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 89 insider conviction over a 126d horizon to identify extreme regimes.
    """
    base = _safe_div(insider_buy_shares, insider_shares_held)
    return _rolling_mean(base, 126)

def icn_460_lvl_252d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 89 insider conviction over a 252d horizon to identify extreme regimes.
    """
    base = _safe_div(insider_buy_shares, insider_shares_held)
    return _rolling_mean(base, 252)

def icn_461_zscore_5d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 89 insider conviction by measuring deviations from the 5d mean.
    """
    base = _safe_div(insider_buy_shares, insider_shares_held)
    return _zscore_rolling(base, 5)

def icn_462_zscore_21d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 89 insider conviction by measuring deviations from the 21d mean.
    """
    base = _safe_div(insider_buy_shares, insider_shares_held)
    return _zscore_rolling(base, 21)

def icn_463_zscore_63d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 89 insider conviction by measuring deviations from the 63d mean.
    """
    base = _safe_div(insider_buy_shares, insider_shares_held)
    return _zscore_rolling(base, 63)

def icn_464_zscore_126d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 89 insider conviction by measuring deviations from the 126d mean.
    """
    base = _safe_div(insider_buy_shares, insider_shares_held)
    return _zscore_rolling(base, 126)

def icn_465_zscore_252d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 89 insider conviction by measuring deviations from the 252d mean.
    """
    base = _safe_div(insider_buy_shares, insider_shares_held)
    return _zscore_rolling(base, 252)

def icn_466_rank_5d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 89 insider conviction to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = _safe_div(insider_buy_shares, insider_shares_held)
    return _rank_pct(base, 5)

def icn_467_rank_21d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 89 insider conviction to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = _safe_div(insider_buy_shares, insider_shares_held)
    return _rank_pct(base, 21)

def icn_468_rank_63d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 89 insider conviction to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = _safe_div(insider_buy_shares, insider_shares_held)
    return _rank_pct(base, 63)

def icn_469_rank_126d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 89 insider conviction to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = _safe_div(insider_buy_shares, insider_shares_held)
    return _rank_pct(base, 126)

def icn_470_rank_252d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 89 insider conviction to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = _safe_div(insider_buy_shares, insider_shares_held)
    return _rank_pct(base, 252)

def icn_471_skew_5d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 89 insider conviction distribution over 5d to detect tail risk or exhaustion.
    """
    base = _safe_div(insider_buy_shares, insider_shares_held)
    return _rolling_skew(base, 5)

def icn_472_skew_21d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 89 insider conviction distribution over 21d to detect tail risk or exhaustion.
    """
    base = _safe_div(insider_buy_shares, insider_shares_held)
    return _rolling_skew(base, 21)

def icn_473_skew_63d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 89 insider conviction distribution over 63d to detect tail risk or exhaustion.
    """
    base = _safe_div(insider_buy_shares, insider_shares_held)
    return _rolling_skew(base, 63)

def icn_474_skew_126d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 89 insider conviction distribution over 126d to detect tail risk or exhaustion.
    """
    base = _safe_div(insider_buy_shares, insider_shares_held)
    return _rolling_skew(base, 126)

def icn_475_skew_252d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 89 insider conviction distribution over 252d to detect tail risk or exhaustion.
    """
    base = _safe_div(insider_buy_shares, insider_shares_held)
    return _rolling_skew(base, 252)

def icn_476_kurt_5d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 89 insider conviction over 5d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(insider_buy_shares, insider_shares_held)
    return _rolling_kurt(base, 5)

def icn_477_kurt_21d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 89 insider conviction over 21d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(insider_buy_shares, insider_shares_held)
    return _rolling_kurt(base, 21)

def icn_478_kurt_63d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 89 insider conviction over 63d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(insider_buy_shares, insider_shares_held)
    return _rolling_kurt(base, 63)

def icn_479_kurt_126d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 89 insider conviction over 126d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(insider_buy_shares, insider_shares_held)
    return _rolling_kurt(base, 126)

def icn_480_kurt_252d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 89 insider conviction over 252d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(insider_buy_shares, insider_shares_held)
    return _rolling_kurt(base, 252)

def icn_481_voladj_5d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 89 insider conviction for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(insider_buy_shares, insider_shares_held)
    return _safe_div(base, _rolling_std(base, 5))

def icn_482_voladj_21d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 89 insider conviction for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(insider_buy_shares, insider_shares_held)
    return _safe_div(base, _rolling_std(base, 21))

def icn_483_voladj_63d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 89 insider conviction for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(insider_buy_shares, insider_shares_held)
    return _safe_div(base, _rolling_std(base, 63))

def icn_484_voladj_126d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 89 insider conviction for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(insider_buy_shares, insider_shares_held)
    return _safe_div(base, _rolling_std(base, 126))

def icn_485_voladj_252d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 89 insider conviction for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(insider_buy_shares, insider_shares_held)
    return _safe_div(base, _rolling_std(base, 252))

def icn_486_lognorm_5d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 89 insider conviction over 5d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(insider_buy_shares, insider_shares_held)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def icn_487_lognorm_21d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 89 insider conviction over 21d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(insider_buy_shares, insider_shares_held)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def icn_488_lognorm_63d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 89 insider conviction over 63d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(insider_buy_shares, insider_shares_held)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def icn_489_lognorm_126d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 89 insider conviction over 126d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(insider_buy_shares, insider_shares_held)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def icn_490_lognorm_252d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 89 insider conviction over 252d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(insider_buy_shares, insider_shares_held)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def icn_491_lvl_5d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 89 insider conviction over a 5d horizon to identify extreme regimes.
    """
    base = insider_buy_shares
    return _rolling_mean(base, 5)

def icn_492_lvl_21d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 89 insider conviction over a 21d horizon to identify extreme regimes.
    """
    base = insider_buy_shares
    return _rolling_mean(base, 21)

def icn_493_lvl_63d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 89 insider conviction over a 63d horizon to identify extreme regimes.
    """
    base = insider_buy_shares
    return _rolling_mean(base, 63)

def icn_494_lvl_126d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 89 insider conviction over a 126d horizon to identify extreme regimes.
    """
    base = insider_buy_shares
    return _rolling_mean(base, 126)

def icn_495_lvl_252d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 89 insider conviction over a 252d horizon to identify extreme regimes.
    """
    base = insider_buy_shares
    return _rolling_mean(base, 252)

def icn_496_zscore_5d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 89 insider conviction by measuring deviations from the 5d mean.
    """
    base = insider_buy_shares
    return _zscore_rolling(base, 5)

def icn_497_zscore_21d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 89 insider conviction by measuring deviations from the 21d mean.
    """
    base = insider_buy_shares
    return _zscore_rolling(base, 21)

def icn_498_zscore_63d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 89 insider conviction by measuring deviations from the 63d mean.
    """
    base = insider_buy_shares
    return _zscore_rolling(base, 63)

def icn_499_zscore_126d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 89 insider conviction by measuring deviations from the 126d mean.
    """
    base = insider_buy_shares
    return _zscore_rolling(base, 126)

def icn_500_zscore_252d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 89 insider conviction by measuring deviations from the 252d mean.
    """
    base = insider_buy_shares
    return _zscore_rolling(base, 252)

def icn_501_rank_5d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 89 insider conviction to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = insider_buy_shares
    return _rank_pct(base, 5)

def icn_502_rank_21d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 89 insider conviction to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = insider_buy_shares
    return _rank_pct(base, 21)

def icn_503_rank_63d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 89 insider conviction to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = insider_buy_shares
    return _rank_pct(base, 63)

def icn_504_rank_126d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 89 insider conviction to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = insider_buy_shares
    return _rank_pct(base, 126)

def icn_505_rank_252d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 89 insider conviction to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = insider_buy_shares
    return _rank_pct(base, 252)

def icn_506_skew_5d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 89 insider conviction distribution over 5d to detect tail risk or exhaustion.
    """
    base = insider_buy_shares
    return _rolling_skew(base, 5)

def icn_507_skew_21d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 89 insider conviction distribution over 21d to detect tail risk or exhaustion.
    """
    base = insider_buy_shares
    return _rolling_skew(base, 21)

def icn_508_skew_63d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 89 insider conviction distribution over 63d to detect tail risk or exhaustion.
    """
    base = insider_buy_shares
    return _rolling_skew(base, 63)

def icn_509_skew_126d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 89 insider conviction distribution over 126d to detect tail risk or exhaustion.
    """
    base = insider_buy_shares
    return _rolling_skew(base, 126)

def icn_510_skew_252d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 89 insider conviction distribution over 252d to detect tail risk or exhaustion.
    """
    base = insider_buy_shares
    return _rolling_skew(base, 252)

def icn_511_kurt_5d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 89 insider conviction over 5d to capture explosive breakdown or reversal points.
    """
    base = insider_buy_shares
    return _rolling_kurt(base, 5)

def icn_512_kurt_21d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 89 insider conviction over 21d to capture explosive breakdown or reversal points.
    """
    base = insider_buy_shares
    return _rolling_kurt(base, 21)

def icn_513_kurt_63d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 89 insider conviction over 63d to capture explosive breakdown or reversal points.
    """
    base = insider_buy_shares
    return _rolling_kurt(base, 63)

def icn_514_kurt_126d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 89 insider conviction over 126d to capture explosive breakdown or reversal points.
    """
    base = insider_buy_shares
    return _rolling_kurt(base, 126)

def icn_515_kurt_252d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 89 insider conviction over 252d to capture explosive breakdown or reversal points.
    """
    base = insider_buy_shares
    return _rolling_kurt(base, 252)

def icn_516_voladj_5d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 89 insider conviction for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = insider_buy_shares
    return _safe_div(base, _rolling_std(base, 5))

def icn_517_voladj_21d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 89 insider conviction for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = insider_buy_shares
    return _safe_div(base, _rolling_std(base, 21))

def icn_518_voladj_63d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 89 insider conviction for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = insider_buy_shares
    return _safe_div(base, _rolling_std(base, 63))

def icn_519_voladj_126d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 89 insider conviction for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = insider_buy_shares
    return _safe_div(base, _rolling_std(base, 126))

def icn_520_voladj_252d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 89 insider conviction for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = insider_buy_shares
    return _safe_div(base, _rolling_std(base, 252))

def icn_521_lognorm_5d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 89 insider conviction over 5d to stabilize variance and capture exponential shifts.
    """
    base = insider_buy_shares
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def icn_522_lognorm_21d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 89 insider conviction over 21d to stabilize variance and capture exponential shifts.
    """
    base = insider_buy_shares
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def icn_523_lognorm_63d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 89 insider conviction over 63d to stabilize variance and capture exponential shifts.
    """
    base = insider_buy_shares
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def icn_524_lognorm_126d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 89 insider conviction over 126d to stabilize variance and capture exponential shifts.
    """
    base = insider_buy_shares
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def icn_525_lognorm_252d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 89 insider conviction over 252d to stabilize variance and capture exponential shifts.
    """
    base = insider_buy_shares
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))
