"""
23_23_dollar_volume_shock — Base Features 526-600
Domain: 23_dollar_volume_shock
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

def dvsh_526_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 23 dollar volume shock over a 5d horizon to identify extreme regimes.
    """
    base = (volume.pct_change(16).rolling(80).mean())
    return _rolling_mean(base, 5)

def dvsh_527_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 23 dollar volume shock over a 21d horizon to identify extreme regimes.
    """
    base = (volume.pct_change(16).rolling(80).mean())
    return _rolling_mean(base, 21)

def dvsh_528_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 23 dollar volume shock over a 63d horizon to identify extreme regimes.
    """
    base = (volume.pct_change(16).rolling(80).mean())
    return _rolling_mean(base, 63)

def dvsh_529_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 23 dollar volume shock over a 126d horizon to identify extreme regimes.
    """
    base = (volume.pct_change(16).rolling(80).mean())
    return _rolling_mean(base, 126)

def dvsh_530_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 23 dollar volume shock over a 252d horizon to identify extreme regimes.
    """
    base = (volume.pct_change(16).rolling(80).mean())
    return _rolling_mean(base, 252)

def dvsh_531_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 23 dollar volume shock by measuring deviations from the 5d mean.
    """
    base = (volume.pct_change(16).rolling(80).mean())
    return _zscore_rolling(base, 5)

def dvsh_532_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 23 dollar volume shock by measuring deviations from the 21d mean.
    """
    base = (volume.pct_change(16).rolling(80).mean())
    return _zscore_rolling(base, 21)

def dvsh_533_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 23 dollar volume shock by measuring deviations from the 63d mean.
    """
    base = (volume.pct_change(16).rolling(80).mean())
    return _zscore_rolling(base, 63)

def dvsh_534_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 23 dollar volume shock by measuring deviations from the 126d mean.
    """
    base = (volume.pct_change(16).rolling(80).mean())
    return _zscore_rolling(base, 126)

def dvsh_535_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 23 dollar volume shock by measuring deviations from the 252d mean.
    """
    base = (volume.pct_change(16).rolling(80).mean())
    return _zscore_rolling(base, 252)

def dvsh_536_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 23 dollar volume shock to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = (volume.pct_change(16).rolling(80).mean())
    return _rank_pct(base, 5)

def dvsh_537_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 23 dollar volume shock to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = (volume.pct_change(16).rolling(80).mean())
    return _rank_pct(base, 21)

def dvsh_538_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 23 dollar volume shock to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = (volume.pct_change(16).rolling(80).mean())
    return _rank_pct(base, 63)

def dvsh_539_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 23 dollar volume shock to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = (volume.pct_change(16).rolling(80).mean())
    return _rank_pct(base, 126)

def dvsh_540_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 23 dollar volume shock to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = (volume.pct_change(16).rolling(80).mean())
    return _rank_pct(base, 252)

def dvsh_541_skew_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 23 dollar volume shock distribution over 5d to detect tail risk or exhaustion.
    """
    base = (volume.pct_change(16).rolling(80).mean())
    return _rolling_skew(base, 5)

def dvsh_542_skew_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 23 dollar volume shock distribution over 21d to detect tail risk or exhaustion.
    """
    base = (volume.pct_change(16).rolling(80).mean())
    return _rolling_skew(base, 21)

def dvsh_543_skew_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 23 dollar volume shock distribution over 63d to detect tail risk or exhaustion.
    """
    base = (volume.pct_change(16).rolling(80).mean())
    return _rolling_skew(base, 63)

def dvsh_544_skew_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 23 dollar volume shock distribution over 126d to detect tail risk or exhaustion.
    """
    base = (volume.pct_change(16).rolling(80).mean())
    return _rolling_skew(base, 126)

def dvsh_545_skew_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 23 dollar volume shock distribution over 252d to detect tail risk or exhaustion.
    """
    base = (volume.pct_change(16).rolling(80).mean())
    return _rolling_skew(base, 252)

def dvsh_546_kurt_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 23 dollar volume shock over 5d to capture explosive breakdown or reversal points.
    """
    base = (volume.pct_change(16).rolling(80).mean())
    return _rolling_kurt(base, 5)

def dvsh_547_kurt_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 23 dollar volume shock over 21d to capture explosive breakdown or reversal points.
    """
    base = (volume.pct_change(16).rolling(80).mean())
    return _rolling_kurt(base, 21)

def dvsh_548_kurt_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 23 dollar volume shock over 63d to capture explosive breakdown or reversal points.
    """
    base = (volume.pct_change(16).rolling(80).mean())
    return _rolling_kurt(base, 63)

def dvsh_549_kurt_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 23 dollar volume shock over 126d to capture explosive breakdown or reversal points.
    """
    base = (volume.pct_change(16).rolling(80).mean())
    return _rolling_kurt(base, 126)

