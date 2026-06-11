# f08_moving_average_dynamics_base_001_075_gemini.py
import pandas as pd
import numpy as np

def _sma(s, w): return s.rolling(w, min_periods=min(w, 5)).mean()
def _ema(s, w): return s.ewm(span=w, min_periods=min(w, 5), adjust=False).mean()
def _mad_slope(ma, w): return (ma - ma.shift(w)) / w
def _mad_spread(ma1, ma2): return (ma1 / ma2.replace(0, np.nan) - 1)

# SMA Spread 001-022
def f08_moving_average_dynamics_open_sma_spread_3d_v001_signal(arg_open: pd.Series) -> pd.Series:
    res = _mad_spread(arg_open, _sma(arg_open, 3))
    return res.replace([np.inf, -np.inf], np.nan)

def f08_moving_average_dynamics_high_sma_spread_3d_v002_signal(arg_high: pd.Series) -> pd.Series:
    res = _mad_spread(arg_high, _sma(arg_high, 3))
    return res.replace([np.inf, -np.inf], np.nan)

def f08_moving_average_dynamics_low_sma_spread_3d_v003_signal(arg_low: pd.Series) -> pd.Series:
    res = _mad_spread(arg_low, _sma(arg_low, 3))
    return res.replace([np.inf, -np.inf], np.nan)

def f08_moving_average_dynamics_close_sma_spread_3d_v004_signal(arg_close: pd.Series) -> pd.Series:
    res = _mad_spread(arg_close, _sma(arg_close, 3))
    return res.replace([np.inf, -np.inf], np.nan)

def f08_moving_average_dynamics_open_sma_spread_5d_v005_signal(arg_open: pd.Series) -> pd.Series:
    res = _mad_spread(arg_open, _sma(arg_open, 5))
    return res.replace([np.inf, -np.inf], np.nan)

def f08_moving_average_dynamics_high_sma_spread_5d_v006_signal(arg_high: pd.Series) -> pd.Series:
    res = _mad_spread(arg_high, _sma(arg_high, 5))
    return res.replace([np.inf, -np.inf], np.nan)

def f08_moving_average_dynamics_low_sma_spread_5d_v007_signal(arg_low: pd.Series) -> pd.Series:
    res = _mad_spread(arg_low, _sma(arg_low, 5))
    return res.replace([np.inf, -np.inf], np.nan)

def f08_moving_average_dynamics_close_sma_spread_5d_v008_signal(arg_close: pd.Series) -> pd.Series:
    res = _mad_spread(arg_close, _sma(arg_close, 5))
    return res.replace([np.inf, -np.inf], np.nan)

def f08_moving_average_dynamics_close_sma_spread_8d_v009_signal(arg_close: pd.Series) -> pd.Series:
    res = _mad_spread(arg_close, _sma(arg_close, 8))
    return res.replace([np.inf, -np.inf], np.nan)

def f08_moving_average_dynamics_close_sma_spread_10d_v010_signal(arg_close: pd.Series) -> pd.Series:
    res = _mad_spread(arg_close, _sma(arg_close, 10))
    return res.replace([np.inf, -np.inf], np.nan)

def f08_moving_average_dynamics_close_sma_spread_12d_v011_signal(arg_close: pd.Series) -> pd.Series:
    res = _mad_spread(arg_close, _sma(arg_close, 12))
    return res.replace([np.inf, -np.inf], np.nan)

def f08_moving_average_dynamics_close_sma_spread_15d_v012_signal(arg_close: pd.Series) -> pd.Series:
    res = _mad_spread(arg_close, _sma(arg_close, 15))
    return res.replace([np.inf, -np.inf], np.nan)

def f08_moving_average_dynamics_close_sma_spread_20d_v013_signal(arg_close: pd.Series) -> pd.Series:
    res = _mad_spread(arg_close, _sma(arg_close, 20))
    return res.replace([np.inf, -np.inf], np.nan)

def f08_moving_average_dynamics_close_sma_spread_21d_v014_signal(arg_close: pd.Series) -> pd.Series:
    res = _mad_spread(arg_close, _sma(arg_close, 21))
    return res.replace([np.inf, -np.inf], np.nan)

def f08_moving_average_dynamics_closeadj_sma_spread_30d_v015_signal(arg_close_adj: pd.Series) -> pd.Series:
    res = _mad_spread(arg_close_adj, _sma(arg_close_adj, 30))
    return res.replace([np.inf, -np.inf], np.nan)

def f08_moving_average_dynamics_closeadj_sma_spread_40d_v016_signal(arg_close_adj: pd.Series) -> pd.Series:
    res = _mad_spread(arg_close_adj, _sma(arg_close_adj, 40))
    return res.replace([np.inf, -np.inf], np.nan)

