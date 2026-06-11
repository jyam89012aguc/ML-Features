"""
118_118_drawdown_recovery_asymmetry — Base Features 001-075
Domain: 118_drawdown_recovery_asymmetry
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

def dras_001_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 118 drawdown recovery asymmetry over a 5d horizon to identify extreme regimes.
    """
    base = (close / close.rolling(252).max() - 1).abs() / (close / close.rolling(252).min() - 1).abs()
    return _rolling_mean(base, 5)

def dras_002_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 118 drawdown recovery asymmetry over a 21d horizon to identify extreme regimes.
    """
    base = (close / close.rolling(252).max() - 1).abs() / (close / close.rolling(252).min() - 1).abs()
    return _rolling_mean(base, 21)

def dras_003_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 118 drawdown recovery asymmetry over a 63d horizon to identify extreme regimes.
    """
    base = (close / close.rolling(252).max() - 1).abs() / (close / close.rolling(252).min() - 1).abs()
    return _rolling_mean(base, 63)

def dras_004_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 118 drawdown recovery asymmetry over a 126d horizon to identify extreme regimes.
    """
    base = (close / close.rolling(252).max() - 1).abs() / (close / close.rolling(252).min() - 1).abs()
    return _rolling_mean(base, 126)

def dras_005_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 118 drawdown recovery asymmetry over a 252d horizon to identify extreme regimes.
    """
    base = (close / close.rolling(252).max() - 1).abs() / (close / close.rolling(252).min() - 1).abs()
    return _rolling_mean(base, 252)

def dras_006_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 118 drawdown recovery asymmetry by measuring deviations from the 5d mean.
    """
    base = (close / close.rolling(252).max() - 1).abs() / (close / close.rolling(252).min() - 1).abs()
    return _zscore_rolling(base, 5)

def dras_007_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 118 drawdown recovery asymmetry by measuring deviations from the 21d mean.
    """
    base = (close / close.rolling(252).max() - 1).abs() / (close / close.rolling(252).min() - 1).abs()
    return _zscore_rolling(base, 21)

def dras_008_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 118 drawdown recovery asymmetry by measuring deviations from the 63d mean.
    """
    base = (close / close.rolling(252).max() - 1).abs() / (close / close.rolling(252).min() - 1).abs()
    return _zscore_rolling(base, 63)

def dras_009_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 118 drawdown recovery asymmetry by measuring deviations from the 126d mean.
    """
    base = (close / close.rolling(252).max() - 1).abs() / (close / close.rolling(252).min() - 1).abs()
    return _zscore_rolling(base, 126)

def dras_010_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 118 drawdown recovery asymmetry by measuring deviations from the 252d mean.
    """
    base = (close / close.rolling(252).max() - 1).abs() / (close / close.rolling(252).min() - 1).abs()
    return _zscore_rolling(base, 252)

def dras_011_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 118 drawdown recovery asymmetry to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = (close / close.rolling(252).max() - 1).abs() / (close / close.rolling(252).min() - 1).abs()
    return _rank_pct(base, 5)

def dras_012_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 118 drawdown recovery asymmetry to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = (close / close.rolling(252).max() - 1).abs() / (close / close.rolling(252).min() - 1).abs()
    return _rank_pct(base, 21)

def dras_013_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 118 drawdown recovery asymmetry to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = (close / close.rolling(252).max() - 1).abs() / (close / close.rolling(252).min() - 1).abs()
    return _rank_pct(base, 63)

def dras_014_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 118 drawdown recovery asymmetry to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = (close / close.rolling(252).max() - 1).abs() / (close / close.rolling(252).min() - 1).abs()
    return _rank_pct(base, 126)

def dras_015_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 118 drawdown recovery asymmetry to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = (close / close.rolling(252).max() - 1).abs() / (close / close.rolling(252).min() - 1).abs()
    return _rank_pct(base, 252)

def dras_016_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 118 drawdown recovery asymmetry distribution over 5d to detect tail risk or exhaustion.
    """
    base = (close / close.rolling(252).max() - 1).abs() / (close / close.rolling(252).min() - 1).abs()
    return _rolling_skew(base, 5)

def dras_017_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 118 drawdown recovery asymmetry distribution over 21d to detect tail risk or exhaustion.
    """
    base = (close / close.rolling(252).max() - 1).abs() / (close / close.rolling(252).min() - 1).abs()
    return _rolling_skew(base, 21)

def dras_018_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 118 drawdown recovery asymmetry distribution over 63d to detect tail risk or exhaustion.
    """
    base = (close / close.rolling(252).max() - 1).abs() / (close / close.rolling(252).min() - 1).abs()
    return _rolling_skew(base, 63)

