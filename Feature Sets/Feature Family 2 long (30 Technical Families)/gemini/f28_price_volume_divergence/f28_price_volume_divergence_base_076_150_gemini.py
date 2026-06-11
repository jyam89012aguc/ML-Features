# f28_price_volume_divergence_base_076_150_gemini.py
import pandas as pd
import numpy as np

def _sma(s, w): return s.rolling(w, min_periods=min(w, 5)).mean()
def _ema(s, w): return s.ewm(span=w, min_periods=min(w, 5), adjust=False).mean()
def _z(s, w): return (s - _sma(s, w)) / s.rolling(w, min_periods=min(w, 5)).std().replace(0, np.nan)

def _pv_div_val(p_roc, v_roc): return p_roc - v_roc
def _pv_conv_val(p_roc, v_roc): return p_roc * v_roc
def _pv_spread_z(p_z, v_z): return p_z - v_z

# Feature 76: f28pvd_f28_price_volume_divergence_pv_corr_63d
def f28pvd_f28_price_volume_divergence_pv_corr_63d_base_v076_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    p_roc = closeadj.pct_change(5)
    v_roc = volume.pct_change(5)
    res = p_roc.rolling(63).corr(v_roc)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 77: f28pvd_f28_price_volume_divergence_pv_corr_80d
def f28pvd_f28_price_volume_divergence_pv_corr_80d_base_v077_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    p_roc = closeadj.pct_change(5)
    v_roc = volume.pct_change(5)
    res = p_roc.rolling(80).corr(v_roc)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 78: f28pvd_f28_price_volume_divergence_pv_corr_100d
def f28pvd_f28_price_volume_divergence_pv_corr_100d_base_v078_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    p_roc = closeadj.pct_change(5)
    v_roc = volume.pct_change(5)
    res = p_roc.rolling(100).corr(v_roc)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 79: f28pvd_f28_price_volume_divergence_pv_corr_120d
def f28pvd_f28_price_volume_divergence_pv_corr_120d_base_v079_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    p_roc = closeadj.pct_change(5)
    v_roc = volume.pct_change(5)
    res = p_roc.rolling(120).corr(v_roc)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 80: f28pvd_f28_price_volume_divergence_pv_corr_126d
def f28pvd_f28_price_volume_divergence_pv_corr_126d_base_v080_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    p_roc = closeadj.pct_change(5)
    v_roc = volume.pct_change(5)
    res = p_roc.rolling(126).corr(v_roc)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 81: f28pvd_f28_price_volume_divergence_pv_corr_150d
def f28pvd_f28_price_volume_divergence_pv_corr_150d_base_v081_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    p_roc = closeadj.pct_change(5)
    v_roc = volume.pct_change(5)
    res = p_roc.rolling(150).corr(v_roc)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 82: f28pvd_f28_price_volume_divergence_pv_corr_200d
def f28pvd_f28_price_volume_divergence_pv_corr_200d_base_v082_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    p_roc = closeadj.pct_change(5)
    v_roc = volume.pct_change(5)
    res = p_roc.rolling(200).corr(v_roc)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 83: f28pvd_f28_price_volume_divergence_pv_corr_250d
def f28pvd_f28_price_volume_divergence_pv_corr_250d_base_v083_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    p_roc = closeadj.pct_change(5)
    v_roc = volume.pct_change(5)
    res = p_roc.rolling(250).corr(v_roc)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 84: f28pvd_f28_price_volume_divergence_pv_corr_252d
def f28pvd_f28_price_volume_divergence_pv_corr_252d_base_v084_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    p_roc = closeadj.pct_change(5)
    v_roc = volume.pct_change(5)
    res = p_roc.rolling(252).corr(v_roc)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 85: f28pvd_f28_price_volume_divergence_pv_corr_300d
def f28pvd_f28_price_volume_divergence_pv_corr_300d_base_v085_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    p_roc = closeadj.pct_change(5)
    v_roc = volume.pct_change(5)
    res = p_roc.rolling(300).corr(v_roc)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 86: f28pvd_f28_price_volume_divergence_pv_corr_400d
