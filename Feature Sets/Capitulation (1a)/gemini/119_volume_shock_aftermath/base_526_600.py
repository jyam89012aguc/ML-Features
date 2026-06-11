"""
119_119_volume_shock_aftermath — Base Features 526-600
Domain: 119_volume_shock_aftermath
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

def vsha_526_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 119 volume shock aftermath over a 5d horizon to identify extreme regimes.
    """
    base = volume / _rolling_mean(volume, 160)
    return _rolling_mean(base, 5)

def vsha_527_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 119 volume shock aftermath over a 21d horizon to identify extreme regimes.
    """
    base = volume / _rolling_mean(volume, 160)
    return _rolling_mean(base, 21)

def vsha_528_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 119 volume shock aftermath over a 63d horizon to identify extreme regimes.
    """
    base = volume / _rolling_mean(volume, 160)
    return _rolling_mean(base, 63)

def vsha_529_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 119 volume shock aftermath over a 126d horizon to identify extreme regimes.
    """
    base = volume / _rolling_mean(volume, 160)
    return _rolling_mean(base, 126)

def vsha_530_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 119 volume shock aftermath over a 252d horizon to identify extreme regimes.
    """
    base = volume / _rolling_mean(volume, 160)
    return _rolling_mean(base, 252)

def vsha_531_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 119 volume shock aftermath by measuring deviations from the 5d mean.
    """
    base = volume / _rolling_mean(volume, 160)
    return _zscore_rolling(base, 5)

def vsha_532_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 119 volume shock aftermath by measuring deviations from the 21d mean.
    """
    base = volume / _rolling_mean(volume, 160)
    return _zscore_rolling(base, 21)

def vsha_533_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 119 volume shock aftermath by measuring deviations from the 63d mean.
    """
    base = volume / _rolling_mean(volume, 160)
    return _zscore_rolling(base, 63)

def vsha_534_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 119 volume shock aftermath by measuring deviations from the 126d mean.
    """
    base = volume / _rolling_mean(volume, 160)
    return _zscore_rolling(base, 126)

def vsha_535_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 119 volume shock aftermath by measuring deviations from the 252d mean.
    """
    base = volume / _rolling_mean(volume, 160)
    return _zscore_rolling(base, 252)

def vsha_536_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 119 volume shock aftermath to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = volume / _rolling_mean(volume, 160)
    return _rank_pct(base, 5)

def vsha_537_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 119 volume shock aftermath to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = volume / _rolling_mean(volume, 160)
    return _rank_pct(base, 21)

def vsha_538_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 119 volume shock aftermath to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = volume / _rolling_mean(volume, 160)
    return _rank_pct(base, 63)

def vsha_539_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 119 volume shock aftermath to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = volume / _rolling_mean(volume, 160)
    return _rank_pct(base, 126)

def vsha_540_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 119 volume shock aftermath to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = volume / _rolling_mean(volume, 160)
    return _rank_pct(base, 252)

def vsha_541_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 119 volume shock aftermath distribution over 5d to detect tail risk or exhaustion.
    """
    base = volume / _rolling_mean(volume, 160)
    return _rolling_skew(base, 5)

def vsha_542_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 119 volume shock aftermath distribution over 21d to detect tail risk or exhaustion.
    """
    base = volume / _rolling_mean(volume, 160)
    return _rolling_skew(base, 21)

def vsha_543_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 119 volume shock aftermath distribution over 63d to detect tail risk or exhaustion.
    """
    base = volume / _rolling_mean(volume, 160)
    return _rolling_skew(base, 63)

def vsha_544_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 119 volume shock aftermath distribution over 126d to detect tail risk or exhaustion.
    """
    base = volume / _rolling_mean(volume, 160)
    return _rolling_skew(base, 126)

def vsha_545_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 119 volume shock aftermath distribution over 252d to detect tail risk or exhaustion.
    """
    base = volume / _rolling_mean(volume, 160)
    return _rolling_skew(base, 252)

def vsha_546_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 119 volume shock aftermath over 5d to capture explosive breakdown or reversal points.
    """
    base = volume / _rolling_mean(volume, 160)
    return _rolling_kurt(base, 5)

def vsha_547_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 119 volume shock aftermath over 21d to capture explosive breakdown or reversal points.
    """
    base = volume / _rolling_mean(volume, 160)
    return _rolling_kurt(base, 21)

def vsha_548_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 119 volume shock aftermath over 63d to capture explosive breakdown or reversal points.
    """
    base = volume / _rolling_mean(volume, 160)
    return _rolling_kurt(base, 63)

def vsha_549_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 119 volume shock aftermath over 126d to capture explosive breakdown or reversal points.
    """
    base = volume / _rolling_mean(volume, 160)
    return _rolling_kurt(base, 126)

