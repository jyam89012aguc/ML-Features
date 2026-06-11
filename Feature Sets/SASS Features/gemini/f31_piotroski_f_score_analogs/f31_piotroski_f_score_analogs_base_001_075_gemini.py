
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
    f['f31_piotroski_f_score_analogs_001'] = _z(_roc(roa, 21), 21)
    f['f31_piotroski_f_score_analogs_002'] = _z(cfo_a.diff(21), 42)
    f['f31_piotroski_f_score_analogs_003'] = _z(accrual / _std(accrual, 21).replace(0, 1), 21)
    f['f31_piotroski_f_score_analogs_004'] = _z(_ema(lev, 21) - _ema(lev, 42), 63)
    f['f31_piotroski_f_score_analogs_005'] = _z(liq, 21)
    f['f31_piotroski_f_score_analogs_006'] = _z(_roc(gm, 21), 21)
    f['f31_piotroski_f_score_analogs_007'] = _z(aturn.diff(63), 126)
    f['f31_piotroski_f_score_analogs_008'] = _z(roa / _std(roa, 63).replace(0, 1), 63)
    f['f31_piotroski_f_score_analogs_009'] = _z(_ema(cfo_a, 63) - _ema(cfo_a, 126), 189)
    f['f31_piotroski_f_score_analogs_010'] = _z(accrual, 63)
    f['f31_piotroski_f_score_analogs_011'] = _z(_roc(lev, 63), 63)
    f['f31_piotroski_f_score_analogs_012'] = _z(liq.diff(63), 126)
    f['f31_piotroski_f_score_analogs_013'] = _z(gm / _std(gm, 63).replace(0, 1), 63)
    f['f31_piotroski_f_score_analogs_014'] = _z(_ema(aturn, 126) - _ema(aturn, 252), 378)
    f['f31_piotroski_f_score_analogs_015'] = _z(roa, 126)
    f['f31_piotroski_f_score_analogs_016'] = _z(_roc(cfo_a, 126), 126)
    f['f31_piotroski_f_score_analogs_017'] = _z(accrual.diff(126), 252)
    f['f31_piotroski_f_score_analogs_018'] = _z(lev / _std(lev, 126).replace(0, 1), 126)
    f['f31_piotroski_f_score_analogs_019'] = _z(_ema(liq, 126) - _ema(liq, 252), 378)
    f['f31_piotroski_f_score_analogs_020'] = _z(gm, 126)
    f['f31_piotroski_f_score_analogs_021'] = _z(_roc(aturn, 252), 252)
    f['f31_piotroski_f_score_analogs_022'] = _z(roa.diff(252), 504)
    f['f31_piotroski_f_score_analogs_023'] = _z(cfo_a / _std(cfo_a, 252).replace(0, 1), 252)
    f['f31_piotroski_f_score_analogs_024'] = _z(_ema(accrual, 252) - _ema(accrual, 504), 756)
    f['f31_piotroski_f_score_analogs_025'] = _z(lev, 252)
    f['f31_piotroski_f_score_analogs_026'] = _z(_roc(liq, 252), 252)
    f['f31_piotroski_f_score_analogs_027'] = _z(gm.diff(252), 504)
    f['f31_piotroski_f_score_analogs_028'] = _z(aturn / _std(aturn, 504).replace(0, 1), 504)
    f['f31_piotroski_f_score_analogs_029'] = _z(_ema(roa, 504) - _ema(roa, 1008), 1512)
    f['f31_piotroski_f_score_analogs_030'] = _z(cfo_a, 504)
    f['f31_piotroski_f_score_analogs_031'] = _z(_roc(accrual, 504), 504)
    f['f31_piotroski_f_score_analogs_032'] = _z(lev.diff(504), 1008)
    f['f31_piotroski_f_score_analogs_033'] = _z(liq / _std(liq, 504).replace(0, 1), 504)
    f['f31_piotroski_f_score_analogs_034'] = _z(_ema(gm, 504) - _ema(gm, 1008), 1512)
    f['f31_piotroski_f_score_analogs_035'] = _z(aturn, 21)
    f['f31_piotroski_f_score_analogs_036'] = _z(_roc(roa, 21), 21)
    f['f31_piotroski_f_score_analogs_037'] = _z(cfo_a.diff(21), 42)
    f['f31_piotroski_f_score_analogs_038'] = _z(accrual / _std(accrual, 21).replace(0, 1), 21)
    f['f31_piotroski_f_score_analogs_039'] = _z(_ema(lev, 21) - _ema(lev, 42), 63)
    f['f31_piotroski_f_score_analogs_040'] = _z(liq, 21)
    f['f31_piotroski_f_score_analogs_041'] = _z(_roc(gm, 21), 21)
    f['f31_piotroski_f_score_analogs_042'] = _z(aturn.diff(63), 126)
    f['f31_piotroski_f_score_analogs_043'] = _z(roa / _std(roa, 63).replace(0, 1), 63)
    f['f31_piotroski_f_score_analogs_044'] = _z(_ema(cfo_a, 63) - _ema(cfo_a, 126), 189)
    f['f31_piotroski_f_score_analogs_045'] = _z(accrual, 63)
    f['f31_piotroski_f_score_analogs_046'] = _z(_roc(lev, 63), 63)
    f['f31_piotroski_f_score_analogs_047'] = _z(liq.diff(63), 126)
    f['f31_piotroski_f_score_analogs_048'] = _z(gm / _std(gm, 63).replace(0, 1), 63)
    f['f31_piotroski_f_score_analogs_049'] = _z(_ema(aturn, 126) - _ema(aturn, 252), 378)
    f['f31_piotroski_f_score_analogs_050'] = _z(roa, 126)
    f['f31_piotroski_f_score_analogs_051'] = _z(_roc(cfo_a, 126), 126)
    f['f31_piotroski_f_score_analogs_052'] = _z(accrual.diff(126), 252)
    f['f31_piotroski_f_score_analogs_053'] = _z(lev / _std(lev, 126).replace(0, 1), 126)
    f['f31_piotroski_f_score_analogs_054'] = _z(_ema(liq, 126) - _ema(liq, 252), 378)
    f['f31_piotroski_f_score_analogs_055'] = _z(gm, 126)
    f['f31_piotroski_f_score_analogs_056'] = _z(_roc(aturn, 252), 252)
    f['f31_piotroski_f_score_analogs_057'] = _z(roa.diff(252), 504)
    f['f31_piotroski_f_score_analogs_058'] = _z(cfo_a / _std(cfo_a, 252).replace(0, 1), 252)
    f['f31_piotroski_f_score_analogs_059'] = _z(_ema(accrual, 252) - _ema(accrual, 504), 756)
    f['f31_piotroski_f_score_analogs_060'] = _z(lev, 252)
    f['f31_piotroski_f_score_analogs_061'] = _z(_roc(liq, 252), 252)
    f['f31_piotroski_f_score_analogs_062'] = _z(gm.diff(252), 504)
    f['f31_piotroski_f_score_analogs_063'] = _z(aturn / _std(aturn, 504).replace(0, 1), 504)
    f['f31_piotroski_f_score_analogs_064'] = _z(_ema(roa, 504) - _ema(roa, 1008), 1512)
    f['f31_piotroski_f_score_analogs_065'] = _z(cfo_a, 504)
    f['f31_piotroski_f_score_analogs_066'] = _z(_roc(accrual, 504), 504)
    f['f31_piotroski_f_score_analogs_067'] = _z(lev.diff(504), 1008)
    f['f31_piotroski_f_score_analogs_068'] = _z(liq / _std(liq, 504).replace(0, 1), 504)
    f['f31_piotroski_f_score_analogs_069'] = _z(_ema(gm, 504) - _ema(gm, 1008), 1512)
    f['f31_piotroski_f_score_analogs_070'] = _z(aturn, 21)
    f['f31_piotroski_f_score_analogs_071'] = _z(_roc(roa, 21), 21)
    f['f31_piotroski_f_score_analogs_072'] = _z(cfo_a.diff(21), 42)
    f['f31_piotroski_f_score_analogs_073'] = _z(accrual / _std(accrual, 21).replace(0, 1), 21)
    f['f31_piotroski_f_score_analogs_074'] = _z(_ema(lev, 21) - _ema(lev, 42), 63)
    f['f31_piotroski_f_score_analogs_075'] = _z(liq, 21)
    return pd.DataFrame(f)