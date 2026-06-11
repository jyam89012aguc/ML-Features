"""
46_46_gap_structure — Base Features 526-600
Domain: 46_gap_structure
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

def gaps_526_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 46 gap structure over a 5d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(80).mean())
    return _rolling_mean(base, 5)

def gaps_527_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 46 gap structure over a 21d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(80).mean())
    return _rolling_mean(base, 21)

def gaps_528_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 46 gap structure over a 63d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(80).mean())
    return _rolling_mean(base, 63)

def gaps_529_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 46 gap structure over a 126d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(80).mean())
    return _rolling_mean(base, 126)

def gaps_530_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 46 gap structure over a 252d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(80).mean())
    return _rolling_mean(base, 252)

def gaps_531_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 46 gap structure by measuring deviations from the 5d mean.
    """
    base = ((close - open).abs().rolling(80).mean())
    return _zscore_rolling(base, 5)

def gaps_532_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 46 gap structure by measuring deviations from the 21d mean.
    """
    base = ((close - open).abs().rolling(80).mean())
    return _zscore_rolling(base, 21)

def gaps_533_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 46 gap structure by measuring deviations from the 63d mean.
    """
    base = ((close - open).abs().rolling(80).mean())
    return _zscore_rolling(base, 63)

def gaps_534_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 46 gap structure by measuring deviations from the 126d mean.
    """
    base = ((close - open).abs().rolling(80).mean())
    return _zscore_rolling(base, 126)

def gaps_535_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 46 gap structure by measuring deviations from the 252d mean.
    """
    base = ((close - open).abs().rolling(80).mean())
    return _zscore_rolling(base, 252)

def gaps_536_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 46 gap structure to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = ((close - open).abs().rolling(80).mean())
    return _rank_pct(base, 5)

def gaps_537_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 46 gap structure to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = ((close - open).abs().rolling(80).mean())
    return _rank_pct(base, 21)

def gaps_538_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 46 gap structure to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = ((close - open).abs().rolling(80).mean())
    return _rank_pct(base, 63)

def gaps_539_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 46 gap structure to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = ((close - open).abs().rolling(80).mean())
    return _rank_pct(base, 126)

def gaps_540_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 46 gap structure to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = ((close - open).abs().rolling(80).mean())
    return _rank_pct(base, 252)

def gaps_541_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 46 gap structure distribution over 5d to detect tail risk or exhaustion.
    """
    base = ((close - open).abs().rolling(80).mean())
    return _rolling_skew(base, 5)

def gaps_542_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 46 gap structure distribution over 21d to detect tail risk or exhaustion.
    """
    base = ((close - open).abs().rolling(80).mean())
    return _rolling_skew(base, 21)

def gaps_543_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 46 gap structure distribution over 63d to detect tail risk or exhaustion.
    """
    base = ((close - open).abs().rolling(80).mean())
    return _rolling_skew(base, 63)

def gaps_544_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 46 gap structure distribution over 126d to detect tail risk or exhaustion.
    """
    base = ((close - open).abs().rolling(80).mean())
    return _rolling_skew(base, 126)

def gaps_545_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 46 gap structure distribution over 252d to detect tail risk or exhaustion.
    """
    base = ((close - open).abs().rolling(80).mean())
    return _rolling_skew(base, 252)

def gaps_546_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 46 gap structure over 5d to capture explosive breakdown or reversal points.
    """
    base = ((close - open).abs().rolling(80).mean())
    return _rolling_kurt(base, 5)

def gaps_547_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 46 gap structure over 21d to capture explosive breakdown or reversal points.
    """
    base = ((close - open).abs().rolling(80).mean())
    return _rolling_kurt(base, 21)

def gaps_548_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 46 gap structure over 63d to capture explosive breakdown or reversal points.
    """
    base = ((close - open).abs().rolling(80).mean())
    return _rolling_kurt(base, 63)

