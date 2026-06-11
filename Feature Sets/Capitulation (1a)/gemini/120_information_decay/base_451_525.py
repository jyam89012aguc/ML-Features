"""
120_120_information_decay — Base Features 451-525
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

def idec_451_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 120 information decay over 5d to stabilize variance and capture exponential shifts.
    """
    base = close.diff().abs().rolling(65).sum()
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def idec_452_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 120 information decay over 21d to stabilize variance and capture exponential shifts.
    """
    base = close.diff().abs().rolling(65).sum()
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def idec_453_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 120 information decay over 63d to stabilize variance and capture exponential shifts.
    """
    base = close.diff().abs().rolling(65).sum()
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def idec_454_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 120 information decay over 126d to stabilize variance and capture exponential shifts.
    """
    base = close.diff().abs().rolling(65).sum()
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def idec_455_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 120 information decay over 252d to stabilize variance and capture exponential shifts.
    """
    base = close.diff().abs().rolling(65).sum()
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def idec_456_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 120 information decay over a 5d horizon to identify extreme regimes.
    """
    base = close.diff().abs().rolling(70).sum()
    return _rolling_mean(base, 5)

def idec_457_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 120 information decay over a 21d horizon to identify extreme regimes.
    """
    base = close.diff().abs().rolling(70).sum()
    return _rolling_mean(base, 21)

def idec_458_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 120 information decay over a 63d horizon to identify extreme regimes.
    """
    base = close.diff().abs().rolling(70).sum()
    return _rolling_mean(base, 63)

def idec_459_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 120 information decay over a 126d horizon to identify extreme regimes.
    """
    base = close.diff().abs().rolling(70).sum()
    return _rolling_mean(base, 126)

def idec_460_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 120 information decay over a 252d horizon to identify extreme regimes.
    """
    base = close.diff().abs().rolling(70).sum()
    return _rolling_mean(base, 252)

def idec_461_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 120 information decay by measuring deviations from the 5d mean.
    """
    base = close.diff().abs().rolling(70).sum()
    return _zscore_rolling(base, 5)

def idec_462_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 120 information decay by measuring deviations from the 21d mean.
    """
    base = close.diff().abs().rolling(70).sum()
    return _zscore_rolling(base, 21)

def idec_463_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 120 information decay by measuring deviations from the 63d mean.
    """
    base = close.diff().abs().rolling(70).sum()
    return _zscore_rolling(base, 63)

def idec_464_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 120 information decay by measuring deviations from the 126d mean.
    """
    base = close.diff().abs().rolling(70).sum()
    return _zscore_rolling(base, 126)

def idec_465_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 120 information decay by measuring deviations from the 252d mean.
    """
    base = close.diff().abs().rolling(70).sum()
    return _zscore_rolling(base, 252)

def idec_466_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 120 information decay to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = close.diff().abs().rolling(70).sum()
    return _rank_pct(base, 5)

def idec_467_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 120 information decay to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = close.diff().abs().rolling(70).sum()
    return _rank_pct(base, 21)

def idec_468_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 120 information decay to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = close.diff().abs().rolling(70).sum()
    return _rank_pct(base, 63)

def idec_469_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 120 information decay to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = close.diff().abs().rolling(70).sum()
    return _rank_pct(base, 126)

def idec_470_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 120 information decay to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = close.diff().abs().rolling(70).sum()
    return _rank_pct(base, 252)

def idec_471_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 120 information decay distribution over 5d to detect tail risk or exhaustion.
    """
    base = close.diff().abs().rolling(70).sum()
    return _rolling_skew(base, 5)

def idec_472_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 120 information decay distribution over 21d to detect tail risk or exhaustion.
    """
    base = close.diff().abs().rolling(70).sum()
    return _rolling_skew(base, 21)

def idec_473_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 120 information decay distribution over 63d to detect tail risk or exhaustion.
    """
    base = close.diff().abs().rolling(70).sum()
    return _rolling_skew(base, 63)

def idec_474_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 120 information decay distribution over 126d to detect tail risk or exhaustion.
    """
    base = close.diff().abs().rolling(70).sum()
    return _rolling_skew(base, 126)

