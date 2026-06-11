"""
90_90_insider_silence — Base Features 301-375
Domain: 90_insider_silence
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

def isil_301_kurt_5d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 90 insider silence over 5d to capture explosive breakdown or reversal points.
    """
    base = insider_sell_value
    return _rolling_kurt(base, 5)

def isil_302_kurt_21d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 90 insider silence over 21d to capture explosive breakdown or reversal points.
    """
    base = insider_sell_value
    return _rolling_kurt(base, 21)

def isil_303_kurt_63d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 90 insider silence over 63d to capture explosive breakdown or reversal points.
    """
    base = insider_sell_value
    return _rolling_kurt(base, 63)

def isil_304_kurt_126d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 90 insider silence over 126d to capture explosive breakdown or reversal points.
    """
    base = insider_sell_value
    return _rolling_kurt(base, 126)

def isil_305_kurt_252d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 90 insider silence over 252d to capture explosive breakdown or reversal points.
    """
    base = insider_sell_value
    return _rolling_kurt(base, 252)

def isil_306_voladj_5d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 90 insider silence for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = insider_sell_value
    return _safe_div(base, _rolling_std(base, 5))

def isil_307_voladj_21d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 90 insider silence for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = insider_sell_value
    return _safe_div(base, _rolling_std(base, 21))

def isil_308_voladj_63d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 90 insider silence for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = insider_sell_value
    return _safe_div(base, _rolling_std(base, 63))

def isil_309_voladj_126d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 90 insider silence for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = insider_sell_value
    return _safe_div(base, _rolling_std(base, 126))

def isil_310_voladj_252d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 90 insider silence for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = insider_sell_value
    return _safe_div(base, _rolling_std(base, 252))

def isil_311_lognorm_5d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 90 insider silence over 5d to stabilize variance and capture exponential shifts.
    """
    base = insider_sell_value
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def isil_312_lognorm_21d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 90 insider silence over 21d to stabilize variance and capture exponential shifts.
    """
    base = insider_sell_value
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def isil_313_lognorm_63d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 90 insider silence over 63d to stabilize variance and capture exponential shifts.
    """
    base = insider_sell_value
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def isil_314_lognorm_126d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 90 insider silence over 126d to stabilize variance and capture exponential shifts.
    """
    base = insider_sell_value
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def isil_315_lognorm_252d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 90 insider silence over 252d to stabilize variance and capture exponential shifts.
    """
    base = insider_sell_value
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def isil_316_lvl_5d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 90 insider silence over a 5d horizon to identify extreme regimes.
    """
    base = _safe_div(insider_sell_shares, insider_shares_held)
    return _rolling_mean(base, 5)

def isil_317_lvl_21d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 90 insider silence over a 21d horizon to identify extreme regimes.
    """
    base = _safe_div(insider_sell_shares, insider_shares_held)
    return _rolling_mean(base, 21)

def isil_318_lvl_63d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 90 insider silence over a 63d horizon to identify extreme regimes.
    """
    base = _safe_div(insider_sell_shares, insider_shares_held)
    return _rolling_mean(base, 63)

def isil_319_lvl_126d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 90 insider silence over a 126d horizon to identify extreme regimes.
    """
    base = _safe_div(insider_sell_shares, insider_shares_held)
    return _rolling_mean(base, 126)

def isil_320_lvl_252d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 90 insider silence over a 252d horizon to identify extreme regimes.
    """
    base = _safe_div(insider_sell_shares, insider_shares_held)
    return _rolling_mean(base, 252)

def isil_321_zscore_5d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 90 insider silence by measuring deviations from the 5d mean.
    """
    base = _safe_div(insider_sell_shares, insider_shares_held)
    return _zscore_rolling(base, 5)

def isil_322_zscore_21d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 90 insider silence by measuring deviations from the 21d mean.
    """
    base = _safe_div(insider_sell_shares, insider_shares_held)
    return _zscore_rolling(base, 21)

def isil_323_zscore_63d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 90 insider silence by measuring deviations from the 63d mean.
    """
    base = _safe_div(insider_sell_shares, insider_shares_held)
    return _zscore_rolling(base, 63)

def isil_324_zscore_126d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 90 insider silence by measuring deviations from the 126d mean.
    """
    base = _safe_div(insider_sell_shares, insider_shares_held)
    return _zscore_rolling(base, 126)

