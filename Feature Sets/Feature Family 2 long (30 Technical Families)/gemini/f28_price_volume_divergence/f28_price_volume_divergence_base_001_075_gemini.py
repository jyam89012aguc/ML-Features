# f28_price_volume_divergence_base_001_075_gemini.py
import pandas as pd
import numpy as np

def _sma(s, w): return s.rolling(w, min_periods=min(w, 5)).mean()
def _ema(s, w): return s.ewm(span=w, min_periods=min(w, 5), adjust=False).mean()
def _z(s, w): return (s - _sma(s, w)) / s.rolling(w, min_periods=min(w, 5)).std().replace(0, np.nan)

def _pv_div_val(p_roc, v_roc): return p_roc - v_roc
def _pv_conv_val(p_roc, v_roc): return p_roc * v_roc
def _pv_spread_z(p_z, v_z): return p_z - v_z

# Feature 1: f28pvd_f28_price_volume_divergence_pv_div_5d
def f28pvd_f28_price_volume_divergence_pv_div_5d_base_v001_signal(close: pd.Series, volume: pd.Series) -> pd.Series:
    p_roc = close.pct_change(5)
    v_roc = volume.pct_change(5)
    res = _pv_div_val(p_roc, v_roc)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 2: f28pvd_f28_price_volume_divergence_pv_div_10d
def f28pvd_f28_price_volume_divergence_pv_div_10d_base_v002_signal(close: pd.Series, volume: pd.Series) -> pd.Series:
    p_roc = close.pct_change(10)
    v_roc = volume.pct_change(10)
    res = _pv_div_val(p_roc, v_roc)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 3: f28pvd_f28_price_volume_divergence_pv_div_15d
def f28pvd_f28_price_volume_divergence_pv_div_15d_base_v003_signal(close: pd.Series, volume: pd.Series) -> pd.Series:
    p_roc = close.pct_change(15)
    v_roc = volume.pct_change(15)
    res = _pv_div_val(p_roc, v_roc)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 4: f28pvd_f28_price_volume_divergence_pv_div_20d
def f28pvd_f28_price_volume_divergence_pv_div_20d_base_v004_signal(close: pd.Series, volume: pd.Series) -> pd.Series:
    p_roc = close.pct_change(20)
    v_roc = volume.pct_change(20)
    res = _pv_div_val(p_roc, v_roc)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 5: f28pvd_f28_price_volume_divergence_pv_div_21d
def f28pvd_f28_price_volume_divergence_pv_div_21d_base_v005_signal(close: pd.Series, volume: pd.Series) -> pd.Series:
    p_roc = close.pct_change(21)
    v_roc = volume.pct_change(21)
    res = _pv_div_val(p_roc, v_roc)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 6: f28pvd_f28_price_volume_divergence_pv_div_30d
def f28pvd_f28_price_volume_divergence_pv_div_30d_base_v006_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    p_roc = closeadj.pct_change(30)
    v_roc = volume.pct_change(30)
    res = _pv_div_val(p_roc, v_roc)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 7: f28pvd_f28_price_volume_divergence_pv_div_40d
def f28pvd_f28_price_volume_divergence_pv_div_40d_base_v007_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    p_roc = closeadj.pct_change(40)
    v_roc = volume.pct_change(40)
    res = _pv_div_val(p_roc, v_roc)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 8: f28pvd_f28_price_volume_divergence_pv_div_50d
def f28pvd_f28_price_volume_divergence_pv_div_50d_base_v008_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    p_roc = closeadj.pct_change(50)
    v_roc = volume.pct_change(50)
    res = _pv_div_val(p_roc, v_roc)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 9: f28pvd_f28_price_volume_divergence_pv_div_60d
def f28pvd_f28_price_volume_divergence_pv_div_60d_base_v009_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    p_roc = closeadj.pct_change(60)
    v_roc = volume.pct_change(60)
    res = _pv_div_val(p_roc, v_roc)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 10: f28pvd_f28_price_volume_divergence_pv_div_63d
def f28pvd_f28_price_volume_divergence_pv_div_63d_base_v010_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    p_roc = closeadj.pct_change(63)
    v_roc = volume.pct_change(63)
    res = _pv_div_val(p_roc, v_roc)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 11: f28pvd_f28_price_volume_divergence_pv_div_80d
