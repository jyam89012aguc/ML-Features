# f20_volatility_compression_expansion_jerk_001_150_gemini.py
import pandas as pd
import numpy as np

def _vol_comp_ratio(vol_s, vol_l):
    return vol_s / vol_l.abs().replace(0, np.nan)

def _bb_width_val(c, w, k=2):
    ma = c.rolling(w).mean()
    std = c.rolling(w).std()
    return (2 * k * std) / ma.abs().replace(0, np.nan)

def _vol_expand_signal(vol, w):
    return (vol - vol.rolling(w).min()) / (vol.rolling(w).max() - vol.rolling(w).min()).replace(0, np.nan)

def _sma(s, w):
    return s.rolling(w, min_periods=min(w, 5)).mean()

def _std(s, w):
    return s.rolling(w, min_periods=min(w, 5)).std()

def _tr(h, l, c):
    cp = c.shift(1)
    return pd.concat([h - l, (h - cp).abs(), (l - cp).abs()], axis=1).max(axis=1)

def _atr(h, l, c, w):
    return _sma(_tr(h, l, c), w)

# [F001-F050] Volatility Ratio Jerks
def f20vce_f20_volatility_compression_expansion_vol_ratio_5d_21d_jerk_5d_v001_signal(close: pd.Series) -> pd.Series:
    res = _vol_comp_ratio(_std(close, 5), _std(close, 21)).pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20vce_f20_volatility_compression_expansion_vol_ratio_5d_63d_jerk_5d_v002_signal(closeadj: pd.Series) -> pd.Series:
    res = _vol_comp_ratio(_std(closeadj, 5), _std(closeadj, 63)).pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20vce_f20_volatility_compression_expansion_vol_ratio_10d_21d_jerk_5d_v003_signal(close: pd.Series) -> pd.Series:
    res = _vol_comp_ratio(_std(close, 10), _std(close, 21)).pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20vce_f20_volatility_compression_expansion_vol_ratio_10d_63d_jerk_5d_v004_signal(closeadj: pd.Series) -> pd.Series:
    res = _vol_comp_ratio(_std(closeadj, 10), _std(closeadj, 63)).pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20vce_f20_volatility_compression_expansion_vol_ratio_21d_42d_jerk_5d_v005_signal(closeadj: pd.Series) -> pd.Series:
    res = _vol_comp_ratio(_std(closeadj, 21), _std(closeadj, 42)).pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20vce_f20_volatility_compression_expansion_vol_ratio_21d_63d_jerk_5d_v006_signal(closeadj: pd.Series) -> pd.Series:
    res = _vol_comp_ratio(_std(closeadj, 21), _std(closeadj, 63)).pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20vce_f20_volatility_compression_expansion_vol_ratio_21d_126d_jerk_10d_v007_signal(closeadj: pd.Series) -> pd.Series:
    res = _vol_comp_ratio(_std(closeadj, 21), _std(closeadj, 126)).pct_change(10).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f20vce_f20_volatility_compression_expansion_vol_ratio_63d_126d_jerk_21d_v008_signal(closeadj: pd.Series) -> pd.Series:
    res = _vol_comp_ratio(_std(closeadj, 63), _std(closeadj, 126)).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f20vce_f20_volatility_compression_expansion_vol_ratio_63d_252d_jerk_21d_v009_signal(closeadj: pd.Series) -> pd.Series:
    res = _vol_comp_ratio(_std(closeadj, 63), _std(closeadj, 252)).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f20vce_f20_volatility_compression_expansion_vol_ratio_126d_252d_jerk_63d_v010_signal(closeadj: pd.Series) -> pd.Series:
    res = _vol_comp_ratio(_std(closeadj, 126), _std(closeadj, 252)).pct_change(63).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f20vce_f20_volatility_compression_expansion_vol_ratio_126d_504d_jerk_63d_v011_signal(closeadj: pd.Series) -> pd.Series:
    res = _vol_comp_ratio(_std(closeadj, 126), _std(closeadj, 504)).pct_change(63).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f20vce_f20_volatility_compression_expansion_vol_ratio_252d_504d_jerk_63d_v012_signal(closeadj: pd.Series) -> pd.Series:
    res = _vol_comp_ratio(_std(closeadj, 252), _std(closeadj, 504)).pct_change(63).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f20vce_f20_volatility_compression_expansion_vol_ratio_5d_126d_jerk_5d_v013_signal(closeadj: pd.Series) -> pd.Series:
    res = _vol_comp_ratio(_std(closeadj, 5), _std(closeadj, 126)).pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20vce_f20_volatility_compression_expansion_vol_ratio_10d_126d_jerk_10d_v014_signal(closeadj: pd.Series) -> pd.Series:
    res = _vol_comp_ratio(_std(closeadj, 10), _std(closeadj, 126)).pct_change(10).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f20vce_f20_volatility_compression_expansion_vol_ratio_21d_252d_jerk_21d_v015_signal(closeadj: pd.Series) -> pd.Series:
    res = _vol_comp_ratio(_std(closeadj, 21), _std(closeadj, 252)).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f20vce_f20_volatility_compression_expansion_vol_ratio_42d_126d_jerk_21d_v016_signal(closeadj: pd.Series) -> pd.Series:
    res = _vol_comp_ratio(_std(closeadj, 42), _std(closeadj, 126)).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f20vce_f20_volatility_compression_expansion_vol_ratio_63d_504d_jerk_63d_v017_signal(closeadj: pd.Series) -> pd.Series:
    res = _vol_comp_ratio(_std(closeadj, 63), _std(closeadj, 504)).pct_change(63).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f20vce_f20_volatility_compression_expansion_vol_ratio_126d_756d_jerk_63d_v018_signal(closeadj: pd.Series) -> pd.Series:
    res = _vol_comp_ratio(_std(closeadj, 126), _std(closeadj, 756)).pct_change(63).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f20vce_f20_volatility_compression_expansion_vol_ratio_5d_21d_jerk_10d_v019_signal(close: pd.Series) -> pd.Series:
    res = _vol_comp_ratio(_std(close, 5), _std(close, 21)).pct_change(10).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f20vce_f20_volatility_compression_expansion_vol_ratio_10d_63d_jerk_21d_v020_signal(closeadj: pd.Series) -> pd.Series:
    res = _vol_comp_ratio(_std(closeadj, 10), _std(closeadj, 63)).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# [F021-F040] BB Width Jerks
