"""
59_59_market_impact_proxy — Base Features 526-600
Domain: 59_market_impact_proxy
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

def mimp_526_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 59 market impact proxy over a 5d horizon to identify extreme regimes.
    """
    base = (volume.pct_change(16).rolling(80).mean())
    return _rolling_mean(base, 5)

def mimp_527_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 59 market impact proxy over a 21d horizon to identify extreme regimes.
    """
    base = (volume.pct_change(16).rolling(80).mean())
    return _rolling_mean(base, 21)

def mimp_528_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 59 market impact proxy over a 63d horizon to identify extreme regimes.
    """
    base = (volume.pct_change(16).rolling(80).mean())
    return _rolling_mean(base, 63)

def mimp_529_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 59 market impact proxy over a 126d horizon to identify extreme regimes.
    """
    base = (volume.pct_change(16).rolling(80).mean())
    return _rolling_mean(base, 126)

def mimp_530_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 59 market impact proxy over a 252d horizon to identify extreme regimes.
    """
    base = (volume.pct_change(16).rolling(80).mean())
    return _rolling_mean(base, 252)

def mimp_531_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 59 market impact proxy by measuring deviations from the 5d mean.
    """
    base = (volume.pct_change(16).rolling(80).mean())
    return _zscore_rolling(base, 5)

def mimp_532_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 59 market impact proxy by measuring deviations from the 21d mean.
    """
    base = (volume.pct_change(16).rolling(80).mean())
    return _zscore_rolling(base, 21)

def mimp_533_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 59 market impact proxy by measuring deviations from the 63d mean.
    """
    base = (volume.pct_change(16).rolling(80).mean())
    return _zscore_rolling(base, 63)

def mimp_534_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 59 market impact proxy by measuring deviations from the 126d mean.
    """
    base = (volume.pct_change(16).rolling(80).mean())
    return _zscore_rolling(base, 126)

def mimp_535_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 59 market impact proxy by measuring deviations from the 252d mean.
    """
    base = (volume.pct_change(16).rolling(80).mean())
    return _zscore_rolling(base, 252)

def mimp_536_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 59 market impact proxy to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = (volume.pct_change(16).rolling(80).mean())
    return _rank_pct(base, 5)

def mimp_537_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 59 market impact proxy to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = (volume.pct_change(16).rolling(80).mean())
    return _rank_pct(base, 21)

def mimp_538_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 59 market impact proxy to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = (volume.pct_change(16).rolling(80).mean())
    return _rank_pct(base, 63)

def mimp_539_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 59 market impact proxy to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = (volume.pct_change(16).rolling(80).mean())
    return _rank_pct(base, 126)

def mimp_540_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 59 market impact proxy to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = (volume.pct_change(16).rolling(80).mean())
    return _rank_pct(base, 252)

def mimp_541_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 59 market impact proxy distribution over 5d to detect tail risk or exhaustion.
    """
    base = (volume.pct_change(16).rolling(80).mean())
    return _rolling_skew(base, 5)

def mimp_542_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 59 market impact proxy distribution over 21d to detect tail risk or exhaustion.
    """
    base = (volume.pct_change(16).rolling(80).mean())
    return _rolling_skew(base, 21)

def mimp_543_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 59 market impact proxy distribution over 63d to detect tail risk or exhaustion.
    """
    base = (volume.pct_change(16).rolling(80).mean())
    return _rolling_skew(base, 63)

def mimp_544_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 59 market impact proxy distribution over 126d to detect tail risk or exhaustion.
    """
    base = (volume.pct_change(16).rolling(80).mean())
    return _rolling_skew(base, 126)

def mimp_545_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 59 market impact proxy distribution over 252d to detect tail risk or exhaustion.
    """
    base = (volume.pct_change(16).rolling(80).mean())
    return _rolling_skew(base, 252)

def mimp_546_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 59 market impact proxy over 5d to capture explosive breakdown or reversal points.
    """
    base = (volume.pct_change(16).rolling(80).mean())
    return _rolling_kurt(base, 5)

def mimp_547_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 59 market impact proxy over 21d to capture explosive breakdown or reversal points.
    """
    base = (volume.pct_change(16).rolling(80).mean())
    return _rolling_kurt(base, 21)

def mimp_548_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 59 market impact proxy over 63d to capture explosive breakdown or reversal points.
    """
    base = (volume.pct_change(16).rolling(80).mean())
    return _rolling_kurt(base, 63)

def mimp_549_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 59 market impact proxy over 126d to capture explosive breakdown or reversal points.
    """
    base = (volume.pct_change(16).rolling(80).mean())
    return _rolling_kurt(base, 126)

