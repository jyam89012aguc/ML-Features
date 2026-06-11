"""
53_53_liquidity_collapse — Base Features 526-600
Domain: 53_liquidity_collapse
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

def lcol_526_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 53 liquidity collapse over a 5d horizon to identify extreme regimes.
    """
    base = (volume.pct_change(16).rolling(80).mean())
    return _rolling_mean(base, 5)

def lcol_527_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 53 liquidity collapse over a 21d horizon to identify extreme regimes.
    """
    base = (volume.pct_change(16).rolling(80).mean())
    return _rolling_mean(base, 21)

def lcol_528_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 53 liquidity collapse over a 63d horizon to identify extreme regimes.
    """
    base = (volume.pct_change(16).rolling(80).mean())
    return _rolling_mean(base, 63)

def lcol_529_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 53 liquidity collapse over a 126d horizon to identify extreme regimes.
    """
    base = (volume.pct_change(16).rolling(80).mean())
    return _rolling_mean(base, 126)

def lcol_530_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 53 liquidity collapse over a 252d horizon to identify extreme regimes.
    """
    base = (volume.pct_change(16).rolling(80).mean())
    return _rolling_mean(base, 252)

def lcol_531_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 53 liquidity collapse by measuring deviations from the 5d mean.
    """
    base = (volume.pct_change(16).rolling(80).mean())
    return _zscore_rolling(base, 5)

def lcol_532_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 53 liquidity collapse by measuring deviations from the 21d mean.
    """
    base = (volume.pct_change(16).rolling(80).mean())
    return _zscore_rolling(base, 21)

def lcol_533_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 53 liquidity collapse by measuring deviations from the 63d mean.
    """
    base = (volume.pct_change(16).rolling(80).mean())
    return _zscore_rolling(base, 63)

def lcol_534_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 53 liquidity collapse by measuring deviations from the 126d mean.
    """
    base = (volume.pct_change(16).rolling(80).mean())
    return _zscore_rolling(base, 126)

def lcol_535_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 53 liquidity collapse by measuring deviations from the 252d mean.
    """
    base = (volume.pct_change(16).rolling(80).mean())
    return _zscore_rolling(base, 252)

def lcol_536_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 53 liquidity collapse to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = (volume.pct_change(16).rolling(80).mean())
    return _rank_pct(base, 5)

def lcol_537_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 53 liquidity collapse to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = (volume.pct_change(16).rolling(80).mean())
    return _rank_pct(base, 21)

def lcol_538_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 53 liquidity collapse to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = (volume.pct_change(16).rolling(80).mean())
    return _rank_pct(base, 63)

def lcol_539_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 53 liquidity collapse to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = (volume.pct_change(16).rolling(80).mean())
    return _rank_pct(base, 126)

def lcol_540_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 53 liquidity collapse to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = (volume.pct_change(16).rolling(80).mean())
    return _rank_pct(base, 252)

def lcol_541_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 53 liquidity collapse distribution over 5d to detect tail risk or exhaustion.
    """
    base = (volume.pct_change(16).rolling(80).mean())
    return _rolling_skew(base, 5)

def lcol_542_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 53 liquidity collapse distribution over 21d to detect tail risk or exhaustion.
    """
    base = (volume.pct_change(16).rolling(80).mean())
    return _rolling_skew(base, 21)

def lcol_543_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 53 liquidity collapse distribution over 63d to detect tail risk or exhaustion.
    """
    base = (volume.pct_change(16).rolling(80).mean())
    return _rolling_skew(base, 63)

def lcol_544_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 53 liquidity collapse distribution over 126d to detect tail risk or exhaustion.
    """
    base = (volume.pct_change(16).rolling(80).mean())
    return _rolling_skew(base, 126)

def lcol_545_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 53 liquidity collapse distribution over 252d to detect tail risk or exhaustion.
    """
    base = (volume.pct_change(16).rolling(80).mean())
    return _rolling_skew(base, 252)

def lcol_546_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 53 liquidity collapse over 5d to capture explosive breakdown or reversal points.
    """
    base = (volume.pct_change(16).rolling(80).mean())
    return _rolling_kurt(base, 5)

def lcol_547_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 53 liquidity collapse over 21d to capture explosive breakdown or reversal points.
    """
    base = (volume.pct_change(16).rolling(80).mean())
    return _rolling_kurt(base, 21)

def lcol_548_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 53 liquidity collapse over 63d to capture explosive breakdown or reversal points.
    """
    base = (volume.pct_change(16).rolling(80).mean())
    return _rolling_kurt(base, 63)

def lcol_549_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 53 liquidity collapse over 126d to capture explosive breakdown or reversal points.
    """
    base = (volume.pct_change(16).rolling(80).mean())
    return _rolling_kurt(base, 126)

