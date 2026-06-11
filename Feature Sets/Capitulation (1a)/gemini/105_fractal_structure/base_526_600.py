"""
105_105_fractal_structure — Base Features 526-600
Domain: 105_fractal_structure
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

def frac_526_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 105 fractal structure over a 5d horizon to identify extreme regimes.
    """
    base = close.diff().abs().rolling(80).sum()
    return _rolling_mean(base, 5)

def frac_527_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 105 fractal structure over a 21d horizon to identify extreme regimes.
    """
    base = close.diff().abs().rolling(80).sum()
    return _rolling_mean(base, 21)

def frac_528_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 105 fractal structure over a 63d horizon to identify extreme regimes.
    """
    base = close.diff().abs().rolling(80).sum()
    return _rolling_mean(base, 63)

def frac_529_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 105 fractal structure over a 126d horizon to identify extreme regimes.
    """
    base = close.diff().abs().rolling(80).sum()
    return _rolling_mean(base, 126)

def frac_530_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 105 fractal structure over a 252d horizon to identify extreme regimes.
    """
    base = close.diff().abs().rolling(80).sum()
    return _rolling_mean(base, 252)

def frac_531_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 105 fractal structure by measuring deviations from the 5d mean.
    """
    base = close.diff().abs().rolling(80).sum()
    return _zscore_rolling(base, 5)

def frac_532_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 105 fractal structure by measuring deviations from the 21d mean.
    """
    base = close.diff().abs().rolling(80).sum()
    return _zscore_rolling(base, 21)

def frac_533_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 105 fractal structure by measuring deviations from the 63d mean.
    """
    base = close.diff().abs().rolling(80).sum()
    return _zscore_rolling(base, 63)

def frac_534_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 105 fractal structure by measuring deviations from the 126d mean.
    """
    base = close.diff().abs().rolling(80).sum()
    return _zscore_rolling(base, 126)

def frac_535_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 105 fractal structure by measuring deviations from the 252d mean.
    """
    base = close.diff().abs().rolling(80).sum()
    return _zscore_rolling(base, 252)

def frac_536_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 105 fractal structure to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = close.diff().abs().rolling(80).sum()
    return _rank_pct(base, 5)

def frac_537_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 105 fractal structure to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = close.diff().abs().rolling(80).sum()
    return _rank_pct(base, 21)

def frac_538_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 105 fractal structure to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = close.diff().abs().rolling(80).sum()
    return _rank_pct(base, 63)

def frac_539_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 105 fractal structure to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = close.diff().abs().rolling(80).sum()
    return _rank_pct(base, 126)

def frac_540_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 105 fractal structure to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = close.diff().abs().rolling(80).sum()
    return _rank_pct(base, 252)

def frac_541_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 105 fractal structure distribution over 5d to detect tail risk or exhaustion.
    """
    base = close.diff().abs().rolling(80).sum()
    return _rolling_skew(base, 5)

def frac_542_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 105 fractal structure distribution over 21d to detect tail risk or exhaustion.
    """
    base = close.diff().abs().rolling(80).sum()
    return _rolling_skew(base, 21)

def frac_543_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 105 fractal structure distribution over 63d to detect tail risk or exhaustion.
    """
    base = close.diff().abs().rolling(80).sum()
    return _rolling_skew(base, 63)

def frac_544_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 105 fractal structure distribution over 126d to detect tail risk or exhaustion.
    """
    base = close.diff().abs().rolling(80).sum()
    return _rolling_skew(base, 126)

def frac_545_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 105 fractal structure distribution over 252d to detect tail risk or exhaustion.
    """
    base = close.diff().abs().rolling(80).sum()
    return _rolling_skew(base, 252)

def frac_546_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 105 fractal structure over 5d to capture explosive breakdown or reversal points.
    """
    base = close.diff().abs().rolling(80).sum()
    return _rolling_kurt(base, 5)

def frac_547_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 105 fractal structure over 21d to capture explosive breakdown or reversal points.
    """
    base = close.diff().abs().rolling(80).sum()
    return _rolling_kurt(base, 21)

def frac_548_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 105 fractal structure over 63d to capture explosive breakdown or reversal points.
    """
    base = close.diff().abs().rolling(80).sum()
    return _rolling_kurt(base, 63)

def frac_549_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 105 fractal structure over 126d to capture explosive breakdown or reversal points.
    """
    base = close.diff().abs().rolling(80).sum()
    return _rolling_kurt(base, 126)