def f28pvd_f28_price_volume_divergence_pv_corr_400d_base_v086_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    p_roc = closeadj.pct_change(5)
    v_roc = volume.pct_change(5)
    res = p_roc.rolling(400).corr(v_roc)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 87: f28pvd_f28_price_volume_divergence_pv_corr_500d
def f28pvd_f28_price_volume_divergence_pv_corr_500d_base_v087_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    p_roc = closeadj.pct_change(5)
    v_roc = volume.pct_change(5)
    res = p_roc.rolling(500).corr(v_roc)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 88: f28pvd_f28_price_volume_divergence_pv_corr_504d
def f28pvd_f28_price_volume_divergence_pv_corr_504d_base_v088_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    p_roc = closeadj.pct_change(5)
    v_roc = volume.pct_change(5)
    res = p_roc.rolling(504).corr(v_roc)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 89: f28pvd_f28_price_volume_divergence_pv_mismatch_5d
def f28pvd_f28_price_volume_divergence_pv_mismatch_5d_base_v089_signal(close: pd.Series, volume: pd.Series) -> pd.Series:
    p_roc = close.pct_change(5)
    v_roc = volume.pct_change(5)
    res = (np.sign(p_roc) != np.sign(v_roc)).astype(float)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 90: f28pvd_f28_price_volume_divergence_pv_mismatch_10d
def f28pvd_f28_price_volume_divergence_pv_mismatch_10d_base_v090_signal(close: pd.Series, volume: pd.Series) -> pd.Series:
    p_roc = close.pct_change(10)
    v_roc = volume.pct_change(10)
    res = (np.sign(p_roc) != np.sign(v_roc)).astype(float)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 91: f28pvd_f28_price_volume_divergence_pv_mismatch_15d
def f28pvd_f28_price_volume_divergence_pv_mismatch_15d_base_v091_signal(close: pd.Series, volume: pd.Series) -> pd.Series:
    p_roc = close.pct_change(15)
    v_roc = volume.pct_change(15)
    res = (np.sign(p_roc) != np.sign(v_roc)).astype(float)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 92: f28pvd_f28_price_volume_divergence_pv_mismatch_20d
def f28pvd_f28_price_volume_divergence_pv_mismatch_20d_base_v092_signal(close: pd.Series, volume: pd.Series) -> pd.Series:
    p_roc = close.pct_change(20)
    v_roc = volume.pct_change(20)
    res = (np.sign(p_roc) != np.sign(v_roc)).astype(float)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 93: f28pvd_f28_price_volume_divergence_pv_mismatch_21d
def f28pvd_f28_price_volume_divergence_pv_mismatch_21d_base_v093_signal(close: pd.Series, volume: pd.Series) -> pd.Series:
    p_roc = close.pct_change(21)
    v_roc = volume.pct_change(21)
    res = (np.sign(p_roc) != np.sign(v_roc)).astype(float)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 94: f28pvd_f28_price_volume_divergence_pv_mismatch_30d
def f28pvd_f28_price_volume_divergence_pv_mismatch_30d_base_v094_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    p_roc = closeadj.pct_change(30)
    v_roc = volume.pct_change(30)
    res = (np.sign(p_roc) != np.sign(v_roc)).astype(float)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 95: f28pvd_f28_price_volume_divergence_pv_mismatch_40d
def f28pvd_f28_price_volume_divergence_pv_mismatch_40d_base_v095_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    p_roc = closeadj.pct_change(40)
    v_roc = volume.pct_change(40)
    res = (np.sign(p_roc) != np.sign(v_roc)).astype(float)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 96: f28pvd_f28_price_volume_divergence_pv_mismatch_50d
def f28pvd_f28_price_volume_divergence_pv_mismatch_50d_base_v096_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    p_roc = closeadj.pct_change(50)
    v_roc = volume.pct_change(50)
    res = (np.sign(p_roc) != np.sign(v_roc)).astype(float)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 97: f28pvd_f28_price_volume_divergence_pv_mismatch_60d
def f28pvd_f28_price_volume_divergence_pv_mismatch_60d_base_v097_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    p_roc = closeadj.pct_change(60)
    v_roc = volume.pct_change(60)
    res = (np.sign(p_roc) != np.sign(v_roc)).astype(float)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 98: f28pvd_f28_price_volume_divergence_pv_mismatch_63d
