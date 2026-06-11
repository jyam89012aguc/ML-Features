"""
59_59_market_impact_proxy — Base Features 676-750
Domain: 59_market_impact_proxy
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

def mimp_676_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 59 market impact proxy to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = (volume.pct_change(20).rolling(100).mean())
    return _rank_pct(base, 5)

def mimp_677_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 59 market impact proxy to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = (volume.pct_change(20).rolling(100).mean())
    return _rank_pct(base, 21)

def mimp_678_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 59 market impact proxy to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = (volume.pct_change(20).rolling(100).mean())
    return _rank_pct(base, 63)

def mimp_679_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 59 market impact proxy to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = (volume.pct_change(20).rolling(100).mean())
    return _rank_pct(base, 126)

def mimp_680_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 59 market impact proxy to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = (volume.pct_change(20).rolling(100).mean())
    return _rank_pct(base, 252)

def mimp_681_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 59 market impact proxy distribution over 5d to detect tail risk or exhaustion.
    """
    base = (volume.pct_change(20).rolling(100).mean())
    return _rolling_skew(base, 5)

def mimp_682_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 59 market impact proxy distribution over 21d to detect tail risk or exhaustion.
    """
    base = (volume.pct_change(20).rolling(100).mean())
    return _rolling_skew(base, 21)

def mimp_683_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 59 market impact proxy distribution over 63d to detect tail risk or exhaustion.
    """
    base = (volume.pct_change(20).rolling(100).mean())
    return _rolling_skew(base, 63)

def mimp_684_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 59 market impact proxy distribution over 126d to detect tail risk or exhaustion.
    """
    base = (volume.pct_change(20).rolling(100).mean())
    return _rolling_skew(base, 126)

def mimp_685_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 59 market impact proxy distribution over 252d to detect tail risk or exhaustion.
    """
    base = (volume.pct_change(20).rolling(100).mean())
    return _rolling_skew(base, 252)

def mimp_686_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 59 market impact proxy over 5d to capture explosive breakdown or reversal points.
    """
    base = (volume.pct_change(20).rolling(100).mean())
    return _rolling_kurt(base, 5)

def mimp_687_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 59 market impact proxy over 21d to capture explosive breakdown or reversal points.
    """
    base = (volume.pct_change(20).rolling(100).mean())
    return _rolling_kurt(base, 21)

def mimp_688_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 59 market impact proxy over 63d to capture explosive breakdown or reversal points.
    """
    base = (volume.pct_change(20).rolling(100).mean())
    return _rolling_kurt(base, 63)

def mimp_689_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 59 market impact proxy over 126d to capture explosive breakdown or reversal points.
    """
    base = (volume.pct_change(20).rolling(100).mean())
    return _rolling_kurt(base, 126)

def mimp_690_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 59 market impact proxy over 252d to capture explosive breakdown or reversal points.
    """
    base = (volume.pct_change(20).rolling(100).mean())
    return _rolling_kurt(base, 252)

def mimp_691_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 59 market impact proxy for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = (volume.pct_change(20).rolling(100).mean())
    return _safe_div(base, _rolling_std(base, 5))

def mimp_692_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 59 market impact proxy for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = (volume.pct_change(20).rolling(100).mean())
    return _safe_div(base, _rolling_std(base, 21))

def mimp_693_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 59 market impact proxy for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = (volume.pct_change(20).rolling(100).mean())
    return _safe_div(base, _rolling_std(base, 63))

def mimp_694_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 59 market impact proxy for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = (volume.pct_change(20).rolling(100).mean())
    return _safe_div(base, _rolling_std(base, 126))

def mimp_695_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 59 market impact proxy for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = (volume.pct_change(20).rolling(100).mean())
    return _safe_div(base, _rolling_std(base, 252))

def mimp_696_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 59 market impact proxy over 5d to stabilize variance and capture exponential shifts.
    """
    base = (volume.pct_change(20).rolling(100).mean())
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def mimp_697_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 59 market impact proxy over 21d to stabilize variance and capture exponential shifts.
    """
    base = (volume.pct_change(20).rolling(100).mean())
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def mimp_698_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 59 market impact proxy over 63d to stabilize variance and capture exponential shifts.
    """
    base = (volume.pct_change(20).rolling(100).mean())
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def mimp_699_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 59 market impact proxy over 126d to stabilize variance and capture exponential shifts.
    """
    base = (volume.pct_change(20).rolling(100).mean())
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def mimp_700_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 59 market impact proxy over 252d to stabilize variance and capture exponential shifts.
    """
    base = (volume.pct_change(20).rolling(100).mean())
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def mimp_701_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 59 market impact proxy over a 5d horizon to identify extreme regimes.
    """
    base = (volume.pct_change(21).rolling(105).mean())
    return _rolling_mean(base, 5)

def mimp_702_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 59 market impact proxy over a 21d horizon to identify extreme regimes.
    """
    base = (volume.pct_change(21).rolling(105).mean())
    return _rolling_mean(base, 21)

