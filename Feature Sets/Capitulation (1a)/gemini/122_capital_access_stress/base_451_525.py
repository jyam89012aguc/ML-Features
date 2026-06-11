"""
122_122_capital_access_stress — Base Features 451-525
Domain: 122_capital_access_stress
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

def cast_451_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 122 capital access stress over 5d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(65).std()
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def cast_452_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 122 capital access stress over 21d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(65).std()
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def cast_453_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 122 capital access stress over 63d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(65).std()
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def cast_454_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 122 capital access stress over 126d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(65).std()
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def cast_455_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 122 capital access stress over 252d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(65).std()
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def cast_456_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 122 capital access stress over a 5d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(70).std()
    return _rolling_mean(base, 5)

def cast_457_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 122 capital access stress over a 21d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(70).std()
    return _rolling_mean(base, 21)

def cast_458_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 122 capital access stress over a 63d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(70).std()
    return _rolling_mean(base, 63)

def cast_459_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 122 capital access stress over a 126d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(70).std()
    return _rolling_mean(base, 126)

def cast_460_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 122 capital access stress over a 252d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(70).std()
    return _rolling_mean(base, 252)

def cast_461_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 122 capital access stress by measuring deviations from the 5d mean.
    """
    base = close.pct_change().rolling(70).std()
    return _zscore_rolling(base, 5)

def cast_462_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 122 capital access stress by measuring deviations from the 21d mean.
    """
    base = close.pct_change().rolling(70).std()
    return _zscore_rolling(base, 21)

def cast_463_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 122 capital access stress by measuring deviations from the 63d mean.
    """
    base = close.pct_change().rolling(70).std()
    return _zscore_rolling(base, 63)

def cast_464_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 122 capital access stress by measuring deviations from the 126d mean.
    """
    base = close.pct_change().rolling(70).std()
    return _zscore_rolling(base, 126)

def cast_465_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 122 capital access stress by measuring deviations from the 252d mean.
    """
    base = close.pct_change().rolling(70).std()
    return _zscore_rolling(base, 252)

def cast_466_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 122 capital access stress to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(70).std()
    return _rank_pct(base, 5)

def cast_467_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 122 capital access stress to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(70).std()
    return _rank_pct(base, 21)

def cast_468_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 122 capital access stress to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(70).std()
    return _rank_pct(base, 63)

def cast_469_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 122 capital access stress to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(70).std()
    return _rank_pct(base, 126)

def cast_470_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 122 capital access stress to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(70).std()
    return _rank_pct(base, 252)

def cast_471_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 122 capital access stress distribution over 5d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(70).std()
    return _rolling_skew(base, 5)

def cast_472_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 122 capital access stress distribution over 21d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(70).std()
    return _rolling_skew(base, 21)

def cast_473_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 122 capital access stress distribution over 63d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(70).std()
    return _rolling_skew(base, 63)

def cast_474_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 122 capital access stress distribution over 126d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(70).std()
    return _rolling_skew(base, 126)

def cast_475_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 122 capital access stress distribution over 252d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(70).std()
    return _rolling_skew(base, 252)

def cast_476_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 122 capital access stress over 5d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(70).std()
    return _rolling_kurt(base, 5)

def cast_477_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 122 capital access stress over 21d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(70).std()
    return _rolling_kurt(base, 21)

def cast_478_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 122 capital access stress over 63d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(70).std()
    return _rolling_kurt(base, 63)

def cast_479_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 122 capital access stress over 126d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(70).std()
    return _rolling_kurt(base, 126)

def cast_480_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 122 capital access stress over 252d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(70).std()
    return _rolling_kurt(base, 252)

def cast_481_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 122 capital access stress for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(70).std()
    return _safe_div(base, _rolling_std(base, 5))

def cast_482_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 122 capital access stress for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(70).std()
    return _safe_div(base, _rolling_std(base, 21))

def cast_483_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 122 capital access stress for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(70).std()
    return _safe_div(base, _rolling_std(base, 63))

def cast_484_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 122 capital access stress for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(70).std()
    return _safe_div(base, _rolling_std(base, 126))

def cast_485_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 122 capital access stress for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(70).std()
    return _safe_div(base, _rolling_std(base, 252))

