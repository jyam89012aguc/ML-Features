"""
92_92_ownership_concentration — Base Features 601-675
Domain: 92_ownership_concentration
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

def ocon_601_zscore_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 92 ownership concentration by measuring deviations from the 5d mean.
    """
    base = _safe_div(inst_buy_value, inst_shares_held)
    return _zscore_rolling(base, 5)

def ocon_602_zscore_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 92 ownership concentration by measuring deviations from the 21d mean.
    """
    base = _safe_div(inst_buy_value, inst_shares_held)
    return _zscore_rolling(base, 21)

def ocon_603_zscore_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 92 ownership concentration by measuring deviations from the 63d mean.
    """
    base = _safe_div(inst_buy_value, inst_shares_held)
    return _zscore_rolling(base, 63)

def ocon_604_zscore_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 92 ownership concentration by measuring deviations from the 126d mean.
    """
    base = _safe_div(inst_buy_value, inst_shares_held)
    return _zscore_rolling(base, 126)

def ocon_605_zscore_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 92 ownership concentration by measuring deviations from the 252d mean.
    """
    base = _safe_div(inst_buy_value, inst_shares_held)
    return _zscore_rolling(base, 252)

def ocon_606_rank_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 92 ownership concentration to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = _safe_div(inst_buy_value, inst_shares_held)
    return _rank_pct(base, 5)

def ocon_607_rank_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 92 ownership concentration to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = _safe_div(inst_buy_value, inst_shares_held)
    return _rank_pct(base, 21)

def ocon_608_rank_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 92 ownership concentration to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = _safe_div(inst_buy_value, inst_shares_held)
    return _rank_pct(base, 63)

def ocon_609_rank_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 92 ownership concentration to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = _safe_div(inst_buy_value, inst_shares_held)
    return _rank_pct(base, 126)

def ocon_610_rank_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 92 ownership concentration to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = _safe_div(inst_buy_value, inst_shares_held)
    return _rank_pct(base, 252)

def ocon_611_skew_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 92 ownership concentration distribution over 5d to detect tail risk or exhaustion.
    """
    base = _safe_div(inst_buy_value, inst_shares_held)
    return _rolling_skew(base, 5)

def ocon_612_skew_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 92 ownership concentration distribution over 21d to detect tail risk or exhaustion.
    """
    base = _safe_div(inst_buy_value, inst_shares_held)
    return _rolling_skew(base, 21)

def ocon_613_skew_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 92 ownership concentration distribution over 63d to detect tail risk or exhaustion.
    """
    base = _safe_div(inst_buy_value, inst_shares_held)
    return _rolling_skew(base, 63)

def ocon_614_skew_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 92 ownership concentration distribution over 126d to detect tail risk or exhaustion.
    """
    base = _safe_div(inst_buy_value, inst_shares_held)
    return _rolling_skew(base, 126)

def ocon_615_skew_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 92 ownership concentration distribution over 252d to detect tail risk or exhaustion.
    """
    base = _safe_div(inst_buy_value, inst_shares_held)
    return _rolling_skew(base, 252)

def ocon_616_kurt_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 92 ownership concentration over 5d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(inst_buy_value, inst_shares_held)
    return _rolling_kurt(base, 5)

def ocon_617_kurt_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 92 ownership concentration over 21d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(inst_buy_value, inst_shares_held)
    return _rolling_kurt(base, 21)

def ocon_618_kurt_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 92 ownership concentration over 63d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(inst_buy_value, inst_shares_held)
    return _rolling_kurt(base, 63)

def ocon_619_kurt_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 92 ownership concentration over 126d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(inst_buy_value, inst_shares_held)
    return _rolling_kurt(base, 126)

def ocon_620_kurt_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 92 ownership concentration over 252d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(inst_buy_value, inst_shares_held)
    return _rolling_kurt(base, 252)

def ocon_621_voladj_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 92 ownership concentration for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(inst_buy_value, inst_shares_held)
    return _safe_div(base, _rolling_std(base, 5))

def ocon_622_voladj_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 92 ownership concentration for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(inst_buy_value, inst_shares_held)
    return _safe_div(base, _rolling_std(base, 21))

def ocon_623_voladj_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 92 ownership concentration for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(inst_buy_value, inst_shares_held)
    return _safe_div(base, _rolling_std(base, 63))

def ocon_624_voladj_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 92 ownership concentration for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(inst_buy_value, inst_shares_held)
    return _safe_div(base, _rolling_std(base, 126))

def ocon_625_voladj_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 92 ownership concentration for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(inst_buy_value, inst_shares_held)
    return _safe_div(base, _rolling_std(base, 252))

def ocon_626_lognorm_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 92 ownership concentration over 5d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(inst_buy_value, inst_shares_held)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def ocon_627_lognorm_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 92 ownership concentration over 21d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(inst_buy_value, inst_shares_held)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def ocon_628_lognorm_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 92 ownership concentration over 63d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(inst_buy_value, inst_shares_held)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def ocon_629_lognorm_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 92 ownership concentration over 126d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(inst_buy_value, inst_shares_held)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def ocon_630_lognorm_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 92 ownership concentration over 252d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(inst_buy_value, inst_shares_held)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def ocon_631_lvl_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 92 ownership concentration over a 5d horizon to identify extreme regimes.
    """
    base = holder_count.diff(21).abs()
    return _rolling_mean(base, 5)