def f20vce_f20_volatility_compression_expansion_bb_width_5d_jerk_5d_v021_signal(close: pd.Series) -> pd.Series:
    res = _bb_width_val(close, 5, 2.0).pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20vce_f20_volatility_compression_expansion_bb_width_10d_jerk_5d_v022_signal(close: pd.Series) -> pd.Series:
    res = _bb_width_val(close, 10, 2.0).pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20vce_f20_volatility_compression_expansion_bb_width_21d_jerk_5d_v023_signal(close: pd.Series) -> pd.Series:
    res = _bb_width_val(close, 21, 2.0).pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20vce_f20_volatility_compression_expansion_bb_width_42d_jerk_10d_v024_signal(closeadj: pd.Series) -> pd.Series:
    res = _bb_width_val(closeadj, 42, 2.0).pct_change(10).pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f20vce_f20_volatility_compression_expansion_bb_width_63d_jerk_21d_v025_signal(closeadj: pd.Series) -> pd.Series:
    res = _bb_width_val(closeadj, 63, 2.0).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f20vce_f20_volatility_compression_expansion_bb_width_126d_jerk_21d_v026_signal(closeadj: pd.Series) -> pd.Series:
    res = _bb_width_val(closeadj, 126, 2.0).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f20vce_f20_volatility_compression_expansion_bb_width_252d_jerk_63d_v027_signal(closeadj: pd.Series) -> pd.Series:
    res = _bb_width_val(closeadj, 252, 2.0).pct_change(63).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f20vce_f20_volatility_compression_expansion_bb_width_504d_jerk_63d_v028_signal(closeadj: pd.Series) -> pd.Series:
    res = _bb_width_val(closeadj, 504, 2.0).pct_change(63).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f20vce_f20_volatility_compression_expansion_bb_width_21d_k1_0_jerk_5d_v029_signal(close: pd.Series) -> pd.Series:
    res = _bb_width_val(close, 21, 1.0).pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20vce_f20_volatility_compression_expansion_bb_width_63d_k1_5_jerk_21d_v030_signal(closeadj: pd.Series) -> pd.Series:
    res = _bb_width_val(closeadj, 63, 1.5).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# F031-F150
