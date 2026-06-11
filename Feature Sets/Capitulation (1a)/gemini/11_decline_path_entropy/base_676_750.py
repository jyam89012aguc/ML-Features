"""
11_11_decline_path_entropy — Base Features 676-750
Domain: 11_decline_path_entropy
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

def dpe_676_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 11 decline path entropy to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = (close.pct_change(20).rolling(100).mean())
    return _rank_pct(base, 5)

def dpe_677_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 11 decline path entropy to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = (close.pct_change(20).rolling(100).mean())
    return _rank_pct(base, 21)

def dpe_678_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 11 decline path entropy to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = (close.pct_change(20).rolling(100).mean())
    return _rank_pct(base, 63)

def dpe_679_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 11 decline path entropy to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = (close.pct_change(20).rolling(100).mean())
    return _rank_pct(base, 126)

def dpe_680_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 11 decline path entropy to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = (close.pct_change(20).rolling(100).mean())
    return _rank_pct(base, 252)

def dpe_681_skew_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 11 decline path entropy distribution over 5d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(20).rolling(100).mean())
    return _rolling_skew(base, 5)

def dpe_682_skew_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 11 decline path entropy distribution over 21d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(20).rolling(100).mean())
    return _rolling_skew(base, 21)

def dpe_683_skew_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 11 decline path entropy distribution over 63d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(20).rolling(100).mean())
    return _rolling_skew(base, 63)

def dpe_684_skew_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 11 decline path entropy distribution over 126d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(20).rolling(100).mean())
    return _rolling_skew(base, 126)

def dpe_685_skew_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 11 decline path entropy distribution over 252d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(20).rolling(100).mean())
    return _rolling_skew(base, 252)

def dpe_686_kurt_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 11 decline path entropy over 5d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(20).rolling(100).mean())
    return _rolling_kurt(base, 5)

def dpe_687_kurt_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 11 decline path entropy over 21d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(20).rolling(100).mean())
    return _rolling_kurt(base, 21)

def dpe_688_kurt_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 11 decline path entropy over 63d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(20).rolling(100).mean())
    return _rolling_kurt(base, 63)

def dpe_689_kurt_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 11 decline path entropy over 126d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(20).rolling(100).mean())
    return _rolling_kurt(base, 126)

def dpe_690_kurt_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 11 decline path entropy over 252d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(20).rolling(100).mean())
    return _rolling_kurt(base, 252)

def dpe_691_voladj_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 11 decline path entropy for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(20).rolling(100).mean())
    return _safe_div(base, _rolling_std(base, 5))

def dpe_692_voladj_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 11 decline path entropy for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(20).rolling(100).mean())
    return _safe_div(base, _rolling_std(base, 21))

def dpe_693_voladj_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 11 decline path entropy for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(20).rolling(100).mean())
    return _safe_div(base, _rolling_std(base, 63))

def dpe_694_voladj_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 11 decline path entropy for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(20).rolling(100).mean())
    return _safe_div(base, _rolling_std(base, 126))

def dpe_695_voladj_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 11 decline path entropy for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(20).rolling(100).mean())
    return _safe_div(base, _rolling_std(base, 252))

def dpe_696_lognorm_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 11 decline path entropy over 5d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(20).rolling(100).mean())
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def dpe_697_lognorm_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 11 decline path entropy over 21d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(20).rolling(100).mean())
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def dpe_698_lognorm_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 11 decline path entropy over 63d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(20).rolling(100).mean())
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def dpe_699_lognorm_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 11 decline path entropy over 126d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(20).rolling(100).mean())
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def dpe_700_lognorm_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 11 decline path entropy over 252d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(20).rolling(100).mean())
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def dpe_701_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 11 decline path entropy over a 5d horizon to identify extreme regimes.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return _rolling_mean(base, 5)

def dpe_702_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 11 decline path entropy over a 21d horizon to identify extreme regimes.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return _rolling_mean(base, 21)

def dpe_703_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 11 decline path entropy over a 63d horizon to identify extreme regimes.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return _rolling_mean(base, 63)

def dpe_704_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 11 decline path entropy over a 126d horizon to identify extreme regimes.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return _rolling_mean(base, 126)

def dpe_705_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 11 decline path entropy over a 252d horizon to identify extreme regimes.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return _rolling_mean(base, 252)

def dpe_706_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 11 decline path entropy by measuring deviations from the 5d mean.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return _zscore_rolling(base, 5)

def dpe_707_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 11 decline path entropy by measuring deviations from the 21d mean.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return _zscore_rolling(base, 21)

def dpe_708_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 11 decline path entropy by measuring deviations from the 63d mean.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return _zscore_rolling(base, 63)

def dpe_709_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 11 decline path entropy by measuring deviations from the 126d mean.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return _zscore_rolling(base, 126)

def dpe_710_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 11 decline path entropy by measuring deviations from the 252d mean.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return _zscore_rolling(base, 252)

def dpe_711_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 11 decline path entropy to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return _rank_pct(base, 5)

def dpe_712_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 11 decline path entropy to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return _rank_pct(base, 21)

def dpe_713_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 11 decline path entropy to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return _rank_pct(base, 63)

def dpe_714_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 11 decline path entropy to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return _rank_pct(base, 126)

def dpe_715_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 11 decline path entropy to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return _rank_pct(base, 252)

def dpe_716_skew_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 11 decline path entropy distribution over 5d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return _rolling_skew(base, 5)

def dpe_717_skew_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 11 decline path entropy distribution over 21d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return _rolling_skew(base, 21)

def dpe_718_skew_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 11 decline path entropy distribution over 63d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return _rolling_skew(base, 63)

def dpe_719_skew_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 11 decline path entropy distribution over 126d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return _rolling_skew(base, 126)

def dpe_720_skew_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 11 decline path entropy distribution over 252d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return _rolling_skew(base, 252)

def dpe_721_kurt_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 11 decline path entropy over 5d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return _rolling_kurt(base, 5)

def dpe_722_kurt_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 11 decline path entropy over 21d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return _rolling_kurt(base, 21)

def dpe_723_kurt_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 11 decline path entropy over 63d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return _rolling_kurt(base, 63)

def dpe_724_kurt_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 11 decline path entropy over 126d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return _rolling_kurt(base, 126)

def dpe_725_kurt_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 11 decline path entropy over 252d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return _rolling_kurt(base, 252)

def dpe_726_voladj_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 11 decline path entropy for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return _safe_div(base, _rolling_std(base, 5))

def dpe_727_voladj_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 11 decline path entropy for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return _safe_div(base, _rolling_std(base, 21))

def dpe_728_voladj_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 11 decline path entropy for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return _safe_div(base, _rolling_std(base, 63))

def dpe_729_voladj_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 11 decline path entropy for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return _safe_div(base, _rolling_std(base, 126))

def dpe_730_voladj_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 11 decline path entropy for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return _safe_div(base, _rolling_std(base, 252))

def dpe_731_lognorm_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 11 decline path entropy over 5d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def dpe_732_lognorm_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 11 decline path entropy over 21d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def dpe_733_lognorm_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 11 decline path entropy over 63d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def dpe_734_lognorm_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 11 decline path entropy over 126d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def dpe_735_lognorm_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 11 decline path entropy over 252d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(21).rolling(105).mean())
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def dpe_736_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 11 decline path entropy over a 5d horizon to identify extreme regimes.
    """
    base = (close.pct_change(22).rolling(110).mean())
    return _rolling_mean(base, 5)

