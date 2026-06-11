"""
121_121_distress_score_ensemble — Base Features 526-600
Domain: 121_distress_score_ensemble
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

def dsen_526_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 121 distress score ensemble over a 5d horizon to identify extreme regimes.
    """
    base = (_zscore_rolling(close, 160) + _zscore_rolling(volume, 160)) / 2
    return _rolling_mean(base, 5)

def dsen_527_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 121 distress score ensemble over a 21d horizon to identify extreme regimes.
    """
    base = (_zscore_rolling(close, 160) + _zscore_rolling(volume, 160)) / 2
    return _rolling_mean(base, 21)

def dsen_528_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 121 distress score ensemble over a 63d horizon to identify extreme regimes.
    """
    base = (_zscore_rolling(close, 160) + _zscore_rolling(volume, 160)) / 2
    return _rolling_mean(base, 63)

def dsen_529_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 121 distress score ensemble over a 126d horizon to identify extreme regimes.
    """
    base = (_zscore_rolling(close, 160) + _zscore_rolling(volume, 160)) / 2
    return _rolling_mean(base, 126)

def dsen_530_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 121 distress score ensemble over a 252d horizon to identify extreme regimes.
    """
    base = (_zscore_rolling(close, 160) + _zscore_rolling(volume, 160)) / 2
    return _rolling_mean(base, 252)

def dsen_531_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 121 distress score ensemble by measuring deviations from the 5d mean.
    """
    base = (_zscore_rolling(close, 160) + _zscore_rolling(volume, 160)) / 2
    return _zscore_rolling(base, 5)

def dsen_532_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 121 distress score ensemble by measuring deviations from the 21d mean.
    """
    base = (_zscore_rolling(close, 160) + _zscore_rolling(volume, 160)) / 2
    return _zscore_rolling(base, 21)

def dsen_533_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 121 distress score ensemble by measuring deviations from the 63d mean.
    """
    base = (_zscore_rolling(close, 160) + _zscore_rolling(volume, 160)) / 2
    return _zscore_rolling(base, 63)

def dsen_534_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 121 distress score ensemble by measuring deviations from the 126d mean.
    """
    base = (_zscore_rolling(close, 160) + _zscore_rolling(volume, 160)) / 2
    return _zscore_rolling(base, 126)

def dsen_535_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 121 distress score ensemble by measuring deviations from the 252d mean.
    """
    base = (_zscore_rolling(close, 160) + _zscore_rolling(volume, 160)) / 2
    return _zscore_rolling(base, 252)

def dsen_536_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 121 distress score ensemble to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = (_zscore_rolling(close, 160) + _zscore_rolling(volume, 160)) / 2
    return _rank_pct(base, 5)

def dsen_537_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 121 distress score ensemble to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = (_zscore_rolling(close, 160) + _zscore_rolling(volume, 160)) / 2
    return _rank_pct(base, 21)

def dsen_538_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 121 distress score ensemble to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = (_zscore_rolling(close, 160) + _zscore_rolling(volume, 160)) / 2
    return _rank_pct(base, 63)

def dsen_539_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 121 distress score ensemble to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = (_zscore_rolling(close, 160) + _zscore_rolling(volume, 160)) / 2
    return _rank_pct(base, 126)

def dsen_540_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 121 distress score ensemble to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = (_zscore_rolling(close, 160) + _zscore_rolling(volume, 160)) / 2
    return _rank_pct(base, 252)

def dsen_541_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 121 distress score ensemble distribution over 5d to detect tail risk or exhaustion.
    """
    base = (_zscore_rolling(close, 160) + _zscore_rolling(volume, 160)) / 2
    return _rolling_skew(base, 5)

def dsen_542_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 121 distress score ensemble distribution over 21d to detect tail risk or exhaustion.
    """
    base = (_zscore_rolling(close, 160) + _zscore_rolling(volume, 160)) / 2
    return _rolling_skew(base, 21)

def dsen_543_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 121 distress score ensemble distribution over 63d to detect tail risk or exhaustion.
    """
    base = (_zscore_rolling(close, 160) + _zscore_rolling(volume, 160)) / 2
    return _rolling_skew(base, 63)

