"""
123_123_relative_weakness_xs — Base Features 526-600
Domain: 123_relative_weakness_xs
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

def rwxs_526_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 123 relative weakness xs over a 5d horizon to identify extreme regimes.
    """
    base = close.pct_change(320)
    return _rolling_mean(base, 5)

def rwxs_527_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 123 relative weakness xs over a 21d horizon to identify extreme regimes.
    """
    base = close.pct_change(320)
    return _rolling_mean(base, 21)

def rwxs_528_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 123 relative weakness xs over a 63d horizon to identify extreme regimes.
    """
    base = close.pct_change(320)
    return _rolling_mean(base, 63)

def rwxs_529_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 123 relative weakness xs over a 126d horizon to identify extreme regimes.
    """
    base = close.pct_change(320)
    return _rolling_mean(base, 126)

def rwxs_530_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 123 relative weakness xs over a 252d horizon to identify extreme regimes.
    """
    base = close.pct_change(320)
    return _rolling_mean(base, 252)

def rwxs_531_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 123 relative weakness xs by measuring deviations from the 5d mean.
    """
    base = close.pct_change(320)
    return _zscore_rolling(base, 5)

def rwxs_532_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 123 relative weakness xs by measuring deviations from the 21d mean.
    """
    base = close.pct_change(320)
    return _zscore_rolling(base, 21)

def rwxs_533_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 123 relative weakness xs by measuring deviations from the 63d mean.
    """
    base = close.pct_change(320)
    return _zscore_rolling(base, 63)

def rwxs_534_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 123 relative weakness xs by measuring deviations from the 126d mean.
    """
    base = close.pct_change(320)
    return _zscore_rolling(base, 126)

def rwxs_535_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 123 relative weakness xs by measuring deviations from the 252d mean.
    """
    base = close.pct_change(320)
    return _zscore_rolling(base, 252)

def rwxs_536_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 123 relative weakness xs to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = close.pct_change(320)
    return _rank_pct(base, 5)

def rwxs_537_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 123 relative weakness xs to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = close.pct_change(320)
    return _rank_pct(base, 21)

def rwxs_538_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 123 relative weakness xs to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = close.pct_change(320)
    return _rank_pct(base, 63)

def rwxs_539_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 123 relative weakness xs to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = close.pct_change(320)
    return _rank_pct(base, 126)

def rwxs_540_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 123 relative weakness xs to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = close.pct_change(320)
    return _rank_pct(base, 252)

def rwxs_541_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 123 relative weakness xs distribution over 5d to detect tail risk or exhaustion.
    """
    base = close.pct_change(320)
    return _rolling_skew(base, 5)

def rwxs_542_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 123 relative weakness xs distribution over 21d to detect tail risk or exhaustion.
    """
    base = close.pct_change(320)
    return _rolling_skew(base, 21)

def rwxs_543_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 123 relative weakness xs distribution over 63d to detect tail risk or exhaustion.
    """
    base = close.pct_change(320)
    return _rolling_skew(base, 63)

def rwxs_544_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 123 relative weakness xs distribution over 126d to detect tail risk or exhaustion.
    """
    base = close.pct_change(320)
    return _rolling_skew(base, 126)

def rwxs_545_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 123 relative weakness xs distribution over 252d to detect tail risk or exhaustion.
    """
    base = close.pct_change(320)
    return _rolling_skew(base, 252)

def rwxs_546_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 123 relative weakness xs over 5d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change(320)
    return _rolling_kurt(base, 5)

def rwxs_547_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 123 relative weakness xs over 21d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change(320)
    return _rolling_kurt(base, 21)

def rwxs_548_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 123 relative weakness xs over 63d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change(320)
    return _rolling_kurt(base, 63)

def rwxs_549_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 123 relative weakness xs over 126d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change(320)
    return _rolling_kurt(base, 126)

def rwxs_550_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 123 relative weakness xs over 252d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change(320)
    return _rolling_kurt(base, 252)

def rwxs_551_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 123 relative weakness xs for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change(320)
    return _safe_div(base, _rolling_std(base, 5))

def rwxs_552_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 123 relative weakness xs for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change(320)
    return _safe_div(base, _rolling_std(base, 21))

def rwxs_553_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 123 relative weakness xs for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change(320)
    return _safe_div(base, _rolling_std(base, 63))

def rwxs_554_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 123 relative weakness xs for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change(320)
    return _safe_div(base, _rolling_std(base, 126))

def rwxs_555_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 123 relative weakness xs for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change(320)
    return _safe_div(base, _rolling_std(base, 252))

def rwxs_556_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 123 relative weakness xs over 5d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change(320)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def rwxs_557_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 123 relative weakness xs over 21d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change(320)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def rwxs_558_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 123 relative weakness xs over 63d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change(320)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def rwxs_559_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 123 relative weakness xs over 126d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change(320)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def rwxs_560_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 123 relative weakness xs over 252d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change(320)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def rwxs_561_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 123 relative weakness xs over a 5d horizon to identify extreme regimes.
    """
    base = close.pct_change(340)
    return _rolling_mean(base, 5)

def rwxs_562_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 123 relative weakness xs over a 21d horizon to identify extreme regimes.
    """
    base = close.pct_change(340)
    return _rolling_mean(base, 21)

