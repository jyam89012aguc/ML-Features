"""
51_51_shadow_wick_analysis — Base Features 526-600
Domain: 51_shadow_wick_analysis
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

def swik_526_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 51 shadow wick analysis over a 5d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(80).mean())
    return _rolling_mean(base, 5)

def swik_527_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 51 shadow wick analysis over a 21d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(80).mean())
    return _rolling_mean(base, 21)

def swik_528_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 51 shadow wick analysis over a 63d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(80).mean())
    return _rolling_mean(base, 63)

def swik_529_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 51 shadow wick analysis over a 126d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(80).mean())
    return _rolling_mean(base, 126)

def swik_530_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 51 shadow wick analysis over a 252d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(80).mean())
    return _rolling_mean(base, 252)

def swik_531_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 51 shadow wick analysis by measuring deviations from the 5d mean.
    """
    base = ((close - open).abs().rolling(80).mean())
    return _zscore_rolling(base, 5)

def swik_532_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 51 shadow wick analysis by measuring deviations from the 21d mean.
    """
    base = ((close - open).abs().rolling(80).mean())
    return _zscore_rolling(base, 21)

def swik_533_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 51 shadow wick analysis by measuring deviations from the 63d mean.
    """
    base = ((close - open).abs().rolling(80).mean())
    return _zscore_rolling(base, 63)

def swik_534_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 51 shadow wick analysis by measuring deviations from the 126d mean.
    """
    base = ((close - open).abs().rolling(80).mean())
    return _zscore_rolling(base, 126)

def swik_535_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 51 shadow wick analysis by measuring deviations from the 252d mean.
    """
    base = ((close - open).abs().rolling(80).mean())
    return _zscore_rolling(base, 252)

def swik_536_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 51 shadow wick analysis to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = ((close - open).abs().rolling(80).mean())
    return _rank_pct(base, 5)

def swik_537_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 51 shadow wick analysis to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = ((close - open).abs().rolling(80).mean())
    return _rank_pct(base, 21)

def swik_538_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 51 shadow wick analysis to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = ((close - open).abs().rolling(80).mean())
    return _rank_pct(base, 63)

def swik_539_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 51 shadow wick analysis to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = ((close - open).abs().rolling(80).mean())
    return _rank_pct(base, 126)

def swik_540_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 51 shadow wick analysis to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = ((close - open).abs().rolling(80).mean())
    return _rank_pct(base, 252)

def swik_541_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 51 shadow wick analysis distribution over 5d to detect tail risk or exhaustion.
    """
    base = ((close - open).abs().rolling(80).mean())
    return _rolling_skew(base, 5)

def swik_542_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 51 shadow wick analysis distribution over 21d to detect tail risk or exhaustion.
    """
    base = ((close - open).abs().rolling(80).mean())
    return _rolling_skew(base, 21)

def swik_543_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 51 shadow wick analysis distribution over 63d to detect tail risk or exhaustion.
    """
    base = ((close - open).abs().rolling(80).mean())
    return _rolling_skew(base, 63)

def swik_544_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 51 shadow wick analysis distribution over 126d to detect tail risk or exhaustion.
    """
    base = ((close - open).abs().rolling(80).mean())
    return _rolling_skew(base, 126)

def swik_545_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 51 shadow wick analysis distribution over 252d to detect tail risk or exhaustion.
    """
    base = ((close - open).abs().rolling(80).mean())
    return _rolling_skew(base, 252)

def swik_546_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 51 shadow wick analysis over 5d to capture explosive breakdown or reversal points.
    """
    base = ((close - open).abs().rolling(80).mean())
    return _rolling_kurt(base, 5)

def swik_547_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 51 shadow wick analysis over 21d to capture explosive breakdown or reversal points.
    """
    base = ((close - open).abs().rolling(80).mean())
    return _rolling_kurt(base, 21)

def swik_548_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 51 shadow wick analysis over 63d to capture explosive breakdown or reversal points.
    """
    base = ((close - open).abs().rolling(80).mean())
    return _rolling_kurt(base, 63)

