"""
112_112_volume_at_price — Base Features 526-600
Domain: 112_volume_at_price
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

def vapr_526_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 112 volume at price over a 5d horizon to identify extreme regimes.
    """
    base = volume * close.pct_change(16)
    return _rolling_mean(base, 5)

def vapr_527_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 112 volume at price over a 21d horizon to identify extreme regimes.
    """
    base = volume * close.pct_change(16)
    return _rolling_mean(base, 21)

def vapr_528_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 112 volume at price over a 63d horizon to identify extreme regimes.
    """
    base = volume * close.pct_change(16)
    return _rolling_mean(base, 63)

def vapr_529_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 112 volume at price over a 126d horizon to identify extreme regimes.
    """
    base = volume * close.pct_change(16)
    return _rolling_mean(base, 126)

def vapr_530_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 112 volume at price over a 252d horizon to identify extreme regimes.
    """
    base = volume * close.pct_change(16)
    return _rolling_mean(base, 252)

def vapr_531_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 112 volume at price by measuring deviations from the 5d mean.
    """
    base = volume * close.pct_change(16)
    return _zscore_rolling(base, 5)

def vapr_532_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 112 volume at price by measuring deviations from the 21d mean.
    """
    base = volume * close.pct_change(16)
    return _zscore_rolling(base, 21)

def vapr_533_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 112 volume at price by measuring deviations from the 63d mean.
    """
    base = volume * close.pct_change(16)
    return _zscore_rolling(base, 63)

def vapr_534_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 112 volume at price by measuring deviations from the 126d mean.
    """
    base = volume * close.pct_change(16)
    return _zscore_rolling(base, 126)

def vapr_535_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 112 volume at price by measuring deviations from the 252d mean.
    """
    base = volume * close.pct_change(16)
    return _zscore_rolling(base, 252)

def vapr_536_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 112 volume at price to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = volume * close.pct_change(16)
    return _rank_pct(base, 5)

def vapr_537_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 112 volume at price to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = volume * close.pct_change(16)
    return _rank_pct(base, 21)

def vapr_538_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 112 volume at price to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = volume * close.pct_change(16)
    return _rank_pct(base, 63)

def vapr_539_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 112 volume at price to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = volume * close.pct_change(16)
    return _rank_pct(base, 126)

def vapr_540_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 112 volume at price to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = volume * close.pct_change(16)
    return _rank_pct(base, 252)

def vapr_541_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 112 volume at price distribution over 5d to detect tail risk or exhaustion.
    """
    base = volume * close.pct_change(16)
    return _rolling_skew(base, 5)

def vapr_542_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 112 volume at price distribution over 21d to detect tail risk or exhaustion.
    """
    base = volume * close.pct_change(16)
    return _rolling_skew(base, 21)

def vapr_543_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 112 volume at price distribution over 63d to detect tail risk or exhaustion.
    """
    base = volume * close.pct_change(16)
    return _rolling_skew(base, 63)

def vapr_544_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 112 volume at price distribution over 126d to detect tail risk or exhaustion.
    """
    base = volume * close.pct_change(16)
    return _rolling_skew(base, 126)

def vapr_545_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 112 volume at price distribution over 252d to detect tail risk or exhaustion.
    """
    base = volume * close.pct_change(16)
    return _rolling_skew(base, 252)

def vapr_546_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 112 volume at price over 5d to capture explosive breakdown or reversal points.
    """
    base = volume * close.pct_change(16)
    return _rolling_kurt(base, 5)

def vapr_547_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 112 volume at price over 21d to capture explosive breakdown or reversal points.
    """
    base = volume * close.pct_change(16)
    return _rolling_kurt(base, 21)

def vapr_548_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 112 volume at price over 63d to capture explosive breakdown or reversal points.
    """
    base = volume * close.pct_change(16)
    return _rolling_kurt(base, 63)

def vapr_549_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 112 volume at price over 126d to capture explosive breakdown or reversal points.
    """
    base = volume * close.pct_change(16)
    return _rolling_kurt(base, 126)