def dras_019_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 118 drawdown recovery asymmetry distribution over 126d to detect tail risk or exhaustion.
    """
    base = (close / close.rolling(252).max() - 1).abs() / (close / close.rolling(252).min() - 1).abs()
    return _rolling_skew(base, 126)

def dras_020_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 118 drawdown recovery asymmetry distribution over 252d to detect tail risk or exhaustion.
    """
    base = (close / close.rolling(252).max() - 1).abs() / (close / close.rolling(252).min() - 1).abs()
    return _rolling_skew(base, 252)

def dras_021_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 118 drawdown recovery asymmetry over 5d to capture explosive breakdown or reversal points.
    """
    base = (close / close.rolling(252).max() - 1).abs() / (close / close.rolling(252).min() - 1).abs()
    return _rolling_kurt(base, 5)

def dras_022_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 118 drawdown recovery asymmetry over 21d to capture explosive breakdown or reversal points.
    """
    base = (close / close.rolling(252).max() - 1).abs() / (close / close.rolling(252).min() - 1).abs()
    return _rolling_kurt(base, 21)

def dras_023_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 118 drawdown recovery asymmetry over 63d to capture explosive breakdown or reversal points.
    """
    base = (close / close.rolling(252).max() - 1).abs() / (close / close.rolling(252).min() - 1).abs()
    return _rolling_kurt(base, 63)

def dras_024_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 118 drawdown recovery asymmetry over 126d to capture explosive breakdown or reversal points.
    """
    base = (close / close.rolling(252).max() - 1).abs() / (close / close.rolling(252).min() - 1).abs()
    return _rolling_kurt(base, 126)

def dras_025_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 118 drawdown recovery asymmetry over 252d to capture explosive breakdown or reversal points.
    """
    base = (close / close.rolling(252).max() - 1).abs() / (close / close.rolling(252).min() - 1).abs()
    return _rolling_kurt(base, 252)

def dras_026_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 118 drawdown recovery asymmetry for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = (close / close.rolling(252).max() - 1).abs() / (close / close.rolling(252).min() - 1).abs()
    return _safe_div(base, _rolling_std(base, 5))

def dras_027_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 118 drawdown recovery asymmetry for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = (close / close.rolling(252).max() - 1).abs() / (close / close.rolling(252).min() - 1).abs()
    return _safe_div(base, _rolling_std(base, 21))

def dras_028_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 118 drawdown recovery asymmetry for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = (close / close.rolling(252).max() - 1).abs() / (close / close.rolling(252).min() - 1).abs()
    return _safe_div(base, _rolling_std(base, 63))

def dras_029_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 118 drawdown recovery asymmetry for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = (close / close.rolling(252).max() - 1).abs() / (close / close.rolling(252).min() - 1).abs()
    return _safe_div(base, _rolling_std(base, 126))

def dras_030_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 118 drawdown recovery asymmetry for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = (close / close.rolling(252).max() - 1).abs() / (close / close.rolling(252).min() - 1).abs()
    return _safe_div(base, _rolling_std(base, 252))

def dras_031_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 118 drawdown recovery asymmetry over 5d to stabilize variance and capture exponential shifts.
    """
    base = (close / close.rolling(252).max() - 1).abs() / (close / close.rolling(252).min() - 1).abs()
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def dras_032_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 118 drawdown recovery asymmetry over 21d to stabilize variance and capture exponential shifts.
    """
    base = (close / close.rolling(252).max() - 1).abs() / (close / close.rolling(252).min() - 1).abs()
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def dras_033_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 118 drawdown recovery asymmetry over 63d to stabilize variance and capture exponential shifts.
    """
    base = (close / close.rolling(252).max() - 1).abs() / (close / close.rolling(252).min() - 1).abs()
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def dras_034_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 118 drawdown recovery asymmetry over 126d to stabilize variance and capture exponential shifts.
    """
    base = (close / close.rolling(252).max() - 1).abs() / (close / close.rolling(252).min() - 1).abs()
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def dras_035_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 118 drawdown recovery asymmetry over 252d to stabilize variance and capture exponential shifts.
    """
    base = (close / close.rolling(252).max() - 1).abs() / (close / close.rolling(252).min() - 1).abs()
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def dras_036_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 118 drawdown recovery asymmetry over a 5d horizon to identify extreme regimes.
    """
    base = close.diff().clip(lower=0).rolling(21).sum() / close.diff().clip(upper=0).abs().rolling(21).sum()
    return _rolling_mean(base, 5)

def dras_037_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 118 drawdown recovery asymmetry over a 21d horizon to identify extreme regimes.
    """
    base = close.diff().clip(lower=0).rolling(21).sum() / close.diff().clip(upper=0).abs().rolling(21).sum()
    return _rolling_mean(base, 21)

