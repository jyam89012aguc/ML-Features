# f05_moving_average_envelope_base_076_150_gemini.py
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

# Base Features 076-150: Envelope Distance, Width, and Multi-Envelope Interactions

def f05mae_f05_moving_average_envelope_sma_21d_3pct_dist_upper_v076_signal(close: pd.Series) -> pd.Series:
    """Distance to upper 3% SMA envelope, 21-day window."""
    ma = _sma(close, 21)
    res = _envelope_dist(close, ma, 0.03, True)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_sma_21d_3pct_dist_lower_v077_signal(close: pd.Series) -> pd.Series:
    """Distance to lower 3% SMA envelope, 21-day window."""
    ma = _sma(close, 21)
    res = _envelope_dist(close, ma, 0.03, False)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_ema_63d_5pct_dist_upper_v078_signal(closeadj: pd.Series) -> pd.Series:
    """Distance to upper 5% EMA envelope, 63-day window."""
    ma = _ema(closeadj, 63)
    res = _envelope_dist(closeadj, ma, 0.05, True)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_ema_63d_5pct_dist_lower_v079_signal(closeadj: pd.Series) -> pd.Series:
    """Distance to lower 5% EMA envelope, 63-day window."""
    ma = _ema(closeadj, 63)
    res = _envelope_dist(closeadj, ma, 0.05, False)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_wma_126d_10pct_dist_upper_v080_signal(closeadj: pd.Series) -> pd.Series:
    """Distance to upper 10% WMA envelope, 126-day window."""
    ma = _wma(closeadj, 126)
    res = _envelope_dist(closeadj, ma, 0.10, True)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_sma_5d_2pct_width_v081_signal(close: pd.Series) -> pd.Series:
    """Width of 2% SMA envelope, 5-day window."""
    ma = _sma(close, 5)
    res = _envelope_width(ma, 0.02)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_ema_21d_5pct_width_v082_signal(close: pd.Series) -> pd.Series:
    """Width of 5% EMA envelope, 21-day window."""
    ma = _ema(close, 21)
    res = _envelope_width(ma, 0.05)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_wma_63d_3pct_width_v083_signal(closeadj: pd.Series) -> pd.Series:
    """Width of 3% WMA envelope, 63-day window."""
    ma = _wma(closeadj, 63)
    res = _envelope_width(ma, 0.03)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_sma_5d_in_21d_5pct_pos_v084_signal(close: pd.Series) -> pd.Series:
    """Position of 5d SMA in 21d 5% SMA envelope."""
    ma5 = _sma(close, 5)
    ma21 = _sma(close, 21)
    res = _envelope_pos(ma5, ma21, 0.05)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_sma_5d_in_63d_10pct_pos_v085_signal(close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Position of 5d SMA in 63d 10% SMA envelope."""
    ma5 = _sma(closeadj, 5)
    ma63 = _sma(closeadj, 63)
    res = _envelope_pos(ma5, ma63, 0.10)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_ema_21d_in_252d_10pct_pos_v086_signal(closeadj: pd.Series) -> pd.Series:
    """Position of 21d EMA in 252d 10% EMA envelope."""
    ma21 = _ema(closeadj, 21)
    ma252 = _ema(closeadj, 252)
    res = _envelope_pos(ma21, ma252, 0.10)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_sma_width_ratio_5d_1pct_5pct_v087_signal(close: pd.Series) -> pd.Series:
    """Ratio of 1% vs 5% SMA envelope width, 5-day window."""
    ma = _sma(close, 5)
    w1 = _envelope_width(ma, 0.01)
    w5 = _envelope_width(ma, 0.05)
    res = w1 / w5.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_sma_21d_1pct_dist_upper_v088_signal(close: pd.Series) -> pd.Series:
    """Distance to upper 1% SMA envelope, 21-day window."""
    ma = _sma(close, 21)
    res = _envelope_dist(close, ma, 0.01, True)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_sma_21d_1pct_dist_lower_v089_signal(close: pd.Series) -> pd.Series:
    """Distance to lower 1% SMA envelope, 21-day window."""
    ma = _sma(close, 21)
    res = _envelope_dist(close, ma, 0.01, False)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_sma_21d_2pct_dist_upper_v090_signal(close: pd.Series) -> pd.Series:
    """Distance to upper 2% SMA envelope, 21-day window."""
    ma = _sma(close, 21)
    res = _envelope_dist(close, ma, 0.02, True)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_sma_21d_2pct_dist_lower_v091_signal(close: pd.Series) -> pd.Series:
    """Distance to lower 2% SMA envelope, 21-day window."""
    ma = _sma(close, 21)
    res = _envelope_dist(close, ma, 0.02, False)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_sma_21d_5pct_dist_upper_v092_signal(close: pd.Series) -> pd.Series:
    """Distance to upper 5% SMA envelope, 21-day window."""
    ma = _sma(close, 21)
    res = _envelope_dist(close, ma, 0.05, True)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_sma_21d_5pct_dist_lower_v093_signal(close: pd.Series) -> pd.Series:
    """Distance to lower 5% SMA envelope, 21-day window."""
    ma = _sma(close, 21)
    res = _envelope_dist(close, ma, 0.05, False)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_sma_21d_10pct_dist_upper_v094_signal(close: pd.Series) -> pd.Series:
    """Distance to upper 10% SMA envelope, 21-day window."""
    ma = _sma(close, 21)
    res = _envelope_dist(close, ma, 0.10, True)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_sma_21d_10pct_dist_lower_v095_signal(close: pd.Series) -> pd.Series:
    """Distance to lower 10% SMA envelope, 21-day window."""
    ma = _sma(close, 21)
    res = _envelope_dist(close, ma, 0.10, False)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_sma_63d_1pct_dist_upper_v096_signal(closeadj: pd.Series) -> pd.Series:
    """Distance to upper 1% SMA envelope, 63-day window."""
    ma = _sma(closeadj, 63)
    res = _envelope_dist(closeadj, ma, 0.01, True)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_sma_63d_1pct_dist_lower_v097_signal(closeadj: pd.Series) -> pd.Series:
    """Distance to lower 1% SMA envelope, 63-day window."""
    ma = _sma(closeadj, 63)
    res = _envelope_dist(closeadj, ma, 0.01, False)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_sma_63d_2pct_dist_upper_v098_signal(closeadj: pd.Series) -> pd.Series:
    """Distance to upper 2% SMA envelope, 63-day window."""
    ma = _sma(closeadj, 63)
    res = _envelope_dist(closeadj, ma, 0.02, True)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_sma_63d_2pct_dist_lower_v099_signal(closeadj: pd.Series) -> pd.Series:
    """Distance to lower 2% SMA envelope, 63-day window."""
    ma = _sma(closeadj, 63)
    res = _envelope_dist(closeadj, ma, 0.02, False)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_sma_63d_3pct_dist_upper_v100_signal(closeadj: pd.Series) -> pd.Series:
    """Distance to upper 3% SMA envelope, 63-day window."""
    ma = _sma(closeadj, 63)
    res = _envelope_dist(closeadj, ma, 0.03, True)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_sma_63d_3pct_dist_lower_v101_signal(closeadj: pd.Series) -> pd.Series:
    """Distance to lower 3% SMA envelope, 63-day window."""
    ma = _sma(closeadj, 63)
    res = _envelope_dist(closeadj, ma, 0.03, False)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_sma_63d_10pct_dist_upper_v102_signal(closeadj: pd.Series) -> pd.Series:
    """Distance to upper 10% SMA envelope, 63-day window."""
    ma = _sma(closeadj, 63)
    res = _envelope_dist(closeadj, ma, 0.10, True)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_sma_63d_10pct_dist_lower_v103_signal(closeadj: pd.Series) -> pd.Series:
    """Distance to lower 10% SMA envelope, 63-day window."""
    ma = _sma(closeadj, 63)
    res = _envelope_dist(closeadj, ma, 0.10, False)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_ema_21d_1pct_dist_upper_v104_signal(close: pd.Series) -> pd.Series:
    """Distance to upper 1% EMA envelope, 21-day window."""
    ma = _ema(close, 21)
    res = _envelope_dist(close, ma, 0.01, True)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_ema_21d_1pct_dist_lower_v105_signal(close: pd.Series) -> pd.Series:
    """Distance to lower 1% EMA envelope, 21-day window."""
    ma = _ema(close, 21)
    res = _envelope_dist(close, ma, 0.01, False)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_ema_21d_2pct_dist_upper_v106_signal(close: pd.Series) -> pd.Series:
    """Distance to upper 2% EMA envelope, 21-day window."""
    ma = _ema(close, 21)
    res = _envelope_dist(close, ma, 0.02, True)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_ema_21d_2pct_dist_lower_v107_signal(close: pd.Series) -> pd.Series:
    """Distance to lower 2% EMA envelope, 21-day window."""
    ma = _ema(close, 21)
    res = _envelope_dist(close, ma, 0.02, False)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_ema_21d_5pct_dist_upper_v108_signal(close: pd.Series) -> pd.Series:
    """Distance to upper 5% EMA envelope, 21-day window."""
    ma = _ema(close, 21)
    res = _envelope_dist(close, ma, 0.05, True)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_ema_21d_5pct_dist_lower_v109_signal(close: pd.Series) -> pd.Series:
    """Distance to lower 5% EMA envelope, 21-day window."""
    ma = _ema(close, 21)
    res = _envelope_dist(close, ma, 0.05, False)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_ema_21d_10pct_dist_upper_v110_signal(close: pd.Series) -> pd.Series:
    """Distance to upper 10% EMA envelope, 21-day window."""
    ma = _ema(close, 21)
    res = _envelope_dist(close, ma, 0.10, True)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_ema_21d_10pct_dist_lower_v111_signal(close: pd.Series) -> pd.Series:
    """Distance to lower 10% EMA envelope, 21-day window."""
    ma = _ema(close, 21)
    res = _envelope_dist(close, ma, 0.10, False)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_ema_63d_1pct_dist_upper_v112_signal(closeadj: pd.Series) -> pd.Series:
    """Distance to upper 1% EMA envelope, 63-day window."""
    ma = _ema(closeadj, 63)
    res = _envelope_dist(closeadj, ma, 0.01, True)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_ema_63d_1pct_dist_lower_v113_signal(closeadj: pd.Series) -> pd.Series:
    """Distance to lower 1% EMA envelope, 63-day window."""
    ma = _ema(closeadj, 63)
    res = _envelope_dist(closeadj, ma, 0.01, False)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_ema_63d_2pct_dist_upper_v114_signal(closeadj: pd.Series) -> pd.Series:
    """Distance to upper 2% EMA envelope, 63-day window."""
    ma = _ema(closeadj, 63)
    res = _envelope_dist(closeadj, ma, 0.02, True)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_ema_63d_2pct_dist_lower_v115_signal(closeadj: pd.Series) -> pd.Series:
    """Distance to lower 2% EMA envelope, 63-day window."""
    ma = _ema(closeadj, 63)
    res = _envelope_dist(closeadj, ma, 0.02, False)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_ema_63d_3pct_dist_upper_v116_signal(closeadj: pd.Series) -> pd.Series:
    """Distance to upper 3% EMA envelope, 63-day window."""
    ma = _ema(closeadj, 63)
    res = _envelope_dist(closeadj, ma, 0.03, True)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_ema_63d_3pct_dist_lower_v117_signal(closeadj: pd.Series) -> pd.Series:
    """Distance to lower 3% EMA envelope, 63-day window."""
    ma = _ema(closeadj, 63)
    res = _envelope_dist(closeadj, ma, 0.03, False)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_ema_63d_10pct_dist_upper_v118_signal(closeadj: pd.Series) -> pd.Series:
    """Distance to upper 10% EMA envelope, 63-day window."""
    ma = _ema(closeadj, 63)
    res = _envelope_dist(closeadj, ma, 0.10, True)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_ema_63d_10pct_dist_lower_v119_signal(closeadj: pd.Series) -> pd.Series:
    """Distance to lower 10% EMA envelope, 63-day window."""
    ma = _ema(closeadj, 63)
    res = _envelope_dist(closeadj, ma, 0.10, False)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_wma_21d_1pct_dist_upper_v120_signal(close: pd.Series) -> pd.Series:
    """Distance to upper 1% WMA envelope, 21-day window."""
    ma = _wma(close, 21)
    res = _envelope_dist(close, ma, 0.01, True)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_wma_21d_1pct_dist_lower_v121_signal(close: pd.Series) -> pd.Series:
    """Distance to lower 1% WMA envelope, 21-day window."""
    ma = _wma(close, 21)
    res = _envelope_dist(close, ma, 0.01, False)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_wma_21d_2pct_dist_upper_v122_signal(close: pd.Series) -> pd.Series:
    """Distance to upper 2% WMA envelope, 21-day window."""
    ma = _wma(close, 21)
    res = _envelope_dist(close, ma, 0.02, True)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_wma_21d_2pct_dist_lower_v123_signal(close: pd.Series) -> pd.Series:
    """Distance to lower 2% WMA envelope, 21-day window."""
    ma = _wma(close, 21)
    res = _envelope_dist(close, ma, 0.02, False)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_wma_21d_5pct_dist_upper_v124_signal(close: pd.Series) -> pd.Series:
    """Distance to upper 5% WMA envelope, 21-day window."""
    ma = _wma(close, 21)
    res = _envelope_dist(close, ma, 0.05, True)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_wma_21d_5pct_dist_lower_v125_signal(close: pd.Series) -> pd.Series:
    """Distance to lower 5% WMA envelope, 21-day window."""
    ma = _wma(close, 21)
    res = _envelope_dist(close, ma, 0.05, False)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_wma_21d_10pct_dist_upper_v126_signal(close: pd.Series) -> pd.Series:
    """Distance to upper 10% WMA envelope, 21-day window."""
    ma = _wma(close, 21)
    res = _envelope_dist(close, ma, 0.10, True)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_wma_21d_10pct_dist_lower_v127_signal(close: pd.Series) -> pd.Series:
    """Distance to lower 10% WMA envelope, 21-day window."""
    ma = _wma(close, 21)
    res = _envelope_dist(close, ma, 0.10, False)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_sma_5d_1pct_width_v128_signal(close: pd.Series) -> pd.Series:
    """Width of 1% SMA envelope, 5-day window."""
    ma = _sma(close, 5)
    res = _envelope_width(ma, 0.01)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_sma_21d_2pct_width_v129_signal(close: pd.Series) -> pd.Series:
    """Width of 2% SMA envelope, 21-day window."""
    ma = _sma(close, 21)
    res = _envelope_width(ma, 0.02)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_sma_63d_5pct_width_v130_signal(closeadj: pd.Series) -> pd.Series:
    """Width of 5% SMA envelope, 63-day window."""
    ma = _sma(closeadj, 63)
    res = _envelope_width(ma, 0.05)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_ema_5d_1pct_width_v131_signal(close: pd.Series) -> pd.Series:
    """Width of 1% EMA envelope, 5-day window."""
    ma = _ema(close, 5)
    res = _envelope_width(ma, 0.01)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_ema_21d_3pct_width_v132_signal(close: pd.Series) -> pd.Series:
    """Width of 3% EMA envelope, 21-day window."""
    ma = _ema(close, 21)
    res = _envelope_width(ma, 0.03)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_ema_126d_10pct_width_v133_signal(closeadj: pd.Series) -> pd.Series:
    """Width of 10% EMA envelope, 126-day window."""
    ma = _ema(closeadj, 126)
    res = _envelope_width(ma, 0.10)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_wma_5d_2pct_width_v134_signal(close: pd.Series) -> pd.Series:
    """Width of 2% WMA envelope, 5-day window."""
    ma = _wma(close, 5)
    res = _envelope_width(ma, 0.02)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_wma_21d_5pct_width_v135_signal(close: pd.Series) -> pd.Series:
    """Width of 5% WMA envelope, 21-day window."""
    ma = _wma(close, 21)
    res = _envelope_width(ma, 0.05)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_wma_252d_10pct_width_v136_signal(closeadj: pd.Series) -> pd.Series:
    """Width of 10% WMA envelope, 252-day window."""
    ma = _wma(closeadj, 252)
    res = _envelope_width(ma, 0.10)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_sma_width_sqz_21d_5pct_v137_signal(close: pd.Series) -> pd.Series:
    """Width squeeze of 5% SMA envelope (current width / 21d mean width)."""
    ma = _sma(close, 21)
    w = _envelope_width(ma, 0.05)
    res = w / _sma(w, 21).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_ema_width_sqz_63d_10pct_v138_signal(closeadj: pd.Series) -> pd.Series:
    """Width squeeze of 10% EMA envelope (current width / 63d mean width)."""
    ma = _ema(closeadj, 63)
    w = _envelope_width(ma, 0.10)
    res = w / _sma(w, 63).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_sma_5d_in_126d_5pct_pos_v139_signal(closeadj: pd.Series) -> pd.Series:
    """Position of 5d SMA in 126d 5% SMA envelope."""
    ma5 = _sma(closeadj, 5)
    ma126 = _sma(closeadj, 126)
    res = _envelope_pos(ma5, ma126, 0.05)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_ema_5d_in_252d_5pct_pos_v140_signal(closeadj: pd.Series) -> pd.Series:
    """Position of 5d EMA in 252d 5% EMA envelope."""
    ma5 = _ema(closeadj, 5)
    ma252 = _ema(closeadj, 252)
    res = _envelope_pos(ma5, ma252, 0.05)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_sma_21d_in_126d_10pct_pos_v141_signal(closeadj: pd.Series) -> pd.Series:
    """Position of 21d SMA in 126d 10% SMA envelope."""
    ma21 = _sma(closeadj, 21)
    ma126 = _sma(closeadj, 126)
    res = _envelope_pos(ma21, ma126, 0.10)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_sma_5d_dist_upper_21d_2pct_v142_signal(close: pd.Series) -> pd.Series:
    """Distance of 5d SMA to upper 2% SMA 21d envelope."""
    ma5 = _sma(close, 5)
    ma21 = _sma(close, 21)
    res = _envelope_dist(ma5, ma21, 0.02, True)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_sma_5d_dist_lower_21d_2pct_v143_signal(close: pd.Series) -> pd.Series:
    """Distance of 5d SMA to lower 2% SMA 21d envelope."""
    ma5 = _sma(close, 5)
    ma21 = _sma(close, 21)
    res = _envelope_dist(ma5, ma21, 0.02, False)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_ema_5d_dist_upper_63d_5pct_v144_signal(closeadj: pd.Series) -> pd.Series:
    """Distance of 5d EMA to upper 5% EMA 63d envelope."""
    ma5 = _ema(closeadj, 5)
    ma63 = _ema(closeadj, 63)
    res = _envelope_dist(ma5, ma63, 0.05, True)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_ema_5d_dist_lower_63d_5pct_v145_signal(closeadj: pd.Series) -> pd.Series:
    """Distance of 5d EMA to lower 5% EMA 63d envelope."""
    ma5 = _ema(closeadj, 5)
    ma63 = _ema(closeadj, 63)
    res = _envelope_dist(ma5, ma63, 0.05, False)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_wma_21d_dist_upper_126d_10pct_v146_signal(closeadj: pd.Series) -> pd.Series:
    """Distance of 21d WMA to upper 10% WMA 126d envelope."""
    ma21 = _wma(closeadj, 21)
    ma126 = _wma(closeadj, 126)
    res = _envelope_dist(ma21, ma126, 0.10, True)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_wma_21d_dist_lower_126d_10pct_v147_signal(closeadj: pd.Series) -> pd.Series:
    """Distance of 21d WMA to lower 10% WMA 126d envelope."""
    ma21 = _wma(closeadj, 21)
    ma126 = _wma(closeadj, 126)
    res = _envelope_dist(ma21, ma126, 0.10, False)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_sma_width_ratio_21d_2pct_63d_5pct_v148_signal(closeadj: pd.Series) -> pd.Series:
    """Ratio of 21d 2% SMA envelope width to 63d 5% SMA envelope width."""
    ma21 = _sma(closeadj, 21)
    ma63 = _sma(closeadj, 63)
    w21 = _envelope_width(ma21, 0.02)
    w63 = _envelope_width(ma63, 0.05)
    res = w21 / w63.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_ema_width_ratio_63d_5pct_252d_10pct_v149_signal(closeadj: pd.Series) -> pd.Series:
    """Ratio of 63d 5% EMA envelope width to 252d 10% EMA envelope width."""
    ma63 = _ema(closeadj, 63)
    ma252 = _ema(closeadj, 252)
    w63 = _envelope_width(ma63, 0.05)
    w252 = _envelope_width(ma252, 0.10)
    res = w63 / w252.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_sma_5d_in_21d_1pct_pos_v150_signal(close: pd.Series) -> pd.Series:
    """Position of 5d SMA in 21d 1% SMA envelope."""
    ma5 = _sma(close, 5)
    ma21 = _sma(close, 21)
    res = _envelope_pos(ma5, ma21, 0.01)
    return res.replace([np.inf, -np.inf], np.nan)

SILVERDB_ACCESS, SOURCE_TABLE, ENTITY_COLUMN, DATE_COLUMN = "read_only", "sep", "ticker", "date"
ORDER_BY, NO_FORWARD_LOOKING = [ENTITY_COLUMN, DATE_COLUMN], True
SOURCE_COLUMNS = {c: f"sep.{c}" for c in ["close", "closeadj"]}

BASE_NAMES = [f for f in globals() if f.startswith("f05mae_") and f.endswith("_signal")]

F05_MOVING_AVERAGE_ENVELOPE_BASE_REGISTRY_076_150 = {
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
    for n, c in F05_MOVING_AVERAGE_ENVELOPE_BASE_REGISTRY_076_150.items():
        r = c["func"](**{i: d[i] for i in c["inputs"]})
        assert isinstance(r, pd.Series)
    print("base 076-150 OK")