def gaps_549_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 46 gap structure over 126d to capture explosive breakdown or reversal points.
    """
    base = ((close - open).abs().rolling(80).mean())
    return _rolling_kurt(base, 126)

def gaps_550_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 46 gap structure over 252d to capture explosive breakdown or reversal points.
    """
    base = ((close - open).abs().rolling(80).mean())
    return _rolling_kurt(base, 252)

def gaps_551_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 46 gap structure for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = ((close - open).abs().rolling(80).mean())
    return _safe_div(base, _rolling_std(base, 5))

def gaps_552_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 46 gap structure for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = ((close - open).abs().rolling(80).mean())
    return _safe_div(base, _rolling_std(base, 21))

def gaps_553_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 46 gap structure for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = ((close - open).abs().rolling(80).mean())
    return _safe_div(base, _rolling_std(base, 63))

def gaps_554_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 46 gap structure for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = ((close - open).abs().rolling(80).mean())
    return _safe_div(base, _rolling_std(base, 126))

def gaps_555_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 46 gap structure for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = ((close - open).abs().rolling(80).mean())
    return _safe_div(base, _rolling_std(base, 252))

def gaps_556_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 46 gap structure over 5d to stabilize variance and capture exponential shifts.
    """
    base = ((close - open).abs().rolling(80).mean())
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def gaps_557_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 46 gap structure over 21d to stabilize variance and capture exponential shifts.
    """
    base = ((close - open).abs().rolling(80).mean())
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def gaps_558_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 46 gap structure over 63d to stabilize variance and capture exponential shifts.
    """
    base = ((close - open).abs().rolling(80).mean())
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def gaps_559_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 46 gap structure over 126d to stabilize variance and capture exponential shifts.
    """
    base = ((close - open).abs().rolling(80).mean())
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def gaps_560_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 46 gap structure over 252d to stabilize variance and capture exponential shifts.
    """
    base = ((close - open).abs().rolling(80).mean())
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def gaps_561_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 46 gap structure over a 5d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(85).mean())
    return _rolling_mean(base, 5)

def gaps_562_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 46 gap structure over a 21d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(85).mean())
    return _rolling_mean(base, 21)

def gaps_563_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 46 gap structure over a 63d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(85).mean())
    return _rolling_mean(base, 63)

def gaps_564_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 46 gap structure over a 126d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(85).mean())
    return _rolling_mean(base, 126)

def gaps_565_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 46 gap structure over a 252d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(85).mean())
    return _rolling_mean(base, 252)

def gaps_566_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 46 gap structure by measuring deviations from the 5d mean.
    """
    base = ((close - open).abs().rolling(85).mean())
    return _zscore_rolling(base, 5)

def gaps_567_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 46 gap structure by measuring deviations from the 21d mean.
    """
    base = ((close - open).abs().rolling(85).mean())
    return _zscore_rolling(base, 21)

def gaps_568_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 46 gap structure by measuring deviations from the 63d mean.
    """
    base = ((close - open).abs().rolling(85).mean())
    return _zscore_rolling(base, 63)

def gaps_569_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 46 gap structure by measuring deviations from the 126d mean.
    """
    base = ((close - open).abs().rolling(85).mean())
    return _zscore_rolling(base, 126)

def gaps_570_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 46 gap structure by measuring deviations from the 252d mean.
    """
    base = ((close - open).abs().rolling(85).mean())
    return _zscore_rolling(base, 252)

def gaps_571_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 46 gap structure to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = ((close - open).abs().rolling(85).mean())
    return _rank_pct(base, 5)

def gaps_572_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 46 gap structure to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = ((close - open).abs().rolling(85).mean())
    return _rank_pct(base, 21)

def gaps_573_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 46 gap structure to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = ((close - open).abs().rolling(85).mean())
    return _rank_pct(base, 63)

def gaps_574_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 46 gap structure to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = ((close - open).abs().rolling(85).mean())
    return _rank_pct(base, 126)

def gaps_575_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 46 gap structure to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = ((close - open).abs().rolling(85).mean())
    return _rank_pct(base, 252)

