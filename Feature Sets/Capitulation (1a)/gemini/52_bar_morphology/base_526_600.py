"""
52_52_bar_morphology — Base Features 526-600
Domain: 52_bar_morphology
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

def bmor_526_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 52 bar morphology over a 5d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(80).mean())
    return _rolling_mean(base, 5)

def bmor_527_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 52 bar morphology over a 21d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(80).mean())
    return _rolling_mean(base, 21)

def bmor_528_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 52 bar morphology over a 63d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(80).mean())
    return _rolling_mean(base, 63)

def bmor_529_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 52 bar morphology over a 126d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(80).mean())
    return _rolling_mean(base, 126)

def bmor_530_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 52 bar morphology over a 252d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(80).mean())
    return _rolling_mean(base, 252)

def bmor_531_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 52 bar morphology by measuring deviations from the 5d mean.
    """
    base = ((close - open).abs().rolling(80).mean())
    return _zscore_rolling(base, 5)

def bmor_532_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 52 bar morphology by measuring deviations from the 21d mean.
    """
    base = ((close - open).abs().rolling(80).mean())
    return _zscore_rolling(base, 21)

def bmor_533_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 52 bar morphology by measuring deviations from the 63d mean.
    """
    base = ((close - open).abs().rolling(80).mean())
    return _zscore_rolling(base, 63)

def bmor_534_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 52 bar morphology by measuring deviations from the 126d mean.
    """
    base = ((close - open).abs().rolling(80).mean())
    return _zscore_rolling(base, 126)

def bmor_535_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 52 bar morphology by measuring deviations from the 252d mean.
    """
    base = ((close - open).abs().rolling(80).mean())
    return _zscore_rolling(base, 252)

def bmor_536_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 52 bar morphology to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = ((close - open).abs().rolling(80).mean())
    return _rank_pct(base, 5)

def bmor_537_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 52 bar morphology to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = ((close - open).abs().rolling(80).mean())
    return _rank_pct(base, 21)

def bmor_538_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 52 bar morphology to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = ((close - open).abs().rolling(80).mean())
    return _rank_pct(base, 63)

def bmor_539_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 52 bar morphology to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = ((close - open).abs().rolling(80).mean())
    return _rank_pct(base, 126)

def bmor_540_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 52 bar morphology to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = ((close - open).abs().rolling(80).mean())
    return _rank_pct(base, 252)

def bmor_541_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 52 bar morphology distribution over 5d to detect tail risk or exhaustion.
    """
    base = ((close - open).abs().rolling(80).mean())
    return _rolling_skew(base, 5)

def bmor_542_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 52 bar morphology distribution over 21d to detect tail risk or exhaustion.
    """
    base = ((close - open).abs().rolling(80).mean())
    return _rolling_skew(base, 21)

def bmor_543_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 52 bar morphology distribution over 63d to detect tail risk or exhaustion.
    """
    base = ((close - open).abs().rolling(80).mean())
    return _rolling_skew(base, 63)

def bmor_544_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 52 bar morphology distribution over 126d to detect tail risk or exhaustion.
    """
    base = ((close - open).abs().rolling(80).mean())
    return _rolling_skew(base, 126)

def bmor_545_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 52 bar morphology distribution over 252d to detect tail risk or exhaustion.
    """
    base = ((close - open).abs().rolling(80).mean())
    return _rolling_skew(base, 252)

def bmor_546_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 52 bar morphology over 5d to capture explosive breakdown or reversal points.
    """
    base = ((close - open).abs().rolling(80).mean())
    return _rolling_kurt(base, 5)

def bmor_547_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 52 bar morphology over 21d to capture explosive breakdown or reversal points.
    """
    base = ((close - open).abs().rolling(80).mean())
    return _rolling_kurt(base, 21)

def bmor_548_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 52 bar morphology over 63d to capture explosive breakdown or reversal points.
    """
    base = ((close - open).abs().rolling(80).mean())
    return _rolling_kurt(base, 63)