def lcol_550_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 53 liquidity collapse over 252d to capture explosive breakdown or reversal points.
    """
    base = (volume.pct_change(16).rolling(80).mean())
    return _rolling_kurt(base, 252)

def lcol_551_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 53 liquidity collapse for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = (volume.pct_change(16).rolling(80).mean())
    return _safe_div(base, _rolling_std(base, 5))

def lcol_552_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 53 liquidity collapse for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = (volume.pct_change(16).rolling(80).mean())
    return _safe_div(base, _rolling_std(base, 21))

def lcol_553_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 53 liquidity collapse for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = (volume.pct_change(16).rolling(80).mean())
    return _safe_div(base, _rolling_std(base, 63))

def lcol_554_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 53 liquidity collapse for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = (volume.pct_change(16).rolling(80).mean())
    return _safe_div(base, _rolling_std(base, 126))

def lcol_555_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 53 liquidity collapse for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = (volume.pct_change(16).rolling(80).mean())
    return _safe_div(base, _rolling_std(base, 252))

def lcol_556_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 53 liquidity collapse over 5d to stabilize variance and capture exponential shifts.
    """
    base = (volume.pct_change(16).rolling(80).mean())
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def lcol_557_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 53 liquidity collapse over 21d to stabilize variance and capture exponential shifts.
    """
    base = (volume.pct_change(16).rolling(80).mean())
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def lcol_558_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 53 liquidity collapse over 63d to stabilize variance and capture exponential shifts.
    """
    base = (volume.pct_change(16).rolling(80).mean())
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def lcol_559_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 53 liquidity collapse over 126d to stabilize variance and capture exponential shifts.
    """
    base = (volume.pct_change(16).rolling(80).mean())
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def lcol_560_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 53 liquidity collapse over 252d to stabilize variance and capture exponential shifts.
    """
    base = (volume.pct_change(16).rolling(80).mean())
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def lcol_561_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 53 liquidity collapse over a 5d horizon to identify extreme regimes.
    """
    base = (volume.pct_change(17).rolling(85).mean())
    return _rolling_mean(base, 5)

def lcol_562_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 53 liquidity collapse over a 21d horizon to identify extreme regimes.
    """
    base = (volume.pct_change(17).rolling(85).mean())
    return _rolling_mean(base, 21)

def lcol_563_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 53 liquidity collapse over a 63d horizon to identify extreme regimes.
    """
    base = (volume.pct_change(17).rolling(85).mean())
    return _rolling_mean(base, 63)

def lcol_564_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 53 liquidity collapse over a 126d horizon to identify extreme regimes.
    """
    base = (volume.pct_change(17).rolling(85).mean())
    return _rolling_mean(base, 126)

def lcol_565_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 53 liquidity collapse over a 252d horizon to identify extreme regimes.
    """
    base = (volume.pct_change(17).rolling(85).mean())
    return _rolling_mean(base, 252)

def lcol_566_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 53 liquidity collapse by measuring deviations from the 5d mean.
    """
    base = (volume.pct_change(17).rolling(85).mean())
    return _zscore_rolling(base, 5)

def lcol_567_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 53 liquidity collapse by measuring deviations from the 21d mean.
    """
    base = (volume.pct_change(17).rolling(85).mean())
    return _zscore_rolling(base, 21)

def lcol_568_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 53 liquidity collapse by measuring deviations from the 63d mean.
    """
    base = (volume.pct_change(17).rolling(85).mean())
    return _zscore_rolling(base, 63)

def lcol_569_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 53 liquidity collapse by measuring deviations from the 126d mean.
    """
    base = (volume.pct_change(17).rolling(85).mean())
    return _zscore_rolling(base, 126)

def lcol_570_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 53 liquidity collapse by measuring deviations from the 252d mean.
    """
    base = (volume.pct_change(17).rolling(85).mean())
    return _zscore_rolling(base, 252)

def lcol_571_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 53 liquidity collapse to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = (volume.pct_change(17).rolling(85).mean())
    return _rank_pct(base, 5)

def lcol_572_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 53 liquidity collapse to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = (volume.pct_change(17).rolling(85).mean())
    return _rank_pct(base, 21)

def lcol_573_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 53 liquidity collapse to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = (volume.pct_change(17).rolling(85).mean())
    return _rank_pct(base, 63)

def lcol_574_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 53 liquidity collapse to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = (volume.pct_change(17).rolling(85).mean())
    return _rank_pct(base, 126)

def lcol_575_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 53 liquidity collapse to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = (volume.pct_change(17).rolling(85).mean())
    return _rank_pct(base, 252)

