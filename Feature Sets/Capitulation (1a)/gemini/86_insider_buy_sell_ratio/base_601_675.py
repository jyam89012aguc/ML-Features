"""
86_86_insider_buy_sell_ratio — Base Features 601-675
Domain: 86_insider_buy_sell_ratio
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

def ibsr_601_zscore_5d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 86 insider buy sell ratio by measuring deviations from the 5d mean.
    """
    base = insider_buy_value - insider_sell_value
    return _zscore_rolling(base, 5)

def ibsr_602_zscore_21d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 86 insider buy sell ratio by measuring deviations from the 21d mean.
    """
    base = insider_buy_value - insider_sell_value
    return _zscore_rolling(base, 21)

def ibsr_603_zscore_63d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 86 insider buy sell ratio by measuring deviations from the 63d mean.
    """
    base = insider_buy_value - insider_sell_value
    return _zscore_rolling(base, 63)

def ibsr_604_zscore_126d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 86 insider buy sell ratio by measuring deviations from the 126d mean.
    """
    base = insider_buy_value - insider_sell_value
    return _zscore_rolling(base, 126)

def ibsr_605_zscore_252d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 86 insider buy sell ratio by measuring deviations from the 252d mean.
    """
    base = insider_buy_value - insider_sell_value
    return _zscore_rolling(base, 252)

def ibsr_606_rank_5d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 86 insider buy sell ratio to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = insider_buy_value - insider_sell_value
    return _rank_pct(base, 5)

def ibsr_607_rank_21d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 86 insider buy sell ratio to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = insider_buy_value - insider_sell_value
    return _rank_pct(base, 21)

def ibsr_608_rank_63d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 86 insider buy sell ratio to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = insider_buy_value - insider_sell_value
    return _rank_pct(base, 63)

def ibsr_609_rank_126d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 86 insider buy sell ratio to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = insider_buy_value - insider_sell_value
    return _rank_pct(base, 126)

def ibsr_610_rank_252d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 86 insider buy sell ratio to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = insider_buy_value - insider_sell_value
    return _rank_pct(base, 252)

def ibsr_611_skew_5d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 86 insider buy sell ratio distribution over 5d to detect tail risk or exhaustion.
    """
    base = insider_buy_value - insider_sell_value
    return _rolling_skew(base, 5)

def ibsr_612_skew_21d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 86 insider buy sell ratio distribution over 21d to detect tail risk or exhaustion.
    """
    base = insider_buy_value - insider_sell_value
    return _rolling_skew(base, 21)

def ibsr_613_skew_63d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 86 insider buy sell ratio distribution over 63d to detect tail risk or exhaustion.
    """
    base = insider_buy_value - insider_sell_value
    return _rolling_skew(base, 63)

def ibsr_614_skew_126d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 86 insider buy sell ratio distribution over 126d to detect tail risk or exhaustion.
    """
    base = insider_buy_value - insider_sell_value
    return _rolling_skew(base, 126)

def ibsr_615_skew_252d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 86 insider buy sell ratio distribution over 252d to detect tail risk or exhaustion.
    """
    base = insider_buy_value - insider_sell_value
    return _rolling_skew(base, 252)

def ibsr_616_kurt_5d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 86 insider buy sell ratio over 5d to capture explosive breakdown or reversal points.
    """
    base = insider_buy_value - insider_sell_value
    return _rolling_kurt(base, 5)

def ibsr_617_kurt_21d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 86 insider buy sell ratio over 21d to capture explosive breakdown or reversal points.
    """
    base = insider_buy_value - insider_sell_value
    return _rolling_kurt(base, 21)

def ibsr_618_kurt_63d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 86 insider buy sell ratio over 63d to capture explosive breakdown or reversal points.
    """
    base = insider_buy_value - insider_sell_value
    return _rolling_kurt(base, 63)

def ibsr_619_kurt_126d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 86 insider buy sell ratio over 126d to capture explosive breakdown or reversal points.
    """
    base = insider_buy_value - insider_sell_value
    return _rolling_kurt(base, 126)

def ibsr_620_kurt_252d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 86 insider buy sell ratio over 252d to capture explosive breakdown or reversal points.
    """
    base = insider_buy_value - insider_sell_value
    return _rolling_kurt(base, 252)

def ibsr_621_voladj_5d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 86 insider buy sell ratio for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = insider_buy_value - insider_sell_value
    return _safe_div(base, _rolling_std(base, 5))

def ibsr_622_voladj_21d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 86 insider buy sell ratio for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = insider_buy_value - insider_sell_value
    return _safe_div(base, _rolling_std(base, 21))

def ibsr_623_voladj_63d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 86 insider buy sell ratio for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = insider_buy_value - insider_sell_value
    return _safe_div(base, _rolling_std(base, 63))

