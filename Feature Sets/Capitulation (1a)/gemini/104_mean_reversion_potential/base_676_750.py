"""
104_104_mean_reversion_potential — Base Features 676-750
Domain: 104_mean_reversion_potential
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

def mrpt_676_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 104 mean reversion potential to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = close / _rolling_mean(close, 385) - 1
    return _rank_pct(base, 5)

def mrpt_677_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 104 mean reversion potential to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = close / _rolling_mean(close, 385) - 1
    return _rank_pct(base, 21)

def mrpt_678_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 104 mean reversion potential to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = close / _rolling_mean(close, 385) - 1
    return _rank_pct(base, 63)

def mrpt_679_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 104 mean reversion potential to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = close / _rolling_mean(close, 385) - 1
    return _rank_pct(base, 126)

def mrpt_680_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 104 mean reversion potential to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = close / _rolling_mean(close, 385) - 1
    return _rank_pct(base, 252)

def mrpt_681_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 104 mean reversion potential distribution over 5d to detect tail risk or exhaustion.
    """
    base = close / _rolling_mean(close, 385) - 1
    return _rolling_skew(base, 5)

def mrpt_682_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 104 mean reversion potential distribution over 21d to detect tail risk or exhaustion.
    """
    base = close / _rolling_mean(close, 385) - 1
    return _rolling_skew(base, 21)

def mrpt_683_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 104 mean reversion potential distribution over 63d to detect tail risk or exhaustion.
    """
    base = close / _rolling_mean(close, 385) - 1
    return _rolling_skew(base, 63)

def mrpt_684_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 104 mean reversion potential distribution over 126d to detect tail risk or exhaustion.
    """
    base = close / _rolling_mean(close, 385) - 1
    return _rolling_skew(base, 126)

def mrpt_685_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 104 mean reversion potential distribution over 252d to detect tail risk or exhaustion.
    """
    base = close / _rolling_mean(close, 385) - 1
    return _rolling_skew(base, 252)

def mrpt_686_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 104 mean reversion potential over 5d to capture explosive breakdown or reversal points.
    """
    base = close / _rolling_mean(close, 385) - 1
    return _rolling_kurt(base, 5)

def mrpt_687_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 104 mean reversion potential over 21d to capture explosive breakdown or reversal points.
    """
    base = close / _rolling_mean(close, 385) - 1
    return _rolling_kurt(base, 21)

def mrpt_688_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 104 mean reversion potential over 63d to capture explosive breakdown or reversal points.
    """
    base = close / _rolling_mean(close, 385) - 1
    return _rolling_kurt(base, 63)

def mrpt_689_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 104 mean reversion potential over 126d to capture explosive breakdown or reversal points.
    """
    base = close / _rolling_mean(close, 385) - 1
    return _rolling_kurt(base, 126)

def mrpt_690_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 104 mean reversion potential over 252d to capture explosive breakdown or reversal points.
    """
    base = close / _rolling_mean(close, 385) - 1
    return _rolling_kurt(base, 252)

def mrpt_691_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 104 mean reversion potential for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = close / _rolling_mean(close, 385) - 1
    return _safe_div(base, _rolling_std(base, 5))

def mrpt_692_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 104 mean reversion potential for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = close / _rolling_mean(close, 385) - 1
    return _safe_div(base, _rolling_std(base, 21))

def mrpt_693_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 104 mean reversion potential for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = close / _rolling_mean(close, 385) - 1
    return _safe_div(base, _rolling_std(base, 63))

def mrpt_694_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 104 mean reversion potential for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = close / _rolling_mean(close, 385) - 1
    return _safe_div(base, _rolling_std(base, 126))

def mrpt_695_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 104 mean reversion potential for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = close / _rolling_mean(close, 385) - 1
    return _safe_div(base, _rolling_std(base, 252))

def mrpt_696_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 104 mean reversion potential over 5d to stabilize variance and capture exponential shifts.
    """
    base = close / _rolling_mean(close, 385) - 1
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def mrpt_697_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 104 mean reversion potential over 21d to stabilize variance and capture exponential shifts.
    """
    base = close / _rolling_mean(close, 385) - 1
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def mrpt_698_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 104 mean reversion potential over 63d to stabilize variance and capture exponential shifts.
    """
    base = close / _rolling_mean(close, 385) - 1
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def mrpt_699_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 104 mean reversion potential over 126d to stabilize variance and capture exponential shifts.
    """
    base = close / _rolling_mean(close, 385) - 1
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def mrpt_700_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 104 mean reversion potential over 252d to stabilize variance and capture exponential shifts.
    """
    base = close / _rolling_mean(close, 385) - 1
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def mrpt_701_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 104 mean reversion potential over a 5d horizon to identify extreme regimes.
    """
    base = close / _rolling_mean(close, 405) - 1
    return _rolling_mean(base, 5)

def mrpt_702_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 104 mean reversion potential over a 21d horizon to identify extreme regimes.
    """
    base = close / _rolling_mean(close, 405) - 1
    return _rolling_mean(base, 21)

