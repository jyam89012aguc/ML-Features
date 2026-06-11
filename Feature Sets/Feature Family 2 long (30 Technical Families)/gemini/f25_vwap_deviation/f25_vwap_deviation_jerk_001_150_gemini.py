import pandas as pd
import numpy as np

def _rolling_vwap(c, v, w):
    """
    Calculates the Volume Weighted Average Price (VWAP) over a rolling window.
    """
    pv = c * v
    return pv.rolling(w).sum() / v.rolling(w).sum().replace(0, np.nan)

def _vwap_dist_val(c, vwap):
    """
    Calculates the percentage distance between the price and the VWAP.
    """
    return (c - vwap) / vwap.abs().replace(0, np.nan)

def _vwap_z(c, vwap, w):
    """
    Calculates the Z-score of the price relative to the VWAP over a rolling window.
    """
    return (c - vwap) / c.rolling(w).std().replace(0, np.nan)

def _typical_price(h, l, c):
    """
    Calculates the typical price: (High + Low + Close) / 3.
    """
    return (h + l + c) / 3.0

def _jerk(s, w1, w2):
    """
    Calculates the jerk (second derivative) as the difference of differences.
    """
    return s.diff(w1).diff(w2)

# V001-V030: Jerks of VWAP Distances (Close)
def f25vd_vwap_dist_5d_jerk_1d_1d_v001_signal(arg_close, arg_volume) -> pd.Series:
    """1d-1d jerk of 5-day VWAP distance."""
    vwap = _rolling_vwap(arg_close, arg_volume, 5)
    dist = _vwap_dist_val(arg_close, vwap)
    res = _jerk(dist, 1, 1)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_dist_5d_jerk_3d_1d_v002_signal(arg_close, arg_volume) -> pd.Series:
    """3d-1d jerk of 5-day VWAP distance."""
    vwap = _rolling_vwap(arg_close, arg_volume, 5)
    dist = _vwap_dist_val(arg_close, vwap)
    res = _jerk(dist, 3, 1)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_dist_5d_jerk_5d_1d_v003_signal(arg_close, arg_volume) -> pd.Series:
    """5d-1d jerk of 5-day VWAP distance."""
    vwap = _rolling_vwap(arg_close, arg_volume, 5)
    dist = _vwap_dist_val(arg_close, vwap)
    res = _jerk(dist, 5, 1)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_dist_21d_jerk_1d_1d_v004_signal(arg_close, arg_volume) -> pd.Series:
    """1d-1d jerk of 21-day VWAP distance."""
    vwap = _rolling_vwap(arg_close, arg_volume, 21)
    dist = _vwap_dist_val(arg_close, vwap)
    res = _jerk(dist, 1, 1)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_dist_21d_jerk_5d_1d_v005_signal(arg_close, arg_volume) -> pd.Series:
    """5d-1d jerk of 21-day VWAP distance."""
    vwap = _rolling_vwap(arg_close, arg_volume, 21)
    dist = _vwap_dist_val(arg_close, vwap)
    res = _jerk(dist, 5, 1)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_dist_21d_jerk_10d_5d_v006_signal(arg_close, arg_volume) -> pd.Series:
    """10d-5d jerk of 21-day VWAP distance."""
    vwap = _rolling_vwap(arg_close, arg_volume, 21)
    dist = _vwap_dist_val(arg_close, vwap)
    res = _jerk(dist, 10, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_dist_63d_jerk_1d_1d_v007_signal(arg_closeadj, arg_volume) -> pd.Series:
    """1d-1d jerk of 63-day VWAP distance."""
    vwap = _rolling_vwap(arg_closeadj, arg_volume, 63)
    dist = _vwap_dist_val(arg_closeadj, vwap)
    res = _jerk(dist, 1, 1)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_dist_63d_jerk_5d_1d_v008_signal(arg_closeadj, arg_volume) -> pd.Series:
    """5d-1d jerk of 63-day VWAP distance."""
    vwap = _rolling_vwap(arg_closeadj, arg_volume, 63)
    dist = _vwap_dist_val(arg_closeadj, vwap)
    res = _jerk(dist, 5, 1)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_dist_63d_jerk_21d_5d_v009_signal(arg_closeadj, arg_volume) -> pd.Series:
    """21d-5d jerk of 63-day VWAP distance."""
    vwap = _rolling_vwap(arg_closeadj, arg_volume, 63)
    dist = _vwap_dist_val(arg_closeadj, vwap)
    res = _jerk(dist, 21, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_dist_126d_jerk_5d_1d_v010_signal(arg_closeadj, arg_volume) -> pd.Series:
    """5d-1d jerk of 126-day VWAP distance."""
    vwap = _rolling_vwap(arg_closeadj, arg_volume, 126)
    dist = _vwap_dist_val(arg_closeadj, vwap)
    res = _jerk(dist, 5, 1)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_dist_126d_jerk_21d_5d_v011_signal(arg_closeadj, arg_volume) -> pd.Series:
    """21d-5d jerk of 126-day VWAP distance."""
    vwap = _rolling_vwap(arg_closeadj, arg_volume, 126)
    dist = _vwap_dist_val(arg_closeadj, vwap)
    res = _jerk(dist, 21, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_dist_252d_jerk_21d_5d_v012_signal(arg_closeadj, arg_volume) -> pd.Series:
    """21d-5d jerk of 252-day VWAP distance."""
    vwap = _rolling_vwap(arg_closeadj, arg_volume, 252)
    dist = _vwap_dist_val(arg_closeadj, vwap)
    res = _jerk(dist, 21, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_dist_252d_jerk_63d_10d_v013_signal(arg_closeadj, arg_volume) -> pd.Series:
    """63d-10d jerk of 252-day VWAP distance."""
    vwap = _rolling_vwap(arg_closeadj, arg_volume, 252)
    dist = _vwap_dist_val(arg_closeadj, vwap)
    res = _jerk(dist, 63, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_dist_10d_jerk_1d_1d_v014_signal(arg_close, arg_volume) -> pd.Series:
    """1d-1d jerk of 10-day VWAP distance."""
    vwap = _rolling_vwap(arg_close, arg_volume, 10)
    dist = _vwap_dist_val(arg_close, vwap)
    res = _jerk(dist, 1, 1)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_dist_42d_jerk_5d_1d_v015_signal(arg_closeadj, arg_volume) -> pd.Series:
    """5d-1d jerk of 42-day VWAP distance."""
    vwap = _rolling_vwap(arg_closeadj, arg_volume, 42)
    dist = _vwap_dist_val(arg_closeadj, vwap)
    res = _jerk(dist, 5, 1)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_dist_5d_tp_jerk_1d_1d_v016_signal(arg_high, arg_low, arg_close, arg_volume) -> pd.Series:
    """1d-1d jerk of 5-day typical-price VWAP distance."""
    tp = _typical_price(arg_high, arg_low, arg_close)
    vwap = _rolling_vwap(tp, arg_volume, 5)
    dist = _vwap_dist_val(tp, vwap)
    res = _jerk(dist, 1, 1)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_dist_21d_tp_jerk_5d_1d_v017_signal(arg_high, arg_low, arg_close, arg_volume) -> pd.Series:
    """5d-1d jerk of 21-day typical-price VWAP distance."""
    tp = _typical_price(arg_high, arg_low, arg_close)
    vwap = _rolling_vwap(tp, arg_volume, 21)
    dist = _vwap_dist_val(tp, vwap)
    res = _jerk(dist, 5, 1)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_dist_63d_tp_jerk_10d_5d_v018_signal(arg_highadj, arg_lowadj, arg_closeadj, arg_volume) -> pd.Series:
    """10d-5d jerk of 63-day typical-price VWAP distance."""
    tp = _typical_price(arg_highadj, arg_lowadj, arg_closeadj)
    vwap = _rolling_vwap(tp, arg_volume, 63)
    dist = _vwap_dist_val(tp, vwap)
    res = _jerk(dist, 10, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_dist_5d_high_jerk_1d_1d_v019_signal(arg_high, arg_close, arg_volume) -> pd.Series:
    """1d-1d jerk of 5-day high-price VWAP distance."""
    vwap = _rolling_vwap(arg_close, arg_volume, 5)
    dist = _vwap_dist_val(arg_high, vwap)
    res = _jerk(dist, 1, 1)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_dist_21d_low_jerk_1d_1d_v020_signal(arg_low, arg_close, arg_volume) -> pd.Series:
    """1d-1d jerk of 21-day low-price VWAP distance."""
    vwap = _rolling_vwap(arg_close, arg_volume, 21)
    dist = _vwap_dist_val(arg_low, vwap)
    res = _jerk(dist, 1, 1)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_dist_5d_ema_21d_jerk_1d_1d_v021_signal(arg_close, arg_volume) -> pd.Series:
    """1d-1d jerk of 21-day EMA of 5-day VWAP distance."""
    vwap = _rolling_vwap(arg_close, arg_volume, 5)
    dist = _vwap_dist_val(arg_close, vwap)
    res = _jerk(dist.ewm(span=21).mean(), 1, 1)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_dist_21d_ema_63d_jerk_5d_1d_v022_signal(arg_close, arg_volume) -> pd.Series:
    """5d-1d jerk of 63-day EMA of 21-day VWAP distance."""
    vwap = _rolling_vwap(arg_close, arg_volume, 21)
    dist = _vwap_dist_val(arg_close, vwap)
    res = _jerk(dist.ewm(span=63).mean(), 5, 1)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_z_5d_jerk_1d_1d_v023_signal(arg_close, arg_volume) -> pd.Series:
    """1d-1d jerk of 5-day VWAP Z-score."""
    vwap = _rolling_vwap(arg_close, arg_volume, 5)
    z = _vwap_z(arg_close, vwap, 5)
    res = _jerk(z, 1, 1)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_z_5d_jerk_3d_1d_v024_signal(arg_close, arg_volume) -> pd.Series:
    """3d-1d jerk of 5-day VWAP Z-score."""
    vwap = _rolling_vwap(arg_close, arg_volume, 5)
    z = _vwap_z(arg_close, vwap, 5)
    res = _jerk(z, 3, 1)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_z_21d_jerk_1d_1d_v025_signal(arg_close, arg_volume) -> pd.Series:
    """1d-1d jerk of 21-day VWAP Z-score."""
    vwap = _rolling_vwap(arg_close, arg_volume, 21)
    z = _vwap_z(arg_close, vwap, 21)
    res = _jerk(z, 1, 1)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_z_21d_jerk_5d_1d_v026_signal(arg_close, arg_volume) -> pd.Series:
    """5d-1d jerk of 21-day VWAP Z-score."""
    vwap = _rolling_vwap(arg_close, arg_volume, 21)
    z = _vwap_z(arg_close, vwap, 21)
    res = _jerk(z, 5, 1)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_z_63d_jerk_1d_1d_v027_signal(arg_closeadj, arg_volume) -> pd.Series:
    """1d-1d jerk of 63-day VWAP Z-score."""
    vwap = _rolling_vwap(arg_closeadj, arg_volume, 63)
    z = _vwap_z(arg_closeadj, vwap, 63)
    res = _jerk(z, 1, 1)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_z_126d_jerk_10d_5d_v028_signal(arg_closeadj, arg_volume) -> pd.Series:
    """10d-5d jerk of 126-day VWAP Z-score."""
    vwap = _rolling_vwap(arg_closeadj, arg_volume, 126)
    z = _vwap_z(arg_closeadj, vwap, 126)
    res = _jerk(z, 10, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_z_252d_jerk_21d_5d_v029_signal(arg_closeadj, arg_volume) -> pd.Series:
    """21d-5d jerk of 252-day VWAP Z-score."""
    vwap = _rolling_vwap(arg_closeadj, arg_volume, 252)
    z = _vwap_z(arg_closeadj, vwap, 252)
    res = _jerk(z, 21, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_z_5d_tp_jerk_1d_1d_v030_signal(arg_high, arg_low, arg_close, arg_volume) -> pd.Series:
    """1d-1d jerk of 5-day typical-price VWAP Z-score."""
    tp = _typical_price(arg_high, arg_low, arg_close)
    vwap = _rolling_vwap(tp, arg_volume, 5)
    z = _vwap_z(tp, vwap, 5)
    res = _jerk(z, 1, 1)
    return res.replace([np.inf, -np.inf], np.nan)

# Generate more functions to reach 150
# V031-V060: More combinations of windows for jerks of distances
def f25vd_vwap_dist_10d_jerk_3d_1d_v031_signal(arg_close, arg_volume) -> pd.Series:
    """3d-1d jerk of 10-day VWAP distance."""
    vwap = _rolling_vwap(arg_close, arg_volume, 10)
    dist = _vwap_dist_val(arg_close, vwap)
    res = _jerk(dist, 3, 1)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_dist_10d_jerk_5d_1d_v032_signal(arg_close, arg_volume) -> pd.Series:
    """5d-1d jerk of 10-day VWAP distance."""
    vwap = _rolling_vwap(arg_close, arg_volume, 10)
    dist = _vwap_dist_val(arg_close, vwap)
    res = _jerk(dist, 5, 1)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_dist_21d_jerk_3d_1d_v033_signal(arg_close, arg_volume) -> pd.Series:
    """3d-1d jerk of 21-day VWAP distance."""
    vwap = _rolling_vwap(arg_close, arg_volume, 21)
    dist = _vwap_dist_val(arg_close, vwap)
    res = _jerk(dist, 3, 1)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_dist_42d_jerk_1d_1d_v034_signal(arg_closeadj, arg_volume) -> pd.Series:
    """1d-1d jerk of 42-day VWAP distance."""
    vwap = _rolling_vwap(arg_closeadj, arg_volume, 42)
    dist = _vwap_dist_val(arg_closeadj, vwap)
    res = _jerk(dist, 1, 1)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_dist_42d_jerk_10d_5d_v035_signal(arg_closeadj, arg_volume) -> pd.Series:
    """10d-5d jerk of 42-day VWAP distance."""
    vwap = _rolling_vwap(arg_closeadj, arg_volume, 42)
    dist = _vwap_dist_val(arg_closeadj, vwap)
    res = _jerk(dist, 10, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_dist_63d_jerk_3d_1d_v036_signal(arg_closeadj, arg_volume) -> pd.Series:
    """3d-1d jerk of 63-day VWAP distance."""
    vwap = _rolling_vwap(arg_closeadj, arg_volume, 63)
    dist = _vwap_dist_val(arg_closeadj, vwap)
    res = _jerk(dist, 3, 1)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_dist_63d_jerk_10d_5d_v037_signal(arg_closeadj, arg_volume) -> pd.Series:
    """10d-5d jerk of 63-day VWAP distance."""
    vwap = _rolling_vwap(arg_closeadj, arg_volume, 63)
    dist = _vwap_dist_val(arg_closeadj, vwap)
    res = _jerk(dist, 10, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_dist_126d_jerk_1d_1d_v038_signal(arg_closeadj, arg_volume) -> pd.Series:
    """1d-1d jerk of 126-day VWAP distance."""
    vwap = _rolling_vwap(arg_closeadj, arg_volume, 126)
    dist = _vwap_dist_val(arg_closeadj, vwap)
    res = _jerk(dist, 1, 1)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_dist_126d_jerk_63d_10d_v039_signal(arg_closeadj, arg_volume) -> pd.Series:
    """63d-10d jerk of 126-day VWAP distance."""
    vwap = _rolling_vwap(arg_closeadj, arg_volume, 126)
    dist = _vwap_dist_val(arg_closeadj, vwap)
    res = _jerk(dist, 63, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_dist_252d_jerk_1d_1d_v040_signal(arg_closeadj, arg_volume) -> pd.Series:
    """1d-1d jerk of 252-day VWAP distance."""
    vwap = _rolling_vwap(arg_closeadj, arg_volume, 252)
    dist = _vwap_dist_val(arg_closeadj, vwap)
    res = _jerk(dist, 1, 1)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_dist_252d_jerk_126d_21d_v041_signal(arg_closeadj, arg_volume) -> pd.Series:
    """126d-21d jerk of 252-day VWAP distance."""
    vwap = _rolling_vwap(arg_closeadj, arg_volume, 252)
    dist = _vwap_dist_val(arg_closeadj, vwap)
    res = _jerk(dist, 126, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_dist_5d_high_jerk_3d_1d_v042_signal(arg_high, arg_close, arg_volume) -> pd.Series:
    """3d-1d jerk of 5-day high-price VWAP distance."""
    vwap = _rolling_vwap(arg_close, arg_volume, 5)
    dist = _vwap_dist_val(arg_high, vwap)
    res = _jerk(dist, 3, 1)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_dist_5d_high_jerk_5d_1d_v043_signal(arg_high, arg_close, arg_volume) -> pd.Series:
    """5d-1d jerk of 5-day high-price VWAP distance."""
    vwap = _rolling_vwap(arg_close, arg_volume, 5)
    dist = _vwap_dist_val(arg_high, vwap)
    res = _jerk(dist, 5, 1)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_dist_21d_high_jerk_1d_1d_v044_signal(arg_high, arg_close, arg_volume) -> pd.Series:
    """1d-1d jerk of 21-day high-price VWAP distance."""
    vwap = _rolling_vwap(arg_close, arg_volume, 21)
    dist = _vwap_dist_val(arg_high, vwap)
    res = _jerk(dist, 1, 1)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_dist_21d_high_jerk_5d_1d_v045_signal(arg_high, arg_close, arg_volume) -> pd.Series:
    """5d-1d jerk of 21-day high-price VWAP distance."""
    vwap = _rolling_vwap(arg_close, arg_volume, 21)
    dist = _vwap_dist_val(arg_high, vwap)
    res = _jerk(dist, 5, 1)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_dist_63d_high_jerk_1d_1d_v046_signal(arg_highadj, arg_closeadj, arg_volume) -> pd.Series:
    """1d-1d jerk of 63-day highadj-price VWAP distance."""
    vwap = _rolling_vwap(arg_closeadj, arg_volume, 63)
    dist = _vwap_dist_val(arg_highadj, vwap)
    res = _jerk(dist, 1, 1)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_dist_5d_low_jerk_3d_1d_v047_signal(arg_low, arg_close, arg_volume) -> pd.Series:
    """3d-1d jerk of 5-day low-price VWAP distance."""
    vwap = _rolling_vwap(arg_close, arg_volume, 5)
    dist = _vwap_dist_val(arg_low, vwap)
    res = _jerk(dist, 3, 1)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_dist_21d_low_jerk_5d_1d_v048_signal(arg_low, arg_close, arg_volume) -> pd.Series:
    """5d-1d jerk of 21-day low-price VWAP distance."""
    vwap = _rolling_vwap(arg_close, arg_volume, 21)
    dist = _vwap_dist_val(arg_low, vwap)
    res = _jerk(dist, 5, 1)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_dist_63d_low_jerk_1d_1d_v049_signal(arg_lowadj, arg_closeadj, arg_volume) -> pd.Series:
    """1d-1d jerk of 63-day lowadj-price VWAP distance."""
    vwap = _rolling_vwap(arg_closeadj, arg_volume, 63)
    dist = _vwap_dist_val(arg_lowadj, vwap)
    res = _jerk(dist, 1, 1)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_dist_5d_tp_jerk_3d_1d_v050_signal(arg_high, arg_low, arg_close, arg_volume) -> pd.Series:
    """3d-1d jerk of 5-day typical-price VWAP distance."""
    tp = _typical_price(arg_high, arg_low, arg_close)
    vwap = _rolling_vwap(tp, arg_volume, 5)
    dist = _vwap_dist_val(tp, vwap)
    res = _jerk(dist, 3, 1)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_dist_5d_tp_jerk_5d_1d_v051_signal(arg_high, arg_low, arg_close, arg_volume) -> pd.Series:
    """5d-1d jerk of 5-day typical-price VWAP distance."""
    tp = _typical_price(arg_high, arg_low, arg_close)
    vwap = _rolling_vwap(tp, arg_volume, 5)
    dist = _vwap_dist_val(tp, vwap)
    res = _jerk(dist, 5, 1)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_dist_21d_tp_jerk_1d_1d_v052_signal(arg_high, arg_low, arg_close, arg_volume) -> pd.Series:
    """1d-1d jerk of 21-day typical-price VWAP distance."""
    tp = _typical_price(arg_high, arg_low, arg_close)
    vwap = _rolling_vwap(tp, arg_volume, 21)
    dist = _vwap_dist_val(tp, vwap)
    res = _jerk(dist, 1, 1)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_dist_21d_tp_jerk_10d_5d_v053_signal(arg_high, arg_low, arg_close, arg_volume) -> pd.Series:
    """10d-5d jerk of 21-day typical-price VWAP distance."""
    tp = _typical_price(arg_high, arg_low, arg_close)
    vwap = _rolling_vwap(tp, arg_volume, 21)
    dist = _vwap_dist_val(tp, vwap)
    res = _jerk(dist, 10, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_dist_63d_tp_jerk_1d_1d_v054_signal(arg_highadj, arg_lowadj, arg_closeadj, arg_volume) -> pd.Series:
    """1d-1d jerk of 63-day typical-price VWAP distance."""
    tp = _typical_price(arg_highadj, arg_lowadj, arg_closeadj)
    vwap = _rolling_vwap(tp, arg_volume, 63)
    dist = _vwap_dist_val(tp, vwap)
    res = _jerk(dist, 1, 1)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_dist_63d_tp_jerk_21d_5d_v055_signal(arg_highadj, arg_lowadj, arg_closeadj, arg_volume) -> pd.Series:
    """21d-5d jerk of 63-day typical-price VWAP distance."""
    tp = _typical_price(arg_highadj, arg_lowadj, arg_closeadj)
    vwap = _rolling_vwap(tp, arg_volume, 63)
    dist = _vwap_dist_val(tp, vwap)
    res = _jerk(dist, 21, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_dist_126d_tp_jerk_5d_1d_v056_signal(arg_highadj, arg_lowadj, arg_closeadj, arg_volume) -> pd.Series:
    """5d-1d jerk of 126-day typical-price VWAP distance."""
    tp = _typical_price(arg_highadj, arg_lowadj, arg_closeadj)
    vwap = _rolling_vwap(tp, arg_volume, 126)
    dist = _vwap_dist_val(tp, vwap)
    res = _jerk(dist, 5, 1)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_dist_252d_tp_jerk_21d_5d_v057_signal(arg_highadj, arg_lowadj, arg_closeadj, arg_volume) -> pd.Series:
    """21d-5d jerk of 252-day typical-price VWAP distance."""
    tp = _typical_price(arg_highadj, arg_lowadj, arg_closeadj)
    vwap = _rolling_vwap(tp, arg_volume, 252)
    dist = _vwap_dist_val(tp, vwap)
    res = _jerk(dist, 21, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_dist_5d_sma_21d_jerk_1d_1d_v058_signal(arg_close, arg_volume) -> pd.Series:
    """1d-1d jerk of 21-day SMA of 5-day VWAP distance."""
    vwap = _rolling_vwap(arg_close, arg_volume, 5)
    dist = _vwap_dist_val(arg_close, vwap)
    res = _jerk(dist.rolling(21).mean(), 1, 1)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_dist_21d_sma_63d_jerk_5d_1d_v059_signal(arg_close, arg_volume) -> pd.Series:
    """5d-1d jerk of 63-day SMA of 21-day VWAP distance."""
    vwap = _rolling_vwap(arg_close, arg_volume, 21)
    dist = _vwap_dist_val(arg_close, vwap)
    res = _jerk(dist.rolling(63).mean(), 5, 1)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_dist_63d_sma_126d_jerk_21d_5d_v060_signal(arg_closeadj, arg_volume) -> pd.Series:
    """21d-5d jerk of 126-day SMA of 63-day VWAP distance."""
    vwap = _rolling_vwap(arg_closeadj, arg_volume, 63)
    dist = _vwap_dist_val(arg_closeadj, vwap)
    res = _jerk(dist.rolling(126).mean(), 21, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# V061-V090: Jerks of VWAP Z-scores
def f25vd_vwap_z_5d_jerk_5d_1d_v061_signal(arg_close, arg_volume) -> pd.Series:
    """5d-1d jerk of 5-day VWAP Z-score."""
    vwap = _rolling_vwap(arg_close, arg_volume, 5)
    z = _vwap_z(arg_close, vwap, 5)
    res = _jerk(z, 5, 1)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_z_5d_jerk_10d_5d_v062_signal(arg_close, arg_volume) -> pd.Series:
    """10d-5d jerk of 5-day VWAP Z-score."""
    vwap = _rolling_vwap(arg_close, arg_volume, 5)
    z = _vwap_z(arg_close, vwap, 5)
    res = _jerk(z, 10, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_z_21d_jerk_3d_1d_v063_signal(arg_close, arg_volume) -> pd.Series:
    """3d-1d jerk of 21-day VWAP Z-score."""
    vwap = _rolling_vwap(arg_close, arg_volume, 21)
    z = _vwap_z(arg_close, vwap, 21)
    res = _jerk(z, 3, 1)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_z_21d_jerk_10d_5d_v064_signal(arg_close, arg_volume) -> pd.Series:
    """10d-5d jerk of 21-day VWAP Z-score."""
    vwap = _rolling_vwap(arg_close, arg_volume, 21)
    z = _vwap_z(arg_close, vwap, 21)
    res = _jerk(z, 10, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_z_21d_jerk_21d_5d_v065_signal(arg_close, arg_volume) -> pd.Series:
    """21d-5d jerk of 21-day VWAP Z-score."""
    vwap = _rolling_vwap(arg_close, arg_volume, 21)
    z = _vwap_z(arg_close, vwap, 21)
    res = _jerk(z, 21, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_z_63d_jerk_5d_1d_v066_signal(arg_closeadj, arg_volume) -> pd.Series:
    """5d-1d jerk of 63-day VWAP Z-score."""
    vwap = _rolling_vwap(arg_closeadj, arg_volume, 63)
    z = _vwap_z(arg_closeadj, vwap, 63)
    res = _jerk(z, 5, 1)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_z_63d_jerk_10d_5d_v067_signal(arg_closeadj, arg_volume) -> pd.Series:
    """10d-5d jerk of 63-day VWAP Z-score."""
    vwap = _rolling_vwap(arg_closeadj, arg_volume, 63)
    z = _vwap_z(arg_closeadj, vwap, 63)
    res = _jerk(z, 10, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_z_63d_jerk_21d_5d_v068_signal(arg_closeadj, arg_volume) -> pd.Series:
    """21d-5d jerk of 63-day VWAP Z-score."""
    vwap = _rolling_vwap(arg_closeadj, arg_volume, 63)
    z = _vwap_z(arg_closeadj, vwap, 63)
    res = _jerk(z, 21, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_z_126d_jerk_1d_1d_v069_signal(arg_closeadj, arg_volume) -> pd.Series:
    """1d-1d jerk of 126-day VWAP Z-score."""
    vwap = _rolling_vwap(arg_closeadj, arg_volume, 126)
    z = _vwap_z(arg_closeadj, vwap, 126)
    res = _jerk(z, 1, 1)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_z_126d_jerk_21d_5d_v070_signal(arg_closeadj, arg_volume) -> pd.Series:
    """21d-5d jerk of 126-day VWAP Z-score."""
    vwap = _rolling_vwap(arg_closeadj, arg_volume, 126)
    z = _vwap_z(arg_closeadj, vwap, 126)
    res = _jerk(z, 21, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_z_252d_jerk_1d_1d_v071_signal(arg_closeadj, arg_volume) -> pd.Series:
    """1d-1d jerk of 252-day VWAP Z-score."""
    vwap = _rolling_vwap(arg_closeadj, arg_volume, 252)
    z = _vwap_z(arg_closeadj, vwap, 252)
    res = _jerk(z, 1, 1)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_z_252d_jerk_63d_10d_v072_signal(arg_closeadj, arg_volume) -> pd.Series:
    """63d-10d jerk of 252-day VWAP Z-score."""
    vwap = _rolling_vwap(arg_closeadj, arg_volume, 252)
    z = _vwap_z(arg_closeadj, vwap, 252)
    res = _jerk(z, 63, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_z_5d_tp_jerk_3d_1d_v073_signal(arg_high, arg_low, arg_close, arg_volume) -> pd.Series:
    """3d-1d jerk of 5-day typical-price VWAP Z-score."""
    tp = _typical_price(arg_high, arg_low, arg_close)
    vwap = _rolling_vwap(tp, arg_volume, 5)
    z = _vwap_z(tp, vwap, 5)
    res = _jerk(z, 3, 1)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_z_5d_tp_jerk_5d_1d_v074_signal(arg_high, arg_low, arg_close, arg_volume) -> pd.Series:
    """5d-1d jerk of 5-day typical-price VWAP Z-score."""
    tp = _typical_price(arg_high, arg_low, arg_close)
    vwap = _rolling_vwap(tp, arg_volume, 5)
    z = _vwap_z(tp, vwap, 5)
    res = _jerk(z, 5, 1)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_z_21d_tp_jerk_1d_1d_v075_signal(arg_high, arg_low, arg_close, arg_volume) -> pd.Series:
    """1d-1d jerk of 21-day typical-price VWAP Z-score."""
    tp = _typical_price(arg_high, arg_low, arg_close)
    vwap = _rolling_vwap(tp, arg_volume, 21)
    z = _vwap_z(tp, vwap, 21)
    res = _jerk(z, 1, 1)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_z_21d_tp_jerk_5d_1d_v076_signal(arg_high, arg_low, arg_close, arg_volume) -> pd.Series:
    """5d-1d jerk of 21-day typical-price VWAP Z-score."""
    tp = _typical_price(arg_high, arg_low, arg_close)
    vwap = _rolling_vwap(tp, arg_volume, 21)
    z = _vwap_z(tp, vwap, 21)
    res = _jerk(z, 5, 1)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_z_63d_tp_jerk_1d_1d_v077_signal(arg_highadj, arg_lowadj, arg_closeadj, arg_volume) -> pd.Series:
    """1d-1d jerk of 63-day typical-price VWAP Z-score."""
    tp = _typical_price(arg_highadj, arg_lowadj, arg_closeadj)
    vwap = _rolling_vwap(tp, arg_volume, 63)
    z = _vwap_z(tp, vwap, 63)
    res = _jerk(z, 1, 1)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_z_63d_tp_jerk_10d_5d_v078_signal(arg_highadj, arg_lowadj, arg_closeadj, arg_volume) -> pd.Series:
    """10d-5d jerk of 63-day typical-price VWAP Z-score."""
    tp = _typical_price(arg_highadj, arg_lowadj, arg_closeadj)
    vwap = _rolling_vwap(tp, arg_volume, 63)
    z = _vwap_z(tp, vwap, 63)
    res = _jerk(z, 10, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_z_126d_tp_jerk_5d_1d_v079_signal(arg_highadj, arg_lowadj, arg_closeadj, arg_volume) -> pd.Series:
    """5d-1d jerk of 126-day typical-price VWAP Z-score."""
    tp = _typical_price(arg_highadj, arg_lowadj, arg_closeadj)
    vwap = _rolling_vwap(tp, arg_volume, 126)
    z = _vwap_z(tp, vwap, 126)
    res = _jerk(z, 5, 1)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_z_252d_tp_jerk_21d_5d_v080_signal(arg_highadj, arg_lowadj, arg_closeadj, arg_volume) -> pd.Series:
    """21d-5d jerk of 252-day typical-price VWAP Z-score."""
    tp = _typical_price(arg_highadj, arg_lowadj, arg_closeadj)
    vwap = _rolling_vwap(tp, arg_volume, 252)
    z = _vwap_z(tp, vwap, 252)
    res = _jerk(z, 21, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_z_5d_ema_21d_jerk_1d_1d_v081_signal(arg_close, arg_volume) -> pd.Series:
    """1d-1d jerk of 21-day EMA of 5-day VWAP Z-score."""
    vwap = _rolling_vwap(arg_close, arg_volume, 5)
    z = _vwap_z(arg_close, vwap, 5)
    res = _jerk(z.ewm(span=21).mean(), 1, 1)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_z_21d_ema_63d_jerk_5d_1d_v082_signal(arg_close, arg_volume) -> pd.Series:
    """5d-1d jerk of 63-day EMA of 21-day VWAP Z-score."""
    vwap = _rolling_vwap(arg_close, arg_volume, 21)
    z = _vwap_z(arg_close, vwap, 21)
    res = _jerk(z.ewm(span=63).mean(), 5, 1)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_z_63d_ema_126d_jerk_10d_5d_v083_signal(arg_closeadj, arg_volume) -> pd.Series:
    """10d-5d jerk of 126-day EMA of 63-day VWAP Z-score."""
    vwap = _rolling_vwap(arg_closeadj, arg_volume, 63)
    z = _vwap_z(arg_closeadj, vwap, 63)
    res = _jerk(z.ewm(span=126).mean(), 10, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_dist_5d_roc_1d_jerk_1d_1d_v084_signal(arg_close, arg_volume) -> pd.Series:
    """1d-1d jerk of 1-day diff of 5-day VWAP distance."""
    vwap = _rolling_vwap(arg_close, arg_volume, 5)
    dist = _vwap_dist_val(arg_close, vwap)
    res = dist.diff(1).diff(1)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_dist_21d_roc_5d_jerk_5d_1d_v085_signal(arg_close, arg_volume) -> pd.Series:
    """5d-1d jerk of 5-day diff of 21-day VWAP distance."""
    vwap = _rolling_vwap(arg_close, arg_volume, 21)
    dist = _vwap_dist_val(arg_close, vwap)
    res = dist.diff(5).diff(1)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_dist_63d_roc_10d_jerk_10d_5d_v086_signal(arg_closeadj, arg_volume) -> pd.Series:
    """10d-5d jerk of 10-day diff of 63-day VWAP distance."""
    vwap = _rolling_vwap(arg_closeadj, arg_volume, 63)
    dist = _vwap_dist_val(arg_closeadj, vwap)
    res = dist.diff(10).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_z_5d_roc_1d_jerk_1d_1d_v087_signal(arg_close, arg_volume) -> pd.Series:
    """1d-1d jerk of 1-day diff of 5-day VWAP Z-score."""
    vwap = _rolling_vwap(arg_close, arg_volume, 5)
    z = _vwap_z(arg_close, vwap, 5)
    res = z.diff(1).diff(1)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_z_21d_roc_5d_jerk_5d_1d_v088_signal(arg_close, arg_volume) -> pd.Series:
    """5d-1d jerk of 5-day diff of 21-day VWAP Z-score."""
    vwap = _rolling_vwap(arg_close, arg_volume, 21)
    z = _vwap_z(arg_close, vwap, 21)
    res = z.diff(5).diff(1)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_z_63d_roc_10d_jerk_10d_5d_v089_signal(arg_closeadj, arg_volume) -> pd.Series:
    """10d-5d jerk of 10-day diff of 63-day VWAP Z-score."""
    vwap = _rolling_vwap(arg_closeadj, arg_volume, 63)
    z = _vwap_z(arg_closeadj, vwap, 63)
    res = z.diff(10).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_dist_5d_tp_roc_1d_jerk_1d_1d_v090_signal(arg_high, arg_low, arg_close, arg_volume) -> pd.Series:
    """1d-1d jerk of 1-day diff of 5-day typical-price VWAP distance."""
    tp = _typical_price(arg_high, arg_low, arg_close)
    vwap = _rolling_vwap(tp, arg_volume, 5)
    dist = _vwap_dist_val(tp, vwap)
    res = dist.diff(1).diff(1)
    return res.replace([np.inf, -np.inf], np.nan)

# V091-V120: More variations with open and median prices
def f25vd_vwap_dist_5d_open_jerk_1d_1d_v091_signal(arg_open, arg_close, arg_volume) -> pd.Series:
    """1d-1d jerk of 5-day open-price VWAP distance."""
    vwap = _rolling_vwap(arg_close, arg_volume, 5)
    dist = _vwap_dist_val(arg_open, vwap)
    res = _jerk(dist, 1, 1)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_dist_21d_open_jerk_5d_1d_v092_signal(arg_open, arg_close, arg_volume) -> pd.Series:
    """5d-1d jerk of 21-day open-price VWAP distance."""
    vwap = _rolling_vwap(arg_close, arg_volume, 21)
    dist = _vwap_dist_val(arg_open, vwap)
    res = _jerk(dist, 5, 1)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_dist_63d_open_jerk_10d_5d_v093_signal(arg_openadj, arg_closeadj, arg_volume) -> pd.Series:
    """10d-5d jerk of 63-day openadj-price VWAP distance."""
    vwap = _rolling_vwap(arg_closeadj, arg_volume, 63)
    dist = _vwap_dist_val(arg_openadj, vwap)
    res = _jerk(dist, 10, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_dist_5d_median_jerk_1d_1d_v094_signal(arg_high, arg_low, arg_close, arg_volume) -> pd.Series:
    """1d-1d jerk of 5-day median-price VWAP distance."""
    median = (arg_high + arg_low) / 2.0
    vwap = _rolling_vwap(arg_close, arg_volume, 5)
    dist = _vwap_dist_val(median, vwap)
    res = _jerk(dist, 1, 1)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_dist_21d_median_jerk_5d_1d_v095_signal(arg_high, arg_low, arg_close, arg_volume) -> pd.Series:
    """5d-1d jerk of 21-day median-price VWAP distance."""
    median = (arg_high + arg_low) / 2.0
    vwap = _rolling_vwap(arg_close, arg_volume, 21)
    dist = _vwap_dist_val(median, vwap)
    res = _jerk(dist, 5, 1)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_dist_63d_median_jerk_10d_5d_v096_signal(arg_highadj, arg_lowadj, arg_closeadj, arg_volume) -> pd.Series:
    """10d-5d jerk of 63-day medianadj-price VWAP distance."""
    median = (arg_highadj + arg_lowadj) / 2.0
    vwap = _rolling_vwap(arg_closeadj, arg_volume, 63)
    dist = _vwap_dist_val(median, vwap)
    res = _jerk(dist, 10, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_z_5d_open_jerk_1d_1d_v097_signal(arg_open, arg_close, arg_volume) -> pd.Series:
    """1d-1d jerk of 5-day open-price VWAP Z-score."""
    vwap = _rolling_vwap(arg_close, arg_volume, 5)
    z = _vwap_z(arg_open, vwap, 5)
    res = _jerk(z, 1, 1)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_z_21d_open_jerk_5d_1d_v098_signal(arg_open, arg_close, arg_volume) -> pd.Series:
    """5d-1d jerk of 21-day open-price VWAP Z-score."""
    vwap = _rolling_vwap(arg_close, arg_volume, 21)
    z = _vwap_z(arg_open, vwap, 21)
    res = _jerk(z, 5, 1)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_z_63d_open_jerk_10d_5d_v099_signal(arg_openadj, arg_closeadj, arg_volume) -> pd.Series:
    """10d-5d jerk of 63-day openadj-price VWAP Z-score."""
    vwap = _rolling_vwap(arg_closeadj, arg_volume, 63)
    z = _vwap_z(arg_openadj, vwap, 63)
    res = _jerk(z, 10, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_z_5d_median_jerk_1d_1d_v100_signal(arg_high, arg_low, arg_close, arg_volume) -> pd.Series:
    """1d-1d jerk of 5-day median-price VWAP Z-score."""
    median = (arg_high + arg_low) / 2.0
    vwap = _rolling_vwap(arg_close, arg_volume, 5)
    z = _vwap_z(median, vwap, 5)
    res = _jerk(z, 1, 1)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_cross_5d_21d_jerk_1d_1d_v101_signal(arg_close, arg_volume) -> pd.Series:
    """1d-1d jerk of crossing of 5-day and 21-day VWAPs."""
    vwap5 = _rolling_vwap(arg_close, arg_volume, 5)
    vwap21 = _rolling_vwap(arg_close, arg_volume, 21)
    cross = (vwap5 - vwap21) / vwap21.abs().replace(0, np.nan)
    res = _jerk(cross, 1, 1)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_cross_21d_63d_jerk_5d_1d_v102_signal(arg_close, arg_closeadj, arg_volume) -> pd.Series:
    """5d-1d jerk of crossing of 21-day and 63-day VWAPs."""
    vwap21 = _rolling_vwap(arg_close, arg_volume, 21)
    vwap63 = _rolling_vwap(arg_closeadj, arg_volume, 63)
    cross = (vwap21 - vwap63) / vwap63.abs().replace(0, np.nan)
    res = _jerk(cross, 5, 1)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_cross_63d_252d_jerk_10d_5d_v103_signal(arg_closeadj, arg_volume) -> pd.Series:
    """10d-5d jerk of crossing of 63-day and 252-day VWAPs."""
    vwap63 = _rolling_vwap(arg_closeadj, arg_volume, 63)
    vwap252 = _rolling_vwap(arg_closeadj, arg_volume, 252)
    cross = (vwap63 - vwap252) / vwap252.abs().replace(0, np.nan)
    res = _jerk(cross, 10, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_cross_5d_tp_21d_tp_jerk_1d_1d_v104_signal(arg_high, arg_low, arg_close, arg_volume) -> pd.Series:
    """1d-1d jerk of crossing of 5-day and 21-day typical-price VWAPs."""
    tp = _typical_price(arg_high, arg_low, arg_close)
    vwap5 = _rolling_vwap(tp, arg_volume, 5)
    vwap21 = _rolling_vwap(tp, arg_volume, 21)
    cross = (vwap5 - vwap21) / vwap21.abs().replace(0, np.nan)
    res = _jerk(cross, 1, 1)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_cross_21d_tp_63d_tp_jerk_5d_1d_v105_signal(arg_high, arg_low, arg_close, arg_highadj, arg_lowadj, arg_closeadj, arg_volume) -> pd.Series:
    """5d-1d jerk of crossing of 21-day and 63-day typical-price VWAPs."""
    tp21 = _typical_price(arg_high, arg_low, arg_close)
    tp63 = _typical_price(arg_highadj, arg_lowadj, arg_closeadj)
    vwap21 = _rolling_vwap(tp21, arg_volume, 21)
    vwap63 = _rolling_vwap(tp63, arg_volume, 63)
    cross = (vwap21 - vwap63) / vwap63.abs().replace(0, np.nan)
    res = _jerk(cross, 5, 1)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_price_vs_vwap_mom_5d_jerk_1d_1d_v106_signal(arg_close, arg_volume) -> pd.Series:
    """1d-1d jerk of 5-day price momentum relative to 5-day VWAP."""
    vwap = _rolling_vwap(arg_close, arg_volume, 5)
    ratio = arg_close / vwap.abs().replace(0, np.nan)
    mom = ratio / ratio.shift(5) - 1
    res = _jerk(mom, 1, 1)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_price_vs_vwap_mom_21d_jerk_5d_1d_v107_signal(arg_close, arg_volume) -> pd.Series:
    """5d-1d jerk of 21-day price momentum relative to 21-day VWAP."""
    vwap = _rolling_vwap(arg_close, arg_volume, 21)
    ratio = arg_close / vwap.abs().replace(0, np.nan)
    mom = ratio / ratio.shift(21) - 1
    res = _jerk(mom, 5, 1)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_dist_5d_max_21d_jerk_1d_1d_v108_signal(arg_close, arg_volume) -> pd.Series:
    """1d-1d jerk of 21-day max of 5-day VWAP distance."""
    vwap = _rolling_vwap(arg_close, arg_volume, 5)
    dist = _vwap_dist_val(arg_close, vwap)
    res = _jerk(dist.rolling(21).max(), 1, 1)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_dist_5d_min_21d_jerk_1d_1d_v109_signal(arg_close, arg_volume) -> pd.Series:
    """1d-1d jerk of 21-day min of 5-day VWAP distance."""
    vwap = _rolling_vwap(arg_close, arg_volume, 5)
    dist = _vwap_dist_val(arg_close, vwap)
    res = _jerk(dist.rolling(21).min(), 1, 1)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_z_5d_std_21d_jerk_1d_1d_v110_signal(arg_close, arg_volume) -> pd.Series:
    """1d-1d jerk of 21-day std of 5-day VWAP Z-score."""
    vwap = _rolling_vwap(arg_close, arg_volume, 5)
    z = _vwap_z(arg_close, vwap, 5)
    res = _jerk(z.rolling(21).std(), 1, 1)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_dist_5d_skew_63d_jerk_5d_1d_v111_signal(arg_close, arg_volume) -> pd.Series:
    """5d-1d jerk of 63-day skew of 5-day VWAP distance."""
    vwap = _rolling_vwap(arg_close, arg_volume, 5)
    dist = _vwap_dist_val(arg_close, vwap)
    res = _jerk(dist.rolling(63).skew(), 5, 1)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_dist_21d_kurt_126d_jerk_10d_5d_v112_signal(arg_close, arg_volume) -> pd.Series:
    """10d-5d jerk of 126-day kurtosis of 21-day VWAP distance."""
    vwap = _rolling_vwap(arg_close, arg_volume, 21)
    dist = _vwap_dist_val(arg_close, vwap)
    res = _jerk(dist.rolling(126).kurt(), 10, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_dist_5d_roc_3d_jerk_1d_v113_signal(arg_close, arg_volume) -> pd.Series:
    """1d jerk of 3-day diff of 5-day VWAP distance."""
    vwap = _rolling_vwap(arg_close, arg_volume, 5)
    dist = _vwap_dist_val(arg_close, vwap)
    res = dist.diff(3).diff(1)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_dist_21d_roc_1d_jerk_5d_v114_signal(arg_close, arg_volume) -> pd.Series:
    """5d jerk of 1-day diff of 21-day VWAP distance."""
    vwap = _rolling_vwap(arg_close, arg_volume, 21)
    dist = _vwap_dist_val(arg_close, vwap)
    res = dist.diff(1).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_z_5d_roc_3d_jerk_1d_v115_signal(arg_close, arg_volume) -> pd.Series:
    """1d jerk of 3-day diff of 5-day VWAP Z-score."""
    vwap = _rolling_vwap(arg_close, arg_volume, 5)
    z = _vwap_z(arg_close, vwap, 5)
    res = z.diff(3).diff(1)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_z_21d_roc_1d_jerk_5d_v116_signal(arg_close, arg_volume) -> pd.Series:
    """5d jerk of 1-day diff of 21-day VWAP Z-score."""
    vwap = _rolling_vwap(arg_close, arg_volume, 21)
    z = _vwap_z(arg_close, vwap, 21)
    res = z.diff(1).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_dist_5d_tp_roc_3d_jerk_1d_v117_signal(arg_high, arg_low, arg_close, arg_volume) -> pd.Series:
    """1d jerk of 3-day diff of 5-day typical-price VWAP distance."""
    tp = _typical_price(arg_high, arg_low, arg_close)
    vwap = _rolling_vwap(tp, arg_volume, 5)
    dist = _vwap_dist_val(tp, vwap)
    res = dist.diff(3).diff(1)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_z_5d_tp_roc_1d_jerk_3d_v118_signal(arg_high, arg_low, arg_close, arg_volume) -> pd.Series:
    """3d jerk of 1-day diff of 5-day typical-price VWAP Z-score."""
    tp = _typical_price(arg_high, arg_low, arg_close)
    vwap = _rolling_vwap(tp, arg_volume, 5)
    z = _vwap_z(tp, vwap, 5)
    res = z.diff(1).diff(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_dist_21d_tp_roc_5d_jerk_1d_v119_signal(arg_high, arg_low, arg_close, arg_volume) -> pd.Series:
    """1d jerk of 5-day diff of 21-day typical-price VWAP distance."""
    tp = _typical_price(arg_high, arg_low, arg_close)
    vwap = _rolling_vwap(tp, arg_volume, 21)
    dist = _vwap_dist_val(tp, vwap)
    res = dist.diff(5).diff(1)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_z_21d_tp_roc_3d_jerk_5d_v120_signal(arg_high, arg_low, arg_close, arg_volume) -> pd.Series:
    """5d jerk of 3-day diff of 21-day typical-price VWAP Z-score."""
    tp = _typical_price(arg_high, arg_low, arg_close)
    vwap = _rolling_vwap(tp, arg_volume, 21)
    z = _vwap_z(tp, vwap, 21)
    res = z.diff(3).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

# V121-V150: Additional variety to reach 150
def f25vd_vwap_dist_5d_lag_1d_jerk_1d_1d_v121_signal(arg_close, arg_volume) -> pd.Series:
    """1d-1d jerk of 1-day lagged 5-day VWAP distance."""
    vwap = _rolling_vwap(arg_close, arg_volume, 5)
    dist = _vwap_dist_val(arg_close, vwap).shift(1)
    res = _jerk(dist, 1, 1)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_dist_21d_lag_5d_jerk_5d_1d_v122_signal(arg_close, arg_volume) -> pd.Series:
    """5d-1d jerk of 5-day lagged 21-day VWAP distance."""
    vwap = _rolling_vwap(arg_close, arg_volume, 21)
    dist = _vwap_dist_val(arg_close, vwap).shift(5)
    res = _jerk(dist, 5, 1)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_z_5d_lag_1d_jerk_1d_1d_v123_signal(arg_close, arg_volume) -> pd.Series:
    """1d-1d jerk of 1-day lagged 5-day VWAP Z-score."""
    vwap = _rolling_vwap(arg_close, arg_volume, 5)
    z = _vwap_z(arg_close, vwap, 5).shift(1)
    res = _jerk(z, 1, 1)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_z_21d_lag_5d_jerk_5d_1d_v124_signal(arg_close, arg_volume) -> pd.Series:
    """5d-1d jerk of 5-day lagged 21-day VWAP Z-score."""
    vwap = _rolling_vwap(arg_close, arg_volume, 21)
    z = _vwap_z(arg_close, vwap, 21).shift(5)
    res = _jerk(z, 5, 1)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_dist_5d_jerk_vs_21d_v125_signal(arg_close, arg_volume) -> pd.Series:
    """Difference between 1d-1d jerk of 5-day VWAP distance and its 21-day SMA jerk."""
    vwap = _rolling_vwap(arg_close, arg_volume, 5)
    dist = _vwap_dist_val(arg_close, vwap)
    res = _jerk(dist, 1, 1) - _jerk(dist.rolling(21).mean(), 1, 1)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_dist_21d_jerk_vs_63d_v126_signal(arg_close, arg_volume) -> pd.Series:
    """Difference between 1d-1d jerk of 21-day VWAP distance and its 63-day SMA jerk."""
    vwap = _rolling_vwap(arg_close, arg_volume, 21)
    dist = _vwap_dist_val(arg_close, vwap)
    res = _jerk(dist, 1, 1) - _jerk(dist.rolling(63).mean(), 1, 1)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_z_5d_jerk_vs_21d_v127_signal(arg_close, arg_volume) -> pd.Series:
    """Difference between 1d-1d jerk of 5-day VWAP Z-score and its 21-day SMA jerk."""
    vwap = _rolling_vwap(arg_close, arg_volume, 5)
    z = _vwap_z(arg_close, vwap, 5)
    res = _jerk(z, 1, 1) - _jerk(z.rolling(21).mean(), 1, 1)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_z_21d_jerk_vs_63d_v128_signal(arg_close, arg_volume) -> pd.Series:
    """Difference between 1d-1d jerk of 21-day VWAP Z-score and its 63-day SMA jerk."""
    vwap = _rolling_vwap(arg_close, arg_volume, 21)
    z = _vwap_z(arg_close, vwap, 21)
    res = _jerk(z, 1, 1) - _jerk(z.rolling(63).mean(), 1, 1)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_dist_5d_norm_jerk_1d_1d_v129_signal(arg_close, arg_volume) -> pd.Series:
    """1d-1d jerk of normalized 5-day VWAP distance."""
    vwap = _rolling_vwap(arg_close, arg_volume, 5)
    dist = _vwap_dist_val(arg_close, vwap)
    vol = arg_close.pct_change().rolling(21).std()
    res = _jerk(dist / vol.replace(0, np.nan), 1, 1)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_dist_21d_norm_jerk_5d_1d_v130_signal(arg_close, arg_volume) -> pd.Series:
    """5d-1d jerk of normalized 21-day VWAP distance."""
    vwap = _rolling_vwap(arg_close, arg_volume, 21)
    dist = _vwap_dist_val(arg_close, vwap)
    vol = arg_close.pct_change().rolling(63).std()
    res = _jerk(dist / vol.replace(0, np.nan), 5, 1)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_dist_5d_tp_norm_jerk_1d_1d_v131_signal(arg_high, arg_low, arg_close, arg_volume) -> pd.Series:
    """1d-1d jerk of normalized 5-day typical-price VWAP distance."""
    tp = _typical_price(arg_high, arg_low, arg_close)
    vwap = _rolling_vwap(tp, arg_volume, 5)
    dist = _vwap_dist_val(tp, vwap)
    vol = tp.pct_change().rolling(21).std()
    res = _jerk(dist / vol.replace(0, np.nan), 1, 1)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_dist_5d_median_norm_jerk_1d_1d_v132_signal(arg_high, arg_low, arg_close, arg_volume) -> pd.Series:
    """1d-1d jerk of normalized 5-day median-price VWAP distance."""
    median = (arg_high + arg_low) / 2.0
    vwap = _rolling_vwap(arg_close, arg_volume, 5)
    dist = _vwap_dist_val(median, vwap)
    vol = median.pct_change().rolling(21).std()
    res = _jerk(dist / vol.replace(0, np.nan), 1, 1)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_dist_5d_jerk_vol_21d_v133_signal(arg_close, arg_volume) -> pd.Series:
    """21-day volatility of 1d-1d jerk of 5-day VWAP distance."""
    vwap = _rolling_vwap(arg_close, arg_volume, 5)
    dist = _vwap_dist_val(arg_close, vwap)
    res = _jerk(dist, 1, 1).rolling(21).std()
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_dist_21d_jerk_vol_63d_v134_signal(arg_close, arg_volume) -> pd.Series:
    """63-day volatility of 1d-1d jerk of 21-day VWAP distance."""
    vwap = _rolling_vwap(arg_close, arg_volume, 21)
    dist = _vwap_dist_val(arg_close, vwap)
    res = _jerk(dist, 1, 1).rolling(63).std()
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_z_5d_jerk_vol_21d_v135_signal(arg_close, arg_volume) -> pd.Series:
    """21-day volatility of 1d-1d jerk of 5-day VWAP Z-score."""
    vwap = _rolling_vwap(arg_close, arg_volume, 5)
    z = _vwap_z(arg_close, vwap, 5)
    res = _jerk(z, 1, 1).rolling(21).std()
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_z_21d_jerk_vol_63d_v136_signal(arg_close, arg_volume) -> pd.Series:
    """63-day volatility of 1d-1d jerk of 21-day VWAP Z-score."""
    vwap = _rolling_vwap(arg_close, arg_volume, 21)
    z = _vwap_z(arg_close, vwap, 21)
    res = _jerk(z, 1, 1).rolling(63).std()
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_dist_5d_jerk_ema_21d_v137_signal(arg_close, arg_volume) -> pd.Series:
    """21-day EMA of 1d-1d jerk of 5-day VWAP distance."""
    vwap = _rolling_vwap(arg_close, arg_volume, 5)
    dist = _vwap_dist_val(arg_close, vwap)
    res = _jerk(dist, 1, 1).ewm(span=21).mean()
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_dist_21d_jerk_ema_63d_v138_signal(arg_close, arg_volume) -> pd.Series:
    """63-day EMA of 1d-1d jerk of 21-day VWAP distance."""
    vwap = _rolling_vwap(arg_close, arg_volume, 21)
    dist = _vwap_dist_val(arg_close, vwap)
    res = _jerk(dist, 1, 1).ewm(span=63).mean()
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_z_5d_jerk_ema_21d_v139_signal(arg_close, arg_volume) -> pd.Series:
    """21-day EMA of 1d-1d jerk of 5-day VWAP Z-score."""
    vwap = _rolling_vwap(arg_close, arg_volume, 5)
    z = _vwap_z(arg_close, vwap, 5)
    res = _jerk(z, 1, 1).ewm(span=21).mean()
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_z_21d_jerk_ema_63d_v140_signal(arg_close, arg_volume) -> pd.Series:
    """63-day EMA of 1d-1d jerk of 21-day VWAP Z-score."""
    vwap = _rolling_vwap(arg_close, arg_volume, 21)
    z = _vwap_z(arg_close, vwap, 21)
    res = _jerk(z, 1, 1).ewm(span=63).mean()
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_dist_5d_tp_jerk_ema_21d_v141_signal(arg_high, arg_low, arg_close, arg_volume) -> pd.Series:
    """21-day EMA of 1d-1d jerk of 5-day typical-price VWAP distance."""
    tp = _typical_price(arg_high, arg_low, arg_close)
    vwap = _rolling_vwap(tp, arg_volume, 5)
    dist = _vwap_dist_val(tp, vwap)
    res = _jerk(dist, 1, 1).ewm(span=21).mean()
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_z_5d_tp_jerk_ema_21d_v142_signal(arg_high, arg_low, arg_close, arg_volume) -> pd.Series:
    """21-day EMA of 1d-1d jerk of 5-day typical-price VWAP Z-score."""
    tp = _typical_price(arg_high, arg_low, arg_close)
    vwap = _rolling_vwap(tp, arg_volume, 5)
    z = _vwap_z(tp, vwap, 5)
    res = _jerk(z, 1, 1).ewm(span=21).mean()
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_dist_5d_median_jerk_ema_21d_v143_signal(arg_high, arg_low, arg_close, arg_volume) -> pd.Series:
    """21-day EMA of 1d-1d jerk of 5-day median-price VWAP distance."""
    median = (arg_high + arg_low) / 2.0
    vwap = _rolling_vwap(arg_close, arg_volume, 5)
    dist = _vwap_dist_val(median, vwap)
    res = _jerk(dist, 1, 1).ewm(span=21).mean()
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_z_5d_median_jerk_ema_21d_v144_signal(arg_high, arg_low, arg_close, arg_volume) -> pd.Series:
    """21-day EMA of 1d-1d jerk of 5-day median-price VWAP Z-score."""
    median = (arg_high + arg_low) / 2.0
    vwap = _rolling_vwap(arg_close, arg_volume, 5)
    z = _vwap_z(median, vwap, 5)
    res = _jerk(z, 1, 1).ewm(span=21).mean()
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_dist_5d_jerk_std_63d_v145_signal(arg_close, arg_volume) -> pd.Series:
    """63-day standard deviation of 1d-1d jerk of 5-day VWAP distance."""
    vwap = _rolling_vwap(arg_close, arg_volume, 5)
    dist = _vwap_dist_val(arg_close, vwap)
    res = _jerk(dist, 1, 1).rolling(63).std()
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_z_5d_jerk_std_63d_v146_signal(arg_close, arg_volume) -> pd.Series:
    """63-day standard deviation of 1d-1d jerk of 5-day VWAP Z-score."""
    vwap = _rolling_vwap(arg_close, arg_volume, 5)
    z = _vwap_z(arg_close, vwap, 5)
    res = _jerk(z, 1, 1).rolling(63).std()
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_dist_21d_jerk_std_126d_v147_signal(arg_close, arg_volume) -> pd.Series:
    """126-day standard deviation of 5d-1d jerk of 21-day VWAP distance."""
    vwap = _rolling_vwap(arg_close, arg_volume, 21)
    dist = _vwap_dist_val(arg_close, vwap)
    res = _jerk(dist, 5, 1).rolling(126).std()
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_z_21d_jerk_std_126d_v148_signal(arg_close, arg_volume) -> pd.Series:
    """126-day standard deviation of 5d-1d jerk of 21-day VWAP Z-score."""
    vwap = _rolling_vwap(arg_close, arg_volume, 21)
    z = _vwap_z(arg_close, vwap, 21)
    res = _jerk(z, 5, 1).rolling(126).std()
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_dist_5d_jerk_skew_126d_v149_signal(arg_close, arg_volume) -> pd.Series:
    """126-day skewness of 1d-1d jerk of 5-day VWAP distance."""
    vwap = _rolling_vwap(arg_close, arg_volume, 5)
    dist = _vwap_dist_val(arg_close, vwap)
    res = _jerk(dist, 1, 1).rolling(126).skew()
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_z_5d_jerk_kurt_126d_v150_signal(arg_close, arg_volume) -> pd.Series:
    """126-day kurtosis of 1d-1d jerk of 5-day VWAP Z-score."""
    vwap = _rolling_vwap(arg_close, arg_volume, 5)
    z = _vwap_z(arg_close, vwap, 5)
    res = _jerk(z, 1, 1).rolling(126).kurt()
    return res.replace([np.inf, -np.inf], np.nan)

SILVERDB_ACCESS, SOURCE_TABLE, ENTITY_COLUMN, DATE_COLUMN = "read_only", "sep", "ticker", "date"
ORDER_BY, NO_FORWARD_LOOKING = [ENTITY_COLUMN, DATE_COLUMN], True
SOURCE_COLUMNS = {c: f"sep.{c.replace('arg_', '')}" for c in ["arg_high", "arg_low", "arg_close", "arg_volume", "arg_highadj", "arg_lowadj", "arg_closeadj", "arg_open", "arg_openadj"]}

F25_VWAP_DEVIATION_JERK_REGISTRY_001_150 = {
    n: {
        "inputs": (inputs := [v for v in globals()[n].__code__.co_varnames[:globals()[n].__code__.co_argcount]]),
        "source_table": SOURCE_TABLE,
        "source_columns": {c: SOURCE_COLUMNS[c] for c in inputs if c in SOURCE_COLUMNS},
        "entity_column": ENTITY_COLUMN, "date_column": DATE_COLUMN,
        "order_by": ORDER_BY, "no_forward_looking": NO_FORWARD_LOOKING, "func": globals()[n]
    } for n in sorted([k for k in globals() if k.startswith('f25vd_') and k.endswith('_signal')])
}

if __name__ == "__main__":
    import pandas as pd; import numpy as np
    sz = 1000
    np.random.seed(42)
    d = pd.DataFrame({
        "arg_high": pd.Series(100 + np.cumsum(np.random.normal(0, 1, sz)) + 2),
        "arg_low": pd.Series(100 + np.cumsum(np.random.normal(0, 1, sz)) - 2),
        "arg_close": pd.Series(100 + np.cumsum(np.random.normal(0, 1, sz))),
        "arg_open": pd.Series(100 + np.cumsum(np.random.normal(0, 1, sz))),
        "arg_volume": pd.Series(np.random.lognormal(10, 1, sz)),
        "arg_highadj": pd.Series(100 + np.cumsum(np.random.normal(0, 1, sz)) + 2),
        "arg_lowadj": pd.Series(100 + np.cumsum(np.random.normal(0, 1, sz)) - 2),
        "arg_closeadj": pd.Series(100 + np.cumsum(np.random.normal(0, 1, sz))),
        "arg_openadj": pd.Series(100 + np.cumsum(np.random.normal(0, 1, sz))),
        "ticker": ["T"]*sz,
        "date": pd.date_range("2010-01-01", periods=sz)
    })
    for n, c in F25_VWAP_DEVIATION_JERK_REGISTRY_001_150.items():
        r = c["func"](**{i: d[i] for i in c["inputs"]})
        assert len(r) > 0, f"{n} failed len"
        assert r.notna().sum() > 0, f"{n} failed all nan"
    print(f"OK")