def f28pvd_f28_price_volume_divergence_pv_div_80d_base_v011_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    p_roc = closeadj.pct_change(80)
    v_roc = volume.pct_change(80)
    res = _pv_div_val(p_roc, v_roc)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 12: f28pvd_f28_price_volume_divergence_pv_div_100d
def f28pvd_f28_price_volume_divergence_pv_div_100d_base_v012_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    p_roc = closeadj.pct_change(100)
    v_roc = volume.pct_change(100)
    res = _pv_div_val(p_roc, v_roc)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 13: f28pvd_f28_price_volume_divergence_pv_div_120d
def f28pvd_f28_price_volume_divergence_pv_div_120d_base_v013_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    p_roc = closeadj.pct_change(120)
    v_roc = volume.pct_change(120)
    res = _pv_div_val(p_roc, v_roc)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 14: f28pvd_f28_price_volume_divergence_pv_div_126d
def f28pvd_f28_price_volume_divergence_pv_div_126d_base_v014_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    p_roc = closeadj.pct_change(126)
    v_roc = volume.pct_change(126)
    res = _pv_div_val(p_roc, v_roc)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 15: f28pvd_f28_price_volume_divergence_pv_div_150d
def f28pvd_f28_price_volume_divergence_pv_div_150d_base_v015_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    p_roc = closeadj.pct_change(150)
    v_roc = volume.pct_change(150)
    res = _pv_div_val(p_roc, v_roc)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 16: f28pvd_f28_price_volume_divergence_pv_div_200d
def f28pvd_f28_price_volume_divergence_pv_div_200d_base_v016_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    p_roc = closeadj.pct_change(200)
    v_roc = volume.pct_change(200)
    res = _pv_div_val(p_roc, v_roc)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 17: f28pvd_f28_price_volume_divergence_pv_div_250d
def f28pvd_f28_price_volume_divergence_pv_div_250d_base_v017_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    p_roc = closeadj.pct_change(250)
    v_roc = volume.pct_change(250)
    res = _pv_div_val(p_roc, v_roc)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 18: f28pvd_f28_price_volume_divergence_pv_div_252d
def f28pvd_f28_price_volume_divergence_pv_div_252d_base_v018_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    p_roc = closeadj.pct_change(252)
    v_roc = volume.pct_change(252)
    res = _pv_div_val(p_roc, v_roc)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 19: f28pvd_f28_price_volume_divergence_pv_div_300d
def f28pvd_f28_price_volume_divergence_pv_div_300d_base_v019_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    p_roc = closeadj.pct_change(300)
    v_roc = volume.pct_change(300)
    res = _pv_div_val(p_roc, v_roc)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 20: f28pvd_f28_price_volume_divergence_pv_div_400d
def f28pvd_f28_price_volume_divergence_pv_div_400d_base_v020_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    p_roc = closeadj.pct_change(400)
    v_roc = volume.pct_change(400)
    res = _pv_div_val(p_roc, v_roc)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 21: f28pvd_f28_price_volume_divergence_pv_div_500d
def f28pvd_f28_price_volume_divergence_pv_div_500d_base_v021_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    p_roc = closeadj.pct_change(500)
    v_roc = volume.pct_change(500)
    res = _pv_div_val(p_roc, v_roc)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 22: f28pvd_f28_price_volume_divergence_pv_div_504d
def f28pvd_f28_price_volume_divergence_pv_div_504d_base_v022_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    p_roc = closeadj.pct_change(504)
    v_roc = volume.pct_change(504)
    res = _pv_div_val(p_roc, v_roc)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 23: f28pvd_f28_price_volume_divergence_pv_conv_5d
def f28pvd_f28_price_volume_divergence_pv_conv_5d_base_v023_signal(close: pd.Series, volume: pd.Series) -> pd.Series:
    p_roc = close.pct_change(5)
    v_roc = volume.pct_change(5)
    res = _pv_conv_val(p_roc, v_roc)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 24: f28pvd_f28_price_volume_divergence_pv_conv_10d
def f28pvd_f28_price_volume_divergence_pv_conv_10d_base_v024_signal(close: pd.Series, volume: pd.Series) -> pd.Series:
    p_roc = close.pct_change(10)
    v_roc = volume.pct_change(10)
    res = _pv_conv_val(p_roc, v_roc)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 25: f28pvd_f28_price_volume_divergence_pv_conv_15d