def mrpt_703_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 104 mean reversion potential over a 63d horizon to identify extreme regimes.
    """
    base = close / _rolling_mean(close, 405) - 1
    return _rolling_mean(base, 63)

def mrpt_704_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 104 mean reversion potential over a 126d horizon to identify extreme regimes.
    """
    base = close / _rolling_mean(close, 405) - 1
    return _rolling_mean(base, 126)

def mrpt_705_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 104 mean reversion potential over a 252d horizon to identify extreme regimes.
    """
    base = close / _rolling_mean(close, 405) - 1
    return _rolling_mean(base, 252)

def mrpt_706_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 104 mean reversion potential by measuring deviations from the 5d mean.
    """
    base = close / _rolling_mean(close, 405) - 1
    return _zscore_rolling(base, 5)

def mrpt_707_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 104 mean reversion potential by measuring deviations from the 21d mean.
    """
    base = close / _rolling_mean(close, 405) - 1
    return _zscore_rolling(base, 21)

def mrpt_708_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 104 mean reversion potential by measuring deviations from the 63d mean.
    """
    base = close / _rolling_mean(close, 405) - 1
    return _zscore_rolling(base, 63)

def mrpt_709_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 104 mean reversion potential by measuring deviations from the 126d mean.
    """
    base = close / _rolling_mean(close, 405) - 1
    return _zscore_rolling(base, 126)

def mrpt_710_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 104 mean reversion potential by measuring deviations from the 252d mean.
    """
    base = close / _rolling_mean(close, 405) - 1
    return _zscore_rolling(base, 252)

def mrpt_711_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 104 mean reversion potential to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = close / _rolling_mean(close, 405) - 1
    return _rank_pct(base, 5)

def mrpt_712_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 104 mean reversion potential to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = close / _rolling_mean(close, 405) - 1
    return _rank_pct(base, 21)

def mrpt_713_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 104 mean reversion potential to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = close / _rolling_mean(close, 405) - 1
    return _rank_pct(base, 63)

def mrpt_714_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 104 mean reversion potential to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = close / _rolling_mean(close, 405) - 1
    return _rank_pct(base, 126)

def mrpt_715_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 104 mean reversion potential to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = close / _rolling_mean(close, 405) - 1
    return _rank_pct(base, 252)

def mrpt_716_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 104 mean reversion potential distribution over 5d to detect tail risk or exhaustion.
    """
    base = close / _rolling_mean(close, 405) - 1
    return _rolling_skew(base, 5)

def mrpt_717_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 104 mean reversion potential distribution over 21d to detect tail risk or exhaustion.
    """
    base = close / _rolling_mean(close, 405) - 1
    return _rolling_skew(base, 21)

def mrpt_718_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 104 mean reversion potential distribution over 63d to detect tail risk or exhaustion.
    """
    base = close / _rolling_mean(close, 405) - 1
    return _rolling_skew(base, 63)

def mrpt_719_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 104 mean reversion potential distribution over 126d to detect tail risk or exhaustion.
    """
    base = close / _rolling_mean(close, 405) - 1
    return _rolling_skew(base, 126)

def mrpt_720_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 104 mean reversion potential distribution over 252d to detect tail risk or exhaustion.
    """
    base = close / _rolling_mean(close, 405) - 1
    return _rolling_skew(base, 252)

def mrpt_721_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 104 mean reversion potential over 5d to capture explosive breakdown or reversal points.
    """
    base = close / _rolling_mean(close, 405) - 1
    return _rolling_kurt(base, 5)

def mrpt_722_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 104 mean reversion potential over 21d to capture explosive breakdown or reversal points.
    """
    base = close / _rolling_mean(close, 405) - 1
    return _rolling_kurt(base, 21)

def mrpt_723_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 104 mean reversion potential over 63d to capture explosive breakdown or reversal points.
    """
    base = close / _rolling_mean(close, 405) - 1
    return _rolling_kurt(base, 63)

