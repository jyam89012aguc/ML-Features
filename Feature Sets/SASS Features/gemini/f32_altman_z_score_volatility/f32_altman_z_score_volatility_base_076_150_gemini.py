
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
    at = df['assets']
    wc = df['workingcapital']
    re = df['retearn']
    ebit = df['ebit']
    market_cap = df['marketcap']
    tl = df['liabilities']
    rev = df['revenue']
    a = wc / at
    b = re / at
    c = ebit / at
    d = market_cap / tl
    e = rev / at
    z = 1.2*a + 1.4*b + 3.3*c + 0.6*d + 1.0*e
    f = {}
    f['f32_altman_z_score_volatility_076'] = _z(_roc(z, 126), 126)
    f['f32_altman_z_score_volatility_077'] = _z(a.diff(126), 252)
    f['f32_altman_z_score_volatility_078'] = _z(b / _std(b, 252).replace(0, 1), 252)
    f['f32_altman_z_score_volatility_079'] = _z(_ema(c, 252) - _ema(c, 504), 756)
    f['f32_altman_z_score_volatility_080'] = _z(d, 252)
    f['f32_altman_z_score_volatility_081'] = _z(_roc(e, 252), 252)
    f['f32_altman_z_score_volatility_082'] = _z(z.diff(252), 504)
    f['f32_altman_z_score_volatility_083'] = _z(a / _std(a, 252).replace(0, 1), 252)
    f['f32_altman_z_score_volatility_084'] = _z(_ema(b, 504) - _ema(b, 1008), 1512)
    f['f32_altman_z_score_volatility_085'] = _z(c, 504)
    f['f32_altman_z_score_volatility_086'] = _z(_roc(d, 504), 504)
    f['f32_altman_z_score_volatility_087'] = _z(e.diff(504), 1008)
    f['f32_altman_z_score_volatility_088'] = _z(z / _std(z, 504).replace(0, 1), 504)
    f['f32_altman_z_score_volatility_089'] = _z(_ema(a, 504) - _ema(a, 1008), 1512)
    f['f32_altman_z_score_volatility_090'] = _z(b, 21)
    f['f32_altman_z_score_volatility_091'] = _z(_roc(c, 21), 21)
    f['f32_altman_z_score_volatility_092'] = _z(d.diff(21), 42)
    f['f32_altman_z_score_volatility_093'] = _z(e / _std(e, 21).replace(0, 1), 21)
    f['f32_altman_z_score_volatility_094'] = _z(_ema(z, 21) - _ema(z, 42), 63)
    f['f32_altman_z_score_volatility_095'] = _z(a, 21)
    f['f32_altman_z_score_volatility_096'] = _z(_roc(b, 63), 63)
    f['f32_altman_z_score_volatility_097'] = _z(c.diff(63), 126)
    f['f32_altman_z_score_volatility_098'] = _z(d / _std(d, 63).replace(0, 1), 63)
    f['f32_altman_z_score_volatility_099'] = _z(_ema(e, 63) - _ema(e, 126), 189)
    f['f32_altman_z_score_volatility_100'] = _z(z, 63)
    f['f32_altman_z_score_volatility_101'] = _z(_roc(a, 63), 63)
    f['f32_altman_z_score_volatility_102'] = _z(b.diff(126), 252)
    f['f32_altman_z_score_volatility_103'] = _z(c / _std(c, 126).replace(0, 1), 126)
    f['f32_altman_z_score_volatility_104'] = _z(_ema(d, 126) - _ema(d, 252), 378)
    f['f32_altman_z_score_volatility_105'] = _z(e, 126)
    f['f32_altman_z_score_volatility_106'] = _z(_roc(z, 126), 126)
    f['f32_altman_z_score_volatility_107'] = _z(a.diff(126), 252)
    f['f32_altman_z_score_volatility_108'] = _z(b / _std(b, 252).replace(0, 1), 252)
    f['f32_altman_z_score_volatility_109'] = _z(_ema(c, 252) - _ema(c, 504), 756)
    f['f32_altman_z_score_volatility_110'] = _z(d, 252)
    f['f32_altman_z_score_volatility_111'] = _z(_roc(e, 252), 252)
    f['f32_altman_z_score_volatility_112'] = _z(z.diff(252), 504)
    f['f32_altman_z_score_volatility_113'] = _z(a / _std(a, 252).replace(0, 1), 252)
    f['f32_altman_z_score_volatility_114'] = _z(_ema(b, 504) - _ema(b, 1008), 1512)
    f['f32_altman_z_score_volatility_115'] = _z(c, 504)
    f['f32_altman_z_score_volatility_116'] = _z(_roc(d, 504), 504)
    f['f32_altman_z_score_volatility_117'] = _z(e.diff(504), 1008)
    f['f32_altman_z_score_volatility_118'] = _z(z / _std(z, 504).replace(0, 1), 504)
    f['f32_altman_z_score_volatility_119'] = _z(_ema(a, 504) - _ema(a, 1008), 1512)
    f['f32_altman_z_score_volatility_120'] = _z(b, 21)
    f['f32_altman_z_score_volatility_121'] = _z(_roc(c, 21), 21)
    f['f32_altman_z_score_volatility_122'] = _z(d.diff(21), 42)
    f['f32_altman_z_score_volatility_123'] = _z(e / _std(e, 21).replace(0, 1), 21)
    f['f32_altman_z_score_volatility_124'] = _z(_ema(z, 21) - _ema(z, 42), 63)
    f['f32_altman_z_score_volatility_125'] = _z(a, 21)
    f['f32_altman_z_score_volatility_126'] = _z(_roc(b, 63), 63)
    f['f32_altman_z_score_volatility_127'] = _z(c.diff(63), 126)
    f['f32_altman_z_score_volatility_128'] = _z(d / _std(d, 63).replace(0, 1), 63)
    f['f32_altman_z_score_volatility_129'] = _z(_ema(e, 63) - _ema(e, 126), 189)
    f['f32_altman_z_score_volatility_130'] = _z(z, 63)
    f['f32_altman_z_score_volatility_131'] = _z(_roc(a, 63), 63)
    f['f32_altman_z_score_volatility_132'] = _z(b.diff(126), 252)
    f['f32_altman_z_score_volatility_133'] = _z(c / _std(c, 126).replace(0, 1), 126)
    f['f32_altman_z_score_volatility_134'] = _z(_ema(d, 126) - _ema(d, 252), 378)
    f['f32_altman_z_score_volatility_135'] = _z(e, 126)
    f['f32_altman_z_score_volatility_136'] = _z(_roc(z, 126), 126)
    f['f32_altman_z_score_volatility_137'] = _z(a.diff(126), 252)
    f['f32_altman_z_score_volatility_138'] = _z(b / _std(b, 252).replace(0, 1), 252)
    f['f32_altman_z_score_volatility_139'] = _z(_ema(c, 252) - _ema(c, 504), 756)
    f['f32_altman_z_score_volatility_140'] = _z(d, 252)
    f['f32_altman_z_score_volatility_141'] = _z(_roc(e, 252), 252)
    f['f32_altman_z_score_volatility_142'] = _z(z.diff(252), 504)
    f['f32_altman_z_score_volatility_143'] = _z(a / _std(a, 252).replace(0, 1), 252)
    f['f32_altman_z_score_volatility_144'] = _z(_ema(b, 504) - _ema(b, 1008), 1512)
    f['f32_altman_z_score_volatility_145'] = _z(c, 504)
    f['f32_altman_z_score_volatility_146'] = _z(_roc(d, 504), 504)
    f['f32_altman_z_score_volatility_147'] = _z(e.diff(504), 1008)
    f['f32_altman_z_score_volatility_148'] = _z(z / _std(z, 504).replace(0, 1), 504)
    f['f32_altman_z_score_volatility_149'] = _z(_ema(a, 504) - _ema(a, 1008), 1512)
    f['f32_altman_z_score_volatility_150'] = _z(b, 21)
    return pd.DataFrame(f)