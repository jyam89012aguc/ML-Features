"""
01_01_drawdown_depth — Base Features 526-600
Domain: 01_drawdown_depth
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

def dd_526_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 01 drawdown depth over a 5d horizon to identify extreme regimes.
    """
    base = (close.pct_change(16).rolling(80).mean())
    return _rolling_mean(base, 5)

def dd_527_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 01 drawdown depth over a 21d horizon to identify extreme regimes.
    """
    base = (close.pct_change(16).rolling(80).mean())
    return _rolling_mean(base, 21)

def dd_528_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 01 drawdown depth over a 63d horizon to identify extreme regimes.
    """
    base = (close.pct_change(16).rolling(80).mean())
    return _rolling_mean(base, 63)

def dd_529_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 01 drawdown depth over a 126d horizon to identify extreme regimes.
    """
    base = (close.pct_change(16).rolling(80).mean())
    return _rolling_mean(base, 126)

def dd_530_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 01 drawdown depth over a 252d horizon to identify extreme regimes.
    """
    base = (close.pct_change(16).rolling(80).mean())
    return _rolling_mean(base, 252)

def dd_531_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 01 drawdown depth by measuring deviations from the 5d mean.
    """
    base = (close.pct_change(16).rolling(80).mean())
    return _zscore_rolling(base, 5)

def dd_532_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 01 drawdown depth by measuring deviations from the 21d mean.
    """
    base = (close.pct_change(16).rolling(80).mean())
    return _zscore_rolling(base, 21)

def dd_533_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 01 drawdown depth by measuring deviations from the 63d mean.
    """
    base = (close.pct_change(16).rolling(80).mean())
    return _zscore_rolling(base, 63)

def dd_534_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 01 drawdown depth by measuring deviations from the 126d mean.
    """
    base = (close.pct_change(16).rolling(80).mean())
    return _zscore_rolling(base, 126)

def dd_535_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 01 drawdown depth by measuring deviations from the 252d mean.
    """
    base = (close.pct_change(16).rolling(80).mean())
    return _zscore_rolling(base, 252)

def dd_536_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 01 drawdown depth to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = (close.pct_change(16).rolling(80).mean())
    return _rank_pct(base, 5)

def dd_537_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 01 drawdown depth to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = (close.pct_change(16).rolling(80).mean())
    return _rank_pct(base, 21)

def dd_538_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 01 drawdown depth to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = (close.pct_change(16).rolling(80).mean())
    return _rank_pct(base, 63)

def dd_539_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 01 drawdown depth to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = (close.pct_change(16).rolling(80).mean())
    return _rank_pct(base, 126)

def dd_540_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 01 drawdown depth to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = (close.pct_change(16).rolling(80).mean())
    return _rank_pct(base, 252)

def dd_541_skew_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 01 drawdown depth distribution over 5d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(16).rolling(80).mean())
    return _rolling_skew(base, 5)

def dd_542_skew_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 01 drawdown depth distribution over 21d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(16).rolling(80).mean())
    return _rolling_skew(base, 21)

def dd_543_skew_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 01 drawdown depth distribution over 63d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(16).rolling(80).mean())
    return _rolling_skew(base, 63)

def dd_544_skew_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 01 drawdown depth distribution over 126d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(16).rolling(80).mean())
    return _rolling_skew(base, 126)

def dd_545_skew_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 01 drawdown depth distribution over 252d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(16).rolling(80).mean())
    return _rolling_skew(base, 252)

def dd_546_kurt_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 01 drawdown depth over 5d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(16).rolling(80).mean())
    return _rolling_kurt(base, 5)

def dd_547_kurt_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 01 drawdown depth over 21d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(16).rolling(80).mean())
    return _rolling_kurt(base, 21)

def dd_548_kurt_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 01 drawdown depth over 63d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(16).rolling(80).mean())
    return _rolling_kurt(base, 63)

def dd_549_kurt_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 01 drawdown depth over 126d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(16).rolling(80).mean())
    return _rolling_kurt(base, 126)

def dd_550_kurt_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 01 drawdown depth over 252d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(16).rolling(80).mean())
    return _rolling_kurt(base, 252)

def dd_551_voladj_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 01 drawdown depth for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(16).rolling(80).mean())
    return _safe_div(base, _rolling_std(base, 5))

def dd_552_voladj_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 01 drawdown depth for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(16).rolling(80).mean())
    return _safe_div(base, _rolling_std(base, 21))

def dd_553_voladj_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 01 drawdown depth for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(16).rolling(80).mean())
    return _safe_div(base, _rolling_std(base, 63))

def dd_554_voladj_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 01 drawdown depth for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(16).rolling(80).mean())
    return _safe_div(base, _rolling_std(base, 126))

def dd_555_voladj_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 01 drawdown depth for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(16).rolling(80).mean())
    return _safe_div(base, _rolling_std(base, 252))

def dd_556_lognorm_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 01 drawdown depth over 5d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(16).rolling(80).mean())
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def dd_557_lognorm_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 01 drawdown depth over 21d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(16).rolling(80).mean())
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def dd_558_lognorm_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 01 drawdown depth over 63d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(16).rolling(80).mean())
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def dd_559_lognorm_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 01 drawdown depth over 126d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(16).rolling(80).mean())
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def dd_560_lognorm_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 01 drawdown depth over 252d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(16).rolling(80).mean())
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def dd_561_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 01 drawdown depth over a 5d horizon to identify extreme regimes.
    """
    base = (close.pct_change(17).rolling(85).mean())
    return _rolling_mean(base, 5)

def dd_562_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 01 drawdown depth over a 21d horizon to identify extreme regimes.
    """
    base = (close.pct_change(17).rolling(85).mean())
    return _rolling_mean(base, 21)

def dd_563_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 01 drawdown depth over a 63d horizon to identify extreme regimes.
    """
    base = (close.pct_change(17).rolling(85).mean())
    return _rolling_mean(base, 63)