def rwxs_563_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 123 relative weakness xs over a 63d horizon to identify extreme regimes.
    """
    base = close.pct_change(340)
    return _rolling_mean(base, 63)

def rwxs_564_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 123 relative weakness xs over a 126d horizon to identify extreme regimes.
    """
    base = close.pct_change(340)
    return _rolling_mean(base, 126)

def rwxs_565_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 123 relative weakness xs over a 252d horizon to identify extreme regimes.
    """
    base = close.pct_change(340)
    return _rolling_mean(base, 252)

def rwxs_566_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 123 relative weakness xs by measuring deviations from the 5d mean.
    """
    base = close.pct_change(340)
    return _zscore_rolling(base, 5)

def rwxs_567_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 123 relative weakness xs by measuring deviations from the 21d mean.
    """
    base = close.pct_change(340)
    return _zscore_rolling(base, 21)

def rwxs_568_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 123 relative weakness xs by measuring deviations from the 63d mean.
    """
    base = close.pct_change(340)
    return _zscore_rolling(base, 63)

def rwxs_569_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 123 relative weakness xs by measuring deviations from the 126d mean.
    """
    base = close.pct_change(340)
    return _zscore_rolling(base, 126)

def rwxs_570_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 123 relative weakness xs by measuring deviations from the 252d mean.
    """
    base = close.pct_change(340)
    return _zscore_rolling(base, 252)

def rwxs_571_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 123 relative weakness xs to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = close.pct_change(340)
    return _rank_pct(base, 5)

def rwxs_572_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 123 relative weakness xs to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = close.pct_change(340)
    return _rank_pct(base, 21)

def rwxs_573_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 123 relative weakness xs to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = close.pct_change(340)
    return _rank_pct(base, 63)

def rwxs_574_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 123 relative weakness xs to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = close.pct_change(340)
    return _rank_pct(base, 126)

def rwxs_575_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 123 relative weakness xs to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = close.pct_change(340)
    return _rank_pct(base, 252)

def rwxs_576_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 123 relative weakness xs distribution over 5d to detect tail risk or exhaustion.
    """
    base = close.pct_change(340)
    return _rolling_skew(base, 5)

def rwxs_577_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 123 relative weakness xs distribution over 21d to detect tail risk or exhaustion.
    """
    base = close.pct_change(340)
    return _rolling_skew(base, 21)

def rwxs_578_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 123 relative weakness xs distribution over 63d to detect tail risk or exhaustion.
    """
    base = close.pct_change(340)
    return _rolling_skew(base, 63)

def rwxs_579_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 123 relative weakness xs distribution over 126d to detect tail risk or exhaustion.
    """
    base = close.pct_change(340)
    return _rolling_skew(base, 126)

def rwxs_580_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 123 relative weakness xs distribution over 252d to detect tail risk or exhaustion.
    """
    base = close.pct_change(340)
    return _rolling_skew(base, 252)

def rwxs_581_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 123 relative weakness xs over 5d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change(340)
    return _rolling_kurt(base, 5)

def rwxs_582_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 123 relative weakness xs over 21d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change(340)
    return _rolling_kurt(base, 21)

def rwxs_583_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 123 relative weakness xs over 63d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change(340)
    return _rolling_kurt(base, 63)

def rwxs_584_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 123 relative weakness xs over 126d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change(340)
    return _rolling_kurt(base, 126)

def rwxs_585_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 123 relative weakness xs over 252d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change(340)
    return _rolling_kurt(base, 252)

def rwxs_586_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 123 relative weakness xs for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change(340)
    return _safe_div(base, _rolling_std(base, 5))

def rwxs_587_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 123 relative weakness xs for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change(340)
    return _safe_div(base, _rolling_std(base, 21))

def rwxs_588_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 123 relative weakness xs for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change(340)
    return _safe_div(base, _rolling_std(base, 63))

def rwxs_589_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 123 relative weakness xs for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change(340)
    return _safe_div(base, _rolling_std(base, 126))

def rwxs_590_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 123 relative weakness xs for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change(340)
    return _safe_div(base, _rolling_std(base, 252))

def rwxs_591_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 123 relative weakness xs over 5d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change(340)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def rwxs_592_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 123 relative weakness xs over 21d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change(340)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def rwxs_593_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 123 relative weakness xs over 63d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change(340)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def rwxs_594_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 123 relative weakness xs over 126d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change(340)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def rwxs_595_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 123 relative weakness xs over 252d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change(340)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def rwxs_596_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 123 relative weakness xs over a 5d horizon to identify extreme regimes.
    """
    base = close.pct_change(360)
    return _rolling_mean(base, 5)

def rwxs_597_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 123 relative weakness xs over a 21d horizon to identify extreme regimes.
    """
    base = close.pct_change(360)
    return _rolling_mean(base, 21)

def rwxs_598_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 123 relative weakness xs over a 63d horizon to identify extreme regimes.
    """
    base = close.pct_change(360)
    return _rolling_mean(base, 63)

def rwxs_599_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 123 relative weakness xs over a 126d horizon to identify extreme regimes.
    """
    base = close.pct_change(360)
    return _rolling_mean(base, 126)

def rwxs_600_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 123 relative weakness xs over a 252d horizon to identify extreme regimes.
    """
    base = close.pct_change(360)
    return _rolling_mean(base, 252)
