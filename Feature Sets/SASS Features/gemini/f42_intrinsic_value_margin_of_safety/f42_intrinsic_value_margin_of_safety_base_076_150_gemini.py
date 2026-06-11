
import numpy as np
import pandas as pd

def _z(s, w):
    return (s - s.rolling(w, min_periods=max(1, w//2)).mean()) / (s.rolling(w, min_periods=max(1, w//2)).std() + 1e-9)

def _sma(s, w):
    return s.rolling(w, min_periods=max(1, w//2)).mean()

def _std(s, w):
    return s.rolling(w, min_periods=max(1, w//2)).std()

def _roc(s, w):
    return s.pct_change(w)

def _ema(s, w):
    return s.ewm(span=w, min_periods=max(1, w//2)).mean()

def _safe_div(a, b):
    return a / b.replace(0, np.nan)

def generate_features(df):
    ni = df['netinc']
    market_cap = df['marketcap']
    at = df['assets']
    re = df['retearn']
    iv_proxy = (ni / 0.1) / market_cap.replace(0, np.nan)
    f = {}
    f['f42_intrinsic_value_margin_of_safety_076'] = _z(_roc(iv_proxy, 63), 63)
    f['f42_intrinsic_value_margin_of_safety_077'] = _z(iv_proxy.diff(126), 252)
    f['f42_intrinsic_value_margin_of_safety_078'] = _z(iv_proxy / _std(iv_proxy, 252).replace(0, 1), 252)
    f['f42_intrinsic_value_margin_of_safety_079'] = _z(_ema(iv_proxy, 504) - _ema(iv_proxy, 1008), 1512)
    f['f42_intrinsic_value_margin_of_safety_080'] = _z(iv_proxy, 21)
    f['f42_intrinsic_value_margin_of_safety_081'] = _z(_roc(iv_proxy, 63), 63)
    f['f42_intrinsic_value_margin_of_safety_082'] = _z(iv_proxy.diff(126), 252)
    f['f42_intrinsic_value_margin_of_safety_083'] = _z(iv_proxy / _std(iv_proxy, 252).replace(0, 1), 252)
    f['f42_intrinsic_value_margin_of_safety_084'] = _z(_ema(iv_proxy, 504) - _ema(iv_proxy, 1008), 1512)
    f['f42_intrinsic_value_margin_of_safety_085'] = _z(iv_proxy, 21)
    f['f42_intrinsic_value_margin_of_safety_086'] = _z(_roc(iv_proxy, 63), 63)
    f['f42_intrinsic_value_margin_of_safety_087'] = _z(iv_proxy.diff(126), 252)
    f['f42_intrinsic_value_margin_of_safety_088'] = _z(iv_proxy / _std(iv_proxy, 252).replace(0, 1), 252)
    f['f42_intrinsic_value_margin_of_safety_089'] = _z(_ema(iv_proxy, 504) - _ema(iv_proxy, 1008), 1512)
    f['f42_intrinsic_value_margin_of_safety_090'] = _z(iv_proxy, 21)
    f['f42_intrinsic_value_margin_of_safety_091'] = _z(_roc(iv_proxy, 63), 63)
    f['f42_intrinsic_value_margin_of_safety_092'] = _z(iv_proxy.diff(126), 252)
    f['f42_intrinsic_value_margin_of_safety_093'] = _z(iv_proxy / _std(iv_proxy, 252).replace(0, 1), 252)
    f['f42_intrinsic_value_margin_of_safety_094'] = _z(_ema(iv_proxy, 504) - _ema(iv_proxy, 1008), 1512)
    f['f42_intrinsic_value_margin_of_safety_095'] = _z(iv_proxy, 21)
    f['f42_intrinsic_value_margin_of_safety_096'] = _z(_roc(iv_proxy, 63), 63)
    f['f42_intrinsic_value_margin_of_safety_097'] = _z(iv_proxy.diff(126), 252)
    f['f42_intrinsic_value_margin_of_safety_098'] = _z(iv_proxy / _std(iv_proxy, 252).replace(0, 1), 252)
    f['f42_intrinsic_value_margin_of_safety_099'] = _z(_ema(iv_proxy, 504) - _ema(iv_proxy, 1008), 1512)
    f['f42_intrinsic_value_margin_of_safety_100'] = _z(iv_proxy, 21)
    f['f42_intrinsic_value_margin_of_safety_101'] = _z(_roc(iv_proxy, 63), 63)
    f['f42_intrinsic_value_margin_of_safety_102'] = _z(iv_proxy.diff(126), 252)
    f['f42_intrinsic_value_margin_of_safety_103'] = _z(iv_proxy / _std(iv_proxy, 252).replace(0, 1), 252)
    f['f42_intrinsic_value_margin_of_safety_104'] = _z(_ema(iv_proxy, 504) - _ema(iv_proxy, 1008), 1512)
    f['f42_intrinsic_value_margin_of_safety_105'] = _z(iv_proxy, 21)
    f['f42_intrinsic_value_margin_of_safety_106'] = _z(_roc(iv_proxy, 63), 63)
    f['f42_intrinsic_value_margin_of_safety_107'] = _z(iv_proxy.diff(126), 252)
    f['f42_intrinsic_value_margin_of_safety_108'] = _z(iv_proxy / _std(iv_proxy, 252).replace(0, 1), 252)
    f['f42_intrinsic_value_margin_of_safety_109'] = _z(_ema(iv_proxy, 504) - _ema(iv_proxy, 1008), 1512)
    f['f42_intrinsic_value_margin_of_safety_110'] = _z(iv_proxy, 21)
    f['f42_intrinsic_value_margin_of_safety_111'] = _z(_roc(iv_proxy, 63), 63)
    f['f42_intrinsic_value_margin_of_safety_112'] = _z(iv_proxy.diff(126), 252)
    f['f42_intrinsic_value_margin_of_safety_113'] = _z(iv_proxy / _std(iv_proxy, 252).replace(0, 1), 252)
    f['f42_intrinsic_value_margin_of_safety_114'] = _z(_ema(iv_proxy, 504) - _ema(iv_proxy, 1008), 1512)
    f['f42_intrinsic_value_margin_of_safety_115'] = _z(iv_proxy, 21)
    f['f42_intrinsic_value_margin_of_safety_116'] = _z(_roc(iv_proxy, 63), 63)
    f['f42_intrinsic_value_margin_of_safety_117'] = _z(iv_proxy.diff(126), 252)
    f['f42_intrinsic_value_margin_of_safety_118'] = _z(iv_proxy / _std(iv_proxy, 252).replace(0, 1), 252)
    f['f42_intrinsic_value_margin_of_safety_119'] = _z(_ema(iv_proxy, 504) - _ema(iv_proxy, 1008), 1512)
    f['f42_intrinsic_value_margin_of_safety_120'] = _z(iv_proxy, 21)
    f['f42_intrinsic_value_margin_of_safety_121'] = _z(_roc(iv_proxy, 63), 63)
    f['f42_intrinsic_value_margin_of_safety_122'] = _z(iv_proxy.diff(126), 252)
    f['f42_intrinsic_value_margin_of_safety_123'] = _z(iv_proxy / _std(iv_proxy, 252).replace(0, 1), 252)
    f['f42_intrinsic_value_margin_of_safety_124'] = _z(_ema(iv_proxy, 504) - _ema(iv_proxy, 1008), 1512)
    f['f42_intrinsic_value_margin_of_safety_125'] = _z(iv_proxy, 21)
    f['f42_intrinsic_value_margin_of_safety_126'] = _z(_roc(iv_proxy, 63), 63)
    f['f42_intrinsic_value_margin_of_safety_127'] = _z(iv_proxy.diff(126), 252)
    f['f42_intrinsic_value_margin_of_safety_128'] = _z(iv_proxy / _std(iv_proxy, 252).replace(0, 1), 252)
    f['f42_intrinsic_value_margin_of_safety_129'] = _z(_ema(iv_proxy, 504) - _ema(iv_proxy, 1008), 1512)
    f['f42_intrinsic_value_margin_of_safety_130'] = _z(iv_proxy, 21)
    f['f42_intrinsic_value_margin_of_safety_131'] = _z(_roc(iv_proxy, 63), 63)
    f['f42_intrinsic_value_margin_of_safety_132'] = _z(iv_proxy.diff(126), 252)
    f['f42_intrinsic_value_margin_of_safety_133'] = _z(iv_proxy / _std(iv_proxy, 252).replace(0, 1), 252)
    f['f42_intrinsic_value_margin_of_safety_134'] = _z(_ema(iv_proxy, 504) - _ema(iv_proxy, 1008), 1512)
    f['f42_intrinsic_value_margin_of_safety_135'] = _z(iv_proxy, 21)
    f['f42_intrinsic_value_margin_of_safety_136'] = _z(_roc(iv_proxy, 63), 63)
    f['f42_intrinsic_value_margin_of_safety_137'] = _z(iv_proxy.diff(126), 252)
    f['f42_intrinsic_value_margin_of_safety_138'] = _z(iv_proxy / _std(iv_proxy, 252).replace(0, 1), 252)
    f['f42_intrinsic_value_margin_of_safety_139'] = _z(_ema(iv_proxy, 504) - _ema(iv_proxy, 1008), 1512)
    f['f42_intrinsic_value_margin_of_safety_140'] = _z(iv_proxy, 21)
    f['f42_intrinsic_value_margin_of_safety_141'] = _z(_roc(iv_proxy, 63), 63)
    f['f42_intrinsic_value_margin_of_safety_142'] = _z(iv_proxy.diff(126), 252)
    f['f42_intrinsic_value_margin_of_safety_143'] = _z(iv_proxy / _std(iv_proxy, 252).replace(0, 1), 252)
    f['f42_intrinsic_value_margin_of_safety_144'] = _z(_ema(iv_proxy, 504) - _ema(iv_proxy, 1008), 1512)
    f['f42_intrinsic_value_margin_of_safety_145'] = _z(iv_proxy, 21)
    f['f42_intrinsic_value_margin_of_safety_146'] = _z(_roc(iv_proxy, 63), 63)
    f['f42_intrinsic_value_margin_of_safety_147'] = _z(iv_proxy.diff(126), 252)
    f['f42_intrinsic_value_margin_of_safety_148'] = _z(iv_proxy / _std(iv_proxy, 252).replace(0, 1), 252)
    f['f42_intrinsic_value_margin_of_safety_149'] = _z(_ema(iv_proxy, 504) - _ema(iv_proxy, 1008), 1512)
    f['f42_intrinsic_value_margin_of_safety_150'] = _z(iv_proxy, 21)
    return pd.DataFrame(f)