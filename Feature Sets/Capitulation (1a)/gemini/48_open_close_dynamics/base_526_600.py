"""
48_48_open_close_dynamics — Base Features 526-600
Domain: 48_open_close_dynamics
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

def ocdy_526_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 48 open close dynamics over a 5d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(80).mean())
    return _rolling_mean(base, 5)

def ocdy_527_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 48 open close dynamics over a 21d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(80).mean())
    return _rolling_mean(base, 21)

def ocdy_528_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 48 open close dynamics over a 63d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(80).mean())
    return _rolling_mean(base, 63)

def ocdy_529_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 48 open close dynamics over a 126d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(80).mean())
    return _rolling_mean(base, 126)

def ocdy_530_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 48 open close dynamics over a 252d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(80).mean())
    return _rolling_mean(base, 252)

def ocdy_531_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 48 open close dynamics by measuring deviations from the 5d mean.
    """
    base = ((close - open).abs().rolling(80).mean())
    return _zscore_rolling(base, 5)

def ocdy_532_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 48 open close dynamics by measuring deviations from the 21d mean.
    """
    base = ((close - open).abs().rolling(80).mean())
    return _zscore_rolling(base, 21)

def ocdy_533_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 48 open close dynamics by measuring deviations from the 63d mean.
    """
    base = ((close - open).abs().rolling(80).mean())
    return _zscore_rolling(base, 63)

def ocdy_534_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 48 open close dynamics by measuring deviations from the 126d mean.
    """
    base = ((close - open).abs().rolling(80).mean())
    return _zscore_rolling(base, 126)

def ocdy_535_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 48 open close dynamics by measuring deviations from the 252d mean.
    """
    base = ((close - open).abs().rolling(80).mean())
    return _zscore_rolling(base, 252)

def ocdy_536_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 48 open close dynamics to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = ((close - open).abs().rolling(80).mean())
    return _rank_pct(base, 5)

def ocdy_537_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 48 open close dynamics to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = ((close - open).abs().rolling(80).mean())
    return _rank_pct(base, 21)

def ocdy_538_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 48 open close dynamics to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = ((close - open).abs().rolling(80).mean())
    return _rank_pct(base, 63)

def ocdy_539_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 48 open close dynamics to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = ((close - open).abs().rolling(80).mean())
    return _rank_pct(base, 126)

def ocdy_540_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 48 open close dynamics to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = ((close - open).abs().rolling(80).mean())
    return _rank_pct(base, 252)

def ocdy_541_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 48 open close dynamics distribution over 5d to detect tail risk or exhaustion.
    """
    base = ((close - open).abs().rolling(80).mean())
    return _rolling_skew(base, 5)

def ocdy_542_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 48 open close dynamics distribution over 21d to detect tail risk or exhaustion.
    """
    base = ((close - open).abs().rolling(80).mean())
    return _rolling_skew(base, 21)

def ocdy_543_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 48 open close dynamics distribution over 63d to detect tail risk or exhaustion.
    """
    base = ((close - open).abs().rolling(80).mean())
    return _rolling_skew(base, 63)

def ocdy_544_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 48 open close dynamics distribution over 126d to detect tail risk or exhaustion.
    """
    base = ((close - open).abs().rolling(80).mean())
    return _rolling_skew(base, 126)

def ocdy_545_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 48 open close dynamics distribution over 252d to detect tail risk or exhaustion.
    """
    base = ((close - open).abs().rolling(80).mean())
    return _rolling_skew(base, 252)

def ocdy_546_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 48 open close dynamics over 5d to capture explosive breakdown or reversal points.
    """
    base = ((close - open).abs().rolling(80).mean())
    return _rolling_kurt(base, 5)

def ocdy_547_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 48 open close dynamics over 21d to capture explosive breakdown or reversal points.
    """
    base = ((close - open).abs().rolling(80).mean())
    return _rolling_kurt(base, 21)

def ocdy_548_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 48 open close dynamics over 63d to capture explosive breakdown or reversal points.
    """
    base = ((close - open).abs().rolling(80).mean())
    return _rolling_kurt(base, 63)