def f28pvd_f28_price_volume_divergence_pv_conv_15d_base_v025_signal(close: pd.Series, volume: pd.Series) -> pd.Series:
    p_roc = close.pct_change(15)
    v_roc = volume.pct_change(15)
    res = _pv_conv_val(p_roc, v_roc)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 26: f28pvd_f28_price_volume_divergence_pv_conv_20d
def f28pvd_f28_price_volume_divergence_pv_conv_20d_base_v026_signal(close: pd.Series, volume: pd.Series) -> pd.Series:
    p_roc = close.pct_change(20)
    v_roc = volume.pct_change(20)
    res = _pv_conv_val(p_roc, v_roc)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 27: f28pvd_f28_price_volume_divergence_pv_conv_21d
def f28pvd_f28_price_volume_divergence_pv_conv_21d_base_v027_signal(close: pd.Series, volume: pd.Series) -> pd.Series:
    p_roc = close.pct_change(21)
    v_roc = volume.pct_change(21)
    res = _pv_conv_val(p_roc, v_roc)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 28: f28pvd_f28_price_volume_divergence_pv_conv_30d
def f28pvd_f28_price_volume_divergence_pv_conv_30d_base_v028_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    p_roc = closeadj.pct_change(30)
    v_roc = volume.pct_change(30)
    res = _pv_conv_val(p_roc, v_roc)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 29: f28pvd_f28_price_volume_divergence_pv_conv_40d
def f28pvd_f28_price_volume_divergence_pv_conv_40d_base_v029_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    p_roc = closeadj.pct_change(40)
    v_roc = volume.pct_change(40)
    res = _pv_conv_val(p_roc, v_roc)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 30: f28pvd_f28_price_volume_divergence_pv_conv_50d
def f28pvd_f28_price_volume_divergence_pv_conv_50d_base_v030_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    p_roc = closeadj.pct_change(50)
    v_roc = volume.pct_change(50)
    res = _pv_conv_val(p_roc, v_roc)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 31: f28pvd_f28_price_volume_divergence_pv_conv_60d
def f28pvd_f28_price_volume_divergence_pv_conv_60d_base_v031_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    p_roc = closeadj.pct_change(60)
    v_roc = volume.pct_change(60)
    res = _pv_conv_val(p_roc, v_roc)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 32: f28pvd_f28_price_volume_divergence_pv_conv_63d
def f28pvd_f28_price_volume_divergence_pv_conv_63d_base_v032_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    p_roc = closeadj.pct_change(63)
    v_roc = volume.pct_change(63)
    res = _pv_conv_val(p_roc, v_roc)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 33: f28pvd_f28_price_volume_divergence_pv_conv_80d
def f28pvd_f28_price_volume_divergence_pv_conv_80d_base_v033_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    p_roc = closeadj.pct_change(80)
    v_roc = volume.pct_change(80)
    res = _pv_conv_val(p_roc, v_roc)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 34: f28pvd_f28_price_volume_divergence_pv_conv_100d
def f28pvd_f28_price_volume_divergence_pv_conv_100d_base_v034_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    p_roc = closeadj.pct_change(100)
    v_roc = volume.pct_change(100)
    res = _pv_conv_val(p_roc, v_roc)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 35: f28pvd_f28_price_volume_divergence_pv_conv_120d
def f28pvd_f28_price_volume_divergence_pv_conv_120d_base_v035_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    p_roc = closeadj.pct_change(120)
    v_roc = volume.pct_change(120)
    res = _pv_conv_val(p_roc, v_roc)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 36: f28pvd_f28_price_volume_divergence_pv_conv_126d
def f28pvd_f28_price_volume_divergence_pv_conv_126d_base_v036_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    p_roc = closeadj.pct_change(126)
    v_roc = volume.pct_change(126)
    res = _pv_conv_val(p_roc, v_roc)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 37: f28pvd_f28_price_volume_divergence_pv_conv_150d
def f28pvd_f28_price_volume_divergence_pv_conv_150d_base_v037_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    p_roc = closeadj.pct_change(150)
    v_roc = volume.pct_change(150)
    res = _pv_conv_val(p_roc, v_roc)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 38: f28pvd_f28_price_volume_divergence_pv_conv_200d