def dvsh_550_kurt_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 23 dollar volume shock over 252d to capture explosive breakdown or reversal points.
    """
    base = (volume.pct_change(16).rolling(80).mean())
    return _rolling_kurt(base, 252)

def dvsh_551_voladj_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 23 dollar volume shock for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = (volume.pct_change(16).rolling(80).mean())
    return _safe_div(base, _rolling_std(base, 5))

def dvsh_552_voladj_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 23 dollar volume shock for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = (volume.pct_change(16).rolling(80).mean())
    return _safe_div(base, _rolling_std(base, 21))

def dvsh_553_voladj_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 23 dollar volume shock for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = (volume.pct_change(16).rolling(80).mean())
    return _safe_div(base, _rolling_std(base, 63))

def dvsh_554_voladj_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 23 dollar volume shock for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = (volume.pct_change(16).rolling(80).mean())
    return _safe_div(base, _rolling_std(base, 126))

def dvsh_555_voladj_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 23 dollar volume shock for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = (volume.pct_change(16).rolling(80).mean())
    return _safe_div(base, _rolling_std(base, 252))

def dvsh_556_lognorm_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 23 dollar volume shock over 5d to stabilize variance and capture exponential shifts.
    """
    base = (volume.pct_change(16).rolling(80).mean())
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def dvsh_557_lognorm_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 23 dollar volume shock over 21d to stabilize variance and capture exponential shifts.
    """
    base = (volume.pct_change(16).rolling(80).mean())
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def dvsh_558_lognorm_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 23 dollar volume shock over 63d to stabilize variance and capture exponential shifts.
    """
    base = (volume.pct_change(16).rolling(80).mean())
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def dvsh_559_lognorm_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 23 dollar volume shock over 126d to stabilize variance and capture exponential shifts.
    """
    base = (volume.pct_change(16).rolling(80).mean())
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def dvsh_560_lognorm_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 23 dollar volume shock over 252d to stabilize variance and capture exponential shifts.
    """
    base = (volume.pct_change(16).rolling(80).mean())
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def dvsh_561_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 23 dollar volume shock over a 5d horizon to identify extreme regimes.
    """
    base = (volume.pct_change(17).rolling(85).mean())
    return _rolling_mean(base, 5)

def dvsh_562_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 23 dollar volume shock over a 21d horizon to identify extreme regimes.
    """
    base = (volume.pct_change(17).rolling(85).mean())
    return _rolling_mean(base, 21)

def dvsh_563_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 23 dollar volume shock over a 63d horizon to identify extreme regimes.
    """
    base = (volume.pct_change(17).rolling(85).mean())
    return _rolling_mean(base, 63)

def dvsh_564_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 23 dollar volume shock over a 126d horizon to identify extreme regimes.
    """
    base = (volume.pct_change(17).rolling(85).mean())
    return _rolling_mean(base, 126)

def dvsh_565_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 23 dollar volume shock over a 252d horizon to identify extreme regimes.
    """
    base = (volume.pct_change(17).rolling(85).mean())
    return _rolling_mean(base, 252)

def dvsh_566_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 23 dollar volume shock by measuring deviations from the 5d mean.
    """
    base = (volume.pct_change(17).rolling(85).mean())
    return _zscore_rolling(base, 5)

def dvsh_567_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 23 dollar volume shock by measuring deviations from the 21d mean.
    """
    base = (volume.pct_change(17).rolling(85).mean())
    return _zscore_rolling(base, 21)

def dvsh_568_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 23 dollar volume shock by measuring deviations from the 63d mean.
    """
    base = (volume.pct_change(17).rolling(85).mean())
    return _zscore_rolling(base, 63)

def dvsh_569_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 23 dollar volume shock by measuring deviations from the 126d mean.
    """
    base = (volume.pct_change(17).rolling(85).mean())
    return _zscore_rolling(base, 126)

def dvsh_570_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 23 dollar volume shock by measuring deviations from the 252d mean.
    """
    base = (volume.pct_change(17).rolling(85).mean())
    return _zscore_rolling(base, 252)

def dvsh_571_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 23 dollar volume shock to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = (volume.pct_change(17).rolling(85).mean())
    return _rank_pct(base, 5)

def dvsh_572_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 23 dollar volume shock to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = (volume.pct_change(17).rolling(85).mean())
    return _rank_pct(base, 21)

def dvsh_573_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 23 dollar volume shock to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = (volume.pct_change(17).rolling(85).mean())
    return _rank_pct(base, 63)

def dvsh_574_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 23 dollar volume shock to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = (volume.pct_change(17).rolling(85).mean())
    return _rank_pct(base, 126)

def dvsh_575_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 23 dollar volume shock to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = (volume.pct_change(17).rolling(85).mean())
    return _rank_pct(base, 252)