def idec_475_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 120 information decay distribution over 252d to detect tail risk or exhaustion.
    """
    base = close.diff().abs().rolling(70).sum()
    return _rolling_skew(base, 252)

def idec_476_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 120 information decay over 5d to capture explosive breakdown or reversal points.
    """
    base = close.diff().abs().rolling(70).sum()
    return _rolling_kurt(base, 5)

def idec_477_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 120 information decay over 21d to capture explosive breakdown or reversal points.
    """
    base = close.diff().abs().rolling(70).sum()
    return _rolling_kurt(base, 21)

def idec_478_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 120 information decay over 63d to capture explosive breakdown or reversal points.
    """
    base = close.diff().abs().rolling(70).sum()
    return _rolling_kurt(base, 63)

def idec_479_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 120 information decay over 126d to capture explosive breakdown or reversal points.
    """
    base = close.diff().abs().rolling(70).sum()
    return _rolling_kurt(base, 126)

def idec_480_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 120 information decay over 252d to capture explosive breakdown or reversal points.
    """
    base = close.diff().abs().rolling(70).sum()
    return _rolling_kurt(base, 252)

def idec_481_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 120 information decay for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = close.diff().abs().rolling(70).sum()
    return _safe_div(base, _rolling_std(base, 5))

def idec_482_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 120 information decay for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = close.diff().abs().rolling(70).sum()
    return _safe_div(base, _rolling_std(base, 21))

def idec_483_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 120 information decay for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = close.diff().abs().rolling(70).sum()
    return _safe_div(base, _rolling_std(base, 63))

def idec_484_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 120 information decay for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = close.diff().abs().rolling(70).sum()
    return _safe_div(base, _rolling_std(base, 126))

def idec_485_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 120 information decay for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = close.diff().abs().rolling(70).sum()
    return _safe_div(base, _rolling_std(base, 252))

def idec_486_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 120 information decay over 5d to stabilize variance and capture exponential shifts.
    """
    base = close.diff().abs().rolling(70).sum()
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def idec_487_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 120 information decay over 21d to stabilize variance and capture exponential shifts.
    """
    base = close.diff().abs().rolling(70).sum()
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def idec_488_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 120 information decay over 63d to stabilize variance and capture exponential shifts.
    """
    base = close.diff().abs().rolling(70).sum()
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def idec_489_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 120 information decay over 126d to stabilize variance and capture exponential shifts.
    """
    base = close.diff().abs().rolling(70).sum()
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def idec_490_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 120 information decay over 252d to stabilize variance and capture exponential shifts.
    """
    base = close.diff().abs().rolling(70).sum()
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def idec_491_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 120 information decay over a 5d horizon to identify extreme regimes.
    """
    base = close.diff().abs().rolling(75).sum()
    return _rolling_mean(base, 5)

def idec_492_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 120 information decay over a 21d horizon to identify extreme regimes.
    """
    base = close.diff().abs().rolling(75).sum()
    return _rolling_mean(base, 21)

def idec_493_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 120 information decay over a 63d horizon to identify extreme regimes.
    """
    base = close.diff().abs().rolling(75).sum()
    return _rolling_mean(base, 63)

def idec_494_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 120 information decay over a 126d horizon to identify extreme regimes.
    """
    base = close.diff().abs().rolling(75).sum()
    return _rolling_mean(base, 126)

def idec_495_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 120 information decay over a 252d horizon to identify extreme regimes.
    """
    base = close.diff().abs().rolling(75).sum()
    return _rolling_mean(base, 252)

def idec_496_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 120 information decay by measuring deviations from the 5d mean.
    """
    base = close.diff().abs().rolling(75).sum()
    return _zscore_rolling(base, 5)

def idec_497_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 120 information decay by measuring deviations from the 21d mean.
    """
    base = close.diff().abs().rolling(75).sum()
    return _zscore_rolling(base, 21)

def idec_498_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 120 information decay by measuring deviations from the 63d mean.
    """
    base = close.diff().abs().rolling(75).sum()
    return _zscore_rolling(base, 63)

def idec_499_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 120 information decay by measuring deviations from the 126d mean.
    """
    base = close.diff().abs().rolling(75).sum()
    return _zscore_rolling(base, 126)