def ocdy_549_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 48 open close dynamics over 126d to capture explosive breakdown or reversal points.
    """
    base = ((close - open).abs().rolling(80).mean())
    return _rolling_kurt(base, 126)

def ocdy_550_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 48 open close dynamics over 252d to capture explosive breakdown or reversal points.
    """
    base = ((close - open).abs().rolling(80).mean())
    return _rolling_kurt(base, 252)

def ocdy_551_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 48 open close dynamics for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = ((close - open).abs().rolling(80).mean())
    return _safe_div(base, _rolling_std(base, 5))

def ocdy_552_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 48 open close dynamics for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = ((close - open).abs().rolling(80).mean())
    return _safe_div(base, _rolling_std(base, 21))

def ocdy_553_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 48 open close dynamics for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = ((close - open).abs().rolling(80).mean())
    return _safe_div(base, _rolling_std(base, 63))

def ocdy_554_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 48 open close dynamics for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = ((close - open).abs().rolling(80).mean())
    return _safe_div(base, _rolling_std(base, 126))

def ocdy_555_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 48 open close dynamics for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = ((close - open).abs().rolling(80).mean())
    return _safe_div(base, _rolling_std(base, 252))

def ocdy_556_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 48 open close dynamics over 5d to stabilize variance and capture exponential shifts.
    """
    base = ((close - open).abs().rolling(80).mean())
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def ocdy_557_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 48 open close dynamics over 21d to stabilize variance and capture exponential shifts.
    """
    base = ((close - open).abs().rolling(80).mean())
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def ocdy_558_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 48 open close dynamics over 63d to stabilize variance and capture exponential shifts.
    """
    base = ((close - open).abs().rolling(80).mean())
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def ocdy_559_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 48 open close dynamics over 126d to stabilize variance and capture exponential shifts.
    """
    base = ((close - open).abs().rolling(80).mean())
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def ocdy_560_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 48 open close dynamics over 252d to stabilize variance and capture exponential shifts.
    """
    base = ((close - open).abs().rolling(80).mean())
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def ocdy_561_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 48 open close dynamics over a 5d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(85).mean())
    return _rolling_mean(base, 5)

def ocdy_562_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 48 open close dynamics over a 21d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(85).mean())
    return _rolling_mean(base, 21)

def ocdy_563_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 48 open close dynamics over a 63d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(85).mean())
    return _rolling_mean(base, 63)

def ocdy_564_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 48 open close dynamics over a 126d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(85).mean())
    return _rolling_mean(base, 126)

def ocdy_565_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 48 open close dynamics over a 252d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(85).mean())
    return _rolling_mean(base, 252)

def ocdy_566_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 48 open close dynamics by measuring deviations from the 5d mean.
    """
    base = ((close - open).abs().rolling(85).mean())
    return _zscore_rolling(base, 5)

def ocdy_567_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 48 open close dynamics by measuring deviations from the 21d mean.
    """
    base = ((close - open).abs().rolling(85).mean())
    return _zscore_rolling(base, 21)

def ocdy_568_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 48 open close dynamics by measuring deviations from the 63d mean.
    """
    base = ((close - open).abs().rolling(85).mean())
    return _zscore_rolling(base, 63)

def ocdy_569_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 48 open close dynamics by measuring deviations from the 126d mean.
    """
    base = ((close - open).abs().rolling(85).mean())
    return _zscore_rolling(base, 126)

def ocdy_570_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 48 open close dynamics by measuring deviations from the 252d mean.
    """
    base = ((close - open).abs().rolling(85).mean())
    return _zscore_rolling(base, 252)

def ocdy_571_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 48 open close dynamics to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = ((close - open).abs().rolling(85).mean())
    return _rank_pct(base, 5)

def ocdy_572_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 48 open close dynamics to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = ((close - open).abs().rolling(85).mean())
    return _rank_pct(base, 21)

def ocdy_573_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 48 open close dynamics to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = ((close - open).abs().rolling(85).mean())
    return _rank_pct(base, 63)

def ocdy_574_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 48 open close dynamics to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = ((close - open).abs().rolling(85).mean())
    return _rank_pct(base, 126)

def ocdy_575_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 48 open close dynamics to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = ((close - open).abs().rolling(85).mean())
    return _rank_pct(base, 252)