def dras_038_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 118 drawdown recovery asymmetry over a 63d horizon to identify extreme regimes.
    """
    base = close.diff().clip(lower=0).rolling(21).sum() / close.diff().clip(upper=0).abs().rolling(21).sum()
    return _rolling_mean(base, 63)

def dras_039_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 118 drawdown recovery asymmetry over a 126d horizon to identify extreme regimes.
    """
    base = close.diff().clip(lower=0).rolling(21).sum() / close.diff().clip(upper=0).abs().rolling(21).sum()
    return _rolling_mean(base, 126)

def dras_040_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 118 drawdown recovery asymmetry over a 252d horizon to identify extreme regimes.
    """
    base = close.diff().clip(lower=0).rolling(21).sum() / close.diff().clip(upper=0).abs().rolling(21).sum()
    return _rolling_mean(base, 252)

def dras_041_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 118 drawdown recovery asymmetry by measuring deviations from the 5d mean.
    """
    base = close.diff().clip(lower=0).rolling(21).sum() / close.diff().clip(upper=0).abs().rolling(21).sum()
    return _zscore_rolling(base, 5)

def dras_042_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 118 drawdown recovery asymmetry by measuring deviations from the 21d mean.
    """
    base = close.diff().clip(lower=0).rolling(21).sum() / close.diff().clip(upper=0).abs().rolling(21).sum()
    return _zscore_rolling(base, 21)

def dras_043_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 118 drawdown recovery asymmetry by measuring deviations from the 63d mean.
    """
    base = close.diff().clip(lower=0).rolling(21).sum() / close.diff().clip(upper=0).abs().rolling(21).sum()
    return _zscore_rolling(base, 63)

def dras_044_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 118 drawdown recovery asymmetry by measuring deviations from the 126d mean.
    """
    base = close.diff().clip(lower=0).rolling(21).sum() / close.diff().clip(upper=0).abs().rolling(21).sum()
    return _zscore_rolling(base, 126)

def dras_045_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 118 drawdown recovery asymmetry by measuring deviations from the 252d mean.
    """
    base = close.diff().clip(lower=0).rolling(21).sum() / close.diff().clip(upper=0).abs().rolling(21).sum()
    return _zscore_rolling(base, 252)

def dras_046_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 118 drawdown recovery asymmetry to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = close.diff().clip(lower=0).rolling(21).sum() / close.diff().clip(upper=0).abs().rolling(21).sum()
    return _rank_pct(base, 5)

def dras_047_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 118 drawdown recovery asymmetry to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = close.diff().clip(lower=0).rolling(21).sum() / close.diff().clip(upper=0).abs().rolling(21).sum()
    return _rank_pct(base, 21)

def dras_048_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 118 drawdown recovery asymmetry to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = close.diff().clip(lower=0).rolling(21).sum() / close.diff().clip(upper=0).abs().rolling(21).sum()
    return _rank_pct(base, 63)

def dras_049_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 118 drawdown recovery asymmetry to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = close.diff().clip(lower=0).rolling(21).sum() / close.diff().clip(upper=0).abs().rolling(21).sum()
    return _rank_pct(base, 126)

def dras_050_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 118 drawdown recovery asymmetry to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = close.diff().clip(lower=0).rolling(21).sum() / close.diff().clip(upper=0).abs().rolling(21).sum()
    return _rank_pct(base, 252)

def dras_051_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 118 drawdown recovery asymmetry distribution over 5d to detect tail risk or exhaustion.
    """
    base = close.diff().clip(lower=0).rolling(21).sum() / close.diff().clip(upper=0).abs().rolling(21).sum()
    return _rolling_skew(base, 5)

def dras_052_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 118 drawdown recovery asymmetry distribution over 21d to detect tail risk or exhaustion.
    """
    base = close.diff().clip(lower=0).rolling(21).sum() / close.diff().clip(upper=0).abs().rolling(21).sum()
    return _rolling_skew(base, 21)

def dras_053_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 118 drawdown recovery asymmetry distribution over 63d to detect tail risk or exhaustion.
    """
    base = close.diff().clip(lower=0).rolling(21).sum() / close.diff().clip(upper=0).abs().rolling(21).sum()
    return _rolling_skew(base, 63)

def dras_054_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 118 drawdown recovery asymmetry distribution over 126d to detect tail risk or exhaustion.
    """
    base = close.diff().clip(lower=0).rolling(21).sum() / close.diff().clip(upper=0).abs().rolling(21).sum()
    return _rolling_skew(base, 126)