def mimp_703_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 59 market impact proxy over a 63d horizon to identify extreme regimes.
    """
    base = (volume.pct_change(21).rolling(105).mean())
    return _rolling_mean(base, 63)

def mimp_704_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 59 market impact proxy over a 126d horizon to identify extreme regimes.
    """
    base = (volume.pct_change(21).rolling(105).mean())
    return _rolling_mean(base, 126)

def mimp_705_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 59 market impact proxy over a 252d horizon to identify extreme regimes.
    """
    base = (volume.pct_change(21).rolling(105).mean())
    return _rolling_mean(base, 252)

def mimp_706_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 59 market impact proxy by measuring deviations from the 5d mean.
    """
    base = (volume.pct_change(21).rolling(105).mean())
    return _zscore_rolling(base, 5)

def mimp_707_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 59 market impact proxy by measuring deviations from the 21d mean.
    """
    base = (volume.pct_change(21).rolling(105).mean())
    return _zscore_rolling(base, 21)

def mimp_708_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 59 market impact proxy by measuring deviations from the 63d mean.
    """
    base = (volume.pct_change(21).rolling(105).mean())
    return _zscore_rolling(base, 63)

def mimp_709_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 59 market impact proxy by measuring deviations from the 126d mean.
    """
    base = (volume.pct_change(21).rolling(105).mean())
    return _zscore_rolling(base, 126)

def mimp_710_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 59 market impact proxy by measuring deviations from the 252d mean.
    """
    base = (volume.pct_change(21).rolling(105).mean())
    return _zscore_rolling(base, 252)

def mimp_711_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 59 market impact proxy to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = (volume.pct_change(21).rolling(105).mean())
    return _rank_pct(base, 5)

def mimp_712_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 59 market impact proxy to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = (volume.pct_change(21).rolling(105).mean())
    return _rank_pct(base, 21)

def mimp_713_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 59 market impact proxy to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = (volume.pct_change(21).rolling(105).mean())
    return _rank_pct(base, 63)

def mimp_714_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 59 market impact proxy to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = (volume.pct_change(21).rolling(105).mean())
    return _rank_pct(base, 126)

def mimp_715_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 59 market impact proxy to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = (volume.pct_change(21).rolling(105).mean())
    return _rank_pct(base, 252)

def mimp_716_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 59 market impact proxy distribution over 5d to detect tail risk or exhaustion.
    """
    base = (volume.pct_change(21).rolling(105).mean())
    return _rolling_skew(base, 5)

def mimp_717_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 59 market impact proxy distribution over 21d to detect tail risk or exhaustion.
    """
    base = (volume.pct_change(21).rolling(105).mean())
    return _rolling_skew(base, 21)

def mimp_718_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 59 market impact proxy distribution over 63d to detect tail risk or exhaustion.
    """
    base = (volume.pct_change(21).rolling(105).mean())
    return _rolling_skew(base, 63)

def mimp_719_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 59 market impact proxy distribution over 126d to detect tail risk or exhaustion.
    """
    base = (volume.pct_change(21).rolling(105).mean())
    return _rolling_skew(base, 126)

def mimp_720_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 59 market impact proxy distribution over 252d to detect tail risk or exhaustion.
    """
    base = (volume.pct_change(21).rolling(105).mean())
    return _rolling_skew(base, 252)

def mimp_721_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 59 market impact proxy over 5d to capture explosive breakdown or reversal points.
    """
    base = (volume.pct_change(21).rolling(105).mean())
    return _rolling_kurt(base, 5)

def mimp_722_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 59 market impact proxy over 21d to capture explosive breakdown or reversal points.
    """
    base = (volume.pct_change(21).rolling(105).mean())
    return _rolling_kurt(base, 21)

def mimp_723_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 59 market impact proxy over 63d to capture explosive breakdown or reversal points.
    """
    base = (volume.pct_change(21).rolling(105).mean())
    return _rolling_kurt(base, 63)

