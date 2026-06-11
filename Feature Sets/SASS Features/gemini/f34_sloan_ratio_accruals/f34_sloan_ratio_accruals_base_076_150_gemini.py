
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
    ocf = df['ncfo']
    at = df['assets']
    sloan = (ni - ocf) / at
    f = {}
    f['f34_sloan_ratio_accruals_076'] = _z(_roc(sloan, 63), 63)
    f['f34_sloan_ratio_accruals_077'] = _z(sloan.diff(126), 252)
    f['f34_sloan_ratio_accruals_078'] = _z(sloan / _std(sloan, 252).replace(0, 1), 252)
    f['f34_sloan_ratio_accruals_079'] = _z(_ema(sloan, 504) - _ema(sloan, 1008), 1512)
    f['f34_sloan_ratio_accruals_080'] = _z(sloan, 21)
    f['f34_sloan_ratio_accruals_081'] = _z(_roc(sloan, 63), 63)
    f['f34_sloan_ratio_accruals_082'] = _z(sloan.diff(126), 252)
    f['f34_sloan_ratio_accruals_083'] = _z(sloan / _std(sloan, 252).replace(0, 1), 252)
    f['f34_sloan_ratio_accruals_084'] = _z(_ema(sloan, 504) - _ema(sloan, 1008), 1512)
    f['f34_sloan_ratio_accruals_085'] = _z(sloan, 21)
    f['f34_sloan_ratio_accruals_086'] = _z(_roc(sloan, 63), 63)
    f['f34_sloan_ratio_accruals_087'] = _z(sloan.diff(126), 252)
    f['f34_sloan_ratio_accruals_088'] = _z(sloan / _std(sloan, 252).replace(0, 1), 252)
    f['f34_sloan_ratio_accruals_089'] = _z(_ema(sloan, 504) - _ema(sloan, 1008), 1512)
    f['f34_sloan_ratio_accruals_090'] = _z(sloan, 21)
    f['f34_sloan_ratio_accruals_091'] = _z(_roc(sloan, 63), 63)
    f['f34_sloan_ratio_accruals_092'] = _z(sloan.diff(126), 252)
    f['f34_sloan_ratio_accruals_093'] = _z(sloan / _std(sloan, 252).replace(0, 1), 252)
    f['f34_sloan_ratio_accruals_094'] = _z(_ema(sloan, 504) - _ema(sloan, 1008), 1512)
    f['f34_sloan_ratio_accruals_095'] = _z(sloan, 21)
    f['f34_sloan_ratio_accruals_096'] = _z(_roc(sloan, 63), 63)
    f['f34_sloan_ratio_accruals_097'] = _z(sloan.diff(126), 252)
    f['f34_sloan_ratio_accruals_098'] = _z(sloan / _std(sloan, 252).replace(0, 1), 252)
    f['f34_sloan_ratio_accruals_099'] = _z(_ema(sloan, 504) - _ema(sloan, 1008), 1512)
    f['f34_sloan_ratio_accruals_100'] = _z(sloan, 21)
    f['f34_sloan_ratio_accruals_101'] = _z(_roc(sloan, 63), 63)
    f['f34_sloan_ratio_accruals_102'] = _z(sloan.diff(126), 252)
    f['f34_sloan_ratio_accruals_103'] = _z(sloan / _std(sloan, 252).replace(0, 1), 252)
    f['f34_sloan_ratio_accruals_104'] = _z(_ema(sloan, 504) - _ema(sloan, 1008), 1512)
    f['f34_sloan_ratio_accruals_105'] = _z(sloan, 21)
    f['f34_sloan_ratio_accruals_106'] = _z(_roc(sloan, 63), 63)
    f['f34_sloan_ratio_accruals_107'] = _z(sloan.diff(126), 252)
    f['f34_sloan_ratio_accruals_108'] = _z(sloan / _std(sloan, 252).replace(0, 1), 252)
    f['f34_sloan_ratio_accruals_109'] = _z(_ema(sloan, 504) - _ema(sloan, 1008), 1512)
    f['f34_sloan_ratio_accruals_110'] = _z(sloan, 21)
    f['f34_sloan_ratio_accruals_111'] = _z(_roc(sloan, 63), 63)
    f['f34_sloan_ratio_accruals_112'] = _z(sloan.diff(126), 252)
    f['f34_sloan_ratio_accruals_113'] = _z(sloan / _std(sloan, 252).replace(0, 1), 252)
    f['f34_sloan_ratio_accruals_114'] = _z(_ema(sloan, 504) - _ema(sloan, 1008), 1512)
    f['f34_sloan_ratio_accruals_115'] = _z(sloan, 21)
    f['f34_sloan_ratio_accruals_116'] = _z(_roc(sloan, 63), 63)
    f['f34_sloan_ratio_accruals_117'] = _z(sloan.diff(126), 252)
    f['f34_sloan_ratio_accruals_118'] = _z(sloan / _std(sloan, 252).replace(0, 1), 252)
    f['f34_sloan_ratio_accruals_119'] = _z(_ema(sloan, 504) - _ema(sloan, 1008), 1512)
    f['f34_sloan_ratio_accruals_120'] = _z(sloan, 21)
    f['f34_sloan_ratio_accruals_121'] = _z(_roc(sloan, 63), 63)
    f['f34_sloan_ratio_accruals_122'] = _z(sloan.diff(126), 252)
    f['f34_sloan_ratio_accruals_123'] = _z(sloan / _std(sloan, 252).replace(0, 1), 252)
    f['f34_sloan_ratio_accruals_124'] = _z(_ema(sloan, 504) - _ema(sloan, 1008), 1512)
    f['f34_sloan_ratio_accruals_125'] = _z(sloan, 21)
    f['f34_sloan_ratio_accruals_126'] = _z(_roc(sloan, 63), 63)
    f['f34_sloan_ratio_accruals_127'] = _z(sloan.diff(126), 252)
    f['f34_sloan_ratio_accruals_128'] = _z(sloan / _std(sloan, 252).replace(0, 1), 252)
    f['f34_sloan_ratio_accruals_129'] = _z(_ema(sloan, 504) - _ema(sloan, 1008), 1512)
    f['f34_sloan_ratio_accruals_130'] = _z(sloan, 21)
    f['f34_sloan_ratio_accruals_131'] = _z(_roc(sloan, 63), 63)
    f['f34_sloan_ratio_accruals_132'] = _z(sloan.diff(126), 252)
    f['f34_sloan_ratio_accruals_133'] = _z(sloan / _std(sloan, 252).replace(0, 1), 252)
    f['f34_sloan_ratio_accruals_134'] = _z(_ema(sloan, 504) - _ema(sloan, 1008), 1512)
    f['f34_sloan_ratio_accruals_135'] = _z(sloan, 21)
    f['f34_sloan_ratio_accruals_136'] = _z(_roc(sloan, 63), 63)
    f['f34_sloan_ratio_accruals_137'] = _z(sloan.diff(126), 252)
    f['f34_sloan_ratio_accruals_138'] = _z(sloan / _std(sloan, 252).replace(0, 1), 252)
    f['f34_sloan_ratio_accruals_139'] = _z(_ema(sloan, 504) - _ema(sloan, 1008), 1512)
    f['f34_sloan_ratio_accruals_140'] = _z(sloan, 21)
    f['f34_sloan_ratio_accruals_141'] = _z(_roc(sloan, 63), 63)
    f['f34_sloan_ratio_accruals_142'] = _z(sloan.diff(126), 252)
    f['f34_sloan_ratio_accruals_143'] = _z(sloan / _std(sloan, 252).replace(0, 1), 252)
    f['f34_sloan_ratio_accruals_144'] = _z(_ema(sloan, 504) - _ema(sloan, 1008), 1512)
    f['f34_sloan_ratio_accruals_145'] = _z(sloan, 21)
    f['f34_sloan_ratio_accruals_146'] = _z(_roc(sloan, 63), 63)
    f['f34_sloan_ratio_accruals_147'] = _z(sloan.diff(126), 252)
    f['f34_sloan_ratio_accruals_148'] = _z(sloan / _std(sloan, 252).replace(0, 1), 252)
    f['f34_sloan_ratio_accruals_149'] = _z(_ema(sloan, 504) - _ema(sloan, 1008), 1512)
    f['f34_sloan_ratio_accruals_150'] = _z(sloan, 21)
    return pd.DataFrame(f)