def f28pvd_f28_price_volume_divergence_pv_mismatch_63d_base_v098_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    p_roc = closeadj.pct_change(63)
    v_roc = volume.pct_change(63)
    res = (np.sign(p_roc) != np.sign(v_roc)).astype(float)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 99: f28pvd_f28_price_volume_divergence_pv_mismatch_80d
def f28pvd_f28_price_volume_divergence_pv_mismatch_80d_base_v099_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    p_roc = closeadj.pct_change(80)
    v_roc = volume.pct_change(80)
    res = (np.sign(p_roc) != np.sign(v_roc)).astype(float)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 100: f28pvd_f28_price_volume_divergence_pv_mismatch_100d
def f28pvd_f28_price_volume_divergence_pv_mismatch_100d_base_v100_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    p_roc = closeadj.pct_change(100)
    v_roc = volume.pct_change(100)
    res = (np.sign(p_roc) != np.sign(v_roc)).astype(float)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 101: f28pvd_f28_price_volume_divergence_pv_mismatch_120d
def f28pvd_f28_price_volume_divergence_pv_mismatch_120d_base_v101_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    p_roc = closeadj.pct_change(120)
    v_roc = volume.pct_change(120)
    res = (np.sign(p_roc) != np.sign(v_roc)).astype(float)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 102: f28pvd_f28_price_volume_divergence_pv_mismatch_126d
def f28pvd_f28_price_volume_divergence_pv_mismatch_126d_base_v102_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    p_roc = closeadj.pct_change(126)
    v_roc = volume.pct_change(126)
    res = (np.sign(p_roc) != np.sign(v_roc)).astype(float)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 103: f28pvd_f28_price_volume_divergence_pv_mismatch_150d
def f28pvd_f28_price_volume_divergence_pv_mismatch_150d_base_v103_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    p_roc = closeadj.pct_change(150)
    v_roc = volume.pct_change(150)
    res = (np.sign(p_roc) != np.sign(v_roc)).astype(float)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 104: f28pvd_f28_price_volume_divergence_pv_mismatch_200d
def f28pvd_f28_price_volume_divergence_pv_mismatch_200d_base_v104_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    p_roc = closeadj.pct_change(200)
    v_roc = volume.pct_change(200)
    res = (np.sign(p_roc) != np.sign(v_roc)).astype(float)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 105: f28pvd_f28_price_volume_divergence_pv_mismatch_250d
def f28pvd_f28_price_volume_divergence_pv_mismatch_250d_base_v105_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    p_roc = closeadj.pct_change(250)
    v_roc = volume.pct_change(250)
    res = (np.sign(p_roc) != np.sign(v_roc)).astype(float)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 106: f28pvd_f28_price_volume_divergence_pv_mismatch_252d
def f28pvd_f28_price_volume_divergence_pv_mismatch_252d_base_v106_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    p_roc = closeadj.pct_change(252)
    v_roc = volume.pct_change(252)
    res = (np.sign(p_roc) != np.sign(v_roc)).astype(float)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 107: f28pvd_f28_price_volume_divergence_pv_mismatch_300d
def f28pvd_f28_price_volume_divergence_pv_mismatch_300d_base_v107_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    p_roc = closeadj.pct_change(300)
    v_roc = volume.pct_change(300)
    res = (np.sign(p_roc) != np.sign(v_roc)).astype(float)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 108: f28pvd_f28_price_volume_divergence_pv_mismatch_400d
def f28pvd_f28_price_volume_divergence_pv_mismatch_400d_base_v108_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    p_roc = closeadj.pct_change(400)
    v_roc = volume.pct_change(400)
    res = (np.sign(p_roc) != np.sign(v_roc)).astype(float)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 109: f28pvd_f28_price_volume_divergence_pv_mismatch_500d
def f28pvd_f28_price_volume_divergence_pv_mismatch_500d_base_v109_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    p_roc = closeadj.pct_change(500)
    v_roc = volume.pct_change(500)
    res = (np.sign(p_roc) != np.sign(v_roc)).astype(float)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 110: f28pvd_f28_price_volume_divergence_pv_mismatch_504d