def gaps_576_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 46 gap structure distribution over 5d to detect tail risk or exhaustion.
    """
    base = ((close - open).abs().rolling(85).mean())
    return _rolling_skew(base, 5)

def gaps_577_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 46 gap structure distribution over 21d to detect tail risk or exhaustion.
    """
    base = ((close - open).abs().rolling(85).mean())
    return _rolling_skew(base, 21)

def gaps_578_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 46 gap structure distribution over 63d to detect tail risk or exhaustion.
    """
    base = ((close - open).abs().rolling(85).mean())
    return _rolling_skew(base, 63)

def gaps_579_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 46 gap structure distribution over 126d to detect tail risk or exhaustion.
    """
    base = ((close - open).abs().rolling(85).mean())
    return _rolling_skew(base, 126)

def gaps_580_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 46 gap structure distribution over 252d to detect tail risk or exhaustion.
    """
    base = ((close - open).abs().rolling(85).mean())
    return _rolling_skew(base, 252)

def gaps_581_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 46 gap structure over 5d to capture explosive breakdown or reversal points.
    """
    base = ((close - open).abs().rolling(85).mean())
    return _rolling_kurt(base, 5)

def gaps_582_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 46 gap structure over 21d to capture explosive breakdown or reversal points.
    """
    base = ((close - open).abs().rolling(85).mean())
    return _rolling_kurt(base, 21)

def gaps_583_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 46 gap structure over 63d to capture explosive breakdown or reversal points.
    """
    base = ((close - open).abs().rolling(85).mean())
    return _rolling_kurt(base, 63)

def gaps_584_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 46 gap structure over 126d to capture explosive breakdown or reversal points.
    """
    base = ((close - open).abs().rolling(85).mean())
    return _rolling_kurt(base, 126)

def gaps_585_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 46 gap structure over 252d to capture explosive breakdown or reversal points.
    """
    base = ((close - open).abs().rolling(85).mean())
    return _rolling_kurt(base, 252)

def gaps_586_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 46 gap structure for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = ((close - open).abs().rolling(85).mean())
    return _safe_div(base, _rolling_std(base, 5))

def gaps_587_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 46 gap structure for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = ((close - open).abs().rolling(85).mean())
    return _safe_div(base, _rolling_std(base, 21))

def gaps_588_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 46 gap structure for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = ((close - open).abs().rolling(85).mean())
    return _safe_div(base, _rolling_std(base, 63))

def gaps_589_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 46 gap structure for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = ((close - open).abs().rolling(85).mean())
    return _safe_div(base, _rolling_std(base, 126))

def gaps_590_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 46 gap structure for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = ((close - open).abs().rolling(85).mean())
    return _safe_div(base, _rolling_std(base, 252))

def gaps_591_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 46 gap structure over 5d to stabilize variance and capture exponential shifts.
    """
    base = ((close - open).abs().rolling(85).mean())
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def gaps_592_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 46 gap structure over 21d to stabilize variance and capture exponential shifts.
    """
    base = ((close - open).abs().rolling(85).mean())
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def gaps_593_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 46 gap structure over 63d to stabilize variance and capture exponential shifts.
    """
    base = ((close - open).abs().rolling(85).mean())
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def gaps_594_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 46 gap structure over 126d to stabilize variance and capture exponential shifts.
    """
    base = ((close - open).abs().rolling(85).mean())
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def gaps_595_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 46 gap structure over 252d to stabilize variance and capture exponential shifts.
    """
    base = ((close - open).abs().rolling(85).mean())
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def gaps_596_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 46 gap structure over a 5d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(90).mean())
    return _rolling_mean(base, 5)

def gaps_597_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 46 gap structure over a 21d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(90).mean())
    return _rolling_mean(base, 21)

def gaps_598_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 46 gap structure over a 63d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(90).mean())
    return _rolling_mean(base, 63)

def gaps_599_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 46 gap structure over a 126d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(90).mean())
    return _rolling_mean(base, 126)

def gaps_600_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 46 gap structure over a 252d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(90).mean())
    return _rolling_mean(base, 252)