def vsha_550_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 119 volume shock aftermath over 252d to capture explosive breakdown or reversal points.
    """
    base = volume / _rolling_mean(volume, 160)
    return _rolling_kurt(base, 252)

def vsha_551_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 119 volume shock aftermath for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = volume / _rolling_mean(volume, 160)
    return _safe_div(base, _rolling_std(base, 5))

def vsha_552_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 119 volume shock aftermath for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = volume / _rolling_mean(volume, 160)
    return _safe_div(base, _rolling_std(base, 21))

def vsha_553_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 119 volume shock aftermath for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = volume / _rolling_mean(volume, 160)
    return _safe_div(base, _rolling_std(base, 63))

def vsha_554_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 119 volume shock aftermath for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = volume / _rolling_mean(volume, 160)
    return _safe_div(base, _rolling_std(base, 126))

def vsha_555_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 119 volume shock aftermath for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = volume / _rolling_mean(volume, 160)
    return _safe_div(base, _rolling_std(base, 252))

def vsha_556_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 119 volume shock aftermath over 5d to stabilize variance and capture exponential shifts.
    """
    base = volume / _rolling_mean(volume, 160)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def vsha_557_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 119 volume shock aftermath over 21d to stabilize variance and capture exponential shifts.
    """
    base = volume / _rolling_mean(volume, 160)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def vsha_558_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 119 volume shock aftermath over 63d to stabilize variance and capture exponential shifts.
    """
    base = volume / _rolling_mean(volume, 160)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def vsha_559_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 119 volume shock aftermath over 126d to stabilize variance and capture exponential shifts.
    """
    base = volume / _rolling_mean(volume, 160)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def vsha_560_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 119 volume shock aftermath over 252d to stabilize variance and capture exponential shifts.
    """
    base = volume / _rolling_mean(volume, 160)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def vsha_561_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 119 volume shock aftermath over a 5d horizon to identify extreme regimes.
    """
    base = volume / _rolling_mean(volume, 170)
    return _rolling_mean(base, 5)

def vsha_562_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 119 volume shock aftermath over a 21d horizon to identify extreme regimes.
    """
    base = volume / _rolling_mean(volume, 170)
    return _rolling_mean(base, 21)

def vsha_563_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 119 volume shock aftermath over a 63d horizon to identify extreme regimes.
    """
    base = volume / _rolling_mean(volume, 170)
    return _rolling_mean(base, 63)

def vsha_564_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 119 volume shock aftermath over a 126d horizon to identify extreme regimes.
    """
    base = volume / _rolling_mean(volume, 170)
    return _rolling_mean(base, 126)

def vsha_565_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 119 volume shock aftermath over a 252d horizon to identify extreme regimes.
    """
    base = volume / _rolling_mean(volume, 170)
    return _rolling_mean(base, 252)

def vsha_566_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 119 volume shock aftermath by measuring deviations from the 5d mean.
    """
    base = volume / _rolling_mean(volume, 170)
    return _zscore_rolling(base, 5)

def vsha_567_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 119 volume shock aftermath by measuring deviations from the 21d mean.
    """
    base = volume / _rolling_mean(volume, 170)
    return _zscore_rolling(base, 21)

def vsha_568_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 119 volume shock aftermath by measuring deviations from the 63d mean.
    """
    base = volume / _rolling_mean(volume, 170)
    return _zscore_rolling(base, 63)

def vsha_569_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 119 volume shock aftermath by measuring deviations from the 126d mean.
    """
    base = volume / _rolling_mean(volume, 170)
    return _zscore_rolling(base, 126)

def vsha_570_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 119 volume shock aftermath by measuring deviations from the 252d mean.
    """
    base = volume / _rolling_mean(volume, 170)
    return _zscore_rolling(base, 252)

def vsha_571_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 119 volume shock aftermath to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = volume / _rolling_mean(volume, 170)
    return _rank_pct(base, 5)

def vsha_572_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 119 volume shock aftermath to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = volume / _rolling_mean(volume, 170)
    return _rank_pct(base, 21)

def vsha_573_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 119 volume shock aftermath to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = volume / _rolling_mean(volume, 170)
    return _rank_pct(base, 63)

def vsha_574_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 119 volume shock aftermath to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = volume / _rolling_mean(volume, 170)
    return _rank_pct(base, 126)

def vsha_575_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 119 volume shock aftermath to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = volume / _rolling_mean(volume, 170)
    return _rank_pct(base, 252)