def vapr_550_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 112 volume at price over 252d to capture explosive breakdown or reversal points.
    """
    base = volume * close.pct_change(16)
    return _rolling_kurt(base, 252)

def vapr_551_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 112 volume at price for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = volume * close.pct_change(16)
    return _safe_div(base, _rolling_std(base, 5))

def vapr_552_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 112 volume at price for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = volume * close.pct_change(16)
    return _safe_div(base, _rolling_std(base, 21))

def vapr_553_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 112 volume at price for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = volume * close.pct_change(16)
    return _safe_div(base, _rolling_std(base, 63))

def vapr_554_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 112 volume at price for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = volume * close.pct_change(16)
    return _safe_div(base, _rolling_std(base, 126))

def vapr_555_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 112 volume at price for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = volume * close.pct_change(16)
    return _safe_div(base, _rolling_std(base, 252))

def vapr_556_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 112 volume at price over 5d to stabilize variance and capture exponential shifts.
    """
    base = volume * close.pct_change(16)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def vapr_557_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 112 volume at price over 21d to stabilize variance and capture exponential shifts.
    """
    base = volume * close.pct_change(16)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def vapr_558_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 112 volume at price over 63d to stabilize variance and capture exponential shifts.
    """
    base = volume * close.pct_change(16)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def vapr_559_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 112 volume at price over 126d to stabilize variance and capture exponential shifts.
    """
    base = volume * close.pct_change(16)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def vapr_560_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 112 volume at price over 252d to stabilize variance and capture exponential shifts.
    """
    base = volume * close.pct_change(16)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def vapr_561_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 112 volume at price over a 5d horizon to identify extreme regimes.
    """
    base = volume * close.pct_change(17)
    return _rolling_mean(base, 5)

def vapr_562_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 112 volume at price over a 21d horizon to identify extreme regimes.
    """
    base = volume * close.pct_change(17)
    return _rolling_mean(base, 21)

def vapr_563_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 112 volume at price over a 63d horizon to identify extreme regimes.
    """
    base = volume * close.pct_change(17)
    return _rolling_mean(base, 63)

def vapr_564_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 112 volume at price over a 126d horizon to identify extreme regimes.
    """
    base = volume * close.pct_change(17)
    return _rolling_mean(base, 126)

def vapr_565_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 112 volume at price over a 252d horizon to identify extreme regimes.
    """
    base = volume * close.pct_change(17)
    return _rolling_mean(base, 252)

def vapr_566_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 112 volume at price by measuring deviations from the 5d mean.
    """
    base = volume * close.pct_change(17)
    return _zscore_rolling(base, 5)

def vapr_567_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 112 volume at price by measuring deviations from the 21d mean.
    """
    base = volume * close.pct_change(17)
    return _zscore_rolling(base, 21)

def vapr_568_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 112 volume at price by measuring deviations from the 63d mean.
    """
    base = volume * close.pct_change(17)
    return _zscore_rolling(base, 63)

def vapr_569_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 112 volume at price by measuring deviations from the 126d mean.
    """
    base = volume * close.pct_change(17)
    return _zscore_rolling(base, 126)

def vapr_570_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 112 volume at price by measuring deviations from the 252d mean.
    """
    base = volume * close.pct_change(17)
    return _zscore_rolling(base, 252)

def vapr_571_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 112 volume at price to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = volume * close.pct_change(17)
    return _rank_pct(base, 5)

def vapr_572_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 112 volume at price to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = volume * close.pct_change(17)
    return _rank_pct(base, 21)

def vapr_573_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 112 volume at price to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = volume * close.pct_change(17)
    return _rank_pct(base, 63)

def vapr_574_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 112 volume at price to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = volume * close.pct_change(17)
    return _rank_pct(base, 126)

def vapr_575_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 112 volume at price to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = volume * close.pct_change(17)
    return _rank_pct(base, 252)

