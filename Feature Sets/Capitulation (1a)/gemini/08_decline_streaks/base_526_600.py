"""
08_08_decline_streaks — Base Features 526-600
Domain: 08_decline_streaks
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

def dstk_526_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 08 decline streaks over a 5d horizon to identify extreme regimes.
    """
    base = (close.pct_change(16).rolling(80).mean())
    return _rolling_mean(base, 5)

def dstk_527_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 08 decline streaks over a 21d horizon to identify extreme regimes.
    """
    base = (close.pct_change(16).rolling(80).mean())
    return _rolling_mean(base, 21)

def dstk_528_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 08 decline streaks over a 63d horizon to identify extreme regimes.
    """
    base = (close.pct_change(16).rolling(80).mean())
    return _rolling_mean(base, 63)

def dstk_529_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 08 decline streaks over a 126d horizon to identify extreme regimes.
    """
    base = (close.pct_change(16).rolling(80).mean())
    return _rolling_mean(base, 126)

def dstk_530_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 08 decline streaks over a 252d horizon to identify extreme regimes.
    """
    base = (close.pct_change(16).rolling(80).mean())
    return _rolling_mean(base, 252)

def dstk_531_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 08 decline streaks by measuring deviations from the 5d mean.
    """
    base = (close.pct_change(16).rolling(80).mean())
    return _zscore_rolling(base, 5)

def dstk_532_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 08 decline streaks by measuring deviations from the 21d mean.
    """
    base = (close.pct_change(16).rolling(80).mean())
    return _zscore_rolling(base, 21)

def dstk_533_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 08 decline streaks by measuring deviations from the 63d mean.
    """
    base = (close.pct_change(16).rolling(80).mean())
    return _zscore_rolling(base, 63)

def dstk_534_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 08 decline streaks by measuring deviations from the 126d mean.
    """
    base = (close.pct_change(16).rolling(80).mean())
    return _zscore_rolling(base, 126)

def dstk_535_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 08 decline streaks by measuring deviations from the 252d mean.
    """
    base = (close.pct_change(16).rolling(80).mean())
    return _zscore_rolling(base, 252)

def dstk_536_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 08 decline streaks to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = (close.pct_change(16).rolling(80).mean())
    return _rank_pct(base, 5)

def dstk_537_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 08 decline streaks to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = (close.pct_change(16).rolling(80).mean())
    return _rank_pct(base, 21)

def dstk_538_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 08 decline streaks to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = (close.pct_change(16).rolling(80).mean())
    return _rank_pct(base, 63)

def dstk_539_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 08 decline streaks to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = (close.pct_change(16).rolling(80).mean())
    return _rank_pct(base, 126)

def dstk_540_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 08 decline streaks to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = (close.pct_change(16).rolling(80).mean())
    return _rank_pct(base, 252)

def dstk_541_skew_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 08 decline streaks distribution over 5d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(16).rolling(80).mean())
    return _rolling_skew(base, 5)

def dstk_542_skew_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 08 decline streaks distribution over 21d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(16).rolling(80).mean())
    return _rolling_skew(base, 21)

def dstk_543_skew_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 08 decline streaks distribution over 63d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(16).rolling(80).mean())
    return _rolling_skew(base, 63)

def dstk_544_skew_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 08 decline streaks distribution over 126d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(16).rolling(80).mean())
    return _rolling_skew(base, 126)

def dstk_545_skew_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 08 decline streaks distribution over 252d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(16).rolling(80).mean())
    return _rolling_skew(base, 252)

def dstk_546_kurt_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 08 decline streaks over 5d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(16).rolling(80).mean())
    return _rolling_kurt(base, 5)

def dstk_547_kurt_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 08 decline streaks over 21d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(16).rolling(80).mean())
    return _rolling_kurt(base, 21)

def dstk_548_kurt_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 08 decline streaks over 63d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(16).rolling(80).mean())
    return _rolling_kurt(base, 63)

def dstk_549_kurt_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 08 decline streaks over 126d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(16).rolling(80).mean())
    return _rolling_kurt(base, 126)

def dstk_550_kurt_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 08 decline streaks over 252d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(16).rolling(80).mean())
    return _rolling_kurt(base, 252)

def dstk_551_voladj_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 08 decline streaks for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(16).rolling(80).mean())
    return _safe_div(base, _rolling_std(base, 5))

def dstk_552_voladj_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 08 decline streaks for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(16).rolling(80).mean())
    return _safe_div(base, _rolling_std(base, 21))

def dstk_553_voladj_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 08 decline streaks for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(16).rolling(80).mean())
    return _safe_div(base, _rolling_std(base, 63))

def dstk_554_voladj_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 08 decline streaks for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(16).rolling(80).mean())
    return _safe_div(base, _rolling_std(base, 126))

def dstk_555_voladj_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 08 decline streaks for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(16).rolling(80).mean())
    return _safe_div(base, _rolling_std(base, 252))

def dstk_556_lognorm_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 08 decline streaks over 5d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(16).rolling(80).mean())
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def dstk_557_lognorm_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 08 decline streaks over 21d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(16).rolling(80).mean())
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def dstk_558_lognorm_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 08 decline streaks over 63d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(16).rolling(80).mean())
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def dstk_559_lognorm_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 08 decline streaks over 126d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(16).rolling(80).mean())
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def dstk_560_lognorm_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 08 decline streaks over 252d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(16).rolling(80).mean())
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def dstk_561_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 08 decline streaks over a 5d horizon to identify extreme regimes.
    """
    base = (close.pct_change(17).rolling(85).mean())
    return _rolling_mean(base, 5)

