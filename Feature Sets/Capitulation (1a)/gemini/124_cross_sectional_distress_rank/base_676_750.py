"""
124_124_cross_sectional_distress_rank — Base Features 676-750
Domain: 124_cross_sectional_distress_rank
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

def csdr_676_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 124 cross sectional distress rank to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = _rank_pct(close.pct_change(200), 252)
    return _rank_pct(base, 5)

def csdr_677_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 124 cross sectional distress rank to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = _rank_pct(close.pct_change(200), 252)
    return _rank_pct(base, 21)

def csdr_678_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 124 cross sectional distress rank to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = _rank_pct(close.pct_change(200), 252)
    return _rank_pct(base, 63)

def csdr_679_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 124 cross sectional distress rank to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = _rank_pct(close.pct_change(200), 252)
    return _rank_pct(base, 126)

def csdr_680_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 124 cross sectional distress rank to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = _rank_pct(close.pct_change(200), 252)
    return _rank_pct(base, 252)

def csdr_681_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 124 cross sectional distress rank distribution over 5d to detect tail risk or exhaustion.
    """
    base = _rank_pct(close.pct_change(200), 252)
    return _rolling_skew(base, 5)

def csdr_682_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 124 cross sectional distress rank distribution over 21d to detect tail risk or exhaustion.
    """
    base = _rank_pct(close.pct_change(200), 252)
    return _rolling_skew(base, 21)

def csdr_683_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 124 cross sectional distress rank distribution over 63d to detect tail risk or exhaustion.
    """
    base = _rank_pct(close.pct_change(200), 252)
    return _rolling_skew(base, 63)

def csdr_684_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 124 cross sectional distress rank distribution over 126d to detect tail risk or exhaustion.
    """
    base = _rank_pct(close.pct_change(200), 252)
    return _rolling_skew(base, 126)

def csdr_685_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 124 cross sectional distress rank distribution over 252d to detect tail risk or exhaustion.
    """
    base = _rank_pct(close.pct_change(200), 252)
    return _rolling_skew(base, 252)

def csdr_686_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 124 cross sectional distress rank over 5d to capture explosive breakdown or reversal points.
    """
    base = _rank_pct(close.pct_change(200), 252)
    return _rolling_kurt(base, 5)

def csdr_687_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 124 cross sectional distress rank over 21d to capture explosive breakdown or reversal points.
    """
    base = _rank_pct(close.pct_change(200), 252)
    return _rolling_kurt(base, 21)

def csdr_688_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 124 cross sectional distress rank over 63d to capture explosive breakdown or reversal points.
    """
    base = _rank_pct(close.pct_change(200), 252)
    return _rolling_kurt(base, 63)

def csdr_689_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 124 cross sectional distress rank over 126d to capture explosive breakdown or reversal points.
    """
    base = _rank_pct(close.pct_change(200), 252)
    return _rolling_kurt(base, 126)

def csdr_690_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 124 cross sectional distress rank over 252d to capture explosive breakdown or reversal points.
    """
    base = _rank_pct(close.pct_change(200), 252)
    return _rolling_kurt(base, 252)

def csdr_691_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 124 cross sectional distress rank for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = _rank_pct(close.pct_change(200), 252)
    return _safe_div(base, _rolling_std(base, 5))

def csdr_692_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 124 cross sectional distress rank for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = _rank_pct(close.pct_change(200), 252)
    return _safe_div(base, _rolling_std(base, 21))

def csdr_693_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 124 cross sectional distress rank for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = _rank_pct(close.pct_change(200), 252)
    return _safe_div(base, _rolling_std(base, 63))

def csdr_694_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 124 cross sectional distress rank for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = _rank_pct(close.pct_change(200), 252)
    return _safe_div(base, _rolling_std(base, 126))

def csdr_695_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 124 cross sectional distress rank for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = _rank_pct(close.pct_change(200), 252)
    return _safe_div(base, _rolling_std(base, 252))

def csdr_696_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 124 cross sectional distress rank over 5d to stabilize variance and capture exponential shifts.
    """
    base = _rank_pct(close.pct_change(200), 252)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def csdr_697_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 124 cross sectional distress rank over 21d to stabilize variance and capture exponential shifts.
    """
    base = _rank_pct(close.pct_change(200), 252)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def csdr_698_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 124 cross sectional distress rank over 63d to stabilize variance and capture exponential shifts.
    """
    base = _rank_pct(close.pct_change(200), 252)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def csdr_699_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 124 cross sectional distress rank over 126d to stabilize variance and capture exponential shifts.
    """
    base = _rank_pct(close.pct_change(200), 252)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def csdr_700_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 124 cross sectional distress rank over 252d to stabilize variance and capture exponential shifts.
    """
    base = _rank_pct(close.pct_change(200), 252)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def csdr_701_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 124 cross sectional distress rank over a 5d horizon to identify extreme regimes.
    """
    base = _rank_pct(close.pct_change(210), 252)
    return _rolling_mean(base, 5)

def csdr_702_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 124 cross sectional distress rank over a 21d horizon to identify extreme regimes.
    """
    base = _rank_pct(close.pct_change(210), 252)
    return _rolling_mean(base, 21)

