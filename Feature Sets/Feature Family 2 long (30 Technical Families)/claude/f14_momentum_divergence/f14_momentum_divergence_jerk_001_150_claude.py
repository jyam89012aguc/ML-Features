"""f14_momentum_divergence jerk features 001-150 (2nd derivative).
Each jerk feature is B - 2*B.shift(k) + B.shift(2k) where k follows the
ROC bracket of the base's primary window. Bracket rule:
  w<=5    -> k=5
  6..21   -> k=5 or 10
  22..63  -> k=10 or 21
  64..200 -> k=21 or 63
  w>200   -> k=63
NaN policy: replace([inf,-inf],nan) at return only.
"""
from __future__ import annotations

import numpy as np
import pandas as pd


def _rsi(s, n):
    d = s.diff(); up = d.clip(lower=0.0); dn = (-d).clip(lower=0.0)
    a = 1.0/float(n)
    au = up.ewm(alpha=a, adjust=False, min_periods=n).mean()
    ad = dn.ewm(alpha=a, adjust=False, min_periods=n).mean()
    return 100.0 - 100.0/(1.0 + au/ad.replace(0.0, np.nan))

def _macd(s, fast, slow):
    return s.ewm(span=fast, adjust=False, min_periods=fast).mean() - s.ewm(span=slow, adjust=False, min_periods=slow).mean()

def _roc(s, n):
    return 100.0*(s/s.shift(n) - 1.0)

def _stoch_k(high, low, close, n):
    ll = low.rolling(n, min_periods=n).min(); hh = high.rolling(n, min_periods=n).max()
    return 100.0*(close - ll)/(hh - ll).replace(0.0, np.nan)

def _wpr(high, low, close, n):
    ll = low.rolling(n, min_periods=n).min(); hh = high.rolling(n, min_periods=n).max()
    return -100.0*(hh - close)/(hh - ll).replace(0.0, np.nan)

def _cmo(s, n):
    d = s.diff()
    up = d.clip(lower=0.0).rolling(n, min_periods=n).sum()
    dn = (-d).clip(lower=0.0).rolling(n, min_periods=n).sum()
    return 100.0*(up - dn)/(up + dn).replace(0.0, np.nan)

def _mfi(high, low, close, volume, n):
    tp = (high + low + close)/3.0; rmf = tp*volume; dn = tp.diff()
    pos = rmf.where(dn>0, 0.0).rolling(n, min_periods=n).sum()
    neg = rmf.where(dn<0, 0.0).rolling(n, min_periods=n).sum()
    return 100.0 - 100.0/(1.0 + pos/neg.replace(0.0, np.nan))

def _ao(high, low):
    mp = (high + low)/2.0
    return mp.rolling(5, min_periods=5).mean() - mp.rolling(34, min_periods=34).mean()

def _ppo(s, fast, slow):
    ef = s.ewm(span=fast, adjust=False, min_periods=fast).mean()
    es = s.ewm(span=slow, adjust=False, min_periods=slow).mean()
    return 100.0*(ef - es)/es.replace(0.0, np.nan)

def _tsi(s, slow, fast):
    m = s.diff()
    e1 = m.ewm(span=slow, adjust=False, min_periods=slow).mean()
    e2 = e1.ewm(span=fast, adjust=False, min_periods=fast).mean()
    a1 = m.abs().ewm(span=slow, adjust=False, min_periods=slow).mean()
    a2 = a1.ewm(span=fast, adjust=False, min_periods=fast).mean()
    return 100.0*e2/a2.replace(0.0, np.nan)

def _j(b, k):
    return (b - 2.0*b.shift(k) + b.shift(2*k)).replace([np.inf,-np.inf], np.nan)


# === Jerk features (2nd derivative of each base feature) ====================


def f14md_f14_momentum_divergence_pslp_rsi_14d_jerk_v001_signal(close):
    n=14
    r=_rsi(close, n)
    pslp=(close - close.shift(n))/close.shift(n).replace(0.0,np.nan)*100.0
    b=pslp - (r - r.shift(n))
    return _j(b, 5)

def f14md_f14_momentum_divergence_pslp_rsi_30d_jerk_v002_signal(closeadj):
    n=30
    r=_rsi(closeadj, 14)
    pslp=(closeadj - closeadj.shift(n))/closeadj.shift(n).replace(0.0,np.nan)*100.0
    b=pslp - (r - r.shift(n))
    return _j(b, 10)

def f14md_f14_momentum_divergence_pslp_macd_20d_jerk_v003_signal(close):
    n=20
    m=_macd(close, 12, 26)/close
    pslp=np.log(close/close.shift(n)); mslp=m - m.shift(n)
    b=pslp - mslp
    return _j(b, 5)

def f14md_f14_momentum_divergence_pslp_roc_25d_jerk_v004_signal(closeadj):
    n=25
    r10=_roc(closeadj, 10); pslp=_roc(closeadj, n); rslp=r10 - r10.shift(n)
    b=pslp - rslp
    return _j(b, 10)

def f14md_f14_momentum_divergence_pslp_stoch_15d_jerk_v005_signal(high, low, close):
    n=15
    k=_stoch_k(high, low, close, 14)
    pslp=(close - close.shift(n))/close.shift(n).replace(0.0,np.nan)*100.0
    b=pslp - (k - k.shift(n))
    return _j(b, 5)

def f14md_f14_momentum_divergence_pslp_cmo_30d_jerk_v006_signal(closeadj):
    n=30
    c=_cmo(closeadj, 14)
    pslp=(closeadj - closeadj.shift(n))/closeadj.shift(n).replace(0.0,np.nan)*100.0
    b=pslp - (c - c.shift(n))
    return _j(b, 21)

def f14md_f14_momentum_divergence_pslp_tsi_40d_jerk_v007_signal(closeadj):
    n=40
    t=_tsi(closeadj, 25, 13)
    pslp=(closeadj - closeadj.shift(n))/closeadj.shift(n).replace(0.0,np.nan)*100.0
    b=pslp - (t - t.shift(n))
    return _j(b, 10)

def f14md_f14_momentum_divergence_pslp_mfi_18d_jerk_v008_signal(high, low, close, volume):
    n=18
    m=_mfi(high, low, close, volume, 14)
    pslp=(close - close.shift(n))/close.shift(n).replace(0.0,np.nan)*100.0
    b=pslp - (m - m.shift(n))
    return _j(b, 10)

def f14md_f14_momentum_divergence_signxor_rsi_10d_jerk_v009_signal(close):
    n=10
    r=_rsi(close, 14)
    sp=np.sign(close.diff(n)); sr=np.sign(r.diff(n))
    b=((sp*sr)<0).astype(float).where(~sp.isna() & ~sr.isna())
    return _j(b, 5)

def f14md_f14_momentum_divergence_signxor_macd_15d_jerk_v010_signal(close):
    n=15
    m=_macd(close, 12, 26)
    sp=np.sign(close.diff(n)); sm=np.sign(m.diff(n))
    b=((sp*sm)<0).astype(float).where(~sp.isna() & ~sm.isna())
    return _j(b, 10)

def f14md_f14_momentum_divergence_signxor_roc_30d_jerk_v011_signal(closeadj):
    n=30
    r=_roc(closeadj, 10)
    sp=np.sign(closeadj.diff(n)); sr=np.sign(r.diff(n))
    b=((sp*sr)<0).astype(float).where(~sp.isna() & ~sr.isna())
    return _j(b, 21)

def f14md_f14_momentum_divergence_signxor_stoch_8d_jerk_v012_signal(high, low, close):
    n=8
    k=_stoch_k(high, low, close, 14)
    sp=np.sign(close.diff(n)); sk=np.sign(k.diff(n))
    b=((sp*sk)<0).astype(float).where(~sp.isna() & ~sk.isna())
    return _j(b, 5)

def f14md_f14_momentum_divergence_corr_rsi_20d_jerk_v013_signal(close):
    n=20
    r=_rsi(close, 14)
    b=close.rolling(n, min_periods=n).corr(r)
    return _j(b, 5)

def f14md_f14_momentum_divergence_corr_rsi_60d_jerk_v014_signal(closeadj):
    n=60
    r=_rsi(closeadj, 14)
    b=closeadj.rolling(n, min_periods=n).corr(r)
    return _j(b, 21)

def f14md_f14_momentum_divergence_corr_macd_40d_jerk_v015_signal(closeadj):
    n=40
    m=_macd(closeadj, 12, 26)
    b=closeadj.rolling(n, min_periods=n).corr(m)
    return _j(b, 10)

def f14md_f14_momentum_divergence_corr_mom_30d_jerk_v016_signal(closeadj):
    n=30
    mom=closeadj.diff()
    b=closeadj.rolling(n, min_periods=n).corr(mom)
    return _j(b, 21)

def f14md_f14_momentum_divergence_corr_tsi_50d_jerk_v017_signal(closeadj):
    n=50
    lp=np.log(closeadj); t=_tsi(closeadj, 25, 13)
    b=lp.rolling(n, min_periods=n).corr(t)
    return _j(b, 10)

def f14md_f14_momentum_divergence_corr_cmo_45d_jerk_v018_signal(closeadj):
    n=45
    ret=np.log(closeadj/closeadj.shift(1)); c=_cmo(closeadj, 20)
    b=ret.rolling(n, min_periods=n).corr(c)
    return _j(b, 21)

def f14md_f14_momentum_divergence_phigh_rsi_low_20d_jerk_v019_signal(close):
    n=20
    r=_rsi(close, 14)
    phi=close.rolling(n, min_periods=n).max(); rhi=r.rolling(n, min_periods=n).max()
    at=(close >= phi*0.999).astype(float).where(~phi.isna())
    b=at*(rhi - r)
    return _j(b, 10)

def f14md_f14_momentum_divergence_plow_rsi_high_30d_jerk_v020_signal(closeadj):
    n=30
    r=_rsi(closeadj, 14)
    plo=closeadj.rolling(n, min_periods=n).min(); rlo=r.rolling(n, min_periods=n).min()
    at=(closeadj <= plo*1.001).astype(float).where(~plo.isna())
    b=at*(r - rlo)
    return _j(b, 21)

def f14md_f14_momentum_divergence_phigh_macd_low_40d_jerk_v021_signal(closeadj):
    n=40
    m=_macd(closeadj, 12, 26)
    phi=closeadj.rolling(n, min_periods=n).max(); mhi=m.rolling(n, min_periods=n).max()
    at=(closeadj >= phi*0.999).astype(float).where(~phi.isna())
    gap=(mhi - m)/m.abs().rolling(n, min_periods=n).mean().replace(0.0, np.nan)
    b=at*gap
    return _j(b, 10)

def f14md_f14_momentum_divergence_phigh_stoch_low_15d_jerk_v022_signal(high, low, close):
    n=15
    k=_stoch_k(high, low, close, 14)
    phi=close.rolling(n, min_periods=n).max(); khi=k.rolling(n, min_periods=n).max()
    at=(close >= phi*0.999).astype(float).where(~phi.isna())
    b=at*(khi - k)
    return _j(b, 5)