def dd_564_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 01 drawdown depth over a 126d horizon to identify extreme regimes.
    """
    base = (close.pct_change(17).rolling(85).mean())
    return _rolling_mean(base, 126)

def dd_565_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 01 drawdown depth over a 252d horizon to identify extreme regimes.
    """
    base = (close.pct_change(17).rolling(85).mean())
    return _rolling_mean(base, 252)

def dd_566_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 01 drawdown depth by measuring deviations from the 5d mean.
    """
    base = (close.pct_change(17).rolling(85).mean())
    return _zscore_rolling(base, 5)

def dd_567_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 01 drawdown depth by measuring deviations from the 21d mean.
    """
    base = (close.pct_change(17).rolling(85).mean())
    return _zscore_rolling(base, 21)

def dd_568_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 01 drawdown depth by measuring deviations from the 63d mean.
    """
    base = (close.pct_change(17).rolling(85).mean())
    return _zscore_rolling(base, 63)

def dd_569_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 01 drawdown depth by measuring deviations from the 126d mean.
    """
    base = (close.pct_change(17).rolling(85).mean())
    return _zscore_rolling(base, 126)

def dd_570_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 01 drawdown depth by measuring deviations from the 252d mean.
    """
    base = (close.pct_change(17).rolling(85).mean())
    return _zscore_rolling(base, 252)

def dd_571_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 01 drawdown depth to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = (close.pct_change(17).rolling(85).mean())
    return _rank_pct(base, 5)

def dd_572_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 01 drawdown depth to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = (close.pct_change(17).rolling(85).mean())
    return _rank_pct(base, 21)

def dd_573_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 01 drawdown depth to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = (close.pct_change(17).rolling(85).mean())
    return _rank_pct(base, 63)

def dd_574_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 01 drawdown depth to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = (close.pct_change(17).rolling(85).mean())
    return _rank_pct(base, 126)

def dd_575_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 01 drawdown depth to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = (close.pct_change(17).rolling(85).mean())
    return _rank_pct(base, 252)

def dd_576_skew_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 01 drawdown depth distribution over 5d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(17).rolling(85).mean())
    return _rolling_skew(base, 5)

def dd_577_skew_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 01 drawdown depth distribution over 21d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(17).rolling(85).mean())
    return _rolling_skew(base, 21)

def dd_578_skew_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 01 drawdown depth distribution over 63d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(17).rolling(85).mean())
    return _rolling_skew(base, 63)

def dd_579_skew_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 01 drawdown depth distribution over 126d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(17).rolling(85).mean())
    return _rolling_skew(base, 126)

def dd_580_skew_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 01 drawdown depth distribution over 252d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(17).rolling(85).mean())
    return _rolling_skew(base, 252)

def dd_581_kurt_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 01 drawdown depth over 5d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(17).rolling(85).mean())
    return _rolling_kurt(base, 5)

def dd_582_kurt_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 01 drawdown depth over 21d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(17).rolling(85).mean())
    return _rolling_kurt(base, 21)

def dd_583_kurt_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 01 drawdown depth over 63d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(17).rolling(85).mean())
    return _rolling_kurt(base, 63)

def dd_584_kurt_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 01 drawdown depth over 126d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(17).rolling(85).mean())
    return _rolling_kurt(base, 126)

def dd_585_kurt_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 01 drawdown depth over 252d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(17).rolling(85).mean())
    return _rolling_kurt(base, 252)

def dd_586_voladj_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 01 drawdown depth for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(17).rolling(85).mean())
    return _safe_div(base, _rolling_std(base, 5))

def dd_587_voladj_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 01 drawdown depth for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(17).rolling(85).mean())
    return _safe_div(base, _rolling_std(base, 21))

def dd_588_voladj_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 01 drawdown depth for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(17).rolling(85).mean())
    return _safe_div(base, _rolling_std(base, 63))

def dd_589_voladj_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 01 drawdown depth for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(17).rolling(85).mean())
    return _safe_div(base, _rolling_std(base, 126))

def dd_590_voladj_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 01 drawdown depth for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(17).rolling(85).mean())
    return _safe_div(base, _rolling_std(base, 252))

def dd_591_lognorm_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 01 drawdown depth over 5d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(17).rolling(85).mean())
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def dd_592_lognorm_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 01 drawdown depth over 21d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(17).rolling(85).mean())
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def dd_593_lognorm_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 01 drawdown depth over 63d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(17).rolling(85).mean())
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def dd_594_lognorm_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 01 drawdown depth over 126d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(17).rolling(85).mean())
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def dd_595_lognorm_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 01 drawdown depth over 252d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(17).rolling(85).mean())
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def dd_596_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 01 drawdown depth over a 5d horizon to identify extreme regimes.
    """
    base = (close.pct_change(18).rolling(90).mean())
    return _rolling_mean(base, 5)

def dd_597_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 01 drawdown depth over a 21d horizon to identify extreme regimes.
    """
    base = (close.pct_change(18).rolling(90).mean())
    return _rolling_mean(base, 21)

def dd_598_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 01 drawdown depth over a 63d horizon to identify extreme regimes.
    """
    base = (close.pct_change(18).rolling(90).mean())
    return _rolling_mean(base, 63)

def dd_599_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 01 drawdown depth over a 126d horizon to identify extreme regimes.
    """
    base = (close.pct_change(18).rolling(90).mean())
    return _rolling_mean(base, 126)

def dd_600_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 01 drawdown depth over a 252d horizon to identify extreme regimes.
    """
    base = (close.pct_change(18).rolling(90).mean())
    return _rolling_mean(base, 252)