def csdr_703_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 124 cross sectional distress rank over a 63d horizon to identify extreme regimes.
    """
    base = _rank_pct(close.pct_change(210), 252)
    return _rolling_mean(base, 63)

def csdr_704_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 124 cross sectional distress rank over a 126d horizon to identify extreme regimes.
    """
    base = _rank_pct(close.pct_change(210), 252)
    return _rolling_mean(base, 126)

def csdr_705_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 124 cross sectional distress rank over a 252d horizon to identify extreme regimes.
    """
    base = _rank_pct(close.pct_change(210), 252)
    return _rolling_mean(base, 252)

def csdr_706_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 124 cross sectional distress rank by measuring deviations from the 5d mean.
    """
    base = _rank_pct(close.pct_change(210), 252)
    return _zscore_rolling(base, 5)

def csdr_707_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 124 cross sectional distress rank by measuring deviations from the 21d mean.
    """
    base = _rank_pct(close.pct_change(210), 252)
    return _zscore_rolling(base, 21)

def csdr_708_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 124 cross sectional distress rank by measuring deviations from the 63d mean.
    """
    base = _rank_pct(close.pct_change(210), 252)
    return _zscore_rolling(base, 63)

def csdr_709_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 124 cross sectional distress rank by measuring deviations from the 126d mean.
    """
    base = _rank_pct(close.pct_change(210), 252)
    return _zscore_rolling(base, 126)

def csdr_710_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 124 cross sectional distress rank by measuring deviations from the 252d mean.
    """
    base = _rank_pct(close.pct_change(210), 252)
    return _zscore_rolling(base, 252)

def csdr_711_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 124 cross sectional distress rank to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = _rank_pct(close.pct_change(210), 252)
    return _rank_pct(base, 5)

def csdr_712_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 124 cross sectional distress rank to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = _rank_pct(close.pct_change(210), 252)
    return _rank_pct(base, 21)

def csdr_713_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 124 cross sectional distress rank to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = _rank_pct(close.pct_change(210), 252)
    return _rank_pct(base, 63)

def csdr_714_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 124 cross sectional distress rank to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = _rank_pct(close.pct_change(210), 252)
    return _rank_pct(base, 126)

def csdr_715_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 124 cross sectional distress rank to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = _rank_pct(close.pct_change(210), 252)
    return _rank_pct(base, 252)

def csdr_716_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 124 cross sectional distress rank distribution over 5d to detect tail risk or exhaustion.
    """
    base = _rank_pct(close.pct_change(210), 252)
    return _rolling_skew(base, 5)

def csdr_717_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 124 cross sectional distress rank distribution over 21d to detect tail risk or exhaustion.
    """
    base = _rank_pct(close.pct_change(210), 252)
    return _rolling_skew(base, 21)

def csdr_718_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 124 cross sectional distress rank distribution over 63d to detect tail risk or exhaustion.
    """
    base = _rank_pct(close.pct_change(210), 252)
    return _rolling_skew(base, 63)

def csdr_719_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 124 cross sectional distress rank distribution over 126d to detect tail risk or exhaustion.
    """
    base = _rank_pct(close.pct_change(210), 252)
    return _rolling_skew(base, 126)

def csdr_720_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 124 cross sectional distress rank distribution over 252d to detect tail risk or exhaustion.
    """
    base = _rank_pct(close.pct_change(210), 252)
    return _rolling_skew(base, 252)

def csdr_721_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 124 cross sectional distress rank over 5d to capture explosive breakdown or reversal points.
    """
    base = _rank_pct(close.pct_change(210), 252)
    return _rolling_kurt(base, 5)

def csdr_722_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 124 cross sectional distress rank over 21d to capture explosive breakdown or reversal points.
    """
    base = _rank_pct(close.pct_change(210), 252)
    return _rolling_kurt(base, 21)

def csdr_723_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 124 cross sectional distress rank over 63d to capture explosive breakdown or reversal points.
    """
    base = _rank_pct(close.pct_change(210), 252)
    return _rolling_kurt(base, 63)