def isil_325_zscore_252d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 90 insider silence by measuring deviations from the 252d mean.
    """
    base = _safe_div(insider_sell_shares, insider_shares_held)
    return _zscore_rolling(base, 252)

def isil_326_rank_5d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 90 insider silence to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = _safe_div(insider_sell_shares, insider_shares_held)
    return _rank_pct(base, 5)

def isil_327_rank_21d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 90 insider silence to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = _safe_div(insider_sell_shares, insider_shares_held)
    return _rank_pct(base, 21)

def isil_328_rank_63d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 90 insider silence to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = _safe_div(insider_sell_shares, insider_shares_held)
    return _rank_pct(base, 63)

def isil_329_rank_126d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 90 insider silence to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = _safe_div(insider_sell_shares, insider_shares_held)
    return _rank_pct(base, 126)

def isil_330_rank_252d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 90 insider silence to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = _safe_div(insider_sell_shares, insider_shares_held)
    return _rank_pct(base, 252)

def isil_331_skew_5d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 90 insider silence distribution over 5d to detect tail risk or exhaustion.
    """
    base = _safe_div(insider_sell_shares, insider_shares_held)
    return _rolling_skew(base, 5)

def isil_332_skew_21d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 90 insider silence distribution over 21d to detect tail risk or exhaustion.
    """
    base = _safe_div(insider_sell_shares, insider_shares_held)
    return _rolling_skew(base, 21)

def isil_333_skew_63d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 90 insider silence distribution over 63d to detect tail risk or exhaustion.
    """
    base = _safe_div(insider_sell_shares, insider_shares_held)
    return _rolling_skew(base, 63)

def isil_334_skew_126d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 90 insider silence distribution over 126d to detect tail risk or exhaustion.
    """
    base = _safe_div(insider_sell_shares, insider_shares_held)
    return _rolling_skew(base, 126)

def isil_335_skew_252d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 90 insider silence distribution over 252d to detect tail risk or exhaustion.
    """
    base = _safe_div(insider_sell_shares, insider_shares_held)
    return _rolling_skew(base, 252)

def isil_336_kurt_5d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 90 insider silence over 5d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(insider_sell_shares, insider_shares_held)
    return _rolling_kurt(base, 5)

def isil_337_kurt_21d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 90 insider silence over 21d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(insider_sell_shares, insider_shares_held)
    return _rolling_kurt(base, 21)

def isil_338_kurt_63d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 90 insider silence over 63d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(insider_sell_shares, insider_shares_held)
    return _rolling_kurt(base, 63)

def isil_339_kurt_126d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 90 insider silence over 126d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(insider_sell_shares, insider_shares_held)
    return _rolling_kurt(base, 126)

def isil_340_kurt_252d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 90 insider silence over 252d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(insider_sell_shares, insider_shares_held)
    return _rolling_kurt(base, 252)

def isil_341_voladj_5d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 90 insider silence for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(insider_sell_shares, insider_shares_held)
    return _safe_div(base, _rolling_std(base, 5))

def isil_342_voladj_21d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 90 insider silence for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(insider_sell_shares, insider_shares_held)
    return _safe_div(base, _rolling_std(base, 21))

def isil_343_voladj_63d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 90 insider silence for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(insider_sell_shares, insider_shares_held)
    return _safe_div(base, _rolling_std(base, 63))

def isil_344_voladj_126d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 90 insider silence for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(insider_sell_shares, insider_shares_held)
    return _safe_div(base, _rolling_std(base, 126))

def isil_345_voladj_252d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 90 insider silence for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(insider_sell_shares, insider_shares_held)
    return _safe_div(base, _rolling_std(base, 252))