def ocon_632_lvl_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 92 ownership concentration over a 21d horizon to identify extreme regimes.
    """
    base = holder_count.diff(21).abs()
    return _rolling_mean(base, 21)

def ocon_633_lvl_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 92 ownership concentration over a 63d horizon to identify extreme regimes.
    """
    base = holder_count.diff(21).abs()
    return _rolling_mean(base, 63)

def ocon_634_lvl_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 92 ownership concentration over a 126d horizon to identify extreme regimes.
    """
    base = holder_count.diff(21).abs()
    return _rolling_mean(base, 126)

def ocon_635_lvl_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 92 ownership concentration over a 252d horizon to identify extreme regimes.
    """
    base = holder_count.diff(21).abs()
    return _rolling_mean(base, 252)

def ocon_636_zscore_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 92 ownership concentration by measuring deviations from the 5d mean.
    """
    base = holder_count.diff(21).abs()
    return _zscore_rolling(base, 5)

def ocon_637_zscore_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 92 ownership concentration by measuring deviations from the 21d mean.
    """
    base = holder_count.diff(21).abs()
    return _zscore_rolling(base, 21)

def ocon_638_zscore_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 92 ownership concentration by measuring deviations from the 63d mean.
    """
    base = holder_count.diff(21).abs()
    return _zscore_rolling(base, 63)

def ocon_639_zscore_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 92 ownership concentration by measuring deviations from the 126d mean.
    """
    base = holder_count.diff(21).abs()
    return _zscore_rolling(base, 126)

def ocon_640_zscore_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 92 ownership concentration by measuring deviations from the 252d mean.
    """
    base = holder_count.diff(21).abs()
    return _zscore_rolling(base, 252)

def ocon_641_rank_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 92 ownership concentration to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = holder_count.diff(21).abs()
    return _rank_pct(base, 5)

def ocon_642_rank_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 92 ownership concentration to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = holder_count.diff(21).abs()
    return _rank_pct(base, 21)

def ocon_643_rank_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 92 ownership concentration to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = holder_count.diff(21).abs()
    return _rank_pct(base, 63)

def ocon_644_rank_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 92 ownership concentration to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = holder_count.diff(21).abs()
    return _rank_pct(base, 126)

def ocon_645_rank_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 92 ownership concentration to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = holder_count.diff(21).abs()
    return _rank_pct(base, 252)

def ocon_646_skew_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 92 ownership concentration distribution over 5d to detect tail risk or exhaustion.
    """
    base = holder_count.diff(21).abs()
    return _rolling_skew(base, 5)

def ocon_647_skew_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 92 ownership concentration distribution over 21d to detect tail risk or exhaustion.
    """
    base = holder_count.diff(21).abs()
    return _rolling_skew(base, 21)

def ocon_648_skew_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 92 ownership concentration distribution over 63d to detect tail risk or exhaustion.
    """
    base = holder_count.diff(21).abs()
    return _rolling_skew(base, 63)

def ocon_649_skew_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 92 ownership concentration distribution over 126d to detect tail risk or exhaustion.
    """
    base = holder_count.diff(21).abs()
    return _rolling_skew(base, 126)

def ocon_650_skew_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 92 ownership concentration distribution over 252d to detect tail risk or exhaustion.
    """
    base = holder_count.diff(21).abs()
    return _rolling_skew(base, 252)

