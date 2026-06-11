"""
94_94_holder_count_dynamics — Base Features 601-675
Domain: 94_holder_count_dynamics
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

def hcd_601_zscore_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 94 holder count dynamics by measuring deviations from the 5d mean.
    """
    base = _safe_div(inst_buy_value, inst_shares_held)
    return _zscore_rolling(base, 5)

def hcd_602_zscore_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 94 holder count dynamics by measuring deviations from the 21d mean.
    """
    base = _safe_div(inst_buy_value, inst_shares_held)
    return _zscore_rolling(base, 21)

def hcd_603_zscore_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 94 holder count dynamics by measuring deviations from the 63d mean.
    """
    base = _safe_div(inst_buy_value, inst_shares_held)
    return _zscore_rolling(base, 63)

def hcd_604_zscore_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 94 holder count dynamics by measuring deviations from the 126d mean.
    """
    base = _safe_div(inst_buy_value, inst_shares_held)
    return _zscore_rolling(base, 126)

def hcd_605_zscore_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 94 holder count dynamics by measuring deviations from the 252d mean.
    """
    base = _safe_div(inst_buy_value, inst_shares_held)
    return _zscore_rolling(base, 252)

def hcd_606_rank_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 94 holder count dynamics to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = _safe_div(inst_buy_value, inst_shares_held)
    return _rank_pct(base, 5)

def hcd_607_rank_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 94 holder count dynamics to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = _safe_div(inst_buy_value, inst_shares_held)
    return _rank_pct(base, 21)

def hcd_608_rank_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 94 holder count dynamics to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = _safe_div(inst_buy_value, inst_shares_held)
    return _rank_pct(base, 63)

def hcd_609_rank_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 94 holder count dynamics to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = _safe_div(inst_buy_value, inst_shares_held)
    return _rank_pct(base, 126)

def hcd_610_rank_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 94 holder count dynamics to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = _safe_div(inst_buy_value, inst_shares_held)
    return _rank_pct(base, 252)

def hcd_611_skew_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 94 holder count dynamics distribution over 5d to detect tail risk or exhaustion.
    """
    base = _safe_div(inst_buy_value, inst_shares_held)
    return _rolling_skew(base, 5)

def hcd_612_skew_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 94 holder count dynamics distribution over 21d to detect tail risk or exhaustion.
    """
    base = _safe_div(inst_buy_value, inst_shares_held)
    return _rolling_skew(base, 21)

def hcd_613_skew_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 94 holder count dynamics distribution over 63d to detect tail risk or exhaustion.
    """
    base = _safe_div(inst_buy_value, inst_shares_held)
    return _rolling_skew(base, 63)

def hcd_614_skew_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 94 holder count dynamics distribution over 126d to detect tail risk or exhaustion.
    """
    base = _safe_div(inst_buy_value, inst_shares_held)
    return _rolling_skew(base, 126)

def hcd_615_skew_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 94 holder count dynamics distribution over 252d to detect tail risk or exhaustion.
    """
    base = _safe_div(inst_buy_value, inst_shares_held)
    return _rolling_skew(base, 252)

def hcd_616_kurt_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 94 holder count dynamics over 5d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(inst_buy_value, inst_shares_held)
    return _rolling_kurt(base, 5)

def hcd_617_kurt_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 94 holder count dynamics over 21d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(inst_buy_value, inst_shares_held)
    return _rolling_kurt(base, 21)

def hcd_618_kurt_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 94 holder count dynamics over 63d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(inst_buy_value, inst_shares_held)
    return _rolling_kurt(base, 63)

def hcd_619_kurt_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 94 holder count dynamics over 126d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(inst_buy_value, inst_shares_held)
    return _rolling_kurt(base, 126)

def hcd_620_kurt_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 94 holder count dynamics over 252d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(inst_buy_value, inst_shares_held)
    return _rolling_kurt(base, 252)

def hcd_621_voladj_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 94 holder count dynamics for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(inst_buy_value, inst_shares_held)
    return _safe_div(base, _rolling_std(base, 5))

def hcd_622_voladj_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 94 holder count dynamics for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(inst_buy_value, inst_shares_held)
    return _safe_div(base, _rolling_std(base, 21))

def hcd_623_voladj_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 94 holder count dynamics for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(inst_buy_value, inst_shares_held)
    return _safe_div(base, _rolling_std(base, 63))

def hcd_624_voladj_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 94 holder count dynamics for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(inst_buy_value, inst_shares_held)
    return _safe_div(base, _rolling_std(base, 126))

def hcd_625_voladj_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 94 holder count dynamics for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(inst_buy_value, inst_shares_held)
    return _safe_div(base, _rolling_std(base, 252))

def hcd_626_lognorm_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 94 holder count dynamics over 5d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(inst_buy_value, inst_shares_held)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def hcd_627_lognorm_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 94 holder count dynamics over 21d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(inst_buy_value, inst_shares_held)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def hcd_628_lognorm_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 94 holder count dynamics over 63d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(inst_buy_value, inst_shares_held)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def hcd_629_lognorm_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 94 holder count dynamics over 126d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(inst_buy_value, inst_shares_held)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def hcd_630_lognorm_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 94 holder count dynamics over 252d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(inst_buy_value, inst_shares_held)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def hcd_631_lvl_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 94 holder count dynamics over a 5d horizon to identify extreme regimes.
    """
    base = holder_count.diff(21).abs()
    return _rolling_mean(base, 5)

