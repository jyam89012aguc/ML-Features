"""
115_115_volatility_term_structure — Base Features 676-750
Domain: 115_volatility_term_structure
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

def vts_676_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 115 volatility term structure to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(100).std()
    return _rank_pct(base, 5)

def vts_677_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 115 volatility term structure to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(100).std()
    return _rank_pct(base, 21)

def vts_678_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 115 volatility term structure to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(100).std()
    return _rank_pct(base, 63)

def vts_679_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 115 volatility term structure to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(100).std()
    return _rank_pct(base, 126)

def vts_680_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 115 volatility term structure to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(100).std()
    return _rank_pct(base, 252)

def vts_681_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 115 volatility term structure distribution over 5d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(100).std()
    return _rolling_skew(base, 5)

def vts_682_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 115 volatility term structure distribution over 21d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(100).std()
    return _rolling_skew(base, 21)

def vts_683_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 115 volatility term structure distribution over 63d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(100).std()
    return _rolling_skew(base, 63)

def vts_684_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 115 volatility term structure distribution over 126d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(100).std()
    return _rolling_skew(base, 126)

def vts_685_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 115 volatility term structure distribution over 252d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(100).std()
    return _rolling_skew(base, 252)

def vts_686_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 115 volatility term structure over 5d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(100).std()
    return _rolling_kurt(base, 5)

def vts_687_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 115 volatility term structure over 21d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(100).std()
    return _rolling_kurt(base, 21)

def vts_688_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 115 volatility term structure over 63d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(100).std()
    return _rolling_kurt(base, 63)

def vts_689_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 115 volatility term structure over 126d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(100).std()
    return _rolling_kurt(base, 126)

def vts_690_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 115 volatility term structure over 252d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(100).std()
    return _rolling_kurt(base, 252)

def vts_691_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 115 volatility term structure for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(100).std()
    return _safe_div(base, _rolling_std(base, 5))

def vts_692_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 115 volatility term structure for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(100).std()
    return _safe_div(base, _rolling_std(base, 21))

def vts_693_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 115 volatility term structure for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(100).std()
    return _safe_div(base, _rolling_std(base, 63))

def vts_694_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 115 volatility term structure for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(100).std()
    return _safe_div(base, _rolling_std(base, 126))

def vts_695_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 115 volatility term structure for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(100).std()
    return _safe_div(base, _rolling_std(base, 252))

def vts_696_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 115 volatility term structure over 5d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(100).std()
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def vts_697_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 115 volatility term structure over 21d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(100).std()
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def vts_698_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 115 volatility term structure over 63d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(100).std()
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def vts_699_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 115 volatility term structure over 126d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(100).std()
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def vts_700_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 115 volatility term structure over 252d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(100).std()
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def vts_701_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 115 volatility term structure over a 5d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(105).std()
    return _rolling_mean(base, 5)

def vts_702_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 115 volatility term structure over a 21d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(105).std()
    return _rolling_mean(base, 21)

def vts_703_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 115 volatility term structure over a 63d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(105).std()
    return _rolling_mean(base, 63)

def vts_704_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 115 volatility term structure over a 126d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(105).std()
    return _rolling_mean(base, 126)

def vts_705_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 115 volatility term structure over a 252d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(105).std()
    return _rolling_mean(base, 252)

def vts_706_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 115 volatility term structure by measuring deviations from the 5d mean.
    """
    base = close.pct_change().rolling(105).std()
    return _zscore_rolling(base, 5)

def vts_707_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 115 volatility term structure by measuring deviations from the 21d mean.
    """
    base = close.pct_change().rolling(105).std()
    return _zscore_rolling(base, 21)

def vts_708_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 115 volatility term structure by measuring deviations from the 63d mean.
    """
    base = close.pct_change().rolling(105).std()
    return _zscore_rolling(base, 63)

def vts_709_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 115 volatility term structure by measuring deviations from the 126d mean.
    """
    base = close.pct_change().rolling(105).std()
    return _zscore_rolling(base, 126)

def vts_710_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 115 volatility term structure by measuring deviations from the 252d mean.
    """
    base = close.pct_change().rolling(105).std()
    return _zscore_rolling(base, 252)

def vts_711_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 115 volatility term structure to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(105).std()
    return _rank_pct(base, 5)

def vts_712_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 115 volatility term structure to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(105).std()
    return _rank_pct(base, 21)

