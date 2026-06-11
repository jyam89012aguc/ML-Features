"""
102_102_seasonal_distress — Base Features 526-600
Domain: 102_seasonal_distress
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

def seas_526_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 102 seasonal distress over a 5d horizon to identify extreme regimes.
    """
    base = close.pct_change(80)
    return _rolling_mean(base, 5)

def seas_527_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 102 seasonal distress over a 21d horizon to identify extreme regimes.
    """
    base = close.pct_change(80)
    return _rolling_mean(base, 21)

def seas_528_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 102 seasonal distress over a 63d horizon to identify extreme regimes.
    """
    base = close.pct_change(80)
    return _rolling_mean(base, 63)

def seas_529_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 102 seasonal distress over a 126d horizon to identify extreme regimes.
    """
    base = close.pct_change(80)
    return _rolling_mean(base, 126)

def seas_530_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 102 seasonal distress over a 252d horizon to identify extreme regimes.
    """
    base = close.pct_change(80)
    return _rolling_mean(base, 252)

def seas_531_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 102 seasonal distress by measuring deviations from the 5d mean.
    """
    base = close.pct_change(80)
    return _zscore_rolling(base, 5)

def seas_532_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 102 seasonal distress by measuring deviations from the 21d mean.
    """
    base = close.pct_change(80)
    return _zscore_rolling(base, 21)

def seas_533_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 102 seasonal distress by measuring deviations from the 63d mean.
    """
    base = close.pct_change(80)
    return _zscore_rolling(base, 63)

def seas_534_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 102 seasonal distress by measuring deviations from the 126d mean.
    """
    base = close.pct_change(80)
    return _zscore_rolling(base, 126)

def seas_535_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 102 seasonal distress by measuring deviations from the 252d mean.
    """
    base = close.pct_change(80)
    return _zscore_rolling(base, 252)

def seas_536_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 102 seasonal distress to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = close.pct_change(80)
    return _rank_pct(base, 5)

def seas_537_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 102 seasonal distress to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = close.pct_change(80)
    return _rank_pct(base, 21)

def seas_538_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 102 seasonal distress to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = close.pct_change(80)
    return _rank_pct(base, 63)

def seas_539_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 102 seasonal distress to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = close.pct_change(80)
    return _rank_pct(base, 126)

def seas_540_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 102 seasonal distress to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = close.pct_change(80)
    return _rank_pct(base, 252)

def seas_541_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 102 seasonal distress distribution over 5d to detect tail risk or exhaustion.
    """
    base = close.pct_change(80)
    return _rolling_skew(base, 5)

def seas_542_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 102 seasonal distress distribution over 21d to detect tail risk or exhaustion.
    """
    base = close.pct_change(80)
    return _rolling_skew(base, 21)

def seas_543_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 102 seasonal distress distribution over 63d to detect tail risk or exhaustion.
    """
    base = close.pct_change(80)
    return _rolling_skew(base, 63)

def seas_544_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 102 seasonal distress distribution over 126d to detect tail risk or exhaustion.
    """
    base = close.pct_change(80)
    return _rolling_skew(base, 126)

def seas_545_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 102 seasonal distress distribution over 252d to detect tail risk or exhaustion.
    """
    base = close.pct_change(80)
    return _rolling_skew(base, 252)

def seas_546_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 102 seasonal distress over 5d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change(80)
    return _rolling_kurt(base, 5)

def seas_547_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 102 seasonal distress over 21d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change(80)
    return _rolling_kurt(base, 21)

def seas_548_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 102 seasonal distress over 63d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change(80)
    return _rolling_kurt(base, 63)

def seas_549_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 102 seasonal distress over 126d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change(80)
    return _rolling_kurt(base, 126)

def seas_550_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 102 seasonal distress over 252d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change(80)
    return _rolling_kurt(base, 252)

def seas_551_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 102 seasonal distress for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change(80)
    return _safe_div(base, _rolling_std(base, 5))

def seas_552_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 102 seasonal distress for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change(80)
    return _safe_div(base, _rolling_std(base, 21))

def seas_553_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 102 seasonal distress for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change(80)
    return _safe_div(base, _rolling_std(base, 63))

def seas_554_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 102 seasonal distress for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change(80)
    return _safe_div(base, _rolling_std(base, 126))

def seas_555_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 102 seasonal distress for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change(80)
    return _safe_div(base, _rolling_std(base, 252))

def seas_556_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 102 seasonal distress over 5d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change(80)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def seas_557_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 102 seasonal distress over 21d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change(80)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def seas_558_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 102 seasonal distress over 63d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change(80)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def seas_559_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 102 seasonal distress over 126d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change(80)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def seas_560_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 102 seasonal distress over 252d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change(80)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def seas_561_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 102 seasonal distress over a 5d horizon to identify extreme regimes.
    """
    base = close.pct_change(85)
    return _rolling_mean(base, 5)

def seas_562_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 102 seasonal distress over a 21d horizon to identify extreme regimes.
    """
    base = close.pct_change(85)
    return _rolling_mean(base, 21)