def vapr_576_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 112 volume at price distribution over 5d to detect tail risk or exhaustion.
    """
    base = volume * close.pct_change(17)
    return _rolling_skew(base, 5)

def vapr_577_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 112 volume at price distribution over 21d to detect tail risk or exhaustion.
    """
    base = volume * close.pct_change(17)
    return _rolling_skew(base, 21)

def vapr_578_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 112 volume at price distribution over 63d to detect tail risk or exhaustion.
    """
    base = volume * close.pct_change(17)
    return _rolling_skew(base, 63)

def vapr_579_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 112 volume at price distribution over 126d to detect tail risk or exhaustion.
    """
    base = volume * close.pct_change(17)
    return _rolling_skew(base, 126)

def vapr_580_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 112 volume at price distribution over 252d to detect tail risk or exhaustion.
    """
    base = volume * close.pct_change(17)
    return _rolling_skew(base, 252)

def vapr_581_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 112 volume at price over 5d to capture explosive breakdown or reversal points.
    """
    base = volume * close.pct_change(17)
    return _rolling_kurt(base, 5)

def vapr_582_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 112 volume at price over 21d to capture explosive breakdown or reversal points.
    """
    base = volume * close.pct_change(17)
    return _rolling_kurt(base, 21)

def vapr_583_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 112 volume at price over 63d to capture explosive breakdown or reversal points.
    """
    base = volume * close.pct_change(17)
    return _rolling_kurt(base, 63)

def vapr_584_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 112 volume at price over 126d to capture explosive breakdown or reversal points.
    """
    base = volume * close.pct_change(17)
    return _rolling_kurt(base, 126)

def vapr_585_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 112 volume at price over 252d to capture explosive breakdown or reversal points.
    """
    base = volume * close.pct_change(17)
    return _rolling_kurt(base, 252)

def vapr_586_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 112 volume at price for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = volume * close.pct_change(17)
    return _safe_div(base, _rolling_std(base, 5))

def vapr_587_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 112 volume at price for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = volume * close.pct_change(17)
    return _safe_div(base, _rolling_std(base, 21))

def vapr_588_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 112 volume at price for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = volume * close.pct_change(17)
    return _safe_div(base, _rolling_std(base, 63))

def vapr_589_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 112 volume at price for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = volume * close.pct_change(17)
    return _safe_div(base, _rolling_std(base, 126))

def vapr_590_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 112 volume at price for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = volume * close.pct_change(17)
    return _safe_div(base, _rolling_std(base, 252))

def vapr_591_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 112 volume at price over 5d to stabilize variance and capture exponential shifts.
    """
    base = volume * close.pct_change(17)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def vapr_592_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 112 volume at price over 21d to stabilize variance and capture exponential shifts.
    """
    base = volume * close.pct_change(17)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def vapr_593_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 112 volume at price over 63d to stabilize variance and capture exponential shifts.
    """
    base = volume * close.pct_change(17)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def vapr_594_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 112 volume at price over 126d to stabilize variance and capture exponential shifts.
    """
    base = volume * close.pct_change(17)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def vapr_595_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 112 volume at price over 252d to stabilize variance and capture exponential shifts.
    """
    base = volume * close.pct_change(17)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def vapr_596_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 112 volume at price over a 5d horizon to identify extreme regimes.
    """
    base = volume * close.pct_change(18)
    return _rolling_mean(base, 5)

def vapr_597_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 112 volume at price over a 21d horizon to identify extreme regimes.
    """
    base = volume * close.pct_change(18)
    return _rolling_mean(base, 21)

def vapr_598_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 112 volume at price over a 63d horizon to identify extreme regimes.
    """
    base = volume * close.pct_change(18)
    return _rolling_mean(base, 63)

def vapr_599_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 112 volume at price over a 126d horizon to identify extreme regimes.
    """
    base = volume * close.pct_change(18)
    return _rolling_mean(base, 126)

def vapr_600_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 112 volume at price over a 252d horizon to identify extreme regimes.
    """
    base = volume * close.pct_change(18)
    return _rolling_mean(base, 252)
