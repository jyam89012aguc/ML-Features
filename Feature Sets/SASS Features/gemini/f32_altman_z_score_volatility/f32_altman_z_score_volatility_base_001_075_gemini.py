
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
    f['f32_altman_z_score_volatility_001'] = _z(_roc(z, 21), 21)
    f['f32_altman_z_score_volatility_002'] = _z(a.diff(21), 42)
    f['f32_altman_z_score_volatility_003'] = _z(b / _std(b, 21).replace(0, 1), 21)
    f['f32_altman_z_score_volatility_004'] = _z(_ema(c, 21) - _ema(c, 42), 63)
    f['f32_altman_z_score_volatility_005'] = _z(d, 21)
    f['f32_altman_z_score_volatility_006'] = _z(_roc(e, 63), 63)
    f['f32_altman_z_score_volatility_007'] = _z(z.diff(63), 126)
    f['f32_altman_z_score_volatility_008'] = _z(a / _std(a, 63).replace(0, 1), 63)
    f['f32_altman_z_score_volatility_009'] = _z(_ema(b, 63) - _ema(b, 126), 189)
    f['f32_altman_z_score_volatility_010'] = _z(c, 63)
    f['f32_altman_z_score_volatility_011'] = _z(_roc(d, 63), 63)
    f['f32_altman_z_score_volatility_012'] = _z(e.diff(126), 252)
    f['f32_altman_z_score_volatility_013'] = _z(z / _std(z, 126).replace(0, 1), 126)
    f['f32_altman_z_score_volatility_014'] = _z(_ema(a, 126) - _ema(a, 252), 378)
    f['f32_altman_z_score_volatility_015'] = _z(b, 126)
    f['f32_altman_z_score_volatility_016'] = _z(_roc(c, 126), 126)
    f['f32_altman_z_score_volatility_017'] = _z(d.diff(126), 252)
    f['f32_altman_z_score_volatility_018'] = _z(e / _std(e, 252).replace(0, 1), 252)
    f['f32_altman_z_score_volatility_019'] = _z(_ema(z, 252) - _ema(z, 504), 756)
    f['f32_altman_z_score_volatility_020'] = _z(a, 252)
    f['f32_altman_z_score_volatility_021'] = _z(_roc(b, 252), 252)
    f['f32_altman_z_score_volatility_022'] = _z(c.diff(252), 504)
    f['f32_altman_z_score_volatility_023'] = _z(d / _std(d, 252).replace(0, 1), 252)
    f['f32_altman_z_score_volatility_024'] = _z(_ema(e, 504) - _ema(e, 1008), 1512)
    f['f32_altman_z_score_volatility_025'] = _z(z, 504)
    f['f32_altman_z_score_volatility_026'] = _z(_roc(a, 504), 504)
    f['f32_altman_z_score_volatility_027'] = _z(b.diff(504), 1008)
    f['f32_altman_z_score_volatility_028'] = _z(c / _std(c, 504).replace(0, 1), 504)
    f['f32_altman_z_score_volatility_029'] = _z(_ema(d, 504) - _ema(d, 1008), 1512)
    f['f32_altman_z_score_volatility_030'] = _z(e, 21)
    f['f32_altman_z_score_volatility_031'] = _z(_roc(z, 21), 21)
    f['f32_altman_z_score_volatility_032'] = _z(a.diff(21), 42)
    f['f32_altman_z_score_volatility_033'] = _z(b / _std(b, 21).replace(0, 1), 21)
    f['f32_altman_z_score_volatility_034'] = _z(_ema(c, 21) - _ema(c, 42), 63)
    f['f32_altman_z_score_volatility_035'] = _z(d, 21)
    f['f32_altman_z_score_volatility_036'] = _z(_roc(e, 63), 63)
    f['f32_altman_z_score_volatility_037'] = _z(z.diff(63), 126)
    f['f32_altman_z_score_volatility_038'] = _z(a / _std(a, 63).replace(0, 1), 63)
    f['f32_altman_z_score_volatility_039'] = _z(_ema(b, 63) - _ema(b, 126), 189)
    f['f32_altman_z_score_volatility_040'] = _z(c, 63)
    f['f32_altman_z_score_volatility_041'] = _z(_roc(d, 63), 63)
    f['f32_altman_z_score_volatility_042'] = _z(e.diff(126), 252)
    f['f32_altman_z_score_volatility_043'] = _z(z / _std(z, 126).replace(0, 1), 126)
    f['f32_altman_z_score_volatility_044'] = _z(_ema(a, 126) - _ema(a, 252), 378)
    f['f32_altman_z_score_volatility_045'] = _z(b, 126)
    f['f32_altman_z_score_volatility_046'] = _z(_roc(c, 126), 126)
    f['f32_altman_z_score_volatility_047'] = _z(d.diff(126), 252)
    f['f32_altman_z_score_volatility_048'] = _z(e / _std(e, 252).replace(0, 1), 252)
    f['f32_altman_z_score_volatility_049'] = _z(_ema(z, 252) - _ema(z, 504), 756)
    f['f32_altman_z_score_volatility_050'] = _z(a, 252)
    f['f32_altman_z_score_volatility_051'] = _z(_roc(b, 252), 252)
    f['f32_altman_z_score_volatility_052'] = _z(c.diff(252), 504)
    f['f32_altman_z_score_volatility_053'] = _z(d / _std(d, 252).replace(0, 1), 252)
    f['f32_altman_z_score_volatility_054'] = _z(_ema(e, 504) - _ema(e, 1008), 1512)
    f['f32_altman_z_score_volatility_055'] = _z(z, 504)
    f['f32_altman_z_score_volatility_056'] = _z(_roc(a, 504), 504)
    f['f32_altman_z_score_volatility_057'] = _z(b.diff(504), 1008)
    f['f32_altman_z_score_volatility_058'] = _z(c / _std(c, 504).replace(0, 1), 504)
    f['f32_altman_z_score_volatility_059'] = _z(_ema(d, 504) - _ema(d, 1008), 1512)
    f['f32_altman_z_score_volatility_060'] = _z(e, 21)
    f['f32_altman_z_score_volatility_061'] = _z(_roc(z, 21), 21)
    f['f32_altman_z_score_volatility_062'] = _z(a.diff(21), 42)
    f['f32_altman_z_score_volatility_063'] = _z(b / _std(b, 21).replace(0, 1), 21)
    f['f32_altman_z_score_volatility_064'] = _z(_ema(c, 21) - _ema(c, 42), 63)
    f['f32_altman_z_score_volatility_065'] = _z(d, 21)
    f['f32_altman_z_score_volatility_066'] = _z(_roc(e, 63), 63)
    f['f32_altman_z_score_volatility_067'] = _z(z.diff(63), 126)
    f['f32_altman_z_score_volatility_068'] = _z(a / _std(a, 63).replace(0, 1), 63)
    f['f32_altman_z_score_volatility_069'] = _z(_ema(b, 63) - _ema(b, 126), 189)
    f['f32_altman_z_score_volatility_070'] = _z(c, 63)
    f['f32_altman_z_score_volatility_071'] = _z(_roc(d, 63), 63)
    f['f32_altman_z_score_volatility_072'] = _z(e.diff(126), 252)
    f['f32_altman_z_score_volatility_073'] = _z(z / _std(z, 126).replace(0, 1), 126)
    f['f32_altman_z_score_volatility_074'] = _z(_ema(a, 126) - _ema(a, 252), 378)
    f['f32_altman_z_score_volatility_075'] = _z(b, 126)
    return pd.DataFrame(f)