def dsen_544_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 121 distress score ensemble distribution over 126d to detect tail risk or exhaustion.
    """
    base = (_zscore_rolling(close, 160) + _zscore_rolling(volume, 160)) / 2
    return _rolling_skew(base, 126)

def dsen_545_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 121 distress score ensemble distribution over 252d to detect tail risk or exhaustion.
    """
    base = (_zscore_rolling(close, 160) + _zscore_rolling(volume, 160)) / 2
    return _rolling_skew(base, 252)

def dsen_546_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 121 distress score ensemble over 5d to capture explosive breakdown or reversal points.
    """
    base = (_zscore_rolling(close, 160) + _zscore_rolling(volume, 160)) / 2
    return _rolling_kurt(base, 5)

def dsen_547_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 121 distress score ensemble over 21d to capture explosive breakdown or reversal points.
    """
    base = (_zscore_rolling(close, 160) + _zscore_rolling(volume, 160)) / 2
    return _rolling_kurt(base, 21)

def dsen_548_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 121 distress score ensemble over 63d to capture explosive breakdown or reversal points.
    """
    base = (_zscore_rolling(close, 160) + _zscore_rolling(volume, 160)) / 2
    return _rolling_kurt(base, 63)

def dsen_549_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 121 distress score ensemble over 126d to capture explosive breakdown or reversal points.
    """
    base = (_zscore_rolling(close, 160) + _zscore_rolling(volume, 160)) / 2
    return _rolling_kurt(base, 126)

def dsen_550_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 121 distress score ensemble over 252d to capture explosive breakdown or reversal points.
    """
    base = (_zscore_rolling(close, 160) + _zscore_rolling(volume, 160)) / 2
    return _rolling_kurt(base, 252)

def dsen_551_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 121 distress score ensemble for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = (_zscore_rolling(close, 160) + _zscore_rolling(volume, 160)) / 2
    return _safe_div(base, _rolling_std(base, 5))

def dsen_552_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 121 distress score ensemble for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = (_zscore_rolling(close, 160) + _zscore_rolling(volume, 160)) / 2
    return _safe_div(base, _rolling_std(base, 21))

def dsen_553_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 121 distress score ensemble for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = (_zscore_rolling(close, 160) + _zscore_rolling(volume, 160)) / 2
    return _safe_div(base, _rolling_std(base, 63))

def dsen_554_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 121 distress score ensemble for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = (_zscore_rolling(close, 160) + _zscore_rolling(volume, 160)) / 2
    return _safe_div(base, _rolling_std(base, 126))

def dsen_555_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 121 distress score ensemble for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = (_zscore_rolling(close, 160) + _zscore_rolling(volume, 160)) / 2
    return _safe_div(base, _rolling_std(base, 252))

def dsen_556_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 121 distress score ensemble over 5d to stabilize variance and capture exponential shifts.
    """
    base = (_zscore_rolling(close, 160) + _zscore_rolling(volume, 160)) / 2
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def dsen_557_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 121 distress score ensemble over 21d to stabilize variance and capture exponential shifts.
    """
    base = (_zscore_rolling(close, 160) + _zscore_rolling(volume, 160)) / 2
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def dsen_558_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 121 distress score ensemble over 63d to stabilize variance and capture exponential shifts.
    """
    base = (_zscore_rolling(close, 160) + _zscore_rolling(volume, 160)) / 2
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def dsen_559_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 121 distress score ensemble over 126d to stabilize variance and capture exponential shifts.
    """
    base = (_zscore_rolling(close, 160) + _zscore_rolling(volume, 160)) / 2
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def dsen_560_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 121 distress score ensemble over 252d to stabilize variance and capture exponential shifts.
    """
    base = (_zscore_rolling(close, 160) + _zscore_rolling(volume, 160)) / 2
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def dsen_561_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 121 distress score ensemble over a 5d horizon to identify extreme regimes.
    """
    base = (_zscore_rolling(close, 170) + _zscore_rolling(volume, 170)) / 2
    return _rolling_mean(base, 5)

def dsen_562_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 121 distress score ensemble over a 21d horizon to identify extreme regimes.
    """
    base = (_zscore_rolling(close, 170) + _zscore_rolling(volume, 170)) / 2
    return _rolling_mean(base, 21)

