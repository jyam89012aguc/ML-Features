
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
    at = df['assets']
    ocf = df['ncfo']
    ltd = df['debtnc']
    ca = df['assetsc']
    cl = df['liabilitiesc']
    so = df['sharesbas']
    gp = df['gp']
    rev = df['revenue']
    roa = ni / at
    cfo_a = ocf / at
    accrual = roa - cfo_a
    lev = ltd / at
    liq = ca / cl
    gm = gp / rev
    aturn = rev / at
    f = {}
    f['f31_piotroski_f_score_analogs_076'] = _z(_roc(roa, 21), 21)
    f['f31_piotroski_f_score_analogs_077'] = _z(cfo_a.diff(63), 126)
    f['f31_piotroski_f_score_analogs_078'] = _z(accrual / _std(accrual, 63).replace(0, 1), 63)
    f['f31_piotroski_f_score_analogs_079'] = _z(_ema(lev, 63) - _ema(lev, 126), 189)
    f['f31_piotroski_f_score_analogs_080'] = _z(liq, 63)
    f['f31_piotroski_f_score_analogs_081'] = _z(_roc(gm, 63), 63)
    f['f31_piotroski_f_score_analogs_082'] = _z(aturn.diff(63), 126)
    f['f31_piotroski_f_score_analogs_083'] = _z(roa / _std(roa, 63).replace(0, 1), 63)
    f['f31_piotroski_f_score_analogs_084'] = _z(_ema(cfo_a, 126) - _ema(cfo_a, 252), 378)
    f['f31_piotroski_f_score_analogs_085'] = _z(accrual, 126)
    f['f31_piotroski_f_score_analogs_086'] = _z(_roc(lev, 126), 126)
    f['f31_piotroski_f_score_analogs_087'] = _z(liq.diff(126), 252)
    f['f31_piotroski_f_score_analogs_088'] = _z(gm / _std(gm, 126).replace(0, 1), 126)
    f['f31_piotroski_f_score_analogs_089'] = _z(_ema(aturn, 126) - _ema(aturn, 252), 378)
    f['f31_piotroski_f_score_analogs_090'] = _z(roa, 126)
    f['f31_piotroski_f_score_analogs_091'] = _z(_roc(cfo_a, 252), 252)
    f['f31_piotroski_f_score_analogs_092'] = _z(accrual.diff(252), 504)
    f['f31_piotroski_f_score_analogs_093'] = _z(lev / _std(lev, 252).replace(0, 1), 252)
    f['f31_piotroski_f_score_analogs_094'] = _z(_ema(liq, 252) - _ema(liq, 504), 756)
    f['f31_piotroski_f_score_analogs_095'] = _z(gm, 252)
    f['f31_piotroski_f_score_analogs_096'] = _z(_roc(aturn, 252), 252)
    f['f31_piotroski_f_score_analogs_097'] = _z(roa.diff(252), 504)
    f['f31_piotroski_f_score_analogs_098'] = _z(cfo_a / _std(cfo_a, 504).replace(0, 1), 504)
    f['f31_piotroski_f_score_analogs_099'] = _z(_ema(accrual, 504) - _ema(accrual, 1008), 1512)
    f['f31_piotroski_f_score_analogs_100'] = _z(lev, 504)
    f['f31_piotroski_f_score_analogs_101'] = _z(_roc(liq, 504), 504)
    f['f31_piotroski_f_score_analogs_102'] = _z(gm.diff(504), 1008)
    f['f31_piotroski_f_score_analogs_103'] = _z(aturn / _std(aturn, 504).replace(0, 1), 504)
    f['f31_piotroski_f_score_analogs_104'] = _z(_ema(roa, 504) - _ema(roa, 1008), 1512)
    f['f31_piotroski_f_score_analogs_105'] = _z(cfo_a, 21)
    f['f31_piotroski_f_score_analogs_106'] = _z(_roc(accrual, 21), 21)
    f['f31_piotroski_f_score_analogs_107'] = _z(lev.diff(21), 42)
    f['f31_piotroski_f_score_analogs_108'] = _z(liq / _std(liq, 21).replace(0, 1), 21)
    f['f31_piotroski_f_score_analogs_109'] = _z(_ema(gm, 21) - _ema(gm, 42), 63)
    f['f31_piotroski_f_score_analogs_110'] = _z(aturn, 21)
    f['f31_piotroski_f_score_analogs_111'] = _z(_roc(roa, 21), 21)
    f['f31_piotroski_f_score_analogs_112'] = _z(cfo_a.diff(63), 126)
    f['f31_piotroski_f_score_analogs_113'] = _z(accrual / _std(accrual, 63).replace(0, 1), 63)
    f['f31_piotroski_f_score_analogs_114'] = _z(_ema(lev, 63) - _ema(lev, 126), 189)
    f['f31_piotroski_f_score_analogs_115'] = _z(liq, 63)
    f['f31_piotroski_f_score_analogs_116'] = _z(_roc(gm, 63), 63)
    f['f31_piotroski_f_score_analogs_117'] = _z(aturn.diff(63), 126)
    f['f31_piotroski_f_score_analogs_118'] = _z(roa / _std(roa, 63).replace(0, 1), 63)
    f['f31_piotroski_f_score_analogs_119'] = _z(_ema(cfo_a, 126) - _ema(cfo_a, 252), 378)
    f['f31_piotroski_f_score_analogs_120'] = _z(accrual, 126)
    f['f31_piotroski_f_score_analogs_121'] = _z(_roc(lev, 126), 126)
    f['f31_piotroski_f_score_analogs_122'] = _z(liq.diff(126), 252)
    f['f31_piotroski_f_score_analogs_123'] = _z(gm / _std(gm, 126).replace(0, 1), 126)
    f['f31_piotroski_f_score_analogs_124'] = _z(_ema(aturn, 126) - _ema(aturn, 252), 378)
    f['f31_piotroski_f_score_analogs_125'] = _z(roa, 126)
    f['f31_piotroski_f_score_analogs_126'] = _z(_roc(cfo_a, 252), 252)
    f['f31_piotroski_f_score_analogs_127'] = _z(accrual.diff(252), 504)
    f['f31_piotroski_f_score_analogs_128'] = _z(lev / _std(lev, 252).replace(0, 1), 252)
    f['f31_piotroski_f_score_analogs_129'] = _z(_ema(liq, 252) - _ema(liq, 504), 756)
    f['f31_piotroski_f_score_analogs_130'] = _z(gm, 252)
    f['f31_piotroski_f_score_analogs_131'] = _z(_roc(aturn, 252), 252)
    f['f31_piotroski_f_score_analogs_132'] = _z(roa.diff(252), 504)
    f['f31_piotroski_f_score_analogs_133'] = _z(cfo_a / _std(cfo_a, 504).replace(0, 1), 504)
    f['f31_piotroski_f_score_analogs_134'] = _z(_ema(accrual, 504) - _ema(accrual, 1008), 1512)
    f['f31_piotroski_f_score_analogs_135'] = _z(lev, 504)
    f['f31_piotroski_f_score_analogs_136'] = _z(_roc(liq, 504), 504)
    f['f31_piotroski_f_score_analogs_137'] = _z(gm.diff(504), 1008)
    f['f31_piotroski_f_score_analogs_138'] = _z(aturn / _std(aturn, 504).replace(0, 1), 504)
    f['f31_piotroski_f_score_analogs_139'] = _z(_ema(roa, 504) - _ema(roa, 1008), 1512)
    f['f31_piotroski_f_score_analogs_140'] = _z(cfo_a, 21)
    f['f31_piotroski_f_score_analogs_141'] = _z(_roc(accrual, 21), 21)
    f['f31_piotroski_f_score_analogs_142'] = _z(lev.diff(21), 42)
    f['f31_piotroski_f_score_analogs_143'] = _z(liq / _std(liq, 21).replace(0, 1), 21)
    f['f31_piotroski_f_score_analogs_144'] = _z(_ema(gm, 21) - _ema(gm, 42), 63)
    f['f31_piotroski_f_score_analogs_145'] = _z(aturn, 21)
    f['f31_piotroski_f_score_analogs_146'] = _z(_roc(roa, 21), 21)
    f['f31_piotroski_f_score_analogs_147'] = _z(cfo_a.diff(63), 126)
    f['f31_piotroski_f_score_analogs_148'] = _z(accrual / _std(accrual, 63).replace(0, 1), 63)
    f['f31_piotroski_f_score_analogs_149'] = _z(_ema(lev, 63) - _ema(lev, 126), 189)
    f['f31_piotroski_f_score_analogs_150'] = _z(liq, 63)
    return pd.DataFrame(f)