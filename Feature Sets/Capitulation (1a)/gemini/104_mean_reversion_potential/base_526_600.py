"""
104_104_mean_reversion_potential — Base Features 526-600
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

def mrpt_526_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 104 mean reversion potential over a 5d horizon to identify extreme regimes.
    """
    base = close / _rolling_mean(close, 305) - 1
    return _rolling_mean(base, 5)

def mrpt_527_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 104 mean reversion potential over a 21d horizon to identify extreme regimes.
    """
    base = close / _rolling_mean(close, 305) - 1
    return _rolling_mean(base, 21)

def mrpt_528_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 104 mean reversion potential over a 63d horizon to identify extreme regimes.
    """
    base = close / _rolling_mean(close, 305) - 1
    return _rolling_mean(base, 63)

def mrpt_529_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 104 mean reversion potential over a 126d horizon to identify extreme regimes.
    """
    base = close / _rolling_mean(close, 305) - 1
    return _rolling_mean(base, 126)

def mrpt_530_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 104 mean reversion potential over a 252d horizon to identify extreme regimes.
    """
    base = close / _rolling_mean(close, 305) - 1
    return _rolling_mean(base, 252)

def mrpt_531_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 104 mean reversion potential by measuring deviations from the 5d mean.
    """
    base = close / _rolling_mean(close, 305) - 1
    return _zscore_rolling(base, 5)

def mrpt_532_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 104 mean reversion potential by measuring deviations from the 21d mean.
    """
    base = close / _rolling_mean(close, 305) - 1
    return _zscore_rolling(base, 21)

def mrpt_533_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 104 mean reversion potential by measuring deviations from the 63d mean.
    """
    base = close / _rolling_mean(close, 305) - 1
    return _zscore_rolling(base, 63)

def mrpt_534_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 104 mean reversion potential by measuring deviations from the 126d mean.
    """
    base = close / _rolling_mean(close, 305) - 1
    return _zscore_rolling(base, 126)

def mrpt_535_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 104 mean reversion potential by measuring deviations from the 252d mean.
    """
    base = close / _rolling_mean(close, 305) - 1
    return _zscore_rolling(base, 252)

def mrpt_536_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 104 mean reversion potential to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = close / _rolling_mean(close, 305) - 1
    return _rank_pct(base, 5)

def mrpt_537_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 104 mean reversion potential to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = close / _rolling_mean(close, 305) - 1
    return _rank_pct(base, 21)

def mrpt_538_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 104 mean reversion potential to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = close / _rolling_mean(close, 305) - 1
    return _rank_pct(base, 63)

def mrpt_539_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 104 mean reversion potential to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = close / _rolling_mean(close, 305) - 1
    return _rank_pct(base, 126)

def mrpt_540_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 104 mean reversion potential to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = close / _rolling_mean(close, 305) - 1
    return _rank_pct(base, 252)

def mrpt_541_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 104 mean reversion potential distribution over 5d to detect tail risk or exhaustion.
    """
    base = close / _rolling_mean(close, 305) - 1
    return _rolling_skew(base, 5)

def mrpt_542_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 104 mean reversion potential distribution over 21d to detect tail risk or exhaustion.
    """
    base = close / _rolling_mean(close, 305) - 1
    return _rolling_skew(base, 21)

def mrpt_543_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 104 mean reversion potential distribution over 63d to detect tail risk or exhaustion.
    """
    base = close / _rolling_mean(close, 305) - 1
    return _rolling_skew(base, 63)

def mrpt_544_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 104 mean reversion potential distribution over 126d to detect tail risk or exhaustion.
    """
    base = close / _rolling_mean(close, 305) - 1
    return _rolling_skew(base, 126)

def mrpt_545_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 104 mean reversion potential distribution over 252d to detect tail risk or exhaustion.
    """
    base = close / _rolling_mean(close, 305) - 1
    return _rolling_skew(base, 252)

def mrpt_546_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 104 mean reversion potential over 5d to capture explosive breakdown or reversal points.
    """
    base = close / _rolling_mean(close, 305) - 1
    return _rolling_kurt(base, 5)

def mrpt_547_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 104 mean reversion potential over 21d to capture explosive breakdown or reversal points.
    """
    base = close / _rolling_mean(close, 305) - 1
    return _rolling_kurt(base, 21)

def mrpt_548_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 104 mean reversion potential over 63d to capture explosive breakdown or reversal points.
    """
    base = close / _rolling_mean(close, 305) - 1
    return _rolling_kurt(base, 63)

def mrpt_549_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 104 mean reversion potential over 126d to capture explosive breakdown or reversal points.
    """
    base = close / _rolling_mean(close, 305) - 1
    return _rolling_kurt(base, 126)