def dsen_563_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 121 distress score ensemble over a 63d horizon to identify extreme regimes.
    """
    base = (_zscore_rolling(close, 170) + _zscore_rolling(volume, 170)) / 2
    return _rolling_mean(base, 63)

def dsen_564_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 121 distress score ensemble over a 126d horizon to identify extreme regimes.
    """
    base = (_zscore_rolling(close, 170) + _zscore_rolling(volume, 170)) / 2
    return _rolling_mean(base, 126)

def dsen_565_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 121 distress score ensemble over a 252d horizon to identify extreme regimes.
    """
    base = (_zscore_rolling(close, 170) + _zscore_rolling(volume, 170)) / 2
    return _rolling_mean(base, 252)

def dsen_566_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 121 distress score ensemble by measuring deviations from the 5d mean.
    """
    base = (_zscore_rolling(close, 170) + _zscore_rolling(volume, 170)) / 2
    return _zscore_rolling(base, 5)

def dsen_567_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 121 distress score ensemble by measuring deviations from the 21d mean.
    """
    base = (_zscore_rolling(close, 170) + _zscore_rolling(volume, 170)) / 2
    return _zscore_rolling(base, 21)

def dsen_568_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 121 distress score ensemble by measuring deviations from the 63d mean.
    """
    base = (_zscore_rolling(close, 170) + _zscore_rolling(volume, 170)) / 2
    return _zscore_rolling(base, 63)

def dsen_569_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 121 distress score ensemble by measuring deviations from the 126d mean.
    """
    base = (_zscore_rolling(close, 170) + _zscore_rolling(volume, 170)) / 2
    return _zscore_rolling(base, 126)

def dsen_570_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 121 distress score ensemble by measuring deviations from the 252d mean.
    """
    base = (_zscore_rolling(close, 170) + _zscore_rolling(volume, 170)) / 2
    return _zscore_rolling(base, 252)

def dsen_571_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 121 distress score ensemble to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = (_zscore_rolling(close, 170) + _zscore_rolling(volume, 170)) / 2
    return _rank_pct(base, 5)

def dsen_572_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 121 distress score ensemble to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = (_zscore_rolling(close, 170) + _zscore_rolling(volume, 170)) / 2
    return _rank_pct(base, 21)

def dsen_573_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 121 distress score ensemble to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = (_zscore_rolling(close, 170) + _zscore_rolling(volume, 170)) / 2
    return _rank_pct(base, 63)

def dsen_574_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 121 distress score ensemble to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = (_zscore_rolling(close, 170) + _zscore_rolling(volume, 170)) / 2
    return _rank_pct(base, 126)

def dsen_575_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 121 distress score ensemble to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = (_zscore_rolling(close, 170) + _zscore_rolling(volume, 170)) / 2
    return _rank_pct(base, 252)

def dsen_576_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 121 distress score ensemble distribution over 5d to detect tail risk or exhaustion.
    """
    base = (_zscore_rolling(close, 170) + _zscore_rolling(volume, 170)) / 2
    return _rolling_skew(base, 5)

def dsen_577_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 121 distress score ensemble distribution over 21d to detect tail risk or exhaustion.
    """
    base = (_zscore_rolling(close, 170) + _zscore_rolling(volume, 170)) / 2
    return _rolling_skew(base, 21)

def dsen_578_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 121 distress score ensemble distribution over 63d to detect tail risk or exhaustion.
    """
    base = (_zscore_rolling(close, 170) + _zscore_rolling(volume, 170)) / 2
    return _rolling_skew(base, 63)

def dsen_579_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 121 distress score ensemble distribution over 126d to detect tail risk or exhaustion.
    """
    base = (_zscore_rolling(close, 170) + _zscore_rolling(volume, 170)) / 2
    return _rolling_skew(base, 126)

def dsen_580_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 121 distress score ensemble distribution over 252d to detect tail risk or exhaustion.
    """
    base = (_zscore_rolling(close, 170) + _zscore_rolling(volume, 170)) / 2
    return _rolling_skew(base, 252)

def dsen_581_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 121 distress score ensemble over 5d to capture explosive breakdown or reversal points.
    """
    base = (_zscore_rolling(close, 170) + _zscore_rolling(volume, 170)) / 2
    return _rolling_kurt(base, 5)

