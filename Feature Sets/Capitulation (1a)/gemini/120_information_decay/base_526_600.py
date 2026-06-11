"""
120_120_information_decay — Base Features 526-600
Domain: 120_information_decay
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

def idec_526_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 120 information decay over a 5d horizon to identify extreme regimes.
    """
    base = close.diff().abs().rolling(80).sum()
    return _rolling_mean(base, 5)

def idec_527_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 120 information decay over a 21d horizon to identify extreme regimes.
    """
    base = close.diff().abs().rolling(80).sum()
    return _rolling_mean(base, 21)

def idec_528_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 120 information decay over a 63d horizon to identify extreme regimes.
    """
    base = close.diff().abs().rolling(80).sum()
    return _rolling_mean(base, 63)

def idec_529_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 120 information decay over a 126d horizon to identify extreme regimes.
    """
    base = close.diff().abs().rolling(80).sum()
    return _rolling_mean(base, 126)

def idec_530_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 120 information decay over a 252d horizon to identify extreme regimes.
    """
    base = close.diff().abs().rolling(80).sum()
    return _rolling_mean(base, 252)

def idec_531_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 120 information decay by measuring deviations from the 5d mean.
    """
    base = close.diff().abs().rolling(80).sum()
    return _zscore_rolling(base, 5)

def idec_532_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 120 information decay by measuring deviations from the 21d mean.
    """
    base = close.diff().abs().rolling(80).sum()
    return _zscore_rolling(base, 21)

def idec_533_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 120 information decay by measuring deviations from the 63d mean.
    """
    base = close.diff().abs().rolling(80).sum()
    return _zscore_rolling(base, 63)

def idec_534_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 120 information decay by measuring deviations from the 126d mean.
    """
    base = close.diff().abs().rolling(80).sum()
    return _zscore_rolling(base, 126)

def idec_535_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 120 information decay by measuring deviations from the 252d mean.
    """
    base = close.diff().abs().rolling(80).sum()
    return _zscore_rolling(base, 252)

def idec_536_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 120 information decay to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = close.diff().abs().rolling(80).sum()
    return _rank_pct(base, 5)

def idec_537_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 120 information decay to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = close.diff().abs().rolling(80).sum()
    return _rank_pct(base, 21)

def idec_538_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 120 information decay to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = close.diff().abs().rolling(80).sum()
    return _rank_pct(base, 63)

def idec_539_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 120 information decay to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = close.diff().abs().rolling(80).sum()
    return _rank_pct(base, 126)

def idec_540_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 120 information decay to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = close.diff().abs().rolling(80).sum()
    return _rank_pct(base, 252)

def idec_541_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 120 information decay distribution over 5d to detect tail risk or exhaustion.
    """
    base = close.diff().abs().rolling(80).sum()
    return _rolling_skew(base, 5)

def idec_542_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 120 information decay distribution over 21d to detect tail risk or exhaustion.
    """
    base = close.diff().abs().rolling(80).sum()
    return _rolling_skew(base, 21)

def idec_543_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 120 information decay distribution over 63d to detect tail risk or exhaustion.
    """
    base = close.diff().abs().rolling(80).sum()
    return _rolling_skew(base, 63)

def idec_544_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 120 information decay distribution over 126d to detect tail risk or exhaustion.
    """
    base = close.diff().abs().rolling(80).sum()
    return _rolling_skew(base, 126)

def idec_545_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 120 information decay distribution over 252d to detect tail risk or exhaustion.
    """
    base = close.diff().abs().rolling(80).sum()
    return _rolling_skew(base, 252)

def idec_546_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 120 information decay over 5d to capture explosive breakdown or reversal points.
    """
    base = close.diff().abs().rolling(80).sum()
    return _rolling_kurt(base, 5)

def idec_547_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 120 information decay over 21d to capture explosive breakdown or reversal points.
    """
    base = close.diff().abs().rolling(80).sum()
    return _rolling_kurt(base, 21)

def idec_548_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 120 information decay over 63d to capture explosive breakdown or reversal points.
    """
    base = close.diff().abs().rolling(80).sum()
    return _rolling_kurt(base, 63)

def idec_549_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 120 information decay over 126d to capture explosive breakdown or reversal points.
    """
    base = close.diff().abs().rolling(80).sum()
    return _rolling_kurt(base, 126)