def f14md_f14_momentum_divergence_plow_mfi_high_25d_jerk_v023_signal(high, low, close, volume):
    n=25
    m=_mfi(high, low, close, volume, 14)
    plo=close.rolling(n, min_periods=n).min(); mlo=m.rolling(n, min_periods=n).min()
    at=(close <= plo*1.001).astype(float).where(~plo.isna())
    b=at*(m - mlo)
    return _j(b, 10)

def f14md_f14_momentum_divergence_dslph_rsi_60d_jerk_v024_signal(closeadj):
    n=60
    r=_rsi(closeadj, 14)
    phi=closeadj.rolling(n, min_periods=n).max(); rhi=r.rolling(n, min_periods=n).max()
    ev=((closeadj >= phi*0.999) & (r < rhi - 5.0)).astype(float).where(~phi.isna() & ~rhi.isna())
    def _ds(x):
        idx=np.where(x>0.5)[0]; return float(len(x)) if idx.size==0 else float(len(x)-1-idx[-1])
    b=ev.rolling(n, min_periods=n).apply(_ds, raw=True)
    return _j(b, 21)

def f14md_f14_momentum_divergence_dsplh_rsi_80d_jerk_v025_signal(closeadj):
    n=80
    r=_rsi(closeadj, 14)
    plo=closeadj.rolling(n, min_periods=n).min(); rlo=r.rolling(n, min_periods=n).min()
    ev=((closeadj <= plo*1.001) & (r > rlo + 5.0)).astype(float).where(~plo.isna() & ~rlo.isna())
    def _ds(x):
        idx=np.where(x>0.5)[0]; return float(len(x)) if idx.size==0 else float(len(x)-1-idx[-1])
    b=ev.rolling(n, min_periods=n).apply(_ds, raw=True)
    return _j(b, 21)

def f14md_f14_momentum_divergence_rsi_minus_mfi_30d_jerk_v026_signal(high, low, close, volume):
    n=30
    r=_rsi(close, 14); m=_mfi(high, low, close, volume, 14)
    d=r - m; mu=d.rolling(n, min_periods=n).mean(); sd=d.rolling(n, min_periods=n).std(ddof=1)
    b=(d - mu)/sd.replace(0.0, np.nan)
    return _j(b, 21)

def f14md_f14_momentum_divergence_rsi_minus_stoch_40d_jerk_v027_signal(high, low, closeadj):
    n=40
    r=_rsi(closeadj, 14); k=_stoch_k(high, low, closeadj, 14)
    d=r - k; mu=d.rolling(n, min_periods=n).mean(); sd=d.rolling(n, min_periods=n).std(ddof=1)
    b=(d - mu)/sd.replace(0.0, np.nan)
    return _j(b, 10)

def f14md_f14_momentum_divergence_macd_minus_rocsign_30d_jerk_v028_signal(closeadj):
    n=30
    m=_macd(closeadj, 12, 26); rc=_roc(closeadj, 10)
    diff=(np.sign(m) - np.sign(rc)).abs()
    b=diff.rolling(n, min_periods=n).mean()
    return _j(b, 21)

def f14md_f14_momentum_divergence_compxor_rsi_30d_jerk_v029_signal(closeadj):
    n=30
    r=_rsi(closeadj, 14); sp=np.sign(closeadj.diff(5)); sr=np.sign(r.diff(5))
    diff=((sp*sr)<0).astype(float).where(~sp.isna() & ~sr.isna())
    b=diff.rolling(n, min_periods=n).sum()
    return _j(b, 10)

def f14md_f14_momentum_divergence_compxor_macd_25d_jerk_v030_signal(close):
    n=25
    m=_macd(close, 12, 26); sp=np.sign(close.diff()); sm=np.sign(m.diff())
    diff=((sp*sm)<0).astype(float).where(~sp.isna() & ~sm.isna())
    b=diff.rolling(n, min_periods=n).sum()
    return _j(b, 10)

def f14md_f14_momentum_divergence_compabs_roc_45d_jerk_v031_signal(closeadj):
    n=45
    rc=_roc(closeadj, 10)
    d=(closeadj.pct_change(5) - rc.diff(5)/100.0).abs()
    b=d.rolling(n, min_periods=n).mean()
    return _j(b, 21)

def f14md_f14_momentum_divergence_arctan_rsidiv_15d_jerk_v032_signal(close):
    n=15
    r=_rsi(close, 14)
    vol=close.pct_change().rolling(20, min_periods=20).std(ddof=1)
    pslp=(close.pct_change(n))/(vol*np.sqrt(n)).replace(0.0, np.nan)
    rslp=r.diff(n)/100.0
    b=np.arctan(2.0*(pslp - 10.0*rslp))
    return _j(b, 10)

def f14md_f14_momentum_divergence_tanh_corrrsi_30d_jerk_v033_signal(closeadj):
    n=30
    r=_rsi(closeadj, 14)
    c=closeadj.rolling(n, min_periods=n).corr(r)
    b=np.tanh(2.0*c)
    return _j(b, 21)

def f14md_f14_momentum_divergence_sigmoid_macdiv_25d_jerk_v034_signal(closeadj):
    n=25
    m=_macd(closeadj, 12, 26)/closeadj
    pslp=np.log(closeadj/closeadj.shift(n)); mslp=m - m.shift(n)
    x=10.0*(pslp - mslp)
    b=1.0/(1.0 + np.exp(-x)) - 0.5
    return _j(b, 10)

def f14md_f14_momentum_divergence_flipcount_pr_40d_jerk_v035_signal(closeadj):
    n=40
    r=_rsi(closeadj, 14)
    d=closeadj.diff() - r.diff()/2.0
    s=np.sign(d); fl=(s != s.shift(1)).astype(float).where(~s.isna() & ~s.shift(1).isna())
    b=fl.rolling(n, min_periods=n).sum()
    return _j(b, 10)

def f14md_f14_momentum_divergence_cumdiv_rsi_30d_jerk_v036_signal(closeadj):
    n=30
    r=_rsi(closeadj, 14)
    d=(closeadj.pct_change() - r.diff()/100.0).abs()
    b=d.rolling(n, min_periods=n).sum()
    return _j(b, 21)

def f14md_f14_momentum_divergence_cumdiv_macd_50d_jerk_v037_signal(closeadj):
    n=50
    m=_macd(closeadj, 12, 26)/closeadj
    d=closeadj.pct_change() - m.diff()
    b=d.rolling(n, min_periods=n).sum()
    return _j(b, 10)

def f14md_f14_momentum_divergence_convrate_rsi_40d_jerk_v038_signal(closeadj):
    r=_rsi(closeadj, 14)
    cl=closeadj.rolling(40, min_periods=40).corr(r); cs=closeadj.rolling(10, min_periods=10).corr(r)
    b=cs - cl
    return _j(b, 21)

def f14md_f14_momentum_divergence_bullintens_rsi_40d_jerk_v039_signal(closeadj):
    n=40
    r=_rsi(closeadj, 14)
    plo=closeadj.rolling(20, min_periods=20).min(); rlo=r.rolling(20, min_periods=20).min()
    at=(closeadj <= plo*1.001).astype(float).where(~plo.isna())
    b=(at*(r - rlo)).rolling(n, min_periods=n).max()
    return _j(b, 10)

def f14md_f14_momentum_divergence_bearintens_rsi_50d_jerk_v040_signal(closeadj):
    n=50
    r=_rsi(closeadj, 14)
    phi=closeadj.rolling(25, min_periods=25).max(); rhi=r.rolling(25, min_periods=25).max()
    at=(closeadj >= phi*0.999).astype(float).where(~phi.isna())
    b=(at*(rhi - r)).rolling(n, min_periods=n).max()
    return _j(b, 21)

def f14md_f14_momentum_divergence_netdiv_rsi_40d_jerk_v041_signal(closeadj):
    n=40
    r=_rsi(closeadj, 14)
    phi=closeadj.rolling(20, min_periods=20).max(); plo=closeadj.rolling(20, min_periods=20).min()
    rhi=r.rolling(20, min_periods=20).max(); rlo=r.rolling(20, min_periods=20).min()
    bull=((closeadj <= plo*1.001).astype(float)*(r - rlo)).rolling(n, min_periods=n).mean()
    bear=((closeadj >= phi*0.999).astype(float)*(rhi - r)).rolling(n, min_periods=n).mean()
    b=bull - bear
    return _j(b, 10)

def f14md_f14_momentum_divergence_regresid_rsi_30d_jerk_v042_signal(closeadj):
    n=30
    r=_rsi(closeadj, 14); lp=np.log(closeadj)
    def _resid(idx):
        i=int(idx[-1]); a=lp.iloc[i-n+1:i+1].values; bb=r.iloc[i-n+1:i+1].values
        if np.any(~np.isfinite(a)) or np.any(~np.isfinite(bb)): return np.nan
        va=((a-a.mean())**2).sum()
        if va<=0: return np.nan
        beta=((a-a.mean())*(bb-bb.mean())).sum()/va; alpha=bb.mean() - beta*a.mean()
        return float(bb[-1] - (alpha + beta*a[-1]))
    idx_s=pd.Series(np.arange(len(closeadj), dtype=float), index=closeadj.index)
    b=idx_s.rolling(n, min_periods=n).apply(_resid, raw=True)
    return _j(b, 10)

def f14md_f14_momentum_divergence_beta_rsi_60d_jerk_v043_signal(closeadj):
    n=60
    r=_rsi(closeadj, 14); lp=np.log(closeadj)
    cov=lp.rolling(n, min_periods=n).cov(r); var=lp.rolling(n, min_periods=n).var(ddof=1)
    b=cov/var.replace(0.0, np.nan)
    return _j(b, 21)

def f14md_f14_momentum_divergence_r2_pm_50d_jerk_v044_signal(closeadj):
    n=50
    mom=closeadj.diff()
    c=closeadj.rolling(n, min_periods=n).corr(mom)
    b=c*c
    return _j(b, 21)

def f14md_f14_momentum_divergence_curv_rsi_25d_jerk_v045_signal(closeadj):
    n=25
    r=_rsi(closeadj, 14)
    pc=(closeadj - 2*closeadj.shift(n) + closeadj.shift(2*n))/closeadj.shift(n).replace(0.0, np.nan)
    rc=(r - 2*r.shift(n) + r.shift(2*n))/100.0
    b=pc - rc
    return _j(b, 10)

def f14md_f14_momentum_divergence_accel_macd_30d_jerk_v046_signal(closeadj):
    n=30
    m=_macd(closeadj, 12, 26)/closeadj
    pa=closeadj.pct_change(n) - closeadj.pct_change(n).shift(n)
    ma=m.diff(n) - m.diff(n).shift(n)
    b=pa - ma
    return _j(b, 21)