def f20vce_f20_volatility_compression_expansion_v031_jerk_signal(closeadj: pd.Series) -> pd.Series:
    return _bb_width_val(closeadj, 10, 2.0).pct_change(5).pct_change(5).replace([np.inf, -np.inf], np.nan)
def f20vce_f20_volatility_compression_expansion_v032_jerk_signal(closeadj: pd.Series) -> pd.Series:
    return _vol_comp_ratio(_std(closeadj, 21), _std(closeadj, 63)).pct_change(10).pct_change(10).replace([np.inf, -np.inf], np.nan)
def f20vce_f20_volatility_compression_expansion_v033_jerk_signal(closeadj: pd.Series) -> pd.Series:
    return _vol_expand_signal(_std(closeadj, 42), 126).diff(5).diff(5).replace([np.inf, -np.inf], np.nan)
def f20vce_f20_volatility_compression_expansion_v034_jerk_signal(closeadj: pd.Series) -> pd.Series:
    return _bb_width_val(closeadj, 63, 1.5).pct_change(21).pct_change(21).replace([np.inf, -np.inf], np.nan)
def f20vce_f20_volatility_compression_expansion_v035_jerk_signal(closeadj: pd.Series) -> pd.Series:
    return _vol_comp_ratio(_std(closeadj, 126), _std(closeadj, 252)).pct_change(63).pct_change(63).replace([np.inf, -np.inf], np.nan)
def f20vce_f20_volatility_compression_expansion_v036_jerk_signal(closeadj: pd.Series) -> pd.Series:
    return _vol_expand_signal(_std(closeadj, 5), 21).diff(5).diff(10).replace([np.inf, -np.inf], np.nan)
def f20vce_f20_volatility_compression_expansion_v037_jerk_signal(closeadj: pd.Series) -> pd.Series:
    return _bb_width_val(closeadj, 10, 1.25).pct_change(5).pct_change(21).replace([np.inf, -np.inf], np.nan)
def f20vce_f20_volatility_compression_expansion_v038_jerk_signal(closeadj: pd.Series) -> pd.Series:
    return _vol_comp_ratio(_std(closeadj, 21), _std(closeadj, 126)).pct_change(10).pct_change(63).replace([np.inf, -np.inf], np.nan)
def f20vce_f20_volatility_compression_expansion_v039_jerk_signal(closeadj: pd.Series) -> pd.Series:
    return _vol_expand_signal(_std(closeadj, 63), 252).diff(21).diff(5).replace([np.inf, -np.inf], np.nan)
def f20vce_f20_volatility_compression_expansion_v040_jerk_signal(closeadj: pd.Series) -> pd.Series:
    return _bb_width_val(closeadj, 126, 2.5).pct_change(63).pct_change(10).replace([np.inf, -np.inf], np.nan)
def f20vce_f20_volatility_compression_expansion_v041_jerk_signal(closeadj: pd.Series) -> pd.Series:
    return _vol_comp_ratio(_std(closeadj, 252), _std(closeadj, 504)).pct_change(5).pct_change(21).replace([np.inf, -np.inf], np.nan)
def f20vce_f20_volatility_compression_expansion_v042_jerk_signal(closeadj: pd.Series) -> pd.Series:
    return _vol_expand_signal(_std(closeadj, 5), 42).diff(10).diff(63).replace([np.inf, -np.inf], np.nan)
def f20vce_f20_volatility_compression_expansion_v043_jerk_signal(closeadj: pd.Series) -> pd.Series:
    return _bb_width_val(closeadj, 10, 0.75).pct_change(21).pct_change(5).replace([np.inf, -np.inf], np.nan)
def f20vce_f20_volatility_compression_expansion_v044_jerk_signal(closeadj: pd.Series) -> pd.Series:
    return _vol_comp_ratio(_std(closeadj, 21), _std(closeadj, 42)).pct_change(63).pct_change(10).replace([np.inf, -np.inf], np.nan)
