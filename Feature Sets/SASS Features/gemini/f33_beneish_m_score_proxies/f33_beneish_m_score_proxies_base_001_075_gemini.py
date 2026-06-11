
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
    f['f33_beneish_m_score_proxies_001'] = _z(_roc(dsri, 21), 21)
    f['f33_beneish_m_score_proxies_002'] = _z(gmi.diff(21), 42)
    f['f33_beneish_m_score_proxies_003'] = _z(aqi / _std(aqi, 63).replace(0, 1), 63)
    f['f33_beneish_m_score_proxies_004'] = _z(_ema(dsri, 63) - _ema(dsri, 126), 189)
    f['f33_beneish_m_score_proxies_005'] = _z(gmi, 63)
    f['f33_beneish_m_score_proxies_006'] = _z(_roc(aqi, 126), 126)
    f['f33_beneish_m_score_proxies_007'] = _z(dsri.diff(126), 252)
    f['f33_beneish_m_score_proxies_008'] = _z(gmi / _std(gmi, 126).replace(0, 1), 126)
    f['f33_beneish_m_score_proxies_009'] = _z(_ema(aqi, 252) - _ema(aqi, 504), 756)
    f['f33_beneish_m_score_proxies_010'] = _z(dsri, 252)
    f['f33_beneish_m_score_proxies_011'] = _z(_roc(gmi, 252), 252)
    f['f33_beneish_m_score_proxies_012'] = _z(aqi.diff(504), 1008)
    f['f33_beneish_m_score_proxies_013'] = _z(dsri / _std(dsri, 504).replace(0, 1), 504)
    f['f33_beneish_m_score_proxies_014'] = _z(_ema(gmi, 504) - _ema(gmi, 1008), 1512)
    f['f33_beneish_m_score_proxies_015'] = _z(aqi, 21)
    f['f33_beneish_m_score_proxies_016'] = _z(_roc(dsri, 21), 21)
    f['f33_beneish_m_score_proxies_017'] = _z(gmi.diff(21), 42)
    f['f33_beneish_m_score_proxies_018'] = _z(aqi / _std(aqi, 63).replace(0, 1), 63)
    f['f33_beneish_m_score_proxies_019'] = _z(_ema(dsri, 63) - _ema(dsri, 126), 189)
    f['f33_beneish_m_score_proxies_020'] = _z(gmi, 63)
    f['f33_beneish_m_score_proxies_021'] = _z(_roc(aqi, 126), 126)
    f['f33_beneish_m_score_proxies_022'] = _z(dsri.diff(126), 252)
    f['f33_beneish_m_score_proxies_023'] = _z(gmi / _std(gmi, 126).replace(0, 1), 126)
    f['f33_beneish_m_score_proxies_024'] = _z(_ema(aqi, 252) - _ema(aqi, 504), 756)
    f['f33_beneish_m_score_proxies_025'] = _z(dsri, 252)
    f['f33_beneish_m_score_proxies_026'] = _z(_roc(gmi, 252), 252)
    f['f33_beneish_m_score_proxies_027'] = _z(aqi.diff(504), 1008)
    f['f33_beneish_m_score_proxies_028'] = _z(dsri / _std(dsri, 504).replace(0, 1), 504)
    f['f33_beneish_m_score_proxies_029'] = _z(_ema(gmi, 504) - _ema(gmi, 1008), 1512)
    f['f33_beneish_m_score_proxies_030'] = _z(aqi, 21)
    f['f33_beneish_m_score_proxies_031'] = _z(_roc(dsri, 21), 21)
    f['f33_beneish_m_score_proxies_032'] = _z(gmi.diff(21), 42)
    f['f33_beneish_m_score_proxies_033'] = _z(aqi / _std(aqi, 63).replace(0, 1), 63)
    f['f33_beneish_m_score_proxies_034'] = _z(_ema(dsri, 63) - _ema(dsri, 126), 189)
    f['f33_beneish_m_score_proxies_035'] = _z(gmi, 63)
    f['f33_beneish_m_score_proxies_036'] = _z(_roc(aqi, 126), 126)
    f['f33_beneish_m_score_proxies_037'] = _z(dsri.diff(126), 252)
    f['f33_beneish_m_score_proxies_038'] = _z(gmi / _std(gmi, 126).replace(0, 1), 126)
    f['f33_beneish_m_score_proxies_039'] = _z(_ema(aqi, 252) - _ema(aqi, 504), 756)
    f['f33_beneish_m_score_proxies_040'] = _z(dsri, 252)
    f['f33_beneish_m_score_proxies_041'] = _z(_roc(gmi, 252), 252)
    f['f33_beneish_m_score_proxies_042'] = _z(aqi.diff(504), 1008)
    f['f33_beneish_m_score_proxies_043'] = _z(dsri / _std(dsri, 504).replace(0, 1), 504)
    f['f33_beneish_m_score_proxies_044'] = _z(_ema(gmi, 504) - _ema(gmi, 1008), 1512)
    f['f33_beneish_m_score_proxies_045'] = _z(aqi, 21)
    f['f33_beneish_m_score_proxies_046'] = _z(_roc(dsri, 21), 21)
    f['f33_beneish_m_score_proxies_047'] = _z(gmi.diff(21), 42)
    f['f33_beneish_m_score_proxies_048'] = _z(aqi / _std(aqi, 63).replace(0, 1), 63)
    f['f33_beneish_m_score_proxies_049'] = _z(_ema(dsri, 63) - _ema(dsri, 126), 189)
    f['f33_beneish_m_score_proxies_050'] = _z(gmi, 63)
    f['f33_beneish_m_score_proxies_051'] = _z(_roc(aqi, 126), 126)
    f['f33_beneish_m_score_proxies_052'] = _z(dsri.diff(126), 252)
    f['f33_beneish_m_score_proxies_053'] = _z(gmi / _std(gmi, 126).replace(0, 1), 126)
    f['f33_beneish_m_score_proxies_054'] = _z(_ema(aqi, 252) - _ema(aqi, 504), 756)
    f['f33_beneish_m_score_proxies_055'] = _z(dsri, 252)
    f['f33_beneish_m_score_proxies_056'] = _z(_roc(gmi, 252), 252)
    f['f33_beneish_m_score_proxies_057'] = _z(aqi.diff(504), 1008)
    f['f33_beneish_m_score_proxies_058'] = _z(dsri / _std(dsri, 504).replace(0, 1), 504)
    f['f33_beneish_m_score_proxies_059'] = _z(_ema(gmi, 504) - _ema(gmi, 1008), 1512)
    f['f33_beneish_m_score_proxies_060'] = _z(aqi, 21)
    f['f33_beneish_m_score_proxies_061'] = _z(_roc(dsri, 21), 21)
    f['f33_beneish_m_score_proxies_062'] = _z(gmi.diff(21), 42)
    f['f33_beneish_m_score_proxies_063'] = _z(aqi / _std(aqi, 63).replace(0, 1), 63)
    f['f33_beneish_m_score_proxies_064'] = _z(_ema(dsri, 63) - _ema(dsri, 126), 189)
    f['f33_beneish_m_score_proxies_065'] = _z(gmi, 63)
    f['f33_beneish_m_score_proxies_066'] = _z(_roc(aqi, 126), 126)
    f['f33_beneish_m_score_proxies_067'] = _z(dsri.diff(126), 252)
    f['f33_beneish_m_score_proxies_068'] = _z(gmi / _std(gmi, 126).replace(0, 1), 126)
    f['f33_beneish_m_score_proxies_069'] = _z(_ema(aqi, 252) - _ema(aqi, 504), 756)
    f['f33_beneish_m_score_proxies_070'] = _z(dsri, 252)
    f['f33_beneish_m_score_proxies_071'] = _z(_roc(gmi, 252), 252)
    f['f33_beneish_m_score_proxies_072'] = _z(aqi.diff(504), 1008)
    f['f33_beneish_m_score_proxies_073'] = _z(dsri / _std(dsri, 504).replace(0, 1), 504)
    f['f33_beneish_m_score_proxies_074'] = _z(_ema(gmi, 504) - _ema(gmi, 1008), 1512)
    f['f33_beneish_m_score_proxies_075'] = _z(aqi, 21)
    return pd.DataFrame(f)