def f14md_f14_momentum_divergence_lag_pr_rsi_30d_jerk_v047_signal(closeadj):
    n=30
    r=_rsi(closeadj, 14); ret=closeadj.pct_change()
    def _bl(idx):
        i=int(idx[-1])
        if i<2*n: return np.nan
        a=ret.iloc[i-n+1:i+1].values; best=0.0; bl=0
        for L in range(-3,4):
            bb=r.shift(L).iloc[i-n+1:i+1].values
            if np.any(~np.isfinite(a)) or np.any(~np.isfinite(bb)): continue
            sa=a.std(); sb=bb.std()
            if sa<=0 or sb<=0: continue
            cc=float(((a-a.mean())*(bb-bb.mean())).mean()/(sa*sb))
            if abs(cc)>abs(best): best=cc; bl=L
        return float(bl)
    idx_s=pd.Series(np.arange(len(closeadj), dtype=float), index=closeadj.index)
    b=idx_s.rolling(n, min_periods=n).apply(_bl, raw=True)
    return _j(b, 10)

def f14md_f14_momentum_divergence_veldiff_rsi_8d_jerk_v048_signal(close):
    n=8
    r=_rsi(close, 14)
    b=close.pct_change(n) - r.pct_change(n)
    return _j(b, 5)

def f14md_f14_momentum_divergence_veldiff_macd_12d_jerk_v049_signal(close):
    n=12
    m=_macd(close, 12, 26); mn=m/close
    b=close.pct_change(n) - mn.diff(n)
    return _j(b, 5)

def f14md_f14_momentum_divergence_veldiff_stoch_18d_jerk_v050_signal(high, low, close):
    n=18
    k=_stoch_k(high, low, close, 14)
    b=close.pct_change(n) - k.diff(n)/100.0
    return _j(b, 10)

def f14md_f14_momentum_divergence_zslp_rsi_40d_jerk_v051_signal(closeadj):
    n=40
    r=_rsi(closeadj, 14)
    d=(closeadj - closeadj.shift(10))/closeadj.shift(10).replace(0.0,np.nan)*100.0 - (r - r.shift(10))
    mu=d.rolling(n, min_periods=n).mean(); sd=d.rolling(n, min_periods=n).std(ddof=1)
    b=(d - mu)/sd.replace(0.0,np.nan)
    return _j(b, 10)

def f14md_f14_momentum_divergence_corrrank_rsi_100d_jerk_v052_signal(closeadj):
    n=100
    r=_rsi(closeadj, 14)
    c=closeadj.rolling(20, min_periods=20).corr(r)
    b=c.rolling(n, min_periods=n).rank(pct=True)
    return _j(b, 21)

def f14md_f14_momentum_divergence_pjerk_rjerk_30d_jerk_v053_signal(closeadj):
    n=30
    r=_rsi(closeadj, 14)
    pj=closeadj.pct_change(n).diff(n).diff(n)
    rj=(r.diff(n)/100.0).diff(n).diff(n)
    b=pj - rj
    return _j(b, 21)

def f14md_f14_momentum_divergence_stochrsi_div_30d_jerk_v054_signal(high, low, closeadj):
    k=_stoch_k(high, low, closeadj, 14); r=_rsi(closeadj, 14)
    b=np.tanh((k - r)/20.0)
    return _j(b, 21)

def f14md_f14_momentum_divergence_lag1_pr_corr_40d_jerk_v055_signal(closeadj):
    n=40
    r=_rsi(closeadj, 14)
    b=closeadj.rolling(n, min_periods=n).corr(r.shift(1))
    return _j(b, 21)

def f14md_f14_momentum_divergence_magdiv_rsi_25d_jerk_v056_signal(close):
    n=25
    r=_rsi(close, 14)
    pm=np.log(close/close.shift(n)).abs(); rm=(r.diff(n)/100.0).abs()
    b=pm - rm
    return _j(b, 10)

def f14md_f14_momentum_divergence_days_div_rsi_60d_jerk_v057_signal(closeadj):
    n=60
    r=_rsi(closeadj, 14)
    phi=closeadj.rolling(20, min_periods=20).max(); rhi=r.rolling(20, min_periods=20).max()
    ev=((closeadj >= phi*0.999) & (r < rhi - 5.0)).astype(float).where(~phi.isna() & ~rhi.isna())
    b=ev.rolling(n, min_periods=n).sum()
    return _j(b, 21)

def f14md_f14_momentum_divergence_multi_macd_60d_jerk_v058_signal(closeadj):
    m=_macd(closeadj, 12, 26)/closeadj
    p1=np.log(closeadj/closeadj.shift(20)); m1=m - m.shift(20)
    p2=np.log(closeadj/closeadj.shift(60)); m2=m - m.shift(60)
    b=(p1 - m1)*0.5 + (p2 - m2)*0.5
    return _j(b, 21)

def f14md_f14_momentum_divergence_streak_xor_50d_jerk_v059_signal(closeadj):
    m=_macd(closeadj, 12, 26); sp=np.sign(closeadj.diff(5)); sm=np.sign(m.diff(5))
    disagree=((sp*sm)<0).astype(float).where(~sp.isna() & ~sm.isna())
    def _str(x):
        s=0
        for v in x[::-1]:
            if v>0.5: s+=1
            else: break
        return float(s)
    b=disagree.rolling(50, min_periods=50).apply(_str, raw=True)
    return _j(b, 10)

def f14md_f14_momentum_divergence_rankcorr_macd_40d_jerk_v060_signal(closeadj):
    n=40
    m=_macd(closeadj, 12, 26); ret=np.log(closeadj/closeadj.shift(1)); md=m.diff()
    def _sp(idx):
        i=int(idx[-1]); a=ret.iloc[i-n+1:i+1].values; bb=md.iloc[i-n+1:i+1].values
        if np.any(~np.isfinite(a)) or np.any(~np.isfinite(bb)): return np.nan
        ra=pd.Series(a).rank().values; rb=pd.Series(bb).rank().values
        sa=ra.std(); sb=rb.std()
        if sa<=0 or sb<=0: return np.nan
        return float(((ra-ra.mean())*(rb-rb.mean())).mean()/(sa*sb))
    idx_s=pd.Series(np.arange(len(closeadj), dtype=float), index=closeadj.index)
    b=idx_s.rolling(n, min_periods=n).apply(_sp, raw=True)
    return _j(b, 10)

def f14md_f14_momentum_divergence_signdir_rsi_20d_jerk_v061_signal(close):
    n=20
    r=_rsi(close, 14)
    b=np.sign(close.diff(n)) - np.sign(r.diff(n))
    return _j(b, 5)

def f14md_f14_momentum_divergence_mad_jerk_pr_30d_jerk_v062_signal(closeadj):
    n=30
    r=_rsi(closeadj, 14)
    d=(closeadj.pct_change() - r.pct_change()).abs()
    b=d.rolling(n, min_periods=n).mean()
    return _j(b, 10)

def f14md_f14_momentum_divergence_hfdiv_rsi_5d_jerk_v063_signal(close):
    n=5
    r=_rsi(close, 14)
    b=np.log(close/close.shift(n)) - r.diff(n)/50.0
    return _j(b, 5)

def f14md_f14_momentum_divergence_tsi_div_80d_jerk_v064_signal(closeadj):
    n=80
    t=_tsi(closeadj, 25, 13)
    d=np.log(closeadj/closeadj.shift(20)) - t.diff(20)/100.0
    mu=d.rolling(n, min_periods=n).mean(); sd=d.rolling(n, min_periods=n).std(ddof=1)
    b=(d - mu)/sd.replace(0.0, np.nan)
    return _j(b, 21)

def f14md_f14_momentum_divergence_netasym_macd_50d_jerk_v065_signal(closeadj):
    n=50
    m=_macd(closeadj, 12, 26)
    phi=closeadj.rolling(20, min_periods=20).max(); plo=closeadj.rolling(20, min_periods=20).min()
    mhi=m.rolling(20, min_periods=20).max(); mlo=m.rolling(20, min_periods=20).min()
    bull=((closeadj <= plo*1.001) & (m > mlo)).astype(float).where(~plo.isna() & ~mlo.isna())
    bear=((closeadj >= phi*0.999) & (m < mhi)).astype(float).where(~phi.isna() & ~mhi.isna())
    b=bull.rolling(n, min_periods=n).sum() - bear.rolling(n, min_periods=n).sum()
    return _j(b, 21)

def f14md_f14_momentum_divergence_msd_norm_pr_50d_jerk_v066_signal(closeadj):
    n=50
    lp=np.log(closeadj); r=_rsi(closeadj, 14)
    zlp=(lp - lp.rolling(n, min_periods=n).mean())/lp.rolling(n, min_periods=n).std(ddof=1).replace(0.0, np.nan)
    zr=(r - r.rolling(n, min_periods=n).mean())/r.rolling(n, min_periods=n).std(ddof=1).replace(0.0, np.nan)
    b=(zlp - zr)**2
    return _j(b, 21)

def f14md_f14_momentum_divergence_hidden_rsi_30d_jerk_v067_signal(closeadj):
    n=30
    r=_rsi(closeadj, 14)
    pln=closeadj.rolling(15, min_periods=15).max(); plt=pln.shift(15)
    rhn=r.rolling(15, min_periods=15).max(); rht=rhn.shift(15)
    cond=((pln < plt) & (rhn > rht)).astype(float).where(~plt.isna() & ~rht.isna())
    b=cond.rolling(n, min_periods=n).mean()
    return _j(b, 21)

def f14md_f14_momentum_divergence_slpratio_rsi_30d_jerk_v068_signal(closeadj):
    n=30
    r=_rsi(closeadj, 14)
    pslp=(closeadj - closeadj.shift(n))/closeadj.shift(n).replace(0.0, np.nan)
    rslp=(r - r.shift(n))/100.0
    b=np.arctan(pslp/rslp.replace(0.0, np.nan))
    return _j(b, 21)

def f14md_f14_momentum_divergence_pmroc_avg_60d_jerk_v069_signal(closeadj):
    n=60
    r5=_roc(closeadj, 5)/100.0
    d=closeadj.pct_change(5) - r5
    b=d.rolling(n, min_periods=n).mean()
    return _j(b, 21)

def f14md_f14_momentum_divergence_obvmom_30d_jerk_v070_signal(close, volume):
    n=30
    sp=np.sign(close.diff())
    obvflow=(volume*sp).rolling(n, min_periods=n).sum(); pflow=(close.diff().abs()*sp).rolling(n, min_periods=n).sum()
    zo=(obvflow - obvflow.rolling(60, min_periods=60).mean())/obvflow.rolling(60, min_periods=60).std(ddof=1).replace(0.0, np.nan)
    zp=(pflow - pflow.rolling(60, min_periods=60).mean())/pflow.rolling(60, min_periods=60).std(ddof=1).replace(0.0, np.nan)
    b=zp - zo
    return _j(b, 10)

