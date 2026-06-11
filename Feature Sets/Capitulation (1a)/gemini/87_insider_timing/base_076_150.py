"""
87_87_insider_timing — Base Features 076-150
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

def itm_076_zscore_5d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 87 insider timing by measuring deviations from the 5d mean.
    """
    base = ceo_buy_value + cfo_buy_value
    return _zscore_rolling(base, 5)

def itm_077_zscore_21d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 87 insider timing by measuring deviations from the 21d mean.
    """
    base = ceo_buy_value + cfo_buy_value
    return _zscore_rolling(base, 21)

def itm_078_zscore_63d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 87 insider timing by measuring deviations from the 63d mean.
    """
    base = ceo_buy_value + cfo_buy_value
    return _zscore_rolling(base, 63)

def itm_079_zscore_126d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 87 insider timing by measuring deviations from the 126d mean.
    """
    base = ceo_buy_value + cfo_buy_value
    return _zscore_rolling(base, 126)

def itm_080_zscore_252d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 87 insider timing by measuring deviations from the 252d mean.
    """
    base = ceo_buy_value + cfo_buy_value
    return _zscore_rolling(base, 252)

def itm_081_rank_5d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 87 insider timing to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = ceo_buy_value + cfo_buy_value
    return _rank_pct(base, 5)

def itm_082_rank_21d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 87 insider timing to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = ceo_buy_value + cfo_buy_value
    return _rank_pct(base, 21)

def itm_083_rank_63d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 87 insider timing to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = ceo_buy_value + cfo_buy_value
    return _rank_pct(base, 63)

def itm_084_rank_126d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 87 insider timing to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = ceo_buy_value + cfo_buy_value
    return _rank_pct(base, 126)

def itm_085_rank_252d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 87 insider timing to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = ceo_buy_value + cfo_buy_value
    return _rank_pct(base, 252)

def itm_086_skew_5d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 87 insider timing distribution over 5d to detect tail risk or exhaustion.
    """
    base = ceo_buy_value + cfo_buy_value
    return _rolling_skew(base, 5)

def itm_087_skew_21d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 87 insider timing distribution over 21d to detect tail risk or exhaustion.
    """
    base = ceo_buy_value + cfo_buy_value
    return _rolling_skew(base, 21)

def itm_088_skew_63d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 87 insider timing distribution over 63d to detect tail risk or exhaustion.
    """
    base = ceo_buy_value + cfo_buy_value
    return _rolling_skew(base, 63)

def itm_089_skew_126d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 87 insider timing distribution over 126d to detect tail risk or exhaustion.
    """
    base = ceo_buy_value + cfo_buy_value
    return _rolling_skew(base, 126)

def itm_090_skew_252d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 87 insider timing distribution over 252d to detect tail risk or exhaustion.
    """
    base = ceo_buy_value + cfo_buy_value
    return _rolling_skew(base, 252)

def itm_091_kurt_5d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 87 insider timing over 5d to capture explosive breakdown or reversal points.
    """
    base = ceo_buy_value + cfo_buy_value
    return _rolling_kurt(base, 5)

def itm_092_kurt_21d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 87 insider timing over 21d to capture explosive breakdown or reversal points.
    """
    base = ceo_buy_value + cfo_buy_value
    return _rolling_kurt(base, 21)

def itm_093_kurt_63d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 87 insider timing over 63d to capture explosive breakdown or reversal points.
    """
    base = ceo_buy_value + cfo_buy_value
    return _rolling_kurt(base, 63)

def itm_094_kurt_126d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 87 insider timing over 126d to capture explosive breakdown or reversal points.
    """
    base = ceo_buy_value + cfo_buy_value
    return _rolling_kurt(base, 126)

def itm_095_kurt_252d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 87 insider timing over 252d to capture explosive breakdown or reversal points.
    """
    base = ceo_buy_value + cfo_buy_value
    return _rolling_kurt(base, 252)

def itm_096_voladj_5d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 87 insider timing for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = ceo_buy_value + cfo_buy_value
    return _safe_div(base, _rolling_std(base, 5))

def itm_097_voladj_21d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 87 insider timing for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = ceo_buy_value + cfo_buy_value
    return _safe_div(base, _rolling_std(base, 21))

def itm_098_voladj_63d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 87 insider timing for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = ceo_buy_value + cfo_buy_value
    return _safe_div(base, _rolling_std(base, 63))

def itm_099_voladj_126d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 87 insider timing for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = ceo_buy_value + cfo_buy_value
    return _safe_div(base, _rolling_std(base, 126))