def ibsr_624_voladj_126d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 86 insider buy sell ratio for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = insider_buy_value - insider_sell_value
    return _safe_div(base, _rolling_std(base, 126))

def ibsr_625_voladj_252d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 86 insider buy sell ratio for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = insider_buy_value - insider_sell_value
    return _safe_div(base, _rolling_std(base, 252))

def ibsr_626_lognorm_5d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 86 insider buy sell ratio over 5d to stabilize variance and capture exponential shifts.
    """
    base = insider_buy_value - insider_sell_value
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def ibsr_627_lognorm_21d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 86 insider buy sell ratio over 21d to stabilize variance and capture exponential shifts.
    """
    base = insider_buy_value - insider_sell_value
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def ibsr_628_lognorm_63d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 86 insider buy sell ratio over 63d to stabilize variance and capture exponential shifts.
    """
    base = insider_buy_value - insider_sell_value
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def ibsr_629_lognorm_126d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 86 insider buy sell ratio over 126d to stabilize variance and capture exponential shifts.
    """
    base = insider_buy_value - insider_sell_value
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def ibsr_630_lognorm_252d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 86 insider buy sell ratio over 252d to stabilize variance and capture exponential shifts.
    """
    base = insider_buy_value - insider_sell_value
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def ibsr_631_lvl_5d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 86 insider buy sell ratio over a 5d horizon to identify extreme regimes.
    """
    base = insider_sell_value
    return _rolling_mean(base, 5)

def ibsr_632_lvl_21d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 86 insider buy sell ratio over a 21d horizon to identify extreme regimes.
    """
    base = insider_sell_value
    return _rolling_mean(base, 21)

def ibsr_633_lvl_63d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 86 insider buy sell ratio over a 63d horizon to identify extreme regimes.
    """
    base = insider_sell_value
    return _rolling_mean(base, 63)

def ibsr_634_lvl_126d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 86 insider buy sell ratio over a 126d horizon to identify extreme regimes.
    """
    base = insider_sell_value
    return _rolling_mean(base, 126)

def ibsr_635_lvl_252d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 86 insider buy sell ratio over a 252d horizon to identify extreme regimes.
    """
    base = insider_sell_value
    return _rolling_mean(base, 252)

def ibsr_636_zscore_5d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 86 insider buy sell ratio by measuring deviations from the 5d mean.
    """
    base = insider_sell_value
    return _zscore_rolling(base, 5)

def ibsr_637_zscore_21d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 86 insider buy sell ratio by measuring deviations from the 21d mean.
    """
    base = insider_sell_value
    return _zscore_rolling(base, 21)

def ibsr_638_zscore_63d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 86 insider buy sell ratio by measuring deviations from the 63d mean.
    """
    base = insider_sell_value
    return _zscore_rolling(base, 63)

def ibsr_639_zscore_126d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 86 insider buy sell ratio by measuring deviations from the 126d mean.
    """
    base = insider_sell_value
    return _zscore_rolling(base, 126)

def ibsr_640_zscore_252d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 86 insider buy sell ratio by measuring deviations from the 252d mean.
    """
    base = insider_sell_value
    return _zscore_rolling(base, 252)

def ibsr_641_rank_5d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 86 insider buy sell ratio to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = insider_sell_value
    return _rank_pct(base, 5)

def ibsr_642_rank_21d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 86 insider buy sell ratio to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = insider_sell_value
    return _rank_pct(base, 21)

def ibsr_643_rank_63d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 86 insider buy sell ratio to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = insider_sell_value
    return _rank_pct(base, 63)

def ibsr_644_rank_126d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 86 insider buy sell ratio to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = insider_sell_value
    return _rank_pct(base, 126)

def ibsr_645_rank_252d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 86 insider buy sell ratio to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = insider_sell_value
    return _rank_pct(base, 252)

def ibsr_646_skew_5d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 86 insider buy sell ratio distribution over 5d to detect tail risk or exhaustion.
    """
    base = insider_sell_value
    return _rolling_skew(base, 5)

def ibsr_647_skew_21d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 86 insider buy sell ratio distribution over 21d to detect tail risk or exhaustion.
    """
    base = insider_sell_value
    return _rolling_skew(base, 21)

def ibsr_648_skew_63d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 86 insider buy sell ratio distribution over 63d to detect tail risk or exhaustion.
    """
    base = insider_sell_value
    return _rolling_skew(base, 63)

def ibsr_649_skew_126d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 86 insider buy sell ratio distribution over 126d to detect tail risk or exhaustion.
    """
    base = insider_sell_value
    return _rolling_skew(base, 126)

def ibsr_650_skew_252d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 86 insider buy sell ratio distribution over 252d to detect tail risk or exhaustion.
    """
    base = insider_sell_value
    return _rolling_skew(base, 252)

