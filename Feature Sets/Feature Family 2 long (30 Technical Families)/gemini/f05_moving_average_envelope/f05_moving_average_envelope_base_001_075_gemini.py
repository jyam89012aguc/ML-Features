# f05_moving_average_envelope_base_001_075_gemini.py
import pandas as pd
import numpy as np

def _sma(s, w):
    return s.rolling(w, min_periods=min(w, 5)).mean()

def _ema(s, w):
    return s.ewm(span=w, min_periods=min(w, 5), adjust=False).mean()

def _wma(s, w):
    weights = np.arange(1, w + 1)
    return s.rolling(w, min_periods=min(w, 5)).apply(lambda x: np.dot(x, weights[-len(x):]) / weights[-len(x):].sum(), raw=True)

def _envelope_pos(price, ma, pct):
    upper = ma * (1 + pct)
    lower = ma * (1 - pct)
    return (price - lower) / (upper - lower).replace(0, np.nan)

def _envelope_dist(price, ma, pct, is_upper=True):
    bound = ma * (1 + pct) if is_upper else ma * (1 - pct)
    return (price - bound) / bound.abs().replace(0, np.nan)

def _envelope_width(ma, pct):
    return (2 * ma * pct) / ma.abs().replace(0, np.nan)

# Base Features 001-075: Price position within envelopes (SMA, EMA, WMA)