def itm_100_voladj_252d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 87 insider timing for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = ceo_buy_value + cfo_buy_value
    return _safe_div(base, _rolling_std(base, 252))

def itm_101_lognorm_5d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 87 insider timing over 5d to stabilize variance and capture exponential shifts.
    """
    base = ceo_buy_value + cfo_buy_value
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def itm_102_lognorm_21d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 87 insider timing over 21d to stabilize variance and capture exponential shifts.
    """
    base = ceo_buy_value + cfo_buy_value
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def itm_103_lognorm_63d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 87 insider timing over 63d to stabilize variance and capture exponential shifts.
    """
    base = ceo_buy_value + cfo_buy_value
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def itm_104_lognorm_126d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 87 insider timing over 126d to stabilize variance and capture exponential shifts.
    """
    base = ceo_buy_value + cfo_buy_value
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def itm_105_lognorm_252d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 87 insider timing over 252d to stabilize variance and capture exponential shifts.
    """
    base = ceo_buy_value + cfo_buy_value
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def itm_106_lvl_5d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 87 insider timing over a 5d horizon to identify extreme regimes.
    """
    base = _safe_div(insider_buy_shares, insider_shares_held)
    return _rolling_mean(base, 5)

def itm_107_lvl_21d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 87 insider timing over a 21d horizon to identify extreme regimes.
    """
    base = _safe_div(insider_buy_shares, insider_shares_held)
    return _rolling_mean(base, 21)

def itm_108_lvl_63d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 87 insider timing over a 63d horizon to identify extreme regimes.
    """
    base = _safe_div(insider_buy_shares, insider_shares_held)
    return _rolling_mean(base, 63)

def itm_109_lvl_126d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 87 insider timing over a 126d horizon to identify extreme regimes.
    """
    base = _safe_div(insider_buy_shares, insider_shares_held)
    return _rolling_mean(base, 126)

def itm_110_lvl_252d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 87 insider timing over a 252d horizon to identify extreme regimes.
    """
    base = _safe_div(insider_buy_shares, insider_shares_held)
    return _rolling_mean(base, 252)

def itm_111_zscore_5d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 87 insider timing by measuring deviations from the 5d mean.
    """
    base = _safe_div(insider_buy_shares, insider_shares_held)
    return _zscore_rolling(base, 5)

def itm_112_zscore_21d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 87 insider timing by measuring deviations from the 21d mean.
    """
    base = _safe_div(insider_buy_shares, insider_shares_held)
    return _zscore_rolling(base, 21)

def itm_113_zscore_63d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 87 insider timing by measuring deviations from the 63d mean.
    """
    base = _safe_div(insider_buy_shares, insider_shares_held)
    return _zscore_rolling(base, 63)

def itm_114_zscore_126d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 87 insider timing by measuring deviations from the 126d mean.
    """
    base = _safe_div(insider_buy_shares, insider_shares_held)
    return _zscore_rolling(base, 126)

def itm_115_zscore_252d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 87 insider timing by measuring deviations from the 252d mean.
    """
    base = _safe_div(insider_buy_shares, insider_shares_held)
    return _zscore_rolling(base, 252)

def itm_116_rank_5d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 87 insider timing to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = _safe_div(insider_buy_shares, insider_shares_held)
    return _rank_pct(base, 5)

def itm_117_rank_21d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 87 insider timing to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = _safe_div(insider_buy_shares, insider_shares_held)
    return _rank_pct(base, 21)

def itm_118_rank_63d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 87 insider timing to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = _safe_div(insider_buy_shares, insider_shares_held)
    return _rank_pct(base, 63)

def itm_119_rank_126d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 87 insider timing to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = _safe_div(insider_buy_shares, insider_shares_held)
    return _rank_pct(base, 126)

def itm_120_rank_252d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 87 insider timing to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = _safe_div(insider_buy_shares, insider_shares_held)
    return _rank_pct(base, 252)

def itm_121_skew_5d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 87 insider timing distribution over 5d to detect tail risk or exhaustion.
    """
    base = _safe_div(insider_buy_shares, insider_shares_held)
    return _rolling_skew(base, 5)

def itm_122_skew_21d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 87 insider timing distribution over 21d to detect tail risk or exhaustion.
    """
    base = _safe_div(insider_buy_shares, insider_shares_held)
    return _rolling_skew(base, 21)

def itm_123_skew_63d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 87 insider timing distribution over 63d to detect tail risk or exhaustion.
    """
    base = _safe_div(insider_buy_shares, insider_shares_held)
    return _rolling_skew(base, 63)