def ibsr_651_kurt_5d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 86 insider buy sell ratio over 5d to capture explosive breakdown or reversal points.
    """
    base = insider_sell_value
    return _rolling_kurt(base, 5)

def ibsr_652_kurt_21d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 86 insider buy sell ratio over 21d to capture explosive breakdown or reversal points.
    """
    base = insider_sell_value
    return _rolling_kurt(base, 21)

def ibsr_653_kurt_63d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 86 insider buy sell ratio over 63d to capture explosive breakdown or reversal points.
    """
    base = insider_sell_value
    return _rolling_kurt(base, 63)

def ibsr_654_kurt_126d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 86 insider buy sell ratio over 126d to capture explosive breakdown or reversal points.
    """
    base = insider_sell_value
    return _rolling_kurt(base, 126)

def ibsr_655_kurt_252d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 86 insider buy sell ratio over 252d to capture explosive breakdown or reversal points.
    """
    base = insider_sell_value
    return _rolling_kurt(base, 252)

def ibsr_656_voladj_5d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 86 insider buy sell ratio for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = insider_sell_value
    return _safe_div(base, _rolling_std(base, 5))

def ibsr_657_voladj_21d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 86 insider buy sell ratio for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = insider_sell_value
    return _safe_div(base, _rolling_std(base, 21))

def ibsr_658_voladj_63d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 86 insider buy sell ratio for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = insider_sell_value
    return _safe_div(base, _rolling_std(base, 63))

def ibsr_659_voladj_126d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 86 insider buy sell ratio for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = insider_sell_value
    return _safe_div(base, _rolling_std(base, 126))

def ibsr_660_voladj_252d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 86 insider buy sell ratio for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = insider_sell_value
    return _safe_div(base, _rolling_std(base, 252))

def ibsr_661_lognorm_5d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 86 insider buy sell ratio over 5d to stabilize variance and capture exponential shifts.
    """
    base = insider_sell_value
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def ibsr_662_lognorm_21d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 86 insider buy sell ratio over 21d to stabilize variance and capture exponential shifts.
    """
    base = insider_sell_value
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def ibsr_663_lognorm_63d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 86 insider buy sell ratio over 63d to stabilize variance and capture exponential shifts.
    """
    base = insider_sell_value
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def ibsr_664_lognorm_126d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 86 insider buy sell ratio over 126d to stabilize variance and capture exponential shifts.
    """
    base = insider_sell_value
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def ibsr_665_lognorm_252d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 86 insider buy sell ratio over 252d to stabilize variance and capture exponential shifts.
    """
    base = insider_sell_value
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def ibsr_666_lvl_5d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 86 insider buy sell ratio over a 5d horizon to identify extreme regimes.
    """
    base = _safe_div(insider_sell_shares, insider_shares_held)
    return _rolling_mean(base, 5)

def ibsr_667_lvl_21d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 86 insider buy sell ratio over a 21d horizon to identify extreme regimes.
    """
    base = _safe_div(insider_sell_shares, insider_shares_held)
    return _rolling_mean(base, 21)

def ibsr_668_lvl_63d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 86 insider buy sell ratio over a 63d horizon to identify extreme regimes.
    """
    base = _safe_div(insider_sell_shares, insider_shares_held)
    return _rolling_mean(base, 63)

def ibsr_669_lvl_126d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 86 insider buy sell ratio over a 126d horizon to identify extreme regimes.
    """
    base = _safe_div(insider_sell_shares, insider_shares_held)
    return _rolling_mean(base, 126)

def ibsr_670_lvl_252d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 86 insider buy sell ratio over a 252d horizon to identify extreme regimes.
    """
    base = _safe_div(insider_sell_shares, insider_shares_held)
    return _rolling_mean(base, 252)

def ibsr_671_zscore_5d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 86 insider buy sell ratio by measuring deviations from the 5d mean.
    """
    base = _safe_div(insider_sell_shares, insider_shares_held)
    return _zscore_rolling(base, 5)

def ibsr_672_zscore_21d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 86 insider buy sell ratio by measuring deviations from the 21d mean.
    """
    base = _safe_div(insider_sell_shares, insider_shares_held)
    return _zscore_rolling(base, 21)

def ibsr_673_zscore_63d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 86 insider buy sell ratio by measuring deviations from the 63d mean.
    """
    base = _safe_div(insider_sell_shares, insider_shares_held)
    return _zscore_rolling(base, 63)

def ibsr_674_zscore_126d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 86 insider buy sell ratio by measuring deviations from the 126d mean.
    """
    base = _safe_div(insider_sell_shares, insider_shares_held)
    return _zscore_rolling(base, 126)

def ibsr_675_zscore_252d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 86 insider buy sell ratio by measuring deviations from the 252d mean.
    """
    base = _safe_div(insider_sell_shares, insider_shares_held)
    return _zscore_rolling(base, 252)