def f14md_f14_momentum_divergence_adaptdiv_rsi_60d_jerk_v071_signal(closeadj):
    r=_rsi(closeadj, 14)
    d=(closeadj.pct_change(5)*100.0 - r.diff(5)).abs()
    med=d.rolling(100, min_periods=100).median()
    fl=(d > med).astype(float).where(~med.isna())
    b=fl.rolling(60, min_periods=60).sum()
    return _j(b, 21)

def f14md_f14_momentum_divergence_avgcoh_macd_50d_jerk_v072_signal(closeadj):
    n=50
    m=_macd(closeadj, 12, 26)
    c0=closeadj.rolling(n, min_periods=n).corr(m).abs()
    cp2=closeadj.rolling(n, min_periods=n).corr(m.shift(2)).abs()
    cn2=closeadj.rolling(n, min_periods=n).corr(m.shift(-2)).abs()
    b=c0 - (cp2 + cn2)*0.5
    return _j(b, 21)

def f14md_f14_momentum_divergence_persistdiv_rsi_40d_jerk_v073_signal(closeadj):
    n=40
    r=_rsi(closeadj, 14)
    s=np.sign(closeadj.pct_change(5)*100.0 - r.diff(5)/20.0)
    b=s.rolling(n, min_periods=n).mean()
    return _j(b, 10)

def f14md_f14_momentum_divergence_quintdiv_rsi_120d_jerk_v074_signal(closeadj):
    r=_rsi(closeadj, 14)
    c=closeadj.rolling(20, min_periods=20).corr(r); dc=c.diff(10)
    pct=dc.rolling(120, min_periods=120).rank(pct=True)
    b=np.ceil(pct*5.0)
    return _j(b, 63)

def f14md_f14_momentum_divergence_skew_diff_rsi_60d_jerk_v075_signal(closeadj):
    n=60
    r=_rsi(closeadj, 14)
    d=closeadj.pct_change() - r.diff()/100.0
    b=d.rolling(n, min_periods=n).skew()
    return _j(b, 21)


# --- v076-v150: jerk versions of base 076-150 -------------------------------


def f14md_f14_momentum_divergence_pslp_minus_rocslp_45d_jerk_v076_signal(closeadj):
    n=45
    rc=_roc(closeadj, 20)
    pslp=(closeadj - closeadj.shift(n))/closeadj.shift(n).replace(0.0,np.nan)*100.0
    b=pslp - (rc - rc.shift(n))
    return _j(b, 21)

def f14md_f14_momentum_divergence_pslp_minus_ppoSlp_30d_jerk_v077_signal(closeadj):
    n=30
    pp=_ppo(closeadj, 12, 26)
    pslp=(closeadj - closeadj.shift(n))/closeadj.shift(n).replace(0.0,np.nan)*100.0
    b=pslp - (pp - pp.shift(n))
    return _j(b, 10)

def f14md_f14_momentum_divergence_pslp_minus_wprSlp_22d_jerk_v078_signal(high, low, closeadj):
    n=22
    w=_wpr(high, low, closeadj, 14)
    pslp=(closeadj - closeadj.shift(n))/closeadj.shift(n).replace(0.0,np.nan)*100.0
    b=pslp - (w - w.shift(n))
    return _j(b, 10)

def f14md_f14_momentum_divergence_pslp_minus_aoSlp_35d_jerk_v079_signal(high, low):
    n=35
    a=_ao(high, low); mp=(high+low)/2.0
    pslp=(mp - mp.shift(n))/mp.shift(n).replace(0.0,np.nan)*100.0
    b=pslp - (a - a.shift(n))/mp
    return _j(b, 21)

def f14md_f14_momentum_divergence_signxor_tsi_20d_jerk_v080_signal(close):
    n=20
    t=_tsi(close, 25, 13); sp=np.sign(close.diff(n)); st=np.sign(t.diff(n))
    b=((sp*st)<0).astype(float).where(~sp.isna() & ~st.isna())
    return _j(b, 10)

def f14md_f14_momentum_divergence_signxor_cmo_25d_jerk_v081_signal(closeadj):
    n=25
    c=_cmo(closeadj, 14); sp=np.sign(closeadj.diff(n)); sc=np.sign(c.diff(n))
    b=((sp*sc)<0).astype(float).where(~sp.isna() & ~sc.isna())
    return _j(b, 21)

def f14md_f14_momentum_divergence_signxor_mfi_18d_jerk_v082_signal(high, low, close, volume):
    n=18
    tp=(high+low+close)/3.0; rmf=tp*volume; dn=tp.diff()
    pos=rmf.where(dn>0, 0.0).rolling(14, min_periods=14).sum()
    neg=rmf.where(dn<0, 0.0).rolling(14, min_periods=14).sum()
    mfi=100.0 - 100.0/(1.0 + pos/neg.replace(0.0, np.nan))
    sp=np.sign(close.diff(n)); sm=np.sign(mfi.diff(n))
    b=((sp*sm)<0).astype(float).where(~sp.isna() & ~sm.isna())
    return _j(b, 10)

def f14md_f14_momentum_divergence_corr_roc_30d_jerk_v083_signal(closeadj):
    n=30
    rc=_roc(closeadj, 10)
    b=np.log(closeadj).rolling(n, min_periods=n).corr(rc)
    return _j(b, 21)

def f14md_f14_momentum_divergence_corr_stoch_45d_jerk_v084_signal(high, low, closeadj):
    n=45
    k=_stoch_k(high, low, closeadj, 14)
    b=closeadj.rolling(n, min_periods=n).corr(k)
    return _j(b, 21)

def f14md_f14_momentum_divergence_corr_wpr_55d_jerk_v085_signal(high, low, closeadj):
    n=55
    w=_wpr(high, low, closeadj, 14)
    b=np.log(closeadj).rolling(n, min_periods=n).corr(w)
    return _j(b, 21)

def f14md_f14_momentum_divergence_corr_ao_70d_jerk_v086_signal(high, low):
    n=70
    a=_ao(high, low); mp=(high+low)/2.0
    b=mp.rolling(n, min_periods=n).corr(a)
    return _j(b, 21)

def f14md_f14_momentum_divergence_corr_ppo_60d_jerk_v087_signal(closeadj):
    n=60
    pp=_ppo(closeadj, 12, 26)
    b=np.log(closeadj).rolling(n, min_periods=n).corr(pp)
    return _j(b, 21)

def f14md_f14_momentum_divergence_phigh_macd_40d_jerk_v088_signal(closeadj):
    n=40
    m=_macd(closeadj, 12, 26)
    phi=closeadj.rolling(n, min_periods=n).max(); mhi=m.rolling(n, min_periods=n).max()
    ev=((closeadj >= phi*0.999) & (m < mhi - mhi.abs().rolling(n, min_periods=n).mean()*0.1)).astype(float).where(~phi.isna())
    def _ds(x):
        idx=np.where(x>0.5)[0]; return float(len(x)) if idx.size==0 else float(len(x)-1-idx[-1])
    b=ev.rolling(80, min_periods=80).apply(_ds, raw=True)
    return _j(b, 21)

def f14md_f14_momentum_divergence_plow_macd_50d_jerk_v089_signal(closeadj):
    n=50
    m=_macd(closeadj, 12, 26)
    plo=closeadj.rolling(n, min_periods=n).min(); mlo=m.rolling(n, min_periods=n).min()
    at=(closeadj <= plo*1.001).astype(float).where(~plo.isna())
    b=at*(m - mlo)
    return _j(b, 21)

def f14md_f14_momentum_divergence_phigh_cmo_30d_jerk_v090_signal(closeadj):
    n=30
    c=_cmo(closeadj, 14)
    phi=closeadj.rolling(n, min_periods=n).max(); chi=c.rolling(n, min_periods=n).max()
    at=(closeadj >= phi*0.999).astype(float).where(~phi.isna())
    b=at*(chi - c)
    return _j(b, 21)

def f14md_f14_momentum_divergence_phigh_tsi_70d_jerk_v091_signal(closeadj):
    n=70
    t=_tsi(closeadj, 25, 13)
    phi=closeadj.rolling(n, min_periods=n).max(); thi=t.rolling(n, min_periods=n).max()
    at=(closeadj >= phi*0.999).astype(float).where(~phi.isna())
    b=at*(thi - t)
    return _j(b, 21)

def f14md_f14_momentum_divergence_dslph_macd_100d_jerk_v092_signal(closeadj):
    n=100
    m=_macd(closeadj, 12, 26)
    phi=closeadj.rolling(25, min_periods=25).max(); mhi=m.rolling(25, min_periods=25).max()
    ev=((closeadj >= phi*0.999) & (m < mhi)).astype(float).where(~phi.isna() & ~mhi.isna())
    def _ds(x):
        idx=np.where(x>0.5)[0]; return float(len(x)) if idx.size==0 else float(len(x)-1-idx[-1])
    b=ev.rolling(n, min_periods=n).apply(_ds, raw=True)
    return _j(b, 21)

def f14md_f14_momentum_divergence_rsi_minus_cmo_40d_jerk_v093_signal(closeadj):
    n=40
    r=_rsi(closeadj, 14); c=_cmo(closeadj, 14); d=r - (c+100.0)/2.0
    mu=d.rolling(n, min_periods=n).mean(); sd=d.rolling(n, min_periods=n).std(ddof=1)
    b=(d - mu)/sd.replace(0.0, np.nan)
    return _j(b, 10)

def f14md_f14_momentum_divergence_macd_minus_ppo_50d_jerk_v094_signal(closeadj):
    n=50
    m=_macd(closeadj, 12, 26); p=_ppo(closeadj, 12, 26)
    b=m.rolling(n, min_periods=n).corr(p)
    return _j(b, 21)

def f14md_f14_momentum_divergence_tsi_minus_rsi_60d_jerk_v095_signal(closeadj):
    n=60
    t=_tsi(closeadj, 25, 13); r=_rsi(closeadj, 14)*2.0 - 100.0
    d=t - r; mu=d.rolling(n, min_periods=n).mean(); sd=d.rolling(n, min_periods=n).std(ddof=1)
    b=(d - mu)/sd.replace(0.0, np.nan)
    return _j(b, 21)

def f14md_f14_momentum_divergence_compxor_macd_50d_jerk_v096_signal(closeadj):
    n=50
    m=_macd(closeadj, 12, 26); sp=np.sign(closeadj.diff(5)); sm=np.sign(m.diff(5))
    fl=((sp*sm)<0).astype(float).where(~sp.isna() & ~sm.isna())
    b=fl.rolling(n, min_periods=n).sum()
    return _j(b, 21)

def f14md_f14_momentum_divergence_compxor_stoch_30d_jerk_v097_signal(high, low, close):
    n=30
    k=_stoch_k(high, low, close, 14); sp=np.sign(close.diff(5)); sk=np.sign(k.diff(5))
    fl=((sp*sk)<0).astype(float).where(~sp.isna() & ~sk.isna())
    b=fl.rolling(n, min_periods=n).sum()
    return _j(b, 10)