def f28pvd_f28_price_volume_divergence_pv_mismatch_504d_base_v110_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    p_roc = closeadj.pct_change(504)
    v_roc = volume.pct_change(504)
    res = (np.sign(p_roc) != np.sign(v_roc)).astype(float)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 111: f28pvd_f28_price_volume_divergence_hl_div_10d
def f28pvd_f28_price_volume_divergence_hl_div_10d_base_v111_signal(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    p_roc = (high - low).pct_change(10)
    v_roc = volume.pct_change(10)
    res = _pv_div_val(p_roc, v_roc)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 112: f28pvd_f28_price_volume_divergence_hl_div_21d
def f28pvd_f28_price_volume_divergence_hl_div_21d_base_v112_signal(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    p_roc = (high - low).pct_change(21)
    v_roc = volume.pct_change(21)
    res = _pv_div_val(p_roc, v_roc)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 113: f28pvd_f28_price_volume_divergence_hl_div_63d
def f28pvd_f28_price_volume_divergence_hl_div_63d_base_v113_signal(close: pd.Series, closeadj: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    h_adj = high * adj
    l_adj = low * adj
    p_roc = (h_adj - l_adj).pct_change(63)
    v_roc = volume.pct_change(63)
    res = _pv_div_val(p_roc, v_roc)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 114: f28pvd_f28_price_volume_divergence_hl_div_126d
def f28pvd_f28_price_volume_divergence_hl_div_126d_base_v114_signal(close: pd.Series, closeadj: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    h_adj = high * adj
    l_adj = low * adj
    p_roc = (h_adj - l_adj).pct_change(126)
    v_roc = volume.pct_change(126)
    res = _pv_div_val(p_roc, v_roc)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 115: f28pvd_f28_price_volume_divergence_hl_div_252d
def f28pvd_f28_price_volume_divergence_hl_div_252d_base_v115_signal(close: pd.Series, closeadj: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    h_adj = high * adj
    l_adj = low * adj
    p_roc = (h_adj - l_adj).pct_change(252)
    v_roc = volume.pct_change(252)
    res = _pv_div_val(p_roc, v_roc)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 116: f28pvd_f28_price_volume_divergence_pv_div_ema_21d
def f28pvd_f28_price_volume_divergence_pv_div_ema_21d_base_v116_signal(close: pd.Series, volume: pd.Series) -> pd.Series:
    p_roc = close.ewm(span=21).mean().pct_change(5)
    v_roc = volume.ewm(span=21).mean().pct_change(5)
    res = _pv_div_val(p_roc, v_roc)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 117: f28pvd_f28_price_volume_divergence_pv_div_ema_63d
def f28pvd_f28_price_volume_divergence_pv_div_ema_63d_base_v117_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    p_roc = closeadj.ewm(span=63).mean().pct_change(5)
    v_roc = volume.ewm(span=63).mean().pct_change(5)
    res = _pv_div_val(p_roc, v_roc)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 118: f28pvd_f28_price_volume_divergence_pv_div_ema_126d
def f28pvd_f28_price_volume_divergence_pv_div_ema_126d_base_v118_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    p_roc = closeadj.ewm(span=126).mean().pct_change(5)
    v_roc = volume.ewm(span=126).mean().pct_change(5)
    res = _pv_div_val(p_roc, v_roc)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 119: f28pvd_f28_price_volume_divergence_pv_div_ema_252d
def f28pvd_f28_price_volume_divergence_pv_div_ema_252d_base_v119_signal(closeadj: pd.Series, volume: pd.Series) -> pd.Series:
    p_roc = closeadj.ewm(span=252).mean().pct_change(5)
    v_roc = volume.ewm(span=252).mean().pct_change(5)
    res = _pv_div_val(p_roc, v_roc)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 120: f28pvd_f28_price_volume_divergence_pv_div_extra_124d
def f28pvd_f28_price_volume_divergence_pv_div_extra_124d_base_v120_signal(close: pd.Series, volume: pd.Series) -> pd.Series:
    p_roc = close.pct_change(124)
    v_roc = volume.pct_change(124)
    res = _pv_div_val(p_roc, v_roc)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 121: f28pvd_f28_price_volume_divergence_pv_div_extra_125d
def f28pvd_f28_price_volume_divergence_pv_div_extra_125d_base_v121_signal(close: pd.Series, volume: pd.Series) -> pd.Series:
    p_roc = close.pct_change(125)
    v_roc = volume.pct_change(125)
    res = _pv_div_val(p_roc, v_roc)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 122: f28pvd_f28_price_volume_divergence_pv_div_extra_126d
def f28pvd_f28_price_volume_divergence_pv_div_extra_126d_base_v122_signal(close: pd.Series, volume: pd.Series) -> pd.Series:
    p_roc = close.pct_change(126)
    v_roc = volume.pct_change(126)
    res = _pv_div_val(p_roc, v_roc)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 123: f28pvd_f28_price_volume_divergence_pv_div_extra_127d
def f28pvd_f28_price_volume_divergence_pv_div_extra_127d_base_v123_signal(close: pd.Series, volume: pd.Series) -> pd.Series:
    p_roc = close.pct_change(127)
    v_roc = volume.pct_change(127)
    res = _pv_div_val(p_roc, v_roc)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 124: f28pvd_f28_price_volume_divergence_pv_div_extra_128d
def f28pvd_f28_price_volume_divergence_pv_div_extra_128d_base_v124_signal(close: pd.Series, volume: pd.Series) -> pd.Series:
    p_roc = close.pct_change(128)
    v_roc = volume.pct_change(128)
    res = _pv_div_val(p_roc, v_roc)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 125: f28pvd_f28_price_volume_divergence_pv_div_extra_129d
def f28pvd_f28_price_volume_divergence_pv_div_extra_129d_base_v125_signal(close: pd.Series, volume: pd.Series) -> pd.Series:
    p_roc = close.pct_change(129)
    v_roc = volume.pct_change(129)
    res = _pv_div_val(p_roc, v_roc)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 126: f28pvd_f28_price_volume_divergence_pv_div_extra_130d
def f28pvd_f28_price_volume_divergence_pv_div_extra_130d_base_v126_signal(close: pd.Series, volume: pd.Series) -> pd.Series:
    p_roc = close.pct_change(130)
    v_roc = volume.pct_change(130)
    res = _pv_div_val(p_roc, v_roc)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 127: f28pvd_f28_price_volume_divergence_pv_div_extra_131d
def f28pvd_f28_price_volume_divergence_pv_div_extra_131d_base_v127_signal(close: pd.Series, volume: pd.Series) -> pd.Series:
    p_roc = close.pct_change(131)
    v_roc = volume.pct_change(131)
    res = _pv_div_val(p_roc, v_roc)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 128: f28pvd_f28_price_volume_divergence_pv_div_extra_132d
def f28pvd_f28_price_volume_divergence_pv_div_extra_132d_base_v128_signal(close: pd.Series, volume: pd.Series) -> pd.Series:
    p_roc = close.pct_change(132)
    v_roc = volume.pct_change(132)
    res = _pv_div_val(p_roc, v_roc)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 129: f28pvd_f28_price_volume_divergence_pv_div_extra_133d
def f28pvd_f28_price_volume_divergence_pv_div_extra_133d_base_v129_signal(close: pd.Series, volume: pd.Series) -> pd.Series:
    p_roc = close.pct_change(133)
    v_roc = volume.pct_change(133)
    res = _pv_div_val(p_roc, v_roc)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 130: f28pvd_f28_price_volume_divergence_pv_div_extra_134d
def f28pvd_f28_price_volume_divergence_pv_div_extra_134d_base_v130_signal(close: pd.Series, volume: pd.Series) -> pd.Series:
    p_roc = close.pct_change(134)
    v_roc = volume.pct_change(134)
    res = _pv_div_val(p_roc, v_roc)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 131: f28pvd_f28_price_volume_divergence_pv_div_extra_135d
def f28pvd_f28_price_volume_divergence_pv_div_extra_135d_base_v131_signal(close: pd.Series, volume: pd.Series) -> pd.Series:
    p_roc = close.pct_change(135)
    v_roc = volume.pct_change(135)
    res = _pv_div_val(p_roc, v_roc)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 132: f28pvd_f28_price_volume_divergence_pv_div_extra_136d
def f28pvd_f28_price_volume_divergence_pv_div_extra_136d_base_v132_signal(close: pd.Series, volume: pd.Series) -> pd.Series:
    p_roc = close.pct_change(136)
    v_roc = volume.pct_change(136)
    res = _pv_div_val(p_roc, v_roc)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 133: f28pvd_f28_price_volume_divergence_pv_div_extra_137d
def f28pvd_f28_price_volume_divergence_pv_div_extra_137d_base_v133_signal(close: pd.Series, volume: pd.Series) -> pd.Series:
    p_roc = close.pct_change(137)
    v_roc = volume.pct_change(137)
    res = _pv_div_val(p_roc, v_roc)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 134: f28pvd_f28_price_volume_divergence_pv_div_extra_138d
def f28pvd_f28_price_volume_divergence_pv_div_extra_138d_base_v134_signal(close: pd.Series, volume: pd.Series) -> pd.Series:
    p_roc = close.pct_change(138)
    v_roc = volume.pct_change(138)
    res = _pv_div_val(p_roc, v_roc)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 135: f28pvd_f28_price_volume_divergence_pv_div_extra_139d
def f28pvd_f28_price_volume_divergence_pv_div_extra_139d_base_v135_signal(close: pd.Series, volume: pd.Series) -> pd.Series:
    p_roc = close.pct_change(139)
    v_roc = volume.pct_change(139)
    res = _pv_div_val(p_roc, v_roc)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 136: f28pvd_f28_price_volume_divergence_pv_div_extra_140d
def f28pvd_f28_price_volume_divergence_pv_div_extra_140d_base_v136_signal(close: pd.Series, volume: pd.Series) -> pd.Series:
    p_roc = close.pct_change(140)
    v_roc = volume.pct_change(140)
    res = _pv_div_val(p_roc, v_roc)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 137: f28pvd_f28_price_volume_divergence_pv_div_extra_141d
def f28pvd_f28_price_volume_divergence_pv_div_extra_141d_base_v137_signal(close: pd.Series, volume: pd.Series) -> pd.Series:
    p_roc = close.pct_change(141)
    v_roc = volume.pct_change(141)
    res = _pv_div_val(p_roc, v_roc)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 138: f28pvd_f28_price_volume_divergence_pv_div_extra_142d
def f28pvd_f28_price_volume_divergence_pv_div_extra_142d_base_v138_signal(close: pd.Series, volume: pd.Series) -> pd.Series:
    p_roc = close.pct_change(142)
    v_roc = volume.pct_change(142)
    res = _pv_div_val(p_roc, v_roc)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 139: f28pvd_f28_price_volume_divergence_pv_div_extra_143d
def f28pvd_f28_price_volume_divergence_pv_div_extra_143d_base_v139_signal(close: pd.Series, volume: pd.Series) -> pd.Series:
    p_roc = close.pct_change(143)
    v_roc = volume.pct_change(143)
    res = _pv_div_val(p_roc, v_roc)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 140: f28pvd_f28_price_volume_divergence_pv_div_extra_144d
def f28pvd_f28_price_volume_divergence_pv_div_extra_144d_base_v140_signal(close: pd.Series, volume: pd.Series) -> pd.Series:
    p_roc = close.pct_change(144)
    v_roc = volume.pct_change(144)
    res = _pv_div_val(p_roc, v_roc)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 141: f28pvd_f28_price_volume_divergence_pv_div_extra_145d
def f28pvd_f28_price_volume_divergence_pv_div_extra_145d_base_v141_signal(close: pd.Series, volume: pd.Series) -> pd.Series:
    p_roc = close.pct_change(145)
    v_roc = volume.pct_change(145)
    res = _pv_div_val(p_roc, v_roc)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 142: f28pvd_f28_price_volume_divergence_pv_div_extra_146d
def f28pvd_f28_price_volume_divergence_pv_div_extra_146d_base_v142_signal(close: pd.Series, volume: pd.Series) -> pd.Series:
    p_roc = close.pct_change(146)
    v_roc = volume.pct_change(146)
    res = _pv_div_val(p_roc, v_roc)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 143: f28pvd_f28_price_volume_divergence_pv_div_extra_147d
def f28pvd_f28_price_volume_divergence_pv_div_extra_147d_base_v143_signal(close: pd.Series, volume: pd.Series) -> pd.Series:
    p_roc = close.pct_change(147)
    v_roc = volume.pct_change(147)
    res = _pv_div_val(p_roc, v_roc)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 144: f28pvd_f28_price_volume_divergence_pv_div_extra_148d
def f28pvd_f28_price_volume_divergence_pv_div_extra_148d_base_v144_signal(close: pd.Series, volume: pd.Series) -> pd.Series:
    p_roc = close.pct_change(148)
    v_roc = volume.pct_change(148)
    res = _pv_div_val(p_roc, v_roc)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 145: f28pvd_f28_price_volume_divergence_pv_div_extra_149d
def f28pvd_f28_price_volume_divergence_pv_div_extra_149d_base_v145_signal(close: pd.Series, volume: pd.Series) -> pd.Series:
    p_roc = close.pct_change(149)
    v_roc = volume.pct_change(149)
    res = _pv_div_val(p_roc, v_roc)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 146: f28pvd_f28_price_volume_divergence_pv_div_extra_150d
def f28pvd_f28_price_volume_divergence_pv_div_extra_150d_base_v146_signal(close: pd.Series, volume: pd.Series) -> pd.Series:
    p_roc = close.pct_change(150)
    v_roc = volume.pct_change(150)
    res = _pv_div_val(p_roc, v_roc)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 147: f28pvd_f28_price_volume_divergence_pv_div_extra_151d
def f28pvd_f28_price_volume_divergence_pv_div_extra_151d_base_v147_signal(close: pd.Series, volume: pd.Series) -> pd.Series:
    p_roc = close.pct_change(151)
    v_roc = volume.pct_change(151)
    res = _pv_div_val(p_roc, v_roc)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 148: f28pvd_f28_price_volume_divergence_pv_div_extra_152d
def f28pvd_f28_price_volume_divergence_pv_div_extra_152d_base_v148_signal(close: pd.Series, volume: pd.Series) -> pd.Series:
    p_roc = close.pct_change(152)
    v_roc = volume.pct_change(152)
    res = _pv_div_val(p_roc, v_roc)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 149: f28pvd_f28_price_volume_divergence_pv_div_extra_153d
def f28pvd_f28_price_volume_divergence_pv_div_extra_153d_base_v149_signal(close: pd.Series, volume: pd.Series) -> pd.Series:
    p_roc = close.pct_change(153)
    v_roc = volume.pct_change(153)
    res = _pv_div_val(p_roc, v_roc)
    return res.replace([np.inf, -np.inf], np.nan)

# Feature 150: f28pvd_f28_price_volume_divergence_pv_div_extra_154d
def f28pvd_f28_price_volume_divergence_pv_div_extra_154d_base_v150_signal(close: pd.Series, volume: pd.Series) -> pd.Series:
    p_roc = close.pct_change(154)
    v_roc = volume.pct_change(154)
    res = _pv_div_val(p_roc, v_roc)
    return res.replace([np.inf, -np.inf], np.nan)

SILVERDB_ACCESS, SOURCE_TABLE, ENTITY_COLUMN, DATE_COLUMN = "read_only", "sep", "ticker", "date"
ORDER_BY, NO_FORWARD_LOOKING = [ENTITY_COLUMN, DATE_COLUMN], True
SOURCE_COLUMNS = {c: f"sep.{c}" for c in ["close", "closeadj", "high", "low", "volume"]}

BASE_NAMES = [f for f in globals() if f.startswith("f28pvd_") and f.endswith("_signal")]

F28_PRICE_VOLUME_DIVERGENCE_BASE_REGISTRY_076_150 = {
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
    for n, c in F28_PRICE_VOLUME_DIVERGENCE_BASE_REGISTRY_076_150.items():
        r = c["func"](**{i: d[i] for i in c["inputs"]})
        assert isinstance(r, pd.Series)
    print("base OK")