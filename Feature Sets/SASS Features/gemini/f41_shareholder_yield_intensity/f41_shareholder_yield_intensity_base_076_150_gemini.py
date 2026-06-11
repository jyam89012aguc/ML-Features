
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
    div = df['ncfdiv']
    buyback = df['ncfcommon']
    debt_red = df['ncfdebt']
    market_cap = df['marketcap']
    sh_yield = (div + buyback + debt_red) / market_cap.replace(0, np.nan)
    f = {}
    f['f41_shareholder_yield_intensity_076'] = _z(_roc(sh_yield, 63), 63)
    f['f41_shareholder_yield_intensity_077'] = _z(sh_yield.diff(126), 252)
    f['f41_shareholder_yield_intensity_078'] = _z(sh_yield / _std(sh_yield, 252).replace(0, 1), 252)
    f['f41_shareholder_yield_intensity_079'] = _z(_ema(sh_yield, 504) - _ema(sh_yield, 1008), 1512)
    f['f41_shareholder_yield_intensity_080'] = _z(sh_yield, 21)
    f['f41_shareholder_yield_intensity_081'] = _z(_roc(sh_yield, 63), 63)
    f['f41_shareholder_yield_intensity_082'] = _z(sh_yield.diff(126), 252)
    f['f41_shareholder_yield_intensity_083'] = _z(sh_yield / _std(sh_yield, 252).replace(0, 1), 252)
    f['f41_shareholder_yield_intensity_084'] = _z(_ema(sh_yield, 504) - _ema(sh_yield, 1008), 1512)
    f['f41_shareholder_yield_intensity_085'] = _z(sh_yield, 21)
    f['f41_shareholder_yield_intensity_086'] = _z(_roc(sh_yield, 63), 63)
    f['f41_shareholder_yield_intensity_087'] = _z(sh_yield.diff(126), 252)
    f['f41_shareholder_yield_intensity_088'] = _z(sh_yield / _std(sh_yield, 252).replace(0, 1), 252)
    f['f41_shareholder_yield_intensity_089'] = _z(_ema(sh_yield, 504) - _ema(sh_yield, 1008), 1512)
    f['f41_shareholder_yield_intensity_090'] = _z(sh_yield, 21)
    f['f41_shareholder_yield_intensity_091'] = _z(_roc(sh_yield, 63), 63)
    f['f41_shareholder_yield_intensity_092'] = _z(sh_yield.diff(126), 252)
    f['f41_shareholder_yield_intensity_093'] = _z(sh_yield / _std(sh_yield, 252).replace(0, 1), 252)
    f['f41_shareholder_yield_intensity_094'] = _z(_ema(sh_yield, 504) - _ema(sh_yield, 1008), 1512)
    f['f41_shareholder_yield_intensity_095'] = _z(sh_yield, 21)
    f['f41_shareholder_yield_intensity_096'] = _z(_roc(sh_yield, 63), 63)
    f['f41_shareholder_yield_intensity_097'] = _z(sh_yield.diff(126), 252)
    f['f41_shareholder_yield_intensity_098'] = _z(sh_yield / _std(sh_yield, 252).replace(0, 1), 252)
    f['f41_shareholder_yield_intensity_099'] = _z(_ema(sh_yield, 504) - _ema(sh_yield, 1008), 1512)
    f['f41_shareholder_yield_intensity_100'] = _z(sh_yield, 21)
    f['f41_shareholder_yield_intensity_101'] = _z(_roc(sh_yield, 63), 63)
    f['f41_shareholder_yield_intensity_102'] = _z(sh_yield.diff(126), 252)
    f['f41_shareholder_yield_intensity_103'] = _z(sh_yield / _std(sh_yield, 252).replace(0, 1), 252)
    f['f41_shareholder_yield_intensity_104'] = _z(_ema(sh_yield, 504) - _ema(sh_yield, 1008), 1512)
    f['f41_shareholder_yield_intensity_105'] = _z(sh_yield, 21)
    f['f41_shareholder_yield_intensity_106'] = _z(_roc(sh_yield, 63), 63)
    f['f41_shareholder_yield_intensity_107'] = _z(sh_yield.diff(126), 252)
    f['f41_shareholder_yield_intensity_108'] = _z(sh_yield / _std(sh_yield, 252).replace(0, 1), 252)
    f['f41_shareholder_yield_intensity_109'] = _z(_ema(sh_yield, 504) - _ema(sh_yield, 1008), 1512)
    f['f41_shareholder_yield_intensity_110'] = _z(sh_yield, 21)
    f['f41_shareholder_yield_intensity_111'] = _z(_roc(sh_yield, 63), 63)
    f['f41_shareholder_yield_intensity_112'] = _z(sh_yield.diff(126), 252)
    f['f41_shareholder_yield_intensity_113'] = _z(sh_yield / _std(sh_yield, 252).replace(0, 1), 252)
    f['f41_shareholder_yield_intensity_114'] = _z(_ema(sh_yield, 504) - _ema(sh_yield, 1008), 1512)
    f['f41_shareholder_yield_intensity_115'] = _z(sh_yield, 21)
    f['f41_shareholder_yield_intensity_116'] = _z(_roc(sh_yield, 63), 63)
    f['f41_shareholder_yield_intensity_117'] = _z(sh_yield.diff(126), 252)
    f['f41_shareholder_yield_intensity_118'] = _z(sh_yield / _std(sh_yield, 252).replace(0, 1), 252)
    f['f41_shareholder_yield_intensity_119'] = _z(_ema(sh_yield, 504) - _ema(sh_yield, 1008), 1512)
    f['f41_shareholder_yield_intensity_120'] = _z(sh_yield, 21)
    f['f41_shareholder_yield_intensity_121'] = _z(_roc(sh_yield, 63), 63)
    f['f41_shareholder_yield_intensity_122'] = _z(sh_yield.diff(126), 252)
    f['f41_shareholder_yield_intensity_123'] = _z(sh_yield / _std(sh_yield, 252).replace(0, 1), 252)
    f['f41_shareholder_yield_intensity_124'] = _z(_ema(sh_yield, 504) - _ema(sh_yield, 1008), 1512)
    f['f41_shareholder_yield_intensity_125'] = _z(sh_yield, 21)
    f['f41_shareholder_yield_intensity_126'] = _z(_roc(sh_yield, 63), 63)
    f['f41_shareholder_yield_intensity_127'] = _z(sh_yield.diff(126), 252)
    f['f41_shareholder_yield_intensity_128'] = _z(sh_yield / _std(sh_yield, 252).replace(0, 1), 252)
    f['f41_shareholder_yield_intensity_129'] = _z(_ema(sh_yield, 504) - _ema(sh_yield, 1008), 1512)
    f['f41_shareholder_yield_intensity_130'] = _z(sh_yield, 21)
    f['f41_shareholder_yield_intensity_131'] = _z(_roc(sh_yield, 63), 63)
    f['f41_shareholder_yield_intensity_132'] = _z(sh_yield.diff(126), 252)
    f['f41_shareholder_yield_intensity_133'] = _z(sh_yield / _std(sh_yield, 252).replace(0, 1), 252)
    f['f41_shareholder_yield_intensity_134'] = _z(_ema(sh_yield, 504) - _ema(sh_yield, 1008), 1512)
    f['f41_shareholder_yield_intensity_135'] = _z(sh_yield, 21)
    f['f41_shareholder_yield_intensity_136'] = _z(_roc(sh_yield, 63), 63)
    f['f41_shareholder_yield_intensity_137'] = _z(sh_yield.diff(126), 252)
    f['f41_shareholder_yield_intensity_138'] = _z(sh_yield / _std(sh_yield, 252).replace(0, 1), 252)
    f['f41_shareholder_yield_intensity_139'] = _z(_ema(sh_yield, 504) - _ema(sh_yield, 1008), 1512)
    f['f41_shareholder_yield_intensity_140'] = _z(sh_yield, 21)
    f['f41_shareholder_yield_intensity_141'] = _z(_roc(sh_yield, 63), 63)
    f['f41_shareholder_yield_intensity_142'] = _z(sh_yield.diff(126), 252)
    f['f41_shareholder_yield_intensity_143'] = _z(sh_yield / _std(sh_yield, 252).replace(0, 1), 252)
    f['f41_shareholder_yield_intensity_144'] = _z(_ema(sh_yield, 504) - _ema(sh_yield, 1008), 1512)
    f['f41_shareholder_yield_intensity_145'] = _z(sh_yield, 21)
    f['f41_shareholder_yield_intensity_146'] = _z(_roc(sh_yield, 63), 63)
    f['f41_shareholder_yield_intensity_147'] = _z(sh_yield.diff(126), 252)
    f['f41_shareholder_yield_intensity_148'] = _z(sh_yield / _std(sh_yield, 252).replace(0, 1), 252)
    f['f41_shareholder_yield_intensity_149'] = _z(_ema(sh_yield, 504) - _ema(sh_yield, 1008), 1512)
    f['f41_shareholder_yield_intensity_150'] = _z(sh_yield, 21)
    return pd.DataFrame(f)