def vts_713_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 115 volatility term structure to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(105).std()
    return _rank_pct(base, 63)

def vts_714_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 115 volatility term structure to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(105).std()
    return _rank_pct(base, 126)

def vts_715_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 115 volatility term structure to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(105).std()
    return _rank_pct(base, 252)

def vts_716_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 115 volatility term structure distribution over 5d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(105).std()
    return _rolling_skew(base, 5)

def vts_717_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 115 volatility term structure distribution over 21d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(105).std()
    return _rolling_skew(base, 21)

def vts_718_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 115 volatility term structure distribution over 63d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(105).std()
    return _rolling_skew(base, 63)

def vts_719_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 115 volatility term structure distribution over 126d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(105).std()
    return _rolling_skew(base, 126)

def vts_720_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 115 volatility term structure distribution over 252d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(105).std()
    return _rolling_skew(base, 252)

def vts_721_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 115 volatility term structure over 5d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(105).std()
    return _rolling_kurt(base, 5)

def vts_722_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 115 volatility term structure over 21d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(105).std()
    return _rolling_kurt(base, 21)

def vts_723_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 115 volatility term structure over 63d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(105).std()
    return _rolling_kurt(base, 63)

def vts_724_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 115 volatility term structure over 126d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(105).std()
    return _rolling_kurt(base, 126)

def vts_725_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 115 volatility term structure over 252d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(105).std()
    return _rolling_kurt(base, 252)

def vts_726_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 115 volatility term structure for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(105).std()
    return _safe_div(base, _rolling_std(base, 5))

def vts_727_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 115 volatility term structure for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(105).std()
    return _safe_div(base, _rolling_std(base, 21))

def vts_728_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 115 volatility term structure for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(105).std()
    return _safe_div(base, _rolling_std(base, 63))

def vts_729_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 115 volatility term structure for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(105).std()
    return _safe_div(base, _rolling_std(base, 126))

def vts_730_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 115 volatility term structure for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(105).std()
    return _safe_div(base, _rolling_std(base, 252))

def vts_731_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 115 volatility term structure over 5d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(105).std()
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def vts_732_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 115 volatility term structure over 21d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(105).std()
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def vts_733_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 115 volatility term structure over 63d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(105).std()
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def vts_734_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 115 volatility term structure over 126d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(105).std()
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def vts_735_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 115 volatility term structure over 252d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(105).std()
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def vts_736_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 115 volatility term structure over a 5d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(110).std()
    return _rolling_mean(base, 5)

def vts_737_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 115 volatility term structure over a 21d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(110).std()
    return _rolling_mean(base, 21)

def vts_738_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 115 volatility term structure over a 63d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(110).std()
    return _rolling_mean(base, 63)

def vts_739_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 115 volatility term structure over a 126d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(110).std()
    return _rolling_mean(base, 126)

def vts_740_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 115 volatility term structure over a 252d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(110).std()
    return _rolling_mean(base, 252)

def vts_741_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 115 volatility term structure by measuring deviations from the 5d mean.
    """
    base = close.pct_change().rolling(110).std()
    return _zscore_rolling(base, 5)

def vts_742_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 115 volatility term structure by measuring deviations from the 21d mean.
    """
    base = close.pct_change().rolling(110).std()
    return _zscore_rolling(base, 21)

def vts_743_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 115 volatility term structure by measuring deviations from the 63d mean.
    """
    base = close.pct_change().rolling(110).std()
    return _zscore_rolling(base, 63)

def vts_744_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 115 volatility term structure by measuring deviations from the 126d mean.
    """
    base = close.pct_change().rolling(110).std()
    return _zscore_rolling(base, 126)

def vts_745_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 115 volatility term structure by measuring deviations from the 252d mean.
    """
    base = close.pct_change().rolling(110).std()
    return _zscore_rolling(base, 252)

def vts_746_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 115 volatility term structure to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(110).std()
    return _rank_pct(base, 5)

def vts_747_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 115 volatility term structure to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(110).std()
    return _rank_pct(base, 21)

def vts_748_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 115 volatility term structure to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(110).std()
    return _rank_pct(base, 63)

def vts_749_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 115 volatility term structure to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(110).std()
    return _rank_pct(base, 126)

def vts_750_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 115 volatility term structure to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(110).std()
    return _rank_pct(base, 252)
