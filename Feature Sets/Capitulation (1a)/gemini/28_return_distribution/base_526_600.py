"""
28_28_return_distribution — Base Features 526-600
Domain: 28_return_distribution
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

def rdis_526_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 28 return distribution over a 5d horizon to identify extreme regimes.
    """
    base = (close.pct_change(16).rolling(80).mean())
    return _rolling_mean(base, 5)

def rdis_527_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 28 return distribution over a 21d horizon to identify extreme regimes.
    """
    base = (close.pct_change(16).rolling(80).mean())
    return _rolling_mean(base, 21)

def rdis_528_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 28 return distribution over a 63d horizon to identify extreme regimes.
    """
    base = (close.pct_change(16).rolling(80).mean())
    return _rolling_mean(base, 63)

def rdis_529_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 28 return distribution over a 126d horizon to identify extreme regimes.
    """
    base = (close.pct_change(16).rolling(80).mean())
    return _rolling_mean(base, 126)

def rdis_530_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 28 return distribution over a 252d horizon to identify extreme regimes.
    """
    base = (close.pct_change(16).rolling(80).mean())
    return _rolling_mean(base, 252)

def rdis_531_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 28 return distribution by measuring deviations from the 5d mean.
    """
    base = (close.pct_change(16).rolling(80).mean())
    return _zscore_rolling(base, 5)

def rdis_532_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 28 return distribution by measuring deviations from the 21d mean.
    """
    base = (close.pct_change(16).rolling(80).mean())
    return _zscore_rolling(base, 21)

def rdis_533_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 28 return distribution by measuring deviations from the 63d mean.
    """
    base = (close.pct_change(16).rolling(80).mean())
    return _zscore_rolling(base, 63)

def rdis_534_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 28 return distribution by measuring deviations from the 126d mean.
    """
    base = (close.pct_change(16).rolling(80).mean())
    return _zscore_rolling(base, 126)

def rdis_535_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 28 return distribution by measuring deviations from the 252d mean.
    """
    base = (close.pct_change(16).rolling(80).mean())
    return _zscore_rolling(base, 252)

def rdis_536_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 28 return distribution to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = (close.pct_change(16).rolling(80).mean())
    return _rank_pct(base, 5)

def rdis_537_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 28 return distribution to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = (close.pct_change(16).rolling(80).mean())
    return _rank_pct(base, 21)

def rdis_538_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 28 return distribution to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = (close.pct_change(16).rolling(80).mean())
    return _rank_pct(base, 63)

def rdis_539_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 28 return distribution to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = (close.pct_change(16).rolling(80).mean())
    return _rank_pct(base, 126)

def rdis_540_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 28 return distribution to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = (close.pct_change(16).rolling(80).mean())
    return _rank_pct(base, 252)

def rdis_541_skew_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 28 return distribution distribution over 5d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(16).rolling(80).mean())
    return _rolling_skew(base, 5)

def rdis_542_skew_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 28 return distribution distribution over 21d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(16).rolling(80).mean())
    return _rolling_skew(base, 21)

def rdis_543_skew_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 28 return distribution distribution over 63d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(16).rolling(80).mean())
    return _rolling_skew(base, 63)

def rdis_544_skew_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 28 return distribution distribution over 126d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(16).rolling(80).mean())
    return _rolling_skew(base, 126)

def rdis_545_skew_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 28 return distribution distribution over 252d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(16).rolling(80).mean())
    return _rolling_skew(base, 252)

def rdis_546_kurt_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 28 return distribution over 5d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(16).rolling(80).mean())
    return _rolling_kurt(base, 5)

def rdis_547_kurt_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 28 return distribution over 21d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(16).rolling(80).mean())
    return _rolling_kurt(base, 21)

def rdis_548_kurt_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 28 return distribution over 63d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(16).rolling(80).mean())
    return _rolling_kurt(base, 63)

def rdis_549_kurt_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 28 return distribution over 126d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(16).rolling(80).mean())
    return _rolling_kurt(base, 126)

def rdis_550_kurt_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 28 return distribution over 252d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(16).rolling(80).mean())
    return _rolling_kurt(base, 252)

def rdis_551_voladj_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 28 return distribution for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(16).rolling(80).mean())
    return _safe_div(base, _rolling_std(base, 5))

def rdis_552_voladj_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 28 return distribution for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(16).rolling(80).mean())
    return _safe_div(base, _rolling_std(base, 21))

def rdis_553_voladj_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 28 return distribution for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(16).rolling(80).mean())
    return _safe_div(base, _rolling_std(base, 63))

def rdis_554_voladj_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 28 return distribution for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(16).rolling(80).mean())
    return _safe_div(base, _rolling_std(base, 126))

def rdis_555_voladj_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 28 return distribution for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(16).rolling(80).mean())
    return _safe_div(base, _rolling_std(base, 252))

def rdis_556_lognorm_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 28 return distribution over 5d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(16).rolling(80).mean())
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def rdis_557_lognorm_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 28 return distribution over 21d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(16).rolling(80).mean())
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def rdis_558_lognorm_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 28 return distribution over 63d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(16).rolling(80).mean())
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def rdis_559_lognorm_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 28 return distribution over 126d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(16).rolling(80).mean())
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def rdis_560_lognorm_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 28 return distribution over 252d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(16).rolling(80).mean())
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def rdis_561_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 28 return distribution over a 5d horizon to identify extreme regimes.
    """
    base = (close.pct_change(17).rolling(85).mean())
    return _rolling_mean(base, 5)