def f28pvd_f28_price_volume_divergence_pv_conv_200d_base_v038_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    p_roc = closeadj.pct_change(200)
    v_roc = volume.pct_change(200)
    res = _pv_conv_val(p_roc, v_roc)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 39: f28pvd_f28_price_volume_divergence_pv_conv_250d
def f28pvd_f28_price_volume_divergence_pv_conv_250d_base_v039_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    p_roc = closeadj.pct_change(250)
    v_roc = volume.pct_change(250)
    res = _pv_conv_val(p_roc, v_roc)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 40: f28pvd_f28_price_volume_divergence_pv_conv_252d
def f28pvd_f28_price_volume_divergence_pv_conv_252d_base_v040_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    p_roc = closeadj.pct_change(252)
    v_roc = volume.pct_change(252)
    res = _pv_conv_val(p_roc, v_roc)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 41: f28pvd_f28_price_volume_divergence_pv_conv_300d
def f28pvd_f28_price_volume_divergence_pv_conv_300d_base_v041_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    p_roc = closeadj.pct_change(300)
    v_roc = volume.pct_change(300)
    res = _pv_conv_val(p_roc, v_roc)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 42: f28pvd_f28_price_volume_divergence_pv_conv_400d
def f28pvd_f28_price_volume_divergence_pv_conv_400d_base_v042_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    p_roc = closeadj.pct_change(400)
    v_roc = volume.pct_change(400)
    res = _pv_conv_val(p_roc, v_roc)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 43: f28pvd_f28_price_volume_divergence_pv_conv_500d
def f28pvd_f28_price_volume_divergence_pv_conv_500d_base_v043_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    p_roc = closeadj.pct_change(500)
    v_roc = volume.pct_change(500)
    res = _pv_conv_val(p_roc, v_roc)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 44: f28pvd_f28_price_volume_divergence_pv_conv_504d
def f28pvd_f28_price_volume_divergence_pv_conv_504d_base_v044_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    p_roc = closeadj.pct_change(504)
    v_roc = volume.pct_change(504)
    res = _pv_conv_val(p_roc, v_roc)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 45: f28pvd_f28_price_volume_divergence_pv_zspread_5d
def f28pvd_f28_price_volume_divergence_pv_zspread_5d_base_v045_signal(close: pd.Series, volume: pd.Series) -> pd.Series:
    p_z = _z(close, 5)
    v_z = _z(volume, 5)
    res = _pv_spread_z(p_z, v_z)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 46: f28pvd_f28_price_volume_divergence_pv_zspread_10d
def f28pvd_f28_price_volume_divergence_pv_zspread_10d_base_v046_signal(close: pd.Series, volume: pd.Series) -> pd.Series:
    p_z = _z(close, 10)
    v_z = _z(volume, 10)
    res = _pv_spread_z(p_z, v_z)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 47: f28pvd_f28_price_volume_divergence_pv_zspread_15d
def f28pvd_f28_price_volume_divergence_pv_zspread_15d_base_v047_signal(close: pd.Series, volume: pd.Series) -> pd.Series:
    p_z = _z(close, 15)
    v_z = _z(volume, 15)
    res = _pv_spread_z(p_z, v_z)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 48: f28pvd_f28_price_volume_divergence_pv_zspread_20d
def f28pvd_f28_price_volume_divergence_pv_zspread_20d_base_v048_signal(close: pd.Series, volume: pd.Series) -> pd.Series:
    p_z = _z(close, 20)
    v_z = _z(volume, 20)
    res = _pv_spread_z(p_z, v_z)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 49: f28pvd_f28_price_volume_divergence_pv_zspread_21d
def f28pvd_f28_price_volume_divergence_pv_zspread_21d_base_v049_signal(close: pd.Series, volume: pd.Series) -> pd.Series:
    p_z = _z(close, 21)
    v_z = _z(volume, 21)
    res = _pv_spread_z(p_z, v_z)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 50: f28pvd_f28_price_volume_divergence_pv_zspread_30d
def f28pvd_f28_price_volume_divergence_pv_zspread_30d_base_v050_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    p_z = _z(closeadj, 30)
    v_z = _z(volume, 30)
    res = _pv_spread_z(p_z, v_z)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 51: f28pvd_f28_price_volume_divergence_pv_zspread_40d