def dstk_562_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 08 decline streaks over a 21d horizon to identify extreme regimes.
    """
    base = (close.pct_change(17).rolling(85).mean())
    return _rolling_mean(base, 21)

def dstk_563_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 08 decline streaks over a 63d horizon to identify extreme regimes.
    """
    base = (close.pct_change(17).rolling(85).mean())
    return _rolling_mean(base, 63)

def dstk_564_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 08 decline streaks over a 126d horizon to identify extreme regimes.
    """
    base = (close.pct_change(17).rolling(85).mean())
    return _rolling_mean(base, 126)

def dstk_565_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 08 decline streaks over a 252d horizon to identify extreme regimes.
    """
    base = (close.pct_change(17).rolling(85).mean())
    return _rolling_mean(base, 252)

def dstk_566_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 08 decline streaks by measuring deviations from the 5d mean.
    """
    base = (close.pct_change(17).rolling(85).mean())
    return _zscore_rolling(base, 5)

def dstk_567_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 08 decline streaks by measuring deviations from the 21d mean.
    """
    base = (close.pct_change(17).rolling(85).mean())
    return _zscore_rolling(base, 21)

def dstk_568_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 08 decline streaks by measuring deviations from the 63d mean.
    """
    base = (close.pct_change(17).rolling(85).mean())
    return _zscore_rolling(base, 63)

def dstk_569_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 08 decline streaks by measuring deviations from the 126d mean.
    """
    base = (close.pct_change(17).rolling(85).mean())
    return _zscore_rolling(base, 126)

