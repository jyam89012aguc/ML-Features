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

# V001-V015: VWAP Distances for various windows using Close price
def f25vd_vwap_dist_5d_base_v001_signal(arg_close, arg_volume) -> pd.Series:
    """VWAP distance for 5-day window using close price."""
    vwap = _rolling_vwap(arg_close, arg_volume, 5)
    res = _vwap_dist_val(arg_close, vwap)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_dist_10d_base_v002_signal(arg_close, arg_volume) -> pd.Series:
    """VWAP distance for 10-day window using close price."""
    vwap = _rolling_vwap(arg_close, arg_volume, 10)
    res = _vwap_dist_val(arg_close, vwap)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_dist_21d_base_v003_signal(arg_close, arg_volume) -> pd.Series:
    """VWAP distance for 21-day window using close price."""
    vwap = _rolling_vwap(arg_close, arg_volume, 21)
    res = _vwap_dist_val(arg_close, vwap)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_dist_42d_base_v004_signal(arg_closeadj, arg_volume) -> pd.Series:
    """VWAP distance for 42-day window using closeadj price."""
    vwap = _rolling_vwap(arg_closeadj, arg_volume, 42)
    res = _vwap_dist_val(arg_closeadj, vwap)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_dist_63d_base_v005_signal(arg_closeadj, arg_volume) -> pd.Series:
    """VWAP distance for 63-day window using closeadj price."""
    vwap = _rolling_vwap(arg_closeadj, arg_volume, 63)
    res = _vwap_dist_val(arg_closeadj, vwap)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_dist_126d_base_v006_signal(arg_closeadj, arg_volume) -> pd.Series:
    """VWAP distance for 126-day window using closeadj price."""
    vwap = _rolling_vwap(arg_closeadj, arg_volume, 126)
    res = _vwap_dist_val(arg_closeadj, vwap)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_dist_252d_base_v007_signal(arg_closeadj, arg_volume) -> pd.Series:
    """VWAP distance for 252-day window using closeadj price."""
    vwap = _rolling_vwap(arg_closeadj, arg_volume, 252)
    res = _vwap_dist_val(arg_closeadj, vwap)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_dist_5d_high_base_v008_signal(arg_high, arg_close, arg_volume) -> pd.Series:
    """VWAP distance for 5-day window using high price relative to close-based VWAP."""
    vwap = _rolling_vwap(arg_close, arg_volume, 5)
    res = _vwap_dist_val(arg_high, vwap)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_dist_21d_high_base_v009_signal(arg_high, arg_close, arg_volume) -> pd.Series:
    """VWAP distance for 21-day window using high price relative to close-based VWAP."""
    vwap = _rolling_vwap(arg_close, arg_volume, 21)
    res = _vwap_dist_val(arg_high, vwap)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_dist_63d_high_base_v010_signal(arg_highadj, arg_closeadj, arg_volume) -> pd.Series:
    """VWAP distance for 63-day window using highadj price relative to closeadj-based VWAP."""
    vwap = _rolling_vwap(arg_closeadj, arg_volume, 63)
    res = _vwap_dist_val(arg_highadj, vwap)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_dist_5d_low_base_v011_signal(arg_low, arg_close, arg_volume) -> pd.Series:
    """VWAP distance for 5-day window using low price relative to close-based VWAP."""
    vwap = _rolling_vwap(arg_close, arg_volume, 5)
    res = _vwap_dist_val(arg_low, vwap)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_dist_21d_low_base_v012_signal(arg_low, arg_close, arg_volume) -> pd.Series:
    """VWAP distance for 21-day window using low price relative to close-based VWAP."""
    vwap = _rolling_vwap(arg_close, arg_volume, 21)
    res = _vwap_dist_val(arg_low, vwap)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_dist_63d_low_base_v013_signal(arg_lowadj, arg_closeadj, arg_volume) -> pd.Series:
    """VWAP distance for 63-day window using lowadj price relative to closeadj-based VWAP."""
    vwap = _rolling_vwap(arg_closeadj, arg_volume, 63)
    res = _vwap_dist_val(arg_lowadj, vwap)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_dist_5d_tp_base_v014_signal(arg_high, arg_low, arg_close, arg_volume) -> pd.Series:
    """VWAP distance for 5-day window using typical price relative to typical-price-based VWAP."""
    tp = _typical_price(arg_high, arg_low, arg_close)
    vwap = _rolling_vwap(tp, arg_volume, 5)
    res = _vwap_dist_val(tp, vwap)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_dist_63d_tp_base_v015_signal(arg_highadj, arg_lowadj, arg_closeadj, arg_volume) -> pd.Series:
    """VWAP distance for 63-day window using typical price relative to typical-price-based VWAP."""
    tp = _typical_price(arg_highadj, arg_lowadj, arg_closeadj)
    vwap = _rolling_vwap(tp, arg_volume, 63)
    res = _vwap_dist_val(tp, vwap)
    return res.replace([np.inf, -np.inf], np.nan)