def f28pvd_f28_price_volume_divergence_pv_zspread_40d_base_v051_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    p_z = _z(closeadj, 40)
    v_z = _z(volume, 40)
    res = _pv_spread_z(p_z, v_z)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 52: f28pvd_f28_price_volume_divergence_pv_zspread_50d
def f28pvd_f28_price_volume_divergence_pv_zspread_50d_base_v052_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    p_z = _z(closeadj, 50)
    v_z = _z(volume, 50)
    res = _pv_spread_z(p_z, v_z)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 53: f28pvd_f28_price_volume_divergence_pv_zspread_60d
def f28pvd_f28_price_volume_divergence_pv_zspread_60d_base_v053_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    p_z = _z(closeadj, 60)
    v_z = _z(volume, 60)
    res = _pv_spread_z(p_z, v_z)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 54: f28pvd_f28_price_volume_divergence_pv_zspread_63d
def f28pvd_f28_price_volume_divergence_pv_zspread_63d_base_v054_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    p_z = _z(closeadj, 63)
    v_z = _z(volume, 63)
    res = _pv_spread_z(p_z, v_z)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 55: f28pvd_f28_price_volume_divergence_pv_zspread_80d
def f28pvd_f28_price_volume_divergence_pv_zspread_80d_base_v055_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    p_z = _z(closeadj, 80)
    v_z = _z(volume, 80)
    res = _pv_spread_z(p_z, v_z)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 56: f28pvd_f28_price_volume_divergence_pv_zspread_100d
def f28pvd_f28_price_volume_divergence_pv_zspread_100d_base_v056_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    p_z = _z(closeadj, 100)
    v_z = _z(volume, 100)
    res = _pv_spread_z(p_z, v_z)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 57: f28pvd_f28_price_volume_divergence_pv_zspread_120d
def f28pvd_f28_price_volume_divergence_pv_zspread_120d_base_v057_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    p_z = _z(closeadj, 120)
    v_z = _z(volume, 120)
    res = _pv_spread_z(p_z, v_z)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 58: f28pvd_f28_price_volume_divergence_pv_zspread_126d
def f28pvd_f28_price_volume_divergence_pv_zspread_126d_base_v058_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    p_z = _z(closeadj, 126)
    v_z = _z(volume, 126)
    res = _pv_spread_z(p_z, v_z)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 59: f28pvd_f28_price_volume_divergence_pv_zspread_150d
def f28pvd_f28_price_volume_divergence_pv_zspread_150d_base_v059_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    p_z = _z(closeadj, 150)
    v_z = _z(volume, 150)
    res = _pv_spread_z(p_z, v_z)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 60: f28pvd_f28_price_volume_divergence_pv_zspread_200d
def f28pvd_f28_price_volume_divergence_pv_zspread_200d_base_v060_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    p_z = _z(closeadj, 200)
    v_z = _z(volume, 200)
    res = _pv_spread_z(p_z, v_z)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 61: f28pvd_f28_price_volume_divergence_pv_zspread_250d
def f28pvd_f28_price_volume_divergence_pv_zspread_250d_base_v061_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    p_z = _z(closeadj, 250)
    v_z = _z(volume, 250)
    res = _pv_spread_z(p_z, v_z)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 62: f28pvd_f28_price_volume_divergence_pv_zspread_252d
def f28pvd_f28_price_volume_divergence_pv_zspread_252d_base_v062_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    p_z = _z(closeadj, 252)
    v_z = _z(volume, 252)
    res = _pv_spread_z(p_z, v_z)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 63: f28pvd_f28_price_volume_divergence_pv_zspread_300d
def f28pvd_f28_price_volume_divergence_pv_zspread_300d_base_v063_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    p_z = _z(closeadj, 300)
    v_z = _z(volume, 300)
    res = _pv_spread_z(p_z, v_z)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 64: f28pvd_f28_price_volume_divergence_pv_zspread_400d
def f28pvd_f28_price_volume_divergence_pv_zspread_400d_base_v064_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    p_z = _z(closeadj, 400)
    v_z = _z(volume, 400)
    res = _pv_spread_z(p_z, v_z)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 65: f28pvd_f28_price_volume_divergence_pv_zspread_500d
def f28pvd_f28_price_volume_divergence_pv_zspread_500d_base_v065_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    p_z = _z(closeadj, 500)
    v_z = _z(volume, 500)
    res = _pv_spread_z(p_z, v_z)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 66: f28pvd_f28_price_volume_divergence_pv_zspread_504d