def f14md_f14_momentum_divergence_arctan_macdiv_30d_jerk_v098_signal(closeadj):
    m=_macd(closeadj, 12, 26)/closeadj
    b=np.arctan(20.0*(closeadj.pct_change(3) - m.diff(3)))
    return _j(b, 10)

def f14md_f14_momentum_divergence_tanh_corr_macd_40d_jerk_v099_signal(closeadj):
    n=40
    m=_macd(closeadj, 12, 26)
    b=np.tanh(2.0*closeadj.rolling(n, min_periods=n).corr(m))
    return _j(b, 10)

def f14md_f14_momentum_divergence_sigmoid_rocdiv_40d_jerk_v100_signal(closeadj):
    n=20
    rc=_roc(closeadj, 10)/100.0
    x=15.0*(closeadj.pct_change(n) - rc.diff(n))
    b=1.0/(1.0 + np.exp(-x)) - 0.5
    return _j(b, 21)

def f14md_f14_momentum_divergence_flipcount_macd_60d_jerk_v101_signal(closeadj):
    n=60
    m=_macd(closeadj, 12, 26)
    scale=closeadj.abs().rolling(20, min_periods=20).mean()/m.abs().rolling(20, min_periods=20).mean().replace(0.0, np.nan)
    d=closeadj.diff() - m.diff()*scale; s=np.sign(d)
    fl=(s != s.shift(1)).astype(float).where(~s.isna() & ~s.shift(1).isna())
    b=fl.rolling(n, min_periods=n).sum()
    return _j(b, 21)

def f14md_f14_momentum_divergence_cumabs_macd_45d_jerk_v102_signal(closeadj):
    n=45
    m=_macd(closeadj, 12, 26)/closeadj
    d=(closeadj.pct_change() - m.diff()).abs()
    b=d.rolling(n, min_periods=n).sum()
    return _j(b, 21)

def f14md_f14_momentum_divergence_convrate_macd_50d_jerk_v103_signal(closeadj):
    m=_macd(closeadj, 12, 26)
    cs=closeadj.rolling(15, min_periods=15).corr(m); cl=closeadj.rolling(60, min_periods=60).corr(m)
    b=cs - cl
    return _j(b, 21)

def f14md_f14_momentum_divergence_bullintens_macd_60d_jerk_v104_signal(closeadj):
    n=60
    m=_macd(closeadj, 12, 26)
    plo=closeadj.rolling(20, min_periods=20).min(); mlo=m.rolling(20, min_periods=20).min()
    at=(closeadj <= plo*1.001).astype(float).where(~plo.isna())
    b=(at*(m - mlo)).rolling(n, min_periods=n).max()
    return _j(b, 21)

def f14md_f14_momentum_divergence_bearintens_macd_60d_jerk_v105_signal(closeadj):
    n=60
    m=_macd(closeadj, 12, 26)
    phi=closeadj.rolling(20, min_periods=20).max(); mhi=m.rolling(20, min_periods=20).max()
    at=(closeadj >= phi*0.999).astype(float).where(~phi.isna())
    b=(at*(mhi - m)).rolling(n, min_periods=n).max()
    return _j(b, 21)

def f14md_f14_momentum_divergence_regresid_macd_40d_jerk_v106_signal(closeadj):
    n=40
    m=_macd(closeadj, 12, 26); lp=np.log(closeadj)
    def _r(idx):
        i=int(idx[-1]); a=lp.iloc[i-n+1:i+1].values; bb=m.iloc[i-n+1:i+1].values
        if np.any(~np.isfinite(a)) or np.any(~np.isfinite(bb)): return np.nan
        va=((a-a.mean())**2).sum()
        if va<=0: return np.nan
        beta=((a-a.mean())*(bb-bb.mean())).sum()/va; alpha=bb.mean() - beta*a.mean()
        return float(bb[-1] - (alpha + beta*a[-1]))
    idx_s=pd.Series(np.arange(len(closeadj), dtype=float), index=closeadj.index)
    b=idx_s.rolling(n, min_periods=n).apply(_r, raw=True)
    return _j(b, 10)

def f14md_f14_momentum_divergence_beta_macd_70d_jerk_v107_signal(closeadj):
    n=70
    m=_macd(closeadj, 12, 26); lp=np.log(closeadj)
    cov=lp.rolling(n, min_periods=n).cov(m); var=lp.rolling(n, min_periods=n).var(ddof=1)
    b=cov/var.replace(0.0, np.nan)
    return _j(b, 21)

def f14md_f14_momentum_divergence_r2_macd_60d_jerk_v108_signal(closeadj):
    n=60
    m=_macd(closeadj, 12, 26)
    c=np.log(closeadj).rolling(n, min_periods=n).corr(m)
    b=c*c
    return _j(b, 21)

def f14md_f14_momentum_divergence_curv_macd_35d_jerk_v109_signal(closeadj):
    n=35
    m=_macd(closeadj, 12, 26)/closeadj
    pc=(closeadj - 2*closeadj.shift(n) + closeadj.shift(2*n))/closeadj.shift(n).replace(0.0, np.nan)
    mc=m - 2*m.shift(n) + m.shift(2*n)
    b=pc - mc
    return _j(b, 21)

def f14md_f14_momentum_divergence_accel_rsi_50d_jerk_v110_signal(closeadj):
    n=50
    r=_rsi(closeadj, 14)
    pa=closeadj.pct_change(n) - closeadj.pct_change(n).shift(n)
    ra=(r.diff(n) - r.diff(n).shift(n))/100.0
    b=pa - ra
    return _j(b, 21)

def f14md_f14_momentum_divergence_lag_macd_50d_jerk_v111_signal(closeadj):
    n=50
    m=_macd(closeadj, 12, 26); ret=closeadj.pct_change(); md=m.diff()
    def _bl(idx):
        i=int(idx[-1])
        if i<2*n: return np.nan
        a=ret.iloc[i-n+1:i+1].values; best=0.0; bl=0
        for L in range(-3,4):
            bb=md.shift(L).iloc[i-n+1:i+1].values
            if np.any(~np.isfinite(a)) or np.any(~np.isfinite(bb)): continue
            sa=a.std(); sb=bb.std()
            if sa<=0 or sb<=0: continue
            cc=float(((a-a.mean())*(bb-bb.mean())).mean()/(sa*sb))
            if abs(cc)>abs(best): best=cc; bl=L
        return float(bl)
    idx_s=pd.Series(np.arange(len(closeadj), dtype=float), index=closeadj.index)
    b=idx_s.rolling(n, min_periods=n).apply(_bl, raw=True)
    return _j(b, 21)

def f14md_f14_momentum_divergence_veldiff_cmo_12d_jerk_v112_signal(close):
    n=12
    c=_cmo(close, 14)
    b=close.pct_change(n) - c.diff(n)/100.0
    return _j(b, 5)

def f14md_f14_momentum_divergence_veldiff_tsi_30d_jerk_v113_signal(closeadj):
    n=30
    t=_tsi(closeadj, 25, 13)
    b=closeadj.pct_change(n) - t.diff(n)/100.0
    return _j(b, 10)

def f14md_f14_momentum_divergence_veldiff_wpr_15d_jerk_v114_signal(high, low, close):
    n=15
    w=_wpr(high, low, close, 14)
    mu=w.rolling(40, min_periods=40).mean(); sd=w.rolling(40, min_periods=40).std(ddof=1)
    zw=(w - mu)/sd.replace(0.0, np.nan)
    phi=close.rolling(n, min_periods=n).max(); plo=close.rolling(n, min_periods=n).min()
    at_high=(close >= phi*0.999).astype(float).where(~phi.isna())
    at_low=(close <= plo*1.001).astype(float).where(~plo.isna())
    b=at_high*zw - at_low*zw
    return _j(b, 5)

def f14md_f14_momentum_divergence_zslp_macd_50d_jerk_v115_signal(closeadj):
    n=50
    m=_macd(closeadj, 12, 26)/closeadj
    d=closeadj.pct_change(15) - m.diff(15)
    mu=d.rolling(n, min_periods=n).mean(); sd=d.rolling(n, min_periods=n).std(ddof=1)
    b=(d - mu)/sd.replace(0.0, np.nan)
    return _j(b, 21)

def f14md_f14_momentum_divergence_corrrank_macd_120d_jerk_v116_signal(closeadj):
    m=_macd(closeadj, 12, 26)
    c=closeadj.rolling(30, min_periods=30).corr(m)
    b=c.rolling(120, min_periods=120).rank(pct=True)
    return _j(b, 63)

def f14md_f14_momentum_divergence_pjerk_mjerk_40d_jerk_v117_signal(closeadj):
    n=40
    m=_macd(closeadj, 12, 26)/closeadj
    pj=closeadj.pct_change(n).diff(n).diff(n)
    mj=m.diff(n).diff(n).diff(n)
    b=pj - mj
    return _j(b, 21)

def f14md_f14_momentum_divergence_signdir_macd_30d_jerk_v118_signal(closeadj):
    n=30
    m=_macd(closeadj, 12, 26)
    b=np.sign(closeadj.diff(n)) - np.sign(m.diff(n))
    return _j(b, 10)

def f14md_f14_momentum_divergence_mad_macd_45d_jerk_v119_signal(closeadj):
    n=45
    m=_macd(closeadj, 12, 26)/closeadj
    d=(closeadj.pct_change(5) - m.diff(5)).abs()
    b=d.rolling(n, min_periods=n).median()
    return _j(b, 21)

def f14md_f14_momentum_divergence_hfdiv_macd_5d_jerk_v120_signal(close):
    n=5
    m=_macd(close, 12, 26)/close
    b=np.log(close/close.shift(n)) - m.diff(n)
    return (_j(b, 10) / b.abs().rolling(10, min_periods=10).mean().replace(0.0, np.nan)).replace([np.inf,-np.inf], np.nan)

def f14md_f14_momentum_divergence_msd_macd_60d_jerk_v121_signal(closeadj):
    n=60
    lp=np.log(closeadj); m=_macd(closeadj, 12, 26)
    zp=(lp - lp.rolling(n, min_periods=n).mean())/lp.rolling(n, min_periods=n).std(ddof=1).replace(0.0, np.nan)
    zm=(m - m.rolling(n, min_periods=n).mean())/m.rolling(n, min_periods=n).std(ddof=1).replace(0.0, np.nan)
    b=(zp - zm)**2
    return _j(b, 21)

def f14md_f14_momentum_divergence_hidden_macd_40d_jerk_v122_signal(closeadj):
    n=40
    m=_macd(closeadj, 12, 26)
    pln=closeadj.rolling(20, min_periods=20).min(); plt=pln.shift(20)
    mln=m.rolling(20, min_periods=20).min(); mlt=mln.shift(20)
    cond=((pln > plt) & (mln < mlt)).astype(float).where(~plt.isna() & ~mlt.isna())
    b=cond.rolling(n, min_periods=n).mean()
    return _j(b, 21)

