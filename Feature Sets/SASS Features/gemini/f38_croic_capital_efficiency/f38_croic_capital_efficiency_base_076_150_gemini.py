
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
    ic = df['invcap']
    croic = fcf / ic.replace(0, np.nan)
    f = {}
    f['f38_croic_capital_efficiency_076'] = _z(_roc(croic, 63), 63)
    f['f38_croic_capital_efficiency_077'] = _z(croic.diff(126), 252)
    f['f38_croic_capital_efficiency_078'] = _z(croic / _std(croic, 252).replace(0, 1), 252)
    f['f38_croic_capital_efficiency_079'] = _z(_ema(croic, 504) - _ema(croic, 1008), 1512)
    f['f38_croic_capital_efficiency_080'] = _z(croic, 21)
    f['f38_croic_capital_efficiency_081'] = _z(_roc(croic, 63), 63)
    f['f38_croic_capital_efficiency_082'] = _z(croic.diff(126), 252)
    f['f38_croic_capital_efficiency_083'] = _z(croic / _std(croic, 252).replace(0, 1), 252)
    f['f38_croic_capital_efficiency_084'] = _z(_ema(croic, 504) - _ema(croic, 1008), 1512)
    f['f38_croic_capital_efficiency_085'] = _z(croic, 21)
    f['f38_croic_capital_efficiency_086'] = _z(_roc(croic, 63), 63)
    f['f38_croic_capital_efficiency_087'] = _z(croic.diff(126), 252)
    f['f38_croic_capital_efficiency_088'] = _z(croic / _std(croic, 252).replace(0, 1), 252)
    f['f38_croic_capital_efficiency_089'] = _z(_ema(croic, 504) - _ema(croic, 1008), 1512)
    f['f38_croic_capital_efficiency_090'] = _z(croic, 21)
    f['f38_croic_capital_efficiency_091'] = _z(_roc(croic, 63), 63)
    f['f38_croic_capital_efficiency_092'] = _z(croic.diff(126), 252)
    f['f38_croic_capital_efficiency_093'] = _z(croic / _std(croic, 252).replace(0, 1), 252)
    f['f38_croic_capital_efficiency_094'] = _z(_ema(croic, 504) - _ema(croic, 1008), 1512)
    f['f38_croic_capital_efficiency_095'] = _z(croic, 21)
    f['f38_croic_capital_efficiency_096'] = _z(_roc(croic, 63), 63)
    f['f38_croic_capital_efficiency_097'] = _z(croic.diff(126), 252)
    f['f38_croic_capital_efficiency_098'] = _z(croic / _std(croic, 252).replace(0, 1), 252)
    f['f38_croic_capital_efficiency_099'] = _z(_ema(croic, 504) - _ema(croic, 1008), 1512)
    f['f38_croic_capital_efficiency_100'] = _z(croic, 21)
    f['f38_croic_capital_efficiency_101'] = _z(_roc(croic, 63), 63)
    f['f38_croic_capital_efficiency_102'] = _z(croic.diff(126), 252)
    f['f38_croic_capital_efficiency_103'] = _z(croic / _std(croic, 252).replace(0, 1), 252)
    f['f38_croic_capital_efficiency_104'] = _z(_ema(croic, 504) - _ema(croic, 1008), 1512)
    f['f38_croic_capital_efficiency_105'] = _z(croic, 21)
    f['f38_croic_capital_efficiency_106'] = _z(_roc(croic, 63), 63)
    f['f38_croic_capital_efficiency_107'] = _z(croic.diff(126), 252)
    f['f38_croic_capital_efficiency_108'] = _z(croic / _std(croic, 252).replace(0, 1), 252)
    f['f38_croic_capital_efficiency_109'] = _z(_ema(croic, 504) - _ema(croic, 1008), 1512)
    f['f38_croic_capital_efficiency_110'] = _z(croic, 21)
    f['f38_croic_capital_efficiency_111'] = _z(_roc(croic, 63), 63)
    f['f38_croic_capital_efficiency_112'] = _z(croic.diff(126), 252)
    f['f38_croic_capital_efficiency_113'] = _z(croic / _std(croic, 252).replace(0, 1), 252)
    f['f38_croic_capital_efficiency_114'] = _z(_ema(croic, 504) - _ema(croic, 1008), 1512)
    f['f38_croic_capital_efficiency_115'] = _z(croic, 21)
    f['f38_croic_capital_efficiency_116'] = _z(_roc(croic, 63), 63)
    f['f38_croic_capital_efficiency_117'] = _z(croic.diff(126), 252)
    f['f38_croic_capital_efficiency_118'] = _z(croic / _std(croic, 252).replace(0, 1), 252)
    f['f38_croic_capital_efficiency_119'] = _z(_ema(croic, 504) - _ema(croic, 1008), 1512)
    f['f38_croic_capital_efficiency_120'] = _z(croic, 21)
    f['f38_croic_capital_efficiency_121'] = _z(_roc(croic, 63), 63)
    f['f38_croic_capital_efficiency_122'] = _z(croic.diff(126), 252)
    f['f38_croic_capital_efficiency_123'] = _z(croic / _std(croic, 252).replace(0, 1), 252)
    f['f38_croic_capital_efficiency_124'] = _z(_ema(croic, 504) - _ema(croic, 1008), 1512)
    f['f38_croic_capital_efficiency_125'] = _z(croic, 21)
    f['f38_croic_capital_efficiency_126'] = _z(_roc(croic, 63), 63)
    f['f38_croic_capital_efficiency_127'] = _z(croic.diff(126), 252)
    f['f38_croic_capital_efficiency_128'] = _z(croic / _std(croic, 252).replace(0, 1), 252)
    f['f38_croic_capital_efficiency_129'] = _z(_ema(croic, 504) - _ema(croic, 1008), 1512)
    f['f38_croic_capital_efficiency_130'] = _z(croic, 21)
    f['f38_croic_capital_efficiency_131'] = _z(_roc(croic, 63), 63)
    f['f38_croic_capital_efficiency_132'] = _z(croic.diff(126), 252)
    f['f38_croic_capital_efficiency_133'] = _z(croic / _std(croic, 252).replace(0, 1), 252)
    f['f38_croic_capital_efficiency_134'] = _z(_ema(croic, 504) - _ema(croic, 1008), 1512)
    f['f38_croic_capital_efficiency_135'] = _z(croic, 21)
    f['f38_croic_capital_efficiency_136'] = _z(_roc(croic, 63), 63)
    f['f38_croic_capital_efficiency_137'] = _z(croic.diff(126), 252)
    f['f38_croic_capital_efficiency_138'] = _z(croic / _std(croic, 252).replace(0, 1), 252)
    f['f38_croic_capital_efficiency_139'] = _z(_ema(croic, 504) - _ema(croic, 1008), 1512)
    f['f38_croic_capital_efficiency_140'] = _z(croic, 21)
    f['f38_croic_capital_efficiency_141'] = _z(_roc(croic, 63), 63)
    f['f38_croic_capital_efficiency_142'] = _z(croic.diff(126), 252)
    f['f38_croic_capital_efficiency_143'] = _z(croic / _std(croic, 252).replace(0, 1), 252)
    f['f38_croic_capital_efficiency_144'] = _z(_ema(croic, 504) - _ema(croic, 1008), 1512)
    f['f38_croic_capital_efficiency_145'] = _z(croic, 21)
    f['f38_croic_capital_efficiency_146'] = _z(_roc(croic, 63), 63)
    f['f38_croic_capital_efficiency_147'] = _z(croic.diff(126), 252)
    f['f38_croic_capital_efficiency_148'] = _z(croic / _std(croic, 252).replace(0, 1), 252)
    f['f38_croic_capital_efficiency_149'] = _z(_ema(croic, 504) - _ema(croic, 1008), 1512)
    f['f38_croic_capital_efficiency_150'] = _z(croic, 21)
    return pd.DataFrame(f)