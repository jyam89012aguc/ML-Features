import pandas as pd
import numpy as np

def _sma(s, w): return s.rolling(w, min_periods=min(w, 5)).mean()
def _ema(s, w): return s.ewm(span=w, min_periods=min(w, 5), adjust=False).mean()
def _roc(s, w): return s.pct_change(w)
def _z(s, w): return (s - _sma(s, w)) / s.rolling(w, min_periods=min(w, 5)).std().replace(0, np.nan)

def _vp_conf(p_roc, v_roc):
    # High volume on positive returns = strong confirmation
    return (p_roc * v_roc)

def _vp_corr(p, v, w):
    return p.rolling(w).corr(v)

def _vp_trend_strength(p, v, w):
    p_up = (p > p.shift(1)).astype(float)
    return (p_up * v).rolling(w).sum() / v.rolling(w).sum().replace(0, np.nan)

# --- Jerk Functions 001-150 ---

# 001-050: Jerks of VP Confirmation
def f24vpc_f24_volume_price_confirmation_vp_conf_p22_v22_jerk_22_22_v001_signal(arg_closeadj, arg_volume) -> pd.Series:
    """22,22-day jerk of 22-day VP confirmation."""
    res = _roc(_roc(_vp_conf(_roc(arg_closeadj, 22), _roc(arg_volume, 22)), 22), 22)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_conf_p22_v22_jerk_63_22_v002_signal(arg_closeadj, arg_volume) -> pd.Series:
    """63,22-day jerk of 22-day VP confirmation."""
    res = _roc(_roc(_vp_conf(_roc(arg_closeadj, 22), _roc(arg_volume, 22)), 63), 22)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_conf_p22_v22_jerk_63_63_v003_signal(arg_closeadj, arg_volume) -> pd.Series:
    """63,63-day jerk of 22-day VP confirmation."""
    res = _roc(_roc(_vp_conf(_roc(arg_closeadj, 22), _roc(arg_volume, 22)), 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_conf_p44_v44_jerk_44_44_v004_signal(arg_closeadj, arg_volume) -> pd.Series:
    """44,44-day jerk of 44-day VP confirmation."""
    res = _roc(_roc(_vp_conf(_roc(arg_closeadj, 44), _roc(arg_volume, 44)), 44), 44)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_conf_p22_v22_sma22_jerk_22_22_v005_signal(arg_closeadj, arg_volume) -> pd.Series:
    """22,22-day jerk of SMA22 of 22-day VP confirmation."""
    res = _roc(_roc(_sma(_vp_conf(_roc(arg_closeadj, 22), _roc(arg_volume, 22)), 22), 22), 22)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_conf_p22_v22_ema22_jerk_22_22_v006_signal(arg_closeadj, arg_volume) -> pd.Series:
    """22,22-day jerk of EMA22 of 22-day VP confirmation."""
    res = _roc(_roc(_ema(_vp_conf(_roc(arg_closeadj, 22), _roc(arg_volume, 22)), 22), 22), 22)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_conf_p22_v22_z252_jerk_22_22_v007_signal(arg_closeadj, arg_volume) -> pd.Series:
    """22,22-day jerk of Z252 of 22-day VP confirmation."""
    res = _roc(_roc(_z(_vp_conf(_roc(arg_closeadj, 22), _roc(arg_volume, 22)), 252), 22), 22)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_conf_p22_v22_cumsum_jerk_22_22_v008_signal(arg_closeadj, arg_volume) -> pd.Series:
    """22,22-day jerk of cumulative 22-day VP confirmation."""
    res = _roc(_roc(_vp_conf(_roc(arg_closeadj, 22), _roc(arg_volume, 22)).cumsum(), 22), 22)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_conf_p22_v22_jerk_5_5_v009_signal(arg_closeadj, arg_volume) -> pd.Series:
    """5,5-day jerk of 22-day VP confirmation."""
    res = _roc(_roc(_vp_conf(_roc(arg_closeadj, 22), _roc(arg_volume, 22)), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_conf_p22_v22_jerk_10_10_v010_signal(arg_closeadj, arg_volume) -> pd.Series:
    """10,10-day jerk of 22-day VP confirmation."""
    res = _roc(_roc(_vp_conf(_roc(arg_closeadj, 22), _roc(arg_volume, 22)), 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_conf_p22_v22_jerk_21_21_v011_signal(arg_closeadj, arg_volume) -> pd.Series:
    """21,21-day jerk of 22-day VP confirmation."""
    res = _roc(_roc(_vp_conf(_roc(arg_closeadj, 22), _roc(arg_volume, 22)), 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_conf_p22_v22_jerk_42_42_v012_signal(arg_closeadj, arg_volume) -> pd.Series:
    """42,42-day jerk of 22-day VP confirmation."""
    res = _roc(_roc(_vp_conf(_roc(arg_closeadj, 22), _roc(arg_volume, 22)), 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_conf_p22_v22_jerk_84_84_v013_signal(arg_closeadj, arg_volume) -> pd.Series:
    """84,84-day jerk of 22-day VP confirmation."""
    res = _roc(_roc(_vp_conf(_roc(arg_closeadj, 22), _roc(arg_volume, 22)), 84), 84)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_conf_p22_v22_jerk_168_168_v014_signal(arg_closeadj, arg_volume) -> pd.Series:
    """168,168-day jerk of 22-day VP confirmation."""
    res = _roc(_roc(_vp_conf(_roc(arg_closeadj, 22), _roc(arg_volume, 22)), 168), 168)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_conf_p22_v22_jerk_336_336_v015_signal(arg_closeadj, arg_volume) -> pd.Series:
    """336,336-day jerk of 22-day VP confirmation."""
    res = _roc(_roc(_vp_conf(_roc(arg_closeadj, 22), _roc(arg_volume, 22)), 336), 336)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_conf_p22_v22_jerk_504_504_v016_signal(arg_closeadj, arg_volume) -> pd.Series:
    """504,504-day jerk of 22-day VP confirmation."""
    res = _roc(_roc(_vp_conf(_roc(arg_closeadj, 22), _roc(arg_volume, 22)), 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_conf_p22_v22_jerk_756_756_v017_signal(arg_closeadj, arg_volume) -> pd.Series:
    """756,756-day jerk of 22-day VP confirmation."""
    res = _roc(_roc(_vp_conf(_roc(arg_closeadj, 22), _roc(arg_volume, 22)), 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_conf_p22_v22_jerk_1008_1008_v018_signal(arg_closeadj, arg_volume) -> pd.Series:
    """1008,1008-day jerk of 22-day VP confirmation."""
    res = _roc(_roc(_vp_conf(_roc(arg_closeadj, 22), _roc(arg_volume, 22)), 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_conf_p22_v22_jerk_1260_1260_v019_signal(arg_closeadj, arg_volume) -> pd.Series:
    """1260,1260-day jerk of 22-day VP confirmation."""
    res = _roc(_roc(_vp_conf(_roc(arg_closeadj, 22), _roc(arg_volume, 22)), 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_conf_p22_v22_sma252_jerk_22_22_v020_signal(arg_closeadj, arg_volume) -> pd.Series:
    """22,22-day jerk of SMA252 of 22-day VP confirmation."""
    res = _roc(_roc(_sma(_vp_conf(_roc(arg_closeadj, 22), _roc(arg_volume, 22)), 252), 22), 22)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_conf_p63_v63_jerk_22_22_v021_signal(arg_closeadj, arg_volume) -> pd.Series:
    """22,22-day jerk of 63-day VP confirmation."""
    res = _roc(_roc(_vp_conf(_roc(arg_closeadj, 63), _roc(arg_volume, 63)), 22), 22)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_conf_p63_v63_jerk_63_63_v022_signal(arg_closeadj, arg_volume) -> pd.Series:
    """63,63-day jerk of 63-day VP confirmation."""
    res = _roc(_roc(_vp_conf(_roc(arg_closeadj, 63), _roc(arg_volume, 63)), 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_conf_p126_v126_jerk_63_63_v023_signal(arg_closeadj, arg_volume) -> pd.Series:
    """63,63-day jerk of 126-day VP confirmation."""
    res = _roc(_roc(_vp_conf(_roc(arg_closeadj, 126), _roc(arg_volume, 126)), 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_conf_p252_v252_jerk_63_63_v024_signal(arg_closeadj, arg_volume) -> pd.Series:
    """63,63-day jerk of 252-day VP confirmation."""
    res = _roc(_roc(_vp_conf(_roc(arg_closeadj, 252), _roc(arg_volume, 252)), 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_conf_p22_v22_jerk_22_63_v025_signal(arg_closeadj, arg_volume) -> pd.Series:
    """22,63-day jerk of 22-day VP confirmation."""
    res = _roc(_roc(_vp_conf(_roc(arg_closeadj, 22), _roc(arg_volume, 22)), 22), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_conf_p22_v22_jerk_63_126_v026_signal(arg_closeadj, arg_volume) -> pd.Series:
    """63,126-day jerk of 22-day VP confirmation."""
    res = _roc(_roc(_vp_conf(_roc(arg_closeadj, 22), _roc(arg_volume, 22)), 63), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_conf_p22_v22_jerk_126_252_v027_signal(arg_closeadj, arg_volume) -> pd.Series:
    """126,252-day jerk of 22-day VP confirmation."""
    res = _roc(_roc(_vp_conf(_roc(arg_closeadj, 22), _roc(arg_volume, 22)), 126), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_conf_p22_v22_sma126_jerk_22_22_v028_signal(arg_closeadj, arg_volume) -> pd.Series:
    """22,22-day jerk of SMA126 of 22-day VP confirmation."""
    res = _roc(_roc(_sma(_vp_conf(_roc(arg_closeadj, 22), _roc(arg_volume, 22)), 126), 22), 22)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_conf_p22_v22_ema126_jerk_22_22_v029_signal(arg_closeadj, arg_volume) -> pd.Series:
    """22,22-day jerk of EMA126 of 22-day VP confirmation."""
    res = _roc(_roc(_ema(_vp_conf(_roc(arg_closeadj, 22), _roc(arg_volume, 22)), 126), 22), 22)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_conf_p22_v22_z126_jerk_22_22_v030_signal(arg_closeadj, arg_volume) -> pd.Series:
    """22,22-day jerk of Z126 of 22-day VP confirmation."""
    res = _roc(_roc(_z(_vp_conf(_roc(arg_closeadj, 22), _roc(arg_volume, 22)), 126), 22), 22)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_conf_p22_v22_jerk_5_10_v031_signal(arg_closeadj, arg_volume) -> pd.Series:
    """5,10-day jerk of 22-day VP confirmation."""
    res = _roc(_roc(_vp_conf(_roc(arg_closeadj, 22), _roc(arg_volume, 22)), 5), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_conf_p22_v22_jerk_10_22_v032_signal(arg_closeadj, arg_volume) -> pd.Series:
    """10,22-day jerk of 22-day VP confirmation."""
    res = _roc(_roc(_vp_conf(_roc(arg_closeadj, 22), _roc(arg_volume, 22)), 10), 22)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_conf_p22_v22_jerk_21_42_v033_signal(arg_closeadj, arg_volume) -> pd.Series:
    """21,42-day jerk of 22-day VP confirmation."""
    res = _roc(_roc(_vp_conf(_roc(arg_closeadj, 22), _roc(arg_volume, 22)), 21), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_conf_p22_v22_jerk_42_84_v034_signal(arg_closeadj, arg_volume) -> pd.Series:
    """42,84-day jerk of 22-day VP confirmation."""
    res = _roc(_roc(_vp_conf(_roc(arg_closeadj, 22), _roc(arg_volume, 22)), 42), 84)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_conf_p22_v22_jerk_84_168_v035_signal(arg_closeadj, arg_volume) -> pd.Series:
    """84,168-day jerk of 22-day VP confirmation."""
    res = _roc(_roc(_vp_conf(_roc(arg_closeadj, 22), _roc(arg_volume, 22)), 84), 168)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_conf_p22_v22_jerk_168_336_v036_signal(arg_closeadj, arg_volume) -> pd.Series:
    """168,336-day jerk of 22-day VP confirmation."""
    res = _roc(_roc(_vp_conf(_roc(arg_closeadj, 22), _roc(arg_volume, 22)), 168), 336)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_conf_p22_v22_jerk_336_504_v037_signal(arg_closeadj, arg_volume) -> pd.Series:
    """336,504-day jerk of 22-day VP confirmation."""
    res = _roc(_roc(_vp_conf(_roc(arg_closeadj, 22), _roc(arg_volume, 22)), 336), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_conf_p22_v22_jerk_504_756_v038_signal(arg_closeadj, arg_volume) -> pd.Series:
    """504,756-day jerk of 22-day VP confirmation."""
    res = _roc(_roc(_vp_conf(_roc(arg_closeadj, 22), _roc(arg_volume, 22)), 504), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_conf_p22_v22_jerk_756_1008_v039_signal(arg_closeadj, arg_volume) -> pd.Series:
    """756,1008-day jerk of 22-day VP confirmation."""
    res = _roc(_roc(_vp_conf(_roc(arg_closeadj, 22), _roc(arg_volume, 22)), 756), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_conf_p22_v22_jerk_1008_1260_v040_signal(arg_closeadj, arg_volume) -> pd.Series:
    """1008,1260-day jerk of 22-day VP confirmation."""
    res = _roc(_roc(_vp_conf(_roc(arg_closeadj, 22), _roc(arg_volume, 22)), 1008), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_conf_p22_v22_weighted_jerk_22_22_v041_signal(arg_closeadj, arg_volume) -> pd.Series:
    """22,22-day jerk of volume-weighted 22-day price ROC."""
    p_roc = _roc(arg_closeadj, 22)
    weighted_roc = (p_roc * arg_volume).rolling(22).sum() / arg_volume.rolling(22).sum().replace(0, np.nan)
    res = _roc(_roc(weighted_roc, 22), 22)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_conf_p22_v22_rel_sma252_jerk_22_22_v042_signal(arg_closeadj, arg_volume) -> pd.Series:
    """22,22-day jerk of (conf / SMA252)."""
    conf = _vp_conf(_roc(arg_closeadj, 22), _roc(arg_volume, 22))
    res = _roc(_roc(conf / _sma(conf, 252).replace(0, np.nan), 22), 22)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_conf_p22_v22_max_252_jerk_22_22_v043_signal(arg_closeadj, arg_volume) -> pd.Series:
    """22,22-day jerk of 252-day max of 22-day VP confirmation."""
    res = _roc(_roc(_vp_conf(_roc(arg_closeadj, 22), _roc(arg_volume, 22)).rolling(252).max(), 22), 22)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_conf_p22_v22_min_252_jerk_22_22_v044_signal(arg_closeadj, arg_volume) -> pd.Series:
    """22,22-day jerk of 252-day min of 22-day VP confirmation."""
    res = _roc(_roc(_vp_conf(_roc(arg_closeadj, 22), _roc(arg_volume, 22)).rolling(252).min(), 22), 22)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_conf_p22_v22_rank_252_jerk_22_22_v045_signal(arg_closeadj, arg_volume) -> pd.Series:
    """22,22-day jerk of 252-day rank of 22-day VP confirmation."""
    res = _roc(_roc(_vp_conf(_roc(arg_closeadj, 22), _roc(arg_volume, 22)).rolling(252).rank(pct=True), 22), 22)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_conf_p22_v22_sma504_jerk_22_22_v046_signal(arg_closeadj, arg_volume) -> pd.Series:
    """22,22-day jerk of SMA504 of 22-day VP confirmation."""
    res = _roc(_roc(_sma(_vp_conf(_roc(arg_closeadj, 22), _roc(arg_volume, 22)), 504), 22), 22)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_conf_p22_v22_ema504_jerk_22_22_v047_signal(arg_closeadj, arg_volume) -> pd.Series:
    """22,22-day jerk of EMA504 of 22-day VP confirmation."""
    res = _roc(_roc(_ema(_vp_conf(_roc(arg_closeadj, 22), _roc(arg_volume, 22)), 504), 22), 22)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_conf_p22_v22_z504_jerk_22_22_v048_signal(arg_closeadj, arg_volume) -> pd.Series:
    """22,22-day jerk of Z504 of 22-day VP confirmation."""
    res = _roc(_roc(_z(_vp_conf(_roc(arg_closeadj, 22), _roc(arg_volume, 22)), 504), 22), 22)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_conf_p22_v22_z1260_jerk_22_22_v049_signal(arg_closeadj, arg_volume) -> pd.Series:
    """22,22-day jerk of Z1260 of 22-day VP confirmation."""
    res = _roc(_roc(_z(_vp_conf(_roc(arg_closeadj, 22), _roc(arg_volume, 22)), 1260), 22), 22)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_conf_p22_v22_sma1260_jerk_22_22_v050_signal(arg_closeadj, arg_volume) -> pd.Series:
    """22,22-day jerk of SMA1260 of 22-day VP confirmation."""
    res = _roc(_roc(_sma(_vp_conf(_roc(arg_closeadj, 22), _roc(arg_volume, 22)), 1260), 22), 22)
    return res.replace([np.inf, -np.inf], np.nan)

# 051-100: Jerks of VP Correlation
def f24vpc_f24_volume_price_confirmation_vp_corr_w22_jerk_22_22_v051_signal(arg_closeadj, arg_volume) -> pd.Series:
    """22,22-day jerk of 22-day price-volume correlation."""
    res = _roc(_roc(_vp_corr(arg_closeadj, arg_volume, 22), 22), 22)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_corr_w22_jerk_63_22_v052_signal(arg_closeadj, arg_volume) -> pd.Series:
    """63,22-day jerk of 22-day price-volume correlation."""
    res = _roc(_roc(_vp_corr(arg_closeadj, arg_volume, 22), 63), 22)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_corr_w63_jerk_22_22_v053_signal(arg_closeadj, arg_volume) -> pd.Series:
    """22,22-day jerk of 63-day price-volume correlation."""
    res = _roc(_roc(_vp_corr(arg_closeadj, arg_volume, 63), 22), 22)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_corr_w63_jerk_63_63_v054_signal(arg_closeadj, arg_volume) -> pd.Series:
    """63,63-day jerk of 63-day price-volume correlation."""
    res = _roc(_roc(_vp_corr(arg_closeadj, arg_volume, 63), 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_corr_w126_jerk_126_126_v055_signal(arg_closeadj, arg_volume) -> pd.Series:
    """126,126-day jerk of 126-day price-volume correlation."""
    res = _roc(_roc(_vp_corr(arg_closeadj, arg_volume, 126), 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_corr_w252_jerk_252_252_v056_signal(arg_closeadj, arg_volume) -> pd.Series:
    """252,252-day jerk of 252-day price-volume correlation."""
    res = _roc(_roc(_vp_corr(arg_closeadj, arg_volume, 252), 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_corr_roc22_w22_jerk_22_22_v057_signal(arg_closeadj, arg_volume) -> pd.Series:
    """22,22-day jerk of 22-day correlation between price ROC and volume ROC."""
    res = _roc(_roc(_vp_corr(_roc(arg_closeadj, 22), _roc(arg_volume, 22), 22), 22), 22)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_corr_sma22_w63_jerk_22_22_v058_signal(arg_closeadj, arg_volume) -> pd.Series:
    """22,22-day jerk of 63-day correlation between price SMA and volume SMA."""
    res = _roc(_roc(_vp_corr(_sma(arg_closeadj, 22), _sma(arg_volume, 22), 63), 22), 22)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_corr_z252_w22_jerk_22_22_v059_signal(arg_closeadj, arg_volume) -> pd.Series:
    """22,22-day jerk of Z252 of 22-day price-volume correlation."""
    res = _roc(_roc(_z(_vp_corr(arg_closeadj, arg_volume, 22), 252), 22), 22)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_corr_cumsum_w22_jerk_22_22_v060_signal(arg_closeadj, arg_volume) -> pd.Series:
    """22,22-day jerk of cumulative 22-day price-volume correlation."""
    res = _roc(_roc(_vp_corr(arg_closeadj, arg_volume, 22).cumsum(), 22), 22)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_corr_w22_jerk_5_5_v061_signal(arg_closeadj, arg_volume) -> pd.Series:
    """5,5-day jerk of 22-day price-volume correlation."""
    res = _roc(_roc(_vp_corr(arg_closeadj, arg_volume, 22), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_corr_w22_jerk_10_10_v062_signal(arg_closeadj, arg_volume) -> pd.Series:
    """10,10-day jerk of 22-day price-volume correlation."""
    res = _roc(_roc(_vp_corr(arg_closeadj, arg_volume, 22), 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_corr_w22_jerk_21_21_v063_signal(arg_closeadj, arg_volume) -> pd.Series:
    """21,21-day jerk of 22-day price-volume correlation."""
    res = _roc(_roc(_vp_corr(arg_closeadj, arg_volume, 22), 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_corr_w22_jerk_42_42_v064_signal(arg_closeadj, arg_volume) -> pd.Series:
    """42,42-day jerk of 22-day price-volume correlation."""
    res = _roc(_roc(_vp_corr(arg_closeadj, arg_volume, 22), 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_corr_w22_jerk_84_84_v065_signal(arg_closeadj, arg_volume) -> pd.Series:
    """84,84-day jerk of 22-day price-volume correlation."""
    res = _roc(_roc(_vp_corr(arg_closeadj, arg_volume, 22), 84), 84)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_corr_w22_jerk_168_168_v066_signal(arg_closeadj, arg_volume) -> pd.Series:
    """168,168-day jerk of 22-day price-volume correlation."""
    res = _roc(_roc(_vp_corr(arg_closeadj, arg_volume, 22), 168), 168)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_corr_w22_jerk_336_336_v067_signal(arg_closeadj, arg_volume) -> pd.Series:
    """336,336-day jerk of 22-day price-volume correlation."""
    res = _roc(_roc(_vp_corr(arg_closeadj, arg_volume, 22), 336), 336)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_corr_w22_jerk_504_504_v068_signal(arg_closeadj, arg_volume) -> pd.Series:
    """504,504-day jerk of 22-day price-volume correlation."""
    res = _roc(_roc(_vp_corr(arg_closeadj, arg_volume, 22), 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_corr_w22_jerk_756_756_v069_signal(arg_closeadj, arg_volume) -> pd.Series:
    """756,756-day jerk of 22-day price-volume correlation."""
    res = _roc(_roc(_vp_corr(arg_closeadj, arg_volume, 22), 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_corr_w22_jerk_1008_1008_v070_signal(arg_closeadj, arg_volume) -> pd.Series:
    """1008,1008-day jerk of 22-day price-volume correlation."""
    res = _roc(_roc(_vp_corr(arg_closeadj, arg_volume, 22), 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_corr_w22_jerk_1260_1260_v071_signal(arg_closeadj, arg_volume) -> pd.Series:
    """1260,1260-day jerk of 22-day price-volume correlation."""
    res = _roc(_roc(_vp_corr(arg_closeadj, arg_volume, 22), 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_corr_sma22_jerk_22_22_v072_signal(arg_closeadj, arg_volume) -> pd.Series:
    """22,22-day jerk of SMA22 of 22-day price-volume correlation."""
    res = _roc(_roc(_sma(_vp_corr(arg_closeadj, arg_volume, 22), 22), 22), 22)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_corr_ema22_jerk_22_22_v073_signal(arg_closeadj, arg_volume) -> pd.Series:
    """22,22-day jerk of EMA22 of 22-day price-volume correlation."""
    res = _roc(_roc(_ema(_vp_corr(arg_closeadj, arg_volume, 22), 22), 22), 22)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_corr_z63_w22_jerk_22_22_v074_signal(arg_closeadj, arg_volume) -> pd.Series:
    """22,22-day jerk of Z63 of 22-day price-volume correlation."""
    res = _roc(_roc(_z(_vp_corr(arg_closeadj, arg_volume, 22), 63), 22), 22)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_corr_z126_w22_jerk_22_22_v075_signal(arg_closeadj, arg_volume) -> pd.Series:
    """22,22-day jerk of Z126 of 22-day price-volume correlation."""
    res = _roc(_roc(_z(_vp_corr(arg_closeadj, arg_volume, 22), 126), 22), 22)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_corr_z504_w22_jerk_22_22_v076_signal(arg_closeadj, arg_volume) -> pd.Series:
    """22,22-day jerk of Z504 of 22-day price-volume correlation."""
    res = _roc(_roc(_z(_vp_corr(arg_closeadj, arg_volume, 22), 504), 22), 22)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_corr_z1260_w22_jerk_22_22_v077_signal(arg_closeadj, arg_volume) -> pd.Series:
    """22,22-day jerk of Z1260 of 22-day price-volume correlation."""
    res = _roc(_roc(_z(_vp_corr(arg_closeadj, arg_volume, 22), 1260), 22), 22)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_corr_sma126_w22_jerk_22_22_v078_signal(arg_closeadj, arg_volume) -> pd.Series:
    """22,22-day jerk of SMA126 of 22-day price-volume correlation."""
    res = _roc(_roc(_sma(_vp_corr(arg_closeadj, arg_volume, 22), 126), 22), 22)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_corr_sma252_w22_jerk_22_22_v079_signal(arg_closeadj, arg_volume) -> pd.Series:
    """22,22-day jerk of SMA252 of 22-day price-volume correlation."""
    res = _roc(_roc(_sma(_vp_corr(arg_closeadj, arg_volume, 22), 252), 22), 22)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_corr_ema252_w22_jerk_22_22_v080_signal(arg_closeadj, arg_volume) -> pd.Series:
    """22,22-day jerk of EMA252 of 22-day price-volume correlation."""
    res = _roc(_roc(_ema(_vp_corr(arg_closeadj, arg_volume, 22), 252), 22), 22)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_corr_max_252_w22_jerk_22_22_v081_signal(arg_closeadj, arg_volume) -> pd.Series:
    """22,22-day jerk of 252-day max of 22-day price-volume correlation."""
    res = _roc(_roc(_vp_corr(arg_closeadj, arg_volume, 22).rolling(252).max(), 22), 22)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_corr_min_252_w22_jerk_22_22_v082_signal(arg_closeadj, arg_volume) -> pd.Series:
    """22,22-day jerk of 252-day min of 22-day price-volume correlation."""
    res = _roc(_roc(_vp_corr(arg_closeadj, arg_volume, 22).rolling(252).min(), 22), 22)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_corr_rank_252_w22_jerk_22_22_v083_signal(arg_closeadj, arg_volume) -> pd.Series:
    """22,22-day jerk of 252-day rank of 22-day price-volume correlation."""
    res = _roc(_roc(_vp_corr(arg_closeadj, arg_volume, 22).rolling(252).rank(pct=True), 22), 22)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_corr_sma22_jerk_63_63_v084_signal(arg_closeadj, arg_volume) -> pd.Series:
    """63,63-day jerk of SMA22 of 22-day price-volume correlation."""
    res = _roc(_roc(_sma(_vp_corr(arg_closeadj, arg_volume, 22), 22), 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_corr_ema22_jerk_63_63_v085_signal(arg_closeadj, arg_volume) -> pd.Series:
    """63,63-day jerk of EMA22 of 22-day price-volume correlation."""
    res = _roc(_roc(_ema(_vp_corr(arg_closeadj, arg_volume, 22), 22), 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_corr_w63_jerk_22_63_v086_signal(arg_closeadj, arg_volume) -> pd.Series:
    """22,63-day jerk of 63-day price-volume correlation."""
    res = _roc(_roc(_vp_corr(arg_closeadj, arg_volume, 63), 22), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_corr_w63_jerk_63_126_v087_signal(arg_closeadj, arg_volume) -> pd.Series:
    """63,126-day jerk of 63-day price-volume correlation."""
    res = _roc(_roc(_vp_corr(arg_closeadj, arg_volume, 63), 63), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_corr_w126_jerk_63_126_v088_signal(arg_closeadj, arg_volume) -> pd.Series:
    """63,126-day jerk of 126-day price-volume correlation."""
    res = _roc(_roc(_vp_corr(arg_closeadj, arg_volume, 126), 63), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_corr_w252_jerk_63_126_v089_signal(arg_closeadj, arg_volume) -> pd.Series:
    """63,126-day jerk of 252-day price-volume correlation."""
    res = _roc(_roc(_vp_corr(arg_closeadj, arg_volume, 252), 63), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_corr_sma504_w22_jerk_22_22_v090_signal(arg_closeadj, arg_volume) -> pd.Series:
    """22,22-day jerk of SMA504 of 22-day price-volume correlation."""
    res = _roc(_roc(_sma(_vp_corr(arg_closeadj, arg_volume, 22), 504), 22), 22)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_corr_ema504_w22_jerk_22_22_v091_signal(arg_closeadj, arg_volume) -> pd.Series:
    """22,22-day jerk of EMA504 of 22-day price-volume correlation."""
    res = _roc(_roc(_ema(_vp_corr(arg_closeadj, arg_volume, 22), 504), 22), 22)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_corr_log_vol_w22_jerk_22_22_v092_signal(arg_closeadj, arg_volume) -> pd.Series:
    """22,22-day jerk of 22-day correlation between price and log volume."""
    res = _roc(_roc(_vp_corr(arg_closeadj, np.log1p(arg_volume), 22), 22), 22)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_corr_log_vol_w63_jerk_22_22_v093_signal(arg_closeadj, arg_volume) -> pd.Series:
    """22,22-day jerk of 63-day correlation between price and log volume."""
    res = _roc(_roc(_vp_corr(arg_closeadj, np.log1p(arg_volume), 63), 22), 22)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_corr_log_vol_w252_jerk_22_22_v094_signal(arg_closeadj, arg_volume) -> pd.Series:
    """22,22-day jerk of 252-day correlation between price and log volume."""
    res = _roc(_roc(_vp_corr(arg_closeadj, np.log1p(arg_volume), 252), 22), 22)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_corr_sma22_w252_jerk_22_22_v095_signal(arg_closeadj, arg_volume) -> pd.Series:
    """22,22-day jerk of 252-day correlation between 22-day price SMA and 22-day volume SMA."""
    res = _roc(_roc(_vp_corr(_sma(arg_closeadj, 22), _sma(arg_volume, 22), 252), 22), 22)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_corr_ema22_w252_jerk_22_22_v096_signal(arg_closeadj, arg_volume) -> pd.Series:
    """22,22-day jerk of 252-day correlation between 22-day price EMA and 22-day volume EMA."""
    res = _roc(_roc(_vp_corr(_ema(arg_closeadj, 22), _ema(arg_volume, 22), 252), 22), 22)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_corr_z252_w63_jerk_22_22_v097_signal(arg_closeadj, arg_volume) -> pd.Series:
    """22,22-day jerk of Z252 of 63-day price-volume correlation."""
    res = _roc(_roc(_z(_vp_corr(arg_closeadj, arg_volume, 63), 252), 22), 22)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_corr_z504_w126_jerk_22_22_v098_signal(arg_closeadj, arg_volume) -> pd.Series:
    """22,22-day jerk of Z504 of 126-day price-volume correlation."""
    res = _roc(_roc(_z(_vp_corr(arg_closeadj, arg_volume, 126), 504), 22), 22)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_corr_rel_sma252_w22_jerk_22_22_v099_signal(arg_closeadj, arg_volume) -> pd.Series:
    """22,22-day jerk of (corr / SMA252)."""
    corr = _vp_corr(arg_closeadj, arg_volume, 22)
    res = _roc(_roc(corr / _sma(corr, 252).replace(0, np.nan), 22), 22)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_corr_rel_sma1260_w22_jerk_22_22_v100_signal(arg_closeadj, arg_volume) -> pd.Series:
    """22,22-day jerk of (corr / SMA1260)."""
    corr = _vp_corr(arg_closeadj, arg_volume, 22)
    res = _roc(_roc(corr / _sma(corr, 1260).replace(0, np.nan), 22), 22)
    return res.replace([np.inf, -np.inf], np.nan)

# 101-150: Jerks of VP Trend Strength
def f24vpc_f24_volume_price_confirmation_vp_trend_strength_w22_jerk_22_22_v101_signal(arg_closeadj, arg_volume) -> pd.Series:
    """22,22-day jerk of 22-day VP trend strength."""
    res = _roc(_roc(_vp_trend_strength(arg_closeadj, arg_volume, 22), 22), 22)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_trend_strength_w22_jerk_63_22_v102_signal(arg_closeadj, arg_volume) -> pd.Series:
    """63,22-day jerk of 22-day VP trend strength."""
    res = _roc(_roc(_vp_trend_strength(arg_closeadj, arg_volume, 22), 63), 22)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_trend_strength_w63_jerk_22_22_v103_signal(arg_closeadj, arg_volume) -> pd.Series:
    """22,22-day jerk of 63-day VP trend strength."""
    res = _roc(_roc(_vp_trend_strength(arg_closeadj, arg_volume, 63), 22), 22)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_trend_strength_w63_jerk_63_63_v104_signal(arg_closeadj, arg_volume) -> pd.Series:
    """63,63-day jerk of 63-day VP trend strength."""
    res = _roc(_roc(_vp_trend_strength(arg_closeadj, arg_volume, 63), 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_trend_strength_w126_jerk_126_126_v105_signal(arg_closeadj, arg_volume) -> pd.Series:
    """126,126-day jerk of 126-day VP trend strength."""
    res = _roc(_roc(_vp_trend_strength(arg_closeadj, arg_volume, 126), 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_trend_strength_w252_jerk_252_252_v106_signal(arg_closeadj, arg_volume) -> pd.Series:
    """252,252-day jerk of 252-day VP trend strength."""
    res = _roc(_roc(_vp_trend_strength(arg_closeadj, arg_volume, 252), 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_trend_strength_ema22_jerk_22_22_v107_signal(arg_closeadj, arg_volume) -> pd.Series:
    """22,22-day jerk of EMA22 of 22-day VP trend strength."""
    res = _roc(_roc(_ema(_vp_trend_strength(arg_closeadj, arg_volume, 22), 22), 22), 22)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_trend_strength_sma63_jerk_22_22_v108_signal(arg_closeadj, arg_volume) -> pd.Series:
    """22,22-day jerk of SMA63 of 63-day VP trend strength."""
    res = _roc(_roc(_sma(_vp_trend_strength(arg_closeadj, arg_volume, 63), 63), 22), 22)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_trend_strength_z252_jerk_22_22_v109_signal(arg_closeadj, arg_volume) -> pd.Series:
    """22,22-day jerk of Z252 of 252-day VP trend strength."""
    res = _roc(_roc(_z(_vp_trend_strength(arg_closeadj, arg_volume, 252), 252), 22), 22)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_trend_strength_cumsum_jerk_22_22_v110_signal(arg_closeadj, arg_volume) -> pd.Series:
    """22,22-day jerk of cumulative 22-day VP trend strength."""
    res = _roc(_roc(_vp_trend_strength(arg_closeadj, arg_volume, 22).cumsum(), 22), 22)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_trend_strength_w22_jerk_5_5_v111_signal(arg_closeadj, arg_volume) -> pd.Series:
    """5,5-day jerk of 22-day VP trend strength."""
    res = _roc(_roc(_vp_trend_strength(arg_closeadj, arg_volume, 22), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_trend_strength_w22_jerk_10_10_v112_signal(arg_closeadj, arg_volume) -> pd.Series:
    """10,10-day jerk of 22-day VP trend strength."""
    res = _roc(_roc(_vp_trend_strength(arg_closeadj, arg_volume, 22), 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_trend_strength_w22_jerk_21_21_v113_signal(arg_closeadj, arg_volume) -> pd.Series:
    """21,21-day jerk of 22-day VP trend strength."""
    res = _roc(_roc(_vp_trend_strength(arg_closeadj, arg_volume, 22), 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_trend_strength_w22_jerk_42_42_v114_signal(arg_closeadj, arg_volume) -> pd.Series:
    """42,42-day jerk of 22-day VP trend strength."""
    res = _roc(_roc(_vp_trend_strength(arg_closeadj, arg_volume, 22), 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_trend_strength_w22_jerk_84_84_v115_signal(arg_closeadj, arg_volume) -> pd.Series:
    """84,84-day jerk of 22-day VP trend strength."""
    res = _roc(_roc(_vp_trend_strength(arg_closeadj, arg_volume, 22), 84), 84)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_trend_strength_w22_jerk_168_168_v116_signal(arg_closeadj, arg_volume) -> pd.Series:
    """168,168-day jerk of 22-day VP trend strength."""
    res = _roc(_roc(_vp_trend_strength(arg_closeadj, arg_volume, 22), 168), 168)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_trend_strength_w22_jerk_336_336_v117_signal(arg_closeadj, arg_volume) -> pd.Series:
    """336,336-day jerk of 22-day VP trend strength."""
    res = _roc(_roc(_vp_trend_strength(arg_closeadj, arg_volume, 22), 336), 336)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_trend_strength_w22_jerk_504_504_v118_signal(arg_closeadj, arg_volume) -> pd.Series:
    """504,504-day jerk of 22-day VP trend strength."""
    res = _roc(_roc(_vp_trend_strength(arg_closeadj, arg_volume, 22), 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_trend_strength_w22_jerk_756_756_v119_signal(arg_closeadj, arg_volume) -> pd.Series:
    """756,756-day jerk of 22-day VP trend strength."""
    res = _roc(_roc(_vp_trend_strength(arg_closeadj, arg_volume, 22), 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_trend_strength_w22_jerk_1008_1008_v120_signal(arg_closeadj, arg_volume) -> pd.Series:
    """1008,1008-day jerk of 22-day VP trend strength."""
    res = _roc(_roc(_vp_trend_strength(arg_closeadj, arg_volume, 22), 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_trend_strength_w22_jerk_1260_1260_v121_signal(arg_closeadj, arg_volume) -> pd.Series:
    """1260,1260-day jerk of 22-day VP trend strength."""
    res = _roc(_roc(_vp_trend_strength(arg_closeadj, arg_volume, 22), 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_trend_strength_sma126_jerk_22_22_v122_signal(arg_closeadj, arg_volume) -> pd.Series:
    """22,22-day jerk of SMA126 of 22-day VP trend strength."""
    res = _roc(_roc(_sma(_vp_trend_strength(arg_closeadj, arg_volume, 22), 126), 22), 22)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_trend_strength_ema126_jerk_22_22_v123_signal(arg_closeadj, arg_volume) -> pd.Series:
    """22,22-day jerk of EMA126 of 22-day VP trend strength."""
    res = _roc(_roc(_ema(_vp_trend_strength(arg_closeadj, arg_volume, 22), 126), 22), 22)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_trend_strength_z126_jerk_22_22_v124_signal(arg_closeadj, arg_volume) -> pd.Series:
    """22,22-day jerk of Z126 of 22-day VP trend strength."""
    res = _roc(_roc(_z(_vp_trend_strength(arg_closeadj, arg_volume, 22), 126), 22), 22)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_trend_strength_z252_jerk_63_63_v125_signal(arg_closeadj, arg_volume) -> pd.Series:
    """63,63-day jerk of Z252 of 22-day VP trend strength."""
    res = _roc(_roc(_z(_vp_trend_strength(arg_closeadj, arg_volume, 22), 252), 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_trend_strength_rel_sma252_jerk_22_22_v126_signal(arg_closeadj, arg_volume) -> pd.Series:
    """22,22-day jerk of (trend_strength / SMA252)."""
    ts = _vp_trend_strength(arg_closeadj, arg_volume, 22)
    res = _roc(_roc(ts / _sma(ts, 252).replace(0, np.nan), 22), 22)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_trend_strength_mul_roc22_jerk_22_22_v127_signal(arg_closeadj, arg_volume) -> pd.Series:
    """22,22-day jerk of (trend_strength * price_roc22)."""
    res = _roc(_roc(_vp_trend_strength(arg_closeadj, arg_volume, 22) * _roc(arg_closeadj, 22), 22), 22)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_trend_strength_sma22_jerk_63_63_v128_signal(arg_closeadj, arg_volume) -> pd.Series:
    """63,63-day jerk of SMA22 of 22-day VP trend strength."""
    res = _roc(_roc(_sma(_vp_trend_strength(arg_closeadj, arg_volume, 22), 22), 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_trend_strength_ema22_jerk_63_63_v129_signal(arg_closeadj, arg_volume) -> pd.Series:
    """63,63-day jerk of EMA22 of 22-day VP trend strength."""
    res = _roc(_roc(_ema(_vp_trend_strength(arg_closeadj, arg_volume, 22), 22), 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_trend_strength_sma504_jerk_22_22_v130_signal(arg_closeadj, arg_volume) -> pd.Series:
    """22,22-day jerk of SMA504 of 22-day VP trend strength."""
    res = _roc(_roc(_sma(_vp_trend_strength(arg_closeadj, arg_volume, 22), 504), 22), 22)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_trend_strength_ema504_jerk_22_22_v131_signal(arg_closeadj, arg_volume) -> pd.Series:
    """22,22-day jerk of EMA504 of 22-day VP trend strength."""
    res = _roc(_roc(_ema(_vp_trend_strength(arg_closeadj, arg_volume, 22), 504), 22), 22)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_trend_strength_z504_jerk_22_22_v132_signal(arg_closeadj, arg_volume) -> pd.Series:
    """22,22-day jerk of Z504 of 22-day VP trend strength."""
    res = _roc(_roc(_z(_vp_trend_strength(arg_closeadj, arg_volume, 22), 504), 22), 22)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_trend_strength_z1260_jerk_22_22_v133_signal(arg_closeadj, arg_volume) -> pd.Series:
    """22,22-day jerk of Z1260 of 22-day VP trend strength."""
    res = _roc(_roc(_z(_vp_trend_strength(arg_closeadj, arg_volume, 22), 1260), 22), 22)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_trend_strength_sma1260_jerk_22_22_v134_signal(arg_closeadj, arg_volume) -> pd.Series:
    """22,22-day jerk of SMA1260 of 22-day VP trend strength."""
    res = _roc(_roc(_sma(_vp_trend_strength(arg_closeadj, arg_volume, 22), 1260), 22), 22)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_trend_strength_ema1260_jerk_22_22_v135_signal(arg_closeadj, arg_volume) -> pd.Series:
    """22,22-day jerk of EMA1260 of 22-day VP trend strength."""
    res = _roc(_roc(_ema(_vp_trend_strength(arg_closeadj, arg_volume, 22), 1260), 22), 22)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_trend_strength_w22_jerk_5_22_v136_signal(arg_closeadj, arg_volume) -> pd.Series:
    """5,22-day jerk of 22-day VP trend strength."""
    res = _roc(_roc(_vp_trend_strength(arg_closeadj, arg_volume, 22), 5), 22)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_trend_strength_w22_jerk_22_63_v137_signal(arg_closeadj, arg_volume) -> pd.Series:
    """22,63-day jerk of 22-day VP trend strength."""
    res = _roc(_roc(_vp_trend_strength(arg_closeadj, arg_volume, 22), 22), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_trend_strength_w22_jerk_63_126_v138_signal(arg_closeadj, arg_volume) -> pd.Series:
    """63,126-day jerk of 22-day VP trend strength."""
    res = _roc(_roc(_vp_trend_strength(arg_closeadj, arg_volume, 22), 63), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_trend_strength_w22_jerk_126_252_v139_signal(arg_closeadj, arg_volume) -> pd.Series:
    """126,252-day jerk of 22-day VP trend strength."""
    res = _roc(_roc(_vp_trend_strength(arg_closeadj, arg_volume, 22), 126), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_trend_strength_w63_jerk_22_63_v140_signal(arg_closeadj, arg_volume) -> pd.Series:
    """22,63-day jerk of 63-day VP trend strength."""
    res = _roc(_roc(_vp_trend_strength(arg_closeadj, arg_volume, 63), 22), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_trend_strength_w63_jerk_63_126_v141_signal(arg_closeadj, arg_volume) -> pd.Series:
    """63,126-day jerk of 63-day VP trend strength."""
    res = _roc(_roc(_vp_trend_strength(arg_closeadj, arg_volume, 63), 63), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_trend_strength_w126_jerk_63_126_v142_signal(arg_closeadj, arg_volume) -> pd.Series:
    """63,126-day jerk of 126-day VP trend strength."""
    res = _roc(_roc(_vp_trend_strength(arg_closeadj, arg_volume, 126), 63), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_trend_strength_w252_jerk_63_126_v143_signal(arg_closeadj, arg_volume) -> pd.Series:
    """63,126-day jerk of 252-day VP trend strength."""
    res = _roc(_roc(_vp_trend_strength(arg_closeadj, arg_volume, 252), 63), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_trend_strength_sma22_jerk_22_22_v144_signal(arg_closeadj, arg_volume) -> pd.Series:
    """22,22-day jerk of SMA22 of 22-day VP trend strength."""
    res = _roc(_roc(_sma(_vp_trend_strength(arg_closeadj, arg_volume, 22), 22), 22), 22)
    return res.replace([np.inf, -np.inf], np.nan)


def f24vpc_f24_volume_price_confirmation_vp_trend_strength_z63_w22_jerk_22_22_v146_signal(arg_closeadj, arg_volume) -> pd.Series:
    """22,22-day jerk of Z63 of 22-day VP trend strength."""
    res = _roc(_roc(_z(_vp_trend_strength(arg_closeadj, arg_volume, 22), 63), 22), 22)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_trend_strength_rel_sma252_jerk_63_63_v147_signal(arg_closeadj, arg_volume) -> pd.Series:
    """63,63-day jerk of (trend_strength / SMA252)."""
    ts = _vp_trend_strength(arg_closeadj, arg_volume, 22)
    res = _roc(_roc(ts / _sma(ts, 252).replace(0, np.nan), 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_trend_strength_mul_roc22_jerk_63_63_v148_signal(arg_closeadj, arg_volume) -> pd.Series:
    """63,63-day jerk of (trend_strength * price_roc22)."""
    res = _roc(_roc(_vp_trend_strength(arg_closeadj, arg_volume, 22) * _roc(arg_closeadj, 22), 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_trend_strength_z252_jerk_22_63_v149_signal(arg_closeadj, arg_volume) -> pd.Series:
    """22,63-day jerk of Z252 of 22-day VP trend strength."""
    res = _roc(_roc(_z(_vp_trend_strength(arg_closeadj, arg_volume, 22), 252), 22), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f24vpc_f24_volume_price_confirmation_vp_trend_strength_w22_jerk_252_252_v150_signal(arg_closeadj, arg_volume) -> pd.Series:
    """252,252-day jerk of 22-day VP trend strength."""
    res = _roc(_roc(_vp_trend_strength(arg_closeadj, arg_volume, 22), 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

# --- Registry and Self-Test ---

SILVERDB_ACCESS, SOURCE_TABLE, ENTITY_COLUMN, DATE_COLUMN = "read_only", "sep", "ticker", "date"
ORDER_BY, NO_FORWARD_LOOKING = [ENTITY_COLUMN, DATE_COLUMN], True
SOURCE_COLUMNS = {c: f"sep.{c.replace('arg_', '')}" for c in ["arg_closeadj", "arg_volume"]}

F24_VOLUME_PRICE_CONFIRMATION_JERK_REGISTRY_001_150 = {
    n: {
        "inputs": (inputs := [v for v in globals()[n].__code__.co_varnames[:globals()[n].__code__.co_argcount]]),
        "source_table": SOURCE_TABLE,
        "source_columns": {c: SOURCE_COLUMNS[c] for c in inputs if c in SOURCE_COLUMNS},
        "entity_column": ENTITY_COLUMN, "date_column": DATE_COLUMN,
        "order_by": ORDER_BY, "no_forward_looking": NO_FORWARD_LOOKING, "func": globals()[n]
    } for n in sorted([k for k in globals() if k.startswith('f24vpc_f24_volume_price_confirmation_') and k.endswith('_signal')])
}

if __name__ == "__main__":
    sz = 2000
    np.random.seed(42)
    d = pd.DataFrame({
        "arg_closeadj": pd.Series(np.exp(np.cumsum(np.random.normal(0.0001, 0.01, sz))) * 100),
        "arg_volume": pd.Series(np.random.lognormal(15, 1, sz)),
        "ticker": ["T"]*sz,
        "date": pd.date_range("2010-01-01", periods=sz)
    })
    for n, c in F24_VOLUME_PRICE_CONFIRMATION_JERK_REGISTRY_001_150.items():
        r = c["func"](**{i: d[i] for i in c["inputs"]})
        assert len(r) > 0, f"{n} failed len"
        assert r.nunique() > 2, f"{n} failed nunique: {r.nunique()}"
    print(f"OK")