def cast_486_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 122 capital access stress over 5d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(70).std()
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def cast_487_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 122 capital access stress over 21d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(70).std()
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def cast_488_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 122 capital access stress over 63d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(70).std()
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def cast_489_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 122 capital access stress over 126d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(70).std()
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def cast_490_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 122 capital access stress over 252d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(70).std()
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def cast_491_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 122 capital access stress over a 5d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(75).std()
    return _rolling_mean(base, 5)

def cast_492_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 122 capital access stress over a 21d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(75).std()
    return _rolling_mean(base, 21)

def cast_493_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 122 capital access stress over a 63d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(75).std()
    return _rolling_mean(base, 63)

def cast_494_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 122 capital access stress over a 126d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(75).std()
    return _rolling_mean(base, 126)

def cast_495_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 122 capital access stress over a 252d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(75).std()
    return _rolling_mean(base, 252)

def cast_496_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 122 capital access stress by measuring deviations from the 5d mean.
    """
    base = close.pct_change().rolling(75).std()
    return _zscore_rolling(base, 5)

def cast_497_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 122 capital access stress by measuring deviations from the 21d mean.
    """
    base = close.pct_change().rolling(75).std()
    return _zscore_rolling(base, 21)

def cast_498_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 122 capital access stress by measuring deviations from the 63d mean.
    """
    base = close.pct_change().rolling(75).std()
    return _zscore_rolling(base, 63)

def cast_499_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 122 capital access stress by measuring deviations from the 126d mean.
    """
    base = close.pct_change().rolling(75).std()
    return _zscore_rolling(base, 126)

def cast_500_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 122 capital access stress by measuring deviations from the 252d mean.
    """
    base = close.pct_change().rolling(75).std()
    return _zscore_rolling(base, 252)

def cast_501_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 122 capital access stress to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(75).std()
    return _rank_pct(base, 5)

def cast_502_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 122 capital access stress to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(75).std()
    return _rank_pct(base, 21)

def cast_503_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 122 capital access stress to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(75).std()
    return _rank_pct(base, 63)

def cast_504_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 122 capital access stress to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(75).std()
    return _rank_pct(base, 126)

def cast_505_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 122 capital access stress to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(75).std()
    return _rank_pct(base, 252)

def cast_506_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 122 capital access stress distribution over 5d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(75).std()
    return _rolling_skew(base, 5)

def cast_507_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 122 capital access stress distribution over 21d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(75).std()
    return _rolling_skew(base, 21)

def cast_508_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 122 capital access stress distribution over 63d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(75).std()
    return _rolling_skew(base, 63)

def cast_509_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 122 capital access stress distribution over 126d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(75).std()
    return _rolling_skew(base, 126)

def cast_510_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 122 capital access stress distribution over 252d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(75).std()
    return _rolling_skew(base, 252)

def cast_511_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 122 capital access stress over 5d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(75).std()
    return _rolling_kurt(base, 5)

def cast_512_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 122 capital access stress over 21d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(75).std()
    return _rolling_kurt(base, 21)

def cast_513_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 122 capital access stress over 63d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(75).std()
    return _rolling_kurt(base, 63)

def cast_514_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 122 capital access stress over 126d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(75).std()
    return _rolling_kurt(base, 126)

def cast_515_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 122 capital access stress over 252d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(75).std()
    return _rolling_kurt(base, 252)

def cast_516_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 122 capital access stress for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(75).std()
    return _safe_div(base, _rolling_std(base, 5))

def cast_517_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 122 capital access stress for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(75).std()
    return _safe_div(base, _rolling_std(base, 21))

def cast_518_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 122 capital access stress for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(75).std()
    return _safe_div(base, _rolling_std(base, 63))

def cast_519_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 122 capital access stress for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(75).std()
    return _safe_div(base, _rolling_std(base, 126))

def cast_520_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 122 capital access stress for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(75).std()
    return _safe_div(base, _rolling_std(base, 252))

def cast_521_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 122 capital access stress over 5d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(75).std()
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def cast_522_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 122 capital access stress over 21d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(75).std()
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def cast_523_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 122 capital access stress over 63d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(75).std()
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def cast_524_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 122 capital access stress over 126d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(75).std()
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def cast_525_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 122 capital access stress over 252d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(75).std()
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))