def lcol_576_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 53 liquidity collapse distribution over 5d to detect tail risk or exhaustion.
    """
    base = (volume.pct_change(17).rolling(85).mean())
    return _rolling_skew(base, 5)

def lcol_577_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 53 liquidity collapse distribution over 21d to detect tail risk or exhaustion.
    """
    base = (volume.pct_change(17).rolling(85).mean())
    return _rolling_skew(base, 21)

def lcol_578_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 53 liquidity collapse distribution over 63d to detect tail risk or exhaustion.
    """
    base = (volume.pct_change(17).rolling(85).mean())
    return _rolling_skew(base, 63)

def lcol_579_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 53 liquidity collapse distribution over 126d to detect tail risk or exhaustion.
    """
    base = (volume.pct_change(17).rolling(85).mean())
    return _rolling_skew(base, 126)

def lcol_580_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 53 liquidity collapse distribution over 252d to detect tail risk or exhaustion.
    """
    base = (volume.pct_change(17).rolling(85).mean())
    return _rolling_skew(base, 252)

def lcol_581_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 53 liquidity collapse over 5d to capture explosive breakdown or reversal points.
    """
    base = (volume.pct_change(17).rolling(85).mean())
    return _rolling_kurt(base, 5)

def lcol_582_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 53 liquidity collapse over 21d to capture explosive breakdown or reversal points.
    """
    base = (volume.pct_change(17).rolling(85).mean())
    return _rolling_kurt(base, 21)

def lcol_583_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 53 liquidity collapse over 63d to capture explosive breakdown or reversal points.
    """
    base = (volume.pct_change(17).rolling(85).mean())
    return _rolling_kurt(base, 63)

def lcol_584_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 53 liquidity collapse over 126d to capture explosive breakdown or reversal points.
    """
    base = (volume.pct_change(17).rolling(85).mean())
    return _rolling_kurt(base, 126)

def lcol_585_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 53 liquidity collapse over 252d to capture explosive breakdown or reversal points.
    """
    base = (volume.pct_change(17).rolling(85).mean())
    return _rolling_kurt(base, 252)

def lcol_586_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 53 liquidity collapse for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = (volume.pct_change(17).rolling(85).mean())
    return _safe_div(base, _rolling_std(base, 5))

def lcol_587_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 53 liquidity collapse for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = (volume.pct_change(17).rolling(85).mean())
    return _safe_div(base, _rolling_std(base, 21))

def lcol_588_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 53 liquidity collapse for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = (volume.pct_change(17).rolling(85).mean())
    return _safe_div(base, _rolling_std(base, 63))

def lcol_589_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 53 liquidity collapse for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = (volume.pct_change(17).rolling(85).mean())
    return _safe_div(base, _rolling_std(base, 126))

def lcol_590_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 53 liquidity collapse for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = (volume.pct_change(17).rolling(85).mean())
    return _safe_div(base, _rolling_std(base, 252))

def lcol_591_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 53 liquidity collapse over 5d to stabilize variance and capture exponential shifts.
    """
    base = (volume.pct_change(17).rolling(85).mean())
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def lcol_592_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 53 liquidity collapse over 21d to stabilize variance and capture exponential shifts.
    """
    base = (volume.pct_change(17).rolling(85).mean())
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def lcol_593_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 53 liquidity collapse over 63d to stabilize variance and capture exponential shifts.
    """
    base = (volume.pct_change(17).rolling(85).mean())
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def lcol_594_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 53 liquidity collapse over 126d to stabilize variance and capture exponential shifts.
    """
    base = (volume.pct_change(17).rolling(85).mean())
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def lcol_595_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 53 liquidity collapse over 252d to stabilize variance and capture exponential shifts.
    """
    base = (volume.pct_change(17).rolling(85).mean())
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def lcol_596_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 53 liquidity collapse over a 5d horizon to identify extreme regimes.
    """
    base = (volume.pct_change(18).rolling(90).mean())
    return _rolling_mean(base, 5)

def lcol_597_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 53 liquidity collapse over a 21d horizon to identify extreme regimes.
    """
    base = (volume.pct_change(18).rolling(90).mean())
    return _rolling_mean(base, 21)

def lcol_598_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 53 liquidity collapse over a 63d horizon to identify extreme regimes.
    """
    base = (volume.pct_change(18).rolling(90).mean())
    return _rolling_mean(base, 63)

def lcol_599_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 53 liquidity collapse over a 126d horizon to identify extreme regimes.
    """
    base = (volume.pct_change(18).rolling(90).mean())
    return _rolling_mean(base, 126)

def lcol_600_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 53 liquidity collapse over a 252d horizon to identify extreme regimes.
    """
    base = (volume.pct_change(18).rolling(90).mean())
    return _rolling_mean(base, 252)