def f20vce_f20_volatility_compression_expansion_v045_jerk_signal(closeadj: pd.Series) -> pd.Series:
    return _vol_expand_signal(_std(closeadj, 63), 126).diff(5).diff(21).replace([np.inf, -np.inf], np.nan)
def f20vce_f20_volatility_compression_expansion_v046_jerk_signal(closeadj: pd.Series) -> pd.Series:
    return _bb_width_val(closeadj, 126, 1.75).pct_change(10).pct_change(63).replace([np.inf, -np.inf], np.nan)
def f20vce_f20_volatility_compression_expansion_v047_jerk_signal(closeadj: pd.Series) -> pd.Series:
    return _vol_comp_ratio(_std(closeadj, 252), _std(closeadj, 756)).pct_change(21).pct_change(5).replace([np.inf, -np.inf], np.nan)
def f20vce_f20_volatility_compression_expansion_v048_jerk_signal(closeadj: pd.Series) -> pd.Series:
    return _vol_expand_signal(_std(closeadj, 10), 63).diff(63).diff(10).replace([np.inf, -np.inf], np.nan)
def f20vce_f20_volatility_compression_expansion_v049_jerk_signal(closeadj: pd.Series) -> pd.Series:
    return _bb_width_val(closeadj, 21, 2.25).pct_change(5).pct_change(21).replace([np.inf, -np.inf], np.nan)
def f20vce_f20_volatility_compression_expansion_v050_jerk_signal(closeadj: pd.Series) -> pd.Series:
    return _vol_comp_ratio(_std(closeadj, 63), _std(closeadj, 126)).pct_change(10).pct_change(63).replace([np.inf, -np.inf], np.nan)

# F051-F100
def f20vce_f20_volatility_compression_expansion_v051_jerk_signal(closeadj: pd.Series) -> pd.Series:
    return _vol_expand_signal(_std(closeadj, 126), 252).diff(21).diff(5).replace([np.inf, -np.inf], np.nan)
def f20vce_f20_volatility_compression_expansion_v052_jerk_signal(closeadj: pd.Series) -> pd.Series:
    return _bb_width_val(closeadj, 252, 1.1).pct_change(63).pct_change(10).replace([np.inf, -np.inf], np.nan)
def f20vce_f20_volatility_compression_expansion_v053_jerk_signal(closeadj: pd.Series) -> pd.Series:
    return _vol_comp_ratio(_std(closeadj, 5), _std(closeadj, 21)).pct_change(5).pct_change(21).replace([np.inf, -np.inf], np.nan)
def f20vce_f20_volatility_compression_expansion_v054_jerk_signal(closeadj: pd.Series) -> pd.Series:
    return _vol_expand_signal(_std(closeadj, 10), 126).diff(10).diff(63).replace([np.inf, -np.inf], np.nan)
def f20vce_f20_volatility_compression_expansion_v055_jerk_signal(closeadj: pd.Series) -> pd.Series:
    return _bb_width_val(closeadj, 21, 1.9).pct_change(21).pct_change(5).replace([np.inf, -np.inf], np.nan)
def f20vce_f20_volatility_compression_expansion_v056_jerk_signal(closeadj: pd.Series) -> pd.Series:
    return _vol_comp_ratio(_std(closeadj, 63), _std(closeadj, 504)).pct_change(63).pct_change(10).replace([np.inf, -np.inf], np.nan)
def f20vce_f20_volatility_compression_expansion_v057_jerk_signal(closeadj: pd.Series) -> pd.Series:
    return _vol_expand_signal(_std(closeadj, 126), 504).diff(5).diff(21).replace([np.inf, -np.inf], np.nan)
def f20vce_f20_volatility_compression_expansion_v058_jerk_signal(closeadj: pd.Series) -> pd.Series:
    return _bb_width_val(closeadj, 252, 2.8).pct_change(10).pct_change(63).replace([np.inf, -np.inf], np.nan)
def f20vce_f20_volatility_compression_expansion_v059_jerk_signal(closeadj: pd.Series) -> pd.Series:
    return _vol_comp_ratio(_std(closeadj, 10), _std(closeadj, 252)).pct_change(21).pct_change(5).replace([np.inf, -np.inf], np.nan)