def hcd_632_lvl_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 94 holder count dynamics over a 21d horizon to identify extreme regimes.
    """
    base = holder_count.diff(21).abs()
    return _rolling_mean(base, 21)

def hcd_633_lvl_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 94 holder count dynamics over a 63d horizon to identify extreme regimes.
    """
    base = holder_count.diff(21).abs()
    return _rolling_mean(base, 63)

def hcd_634_lvl_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 94 holder count dynamics over a 126d horizon to identify extreme regimes.
    """
    base = holder_count.diff(21).abs()
    return _rolling_mean(base, 126)

def hcd_635_lvl_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 94 holder count dynamics over a 252d horizon to identify extreme regimes.
    """
    base = holder_count.diff(21).abs()
    return _rolling_mean(base, 252)

def hcd_636_zscore_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 94 holder count dynamics by measuring deviations from the 5d mean.
    """
    base = holder_count.diff(21).abs()
    return _zscore_rolling(base, 5)

def hcd_637_zscore_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 94 holder count dynamics by measuring deviations from the 21d mean.
    """
    base = holder_count.diff(21).abs()
    return _zscore_rolling(base, 21)

def hcd_638_zscore_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 94 holder count dynamics by measuring deviations from the 63d mean.
    """
    base = holder_count.diff(21).abs()
    return _zscore_rolling(base, 63)

def hcd_639_zscore_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 94 holder count dynamics by measuring deviations from the 126d mean.
    """
    base = holder_count.diff(21).abs()
    return _zscore_rolling(base, 126)

def hcd_640_zscore_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 94 holder count dynamics by measuring deviations from the 252d mean.
    """
    base = holder_count.diff(21).abs()
    return _zscore_rolling(base, 252)

def hcd_641_rank_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 94 holder count dynamics to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = holder_count.diff(21).abs()
    return _rank_pct(base, 5)

def hcd_642_rank_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 94 holder count dynamics to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = holder_count.diff(21).abs()
    return _rank_pct(base, 21)

def hcd_643_rank_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 94 holder count dynamics to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = holder_count.diff(21).abs()
    return _rank_pct(base, 63)

def hcd_644_rank_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 94 holder count dynamics to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = holder_count.diff(21).abs()
    return _rank_pct(base, 126)

def hcd_645_rank_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 94 holder count dynamics to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = holder_count.diff(21).abs()
    return _rank_pct(base, 252)

def hcd_646_skew_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 94 holder count dynamics distribution over 5d to detect tail risk or exhaustion.
    """
    base = holder_count.diff(21).abs()
    return _rolling_skew(base, 5)

def hcd_647_skew_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 94 holder count dynamics distribution over 21d to detect tail risk or exhaustion.
    """
    base = holder_count.diff(21).abs()
    return _rolling_skew(base, 21)

def hcd_648_skew_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 94 holder count dynamics distribution over 63d to detect tail risk or exhaustion.
    """
    base = holder_count.diff(21).abs()
    return _rolling_skew(base, 63)

def hcd_649_skew_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 94 holder count dynamics distribution over 126d to detect tail risk or exhaustion.
    """
    base = holder_count.diff(21).abs()
    return _rolling_skew(base, 126)

def hcd_650_skew_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 94 holder count dynamics distribution over 252d to detect tail risk or exhaustion.
    """
    base = holder_count.diff(21).abs()
    return _rolling_skew(base, 252)