def swik_549_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 51 shadow wick analysis over 126d to capture explosive breakdown or reversal points.
    """
    base = ((close - open).abs().rolling(80).mean())
    return _rolling_kurt(base, 126)

def swik_550_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 51 shadow wick analysis over 252d to capture explosive breakdown or reversal points.
    """
    base = ((close - open).abs().rolling(80).mean())
    return _rolling_kurt(base, 252)

def swik_551_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 51 shadow wick analysis for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = ((close - open).abs().rolling(80).mean())
    return _safe_div(base, _rolling_std(base, 5))

def swik_552_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 51 shadow wick analysis for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = ((close - open).abs().rolling(80).mean())
    return _safe_div(base, _rolling_std(base, 21))

def swik_553_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 51 shadow wick analysis for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = ((close - open).abs().rolling(80).mean())
    return _safe_div(base, _rolling_std(base, 63))

def swik_554_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 51 shadow wick analysis for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = ((close - open).abs().rolling(80).mean())
    return _safe_div(base, _rolling_std(base, 126))

def swik_555_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 51 shadow wick analysis for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = ((close - open).abs().rolling(80).mean())
    return _safe_div(base, _rolling_std(base, 252))

def swik_556_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 51 shadow wick analysis over 5d to stabilize variance and capture exponential shifts.
    """
    base = ((close - open).abs().rolling(80).mean())
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def swik_557_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 51 shadow wick analysis over 21d to stabilize variance and capture exponential shifts.
    """
    base = ((close - open).abs().rolling(80).mean())
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def swik_558_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 51 shadow wick analysis over 63d to stabilize variance and capture exponential shifts.
    """
    base = ((close - open).abs().rolling(80).mean())
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def swik_559_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 51 shadow wick analysis over 126d to stabilize variance and capture exponential shifts.
    """
    base = ((close - open).abs().rolling(80).mean())
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def swik_560_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 51 shadow wick analysis over 252d to stabilize variance and capture exponential shifts.
    """
    base = ((close - open).abs().rolling(80).mean())
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def swik_561_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 51 shadow wick analysis over a 5d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(85).mean())
    return _rolling_mean(base, 5)

def swik_562_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 51 shadow wick analysis over a 21d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(85).mean())
    return _rolling_mean(base, 21)

def swik_563_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 51 shadow wick analysis over a 63d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(85).mean())
    return _rolling_mean(base, 63)

def swik_564_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 51 shadow wick analysis over a 126d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(85).mean())
    return _rolling_mean(base, 126)

def swik_565_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 51 shadow wick analysis over a 252d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(85).mean())
    return _rolling_mean(base, 252)

def swik_566_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 51 shadow wick analysis by measuring deviations from the 5d mean.
    """
    base = ((close - open).abs().rolling(85).mean())
    return _zscore_rolling(base, 5)

def swik_567_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 51 shadow wick analysis by measuring deviations from the 21d mean.
    """
    base = ((close - open).abs().rolling(85).mean())
    return _zscore_rolling(base, 21)

def swik_568_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 51 shadow wick analysis by measuring deviations from the 63d mean.
    """
    base = ((close - open).abs().rolling(85).mean())
    return _zscore_rolling(base, 63)

def swik_569_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 51 shadow wick analysis by measuring deviations from the 126d mean.
    """
    base = ((close - open).abs().rolling(85).mean())
    return _zscore_rolling(base, 126)

def swik_570_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 51 shadow wick analysis by measuring deviations from the 252d mean.
    """
    base = ((close - open).abs().rolling(85).mean())
    return _zscore_rolling(base, 252)

def swik_571_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 51 shadow wick analysis to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = ((close - open).abs().rolling(85).mean())
    return _rank_pct(base, 5)

def swik_572_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 51 shadow wick analysis to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = ((close - open).abs().rolling(85).mean())
    return _rank_pct(base, 21)

def swik_573_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 51 shadow wick analysis to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = ((close - open).abs().rolling(85).mean())
    return _rank_pct(base, 63)

def swik_574_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 51 shadow wick analysis to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = ((close - open).abs().rolling(85).mean())
    return _rank_pct(base, 126)

def swik_575_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 51 shadow wick analysis to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = ((close - open).abs().rolling(85).mean())
    return _rank_pct(base, 252)