def f08_moving_average_dynamics_closeadj_sma_spread_50d_v017_signal(arg_close_adj: pd.Series) -> pd.Series:
    res = _mad_spread(arg_close_adj, _sma(arg_close_adj, 50))
    return res.replace([np.inf, -np.inf], np.nan)

def f08_moving_average_dynamics_closeadj_sma_spread_63d_v018_signal(arg_close_adj: pd.Series) -> pd.Series:
    res = _mad_spread(arg_close_adj, _sma(arg_close_adj, 63))
    return res.replace([np.inf, -np.inf], np.nan)

def f08_moving_average_dynamics_closeadj_sma_spread_100d_v019_signal(arg_close_adj: pd.Series) -> pd.Series:
    res = _mad_spread(arg_close_adj, _sma(arg_close_adj, 100))
    return res.replace([np.inf, -np.inf], np.nan)

def f08_moving_average_dynamics_closeadj_sma_spread_126d_v020_signal(arg_close_adj: pd.Series) -> pd.Series:
    res = _mad_spread(arg_close_adj, _sma(arg_close_adj, 126))
    return res.replace([np.inf, -np.inf], np.nan)

def f08_moving_average_dynamics_closeadj_sma_spread_200d_v021_signal(arg_close_adj: pd.Series) -> pd.Series:
    res = _mad_spread(arg_close_adj, _sma(arg_close_adj, 200))
    return res.replace([np.inf, -np.inf], np.nan)

def f08_moving_average_dynamics_closeadj_sma_spread_252d_v022_signal(arg_close_adj: pd.Series) -> pd.Series:
    res = _mad_spread(arg_close_adj, _sma(arg_close_adj, 252))
    return res.replace([np.inf, -np.inf], np.nan)

# EMA Spread 023-044
def f08_moving_average_dynamics_open_ema_spread_3d_v023_signal(arg_open: pd.Series) -> pd.Series:
    res = _mad_spread(arg_open, _ema(arg_open, 3))
    return res.replace([np.inf, -np.inf], np.nan)

def f08_moving_average_dynamics_high_ema_spread_3d_v024_signal(arg_high: pd.Series) -> pd.Series:
    res = _mad_spread(arg_high, _ema(arg_high, 3))
    return res.replace([np.inf, -np.inf], np.nan)

def f08_moving_average_dynamics_low_ema_spread_3d_v025_signal(arg_low: pd.Series) -> pd.Series:
    res = _mad_spread(arg_low, _ema(arg_low, 3))
    return res.replace([np.inf, -np.inf], np.nan)

def f08_moving_average_dynamics_close_ema_spread_3d_v026_signal(arg_close: pd.Series) -> pd.Series:
    res = _mad_spread(arg_close, _ema(arg_close, 3))
    return res.replace([np.inf, -np.inf], np.nan)

def f08_moving_average_dynamics_open_ema_spread_5d_v027_signal(arg_open: pd.Series) -> pd.Series:
    res = _mad_spread(arg_open, _ema(arg_open, 5))
    return res.replace([np.inf, -np.inf], np.nan)

def f08_moving_average_dynamics_high_ema_spread_5d_v028_signal(arg_high: pd.Series) -> pd.Series:
    res = _mad_spread(arg_high, _ema(arg_high, 5))
    return res.replace([np.inf, -np.inf], np.nan)

def f08_moving_average_dynamics_low_ema_spread_5d_v029_signal(arg_low: pd.Series) -> pd.Series:
    res = _mad_spread(arg_low, _ema(arg_low, 5))
    return res.replace([np.inf, -np.inf], np.nan)

def f08_moving_average_dynamics_close_ema_spread_5d_v030_signal(arg_close: pd.Series) -> pd.Series:
    res = _mad_spread(arg_close, _ema(arg_close, 5))
    return res.replace([np.inf, -np.inf], np.nan)

def f08_moving_average_dynamics_close_ema_spread_8d_v031_signal(arg_close: pd.Series) -> pd.Series:
    res = _mad_spread(arg_close, _ema(arg_close, 8))
    return res.replace([np.inf, -np.inf], np.nan)

def f08_moving_average_dynamics_close_ema_spread_10d_v032_signal(arg_close: pd.Series) -> pd.Series:
    res = _mad_spread(arg_close, _ema(arg_close, 10))
    return res.replace([np.inf, -np.inf], np.nan)

def f08_moving_average_dynamics_close_ema_spread_12d_v033_signal(arg_close: pd.Series) -> pd.Series:
    res = _mad_spread(arg_close, _ema(arg_close, 12))
    return res.replace([np.inf, -np.inf], np.nan)

def f08_moving_average_dynamics_close_ema_spread_15d_v034_signal(arg_close: pd.Series) -> pd.Series:
    res = _mad_spread(arg_close, _ema(arg_close, 15))
    return res.replace([np.inf, -np.inf], np.nan)

