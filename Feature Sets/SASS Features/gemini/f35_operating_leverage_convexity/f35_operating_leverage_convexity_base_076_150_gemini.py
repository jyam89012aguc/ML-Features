
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
    ebit = df['ebit']
    rev = df['revenue']
    op_lev = ebit.pct_change(63) / rev.pct_change(63).replace(0, np.nan)
    f = {}
    f['f35_operating_leverage_convexity_076'] = _z(_roc(op_lev, 63), 63)
    f['f35_operating_leverage_convexity_077'] = _z(op_lev.diff(126), 252)
    f['f35_operating_leverage_convexity_078'] = _z(op_lev / _std(op_lev, 252).replace(0, 1), 252)
    f['f35_operating_leverage_convexity_079'] = _z(_ema(op_lev, 504) - _ema(op_lev, 1008), 1512)
    f['f35_operating_leverage_convexity_080'] = _z(op_lev, 21)
    f['f35_operating_leverage_convexity_081'] = _z(_roc(op_lev, 63), 63)
    f['f35_operating_leverage_convexity_082'] = _z(op_lev.diff(126), 252)
    f['f35_operating_leverage_convexity_083'] = _z(op_lev / _std(op_lev, 252).replace(0, 1), 252)
    f['f35_operating_leverage_convexity_084'] = _z(_ema(op_lev, 504) - _ema(op_lev, 1008), 1512)
    f['f35_operating_leverage_convexity_085'] = _z(op_lev, 21)
    f['f35_operating_leverage_convexity_086'] = _z(_roc(op_lev, 63), 63)
    f['f35_operating_leverage_convexity_087'] = _z(op_lev.diff(126), 252)
    f['f35_operating_leverage_convexity_088'] = _z(op_lev / _std(op_lev, 252).replace(0, 1), 252)
    f['f35_operating_leverage_convexity_089'] = _z(_ema(op_lev, 504) - _ema(op_lev, 1008), 1512)
    f['f35_operating_leverage_convexity_090'] = _z(op_lev, 21)
    f['f35_operating_leverage_convexity_091'] = _z(_roc(op_lev, 63), 63)
    f['f35_operating_leverage_convexity_092'] = _z(op_lev.diff(126), 252)
    f['f35_operating_leverage_convexity_093'] = _z(op_lev / _std(op_lev, 252).replace(0, 1), 252)
    f['f35_operating_leverage_convexity_094'] = _z(_ema(op_lev, 504) - _ema(op_lev, 1008), 1512)
    f['f35_operating_leverage_convexity_095'] = _z(op_lev, 21)
    f['f35_operating_leverage_convexity_096'] = _z(_roc(op_lev, 63), 63)
    f['f35_operating_leverage_convexity_097'] = _z(op_lev.diff(126), 252)
    f['f35_operating_leverage_convexity_098'] = _z(op_lev / _std(op_lev, 252).replace(0, 1), 252)
    f['f35_operating_leverage_convexity_099'] = _z(_ema(op_lev, 504) - _ema(op_lev, 1008), 1512)
    f['f35_operating_leverage_convexity_100'] = _z(op_lev, 21)
    f['f35_operating_leverage_convexity_101'] = _z(_roc(op_lev, 63), 63)
    f['f35_operating_leverage_convexity_102'] = _z(op_lev.diff(126), 252)
    f['f35_operating_leverage_convexity_103'] = _z(op_lev / _std(op_lev, 252).replace(0, 1), 252)
    f['f35_operating_leverage_convexity_104'] = _z(_ema(op_lev, 504) - _ema(op_lev, 1008), 1512)
    f['f35_operating_leverage_convexity_105'] = _z(op_lev, 21)
    f['f35_operating_leverage_convexity_106'] = _z(_roc(op_lev, 63), 63)
    f['f35_operating_leverage_convexity_107'] = _z(op_lev.diff(126), 252)
    f['f35_operating_leverage_convexity_108'] = _z(op_lev / _std(op_lev, 252).replace(0, 1), 252)
    f['f35_operating_leverage_convexity_109'] = _z(_ema(op_lev, 504) - _ema(op_lev, 1008), 1512)
    f['f35_operating_leverage_convexity_110'] = _z(op_lev, 21)
    f['f35_operating_leverage_convexity_111'] = _z(_roc(op_lev, 63), 63)
    f['f35_operating_leverage_convexity_112'] = _z(op_lev.diff(126), 252)
    f['f35_operating_leverage_convexity_113'] = _z(op_lev / _std(op_lev, 252).replace(0, 1), 252)
    f['f35_operating_leverage_convexity_114'] = _z(_ema(op_lev, 504) - _ema(op_lev, 1008), 1512)
    f['f35_operating_leverage_convexity_115'] = _z(op_lev, 21)
    f['f35_operating_leverage_convexity_116'] = _z(_roc(op_lev, 63), 63)
    f['f35_operating_leverage_convexity_117'] = _z(op_lev.diff(126), 252)
    f['f35_operating_leverage_convexity_118'] = _z(op_lev / _std(op_lev, 252).replace(0, 1), 252)
    f['f35_operating_leverage_convexity_119'] = _z(_ema(op_lev, 504) - _ema(op_lev, 1008), 1512)
    f['f35_operating_leverage_convexity_120'] = _z(op_lev, 21)
    f['f35_operating_leverage_convexity_121'] = _z(_roc(op_lev, 63), 63)
    f['f35_operating_leverage_convexity_122'] = _z(op_lev.diff(126), 252)
    f['f35_operating_leverage_convexity_123'] = _z(op_lev / _std(op_lev, 252).replace(0, 1), 252)
    f['f35_operating_leverage_convexity_124'] = _z(_ema(op_lev, 504) - _ema(op_lev, 1008), 1512)
    f['f35_operating_leverage_convexity_125'] = _z(op_lev, 21)
    f['f35_operating_leverage_convexity_126'] = _z(_roc(op_lev, 63), 63)
    f['f35_operating_leverage_convexity_127'] = _z(op_lev.diff(126), 252)
    f['f35_operating_leverage_convexity_128'] = _z(op_lev / _std(op_lev, 252).replace(0, 1), 252)
    f['f35_operating_leverage_convexity_129'] = _z(_ema(op_lev, 504) - _ema(op_lev, 1008), 1512)
    f['f35_operating_leverage_convexity_130'] = _z(op_lev, 21)
    f['f35_operating_leverage_convexity_131'] = _z(_roc(op_lev, 63), 63)
    f['f35_operating_leverage_convexity_132'] = _z(op_lev.diff(126), 252)
    f['f35_operating_leverage_convexity_133'] = _z(op_lev / _std(op_lev, 252).replace(0, 1), 252)
    f['f35_operating_leverage_convexity_134'] = _z(_ema(op_lev, 504) - _ema(op_lev, 1008), 1512)
    f['f35_operating_leverage_convexity_135'] = _z(op_lev, 21)
    f['f35_operating_leverage_convexity_136'] = _z(_roc(op_lev, 63), 63)
    f['f35_operating_leverage_convexity_137'] = _z(op_lev.diff(126), 252)
    f['f35_operating_leverage_convexity_138'] = _z(op_lev / _std(op_lev, 252).replace(0, 1), 252)
    f['f35_operating_leverage_convexity_139'] = _z(_ema(op_lev, 504) - _ema(op_lev, 1008), 1512)
    f['f35_operating_leverage_convexity_140'] = _z(op_lev, 21)
    f['f35_operating_leverage_convexity_141'] = _z(_roc(op_lev, 63), 63)
    f['f35_operating_leverage_convexity_142'] = _z(op_lev.diff(126), 252)
    f['f35_operating_leverage_convexity_143'] = _z(op_lev / _std(op_lev, 252).replace(0, 1), 252)
    f['f35_operating_leverage_convexity_144'] = _z(_ema(op_lev, 504) - _ema(op_lev, 1008), 1512)
    f['f35_operating_leverage_convexity_145'] = _z(op_lev, 21)
    f['f35_operating_leverage_convexity_146'] = _z(_roc(op_lev, 63), 63)
    f['f35_operating_leverage_convexity_147'] = _z(op_lev.diff(126), 252)
    f['f35_operating_leverage_convexity_148'] = _z(op_lev / _std(op_lev, 252).replace(0, 1), 252)
    f['f35_operating_leverage_convexity_149'] = _z(_ema(op_lev, 504) - _ema(op_lev, 1008), 1512)
    f['f35_operating_leverage_convexity_150'] = _z(op_lev, 21)
    return pd.DataFrame(f)