def f14md_f14_momentum_divergence_slpratio_macd_45d_jerk_v123_signal(closeadj):
    n=45
    m=_macd(closeadj, 12, 26)/closeadj
    pslp=(closeadj - closeadj.shift(n))/closeadj.shift(n).replace(0.0, np.nan)
    mslp=m - m.shift(n)
    b=np.arctan(pslp/mslp.replace(0.0, np.nan))
    return _j(b, 21)

def f14md_f14_momentum_divergence_pmstoch_avg_50d_jerk_v124_signal(high, low, closeadj):
    n=50
    k=_stoch_k(high, low, closeadj, 14)
    d=closeadj.pct_change(5) - k.diff(5)/100.0
    b=d.rolling(n, min_periods=n).mean()
    return _j(b, 21)

def f14md_f14_momentum_divergence_obvmom_60d_jerk_v125_signal(close, volume):
    n=60
    sp=np.sign(close.diff())
    obv=(volume*sp).rolling(n, min_periods=n).sum(); pflow=(close.diff().abs()*sp).rolling(n, min_periods=n).sum()
    zo=(obv - obv.rolling(120, min_periods=120).mean())/obv.rolling(120, min_periods=120).std(ddof=1).replace(0.0, np.nan)
    zp=(pflow - pflow.rolling(120, min_periods=120).mean())/pflow.rolling(120, min_periods=120).std(ddof=1).replace(0.0, np.nan)
    b=zp - zo
    return _j(b, 21)

def f14md_f14_momentum_divergence_adapt_macd_80d_jerk_v126_signal(closeadj):
    m=_macd(closeadj, 12, 26)/closeadj
    d=(closeadj.pct_change(5) - m.diff(5)).abs()
    med=d.rolling(150, min_periods=150).median()
    fl=(d > med).astype(float).where(~med.isna())
    b=fl.rolling(80, min_periods=80).sum()
    return _j(b, 21)

def f14md_f14_momentum_divergence_persist_macd_60d_jerk_v127_signal(closeadj):
    n=60
    m=_macd(closeadj, 12, 26)/closeadj
    s=np.sign(closeadj.pct_change(5) - m.diff(5))
    b=s.rolling(n, min_periods=n).mean()
    return _j(b, 21)

def f14md_f14_momentum_divergence_skew_macd_80d_jerk_v128_signal(closeadj):
    n=80
    m=_macd(closeadj, 12, 26)/closeadj
    d=closeadj.pct_change() - m.diff()
    b=d.rolling(n, min_periods=n).skew()
    return _j(b, 21)

def f14md_f14_momentum_divergence_kurt_div_rsi_80d_jerk_v129_signal(closeadj):
    n=80
    r=_rsi(closeadj, 14)
    d=closeadj.pct_change() - r.diff()/100.0
    b=d.rolling(n, min_periods=n).kurt()
    return _j(b, 21)

def f14md_f14_momentum_divergence_acfr1_div_60d_jerk_v130_signal(closeadj):
    n=60
    r=_rsi(closeadj, 14)
    d=closeadj.pct_change() - r.diff()/100.0
    b=d.rolling(n, min_periods=n).corr(d.shift(1))
    return _j(b, 21)

def f14md_f14_momentum_divergence_atrnorm_pslp_40d_jerk_v131_signal(high, low, closeadj):
    n=40
    pc=closeadj.shift(1)
    tr=pd.concat([(high-low).abs(),(high-pc).abs(),(low-pc).abs()], axis=1).max(axis=1)
    atr=tr.rolling(n, min_periods=n).mean()/closeadj
    r=_rsi(closeadj, 14); d=closeadj.pct_change(n) - r.diff(n)/100.0
    b=d/atr.replace(0.0, np.nan)
    return _j(b, 10)

def f14md_f14_momentum_divergence_argextr_rsi_25d_jerk_v132_signal(closeadj):
    n=25
    r=_rsi(closeadj, 14)
    def _arg(arr): return float(np.argmax(arr))
    pa=closeadj.rolling(n, min_periods=n).apply(_arg, raw=True)
    ra=r.rolling(n, min_periods=n).apply(_arg, raw=True)
    b=pa - ra
    return _j(b, 10)

def f14md_f14_momentum_divergence_argextr_macd_45d_jerk_v133_signal(closeadj):
    n=45
    m=_macd(closeadj, 12, 26)
    def _arg(arr): return float(np.argmin(arr))
    pa=closeadj.rolling(n, min_periods=n).apply(_arg, raw=True)
    ma=m.rolling(n, min_periods=n).apply(_arg, raw=True)
    b=pa - ma
    return _j(b, 21)

def f14md_f14_momentum_divergence_pctile_div_rsi_60d_jerk_v134_signal(closeadj):
    n=60
    r=_rsi(closeadj, 14)
    pp=closeadj.rolling(n, min_periods=n).rank(pct=True); rp=r.rolling(n, min_periods=n).rank(pct=True)
    b=pp - rp
    return _j(b, 21)

def f14md_f14_momentum_divergence_pctile_div_macd_80d_jerk_v135_signal(closeadj):
    n=80
    m=_macd(closeadj, 12, 26)
    pp=closeadj.rolling(n, min_periods=n).rank(pct=True); mp=m.rolling(n, min_periods=n).rank(pct=True)
    b=pp - mp
    return _j(b, 21)

def f14md_f14_momentum_divergence_zspread_rsi_45d_jerk_v136_signal(closeadj):
    n=45
    lp=np.log(closeadj); r=_rsi(closeadj, 14)
    zp=(lp - lp.rolling(n, min_periods=n).mean())/lp.rolling(n, min_periods=n).std(ddof=1).replace(0.0, np.nan)
    zr=(r - r.rolling(n, min_periods=n).mean())/r.rolling(n, min_periods=n).std(ddof=1).replace(0.0, np.nan)
    b=zp - zr
    return _j(b, 21)

def f14md_f14_momentum_divergence_zspread_macd_70d_jerk_v137_signal(closeadj):
    n=70
    lp=np.log(closeadj); m=_macd(closeadj, 12, 26)
    zp=(lp - lp.rolling(n, min_periods=n).mean())/lp.rolling(n, min_periods=n).std(ddof=1).replace(0.0, np.nan)
    zm=(m - m.rolling(n, min_periods=n).mean())/m.rolling(n, min_periods=n).std(ddof=1).replace(0.0, np.nan)
    b=zp - zm
    return _j(b, 21)

def f14md_f14_momentum_divergence_volprice_rsi_50d_jerk_v138_signal(close, volume):
    n=50
    vwret=np.log(close/close.shift(1))*np.log1p(volume)
    r=_rsi(close, 14).diff()
    b=vwret.rolling(n, min_periods=n).corr(r)
    return _j(b, 21)

def f14md_f14_momentum_divergence_oscslp_diff_25d_jerk_v139_signal(closeadj):
    n=25
    r=_rsi(closeadj, 14); c=_cmo(closeadj, 14)
    b=r.diff(n) - c.diff(n)
    return _j(b, 21)

def f14md_f14_momentum_divergence_oscslp_diff_long_60d_jerk_v140_signal(closeadj):
    n=60
    m=_macd(closeadj, 12, 26); p=_ppo(closeadj, 12, 26)
    scale=m.abs().rolling(60, min_periods=60).mean()/p.abs().rolling(60, min_periods=60).mean().replace(0.0, np.nan)
    b=m.diff(n) - p.diff(n)*scale
    return _j(b, 21)

def f14md_f14_momentum_divergence_intrabar_diff_5d_jerk_v141_signal(high, low, close, open):
    n=5
    bar_mom=(close - open)/(high - low).replace(0.0, np.nan)
    s1=np.sign(close.diff()); s2=np.sign(bar_mom)
    flag=((s1*s2)<0).astype(float).where(~s1.isna() & ~s2.isna())
    b=flag.rolling(n, min_periods=n).sum()
    return _j(b, 5)

def f14md_f14_momentum_divergence_runrocdiff_40d_jerk_v142_signal(closeadj):
    rc1=_roc(closeadj, 10); rc2=_roc(closeadj, 20)
    s=np.sign(rc1 - rc2)
    b=s.rolling(40, min_periods=40).sum()
    return _j(b, 21)

def f14md_f14_momentum_divergence_pricerocstd_40d_jerk_v143_signal(closeadj):
    n=40
    rc=_roc(closeadj, 10); lp=np.log(closeadj)*100.0
    d=lp - rc
    b=d.rolling(n, min_periods=n).std(ddof=1)
    return _j(b, 21)

def f14md_f14_momentum_divergence_topqdiv_macd_60d_jerk_v144_signal(closeadj):
    n=60
    m=_macd(closeadj, 12, 26)/closeadj
    d=(closeadj.pct_change(5) - m.diff(5)).abs()
    b=d.rolling(n, min_periods=n).quantile(0.75)
    return _j(b, 21)

def f14md_f14_momentum_divergence_corr_pcurv_rsi_50d_jerk_v145_signal(closeadj):
    n=50
    r=_rsi(closeadj, 14)
    pc=closeadj - 2*closeadj.shift(5) + closeadj.shift(10)
    rc=r - 2*r.shift(5) + r.shift(10)
    b=pc.rolling(n, min_periods=n).corr(rc)
    return _j(b, 21)

def f14md_f14_momentum_divergence_lag2_pr_rsi_55d_jerk_v146_signal(closeadj):
    n=55
    r=_rsi(closeadj, 14)
    b=closeadj.rolling(n, min_periods=n).corr(r.shift(2))
    return _j(b, 21)

def f14md_f14_momentum_divergence_lag_neg2_pr_macd_45d_jerk_v147_signal(closeadj):
    n=45
    m=_macd(closeadj, 12, 26)
    b=closeadj.shift(2).rolling(n, min_periods=n).corr(m)
    return _j(b, 21)

def f14md_f14_momentum_divergence_zwedge_rsi_macd_60d_jerk_v148_signal(closeadj):
    n=60
    r=_rsi(closeadj, 14); m=_macd(closeadj, 12, 26)
    zr=(r - r.rolling(n, min_periods=n).mean())/r.rolling(n, min_periods=n).std(ddof=1).replace(0.0, np.nan)
    zm=(m - m.rolling(n, min_periods=n).mean())/m.rolling(n, min_periods=n).std(ddof=1).replace(0.0, np.nan)
    b=zr - zm
    return _j(b, 21)

def f14md_f14_momentum_divergence_emadiv_rsi_45d_jerk_v149_signal(closeadj):
    r=_rsi(closeadj, 14)
    d=closeadj.pct_change() - r.diff()/100.0
    b=d.ewm(span=20, adjust=False, min_periods=20).mean()
    return (_j(b, 63) / b.abs().rolling(63, min_periods=63).mean().replace(0.0, np.nan)).replace([np.inf,-np.inf], np.nan)

