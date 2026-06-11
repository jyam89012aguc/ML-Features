
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
    ni = df['netinc']
    at = df['assets']
    ca = df['assetsc']
    cl = df['liabilitiesc']
    gp = df['gp']
    ocf = df['ncfo']
    dsri = (rev/rev.shift(252)) / (ni/ni.shift(252))
    gmi = (gp.shift(252)/rev.shift(252)) / (gp/rev)
    aqi = (1-(ca+cl)/at) / (1-(ca.shift(252)+cl.shift(252))/at.shift(252))
    f = {}
    f['f33_beneish_m_score_proxies_076'] = _z(_roc(dsri, 21), 21)
    f['f33_beneish_m_score_proxies_077'] = _z(gmi.diff(21), 42)
    f['f33_beneish_m_score_proxies_078'] = _z(aqi / _std(aqi, 63).replace(0, 1), 63)
    f['f33_beneish_m_score_proxies_079'] = _z(_ema(dsri, 63) - _ema(dsri, 126), 189)
    f['f33_beneish_m_score_proxies_080'] = _z(gmi, 63)
    f['f33_beneish_m_score_proxies_081'] = _z(_roc(aqi, 126), 126)
    f['f33_beneish_m_score_proxies_082'] = _z(dsri.diff(126), 252)
    f['f33_beneish_m_score_proxies_083'] = _z(gmi / _std(gmi, 126).replace(0, 1), 126)
    f['f33_beneish_m_score_proxies_084'] = _z(_ema(aqi, 252) - _ema(aqi, 504), 756)
    f['f33_beneish_m_score_proxies_085'] = _z(dsri, 252)
    f['f33_beneish_m_score_proxies_086'] = _z(_roc(gmi, 252), 252)
    f['f33_beneish_m_score_proxies_087'] = _z(aqi.diff(504), 1008)
    f['f33_beneish_m_score_proxies_088'] = _z(dsri / _std(dsri, 504).replace(0, 1), 504)
    f['f33_beneish_m_score_proxies_089'] = _z(_ema(gmi, 504) - _ema(gmi, 1008), 1512)
    f['f33_beneish_m_score_proxies_090'] = _z(aqi, 21)
    f['f33_beneish_m_score_proxies_091'] = _z(_roc(dsri, 21), 21)
    f['f33_beneish_m_score_proxies_092'] = _z(gmi.diff(21), 42)
    f['f33_beneish_m_score_proxies_093'] = _z(aqi / _std(aqi, 63).replace(0, 1), 63)
    f['f33_beneish_m_score_proxies_094'] = _z(_ema(dsri, 63) - _ema(dsri, 126), 189)
    f['f33_beneish_m_score_proxies_095'] = _z(gmi, 63)
    f['f33_beneish_m_score_proxies_096'] = _z(_roc(aqi, 126), 126)
    f['f33_beneish_m_score_proxies_097'] = _z(dsri.diff(126), 252)
    f['f33_beneish_m_score_proxies_098'] = _z(gmi / _std(gmi, 126).replace(0, 1), 126)
    f['f33_beneish_m_score_proxies_099'] = _z(_ema(aqi, 252) - _ema(aqi, 504), 756)
    f['f33_beneish_m_score_proxies_100'] = _z(dsri, 252)
    f['f33_beneish_m_score_proxies_101'] = _z(_roc(gmi, 252), 252)
    f['f33_beneish_m_score_proxies_102'] = _z(aqi.diff(504), 1008)
    f['f33_beneish_m_score_proxies_103'] = _z(dsri / _std(dsri, 504).replace(0, 1), 504)
    f['f33_beneish_m_score_proxies_104'] = _z(_ema(gmi, 504) - _ema(gmi, 1008), 1512)
    f['f33_beneish_m_score_proxies_105'] = _z(aqi, 21)
    f['f33_beneish_m_score_proxies_106'] = _z(_roc(dsri, 21), 21)
    f['f33_beneish_m_score_proxies_107'] = _z(gmi.diff(21), 42)
    f['f33_beneish_m_score_proxies_108'] = _z(aqi / _std(aqi, 63).replace(0, 1), 63)
    f['f33_beneish_m_score_proxies_109'] = _z(_ema(dsri, 63) - _ema(dsri, 126), 189)
    f['f33_beneish_m_score_proxies_110'] = _z(gmi, 63)
    f['f33_beneish_m_score_proxies_111'] = _z(_roc(aqi, 126), 126)
    f['f33_beneish_m_score_proxies_112'] = _z(dsri.diff(126), 252)
    f['f33_beneish_m_score_proxies_113'] = _z(gmi / _std(gmi, 126).replace(0, 1), 126)
    f['f33_beneish_m_score_proxies_114'] = _z(_ema(aqi, 252) - _ema(aqi, 504), 756)
    f['f33_beneish_m_score_proxies_115'] = _z(dsri, 252)
    f['f33_beneish_m_score_proxies_116'] = _z(_roc(gmi, 252), 252)
    f['f33_beneish_m_score_proxies_117'] = _z(aqi.diff(504), 1008)
    f['f33_beneish_m_score_proxies_118'] = _z(dsri / _std(dsri, 504).replace(0, 1), 504)
    f['f33_beneish_m_score_proxies_119'] = _z(_ema(gmi, 504) - _ema(gmi, 1008), 1512)
    f['f33_beneish_m_score_proxies_120'] = _z(aqi, 21)
    f['f33_beneish_m_score_proxies_121'] = _z(_roc(dsri, 21), 21)
    f['f33_beneish_m_score_proxies_122'] = _z(gmi.diff(21), 42)
    f['f33_beneish_m_score_proxies_123'] = _z(aqi / _std(aqi, 63).replace(0, 1), 63)
    f['f33_beneish_m_score_proxies_124'] = _z(_ema(dsri, 63) - _ema(dsri, 126), 189)
    f['f33_beneish_m_score_proxies_125'] = _z(gmi, 63)
    f['f33_beneish_m_score_proxies_126'] = _z(_roc(aqi, 126), 126)
    f['f33_beneish_m_score_proxies_127'] = _z(dsri.diff(126), 252)
    f['f33_beneish_m_score_proxies_128'] = _z(gmi / _std(gmi, 126).replace(0, 1), 126)
    f['f33_beneish_m_score_proxies_129'] = _z(_ema(aqi, 252) - _ema(aqi, 504), 756)
    f['f33_beneish_m_score_proxies_130'] = _z(dsri, 252)
    f['f33_beneish_m_score_proxies_131'] = _z(_roc(gmi, 252), 252)
    f['f33_beneish_m_score_proxies_132'] = _z(aqi.diff(504), 1008)
    f['f33_beneish_m_score_proxies_133'] = _z(dsri / _std(dsri, 504).replace(0, 1), 504)
    f['f33_beneish_m_score_proxies_134'] = _z(_ema(gmi, 504) - _ema(gmi, 1008), 1512)
    f['f33_beneish_m_score_proxies_135'] = _z(aqi, 21)
    f['f33_beneish_m_score_proxies_136'] = _z(_roc(dsri, 21), 21)
    f['f33_beneish_m_score_proxies_137'] = _z(gmi.diff(21), 42)
    f['f33_beneish_m_score_proxies_138'] = _z(aqi / _std(aqi, 63).replace(0, 1), 63)
    f['f33_beneish_m_score_proxies_139'] = _z(_ema(dsri, 63) - _ema(dsri, 126), 189)
    f['f33_beneish_m_score_proxies_140'] = _z(gmi, 63)
    f['f33_beneish_m_score_proxies_141'] = _z(_roc(aqi, 126), 126)
    f['f33_beneish_m_score_proxies_142'] = _z(dsri.diff(126), 252)
    f['f33_beneish_m_score_proxies_143'] = _z(gmi / _std(gmi, 126).replace(0, 1), 126)
    f['f33_beneish_m_score_proxies_144'] = _z(_ema(aqi, 252) - _ema(aqi, 504), 756)
    f['f33_beneish_m_score_proxies_145'] = _z(dsri, 252)
    f['f33_beneish_m_score_proxies_146'] = _z(_roc(gmi, 252), 252)
    f['f33_beneish_m_score_proxies_147'] = _z(aqi.diff(504), 1008)
    f['f33_beneish_m_score_proxies_148'] = _z(dsri / _std(dsri, 504).replace(0, 1), 504)
    f['f33_beneish_m_score_proxies_149'] = _z(_ema(gmi, 504) - _ema(gmi, 1008), 1512)
    f['f33_beneish_m_score_proxies_150'] = _z(aqi, 21)
    return pd.DataFrame(f)