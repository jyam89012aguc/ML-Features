# f11_raw_roc_family_base_001_075_gemini.py
import pandas as pd
import numpy as np

def _sma(s, w): return s.rolling(w, min_periods=min(w, 5)).mean()
def _ema(s, w): return s.ewm(span=w, min_periods=min(w, 5), adjust=False).mean()
def _raw_roc(price, w):
    return (price - price.shift(w)) / price.shift(w).abs().replace(0, np.nan)
def _log_roc(price, w):
    return np.log(price / price.shift(w).replace(0, np.nan))
def _roc_zscore(price, w, lookback):
    roc = (price - price.shift(w)) / price.shift(w).abs().replace(0, np.nan)
    return (roc - roc.rolling(lookback).mean()) / roc.rolling(lookback).std().replace(0, np.nan)

# Raw ROC for 1 day
def f11rf_f11_raw_roc_family_raw_roc_1d_base_v001_signal(close: pd.Series) -> pd.Series:
    """Calculates the 1-day Raw Rate of Change (ROC) using the close price.
    Formula: (price - price.shift(1)) / price.shift(1).abs()
    """
    res = _raw_roc(close, 1)
    return res.replace([np.inf, -np.inf], np.nan)

# Raw ROC for 2 days
def f11rf_f11_raw_roc_family_raw_roc_2d_base_v002_signal(close: pd.Series) -> pd.Series:
    """Calculates the 2-day Raw Rate of Change (ROC) using the close price.
    Formula: (price - price.shift(2)) / price.shift(2).abs()
    """
    res = _raw_roc(close, 2)
    return res.replace([np.inf, -np.inf], np.nan)

# Raw ROC for 3 days
def f11rf_f11_raw_roc_family_raw_roc_3d_base_v003_signal(close: pd.Series) -> pd.Series:
    """Calculates the 3-day Raw Rate of Change (ROC) using the close price.
    Formula: (price - price.shift(3)) / price.shift(3).abs()
    """
    res = _raw_roc(close, 3)
    return res.replace([np.inf, -np.inf], np.nan)