def idec_500_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 120 information decay by measuring deviations from the 252d mean.
    """
    base = close.diff().abs().rolling(75).sum()
    return _zscore_rolling(base, 252)

def idec_501_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 120 information decay to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = close.diff().abs().rolling(75).sum()
    return _rank_pct(base, 5)

def idec_502_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 120 information decay to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = close.diff().abs().rolling(75).sum()
    return _rank_pct(base, 21)

def idec_503_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 120 information decay to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = close.diff().abs().rolling(75).sum()
    return _rank_pct(base, 63)

def idec_504_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 120 information decay to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = close.diff().abs().rolling(75).sum()
    return _rank_pct(base, 126)

def idec_505_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 120 information decay to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = close.diff().abs().rolling(75).sum()
    return _rank_pct(base, 252)

def idec_506_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 120 information decay distribution over 5d to detect tail risk or exhaustion.
    """
    base = close.diff().abs().rolling(75).sum()
    return _rolling_skew(base, 5)

def idec_507_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 120 information decay distribution over 21d to detect tail risk or exhaustion.
    """
    base = close.diff().abs().rolling(75).sum()
    return _rolling_skew(base, 21)

def idec_508_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 120 information decay distribution over 63d to detect tail risk or exhaustion.
    """
    base = close.diff().abs().rolling(75).sum()
    return _rolling_skew(base, 63)

def idec_509_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 120 information decay distribution over 126d to detect tail risk or exhaustion.
    """
    base = close.diff().abs().rolling(75).sum()
    return _rolling_skew(base, 126)

def idec_510_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 120 information decay distribution over 252d to detect tail risk or exhaustion.
    """
    base = close.diff().abs().rolling(75).sum()
    return _rolling_skew(base, 252)

def idec_511_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 120 information decay over 5d to capture explosive breakdown or reversal points.
    """
    base = close.diff().abs().rolling(75).sum()
    return _rolling_kurt(base, 5)

def idec_512_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 120 information decay over 21d to capture explosive breakdown or reversal points.
    """
    base = close.diff().abs().rolling(75).sum()
    return _rolling_kurt(base, 21)

def idec_513_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 120 information decay over 63d to capture explosive breakdown or reversal points.
    """
    base = close.diff().abs().rolling(75).sum()
    return _rolling_kurt(base, 63)

def idec_514_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 120 information decay over 126d to capture explosive breakdown or reversal points.
    """
    base = close.diff().abs().rolling(75).sum()
    return _rolling_kurt(base, 126)

def idec_515_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 120 information decay over 252d to capture explosive breakdown or reversal points.
    """
    base = close.diff().abs().rolling(75).sum()
    return _rolling_kurt(base, 252)

def idec_516_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 120 information decay for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = close.diff().abs().rolling(75).sum()
    return _safe_div(base, _rolling_std(base, 5))

def idec_517_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 120 information decay for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = close.diff().abs().rolling(75).sum()
    return _safe_div(base, _rolling_std(base, 21))

def idec_518_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 120 information decay for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = close.diff().abs().rolling(75).sum()
    return _safe_div(base, _rolling_std(base, 63))

def idec_519_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 120 information decay for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = close.diff().abs().rolling(75).sum()
    return _safe_div(base, _rolling_std(base, 126))

def idec_520_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 120 information decay for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = close.diff().abs().rolling(75).sum()
    return _safe_div(base, _rolling_std(base, 252))

def idec_521_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 120 information decay over 5d to stabilize variance and capture exponential shifts.
    """
    base = close.diff().abs().rolling(75).sum()
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def idec_522_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 120 information decay over 21d to stabilize variance and capture exponential shifts.
    """
    base = close.diff().abs().rolling(75).sum()
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def idec_523_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 120 information decay over 63d to stabilize variance and capture exponential shifts.
    """
    base = close.diff().abs().rolling(75).sum()
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def idec_524_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 120 information decay over 126d to stabilize variance and capture exponential shifts.
    """
    base = close.diff().abs().rolling(75).sum()
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def idec_525_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 120 information decay over 252d to stabilize variance and capture exponential shifts.
    """
    base = close.diff().abs().rolling(75).sum()
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))