def dstk_570_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 08 decline streaks by measuring deviations from the 252d mean.
    """
    base = (close.pct_change(17).rolling(85).mean())
    return _zscore_rolling(base, 252)

def dstk_571_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 08 decline streaks to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = (close.pct_change(17).rolling(85).mean())
    return _rank_pct(base, 5)

def dstk_572_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 08 decline streaks to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = (close.pct_change(17).rolling(85).mean())
    return _rank_pct(base, 21)

def dstk_573_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 08 decline streaks to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = (close.pct_change(17).rolling(85).mean())
    return _rank_pct(base, 63)

def dstk_574_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 08 decline streaks to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = (close.pct_change(17).rolling(85).mean())
    return _rank_pct(base, 126)

def dstk_575_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 08 decline streaks to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = (close.pct_change(17).rolling(85).mean())
    return _rank_pct(base, 252)

def dstk_576_skew_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 08 decline streaks distribution over 5d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(17).rolling(85).mean())
    return _rolling_skew(base, 5)

def dstk_577_skew_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 08 decline streaks distribution over 21d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(17).rolling(85).mean())
    return _rolling_skew(base, 21)

def dstk_578_skew_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 08 decline streaks distribution over 63d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(17).rolling(85).mean())
    return _rolling_skew(base, 63)

def dstk_579_skew_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 08 decline streaks distribution over 126d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(17).rolling(85).mean())
    return _rolling_skew(base, 126)

def dstk_580_skew_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 08 decline streaks distribution over 252d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(17).rolling(85).mean())
    return _rolling_skew(base, 252)

def dstk_581_kurt_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 08 decline streaks over 5d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(17).rolling(85).mean())
    return _rolling_kurt(base, 5)

def dstk_582_kurt_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 08 decline streaks over 21d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(17).rolling(85).mean())
    return _rolling_kurt(base, 21)

def dstk_583_kurt_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 08 decline streaks over 63d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(17).rolling(85).mean())
    return _rolling_kurt(base, 63)

def dstk_584_kurt_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 08 decline streaks over 126d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(17).rolling(85).mean())
    return _rolling_kurt(base, 126)

def dstk_585_kurt_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 08 decline streaks over 252d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(17).rolling(85).mean())
    return _rolling_kurt(base, 252)

def dstk_586_voladj_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 08 decline streaks for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(17).rolling(85).mean())
    return _safe_div(base, _rolling_std(base, 5))

def dstk_587_voladj_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 08 decline streaks for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(17).rolling(85).mean())
    return _safe_div(base, _rolling_std(base, 21))

def dstk_588_voladj_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 08 decline streaks for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(17).rolling(85).mean())
    return _safe_div(base, _rolling_std(base, 63))

def dstk_589_voladj_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 08 decline streaks for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(17).rolling(85).mean())
    return _safe_div(base, _rolling_std(base, 126))

def dstk_590_voladj_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 08 decline streaks for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(17).rolling(85).mean())
    return _safe_div(base, _rolling_std(base, 252))

def dstk_591_lognorm_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 08 decline streaks over 5d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(17).rolling(85).mean())
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def dstk_592_lognorm_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 08 decline streaks over 21d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(17).rolling(85).mean())
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def dstk_593_lognorm_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 08 decline streaks over 63d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(17).rolling(85).mean())
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def dstk_594_lognorm_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 08 decline streaks over 126d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(17).rolling(85).mean())
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def dstk_595_lognorm_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 08 decline streaks over 252d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(17).rolling(85).mean())
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def dstk_596_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 08 decline streaks over a 5d horizon to identify extreme regimes.
    """
    base = (close.pct_change(18).rolling(90).mean())
    return _rolling_mean(base, 5)

def dstk_597_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 08 decline streaks over a 21d horizon to identify extreme regimes.
    """
    base = (close.pct_change(18).rolling(90).mean())
    return _rolling_mean(base, 21)

def dstk_598_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 08 decline streaks over a 63d horizon to identify extreme regimes.
    """
    base = (close.pct_change(18).rolling(90).mean())
    return _rolling_mean(base, 63)

def dstk_599_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 08 decline streaks over a 126d horizon to identify extreme regimes.
    """
    base = (close.pct_change(18).rolling(90).mean())
    return _rolling_mean(base, 126)

def dstk_600_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 08 decline streaks over a 252d horizon to identify extreme regimes.
    """
    base = (close.pct_change(18).rolling(90).mean())
    return _rolling_mean(base, 252)