def hcd_651_kurt_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 94 holder count dynamics over 5d to capture explosive breakdown or reversal points.
    """
    base = holder_count.diff(21).abs()
    return _rolling_kurt(base, 5)

def hcd_652_kurt_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 94 holder count dynamics over 21d to capture explosive breakdown or reversal points.
    """
    base = holder_count.diff(21).abs()
    return _rolling_kurt(base, 21)

def hcd_653_kurt_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 94 holder count dynamics over 63d to capture explosive breakdown or reversal points.
    """
    base = holder_count.diff(21).abs()
    return _rolling_kurt(base, 63)

def hcd_654_kurt_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 94 holder count dynamics over 126d to capture explosive breakdown or reversal points.
    """
    base = holder_count.diff(21).abs()
    return _rolling_kurt(base, 126)

def hcd_655_kurt_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 94 holder count dynamics over 252d to capture explosive breakdown or reversal points.
    """
    base = holder_count.diff(21).abs()
    return _rolling_kurt(base, 252)

def hcd_656_voladj_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 94 holder count dynamics for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = holder_count.diff(21).abs()
    return _safe_div(base, _rolling_std(base, 5))

def hcd_657_voladj_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 94 holder count dynamics for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = holder_count.diff(21).abs()
    return _safe_div(base, _rolling_std(base, 21))

def hcd_658_voladj_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 94 holder count dynamics for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = holder_count.diff(21).abs()
    return _safe_div(base, _rolling_std(base, 63))

def hcd_659_voladj_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 94 holder count dynamics for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = holder_count.diff(21).abs()
    return _safe_div(base, _rolling_std(base, 126))

def hcd_660_voladj_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 94 holder count dynamics for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = holder_count.diff(21).abs()
    return _safe_div(base, _rolling_std(base, 252))

def hcd_661_lognorm_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 94 holder count dynamics over 5d to stabilize variance and capture exponential shifts.
    """
    base = holder_count.diff(21).abs()
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def hcd_662_lognorm_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 94 holder count dynamics over 21d to stabilize variance and capture exponential shifts.
    """
    base = holder_count.diff(21).abs()
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def hcd_663_lognorm_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 94 holder count dynamics over 63d to stabilize variance and capture exponential shifts.
    """
    base = holder_count.diff(21).abs()
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def hcd_664_lognorm_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 94 holder count dynamics over 126d to stabilize variance and capture exponential shifts.
    """
    base = holder_count.diff(21).abs()
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def hcd_665_lognorm_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 94 holder count dynamics over 252d to stabilize variance and capture exponential shifts.
    """
    base = holder_count.diff(21).abs()
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def hcd_666_lvl_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 94 holder count dynamics over a 5d horizon to identify extreme regimes.
    """
    base = inst_buy_value + inst_sell_value
    return _rolling_mean(base, 5)

def hcd_667_lvl_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 94 holder count dynamics over a 21d horizon to identify extreme regimes.
    """
    base = inst_buy_value + inst_sell_value
    return _rolling_mean(base, 21)

def hcd_668_lvl_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 94 holder count dynamics over a 63d horizon to identify extreme regimes.
    """
    base = inst_buy_value + inst_sell_value
    return _rolling_mean(base, 63)

def hcd_669_lvl_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 94 holder count dynamics over a 126d horizon to identify extreme regimes.
    """
    base = inst_buy_value + inst_sell_value
    return _rolling_mean(base, 126)

def hcd_670_lvl_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 94 holder count dynamics over a 252d horizon to identify extreme regimes.
    """
    base = inst_buy_value + inst_sell_value
    return _rolling_mean(base, 252)

def hcd_671_zscore_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 94 holder count dynamics by measuring deviations from the 5d mean.
    """
    base = inst_buy_value + inst_sell_value
    return _zscore_rolling(base, 5)

def hcd_672_zscore_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 94 holder count dynamics by measuring deviations from the 21d mean.
    """
    base = inst_buy_value + inst_sell_value
    return _zscore_rolling(base, 21)

def hcd_673_zscore_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 94 holder count dynamics by measuring deviations from the 63d mean.
    """
    base = inst_buy_value + inst_sell_value
    return _zscore_rolling(base, 63)

def hcd_674_zscore_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 94 holder count dynamics by measuring deviations from the 126d mean.
    """
    base = inst_buy_value + inst_sell_value
    return _zscore_rolling(base, 126)

def hcd_675_zscore_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 94 holder count dynamics by measuring deviations from the 252d mean.
    """
    base = inst_buy_value + inst_sell_value
    return _zscore_rolling(base, 252)