def isil_346_lognorm_5d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 90 insider silence over 5d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(insider_sell_shares, insider_shares_held)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def isil_347_lognorm_21d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 90 insider silence over 21d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(insider_sell_shares, insider_shares_held)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def isil_348_lognorm_63d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 90 insider silence over 63d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(insider_sell_shares, insider_shares_held)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def isil_349_lognorm_126d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 90 insider silence over 126d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(insider_sell_shares, insider_shares_held)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def isil_350_lognorm_252d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 90 insider silence over 252d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(insider_sell_shares, insider_shares_held)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def isil_351_lvl_5d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 90 insider silence over a 5d horizon to identify extreme regimes.
    """
    base = insider_buy_value
    return _rolling_mean(base, 5)

def isil_352_lvl_21d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 90 insider silence over a 21d horizon to identify extreme regimes.
    """
    base = insider_buy_value
    return _rolling_mean(base, 21)

def isil_353_lvl_63d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 90 insider silence over a 63d horizon to identify extreme regimes.
    """
    base = insider_buy_value
    return _rolling_mean(base, 63)

def isil_354_lvl_126d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 90 insider silence over a 126d horizon to identify extreme regimes.
    """
    base = insider_buy_value
    return _rolling_mean(base, 126)

def isil_355_lvl_252d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 90 insider silence over a 252d horizon to identify extreme regimes.
    """
    base = insider_buy_value
    return _rolling_mean(base, 252)

def isil_356_zscore_5d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 90 insider silence by measuring deviations from the 5d mean.
    """
    base = insider_buy_value
    return _zscore_rolling(base, 5)

def isil_357_zscore_21d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 90 insider silence by measuring deviations from the 21d mean.
    """
    base = insider_buy_value
    return _zscore_rolling(base, 21)

def isil_358_zscore_63d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 90 insider silence by measuring deviations from the 63d mean.
    """
    base = insider_buy_value
    return _zscore_rolling(base, 63)

def isil_359_zscore_126d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 90 insider silence by measuring deviations from the 126d mean.
    """
    base = insider_buy_value
    return _zscore_rolling(base, 126)

def isil_360_zscore_252d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 90 insider silence by measuring deviations from the 252d mean.
    """
    base = insider_buy_value
    return _zscore_rolling(base, 252)

def isil_361_rank_5d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 90 insider silence to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = insider_buy_value
    return _rank_pct(base, 5)

def isil_362_rank_21d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 90 insider silence to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = insider_buy_value
    return _rank_pct(base, 21)

def isil_363_rank_63d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 90 insider silence to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = insider_buy_value
    return _rank_pct(base, 63)

def isil_364_rank_126d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 90 insider silence to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = insider_buy_value
    return _rank_pct(base, 126)

def isil_365_rank_252d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 90 insider silence to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = insider_buy_value
    return _rank_pct(base, 252)

def isil_366_skew_5d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 90 insider silence distribution over 5d to detect tail risk or exhaustion.
    """
    base = insider_buy_value
    return _rolling_skew(base, 5)

def isil_367_skew_21d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 90 insider silence distribution over 21d to detect tail risk or exhaustion.
    """
    base = insider_buy_value
    return _rolling_skew(base, 21)

def isil_368_skew_63d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 90 insider silence distribution over 63d to detect tail risk or exhaustion.
    """
    base = insider_buy_value
    return _rolling_skew(base, 63)

def isil_369_skew_126d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 90 insider silence distribution over 126d to detect tail risk or exhaustion.
    """
    base = insider_buy_value
    return _rolling_skew(base, 126)

def isil_370_skew_252d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 90 insider silence distribution over 252d to detect tail risk or exhaustion.
    """
    base = insider_buy_value
    return _rolling_skew(base, 252)

def isil_371_kurt_5d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 90 insider silence over 5d to capture explosive breakdown or reversal points.
    """
    base = insider_buy_value
    return _rolling_kurt(base, 5)

def isil_372_kurt_21d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 90 insider silence over 21d to capture explosive breakdown or reversal points.
    """
    base = insider_buy_value
    return _rolling_kurt(base, 21)

def isil_373_kurt_63d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 90 insider silence over 63d to capture explosive breakdown or reversal points.
    """
    base = insider_buy_value
    return _rolling_kurt(base, 63)

def isil_374_kurt_126d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 90 insider silence over 126d to capture explosive breakdown or reversal points.
    """
    base = insider_buy_value
    return _rolling_kurt(base, 126)

def isil_375_kurt_252d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 90 insider silence over 252d to capture explosive breakdown or reversal points.
    """
    base = insider_buy_value
    return _rolling_kurt(base, 252)