def f08_moving_average_dynamics_close_ema_spread_20d_v035_signal(arg_close: pd.Series) -> pd.Series:
    res = _mad_spread(arg_close, _ema(arg_close, 20))
    return res.replace([np.inf, -np.inf], np.nan)

def f08_moving_average_dynamics_close_ema_spread_21d_v036_signal(arg_close: pd.Series) -> pd.Series:
    res = _mad_spread(arg_close, _ema(arg_close, 21))
    return res.replace([np.inf, -np.inf], np.nan)

def f08_moving_average_dynamics_closeadj_ema_spread_30d_v037_signal(arg_close_adj: pd.Series) -> pd.Series:
    res = _mad_spread(arg_close_adj, _ema(arg_close_adj, 30))
    return res.replace([np.inf, -np.inf], np.nan)

def f08_moving_average_dynamics_closeadj_ema_spread_40d_v038_signal(arg_close_adj: pd.Series) -> pd.Series:
    res = _mad_spread(arg_close_adj, _ema(arg_close_adj, 40))
    return res.replace([np.inf, -np.inf], np.nan)

def f08_moving_average_dynamics_closeadj_ema_spread_50d_v039_signal(arg_close_adj: pd.Series) -> pd.Series:
    res = _mad_spread(arg_close_adj, _ema(arg_close_adj, 50))
    return res.replace([np.inf, -np.inf], np.nan)

def f08_moving_average_dynamics_closeadj_ema_spread_63d_v040_signal(arg_close_adj: pd.Series) -> pd.Series:
    res = _mad_spread(arg_close_adj, _ema(arg_close_adj, 63))
    return res.replace([np.inf, -np.inf], np.nan)

def f08_moving_average_dynamics_closeadj_ema_spread_100d_v041_signal(arg_close_adj: pd.Series) -> pd.Series:
    res = _mad_spread(arg_close_adj, _ema(arg_close_adj, 100))
    return res.replace([np.inf, -np.inf], np.nan)

def f08_moving_average_dynamics_closeadj_ema_spread_126d_v042_signal(arg_close_adj: pd.Series) -> pd.Series:
    res = _mad_spread(arg_close_adj, _ema(arg_close_adj, 126))
    return res.replace([np.inf, -np.inf], np.nan)

def f08_moving_average_dynamics_closeadj_ema_spread_200d_v043_signal(arg_close_adj: pd.Series) -> pd.Series:
    res = _mad_spread(arg_close_adj, _ema(arg_close_adj, 200))
    return res.replace([np.inf, -np.inf], np.nan)

def f08_moving_average_dynamics_closeadj_ema_spread_252d_v044_signal(arg_close_adj: pd.Series) -> pd.Series:
    res = _mad_spread(arg_close_adj, _ema(arg_close_adj, 252))
    return res.replace([np.inf, -np.inf], np.nan)