def idec_550_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 120 information decay over 252d to capture explosive breakdown or reversal points.
    """
    base = close.diff().abs().rolling(80).sum()
    return _rolling_kurt(base, 252)

def idec_551_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 120 information decay for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = close.diff().abs().rolling(80).sum()
    return _safe_div(base, _rolling_std(base, 5))

def idec_552_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 120 information decay for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = close.diff().abs().rolling(80).sum()
    return _safe_div(base, _rolling_std(base, 21))

def idec_553_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 120 information decay for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = close.diff().abs().rolling(80).sum()
    return _safe_div(base, _rolling_std(base, 63))

def idec_554_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 120 information decay for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = close.diff().abs().rolling(80).sum()
    return _safe_div(base, _rolling_std(base, 126))

def idec_555_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 120 information decay for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = close.diff().abs().rolling(80).sum()
    return _safe_div(base, _rolling_std(base, 252))

def idec_556_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 120 information decay over 5d to stabilize variance and capture exponential shifts.
    """
    base = close.diff().abs().rolling(80).sum()
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def idec_557_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 120 information decay over 21d to stabilize variance and capture exponential shifts.
    """
    base = close.diff().abs().rolling(80).sum()
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def idec_558_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 120 information decay over 63d to stabilize variance and capture exponential shifts.
    """
    base = close.diff().abs().rolling(80).sum()
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def idec_559_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 120 information decay over 126d to stabilize variance and capture exponential shifts.
    """
    base = close.diff().abs().rolling(80).sum()
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def idec_560_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 120 information decay over 252d to stabilize variance and capture exponential shifts.
    """
    base = close.diff().abs().rolling(80).sum()
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def idec_561_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 120 information decay over a 5d horizon to identify extreme regimes.
    """
    base = close.diff().abs().rolling(85).sum()
    return _rolling_mean(base, 5)

def idec_562_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 120 information decay over a 21d horizon to identify extreme regimes.
    """
    base = close.diff().abs().rolling(85).sum()
    return _rolling_mean(base, 21)

def idec_563_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 120 information decay over a 63d horizon to identify extreme regimes.
    """
    base = close.diff().abs().rolling(85).sum()
    return _rolling_mean(base, 63)

def idec_564_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 120 information decay over a 126d horizon to identify extreme regimes.
    """
    base = close.diff().abs().rolling(85).sum()
    return _rolling_mean(base, 126)

def idec_565_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 120 information decay over a 252d horizon to identify extreme regimes.
    """
    base = close.diff().abs().rolling(85).sum()
    return _rolling_mean(base, 252)

def idec_566_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 120 information decay by measuring deviations from the 5d mean.
    """
    base = close.diff().abs().rolling(85).sum()
    return _zscore_rolling(base, 5)

def idec_567_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 120 information decay by measuring deviations from the 21d mean.
    """
    base = close.diff().abs().rolling(85).sum()
    return _zscore_rolling(base, 21)

def idec_568_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 120 information decay by measuring deviations from the 63d mean.
    """
    base = close.diff().abs().rolling(85).sum()
    return _zscore_rolling(base, 63)

def idec_569_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 120 information decay by measuring deviations from the 126d mean.
    """
    base = close.diff().abs().rolling(85).sum()
    return _zscore_rolling(base, 126)

def idec_570_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 120 information decay by measuring deviations from the 252d mean.
    """
    base = close.diff().abs().rolling(85).sum()
    return _zscore_rolling(base, 252)

def idec_571_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 120 information decay to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = close.diff().abs().rolling(85).sum()
    return _rank_pct(base, 5)

def idec_572_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 120 information decay to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = close.diff().abs().rolling(85).sum()
    return _rank_pct(base, 21)

def idec_573_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 120 information decay to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = close.diff().abs().rolling(85).sum()
    return _rank_pct(base, 63)

def idec_574_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 120 information decay to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = close.diff().abs().rolling(85).sum()
    return _rank_pct(base, 126)

def idec_575_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 120 information decay to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = close.diff().abs().rolling(85).sum()
    return _rank_pct(base, 252)