def f14md_f14_momentum_divergence_atrnorm_macd_60d_jerk_v150_signal(high, low, closeadj):
    n=60
    pc=closeadj.shift(1)
    tr=pd.concat([(high-low).abs(),(high-pc).abs(),(low-pc).abs()], axis=1).max(axis=1)
    atr=tr.rolling(n, min_periods=n).mean()/closeadj
    m=_macd(closeadj, 12, 26)/closeadj
    d=closeadj.pct_change(n) - m.diff(n)
    b=d/atr.replace(0.0, np.nan)
    return _j(b, 21)


# ---------------------------------------------------------------------------


def _e(fn, *inputs):
    return fn.__name__, {"inputs": list(inputs), "func": fn}


f14_momentum_divergence_jerk_001_150_REGISTRY = dict([
    _e(f14md_f14_momentum_divergence_pslp_rsi_14d_jerk_v001_signal, "close"),
    _e(f14md_f14_momentum_divergence_pslp_rsi_30d_jerk_v002_signal, "closeadj"),
    _e(f14md_f14_momentum_divergence_pslp_macd_20d_jerk_v003_signal, "close"),
    _e(f14md_f14_momentum_divergence_pslp_roc_25d_jerk_v004_signal, "closeadj"),
    _e(f14md_f14_momentum_divergence_pslp_stoch_15d_jerk_v005_signal, "high", "low", "close"),
    _e(f14md_f14_momentum_divergence_pslp_cmo_30d_jerk_v006_signal, "closeadj"),
    _e(f14md_f14_momentum_divergence_pslp_tsi_40d_jerk_v007_signal, "closeadj"),
    _e(f14md_f14_momentum_divergence_pslp_mfi_18d_jerk_v008_signal, "high", "low", "close", "volume"),
    _e(f14md_f14_momentum_divergence_signxor_rsi_10d_jerk_v009_signal, "close"),
    _e(f14md_f14_momentum_divergence_signxor_macd_15d_jerk_v010_signal, "close"),
    _e(f14md_f14_momentum_divergence_signxor_roc_30d_jerk_v011_signal, "closeadj"),
    _e(f14md_f14_momentum_divergence_signxor_stoch_8d_jerk_v012_signal, "high", "low", "close"),
    _e(f14md_f14_momentum_divergence_corr_rsi_20d_jerk_v013_signal, "close"),
    _e(f14md_f14_momentum_divergence_corr_rsi_60d_jerk_v014_signal, "closeadj"),
    _e(f14md_f14_momentum_divergence_corr_macd_40d_jerk_v015_signal, "closeadj"),
    _e(f14md_f14_momentum_divergence_corr_mom_30d_jerk_v016_signal, "closeadj"),
    _e(f14md_f14_momentum_divergence_corr_tsi_50d_jerk_v017_signal, "closeadj"),
    _e(f14md_f14_momentum_divergence_corr_cmo_45d_jerk_v018_signal, "closeadj"),
    _e(f14md_f14_momentum_divergence_phigh_rsi_low_20d_jerk_v019_signal, "close"),
    _e(f14md_f14_momentum_divergence_plow_rsi_high_30d_jerk_v020_signal, "closeadj"),
    _e(f14md_f14_momentum_divergence_phigh_macd_low_40d_jerk_v021_signal, "closeadj"),
    _e(f14md_f14_momentum_divergence_phigh_stoch_low_15d_jerk_v022_signal, "high", "low", "close"),
    _e(f14md_f14_momentum_divergence_plow_mfi_high_25d_jerk_v023_signal, "high", "low", "close", "volume"),
    _e(f14md_f14_momentum_divergence_dslph_rsi_60d_jerk_v024_signal, "closeadj"),
    _e(f14md_f14_momentum_divergence_dsplh_rsi_80d_jerk_v025_signal, "closeadj"),
    _e(f14md_f14_momentum_divergence_rsi_minus_mfi_30d_jerk_v026_signal, "high", "low", "close", "volume"),
    _e(f14md_f14_momentum_divergence_rsi_minus_stoch_40d_jerk_v027_signal, "high", "low", "closeadj"),
    _e(f14md_f14_momentum_divergence_macd_minus_rocsign_30d_jerk_v028_signal, "closeadj"),
    _e(f14md_f14_momentum_divergence_compxor_rsi_30d_jerk_v029_signal, "closeadj"),
    _e(f14md_f14_momentum_divergence_compxor_macd_25d_jerk_v030_signal, "close"),
    _e(f14md_f14_momentum_divergence_compabs_roc_45d_jerk_v031_signal, "closeadj"),
    _e(f14md_f14_momentum_divergence_arctan_rsidiv_15d_jerk_v032_signal, "close"),
    _e(f14md_f14_momentum_divergence_tanh_corrrsi_30d_jerk_v033_signal, "closeadj"),
    _e(f14md_f14_momentum_divergence_sigmoid_macdiv_25d_jerk_v034_signal, "closeadj"),
    _e(f14md_f14_momentum_divergence_flipcount_pr_40d_jerk_v035_signal, "closeadj"),
    _e(f14md_f14_momentum_divergence_cumdiv_rsi_30d_jerk_v036_signal, "closeadj"),
    _e(f14md_f14_momentum_divergence_cumdiv_macd_50d_jerk_v037_signal, "closeadj"),
    _e(f14md_f14_momentum_divergence_convrate_rsi_40d_jerk_v038_signal, "closeadj"),
    _e(f14md_f14_momentum_divergence_bullintens_rsi_40d_jerk_v039_signal, "closeadj"),
    _e(f14md_f14_momentum_divergence_bearintens_rsi_50d_jerk_v040_signal, "closeadj"),
    _e(f14md_f14_momentum_divergence_netdiv_rsi_40d_jerk_v041_signal, "closeadj"),
    _e(f14md_f14_momentum_divergence_regresid_rsi_30d_jerk_v042_signal, "closeadj"),
    _e(f14md_f14_momentum_divergence_beta_rsi_60d_jerk_v043_signal, "closeadj"),
    _e(f14md_f14_momentum_divergence_r2_pm_50d_jerk_v044_signal, "closeadj"),
    _e(f14md_f14_momentum_divergence_curv_rsi_25d_jerk_v045_signal, "closeadj"),
    _e(f14md_f14_momentum_divergence_accel_macd_30d_jerk_v046_signal, "closeadj"),
    _e(f14md_f14_momentum_divergence_lag_pr_rsi_30d_jerk_v047_signal, "closeadj"),
    _e(f14md_f14_momentum_divergence_veldiff_rsi_8d_jerk_v048_signal, "close"),
    _e(f14md_f14_momentum_divergence_veldiff_macd_12d_jerk_v049_signal, "close"),
    _e(f14md_f14_momentum_divergence_veldiff_stoch_18d_jerk_v050_signal, "high", "low", "close"),
    _e(f14md_f14_momentum_divergence_zslp_rsi_40d_jerk_v051_signal, "closeadj"),
    _e(f14md_f14_momentum_divergence_corrrank_rsi_100d_jerk_v052_signal, "closeadj"),
    _e(f14md_f14_momentum_divergence_pjerk_rjerk_30d_jerk_v053_signal, "closeadj"),
    _e(f14md_f14_momentum_divergence_stochrsi_div_30d_jerk_v054_signal, "high", "low", "closeadj"),
    _e(f14md_f14_momentum_divergence_lag1_pr_corr_40d_jerk_v055_signal, "closeadj"),
    _e(f14md_f14_momentum_divergence_magdiv_rsi_25d_jerk_v056_signal, "close"),
    _e(f14md_f14_momentum_divergence_days_div_rsi_60d_jerk_v057_signal, "closeadj"),
    _e(f14md_f14_momentum_divergence_multi_macd_60d_jerk_v058_signal, "closeadj"),
    _e(f14md_f14_momentum_divergence_streak_xor_50d_jerk_v059_signal, "closeadj"),
    _e(f14md_f14_momentum_divergence_rankcorr_macd_40d_jerk_v060_signal, "closeadj"),
    _e(f14md_f14_momentum_divergence_signdir_rsi_20d_jerk_v061_signal, "close"),
    _e(f14md_f14_momentum_divergence_mad_jerk_pr_30d_jerk_v062_signal, "closeadj"),
    _e(f14md_f14_momentum_divergence_hfdiv_rsi_5d_jerk_v063_signal, "close"),
    _e(f14md_f14_momentum_divergence_tsi_div_80d_jerk_v064_signal, "closeadj"),
    _e(f14md_f14_momentum_divergence_netasym_macd_50d_jerk_v065_signal, "closeadj"),
    _e(f14md_f14_momentum_divergence_msd_norm_pr_50d_jerk_v066_signal, "closeadj"),
    _e(f14md_f14_momentum_divergence_hidden_rsi_30d_jerk_v067_signal, "closeadj"),
    _e(f14md_f14_momentum_divergence_slpratio_rsi_30d_jerk_v068_signal, "closeadj"),
    _e(f14md_f14_momentum_divergence_pmroc_avg_60d_jerk_v069_signal, "closeadj"),
    _e(f14md_f14_momentum_divergence_obvmom_30d_jerk_v070_signal, "close", "volume"),
    _e(f14md_f14_momentum_divergence_adaptdiv_rsi_60d_jerk_v071_signal, "closeadj"),
    _e(f14md_f14_momentum_divergence_avgcoh_macd_50d_jerk_v072_signal, "closeadj"),
    _e(f14md_f14_momentum_divergence_persistdiv_rsi_40d_jerk_v073_signal, "closeadj"),
    _e(f14md_f14_momentum_divergence_quintdiv_rsi_120d_jerk_v074_signal, "closeadj"),
    _e(f14md_f14_momentum_divergence_skew_diff_rsi_60d_jerk_v075_signal, "closeadj"),
    _e(f14md_f14_momentum_divergence_pslp_minus_rocslp_45d_jerk_v076_signal, "closeadj"),
    _e(f14md_f14_momentum_divergence_pslp_minus_ppoSlp_30d_jerk_v077_signal, "closeadj"),
    _e(f14md_f14_momentum_divergence_pslp_minus_wprSlp_22d_jerk_v078_signal, "high", "low", "closeadj"),
    _e(f14md_f14_momentum_divergence_pslp_minus_aoSlp_35d_jerk_v079_signal, "high", "low"),
    _e(f14md_f14_momentum_divergence_signxor_tsi_20d_jerk_v080_signal, "close"),
    _e(f14md_f14_momentum_divergence_signxor_cmo_25d_jerk_v081_signal, "closeadj"),
    _e(f14md_f14_momentum_divergence_signxor_mfi_18d_jerk_v082_signal, "high", "low", "close", "volume"),
    _e(f14md_f14_momentum_divergence_corr_roc_30d_jerk_v083_signal, "closeadj"),
    _e(f14md_f14_momentum_divergence_corr_stoch_45d_jerk_v084_signal, "high", "low", "closeadj"),
    _e(f14md_f14_momentum_divergence_corr_wpr_55d_jerk_v085_signal, "high", "low", "closeadj"),
    _e(f14md_f14_momentum_divergence_corr_ao_70d_jerk_v086_signal, "high", "low"),
    _e(f14md_f14_momentum_divergence_corr_ppo_60d_jerk_v087_signal, "closeadj"),
    _e(f14md_f14_momentum_divergence_phigh_macd_40d_jerk_v088_signal, "closeadj"),
    _e(f14md_f14_momentum_divergence_plow_macd_50d_jerk_v089_signal, "closeadj"),
    _e(f14md_f14_momentum_divergence_phigh_cmo_30d_jerk_v090_signal, "closeadj"),
    _e(f14md_f14_momentum_divergence_phigh_tsi_70d_jerk_v091_signal, "closeadj"),
    _e(f14md_f14_momentum_divergence_dslph_macd_100d_jerk_v092_signal, "closeadj"),
    _e(f14md_f14_momentum_divergence_rsi_minus_cmo_40d_jerk_v093_signal, "closeadj"),
    _e(f14md_f14_momentum_divergence_macd_minus_ppo_50d_jerk_v094_signal, "closeadj"),
    _e(f14md_f14_momentum_divergence_tsi_minus_rsi_60d_jerk_v095_signal, "closeadj"),
    _e(f14md_f14_momentum_divergence_compxor_macd_50d_jerk_v096_signal, "closeadj"),
    _e(f14md_f14_momentum_divergence_compxor_stoch_30d_jerk_v097_signal, "high", "low", "close"),
    _e(f14md_f14_momentum_divergence_arctan_macdiv_30d_jerk_v098_signal, "closeadj"),
    _e(f14md_f14_momentum_divergence_tanh_corr_macd_40d_jerk_v099_signal, "closeadj"),
    _e(f14md_f14_momentum_divergence_sigmoid_rocdiv_40d_jerk_v100_signal, "closeadj"),
    _e(f14md_f14_momentum_divergence_flipcount_macd_60d_jerk_v101_signal, "closeadj"),
    _e(f14md_f14_momentum_divergence_cumabs_macd_45d_jerk_v102_signal, "closeadj"),
    _e(f14md_f14_momentum_divergence_convrate_macd_50d_jerk_v103_signal, "closeadj"),
    _e(f14md_f14_momentum_divergence_bullintens_macd_60d_jerk_v104_signal, "closeadj"),
    _e(f14md_f14_momentum_divergence_bearintens_macd_60d_jerk_v105_signal, "closeadj"),
    _e(f14md_f14_momentum_divergence_regresid_macd_40d_jerk_v106_signal, "closeadj"),
    _e(f14md_f14_momentum_divergence_beta_macd_70d_jerk_v107_signal, "closeadj"),
    _e(f14md_f14_momentum_divergence_r2_macd_60d_jerk_v108_signal, "closeadj"),
    _e(f14md_f14_momentum_divergence_curv_macd_35d_jerk_v109_signal, "closeadj"),
    _e(f14md_f14_momentum_divergence_accel_rsi_50d_jerk_v110_signal, "closeadj"),
    _e(f14md_f14_momentum_divergence_lag_macd_50d_jerk_v111_signal, "closeadj"),
    _e(f14md_f14_momentum_divergence_veldiff_cmo_12d_jerk_v112_signal, "close"),
    _e(f14md_f14_momentum_divergence_veldiff_tsi_30d_jerk_v113_signal, "closeadj"),
    _e(f14md_f14_momentum_divergence_veldiff_wpr_15d_jerk_v114_signal, "high", "low", "close"),
    _e(f14md_f14_momentum_divergence_zslp_macd_50d_jerk_v115_signal, "closeadj"),
    _e(f14md_f14_momentum_divergence_corrrank_macd_120d_jerk_v116_signal, "closeadj"),
    _e(f14md_f14_momentum_divergence_pjerk_mjerk_40d_jerk_v117_signal, "closeadj"),
    _e(f14md_f14_momentum_divergence_signdir_macd_30d_jerk_v118_signal, "closeadj"),
    _e(f14md_f14_momentum_divergence_mad_macd_45d_jerk_v119_signal, "closeadj"),
    _e(f14md_f14_momentum_divergence_hfdiv_macd_5d_jerk_v120_signal, "close"),
    _e(f14md_f14_momentum_divergence_msd_macd_60d_jerk_v121_signal, "closeadj"),
    _e(f14md_f14_momentum_divergence_hidden_macd_40d_jerk_v122_signal, "closeadj"),
    _e(f14md_f14_momentum_divergence_slpratio_macd_45d_jerk_v123_signal, "closeadj"),
    _e(f14md_f14_momentum_divergence_pmstoch_avg_50d_jerk_v124_signal, "high", "low", "closeadj"),
    _e(f14md_f14_momentum_divergence_obvmom_60d_jerk_v125_signal, "close", "volume"),
    _e(f14md_f14_momentum_divergence_adapt_macd_80d_jerk_v126_signal, "closeadj"),
    _e(f14md_f14_momentum_divergence_persist_macd_60d_jerk_v127_signal, "closeadj"),
    _e(f14md_f14_momentum_divergence_skew_macd_80d_jerk_v128_signal, "closeadj"),
    _e(f14md_f14_momentum_divergence_kurt_div_rsi_80d_jerk_v129_signal, "closeadj"),
    _e(f14md_f14_momentum_divergence_acfr1_div_60d_jerk_v130_signal, "closeadj"),
    _e(f14md_f14_momentum_divergence_atrnorm_pslp_40d_jerk_v131_signal, "high", "low", "closeadj"),
    _e(f14md_f14_momentum_divergence_argextr_rsi_25d_jerk_v132_signal, "closeadj"),
    _e(f14md_f14_momentum_divergence_argextr_macd_45d_jerk_v133_signal, "closeadj"),
    _e(f14md_f14_momentum_divergence_pctile_div_rsi_60d_jerk_v134_signal, "closeadj"),
    _e(f14md_f14_momentum_divergence_pctile_div_macd_80d_jerk_v135_signal, "closeadj"),
    _e(f14md_f14_momentum_divergence_zspread_rsi_45d_jerk_v136_signal, "closeadj"),
    _e(f14md_f14_momentum_divergence_zspread_macd_70d_jerk_v137_signal, "closeadj"),
    _e(f14md_f14_momentum_divergence_volprice_rsi_50d_jerk_v138_signal, "close", "volume"),
    _e(f14md_f14_momentum_divergence_oscslp_diff_25d_jerk_v139_signal, "closeadj"),
    _e(f14md_f14_momentum_divergence_oscslp_diff_long_60d_jerk_v140_signal, "closeadj"),
    _e(f14md_f14_momentum_divergence_intrabar_diff_5d_jerk_v141_signal, "high", "low", "close", "open"),
    _e(f14md_f14_momentum_divergence_runrocdiff_40d_jerk_v142_signal, "closeadj"),
    _e(f14md_f14_momentum_divergence_pricerocstd_40d_jerk_v143_signal, "closeadj"),
    _e(f14md_f14_momentum_divergence_topqdiv_macd_60d_jerk_v144_signal, "closeadj"),
    _e(f14md_f14_momentum_divergence_corr_pcurv_rsi_50d_jerk_v145_signal, "closeadj"),
    _e(f14md_f14_momentum_divergence_lag2_pr_rsi_55d_jerk_v146_signal, "closeadj"),
    _e(f14md_f14_momentum_divergence_lag_neg2_pr_macd_45d_jerk_v147_signal, "closeadj"),
    _e(f14md_f14_momentum_divergence_zwedge_rsi_macd_60d_jerk_v148_signal, "closeadj"),
    _e(f14md_f14_momentum_divergence_emadiv_rsi_45d_jerk_v149_signal, "closeadj"),
    _e(f14md_f14_momentum_divergence_atrnorm_macd_60d_jerk_v150_signal, "high", "low", "closeadj"),
])


