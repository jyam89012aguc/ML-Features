# f23_on_balance_volume_family_base_001_075_gemini.py
import pandas as pd
import numpy as np

def _sma(s, w):
    """Simple Moving Average"""
    return s.rolling(w, min_periods=min(w, 5)).mean()

def _ema(s, w):
    """Exponential Moving Average"""
    return s.ewm(span=w, min_periods=min(w, 5), adjust=False).mean()

def _obv_calc(c, v):
    """On-Balance Volume Calculation"""
    return (v * np.sign(c.diff().fillna(0))).cumsum()

def _obv_zscore(obv, w):
    """OBV Z-Score relative to its rolling window"""
    return (obv - obv.rolling(w).mean()) / obv.rolling(w).std().replace(0, np.nan)

def _obv_rel_dist(obv, w):
    """OBV relative distance to its moving average"""
    ma = obv.rolling(w).mean()
    return (obv - ma) / ma.abs().replace(0, np.nan)

# --- Features 001 - 010: Standard OBV and simple variations ---

def f23obv_f23_on_balance_volume_family_standard_obv_v001_signal(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Standard On-Balance Volume (OBV) feature."""
    res = _obv_calc(close, volume)
    return res.replace([np.inf, -np.inf], np.nan)

def f23obv_f23_on_balance_volume_family_obv_sma_5d_v002_signal(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Standard OBV smoothed with a 5-day SMA."""
    obv = _obv_calc(close, volume)
    res = _sma(obv, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f23obv_f23_on_balance_volume_family_obv_ema_5d_v003_signal(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Standard OBV smoothed with a 5-day EMA."""
    obv = _obv_calc(close, volume)
    res = _ema(obv, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f23obv_f23_on_balance_volume_family_obv_sma_10d_v004_signal(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Standard OBV smoothed with a 10-day SMA."""
    obv = _obv_calc(close, volume)
    res = _sma(obv, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f23obv_f23_on_balance_volume_family_obv_ema_10d_v005_signal(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Standard OBV smoothed with a 10-day EMA."""
    obv = _obv_calc(close, volume)
    res = _ema(obv, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f23obv_f23_on_balance_volume_family_obv_sma_21d_v006_signal(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Standard OBV smoothed with a 21-day SMA."""
    obv = _obv_calc(close, volume)
    res = _sma(obv, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f23obv_f23_on_balance_volume_family_obv_ema_21d_v007_signal(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Standard OBV smoothed with a 21-day EMA."""
    obv = _obv_calc(close, volume)
    res = _ema(obv, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f23obv_f23_on_balance_volume_family_obv_adj_sma_63d_v008_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    """Standard OBV using closeadj smoothed with a 63-day SMA."""
    obv = _obv_calc(closeadj, volume)
    res = _sma(obv, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f23obv_f23_on_balance_volume_family_obv_adj_ema_63d_v009_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    """Standard OBV using closeadj smoothed with a 63-day EMA."""
    obv = _obv_calc(closeadj, volume)
    res = _ema(obv, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f23obv_f23_on_balance_volume_family_obv_adj_sma_126d_v010_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    """Standard OBV using closeadj smoothed with a 126-day SMA."""
    obv = _obv_calc(closeadj, volume)
    res = _sma(obv, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# --- Features 011 - 020: OBV Z-Scores ---

def f23obv_f23_on_balance_volume_family_obv_zscore_5d_v011_signal(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OBV Z-score over a 5-day window."""
    obv = _obv_calc(close, volume)
    res = _obv_zscore(obv, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f23obv_f23_on_balance_volume_family_obv_zscore_10d_v012_signal(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OBV Z-score over a 10-day window."""
    obv = _obv_calc(close, volume)
    res = _obv_zscore(obv, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f23obv_f23_on_balance_volume_family_obv_zscore_21d_v013_signal(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OBV Z-score over a 21-day window."""
    obv = _obv_calc(close, volume)
    res = _obv_zscore(obv, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f23obv_f23_on_balance_volume_family_obv_adj_zscore_63d_v014_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    """OBV Z-score using closeadj over a 63-day window."""
    obv = _obv_calc(closeadj, volume)
    res = _obv_zscore(obv, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f23obv_f23_on_balance_volume_family_obv_adj_zscore_126d_v015_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    """OBV Z-score using closeadj over a 126-day window."""
    obv = _obv_calc(closeadj, volume)
    res = _obv_zscore(obv, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f23obv_f23_on_balance_volume_family_obv_adj_zscore_252d_v016_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    """OBV Z-score using closeadj over a 252-day window."""
    obv = _obv_calc(closeadj, volume)
    res = _obv_zscore(obv, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f23obv_f23_on_balance_volume_family_obv_zscore_ema_21d_v017_signal(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of OBV smoothed with a 21-day EMA."""
    obv = _ema(_obv_calc(close, volume), 21)
    res = _obv_zscore(obv, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f23obv_f23_on_balance_volume_family_obv_adj_zscore_ema_63d_v018_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of OBV using closeadj smoothed with a 63-day EMA."""
    obv = _ema(_obv_calc(closeadj, volume), 63)
    res = _obv_zscore(obv, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f23obv_f23_on_balance_volume_family_obv_adj_zscore_sma_126d_v019_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of OBV using closeadj smoothed with a 126-day SMA."""
    obv = _sma(_obv_calc(closeadj, volume), 126)
    res = _obv_zscore(obv, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f23obv_f23_on_balance_volume_family_obv_adj_zscore_sma_252d_v020_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of OBV using closeadj smoothed with a 252-day SMA."""
    obv = _sma(_obv_calc(closeadj, volume), 252)
    res = _obv_zscore(obv, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# --- Features 021 - 030: OBV Relative Distances ---

def f23obv_f23_on_balance_volume_family_obv_rel_dist_5d_v021_signal(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OBV relative distance to its 5-day SMA."""
    obv = _obv_calc(close, volume)
    res = _obv_rel_dist(obv, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f23obv_f23_on_balance_volume_family_obv_rel_dist_10d_v022_signal(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OBV relative distance to its 10-day SMA."""
    obv = _obv_calc(close, volume)
    res = _obv_rel_dist(obv, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f23obv_f23_on_balance_volume_family_obv_rel_dist_21d_v023_signal(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OBV relative distance to its 21-day SMA."""
    obv = _obv_calc(close, volume)
    res = _obv_rel_dist(obv, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f23obv_f23_on_balance_volume_family_obv_adj_rel_dist_63d_v024_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    """OBV using closeadj relative distance to its 63-day SMA."""
    obv = _obv_calc(closeadj, volume)
    res = _obv_rel_dist(obv, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f23obv_f23_on_balance_volume_family_obv_adj_rel_dist_126d_v025_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    """OBV using closeadj relative distance to its 126-day SMA."""
    obv = _obv_calc(closeadj, volume)
    res = _obv_rel_dist(obv, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f23obv_f23_on_balance_volume_family_obv_adj_rel_dist_252d_v026_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    """OBV using closeadj relative distance to its 252-day SMA."""
    obv = _obv_calc(closeadj, volume)
    res = _obv_rel_dist(obv, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f23obv_f23_on_balance_volume_family_obv_ema_rel_dist_21d_v027_signal(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Relative distance of 21-day EMA of OBV to its SMA."""
    obv = _ema(_obv_calc(close, volume), 21)
    res = _obv_rel_dist(obv, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f23obv_f23_on_balance_volume_family_obv_adj_ema_rel_dist_63d_v028_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    """Relative distance of 63-day EMA of OBV (using closeadj) to its SMA."""
    obv = _ema(_obv_calc(closeadj, volume), 63)
    res = _obv_rel_dist(obv, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f23obv_f23_on_balance_volume_family_obv_adj_ema_rel_dist_126d_v029_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    """Relative distance of 126-day EMA of OBV (using closeadj) to its SMA."""
    obv = _ema(_obv_calc(closeadj, volume), 126)
    res = _obv_rel_dist(obv, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f23obv_f23_on_balance_volume_family_obv_adj_ema_rel_dist_252d_v030_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    """Relative distance of 252-day EMA of OBV (using closeadj) to its SMA."""
    obv = _ema(_obv_calc(closeadj, volume), 252)
    res = _obv_rel_dist(obv, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# --- Features 031 - 040: Price-OBV Correlation ---

def f23obv_f23_on_balance_volume_family_price_obv_corr_5d_v031_signal(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Correlation between Price and OBV over 5 days."""
    obv = _obv_calc(close, volume)
    res = close.rolling(5).corr(obv)
    return res.replace([np.inf, -np.inf], np.nan)

def f23obv_f23_on_balance_volume_family_price_obv_corr_10d_v032_signal(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Correlation between Price and OBV over 10 days."""
    obv = _obv_calc(close, volume)
    res = close.rolling(10).corr(obv)
    return res.replace([np.inf, -np.inf], np.nan)

def f23obv_f23_on_balance_volume_family_price_obv_corr_21d_v033_signal(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Correlation between Price and OBV over 21 days."""
    obv = _obv_calc(close, volume)
    res = close.rolling(21).corr(obv)
    return res.replace([np.inf, -np.inf], np.nan)

def f23obv_f23_on_balance_volume_family_price_obv_adj_corr_63d_v034_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    """Correlation between closeadj and OBV over 63 days."""
    obv = _obv_calc(closeadj, volume)
    res = closeadj.rolling(63).corr(obv)
    return res.replace([np.inf, -np.inf], np.nan)

def f23obv_f23_on_balance_volume_family_price_obv_adj_corr_126d_v035_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    """Correlation between closeadj and OBV over 126 days."""
    obv = _obv_calc(closeadj, volume)
    res = closeadj.rolling(126).corr(obv)
    return res.replace([np.inf, -np.inf], np.nan)

def f23obv_f23_on_balance_volume_family_price_obv_adj_corr_252d_v036_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    """Correlation between closeadj and OBV over 252 days."""
    obv = _obv_calc(closeadj, volume)
    res = closeadj.rolling(252).corr(obv)
    return res.replace([np.inf, -np.inf], np.nan)

def f23obv_f23_on_balance_volume_family_obv_sma_price_corr_21d_v037_signal(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Correlation between 21-day Price SMA and 21-day OBV SMA."""
    obv_sma = _sma(_obv_calc(close, volume), 21)
    price_sma = _sma(close, 21)
    res = price_sma.rolling(21).corr(obv_sma)
    return res.replace([np.inf, -np.inf], np.nan)

def f23obv_f23_on_balance_volume_family_obv_adj_sma_price_corr_63d_v038_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    """Correlation between 63-day closeadj SMA and 63-day OBV SMA."""
    obv_sma = _sma(_obv_calc(closeadj, volume), 63)
    price_sma = _sma(closeadj, 63)
    res = price_sma.rolling(63).corr(obv_sma)
    return res.replace([np.inf, -np.inf], np.nan)

def f23obv_f23_on_balance_volume_family_obv_adj_ema_price_corr_126d_v039_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    """Correlation between 126-day closeadj EMA and 126-day OBV EMA."""
    obv_ema = _ema(_obv_calc(closeadj, volume), 126)
    price_ema = _ema(closeadj, 126)
    res = price_ema.rolling(126).corr(obv_ema)
    return res.replace([np.inf, -np.inf], np.nan)

def f23obv_f23_on_balance_volume_family_obv_adj_ema_price_corr_252d_v040_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    """Correlation between 252-day closeadj EMA and 252-day OBV EMA."""
    obv_ema = _ema(_obv_calc(closeadj, volume), 252)
    price_ema = _ema(closeadj, 252)
    res = price_ema.rolling(252).corr(obv_ema)
    return res.replace([np.inf, -np.inf], np.nan)

# --- Features 041 - 050: OBV Acceleration (Diff of Diff) ---

def f23obv_f23_on_balance_volume_family_obv_accel_5d_v041_signal(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OBV acceleration (diff of diff) over 5 days."""
    obv = _obv_calc(close, volume)
    res = obv.diff(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f23obv_f23_on_balance_volume_family_obv_accel_10d_v042_signal(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OBV acceleration (diff of diff) over 10 days."""
    obv = _obv_calc(close, volume)
    res = obv.diff(10).diff(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f23obv_f23_on_balance_volume_family_obv_accel_21d_v043_signal(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OBV acceleration (diff of diff) over 21 days."""
    obv = _obv_calc(close, volume)
    res = obv.diff(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f23obv_f23_on_balance_volume_family_obv_adj_accel_63d_v044_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    """OBV using closeadj acceleration (diff of diff) over 63 days."""
    obv = _obv_calc(closeadj, volume)
    res = obv.diff(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f23obv_f23_on_balance_volume_family_obv_adj_accel_126d_v045_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    """OBV using closeadj acceleration (diff of diff) over 126 days."""
    obv = _obv_calc(closeadj, volume)
    res = obv.diff(126).diff(126)
    return res.replace([np.inf, -np.inf], np.nan)

def f23obv_f23_on_balance_volume_family_obv_adj_accel_252d_v046_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    """OBV using closeadj acceleration (diff of diff) over 252 days."""
    obv = _obv_calc(closeadj, volume)
    res = obv.diff(252).diff(252)
    return res.replace([np.inf, -np.inf], np.nan)

def f23obv_f23_on_balance_volume_family_obv_sma_accel_21d_v047_signal(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Acceleration of 21-day SMA of OBV."""
    obv_sma = _sma(_obv_calc(close, volume), 21)
    res = obv_sma.diff(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f23obv_f23_on_balance_volume_family_obv_adj_sma_accel_63d_v048_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    """Acceleration of 63-day SMA of OBV (using closeadj)."""
    obv_sma = _sma(_obv_calc(closeadj, volume), 63)
    res = obv_sma.diff(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f23obv_f23_on_balance_volume_family_obv_adj_ema_accel_126d_v049_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    """Acceleration of 126-day EMA of OBV (using closeadj)."""
    obv_ema = _ema(_obv_calc(closeadj, volume), 126)
    res = obv_ema.diff(126).diff(126)
    return res.replace([np.inf, -np.inf], np.nan)

def f23obv_f23_on_balance_volume_family_obv_adj_ema_accel_252d_v050_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    """Acceleration of 252-day EMA of OBV (using closeadj)."""
    obv_ema = _ema(_obv_calc(closeadj, volume), 252)
    res = obv_ema.diff(252).diff(252)
    return res.replace([np.inf, -np.inf], np.nan)

# --- Features 051 - 075: Mixed and Advanced Variations ---

def f23obv_f23_on_balance_volume_family_obv_zscore_rel_dist_ratio_21d_v051_signal(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of OBV Z-score to OBV relative distance over 21 days."""
    obv = _obv_calc(close, volume)
    z = _obv_zscore(obv, 21)
    d = _obv_rel_dist(obv, 21)
    res = z / d.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f23obv_f23_on_balance_volume_family_obv_adj_zscore_rel_dist_ratio_63d_v052_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of OBV (closeadj) Z-score to OBV relative distance over 63 days."""
    obv = _obv_calc(closeadj, volume)
    z = _obv_zscore(obv, 63)
    d = _obv_rel_dist(obv, 63)
    res = z / d.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f23obv_f23_on_balance_volume_family_obv_sma_diff_v053_signal(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Difference between 5-day and 21-day SMA of OBV."""
    obv = _obv_calc(close, volume)
    res = _sma(obv, 5) - _sma(obv, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f23obv_f23_on_balance_volume_family_obv_adj_sma_diff_v054_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    """Difference between 21-day and 63-day SMA of OBV (using closeadj)."""
    obv = _obv_calc(closeadj, volume)
    res = _sma(obv, 21) - _sma(obv, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f23obv_f23_on_balance_volume_family_obv_ema_diff_v055_signal(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Difference between 5-day and 21-day EMA of OBV."""
    obv = _obv_calc(close, volume)
    res = _ema(obv, 5) - _ema(obv, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f23obv_f23_on_balance_volume_family_obv_adj_ema_diff_v056_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    """Difference between 21-day and 63-day EMA of OBV (using closeadj)."""
    obv = _obv_calc(closeadj, volume)
    res = _ema(obv, 21) - _ema(obv, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f23obv_f23_on_balance_volume_family_obv_vol_norm_5d_v057_signal(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OBV normalized by its 5-day rolling volume mean."""
    obv = _obv_calc(close, volume)
    res = obv / volume.rolling(5).mean().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f23obv_f23_on_balance_volume_family_obv_adj_vol_norm_63d_v058_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    """OBV (using closeadj) normalized by its 63-day rolling volume mean."""
    obv = _obv_calc(closeadj, volume)
    res = obv / volume.rolling(63).mean().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f23obv_f23_on_balance_volume_family_obv_range_norm_21d_v059_signal(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OBV normalized by its 21-day range (max-min)."""
    obv = _obv_calc(close, volume)
    r = obv.rolling(21).max() - obv.rolling(21).min()
    res = (obv - obv.rolling(21).min()) / r.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f23obv_f23_on_balance_volume_family_obv_adj_range_norm_63d_v060_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    """OBV (using closeadj) normalized by its 63-day range (max-min)."""
    obv = _obv_calc(closeadj, volume)
    r = obv.rolling(63).max() - obv.rolling(63).min()
    res = (obv - obv.rolling(63).min()) / r.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f23obv_f23_on_balance_volume_family_obv_slope_simple_5d_v061_signal(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Simple 5-day slope of OBV."""
    obv = _obv_calc(close, volume)
    res = obv.diff(5) / 5
    return res.replace([np.inf, -np.inf], np.nan)

def f23obv_f23_on_balance_volume_family_obv_adj_slope_simple_63d_v062_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    """Simple 63-day slope of OBV (using closeadj)."""
    obv = _obv_calc(closeadj, volume)
    res = obv.diff(63) / 63
    return res.replace([np.inf, -np.inf], np.nan)

def f23obv_f23_on_balance_volume_family_obv_vol_ratio_21d_v063_signal(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of OBV 21-day change to 21-day total volume."""
    obv = _obv_calc(close, volume)
    res = obv.diff(21) / volume.rolling(21).sum().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f23obv_f23_on_balance_volume_family_obv_adj_vol_ratio_63d_v064_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of OBV (closeadj) 63-day change to 63-day total volume."""
    obv = _obv_calc(closeadj, volume)
    res = obv.diff(63) / volume.rolling(63).sum().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f23obv_f23_on_balance_volume_family_obv_std_norm_21d_v065_signal(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OBV change normalized by its 21-day standard deviation."""
    obv = _obv_calc(close, volume)
    res = obv.diff(21) / obv.rolling(21).std().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f23obv_f23_on_balance_volume_family_obv_adj_std_norm_63d_v066_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    """OBV (closeadj) change normalized by its 63-day standard deviation."""
    obv = _obv_calc(closeadj, volume)
    res = obv.diff(63) / obv.rolling(63).std().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f23obv_f23_on_balance_volume_family_obv_cum_sum_ratio_21d_v067_signal(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of OBV to cumulative volume over 21 days."""
    obv = _obv_calc(close, volume)
    res = obv / volume.rolling(21).sum().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f23obv_f23_on_balance_volume_family_obv_adj_cum_sum_ratio_63d_v068_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of OBV (closeadj) to cumulative volume over 63 days."""
    obv = _obv_calc(closeadj, volume)
    res = obv / volume.rolling(63).sum().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f23obv_f23_on_balance_volume_family_obv_adj_ema_63d_zscore_v069_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of 63-day EMA of OBV (using closeadj)."""
    obv_ema = _ema(_obv_calc(closeadj, volume), 63)
    res = _obv_zscore(obv_ema, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f23obv_f23_on_balance_volume_family_obv_adj_ema_126d_zscore_v070_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of 126-day EMA of OBV (using closeadj)."""
    obv_ema = _ema(_obv_calc(closeadj, volume), 126)
    res = _obv_zscore(obv_ema, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f23obv_f23_on_balance_volume_family_obv_adj_ema_252d_zscore_v071_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of 252-day EMA of OBV (using closeadj)."""
    obv_ema = _ema(_obv_calc(closeadj, volume), 252)
    res = _obv_zscore(obv_ema, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f23obv_f23_on_balance_volume_family_obv_adj_sma_126d_rel_dist_v072_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    """Relative distance of 126-day SMA of OBV (using closeadj)."""
    obv_sma = _sma(_obv_calc(closeadj, volume), 126)
    res = _obv_rel_dist(obv_sma, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f23obv_f23_on_balance_volume_family_obv_adj_sma_252d_rel_dist_v073_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    """Relative distance of 252-day SMA of OBV (using closeadj)."""
    obv_sma = _sma(_obv_calc(closeadj, volume), 252)
    res = _obv_rel_dist(obv_sma, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f23obv_f23_on_balance_volume_family_obv_adj_ema_63d_accel_v074_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    """Acceleration of 63-day EMA of OBV (using closeadj)."""
    obv_ema = _ema(_obv_calc(closeadj, volume), 63)
    res = obv_ema.diff(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f23obv_f23_on_balance_volume_family_obv_adj_ema_126d_accel_v075_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    """Acceleration of 126-day EMA of OBV (using closeadj)."""
    obv_ema = _ema(_obv_calc(closeadj, volume), 126)
    res = obv_ema.diff(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

SILVERDB_ACCESS, SOURCE_TABLE, ENTITY_COLUMN, DATE_COLUMN = "read_only", "sep", "ticker", "date"
ORDER_BY, NO_FORWARD_LOOKING = [ENTITY_COLUMN, DATE_COLUMN], True
SOURCE_COLUMNS = {c: f"sep.{c}" for c in ["close", "closeadj", "volume"]}

BASE_NAMES = [f for f in globals() if f.startswith("f23obv_") and f.endswith("_signal")]

F23_ON_BALANCE_VOLUME_FAMILY_BASE_REGISTRY_001_075 = {
    n: {
        "inputs": (inputs := [v for v in globals()[n].__code__.co_varnames[:globals()[n].__code__.co_argcount]]),
        "source_table": SOURCE_TABLE,
        "source_columns": {c: SOURCE_COLUMNS[c] for c in inputs if c in SOURCE_COLUMNS},
        "entity_column": ENTITY_COLUMN, "date_column": DATE_COLUMN,
        "order_by": ORDER_BY, "no_forward_looking": NO_FORWARD_LOOKING, "func": globals()[n]
    } for n in sorted(BASE_NAMES)
}

if __name__ == "__main__":
    sz = 1000
    d = pd.DataFrame({
        "close": np.linspace(100, 200, sz) + np.sin(np.linspace(0, 10, sz)),
        "closeadj": np.linspace(100, 200, sz) + np.sin(np.linspace(0, 10, sz)),
        "volume": np.abs(np.cos(np.linspace(0, 10, sz))) * 1000 + 100,
        "ticker": ["T"]*sz,
        "date": pd.date_range("2020-01-01", periods=sz)
    })
    for n, c in F23_ON_BALANCE_VOLUME_FAMILY_BASE_REGISTRY_001_075.items():
        r = c["func"](**{i: d[i] for i in c["inputs"]})
        assert isinstance(r, pd.Series)
    print("base 001-075 OK")