def csdr_724_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 124 cross sectional distress rank over 126d to capture explosive breakdown or reversal points.
    """
    base = _rank_pct(close.pct_change(210), 252)
    return _rolling_kurt(base, 126)

def csdr_725_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 124 cross sectional distress rank over 252d to capture explosive breakdown or reversal points.
    """
    base = _rank_pct(close.pct_change(210), 252)
    return _rolling_kurt(base, 252)

def csdr_726_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 124 cross sectional distress rank for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = _rank_pct(close.pct_change(210), 252)
    return _safe_div(base, _rolling_std(base, 5))

def csdr_727_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 124 cross sectional distress rank for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = _rank_pct(close.pct_change(210), 252)
    return _safe_div(base, _rolling_std(base, 21))

def csdr_728_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 124 cross sectional distress rank for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = _rank_pct(close.pct_change(210), 252)
    return _safe_div(base, _rolling_std(base, 63))

def csdr_729_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 124 cross sectional distress rank for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = _rank_pct(close.pct_change(210), 252)
    return _safe_div(base, _rolling_std(base, 126))

def csdr_730_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 124 cross sectional distress rank for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = _rank_pct(close.pct_change(210), 252)
    return _safe_div(base, _rolling_std(base, 252))

def csdr_731_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 124 cross sectional distress rank over 5d to stabilize variance and capture exponential shifts.
    """
    base = _rank_pct(close.pct_change(210), 252)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def csdr_732_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 124 cross sectional distress rank over 21d to stabilize variance and capture exponential shifts.
    """
    base = _rank_pct(close.pct_change(210), 252)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def csdr_733_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 124 cross sectional distress rank over 63d to stabilize variance and capture exponential shifts.
    """
    base = _rank_pct(close.pct_change(210), 252)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def csdr_734_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 124 cross sectional distress rank over 126d to stabilize variance and capture exponential shifts.
    """
    base = _rank_pct(close.pct_change(210), 252)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def csdr_735_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 124 cross sectional distress rank over 252d to stabilize variance and capture exponential shifts.
    """
    base = _rank_pct(close.pct_change(210), 252)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def csdr_736_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 124 cross sectional distress rank over a 5d horizon to identify extreme regimes.
    """
    base = _rank_pct(close.pct_change(220), 252)
    return _rolling_mean(base, 5)

def csdr_737_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 124 cross sectional distress rank over a 21d horizon to identify extreme regimes.
    """
    base = _rank_pct(close.pct_change(220), 252)
    return _rolling_mean(base, 21)

def csdr_738_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 124 cross sectional distress rank over a 63d horizon to identify extreme regimes.
    """
    base = _rank_pct(close.pct_change(220), 252)
    return _rolling_mean(base, 63)

def csdr_739_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 124 cross sectional distress rank over a 126d horizon to identify extreme regimes.
    """
    base = _rank_pct(close.pct_change(220), 252)
    return _rolling_mean(base, 126)

def csdr_740_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 124 cross sectional distress rank over a 252d horizon to identify extreme regimes.
    """
    base = _rank_pct(close.pct_change(220), 252)
    return _rolling_mean(base, 252)

def csdr_741_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 124 cross sectional distress rank by measuring deviations from the 5d mean.
    """
    base = _rank_pct(close.pct_change(220), 252)
    return _zscore_rolling(base, 5)

def csdr_742_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 124 cross sectional distress rank by measuring deviations from the 21d mean.
    """
    base = _rank_pct(close.pct_change(220), 252)
    return _zscore_rolling(base, 21)

def csdr_743_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 124 cross sectional distress rank by measuring deviations from the 63d mean.
    """
    base = _rank_pct(close.pct_change(220), 252)
    return _zscore_rolling(base, 63)

def csdr_744_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 124 cross sectional distress rank by measuring deviations from the 126d mean.
    """
    base = _rank_pct(close.pct_change(220), 252)
    return _zscore_rolling(base, 126)

def csdr_745_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 124 cross sectional distress rank by measuring deviations from the 252d mean.
    """
    base = _rank_pct(close.pct_change(220), 252)
    return _zscore_rolling(base, 252)

def csdr_746_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 124 cross sectional distress rank to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = _rank_pct(close.pct_change(220), 252)
    return _rank_pct(base, 5)

def csdr_747_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 124 cross sectional distress rank to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = _rank_pct(close.pct_change(220), 252)
    return _rank_pct(base, 21)

def csdr_748_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 124 cross sectional distress rank to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = _rank_pct(close.pct_change(220), 252)
    return _rank_pct(base, 63)

def csdr_749_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 124 cross sectional distress rank to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = _rank_pct(close.pct_change(220), 252)
    return _rank_pct(base, 126)

def csdr_750_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 124 cross sectional distress rank to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = _rank_pct(close.pct_change(220), 252)
    return _rank_pct(base, 252)
