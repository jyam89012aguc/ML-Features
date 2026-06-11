"""
87_87_insider_timing — Base Features 451-525
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

def itm_451_lognorm_5d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 87 insider timing over 5d to stabilize variance and capture exponential shifts.
    """
    base = ceo_buy_value + cfo_buy_value
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def itm_452_lognorm_21d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 87 insider timing over 21d to stabilize variance and capture exponential shifts.
    """
    base = ceo_buy_value + cfo_buy_value
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def itm_453_lognorm_63d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 87 insider timing over 63d to stabilize variance and capture exponential shifts.
    """
    base = ceo_buy_value + cfo_buy_value
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def itm_454_lognorm_126d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 87 insider timing over 126d to stabilize variance and capture exponential shifts.
    """
    base = ceo_buy_value + cfo_buy_value
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def itm_455_lognorm_252d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 87 insider timing over 252d to stabilize variance and capture exponential shifts.
    """
    base = ceo_buy_value + cfo_buy_value
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def itm_456_lvl_5d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 87 insider timing over a 5d horizon to identify extreme regimes.
    """
    base = _safe_div(insider_buy_shares, insider_shares_held)
    return _rolling_mean(base, 5)

def itm_457_lvl_21d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 87 insider timing over a 21d horizon to identify extreme regimes.
    """
    base = _safe_div(insider_buy_shares, insider_shares_held)
    return _rolling_mean(base, 21)

def itm_458_lvl_63d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 87 insider timing over a 63d horizon to identify extreme regimes.
    """
    base = _safe_div(insider_buy_shares, insider_shares_held)
    return _rolling_mean(base, 63)

def itm_459_lvl_126d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 87 insider timing over a 126d horizon to identify extreme regimes.
    """
    base = _safe_div(insider_buy_shares, insider_shares_held)
    return _rolling_mean(base, 126)

def itm_460_lvl_252d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 87 insider timing over a 252d horizon to identify extreme regimes.
    """
    base = _safe_div(insider_buy_shares, insider_shares_held)
    return _rolling_mean(base, 252)

def itm_461_zscore_5d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 87 insider timing by measuring deviations from the 5d mean.
    """
    base = _safe_div(insider_buy_shares, insider_shares_held)
    return _zscore_rolling(base, 5)

def itm_462_zscore_21d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 87 insider timing by measuring deviations from the 21d mean.
    """
    base = _safe_div(insider_buy_shares, insider_shares_held)
    return _zscore_rolling(base, 21)

def itm_463_zscore_63d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 87 insider timing by measuring deviations from the 63d mean.
    """
    base = _safe_div(insider_buy_shares, insider_shares_held)
    return _zscore_rolling(base, 63)

def itm_464_zscore_126d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 87 insider timing by measuring deviations from the 126d mean.
    """
    base = _safe_div(insider_buy_shares, insider_shares_held)
    return _zscore_rolling(base, 126)

def itm_465_zscore_252d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 87 insider timing by measuring deviations from the 252d mean.
    """
    base = _safe_div(insider_buy_shares, insider_shares_held)
    return _zscore_rolling(base, 252)

def itm_466_rank_5d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 87 insider timing to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = _safe_div(insider_buy_shares, insider_shares_held)
    return _rank_pct(base, 5)

def itm_467_rank_21d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 87 insider timing to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = _safe_div(insider_buy_shares, insider_shares_held)
    return _rank_pct(base, 21)

def itm_468_rank_63d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 87 insider timing to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = _safe_div(insider_buy_shares, insider_shares_held)
    return _rank_pct(base, 63)

def itm_469_rank_126d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 87 insider timing to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = _safe_div(insider_buy_shares, insider_shares_held)
    return _rank_pct(base, 126)

def itm_470_rank_252d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 87 insider timing to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = _safe_div(insider_buy_shares, insider_shares_held)
    return _rank_pct(base, 252)

def itm_471_skew_5d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 87 insider timing distribution over 5d to detect tail risk or exhaustion.
    """
    base = _safe_div(insider_buy_shares, insider_shares_held)
    return _rolling_skew(base, 5)

def itm_472_skew_21d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 87 insider timing distribution over 21d to detect tail risk or exhaustion.
    """
    base = _safe_div(insider_buy_shares, insider_shares_held)
    return _rolling_skew(base, 21)