# V016-V030: VWAP Z-Scores
def f25vd_vwap_z_5d_base_v016_signal(arg_close, arg_volume) -> pd.Series:
    """VWAP z-score for 5-day window using close price."""
    vwap = _rolling_vwap(arg_close, arg_volume, 5)
    res = _vwap_z(arg_close, vwap, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_z_10d_base_v017_signal(arg_close, arg_volume) -> pd.Series:
    """VWAP z-score for 10-day window using close price."""
    vwap = _rolling_vwap(arg_close, arg_volume, 10)
    res = _vwap_z(arg_close, vwap, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_z_21d_base_v018_signal(arg_close, arg_volume) -> pd.Series:
    """VWAP z-score for 21-day window using close price."""
    vwap = _rolling_vwap(arg_close, arg_volume, 21)
    res = _vwap_z(arg_close, vwap, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_z_42d_base_v019_signal(arg_closeadj, arg_volume) -> pd.Series:
    """VWAP z-score for 42-day window using closeadj price."""
    vwap = _rolling_vwap(arg_closeadj, arg_volume, 42)
    res = _vwap_z(arg_closeadj, vwap, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_z_63d_base_v020_signal(arg_closeadj, arg_volume) -> pd.Series:
    """VWAP z-score for 63-day window using closeadj price."""
    vwap = _rolling_vwap(arg_closeadj, arg_volume, 63)
    res = _vwap_z(arg_closeadj, vwap, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_z_126d_base_v021_signal(arg_closeadj, arg_volume) -> pd.Series:
    """VWAP z-score for 126-day window using closeadj price."""
    vwap = _rolling_vwap(arg_closeadj, arg_volume, 126)
    res = _vwap_z(arg_closeadj, vwap, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_z_252d_base_v022_signal(arg_closeadj, arg_volume) -> pd.Series:
    """VWAP z-score for 252-day window using closeadj price."""
    vwap = _rolling_vwap(arg_closeadj, arg_volume, 252)
    res = _vwap_z(arg_closeadj, vwap, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_z_5d_tp_base_v023_signal(arg_high, arg_low, arg_close, arg_volume) -> pd.Series:
    """VWAP z-score for 5-day window using typical price."""
    tp = _typical_price(arg_high, arg_low, arg_close)
    vwap = _rolling_vwap(tp, arg_volume, 5)
    res = _vwap_z(tp, vwap, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_z_21d_tp_base_v024_signal(arg_high, arg_low, arg_close, arg_volume) -> pd.Series:
    """VWAP z-score for 21-day window using typical price."""
    tp = _typical_price(arg_high, arg_low, arg_close)
    vwap = _rolling_vwap(tp, arg_volume, 21)
    res = _vwap_z(tp, vwap, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_z_63d_tp_base_v025_signal(arg_highadj, arg_lowadj, arg_closeadj, arg_volume) -> pd.Series:
    """VWAP z-score for 63-day window using typical price."""
    tp = _typical_price(arg_highadj, arg_lowadj, arg_closeadj)
    vwap = _rolling_vwap(tp, arg_volume, 63)
    res = _vwap_z(tp, vwap, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_z_126d_tp_base_v026_signal(arg_highadj, arg_lowadj, arg_closeadj, arg_volume) -> pd.Series:
    """VWAP z-score for 126-day window using typical price."""
    tp = _typical_price(arg_highadj, arg_lowadj, arg_closeadj)
    vwap = _rolling_vwap(tp, arg_volume, 126)
    res = _vwap_z(tp, vwap, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_z_252d_tp_base_v027_signal(arg_highadj, arg_lowadj, arg_closeadj, arg_volume) -> pd.Series:
    """VWAP z-score for 252-day window using typical price."""
    tp = _typical_price(arg_highadj, arg_lowadj, arg_closeadj)
    vwap = _rolling_vwap(tp, arg_volume, 252)
    res = _vwap_z(tp, vwap, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_z_5d_high_base_v028_signal(arg_high, arg_close, arg_volume) -> pd.Series:
    """VWAP z-score for 5-day window using high price."""
    vwap = _rolling_vwap(arg_close, arg_volume, 5)
    res = _vwap_z(arg_high, vwap, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_z_21d_high_base_v029_signal(arg_high, arg_close, arg_volume) -> pd.Series:
    """VWAP z-score for 21-day window using high price."""
    vwap = _rolling_vwap(arg_close, arg_volume, 21)
    res = _vwap_z(arg_high, vwap, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_z_63d_high_base_v030_signal(arg_highadj, arg_closeadj, arg_volume) -> pd.Series:
    """VWAP z-score for 63-day window using highadj price."""
    vwap = _rolling_vwap(arg_closeadj, arg_volume, 63)
    res = _vwap_z(arg_highadj, vwap, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# V031-V045: Crossings of VWAPs of different windows
def f25vd_vwap_cross_5d_21d_base_v031_signal(arg_close, arg_volume) -> pd.Series:
    """Crossing of 5-day VWAP and 21-day VWAP."""
    vwap5 = _rolling_vwap(arg_close, arg_volume, 5)
    vwap21 = _rolling_vwap(arg_close, arg_volume, 21)
    res = (vwap5 - vwap21) / vwap21.abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_cross_5d_63d_base_v032_signal(arg_close, arg_closeadj, arg_volume) -> pd.Series:
    """Crossing of 5-day VWAP and 63-day VWAP."""
    vwap5 = _rolling_vwap(arg_close, arg_volume, 5)
    vwap63 = _rolling_vwap(arg_closeadj, arg_volume, 63)
    res = (vwap5 - vwap63) / vwap63.abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_cross_21d_63d_base_v033_signal(arg_close, arg_closeadj, arg_volume) -> pd.Series:
    """Crossing of 21-day VWAP and 63-day VWAP."""
    vwap21 = _rolling_vwap(arg_close, arg_volume, 21)
    vwap63 = _rolling_vwap(arg_closeadj, arg_volume, 63)
    res = (vwap21 - vwap63) / vwap63.abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_cross_21d_126d_base_v034_signal(arg_close, arg_closeadj, arg_volume) -> pd.Series:
    """Crossing of 21-day VWAP and 126-day VWAP."""
    vwap21 = _rolling_vwap(arg_close, arg_volume, 21)
    vwap126 = _rolling_vwap(arg_closeadj, arg_volume, 126)
    res = (vwap21 - vwap126) / vwap126.abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_cross_63d_252d_base_v035_signal(arg_closeadj, arg_volume) -> pd.Series:
    """Crossing of 63-day VWAP and 252-day VWAP."""
    vwap63 = _rolling_vwap(arg_closeadj, arg_volume, 63)
    vwap252 = _rolling_vwap(arg_closeadj, arg_volume, 252)
    res = (vwap63 - vwap252) / vwap252.abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_cross_5d_21d_tp_base_v036_signal(arg_high, arg_low, arg_close, arg_volume) -> pd.Series:
    """Crossing of 5-day and 21-day typical price VWAPs."""
    tp = _typical_price(arg_high, arg_low, arg_close)
    vwap5 = _rolling_vwap(tp, arg_volume, 5)
    vwap21 = _rolling_vwap(tp, arg_volume, 21)
    res = (vwap5 - vwap21) / vwap21.abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_cross_21d_63d_tp_base_v037_signal(arg_high, arg_low, arg_close, arg_highadj, arg_lowadj, arg_closeadj, arg_volume) -> pd.Series:
    """Crossing of 21-day and 63-day typical price VWAPs."""
    tp21 = _typical_price(arg_high, arg_low, arg_close)
    tp63 = _typical_price(arg_highadj, arg_lowadj, arg_closeadj)
    vwap21 = _rolling_vwap(tp21, arg_volume, 21)
    vwap63 = _rolling_vwap(tp63, arg_volume, 63)
    res = (vwap21 - vwap63) / vwap63.abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_cross_63d_126d_tp_base_v038_signal(arg_highadj, arg_lowadj, arg_closeadj, arg_volume) -> pd.Series:
    """Crossing of 63-day and 126-day typical price VWAPs."""
    tp = _typical_price(arg_highadj, arg_lowadj, arg_closeadj)
    vwap63 = _rolling_vwap(tp, arg_volume, 63)
    vwap126 = _rolling_vwap(tp, arg_volume, 126)
    res = (vwap63 - vwap126) / vwap126.abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_cross_126d_252d_tp_base_v039_signal(arg_highadj, arg_lowadj, arg_closeadj, arg_volume) -> pd.Series:
    """Crossing of 126-day and 252-day typical price VWAPs."""
    tp = _typical_price(arg_highadj, arg_lowadj, arg_closeadj)
    vwap126 = _rolling_vwap(tp, arg_volume, 126)
    vwap252 = _rolling_vwap(tp, arg_volume, 252)
    res = (vwap126 - vwap252) / vwap252.abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_cross_10d_42d_base_v040_signal(arg_close, arg_closeadj, arg_volume) -> pd.Series:
    """Crossing of 10-day and 42-day VWAPs."""
    vwap10 = _rolling_vwap(arg_close, arg_volume, 10)
    vwap42 = _rolling_vwap(arg_closeadj, arg_volume, 42)
    res = (vwap10 - vwap42) / vwap42.abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_cross_5d_10d_base_v041_signal(arg_close, arg_volume) -> pd.Series:
    """Crossing of 5-day and 10-day VWAPs."""
    vwap5 = _rolling_vwap(arg_close, arg_volume, 5)
    vwap10 = _rolling_vwap(arg_close, arg_volume, 10)
    res = (vwap5 - vwap10) / vwap10.abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_cross_10d_21d_base_v042_signal(arg_close, arg_volume) -> pd.Series:
    """Crossing of 10-day and 21-day VWAPs."""
    vwap10 = _rolling_vwap(arg_close, arg_volume, 10)
    vwap21 = _rolling_vwap(arg_close, arg_volume, 21)
    res = (vwap10 - vwap21) / vwap21.abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_cross_42d_63d_base_v043_signal(arg_closeadj, arg_volume) -> pd.Series:
    """Crossing of 42-day and 63-day VWAPs."""
    vwap42 = _rolling_vwap(arg_closeadj, arg_volume, 42)
    vwap63 = _rolling_vwap(arg_closeadj, arg_volume, 63)
    res = (vwap42 - vwap63) / vwap63.abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_cross_63d_126d_base_v044_signal(arg_closeadj, arg_volume) -> pd.Series:
    """Crossing of 63-day and 126-day VWAPs."""
    vwap63 = _rolling_vwap(arg_closeadj, arg_volume, 63)
    vwap126 = _rolling_vwap(arg_closeadj, arg_volume, 126)
    res = (vwap63 - vwap126) / vwap126.abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_cross_126d_252d_base_v045_signal(arg_closeadj, arg_volume) -> pd.Series:
    """Crossing of 126-day and 252-day VWAPs."""
    vwap126 = _rolling_vwap(arg_closeadj, arg_volume, 126)
    vwap252 = _rolling_vwap(arg_closeadj, arg_volume, 252)
    res = (vwap126 - vwap252) / vwap252.abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# V046-V060: Momentum of price relative to VWAP
def f25vd_price_vs_vwap_mom_5d_base_v046_signal(arg_close, arg_volume) -> pd.Series:
    """5-day momentum of price relative to 5-day VWAP."""
    vwap = _rolling_vwap(arg_close, arg_volume, 5)
    ratio = arg_close / vwap.abs().replace(0, np.nan)
    res = ratio / ratio.shift(5) - 1
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_price_vs_vwap_mom_21d_base_v047_signal(arg_close, arg_volume) -> pd.Series:
    """21-day momentum of price relative to 21-day VWAP."""
    vwap = _rolling_vwap(arg_close, arg_volume, 21)
    ratio = arg_close / vwap.abs().replace(0, np.nan)
    res = ratio / ratio.shift(21) - 1
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_price_vs_vwap_mom_63d_base_v048_signal(arg_closeadj, arg_volume) -> pd.Series:
    """63-day momentum of price relative to 63-day VWAP."""
    vwap = _rolling_vwap(arg_closeadj, arg_volume, 63)
    ratio = arg_closeadj / vwap.abs().replace(0, np.nan)
    res = ratio / ratio.shift(63) - 1
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_price_vs_vwap_mom_126d_base_v049_signal(arg_closeadj, arg_volume) -> pd.Series:
    """126-day momentum of price relative to 126-day VWAP."""
    vwap = _rolling_vwap(arg_closeadj, arg_volume, 126)
    ratio = arg_closeadj / vwap.abs().replace(0, np.nan)
    res = ratio / ratio.shift(126) - 1
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_price_vs_vwap_mom_252d_base_v050_signal(arg_closeadj, arg_volume) -> pd.Series:
    """252-day momentum of price relative to 252-day VWAP."""
    vwap = _rolling_vwap(arg_closeadj, arg_volume, 252)
    ratio = arg_closeadj / vwap.abs().replace(0, np.nan)
    res = ratio / ratio.shift(252) - 1
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_tp_vs_vwap_mom_5d_base_v051_signal(arg_high, arg_low, arg_close, arg_volume) -> pd.Series:
    """5-day momentum of typical price relative to 5-day typical price VWAP."""
    tp = _typical_price(arg_high, arg_low, arg_close)
    vwap = _rolling_vwap(tp, arg_volume, 5)
    ratio = tp / vwap.abs().replace(0, np.nan)
    res = ratio / ratio.shift(5) - 1
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_tp_vs_vwap_mom_21d_base_v052_signal(arg_high, arg_low, arg_close, arg_volume) -> pd.Series:
    """21-day momentum of typical price relative to 21-day typical price VWAP."""
    tp = _typical_price(arg_high, arg_low, arg_close)
    vwap = _rolling_vwap(tp, arg_volume, 21)
    ratio = tp / vwap.abs().replace(0, np.nan)
    res = ratio / ratio.shift(21) - 1
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_tp_vs_vwap_mom_63d_base_v053_signal(arg_highadj, arg_lowadj, arg_closeadj, arg_volume) -> pd.Series:
    """63-day momentum of typical price relative to 63-day typical price VWAP."""
    tp = _typical_price(arg_highadj, arg_lowadj, arg_closeadj)
    vwap = _rolling_vwap(tp, arg_volume, 63)
    ratio = tp / vwap.abs().replace(0, np.nan)
    res = ratio / ratio.shift(63) - 1
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_high_vs_vwap_mom_5d_base_v054_signal(arg_high, arg_close, arg_volume) -> pd.Series:
    """5-day momentum of high price relative to 5-day close-based VWAP."""
    vwap = _rolling_vwap(arg_close, arg_volume, 5)
    ratio = arg_high / vwap.abs().replace(0, np.nan)
    res = ratio / ratio.shift(5) - 1
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_low_vs_vwap_mom_5d_base_v055_signal(arg_low, arg_close, arg_volume) -> pd.Series:
    """5-day momentum of low price relative to 5-day close-based VWAP."""
    vwap = _rolling_vwap(arg_close, arg_volume, 5)
    ratio = arg_low / vwap.abs().replace(0, np.nan)
    res = ratio / ratio.shift(5) - 1
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_price_vs_vwap_mom_10d_base_v056_signal(arg_close, arg_volume) -> pd.Series:
    """10-day momentum of price relative to 10-day VWAP."""
    vwap = _rolling_vwap(arg_close, arg_volume, 10)
    ratio = arg_close / vwap.abs().replace(0, np.nan)
    res = ratio / ratio.shift(10) - 1
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_price_vs_vwap_mom_42d_base_v057_signal(arg_closeadj, arg_volume) -> pd.Series:
    """42-day momentum of price relative to 42-day VWAP."""
    vwap = _rolling_vwap(arg_closeadj, arg_volume, 42)
    ratio = arg_closeadj / vwap.abs().replace(0, np.nan)
    res = ratio / ratio.shift(42) - 1
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_price_vs_vwap_mom_126d_tp_base_v058_signal(arg_highadj, arg_lowadj, arg_closeadj, arg_volume) -> pd.Series:
    """126-day momentum of typical price relative to 126-day VWAP."""
    tp = _typical_price(arg_highadj, arg_lowadj, arg_closeadj)
    vwap = _rolling_vwap(tp, arg_volume, 126)
    ratio = tp / vwap.abs().replace(0, np.nan)
    res = ratio / ratio.shift(126) - 1
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_z_5d_dist_sma_21d_base_v059_signal(arg_close, arg_volume) -> pd.Series:
    """SMA of 5-day VWAP Z-score over 21 days."""
    vwap = _rolling_vwap(arg_close, arg_volume, 5)
    z = _vwap_z(arg_close, vwap, 5)
    res = z.rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_z_21d_dist_sma_63d_base_v060_signal(arg_close, arg_closeadj, arg_volume) -> pd.Series:
    """SMA of 21-day VWAP Z-score over 63 days."""
    vwap = _rolling_vwap(arg_close, arg_volume, 21)
    z = _vwap_z(arg_close, vwap, 21)
    res = z.rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)

# V061-V075: Mixed variety
def f25vd_vwap_dist_5d_to_252d_base_v061_signal(arg_close, arg_closeadj, arg_volume) -> pd.Series:
    """Ratio of 5-day VWAP to 252-day VWAP."""
    vwap5 = _rolling_vwap(arg_close, arg_volume, 5)
    vwap252 = _rolling_vwap(arg_closeadj, arg_volume, 252)
    res = vwap5 / vwap252.abs().replace(0, np.nan) - 1
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_dist_21d_to_126d_base_v062_signal(arg_close, arg_closeadj, arg_volume) -> pd.Series:
    """Ratio of 21-day VWAP to 126-day VWAP."""
    vwap21 = _rolling_vwap(arg_close, arg_volume, 21)
    vwap126 = _rolling_vwap(arg_closeadj, arg_volume, 126)
    res = vwap21 / vwap126.abs().replace(0, np.nan) - 1
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_dist_tp_5d_to_21d_base_v063_signal(arg_high, arg_low, arg_close, arg_volume) -> pd.Series:
    """Ratio of 5-day typical price VWAP to 21-day typical price VWAP."""
    tp = _typical_price(arg_high, arg_low, arg_close)
    vwap5 = _rolling_vwap(tp, arg_volume, 5)
    vwap21 = _rolling_vwap(tp, arg_volume, 21)
    res = vwap5 / vwap21.abs().replace(0, np.nan) - 1
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_dist_tp_21d_to_63d_base_v064_signal(arg_high, arg_low, arg_close, arg_highadj, arg_lowadj, arg_closeadj, arg_volume) -> pd.Series:
    """Ratio of 21-day typical price VWAP to 63-day typical price VWAP."""
    tp21 = _typical_price(arg_high, arg_low, arg_close)
    tp63 = _typical_price(arg_highadj, arg_lowadj, arg_closeadj)
    vwap21 = _rolling_vwap(tp21, arg_volume, 21)
    vwap63 = _rolling_vwap(tp63, arg_volume, 63)
    res = vwap21 / vwap63.abs().replace(0, np.nan) - 1
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_dist_tp_63d_to_252d_base_v065_signal(arg_highadj, arg_lowadj, arg_closeadj, arg_volume) -> pd.Series:
    """Ratio of 63-day typical price VWAP to 252-day typical price VWAP."""
    tp = _typical_price(arg_highadj, arg_lowadj, arg_closeadj)
    vwap63 = _rolling_vwap(tp, arg_volume, 63)
    vwap252 = _rolling_vwap(tp, arg_volume, 252)
    res = vwap63 / vwap252.abs().replace(0, np.nan) - 1
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_z_5d_std_21d_base_v066_signal(arg_close, arg_volume) -> pd.Series:
    """Standard deviation of 5-day VWAP Z-score over 21 days."""
    vwap = _rolling_vwap(arg_close, arg_volume, 5)
    z = _vwap_z(arg_close, vwap, 5)
    res = z.rolling(21).std()
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_z_21d_std_63d_base_v067_signal(arg_close, arg_volume) -> pd.Series:
    """Standard deviation of 21-day VWAP Z-score over 63 days."""
    vwap = _rolling_vwap(arg_close, arg_volume, 21)
    z = _vwap_z(arg_close, vwap, 21)
    res = z.rolling(63).std()
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_dist_5d_max_21d_base_v068_signal(arg_close, arg_volume) -> pd.Series:
    """Maximum 5-day VWAP distance over 21 days."""
    vwap = _rolling_vwap(arg_close, arg_volume, 5)
    dist = _vwap_dist_val(arg_close, vwap)
    res = dist.rolling(21).max()
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_dist_5d_min_21d_base_v069_signal(arg_close, arg_volume) -> pd.Series:
    """Minimum 5-day VWAP distance over 21 days."""
    vwap = _rolling_vwap(arg_close, arg_volume, 5)
    dist = _vwap_dist_val(arg_close, vwap)
    res = dist.rolling(21).min()
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_dist_21d_max_63d_base_v070_signal(arg_close, arg_volume) -> pd.Series:
    """Maximum 21-day VWAP distance over 63 days."""
    vwap = _rolling_vwap(arg_close, arg_volume, 21)
    dist = _vwap_dist_val(arg_close, vwap)
    res = dist.rolling(63).max()
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_dist_21d_min_63d_base_v071_signal(arg_close, arg_volume) -> pd.Series:
    """Minimum 21-day VWAP distance over 63 days."""
    vwap = _rolling_vwap(arg_close, arg_volume, 21)
    dist = _vwap_dist_val(arg_close, vwap)
    res = dist.rolling(63).min()
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_z_5d_skew_63d_base_v072_signal(arg_close, arg_volume) -> pd.Series:
    """Skewness of 5-day VWAP Z-score over 63 days."""
    vwap = _rolling_vwap(arg_close, arg_volume, 5)
    z = _vwap_z(arg_close, vwap, 5)
    res = z.rolling(63).skew()
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_z_21d_skew_126d_base_v073_signal(arg_close, arg_volume) -> pd.Series:
    """Skewness of 21-day VWAP Z-score over 126 days."""
    vwap = _rolling_vwap(arg_close, arg_volume, 21)
    z = _vwap_z(arg_close, vwap, 21)
    res = z.rolling(126).skew()
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_dist_5d_range_21d_base_v074_signal(arg_close, arg_volume) -> pd.Series:
    """Range (Max-Min) of 5-day VWAP distance over 21 days."""
    vwap = _rolling_vwap(arg_close, arg_volume, 5)
    dist = _vwap_dist_val(arg_close, vwap)
    res = dist.rolling(21).max() - dist.rolling(21).min()
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_dist_21d_range_63d_base_v075_signal(arg_close, arg_volume) -> pd.Series:
    """Range (Max-Min) of 21-day VWAP distance over 63 days."""
    vwap = _rolling_vwap(arg_close, arg_volume, 21)
    dist = _vwap_dist_val(arg_close, vwap)
    res = dist.rolling(63).max() - dist.rolling(63).min()
    return res.replace([np.inf, -np.inf], np.nan)

SILVERDB_ACCESS, SOURCE_TABLE, ENTITY_COLUMN, DATE_COLUMN = "read_only", "sep", "ticker", "date"
ORDER_BY, NO_FORWARD_LOOKING = [ENTITY_COLUMN, DATE_COLUMN], True
SOURCE_COLUMNS = {c: f"sep.{c.replace('arg_', '')}" for c in ["arg_high", "arg_low", "arg_close", "arg_volume", "arg_highadj", "arg_lowadj", "arg_closeadj"]}

F25_VWAP_DEVIATION_BASE_REGISTRY_001_075 = {
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
        "arg_volume": pd.Series(np.random.lognormal(10, 1, sz)),
        "arg_highadj": pd.Series(100 + np.cumsum(np.random.normal(0, 1, sz)) + 2),
        "arg_lowadj": pd.Series(100 + np.cumsum(np.random.normal(0, 1, sz)) - 2),
        "arg_closeadj": pd.Series(100 + np.cumsum(np.random.normal(0, 1, sz))),
        "ticker": ["T"]*sz,
        "date": pd.date_range("2010-01-01", periods=sz)
    })
    for n, c in F25_VWAP_DEVIATION_BASE_REGISTRY_001_075.items():
        r = c["func"](**{i: d[i] for i in c["inputs"]})
        assert len(r) > 0, f"{n} failed len"
        # Some features might have many NaNs initially due to large windows, but should have values later
        assert r.notna().sum() > 0, f"{n} failed all nan"
    print(f"OK")