def dsen_582_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 121 distress score ensemble over 21d to capture explosive breakdown or reversal points.
    """
    base = (_zscore_rolling(close, 170) + _zscore_rolling(volume, 170)) / 2
    return _rolling_kurt(base, 21)

def dsen_583_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 121 distress score ensemble over 63d to capture explosive breakdown or reversal points.
    """
    base = (_zscore_rolling(close, 170) + _zscore_rolling(volume, 170)) / 2
    return _rolling_kurt(base, 63)

def dsen_584_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 121 distress score ensemble over 126d to capture explosive breakdown or reversal points.
    """
    base = (_zscore_rolling(close, 170) + _zscore_rolling(volume, 170)) / 2
    return _rolling_kurt(base, 126)

def dsen_585_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 121 distress score ensemble over 252d to capture explosive breakdown or reversal points.
    """
    base = (_zscore_rolling(close, 170) + _zscore_rolling(volume, 170)) / 2
    return _rolling_kurt(base, 252)

def dsen_586_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 121 distress score ensemble for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = (_zscore_rolling(close, 170) + _zscore_rolling(volume, 170)) / 2
    return _safe_div(base, _rolling_std(base, 5))

def dsen_587_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 121 distress score ensemble for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = (_zscore_rolling(close, 170) + _zscore_rolling(volume, 170)) / 2
    return _safe_div(base, _rolling_std(base, 21))

def dsen_588_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 121 distress score ensemble for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = (_zscore_rolling(close, 170) + _zscore_rolling(volume, 170)) / 2
    return _safe_div(base, _rolling_std(base, 63))

def dsen_589_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 121 distress score ensemble for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = (_zscore_rolling(close, 170) + _zscore_rolling(volume, 170)) / 2
    return _safe_div(base, _rolling_std(base, 126))

def dsen_590_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 121 distress score ensemble for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = (_zscore_rolling(close, 170) + _zscore_rolling(volume, 170)) / 2
    return _safe_div(base, _rolling_std(base, 252))

def dsen_591_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 121 distress score ensemble over 5d to stabilize variance and capture exponential shifts.
    """
    base = (_zscore_rolling(close, 170) + _zscore_rolling(volume, 170)) / 2
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def dsen_592_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 121 distress score ensemble over 21d to stabilize variance and capture exponential shifts.
    """
    base = (_zscore_rolling(close, 170) + _zscore_rolling(volume, 170)) / 2
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def dsen_593_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 121 distress score ensemble over 63d to stabilize variance and capture exponential shifts.
    """
    base = (_zscore_rolling(close, 170) + _zscore_rolling(volume, 170)) / 2
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def dsen_594_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 121 distress score ensemble over 126d to stabilize variance and capture exponential shifts.
    """
    base = (_zscore_rolling(close, 170) + _zscore_rolling(volume, 170)) / 2
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def dsen_595_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 121 distress score ensemble over 252d to stabilize variance and capture exponential shifts.
    """
    base = (_zscore_rolling(close, 170) + _zscore_rolling(volume, 170)) / 2
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def dsen_596_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 121 distress score ensemble over a 5d horizon to identify extreme regimes.
    """
    base = (_zscore_rolling(close, 180) + _zscore_rolling(volume, 180)) / 2
    return _rolling_mean(base, 5)

def dsen_597_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 121 distress score ensemble over a 21d horizon to identify extreme regimes.
    """
    base = (_zscore_rolling(close, 180) + _zscore_rolling(volume, 180)) / 2
    return _rolling_mean(base, 21)

def dsen_598_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 121 distress score ensemble over a 63d horizon to identify extreme regimes.
    """
    base = (_zscore_rolling(close, 180) + _zscore_rolling(volume, 180)) / 2
    return _rolling_mean(base, 63)

def dsen_599_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 121 distress score ensemble over a 126d horizon to identify extreme regimes.
    """
    base = (_zscore_rolling(close, 180) + _zscore_rolling(volume, 180)) / 2
    return _rolling_mean(base, 126)

def dsen_600_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 121 distress score ensemble over a 252d horizon to identify extreme regimes.
    """
    base = (_zscore_rolling(close, 180) + _zscore_rolling(volume, 180)) / 2
    return _rolling_mean(base, 252)
