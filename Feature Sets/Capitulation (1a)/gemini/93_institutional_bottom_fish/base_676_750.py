"""
93_93_institutional_bottom_fish — Base Features 676-750
Domain: 93_institutional_bottom_fish
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

def ibf_676_rank_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 93 institutional bottom fish to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = inst_buy_value + inst_sell_value
    return _rank_pct(base, 5)

def ibf_677_rank_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 93 institutional bottom fish to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = inst_buy_value + inst_sell_value
    return _rank_pct(base, 21)

def ibf_678_rank_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 93 institutional bottom fish to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = inst_buy_value + inst_sell_value
    return _rank_pct(base, 63)

def ibf_679_rank_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 93 institutional bottom fish to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = inst_buy_value + inst_sell_value
    return _rank_pct(base, 126)

def ibf_680_rank_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 93 institutional bottom fish to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = inst_buy_value + inst_sell_value
    return _rank_pct(base, 252)

def ibf_681_skew_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 93 institutional bottom fish distribution over 5d to detect tail risk or exhaustion.
    """
    base = inst_buy_value + inst_sell_value
    return _rolling_skew(base, 5)

def ibf_682_skew_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 93 institutional bottom fish distribution over 21d to detect tail risk or exhaustion.
    """
    base = inst_buy_value + inst_sell_value
    return _rolling_skew(base, 21)

def ibf_683_skew_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 93 institutional bottom fish distribution over 63d to detect tail risk or exhaustion.
    """
    base = inst_buy_value + inst_sell_value
    return _rolling_skew(base, 63)

def ibf_684_skew_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 93 institutional bottom fish distribution over 126d to detect tail risk or exhaustion.
    """
    base = inst_buy_value + inst_sell_value
    return _rolling_skew(base, 126)

def ibf_685_skew_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 93 institutional bottom fish distribution over 252d to detect tail risk or exhaustion.
    """
    base = inst_buy_value + inst_sell_value
    return _rolling_skew(base, 252)

def ibf_686_kurt_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 93 institutional bottom fish over 5d to capture explosive breakdown or reversal points.
    """
    base = inst_buy_value + inst_sell_value
    return _rolling_kurt(base, 5)

def ibf_687_kurt_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 93 institutional bottom fish over 21d to capture explosive breakdown or reversal points.
    """
    base = inst_buy_value + inst_sell_value
    return _rolling_kurt(base, 21)

def ibf_688_kurt_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 93 institutional bottom fish over 63d to capture explosive breakdown or reversal points.
    """
    base = inst_buy_value + inst_sell_value
    return _rolling_kurt(base, 63)

def ibf_689_kurt_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 93 institutional bottom fish over 126d to capture explosive breakdown or reversal points.
    """
    base = inst_buy_value + inst_sell_value
    return _rolling_kurt(base, 126)

def ibf_690_kurt_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 93 institutional bottom fish over 252d to capture explosive breakdown or reversal points.
    """
    base = inst_buy_value + inst_sell_value
    return _rolling_kurt(base, 252)

def ibf_691_voladj_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 93 institutional bottom fish for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = inst_buy_value + inst_sell_value
    return _safe_div(base, _rolling_std(base, 5))

def ibf_692_voladj_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 93 institutional bottom fish for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = inst_buy_value + inst_sell_value
    return _safe_div(base, _rolling_std(base, 21))

def ibf_693_voladj_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 93 institutional bottom fish for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = inst_buy_value + inst_sell_value
    return _safe_div(base, _rolling_std(base, 63))

def ibf_694_voladj_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 93 institutional bottom fish for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = inst_buy_value + inst_sell_value
    return _safe_div(base, _rolling_std(base, 126))

def ibf_695_voladj_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 93 institutional bottom fish for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = inst_buy_value + inst_sell_value
    return _safe_div(base, _rolling_std(base, 252))

def ibf_696_lognorm_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 93 institutional bottom fish over 5d to stabilize variance and capture exponential shifts.
    """
    base = inst_buy_value + inst_sell_value
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def ibf_697_lognorm_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 93 institutional bottom fish over 21d to stabilize variance and capture exponential shifts.
    """
    base = inst_buy_value + inst_sell_value
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def ibf_698_lognorm_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 93 institutional bottom fish over 63d to stabilize variance and capture exponential shifts.
    """
    base = inst_buy_value + inst_sell_value
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def ibf_699_lognorm_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 93 institutional bottom fish over 126d to stabilize variance and capture exponential shifts.
    """
    base = inst_buy_value + inst_sell_value
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def ibf_700_lognorm_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 93 institutional bottom fish over 252d to stabilize variance and capture exponential shifts.
    """
    base = inst_buy_value + inst_sell_value
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def ibf_701_lvl_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 93 institutional bottom fish over a 5d horizon to identify extreme regimes.
    """
    base = inst_buy_value
    return _rolling_mean(base, 5)

def ibf_702_lvl_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 93 institutional bottom fish over a 21d horizon to identify extreme regimes.
    """
    base = inst_buy_value
    return _rolling_mean(base, 21)