def frac_550_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 105 fractal structure over 252d to capture explosive breakdown or reversal points.
    """
    base = close.diff().abs().rolling(80).sum()
    return _rolling_kurt(base, 252)

def frac_551_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 105 fractal structure for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = close.diff().abs().rolling(80).sum()
    return _safe_div(base, _rolling_std(base, 5))

def frac_552_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 105 fractal structure for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = close.diff().abs().rolling(80).sum()
    return _safe_div(base, _rolling_std(base, 21))

def frac_553_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 105 fractal structure for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = close.diff().abs().rolling(80).sum()
    return _safe_div(base, _rolling_std(base, 63))

def frac_554_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 105 fractal structure for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = close.diff().abs().rolling(80).sum()
    return _safe_div(base, _rolling_std(base, 126))

def frac_555_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 105 fractal structure for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = close.diff().abs().rolling(80).sum()
    return _safe_div(base, _rolling_std(base, 252))

def frac_556_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 105 fractal structure over 5d to stabilize variance and capture exponential shifts.
    """
    base = close.diff().abs().rolling(80).sum()
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def frac_557_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 105 fractal structure over 21d to stabilize variance and capture exponential shifts.
    """
    base = close.diff().abs().rolling(80).sum()
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def frac_558_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 105 fractal structure over 63d to stabilize variance and capture exponential shifts.
    """
    base = close.diff().abs().rolling(80).sum()
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def frac_559_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 105 fractal structure over 126d to stabilize variance and capture exponential shifts.
    """
    base = close.diff().abs().rolling(80).sum()
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def frac_560_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 105 fractal structure over 252d to stabilize variance and capture exponential shifts.
    """
    base = close.diff().abs().rolling(80).sum()
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def frac_561_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 105 fractal structure over a 5d horizon to identify extreme regimes.
    """
    base = close.diff().abs().rolling(85).sum()
    return _rolling_mean(base, 5)

def frac_562_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 105 fractal structure over a 21d horizon to identify extreme regimes.
    """
    base = close.diff().abs().rolling(85).sum()
    return _rolling_mean(base, 21)

def frac_563_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 105 fractal structure over a 63d horizon to identify extreme regimes.
    """
    base = close.diff().abs().rolling(85).sum()
    return _rolling_mean(base, 63)

def frac_564_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 105 fractal structure over a 126d horizon to identify extreme regimes.
    """
    base = close.diff().abs().rolling(85).sum()
    return _rolling_mean(base, 126)

def frac_565_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 105 fractal structure over a 252d horizon to identify extreme regimes.
    """
    base = close.diff().abs().rolling(85).sum()
    return _rolling_mean(base, 252)

def frac_566_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 105 fractal structure by measuring deviations from the 5d mean.
    """
    base = close.diff().abs().rolling(85).sum()
    return _zscore_rolling(base, 5)

def frac_567_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 105 fractal structure by measuring deviations from the 21d mean.
    """
    base = close.diff().abs().rolling(85).sum()
    return _zscore_rolling(base, 21)

def frac_568_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 105 fractal structure by measuring deviations from the 63d mean.
    """
    base = close.diff().abs().rolling(85).sum()
    return _zscore_rolling(base, 63)

def frac_569_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 105 fractal structure by measuring deviations from the 126d mean.
    """
    base = close.diff().abs().rolling(85).sum()
    return _zscore_rolling(base, 126)

def frac_570_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 105 fractal structure by measuring deviations from the 252d mean.
    """
    base = close.diff().abs().rolling(85).sum()
    return _zscore_rolling(base, 252)

def frac_571_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 105 fractal structure to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = close.diff().abs().rolling(85).sum()
    return _rank_pct(base, 5)

def frac_572_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 105 fractal structure to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = close.diff().abs().rolling(85).sum()
    return _rank_pct(base, 21)

def frac_573_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 105 fractal structure to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = close.diff().abs().rolling(85).sum()
    return _rank_pct(base, 63)

def frac_574_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 105 fractal structure to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = close.diff().abs().rolling(85).sum()
    return _rank_pct(base, 126)

def frac_575_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 105 fractal structure to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = close.diff().abs().rolling(85).sum()
    return _rank_pct(base, 252)

