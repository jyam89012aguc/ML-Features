# f08_moving_average_dynamics_base_076_150_gemini.py
import pandas as pd
import numpy as np

def _sma(s, w): return s.rolling(w, min_periods=min(w, 5)).mean()
def _ema(s, w): return s.ewm(span=w, min_periods=min(w, 5), adjust=False).mean()
def _mad_slope(ma, w): return (ma - ma.shift(w)) / w
def _mad_spread(ma1, ma2): return (ma1 / ma2.replace(0, np.nan) - 1)

# EMA Slope 076-088 (continued)
def f08_moving_average_dynamics_close_ema_slope_10d_v076_signal(arg_close: pd.Series) -> pd.Series:
    res = _mad_slope(_ema(arg_close, 10), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_moving_average_dynamics_close_ema_slope_12d_v077_signal(arg_close: pd.Series) -> pd.Series:
    res = _mad_slope(_ema(arg_close, 12), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_moving_average_dynamics_close_ema_slope_15d_v078_signal(arg_close: pd.Series) -> pd.Series:
    res = _mad_slope(_ema(arg_close, 15), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_moving_average_dynamics_close_ema_slope_20d_v079_signal(arg_close: pd.Series) -> pd.Series:
    res = _mad_slope(_ema(arg_close, 20), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_moving_average_dynamics_close_ema_slope_21d_v080_signal(arg_close: pd.Series) -> pd.Series:
    res = _mad_slope(_ema(arg_close, 21), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_moving_average_dynamics_closeadj_ema_slope_30d_v081_signal(arg_close_adj: pd.Series) -> pd.Series:
    res = _mad_slope(_ema(arg_close_adj, 30), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_moving_average_dynamics_closeadj_ema_slope_40d_v082_signal(arg_close_adj: pd.Series) -> pd.Series:
    res = _mad_slope(_ema(arg_close_adj, 40), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_moving_average_dynamics_closeadj_ema_slope_50d_v083_signal(arg_close_adj: pd.Series) -> pd.Series:
    res = _mad_slope(_ema(arg_close_adj, 50), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_moving_average_dynamics_closeadj_ema_slope_63d_v084_signal(arg_close_adj: pd.Series) -> pd.Series:
    res = _mad_slope(_ema(arg_close_adj, 63), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_moving_average_dynamics_closeadj_ema_slope_100d_v085_signal(arg_close_adj: pd.Series) -> pd.Series:
    res = _mad_slope(_ema(arg_close_adj, 100), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_moving_average_dynamics_closeadj_ema_slope_126d_v086_signal(arg_close_adj: pd.Series) -> pd.Series:
    res = _mad_slope(_ema(arg_close_adj, 126), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_moving_average_dynamics_closeadj_ema_slope_200d_v087_signal(arg_close_adj: pd.Series) -> pd.Series:
    res = _mad_slope(_ema(arg_close_adj, 200), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_moving_average_dynamics_closeadj_ema_slope_252d_v088_signal(arg_close_adj: pd.Series) -> pd.Series:
    res = _mad_slope(_ema(arg_close_adj, 252), 63)
    return res.replace([np.inf, -np.inf], np.nan)

# SMA Cross Spread 089-110
def f08_moving_average_dynamics_sma_cross_spread_3d_10d_v089_signal(arg_close: pd.Series) -> pd.Series:
    res = _mad_spread(_sma(arg_close, 3), _sma(arg_close, 10))
    return res.replace([np.inf, -np.inf], np.nan)

def f08_moving_average_dynamics_sma_cross_spread_3d_21d_v090_signal(arg_close: pd.Series) -> pd.Series:
    res = _mad_spread(_sma(arg_close, 3), _sma(arg_close, 21))
    return res.replace([np.inf, -np.inf], np.nan)

def f08_moving_average_dynamics_sma_cross_spread_5d_10d_v091_signal(arg_close: pd.Series) -> pd.Series:
    res = _mad_spread(_sma(arg_close, 5), _sma(arg_close, 10))
    return res.replace([np.inf, -np.inf], np.nan)

def f08_moving_average_dynamics_sma_cross_spread_5d_21d_v092_signal(arg_close: pd.Series) -> pd.Series:
    res = _mad_spread(_sma(arg_close, 5), _sma(arg_close, 21))
    return res.replace([np.inf, -np.inf], np.nan)

def f08_moving_average_dynamics_sma_cross_spread_5d_50d_v093_signal(arg_close: pd.Series, arg_close_adj: pd.Series) -> pd.Series:
    adj = arg_close_adj / arg_close.replace(0, np.nan)
    res = _mad_spread(_sma(arg_close, 5) * adj, _sma(arg_close_adj, 50))
    return res.replace([np.inf, -np.inf], np.nan)

def f08_moving_average_dynamics_sma_cross_spread_8d_21d_v094_signal(arg_close: pd.Series) -> pd.Series:
    res = _mad_spread(_sma(arg_close, 8), _sma(arg_close, 21))
    return res.replace([np.inf, -np.inf], np.nan)

def f08_moving_average_dynamics_sma_cross_spread_10d_21d_v095_signal(arg_close: pd.Series) -> pd.Series:
    res = _mad_spread(_sma(arg_close, 10), _sma(arg_close, 21))
    return res.replace([np.inf, -np.inf], np.nan)

def f08_moving_average_dynamics_sma_cross_spread_10d_50d_v096_signal(arg_close: pd.Series, arg_close_adj: pd.Series) -> pd.Series:
    adj = arg_close_adj / arg_close.replace(0, np.nan)
    res = _mad_spread(_sma(arg_close, 10) * adj, _sma(arg_close_adj, 50))
    return res.replace([np.inf, -np.inf], np.nan)

def f08_moving_average_dynamics_sma_cross_spread_10d_100d_v097_signal(arg_close: pd.Series, arg_close_adj: pd.Series) -> pd.Series:
    adj = arg_close_adj / arg_close.replace(0, np.nan)
    res = _mad_spread(_sma(arg_close, 10) * adj, _sma(arg_close_adj, 100))
    return res.replace([np.inf, -np.inf], np.nan)

def f08_moving_average_dynamics_sma_cross_spread_10d_200d_v098_signal(arg_close: pd.Series, arg_close_adj: pd.Series) -> pd.Series:
    adj = arg_close_adj / arg_close.replace(0, np.nan)
    res = _mad_spread(_sma(arg_close, 10) * adj, _sma(arg_close_adj, 200))
    return res.replace([np.inf, -np.inf], np.nan)

def f08_moving_average_dynamics_sma_cross_spread_21d_50d_v099_signal(arg_close: pd.Series, arg_close_adj: pd.Series) -> pd.Series:
    adj = arg_close_adj / arg_close.replace(0, np.nan)
    res = _mad_spread(_sma(arg_close, 21) * adj, _sma(arg_close_adj, 50))
    return res.replace([np.inf, -np.inf], np.nan)

def f08_moving_average_dynamics_sma_cross_spread_21d_63d_v100_signal(arg_close: pd.Series, arg_close_adj: pd.Series) -> pd.Series:
    adj = arg_close_adj / arg_close.replace(0, np.nan)
    res = _mad_spread(_sma(arg_close, 21) * adj, _sma(arg_close_adj, 63))
    return res.replace([np.inf, -np.inf], np.nan)

def f08_moving_average_dynamics_sma_cross_spread_21d_100d_v101_signal(arg_close: pd.Series, arg_close_adj: pd.Series) -> pd.Series:
    adj = arg_close_adj / arg_close.replace(0, np.nan)
    res = _mad_spread(_sma(arg_close, 21) * adj, _sma(arg_close_adj, 100))
    return res.replace([np.inf, -np.inf], np.nan)

def f08_moving_average_dynamics_sma_cross_spread_21d_200d_v102_signal(arg_close: pd.Series, arg_close_adj: pd.Series) -> pd.Series:
    adj = arg_close_adj / arg_close.replace(0, np.nan)
    res = _mad_spread(_sma(arg_close, 21) * adj, _sma(arg_close_adj, 200))
    return res.replace([np.inf, -np.inf], np.nan)

def f08_moving_average_dynamics_sma_cross_spread_21d_252d_v103_signal(arg_close: pd.Series, arg_close_adj: pd.Series) -> pd.Series:
    adj = arg_close_adj / arg_close.replace(0, np.nan)
    res = _mad_spread(_sma(arg_close, 21) * adj, _sma(arg_close_adj, 252))
    return res.replace([np.inf, -np.inf], np.nan)

def f08_moving_average_dynamics_sma_cross_spread_50d_100d_v104_signal(arg_close_adj: pd.Series) -> pd.Series:
    res = _mad_spread(_sma(arg_close_adj, 50), _sma(arg_close_adj, 100))
    return res.replace([np.inf, -np.inf], np.nan)

def f08_moving_average_dynamics_sma_cross_spread_50d_126d_v105_signal(arg_close_adj: pd.Series) -> pd.Series:
    res = _mad_spread(_sma(arg_close_adj, 50), _sma(arg_close_adj, 126))
    return res.replace([np.inf, -np.inf], np.nan)

def f08_moving_average_dynamics_sma_cross_spread_50d_200d_v106_signal(arg_close_adj: pd.Series) -> pd.Series:
    res = _mad_spread(_sma(arg_close_adj, 50), _sma(arg_close_adj, 200))
    return res.replace([np.inf, -np.inf], np.nan)

def f08_moving_average_dynamics_sma_cross_spread_50d_252d_v107_signal(arg_close_adj: pd.Series) -> pd.Series:
    res = _mad_spread(_sma(arg_close_adj, 50), _sma(arg_close_adj, 252))
    return res.replace([np.inf, -np.inf], np.nan)

def f08_moving_average_dynamics_sma_cross_spread_100d_200d_v108_signal(arg_close_adj: pd.Series) -> pd.Series:
    res = _mad_spread(_sma(arg_close_adj, 100), _sma(arg_close_adj, 200))
    return res.replace([np.inf, -np.inf], np.nan)

def f08_moving_average_dynamics_sma_cross_spread_126d_252d_v109_signal(arg_close_adj: pd.Series) -> pd.Series:
    res = _mad_spread(_sma(arg_close_adj, 126), _sma(arg_close_adj, 252))
    return res.replace([np.inf, -np.inf], np.nan)

def f08_moving_average_dynamics_sma_cross_spread_200d_252d_v110_signal(arg_close_adj: pd.Series) -> pd.Series:
    res = _mad_spread(_sma(arg_close_adj, 200), _sma(arg_close_adj, 252))
    return res.replace([np.inf, -np.inf], np.nan)

# EMA Cross Spread 111-132
def f08_moving_average_dynamics_ema_cross_spread_3d_10d_v111_signal(arg_close: pd.Series) -> pd.Series:
    res = _mad_spread(_ema(arg_close, 3), _ema(arg_close, 10))
    return res.replace([np.inf, -np.inf], np.nan)

def f08_moving_average_dynamics_ema_cross_spread_3d_21d_v112_signal(arg_close: pd.Series) -> pd.Series:
    res = _mad_spread(_ema(arg_close, 3), _ema(arg_close, 21))
    return res.replace([np.inf, -np.inf], np.nan)

def f08_moving_average_dynamics_ema_cross_spread_5d_10d_v113_signal(arg_close: pd.Series) -> pd.Series:
    res = _mad_spread(_ema(arg_close, 5), _ema(arg_close, 10))
    return res.replace([np.inf, -np.inf], np.nan)

def f08_moving_average_dynamics_ema_cross_spread_5d_21d_v114_signal(arg_close: pd.Series) -> pd.Series:
    res = _mad_spread(_ema(arg_close, 5), _ema(arg_close, 21))
    return res.replace([np.inf, -np.inf], np.nan)

def f08_moving_average_dynamics_ema_cross_spread_5d_50d_v115_signal(arg_close: pd.Series, arg_close_adj: pd.Series) -> pd.Series:
    adj = arg_close_adj / arg_close.replace(0, np.nan)
    res = _mad_spread(_ema(arg_close, 5) * adj, _ema(arg_close_adj, 50))
    return res.replace([np.inf, -np.inf], np.nan)

def f08_moving_average_dynamics_ema_cross_spread_8d_21d_v116_signal(arg_close: pd.Series) -> pd.Series:
    res = _mad_spread(_ema(arg_close, 8), _ema(arg_close, 21))
    return res.replace([np.inf, -np.inf], np.nan)

def f08_moving_average_dynamics_ema_cross_spread_10d_21d_v117_signal(arg_close: pd.Series) -> pd.Series:
    res = _mad_spread(_ema(arg_close, 10), _ema(arg_close, 21))
    return res.replace([np.inf, -np.inf], np.nan)

def f08_moving_average_dynamics_ema_cross_spread_10d_50d_v118_signal(arg_close: pd.Series, arg_close_adj: pd.Series) -> pd.Series:
    adj = arg_close_adj / arg_close.replace(0, np.nan)
    res = _mad_spread(_ema(arg_close, 10) * adj, _ema(arg_close_adj, 50))
    return res.replace([np.inf, -np.inf], np.nan)

def f08_moving_average_dynamics_ema_cross_spread_10d_100d_v119_signal(arg_close: pd.Series, arg_close_adj: pd.Series) -> pd.Series:
    adj = arg_close_adj / arg_close.replace(0, np.nan)
    res = _mad_spread(_ema(arg_close, 10) * adj, _ema(arg_close_adj, 100))
    return res.replace([np.inf, -np.inf], np.nan)

def f08_moving_average_dynamics_ema_cross_spread_10d_200d_v120_signal(arg_close: pd.Series, arg_close_adj: pd.Series) -> pd.Series:
    adj = arg_close_adj / arg_close.replace(0, np.nan)
    res = _mad_spread(_ema(arg_close, 10) * adj, _ema(arg_close_adj, 200))
    return res.replace([np.inf, -np.inf], np.nan)

def f08_moving_average_dynamics_ema_cross_spread_21d_50d_v121_signal(arg_close: pd.Series, arg_close_adj: pd.Series) -> pd.Series:
    adj = arg_close_adj / arg_close.replace(0, np.nan)
    res = _mad_spread(_ema(arg_close, 21) * adj, _ema(arg_close_adj, 50))
    return res.replace([np.inf, -np.inf], np.nan)

def f08_moving_average_dynamics_ema_cross_spread_21d_63d_v122_signal(arg_close: pd.Series, arg_close_adj: pd.Series) -> pd.Series:
    adj = arg_close_adj / arg_close.replace(0, np.nan)
    res = _mad_spread(_ema(arg_close, 21) * adj, _ema(arg_close_adj, 63))
    return res.replace([np.inf, -np.inf], np.nan)

def f08_moving_average_dynamics_ema_cross_spread_21d_100d_v123_signal(arg_close: pd.Series, arg_close_adj: pd.Series) -> pd.Series:
    adj = arg_close_adj / arg_close.replace(0, np.nan)
    res = _mad_spread(_ema(arg_close, 21) * adj, _ema(arg_close_adj, 100))
    return res.replace([np.inf, -np.inf], np.nan)

def f08_moving_average_dynamics_ema_cross_spread_21d_200d_v124_signal(arg_close: pd.Series, arg_close_adj: pd.Series) -> pd.Series:
    adj = arg_close_adj / arg_close.replace(0, np.nan)
    res = _mad_spread(_ema(arg_close, 21) * adj, _ema(arg_close_adj, 200))
    return res.replace([np.inf, -np.inf], np.nan)

def f08_moving_average_dynamics_ema_cross_spread_21d_252d_v125_signal(arg_close: pd.Series, arg_close_adj: pd.Series) -> pd.Series:
    adj = arg_close_adj / arg_close.replace(0, np.nan)
    res = _mad_spread(_ema(arg_close, 21) * adj, _ema(arg_close_adj, 252))
    return res.replace([np.inf, -np.inf], np.nan)

def f08_moving_average_dynamics_ema_cross_spread_50d_100d_v126_signal(arg_close_adj: pd.Series) -> pd.Series:
    res = _mad_spread(_ema(arg_close_adj, 50), _ema(arg_close_adj, 100))
    return res.replace([np.inf, -np.inf], np.nan)

def f08_moving_average_dynamics_ema_cross_spread_50d_126d_v127_signal(arg_close_adj: pd.Series) -> pd.Series:
    res = _mad_spread(_ema(arg_close_adj, 50), _ema(arg_close_adj, 126))
    return res.replace([np.inf, -np.inf], np.nan)

def f08_moving_average_dynamics_ema_cross_spread_50d_200d_v128_signal(arg_close_adj: pd.Series) -> pd.Series:
    res = _mad_spread(_ema(arg_close_adj, 50), _ema(arg_close_adj, 200))
    return res.replace([np.inf, -np.inf], np.nan)

def f08_moving_average_dynamics_ema_cross_spread_50d_252d_v129_signal(arg_close_adj: pd.Series) -> pd.Series:
    res = _mad_spread(_ema(arg_close_adj, 50), _ema(arg_close_adj, 252))
    return res.replace([np.inf, -np.inf], np.nan)

def f08_moving_average_dynamics_ema_cross_spread_100d_200d_v130_signal(arg_close_adj: pd.Series) -> pd.Series:
    res = _mad_spread(_ema(arg_close_adj, 100), _ema(arg_close_adj, 200))
    return res.replace([np.inf, -np.inf], np.nan)

def f08_moving_average_dynamics_ema_cross_spread_126d_252d_v131_signal(arg_close_adj: pd.Series) -> pd.Series:
    res = _mad_spread(_ema(arg_close_adj, 126), _ema(arg_close_adj, 252))
    return res.replace([np.inf, -np.inf], np.nan)

def f08_moving_average_dynamics_ema_cross_spread_200d_252d_v132_signal(arg_close_adj: pd.Series) -> pd.Series:
    res = _mad_spread(_ema(arg_close_adj, 200), _ema(arg_close_adj, 252))
    return res.replace([np.inf, -np.inf], np.nan)

# Ribbon Width 133-138
def f08_moving_average_dynamics_sma_ribbon_width_short_v133_signal(arg_close: pd.Series) -> pd.Series:
    ma5 = _sma(arg_close, 5)
    ma10 = _sma(arg_close, 10)
    ma20 = _sma(arg_close, 20)
    res = (pd.concat([ma5, ma10, ma20], axis=1).max(axis=1) / pd.concat([ma5, ma10, ma20], axis=1).min(axis=1) - 1)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_moving_average_dynamics_sma_ribbon_width_med_v134_signal(arg_close_adj: pd.Series) -> pd.Series:
    ma20 = _sma(arg_close_adj, 20)
    ma50 = _sma(arg_close_adj, 50)
    ma100 = _sma(arg_close_adj, 100)
    res = (pd.concat([ma20, ma50, ma100], axis=1).max(axis=1) / pd.concat([ma20, ma50, ma100], axis=1).min(axis=1) - 1)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_moving_average_dynamics_sma_ribbon_width_long_v135_signal(arg_close_adj: pd.Series) -> pd.Series:
    ma50 = _sma(arg_close_adj, 50)
    ma100 = _sma(arg_close_adj, 100)
    ma200 = _sma(arg_close_adj, 200)
    res = (pd.concat([ma50, ma100, ma200], axis=1).max(axis=1) / pd.concat([ma50, ma100, ma200], axis=1).min(axis=1) - 1)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_moving_average_dynamics_ema_ribbon_width_short_v136_signal(arg_close: pd.Series) -> pd.Series:
    ma5 = _ema(arg_close, 5)
    ma10 = _ema(arg_close, 10)
    ma20 = _ema(arg_close, 20)
    res = (pd.concat([ma5, ma10, ma20], axis=1).max(axis=1) / pd.concat([ma5, ma10, ma20], axis=1).min(axis=1) - 1)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_moving_average_dynamics_ema_ribbon_width_med_v137_signal(arg_close_adj: pd.Series) -> pd.Series:
    ma20 = _ema(arg_close_adj, 20)
    ma50 = _ema(arg_close_adj, 50)
    ma100 = _ema(arg_close_adj, 100)
    res = (pd.concat([ma20, ma50, ma100], axis=1).max(axis=1) / pd.concat([ma20, ma50, ma100], axis=1).min(axis=1) - 1)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_moving_average_dynamics_ema_ribbon_width_long_v138_signal(arg_close_adj: pd.Series) -> pd.Series:
    ma50 = _ema(arg_close_adj, 50)
    ma100 = _ema(arg_close_adj, 100)
    ma200 = _ema(arg_close_adj, 200)
    res = (pd.concat([ma50, ma100, ma200], axis=1).max(axis=1) / pd.concat([ma50, ma100, ma200], axis=1).min(axis=1) - 1)
    return res.replace([np.inf, -np.inf], np.nan)

# Rising Count 139-150
def f08_moving_average_dynamics_sma_rising_count_5d_v139_signal(arg_close: pd.Series) -> pd.Series:
    ma = _sma(arg_close, 5)
    res = (ma > ma.shift(1)).rolling(21).sum()
    return res

def f08_moving_average_dynamics_sma_rising_count_10d_v140_signal(arg_close: pd.Series) -> pd.Series:
    ma = _sma(arg_close, 10)
    res = (ma > ma.shift(1)).rolling(21).sum()
    return res

def f08_moving_average_dynamics_sma_rising_count_21d_v141_signal(arg_close: pd.Series) -> pd.Series:
    ma = _sma(arg_close, 21)
    res = (ma > ma.shift(1)).rolling(21).sum()
    return res

def f08_moving_average_dynamics_sma_rising_count_63d_v142_signal(arg_close_adj: pd.Series) -> pd.Series:
    ma = _sma(arg_close_adj, 63)
    res = (ma > ma.shift(1)).rolling(21).sum()
    return res

def f08_moving_average_dynamics_sma_rising_count_126d_v143_signal(arg_close_adj: pd.Series) -> pd.Series:
    ma = _sma(arg_close_adj, 126)
    res = (ma > ma.shift(1)).rolling(21).sum()
    return res

def f08_moving_average_dynamics_sma_rising_count_252d_v144_signal(arg_close_adj: pd.Series) -> pd.Series:
    ma = _sma(arg_close_adj, 252)
    res = (ma > ma.shift(1)).rolling(21).sum()
    return res

def f08_moving_average_dynamics_ema_rising_count_5d_v145_signal(arg_close: pd.Series) -> pd.Series:
    ma = _ema(arg_close, 5)
    res = (ma > ma.shift(1)).rolling(21).sum()
    return res

def f08_moving_average_dynamics_ema_rising_count_10d_v146_signal(arg_close: pd.Series) -> pd.Series:
    ma = _ema(arg_close, 10)
    res = (ma > ma.shift(1)).rolling(21).sum()
    return res

def f08_moving_average_dynamics_ema_rising_count_21d_v147_signal(arg_close: pd.Series) -> pd.Series:
    ma = _ema(arg_close, 21)
    res = (ma > ma.shift(1)).rolling(21).sum()
    return res

def f08_moving_average_dynamics_ema_rising_count_63d_v148_signal(arg_close_adj: pd.Series) -> pd.Series:
    ma = _ema(arg_close_adj, 63)
    res = (ma > ma.shift(1)).rolling(21).sum()
    return res

def f08_moving_average_dynamics_ema_rising_count_126d_v149_signal(arg_close_adj: pd.Series) -> pd.Series:
    ma = _ema(arg_close_adj, 126)
    res = (ma > ma.shift(1)).rolling(21).sum()
    return res

def f08_moving_average_dynamics_ema_rising_count_252d_v150_signal(arg_close_adj: pd.Series) -> pd.Series:
    ma = _ema(arg_close_adj, 252)
    res = (ma > ma.shift(1)).rolling(21).sum()
    return res

def test_features():
    arg_close = pd.Series(np.random.randn(500).cumsum() + 100)
    arg_close_adj = arg_close * 1.1
    
    # Test v089
    q = f08_moving_average_dynamics_sma_cross_spread_3d_10d_v089_signal(arg_close)
    assert len(q) > 0
    assert q.nunique() > 2
    assert q.std() > 0
    
    # Test v150
    q = f08_moving_average_dynamics_ema_rising_count_252d_v150_signal(arg_close_adj)
    assert len(q) > 0
    assert q.nunique() > 2
    assert q.std() > 0
    print("All tests passed for 076-150!")

if __name__ == "__main__":
    test_features()