# Raw ROC for 5 days
def f11rf_f11_raw_roc_family_raw_roc_5d_base_v004_signal(close: pd.Series) -> pd.Series:
    """Calculates the 5-day Raw Rate of Change (ROC) using the close price.
    Formula: (price - price.shift(5)) / price.shift(5).abs()
    """
    res = _raw_roc(close, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Raw ROC for 10 days
def f11rf_f11_raw_roc_family_raw_roc_10d_base_v005_signal(close: pd.Series) -> pd.Series:
    """Calculates the 10-day Raw Rate of Change (ROC) using the close price.
    Formula: (price - price.shift(10)) / price.shift(10).abs()
    """
    res = _raw_roc(close, 10)
    return res.replace([np.inf, -np.inf], np.nan)

# Raw ROC for 21 days
def f11rf_f11_raw_roc_family_raw_roc_21d_base_v006_signal(close: pd.Series) -> pd.Series:
    """Calculates the 21-day Raw Rate of Change (ROC) using the close price.
    Formula: (price - price.shift(21)) / price.shift(21).abs()
    """
    res = _raw_roc(close, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Raw ROC for 42 days (using closeadj)
def f11rf_f11_raw_roc_family_raw_roc_42d_base_v007_signal(closeadj: pd.Series) -> pd.Series:
    """Calculates the 42-day Raw Rate of Change (ROC) using the adjusted close price.
    Formula: (price - price.shift(42)) / price.shift(42).abs()
    """
    res = _raw_roc(closeadj, 42)
    return res.replace([np.inf, -np.inf], np.nan)

# Raw ROC for 63 days (using closeadj)
def f11rf_f11_raw_roc_family_raw_roc_63d_base_v008_signal(closeadj: pd.Series) -> pd.Series:
    """Calculates the 63-day Raw Rate of Change (ROC) using the adjusted close price.
    Formula: (price - price.shift(63)) / price.shift(63).abs()
    """
    res = _raw_roc(closeadj, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Raw ROC for 126 days (using closeadj)
def f11rf_f11_raw_roc_family_raw_roc_126d_base_v009_signal(closeadj: pd.Series) -> pd.Series:
    """Calculates the 126-day Raw Rate of Change (ROC) using the adjusted close price.
    Formula: (price - price.shift(126)) / price.shift(126).abs()
    """
    res = _raw_roc(closeadj, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Raw ROC for 252 days (using closeadj)
def f11rf_f11_raw_roc_family_raw_roc_252d_base_v010_signal(closeadj: pd.Series) -> pd.Series:
    """Calculates the 252-day Raw Rate of Change (ROC) using the adjusted close price.
    Formula: (price - price.shift(252)) / price.shift(252).abs()
    """
    res = _raw_roc(closeadj, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Log ROC for 1 day
def f11rf_f11_raw_roc_family_log_roc_1d_base_v011_signal(close: pd.Series) -> pd.Series:
    """Calculates the 1-day Logarithmic Rate of Change (ROC) using the close price.
    Formula: ln(price / price.shift(1))
    """
    res = _log_roc(close, 1)
    return res.replace([np.inf, -np.inf], np.nan)

# Log ROC for 2 days
def f11rf_f11_raw_roc_family_log_roc_2d_base_v012_signal(close: pd.Series) -> pd.Series:
    """Calculates the 2-day Logarithmic Rate of Change (ROC) using the close price.
    Formula: ln(price / price.shift(2))
    """
    res = _log_roc(close, 2)
    return res.replace([np.inf, -np.inf], np.nan)

# Log ROC for 3 days
def f11rf_f11_raw_roc_family_log_roc_3d_base_v013_signal(close: pd.Series) -> pd.Series:
    """Calculates the 3-day Logarithmic Rate of Change (ROC) using the close price.
    Formula: ln(price / price.shift(3))
    """
    res = _log_roc(close, 3)
    return res.replace([np.inf, -np.inf], np.nan)

# Log ROC for 5 days
def f11rf_f11_raw_roc_family_log_roc_5d_base_v014_signal(close: pd.Series) -> pd.Series:
    """Calculates the 5-day Logarithmic Rate of Change (ROC) using the close price.
    Formula: ln(price / price.shift(5))
    """
    res = _log_roc(close, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Log ROC for 10 days
def f11rf_f11_raw_roc_family_log_roc_10d_base_v015_signal(close: pd.Series) -> pd.Series:
    """Calculates the 10-day Logarithmic Rate of Change (ROC) using the close price.
    Formula: ln(price / price.shift(10))
    """
    res = _log_roc(close, 10)
    return res.replace([np.inf, -np.inf], np.nan)

# Log ROC for 21 days
def f11rf_f11_raw_roc_family_log_roc_21d_base_v016_signal(close: pd.Series) -> pd.Series:
    """Calculates the 21-day Logarithmic Rate of Change (ROC) using the close price.
    Formula: ln(price / price.shift(21))
    """
    res = _log_roc(close, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Log ROC for 42 days (using closeadj)
def f11rf_f11_raw_roc_family_log_roc_42d_base_v017_signal(closeadj: pd.Series) -> pd.Series:
    """Calculates the 42-day Logarithmic Rate of Change (ROC) using the adjusted close price.
    Formula: ln(price / price.shift(42))
    """
    res = _log_roc(closeadj, 42)
    return res.replace([np.inf, -np.inf], np.nan)

# Log ROC for 63 days (using closeadj)
def f11rf_f11_raw_roc_family_log_roc_63d_base_v018_signal(closeadj: pd.Series) -> pd.Series:
    """Calculates the 63-day Logarithmic Rate of Change (ROC) using the adjusted close price.
    Formula: ln(price / price.shift(63))
    """
    res = _log_roc(closeadj, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Log ROC for 126 days (using closeadj)
def f11rf_f11_raw_roc_family_log_roc_126d_base_v019_signal(closeadj: pd.Series) -> pd.Series:
    """Calculates the 126-day Logarithmic Rate of Change (ROC) using the adjusted close price.
    Formula: ln(price / price.shift(126))
    """
    res = _log_roc(closeadj, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Log ROC for 252 days (using closeadj)
def f11rf_f11_raw_roc_family_log_roc_252d_base_v020_signal(closeadj: pd.Series) -> pd.Series:
    """Calculates the 252-day Logarithmic Rate of Change (ROC) using the adjusted close price.
    Formula: ln(price / price.shift(252))
    """
    res = _log_roc(closeadj, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Z-scored Raw ROC for 5 days with 21d lookback
def f11rf_f11_raw_roc_family_zscore_roc_5d_21l_base_v021_signal(close: pd.Series) -> pd.Series:
    """Calculates the z-score of the 5-day Raw ROC over a 21-day rolling window.
    Formula: (roc - mean(roc, 21)) / std(roc, 21)
    """
    res = _roc_zscore(close, 5, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Z-scored Raw ROC for 10 days with 63d lookback
def f11rf_f11_raw_roc_family_zscore_roc_10d_63l_base_v022_signal(close: pd.Series) -> pd.Series:
    """Calculates the z-score of the 10-day Raw ROC over a 63-day rolling window.
    Formula: (roc - mean(roc, 63)) / std(roc, 63)
    """
    res = _roc_zscore(close, 10, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Z-scored Raw ROC for 21 days with 126d lookback
def f11rf_f11_raw_roc_family_zscore_roc_21d_126l_base_v023_signal(close: pd.Series) -> pd.Series:
    """Calculates the z-score of the 21-day Raw ROC over a 126-day rolling window.
    Formula: (roc - mean(roc, 126)) / std(roc, 126)
    """
    res = _roc_zscore(close, 21, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Z-scored Raw ROC for 63 days with 252d lookback (using closeadj)
def f11rf_f11_raw_roc_family_zscore_roc_63d_252l_base_v024_signal(closeadj: pd.Series) -> pd.Series:
    """Calculates the z-score of the 63-day Raw ROC over a 252-day rolling window using adjusted close price.
    Formula: (roc - mean(roc, 252)) / std(roc, 252)
    """
    res = _roc_zscore(closeadj, 63, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Raw ROC of SMA 5
def f11rf_f11_raw_roc_family_raw_roc_sma5_5d_base_v025_signal(close: pd.Series) -> pd.Series:
    """Calculates the 5-day Raw ROC of the 5-day Simple Moving Average (SMA) of close price."""
    res = _raw_roc(_sma(close, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Raw ROC of SMA 10
def f11rf_f11_raw_roc_family_raw_roc_sma10_10d_base_v026_signal(close: pd.Series) -> pd.Series:
    """Calculates the 10-day Raw ROC of the 10-day Simple Moving Average (SMA) of close price."""
    res = _raw_roc(_sma(close, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

# Raw ROC of SMA 21
def f11rf_f11_raw_roc_family_raw_roc_sma21_21d_base_v027_signal(close: pd.Series) -> pd.Series:
    """Calculates the 21-day Raw ROC of the 21-day Simple Moving Average (SMA) of close price."""
    res = _raw_roc(_sma(close, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Raw ROC of SMA 63 (using closeadj)
def f11rf_f11_raw_roc_family_raw_roc_sma63_63d_base_v028_signal(closeadj: pd.Series) -> pd.Series:
    """Calculates the 63-day Raw ROC of the 63-day Simple Moving Average (SMA) of adjusted close price."""
    res = _raw_roc(_sma(closeadj, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Log ROC of EMA 5
def f11rf_f11_raw_roc_family_log_roc_ema5_5d_base_v029_signal(close: pd.Series) -> pd.Series:
    """Calculates the 5-day Log ROC of the 5-day Exponential Moving Average (EMA) of close price."""
    res = _log_roc(_ema(close, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Log ROC of EMA 10
def f11rf_f11_raw_roc_family_log_roc_ema10_10d_base_v030_signal(close: pd.Series) -> pd.Series:
    """Calculates the 10-day Log ROC of the 10-day Exponential Moving Average (EMA) of close price."""
    res = _log_roc(_ema(close, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

# Mean-reversion ROC: 5d Raw ROC minus its 21d SMA
def f11rf_f11_raw_roc_family_mr_roc_5d_21ma_base_v031_signal(close: pd.Series) -> pd.Series:
    """Calculates the difference between the 5-day Raw ROC and its 21-day SMA (mean-reversion indicator)."""
    roc = _raw_roc(close, 5)
    res = roc - _sma(roc, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Mean-reversion ROC: 10d Raw ROC minus its 42d SMA
def f11rf_f11_raw_roc_family_mr_roc_10d_42ma_base_v032_signal(close: pd.Series) -> pd.Series:
    """Calculates the difference between the 10-day Raw ROC and its 42-day SMA (mean-reversion indicator)."""
    roc = _raw_roc(close, 10)
    res = roc - _sma(roc, 42)
    return res.replace([np.inf, -np.inf], np.nan)

# Mean-reversion ROC: 21d Raw ROC minus its 63d SMA
def f11rf_f11_raw_roc_family_mr_roc_21d_63ma_base_v033_signal(close: pd.Series) -> pd.Series:
    """Calculates the difference between the 21-day Raw ROC and its 63-day SMA (mean-reversion indicator)."""
    roc = _raw_roc(close, 21)
    res = roc - _sma(roc, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Mean-reversion ROC: 63d Raw ROC minus its 126d SMA (using closeadj)
def f11rf_f11_raw_roc_family_mr_roc_63d_126ma_base_v034_signal(closeadj: pd.Series) -> pd.Series:
    """Calculates the difference between the 63-day Raw ROC and its 126-day SMA using adjusted close price."""
    roc = _raw_roc(closeadj, 63)
    res = roc - _sma(roc, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Raw ROC 1d z-score 252d
def f11rf_f11_raw_roc_family_raw_roc_1d_z252_base_v035_signal(close: pd.Series) -> pd.Series:
    """Calculates the z-score of the 1-day Raw ROC over a 252-day rolling window."""
    res = _roc_zscore(close, 1, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Raw ROC 2d z-score 252d
def f11rf_f11_raw_roc_family_raw_roc_2d_z252_base_v036_signal(close: pd.Series) -> pd.Series:
    """Calculates the z-score of the 2-day Raw ROC over a 252-day rolling window."""
    res = _roc_zscore(close, 2, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Raw ROC 3d z-score 252d
def f11rf_f11_raw_roc_family_raw_roc_3d_z252_base_v037_signal(close: pd.Series) -> pd.Series:
    """Calculates the z-score of the 3-day Raw ROC over a 252-day rolling window."""
    res = _roc_zscore(close, 3, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Raw ROC 5d z-score 252d
def f11rf_f11_raw_roc_family_raw_roc_5d_z252_base_v038_signal(close: pd.Series) -> pd.Series:
    """Calculates the z-score of the 5-day Raw ROC over a 252-day rolling window."""
    res = _roc_zscore(close, 5, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Raw ROC 10d z-score 252d
def f11rf_f11_raw_roc_family_raw_roc_10d_z252_base_v039_signal(close: pd.Series) -> pd.Series:
    """Calculates the z-score of the 10-day Raw ROC over a 252-day rolling window."""
    res = _roc_zscore(close, 10, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Raw ROC 21d z-score 252d
def f11rf_f11_raw_roc_family_raw_roc_21d_z252_base_v040_signal(close: pd.Series) -> pd.Series:
    """Calculates the z-score of the 21-day Raw ROC over a 252-day rolling window."""
    res = _roc_zscore(close, 21, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Raw ROC 42d z-score 252d (using closeadj)
def f11rf_f11_raw_roc_family_raw_roc_42d_z252_base_v041_signal(closeadj: pd.Series) -> pd.Series:
    """Calculates the z-score of the 42-day Raw ROC over a 252-day rolling window using adjusted close price."""
    res = _roc_zscore(closeadj, 42, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Raw ROC 63d z-score 252d (using closeadj)

# Raw ROC 126d z-score 252d (using closeadj)
def f11rf_f11_raw_roc_family_raw_roc_126d_z252_base_v043_signal(closeadj: pd.Series) -> pd.Series:
    """Calculates the z-score of the 126-day Raw ROC over a 252-day rolling window using adjusted close price."""
    res = _roc_zscore(closeadj, 126, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Log ROC 1d z-score 252d
def f11rf_f11_raw_roc_family_log_roc_1d_z252_base_v044_signal(close: pd.Series) -> pd.Series:
    """Calculates the z-score of the 1-day Log ROC over a 252-day rolling window."""
    roc = _log_roc(close, 1)
    res = (roc - roc.rolling(252).mean()) / roc.rolling(252).std().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Log ROC 5d z-score 252d
def f11rf_f11_raw_roc_family_log_roc_5d_z252_base_v045_signal(close: pd.Series) -> pd.Series:
    """Calculates the z-score of the 5-day Log ROC over a 252-day rolling window."""
    roc = _log_roc(close, 5)
    res = (roc - roc.rolling(252).mean()) / roc.rolling(252).std().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Log ROC 21d z-score 252d
def f11rf_f11_raw_roc_family_log_roc_21d_z252_base_v046_signal(close: pd.Series) -> pd.Series:
    """Calculates the z-score of the 21-day Log ROC over a 252-day rolling window."""
    roc = _log_roc(close, 21)
    res = (roc - roc.rolling(252).mean()) / roc.rolling(252).std().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Log ROC 63d z-score 252d (using closeadj)
def f11rf_f11_raw_roc_family_log_roc_63d_z252_base_v047_signal(closeadj: pd.Series) -> pd.Series:
    """Calculates the z-score of the 63-day Log ROC over a 252-day rolling window using adjusted close price."""
    roc = _log_roc(closeadj, 63)
    res = (roc - roc.rolling(252).mean()) / roc.rolling(252).std().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Ratio of 5d ROC to 21d ROC
def f11rf_f11_raw_roc_family_roc_ratio_5d_21d_base_v048_signal(close: pd.Series) -> pd.Series:
    """Calculates the ratio of the 5-day Raw ROC to the 21-day Raw ROC."""
    res = _raw_roc(close, 5) / _raw_roc(close, 21).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Ratio of 21d ROC to 63d ROC
def f11rf_f11_raw_roc_family_roc_ratio_21d_63d_base_v049_signal(closeadj: pd.Series) -> pd.Series:
    """Calculates the ratio of the 21-day Raw ROC to the 63-day Raw ROC using adjusted close price."""
    res = _raw_roc(closeadj, 21) / _raw_roc(closeadj, 63).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Difference between 5d Raw ROC and 5d Log ROC
def f11rf_f11_raw_roc_family_roc_diff_raw_log_5d_base_v050_signal(close: pd.Series) -> pd.Series:
    """Calculates the difference between 5-day Raw ROC and 5-day Log ROC."""
    res = _raw_roc(close, 5) - _log_roc(close, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Difference between 21d Raw ROC and 21d Log ROC
def f11rf_f11_raw_roc_family_roc_diff_raw_log_21d_base_v051_signal(close: pd.Series) -> pd.Series:
    """Calculates the difference between 21-day Raw ROC and 21-day Log ROC."""
    res = _raw_roc(close, 21) - _log_roc(close, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Raw ROC of Volume 5d
def f11rf_f11_raw_roc_family_volume_roc_5d_base_v052_signal(volume: pd.Series) -> pd.Series:
    """Calculates the 5-day Raw ROC of the volume series."""
    res = _raw_roc(volume, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Raw ROC of Volume 21d
def f11rf_f11_raw_roc_family_volume_roc_21d_base_v053_signal(volume: pd.Series) -> pd.Series:
    """Calculates the 21-day Raw ROC of the volume series."""
    res = _raw_roc(volume, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Raw ROC of ATR 21d
def f11rf_f11_raw_roc_family_atr_roc_21d_base_v054_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Calculates the 21-day Raw ROC of the 21-day ATR."""
    tr = pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1)
    atr = _sma(tr, 21)
    res = _raw_roc(atr, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Raw ROC of SMA 252 (using closeadj)
def f11rf_f11_raw_roc_family_raw_roc_sma252_252d_base_v055_signal(closeadj: pd.Series) -> pd.Series:
    """Calculates the 252-day Raw ROC of the 252-day SMA using adjusted close price."""
    res = _raw_roc(_sma(closeadj, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Log ROC of SMA 252 (using closeadj)
def f11rf_f11_raw_roc_family_log_roc_sma252_252d_base_v056_signal(closeadj: pd.Series) -> pd.Series:
    """Calculates the 252-day Log ROC of the 252-day SMA using adjusted close price."""
    res = _log_roc(_sma(closeadj, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Raw ROC 5d of High
def f11rf_f11_raw_roc_family_high_roc_5d_base_v057_signal(high: pd.Series) -> pd.Series:
    """Calculates the 5-day Raw ROC of the high price."""
    res = _raw_roc(high, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Raw ROC 5d of Low
def f11rf_f11_raw_roc_family_low_roc_5d_base_v058_signal(low: pd.Series) -> pd.Series:
    """Calculates the 5-day Raw ROC of the low price."""
    res = _raw_roc(low, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Raw ROC 21d of High
def f11rf_f11_raw_roc_family_high_roc_21d_base_v059_signal(high: pd.Series) -> pd.Series:
    """Calculates the 21-day Raw ROC of the high price."""
    res = _raw_roc(high, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Raw ROC 21d of Low
def f11rf_f11_raw_roc_family_low_roc_21d_base_v060_signal(low: pd.Series) -> pd.Series:
    """Calculates the 21-day Raw ROC of the low price."""
    res = _raw_roc(low, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Raw ROC 63d of High (using closeadj-adjusted high)
def f11rf_f11_raw_roc_family_high_roc_63d_base_v061_signal(high: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Calculates the 63-day Raw ROC of the high price adjusted by the close adjustment factor."""
    adj = closeadj / close.replace(0, np.nan)
    res = _raw_roc(high * adj, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Raw ROC 63d of Low (using closeadj-adjusted low)
def f11rf_f11_raw_roc_family_low_roc_63d_base_v062_signal(low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Calculates the 63-day Raw ROC of the low price adjusted by the close adjustment factor."""
    adj = closeadj / close.replace(0, np.nan)
    res = _raw_roc(low * adj, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Z-scored Raw ROC 5d of Volume
def f11rf_f11_raw_roc_family_volume_roc_zscore_5d_base_v063_signal(volume: pd.Series) -> pd.Series:
    """Calculates the z-score of the 5-day Raw ROC of volume over a 63-day window."""
    res = _roc_zscore(volume, 5, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Z-scored Raw ROC 21d of Volume
def f11rf_f11_raw_roc_family_volume_roc_zscore_21d_base_v064_signal(volume: pd.Series) -> pd.Series:
    """Calculates the z-score of the 21-day Raw ROC of volume over a 63-day window."""
    res = _roc_zscore(volume, 21, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Raw ROC of (High+Low)/2 5d
def f11rf_f11_raw_roc_family_hl2_roc_5d_base_v065_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    """Calculates the 5-day Raw ROC of the median price (H+L)/2."""
    res = _raw_roc((high + low) / 2, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Raw ROC of (High+Low)/2 21d
def f11rf_f11_raw_roc_family_hl2_roc_21d_base_v066_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    """Calculates the 21-day Raw ROC of the median price (H+L)/2."""
    res = _raw_roc((high + low) / 2, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Raw ROC of (High+Low)/2 63d (using closeadj-adjusted)
def f11rf_f11_raw_roc_family_hl2_roc_63d_base_v067_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Calculates the 63-day Raw ROC of the median price (H+L)/2 using adjusted price components."""
    adj = closeadj / close.replace(0, np.nan)
    res = _raw_roc((high * adj + low * adj) / 2, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Raw ROC of 5d SMA of Volume
def f11rf_f11_raw_roc_family_volume_sma5_roc_5d_base_v068_signal(volume: pd.Series) -> pd.Series:
    """Calculates the 5-day Raw ROC of the 5-day SMA of volume."""
    res = _raw_roc(_sma(volume, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Raw ROC of 21d SMA of Volume
def f11rf_f11_raw_roc_family_volume_sma21_roc_21d_base_v069_signal(volume: pd.Series) -> pd.Series:
    """Calculates the 21-day Raw ROC of the 21-day SMA of volume."""
    res = _raw_roc(_sma(volume, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Raw ROC of 10d EMA of Price
def f11rf_f11_raw_roc_family_price_ema10_roc_10d_base_v070_signal(close: pd.Series) -> pd.Series:
    """Calculates the 10-day Raw ROC of the 10-day EMA of close price."""
    res = _raw_roc(_ema(close, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

# Raw ROC of 42d EMA of Price (using closeadj)
def f11rf_f11_raw_roc_family_price_ema42_roc_42d_base_v071_signal(closeadj: pd.Series) -> pd.Series:
    """Calculates the 42-day Raw ROC of the 42-day EMA of adjusted close price."""
    res = _raw_roc(_ema(closeadj, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

# Cumulative Raw ROC: sum of 1d ROC over 5 days
def f11rf_f11_raw_roc_family_cum_roc_1d_5d_base_v072_signal(close: pd.Series) -> pd.Series:
    """Calculates the cumulative 1-day Raw ROC over a 5-day rolling window."""
    res = _raw_roc(close, 1).rolling(5).sum()
    return res.replace([np.inf, -np.inf], np.nan)

# Cumulative Raw ROC: sum of 1d ROC over 21 days
def f11rf_f11_raw_roc_family_cum_roc_1d_21d_base_v073_signal(close: pd.Series) -> pd.Series:
    """Calculates the cumulative 1-day Raw ROC over a 21-day rolling window."""
    res = _raw_roc(close, 1).rolling(21).sum()
    return res.replace([np.inf, -np.inf], np.nan)

# Cumulative Log ROC: sum of 1d Log ROC over 5 days
def f11rf_f11_raw_roc_family_cum_log_roc_1d_5d_base_v074_signal(close: pd.Series) -> pd.Series:
    """Calculates the cumulative 1-day Log ROC over a 5-day rolling window."""
    res = _log_roc(close, 1).rolling(5).sum()
    return res.replace([np.inf, -np.inf], np.nan)

# Cumulative Log ROC: sum of 1d Log ROC over 21 days
def f11rf_f11_raw_roc_family_cum_log_roc_1d_21d_base_v075_signal(close: pd.Series) -> pd.Series:
    """Calculates the cumulative 1-day Log ROC over a 21-day rolling window."""
    res = _log_roc(close, 1).rolling(21).sum()
    return res.replace([np.inf, -np.inf], np.nan)


SILVERDB_ACCESS, SOURCE_TABLE, ENTITY_COLUMN, DATE_COLUMN = "read_only", "sep", "ticker", "date"
ORDER_BY, NO_FORWARD_LOOKING = [ENTITY_COLUMN, DATE_COLUMN], True
SOURCE_COLUMNS = {c: f"sep.{c}" for c in ["close", "closeadj", "high", "low", "volume"]}

BASE_NAMES = [f for f in globals() if f.startswith("f11rf_") and f.endswith("_signal")]

F11_RAW_ROC_FAMILY_BASE_REGISTRY_001_075 = {
    n: {
        "inputs": (inputs := [v for v in globals()[n].__code__.co_varnames[:globals()[n].__code__.co_argcount]]),
        "source_table": SOURCE_TABLE,
        "source_columns": {c: SOURCE_COLUMNS[c] for c in inputs if c in SOURCE_COLUMNS},
        "entity_column": ENTITY_COLUMN, "date_column": DATE_COLUMN,
        "order_by": ORDER_BY, "no_forward_looking": NO_FORWARD_LOOKING, "func": globals()[n]
    } for n in sorted(BASE_NAMES)
}

if __name__ == "__main__":
    import pandas as pd; import numpy as np
    sz = 500; d = pd.DataFrame({"close": np.random.randn(sz).cumsum()+100, "closeadj": np.random.randn(sz).cumsum()+100, "high": np.random.randn(sz).cumsum()+110, "low": np.random.randn(sz).cumsum()+90, "volume": np.random.randn(sz).cumsum()+1000, "ticker": ["T"]*sz, "date": pd.date_range("2020-01-01", periods=sz)})
    for n, c in F11_RAW_ROC_FAMILY_BASE_REGISTRY_001_075.items():
        r = c["func"](**{i: d[i] for i in c["inputs"]})
        assert isinstance(r, pd.Series)
    print("base 001-075 OK")
