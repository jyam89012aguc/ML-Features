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

def _median_price(h, l):
    """
    Calculates the median price: (High + Low) / 2.
    """
    return (h + l) / 2.0

# V076-V090: VWAP Distances using Open and Median Prices
def f25vd_vwap_dist_5d_open_base_v076_signal(arg_open, arg_close, arg_volume) -> pd.Series:
    """VWAP distance for 5-day window using open price relative to close-based VWAP."""
    vwap = _rolling_vwap(arg_close, arg_volume, 5)
    res = _vwap_dist_val(arg_open, vwap)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_dist_21d_open_base_v077_signal(arg_open, arg_close, arg_volume) -> pd.Series:
    """VWAP distance for 21-day window using open price relative to close-based VWAP."""
    vwap = _rolling_vwap(arg_close, arg_volume, 21)
    res = _vwap_dist_val(arg_open, vwap)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_dist_63d_open_base_v078_signal(arg_openadj, arg_closeadj, arg_volume) -> pd.Series:
    """VWAP distance for 63-day window using openadj price relative to closeadj-based VWAP."""
    vwap = _rolling_vwap(arg_closeadj, arg_volume, 63)
    res = _vwap_dist_val(arg_openadj, vwap)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_dist_5d_median_base_v079_signal(arg_high, arg_low, arg_close, arg_volume) -> pd.Series:
    """VWAP distance for 5-day window using median price relative to close-based VWAP."""
    median = _median_price(arg_high, arg_low)
    vwap = _rolling_vwap(arg_close, arg_volume, 5)
    res = _vwap_dist_val(median, vwap)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_dist_21d_median_base_v080_signal(arg_high, arg_low, arg_close, arg_volume) -> pd.Series:
    """VWAP distance for 21-day window using median price relative to close-based VWAP."""
    median = _median_price(arg_high, arg_low)
    vwap = _rolling_vwap(arg_close, arg_volume, 21)
    res = _vwap_dist_val(median, vwap)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_dist_63d_median_base_v081_signal(arg_highadj, arg_lowadj, arg_closeadj, arg_volume) -> pd.Series:
    """VWAP distance for 63-day window using medianadj price relative to closeadj-based VWAP."""
    median = _median_price(arg_highadj, arg_lowadj)
    vwap = _rolling_vwap(arg_closeadj, arg_volume, 63)
    res = _vwap_dist_val(median, vwap)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_dist_5d_median_based_base_v082_signal(arg_high, arg_low, arg_volume) -> pd.Series:
    """VWAP distance for 5-day window using median-price-based VWAP."""
    median = _median_price(arg_high, arg_low)
    vwap = _rolling_vwap(median, arg_volume, 5)
    res = _vwap_dist_val(median, vwap)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_dist_21d_median_based_base_v083_signal(arg_high, arg_low, arg_volume) -> pd.Series:
    """VWAP distance for 21-day window using median-price-based VWAP."""
    median = _median_price(arg_high, arg_low)
    vwap = _rolling_vwap(median, arg_volume, 21)
    res = _vwap_dist_val(median, vwap)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_dist_63d_median_based_base_v084_signal(arg_highadj, arg_lowadj, arg_volume) -> pd.Series:
    """VWAP distance for 63-day window using medianadj-price-based VWAP."""
    median = _median_price(arg_highadj, arg_lowadj)
    vwap = _rolling_vwap(median, arg_volume, 63)
    res = _vwap_dist_val(median, vwap)
    return res.replace([np.inf, -np.inf], np.nan)


