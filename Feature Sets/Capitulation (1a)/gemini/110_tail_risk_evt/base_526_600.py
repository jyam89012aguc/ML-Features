"""
110_110_tail_risk_evt — Base Features 526-600
Domain: 110_tail_risk_evt
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

def trev_526_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 110 tail risk evt over a 5d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(800).quantile(0.01)
    return _rolling_mean(base, 5)

def trev_527_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 110 tail risk evt over a 21d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(800).quantile(0.01)
    return _rolling_mean(base, 21)

def trev_528_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 110 tail risk evt over a 63d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(800).quantile(0.01)
    return _rolling_mean(base, 63)

def trev_529_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 110 tail risk evt over a 126d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(800).quantile(0.01)
    return _rolling_mean(base, 126)

def trev_530_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 110 tail risk evt over a 252d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(800).quantile(0.01)
    return _rolling_mean(base, 252)

def trev_531_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 110 tail risk evt by measuring deviations from the 5d mean.
    """
    base = close.pct_change().rolling(800).quantile(0.01)
    return _zscore_rolling(base, 5)

def trev_532_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 110 tail risk evt by measuring deviations from the 21d mean.
    """
    base = close.pct_change().rolling(800).quantile(0.01)
    return _zscore_rolling(base, 21)

def trev_533_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 110 tail risk evt by measuring deviations from the 63d mean.
    """
    base = close.pct_change().rolling(800).quantile(0.01)
    return _zscore_rolling(base, 63)

def trev_534_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 110 tail risk evt by measuring deviations from the 126d mean.
    """
    base = close.pct_change().rolling(800).quantile(0.01)
    return _zscore_rolling(base, 126)

def trev_535_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 110 tail risk evt by measuring deviations from the 252d mean.
    """
    base = close.pct_change().rolling(800).quantile(0.01)
    return _zscore_rolling(base, 252)

def trev_536_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 110 tail risk evt to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(800).quantile(0.01)
    return _rank_pct(base, 5)

def trev_537_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 110 tail risk evt to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(800).quantile(0.01)
    return _rank_pct(base, 21)

def trev_538_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 110 tail risk evt to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(800).quantile(0.01)
    return _rank_pct(base, 63)

def trev_539_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 110 tail risk evt to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(800).quantile(0.01)
    return _rank_pct(base, 126)

def trev_540_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 110 tail risk evt to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(800).quantile(0.01)
    return _rank_pct(base, 252)

def trev_541_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 110 tail risk evt distribution over 5d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(800).quantile(0.01)
    return _rolling_skew(base, 5)

def trev_542_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 110 tail risk evt distribution over 21d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(800).quantile(0.01)
    return _rolling_skew(base, 21)

def trev_543_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 110 tail risk evt distribution over 63d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(800).quantile(0.01)
    return _rolling_skew(base, 63)

def trev_544_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 110 tail risk evt distribution over 126d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(800).quantile(0.01)
    return _rolling_skew(base, 126)

def trev_545_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 110 tail risk evt distribution over 252d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(800).quantile(0.01)
    return _rolling_skew(base, 252)

def trev_546_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 110 tail risk evt over 5d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(800).quantile(0.01)
    return _rolling_kurt(base, 5)

def trev_547_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 110 tail risk evt over 21d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(800).quantile(0.01)
    return _rolling_kurt(base, 21)

def trev_548_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 110 tail risk evt over 63d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(800).quantile(0.01)
    return _rolling_kurt(base, 63)

def trev_549_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 110 tail risk evt over 126d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(800).quantile(0.01)
    return _rolling_kurt(base, 126)

def trev_550_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 110 tail risk evt over 252d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(800).quantile(0.01)
    return _rolling_kurt(base, 252)

def trev_551_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 110 tail risk evt for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(800).quantile(0.01)
    return _safe_div(base, _rolling_std(base, 5))

def trev_552_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 110 tail risk evt for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(800).quantile(0.01)
    return _safe_div(base, _rolling_std(base, 21))

def trev_553_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 110 tail risk evt for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(800).quantile(0.01)
    return _safe_div(base, _rolling_std(base, 63))

def trev_554_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 110 tail risk evt for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(800).quantile(0.01)
    return _safe_div(base, _rolling_std(base, 126))

def trev_555_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 110 tail risk evt for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(800).quantile(0.01)
    return _safe_div(base, _rolling_std(base, 252))

def trev_556_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 110 tail risk evt over 5d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(800).quantile(0.01)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def trev_557_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 110 tail risk evt over 21d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(800).quantile(0.01)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def trev_558_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 110 tail risk evt over 63d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(800).quantile(0.01)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def trev_559_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 110 tail risk evt over 126d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(800).quantile(0.01)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def trev_560_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 110 tail risk evt over 252d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(800).quantile(0.01)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def trev_561_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 110 tail risk evt over a 5d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(850).quantile(0.01)
    return _rolling_mean(base, 5)