def f20vce_f20_volatility_compression_expansion_v060_jerk_signal(closeadj: pd.Series) -> pd.Series:
    return _vol_expand_signal(_std(closeadj, 21), 63).diff(63).diff(10).replace([np.inf, -np.inf], np.nan)
def f20vce_f20_volatility_compression_expansion_v061_jerk_signal(closeadj: pd.Series) -> pd.Series:
    return _bb_width_val(closeadj, 42, 1.3).pct_change(5).pct_change(21).replace([np.inf, -np.inf], np.nan)
def f20vce_f20_volatility_compression_expansion_v064_jerk_signal(closeadj: pd.Series) -> pd.Series:
    return _bb_width_val(closeadj, 252, 2.1).pct_change(63).pct_change(10).replace([np.inf, -np.inf], np.nan)
def f20vce_f20_volatility_compression_expansion_v065_jerk_signal(closeadj: pd.Series) -> pd.Series:
    return _vol_comp_ratio(_std(closeadj, 5), _std(closeadj, 42)).pct_change(5).pct_change(21).replace([np.inf, -np.inf], np.nan)
def f20vce_f20_volatility_compression_expansion_v066_jerk_signal(closeadj: pd.Series) -> pd.Series:
    return _vol_expand_signal(_std(closeadj, 10), 21).diff(10).diff(63).replace([np.inf, -np.inf], np.nan)
def f20vce_f20_volatility_compression_expansion_v067_jerk_signal(closeadj: pd.Series) -> pd.Series:
    return _bb_width_val(closeadj, 21, 1.6).pct_change(21).pct_change(5).replace([np.inf, -np.inf], np.nan)
def f20vce_f20_volatility_compression_expansion_v068_jerk_signal(closeadj: pd.Series) -> pd.Series:
    return _vol_comp_ratio(_std(closeadj, 63), _std(closeadj, 252)).pct_change(63).pct_change(10).replace([np.inf, -np.inf], np.nan)
def f20vce_f20_volatility_compression_expansion_v070_jerk_signal(closeadj: pd.Series) -> pd.Series:
    return _bb_width_val(closeadj, 252, 2.4).pct_change(10).pct_change(63).replace([np.inf, -np.inf], np.nan)
def f20vce_f20_volatility_compression_expansion_v071_jerk_signal(closeadj: pd.Series) -> pd.Series:
    return _vol_comp_ratio(_std(closeadj, 10), _std(closeadj, 63)).pct_change(21).pct_change(5).replace([np.inf, -np.inf], np.nan)
def f20vce_f20_volatility_compression_expansion_v072_jerk_signal(closeadj: pd.Series) -> pd.Series:
    return _vol_expand_signal(_std(closeadj, 21), 126).diff(63).diff(10).replace([np.inf, -np.inf], np.nan)
def f20vce_f20_volatility_compression_expansion_v073_jerk_signal(closeadj: pd.Series) -> pd.Series:
    return _bb_width_val(closeadj, 42, 1.4).pct_change(5).pct_change(21).replace([np.inf, -np.inf], np.nan)
def f20vce_f20_volatility_compression_expansion_v076_jerk_signal(closeadj: pd.Series) -> pd.Series:
    return _bb_width_val(closeadj, 252, 2.2).pct_change(63).pct_change(10).replace([np.inf, -np.inf], np.nan)
def f20vce_f20_volatility_compression_expansion_v077_jerk_signal(closeadj: pd.Series) -> pd.Series:
    return _vol_comp_ratio(_std(closeadj, 5), _std(closeadj, 63)).pct_change(5).pct_change(21).replace([np.inf, -np.inf], np.nan)
def f20vce_f20_volatility_compression_expansion_v078_jerk_signal(closeadj: pd.Series) -> pd.Series:
    return _vol_expand_signal(_std(closeadj, 10), 42).diff(10).diff(63).replace([np.inf, -np.inf], np.nan)
def f20vce_f20_volatility_compression_expansion_v079_jerk_signal(closeadj: pd.Series) -> pd.Series:
    return _bb_width_val(closeadj, 21, 1.8).pct_change(21).pct_change(5).replace([np.inf, -np.inf], np.nan)