def f05mae_f05_moving_average_envelope_sma_5d_1pct_pos_v001_signal(close: pd.Series) -> pd.Series:
    """Price position in 1% SMA envelope, 5-day window."""
    ma = _sma(close, 5)
    res = _envelope_pos(close, ma, 0.01)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_sma_5d_2pct_pos_v002_signal(close: pd.Series) -> pd.Series:
    """Price position in 2% SMA envelope, 5-day window."""
    ma = _sma(close, 5)
    res = _envelope_pos(close, ma, 0.02)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_sma_5d_3pct_pos_v003_signal(close: pd.Series) -> pd.Series:
    """Price position in 3% SMA envelope, 5-day window."""
    ma = _sma(close, 5)
    res = _envelope_pos(close, ma, 0.03)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_sma_5d_5pct_pos_v004_signal(close: pd.Series) -> pd.Series:
    """Price position in 5% SMA envelope, 5-day window."""
    ma = _sma(close, 5)
    res = _envelope_pos(close, ma, 0.05)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_sma_5d_10pct_pos_v005_signal(close: pd.Series) -> pd.Series:
    """Price position in 10% SMA envelope, 5-day window."""
    ma = _sma(close, 5)
    res = _envelope_pos(close, ma, 0.10)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_sma_21d_1pct_pos_v006_signal(close: pd.Series) -> pd.Series:
    """Price position in 1% SMA envelope, 21-day window."""
    ma = _sma(close, 21)
    res = _envelope_pos(close, ma, 0.01)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_sma_21d_2pct_pos_v007_signal(close: pd.Series) -> pd.Series:
    """Price position in 2% SMA envelope, 21-day window."""
    ma = _sma(close, 21)
    res = _envelope_pos(close, ma, 0.02)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_sma_21d_3pct_pos_v008_signal(close: pd.Series) -> pd.Series:
    """Price position in 3% SMA envelope, 21-day window."""
    ma = _sma(close, 21)
    res = _envelope_pos(close, ma, 0.03)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_sma_21d_5pct_pos_v009_signal(close: pd.Series) -> pd.Series:
    """Price position in 5% SMA envelope, 21-day window."""
    ma = _sma(close, 21)
    res = _envelope_pos(close, ma, 0.05)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_sma_21d_10pct_pos_v010_signal(close: pd.Series) -> pd.Series:
    """Price position in 10% SMA envelope, 21-day window."""
    ma = _sma(close, 21)
    res = _envelope_pos(close, ma, 0.10)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_sma_63d_1pct_pos_v011_signal(closeadj: pd.Series) -> pd.Series:
    """Price position in 1% SMA envelope, 63-day window."""
    ma = _sma(closeadj, 63)
    res = _envelope_pos(closeadj, ma, 0.01)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_sma_63d_2pct_pos_v012_signal(closeadj: pd.Series) -> pd.Series:
    """Price position in 2% SMA envelope, 63-day window."""
    ma = _sma(closeadj, 63)
    res = _envelope_pos(closeadj, ma, 0.02)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_sma_63d_3pct_pos_v013_signal(closeadj: pd.Series) -> pd.Series:
    """Price position in 3% SMA envelope, 63-day window."""
    ma = _sma(closeadj, 63)
    res = _envelope_pos(closeadj, ma, 0.03)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_sma_63d_5pct_pos_v014_signal(closeadj: pd.Series) -> pd.Series:
    """Price position in 5% SMA envelope, 63-day window."""
    ma = _sma(closeadj, 63)
    res = _envelope_pos(closeadj, ma, 0.05)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_sma_63d_10pct_pos_v015_signal(closeadj: pd.Series) -> pd.Series:
    """Price position in 10% SMA envelope, 63-day window."""
    ma = _sma(closeadj, 63)
    res = _envelope_pos(closeadj, ma, 0.10)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_sma_126d_1pct_pos_v016_signal(closeadj: pd.Series) -> pd.Series:
    """Price position in 1% SMA envelope, 126-day window."""
    ma = _sma(closeadj, 126)
    res = _envelope_pos(closeadj, ma, 0.01)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_sma_126d_2pct_pos_v017_signal(closeadj: pd.Series) -> pd.Series:
    """Price position in 2% SMA envelope, 126-day window."""
    ma = _sma(closeadj, 126)
    res = _envelope_pos(closeadj, ma, 0.02)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_sma_126d_3pct_pos_v018_signal(closeadj: pd.Series) -> pd.Series:
    """Price position in 3% SMA envelope, 126-day window."""
    ma = _sma(closeadj, 126)
    res = _envelope_pos(closeadj, ma, 0.03)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_sma_126d_5pct_pos_v019_signal(closeadj: pd.Series) -> pd.Series:
    """Price position in 5% SMA envelope, 126-day window."""
    ma = _sma(closeadj, 126)
    res = _envelope_pos(closeadj, ma, 0.05)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_sma_126d_10pct_pos_v020_signal(closeadj: pd.Series) -> pd.Series:
    """Price position in 10% SMA envelope, 126-day window."""
    ma = _sma(closeadj, 126)
    res = _envelope_pos(closeadj, ma, 0.10)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_sma_252d_1pct_pos_v021_signal(closeadj: pd.Series) -> pd.Series:
    """Price position in 1% SMA envelope, 252-day window."""
    ma = _sma(closeadj, 252)
    res = _envelope_pos(closeadj, ma, 0.01)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_sma_252d_2pct_pos_v022_signal(closeadj: pd.Series) -> pd.Series:
    """Price position in 2% SMA envelope, 252-day window."""
    ma = _sma(closeadj, 252)
    res = _envelope_pos(closeadj, ma, 0.02)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_sma_252d_3pct_pos_v023_signal(closeadj: pd.Series) -> pd.Series:
    """Price position in 3% SMA envelope, 252-day window."""
    ma = _sma(closeadj, 252)
    res = _envelope_pos(closeadj, ma, 0.03)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_sma_252d_5pct_pos_v024_signal(closeadj: pd.Series) -> pd.Series:
    """Price position in 5% SMA envelope, 252-day window."""
    ma = _sma(closeadj, 252)
    res = _envelope_pos(closeadj, ma, 0.05)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_sma_252d_10pct_pos_v025_signal(closeadj: pd.Series) -> pd.Series:
    """Price position in 10% SMA envelope, 252-day window."""
    ma = _sma(closeadj, 252)
    res = _envelope_pos(closeadj, ma, 0.10)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_ema_5d_1pct_pos_v026_signal(close: pd.Series) -> pd.Series:
    """Price position in 1% EMA envelope, 5-day window."""
    ma = _ema(close, 5)
    res = _envelope_pos(close, ma, 0.01)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_ema_5d_2pct_pos_v027_signal(close: pd.Series) -> pd.Series:
    """Price position in 2% EMA envelope, 5-day window."""
    ma = _ema(close, 5)
    res = _envelope_pos(close, ma, 0.02)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_ema_5d_3pct_pos_v028_signal(close: pd.Series) -> pd.Series:
    """Price position in 3% EMA envelope, 5-day window."""
    ma = _ema(close, 5)
    res = _envelope_pos(close, ma, 0.03)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_ema_5d_5pct_pos_v029_signal(close: pd.Series) -> pd.Series:
    """Price position in 5% EMA envelope, 5-day window."""
    ma = _ema(close, 5)
    res = _envelope_pos(close, ma, 0.05)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_ema_5d_10pct_pos_v030_signal(close: pd.Series) -> pd.Series:
    """Price position in 10% EMA envelope, 5-day window."""
    ma = _ema(close, 5)
    res = _envelope_pos(close, ma, 0.10)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_ema_21d_1pct_pos_v031_signal(close: pd.Series) -> pd.Series:
    """Price position in 1% EMA envelope, 21-day window."""
    ma = _ema(close, 21)
    res = _envelope_pos(close, ma, 0.01)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_ema_21d_2pct_pos_v032_signal(close: pd.Series) -> pd.Series:
    """Price position in 2% EMA envelope, 21-day window."""
    ma = _ema(close, 21)
    res = _envelope_pos(close, ma, 0.02)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_ema_21d_3pct_pos_v033_signal(close: pd.Series) -> pd.Series:
    """Price position in 3% EMA envelope, 21-day window."""
    ma = _ema(close, 21)
    res = _envelope_pos(close, ma, 0.03)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_ema_21d_5pct_pos_v034_signal(close: pd.Series) -> pd.Series:
    """Price position in 5% EMA envelope, 21-day window."""
    ma = _ema(close, 21)
    res = _envelope_pos(close, ma, 0.05)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_ema_21d_10pct_pos_v035_signal(close: pd.Series) -> pd.Series:
    """Price position in 10% EMA envelope, 21-day window."""
    ma = _ema(close, 21)
    res = _envelope_pos(close, ma, 0.10)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_ema_63d_1pct_pos_v036_signal(closeadj: pd.Series) -> pd.Series:
    """Price position in 1% EMA envelope, 63-day window."""
    ma = _ema(closeadj, 63)
    res = _envelope_pos(closeadj, ma, 0.01)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_ema_63d_2pct_pos_v037_signal(closeadj: pd.Series) -> pd.Series:
    """Price position in 2% EMA envelope, 63-day window."""
    ma = _ema(closeadj, 63)
    res = _envelope_pos(closeadj, ma, 0.02)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_ema_63d_3pct_pos_v038_signal(closeadj: pd.Series) -> pd.Series:
    """Price position in 3% EMA envelope, 63-day window."""
    ma = _ema(closeadj, 63)
    res = _envelope_pos(closeadj, ma, 0.03)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_ema_63d_5pct_pos_v039_signal(closeadj: pd.Series) -> pd.Series:
    """Price position in 5% EMA envelope, 63-day window."""
    ma = _ema(closeadj, 63)
    res = _envelope_pos(closeadj, ma, 0.05)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_ema_63d_10pct_pos_v040_signal(closeadj: pd.Series) -> pd.Series:
    """Price position in 10% EMA envelope, 63-day window."""
    ma = _ema(closeadj, 63)
    res = _envelope_pos(closeadj, ma, 0.10)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_ema_126d_1pct_pos_v041_signal(closeadj: pd.Series) -> pd.Series:
    """Price position in 1% EMA envelope, 126-day window."""
    ma = _ema(closeadj, 126)
    res = _envelope_pos(closeadj, ma, 0.01)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_ema_126d_2pct_pos_v042_signal(closeadj: pd.Series) -> pd.Series:
    """Price position in 2% EMA envelope, 126-day window."""
    ma = _ema(closeadj, 126)
    res = _envelope_pos(closeadj, ma, 0.02)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_ema_126d_3pct_pos_v043_signal(closeadj: pd.Series) -> pd.Series:
    """Price position in 3% EMA envelope, 126-day window."""
    ma = _ema(closeadj, 126)
    res = _envelope_pos(closeadj, ma, 0.03)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_ema_126d_5pct_pos_v044_signal(closeadj: pd.Series) -> pd.Series:
    """Price position in 5% EMA envelope, 126-day window."""
    ma = _ema(closeadj, 126)
    res = _envelope_pos(closeadj, ma, 0.05)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_ema_126d_10pct_pos_v045_signal(closeadj: pd.Series) -> pd.Series:
    """Price position in 10% EMA envelope, 126-day window."""
    ma = _ema(closeadj, 126)
    res = _envelope_pos(closeadj, ma, 0.10)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_ema_252d_1pct_pos_v046_signal(closeadj: pd.Series) -> pd.Series:
    """Price position in 1% EMA envelope, 252-day window."""
    ma = _ema(closeadj, 252)
    res = _envelope_pos(closeadj, ma, 0.01)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_ema_252d_2pct_pos_v047_signal(closeadj: pd.Series) -> pd.Series:
    """Price position in 2% EMA envelope, 252-day window."""
    ma = _ema(closeadj, 252)
    res = _envelope_pos(closeadj, ma, 0.02)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_ema_252d_3pct_pos_v048_signal(closeadj: pd.Series) -> pd.Series:
    """Price position in 3% EMA envelope, 252-day window."""
    ma = _ema(closeadj, 252)
    res = _envelope_pos(closeadj, ma, 0.03)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_ema_252d_5pct_pos_v049_signal(closeadj: pd.Series) -> pd.Series:
    """Price position in 5% EMA envelope, 252-day window."""
    ma = _ema(closeadj, 252)
    res = _envelope_pos(closeadj, ma, 0.05)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_ema_252d_10pct_pos_v050_signal(closeadj: pd.Series) -> pd.Series:
    """Price position in 10% EMA envelope, 252-day window."""
    ma = _ema(closeadj, 252)
    res = _envelope_pos(closeadj, ma, 0.10)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_wma_5d_1pct_pos_v051_signal(close: pd.Series) -> pd.Series:
    """Price position in 1% WMA envelope, 5-day window."""
    ma = _wma(close, 5)
    res = _envelope_pos(close, ma, 0.01)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_wma_5d_2pct_pos_v052_signal(close: pd.Series) -> pd.Series:
    """Price position in 2% WMA envelope, 5-day window."""
    ma = _wma(close, 5)
    res = _envelope_pos(close, ma, 0.02)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_wma_5d_3pct_pos_v053_signal(close: pd.Series) -> pd.Series:
    """Price position in 3% WMA envelope, 5-day window."""
    ma = _wma(close, 5)
    res = _envelope_pos(close, ma, 0.03)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_wma_5d_5pct_pos_v054_signal(close: pd.Series) -> pd.Series:
    """Price position in 5% WMA envelope, 5-day window."""
    ma = _wma(close, 5)
    res = _envelope_pos(close, ma, 0.05)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_wma_5d_10pct_pos_v055_signal(close: pd.Series) -> pd.Series:
    """Price position in 10% WMA envelope, 5-day window."""
    ma = _wma(close, 5)
    res = _envelope_pos(close, ma, 0.10)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_wma_21d_1pct_pos_v056_signal(close: pd.Series) -> pd.Series:
    """Price position in 1% WMA envelope, 21-day window."""
    ma = _wma(close, 21)
    res = _envelope_pos(close, ma, 0.01)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_wma_21d_2pct_pos_v057_signal(close: pd.Series) -> pd.Series:
    """Price position in 2% WMA envelope, 21-day window."""
    ma = _wma(close, 21)
    res = _envelope_pos(close, ma, 0.02)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_wma_21d_3pct_pos_v058_signal(close: pd.Series) -> pd.Series:
    """Price position in 3% WMA envelope, 21-day window."""
    ma = _wma(close, 21)
    res = _envelope_pos(close, ma, 0.03)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_wma_21d_5pct_pos_v059_signal(close: pd.Series) -> pd.Series:
    """Price position in 5% WMA envelope, 21-day window."""
    ma = _wma(close, 21)
    res = _envelope_pos(close, ma, 0.05)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_wma_21d_10pct_pos_v060_signal(close: pd.Series) -> pd.Series:
    """Price position in 10% WMA envelope, 21-day window."""
    ma = _wma(close, 21)
    res = _envelope_pos(close, ma, 0.10)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_wma_63d_1pct_pos_v061_signal(closeadj: pd.Series) -> pd.Series:
    """Price position in 1% WMA envelope, 63-day window."""
    ma = _wma(closeadj, 63)
    res = _envelope_pos(closeadj, ma, 0.01)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_wma_63d_2pct_pos_v062_signal(closeadj: pd.Series) -> pd.Series:
    """Price position in 2% WMA envelope, 63-day window."""
    ma = _wma(closeadj, 63)
    res = _envelope_pos(closeadj, ma, 0.02)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_wma_63d_3pct_pos_v063_signal(closeadj: pd.Series) -> pd.Series:
    """Price position in 3% WMA envelope, 63-day window."""
    ma = _wma(closeadj, 63)
    res = _envelope_pos(closeadj, ma, 0.03)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_wma_63d_5pct_pos_v064_signal(closeadj: pd.Series) -> pd.Series:
    """Price position in 5% WMA envelope, 63-day window."""
    ma = _wma(closeadj, 63)
    res = _envelope_pos(closeadj, ma, 0.05)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_wma_63d_10pct_pos_v065_signal(closeadj: pd.Series) -> pd.Series:
    """Price position in 10% WMA envelope, 63-day window."""
    ma = _wma(closeadj, 63)
    res = _envelope_pos(closeadj, ma, 0.10)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_wma_126d_1pct_pos_v066_signal(closeadj: pd.Series) -> pd.Series:
    """Price position in 1% WMA envelope, 126-day window."""
    ma = _wma(closeadj, 126)
    res = _envelope_pos(closeadj, ma, 0.01)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_wma_126d_2pct_pos_v067_signal(closeadj: pd.Series) -> pd.Series:
    """Price position in 2% WMA envelope, 126-day window."""
    ma = _wma(closeadj, 126)
    res = _envelope_pos(closeadj, ma, 0.02)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_wma_126d_3pct_pos_v068_signal(closeadj: pd.Series) -> pd.Series:
    """Price position in 3% WMA envelope, 126-day window."""
    ma = _wma(closeadj, 126)
    res = _envelope_pos(closeadj, ma, 0.03)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_wma_126d_5pct_pos_v069_signal(closeadj: pd.Series) -> pd.Series:
    """Price position in 5% WMA envelope, 126-day window."""
    ma = _wma(closeadj, 126)
    res = _envelope_pos(closeadj, ma, 0.05)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_wma_126d_10pct_pos_v070_signal(closeadj: pd.Series) -> pd.Series:
    """Price position in 10% WMA envelope, 126-day window."""
    ma = _wma(closeadj, 126)
    res = _envelope_pos(closeadj, ma, 0.10)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_wma_252d_1pct_pos_v071_signal(closeadj: pd.Series) -> pd.Series:
    """Price position in 1% WMA envelope, 252-day window."""
    ma = _wma(closeadj, 252)
    res = _envelope_pos(closeadj, ma, 0.01)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_wma_252d_2pct_pos_v072_signal(closeadj: pd.Series) -> pd.Series:
    """Price position in 2% WMA envelope, 252-day window."""
    ma = _wma(closeadj, 252)
    res = _envelope_pos(closeadj, ma, 0.02)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_wma_252d_3pct_pos_v073_signal(closeadj: pd.Series) -> pd.Series:
    """Price position in 3% WMA envelope, 252-day window."""
    ma = _wma(closeadj, 252)
    res = _envelope_pos(closeadj, ma, 0.03)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_wma_252d_5pct_pos_v074_signal(closeadj: pd.Series) -> pd.Series:
    """Price position in 5% WMA envelope, 252-day window."""
    ma = _wma(closeadj, 252)
    res = _envelope_pos(closeadj, ma, 0.05)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_wma_252d_10pct_pos_v075_signal(closeadj: pd.Series) -> pd.Series:
    """Price position in 10% WMA envelope, 252-day window."""
    ma = _wma(closeadj, 252)
    res = _envelope_pos(closeadj, ma, 0.10)
    return res.replace([np.inf, -np.inf], np.nan)

