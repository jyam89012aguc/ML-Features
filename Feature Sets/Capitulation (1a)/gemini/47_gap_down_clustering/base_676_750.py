"""
47_47_gap_down_clustering — Base Features 676-750
Domain: 47_gap_down_clustering
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

def gapc_676_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 47 gap down clustering to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = ((close - open).abs().rolling(100).mean())
    return _rank_pct(base, 5)

def gapc_677_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 47 gap down clustering to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = ((close - open).abs().rolling(100).mean())
    return _rank_pct(base, 21)

def gapc_678_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 47 gap down clustering to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = ((close - open).abs().rolling(100).mean())
    return _rank_pct(base, 63)

def gapc_679_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 47 gap down clustering to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = ((close - open).abs().rolling(100).mean())
    return _rank_pct(base, 126)

def gapc_680_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 47 gap down clustering to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = ((close - open).abs().rolling(100).mean())
    return _rank_pct(base, 252)

def gapc_681_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 47 gap down clustering distribution over 5d to detect tail risk or exhaustion.
    """
    base = ((close - open).abs().rolling(100).mean())
    return _rolling_skew(base, 5)

def gapc_682_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 47 gap down clustering distribution over 21d to detect tail risk or exhaustion.
    """
    base = ((close - open).abs().rolling(100).mean())
    return _rolling_skew(base, 21)

def gapc_683_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 47 gap down clustering distribution over 63d to detect tail risk or exhaustion.
    """
    base = ((close - open).abs().rolling(100).mean())
    return _rolling_skew(base, 63)

def gapc_684_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 47 gap down clustering distribution over 126d to detect tail risk or exhaustion.
    """
    base = ((close - open).abs().rolling(100).mean())
    return _rolling_skew(base, 126)

def gapc_685_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 47 gap down clustering distribution over 252d to detect tail risk or exhaustion.
    """
    base = ((close - open).abs().rolling(100).mean())
    return _rolling_skew(base, 252)

def gapc_686_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 47 gap down clustering over 5d to capture explosive breakdown or reversal points.
    """
    base = ((close - open).abs().rolling(100).mean())
    return _rolling_kurt(base, 5)

def gapc_687_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 47 gap down clustering over 21d to capture explosive breakdown or reversal points.
    """
    base = ((close - open).abs().rolling(100).mean())
    return _rolling_kurt(base, 21)

def gapc_688_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 47 gap down clustering over 63d to capture explosive breakdown or reversal points.
    """
    base = ((close - open).abs().rolling(100).mean())
    return _rolling_kurt(base, 63)

def gapc_689_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 47 gap down clustering over 126d to capture explosive breakdown or reversal points.
    """
    base = ((close - open).abs().rolling(100).mean())
    return _rolling_kurt(base, 126)

def gapc_690_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 47 gap down clustering over 252d to capture explosive breakdown or reversal points.
    """
    base = ((close - open).abs().rolling(100).mean())
    return _rolling_kurt(base, 252)

def gapc_691_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 47 gap down clustering for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = ((close - open).abs().rolling(100).mean())
    return _safe_div(base, _rolling_std(base, 5))

def gapc_692_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 47 gap down clustering for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = ((close - open).abs().rolling(100).mean())
    return _safe_div(base, _rolling_std(base, 21))

def gapc_693_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 47 gap down clustering for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = ((close - open).abs().rolling(100).mean())
    return _safe_div(base, _rolling_std(base, 63))

def gapc_694_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 47 gap down clustering for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = ((close - open).abs().rolling(100).mean())
    return _safe_div(base, _rolling_std(base, 126))

def gapc_695_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 47 gap down clustering for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = ((close - open).abs().rolling(100).mean())
    return _safe_div(base, _rolling_std(base, 252))

def gapc_696_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 47 gap down clustering over 5d to stabilize variance and capture exponential shifts.
    """
    base = ((close - open).abs().rolling(100).mean())
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def gapc_697_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 47 gap down clustering over 21d to stabilize variance and capture exponential shifts.
    """
    base = ((close - open).abs().rolling(100).mean())
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def gapc_698_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 47 gap down clustering over 63d to stabilize variance and capture exponential shifts.
    """
    base = ((close - open).abs().rolling(100).mean())
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def gapc_699_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 47 gap down clustering over 126d to stabilize variance and capture exponential shifts.
    """
    base = ((close - open).abs().rolling(100).mean())
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def gapc_700_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 47 gap down clustering over 252d to stabilize variance and capture exponential shifts.
    """
    base = ((close - open).abs().rolling(100).mean())
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def gapc_701_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 47 gap down clustering over a 5d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(105).mean())
    return _rolling_mean(base, 5)

