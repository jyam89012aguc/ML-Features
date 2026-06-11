
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
    fcf = df['fcf']
    ni = df['netinc']
    ebitda = df['ebitda']
    fcf_conv = fcf / ni.replace(0, np.nan)
    f = {}
    f['f37_fcf_conversion_velocity_076'] = _z(_roc(fcf_conv, 63), 63)
    f['f37_fcf_conversion_velocity_077'] = _z(fcf_conv.diff(126), 252)
    f['f37_fcf_conversion_velocity_078'] = _z(fcf_conv / _std(fcf_conv, 252).replace(0, 1), 252)
    f['f37_fcf_conversion_velocity_079'] = _z(_ema(fcf_conv, 504) - _ema(fcf_conv, 1008), 1512)
    f['f37_fcf_conversion_velocity_080'] = _z(fcf_conv, 21)
    f['f37_fcf_conversion_velocity_081'] = _z(_roc(fcf_conv, 63), 63)
    f['f37_fcf_conversion_velocity_082'] = _z(fcf_conv.diff(126), 252)
    f['f37_fcf_conversion_velocity_083'] = _z(fcf_conv / _std(fcf_conv, 252).replace(0, 1), 252)
    f['f37_fcf_conversion_velocity_084'] = _z(_ema(fcf_conv, 504) - _ema(fcf_conv, 1008), 1512)
    f['f37_fcf_conversion_velocity_085'] = _z(fcf_conv, 21)
    f['f37_fcf_conversion_velocity_086'] = _z(_roc(fcf_conv, 63), 63)
    f['f37_fcf_conversion_velocity_087'] = _z(fcf_conv.diff(126), 252)
    f['f37_fcf_conversion_velocity_088'] = _z(fcf_conv / _std(fcf_conv, 252).replace(0, 1), 252)
    f['f37_fcf_conversion_velocity_089'] = _z(_ema(fcf_conv, 504) - _ema(fcf_conv, 1008), 1512)
    f['f37_fcf_conversion_velocity_090'] = _z(fcf_conv, 21)
    f['f37_fcf_conversion_velocity_091'] = _z(_roc(fcf_conv, 63), 63)
    f['f37_fcf_conversion_velocity_092'] = _z(fcf_conv.diff(126), 252)
    f['f37_fcf_conversion_velocity_093'] = _z(fcf_conv / _std(fcf_conv, 252).replace(0, 1), 252)
    f['f37_fcf_conversion_velocity_094'] = _z(_ema(fcf_conv, 504) - _ema(fcf_conv, 1008), 1512)
    f['f37_fcf_conversion_velocity_095'] = _z(fcf_conv, 21)
    f['f37_fcf_conversion_velocity_096'] = _z(_roc(fcf_conv, 63), 63)
    f['f37_fcf_conversion_velocity_097'] = _z(fcf_conv.diff(126), 252)
    f['f37_fcf_conversion_velocity_098'] = _z(fcf_conv / _std(fcf_conv, 252).replace(0, 1), 252)
    f['f37_fcf_conversion_velocity_099'] = _z(_ema(fcf_conv, 504) - _ema(fcf_conv, 1008), 1512)
    f['f37_fcf_conversion_velocity_100'] = _z(fcf_conv, 21)
    f['f37_fcf_conversion_velocity_101'] = _z(_roc(fcf_conv, 63), 63)
    f['f37_fcf_conversion_velocity_102'] = _z(fcf_conv.diff(126), 252)
    f['f37_fcf_conversion_velocity_103'] = _z(fcf_conv / _std(fcf_conv, 252).replace(0, 1), 252)
    f['f37_fcf_conversion_velocity_104'] = _z(_ema(fcf_conv, 504) - _ema(fcf_conv, 1008), 1512)
    f['f37_fcf_conversion_velocity_105'] = _z(fcf_conv, 21)
    f['f37_fcf_conversion_velocity_106'] = _z(_roc(fcf_conv, 63), 63)
    f['f37_fcf_conversion_velocity_107'] = _z(fcf_conv.diff(126), 252)
    f['f37_fcf_conversion_velocity_108'] = _z(fcf_conv / _std(fcf_conv, 252).replace(0, 1), 252)
    f['f37_fcf_conversion_velocity_109'] = _z(_ema(fcf_conv, 504) - _ema(fcf_conv, 1008), 1512)
    f['f37_fcf_conversion_velocity_110'] = _z(fcf_conv, 21)
    f['f37_fcf_conversion_velocity_111'] = _z(_roc(fcf_conv, 63), 63)
    f['f37_fcf_conversion_velocity_112'] = _z(fcf_conv.diff(126), 252)
    f['f37_fcf_conversion_velocity_113'] = _z(fcf_conv / _std(fcf_conv, 252).replace(0, 1), 252)
    f['f37_fcf_conversion_velocity_114'] = _z(_ema(fcf_conv, 504) - _ema(fcf_conv, 1008), 1512)
    f['f37_fcf_conversion_velocity_115'] = _z(fcf_conv, 21)
    f['f37_fcf_conversion_velocity_116'] = _z(_roc(fcf_conv, 63), 63)
    f['f37_fcf_conversion_velocity_117'] = _z(fcf_conv.diff(126), 252)
    f['f37_fcf_conversion_velocity_118'] = _z(fcf_conv / _std(fcf_conv, 252).replace(0, 1), 252)
    f['f37_fcf_conversion_velocity_119'] = _z(_ema(fcf_conv, 504) - _ema(fcf_conv, 1008), 1512)
    f['f37_fcf_conversion_velocity_120'] = _z(fcf_conv, 21)
    f['f37_fcf_conversion_velocity_121'] = _z(_roc(fcf_conv, 63), 63)
    f['f37_fcf_conversion_velocity_122'] = _z(fcf_conv.diff(126), 252)
    f['f37_fcf_conversion_velocity_123'] = _z(fcf_conv / _std(fcf_conv, 252).replace(0, 1), 252)
    f['f37_fcf_conversion_velocity_124'] = _z(_ema(fcf_conv, 504) - _ema(fcf_conv, 1008), 1512)
    f['f37_fcf_conversion_velocity_125'] = _z(fcf_conv, 21)
    f['f37_fcf_conversion_velocity_126'] = _z(_roc(fcf_conv, 63), 63)
    f['f37_fcf_conversion_velocity_127'] = _z(fcf_conv.diff(126), 252)
    f['f37_fcf_conversion_velocity_128'] = _z(fcf_conv / _std(fcf_conv, 252).replace(0, 1), 252)
    f['f37_fcf_conversion_velocity_129'] = _z(_ema(fcf_conv, 504) - _ema(fcf_conv, 1008), 1512)
    f['f37_fcf_conversion_velocity_130'] = _z(fcf_conv, 21)
    f['f37_fcf_conversion_velocity_131'] = _z(_roc(fcf_conv, 63), 63)
    f['f37_fcf_conversion_velocity_132'] = _z(fcf_conv.diff(126), 252)
    f['f37_fcf_conversion_velocity_133'] = _z(fcf_conv / _std(fcf_conv, 252).replace(0, 1), 252)
    f['f37_fcf_conversion_velocity_134'] = _z(_ema(fcf_conv, 504) - _ema(fcf_conv, 1008), 1512)
    f['f37_fcf_conversion_velocity_135'] = _z(fcf_conv, 21)
    f['f37_fcf_conversion_velocity_136'] = _z(_roc(fcf_conv, 63), 63)
    f['f37_fcf_conversion_velocity_137'] = _z(fcf_conv.diff(126), 252)
    f['f37_fcf_conversion_velocity_138'] = _z(fcf_conv / _std(fcf_conv, 252).replace(0, 1), 252)
    f['f37_fcf_conversion_velocity_139'] = _z(_ema(fcf_conv, 504) - _ema(fcf_conv, 1008), 1512)
    f['f37_fcf_conversion_velocity_140'] = _z(fcf_conv, 21)
    f['f37_fcf_conversion_velocity_141'] = _z(_roc(fcf_conv, 63), 63)
    f['f37_fcf_conversion_velocity_142'] = _z(fcf_conv.diff(126), 252)
    f['f37_fcf_conversion_velocity_143'] = _z(fcf_conv / _std(fcf_conv, 252).replace(0, 1), 252)
    f['f37_fcf_conversion_velocity_144'] = _z(_ema(fcf_conv, 504) - _ema(fcf_conv, 1008), 1512)
    f['f37_fcf_conversion_velocity_145'] = _z(fcf_conv, 21)
    f['f37_fcf_conversion_velocity_146'] = _z(_roc(fcf_conv, 63), 63)
    f['f37_fcf_conversion_velocity_147'] = _z(fcf_conv.diff(126), 252)
    f['f37_fcf_conversion_velocity_148'] = _z(fcf_conv / _std(fcf_conv, 252).replace(0, 1), 252)
    f['f37_fcf_conversion_velocity_149'] = _z(_ema(fcf_conv, 504) - _ema(fcf_conv, 1008), 1512)
    f['f37_fcf_conversion_velocity_150'] = _z(fcf_conv, 21)
    return pd.DataFrame(f)