def swik_576_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 51 shadow wick analysis distribution over 5d to detect tail risk or exhaustion.
    """
    base = ((close - open).abs().rolling(85).mean())
    return _rolling_skew(base, 5)

def swik_577_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 51 shadow wick analysis distribution over 21d to detect tail risk or exhaustion.
    """
    base = ((close - open).abs().rolling(85).mean())
    return _rolling_skew(base, 21)

def swik_578_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 51 shadow wick analysis distribution over 63d to detect tail risk or exhaustion.
    """
    base = ((close - open).abs().rolling(85).mean())
    return _rolling_skew(base, 63)

def swik_579_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 51 shadow wick analysis distribution over 126d to detect tail risk or exhaustion.
    """
    base = ((close - open).abs().rolling(85).mean())
    return _rolling_skew(base, 126)

def swik_580_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 51 shadow wick analysis distribution over 252d to detect tail risk or exhaustion.
    """
    base = ((close - open).abs().rolling(85).mean())
    return _rolling_skew(base, 252)

def swik_581_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 51 shadow wick analysis over 5d to capture explosive breakdown or reversal points.
    """
    base = ((close - open).abs().rolling(85).mean())
    return _rolling_kurt(base, 5)

def swik_582_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 51 shadow wick analysis over 21d to capture explosive breakdown or reversal points.
    """
    base = ((close - open).abs().rolling(85).mean())
    return _rolling_kurt(base, 21)

def swik_583_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 51 shadow wick analysis over 63d to capture explosive breakdown or reversal points.
    """
    base = ((close - open).abs().rolling(85).mean())
    return _rolling_kurt(base, 63)

def swik_584_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 51 shadow wick analysis over 126d to capture explosive breakdown or reversal points.
    """
    base = ((close - open).abs().rolling(85).mean())
    return _rolling_kurt(base, 126)

def swik_585_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 51 shadow wick analysis over 252d to capture explosive breakdown or reversal points.
    """
    base = ((close - open).abs().rolling(85).mean())
    return _rolling_kurt(base, 252)

def swik_586_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 51 shadow wick analysis for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = ((close - open).abs().rolling(85).mean())
    return _safe_div(base, _rolling_std(base, 5))

def swik_587_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 51 shadow wick analysis for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = ((close - open).abs().rolling(85).mean())
    return _safe_div(base, _rolling_std(base, 21))

def swik_588_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 51 shadow wick analysis for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = ((close - open).abs().rolling(85).mean())
    return _safe_div(base, _rolling_std(base, 63))

def swik_589_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 51 shadow wick analysis for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = ((close - open).abs().rolling(85).mean())
    return _safe_div(base, _rolling_std(base, 126))

def swik_590_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 51 shadow wick analysis for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = ((close - open).abs().rolling(85).mean())
    return _safe_div(base, _rolling_std(base, 252))

def swik_591_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 51 shadow wick analysis over 5d to stabilize variance and capture exponential shifts.
    """
    base = ((close - open).abs().rolling(85).mean())
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def swik_592_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 51 shadow wick analysis over 21d to stabilize variance and capture exponential shifts.
    """
    base = ((close - open).abs().rolling(85).mean())
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def swik_593_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 51 shadow wick analysis over 63d to stabilize variance and capture exponential shifts.
    """
    base = ((close - open).abs().rolling(85).mean())
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def swik_594_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 51 shadow wick analysis over 126d to stabilize variance and capture exponential shifts.
    """
    base = ((close - open).abs().rolling(85).mean())
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def swik_595_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 51 shadow wick analysis over 252d to stabilize variance and capture exponential shifts.
    """
    base = ((close - open).abs().rolling(85).mean())
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def swik_596_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 51 shadow wick analysis over a 5d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(90).mean())
    return _rolling_mean(base, 5)

def swik_597_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 51 shadow wick analysis over a 21d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(90).mean())
    return _rolling_mean(base, 21)

def swik_598_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 51 shadow wick analysis over a 63d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(90).mean())
    return _rolling_mean(base, 63)

def swik_599_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 51 shadow wick analysis over a 126d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(90).mean())
    return _rolling_mean(base, 126)

def swik_600_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 51 shadow wick analysis over a 252d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(90).mean())
    return _rolling_mean(base, 252)