def frac_576_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 105 fractal structure distribution over 5d to detect tail risk or exhaustion.
    """
    base = close.diff().abs().rolling(85).sum()
    return _rolling_skew(base, 5)

def frac_577_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 105 fractal structure distribution over 21d to detect tail risk or exhaustion.
    """
    base = close.diff().abs().rolling(85).sum()
    return _rolling_skew(base, 21)

def frac_578_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 105 fractal structure distribution over 63d to detect tail risk or exhaustion.
    """
    base = close.diff().abs().rolling(85).sum()
    return _rolling_skew(base, 63)

def frac_579_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 105 fractal structure distribution over 126d to detect tail risk or exhaustion.
    """
    base = close.diff().abs().rolling(85).sum()
    return _rolling_skew(base, 126)

def frac_580_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 105 fractal structure distribution over 252d to detect tail risk or exhaustion.
    """
    base = close.diff().abs().rolling(85).sum()
    return _rolling_skew(base, 252)

def frac_581_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 105 fractal structure over 5d to capture explosive breakdown or reversal points.
    """
    base = close.diff().abs().rolling(85).sum()
    return _rolling_kurt(base, 5)

def frac_582_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 105 fractal structure over 21d to capture explosive breakdown or reversal points.
    """
    base = close.diff().abs().rolling(85).sum()
    return _rolling_kurt(base, 21)

def frac_583_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 105 fractal structure over 63d to capture explosive breakdown or reversal points.
    """
    base = close.diff().abs().rolling(85).sum()
    return _rolling_kurt(base, 63)

def frac_584_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 105 fractal structure over 126d to capture explosive breakdown or reversal points.
    """
    base = close.diff().abs().rolling(85).sum()
    return _rolling_kurt(base, 126)

def frac_585_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 105 fractal structure over 252d to capture explosive breakdown or reversal points.
    """
    base = close.diff().abs().rolling(85).sum()
    return _rolling_kurt(base, 252)

def frac_586_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 105 fractal structure for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = close.diff().abs().rolling(85).sum()
    return _safe_div(base, _rolling_std(base, 5))

def frac_587_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 105 fractal structure for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = close.diff().abs().rolling(85).sum()
    return _safe_div(base, _rolling_std(base, 21))

def frac_588_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 105 fractal structure for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = close.diff().abs().rolling(85).sum()
    return _safe_div(base, _rolling_std(base, 63))

def frac_589_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 105 fractal structure for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = close.diff().abs().rolling(85).sum()
    return _safe_div(base, _rolling_std(base, 126))

def frac_590_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 105 fractal structure for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = close.diff().abs().rolling(85).sum()
    return _safe_div(base, _rolling_std(base, 252))

def frac_591_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 105 fractal structure over 5d to stabilize variance and capture exponential shifts.
    """
    base = close.diff().abs().rolling(85).sum()
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def frac_592_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 105 fractal structure over 21d to stabilize variance and capture exponential shifts.
    """
    base = close.diff().abs().rolling(85).sum()
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def frac_593_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 105 fractal structure over 63d to stabilize variance and capture exponential shifts.
    """
    base = close.diff().abs().rolling(85).sum()
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def frac_594_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 105 fractal structure over 126d to stabilize variance and capture exponential shifts.
    """
    base = close.diff().abs().rolling(85).sum()
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def frac_595_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 105 fractal structure over 252d to stabilize variance and capture exponential shifts.
    """
    base = close.diff().abs().rolling(85).sum()
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def frac_596_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 105 fractal structure over a 5d horizon to identify extreme regimes.
    """
    base = close.diff().abs().rolling(90).sum()
    return _rolling_mean(base, 5)

def frac_597_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 105 fractal structure over a 21d horizon to identify extreme regimes.
    """
    base = close.diff().abs().rolling(90).sum()
    return _rolling_mean(base, 21)

def frac_598_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 105 fractal structure over a 63d horizon to identify extreme regimes.
    """
    base = close.diff().abs().rolling(90).sum()
    return _rolling_mean(base, 63)

def frac_599_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 105 fractal structure over a 126d horizon to identify extreme regimes.
    """
    base = close.diff().abs().rolling(90).sum()
    return _rolling_mean(base, 126)

def frac_600_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 105 fractal structure over a 252d horizon to identify extreme regimes.
    """
    base = close.diff().abs().rolling(90).sum()
    return _rolling_mean(base, 252)