def gapc_702_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 47 gap down clustering over a 21d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(105).mean())
    return _rolling_mean(base, 21)

def gapc_703_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 47 gap down clustering over a 63d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(105).mean())
    return _rolling_mean(base, 63)

def gapc_704_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 47 gap down clustering over a 126d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(105).mean())
    return _rolling_mean(base, 126)

def gapc_705_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 47 gap down clustering over a 252d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(105).mean())
    return _rolling_mean(base, 252)

def gapc_706_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 47 gap down clustering by measuring deviations from the 5d mean.
    """
    base = ((close - open).abs().rolling(105).mean())
    return _zscore_rolling(base, 5)

def gapc_707_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 47 gap down clustering by measuring deviations from the 21d mean.
    """
    base = ((close - open).abs().rolling(105).mean())
    return _zscore_rolling(base, 21)

def gapc_708_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 47 gap down clustering by measuring deviations from the 63d mean.
    """
    base = ((close - open).abs().rolling(105).mean())
    return _zscore_rolling(base, 63)

def gapc_709_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 47 gap down clustering by measuring deviations from the 126d mean.
    """
    base = ((close - open).abs().rolling(105).mean())
    return _zscore_rolling(base, 126)

def gapc_710_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 47 gap down clustering by measuring deviations from the 252d mean.
    """
    base = ((close - open).abs().rolling(105).mean())
    return _zscore_rolling(base, 252)

def gapc_711_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 47 gap down clustering to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = ((close - open).abs().rolling(105).mean())
    return _rank_pct(base, 5)

def gapc_712_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 47 gap down clustering to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = ((close - open).abs().rolling(105).mean())
    return _rank_pct(base, 21)

def gapc_713_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 47 gap down clustering to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = ((close - open).abs().rolling(105).mean())
    return _rank_pct(base, 63)

def gapc_714_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 47 gap down clustering to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = ((close - open).abs().rolling(105).mean())
    return _rank_pct(base, 126)

def gapc_715_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 47 gap down clustering to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = ((close - open).abs().rolling(105).mean())
    return _rank_pct(base, 252)

def gapc_716_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 47 gap down clustering distribution over 5d to detect tail risk or exhaustion.
    """
    base = ((close - open).abs().rolling(105).mean())
    return _rolling_skew(base, 5)

def gapc_717_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 47 gap down clustering distribution over 21d to detect tail risk or exhaustion.
    """
    base = ((close - open).abs().rolling(105).mean())
    return _rolling_skew(base, 21)

def gapc_718_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 47 gap down clustering distribution over 63d to detect tail risk or exhaustion.
    """
    base = ((close - open).abs().rolling(105).mean())
    return _rolling_skew(base, 63)

def gapc_719_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 47 gap down clustering distribution over 126d to detect tail risk or exhaustion.
    """
    base = ((close - open).abs().rolling(105).mean())
    return _rolling_skew(base, 126)

def gapc_720_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 47 gap down clustering distribution over 252d to detect tail risk or exhaustion.
    """
    base = ((close - open).abs().rolling(105).mean())
    return _rolling_skew(base, 252)

def gapc_721_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 47 gap down clustering over 5d to capture explosive breakdown or reversal points.
    """
    base = ((close - open).abs().rolling(105).mean())
    return _rolling_kurt(base, 5)

def gapc_722_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 47 gap down clustering over 21d to capture explosive breakdown or reversal points.
    """
    base = ((close - open).abs().rolling(105).mean())
    return _rolling_kurt(base, 21)

def gapc_723_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 47 gap down clustering over 63d to capture explosive breakdown or reversal points.
    """
    base = ((close - open).abs().rolling(105).mean())
    return _rolling_kurt(base, 63)

def gapc_724_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 47 gap down clustering over 126d to capture explosive breakdown or reversal points.
    """
    base = ((close - open).abs().rolling(105).mean())
    return _rolling_kurt(base, 126)

