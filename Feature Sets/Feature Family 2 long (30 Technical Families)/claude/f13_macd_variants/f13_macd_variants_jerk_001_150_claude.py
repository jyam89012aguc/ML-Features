"""f13_macd_variants jerk features 001-150 (2nd derivative).
Each jerk feature is B - 2*B.shift(k) + B.shift(2k) where k follows the ROC bracket
of the base's primary window. NaN policy: replace([inf,-inf], nan) at return."""
from __future__ import annotations

import numpy as np
import pandas as pd


def _ema(s, n):
    return s.ewm(span=n, adjust=False, min_periods=n).mean()

def _wilder(s, n):
    return s.ewm(alpha=1.0 / float(n), adjust=False, min_periods=n).mean()

def _wma(s, n):
    w = np.arange(1, n + 1, dtype=float)
    return s.rolling(n, min_periods=n).apply(lambda x: float(np.dot(x, w) / w.sum()), raw=True)

def _hma(s, n):
    n2 = max(2, n // 2); sq = max(2, int(np.sqrt(n)))
    return _wma(2.0 * _wma(s, n2) - _wma(s, n), sq)

def _dema(s, n):
    e1 = _ema(s, n); return 2.0 * e1 - _ema(e1, n)

def _zlema(s, n):
    lag = (n - 1) // 2
    return _ema(s + (s - s.shift(lag)), n)

def _tr(high, low, close):
    pc = close.shift(1)
    return pd.concat([(high - low).abs(), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)

def _atr(high, low, close, n):
    return _wilder(_tr(high, low, close), n)


# --- File 1 jerks ----------------------------------------------------------


def f13mc_f13_macd_variants_macddetrend_12_26_jerk_v001_signal(close):
    m=_ema(close,12)-_ema(close,26)
    b = m - m.rolling(30, min_periods=15).mean()
    return(b-2.0*b.shift(10)+b.shift(20)).replace([np.inf,-np.inf],np.nan)

def f13mc_f13_macd_variants_macdslowdetrend_50_200_jerk_v002_signal(closeadj):
    m = _ema(closeadj, 50) - _ema(closeadj, 200)
    b = m - m.rolling(100, min_periods=50).mean()
    return(b-2.0*b.shift(21)+b.shift(42)).replace([np.inf,-np.inf],np.nan)

def f13mc_f13_macd_variants_macd_3_10_jerk_v003_signal(close):
    b = _ema(close, 3) - _ema(close, 10)
    return(b-2.0*b.shift(5)+b.shift(10)).replace([np.inf,-np.inf],np.nan)

def f13mc_f13_macd_variants_macdnorm_12_26_jerk_v004_signal(close):
    e12 = _ema(close, 12); e26 = _ema(close, 26)
    b = (e12 - e26) / e26.replace(0.0, np.nan)
    return(b-2.0*b.shift(21)+b.shift(42)).replace([np.inf,-np.inf],np.nan)

def f13mc_f13_macd_variants_macdrank_8_21_60d_jerk_v005_signal(close):
    m = _ema(close, 8) - _ema(close, 21)
    b = m.rolling(60, min_periods=30).rank(pct=True)
    return(b-2.0*b.shift(10)+b.shift(20)).replace([np.inf,-np.inf],np.nan)

def f13mc_f13_macd_variants_macdnorm_50_200_jerk_v006_signal(closeadj):
    e1 = _ema(closeadj, 50); e2 = _ema(closeadj, 200)
    b = (e1 - e2) / e2.replace(0.0, np.nan)
    return(b-2.0*b.shift(63)+b.shift(126)).replace([np.inf,-np.inf],np.nan)

def f13mc_f13_macd_variants_macdsignagree_5_35_19_39_jerk_v007_signal(close):
    a = _ema(close, 5) - _ema(close, 35); c = _ema(close, 19) - _ema(close, 39)
    b = np.sign(a) * np.sign(c)
    return(b-2.0*b.shift(10)+b.shift(20)).replace([np.inf,-np.inf],np.nan)

def f13mc_f13_macd_variants_macdnorm_19_39_z_jerk_v008_signal(closeadj):
    e1 = _ema(closeadj, 19); e2 = _ema(closeadj, 39)
    r = (e1 - e2) / e2.replace(0.0, np.nan)
    mu = r.rolling(90, min_periods=45).mean(); sd = r.rolling(90, min_periods=45).std()
    b = (r - mu) / sd.replace(0.0, np.nan)
    return(b-2.0*b.shift(63)+b.shift(126)).replace([np.inf,-np.inf],np.nan)

def f13mc_f13_macd_variants_signal_12_26_9_jerk_v009_signal(close):
    m=_ema(close,12)-_ema(close,26); b = _ema(m, 9)
    return(b-2.0*b.shift(10)+b.shift(20)).replace([np.inf,-np.inf],np.nan)

def f13mc_f13_macd_variants_signalnorm_19_39_13_jerk_v010_signal(closeadj):
    e1 = _ema(closeadj, 19); e2 = _ema(closeadj, 39); m = e1 - e2
    b = _ema(m, 13) / e2.replace(0.0, np.nan)
    return(b-2.0*b.shift(10)+b.shift(20)).replace([np.inf,-np.inf],np.nan)

def f13mc_f13_macd_variants_hist_12_26_9_jerk_v011_signal(close):
    m=_ema(close,12)-_ema(close,26); b = m - _ema(m, 9)
    return(b-2.0*b.shift(10)+b.shift(20)).replace([np.inf,-np.inf],np.nan)

def f13mc_f13_macd_variants_hist_8_21_5_jerk_v012_signal(close):
    m = _ema(close, 8) - _ema(close, 21); b = m - _ema(m, 5)
    base=b.abs().rolling(20,min_periods=10).mean()
    jraw=b-2.0*b.shift(10)+b.shift(20)
    return(jraw/base.replace(0.0,np.nan)).replace([np.inf,-np.inf],np.nan)

def f13mc_f13_macd_variants_hist_50_200_30_jerk_v013_signal(closeadj):
    m = _ema(closeadj, 50) - _ema(closeadj, 200); b = m - _ema(m, 30)
    return(b-2.0*b.shift(21)+b.shift(42)).replace([np.inf,-np.inf],np.nan)

def f13mc_f13_macd_variants_histdetrend_12_26_9_jerk_v014_signal(close):
    m=_ema(close,12)-_ema(close,26)
    h = m - _ema(m, 9); b = h - h.rolling(20, min_periods=20).mean()
    return(b-2.0*b.shift(10)+b.shift(20)).replace([np.inf,-np.inf],np.nan)

def f13mc_f13_macd_variants_histabs_12_26_9_jerk_v015_signal(close):
    m=_ema(close,12)-_ema(close,26); h = (m - _ema(m, 9)).abs()
    b = h / close.replace(0.0, np.nan)
    return(b-2.0*b.shift(10)+b.shift(20)).replace([np.inf,-np.inf],np.nan)

def f13mc_f13_macd_variants_signxsig_12_26_9_jerk_v016_signal(close):
    m=_ema(close,12)-_ema(close,26); sig = _ema(m, 9); b = np.sign(m - sig)
    return(b-2.0*b.shift(10)+b.shift(20)).replace([np.inf,-np.inf],np.nan)

def f13mc_f13_macd_variants_signxzero_12_26_jerk_v017_signal(close):
    m=_ema(close,12)-_ema(close,26); b = np.sign(m)
    return(b-2.0*b.shift(10)+b.shift(20)).replace([np.inf,-np.inf],np.nan)

def f13mc_f13_macd_variants_signxzero_50_200_jerk_v018_signal(closeadj):
    m = _ema(closeadj, 50) - _ema(closeadj, 200); b = np.sign(m)
    return(b-2.0*b.shift(21)+b.shift(42)).replace([np.inf,-np.inf],np.nan)

def f13mc_f13_macd_variants_bullstate_12_26_9_jerk_v019_signal(close):
    m=_ema(close,12)-_ema(close,26); sig = _ema(m, 9)
    b = ((m > sig) & (m > 0.0)).astype(float) - ((m < sig) & (m < 0.0)).astype(float)
    return(b-2.0*b.shift(10)+b.shift(20)).replace([np.inf,-np.inf],np.nan)

def f13mc_f13_macd_variants_quaddays_12_26_9_jerk_v020_signal(close):
    m=_ema(close,12)-_ema(close,26); sig = _ema(m, 9)
    state = 2.0 * np.sign(m) + np.sign(m - sig)
    flip = (state != state.shift(1)).astype(float).where(~state.isna() & ~state.shift(1).isna())
    def _ds(x):
        idx = np.where(x > 0.5)[0]
        return 60.0 if idx.size == 0 else float(len(x) - 1 - idx[-1])
    b = flip.rolling(60, min_periods=20).apply(_ds, raw=True)
    return(b-2.0*b.shift(10)+b.shift(20)).replace([np.inf,-np.inf],np.nan)

def f13mc_f13_macd_variants_histslopesign_12_26_9_jerk_v021_signal(close):
    m=_ema(close,12)-_ema(close,26); h = m - _ema(m, 9); b = np.sign(h.diff(3))
    return(b-2.0*b.shift(10)+b.shift(20)).replace([np.inf,-np.inf],np.nan)

def f13mc_f13_macd_variants_dayssincex_12_26_9_jerk_v022_signal(close):
    m=_ema(close,12)-_ema(close,26); sig = _ema(m, 9)
    s = np.sign(m - sig); flip = (s != s.shift(1)).astype(float).where(~s.isna() & ~s.shift(1).isna())
    def _ds(x):
        idx = np.where(x > 0.5)[0]
        return 100.0 if idx.size == 0 else float(len(x) - 1 - idx[-1])
    b = flip.rolling(100, min_periods=20).apply(_ds, raw=True)
    return(b-2.0*b.shift(10)+b.shift(20)).replace([np.inf,-np.inf],np.nan)

def f13mc_f13_macd_variants_dayssincez_19_39_jerk_v023_signal(closeadj):
    m = _ema(closeadj, 19) - _ema(closeadj, 39); s = np.sign(m)
    flip = (s != s.shift(1)).astype(float).where(~s.isna() & ~s.shift(1).isna())
    def _ds(x):
        idx = np.where(x > 0.5)[0]
        return 120.0 if idx.size == 0 else float(len(x) - 1 - idx[-1])
    b = flip.rolling(120, min_periods=30).apply(_ds, raw=True)
    return(b-2.0*b.shift(21)+b.shift(42)).replace([np.inf,-np.inf],np.nan)

def f13mc_f13_macd_variants_streakabove_12_26_9_jerk_v024_signal(close):
    m=_ema(close,12)-_ema(close,26); sig = _ema(m, 9)
    above = (m > sig).astype(float).where(~m.isna() & ~sig.isna())
    grp = (above != above.shift(1)).cumsum(); run = above.groupby(grp).cumcount() + 1.0
    out = np.where(above > 0.5, run, -run); b = pd.Series(out, index=close.index, dtype=float).clip(-60.0, 60.0).where(~above.isna())
    return(b-2.0*b.shift(10)+b.shift(20)).replace([np.inf,-np.inf],np.nan)

def f13mc_f13_macd_variants_streakabovez_50_200_jerk_v025_signal(closeadj):
    m = _ema(closeadj, 50) - _ema(closeadj, 200)
    above = (m > 0.0).astype(float).where(~m.isna())
    grp = (above != above.shift(1)).cumsum(); run = above.groupby(grp).cumcount() + 1.0
    out = np.where(above > 0.5, run, -run); b = pd.Series(out, index=closeadj.index, dtype=float).clip(-150.0, 150.0).where(~above.isna())
    return(b-2.0*b.shift(21)+b.shift(42)).replace([np.inf,-np.inf],np.nan)

def f13mc_f13_macd_variants_xcount_12_26_9_60d_jerk_v026_signal(closeadj):
    m=_ema(closeadj,12)-_ema(closeadj,26); sig = _ema(m, 9)
    s = np.sign(m - sig); flip = (s != s.shift(1)).astype(float).where(~s.isna() & ~s.shift(1).isna())
    b = flip.rolling(60, min_periods=60).sum()
    return(b-2.0*b.shift(10)+b.shift(20)).replace([np.inf,-np.inf],np.nan)

def f13mc_f13_macd_variants_xcountz_19_39_120d_jerk_v027_signal(closeadj):
    m = _ema(closeadj, 19) - _ema(closeadj, 39); s = np.sign(m)
    flip = (s != s.shift(1)).astype(float).where(~s.isna() & ~s.shift(1).isna())
    b = flip.rolling(120, min_periods=120).sum()
    return(b-2.0*b.shift(21)+b.shift(42)).replace([np.inf,-np.inf],np.nan)

def f13mc_f13_macd_variants_histrank_12_26_9_60d_jerk_v028_signal(closeadj):
    m=_ema(closeadj,12)-_ema(closeadj,26); h = m - _ema(m, 9)
    b = h.rolling(60, min_periods=30).rank(pct=True)
    return(b-2.0*b.shift(10)+b.shift(20)).replace([np.inf,-np.inf],np.nan)

def f13mc_f13_macd_variants_histratio_to_macdabs_60d_jerk_v029_signal(closeadj):
    m=_ema(closeadj,12)-_ema(closeadj,26); h = m - _ema(m, 9)
    sc = m.abs().rolling(60, min_periods=30).mean(); b = h / sc.replace(0.0, np.nan)
    return(b-2.0*b.shift(21)+b.shift(42)).replace([np.inf,-np.inf],np.nan)

def f13mc_f13_macd_variants_histskew_12_26_9_60d_jerk_v030_signal(closeadj):
    m=_ema(closeadj,12)-_ema(closeadj,26); h = m - _ema(m, 9)
    b = h.rolling(60, min_periods=30).skew()
    return(b-2.0*b.shift(21)+b.shift(42)).replace([np.inf,-np.inf],np.nan)

def f13mc_f13_macd_variants_histkurt_12_26_9_80d_jerk_v031_signal(closeadj):
    m=_ema(closeadj,12)-_ema(closeadj,26); h = m - _ema(m, 9)
    b = h.rolling(80, min_periods=40).kurt()
    return(b-2.0*b.shift(21)+b.shift(42)).replace([np.inf,-np.inf],np.nan)

def f13mc_f13_macd_variants_histrank_19_39_13_120d_jerk_v032_signal(closeadj):
    m = _ema(closeadj, 19) - _ema(closeadj, 39); h = m - _ema(m, 13)
    b = h.rolling(120, min_periods=60).rank(pct=True)
    return(b-2.0*b.shift(21)+b.shift(42)).replace([np.inf,-np.inf],np.nan)

def f13mc_f13_macd_variants_macdrank_12_26_120d_jerk_v033_signal(closeadj):
    m=_ema(closeadj,12)-_ema(closeadj,26)
    b = m.rolling(120, min_periods=60).rank(pct=True)
    return(b-2.0*b.shift(21)+b.shift(42)).replace([np.inf,-np.inf],np.nan)

def f13mc_f13_macd_variants_macdz_12_26_60d_jerk_v034_signal(closeadj):
    m=_ema(closeadj,12)-_ema(closeadj,26)
    mu = m.rolling(60, min_periods=30).mean(); sd = m.rolling(60, min_periods=30).std()
    b = (m - mu) / sd.replace(0.0, np.nan)
    return(b-2.0*b.shift(21)+b.shift(42)).replace([np.inf,-np.inf],np.nan)

def f13mc_f13_macd_variants_macdbandbreaks_12_26_60d_jerk_v035_signal(closeadj):
    m=_ema(closeadj,12)-_ema(closeadj,26)
    mu = m.rolling(60, min_periods=30).mean(); sd = m.rolling(60, min_periods=30).std()
    upper = mu + 2.0 * sd
    flag = (m > upper).astype(float).where(~upper.isna() & ~m.isna())
    b = flag.rolling(30, min_periods=15).sum()
    return(b-2.0*b.shift(10)+b.shift(20)).replace([np.inf,-np.inf],np.nan)

def f13mc_f13_macd_variants_macdrank_50_200_252d_jerk_v036_signal(closeadj):
    m = _ema(closeadj, 50) - _ema(closeadj, 200)
    b = m.rolling(252, min_periods=120).rank(pct=True)
    return(b-2.0*b.shift(63)+b.shift(126)).replace([np.inf,-np.inf],np.nan)

def f13mc_f13_macd_variants_macdvszero_dist_12_26_60d_jerk_v037_signal(closeadj):
    m=_ema(closeadj,12)-_ema(closeadj,26); sd = m.rolling(60, min_periods=30).std()
    b = m.abs() / sd.replace(0.0, np.nan)
    return(b-2.0*b.shift(21)+b.shift(42)).replace([np.inf,-np.inf],np.nan)

def f13mc_f13_macd_variants_tanhmacdz_19_39_60d_jerk_v038_signal(closeadj):
    m = _ema(closeadj, 19) - _ema(closeadj, 39)
    z = (m - m.rolling(60, min_periods=30).mean()) / m.rolling(60, min_periods=30).std().replace(0.0, np.nan)
    b = np.tanh(z)
    return(b-2.0*b.shift(21)+b.shift(42)).replace([np.inf,-np.inf],np.nan)

def f13mc_f13_macd_variants_tanhhist_8_21_5_jerk_v039_signal(close):
    m = _ema(close, 8) - _ema(close, 21); h = (m - _ema(m, 5)) / close.replace(0.0, np.nan)
    b = np.tanh(h * 200.0)
    return(b-2.0*b.shift(5)+b.shift(10)).replace([np.inf,-np.inf],np.nan)

def f13mc_f13_macd_variants_signhist_50_200_30_jerk_v040_signal(closeadj):
    m = _ema(closeadj, 50) - _ema(closeadj, 200); h = m - _ema(m, 30); b = np.sign(h)
    return(b-2.0*b.shift(21)+b.shift(42)).replace([np.inf,-np.inf],np.nan)

def f13mc_f13_macd_variants_macdslopenorm_12_26_jerk_v041_signal(close):
    m=_ema(close,12)-_ema(close,26); base = m.abs().rolling(20, min_periods=10).mean()
    b = m.diff(5) / base.replace(0.0, np.nan)
    return(b-2.0*b.shift(10)+b.shift(20)).replace([np.inf,-np.inf],np.nan)

def f13mc_f13_macd_variants_histslope5_12_26_9_jerk_v042_signal(close):
    m=_ema(close,12)-_ema(close,26); h = m - _ema(m, 9); b = h.diff(5)
    return(b-2.0*b.shift(10)+b.shift(20)).replace([np.inf,-np.inf],np.nan)

def f13mc_f13_macd_variants_macdcurv_50_200_jerk_v043_signal(closeadj):
    m = _ema(closeadj, 50) - _ema(closeadj, 200); b = m - 2.0 * m.shift(10) + m.shift(20)
    return(b-2.0*b.shift(21)+b.shift(42)).replace([np.inf,-np.inf],np.nan)

def f13mc_f13_macd_variants_histcurv_12_26_9_jerk_v044_signal(close):
    m=_ema(close,12)-_ema(close,26); h = m - _ema(m, 9); b = h - 2.0 * h.shift(3) + h.shift(6)
    return(b-2.0*b.shift(10)+b.shift(20)).replace([np.inf,-np.inf],np.nan)

def f13mc_f13_macd_variants_hma_macd_12_26_jerk_v045_signal(close):
    b = _hma(close, 12) - _hma(close, 26)
    return(b-2.0*b.shift(10)+b.shift(20)).replace([np.inf,-np.inf],np.nan)

def f13mc_f13_macd_variants_dema_macd_12_26_jerk_v046_signal(close):
    b = _dema(close, 12) - _dema(close, 26)
    base = b.abs().rolling(30, min_periods=15).mean()
    jraw = b-2.0*b.shift(21)+b.shift(42)
    return(jraw/base.replace(0.0,np.nan)).replace([np.inf,-np.inf],np.nan)

def f13mc_f13_macd_variants_zlemaMACD_histsign_jerk_v047_signal(close):
    m = _zlema(close, 12) - _zlema(close, 26); h = m - _ema(m, 5); b = np.sign(h)
    return(b-2.0*b.shift(10)+b.shift(20)).replace([np.inf,-np.inf],np.nan)

def f13mc_f13_macd_variants_wilderhist_12_26_9_jerk_v048_signal(close):
    m = _wilder(close, 12) - _wilder(close, 26); b = m - _wilder(m, 9)
    base=b.abs().rolling(20,min_periods=10).mean()
    jraw=b-2.0*b.shift(5)+b.shift(10)
    return(jraw/base.replace(0.0,np.nan)).replace([np.inf,-np.inf],np.nan)

def f13mc_f13_macd_variants_wma_macd_12_26_jerk_v049_signal(close):
    b = _wma(close, 12) - _wma(close, 26)
    return(b-2.0*b.shift(10)+b.shift(20)).replace([np.inf,-np.inf],np.nan)

def f13mc_f13_macd_variants_macdkerdiff_hma_jerk_v050_signal(closeadj):
    h = _hma(closeadj, 12) - _hma(closeadj, 26); e = _ema(closeadj, 12) - _ema(closeadj, 26); b = h - e
    base=b.abs().rolling(20,min_periods=10).mean()
    jraw=b-2.0*b.shift(21)+b.shift(42)
    return(jraw/base.replace(0.0,np.nan)).replace([np.inf,-np.inf],np.nan)

def f13mc_f13_macd_variants_macdkerdiff_dema_jerk_v051_signal(close):
    d = _dema(close, 12) - _dema(close, 26); e = _ema(close, 12) - _ema(close, 26); b = d - e
    base=b.abs().rolling(20,min_periods=10).mean()
    jraw=b-2.0*b.shift(21)+b.shift(42)
    return(jraw/base.replace(0.0,np.nan)).replace([np.inf,-np.inf],np.nan)

def f13mc_f13_macd_variants_macdkerdiff_zlema_hma_jerk_v052_signal(close):
    z = _zlema(close, 12) - _zlema(close, 26); h = _hma(close, 12) - _hma(close, 26); b = z - h
    return(b-2.0*b.shift(10)+b.shift(20)).replace([np.inf,-np.inf],np.nan)

def f13mc_f13_macd_variants_macdkerdiff_wilder_jerk_v053_signal(closeadj):
    w = _wilder(closeadj, 12) - _wilder(closeadj, 26); e = _ema(closeadj, 12) - _ema(closeadj, 26); b = w - e
    base=b.abs().rolling(20,min_periods=10).mean()
    jraw=b-2.0*b.shift(21)+b.shift(42)
    return(jraw/base.replace(0.0,np.nan)).replace([np.inf,-np.inf],np.nan)

def f13mc_f13_macd_variants_macdsign_xor_jerk_v054_signal(close):
    a = _ema(close, 8) - _ema(close, 21); c = _ema(close, 12) - _ema(close, 26); b = np.sign(a) - np.sign(c)
    return(b-2.0*b.shift(10)+b.shift(20)).replace([np.inf,-np.inf],np.nan)

def f13mc_f13_macd_variants_macddiff_fastslow_jerk_v055_signal(closeadj):
    a1 = (_ema(closeadj, 5) - _ema(closeadj, 35)) / _ema(closeadj, 35).replace(0.0, np.nan)
    a2 = (_ema(closeadj, 19) - _ema(closeadj, 39)) / _ema(closeadj, 39).replace(0.0, np.nan)
    b = a1 - a2
    return(b-2.0*b.shift(21)+b.shift(42)).replace([np.inf,-np.inf],np.nan)

def f13mc_f13_macd_variants_macddiff_short_long_jerk_v056_signal(closeadj):
    a = _ema(closeadj, 8) - _ema(closeadj, 21); c = _ema(closeadj, 50) - _ema(closeadj, 200); b = np.sign(a) - np.sign(c)
    return(b-2.0*b.shift(21)+b.shift(42)).replace([np.inf,-np.inf],np.nan)

def f13mc_f13_macd_variants_macdvolconf_12_26_jerk_v057_signal(close, volume):
    m=_ema(close,12)-_ema(close,26)
    vs = np.sign(volume - volume.rolling(20, min_periods=20).mean())
    b = np.sign(m) * vs
    return(b-2.0*b.shift(10)+b.shift(20)).replace([np.inf,-np.inf],np.nan)

def f13mc_f13_macd_variants_vwmacd_norm_12_26_jerk_v058_signal(close, volume):
    pv = close * volume
    n12 = pv.rolling(12, min_periods=12).sum() / volume.rolling(12, min_periods=12).sum().replace(0.0, np.nan)
    n26 = pv.rolling(26, min_periods=26).sum() / volume.rolling(26, min_periods=26).sum().replace(0.0, np.nan)
    b = (n12 - n26) / n26.replace(0.0, np.nan)
    return(b-2.0*b.shift(10)+b.shift(20)).replace([np.inf,-np.inf],np.nan)

def f13mc_f13_macd_variants_volmacd_12_26_jerk_v059_signal(volume):
    lv = np.log(volume.replace(0.0, np.nan)); b = _ema(lv, 12) - _ema(lv, 26)
    return(b-2.0*b.shift(10)+b.shift(20)).replace([np.inf,-np.inf],np.nan)

def f13mc_f13_macd_variants_macdpx_agree_12_26_10d_jerk_v060_signal(close):
    m=_ema(close,12)-_ema(close,26); b = np.sign(m.diff(10)) * np.sign(close.diff(10))
    return(b-2.0*b.shift(10)+b.shift(20)).replace([np.inf,-np.inf],np.nan)

def f13mc_f13_macd_variants_macdpx_disag_19_39_30d_jerk_v061_signal(closeadj):
    m = _ema(closeadj, 19) - _ema(closeadj, 39)
    ms = np.sign(m.diff(21)); ps = np.sign(closeadj.diff(21))
    dis = (ms * ps < 0.0).astype(float).where(~ms.isna() & ~ps.isna())
    b = dis.rolling(30, min_periods=30).sum()
    return(b-2.0*b.shift(21)+b.shift(42)).replace([np.inf,-np.inf],np.nan)

def f13mc_f13_macd_variants_macdvspx_diff_50_200_jerk_v062_signal(closeadj):
    m = _ema(closeadj, 50) - _ema(closeadj, 200)
    mz = (m - m.rolling(60, min_periods=30).mean()) / m.rolling(60, min_periods=30).std().replace(0.0, np.nan)
    cz = (closeadj - closeadj.rolling(60, min_periods=30).mean()) / closeadj.rolling(60, min_periods=30).std().replace(0.0, np.nan)
    b = mz - cz
    return(b-2.0*b.shift(21)+b.shift(42)).replace([np.inf,-np.inf],np.nan)

def f13mc_f13_macd_variants_histaccelsign_12_26_9_jerk_v063_signal(close):
    m=_ema(close,12)-_ema(close,26); h = m - _ema(m, 9); ss = np.sign(h.diff(3)); b = ss - ss.shift(5)
    return(b-2.0*b.shift(10)+b.shift(20)).replace([np.inf,-np.inf],np.nan)

def f13mc_f13_macd_variants_triplecross_12_26_9_30d_jerk_v064_signal(close):
    m=_ema(close,12)-_ema(close,26); h = m - _ema(m, 9); s = np.sign(h)
    flip = (s != s.shift(1)).astype(float).where(~s.isna() & ~s.shift(1).isna())
    b = flip.rolling(30, min_periods=30).sum()
    return(b-2.0*b.shift(10)+b.shift(20)).replace([np.inf,-np.inf],np.nan)

def f13mc_f13_macd_variants_histslopechange_19_39_13_jerk_v065_signal(closeadj):
    m = _ema(closeadj, 19) - _ema(closeadj, 39); h = m - _ema(m, 13); sl = np.sign(h.diff(5)); b = sl - sl.shift(5)
    return(b-2.0*b.shift(21)+b.shift(42)).replace([np.inf,-np.inf],np.nan)

def f13mc_f13_macd_variants_histovermacd_12_26_9_jerk_v066_signal(close):
    m=_ema(close,12)-_ema(close,26); h = m - _ema(m, 9); b = h / m.abs().replace(0.0, np.nan)
    return(b-2.0*b.shift(10)+b.shift(20)).replace([np.inf,-np.inf],np.nan)

def f13mc_f13_macd_variants_histoversig_12_26_9_jerk_v067_signal(close):
    m=_ema(close,12)-_ema(close,26); sig = _ema(m, 9); h = m - sig; b = h / sig.abs().replace(0.0, np.nan)
    return(b-2.0*b.shift(10)+b.shift(20)).replace([np.inf,-np.inf],np.nan)

def f13mc_f13_macd_variants_signoverhist_12_26_9_jerk_v068_signal(close):
    m=_ema(close,12)-_ema(close,26); sig = _ema(m, 9); h = m - sig
    ratio = h.abs() / sig.abs().replace(0.0, np.nan); b = np.sign(sig) * (1.0 - np.tanh(ratio))
    return(b-2.0*b.shift(10)+b.shift(20)).replace([np.inf,-np.inf],np.nan)

def f13mc_f13_macd_variants_macdstd_60d_jerk_v069_signal(closeadj):
    m=_ema(closeadj,12)-_ema(closeadj,26); b = m.rolling(60, min_periods=30).std()
    return(b-2.0*b.shift(21)+b.shift(42)).replace([np.inf,-np.inf],np.nan)

def f13mc_f13_macd_variants_medmacd_12_26_15_jerk_v070_signal(close):
    m=_ema(close,12)-_ema(close,26); b = m.rolling(15, min_periods=15).median()
    return(b-2.0*b.shift(10)+b.shift(20)).replace([np.inf,-np.inf],np.nan)

def f13mc_f13_macd_variants_macd_vs_smaMACD_signdays_jerk_v071_signal(close):
    m=_ema(close,12)-_ema(close,26); sma20 = m.rolling(20, min_periods=20).mean()
    s = np.sign(m - sma20); flip = (s != s.shift(1)).astype(float).where(~s.isna() & ~s.shift(1).isna())
    def _ds(x):
        idx = np.where(x > 0.5)[0]
        return 60.0 if idx.size == 0 else float(len(x) - 1 - idx[-1])
    b = flip.rolling(60, min_periods=20).apply(_ds, raw=True)
    return(b-2.0*b.shift(10)+b.shift(20)).replace([np.inf,-np.inf],np.nan)

def f13mc_f13_macd_variants_macdcomposite_jerk_v072_signal(closeadj):
    m1 = (_ema(closeadj, 8) - _ema(closeadj, 21)) / _ema(closeadj, 21).replace(0.0, np.nan)
    m2 = (_ema(closeadj, 19) - _ema(closeadj, 39)) / _ema(closeadj, 39).replace(0.0, np.nan)
    m3 = (_ema(closeadj, 50) - _ema(closeadj, 200)) / _ema(closeadj, 200).replace(0.0, np.nan)
    b = (m1 + m2 + m3) / 3.0
    return(b-2.0*b.shift(63)+b.shift(126)).replace([np.inf,-np.inf],np.nan)

def f13mc_f13_macd_variants_macdratio_log_50_200_jerk_v073_signal(closeadj):
    e1 = _ema(closeadj, 50); e2 = _ema(closeadj, 200)
    lr = np.log(e1.replace(0.0, np.nan) / e2.replace(0.0, np.nan))
    b = lr - lr.rolling(60, min_periods=30).mean()
    return(b-2.0*b.shift(21)+b.shift(42)).replace([np.inf,-np.inf],np.nan)

def f13mc_f13_macd_variants_histsignconf_12_26_9_jerk_v074_signal(close):
    m=_ema(close,12)-_ema(close,26); sig = _ema(m, 9); h = m - sig
    b = (np.sign(h) * np.sign(h.diff(3))).where(~h.isna() & ~h.shift(3).isna())
    return(b-2.0*b.shift(10)+b.shift(20)).replace([np.inf,-np.inf],np.nan)

def f13mc_f13_macd_variants_macdbias_19_39_60d_jerk_v075_signal(closeadj):
    m = _ema(closeadj, 19) - _ema(closeadj, 39); sd = m.rolling(60, min_periods=30).std()
    b = m / sd.replace(0.0, np.nan)
    return(b-2.0*b.shift(21)+b.shift(42)).replace([np.inf,-np.inf],np.nan)


# --- File 2 jerks (076-150) ------------------------------------------------


def f13mc_f13_macd_variants_macd_hl2_12_26_jerk_v076_signal(high, low):
    hl2 = (high + low) / 2.0; b = _ema(hl2, 12) - _ema(hl2, 26)
    base=b.abs().rolling(20,min_periods=10).mean()
    jraw=b-2.0*b.shift(5)+b.shift(10)
    return(jraw/base.replace(0.0,np.nan)).replace([np.inf,-np.inf],np.nan)

def f13mc_f13_macd_variants_macd_hlc3_19_39_jerk_v077_signal(high, low, closeadj):
    hlc3 = (high + low + closeadj) / 3.0; b = _ema(hlc3, 19) - _ema(hlc3, 39)
    base = b.abs().rolling(40, min_periods=20).mean()
    jraw = b-2.0*b.shift(10)+b.shift(20)
    return(jraw/base.replace(0.0,np.nan)).replace([np.inf,-np.inf],np.nan)

def f13mc_f13_macd_variants_macd_ohlc4_minus_close_jerk_v078_signal(open, high, low, close):
    ohlc4 = (open + high + low + close) / 4.0
    a = _ema(ohlc4, 12) - _ema(ohlc4, 26); c = _ema(close, 12) - _ema(close, 26); b = a - c
    return(b-2.0*b.shift(10)+b.shift(20)).replace([np.inf,-np.inf],np.nan)

def f13mc_f13_macd_variants_macd_high_minus_close_12_26_jerk_v079_signal(high, close):
    a = _ema(high, 12) - _ema(high, 26); c = _ema(close, 12) - _ema(close, 26); b = a - c
    return(b-2.0*b.shift(10)+b.shift(20)).replace([np.inf,-np.inf],np.nan)

def f13mc_f13_macd_variants_macdLow_streak_19_39_jerk_v080_signal(low):
    m = _ema(low, 19) - _ema(low, 39)
    above = (m > 0.0).astype(float).where(~m.isna())
    grp = (above != above.shift(1)).cumsum(); run = above.groupby(grp).cumcount() + 1.0
    out = np.where(above > 0.5, run, -run); b = pd.Series(out, index=low.index, dtype=float).clip(-80.0, 80.0).where(~above.isna())
    return(b-2.0*b.shift(21)+b.shift(42)).replace([np.inf,-np.inf],np.nan)

def f13mc_f13_macd_variants_macd_highlow_diff_19_39_jerk_v081_signal(high, low):
    mh = _ema(high, 19) - _ema(high, 39); ml = _ema(low, 19) - _ema(low, 39); b = mh - ml
    return(b-2.0*b.shift(21)+b.shift(42)).replace([np.inf,-np.inf],np.nan)

def f13mc_f13_macd_variants_ppo_quantile_12_26_252d_jerk_v082_signal(closeadj):
    e12 = _ema(closeadj, 12); e26 = _ema(closeadj, 26)
    ppo = (e12 - e26) / e26.replace(0.0, np.nan) * 100.0
    b = ppo.rolling(252, min_periods=120).rank(pct=True)
    return(b-2.0*b.shift(63)+b.shift(126)).replace([np.inf,-np.inf],np.nan)

def f13mc_f13_macd_variants_ppo_xover_count_60d_jerk_v083_signal(closeadj):
    e12 = _ema(closeadj, 12); e26 = _ema(closeadj, 26)
    ppo = (e12 - e26) / e26.replace(0.0, np.nan) * 100.0
    s = np.sign(ppo); flip = (s != s.shift(1)).astype(float).where(~s.isna() & ~s.shift(1).isna())
    b = flip.rolling(60, min_periods=60).sum()
    return(b-2.0*b.shift(21)+b.shift(42)).replace([np.inf,-np.inf],np.nan)

def f13mc_f13_macd_variants_ppo_50_200_z_jerk_v084_signal(closeadj):
    e1 = _ema(closeadj, 50); e2 = _ema(closeadj, 200)
    ppo = (e1 - e2) / e2.replace(0.0, np.nan) * 100.0
    mu = ppo.rolling(60, min_periods=30).mean(); sd = ppo.rolling(60, min_periods=30).std()
    b = (ppo - mu) / sd.replace(0.0, np.nan)
    return(b-2.0*b.shift(21)+b.shift(42)).replace([np.inf,-np.inf],np.nan)

def f13mc_f13_macd_variants_macd_logret_12_26_jerk_v085_signal(close):
    lr = np.log(close / close.shift(1).replace(0.0, np.nan)); b = _ema(lr, 12) - _ema(lr, 26)
    return(b-2.0*b.shift(10)+b.shift(20)).replace([np.inf,-np.inf],np.nan)

def f13mc_f13_macd_variants_macd_absret_12_26_jerk_v086_signal(close):
    ar = (np.log(close / close.shift(1).replace(0.0, np.nan))).abs(); b = _ema(ar, 12) - _ema(ar, 26)
    return(b-2.0*b.shift(10)+b.shift(20)).replace([np.inf,-np.inf],np.nan)

def f13mc_f13_macd_variants_macd_squaredret_19_39_jerk_v087_signal(closeadj):
    sr = (np.log(closeadj / closeadj.shift(1).replace(0.0, np.nan))) ** 2.0; b = _ema(sr, 19) - _ema(sr, 39)
    return(b-2.0*b.shift(21)+b.shift(42)).replace([np.inf,-np.inf],np.nan)

def f13mc_f13_macd_variants_obv_macd_12_26_jerk_v088_signal(close, volume):
    obv = (np.sign(close.diff()) * volume).cumsum(skipna=True); b = _ema(obv, 12) - _ema(obv, 26)
    return(b-2.0*b.shift(10)+b.shift(20)).replace([np.inf,-np.inf],np.nan)

def f13mc_f13_macd_variants_obv_macd_hist_19_39_9_jerk_v089_signal(close, volume):
    obv = (np.sign(close.diff()) * volume).cumsum(skipna=True)
    m = _ema(obv, 19) - _ema(obv, 39); b = m - _ema(m, 9)
    return(b-2.0*b.shift(21)+b.shift(42)).replace([np.inf,-np.inf],np.nan)

def f13mc_f13_macd_variants_pvt_macd_12_26_jerk_v090_signal(close, volume):
    pct = close.pct_change(); pvt = (volume * pct).cumsum(skipna=True)
    b = _ema(pvt, 12) - _ema(pvt, 26)
    return(b-2.0*b.shift(10)+b.shift(20)).replace([np.inf,-np.inf],np.nan)

def f13mc_f13_macd_variants_volMACD_sign_12_26_jerk_v091_signal(volume):
    m = _ema(volume, 12) - _ema(volume, 26); b = np.sign(m)
    return(b-2.0*b.shift(10)+b.shift(20)).replace([np.inf,-np.inf],np.nan)

def f13mc_f13_macd_variants_macd_over_atr_sign_12_26_14_jerk_v092_signal(high, low, close):
    m=_ema(close,12)-_ema(close,26); atr = _atr(high, low, close, 14)
    strong = (m.abs() > atr).astype(float).where(~atr.isna() & ~m.isna()); b = np.sign(m) * strong
    return(b-2.0*b.shift(10)+b.shift(20)).replace([np.inf,-np.inf],np.nan)

def f13mc_f13_macd_variants_macd_over_atr_streak_50_200_50_jerk_v093_signal(high, low, closeadj):
    m = _ema(closeadj, 50) - _ema(closeadj, 200); atr = _atr(high, low, closeadj, 50)
    r = m / atr.replace(0.0, np.nan)
    above = (r > 0.0).astype(float).where(~r.isna())
    grp = (above != above.shift(1)).cumsum(); run = above.groupby(grp).cumcount() + 1.0
    out = np.where(above > 0.5, run, -run); b = pd.Series(out, index=closeadj.index, dtype=float).clip(-100.0, 100.0).where(~above.isna())
    return(b-2.0*b.shift(63)+b.shift(126)).replace([np.inf,-np.inf],np.nan)

def f13mc_f13_macd_variants_hist_over_atr_sign_12_26_9_14_jerk_v094_signal(high, low, close):
    m=_ema(close,12)-_ema(close,26); h = m - _ema(m, 9); atr = _atr(high, low, close, 14)
    strong = (h.abs() > 0.5 * atr).astype(float).where(~atr.isna() & ~h.isna()); b = np.sign(h) * strong
    return(b-2.0*b.shift(10)+b.shift(20)).replace([np.inf,-np.inf],np.nan)

def f13mc_f13_macd_variants_sign_macd_logret_12_26_jerk_v095_signal(close):
    lr = np.log(close / close.shift(1).replace(0.0, np.nan)); m = _ema(lr, 12) - _ema(lr, 26); b = np.sign(m)
    return(b-2.0*b.shift(10)+b.shift(20)).replace([np.inf,-np.inf],np.nan)

def f13mc_f13_macd_variants_sign_macd_obv_12_26_jerk_v096_signal(close, volume):
    obv = (np.sign(close.diff()) * volume).cumsum(skipna=True); m = _ema(obv, 12) - _ema(obv, 26); b = np.sign(m)
    return(b-2.0*b.shift(10)+b.shift(20)).replace([np.inf,-np.inf],np.nan)

def f13mc_f13_macd_variants_dayssince_obv_x_12_26_jerk_v097_signal(close, volume):
    obv = (np.sign(close.diff()) * volume).cumsum(skipna=True)
    m = _ema(obv, 12) - _ema(obv, 26); s = np.sign(m)
    flip = (s != s.shift(1)).astype(float).where(~s.isna() & ~s.shift(1).isna())
    def _ds(x):
        idx = np.where(x > 0.5)[0]
        return 80.0 if idx.size == 0 else float(len(x) - 1 - idx[-1])
    b = flip.rolling(80, min_periods=20).apply(_ds, raw=True)
    return(b-2.0*b.shift(10)+b.shift(20)).replace([np.inf,-np.inf],np.nan)

def f13mc_f13_macd_variants_streak_logretmacd_12_26_jerk_v098_signal(close):
    lr = np.log(close / close.shift(1).replace(0.0, np.nan)); m = _ema(lr, 12) - _ema(lr, 26)
    above = (m > 0.0).astype(float).where(~m.isna())
    grp = (above != above.shift(1)).cumsum(); run = above.groupby(grp).cumcount() + 1.0
    out = np.where(above > 0.5, run, -run); b = pd.Series(out, index=close.index, dtype=float).clip(-50.0, 50.0).where(~above.isna())
    return(b-2.0*b.shift(10)+b.shift(20)).replace([np.inf,-np.inf],np.nan)

def f13mc_f13_macd_variants_macd_obv_pos_state_jerk_v099_signal(close, volume):
    obv = (np.sign(close.diff()) * volume).cumsum(skipna=True)
    mo = _ema(obv, 12) - _ema(obv, 26); mp = _ema(close, 12) - _ema(close, 26)
    b = np.sign(mo) + np.sign(mp)
    return(b-2.0*b.shift(10)+b.shift(20)).replace([np.inf,-np.inf],np.nan)

def f13mc_f13_macd_variants_hist_hl2_z_60d_jerk_v100_signal(high, low):
    hl2 = (high + low) / 2.0; m = _ema(hl2, 12) - _ema(hl2, 26); h = m - _ema(m, 9)
    mu = h.rolling(60, min_periods=30).mean(); sd = h.rolling(60, min_periods=30).std()
    b = (h - mu) / sd.replace(0.0, np.nan)
    return(b-2.0*b.shift(21)+b.shift(42)).replace([np.inf,-np.inf],np.nan)

def f13mc_f13_macd_variants_hist_logret_8_21_5_jerk_v101_signal(close):
    lr = np.log(close / close.shift(1).replace(0.0, np.nan)); m = _ema(lr, 8) - _ema(lr, 21); b = m - _ema(m, 5)
    return(b-2.0*b.shift(5)+b.shift(10)).replace([np.inf,-np.inf],np.nan)

def f13mc_f13_macd_variants_hist_obv_12_26_9_jerk_v102_signal(close, volume):
    obv = (np.sign(close.diff()) * volume).cumsum(skipna=True); m = _ema(obv, 12) - _ema(obv, 26); b = m - _ema(m, 9)
    return(b-2.0*b.shift(10)+b.shift(20)).replace([np.inf,-np.inf],np.nan)

def f13mc_f13_macd_variants_slope_hl2_macd_12_26_jerk_v103_signal(high, low):
    hl2 = (high + low) / 2.0; m = _ema(hl2, 12) - _ema(hl2, 26); b = m.diff(5)
    base=b.abs().rolling(20,min_periods=10).mean()
    jraw=b-2.0*b.shift(10)+b.shift(20)
    return(jraw/base.replace(0.0,np.nan)).replace([np.inf,-np.inf],np.nan)

def f13mc_f13_macd_variants_curv_logret_macd_12_26_jerk_v104_signal(close):
    lr = np.log(close / close.shift(1).replace(0.0, np.nan)); m = _ema(lr, 12) - _ema(lr, 26)
    b = m - 2.0 * m.shift(5) + m.shift(10)
    return(b-2.0*b.shift(10)+b.shift(20)).replace([np.inf,-np.inf],np.nan)

def f13mc_f13_macd_variants_obv_macd_z_19_39_60d_jerk_v105_signal(close, volume):
    obv = (np.sign(close.diff()) * volume).cumsum(skipna=True); m = _ema(obv, 19) - _ema(obv, 39)
    mu = m.rolling(60, min_periods=30).mean(); sd = m.rolling(60, min_periods=30).std()
    b = (m - mu) / sd.replace(0.0, np.nan)
    return(b-2.0*b.shift(21)+b.shift(42)).replace([np.inf,-np.inf],np.nan)

def f13mc_f13_macd_variants_signal_rank_12_26_9_60d_jerk_v106_signal(closeadj):
    m=_ema(closeadj,12)-_ema(closeadj,26); sig = _ema(m, 9); b = sig.rolling(60, min_periods=30).rank(pct=True)
    return(b-2.0*b.shift(21)+b.shift(42)).replace([np.inf,-np.inf],np.nan)

def f13mc_f13_macd_variants_signalslope_12_26_9_5d_jerk_v107_signal(closeadj):
    m=_ema(closeadj,12)-_ema(closeadj,26); sig = _ema(m, 9); b = sig.diff(5)
    base=b.abs().rolling(20,min_periods=10).mean()
    jraw=b-2.0*b.shift(21)+b.shift(42)
    return(jraw/base.replace(0.0,np.nan)).replace([np.inf,-np.inf],np.nan)

def f13mc_f13_macd_variants_dualsignal_diff_12_26_jerk_v108_signal(close):
    m=_ema(close,12)-_ema(close,26); b = _ema(m, 9) - _ema(m, 21)
    return(b-2.0*b.shift(10)+b.shift(20)).replace([np.inf,-np.inf],np.nan)

def f13mc_f13_macd_variants_macd_lower_band_breaks_60d_jerk_v109_signal(closeadj):
    m=_ema(closeadj,12)-_ema(closeadj,26)
    mu = m.rolling(60, min_periods=30).mean(); sd = m.rolling(60, min_periods=30).std(); lower = mu - 2.0 * sd
    flag = (m < lower).astype(float).where(~lower.isna() & ~m.isna())
    b = flag.rolling(30, min_periods=15).sum()
    return(b-2.0*b.shift(10)+b.shift(20)).replace([np.inf,-np.inf],np.nan)

def f13mc_f13_macd_variants_macd_bandwidth_60d_jerk_v110_signal(closeadj):
    m=_ema(closeadj,12)-_ema(closeadj,26)
    sd = m.rolling(60, min_periods=30).std(); mu = m.rolling(60, min_periods=30).mean()
    b = 4.0 * sd / (mu.abs() + 1e-9)
    return(b-2.0*b.shift(21)+b.shift(42)).replace([np.inf,-np.inf],np.nan)

def f13mc_f13_macd_variants_macd_regime_align_jerk_v111_signal(closeadj):
    a = np.sign(_ema(closeadj, 8) - _ema(closeadj, 21))
    c = np.sign(_ema(closeadj, 19) - _ema(closeadj, 39))
    d = np.sign(_ema(closeadj, 50) - _ema(closeadj, 200))
    b = a + c + d
    return(b-2.0*b.shift(21)+b.shift(42)).replace([np.inf,-np.inf],np.nan)

def f13mc_f13_macd_variants_macd_pair_disagree_count_60d_jerk_v112_signal(closeadj):
    a = np.sign(_ema(closeadj, 8) - _ema(closeadj, 21)); c = np.sign(_ema(closeadj, 50) - _ema(closeadj, 200))
    dis = (a * c < 0.0).astype(float).where(~a.isna() & ~c.isna())
    b = dis.rolling(60, min_periods=30).sum()
    return(b-2.0*b.shift(21)+b.shift(42)).replace([np.inf,-np.inf],np.nan)

def f13mc_f13_macd_variants_macd_x_signal_pair_jerk_v113_signal(close):
    m1 = _ema(close, 8) - _ema(close, 21); h1 = m1 - _ema(m1, 5)
    m2 = _ema(close, 12) - _ema(close, 26); h2 = m2 - _ema(m2, 9)
    b = (np.sign(h1) != np.sign(h2)).astype(float).where(~h1.isna() & ~h2.isna())
    return(b-2.0*b.shift(10)+b.shift(20)).replace([np.inf,-np.inf],np.nan)

def f13mc_f13_macd_variants_ao_rank_5_34_60d_jerk_v114_signal(high, low):
    hl2 = (high + low) / 2.0
    ao = hl2.rolling(5, min_periods=5).mean() - hl2.rolling(34, min_periods=34).mean()
    b = ao.rolling(60, min_periods=30).rank(pct=True)
    return(b-2.0*b.shift(21)+b.shift(42)).replace([np.inf,-np.inf],np.nan)

def f13mc_f13_macd_variants_ac_5_34_jerk_v115_signal(high, low):
    hl2 = (high + low) / 2.0
    ao = hl2.rolling(5, min_periods=5).mean() - hl2.rolling(34, min_periods=34).mean()
    b = ao - ao.rolling(5, min_periods=5).mean()
    return(b-2.0*b.shift(10)+b.shift(20)).replace([np.inf,-np.inf],np.nan)

def f13mc_f13_macd_variants_ao_sign_5_34_jerk_v116_signal(high, low):
    hl2 = (high + low) / 2.0
    ao = hl2.rolling(5, min_periods=5).mean() - hl2.rolling(34, min_periods=34).mean()
    b = np.sign(ao)
    return(b-2.0*b.shift(10)+b.shift(20)).replace([np.inf,-np.inf],np.nan)

def f13mc_f13_macd_variants_kst_sum_jerk_v117_signal(closeadj):
    r10 = closeadj.pct_change(10).rolling(10, min_periods=10).mean()
    r15 = closeadj.pct_change(15).rolling(10, min_periods=10).mean()
    r20 = closeadj.pct_change(20).rolling(10, min_periods=10).mean()
    r30 = closeadj.pct_change(30).rolling(15, min_periods=15).mean()
    b = 1.0 * r10 + 2.0 * r15 + 3.0 * r20 + 4.0 * r30
    return(b-2.0*b.shift(63)+b.shift(126)).replace([np.inf,-np.inf],np.nan)

def f13mc_f13_macd_variants_kst_hist_9_jerk_v118_signal(closeadj):
    r10 = closeadj.pct_change(10).rolling(10, min_periods=10).mean()
    r15 = closeadj.pct_change(15).rolling(10, min_periods=10).mean()
    r20 = closeadj.pct_change(20).rolling(10, min_periods=10).mean()
    r30 = closeadj.pct_change(30).rolling(15, min_periods=15).mean()
    kst = 1.0 * r10 + 2.0 * r15 + 3.0 * r20 + 4.0 * r30
    b = kst - _ema(kst, 9)
    return(b-2.0*b.shift(21)+b.shift(42)).replace([np.inf,-np.inf],np.nan)

def f13mc_f13_macd_variants_atrMACD_14_50_jerk_v119_signal(high, low, close):
    atr = _atr(high, low, close, 14); b = _ema(atr, 14) - _ema(atr, 50)
    return(b-2.0*b.shift(21)+b.shift(42)).replace([np.inf,-np.inf],np.nan)

def f13mc_f13_macd_variants_atrMACD_sign_14_50_jerk_v120_signal(high, low, closeadj):
    atr = _atr(high, low, closeadj, 14); m = _ema(atr, 14) - _ema(atr, 50); b = np.sign(m)
    return(b-2.0*b.shift(21)+b.shift(42)).replace([np.inf,-np.inf],np.nan)

def f13mc_f13_macd_variants_macdrank_19_39_252d_jerk_v121_signal(closeadj):
    m = _ema(closeadj, 19) - _ema(closeadj, 39); b = m.rolling(252, min_periods=120).rank(pct=True)
    return(b-2.0*b.shift(21)+b.shift(42)).replace([np.inf,-np.inf],np.nan)

def f13mc_f13_macd_variants_macdz_50_200_120d_jerk_v122_signal(closeadj):
    m = _ema(closeadj, 50) - _ema(closeadj, 200)
    mu = m.rolling(120, min_periods=60).mean(); sd = m.rolling(120, min_periods=60).std()
    b = (m - mu) / sd.replace(0.0, np.nan)
    return(b-2.0*b.shift(21)+b.shift(42)).replace([np.inf,-np.inf],np.nan)

def f13mc_f13_macd_variants_macd_volconfirm_20d_jerk_v123_signal(close, volume):
    m=_ema(close,12)-_ema(close,26); vol_dev = volume - volume.rolling(20, min_periods=20).mean()
    agree = (np.sign(m) * np.sign(vol_dev) > 0.0).astype(float).where(~m.isna() & ~vol_dev.isna())
    b = agree.rolling(20, min_periods=20).mean()
    return(b-2.0*b.shift(10)+b.shift(20)).replace([np.inf,-np.inf],np.nan)

def f13mc_f13_macd_variants_macd_volMACD_interact_jerk_v124_signal(close, volume):
    mp = _ema(close, 12) - _ema(close, 26)
    lv = np.log(volume.replace(0.0, np.nan)); mv = _ema(lv, 12) - _ema(lv, 26)
    b = np.sign(mp) * np.sign(mv)
    return(b-2.0*b.shift(10)+b.shift(20)).replace([np.inf,-np.inf],np.nan)

def f13mc_f13_macd_variants_hist_autocorr1_60d_jerk_v125_signal(closeadj):
    m=_ema(closeadj,12)-_ema(closeadj,26); h = m - _ema(m, 9)
    b = h.rolling(60, min_periods=30).apply(
        lambda x: float(pd.Series(x).autocorr(lag=1)) if pd.Series(x).std() > 0 else np.nan, raw=False)
    return(b-2.0*b.shift(21)+b.shift(42)).replace([np.inf,-np.inf],np.nan)

def f13mc_f13_macd_variants_macd_autocorr1_60d_jerk_v126_signal(closeadj):
    m=_ema(closeadj,12)-_ema(closeadj,26)
    b = m.rolling(60, min_periods=30).apply(
        lambda x: float(pd.Series(x).autocorr(lag=1)) if pd.Series(x).std() > 0 else np.nan, raw=False)
    return(b-2.0*b.shift(21)+b.shift(42)).replace([np.inf,-np.inf],np.nan)

def f13mc_f13_macd_variants_macd_above_close_state_50_200_jerk_v127_signal(closeadj):
    m = _ema(closeadj, 50) - _ema(closeadj, 200); e200 = _ema(closeadj, 200)
    b = np.sign(m) * np.sign(closeadj - e200)
    return(b-2.0*b.shift(21)+b.shift(42)).replace([np.inf,-np.inf],np.nan)

def f13mc_f13_macd_variants_histflip_50_200_30_event_60d_jerk_v128_signal(closeadj):
    m = _ema(closeadj, 50) - _ema(closeadj, 200); h = m - _ema(m, 30); s = np.sign(h)
    flip = (s != s.shift(1)).astype(float).where(~s.isna() & ~s.shift(1).isna())
    b = flip.rolling(60, min_periods=60).sum()
    return(b-2.0*b.shift(21)+b.shift(42)).replace([np.inf,-np.inf],np.nan)

def f13mc_f13_macd_variants_histflip_19_39_13_event_30d_jerk_v129_signal(closeadj):
    m = _ema(closeadj, 19) - _ema(closeadj, 39); h = m - _ema(m, 13); s = np.sign(h)
    flip = (s != s.shift(1)).astype(float).where(~s.isna() & ~s.shift(1).isna())
    b = flip.rolling(30, min_periods=30).sum()
    return(b-2.0*b.shift(21)+b.shift(42)).replace([np.inf,-np.inf],np.nan)

def f13mc_f13_macd_variants_macd_x_pricez_12_26_60d_jerk_v130_signal(closeadj):
    m=_ema(closeadj,12)-_ema(closeadj,26)
    zp = (closeadj - closeadj.rolling(60, min_periods=30).mean()) / closeadj.rolling(60, min_periods=30).std().replace(0.0, np.nan)
    b = np.sign(m) * np.sign(zp)
    return(b-2.0*b.shift(21)+b.shift(42)).replace([np.inf,-np.inf],np.nan)

def f13mc_f13_macd_variants_macd_medsmoothed_minus_classic_jerk_v131_signal(close):
    med5 = close.rolling(5, min_periods=5).median()
    a = _ema(med5, 12) - _ema(med5, 26); c = _ema(close, 12) - _ema(close, 26); b = a - c
    return(b-2.0*b.shift(10)+b.shift(20)).replace([np.inf,-np.inf],np.nan)

def f13mc_f13_macd_variants_macd_minmaxmid_minus_classic_jerk_v132_signal(high, low, closeadj):
    mid = (low.rolling(5, min_periods=5).min() + high.rolling(5, min_periods=5).max()) / 2.0
    a = _ema(mid, 12) - _ema(mid, 26); c = _ema(closeadj, 12) - _ema(closeadj, 26); b = a - c
    return(b-2.0*b.shift(10)+b.shift(20)).replace([np.inf,-np.inf],np.nan)

def f13mc_f13_macd_variants_histmaxabs_12_26_9_60d_jerk_v134_signal(closeadj):
    m=_ema(closeadj,12)-_ema(closeadj,26); h = (m - _ema(m, 9)).abs()
    b = h.rolling(60, min_periods=30).max()
    return(b-2.0*b.shift(21)+b.shift(42)).replace([np.inf,-np.inf],np.nan)

def f13mc_f13_macd_variants_macdrank_12_50_120d_jerk_v135_signal(closeadj):
    m = _ema(closeadj, 12) - _ema(closeadj, 50); b = m.rolling(120, min_periods=60).rank(pct=True)
    return(b-2.0*b.shift(63)+b.shift(126)).replace([np.inf,-np.inf],np.nan)

def f13mc_f13_macd_variants_macd_sign_8_50_jerk_v136_signal(closeadj):
    m = _ema(closeadj, 8) - _ema(closeadj, 50); b = np.sign(m)
    return(b-2.0*b.shift(21)+b.shift(42)).replace([np.inf,-np.inf],np.nan)

def f13mc_f13_macd_variants_macdz_26_100_60d_jerk_v137_signal(closeadj):
    m = _ema(closeadj, 26) - _ema(closeadj, 100)
    mu = m.rolling(60, min_periods=30).mean(); sd = m.rolling(60, min_periods=30).std()
    b = (m - mu) / sd.replace(0.0, np.nan)
    return(b-2.0*b.shift(21)+b.shift(42)).replace([np.inf,-np.inf],np.nan)

def f13mc_f13_macd_variants_macdpctbucket_12_26_60d_jerk_v138_signal(closeadj):
    m=_ema(closeadj,12)-_ema(closeadj,26); r = m.rolling(60, min_periods=30).rank(pct=True)
    b = (r * 5.0).apply(np.floor).clip(0.0, 4.0).where(~r.isna())
    return(b-2.0*b.shift(10)+b.shift(20)).replace([np.inf,-np.inf],np.nan)

def f13mc_f13_macd_variants_macd_pos_streak_run_50_200_jerk_v139_signal(closeadj):
    m = _ema(closeadj, 50) - _ema(closeadj, 200)
    above = (m > 0.0).astype(float).where(~m.isna())
    grp = (above != above.shift(1)).cumsum(); run = above.groupby(grp).cumcount() + 1.0
    out = np.where(above > 0.5, run, 0.0); b = pd.Series(out, index=closeadj.index, dtype=float).clip(0.0, 250.0).where(~above.isna())
    return(b-2.0*b.shift(21)+b.shift(42)).replace([np.inf,-np.inf],np.nan)

def f13mc_f13_macd_variants_dayssince_macd_max_60d_jerk_v140_signal(closeadj):
    m=_ema(closeadj,12)-_ema(closeadj,26)
    def _ds(x):
        return float(len(x) - 1 - int(np.argmax(x)))
    b = m.rolling(60, min_periods=60).apply(_ds, raw=True)
    return(b-2.0*b.shift(21)+b.shift(42)).replace([np.inf,-np.inf],np.nan)

def f13mc_f13_macd_variants_dayssince_hist_min_30d_jerk_v141_signal(closeadj):
    m=_ema(closeadj,12)-_ema(closeadj,26); h = m - _ema(m, 9)
    def _ds(x):
        return float(len(x) - 1 - int(np.argmin(x)))
    b = h.rolling(30, min_periods=30).apply(_ds, raw=True)
    return(b-2.0*b.shift(10)+b.shift(20)).replace([np.inf,-np.inf],np.nan)

def f13mc_f13_macd_variants_diff_macd_pair_rank_60d_jerk_v142_signal(closeadj):
    m1 = _ema(closeadj, 8) - _ema(closeadj, 21); m2 = _ema(closeadj, 12) - _ema(closeadj, 26)
    d = m1 - m2; b = d.rolling(60, min_periods=30).rank(pct=True)
    return(b-2.0*b.shift(21)+b.shift(42)).replace([np.inf,-np.inf],np.nan)

def f13mc_f13_macd_variants_histaccelfrac_12_26_9_30d_jerk_v143_signal(closeadj):
    m=_ema(closeadj,12)-_ema(closeadj,26); h = m - _ema(m, 9)
    accel = (np.sign(h) * np.sign(h.diff(3)) > 0.0).astype(float).where(~h.isna() & ~h.shift(3).isna())
    b = accel.rolling(30, min_periods=30).mean()
    return(b-2.0*b.shift(10)+b.shift(20)).replace([np.inf,-np.inf],np.nan)

def f13mc_f13_macd_variants_hist_vs_emahist_sign_12_26_9_5_jerk_v144_signal(close):
    m=_ema(close,12)-_ema(close,26); h = m - _ema(m, 9); b = np.sign(h - _ema(h, 5))
    return(b-2.0*b.shift(10)+b.shift(20)).replace([np.inf,-np.inf],np.nan)

def f13mc_f13_macd_variants_hist_minus_emahist_12_26_9_5_jerk_v145_signal(close):
    m=_ema(close,12)-_ema(close,26); h = m - _ema(m, 9); b = h - _ema(h, 5)
    base=b.abs().rolling(20,min_periods=10).mean()
    jraw=b-2.0*b.shift(5)+b.shift(10)
    return(jraw/base.replace(0.0,np.nan)).replace([np.inf,-np.inf],np.nan)

def f13mc_f13_macd_variants_macdrelative_rank_30d_jerk_v146_signal(closeadj):
    e1 = _ema(closeadj, 12); e2 = _ema(closeadj, 26); r = (e1 - e2) / e2.replace(0.0, np.nan)
    b = r.rolling(30, min_periods=15).rank(pct=True)
    return(b-2.0*b.shift(10)+b.shift(20)).replace([np.inf,-np.inf],np.nan)

def f13mc_f13_macd_variants_macdHmacdL_sign_12_26_jerk_v147_signal(high, low):
    mh = _ema(high, 12) - _ema(high, 26); ml = _ema(low, 12) - _ema(low, 26); b = np.sign(mh) - np.sign(ml)
    return(b-2.0*b.shift(10)+b.shift(20)).replace([np.inf,-np.inf],np.nan)

def f13mc_f13_macd_variants_macd_x_signal_pair2_60d_jerk_v148_signal(closeadj):
    m = _ema(closeadj, 19) - _ema(closeadj, 39); sig = _ema(m, 13); s = np.sign(m - sig)
    flip = (s != s.shift(1)).astype(float).where(~s.isna() & ~s.shift(1).isna())
    b = flip.rolling(60, min_periods=60).sum()
    return(b-2.0*b.shift(21)+b.shift(42)).replace([np.inf,-np.inf],np.nan)

def f13mc_f13_macd_variants_tanh_macdbias_50_200_60d_jerk_v149_signal(closeadj):
    m = _ema(closeadj, 50) - _ema(closeadj, 200); sd = m.rolling(60, min_periods=30).std()
    b = np.tanh(m / sd.replace(0.0, np.nan))
    return(b-2.0*b.shift(21)+b.shift(42)).replace([np.inf,-np.inf],np.nan)

def f13mc_f13_macd_variants_macdslope_rank_12_26_60d_jerk_v150_signal(closeadj):
    m=_ema(closeadj,12)-_ema(closeadj,26); sl = m.diff(5); b = sl.rolling(60, min_periods=30).rank(pct=True)
    return(b-2.0*b.shift(10)+b.shift(20)).replace([np.inf,-np.inf],np.nan)


# ---------------------------------------------------------------------------
# Registry
# ---------------------------------------------------------------------------


f13_macd_variants_jerk_001_150_REGISTRY = {
"f13mc_f13_macd_variants_macddetrend_12_26_jerk_v001_signal": {"inputs":["close"],"func":f13mc_f13_macd_variants_macddetrend_12_26_jerk_v001_signal},
"f13mc_f13_macd_variants_macdslowdetrend_50_200_jerk_v002_signal": {"inputs":["closeadj"],"func":f13mc_f13_macd_variants_macdslowdetrend_50_200_jerk_v002_signal},
"f13mc_f13_macd_variants_macd_3_10_jerk_v003_signal": {"inputs":["close"],"func":f13mc_f13_macd_variants_macd_3_10_jerk_v003_signal},
"f13mc_f13_macd_variants_macdnorm_12_26_jerk_v004_signal": {"inputs":["close"],"func":f13mc_f13_macd_variants_macdnorm_12_26_jerk_v004_signal},
"f13mc_f13_macd_variants_macdrank_8_21_60d_jerk_v005_signal": {"inputs":["close"],"func":f13mc_f13_macd_variants_macdrank_8_21_60d_jerk_v005_signal},
"f13mc_f13_macd_variants_macdnorm_50_200_jerk_v006_signal": {"inputs":["closeadj"],"func":f13mc_f13_macd_variants_macdnorm_50_200_jerk_v006_signal},
"f13mc_f13_macd_variants_macdsignagree_5_35_19_39_jerk_v007_signal": {"inputs":["close"],"func":f13mc_f13_macd_variants_macdsignagree_5_35_19_39_jerk_v007_signal},
"f13mc_f13_macd_variants_macdnorm_19_39_z_jerk_v008_signal": {"inputs":["closeadj"],"func":f13mc_f13_macd_variants_macdnorm_19_39_z_jerk_v008_signal},
"f13mc_f13_macd_variants_signal_12_26_9_jerk_v009_signal": {"inputs":["close"],"func":f13mc_f13_macd_variants_signal_12_26_9_jerk_v009_signal},
"f13mc_f13_macd_variants_signalnorm_19_39_13_jerk_v010_signal": {"inputs":["closeadj"],"func":f13mc_f13_macd_variants_signalnorm_19_39_13_jerk_v010_signal},
"f13mc_f13_macd_variants_hist_12_26_9_jerk_v011_signal": {"inputs":["close"],"func":f13mc_f13_macd_variants_hist_12_26_9_jerk_v011_signal},
"f13mc_f13_macd_variants_hist_8_21_5_jerk_v012_signal": {"inputs":["close"],"func":f13mc_f13_macd_variants_hist_8_21_5_jerk_v012_signal},
"f13mc_f13_macd_variants_hist_50_200_30_jerk_v013_signal": {"inputs":["closeadj"],"func":f13mc_f13_macd_variants_hist_50_200_30_jerk_v013_signal},
"f13mc_f13_macd_variants_histdetrend_12_26_9_jerk_v014_signal": {"inputs":["close"],"func":f13mc_f13_macd_variants_histdetrend_12_26_9_jerk_v014_signal},
"f13mc_f13_macd_variants_histabs_12_26_9_jerk_v015_signal": {"inputs":["close"],"func":f13mc_f13_macd_variants_histabs_12_26_9_jerk_v015_signal},
"f13mc_f13_macd_variants_signxsig_12_26_9_jerk_v016_signal": {"inputs":["close"],"func":f13mc_f13_macd_variants_signxsig_12_26_9_jerk_v016_signal},
"f13mc_f13_macd_variants_signxzero_12_26_jerk_v017_signal": {"inputs":["close"],"func":f13mc_f13_macd_variants_signxzero_12_26_jerk_v017_signal},
"f13mc_f13_macd_variants_signxzero_50_200_jerk_v018_signal": {"inputs":["closeadj"],"func":f13mc_f13_macd_variants_signxzero_50_200_jerk_v018_signal},
"f13mc_f13_macd_variants_bullstate_12_26_9_jerk_v019_signal": {"inputs":["close"],"func":f13mc_f13_macd_variants_bullstate_12_26_9_jerk_v019_signal},
"f13mc_f13_macd_variants_quaddays_12_26_9_jerk_v020_signal": {"inputs":["close"],"func":f13mc_f13_macd_variants_quaddays_12_26_9_jerk_v020_signal},
"f13mc_f13_macd_variants_histslopesign_12_26_9_jerk_v021_signal": {"inputs":["close"],"func":f13mc_f13_macd_variants_histslopesign_12_26_9_jerk_v021_signal},
"f13mc_f13_macd_variants_dayssincex_12_26_9_jerk_v022_signal": {"inputs":["close"],"func":f13mc_f13_macd_variants_dayssincex_12_26_9_jerk_v022_signal},
"f13mc_f13_macd_variants_dayssincez_19_39_jerk_v023_signal": {"inputs":["closeadj"],"func":f13mc_f13_macd_variants_dayssincez_19_39_jerk_v023_signal},
"f13mc_f13_macd_variants_streakabove_12_26_9_jerk_v024_signal": {"inputs":["close"],"func":f13mc_f13_macd_variants_streakabove_12_26_9_jerk_v024_signal},
"f13mc_f13_macd_variants_streakabovez_50_200_jerk_v025_signal": {"inputs":["closeadj"],"func":f13mc_f13_macd_variants_streakabovez_50_200_jerk_v025_signal},
"f13mc_f13_macd_variants_xcount_12_26_9_60d_jerk_v026_signal": {"inputs":["closeadj"],"func":f13mc_f13_macd_variants_xcount_12_26_9_60d_jerk_v026_signal},
"f13mc_f13_macd_variants_xcountz_19_39_120d_jerk_v027_signal": {"inputs":["closeadj"],"func":f13mc_f13_macd_variants_xcountz_19_39_120d_jerk_v027_signal},
"f13mc_f13_macd_variants_histrank_12_26_9_60d_jerk_v028_signal": {"inputs":["closeadj"],"func":f13mc_f13_macd_variants_histrank_12_26_9_60d_jerk_v028_signal},
"f13mc_f13_macd_variants_histratio_to_macdabs_60d_jerk_v029_signal": {"inputs":["closeadj"],"func":f13mc_f13_macd_variants_histratio_to_macdabs_60d_jerk_v029_signal},
"f13mc_f13_macd_variants_histskew_12_26_9_60d_jerk_v030_signal": {"inputs":["closeadj"],"func":f13mc_f13_macd_variants_histskew_12_26_9_60d_jerk_v030_signal},
"f13mc_f13_macd_variants_histkurt_12_26_9_80d_jerk_v031_signal": {"inputs":["closeadj"],"func":f13mc_f13_macd_variants_histkurt_12_26_9_80d_jerk_v031_signal},
"f13mc_f13_macd_variants_histrank_19_39_13_120d_jerk_v032_signal": {"inputs":["closeadj"],"func":f13mc_f13_macd_variants_histrank_19_39_13_120d_jerk_v032_signal},
"f13mc_f13_macd_variants_macdrank_12_26_120d_jerk_v033_signal": {"inputs":["closeadj"],"func":f13mc_f13_macd_variants_macdrank_12_26_120d_jerk_v033_signal},
"f13mc_f13_macd_variants_macdz_12_26_60d_jerk_v034_signal": {"inputs":["closeadj"],"func":f13mc_f13_macd_variants_macdz_12_26_60d_jerk_v034_signal},
"f13mc_f13_macd_variants_macdbandbreaks_12_26_60d_jerk_v035_signal": {"inputs":["closeadj"],"func":f13mc_f13_macd_variants_macdbandbreaks_12_26_60d_jerk_v035_signal},
"f13mc_f13_macd_variants_macdrank_50_200_252d_jerk_v036_signal": {"inputs":["closeadj"],"func":f13mc_f13_macd_variants_macdrank_50_200_252d_jerk_v036_signal},
"f13mc_f13_macd_variants_macdvszero_dist_12_26_60d_jerk_v037_signal": {"inputs":["closeadj"],"func":f13mc_f13_macd_variants_macdvszero_dist_12_26_60d_jerk_v037_signal},
"f13mc_f13_macd_variants_tanhmacdz_19_39_60d_jerk_v038_signal": {"inputs":["closeadj"],"func":f13mc_f13_macd_variants_tanhmacdz_19_39_60d_jerk_v038_signal},
"f13mc_f13_macd_variants_tanhhist_8_21_5_jerk_v039_signal": {"inputs":["close"],"func":f13mc_f13_macd_variants_tanhhist_8_21_5_jerk_v039_signal},
"f13mc_f13_macd_variants_signhist_50_200_30_jerk_v040_signal": {"inputs":["closeadj"],"func":f13mc_f13_macd_variants_signhist_50_200_30_jerk_v040_signal},
"f13mc_f13_macd_variants_macdslopenorm_12_26_jerk_v041_signal": {"inputs":["close"],"func":f13mc_f13_macd_variants_macdslopenorm_12_26_jerk_v041_signal},
"f13mc_f13_macd_variants_histslope5_12_26_9_jerk_v042_signal": {"inputs":["close"],"func":f13mc_f13_macd_variants_histslope5_12_26_9_jerk_v042_signal},
"f13mc_f13_macd_variants_macdcurv_50_200_jerk_v043_signal": {"inputs":["closeadj"],"func":f13mc_f13_macd_variants_macdcurv_50_200_jerk_v043_signal},
"f13mc_f13_macd_variants_histcurv_12_26_9_jerk_v044_signal": {"inputs":["close"],"func":f13mc_f13_macd_variants_histcurv_12_26_9_jerk_v044_signal},
"f13mc_f13_macd_variants_hma_macd_12_26_jerk_v045_signal": {"inputs":["close"],"func":f13mc_f13_macd_variants_hma_macd_12_26_jerk_v045_signal},
"f13mc_f13_macd_variants_dema_macd_12_26_jerk_v046_signal": {"inputs":["close"],"func":f13mc_f13_macd_variants_dema_macd_12_26_jerk_v046_signal},
"f13mc_f13_macd_variants_zlemaMACD_histsign_jerk_v047_signal": {"inputs":["close"],"func":f13mc_f13_macd_variants_zlemaMACD_histsign_jerk_v047_signal},
"f13mc_f13_macd_variants_wilderhist_12_26_9_jerk_v048_signal": {"inputs":["close"],"func":f13mc_f13_macd_variants_wilderhist_12_26_9_jerk_v048_signal},
"f13mc_f13_macd_variants_wma_macd_12_26_jerk_v049_signal": {"inputs":["close"],"func":f13mc_f13_macd_variants_wma_macd_12_26_jerk_v049_signal},
"f13mc_f13_macd_variants_macdkerdiff_hma_jerk_v050_signal": {"inputs":["closeadj"],"func":f13mc_f13_macd_variants_macdkerdiff_hma_jerk_v050_signal},
"f13mc_f13_macd_variants_macdkerdiff_dema_jerk_v051_signal": {"inputs":["close"],"func":f13mc_f13_macd_variants_macdkerdiff_dema_jerk_v051_signal},
"f13mc_f13_macd_variants_macdkerdiff_zlema_hma_jerk_v052_signal": {"inputs":["close"],"func":f13mc_f13_macd_variants_macdkerdiff_zlema_hma_jerk_v052_signal},
"f13mc_f13_macd_variants_macdkerdiff_wilder_jerk_v053_signal": {"inputs":["closeadj"],"func":f13mc_f13_macd_variants_macdkerdiff_wilder_jerk_v053_signal},
"f13mc_f13_macd_variants_macdsign_xor_jerk_v054_signal": {"inputs":["close"],"func":f13mc_f13_macd_variants_macdsign_xor_jerk_v054_signal},
"f13mc_f13_macd_variants_macddiff_fastslow_jerk_v055_signal": {"inputs":["closeadj"],"func":f13mc_f13_macd_variants_macddiff_fastslow_jerk_v055_signal},
"f13mc_f13_macd_variants_macddiff_short_long_jerk_v056_signal": {"inputs":["closeadj"],"func":f13mc_f13_macd_variants_macddiff_short_long_jerk_v056_signal},
"f13mc_f13_macd_variants_macdvolconf_12_26_jerk_v057_signal": {"inputs":["close", "volume"],"func":f13mc_f13_macd_variants_macdvolconf_12_26_jerk_v057_signal},
"f13mc_f13_macd_variants_vwmacd_norm_12_26_jerk_v058_signal": {"inputs":["close", "volume"],"func":f13mc_f13_macd_variants_vwmacd_norm_12_26_jerk_v058_signal},
"f13mc_f13_macd_variants_volmacd_12_26_jerk_v059_signal": {"inputs":["volume"],"func":f13mc_f13_macd_variants_volmacd_12_26_jerk_v059_signal},
"f13mc_f13_macd_variants_macdpx_agree_12_26_10d_jerk_v060_signal": {"inputs":["close"],"func":f13mc_f13_macd_variants_macdpx_agree_12_26_10d_jerk_v060_signal},
"f13mc_f13_macd_variants_macdpx_disag_19_39_30d_jerk_v061_signal": {"inputs":["closeadj"],"func":f13mc_f13_macd_variants_macdpx_disag_19_39_30d_jerk_v061_signal},
"f13mc_f13_macd_variants_macdvspx_diff_50_200_jerk_v062_signal": {"inputs":["closeadj"],"func":f13mc_f13_macd_variants_macdvspx_diff_50_200_jerk_v062_signal},
"f13mc_f13_macd_variants_histaccelsign_12_26_9_jerk_v063_signal": {"inputs":["close"],"func":f13mc_f13_macd_variants_histaccelsign_12_26_9_jerk_v063_signal},
"f13mc_f13_macd_variants_triplecross_12_26_9_30d_jerk_v064_signal": {"inputs":["close"],"func":f13mc_f13_macd_variants_triplecross_12_26_9_30d_jerk_v064_signal},
"f13mc_f13_macd_variants_histslopechange_19_39_13_jerk_v065_signal": {"inputs":["closeadj"],"func":f13mc_f13_macd_variants_histslopechange_19_39_13_jerk_v065_signal},
"f13mc_f13_macd_variants_histovermacd_12_26_9_jerk_v066_signal": {"inputs":["close"],"func":f13mc_f13_macd_variants_histovermacd_12_26_9_jerk_v066_signal},
"f13mc_f13_macd_variants_histoversig_12_26_9_jerk_v067_signal": {"inputs":["close"],"func":f13mc_f13_macd_variants_histoversig_12_26_9_jerk_v067_signal},
"f13mc_f13_macd_variants_signoverhist_12_26_9_jerk_v068_signal": {"inputs":["close"],"func":f13mc_f13_macd_variants_signoverhist_12_26_9_jerk_v068_signal},
"f13mc_f13_macd_variants_macdstd_60d_jerk_v069_signal": {"inputs":["closeadj"],"func":f13mc_f13_macd_variants_macdstd_60d_jerk_v069_signal},
"f13mc_f13_macd_variants_medmacd_12_26_15_jerk_v070_signal": {"inputs":["close"],"func":f13mc_f13_macd_variants_medmacd_12_26_15_jerk_v070_signal},
"f13mc_f13_macd_variants_macd_vs_smaMACD_signdays_jerk_v071_signal": {"inputs":["close"],"func":f13mc_f13_macd_variants_macd_vs_smaMACD_signdays_jerk_v071_signal},
"f13mc_f13_macd_variants_macdcomposite_jerk_v072_signal": {"inputs":["closeadj"],"func":f13mc_f13_macd_variants_macdcomposite_jerk_v072_signal},
"f13mc_f13_macd_variants_macdratio_log_50_200_jerk_v073_signal": {"inputs":["closeadj"],"func":f13mc_f13_macd_variants_macdratio_log_50_200_jerk_v073_signal},
"f13mc_f13_macd_variants_histsignconf_12_26_9_jerk_v074_signal": {"inputs":["close"],"func":f13mc_f13_macd_variants_histsignconf_12_26_9_jerk_v074_signal},
"f13mc_f13_macd_variants_macdbias_19_39_60d_jerk_v075_signal": {"inputs":["closeadj"],"func":f13mc_f13_macd_variants_macdbias_19_39_60d_jerk_v075_signal},
"f13mc_f13_macd_variants_macd_hl2_12_26_jerk_v076_signal": {"inputs":["high", "low"],"func":f13mc_f13_macd_variants_macd_hl2_12_26_jerk_v076_signal},
"f13mc_f13_macd_variants_macd_hlc3_19_39_jerk_v077_signal": {"inputs":["high", "low", "closeadj"],"func":f13mc_f13_macd_variants_macd_hlc3_19_39_jerk_v077_signal},
"f13mc_f13_macd_variants_macd_ohlc4_minus_close_jerk_v078_signal": {"inputs":["open", "high", "low", "close"],"func":f13mc_f13_macd_variants_macd_ohlc4_minus_close_jerk_v078_signal},
"f13mc_f13_macd_variants_macd_high_minus_close_12_26_jerk_v079_signal": {"inputs":["high", "close"],"func":f13mc_f13_macd_variants_macd_high_minus_close_12_26_jerk_v079_signal},
"f13mc_f13_macd_variants_macdLow_streak_19_39_jerk_v080_signal": {"inputs":["low"],"func":f13mc_f13_macd_variants_macdLow_streak_19_39_jerk_v080_signal},
"f13mc_f13_macd_variants_macd_highlow_diff_19_39_jerk_v081_signal": {"inputs":["high", "low"],"func":f13mc_f13_macd_variants_macd_highlow_diff_19_39_jerk_v081_signal},
"f13mc_f13_macd_variants_ppo_quantile_12_26_252d_jerk_v082_signal": {"inputs":["closeadj"],"func":f13mc_f13_macd_variants_ppo_quantile_12_26_252d_jerk_v082_signal},
"f13mc_f13_macd_variants_ppo_xover_count_60d_jerk_v083_signal": {"inputs":["closeadj"],"func":f13mc_f13_macd_variants_ppo_xover_count_60d_jerk_v083_signal},
"f13mc_f13_macd_variants_ppo_50_200_z_jerk_v084_signal": {"inputs":["closeadj"],"func":f13mc_f13_macd_variants_ppo_50_200_z_jerk_v084_signal},
"f13mc_f13_macd_variants_macd_logret_12_26_jerk_v085_signal": {"inputs":["close"],"func":f13mc_f13_macd_variants_macd_logret_12_26_jerk_v085_signal},
"f13mc_f13_macd_variants_macd_absret_12_26_jerk_v086_signal": {"inputs":["close"],"func":f13mc_f13_macd_variants_macd_absret_12_26_jerk_v086_signal},
"f13mc_f13_macd_variants_macd_squaredret_19_39_jerk_v087_signal": {"inputs":["closeadj"],"func":f13mc_f13_macd_variants_macd_squaredret_19_39_jerk_v087_signal},
"f13mc_f13_macd_variants_obv_macd_12_26_jerk_v088_signal": {"inputs":["close", "volume"],"func":f13mc_f13_macd_variants_obv_macd_12_26_jerk_v088_signal},
"f13mc_f13_macd_variants_obv_macd_hist_19_39_9_jerk_v089_signal": {"inputs":["close", "volume"],"func":f13mc_f13_macd_variants_obv_macd_hist_19_39_9_jerk_v089_signal},
"f13mc_f13_macd_variants_pvt_macd_12_26_jerk_v090_signal": {"inputs":["close", "volume"],"func":f13mc_f13_macd_variants_pvt_macd_12_26_jerk_v090_signal},
"f13mc_f13_macd_variants_volMACD_sign_12_26_jerk_v091_signal": {"inputs":["volume"],"func":f13mc_f13_macd_variants_volMACD_sign_12_26_jerk_v091_signal},
"f13mc_f13_macd_variants_macd_over_atr_sign_12_26_14_jerk_v092_signal": {"inputs":["high", "low", "close"],"func":f13mc_f13_macd_variants_macd_over_atr_sign_12_26_14_jerk_v092_signal},
"f13mc_f13_macd_variants_macd_over_atr_streak_50_200_50_jerk_v093_signal": {"inputs":["high", "low", "closeadj"],"func":f13mc_f13_macd_variants_macd_over_atr_streak_50_200_50_jerk_v093_signal},
"f13mc_f13_macd_variants_hist_over_atr_sign_12_26_9_14_jerk_v094_signal": {"inputs":["high", "low", "close"],"func":f13mc_f13_macd_variants_hist_over_atr_sign_12_26_9_14_jerk_v094_signal},
"f13mc_f13_macd_variants_sign_macd_logret_12_26_jerk_v095_signal": {"inputs":["close"],"func":f13mc_f13_macd_variants_sign_macd_logret_12_26_jerk_v095_signal},
"f13mc_f13_macd_variants_sign_macd_obv_12_26_jerk_v096_signal": {"inputs":["close", "volume"],"func":f13mc_f13_macd_variants_sign_macd_obv_12_26_jerk_v096_signal},
"f13mc_f13_macd_variants_dayssince_obv_x_12_26_jerk_v097_signal": {"inputs":["close", "volume"],"func":f13mc_f13_macd_variants_dayssince_obv_x_12_26_jerk_v097_signal},
"f13mc_f13_macd_variants_streak_logretmacd_12_26_jerk_v098_signal": {"inputs":["close"],"func":f13mc_f13_macd_variants_streak_logretmacd_12_26_jerk_v098_signal},
"f13mc_f13_macd_variants_macd_obv_pos_state_jerk_v099_signal": {"inputs":["close", "volume"],"func":f13mc_f13_macd_variants_macd_obv_pos_state_jerk_v099_signal},
"f13mc_f13_macd_variants_hist_hl2_z_60d_jerk_v100_signal": {"inputs":["high", "low"],"func":f13mc_f13_macd_variants_hist_hl2_z_60d_jerk_v100_signal},
"f13mc_f13_macd_variants_hist_logret_8_21_5_jerk_v101_signal": {"inputs":["close"],"func":f13mc_f13_macd_variants_hist_logret_8_21_5_jerk_v101_signal},
"f13mc_f13_macd_variants_hist_obv_12_26_9_jerk_v102_signal": {"inputs":["close", "volume"],"func":f13mc_f13_macd_variants_hist_obv_12_26_9_jerk_v102_signal},
"f13mc_f13_macd_variants_slope_hl2_macd_12_26_jerk_v103_signal": {"inputs":["high", "low"],"func":f13mc_f13_macd_variants_slope_hl2_macd_12_26_jerk_v103_signal},
"f13mc_f13_macd_variants_curv_logret_macd_12_26_jerk_v104_signal": {"inputs":["close"],"func":f13mc_f13_macd_variants_curv_logret_macd_12_26_jerk_v104_signal},
"f13mc_f13_macd_variants_obv_macd_z_19_39_60d_jerk_v105_signal": {"inputs":["close", "volume"],"func":f13mc_f13_macd_variants_obv_macd_z_19_39_60d_jerk_v105_signal},
"f13mc_f13_macd_variants_signal_rank_12_26_9_60d_jerk_v106_signal": {"inputs":["closeadj"],"func":f13mc_f13_macd_variants_signal_rank_12_26_9_60d_jerk_v106_signal},
"f13mc_f13_macd_variants_signalslope_12_26_9_5d_jerk_v107_signal": {"inputs":["closeadj"],"func":f13mc_f13_macd_variants_signalslope_12_26_9_5d_jerk_v107_signal},
"f13mc_f13_macd_variants_dualsignal_diff_12_26_jerk_v108_signal": {"inputs":["close"],"func":f13mc_f13_macd_variants_dualsignal_diff_12_26_jerk_v108_signal},
"f13mc_f13_macd_variants_macd_lower_band_breaks_60d_jerk_v109_signal": {"inputs":["closeadj"],"func":f13mc_f13_macd_variants_macd_lower_band_breaks_60d_jerk_v109_signal},
"f13mc_f13_macd_variants_macd_bandwidth_60d_jerk_v110_signal": {"inputs":["closeadj"],"func":f13mc_f13_macd_variants_macd_bandwidth_60d_jerk_v110_signal},
"f13mc_f13_macd_variants_macd_regime_align_jerk_v111_signal": {"inputs":["closeadj"],"func":f13mc_f13_macd_variants_macd_regime_align_jerk_v111_signal},
"f13mc_f13_macd_variants_macd_pair_disagree_count_60d_jerk_v112_signal": {"inputs":["closeadj"],"func":f13mc_f13_macd_variants_macd_pair_disagree_count_60d_jerk_v112_signal},
"f13mc_f13_macd_variants_macd_x_signal_pair_jerk_v113_signal": {"inputs":["close"],"func":f13mc_f13_macd_variants_macd_x_signal_pair_jerk_v113_signal},
"f13mc_f13_macd_variants_ao_rank_5_34_60d_jerk_v114_signal": {"inputs":["high", "low"],"func":f13mc_f13_macd_variants_ao_rank_5_34_60d_jerk_v114_signal},
"f13mc_f13_macd_variants_ac_5_34_jerk_v115_signal": {"inputs":["high", "low"],"func":f13mc_f13_macd_variants_ac_5_34_jerk_v115_signal},
"f13mc_f13_macd_variants_ao_sign_5_34_jerk_v116_signal": {"inputs":["high", "low"],"func":f13mc_f13_macd_variants_ao_sign_5_34_jerk_v116_signal},
"f13mc_f13_macd_variants_kst_sum_jerk_v117_signal": {"inputs":["closeadj"],"func":f13mc_f13_macd_variants_kst_sum_jerk_v117_signal},
"f13mc_f13_macd_variants_kst_hist_9_jerk_v118_signal": {"inputs":["closeadj"],"func":f13mc_f13_macd_variants_kst_hist_9_jerk_v118_signal},
"f13mc_f13_macd_variants_atrMACD_14_50_jerk_v119_signal": {"inputs":["high", "low", "close"],"func":f13mc_f13_macd_variants_atrMACD_14_50_jerk_v119_signal},
"f13mc_f13_macd_variants_atrMACD_sign_14_50_jerk_v120_signal": {"inputs":["high", "low", "closeadj"],"func":f13mc_f13_macd_variants_atrMACD_sign_14_50_jerk_v120_signal},
"f13mc_f13_macd_variants_macdrank_19_39_252d_jerk_v121_signal": {"inputs":["closeadj"],"func":f13mc_f13_macd_variants_macdrank_19_39_252d_jerk_v121_signal},
"f13mc_f13_macd_variants_macdz_50_200_120d_jerk_v122_signal": {"inputs":["closeadj"],"func":f13mc_f13_macd_variants_macdz_50_200_120d_jerk_v122_signal},
"f13mc_f13_macd_variants_macd_volconfirm_20d_jerk_v123_signal": {"inputs":["close", "volume"],"func":f13mc_f13_macd_variants_macd_volconfirm_20d_jerk_v123_signal},
"f13mc_f13_macd_variants_macd_volMACD_interact_jerk_v124_signal": {"inputs":["close", "volume"],"func":f13mc_f13_macd_variants_macd_volMACD_interact_jerk_v124_signal},
"f13mc_f13_macd_variants_hist_autocorr1_60d_jerk_v125_signal": {"inputs":["closeadj"],"func":f13mc_f13_macd_variants_hist_autocorr1_60d_jerk_v125_signal},
"f13mc_f13_macd_variants_macd_autocorr1_60d_jerk_v126_signal": {"inputs":["closeadj"],"func":f13mc_f13_macd_variants_macd_autocorr1_60d_jerk_v126_signal},
"f13mc_f13_macd_variants_macd_above_close_state_50_200_jerk_v127_signal": {"inputs":["closeadj"],"func":f13mc_f13_macd_variants_macd_above_close_state_50_200_jerk_v127_signal},
"f13mc_f13_macd_variants_histflip_50_200_30_event_60d_jerk_v128_signal": {"inputs":["closeadj"],"func":f13mc_f13_macd_variants_histflip_50_200_30_event_60d_jerk_v128_signal},
"f13mc_f13_macd_variants_histflip_19_39_13_event_30d_jerk_v129_signal": {"inputs":["closeadj"],"func":f13mc_f13_macd_variants_histflip_19_39_13_event_30d_jerk_v129_signal},
"f13mc_f13_macd_variants_macd_x_pricez_12_26_60d_jerk_v130_signal": {"inputs":["closeadj"],"func":f13mc_f13_macd_variants_macd_x_pricez_12_26_60d_jerk_v130_signal},
"f13mc_f13_macd_variants_macd_medsmoothed_minus_classic_jerk_v131_signal": {"inputs":["close"],"func":f13mc_f13_macd_variants_macd_medsmoothed_minus_classic_jerk_v131_signal},
"f13mc_f13_macd_variants_macd_minmaxmid_minus_classic_jerk_v132_signal": {"inputs":["high", "low", "closeadj"],"func":f13mc_f13_macd_variants_macd_minmaxmid_minus_classic_jerk_v132_signal},
"f13mc_f13_macd_variants_histmaxabs_12_26_9_60d_jerk_v134_signal": {"inputs":["closeadj"],"func":f13mc_f13_macd_variants_histmaxabs_12_26_9_60d_jerk_v134_signal},
"f13mc_f13_macd_variants_macdrank_12_50_120d_jerk_v135_signal": {"inputs":["closeadj"],"func":f13mc_f13_macd_variants_macdrank_12_50_120d_jerk_v135_signal},
"f13mc_f13_macd_variants_macd_sign_8_50_jerk_v136_signal": {"inputs":["closeadj"],"func":f13mc_f13_macd_variants_macd_sign_8_50_jerk_v136_signal},
"f13mc_f13_macd_variants_macdz_26_100_60d_jerk_v137_signal": {"inputs":["closeadj"],"func":f13mc_f13_macd_variants_macdz_26_100_60d_jerk_v137_signal},
"f13mc_f13_macd_variants_macdpctbucket_12_26_60d_jerk_v138_signal": {"inputs":["closeadj"],"func":f13mc_f13_macd_variants_macdpctbucket_12_26_60d_jerk_v138_signal},
"f13mc_f13_macd_variants_macd_pos_streak_run_50_200_jerk_v139_signal": {"inputs":["closeadj"],"func":f13mc_f13_macd_variants_macd_pos_streak_run_50_200_jerk_v139_signal},
"f13mc_f13_macd_variants_dayssince_macd_max_60d_jerk_v140_signal": {"inputs":["closeadj"],"func":f13mc_f13_macd_variants_dayssince_macd_max_60d_jerk_v140_signal},
"f13mc_f13_macd_variants_dayssince_hist_min_30d_jerk_v141_signal": {"inputs":["closeadj"],"func":f13mc_f13_macd_variants_dayssince_hist_min_30d_jerk_v141_signal},
"f13mc_f13_macd_variants_diff_macd_pair_rank_60d_jerk_v142_signal": {"inputs":["closeadj"],"func":f13mc_f13_macd_variants_diff_macd_pair_rank_60d_jerk_v142_signal},
"f13mc_f13_macd_variants_histaccelfrac_12_26_9_30d_jerk_v143_signal": {"inputs":["closeadj"],"func":f13mc_f13_macd_variants_histaccelfrac_12_26_9_30d_jerk_v143_signal},
"f13mc_f13_macd_variants_hist_vs_emahist_sign_12_26_9_5_jerk_v144_signal": {"inputs":["close"],"func":f13mc_f13_macd_variants_hist_vs_emahist_sign_12_26_9_5_jerk_v144_signal},
"f13mc_f13_macd_variants_hist_minus_emahist_12_26_9_5_jerk_v145_signal": {"inputs":["close"],"func":f13mc_f13_macd_variants_hist_minus_emahist_12_26_9_5_jerk_v145_signal},
"f13mc_f13_macd_variants_macdrelative_rank_30d_jerk_v146_signal": {"inputs":["closeadj"],"func":f13mc_f13_macd_variants_macdrelative_rank_30d_jerk_v146_signal},
"f13mc_f13_macd_variants_macdHmacdL_sign_12_26_jerk_v147_signal": {"inputs":["high", "low"],"func":f13mc_f13_macd_variants_macdHmacdL_sign_12_26_jerk_v147_signal},
"f13mc_f13_macd_variants_macd_x_signal_pair2_60d_jerk_v148_signal": {"inputs":["closeadj"],"func":f13mc_f13_macd_variants_macd_x_signal_pair2_60d_jerk_v148_signal},
"f13mc_f13_macd_variants_tanh_macdbias_50_200_60d_jerk_v149_signal": {"inputs":["closeadj"],"func":f13mc_f13_macd_variants_tanh_macdbias_50_200_60d_jerk_v149_signal},
"f13mc_f13_macd_variants_macdslope_rank_12_26_60d_jerk_v150_signal": {"inputs":["closeadj"],"func":f13mc_f13_macd_variants_macdslope_rank_12_26_60d_jerk_v150_signal},
}


# ---------------------------------------------------------------------------
# Self-test
# ---------------------------------------------------------------------------


def _synthetic_inputs(n: int = 800, seed: int = 42) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    seg = n // 4
    rest = n - 3 * seg
    ret = np.concatenate([
        rng.normal(0.0012, 0.011, seg),
        rng.normal(-0.0005, 0.018, seg),
        rng.normal(-0.0010, 0.014, seg),
        rng.normal(0.0008, 0.012, rest),
    ])
    close = 50.0 * np.exp(np.cumsum(ret))
    adj_drift = rng.normal(0.0, 0.0003, size=n).cumsum()
    closeadj = close * np.exp(adj_drift)
    intraday = rng.normal(0.0, 0.008, size=n)
    open_ = close * np.exp(-intraday * 0.5)
    high = np.maximum(close, open_) * np.exp(np.abs(rng.normal(0.0, 0.006, size=n)))
    low = np.minimum(close, open_) * np.exp(-np.abs(rng.normal(0.0, 0.006, size=n)))
    volume = rng.lognormal(mean=13.0, sigma=0.6, size=n)
    idx = pd.RangeIndex(n)
    return pd.DataFrame({
        "open": pd.Series(open_, index=idx, dtype=float),
        "high": pd.Series(high, index=idx, dtype=float),
        "low": pd.Series(low, index=idx, dtype=float),
        "close": pd.Series(close, index=idx, dtype=float),
        "closeadj": pd.Series(closeadj, index=idx, dtype=float),
        "volume": pd.Series(volume, index=idx, dtype=float),
    })


def _self_test() -> None:
    df = _synthetic_inputs(n=800, seed=42)
    results: dict[str, pd.Series] = {}
    for name, entry in f13_macd_variants_jerk_001_150_REGISTRY.items():
        args = [df[col] for col in entry["inputs"]]
        out = entry["func"](*args)
        assert isinstance(out, pd.Series), f"{name}: not a Series"
        assert len(out) == len(df), f"{name}: length mismatch"
        clean = out.dropna()
        assert len(clean) > 0, f"{name}: all NaN"
        assert float(clean.std()) > 0.0 or clean.nunique() > 1, f"{name}: constant/all-zero"
        results[name] = out

    warm = 252
    coverage_ok = sum(1 for s in results.values() if s.iloc[warm:].isna().mean() < 0.5)
    frac = coverage_ok / len(results)
    assert frac >= 0.80, f"NaN-coverage too low: {frac:.2%} have <50% NaN after warm-up"

    aligned = pd.concat({n: results[n] for n in results}, axis=1).iloc[warm:]
    aligned = aligned.replace([np.inf,-np.inf],np.nan)
    corr = aligned.corr(min_periods=50).abs()
    np.fill_diagonal(corr.values, 0.0)
    max_corr = float(corr.max().max())
    if max_corr > 0.95:
        print(f"FAILING max |corr| = {max_corr:.4f}. Top pairs:")
        for i, a in enumerate(corr.columns):
            for j, b in enumerate(corr.columns):
                if j > i and corr.iloc[i, j] > 0.94:
                    print(f"  {a}  vs  {b}  ->  {corr.iloc[i, j]:.4f}")
    assert max_corr <= 0.95 + 1e-9, f"max pairwise |corr|={max_corr:.4f} exceeds 0.95"
    print(f"OK jerk_001_150: {len(results)} features, max |corr|={max_corr:.4f}, coverage_ok={frac:.2%}")


if __name__ == "__main__":
    _self_test()