# SMA Slope 045-066
def f08_moving_average_dynamics_open_sma_slope_3d_v045_signal(arg_open: pd.Series) -> pd.Series:
    res = _mad_slope(_sma(arg_open, 3), 3)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_moving_average_dynamics_high_sma_slope_3d_v046_signal(arg_high: pd.Series) -> pd.Series:
    res = _mad_slope(_sma(arg_high, 3), 3)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_moving_average_dynamics_low_sma_slope_3d_v047_signal(arg_low: pd.Series) -> pd.Series:
    res = _mad_slope(_sma(arg_low, 3), 3)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_moving_average_dynamics_close_sma_slope_3d_v048_signal(arg_close: pd.Series) -> pd.Series:
    res = _mad_slope(_sma(arg_close, 3), 3)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_moving_average_dynamics_open_sma_slope_5d_v049_signal(arg_open: pd.Series) -> pd.Series:
    res = _mad_slope(_sma(arg_open, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_moving_average_dynamics_high_sma_slope_5d_v050_signal(arg_high: pd.Series) -> pd.Series:
    res = _mad_slope(_sma(arg_high, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_moving_average_dynamics_low_sma_slope_5d_v051_signal(arg_low: pd.Series) -> pd.Series:
    res = _mad_slope(_sma(arg_low, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_moving_average_dynamics_close_sma_slope_5d_v052_signal(arg_close: pd.Series) -> pd.Series:
    res = _mad_slope(_sma(arg_close, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_moving_average_dynamics_close_sma_slope_8d_v053_signal(arg_close: pd.Series) -> pd.Series:
    res = _mad_slope(_sma(arg_close, 8), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_moving_average_dynamics_close_sma_slope_10d_v054_signal(arg_close: pd.Series) -> pd.Series:
    res = _mad_slope(_sma(arg_close, 10), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_moving_average_dynamics_close_sma_slope_12d_v055_signal(arg_close: pd.Series) -> pd.Series:
    res = _mad_slope(_sma(arg_close, 12), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_moving_average_dynamics_close_sma_slope_15d_v056_signal(arg_close: pd.Series) -> pd.Series:
    res = _mad_slope(_sma(arg_close, 15), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_moving_average_dynamics_close_sma_slope_20d_v057_signal(arg_close: pd.Series) -> pd.Series:
    res = _mad_slope(_sma(arg_close, 20), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_moving_average_dynamics_close_sma_slope_21d_v058_signal(arg_close: pd.Series) -> pd.Series:
    res = _mad_slope(_sma(arg_close, 21), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_moving_average_dynamics_closeadj_sma_slope_30d_v059_signal(arg_close_adj: pd.Series) -> pd.Series:
    res = _mad_slope(_sma(arg_close_adj, 30), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_moving_average_dynamics_closeadj_sma_slope_40d_v060_signal(arg_close_adj: pd.Series) -> pd.Series:
    res = _mad_slope(_sma(arg_close_adj, 40), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_moving_average_dynamics_closeadj_sma_slope_50d_v061_signal(arg_close_adj: pd.Series) -> pd.Series:
    res = _mad_slope(_sma(arg_close_adj, 50), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_moving_average_dynamics_closeadj_sma_slope_63d_v062_signal(arg_close_adj: pd.Series) -> pd.Series:
    res = _mad_slope(_sma(arg_close_adj, 63), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_moving_average_dynamics_closeadj_sma_slope_100d_v063_signal(arg_close_adj: pd.Series) -> pd.Series:
    res = _mad_slope(_sma(arg_close_adj, 100), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_moving_average_dynamics_closeadj_sma_slope_126d_v064_signal(arg_close_adj: pd.Series) -> pd.Series:
    res = _mad_slope(_sma(arg_close_adj, 126), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_moving_average_dynamics_closeadj_sma_slope_200d_v065_signal(arg_close_adj: pd.Series) -> pd.Series:
    res = _mad_slope(_sma(arg_close_adj, 200), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_moving_average_dynamics_closeadj_sma_slope_252d_v066_signal(arg_close_adj: pd.Series) -> pd.Series:
    res = _mad_slope(_sma(arg_close_adj, 252), 63)
    return res.replace([np.inf, -np.inf], np.nan)

# EMA Slope 067-075
def f08_moving_average_dynamics_open_ema_slope_3d_v067_signal(arg_open: pd.Series) -> pd.Series:
    res = _mad_slope(_ema(arg_open, 3), 3)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_moving_average_dynamics_high_ema_slope_3d_v068_signal(arg_high: pd.Series) -> pd.Series:
    res = _mad_slope(_ema(arg_high, 3), 3)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_moving_average_dynamics_low_ema_slope_3d_v069_signal(arg_low: pd.Series) -> pd.Series:
    res = _mad_slope(_ema(arg_low, 3), 3)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_moving_average_dynamics_close_ema_slope_3d_v070_signal(arg_close: pd.Series) -> pd.Series:
    res = _mad_slope(_ema(arg_close, 3), 3)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_moving_average_dynamics_open_ema_slope_5d_v071_signal(arg_open: pd.Series) -> pd.Series:
    res = _mad_slope(_ema(arg_open, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_moving_average_dynamics_high_ema_slope_5d_v072_signal(arg_high: pd.Series) -> pd.Series:
    res = _mad_slope(_ema(arg_high, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_moving_average_dynamics_low_ema_slope_5d_v073_signal(arg_low: pd.Series) -> pd.Series:
    res = _mad_slope(_ema(arg_low, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_moving_average_dynamics_close_ema_slope_5d_v074_signal(arg_close: pd.Series) -> pd.Series:
    res = _mad_slope(_ema(arg_close, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_moving_average_dynamics_close_ema_slope_8d_v075_signal(arg_close: pd.Series) -> pd.Series:
    res = _mad_slope(_ema(arg_close, 8), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def test_features():
    arg_open = pd.Series(np.random.randn(500).cumsum() + 100)
    arg_high = arg_open + np.random.rand(500)
    arg_low = arg_open - np.random.rand(500)
    arg_close = arg_open + np.random.randn(500)
    arg_close_adj = arg_close * 1.1
    
    # Test v001
    q = f08_moving_average_dynamics_open_sma_spread_3d_v001_signal(arg_open)
    assert len(q) > 0
    assert q.nunique() > 2
    assert q.std() > 0
    
    # Test v075
    q = f08_moving_average_dynamics_close_ema_slope_8d_v075_signal(arg_close)
    assert len(q) > 0
    assert q.nunique() > 2
    assert q.std() > 0
    print("All tests passed for 001-075!")

if __name__ == "__main__":
    test_features()