def idec_576_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 120 information decay distribution over 5d to detect tail risk or exhaustion.
    """
    base = close.diff().abs().rolling(85).sum()
    return _rolling_skew(base, 5)

def idec_577_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 120 information decay distribution over 21d to detect tail risk or exhaustion.
    """
    base = close.diff().abs().rolling(85).sum()
    return _rolling_skew(base, 21)

def idec_578_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 120 information decay distribution over 63d to detect tail risk or exhaustion.
    """
    base = close.diff().abs().rolling(85).sum()
    return _rolling_skew(base, 63)

def idec_579_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 120 information decay distribution over 126d to detect tail risk or exhaustion.
    """
    base = close.diff().abs().rolling(85).sum()
    return _rolling_skew(base, 126)

def idec_580_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 120 information decay distribution over 252d to detect tail risk or exhaustion.
    """
    base = close.diff().abs().rolling(85).sum()
    return _rolling_skew(base, 252)

def idec_581_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 120 information decay over 5d to capture explosive breakdown or reversal points.
    """
    base = close.diff().abs().rolling(85).sum()
    return _rolling_kurt(base, 5)

def idec_582_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 120 information decay over 21d to capture explosive breakdown or reversal points.
    """
    base = close.diff().abs().rolling(85).sum()
    return _rolling_kurt(base, 21)

def idec_583_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 120 information decay over 63d to capture explosive breakdown or reversal points.
    """
    base = close.diff().abs().rolling(85).sum()
    return _rolling_kurt(base, 63)

def idec_584_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 120 information decay over 126d to capture explosive breakdown or reversal points.
    """
    base = close.diff().abs().rolling(85).sum()
    return _rolling_kurt(base, 126)

def idec_585_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 120 information decay over 252d to capture explosive breakdown or reversal points.
    """
    base = close.diff().abs().rolling(85).sum()
    return _rolling_kurt(base, 252)

def idec_586_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 120 information decay for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = close.diff().abs().rolling(85).sum()
    return _safe_div(base, _rolling_std(base, 5))

def idec_587_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 120 information decay for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = close.diff().abs().rolling(85).sum()
    return _safe_div(base, _rolling_std(base, 21))

def idec_588_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 120 information decay for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = close.diff().abs().rolling(85).sum()
    return _safe_div(base, _rolling_std(base, 63))

def idec_589_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 120 information decay for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = close.diff().abs().rolling(85).sum()
    return _safe_div(base, _rolling_std(base, 126))

def idec_590_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 120 information decay for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = close.diff().abs().rolling(85).sum()
    return _safe_div(base, _rolling_std(base, 252))

def idec_591_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 120 information decay over 5d to stabilize variance and capture exponential shifts.
    """
    base = close.diff().abs().rolling(85).sum()
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def idec_592_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 120 information decay over 21d to stabilize variance and capture exponential shifts.
    """
    base = close.diff().abs().rolling(85).sum()
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def idec_593_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 120 information decay over 63d to stabilize variance and capture exponential shifts.
    """
    base = close.diff().abs().rolling(85).sum()
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def idec_594_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 120 information decay over 126d to stabilize variance and capture exponential shifts.
    """
    base = close.diff().abs().rolling(85).sum()
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def idec_595_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 120 information decay over 252d to stabilize variance and capture exponential shifts.
    """
    base = close.diff().abs().rolling(85).sum()
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def idec_596_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 120 information decay over a 5d horizon to identify extreme regimes.
    """
    base = close.diff().abs().rolling(90).sum()
    return _rolling_mean(base, 5)

def idec_597_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 120 information decay over a 21d horizon to identify extreme regimes.
    """
    base = close.diff().abs().rolling(90).sum()
    return _rolling_mean(base, 21)

def idec_598_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 120 information decay over a 63d horizon to identify extreme regimes.
    """
    base = close.diff().abs().rolling(90).sum()
    return _rolling_mean(base, 63)

def idec_599_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 120 information decay over a 126d horizon to identify extreme regimes.
    """
    base = close.diff().abs().rolling(90).sum()
    return _rolling_mean(base, 126)

def idec_600_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 120 information decay over a 252d horizon to identify extreme regimes.
    """
    base = close.diff().abs().rolling(90).sum()
    return _rolling_mean(base, 252)