def mimp_550_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 59 market impact proxy over 252d to capture explosive breakdown or reversal points.
    """
    base = (volume.pct_change(16).rolling(80).mean())
    return _rolling_kurt(base, 252)

def mimp_551_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 59 market impact proxy for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = (volume.pct_change(16).rolling(80).mean())
    return _safe_div(base, _rolling_std(base, 5))

def mimp_552_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 59 market impact proxy for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = (volume.pct_change(16).rolling(80).mean())
    return _safe_div(base, _rolling_std(base, 21))

def mimp_553_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 59 market impact proxy for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = (volume.pct_change(16).rolling(80).mean())
    return _safe_div(base, _rolling_std(base, 63))

def mimp_554_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 59 market impact proxy for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = (volume.pct_change(16).rolling(80).mean())
    return _safe_div(base, _rolling_std(base, 126))

def mimp_555_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 59 market impact proxy for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = (volume.pct_change(16).rolling(80).mean())
    return _safe_div(base, _rolling_std(base, 252))

def mimp_556_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 59 market impact proxy over 5d to stabilize variance and capture exponential shifts.
    """
    base = (volume.pct_change(16).rolling(80).mean())
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def mimp_557_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 59 market impact proxy over 21d to stabilize variance and capture exponential shifts.
    """
    base = (volume.pct_change(16).rolling(80).mean())
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def mimp_558_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 59 market impact proxy over 63d to stabilize variance and capture exponential shifts.
    """
    base = (volume.pct_change(16).rolling(80).mean())
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def mimp_559_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 59 market impact proxy over 126d to stabilize variance and capture exponential shifts.
    """
    base = (volume.pct_change(16).rolling(80).mean())
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def mimp_560_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 59 market impact proxy over 252d to stabilize variance and capture exponential shifts.
    """
    base = (volume.pct_change(16).rolling(80).mean())
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def mimp_561_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 59 market impact proxy over a 5d horizon to identify extreme regimes.
    """
    base = (volume.pct_change(17).rolling(85).mean())
    return _rolling_mean(base, 5)

def mimp_562_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 59 market impact proxy over a 21d horizon to identify extreme regimes.
    """
    base = (volume.pct_change(17).rolling(85).mean())
    return _rolling_mean(base, 21)

def mimp_563_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 59 market impact proxy over a 63d horizon to identify extreme regimes.
    """
    base = (volume.pct_change(17).rolling(85).mean())
    return _rolling_mean(base, 63)

def mimp_564_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 59 market impact proxy over a 126d horizon to identify extreme regimes.
    """
    base = (volume.pct_change(17).rolling(85).mean())
    return _rolling_mean(base, 126)

def mimp_565_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 59 market impact proxy over a 252d horizon to identify extreme regimes.
    """
    base = (volume.pct_change(17).rolling(85).mean())
    return _rolling_mean(base, 252)

def mimp_566_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 59 market impact proxy by measuring deviations from the 5d mean.
    """
    base = (volume.pct_change(17).rolling(85).mean())
    return _zscore_rolling(base, 5)

def mimp_567_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 59 market impact proxy by measuring deviations from the 21d mean.
    """
    base = (volume.pct_change(17).rolling(85).mean())
    return _zscore_rolling(base, 21)

def mimp_568_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 59 market impact proxy by measuring deviations from the 63d mean.
    """
    base = (volume.pct_change(17).rolling(85).mean())
    return _zscore_rolling(base, 63)

def mimp_569_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 59 market impact proxy by measuring deviations from the 126d mean.
    """
    base = (volume.pct_change(17).rolling(85).mean())
    return _zscore_rolling(base, 126)

def mimp_570_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 59 market impact proxy by measuring deviations from the 252d mean.
    """
    base = (volume.pct_change(17).rolling(85).mean())
    return _zscore_rolling(base, 252)

def mimp_571_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 59 market impact proxy to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = (volume.pct_change(17).rolling(85).mean())
    return _rank_pct(base, 5)

def mimp_572_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 59 market impact proxy to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = (volume.pct_change(17).rolling(85).mean())
    return _rank_pct(base, 21)

def mimp_573_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 59 market impact proxy to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = (volume.pct_change(17).rolling(85).mean())
    return _rank_pct(base, 63)

def mimp_574_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 59 market impact proxy to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = (volume.pct_change(17).rolling(85).mean())
    return _rank_pct(base, 126)

def mimp_575_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 59 market impact proxy to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = (volume.pct_change(17).rolling(85).mean())
    return _rank_pct(base, 252)