def mrpt_550_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 104 mean reversion potential over 252d to capture explosive breakdown or reversal points.
    """
    base = close / _rolling_mean(close, 305) - 1
    return _rolling_kurt(base, 252)

def mrpt_551_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 104 mean reversion potential for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = close / _rolling_mean(close, 305) - 1
    return _safe_div(base, _rolling_std(base, 5))

def mrpt_552_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 104 mean reversion potential for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = close / _rolling_mean(close, 305) - 1
    return _safe_div(base, _rolling_std(base, 21))

def mrpt_553_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 104 mean reversion potential for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = close / _rolling_mean(close, 305) - 1
    return _safe_div(base, _rolling_std(base, 63))

def mrpt_554_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 104 mean reversion potential for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = close / _rolling_mean(close, 305) - 1
    return _safe_div(base, _rolling_std(base, 126))

def mrpt_555_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 104 mean reversion potential for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = close / _rolling_mean(close, 305) - 1
    return _safe_div(base, _rolling_std(base, 252))

def mrpt_556_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 104 mean reversion potential over 5d to stabilize variance and capture exponential shifts.
    """
    base = close / _rolling_mean(close, 305) - 1
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def mrpt_557_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 104 mean reversion potential over 21d to stabilize variance and capture exponential shifts.
    """
    base = close / _rolling_mean(close, 305) - 1
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def mrpt_558_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 104 mean reversion potential over 63d to stabilize variance and capture exponential shifts.
    """
    base = close / _rolling_mean(close, 305) - 1
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def mrpt_559_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 104 mean reversion potential over 126d to stabilize variance and capture exponential shifts.
    """
    base = close / _rolling_mean(close, 305) - 1
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def mrpt_560_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 104 mean reversion potential over 252d to stabilize variance and capture exponential shifts.
    """
    base = close / _rolling_mean(close, 305) - 1
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def mrpt_561_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 104 mean reversion potential over a 5d horizon to identify extreme regimes.
    """
    base = close / _rolling_mean(close, 325) - 1
    return _rolling_mean(base, 5)

def mrpt_562_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 104 mean reversion potential over a 21d horizon to identify extreme regimes.
    """
    base = close / _rolling_mean(close, 325) - 1
    return _rolling_mean(base, 21)

def mrpt_563_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 104 mean reversion potential over a 63d horizon to identify extreme regimes.
    """
    base = close / _rolling_mean(close, 325) - 1
    return _rolling_mean(base, 63)

def mrpt_564_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 104 mean reversion potential over a 126d horizon to identify extreme regimes.
    """
    base = close / _rolling_mean(close, 325) - 1
    return _rolling_mean(base, 126)

def mrpt_565_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 104 mean reversion potential over a 252d horizon to identify extreme regimes.
    """
    base = close / _rolling_mean(close, 325) - 1
    return _rolling_mean(base, 252)

def mrpt_566_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 104 mean reversion potential by measuring deviations from the 5d mean.
    """
    base = close / _rolling_mean(close, 325) - 1
    return _zscore_rolling(base, 5)

def mrpt_567_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 104 mean reversion potential by measuring deviations from the 21d mean.
    """
    base = close / _rolling_mean(close, 325) - 1
    return _zscore_rolling(base, 21)

def mrpt_568_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 104 mean reversion potential by measuring deviations from the 63d mean.
    """
    base = close / _rolling_mean(close, 325) - 1
    return _zscore_rolling(base, 63)

def mrpt_569_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 104 mean reversion potential by measuring deviations from the 126d mean.
    """
    base = close / _rolling_mean(close, 325) - 1
    return _zscore_rolling(base, 126)

def mrpt_570_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 104 mean reversion potential by measuring deviations from the 252d mean.
    """
    base = close / _rolling_mean(close, 325) - 1
    return _zscore_rolling(base, 252)

def mrpt_571_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 104 mean reversion potential to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = close / _rolling_mean(close, 325) - 1
    return _rank_pct(base, 5)

def mrpt_572_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 104 mean reversion potential to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = close / _rolling_mean(close, 325) - 1
    return _rank_pct(base, 21)

def mrpt_573_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 104 mean reversion potential to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = close / _rolling_mean(close, 325) - 1
    return _rank_pct(base, 63)

def mrpt_574_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 104 mean reversion potential to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = close / _rolling_mean(close, 325) - 1
    return _rank_pct(base, 126)

def mrpt_575_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 104 mean reversion potential to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = close / _rolling_mean(close, 325) - 1
    return _rank_pct(base, 252)