def f28pvd_f28_price_volume_divergence_pv_zspread_504d_base_v066_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    p_z = _z(closeadj, 504)
    v_z = _z(volume, 504)
    res = _pv_spread_z(p_z, v_z)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 67: f28pvd_f28_price_volume_divergence_pv_corr_5d
def f28pvd_f28_price_volume_divergence_pv_corr_5d_base_v067_signal(close: pd.Series, volume: pd.Series) -> pd.Series:
    p_roc = close.pct_change(5)
    v_roc = volume.pct_change(5)
    res = p_roc.rolling(5).corr(v_roc)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 68: f28pvd_f28_price_volume_divergence_pv_corr_10d
def f28pvd_f28_price_volume_divergence_pv_corr_10d_base_v068_signal(close: pd.Series, volume: pd.Series) -> pd.Series:
    p_roc = close.pct_change(5)
    v_roc = volume.pct_change(5)
    res = p_roc.rolling(10).corr(v_roc)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 69: f28pvd_f28_price_volume_divergence_pv_corr_15d
def f28pvd_f28_price_volume_divergence_pv_corr_15d_base_v069_signal(close: pd.Series, volume: pd.Series) -> pd.Series:
    p_roc = close.pct_change(5)
    v_roc = volume.pct_change(5)
    res = p_roc.rolling(15).corr(v_roc)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 70: f28pvd_f28_price_volume_divergence_pv_corr_20d
def f28pvd_f28_price_volume_divergence_pv_corr_20d_base_v070_signal(close: pd.Series, volume: pd.Series) -> pd.Series:
    p_roc = close.pct_change(5)
    v_roc = volume.pct_change(5)
    res = p_roc.rolling(20).corr(v_roc)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 71: f28pvd_f28_price_volume_divergence_pv_corr_21d
def f28pvd_f28_price_volume_divergence_pv_corr_21d_base_v071_signal(close: pd.Series, volume: pd.Series) -> pd.Series:
    p_roc = close.pct_change(5)
    v_roc = volume.pct_change(5)
    res = p_roc.rolling(21).corr(v_roc)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 72: f28pvd_f28_price_volume_divergence_pv_corr_30d
def f28pvd_f28_price_volume_divergence_pv_corr_30d_base_v072_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    p_roc = closeadj.pct_change(5)
    v_roc = volume.pct_change(5)
    res = p_roc.rolling(30).corr(v_roc)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 73: f28pvd_f28_price_volume_divergence_pv_corr_40d
def f28pvd_f28_price_volume_divergence_pv_corr_40d_base_v073_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    p_roc = closeadj.pct_change(5)
    v_roc = volume.pct_change(5)
    res = p_roc.rolling(40).corr(v_roc)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 74: f28pvd_f28_price_volume_divergence_pv_corr_50d
def f28pvd_f28_price_volume_divergence_pv_corr_50d_base_v074_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    p_roc = closeadj.pct_change(5)
    v_roc = volume.pct_change(5)
    res = p_roc.rolling(50).corr(v_roc)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 75: f28pvd_f28_price_volume_divergence_pv_corr_60d
def f28pvd_f28_price_volume_divergence_pv_corr_60d_base_v075_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    p_roc = closeadj.pct_change(5)
    v_roc = volume.pct_change(5)
    res = p_roc.rolling(60).corr(v_roc)
    return res.replace([np.inf, -np.inf], np.nan)

SILVERDB_ACCESS, SOURCE_TABLE, ENTITY_COLUMN, DATE_COLUMN = "read_only", "sep", "ticker", "date"
ORDER_BY, NO_FORWARD_LOOKING = [ENTITY_COLUMN, DATE_COLUMN], True
SOURCE_COLUMNS = {c: f"sep.{c}" for c in ["close", "closeadj", "high", "low", "volume"]}

BASE_NAMES = [f for f in globals() if f.startswith("f28pvd_") and f.endswith("_signal")]

F28_PRICE_VOLUME_DIVERGENCE_BASE_REGISTRY_001_075 = {
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
    for n, c in F28_PRICE_VOLUME_DIVERGENCE_BASE_REGISTRY_001_075.items():
        r = c["func"](**{i: d[i] for i in c["inputs"]})
        assert isinstance(r, pd.Series)
    print("base OK")