def _synthetic_inputs(n=800, seed=42):
    rng=np.random.default_rng(seed); seg=n//4; rest=n-3*seg
    ret=np.concatenate([rng.normal(0.0012,0.011,seg),rng.normal(-0.0005,0.018,seg),rng.normal(-0.0010,0.014,seg),rng.normal(0.0008,0.012,rest)])
    close=50.0*np.exp(np.cumsum(ret))
    closeadj=close*np.exp(rng.normal(0.0,0.0003,size=n).cumsum())
    intra=rng.normal(0.0,0.008,size=n); open_=close*np.exp(-intra*0.5)
    high=np.maximum(close,open_)*np.exp(np.abs(rng.normal(0.0,0.006,size=n)))
    low=np.minimum(close,open_)*np.exp(-np.abs(rng.normal(0.0,0.006,size=n)))
    volume=rng.lognormal(mean=13.0,sigma=0.6,size=n)
    idx=pd.RangeIndex(n)
    return pd.DataFrame({"open":pd.Series(open_,index=idx,dtype=float),"high":pd.Series(high,index=idx,dtype=float),"low":pd.Series(low,index=idx,dtype=float),"close":pd.Series(close,index=idx,dtype=float),"closeadj":pd.Series(closeadj,index=idx,dtype=float),"volume":pd.Series(volume,index=idx,dtype=float)})


def _self_test():
    df=_synthetic_inputs(800,42); results={}
    for name,entry in f14_momentum_divergence_jerk_001_150_REGISTRY.items():
        out=entry["func"](*[df[c] for c in entry["inputs"]])
        assert isinstance(out,pd.Series); assert len(out)==len(df)
        clean=out.dropna(); assert len(clean)>0, f"{name}: all NaN"
        assert float(clean.std())>0.0 or clean.nunique()>1, f"{name}: constant"
        results[name]=out
    warm=252
    frac=sum(1 for s in results.values() if s.iloc[warm:].isna().mean()<0.5)/len(results)
    assert frac>=0.80, f"coverage frac={frac:.2%}"
    A=pd.concat({n:results[n] for n in results},axis=1).iloc[warm:].replace([np.inf,-np.inf],np.nan)
    C=A.corr(min_periods=50).abs(); np.fill_diagonal(C.values,0.0)
    mc=float(C.max().max())
    if mc>0.95:
        print(f"FAILING max |corr|={mc:.4f}. Top pairs:")
        for i,a in enumerate(C.columns):
            for j,b in enumerate(C.columns):
                if j>i and C.iloc[i,j]>0.94:
                    print(f"  {a}  vs  {b}  -> {C.iloc[i,j]:.4f}")
    assert mc<=0.95+1e-9, f"max pairwise |corr|={mc:.4f} exceeds 0.95"
    print(f"OK jerk_001_150: {len(results)} features, max |corr|={mc:.4f}, coverage_ok={frac:.2%}")


if __name__ == "__main__":
    _self_test()
