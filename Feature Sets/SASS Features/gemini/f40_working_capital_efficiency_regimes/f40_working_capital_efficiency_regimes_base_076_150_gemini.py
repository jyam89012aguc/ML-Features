
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
    ca = df['assetsc']
    cl = df['liabilitiesc']
    rev = df['revenue']
    wc_eff = (ca - cl) / rev.replace(0, np.nan)
    f = {}
    f['f40_working_capital_efficiency_regimes_076'] = _z(_roc(wc_eff, 63), 63)
    f['f40_working_capital_efficiency_regimes_077'] = _z(wc_eff.diff(126), 252)
    f['f40_working_capital_efficiency_regimes_078'] = _z(wc_eff / _std(wc_eff, 252).replace(0, 1), 252)
    f['f40_working_capital_efficiency_regimes_079'] = _z(_ema(wc_eff, 504) - _ema(wc_eff, 1008), 1512)
    f['f40_working_capital_efficiency_regimes_080'] = _z(wc_eff, 21)
    f['f40_working_capital_efficiency_regimes_081'] = _z(_roc(wc_eff, 63), 63)
    f['f40_working_capital_efficiency_regimes_082'] = _z(wc_eff.diff(126), 252)
    f['f40_working_capital_efficiency_regimes_083'] = _z(wc_eff / _std(wc_eff, 252).replace(0, 1), 252)
    f['f40_working_capital_efficiency_regimes_084'] = _z(_ema(wc_eff, 504) - _ema(wc_eff, 1008), 1512)
    f['f40_working_capital_efficiency_regimes_085'] = _z(wc_eff, 21)
    f['f40_working_capital_efficiency_regimes_086'] = _z(_roc(wc_eff, 63), 63)
    f['f40_working_capital_efficiency_regimes_087'] = _z(wc_eff.diff(126), 252)
    f['f40_working_capital_efficiency_regimes_088'] = _z(wc_eff / _std(wc_eff, 252).replace(0, 1), 252)
    f['f40_working_capital_efficiency_regimes_089'] = _z(_ema(wc_eff, 504) - _ema(wc_eff, 1008), 1512)
    f['f40_working_capital_efficiency_regimes_090'] = _z(wc_eff, 21)
    f['f40_working_capital_efficiency_regimes_091'] = _z(_roc(wc_eff, 63), 63)
    f['f40_working_capital_efficiency_regimes_092'] = _z(wc_eff.diff(126), 252)
    f['f40_working_capital_efficiency_regimes_093'] = _z(wc_eff / _std(wc_eff, 252).replace(0, 1), 252)
    f['f40_working_capital_efficiency_regimes_094'] = _z(_ema(wc_eff, 504) - _ema(wc_eff, 1008), 1512)
    f['f40_working_capital_efficiency_regimes_095'] = _z(wc_eff, 21)
    f['f40_working_capital_efficiency_regimes_096'] = _z(_roc(wc_eff, 63), 63)
    f['f40_working_capital_efficiency_regimes_097'] = _z(wc_eff.diff(126), 252)
    f['f40_working_capital_efficiency_regimes_098'] = _z(wc_eff / _std(wc_eff, 252).replace(0, 1), 252)
    f['f40_working_capital_efficiency_regimes_099'] = _z(_ema(wc_eff, 504) - _ema(wc_eff, 1008), 1512)
    f['f40_working_capital_efficiency_regimes_100'] = _z(wc_eff, 21)
    f['f40_working_capital_efficiency_regimes_101'] = _z(_roc(wc_eff, 63), 63)
    f['f40_working_capital_efficiency_regimes_102'] = _z(wc_eff.diff(126), 252)
    f['f40_working_capital_efficiency_regimes_103'] = _z(wc_eff / _std(wc_eff, 252).replace(0, 1), 252)
    f['f40_working_capital_efficiency_regimes_104'] = _z(_ema(wc_eff, 504) - _ema(wc_eff, 1008), 1512)
    f['f40_working_capital_efficiency_regimes_105'] = _z(wc_eff, 21)
    f['f40_working_capital_efficiency_regimes_106'] = _z(_roc(wc_eff, 63), 63)
    f['f40_working_capital_efficiency_regimes_107'] = _z(wc_eff.diff(126), 252)
    f['f40_working_capital_efficiency_regimes_108'] = _z(wc_eff / _std(wc_eff, 252).replace(0, 1), 252)
    f['f40_working_capital_efficiency_regimes_109'] = _z(_ema(wc_eff, 504) - _ema(wc_eff, 1008), 1512)
    f['f40_working_capital_efficiency_regimes_110'] = _z(wc_eff, 21)
    f['f40_working_capital_efficiency_regimes_111'] = _z(_roc(wc_eff, 63), 63)
    f['f40_working_capital_efficiency_regimes_112'] = _z(wc_eff.diff(126), 252)
    f['f40_working_capital_efficiency_regimes_113'] = _z(wc_eff / _std(wc_eff, 252).replace(0, 1), 252)
    f['f40_working_capital_efficiency_regimes_114'] = _z(_ema(wc_eff, 504) - _ema(wc_eff, 1008), 1512)
    f['f40_working_capital_efficiency_regimes_115'] = _z(wc_eff, 21)
    f['f40_working_capital_efficiency_regimes_116'] = _z(_roc(wc_eff, 63), 63)
    f['f40_working_capital_efficiency_regimes_117'] = _z(wc_eff.diff(126), 252)
    f['f40_working_capital_efficiency_regimes_118'] = _z(wc_eff / _std(wc_eff, 252).replace(0, 1), 252)
    f['f40_working_capital_efficiency_regimes_119'] = _z(_ema(wc_eff, 504) - _ema(wc_eff, 1008), 1512)
    f['f40_working_capital_efficiency_regimes_120'] = _z(wc_eff, 21)
    f['f40_working_capital_efficiency_regimes_121'] = _z(_roc(wc_eff, 63), 63)
    f['f40_working_capital_efficiency_regimes_122'] = _z(wc_eff.diff(126), 252)
    f['f40_working_capital_efficiency_regimes_123'] = _z(wc_eff / _std(wc_eff, 252).replace(0, 1), 252)
    f['f40_working_capital_efficiency_regimes_124'] = _z(_ema(wc_eff, 504) - _ema(wc_eff, 1008), 1512)
    f['f40_working_capital_efficiency_regimes_125'] = _z(wc_eff, 21)
    f['f40_working_capital_efficiency_regimes_126'] = _z(_roc(wc_eff, 63), 63)
    f['f40_working_capital_efficiency_regimes_127'] = _z(wc_eff.diff(126), 252)
    f['f40_working_capital_efficiency_regimes_128'] = _z(wc_eff / _std(wc_eff, 252).replace(0, 1), 252)
    f['f40_working_capital_efficiency_regimes_129'] = _z(_ema(wc_eff, 504) - _ema(wc_eff, 1008), 1512)
    f['f40_working_capital_efficiency_regimes_130'] = _z(wc_eff, 21)
    f['f40_working_capital_efficiency_regimes_131'] = _z(_roc(wc_eff, 63), 63)
    f['f40_working_capital_efficiency_regimes_132'] = _z(wc_eff.diff(126), 252)
    f['f40_working_capital_efficiency_regimes_133'] = _z(wc_eff / _std(wc_eff, 252).replace(0, 1), 252)
    f['f40_working_capital_efficiency_regimes_134'] = _z(_ema(wc_eff, 504) - _ema(wc_eff, 1008), 1512)
    f['f40_working_capital_efficiency_regimes_135'] = _z(wc_eff, 21)
    f['f40_working_capital_efficiency_regimes_136'] = _z(_roc(wc_eff, 63), 63)
    f['f40_working_capital_efficiency_regimes_137'] = _z(wc_eff.diff(126), 252)
    f['f40_working_capital_efficiency_regimes_138'] = _z(wc_eff / _std(wc_eff, 252).replace(0, 1), 252)
    f['f40_working_capital_efficiency_regimes_139'] = _z(_ema(wc_eff, 504) - _ema(wc_eff, 1008), 1512)
    f['f40_working_capital_efficiency_regimes_140'] = _z(wc_eff, 21)
    f['f40_working_capital_efficiency_regimes_141'] = _z(_roc(wc_eff, 63), 63)
    f['f40_working_capital_efficiency_regimes_142'] = _z(wc_eff.diff(126), 252)
    f['f40_working_capital_efficiency_regimes_143'] = _z(wc_eff / _std(wc_eff, 252).replace(0, 1), 252)
    f['f40_working_capital_efficiency_regimes_144'] = _z(_ema(wc_eff, 504) - _ema(wc_eff, 1008), 1512)
    f['f40_working_capital_efficiency_regimes_145'] = _z(wc_eff, 21)
    f['f40_working_capital_efficiency_regimes_146'] = _z(_roc(wc_eff, 63), 63)
    f['f40_working_capital_efficiency_regimes_147'] = _z(wc_eff.diff(126), 252)
    f['f40_working_capital_efficiency_regimes_148'] = _z(wc_eff / _std(wc_eff, 252).replace(0, 1), 252)
    f['f40_working_capital_efficiency_regimes_149'] = _z(_ema(wc_eff, 504) - _ema(wc_eff, 1008), 1512)
    f['f40_working_capital_efficiency_regimes_150'] = _z(wc_eff, 21)
    return pd.DataFrame(f)