def ibf_703_lvl_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 93 institutional bottom fish over a 63d horizon to identify extreme regimes.
    """
    base = inst_buy_value
    return _rolling_mean(base, 63)

def ibf_704_lvl_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 93 institutional bottom fish over a 126d horizon to identify extreme regimes.
    """
    base = inst_buy_value
    return _rolling_mean(base, 126)

def ibf_705_lvl_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 93 institutional bottom fish over a 252d horizon to identify extreme regimes.
    """
    base = inst_buy_value
    return _rolling_mean(base, 252)

def ibf_706_zscore_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 93 institutional bottom fish by measuring deviations from the 5d mean.
    """
    base = inst_buy_value
    return _zscore_rolling(base, 5)

def ibf_707_zscore_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 93 institutional bottom fish by measuring deviations from the 21d mean.
    """
    base = inst_buy_value
    return _zscore_rolling(base, 21)

def ibf_708_zscore_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 93 institutional bottom fish by measuring deviations from the 63d mean.
    """
    base = inst_buy_value
    return _zscore_rolling(base, 63)

def ibf_709_zscore_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 93 institutional bottom fish by measuring deviations from the 126d mean.
    """
    base = inst_buy_value
    return _zscore_rolling(base, 126)

def ibf_710_zscore_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 93 institutional bottom fish by measuring deviations from the 252d mean.
    """
    base = inst_buy_value
    return _zscore_rolling(base, 252)

def ibf_711_rank_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 93 institutional bottom fish to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = inst_buy_value
    return _rank_pct(base, 5)

def ibf_712_rank_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 93 institutional bottom fish to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = inst_buy_value
    return _rank_pct(base, 21)

def ibf_713_rank_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 93 institutional bottom fish to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = inst_buy_value
    return _rank_pct(base, 63)

def ibf_714_rank_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 93 institutional bottom fish to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = inst_buy_value
    return _rank_pct(base, 126)

def ibf_715_rank_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 93 institutional bottom fish to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = inst_buy_value
    return _rank_pct(base, 252)

def ibf_716_skew_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 93 institutional bottom fish distribution over 5d to detect tail risk or exhaustion.
    """
    base = inst_buy_value
    return _rolling_skew(base, 5)

def ibf_717_skew_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 93 institutional bottom fish distribution over 21d to detect tail risk or exhaustion.
    """
    base = inst_buy_value
    return _rolling_skew(base, 21)

def ibf_718_skew_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 93 institutional bottom fish distribution over 63d to detect tail risk or exhaustion.
    """
    base = inst_buy_value
    return _rolling_skew(base, 63)

def ibf_719_skew_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 93 institutional bottom fish distribution over 126d to detect tail risk or exhaustion.
    """
    base = inst_buy_value
    return _rolling_skew(base, 126)

def ibf_720_skew_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 93 institutional bottom fish distribution over 252d to detect tail risk or exhaustion.
    """
    base = inst_buy_value
    return _rolling_skew(base, 252)

def ibf_721_kurt_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 93 institutional bottom fish over 5d to capture explosive breakdown or reversal points.
    """
    base = inst_buy_value
    return _rolling_kurt(base, 5)

def ibf_722_kurt_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 93 institutional bottom fish over 21d to capture explosive breakdown or reversal points.
    """
    base = inst_buy_value
    return _rolling_kurt(base, 21)

def ibf_723_kurt_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 93 institutional bottom fish over 63d to capture explosive breakdown or reversal points.
    """
    base = inst_buy_value
    return _rolling_kurt(base, 63)

