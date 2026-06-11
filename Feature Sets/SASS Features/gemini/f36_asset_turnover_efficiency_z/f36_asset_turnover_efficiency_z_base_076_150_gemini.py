
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
    rev = df['revenue']
    at = df['assets']
    aturn = rev / at
    f = {}
    f['f36_asset_turnover_efficiency_z_076'] = _z(_roc(aturn, 63), 63)
    f['f36_asset_turnover_efficiency_z_077'] = _z(aturn.diff(126), 252)
    f['f36_asset_turnover_efficiency_z_078'] = _z(aturn / _std(aturn, 252).replace(0, 1), 252)
    f['f36_asset_turnover_efficiency_z_079'] = _z(_ema(aturn, 504) - _ema(aturn, 1008), 1512)
    f['f36_asset_turnover_efficiency_z_080'] = _z(aturn, 21)
    f['f36_asset_turnover_efficiency_z_081'] = _z(_roc(aturn, 63), 63)
    f['f36_asset_turnover_efficiency_z_082'] = _z(aturn.diff(126), 252)
    f['f36_asset_turnover_efficiency_z_083'] = _z(aturn / _std(aturn, 252).replace(0, 1), 252)
    f['f36_asset_turnover_efficiency_z_084'] = _z(_ema(aturn, 504) - _ema(aturn, 1008), 1512)
    f['f36_asset_turnover_efficiency_z_085'] = _z(aturn, 21)
    f['f36_asset_turnover_efficiency_z_086'] = _z(_roc(aturn, 63), 63)
    f['f36_asset_turnover_efficiency_z_087'] = _z(aturn.diff(126), 252)
    f['f36_asset_turnover_efficiency_z_088'] = _z(aturn / _std(aturn, 252).replace(0, 1), 252)
    f['f36_asset_turnover_efficiency_z_089'] = _z(_ema(aturn, 504) - _ema(aturn, 1008), 1512)
    f['f36_asset_turnover_efficiency_z_090'] = _z(aturn, 21)
    f['f36_asset_turnover_efficiency_z_091'] = _z(_roc(aturn, 63), 63)
    f['f36_asset_turnover_efficiency_z_092'] = _z(aturn.diff(126), 252)
    f['f36_asset_turnover_efficiency_z_093'] = _z(aturn / _std(aturn, 252).replace(0, 1), 252)
    f['f36_asset_turnover_efficiency_z_094'] = _z(_ema(aturn, 504) - _ema(aturn, 1008), 1512)
    f['f36_asset_turnover_efficiency_z_095'] = _z(aturn, 21)
    f['f36_asset_turnover_efficiency_z_096'] = _z(_roc(aturn, 63), 63)
    f['f36_asset_turnover_efficiency_z_097'] = _z(aturn.diff(126), 252)
    f['f36_asset_turnover_efficiency_z_098'] = _z(aturn / _std(aturn, 252).replace(0, 1), 252)
    f['f36_asset_turnover_efficiency_z_099'] = _z(_ema(aturn, 504) - _ema(aturn, 1008), 1512)
    f['f36_asset_turnover_efficiency_z_100'] = _z(aturn, 21)
    f['f36_asset_turnover_efficiency_z_101'] = _z(_roc(aturn, 63), 63)
    f['f36_asset_turnover_efficiency_z_102'] = _z(aturn.diff(126), 252)
    f['f36_asset_turnover_efficiency_z_103'] = _z(aturn / _std(aturn, 252).replace(0, 1), 252)
    f['f36_asset_turnover_efficiency_z_104'] = _z(_ema(aturn, 504) - _ema(aturn, 1008), 1512)
    f['f36_asset_turnover_efficiency_z_105'] = _z(aturn, 21)
    f['f36_asset_turnover_efficiency_z_106'] = _z(_roc(aturn, 63), 63)
    f['f36_asset_turnover_efficiency_z_107'] = _z(aturn.diff(126), 252)
    f['f36_asset_turnover_efficiency_z_108'] = _z(aturn / _std(aturn, 252).replace(0, 1), 252)
    f['f36_asset_turnover_efficiency_z_109'] = _z(_ema(aturn, 504) - _ema(aturn, 1008), 1512)
    f['f36_asset_turnover_efficiency_z_110'] = _z(aturn, 21)
    f['f36_asset_turnover_efficiency_z_111'] = _z(_roc(aturn, 63), 63)
    f['f36_asset_turnover_efficiency_z_112'] = _z(aturn.diff(126), 252)
    f['f36_asset_turnover_efficiency_z_113'] = _z(aturn / _std(aturn, 252).replace(0, 1), 252)
    f['f36_asset_turnover_efficiency_z_114'] = _z(_ema(aturn, 504) - _ema(aturn, 1008), 1512)
    f['f36_asset_turnover_efficiency_z_115'] = _z(aturn, 21)
    f['f36_asset_turnover_efficiency_z_116'] = _z(_roc(aturn, 63), 63)
    f['f36_asset_turnover_efficiency_z_117'] = _z(aturn.diff(126), 252)
    f['f36_asset_turnover_efficiency_z_118'] = _z(aturn / _std(aturn, 252).replace(0, 1), 252)
    f['f36_asset_turnover_efficiency_z_119'] = _z(_ema(aturn, 504) - _ema(aturn, 1008), 1512)
    f['f36_asset_turnover_efficiency_z_120'] = _z(aturn, 21)
    f['f36_asset_turnover_efficiency_z_121'] = _z(_roc(aturn, 63), 63)
    f['f36_asset_turnover_efficiency_z_122'] = _z(aturn.diff(126), 252)
    f['f36_asset_turnover_efficiency_z_123'] = _z(aturn / _std(aturn, 252).replace(0, 1), 252)
    f['f36_asset_turnover_efficiency_z_124'] = _z(_ema(aturn, 504) - _ema(aturn, 1008), 1512)
    f['f36_asset_turnover_efficiency_z_125'] = _z(aturn, 21)
    f['f36_asset_turnover_efficiency_z_126'] = _z(_roc(aturn, 63), 63)
    f['f36_asset_turnover_efficiency_z_127'] = _z(aturn.diff(126), 252)
    f['f36_asset_turnover_efficiency_z_128'] = _z(aturn / _std(aturn, 252).replace(0, 1), 252)
    f['f36_asset_turnover_efficiency_z_129'] = _z(_ema(aturn, 504) - _ema(aturn, 1008), 1512)
    f['f36_asset_turnover_efficiency_z_130'] = _z(aturn, 21)
    f['f36_asset_turnover_efficiency_z_131'] = _z(_roc(aturn, 63), 63)
    f['f36_asset_turnover_efficiency_z_132'] = _z(aturn.diff(126), 252)
    f['f36_asset_turnover_efficiency_z_133'] = _z(aturn / _std(aturn, 252).replace(0, 1), 252)
    f['f36_asset_turnover_efficiency_z_134'] = _z(_ema(aturn, 504) - _ema(aturn, 1008), 1512)
    f['f36_asset_turnover_efficiency_z_135'] = _z(aturn, 21)
    f['f36_asset_turnover_efficiency_z_136'] = _z(_roc(aturn, 63), 63)
    f['f36_asset_turnover_efficiency_z_137'] = _z(aturn.diff(126), 252)
    f['f36_asset_turnover_efficiency_z_138'] = _z(aturn / _std(aturn, 252).replace(0, 1), 252)
    f['f36_asset_turnover_efficiency_z_139'] = _z(_ema(aturn, 504) - _ema(aturn, 1008), 1512)
    f['f36_asset_turnover_efficiency_z_140'] = _z(aturn, 21)
    f['f36_asset_turnover_efficiency_z_141'] = _z(_roc(aturn, 63), 63)
    f['f36_asset_turnover_efficiency_z_142'] = _z(aturn.diff(126), 252)
    f['f36_asset_turnover_efficiency_z_143'] = _z(aturn / _std(aturn, 252).replace(0, 1), 252)
    f['f36_asset_turnover_efficiency_z_144'] = _z(_ema(aturn, 504) - _ema(aturn, 1008), 1512)
    f['f36_asset_turnover_efficiency_z_145'] = _z(aturn, 21)
    f['f36_asset_turnover_efficiency_z_146'] = _z(_roc(aturn, 63), 63)
    f['f36_asset_turnover_efficiency_z_147'] = _z(aturn.diff(126), 252)
    f['f36_asset_turnover_efficiency_z_148'] = _z(aturn / _std(aturn, 252).replace(0, 1), 252)
    f['f36_asset_turnover_efficiency_z_149'] = _z(_ema(aturn, 504) - _ema(aturn, 1008), 1512)
    f['f36_asset_turnover_efficiency_z_150'] = _z(aturn, 21)
    return pd.DataFrame(f)