def ocdy_576_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 48 open close dynamics distribution over 5d to detect tail risk or exhaustion.
    """
    base = ((close - open).abs().rolling(85).mean())
    return _rolling_skew(base, 5)

def ocdy_577_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 48 open close dynamics distribution over 21d to detect tail risk or exhaustion.
    """
    base = ((close - open).abs().rolling(85).mean())
    return _rolling_skew(base, 21)

def ocdy_578_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 48 open close dynamics distribution over 63d to detect tail risk or exhaustion.
    """
    base = ((close - open).abs().rolling(85).mean())
    return _rolling_skew(base, 63)

def ocdy_579_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 48 open close dynamics distribution over 126d to detect tail risk or exhaustion.
    """
    base = ((close - open).abs().rolling(85).mean())
    return _rolling_skew(base, 126)

def ocdy_580_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 48 open close dynamics distribution over 252d to detect tail risk or exhaustion.
    """
    base = ((close - open).abs().rolling(85).mean())
    return _rolling_skew(base, 252)

def ocdy_581_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 48 open close dynamics over 5d to capture explosive breakdown or reversal points.
    """
    base = ((close - open).abs().rolling(85).mean())
    return _rolling_kurt(base, 5)

def ocdy_582_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 48 open close dynamics over 21d to capture explosive breakdown or reversal points.
    """
    base = ((close - open).abs().rolling(85).mean())
    return _rolling_kurt(base, 21)

def ocdy_583_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 48 open close dynamics over 63d to capture explosive breakdown or reversal points.
    """
    base = ((close - open).abs().rolling(85).mean())
    return _rolling_kurt(base, 63)

def ocdy_584_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 48 open close dynamics over 126d to capture explosive breakdown or reversal points.
    """
    base = ((close - open).abs().rolling(85).mean())
    return _rolling_kurt(base, 126)

def ocdy_585_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 48 open close dynamics over 252d to capture explosive breakdown or reversal points.
    """
    base = ((close - open).abs().rolling(85).mean())
    return _rolling_kurt(base, 252)

def ocdy_586_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 48 open close dynamics for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = ((close - open).abs().rolling(85).mean())
    return _safe_div(base, _rolling_std(base, 5))

def ocdy_587_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 48 open close dynamics for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = ((close - open).abs().rolling(85).mean())
    return _safe_div(base, _rolling_std(base, 21))

def ocdy_588_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 48 open close dynamics for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = ((close - open).abs().rolling(85).mean())
    return _safe_div(base, _rolling_std(base, 63))

def ocdy_589_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 48 open close dynamics for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = ((close - open).abs().rolling(85).mean())
    return _safe_div(base, _rolling_std(base, 126))

def ocdy_590_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 48 open close dynamics for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = ((close - open).abs().rolling(85).mean())
    return _safe_div(base, _rolling_std(base, 252))

def ocdy_591_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 48 open close dynamics over 5d to stabilize variance and capture exponential shifts.
    """
    base = ((close - open).abs().rolling(85).mean())
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def ocdy_592_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 48 open close dynamics over 21d to stabilize variance and capture exponential shifts.
    """
    base = ((close - open).abs().rolling(85).mean())
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def ocdy_593_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 48 open close dynamics over 63d to stabilize variance and capture exponential shifts.
    """
    base = ((close - open).abs().rolling(85).mean())
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def ocdy_594_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 48 open close dynamics over 126d to stabilize variance and capture exponential shifts.
    """
    base = ((close - open).abs().rolling(85).mean())
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def ocdy_595_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 48 open close dynamics over 252d to stabilize variance and capture exponential shifts.
    """
    base = ((close - open).abs().rolling(85).mean())
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def ocdy_596_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 48 open close dynamics over a 5d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(90).mean())
    return _rolling_mean(base, 5)

def ocdy_597_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 48 open close dynamics over a 21d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(90).mean())
    return _rolling_mean(base, 21)

def ocdy_598_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 48 open close dynamics over a 63d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(90).mean())
    return _rolling_mean(base, 63)

def ocdy_599_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 48 open close dynamics over a 126d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(90).mean())
    return _rolling_mean(base, 126)

def ocdy_600_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 48 open close dynamics over a 252d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(90).mean())
    return _rolling_mean(base, 252)