def trev_562_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 110 tail risk evt over a 21d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(850).quantile(0.01)
    return _rolling_mean(base, 21)

def trev_563_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 110 tail risk evt over a 63d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(850).quantile(0.01)
    return _rolling_mean(base, 63)

def trev_564_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 110 tail risk evt over a 126d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(850).quantile(0.01)
    return _rolling_mean(base, 126)

def trev_565_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 110 tail risk evt over a 252d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(850).quantile(0.01)
    return _rolling_mean(base, 252)

def trev_566_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 110 tail risk evt by measuring deviations from the 5d mean.
    """
    base = close.pct_change().rolling(850).quantile(0.01)
    return _zscore_rolling(base, 5)

def trev_567_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 110 tail risk evt by measuring deviations from the 21d mean.
    """
    base = close.pct_change().rolling(850).quantile(0.01)
    return _zscore_rolling(base, 21)

def trev_568_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 110 tail risk evt by measuring deviations from the 63d mean.
    """
    base = close.pct_change().rolling(850).quantile(0.01)
    return _zscore_rolling(base, 63)

def trev_569_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 110 tail risk evt by measuring deviations from the 126d mean.
    """
    base = close.pct_change().rolling(850).quantile(0.01)
    return _zscore_rolling(base, 126)

def trev_570_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 110 tail risk evt by measuring deviations from the 252d mean.
    """
    base = close.pct_change().rolling(850).quantile(0.01)
    return _zscore_rolling(base, 252)

def trev_571_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 110 tail risk evt to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(850).quantile(0.01)
    return _rank_pct(base, 5)

def trev_572_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 110 tail risk evt to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(850).quantile(0.01)
    return _rank_pct(base, 21)

def trev_573_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 110 tail risk evt to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(850).quantile(0.01)
    return _rank_pct(base, 63)

def trev_574_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 110 tail risk evt to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(850).quantile(0.01)
    return _rank_pct(base, 126)

def trev_575_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 110 tail risk evt to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(850).quantile(0.01)
    return _rank_pct(base, 252)

def trev_576_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 110 tail risk evt distribution over 5d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(850).quantile(0.01)
    return _rolling_skew(base, 5)

def trev_577_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 110 tail risk evt distribution over 21d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(850).quantile(0.01)
    return _rolling_skew(base, 21)

def trev_578_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 110 tail risk evt distribution over 63d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(850).quantile(0.01)
    return _rolling_skew(base, 63)

def trev_579_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 110 tail risk evt distribution over 126d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(850).quantile(0.01)
    return _rolling_skew(base, 126)

def trev_580_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 110 tail risk evt distribution over 252d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(850).quantile(0.01)
    return _rolling_skew(base, 252)

def trev_581_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 110 tail risk evt over 5d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(850).quantile(0.01)
    return _rolling_kurt(base, 5)

def trev_582_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 110 tail risk evt over 21d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(850).quantile(0.01)
    return _rolling_kurt(base, 21)

def trev_583_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 110 tail risk evt over 63d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(850).quantile(0.01)
    return _rolling_kurt(base, 63)

def trev_584_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 110 tail risk evt over 126d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(850).quantile(0.01)
    return _rolling_kurt(base, 126)

def trev_585_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 110 tail risk evt over 252d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(850).quantile(0.01)
    return _rolling_kurt(base, 252)

def trev_586_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 110 tail risk evt for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(850).quantile(0.01)
    return _safe_div(base, _rolling_std(base, 5))

def trev_587_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 110 tail risk evt for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(850).quantile(0.01)
    return _safe_div(base, _rolling_std(base, 21))

def trev_588_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 110 tail risk evt for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(850).quantile(0.01)
    return _safe_div(base, _rolling_std(base, 63))

def trev_589_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 110 tail risk evt for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(850).quantile(0.01)
    return _safe_div(base, _rolling_std(base, 126))

def trev_590_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 110 tail risk evt for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(850).quantile(0.01)
    return _safe_div(base, _rolling_std(base, 252))

def trev_591_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 110 tail risk evt over 5d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(850).quantile(0.01)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def trev_592_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 110 tail risk evt over 21d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(850).quantile(0.01)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def trev_593_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 110 tail risk evt over 63d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(850).quantile(0.01)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def trev_594_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 110 tail risk evt over 126d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(850).quantile(0.01)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def trev_595_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 110 tail risk evt over 252d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(850).quantile(0.01)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def trev_596_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 110 tail risk evt over a 5d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(900).quantile(0.01)
    return _rolling_mean(base, 5)

def trev_597_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 110 tail risk evt over a 21d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(900).quantile(0.01)
    return _rolling_mean(base, 21)

def trev_598_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 110 tail risk evt over a 63d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(900).quantile(0.01)
    return _rolling_mean(base, 63)

def trev_599_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 110 tail risk evt over a 126d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(900).quantile(0.01)
    return _rolling_mean(base, 126)

def trev_600_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 110 tail risk evt over a 252d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(900).quantile(0.01)
    return _rolling_mean(base, 252)