def rdis_562_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 28 return distribution over a 21d horizon to identify extreme regimes.
    """
    base = (close.pct_change(17).rolling(85).mean())
    return _rolling_mean(base, 21)

def rdis_563_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 28 return distribution over a 63d horizon to identify extreme regimes.
    """
    base = (close.pct_change(17).rolling(85).mean())
    return _rolling_mean(base, 63)

def rdis_564_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 28 return distribution over a 126d horizon to identify extreme regimes.
    """
    base = (close.pct_change(17).rolling(85).mean())
    return _rolling_mean(base, 126)

def rdis_565_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 28 return distribution over a 252d horizon to identify extreme regimes.
    """
    base = (close.pct_change(17).rolling(85).mean())
    return _rolling_mean(base, 252)

def rdis_566_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 28 return distribution by measuring deviations from the 5d mean.
    """
    base = (close.pct_change(17).rolling(85).mean())
    return _zscore_rolling(base, 5)

def rdis_567_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 28 return distribution by measuring deviations from the 21d mean.
    """
    base = (close.pct_change(17).rolling(85).mean())
    return _zscore_rolling(base, 21)

def rdis_568_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 28 return distribution by measuring deviations from the 63d mean.
    """
    base = (close.pct_change(17).rolling(85).mean())
    return _zscore_rolling(base, 63)

def rdis_569_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 28 return distribution by measuring deviations from the 126d mean.
    """
    base = (close.pct_change(17).rolling(85).mean())
    return _zscore_rolling(base, 126)

def rdis_570_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 28 return distribution by measuring deviations from the 252d mean.
    """
    base = (close.pct_change(17).rolling(85).mean())
    return _zscore_rolling(base, 252)

def rdis_571_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 28 return distribution to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = (close.pct_change(17).rolling(85).mean())
    return _rank_pct(base, 5)

def rdis_572_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 28 return distribution to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = (close.pct_change(17).rolling(85).mean())
    return _rank_pct(base, 21)

def rdis_573_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 28 return distribution to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = (close.pct_change(17).rolling(85).mean())
    return _rank_pct(base, 63)

def rdis_574_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 28 return distribution to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = (close.pct_change(17).rolling(85).mean())
    return _rank_pct(base, 126)

def rdis_575_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 28 return distribution to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = (close.pct_change(17).rolling(85).mean())
    return _rank_pct(base, 252)

def rdis_576_skew_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 28 return distribution distribution over 5d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(17).rolling(85).mean())
    return _rolling_skew(base, 5)

def rdis_577_skew_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 28 return distribution distribution over 21d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(17).rolling(85).mean())
    return _rolling_skew(base, 21)

def rdis_578_skew_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 28 return distribution distribution over 63d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(17).rolling(85).mean())
    return _rolling_skew(base, 63)

def rdis_579_skew_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 28 return distribution distribution over 126d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(17).rolling(85).mean())
    return _rolling_skew(base, 126)

def rdis_580_skew_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 28 return distribution distribution over 252d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(17).rolling(85).mean())
    return _rolling_skew(base, 252)

def rdis_581_kurt_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 28 return distribution over 5d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(17).rolling(85).mean())
    return _rolling_kurt(base, 5)

def rdis_582_kurt_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 28 return distribution over 21d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(17).rolling(85).mean())
    return _rolling_kurt(base, 21)

def rdis_583_kurt_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 28 return distribution over 63d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(17).rolling(85).mean())
    return _rolling_kurt(base, 63)

def rdis_584_kurt_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 28 return distribution over 126d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(17).rolling(85).mean())
    return _rolling_kurt(base, 126)

def rdis_585_kurt_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 28 return distribution over 252d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(17).rolling(85).mean())
    return _rolling_kurt(base, 252)

def rdis_586_voladj_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 28 return distribution for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(17).rolling(85).mean())
    return _safe_div(base, _rolling_std(base, 5))

def rdis_587_voladj_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 28 return distribution for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(17).rolling(85).mean())
    return _safe_div(base, _rolling_std(base, 21))

def rdis_588_voladj_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 28 return distribution for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(17).rolling(85).mean())
    return _safe_div(base, _rolling_std(base, 63))

def rdis_589_voladj_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 28 return distribution for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(17).rolling(85).mean())
    return _safe_div(base, _rolling_std(base, 126))

def rdis_590_voladj_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 28 return distribution for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(17).rolling(85).mean())
    return _safe_div(base, _rolling_std(base, 252))

def rdis_591_lognorm_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 28 return distribution over 5d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(17).rolling(85).mean())
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def rdis_592_lognorm_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 28 return distribution over 21d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(17).rolling(85).mean())
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def rdis_593_lognorm_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 28 return distribution over 63d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(17).rolling(85).mean())
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def rdis_594_lognorm_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 28 return distribution over 126d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(17).rolling(85).mean())
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def rdis_595_lognorm_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 28 return distribution over 252d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(17).rolling(85).mean())
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def rdis_596_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 28 return distribution over a 5d horizon to identify extreme regimes.
    """
    base = (close.pct_change(18).rolling(90).mean())
    return _rolling_mean(base, 5)

def rdis_597_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 28 return distribution over a 21d horizon to identify extreme regimes.
    """
    base = (close.pct_change(18).rolling(90).mean())
    return _rolling_mean(base, 21)

def rdis_598_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 28 return distribution over a 63d horizon to identify extreme regimes.
    """
    base = (close.pct_change(18).rolling(90).mean())
    return _rolling_mean(base, 63)

def rdis_599_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 28 return distribution over a 126d horizon to identify extreme regimes.
    """
    base = (close.pct_change(18).rolling(90).mean())
    return _rolling_mean(base, 126)

def rdis_600_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 28 return distribution over a 252d horizon to identify extreme regimes.
    """
    base = (close.pct_change(18).rolling(90).mean())
    return _rolling_mean(base, 252)