def itm_473_skew_63d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 87 insider timing distribution over 63d to detect tail risk or exhaustion.
    """
    base = _safe_div(insider_buy_shares, insider_shares_held)
    return _rolling_skew(base, 63)

def itm_474_skew_126d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 87 insider timing distribution over 126d to detect tail risk or exhaustion.
    """
    base = _safe_div(insider_buy_shares, insider_shares_held)
    return _rolling_skew(base, 126)

def itm_475_skew_252d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 87 insider timing distribution over 252d to detect tail risk or exhaustion.
    """
    base = _safe_div(insider_buy_shares, insider_shares_held)
    return _rolling_skew(base, 252)

def itm_476_kurt_5d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 87 insider timing over 5d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(insider_buy_shares, insider_shares_held)
    return _rolling_kurt(base, 5)

def itm_477_kurt_21d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 87 insider timing over 21d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(insider_buy_shares, insider_shares_held)
    return _rolling_kurt(base, 21)

def itm_478_kurt_63d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 87 insider timing over 63d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(insider_buy_shares, insider_shares_held)
    return _rolling_kurt(base, 63)

def itm_479_kurt_126d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 87 insider timing over 126d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(insider_buy_shares, insider_shares_held)
    return _rolling_kurt(base, 126)

def itm_480_kurt_252d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 87 insider timing over 252d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(insider_buy_shares, insider_shares_held)
    return _rolling_kurt(base, 252)

def itm_481_voladj_5d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 87 insider timing for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(insider_buy_shares, insider_shares_held)
    return _safe_div(base, _rolling_std(base, 5))

def itm_482_voladj_21d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 87 insider timing for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(insider_buy_shares, insider_shares_held)
    return _safe_div(base, _rolling_std(base, 21))

def itm_483_voladj_63d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 87 insider timing for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(insider_buy_shares, insider_shares_held)
    return _safe_div(base, _rolling_std(base, 63))

def itm_484_voladj_126d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 87 insider timing for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(insider_buy_shares, insider_shares_held)
    return _safe_div(base, _rolling_std(base, 126))

def itm_485_voladj_252d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 87 insider timing for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(insider_buy_shares, insider_shares_held)
    return _safe_div(base, _rolling_std(base, 252))

def itm_486_lognorm_5d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 87 insider timing over 5d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(insider_buy_shares, insider_shares_held)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def itm_487_lognorm_21d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 87 insider timing over 21d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(insider_buy_shares, insider_shares_held)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def itm_488_lognorm_63d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 87 insider timing over 63d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(insider_buy_shares, insider_shares_held)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def itm_489_lognorm_126d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 87 insider timing over 126d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(insider_buy_shares, insider_shares_held)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def itm_490_lognorm_252d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 87 insider timing over 252d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(insider_buy_shares, insider_shares_held)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def itm_491_lvl_5d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 87 insider timing over a 5d horizon to identify extreme regimes.
    """
    base = insider_buy_shares
    return _rolling_mean(base, 5)

def itm_492_lvl_21d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 87 insider timing over a 21d horizon to identify extreme regimes.
    """
    base = insider_buy_shares
    return _rolling_mean(base, 21)

def itm_493_lvl_63d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 87 insider timing over a 63d horizon to identify extreme regimes.
    """
    base = insider_buy_shares
    return _rolling_mean(base, 63)

def itm_494_lvl_126d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 87 insider timing over a 126d horizon to identify extreme regimes.
    """
    base = insider_buy_shares
    return _rolling_mean(base, 126)

def itm_495_lvl_252d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 87 insider timing over a 252d horizon to identify extreme regimes.
    """
    base = insider_buy_shares
    return _rolling_mean(base, 252)

def itm_496_zscore_5d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 87 insider timing by measuring deviations from the 5d mean.
    """
    base = insider_buy_shares
    return _zscore_rolling(base, 5)

def itm_497_zscore_21d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 87 insider timing by measuring deviations from the 21d mean.
    """
    base = insider_buy_shares
    return _zscore_rolling(base, 21)