def mrpt_724_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 104 mean reversion potential over 126d to capture explosive breakdown or reversal points.
    """
    base = close / _rolling_mean(close, 405) - 1
    return _rolling_kurt(base, 126)

def mrpt_725_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 104 mean reversion potential over 252d to capture explosive breakdown or reversal points.
    """
    base = close / _rolling_mean(close, 405) - 1
    return _rolling_kurt(base, 252)

def mrpt_726_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 104 mean reversion potential for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = close / _rolling_mean(close, 405) - 1
    return _safe_div(base, _rolling_std(base, 5))

def mrpt_727_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 104 mean reversion potential for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = close / _rolling_mean(close, 405) - 1
    return _safe_div(base, _rolling_std(base, 21))

def mrpt_728_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 104 mean reversion potential for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = close / _rolling_mean(close, 405) - 1
    return _safe_div(base, _rolling_std(base, 63))

def mrpt_729_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 104 mean reversion potential for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = close / _rolling_mean(close, 405) - 1
    return _safe_div(base, _rolling_std(base, 126))

def mrpt_730_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 104 mean reversion potential for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = close / _rolling_mean(close, 405) - 1
    return _safe_div(base, _rolling_std(base, 252))

def mrpt_731_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 104 mean reversion potential over 5d to stabilize variance and capture exponential shifts.
    """
    base = close / _rolling_mean(close, 405) - 1
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def mrpt_732_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 104 mean reversion potential over 21d to stabilize variance and capture exponential shifts.
    """
    base = close / _rolling_mean(close, 405) - 1
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def mrpt_733_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 104 mean reversion potential over 63d to stabilize variance and capture exponential shifts.
    """
    base = close / _rolling_mean(close, 405) - 1
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def mrpt_734_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 104 mean reversion potential over 126d to stabilize variance and capture exponential shifts.
    """
    base = close / _rolling_mean(close, 405) - 1
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def mrpt_735_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 104 mean reversion potential over 252d to stabilize variance and capture exponential shifts.
    """
    base = close / _rolling_mean(close, 405) - 1
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def mrpt_736_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 104 mean reversion potential over a 5d horizon to identify extreme regimes.
    """
    base = close / _rolling_mean(close, 425) - 1
    return _rolling_mean(base, 5)

def mrpt_737_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 104 mean reversion potential over a 21d horizon to identify extreme regimes.
    """
    base = close / _rolling_mean(close, 425) - 1
    return _rolling_mean(base, 21)

def mrpt_738_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 104 mean reversion potential over a 63d horizon to identify extreme regimes.
    """
    base = close / _rolling_mean(close, 425) - 1
    return _rolling_mean(base, 63)

def mrpt_739_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 104 mean reversion potential over a 126d horizon to identify extreme regimes.
    """
    base = close / _rolling_mean(close, 425) - 1
    return _rolling_mean(base, 126)

def mrpt_740_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 104 mean reversion potential over a 252d horizon to identify extreme regimes.
    """
    base = close / _rolling_mean(close, 425) - 1
    return _rolling_mean(base, 252)

def mrpt_741_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 104 mean reversion potential by measuring deviations from the 5d mean.
    """
    base = close / _rolling_mean(close, 425) - 1
    return _zscore_rolling(base, 5)

def mrpt_742_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 104 mean reversion potential by measuring deviations from the 21d mean.
    """
    base = close / _rolling_mean(close, 425) - 1
    return _zscore_rolling(base, 21)

def mrpt_743_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 104 mean reversion potential by measuring deviations from the 63d mean.
    """
    base = close / _rolling_mean(close, 425) - 1
    return _zscore_rolling(base, 63)

def mrpt_744_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 104 mean reversion potential by measuring deviations from the 126d mean.
    """
    base = close / _rolling_mean(close, 425) - 1
    return _zscore_rolling(base, 126)

def mrpt_745_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 104 mean reversion potential by measuring deviations from the 252d mean.
    """
    base = close / _rolling_mean(close, 425) - 1
    return _zscore_rolling(base, 252)

def mrpt_746_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 104 mean reversion potential to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = close / _rolling_mean(close, 425) - 1
    return _rank_pct(base, 5)

def mrpt_747_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 104 mean reversion potential to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = close / _rolling_mean(close, 425) - 1
    return _rank_pct(base, 21)

def mrpt_748_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 104 mean reversion potential to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = close / _rolling_mean(close, 425) - 1
    return _rank_pct(base, 63)

def mrpt_749_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 104 mean reversion potential to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = close / _rolling_mean(close, 425) - 1
    return _rank_pct(base, 126)

def mrpt_750_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 104 mean reversion potential to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = close / _rolling_mean(close, 425) - 1
    return _rank_pct(base, 252)