def ocon_651_kurt_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 92 ownership concentration over 5d to capture explosive breakdown or reversal points.
    """
    base = holder_count.diff(21).abs()
    return _rolling_kurt(base, 5)

def ocon_652_kurt_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 92 ownership concentration over 21d to capture explosive breakdown or reversal points.
    """
    base = holder_count.diff(21).abs()
    return _rolling_kurt(base, 21)

def ocon_653_kurt_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 92 ownership concentration over 63d to capture explosive breakdown or reversal points.
    """
    base = holder_count.diff(21).abs()
    return _rolling_kurt(base, 63)

def ocon_654_kurt_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 92 ownership concentration over 126d to capture explosive breakdown or reversal points.
    """
    base = holder_count.diff(21).abs()
    return _rolling_kurt(base, 126)

def ocon_655_kurt_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 92 ownership concentration over 252d to capture explosive breakdown or reversal points.
    """
    base = holder_count.diff(21).abs()
    return _rolling_kurt(base, 252)

def ocon_656_voladj_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 92 ownership concentration for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = holder_count.diff(21).abs()
    return _safe_div(base, _rolling_std(base, 5))

def ocon_657_voladj_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 92 ownership concentration for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = holder_count.diff(21).abs()
    return _safe_div(base, _rolling_std(base, 21))

def ocon_658_voladj_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 92 ownership concentration for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = holder_count.diff(21).abs()
    return _safe_div(base, _rolling_std(base, 63))

def ocon_659_voladj_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 92 ownership concentration for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = holder_count.diff(21).abs()
    return _safe_div(base, _rolling_std(base, 126))

def ocon_660_voladj_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 92 ownership concentration for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = holder_count.diff(21).abs()
    return _safe_div(base, _rolling_std(base, 252))

def ocon_661_lognorm_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 92 ownership concentration over 5d to stabilize variance and capture exponential shifts.
    """
    base = holder_count.diff(21).abs()
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def ocon_662_lognorm_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 92 ownership concentration over 21d to stabilize variance and capture exponential shifts.
    """
    base = holder_count.diff(21).abs()
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def ocon_663_lognorm_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 92 ownership concentration over 63d to stabilize variance and capture exponential shifts.
    """
    base = holder_count.diff(21).abs()
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def ocon_664_lognorm_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 92 ownership concentration over 126d to stabilize variance and capture exponential shifts.
    """
    base = holder_count.diff(21).abs()
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def ocon_665_lognorm_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 92 ownership concentration over 252d to stabilize variance and capture exponential shifts.
    """
    base = holder_count.diff(21).abs()
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def ocon_666_lvl_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 92 ownership concentration over a 5d horizon to identify extreme regimes.
    """
    base = inst_buy_value + inst_sell_value
    return _rolling_mean(base, 5)

def ocon_667_lvl_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 92 ownership concentration over a 21d horizon to identify extreme regimes.
    """
    base = inst_buy_value + inst_sell_value
    return _rolling_mean(base, 21)

def ocon_668_lvl_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 92 ownership concentration over a 63d horizon to identify extreme regimes.
    """
    base = inst_buy_value + inst_sell_value
    return _rolling_mean(base, 63)

def ocon_669_lvl_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 92 ownership concentration over a 126d horizon to identify extreme regimes.
    """
    base = inst_buy_value + inst_sell_value
    return _rolling_mean(base, 126)

def ocon_670_lvl_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 92 ownership concentration over a 252d horizon to identify extreme regimes.
    """
    base = inst_buy_value + inst_sell_value
    return _rolling_mean(base, 252)

def ocon_671_zscore_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 92 ownership concentration by measuring deviations from the 5d mean.
    """
    base = inst_buy_value + inst_sell_value
    return _zscore_rolling(base, 5)

def ocon_672_zscore_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 92 ownership concentration by measuring deviations from the 21d mean.
    """
    base = inst_buy_value + inst_sell_value
    return _zscore_rolling(base, 21)

def ocon_673_zscore_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 92 ownership concentration by measuring deviations from the 63d mean.
    """
    base = inst_buy_value + inst_sell_value
    return _zscore_rolling(base, 63)

def ocon_674_zscore_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 92 ownership concentration by measuring deviations from the 126d mean.
    """
    base = inst_buy_value + inst_sell_value
    return _zscore_rolling(base, 126)

def ocon_675_zscore_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 92 ownership concentration by measuring deviations from the 252d mean.
    """
    base = inst_buy_value + inst_sell_value
    return _zscore_rolling(base, 252)