def dpe_737_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 11 decline path entropy over a 21d horizon to identify extreme regimes.
    """
    base = (close.pct_change(22).rolling(110).mean())
    return _rolling_mean(base, 21)

def dpe_738_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 11 decline path entropy over a 63d horizon to identify extreme regimes.
    """
    base = (close.pct_change(22).rolling(110).mean())
    return _rolling_mean(base, 63)

def dpe_739_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 11 decline path entropy over a 126d horizon to identify extreme regimes.
    """
    base = (close.pct_change(22).rolling(110).mean())
    return _rolling_mean(base, 126)

def dpe_740_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 11 decline path entropy over a 252d horizon to identify extreme regimes.
    """
    base = (close.pct_change(22).rolling(110).mean())
    return _rolling_mean(base, 252)

def dpe_741_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 11 decline path entropy by measuring deviations from the 5d mean.
    """
    base = (close.pct_change(22).rolling(110).mean())
    return _zscore_rolling(base, 5)

def dpe_742_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 11 decline path entropy by measuring deviations from the 21d mean.
    """
    base = (close.pct_change(22).rolling(110).mean())
    return _zscore_rolling(base, 21)

def dpe_743_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 11 decline path entropy by measuring deviations from the 63d mean.
    """
    base = (close.pct_change(22).rolling(110).mean())
    return _zscore_rolling(base, 63)

def dpe_744_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 11 decline path entropy by measuring deviations from the 126d mean.
    """
    base = (close.pct_change(22).rolling(110).mean())
    return _zscore_rolling(base, 126)

def dpe_745_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 11 decline path entropy by measuring deviations from the 252d mean.
    """
    base = (close.pct_change(22).rolling(110).mean())
    return _zscore_rolling(base, 252)

def dpe_746_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 11 decline path entropy to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = (close.pct_change(22).rolling(110).mean())
    return _rank_pct(base, 5)

def dpe_747_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 11 decline path entropy to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = (close.pct_change(22).rolling(110).mean())
    return _rank_pct(base, 21)

def dpe_748_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 11 decline path entropy to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = (close.pct_change(22).rolling(110).mean())
    return _rank_pct(base, 63)

def dpe_749_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 11 decline path entropy to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = (close.pct_change(22).rolling(110).mean())
    return _rank_pct(base, 126)

def dpe_750_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 11 decline path entropy to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = (close.pct_change(22).rolling(110).mean())
    return _rank_pct(base, 252)