def gapc_725_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 47 gap down clustering over 252d to capture explosive breakdown or reversal points.
    """
    base = ((close - open).abs().rolling(105).mean())
    return _rolling_kurt(base, 252)

def gapc_726_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 47 gap down clustering for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = ((close - open).abs().rolling(105).mean())
    return _safe_div(base, _rolling_std(base, 5))

def gapc_727_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 47 gap down clustering for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = ((close - open).abs().rolling(105).mean())
    return _safe_div(base, _rolling_std(base, 21))

def gapc_728_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 47 gap down clustering for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = ((close - open).abs().rolling(105).mean())
    return _safe_div(base, _rolling_std(base, 63))

def gapc_729_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 47 gap down clustering for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = ((close - open).abs().rolling(105).mean())
    return _safe_div(base, _rolling_std(base, 126))

def gapc_730_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 47 gap down clustering for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = ((close - open).abs().rolling(105).mean())
    return _safe_div(base, _rolling_std(base, 252))

def gapc_731_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 47 gap down clustering over 5d to stabilize variance and capture exponential shifts.
    """
    base = ((close - open).abs().rolling(105).mean())
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def gapc_732_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 47 gap down clustering over 21d to stabilize variance and capture exponential shifts.
    """
    base = ((close - open).abs().rolling(105).mean())
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def gapc_733_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 47 gap down clustering over 63d to stabilize variance and capture exponential shifts.
    """
    base = ((close - open).abs().rolling(105).mean())
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def gapc_734_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 47 gap down clustering over 126d to stabilize variance and capture exponential shifts.
    """
    base = ((close - open).abs().rolling(105).mean())
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def gapc_735_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 47 gap down clustering over 252d to stabilize variance and capture exponential shifts.
    """
    base = ((close - open).abs().rolling(105).mean())
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def gapc_736_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 47 gap down clustering over a 5d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(110).mean())
    return _rolling_mean(base, 5)

def gapc_737_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 47 gap down clustering over a 21d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(110).mean())
    return _rolling_mean(base, 21)

def gapc_738_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 47 gap down clustering over a 63d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(110).mean())
    return _rolling_mean(base, 63)

def gapc_739_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 47 gap down clustering over a 126d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(110).mean())
    return _rolling_mean(base, 126)

def gapc_740_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 47 gap down clustering over a 252d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(110).mean())
    return _rolling_mean(base, 252)

def gapc_741_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 47 gap down clustering by measuring deviations from the 5d mean.
    """
    base = ((close - open).abs().rolling(110).mean())
    return _zscore_rolling(base, 5)

def gapc_742_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 47 gap down clustering by measuring deviations from the 21d mean.
    """
    base = ((close - open).abs().rolling(110).mean())
    return _zscore_rolling(base, 21)

def gapc_743_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 47 gap down clustering by measuring deviations from the 63d mean.
    """
    base = ((close - open).abs().rolling(110).mean())
    return _zscore_rolling(base, 63)

def gapc_744_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 47 gap down clustering by measuring deviations from the 126d mean.
    """
    base = ((close - open).abs().rolling(110).mean())
    return _zscore_rolling(base, 126)

def gapc_745_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 47 gap down clustering by measuring deviations from the 252d mean.
    """
    base = ((close - open).abs().rolling(110).mean())
    return _zscore_rolling(base, 252)

def gapc_746_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 47 gap down clustering to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = ((close - open).abs().rolling(110).mean())
    return _rank_pct(base, 5)

def gapc_747_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 47 gap down clustering to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = ((close - open).abs().rolling(110).mean())
    return _rank_pct(base, 21)

def gapc_748_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 47 gap down clustering to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = ((close - open).abs().rolling(110).mean())
    return _rank_pct(base, 63)

def gapc_749_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 47 gap down clustering to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = ((close - open).abs().rolling(110).mean())
    return _rank_pct(base, 126)

def gapc_750_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 47 gap down clustering to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = ((close - open).abs().rolling(110).mean())
    return _rank_pct(base, 252)