def mimp_724_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 59 market impact proxy over 126d to capture explosive breakdown or reversal points.
    """
    base = (volume.pct_change(21).rolling(105).mean())
    return _rolling_kurt(base, 126)

def mimp_725_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 59 market impact proxy over 252d to capture explosive breakdown or reversal points.
    """
    base = (volume.pct_change(21).rolling(105).mean())
    return _rolling_kurt(base, 252)

def mimp_726_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 59 market impact proxy for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = (volume.pct_change(21).rolling(105).mean())
    return _safe_div(base, _rolling_std(base, 5))

def mimp_727_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 59 market impact proxy for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = (volume.pct_change(21).rolling(105).mean())
    return _safe_div(base, _rolling_std(base, 21))

def mimp_728_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 59 market impact proxy for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = (volume.pct_change(21).rolling(105).mean())
    return _safe_div(base, _rolling_std(base, 63))

def mimp_729_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 59 market impact proxy for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = (volume.pct_change(21).rolling(105).mean())
    return _safe_div(base, _rolling_std(base, 126))

def mimp_730_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 59 market impact proxy for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = (volume.pct_change(21).rolling(105).mean())
    return _safe_div(base, _rolling_std(base, 252))

def mimp_731_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 59 market impact proxy over 5d to stabilize variance and capture exponential shifts.
    """
    base = (volume.pct_change(21).rolling(105).mean())
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def mimp_732_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 59 market impact proxy over 21d to stabilize variance and capture exponential shifts.
    """
    base = (volume.pct_change(21).rolling(105).mean())
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def mimp_733_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 59 market impact proxy over 63d to stabilize variance and capture exponential shifts.
    """
    base = (volume.pct_change(21).rolling(105).mean())
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def mimp_734_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 59 market impact proxy over 126d to stabilize variance and capture exponential shifts.
    """
    base = (volume.pct_change(21).rolling(105).mean())
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def mimp_735_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 59 market impact proxy over 252d to stabilize variance and capture exponential shifts.
    """
    base = (volume.pct_change(21).rolling(105).mean())
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def mimp_736_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 59 market impact proxy over a 5d horizon to identify extreme regimes.
    """
    base = (volume.pct_change(22).rolling(110).mean())
    return _rolling_mean(base, 5)

def mimp_737_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 59 market impact proxy over a 21d horizon to identify extreme regimes.
    """
    base = (volume.pct_change(22).rolling(110).mean())
    return _rolling_mean(base, 21)

def mimp_738_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 59 market impact proxy over a 63d horizon to identify extreme regimes.
    """
    base = (volume.pct_change(22).rolling(110).mean())
    return _rolling_mean(base, 63)

def mimp_739_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 59 market impact proxy over a 126d horizon to identify extreme regimes.
    """
    base = (volume.pct_change(22).rolling(110).mean())
    return _rolling_mean(base, 126)

def mimp_740_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 59 market impact proxy over a 252d horizon to identify extreme regimes.
    """
    base = (volume.pct_change(22).rolling(110).mean())
    return _rolling_mean(base, 252)

def mimp_741_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 59 market impact proxy by measuring deviations from the 5d mean.
    """
    base = (volume.pct_change(22).rolling(110).mean())
    return _zscore_rolling(base, 5)

def mimp_742_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 59 market impact proxy by measuring deviations from the 21d mean.
    """
    base = (volume.pct_change(22).rolling(110).mean())
    return _zscore_rolling(base, 21)

def mimp_743_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 59 market impact proxy by measuring deviations from the 63d mean.
    """
    base = (volume.pct_change(22).rolling(110).mean())
    return _zscore_rolling(base, 63)

def mimp_744_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 59 market impact proxy by measuring deviations from the 126d mean.
    """
    base = (volume.pct_change(22).rolling(110).mean())
    return _zscore_rolling(base, 126)

def mimp_745_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 59 market impact proxy by measuring deviations from the 252d mean.
    """
    base = (volume.pct_change(22).rolling(110).mean())
    return _zscore_rolling(base, 252)

def mimp_746_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 59 market impact proxy to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = (volume.pct_change(22).rolling(110).mean())
    return _rank_pct(base, 5)

def mimp_747_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 59 market impact proxy to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = (volume.pct_change(22).rolling(110).mean())
    return _rank_pct(base, 21)

def mimp_748_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 59 market impact proxy to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = (volume.pct_change(22).rolling(110).mean())
    return _rank_pct(base, 63)

def mimp_749_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 59 market impact proxy to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = (volume.pct_change(22).rolling(110).mean())
    return _rank_pct(base, 126)

def mimp_750_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 59 market impact proxy to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = (volume.pct_change(22).rolling(110).mean())
    return _rank_pct(base, 252)