def f20vce_f20_volatility_compression_expansion_v081_jerk_signal(closeadj: pd.Series) -> pd.Series:
    return _vol_expand_signal(_std(closeadj, 126), 756).diff(5).diff(21).replace([np.inf, -np.inf], np.nan)
def f20vce_f20_volatility_compression_expansion_v082_jerk_signal(closeadj: pd.Series) -> pd.Series:
    return _bb_width_val(closeadj, 252, 2.6).pct_change(10).pct_change(63).replace([np.inf, -np.inf], np.nan)
def f20vce_f20_volatility_compression_expansion_v083_jerk_signal(closeadj: pd.Series) -> pd.Series:
    return _vol_comp_ratio(_std(closeadj, 10), _std(closeadj, 126)).pct_change(21).pct_change(5).replace([np.inf, -np.inf], np.nan)
def f20vce_f20_volatility_compression_expansion_v084_jerk_signal(closeadj: pd.Series) -> pd.Series:
    return _vol_expand_signal(_std(closeadj, 21), 252).diff(63).diff(10).replace([np.inf, -np.inf], np.nan)
def f20vce_f20_volatility_compression_expansion_v085_jerk_signal(closeadj: pd.Series) -> pd.Series:
    return _bb_width_val(closeadj, 42, 1.5).pct_change(5).pct_change(21).replace([np.inf, -np.inf], np.nan)
def f20vce_f20_volatility_compression_expansion_v086_jerk_signal(closeadj: pd.Series) -> pd.Series:
    return _vol_comp_ratio(_std(closeadj, 63), _std(closeadj, 252)).pct_change(10).pct_change(63).replace([np.inf, -np.inf], np.nan)
def f20vce_f20_volatility_compression_expansion_v087_jerk_signal(closeadj: pd.Series) -> pd.Series:
    return _vol_expand_signal(_std(closeadj, 126), 504).diff(21).diff(5).replace([np.inf, -np.inf], np.nan)
def f20vce_f20_volatility_compression_expansion_v088_jerk_signal(closeadj: pd.Series) -> pd.Series:
    return _bb_width_val(closeadj, 252, 2.3).pct_change(63).pct_change(10).replace([np.inf, -np.inf], np.nan)
def f20vce_f20_volatility_compression_expansion_v089_jerk_signal(closeadj: pd.Series) -> pd.Series:
    return _vol_comp_ratio(_std(closeadj, 5), _std(closeadj, 126)).pct_change(5).pct_change(21).replace([np.inf, -np.inf], np.nan)
def f20vce_f20_volatility_compression_expansion_v090_jerk_signal(closeadj: pd.Series) -> pd.Series:
    return _vol_expand_signal(_std(closeadj, 10), 63).diff(10).diff(63).replace([np.inf, -np.inf], np.nan)
def f20vce_f20_volatility_compression_expansion_v091_jerk_signal(closeadj: pd.Series) -> pd.Series:
    return _bb_width_val(closeadj, 21, 1.7).pct_change(21).pct_change(5).replace([np.inf, -np.inf], np.nan)
def f20vce_f20_volatility_compression_expansion_v092_jerk_signal(closeadj: pd.Series) -> pd.Series:
    return _vol_comp_ratio(_std(closeadj, 63), _std(closeadj, 756)).pct_change(63).pct_change(10).replace([np.inf, -np.inf], np.nan)
def f20vce_f20_volatility_compression_expansion_v093_jerk_signal(closeadj: pd.Series) -> pd.Series:
    return _vol_expand_signal(_std(closeadj, 126), 1008).diff(5).diff(21).replace([np.inf, -np.inf], np.nan)
def f20vce_f20_volatility_compression_expansion_v094_jerk_signal(closeadj: pd.Series) -> pd.Series:
    return _bb_width_val(closeadj, 252, 2.7).pct_change(10).pct_change(63).replace([np.inf, -np.inf], np.nan)
def f20vce_f20_volatility_compression_expansion_v095_jerk_signal(closeadj: pd.Series) -> pd.Series:
    return _vol_comp_ratio(_std(closeadj, 10), _std(closeadj, 504)).pct_change(21).pct_change(5).replace([np.inf, -np.inf], np.nan)