def bmor_549_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 52 bar morphology over 126d to capture explosive breakdown or reversal points.
    """
    base = ((close - open).abs().rolling(80).mean())
    return _rolling_kurt(base, 126)

def bmor_550_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 52 bar morphology over 252d to capture explosive breakdown or reversal points.
    """
    base = ((close - open).abs().rolling(80).mean())
    return _rolling_kurt(base, 252)

def bmor_551_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 52 bar morphology for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = ((close - open).abs().rolling(80).mean())
    return _safe_div(base, _rolling_std(base, 5))

def bmor_552_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 52 bar morphology for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = ((close - open).abs().rolling(80).mean())
    return _safe_div(base, _rolling_std(base, 21))

def bmor_553_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 52 bar morphology for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = ((close - open).abs().rolling(80).mean())
    return _safe_div(base, _rolling_std(base, 63))

def bmor_554_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 52 bar morphology for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = ((close - open).abs().rolling(80).mean())
    return _safe_div(base, _rolling_std(base, 126))

def bmor_555_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 52 bar morphology for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = ((close - open).abs().rolling(80).mean())
    return _safe_div(base, _rolling_std(base, 252))

def bmor_556_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 52 bar morphology over 5d to stabilize variance and capture exponential shifts.
    """
    base = ((close - open).abs().rolling(80).mean())
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def bmor_557_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 52 bar morphology over 21d to stabilize variance and capture exponential shifts.
    """
    base = ((close - open).abs().rolling(80).mean())
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def bmor_558_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 52 bar morphology over 63d to stabilize variance and capture exponential shifts.
    """
    base = ((close - open).abs().rolling(80).mean())
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def bmor_559_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 52 bar morphology over 126d to stabilize variance and capture exponential shifts.
    """
    base = ((close - open).abs().rolling(80).mean())
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def bmor_560_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 52 bar morphology over 252d to stabilize variance and capture exponential shifts.
    """
    base = ((close - open).abs().rolling(80).mean())
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def bmor_561_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 52 bar morphology over a 5d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(85).mean())
    return _rolling_mean(base, 5)

def bmor_562_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 52 bar morphology over a 21d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(85).mean())
    return _rolling_mean(base, 21)

def bmor_563_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 52 bar morphology over a 63d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(85).mean())
    return _rolling_mean(base, 63)

def bmor_564_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 52 bar morphology over a 126d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(85).mean())
    return _rolling_mean(base, 126)

def bmor_565_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 52 bar morphology over a 252d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(85).mean())
    return _rolling_mean(base, 252)

def bmor_566_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 52 bar morphology by measuring deviations from the 5d mean.
    """
    base = ((close - open).abs().rolling(85).mean())
    return _zscore_rolling(base, 5)

def bmor_567_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 52 bar morphology by measuring deviations from the 21d mean.
    """
    base = ((close - open).abs().rolling(85).mean())
    return _zscore_rolling(base, 21)

def bmor_568_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 52 bar morphology by measuring deviations from the 63d mean.
    """
    base = ((close - open).abs().rolling(85).mean())
    return _zscore_rolling(base, 63)

def bmor_569_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 52 bar morphology by measuring deviations from the 126d mean.
    """
    base = ((close - open).abs().rolling(85).mean())
    return _zscore_rolling(base, 126)

def bmor_570_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 52 bar morphology by measuring deviations from the 252d mean.
    """
    base = ((close - open).abs().rolling(85).mean())
    return _zscore_rolling(base, 252)

def bmor_571_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 52 bar morphology to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = ((close - open).abs().rolling(85).mean())
    return _rank_pct(base, 5)

def bmor_572_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 52 bar morphology to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = ((close - open).abs().rolling(85).mean())
    return _rank_pct(base, 21)

def bmor_573_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 52 bar morphology to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = ((close - open).abs().rolling(85).mean())
    return _rank_pct(base, 63)

def bmor_574_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 52 bar morphology to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = ((close - open).abs().rolling(85).mean())
    return _rank_pct(base, 126)

def bmor_575_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 52 bar morphology to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = ((close - open).abs().rolling(85).mean())
    return _rank_pct(base, 252)