def dvsh_576_skew_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 23 dollar volume shock distribution over 5d to detect tail risk or exhaustion.
    """
    base = (volume.pct_change(17).rolling(85).mean())
    return _rolling_skew(base, 5)

def dvsh_577_skew_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 23 dollar volume shock distribution over 21d to detect tail risk or exhaustion.
    """
    base = (volume.pct_change(17).rolling(85).mean())
    return _rolling_skew(base, 21)

def dvsh_578_skew_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 23 dollar volume shock distribution over 63d to detect tail risk or exhaustion.
    """
    base = (volume.pct_change(17).rolling(85).mean())
    return _rolling_skew(base, 63)

def dvsh_579_skew_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 23 dollar volume shock distribution over 126d to detect tail risk or exhaustion.
    """
    base = (volume.pct_change(17).rolling(85).mean())
    return _rolling_skew(base, 126)

def dvsh_580_skew_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 23 dollar volume shock distribution over 252d to detect tail risk or exhaustion.
    """
    base = (volume.pct_change(17).rolling(85).mean())
    return _rolling_skew(base, 252)

def dvsh_581_kurt_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 23 dollar volume shock over 5d to capture explosive breakdown or reversal points.
    """
    base = (volume.pct_change(17).rolling(85).mean())
    return _rolling_kurt(base, 5)

def dvsh_582_kurt_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 23 dollar volume shock over 21d to capture explosive breakdown or reversal points.
    """
    base = (volume.pct_change(17).rolling(85).mean())
    return _rolling_kurt(base, 21)

def dvsh_583_kurt_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 23 dollar volume shock over 63d to capture explosive breakdown or reversal points.
    """
    base = (volume.pct_change(17).rolling(85).mean())
    return _rolling_kurt(base, 63)

def dvsh_584_kurt_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 23 dollar volume shock over 126d to capture explosive breakdown or reversal points.
    """
    base = (volume.pct_change(17).rolling(85).mean())
    return _rolling_kurt(base, 126)

def dvsh_585_kurt_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 23 dollar volume shock over 252d to capture explosive breakdown or reversal points.
    """
    base = (volume.pct_change(17).rolling(85).mean())
    return _rolling_kurt(base, 252)

def dvsh_586_voladj_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 23 dollar volume shock for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = (volume.pct_change(17).rolling(85).mean())
    return _safe_div(base, _rolling_std(base, 5))

def dvsh_587_voladj_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 23 dollar volume shock for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = (volume.pct_change(17).rolling(85).mean())
    return _safe_div(base, _rolling_std(base, 21))

def dvsh_588_voladj_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 23 dollar volume shock for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = (volume.pct_change(17).rolling(85).mean())
    return _safe_div(base, _rolling_std(base, 63))

def dvsh_589_voladj_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 23 dollar volume shock for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = (volume.pct_change(17).rolling(85).mean())
    return _safe_div(base, _rolling_std(base, 126))

def dvsh_590_voladj_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 23 dollar volume shock for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = (volume.pct_change(17).rolling(85).mean())
    return _safe_div(base, _rolling_std(base, 252))

def dvsh_591_lognorm_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 23 dollar volume shock over 5d to stabilize variance and capture exponential shifts.
    """
    base = (volume.pct_change(17).rolling(85).mean())
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def dvsh_592_lognorm_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 23 dollar volume shock over 21d to stabilize variance and capture exponential shifts.
    """
    base = (volume.pct_change(17).rolling(85).mean())
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def dvsh_593_lognorm_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 23 dollar volume shock over 63d to stabilize variance and capture exponential shifts.
    """
    base = (volume.pct_change(17).rolling(85).mean())
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def dvsh_594_lognorm_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 23 dollar volume shock over 126d to stabilize variance and capture exponential shifts.
    """
    base = (volume.pct_change(17).rolling(85).mean())
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def dvsh_595_lognorm_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 23 dollar volume shock over 252d to stabilize variance and capture exponential shifts.
    """
    base = (volume.pct_change(17).rolling(85).mean())
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def dvsh_596_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 23 dollar volume shock over a 5d horizon to identify extreme regimes.
    """
    base = (volume.pct_change(18).rolling(90).mean())
    return _rolling_mean(base, 5)

def dvsh_597_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 23 dollar volume shock over a 21d horizon to identify extreme regimes.
    """
    base = (volume.pct_change(18).rolling(90).mean())
    return _rolling_mean(base, 21)

def dvsh_598_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 23 dollar volume shock over a 63d horizon to identify extreme regimes.
    """
    base = (volume.pct_change(18).rolling(90).mean())
    return _rolling_mean(base, 63)

def dvsh_599_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 23 dollar volume shock over a 126d horizon to identify extreme regimes.
    """
    base = (volume.pct_change(18).rolling(90).mean())
    return _rolling_mean(base, 126)

def dvsh_600_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 23 dollar volume shock over a 252d horizon to identify extreme regimes.
    """
    base = (volume.pct_change(18).rolling(90).mean())
    return _rolling_mean(base, 252)