def itm_498_zscore_63d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 87 insider timing by measuring deviations from the 63d mean.
    """
    base = insider_buy_shares
    return _zscore_rolling(base, 63)

def itm_499_zscore_126d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 87 insider timing by measuring deviations from the 126d mean.
    """
    base = insider_buy_shares
    return _zscore_rolling(base, 126)

def itm_500_zscore_252d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 87 insider timing by measuring deviations from the 252d mean.
    """
    base = insider_buy_shares
    return _zscore_rolling(base, 252)

def itm_501_rank_5d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 87 insider timing to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = insider_buy_shares
    return _rank_pct(base, 5)

def itm_502_rank_21d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 87 insider timing to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = insider_buy_shares
    return _rank_pct(base, 21)

def itm_503_rank_63d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 87 insider timing to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = insider_buy_shares
    return _rank_pct(base, 63)

def itm_504_rank_126d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 87 insider timing to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = insider_buy_shares
    return _rank_pct(base, 126)

def itm_505_rank_252d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 87 insider timing to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = insider_buy_shares
    return _rank_pct(base, 252)

def itm_506_skew_5d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 87 insider timing distribution over 5d to detect tail risk or exhaustion.
    """
    base = insider_buy_shares
    return _rolling_skew(base, 5)

def itm_507_skew_21d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 87 insider timing distribution over 21d to detect tail risk or exhaustion.
    """
    base = insider_buy_shares
    return _rolling_skew(base, 21)

def itm_508_skew_63d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 87 insider timing distribution over 63d to detect tail risk or exhaustion.
    """
    base = insider_buy_shares
    return _rolling_skew(base, 63)

def itm_509_skew_126d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 87 insider timing distribution over 126d to detect tail risk or exhaustion.
    """
    base = insider_buy_shares
    return _rolling_skew(base, 126)

def itm_510_skew_252d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 87 insider timing distribution over 252d to detect tail risk or exhaustion.
    """
    base = insider_buy_shares
    return _rolling_skew(base, 252)

def itm_511_kurt_5d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 87 insider timing over 5d to capture explosive breakdown or reversal points.
    """
    base = insider_buy_shares
    return _rolling_kurt(base, 5)

def itm_512_kurt_21d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 87 insider timing over 21d to capture explosive breakdown or reversal points.
    """
    base = insider_buy_shares
    return _rolling_kurt(base, 21)

def itm_513_kurt_63d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 87 insider timing over 63d to capture explosive breakdown or reversal points.
    """
    base = insider_buy_shares
    return _rolling_kurt(base, 63)

def itm_514_kurt_126d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 87 insider timing over 126d to capture explosive breakdown or reversal points.
    """
    base = insider_buy_shares
    return _rolling_kurt(base, 126)

def itm_515_kurt_252d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 87 insider timing over 252d to capture explosive breakdown or reversal points.
    """
    base = insider_buy_shares
    return _rolling_kurt(base, 252)

def itm_516_voladj_5d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 87 insider timing for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = insider_buy_shares
    return _safe_div(base, _rolling_std(base, 5))

def itm_517_voladj_21d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 87 insider timing for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = insider_buy_shares
    return _safe_div(base, _rolling_std(base, 21))

def itm_518_voladj_63d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 87 insider timing for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = insider_buy_shares
    return _safe_div(base, _rolling_std(base, 63))

def itm_519_voladj_126d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 87 insider timing for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = insider_buy_shares
    return _safe_div(base, _rolling_std(base, 126))

def itm_520_voladj_252d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 87 insider timing for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = insider_buy_shares
    return _safe_div(base, _rolling_std(base, 252))

def itm_521_lognorm_5d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 87 insider timing over 5d to stabilize variance and capture exponential shifts.
    """
    base = insider_buy_shares
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def itm_522_lognorm_21d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 87 insider timing over 21d to stabilize variance and capture exponential shifts.
    """
    base = insider_buy_shares
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def itm_523_lognorm_63d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 87 insider timing over 63d to stabilize variance and capture exponential shifts.
    """
    base = insider_buy_shares
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def itm_524_lognorm_126d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 87 insider timing over 126d to stabilize variance and capture exponential shifts.
    """
    base = insider_buy_shares
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def itm_525_lognorm_252d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 87 insider timing over 252d to stabilize variance and capture exponential shifts.
    """
    base = insider_buy_shares
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))