def dras_055_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 118 drawdown recovery asymmetry distribution over 252d to detect tail risk or exhaustion.
    """
    base = close.diff().clip(lower=0).rolling(21).sum() / close.diff().clip(upper=0).abs().rolling(21).sum()
    return _rolling_skew(base, 252)

def dras_056_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 118 drawdown recovery asymmetry over 5d to capture explosive breakdown or reversal points.
    """
    base = close.diff().clip(lower=0).rolling(21).sum() / close.diff().clip(upper=0).abs().rolling(21).sum()
    return _rolling_kurt(base, 5)

def dras_057_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 118 drawdown recovery asymmetry over 21d to capture explosive breakdown or reversal points.
    """
    base = close.diff().clip(lower=0).rolling(21).sum() / close.diff().clip(upper=0).abs().rolling(21).sum()
    return _rolling_kurt(base, 21)

def dras_058_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 118 drawdown recovery asymmetry over 63d to capture explosive breakdown or reversal points.
    """
    base = close.diff().clip(lower=0).rolling(21).sum() / close.diff().clip(upper=0).abs().rolling(21).sum()
    return _rolling_kurt(base, 63)

def dras_059_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 118 drawdown recovery asymmetry over 126d to capture explosive breakdown or reversal points.
    """
    base = close.diff().clip(lower=0).rolling(21).sum() / close.diff().clip(upper=0).abs().rolling(21).sum()
    return _rolling_kurt(base, 126)

def dras_060_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 118 drawdown recovery asymmetry over 252d to capture explosive breakdown or reversal points.
    """
    base = close.diff().clip(lower=0).rolling(21).sum() / close.diff().clip(upper=0).abs().rolling(21).sum()
    return _rolling_kurt(base, 252)

def dras_061_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 118 drawdown recovery asymmetry for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = close.diff().clip(lower=0).rolling(21).sum() / close.diff().clip(upper=0).abs().rolling(21).sum()
    return _safe_div(base, _rolling_std(base, 5))

def dras_062_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 118 drawdown recovery asymmetry for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = close.diff().clip(lower=0).rolling(21).sum() / close.diff().clip(upper=0).abs().rolling(21).sum()
    return _safe_div(base, _rolling_std(base, 21))

def dras_063_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 118 drawdown recovery asymmetry for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = close.diff().clip(lower=0).rolling(21).sum() / close.diff().clip(upper=0).abs().rolling(21).sum()
    return _safe_div(base, _rolling_std(base, 63))

def dras_064_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 118 drawdown recovery asymmetry for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = close.diff().clip(lower=0).rolling(21).sum() / close.diff().clip(upper=0).abs().rolling(21).sum()
    return _safe_div(base, _rolling_std(base, 126))

def dras_065_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 118 drawdown recovery asymmetry for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = close.diff().clip(lower=0).rolling(21).sum() / close.diff().clip(upper=0).abs().rolling(21).sum()
    return _safe_div(base, _rolling_std(base, 252))

def dras_066_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 118 drawdown recovery asymmetry over 5d to stabilize variance and capture exponential shifts.
    """
    base = close.diff().clip(lower=0).rolling(21).sum() / close.diff().clip(upper=0).abs().rolling(21).sum()
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def dras_067_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 118 drawdown recovery asymmetry over 21d to stabilize variance and capture exponential shifts.
    """
    base = close.diff().clip(lower=0).rolling(21).sum() / close.diff().clip(upper=0).abs().rolling(21).sum()
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def dras_068_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 118 drawdown recovery asymmetry over 63d to stabilize variance and capture exponential shifts.
    """
    base = close.diff().clip(lower=0).rolling(21).sum() / close.diff().clip(upper=0).abs().rolling(21).sum()
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def dras_069_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 118 drawdown recovery asymmetry over 126d to stabilize variance and capture exponential shifts.
    """
    base = close.diff().clip(lower=0).rolling(21).sum() / close.diff().clip(upper=0).abs().rolling(21).sum()
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def dras_070_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 118 drawdown recovery asymmetry over 252d to stabilize variance and capture exponential shifts.
    """
    base = close.diff().clip(lower=0).rolling(21).sum() / close.diff().clip(upper=0).abs().rolling(21).sum()
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def dras_071_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 118 drawdown recovery asymmetry over a 5d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(21).skew()
    return _rolling_mean(base, 5)

def dras_072_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 118 drawdown recovery asymmetry over a 21d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(21).skew()
    return _rolling_mean(base, 21)

def dras_073_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 118 drawdown recovery asymmetry over a 63d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(21).skew()
    return _rolling_mean(base, 63)

def dras_074_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 118 drawdown recovery asymmetry over a 126d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(21).skew()
    return _rolling_mean(base, 126)

def dras_075_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 118 drawdown recovery asymmetry over a 252d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(21).skew()
    return _rolling_mean(base, 252)