SILVERDB_ACCESS, SOURCE_TABLE, ENTITY_COLUMN, DATE_COLUMN = "read_only", "sep", "ticker", "date"
ORDER_BY, NO_FORWARD_LOOKING = [ENTITY_COLUMN, DATE_COLUMN], True
SOURCE_COLUMNS = {c: f"sep.{c}" for c in ["close", "closeadj"]}

BASE_NAMES = [f for f in globals() if f.startswith("f05mae_") and f.endswith("_signal")]

F05_MOVING_AVERAGE_ENVELOPE_BASE_REGISTRY_001_075 = {
    n: {
        "inputs": (inputs := [v for v in globals()[n].__code__.co_varnames[:globals()[n].__code__.co_argcount]]),
        "source_table": SOURCE_TABLE,
        "source_columns": {c: SOURCE_COLUMNS[c] for c in inputs if c in SOURCE_COLUMNS},
        "entity_column": ENTITY_COLUMN, "date_column": DATE_COLUMN,
        "order_by": ORDER_BY, "no_forward_looking": NO_FORWARD_LOOKING, "func": globals()[n]
    } for n in sorted(BASE_NAMES)
}

if __name__ == "__main__":
    sz = 500
    d = pd.DataFrame({
        "close": np.random.randn(sz).cumsum() + 100,
        "closeadj": np.random.randn(sz).cumsum() + 100,
        "ticker": ["T"] * sz,
        "date": pd.date_range("2020-01-01", periods=sz)
    })
    for n, c in F05_MOVING_AVERAGE_ENVELOPE_BASE_REGISTRY_001_075.items():
        r = c["func"](**{i: d[i] for i in c["inputs"]})
        assert isinstance(r, pd.Series)
    print("base 001-075 OK")