def f25vd_vwap_z_5d_median_base_v086_signal(arg_high, arg_low, arg_close, arg_volume) -> pd.Series:
    """VWAP z-score for 5-day window using median price relative to close-based VWAP."""
    median = _median_price(arg_high, arg_low)
    vwap = _rolling_vwap(arg_close, arg_volume, 5)
    res = _vwap_z(median, vwap, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_z_21d_median_base_v087_signal(arg_high, arg_low, arg_close, arg_volume) -> pd.Series:
    """VWAP z-score for 21-day window using median price relative to close-based VWAP."""
    median = _median_price(arg_high, arg_low)
    vwap = _rolling_vwap(arg_close, arg_volume, 21)
    res = _vwap_z(median, vwap, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_z_63d_median_base_v088_signal(arg_highadj, arg_lowadj, arg_closeadj, arg_volume) -> pd.Series:
    """VWAP z-score for 63-day window using medianadj price relative to closeadj-based VWAP."""
    median = _median_price(arg_highadj, arg_lowadj)
    vwap = _rolling_vwap(arg_closeadj, arg_volume, 63)
    res = _vwap_z(median, vwap, 63)
    return res.replace([np.inf, -np.inf], np.nan)



# V091-V110: Statistical properties of VWAP distances
def f25vd_vwap_dist_5d_kurt_63d_base_v091_signal(arg_close, arg_volume) -> pd.Series:
    """Kurtosis of 5-day VWAP distance over 63 days."""
    vwap = _rolling_vwap(arg_close, arg_volume, 5)
    dist = _vwap_dist_val(arg_close, vwap)
    res = dist.rolling(63).kurt()
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_dist_21d_kurt_126d_base_v092_signal(arg_close, arg_volume) -> pd.Series:
    """Kurtosis of 21-day VWAP distance over 126 days."""
    vwap = _rolling_vwap(arg_close, arg_volume, 21)
    dist = _vwap_dist_val(arg_close, vwap)
    res = dist.rolling(126).kurt()
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_dist_5d_std_252d_base_v093_signal(arg_close, arg_volume) -> pd.Series:
    """Standard deviation of 5-day VWAP distance over 252 days."""
    vwap = _rolling_vwap(arg_close, arg_volume, 5)
    dist = _vwap_dist_val(arg_close, vwap)
    res = dist.rolling(252).std()
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_z_5d_max_63d_base_v094_signal(arg_close, arg_volume) -> pd.Series:
    """Maximum of 5-day VWAP Z-score over 63 days."""
    vwap = _rolling_vwap(arg_close, arg_volume, 5)
    z = _vwap_z(arg_close, vwap, 5)
    res = z.rolling(63).max()
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_z_21d_min_126d_base_v095_signal(arg_close, arg_volume) -> pd.Series:
    """Minimum of 21-day VWAP Z-score over 126 days."""
    vwap = _rolling_vwap(arg_close, arg_volume, 21)
    z = _vwap_z(arg_close, vwap, 21)
    res = z.rolling(126).min()
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_dist_5d_tp_kurt_63d_base_v096_signal(arg_high, arg_low, arg_close, arg_volume) -> pd.Series:
    """Kurtosis of 5-day typical-price VWAP distance over 63 days."""
    tp = _typical_price(arg_high, arg_low, arg_close)
    vwap = _rolling_vwap(tp, arg_volume, 5)
    dist = _vwap_dist_val(tp, vwap)
    res = dist.rolling(63).kurt()
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_dist_21d_tp_std_126d_base_v097_signal(arg_high, arg_low, arg_close, arg_volume) -> pd.Series:
    """Standard deviation of 21-day typical-price VWAP distance over 126 days."""
    tp = _typical_price(arg_high, arg_low, arg_close)
    vwap = _rolling_vwap(tp, arg_volume, 21)
    dist = _vwap_dist_val(tp, vwap)
    res = dist.rolling(126).std()
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_z_5d_tp_skew_252d_base_v098_signal(arg_high, arg_low, arg_close, arg_volume) -> pd.Series:
    """Skewness of 5-day typical-price VWAP Z-score over 252 days."""
    tp = _typical_price(arg_high, arg_low, arg_close)
    vwap = _rolling_vwap(tp, arg_volume, 5)
    z = _vwap_z(tp, vwap, 5)
    res = z.rolling(252).skew()
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_dist_5d_sma_21d_base_v099_signal(arg_close, arg_volume) -> pd.Series:
    """SMA of 5-day VWAP distance over 21 days."""
    vwap = _rolling_vwap(arg_close, arg_volume, 5)
    dist = _vwap_dist_val(arg_close, vwap)
    res = dist.rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_dist_21d_sma_63d_base_v100_signal(arg_close, arg_volume) -> pd.Series:
    """SMA of 21-day VWAP distance over 63 days."""
    vwap = _rolling_vwap(arg_close, arg_volume, 21)
    dist = _vwap_dist_val(arg_close, vwap)
    res = dist.rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_dist_63d_sma_126d_base_v101_signal(arg_closeadj, arg_volume) -> pd.Series:
    """SMA of 63-day VWAP distance over 126 days."""
    vwap = _rolling_vwap(arg_closeadj, arg_volume, 63)
    dist = _vwap_dist_val(arg_closeadj, vwap)
    res = dist.rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_z_5d_ema_21d_base_v102_signal(arg_close, arg_volume) -> pd.Series:
    """EMA of 5-day VWAP Z-score over 21 days."""
    vwap = _rolling_vwap(arg_close, arg_volume, 5)
    z = _vwap_z(arg_close, vwap, 5)
    res = z.ewm(span=21).mean()
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_z_21d_ema_63d_base_v103_signal(arg_close, arg_volume) -> pd.Series:
    """EMA of 21-day VWAP Z-score over 63 days."""
    vwap = _rolling_vwap(arg_close, arg_volume, 21)
    z = _vwap_z(arg_close, vwap, 21)
    res = z.ewm(span=63).mean()
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_dist_5d_med_sma_21d_base_v104_signal(arg_high, arg_low, arg_close, arg_volume) -> pd.Series:
    """SMA of 5-day median-price VWAP distance over 21 days."""
    median = _median_price(arg_high, arg_low)
    vwap = _rolling_vwap(arg_close, arg_volume, 5)
    dist = _vwap_dist_val(median, vwap)
    res = dist.rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_dist_21d_med_sma_63d_base_v105_signal(arg_high, arg_low, arg_close, arg_volume) -> pd.Series:
    """SMA of 21-day median-price VWAP distance over 63 days."""
    median = _median_price(arg_high, arg_low)
    vwap = _rolling_vwap(arg_close, arg_volume, 21)
    dist = _vwap_dist_val(median, vwap)
    res = dist.rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_z_5d_med_ema_21d_base_v106_signal(arg_high, arg_low, arg_close, arg_volume) -> pd.Series:
    """EMA of 5-day median-price VWAP Z-score over 21 days."""
    median = _median_price(arg_high, arg_low)
    vwap = _rolling_vwap(arg_close, arg_volume, 5)
    z = _vwap_z(median, vwap, 5)
    res = z.ewm(span=21).mean()
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_dist_5d_tp_sma_21d_base_v107_signal(arg_high, arg_low, arg_close, arg_volume) -> pd.Series:
    """SMA of 5-day typical-price VWAP distance over 21 days."""
    tp = _typical_price(arg_high, arg_low, arg_close)
    vwap = _rolling_vwap(tp, arg_volume, 5)
    dist = _vwap_dist_val(tp, vwap)
    res = dist.rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_dist_21d_tp_sma_63d_base_v108_signal(arg_high, arg_low, arg_close, arg_volume) -> pd.Series:
    """SMA of 21-day typical-price VWAP distance over 63 days."""
    tp = _typical_price(arg_high, arg_low, arg_close)
    vwap = _rolling_vwap(tp, arg_volume, 21)
    dist = _vwap_dist_val(tp, vwap)
    res = dist.rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_z_5d_tp_ema_21d_base_v109_signal(arg_high, arg_low, arg_close, arg_volume) -> pd.Series:
    """EMA of 5-day typical-price VWAP Z-score over 21 days."""
    tp = _typical_price(arg_high, arg_low, arg_close)
    vwap = _rolling_vwap(tp, arg_volume, 5)
    z = _vwap_z(tp, vwap, 5)
    res = z.ewm(span=21).mean()
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_dist_5d_roc_10d_base_v110_signal(arg_close, arg_volume) -> pd.Series:
    """10-day ROC of 5-day VWAP distance."""
    vwap = _rolling_vwap(arg_close, arg_volume, 5)
    dist = _vwap_dist_val(arg_close, vwap)
    res = dist.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)

# V111-V130: More variations with ROC and Shift
def f25vd_vwap_dist_21d_roc_21d_base_v111_signal(arg_close, arg_volume) -> pd.Series:
    """21-day ROC of 21-day VWAP distance."""
    vwap = _rolling_vwap(arg_close, arg_volume, 21)
    dist = _vwap_dist_val(arg_close, vwap)
    res = dist.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_z_5d_roc_5d_base_v112_signal(arg_close, arg_volume) -> pd.Series:
    """5-day ROC of 5-day VWAP Z-score."""
    vwap = _rolling_vwap(arg_close, arg_volume, 5)
    z = _vwap_z(arg_close, vwap, 5)
    res = z.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_z_21d_roc_10d_base_v113_signal(arg_close, arg_volume) -> pd.Series:
    """10-day ROC of 21-day VWAP Z-score."""
    vwap = _rolling_vwap(arg_close, arg_volume, 21)
    z = _vwap_z(arg_close, vwap, 21)
    res = z.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_dist_5d_tp_roc_5d_base_v114_signal(arg_high, arg_low, arg_close, arg_volume) -> pd.Series:
    """5-day ROC of 5-day typical-price VWAP distance."""
    tp = _typical_price(arg_high, arg_low, arg_close)
    vwap = _rolling_vwap(tp, arg_volume, 5)
    dist = _vwap_dist_val(tp, vwap)
    res = dist.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_dist_21d_tp_roc_10d_base_v115_signal(arg_high, arg_low, arg_close, arg_volume) -> pd.Series:
    """10-day ROC of 21-day typical-price VWAP distance."""
    tp = _typical_price(arg_high, arg_low, arg_close)
    vwap = _rolling_vwap(tp, arg_volume, 21)
    dist = _vwap_dist_val(tp, vwap)
    res = dist.diff(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_z_5d_tp_roc_21d_base_v116_signal(arg_high, arg_low, arg_close, arg_volume) -> pd.Series:
    """21-day ROC of 5-day typical-price VWAP Z-score."""
    tp = _typical_price(arg_high, arg_low, arg_close)
    vwap = _rolling_vwap(tp, arg_volume, 5)
    z = _vwap_z(tp, vwap, 5)
    res = z.diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_dist_5d_lag_5d_base_v117_signal(arg_close, arg_volume) -> pd.Series:
    """5-day lagged 5-day VWAP distance."""
    vwap = _rolling_vwap(arg_close, arg_volume, 5)
    dist = _vwap_dist_val(arg_close, vwap)
    res = dist.shift(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_dist_21d_lag_10d_base_v118_signal(arg_close, arg_volume) -> pd.Series:
    """10-day lagged 21-day VWAP distance."""
    vwap = _rolling_vwap(arg_close, arg_volume, 21)
    dist = _vwap_dist_val(arg_close, vwap)
    res = dist.shift(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_z_5d_lag_21d_base_v119_signal(arg_close, arg_volume) -> pd.Series:
    """21-day lagged 5-day VWAP Z-score."""
    vwap = _rolling_vwap(arg_close, arg_volume, 5)
    z = _vwap_z(arg_close, vwap, 5)
    res = z.shift(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_dist_5d_tp_lag_5d_base_v120_signal(arg_high, arg_low, arg_close, arg_volume) -> pd.Series:
    """5-day lagged 5-day typical-price VWAP distance."""
    tp = _typical_price(arg_high, arg_low, arg_close)
    vwap = _rolling_vwap(tp, arg_volume, 5)
    dist = _vwap_dist_val(tp, vwap)
    res = dist.shift(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_cross_5d_21d_ema_21d_base_v121_signal(arg_close, arg_volume) -> pd.Series:
    """EMA of crossing of 5-day and 21-day VWAPs over 21 days."""
    vwap5 = _rolling_vwap(arg_close, arg_volume, 5)
    vwap21 = _rolling_vwap(arg_close, arg_volume, 21)
    cross = (vwap5 - vwap21) / vwap21.abs().replace(0, np.nan)
    res = cross.ewm(span=21).mean()
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_cross_21d_63d_ema_63d_base_v122_signal(arg_close, arg_closeadj, arg_volume) -> pd.Series:
    """EMA of crossing of 21-day and 63-day VWAPs over 63 days."""
    vwap21 = _rolling_vwap(arg_close, arg_volume, 21)
    vwap63 = _rolling_vwap(arg_closeadj, arg_volume, 63)
    cross = (vwap21 - vwap63) / vwap63.abs().replace(0, np.nan)
    res = cross.ewm(span=63).mean()
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_cross_5d_tp_21d_tp_ema_21d_base_v123_signal(arg_high, arg_low, arg_close, arg_volume) -> pd.Series:
    """EMA of crossing of 5-day and 21-day typical-price VWAPs over 21 days."""
    tp = _typical_price(arg_high, arg_low, arg_close)
    vwap5 = _rolling_vwap(tp, arg_volume, 5)
    vwap21 = _rolling_vwap(tp, arg_volume, 21)
    cross = (vwap5 - vwap21) / vwap21.abs().replace(0, np.nan)
    res = cross.ewm(span=21).mean()
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_dist_5d_vs_sma_21d_base_v124_signal(arg_close, arg_volume) -> pd.Series:
    """Ratio of 5-day VWAP distance to its 21-day SMA."""
    vwap = _rolling_vwap(arg_close, arg_volume, 5)
    dist = _vwap_dist_val(arg_close, vwap)
    res = dist / dist.rolling(21).mean().abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_z_5d_vs_ema_21d_base_v125_signal(arg_close, arg_volume) -> pd.Series:
    """Difference between 5-day VWAP Z-score and its 21-day EMA."""
    vwap = _rolling_vwap(arg_close, arg_volume, 5)
    z = _vwap_z(arg_close, vwap, 5)
    res = z - z.ewm(span=21).mean()
    return res.replace([np.inf, -np.inf], np.nan)

# V126-V150: Volume-weighted price momentum variations
def f25vd_vwap_mom_5d_base_v126_signal(arg_close, arg_volume) -> pd.Series:
    """5-day momentum of 5-day VWAP."""
    vwap = _rolling_vwap(arg_close, arg_volume, 5)
    res = vwap / vwap.shift(5) - 1
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_mom_21d_base_v127_signal(arg_close, arg_volume) -> pd.Series:
    """21-day momentum of 21-day VWAP."""
    vwap = _rolling_vwap(arg_close, arg_volume, 21)
    res = vwap / vwap.shift(21) - 1
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_mom_63d_base_v128_signal(arg_closeadj, arg_volume) -> pd.Series:
    """63-day momentum of 63-day VWAP."""
    vwap = _rolling_vwap(arg_closeadj, arg_volume, 63)
    res = vwap / vwap.shift(63) - 1
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_mom_126d_base_v129_signal(arg_closeadj, arg_volume) -> pd.Series:
    """126-day momentum of 126-day VWAP."""
    vwap = _rolling_vwap(arg_closeadj, arg_volume, 126)
    res = vwap / vwap.shift(126) - 1
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_mom_252d_base_v130_signal(arg_closeadj, arg_volume) -> pd.Series:
    """252-day momentum of 252-day VWAP."""
    vwap = _rolling_vwap(arg_closeadj, arg_volume, 252)
    res = vwap / vwap.shift(252) - 1
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_tp_mom_5d_base_v131_signal(arg_high, arg_low, arg_close, arg_volume) -> pd.Series:
    """5-day momentum of 5-day typical-price VWAP."""
    tp = _typical_price(arg_high, arg_low, arg_close)
    vwap = _rolling_vwap(tp, arg_volume, 5)
    res = vwap / vwap.shift(5) - 1
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_tp_mom_21d_base_v132_signal(arg_high, arg_low, arg_close, arg_volume) -> pd.Series:
    """21-day momentum of 21-day typical-price VWAP."""
    tp = _typical_price(arg_high, arg_low, arg_close)
    vwap = _rolling_vwap(tp, arg_volume, 21)
    res = vwap / vwap.shift(21) - 1
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_tp_mom_63d_base_v133_signal(arg_highadj, arg_lowadj, arg_closeadj, arg_volume) -> pd.Series:
    """63-day momentum of 63-day typical-price VWAP."""
    tp = _typical_price(arg_highadj, arg_lowadj, arg_closeadj)
    vwap = _rolling_vwap(tp, arg_volume, 63)
    res = vwap / vwap.shift(63) - 1
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_med_mom_5d_base_v134_signal(arg_high, arg_low, arg_volume) -> pd.Series:
    """5-day momentum of 5-day median-price VWAP."""
    median = _median_price(arg_high, arg_low)
    vwap = _rolling_vwap(median, arg_volume, 5)
    res = vwap / vwap.shift(5) - 1
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_med_mom_21d_base_v135_signal(arg_high, arg_low, arg_volume) -> pd.Series:
    """21-day momentum of 21-day median-price VWAP."""
    median = _median_price(arg_high, arg_low)
    vwap = _rolling_vwap(median, arg_volume, 21)
    res = vwap / vwap.shift(21) - 1
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_dist_5d_vs_21d_base_v136_signal(arg_close, arg_volume) -> pd.Series:
    """Difference between 5-day and 21-day VWAP distances."""
    vwap5 = _rolling_vwap(arg_close, arg_volume, 5)
    vwap21 = _rolling_vwap(arg_close, arg_volume, 21)
    res = _vwap_dist_val(arg_close, vwap5) - _vwap_dist_val(arg_close, vwap21)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_dist_21d_vs_63d_base_v137_signal(arg_close, arg_closeadj, arg_volume) -> pd.Series:
    """Difference between 21-day and 63-day VWAP distances."""
    vwap21 = _rolling_vwap(arg_close, arg_volume, 21)
    vwap63 = _rolling_vwap(arg_closeadj, arg_volume, 63)
    res = _vwap_dist_val(arg_close, vwap21) - _vwap_dist_val(arg_closeadj, vwap63)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_z_5d_vs_21d_base_v138_signal(arg_close, arg_volume) -> pd.Series:
    """Difference between 5-day and 21-day VWAP Z-scores."""
    vwap5 = _rolling_vwap(arg_close, arg_volume, 5)
    vwap21 = _rolling_vwap(arg_close, arg_volume, 21)
    res = _vwap_z(arg_close, vwap5, 5) - _vwap_z(arg_close, vwap21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_z_21d_vs_63d_base_v139_signal(arg_close, arg_closeadj, arg_volume) -> pd.Series:
    """Difference between 21-day and 63-day VWAP Z-scores."""
    vwap21 = _rolling_vwap(arg_close, arg_volume, 21)
    vwap63 = _rolling_vwap(arg_closeadj, arg_volume, 63)
    res = _vwap_z(arg_close, vwap21, 21) - _vwap_z(arg_closeadj, vwap63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_dist_tp_5d_vs_21d_base_v140_signal(arg_high, arg_low, arg_close, arg_volume) -> pd.Series:
    """Difference between 5-day and 21-day typical-price VWAP distances."""
    tp = _typical_price(arg_high, arg_low, arg_close)
    vwap5 = _rolling_vwap(tp, arg_volume, 5)
    vwap21 = _rolling_vwap(tp, arg_volume, 21)
    res = _vwap_dist_val(tp, vwap5) - _vwap_dist_val(tp, vwap21)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_dist_med_5d_vs_21d_base_v141_signal(arg_high, arg_low, arg_volume) -> pd.Series:
    """Difference between 5-day and 21-day median-price VWAP distances."""
    median = _median_price(arg_high, arg_low)
    vwap5 = _rolling_vwap(median, arg_volume, 5)
    vwap21 = _rolling_vwap(median, arg_volume, 21)
    res = _vwap_dist_val(median, vwap5) - _vwap_dist_val(median, vwap21)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_dist_5d_norm_base_v142_signal(arg_close, arg_volume) -> pd.Series:
    """Normalized 5-day VWAP distance (dist / 21-day volatility)."""
    vwap = _rolling_vwap(arg_close, arg_volume, 5)
    dist = _vwap_dist_val(arg_close, vwap)
    vol = arg_close.pct_change().rolling(21).std()
    res = dist / vol.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_dist_21d_norm_base_v143_signal(arg_close, arg_volume) -> pd.Series:
    """Normalized 21-day VWAP distance (dist / 63-day volatility)."""
    vwap = _rolling_vwap(arg_close, arg_volume, 21)
    dist = _vwap_dist_val(arg_close, vwap)
    vol = arg_close.pct_change().rolling(63).std()
    res = dist / vol.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_dist_tp_5d_norm_base_v144_signal(arg_high, arg_low, arg_close, arg_volume) -> pd.Series:
    """Normalized 5-day typical-price VWAP distance."""
    tp = _typical_price(arg_high, arg_low, arg_close)
    vwap = _rolling_vwap(tp, arg_volume, 5)
    dist = _vwap_dist_val(tp, vwap)
    vol = tp.pct_change().rolling(21).std()
    res = dist / vol.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_dist_med_5d_norm_base_v145_signal(arg_high, arg_low, arg_volume) -> pd.Series:
    """Normalized 5-day median-price VWAP distance."""
    median = _median_price(arg_high, arg_low)
    vwap = _rolling_vwap(median, arg_volume, 5)
    dist = _vwap_dist_val(median, vwap)
    vol = median.pct_change().rolling(21).std()
    res = dist / vol.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_dist_5d_div_21d_base_v146_signal(arg_close, arg_volume) -> pd.Series:
    """Ratio of 5-day VWAP distance to 21-day VWAP distance."""
    vwap5 = _rolling_vwap(arg_close, arg_volume, 5)
    vwap21 = _rolling_vwap(arg_close, arg_volume, 21)
    res = _vwap_dist_val(arg_close, vwap5) / _vwap_dist_val(arg_close, vwap21).abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_dist_21d_div_63d_base_v147_signal(arg_close, arg_closeadj, arg_volume) -> pd.Series:
    """Ratio of 21-day VWAP distance to 63-day VWAP distance."""
    vwap21 = _rolling_vwap(arg_close, arg_volume, 21)
    vwap63 = _rolling_vwap(arg_closeadj, arg_volume, 63)
    res = _vwap_dist_val(arg_close, vwap21) / _vwap_dist_val(arg_closeadj, vwap63).abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_z_5d_div_21d_base_v148_signal(arg_close, arg_volume) -> pd.Series:
    """Ratio of 5-day VWAP Z-score to 21-day VWAP Z-score."""
    vwap5 = _rolling_vwap(arg_close, arg_volume, 5)
    vwap21 = _rolling_vwap(arg_close, arg_volume, 21)
    res = _vwap_z(arg_close, vwap5, 5) / _vwap_z(arg_close, vwap21, 21).abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_dist_tp_5d_div_21d_base_v149_signal(arg_high, arg_low, arg_close, arg_volume) -> pd.Series:
    """Ratio of 5-day typical-price VWAP distance to 21-day typical-price VWAP distance."""
    tp = _typical_price(arg_high, arg_low, arg_close)
    vwap5 = _rolling_vwap(tp, arg_volume, 5)
    vwap21 = _rolling_vwap(tp, arg_volume, 21)
    res = _vwap_dist_val(tp, vwap5) / _vwap_dist_val(tp, vwap21).abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f25vd_vwap_dist_med_5d_div_21d_base_v150_signal(arg_high, arg_low, arg_volume) -> pd.Series:
    """Ratio of 5-day median-price VWAP distance to 21-day median-price VWAP distance."""
    median = _median_price(arg_high, arg_low)
    vwap5 = _rolling_vwap(median, arg_volume, 5)
    vwap21 = _rolling_vwap(median, arg_volume, 21)
    res = _vwap_dist_val(median, vwap5) / _vwap_dist_val(median, vwap21).abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

SILVERDB_ACCESS, SOURCE_TABLE, ENTITY_COLUMN, DATE_COLUMN = "read_only", "sep", "ticker", "date"
ORDER_BY, NO_FORWARD_LOOKING = [ENTITY_COLUMN, DATE_COLUMN], True
SOURCE_COLUMNS = {c: f"sep.{c.replace('arg_', '')}" for c in ["arg_high", "arg_low", "arg_close", "arg_volume", "arg_highadj", "arg_lowadj", "arg_closeadj", "arg_open", "arg_openadj"]}

F25_VWAP_DEVIATION_BASE_REGISTRY_076_150 = {
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
    for n, c in F25_VWAP_DEVIATION_BASE_REGISTRY_076_150.items():
        r = c["func"](**{i: d[i] for i in c["inputs"]})
        assert len(r) > 0, f"{n} failed len"
        assert r.notna().sum() > 0, f"{n} failed all nan"
    print(f"OK")