def itm_124_skew_126d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 87 insider timing distribution over 126d to detect tail risk or exhaustion.
    """
    base = _safe_div(insider_buy_shares, insider_shares_held)
    return _rolling_skew(base, 126)

def itm_125_skew_252d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 87 insider timing distribution over 252d to detect tail risk or exhaustion.
    """
    base = _safe_div(insider_buy_shares, insider_shares_held)
    return _rolling_skew(base, 252)

def itm_126_kurt_5d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 87 insider timing over 5d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(insider_buy_shares, insider_shares_held)
    return _rolling_kurt(base, 5)

def itm_127_kurt_21d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 87 insider timing over 21d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(insider_buy_shares, insider_shares_held)
    return _rolling_kurt(base, 21)

def itm_128_kurt_63d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 87 insider timing over 63d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(insider_buy_shares, insider_shares_held)
    return _rolling_kurt(base, 63)

def itm_129_kurt_126d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 87 insider timing over 126d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(insider_buy_shares, insider_shares_held)
    return _rolling_kurt(base, 126)

def itm_130_kurt_252d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 87 insider timing over 252d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(insider_buy_shares, insider_shares_held)
    return _rolling_kurt(base, 252)

def itm_131_voladj_5d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 87 insider timing for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(insider_buy_shares, insider_shares_held)
    return _safe_div(base, _rolling_std(base, 5))

def itm_132_voladj_21d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 87 insider timing for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(insider_buy_shares, insider_shares_held)
    return _safe_div(base, _rolling_std(base, 21))

def itm_133_voladj_63d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 87 insider timing for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(insider_buy_shares, insider_shares_held)
    return _safe_div(base, _rolling_std(base, 63))

def itm_134_voladj_126d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 87 insider timing for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(insider_buy_shares, insider_shares_held)
    return _safe_div(base, _rolling_std(base, 126))

def itm_135_voladj_252d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 87 insider timing for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(insider_buy_shares, insider_shares_held)
    return _safe_div(base, _rolling_std(base, 252))

def itm_136_lognorm_5d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 87 insider timing over 5d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(insider_buy_shares, insider_shares_held)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def itm_137_lognorm_21d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 87 insider timing over 21d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(insider_buy_shares, insider_shares_held)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def itm_138_lognorm_63d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 87 insider timing over 63d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(insider_buy_shares, insider_shares_held)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def itm_139_lognorm_126d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 87 insider timing over 126d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(insider_buy_shares, insider_shares_held)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def itm_140_lognorm_252d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 87 insider timing over 252d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(insider_buy_shares, insider_shares_held)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def itm_141_lvl_5d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 87 insider timing over a 5d horizon to identify extreme regimes.
    """
    base = insider_buy_shares
    return _rolling_mean(base, 5)

def itm_142_lvl_21d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 87 insider timing over a 21d horizon to identify extreme regimes.
    """
    base = insider_buy_shares
    return _rolling_mean(base, 21)

def itm_143_lvl_63d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 87 insider timing over a 63d horizon to identify extreme regimes.
    """
    base = insider_buy_shares
    return _rolling_mean(base, 63)

def itm_144_lvl_126d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 87 insider timing over a 126d horizon to identify extreme regimes.
    """
    base = insider_buy_shares
    return _rolling_mean(base, 126)

def itm_145_lvl_252d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 87 insider timing over a 252d horizon to identify extreme regimes.
    """
    base = insider_buy_shares
    return _rolling_mean(base, 252)

def itm_146_zscore_5d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 87 insider timing by measuring deviations from the 5d mean.
    """
    base = insider_buy_shares
    return _zscore_rolling(base, 5)

def itm_147_zscore_21d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 87 insider timing by measuring deviations from the 21d mean.
    """
    base = insider_buy_shares
    return _zscore_rolling(base, 21)

def itm_148_zscore_63d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 87 insider timing by measuring deviations from the 63d mean.
    """
    base = insider_buy_shares
    return _zscore_rolling(base, 63)

def itm_149_zscore_126d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 87 insider timing by measuring deviations from the 126d mean.
    """
    base = insider_buy_shares
    return _zscore_rolling(base, 126)

def itm_150_zscore_252d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 87 insider timing by measuring deviations from the 252d mean.
    """
    base = insider_buy_shares
    return _zscore_rolling(base, 252)