def mimp_576_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 59 market impact proxy distribution over 5d to detect tail risk or exhaustion.
    """
    base = (volume.pct_change(17).rolling(85).mean())
    return _rolling_skew(base, 5)

def mimp_577_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 59 market impact proxy distribution over 21d to detect tail risk or exhaustion.
    """
    base = (volume.pct_change(17).rolling(85).mean())
    return _rolling_skew(base, 21)

def mimp_578_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 59 market impact proxy distribution over 63d to detect tail risk or exhaustion.
    """
    base = (volume.pct_change(17).rolling(85).mean())
    return _rolling_skew(base, 63)

def mimp_579_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 59 market impact proxy distribution over 126d to detect tail risk or exhaustion.
    """
    base = (volume.pct_change(17).rolling(85).mean())
    return _rolling_skew(base, 126)

def mimp_580_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 59 market impact proxy distribution over 252d to detect tail risk or exhaustion.
    """
    base = (volume.pct_change(17).rolling(85).mean())
    return _rolling_skew(base, 252)

def mimp_581_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 59 market impact proxy over 5d to capture explosive breakdown or reversal points.
    """
    base = (volume.pct_change(17).rolling(85).mean())
    return _rolling_kurt(base, 5)

def mimp_582_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 59 market impact proxy over 21d to capture explosive breakdown or reversal points.
    """
    base = (volume.pct_change(17).rolling(85).mean())
    return _rolling_kurt(base, 21)

def mimp_583_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 59 market impact proxy over 63d to capture explosive breakdown or reversal points.
    """
    base = (volume.pct_change(17).rolling(85).mean())
    return _rolling_kurt(base, 63)

def mimp_584_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 59 market impact proxy over 126d to capture explosive breakdown or reversal points.
    """
    base = (volume.pct_change(17).rolling(85).mean())
    return _rolling_kurt(base, 126)

def mimp_585_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 59 market impact proxy over 252d to capture explosive breakdown or reversal points.
    """
    base = (volume.pct_change(17).rolling(85).mean())
    return _rolling_kurt(base, 252)

def mimp_586_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 59 market impact proxy for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = (volume.pct_change(17).rolling(85).mean())
    return _safe_div(base, _rolling_std(base, 5))

def mimp_587_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 59 market impact proxy for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = (volume.pct_change(17).rolling(85).mean())
    return _safe_div(base, _rolling_std(base, 21))

def mimp_588_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 59 market impact proxy for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = (volume.pct_change(17).rolling(85).mean())
    return _safe_div(base, _rolling_std(base, 63))

def mimp_589_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 59 market impact proxy for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = (volume.pct_change(17).rolling(85).mean())
    return _safe_div(base, _rolling_std(base, 126))

def mimp_590_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 59 market impact proxy for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = (volume.pct_change(17).rolling(85).mean())
    return _safe_div(base, _rolling_std(base, 252))

def mimp_591_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 59 market impact proxy over 5d to stabilize variance and capture exponential shifts.
    """
    base = (volume.pct_change(17).rolling(85).mean())
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def mimp_592_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 59 market impact proxy over 21d to stabilize variance and capture exponential shifts.
    """
    base = (volume.pct_change(17).rolling(85).mean())
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def mimp_593_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 59 market impact proxy over 63d to stabilize variance and capture exponential shifts.
    """
    base = (volume.pct_change(17).rolling(85).mean())
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def mimp_594_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 59 market impact proxy over 126d to stabilize variance and capture exponential shifts.
    """
    base = (volume.pct_change(17).rolling(85).mean())
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def mimp_595_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 59 market impact proxy over 252d to stabilize variance and capture exponential shifts.
    """
    base = (volume.pct_change(17).rolling(85).mean())
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def mimp_596_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 59 market impact proxy over a 5d horizon to identify extreme regimes.
    """
    base = (volume.pct_change(18).rolling(90).mean())
    return _rolling_mean(base, 5)

def mimp_597_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 59 market impact proxy over a 21d horizon to identify extreme regimes.
    """
    base = (volume.pct_change(18).rolling(90).mean())
    return _rolling_mean(base, 21)

def mimp_598_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 59 market impact proxy over a 63d horizon to identify extreme regimes.
    """
    base = (volume.pct_change(18).rolling(90).mean())
    return _rolling_mean(base, 63)

def mimp_599_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 59 market impact proxy over a 126d horizon to identify extreme regimes.
    """
    base = (volume.pct_change(18).rolling(90).mean())
    return _rolling_mean(base, 126)

def mimp_600_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 59 market impact proxy over a 252d horizon to identify extreme regimes.
    """
    base = (volume.pct_change(18).rolling(90).mean())
    return _rolling_mean(base, 252)