def f20vce_f20_volatility_compression_expansion_v096_jerk_signal(closeadj: pd.Series) -> pd.Series:
    return _vol_expand_signal(_std(closeadj, 21), 504).diff(63).diff(10).replace([np.inf, -np.inf], np.nan)
def f20vce_f20_volatility_compression_expansion_v097_jerk_signal(closeadj: pd.Series) -> pd.Series:
    return _bb_width_val(closeadj, 42, 1.1).pct_change(5).pct_change(21).replace([np.inf, -np.inf], np.nan)
def f20vce_f20_volatility_compression_expansion_v100_jerk_signal(closeadj: pd.Series) -> pd.Series:
    return _bb_width_val(closeadj, 252, 2.9).pct_change(63).pct_change(10).replace([np.inf, -np.inf], np.nan)

# F101-F150
def f20vce_f20_volatility_compression_expansion_v101_jerk_signal(closeadj: pd.Series) -> pd.Series:
    return _vol_comp_ratio(_std(closeadj, 5), _std(closeadj, 252)).pct_change(5).pct_change(21).replace([np.inf, -np.inf], np.nan)
def f20vce_f20_volatility_compression_expansion_v103_jerk_signal(closeadj: pd.Series) -> pd.Series:
    return _bb_width_val(closeadj, 21, 2.1).pct_change(21).pct_change(5).replace([np.inf, -np.inf], np.nan)
def f20vce_f20_volatility_compression_expansion_v104_jerk_signal(closeadj: pd.Series) -> pd.Series:
    return _vol_comp_ratio(_std(closeadj, 63), _std(closeadj, 1008)).pct_change(63).pct_change(10).replace([np.inf, -np.inf], np.nan)
def f20vce_f20_volatility_compression_expansion_v105_jerk_signal(closeadj: pd.Series) -> pd.Series:
    return _vol_expand_signal(_std(closeadj, 126), 1512).diff(5).diff(21).replace([np.inf, -np.inf], np.nan)
def f20vce_f20_volatility_compression_expansion_v106_jerk_signal(closeadj: pd.Series) -> pd.Series:
    return _bb_width_val(closeadj, 252, 0.9).pct_change(10).pct_change(63).replace([np.inf, -np.inf], np.nan)
def f20vce_f20_volatility_compression_expansion_v107_jerk_signal(closeadj: pd.Series) -> pd.Series:
    return _vol_comp_ratio(_std(closeadj, 10), _std(closeadj, 42)).pct_change(21).pct_change(5).replace([np.inf, -np.inf], np.nan)
def f20vce_f20_volatility_compression_expansion_v109_jerk_signal(closeadj: pd.Series) -> pd.Series:
    return _bb_width_val(closeadj, 42, 1.2).pct_change(5).pct_change(21).replace([np.inf, -np.inf], np.nan)
def f20vce_f20_volatility_compression_expansion_v112_jerk_signal(closeadj: pd.Series) -> pd.Series:
    return _bb_width_val(closeadj, 252, 2.05).pct_change(63).pct_change(10).replace([np.inf, -np.inf], np.nan)
def f20vce_f20_volatility_compression_expansion_v115_jerk_signal(closeadj: pd.Series) -> pd.Series:
    return _bb_width_val(closeadj, 21, 1.95).pct_change(21).pct_change(5).replace([np.inf, -np.inf], np.nan)
def f20vce_f20_volatility_compression_expansion_v118_jerk_signal(closeadj: pd.Series) -> pd.Series:
    return _bb_width_val(closeadj, 252, 2.15).pct_change(10).pct_change(63).replace([np.inf, -np.inf], np.nan)
def f20vce_f20_volatility_compression_expansion_v121_jerk_signal(closeadj: pd.Series) -> pd.Series:
    return _bb_width_val(closeadj, 42, 1.15).pct_change(5).pct_change(21).replace([np.inf, -np.inf], np.nan)
def f20vce_f20_volatility_compression_expansion_v124_jerk_signal(closeadj: pd.Series) -> pd.Series:
    return _bb_width_val(closeadj, 252, 1.85).pct_change(63).pct_change(10).replace([np.inf, -np.inf], np.nan)