def vsha_576_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 119 volume shock aftermath distribution over 5d to detect tail risk or exhaustion.
    """
    base = volume / _rolling_mean(volume, 170)
    return _rolling_skew(base, 5)

def vsha_577_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 119 volume shock aftermath distribution over 21d to detect tail risk or exhaustion.
    """
    base = volume / _rolling_mean(volume, 170)
    return _rolling_skew(base, 21)

def vsha_578_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 119 volume shock aftermath distribution over 63d to detect tail risk or exhaustion.
    """
    base = volume / _rolling_mean(volume, 170)
    return _rolling_skew(base, 63)

def vsha_579_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 119 volume shock aftermath distribution over 126d to detect tail risk or exhaustion.
    """
    base = volume / _rolling_mean(volume, 170)
    return _rolling_skew(base, 126)

def vsha_580_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 119 volume shock aftermath distribution over 252d to detect tail risk or exhaustion.
    """
    base = volume / _rolling_mean(volume, 170)
    return _rolling_skew(base, 252)

def vsha_581_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 119 volume shock aftermath over 5d to capture explosive breakdown or reversal points.
    """
    base = volume / _rolling_mean(volume, 170)
    return _rolling_kurt(base, 5)

def vsha_582_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 119 volume shock aftermath over 21d to capture explosive breakdown or reversal points.
    """
    base = volume / _rolling_mean(volume, 170)
    return _rolling_kurt(base, 21)

def vsha_583_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 119 volume shock aftermath over 63d to capture explosive breakdown or reversal points.
    """
    base = volume / _rolling_mean(volume, 170)
    return _rolling_kurt(base, 63)

def vsha_584_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 119 volume shock aftermath over 126d to capture explosive breakdown or reversal points.
    """
    base = volume / _rolling_mean(volume, 170)
    return _rolling_kurt(base, 126)

def vsha_585_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 119 volume shock aftermath over 252d to capture explosive breakdown or reversal points.
    """
    base = volume / _rolling_mean(volume, 170)
    return _rolling_kurt(base, 252)

def vsha_586_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 119 volume shock aftermath for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = volume / _rolling_mean(volume, 170)
    return _safe_div(base, _rolling_std(base, 5))

def vsha_587_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 119 volume shock aftermath for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = volume / _rolling_mean(volume, 170)
    return _safe_div(base, _rolling_std(base, 21))

def vsha_588_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 119 volume shock aftermath for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = volume / _rolling_mean(volume, 170)
    return _safe_div(base, _rolling_std(base, 63))

def vsha_589_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 119 volume shock aftermath for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = volume / _rolling_mean(volume, 170)
    return _safe_div(base, _rolling_std(base, 126))

def vsha_590_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 119 volume shock aftermath for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = volume / _rolling_mean(volume, 170)
    return _safe_div(base, _rolling_std(base, 252))

def vsha_591_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 119 volume shock aftermath over 5d to stabilize variance and capture exponential shifts.
    """
    base = volume / _rolling_mean(volume, 170)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def vsha_592_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 119 volume shock aftermath over 21d to stabilize variance and capture exponential shifts.
    """
    base = volume / _rolling_mean(volume, 170)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def vsha_593_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 119 volume shock aftermath over 63d to stabilize variance and capture exponential shifts.
    """
    base = volume / _rolling_mean(volume, 170)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def vsha_594_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 119 volume shock aftermath over 126d to stabilize variance and capture exponential shifts.
    """
    base = volume / _rolling_mean(volume, 170)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def vsha_595_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 119 volume shock aftermath over 252d to stabilize variance and capture exponential shifts.
    """
    base = volume / _rolling_mean(volume, 170)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def vsha_596_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 119 volume shock aftermath over a 5d horizon to identify extreme regimes.
    """
    base = volume / _rolling_mean(volume, 180)
    return _rolling_mean(base, 5)

def vsha_597_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 119 volume shock aftermath over a 21d horizon to identify extreme regimes.
    """
    base = volume / _rolling_mean(volume, 180)
    return _rolling_mean(base, 21)

def vsha_598_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 119 volume shock aftermath over a 63d horizon to identify extreme regimes.
    """
    base = volume / _rolling_mean(volume, 180)
    return _rolling_mean(base, 63)

def vsha_599_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 119 volume shock aftermath over a 126d horizon to identify extreme regimes.
    """
    base = volume / _rolling_mean(volume, 180)
    return _rolling_mean(base, 126)

def vsha_600_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 119 volume shock aftermath over a 252d horizon to identify extreme regimes.
    """
    base = volume / _rolling_mean(volume, 180)
    return _rolling_mean(base, 252)