def bmor_576_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 52 bar morphology distribution over 5d to detect tail risk or exhaustion.
    """
    base = ((close - open).abs().rolling(85).mean())
    return _rolling_skew(base, 5)

def bmor_577_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 52 bar morphology distribution over 21d to detect tail risk or exhaustion.
    """
    base = ((close - open).abs().rolling(85).mean())
    return _rolling_skew(base, 21)

def bmor_578_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 52 bar morphology distribution over 63d to detect tail risk or exhaustion.
    """
    base = ((close - open).abs().rolling(85).mean())
    return _rolling_skew(base, 63)

def bmor_579_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 52 bar morphology distribution over 126d to detect tail risk or exhaustion.
    """
    base = ((close - open).abs().rolling(85).mean())
    return _rolling_skew(base, 126)

def bmor_580_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 52 bar morphology distribution over 252d to detect tail risk or exhaustion.
    """
    base = ((close - open).abs().rolling(85).mean())
    return _rolling_skew(base, 252)

def bmor_581_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 52 bar morphology over 5d to capture explosive breakdown or reversal points.
    """
    base = ((close - open).abs().rolling(85).mean())
    return _rolling_kurt(base, 5)

def bmor_582_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 52 bar morphology over 21d to capture explosive breakdown or reversal points.
    """
    base = ((close - open).abs().rolling(85).mean())
    return _rolling_kurt(base, 21)

def bmor_583_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 52 bar morphology over 63d to capture explosive breakdown or reversal points.
    """
    base = ((close - open).abs().rolling(85).mean())
    return _rolling_kurt(base, 63)

def bmor_584_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 52 bar morphology over 126d to capture explosive breakdown or reversal points.
    """
    base = ((close - open).abs().rolling(85).mean())
    return _rolling_kurt(base, 126)

def bmor_585_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 52 bar morphology over 252d to capture explosive breakdown or reversal points.
    """
    base = ((close - open).abs().rolling(85).mean())
    return _rolling_kurt(base, 252)

def bmor_586_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 52 bar morphology for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = ((close - open).abs().rolling(85).mean())
    return _safe_div(base, _rolling_std(base, 5))

def bmor_587_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 52 bar morphology for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = ((close - open).abs().rolling(85).mean())
    return _safe_div(base, _rolling_std(base, 21))

def bmor_588_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 52 bar morphology for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = ((close - open).abs().rolling(85).mean())
    return _safe_div(base, _rolling_std(base, 63))

def bmor_589_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 52 bar morphology for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = ((close - open).abs().rolling(85).mean())
    return _safe_div(base, _rolling_std(base, 126))

def bmor_590_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 52 bar morphology for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = ((close - open).abs().rolling(85).mean())
    return _safe_div(base, _rolling_std(base, 252))

def bmor_591_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 52 bar morphology over 5d to stabilize variance and capture exponential shifts.
    """
    base = ((close - open).abs().rolling(85).mean())
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def bmor_592_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 52 bar morphology over 21d to stabilize variance and capture exponential shifts.
    """
    base = ((close - open).abs().rolling(85).mean())
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def bmor_593_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 52 bar morphology over 63d to stabilize variance and capture exponential shifts.
    """
    base = ((close - open).abs().rolling(85).mean())
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def bmor_594_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 52 bar morphology over 126d to stabilize variance and capture exponential shifts.
    """
    base = ((close - open).abs().rolling(85).mean())
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def bmor_595_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 52 bar morphology over 252d to stabilize variance and capture exponential shifts.
    """
    base = ((close - open).abs().rolling(85).mean())
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def bmor_596_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 52 bar morphology over a 5d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(90).mean())
    return _rolling_mean(base, 5)

def bmor_597_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 52 bar morphology over a 21d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(90).mean())
    return _rolling_mean(base, 21)

def bmor_598_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 52 bar morphology over a 63d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(90).mean())
    return _rolling_mean(base, 63)

def bmor_599_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 52 bar morphology over a 126d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(90).mean())
    return _rolling_mean(base, 126)

def bmor_600_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 52 bar morphology over a 252d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(90).mean())
    return _rolling_mean(base, 252)