def f20vce_f20_volatility_compression_expansion_v127_jerk_signal(closeadj: pd.Series) -> pd.Series:
    return _bb_width_val(closeadj, 21, 2.05).pct_change(21).pct_change(5).replace([np.inf, -np.inf], np.nan)
def f20vce_f20_volatility_compression_expansion_v130_jerk_signal(closeadj: pd.Series) -> pd.Series:
    return _bb_width_val(closeadj, 252, 2.25).pct_change(10).pct_change(63).replace([np.inf, -np.inf], np.nan)
def f20vce_f20_volatility_compression_expansion_v133_jerk_signal(closeadj: pd.Series) -> pd.Series:
    return _bb_width_val(closeadj, 42, 1.35).pct_change(5).pct_change(21).replace([np.inf, -np.inf], np.nan)
def f20vce_f20_volatility_compression_expansion_v136_jerk_signal(closeadj: pd.Series) -> pd.Series:
    return _bb_width_val(closeadj, 252, 2.45).pct_change(63).pct_change(10).replace([np.inf, -np.inf], np.nan)
def f20vce_f20_volatility_compression_expansion_v139_jerk_signal(closeadj: pd.Series) -> pd.Series:
    return _bb_width_val(closeadj, 21, 1.55).pct_change(21).pct_change(5).replace([np.inf, -np.inf], np.nan)
def f20vce_f20_volatility_compression_expansion_v142_jerk_signal(closeadj: pd.Series) -> pd.Series:
    return _bb_width_val(closeadj, 252, 2.65).pct_change(10).pct_change(63).replace([np.inf, -np.inf], np.nan)
def f20vce_f20_volatility_compression_expansion_v145_jerk_signal(closeadj: pd.Series) -> pd.Series:
    return _bb_width_val(closeadj, 42, 1.45).pct_change(5).pct_change(21).replace([np.inf, -np.inf], np.nan)
def f20vce_f20_volatility_compression_expansion_v148_jerk_signal(closeadj: pd.Series) -> pd.Series:
    return _bb_width_val(closeadj, 252, 1.15).pct_change(63).pct_change(10).replace([np.inf, -np.inf], np.nan)

SILVERDB_ACCESS, SOURCE_TABLE, ENTITY_COLUMN, DATE_COLUMN = "read_only", "sep", "ticker", "date"
ORDER_BY, NO_FORWARD_LOOKING = [ENTITY_COLUMN, DATE_COLUMN], True
SOURCE_COLUMNS = {c: f"sep.{c}" for c in ["close", "closeadj", "high", "low"]}

JERK_NAMES = [f for f in globals() if f.startswith("f20vce_") and f.endswith("_signal")]

F20_VOLATILITY_COMPRESSION_EXPANSION_JERK_REGISTRY_001_150 = {
    n: {
        "inputs": (inputs := [v for v in globals()[n].__code__.co_varnames[:globals()[n].__code__.co_argcount]]),
        "source_table": SOURCE_TABLE,
        "source_columns": {c: SOURCE_COLUMNS[c] for c in inputs if c in SOURCE_COLUMNS},
        "entity_column": ENTITY_COLUMN, "date_column": DATE_COLUMN,
        "order_by": ORDER_BY, "no_forward_looking": NO_FORWARD_LOOKING, "func": globals()[n]
    } for n in sorted(JERK_NAMES)
}

if __name__ == "__main__":
    sz = 1000
    d = pd.DataFrame({
        "close": np.random.randn(sz).cumsum() + 100,
        "closeadj": np.random.randn(sz).cumsum() + 100,
        "high": np.random.randn(sz).cumsum() + 110,
        "low": np.random.randn(sz).cumsum() + 90,
        "ticker": ["T"] * sz,
        "date": pd.date_range("2020-01-01", periods=sz)
    })
    for n, c in F20_VOLATILITY_COMPRESSION_EXPANSION_JERK_REGISTRY_001_150.items():
        r = c["func"](**{i: d[i] for i in c["inputs"]})
        assert isinstance(r, pd.Series)
    print("jerk 001_150 OK")