def mrpt_576_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 104 mean reversion potential distribution over 5d to detect tail risk or exhaustion.
    """
    base = close / _rolling_mean(close, 325) - 1
    return _rolling_skew(base, 5)

def mrpt_577_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 104 mean reversion potential distribution over 21d to detect tail risk or exhaustion.
    """
    base = close / _rolling_mean(close, 325) - 1
    return _rolling_skew(base, 21)

def mrpt_578_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 104 mean reversion potential distribution over 63d to detect tail risk or exhaustion.
    """
    base = close / _rolling_mean(close, 325) - 1
    return _rolling_skew(base, 63)

def mrpt_579_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 104 mean reversion potential distribution over 126d to detect tail risk or exhaustion.
    """
    base = close / _rolling_mean(close, 325) - 1
    return _rolling_skew(base, 126)

def mrpt_580_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 104 mean reversion potential distribution over 252d to detect tail risk or exhaustion.
    """
    base = close / _rolling_mean(close, 325) - 1
    return _rolling_skew(base, 252)

def mrpt_581_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 104 mean reversion potential over 5d to capture explosive breakdown or reversal points.
    """
    base = close / _rolling_mean(close, 325) - 1
    return _rolling_kurt(base, 5)

def mrpt_582_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 104 mean reversion potential over 21d to capture explosive breakdown or reversal points.
    """
    base = close / _rolling_mean(close, 325) - 1
    return _rolling_kurt(base, 21)

def mrpt_583_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 104 mean reversion potential over 63d to capture explosive breakdown or reversal points.
    """
    base = close / _rolling_mean(close, 325) - 1
    return _rolling_kurt(base, 63)

def mrpt_584_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 104 mean reversion potential over 126d to capture explosive breakdown or reversal points.
    """
    base = close / _rolling_mean(close, 325) - 1
    return _rolling_kurt(base, 126)

def mrpt_585_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 104 mean reversion potential over 252d to capture explosive breakdown or reversal points.
    """
    base = close / _rolling_mean(close, 325) - 1
    return _rolling_kurt(base, 252)

def mrpt_586_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 104 mean reversion potential for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = close / _rolling_mean(close, 325) - 1
    return _safe_div(base, _rolling_std(base, 5))

def mrpt_587_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 104 mean reversion potential for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = close / _rolling_mean(close, 325) - 1
    return _safe_div(base, _rolling_std(base, 21))

def mrpt_588_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 104 mean reversion potential for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = close / _rolling_mean(close, 325) - 1
    return _safe_div(base, _rolling_std(base, 63))

def mrpt_589_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 104 mean reversion potential for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = close / _rolling_mean(close, 325) - 1
    return _safe_div(base, _rolling_std(base, 126))

def mrpt_590_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 104 mean reversion potential for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = close / _rolling_mean(close, 325) - 1
    return _safe_div(base, _rolling_std(base, 252))

def mrpt_591_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 104 mean reversion potential over 5d to stabilize variance and capture exponential shifts.
    """
    base = close / _rolling_mean(close, 325) - 1
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def mrpt_592_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 104 mean reversion potential over 21d to stabilize variance and capture exponential shifts.
    """
    base = close / _rolling_mean(close, 325) - 1
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def mrpt_593_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 104 mean reversion potential over 63d to stabilize variance and capture exponential shifts.
    """
    base = close / _rolling_mean(close, 325) - 1
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def mrpt_594_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 104 mean reversion potential over 126d to stabilize variance and capture exponential shifts.
    """
    base = close / _rolling_mean(close, 325) - 1
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def mrpt_595_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 104 mean reversion potential over 252d to stabilize variance and capture exponential shifts.
    """
    base = close / _rolling_mean(close, 325) - 1
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def mrpt_596_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 104 mean reversion potential over a 5d horizon to identify extreme regimes.
    """
    base = close / _rolling_mean(close, 345) - 1
    return _rolling_mean(base, 5)

def mrpt_597_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 104 mean reversion potential over a 21d horizon to identify extreme regimes.
    """
    base = close / _rolling_mean(close, 345) - 1
    return _rolling_mean(base, 21)

def mrpt_598_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 104 mean reversion potential over a 63d horizon to identify extreme regimes.
    """
    base = close / _rolling_mean(close, 345) - 1
    return _rolling_mean(base, 63)

def mrpt_599_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 104 mean reversion potential over a 126d horizon to identify extreme regimes.
    """
    base = close / _rolling_mean(close, 345) - 1
    return _rolling_mean(base, 126)

def mrpt_600_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 104 mean reversion potential over a 252d horizon to identify extreme regimes.
    """
    base = close / _rolling_mean(close, 345) - 1
    return _rolling_mean(base, 252)