def ibf_724_kurt_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 93 institutional bottom fish over 126d to capture explosive breakdown or reversal points.
    """
    base = inst_buy_value
    return _rolling_kurt(base, 126)

def ibf_725_kurt_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 93 institutional bottom fish over 252d to capture explosive breakdown or reversal points.
    """
    base = inst_buy_value
    return _rolling_kurt(base, 252)

def ibf_726_voladj_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 93 institutional bottom fish for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = inst_buy_value
    return _safe_div(base, _rolling_std(base, 5))

def ibf_727_voladj_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 93 institutional bottom fish for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = inst_buy_value
    return _safe_div(base, _rolling_std(base, 21))

def ibf_728_voladj_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 93 institutional bottom fish for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = inst_buy_value
    return _safe_div(base, _rolling_std(base, 63))

def ibf_729_voladj_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 93 institutional bottom fish for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = inst_buy_value
    return _safe_div(base, _rolling_std(base, 126))

def ibf_730_voladj_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 93 institutional bottom fish for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = inst_buy_value
    return _safe_div(base, _rolling_std(base, 252))

def ibf_731_lognorm_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 93 institutional bottom fish over 5d to stabilize variance and capture exponential shifts.
    """
    base = inst_buy_value
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def ibf_732_lognorm_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 93 institutional bottom fish over 21d to stabilize variance and capture exponential shifts.
    """
    base = inst_buy_value
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def ibf_733_lognorm_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 93 institutional bottom fish over 63d to stabilize variance and capture exponential shifts.
    """
    base = inst_buy_value
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def ibf_734_lognorm_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 93 institutional bottom fish over 126d to stabilize variance and capture exponential shifts.
    """
    base = inst_buy_value
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def ibf_735_lognorm_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 93 institutional bottom fish over 252d to stabilize variance and capture exponential shifts.
    """
    base = inst_buy_value
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def ibf_736_lvl_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 93 institutional bottom fish over a 5d horizon to identify extreme regimes.
    """
    base = inst_sell_value
    return _rolling_mean(base, 5)

def ibf_737_lvl_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 93 institutional bottom fish over a 21d horizon to identify extreme regimes.
    """
    base = inst_sell_value
    return _rolling_mean(base, 21)

def ibf_738_lvl_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 93 institutional bottom fish over a 63d horizon to identify extreme regimes.
    """
    base = inst_sell_value
    return _rolling_mean(base, 63)

def ibf_739_lvl_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 93 institutional bottom fish over a 126d horizon to identify extreme regimes.
    """
    base = inst_sell_value
    return _rolling_mean(base, 126)

def ibf_740_lvl_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 93 institutional bottom fish over a 252d horizon to identify extreme regimes.
    """
    base = inst_sell_value
    return _rolling_mean(base, 252)

def ibf_741_zscore_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 93 institutional bottom fish by measuring deviations from the 5d mean.
    """
    base = inst_sell_value
    return _zscore_rolling(base, 5)

def ibf_742_zscore_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 93 institutional bottom fish by measuring deviations from the 21d mean.
    """
    base = inst_sell_value
    return _zscore_rolling(base, 21)

def ibf_743_zscore_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 93 institutional bottom fish by measuring deviations from the 63d mean.
    """
    base = inst_sell_value
    return _zscore_rolling(base, 63)

def ibf_744_zscore_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 93 institutional bottom fish by measuring deviations from the 126d mean.
    """
    base = inst_sell_value
    return _zscore_rolling(base, 126)

def ibf_745_zscore_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 93 institutional bottom fish by measuring deviations from the 252d mean.
    """
    base = inst_sell_value
    return _zscore_rolling(base, 252)

def ibf_746_rank_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 93 institutional bottom fish to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = inst_sell_value
    return _rank_pct(base, 5)

def ibf_747_rank_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 93 institutional bottom fish to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = inst_sell_value
    return _rank_pct(base, 21)

def ibf_748_rank_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 93 institutional bottom fish to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = inst_sell_value
    return _rank_pct(base, 63)

def ibf_749_rank_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 93 institutional bottom fish to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = inst_sell_value
    return _rank_pct(base, 126)

def ibf_750_rank_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 93 institutional bottom fish to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = inst_sell_value
    return _rank_pct(base, 252)