def seas_563_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 102 seasonal distress over a 63d horizon to identify extreme regimes.
    """
    base = close.pct_change(85)
    return _rolling_mean(base, 63)

def seas_564_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 102 seasonal distress over a 126d horizon to identify extreme regimes.
    """
    base = close.pct_change(85)
    return _rolling_mean(base, 126)

def seas_565_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 102 seasonal distress over a 252d horizon to identify extreme regimes.
    """
    base = close.pct_change(85)
    return _rolling_mean(base, 252)

def seas_566_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 102 seasonal distress by measuring deviations from the 5d mean.
    """
    base = close.pct_change(85)
    return _zscore_rolling(base, 5)

def seas_567_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 102 seasonal distress by measuring deviations from the 21d mean.
    """
    base = close.pct_change(85)
    return _zscore_rolling(base, 21)

def seas_568_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 102 seasonal distress by measuring deviations from the 63d mean.
    """
    base = close.pct_change(85)
    return _zscore_rolling(base, 63)

def seas_569_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 102 seasonal distress by measuring deviations from the 126d mean.
    """
    base = close.pct_change(85)
    return _zscore_rolling(base, 126)

def seas_570_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 102 seasonal distress by measuring deviations from the 252d mean.
    """
    base = close.pct_change(85)
    return _zscore_rolling(base, 252)

def seas_571_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 102 seasonal distress to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = close.pct_change(85)
    return _rank_pct(base, 5)

def seas_572_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 102 seasonal distress to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = close.pct_change(85)
    return _rank_pct(base, 21)

def seas_573_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 102 seasonal distress to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = close.pct_change(85)
    return _rank_pct(base, 63)

def seas_574_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 102 seasonal distress to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = close.pct_change(85)
    return _rank_pct(base, 126)

def seas_575_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 102 seasonal distress to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = close.pct_change(85)
    return _rank_pct(base, 252)

def seas_576_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 102 seasonal distress distribution over 5d to detect tail risk or exhaustion.
    """
    base = close.pct_change(85)
    return _rolling_skew(base, 5)

def seas_577_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 102 seasonal distress distribution over 21d to detect tail risk or exhaustion.
    """
    base = close.pct_change(85)
    return _rolling_skew(base, 21)

def seas_578_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 102 seasonal distress distribution over 63d to detect tail risk or exhaustion.
    """
    base = close.pct_change(85)
    return _rolling_skew(base, 63)

def seas_579_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 102 seasonal distress distribution over 126d to detect tail risk or exhaustion.
    """
    base = close.pct_change(85)
    return _rolling_skew(base, 126)

def seas_580_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 102 seasonal distress distribution over 252d to detect tail risk or exhaustion.
    """
    base = close.pct_change(85)
    return _rolling_skew(base, 252)

def seas_581_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 102 seasonal distress over 5d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change(85)
    return _rolling_kurt(base, 5)

def seas_582_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 102 seasonal distress over 21d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change(85)
    return _rolling_kurt(base, 21)

def seas_583_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 102 seasonal distress over 63d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change(85)
    return _rolling_kurt(base, 63)

def seas_584_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 102 seasonal distress over 126d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change(85)
    return _rolling_kurt(base, 126)

def seas_585_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 102 seasonal distress over 252d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change(85)
    return _rolling_kurt(base, 252)

def seas_586_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 102 seasonal distress for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change(85)
    return _safe_div(base, _rolling_std(base, 5))

def seas_587_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 102 seasonal distress for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change(85)
    return _safe_div(base, _rolling_std(base, 21))

def seas_588_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 102 seasonal distress for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change(85)
    return _safe_div(base, _rolling_std(base, 63))

def seas_589_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 102 seasonal distress for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change(85)
    return _safe_div(base, _rolling_std(base, 126))

def seas_590_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 102 seasonal distress for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change(85)
    return _safe_div(base, _rolling_std(base, 252))

def seas_591_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 102 seasonal distress over 5d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change(85)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def seas_592_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 102 seasonal distress over 21d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change(85)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def seas_593_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 102 seasonal distress over 63d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change(85)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def seas_594_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 102 seasonal distress over 126d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change(85)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def seas_595_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 102 seasonal distress over 252d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change(85)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def seas_596_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 102 seasonal distress over a 5d horizon to identify extreme regimes.
    """
    base = close.pct_change(90)
    return _rolling_mean(base, 5)

def seas_597_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 102 seasonal distress over a 21d horizon to identify extreme regimes.
    """
    base = close.pct_change(90)
    return _rolling_mean(base, 21)

def seas_598_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 102 seasonal distress over a 63d horizon to identify extreme regimes.
    """
    base = close.pct_change(90)
    return _rolling_mean(base, 63)

def seas_599_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 102 seasonal distress over a 126d horizon to identify extreme regimes.
    """
    base = close.pct_change(90)
    return _rolling_mean(base, 126)

def seas_600_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 102 seasonal distress over a 252d horizon to identify extreme regimes.
    """
    base = close.pct_change(90)
    return _rolling_mean(base, 252)
