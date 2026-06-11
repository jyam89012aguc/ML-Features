"""f03_trend_strength_metrics slope features 001-150 (1st derivative).
Each slope feature is base.diff(k) where k follows the ROC bracket of
the base's primary window. NaN policy: replace([inf,-inf],nan) at return."""
from __future__ import annotations

import numpy as np
import pandas as pd


def _tr(high, low, close):
    pc=close.shift(1)
    return pd.concat([(high-low).abs(),(high-pc).abs(),(low-pc).abs()],axis=1).max(axis=1)

def _wilder(s, n):
    return s.ewm(alpha=1.0/float(n),adjust=False,min_periods=n).mean()

def _plus_dm(high, low):
    up=high.diff(); dn=-low.diff()
    return pd.Series(np.where((up>dn)&(up>0.0),up,0.0),index=high.index,dtype=float)

def _minus_dm(high, low):
    up=high.diff(); dn=-low.diff()
    return pd.Series(np.where((dn>up)&(dn>0.0),dn,0.0),index=high.index,dtype=float)



def f03ts_f03_trend_strength_metrics_adx_50d_slope_v002_signal(high, low, closeadj):
    n=50
    atr=_wilder(_tr(high,low,closeadj),n)
    pdi=100.0*_wilder(_plus_dm(high,low),n)/atr.replace(0.0,np.nan); mdi=100.0*_wilder(_minus_dm(high,low),n)/atr.replace(0.0,np.nan)
    dx=100.0*(pdi-mdi).abs()/(pdi+mdi).replace(0.0,np.nan)
    b=_wilder(dx, n)
    return b.diff(21).replace([np.inf,-np.inf],np.nan)

def f03ts_f03_trend_strength_metrics_dmidiff_21d_slope_v003_signal(high, low, close):
    n=21
    atr=_wilder(_tr(high,low,close),n)
    pdi=100.0*_wilder(_plus_dm(high,low),n)/atr.replace(0.0,np.nan); mdi=100.0*_wilder(_minus_dm(high,low),n)/atr.replace(0.0,np.nan)
    b=pdi - mdi
    return b.diff(10).replace([np.inf,-np.inf],np.nan)

def f03ts_f03_trend_strength_metrics_dmiratio_30d_slope_v004_signal(high, low, closeadj):
    n=30
    atr=_wilder(_tr(high,low,closeadj),n)
    pdi=100.0*_wilder(_plus_dm(high,low),n)/atr.replace(0.0,np.nan); mdi=100.0*_wilder(_minus_dm(high,low),n)/atr.replace(0.0,np.nan)
    s=np.sign(pdi - mdi)
    flip=(s != s.shift(1)).astype(float).where(~s.isna() & ~s.shift(1).isna())
    def _streak(x):
        idx = np.where(x > 0.5)[0]
        if idx.size == 0:
            return 100.0
        return float(len(x) - 1 - idx[-1])
    b=flip.rolling(100,min_periods=100).apply(_streak, raw=True)
    return b.diff(21).replace([np.inf,-np.inf],np.nan)

def f03ts_f03_trend_strength_metrics_adxstrong_60d_slope_v005_signal(high, low, closeadj):
    n=14
    atr=_wilder(_tr(high,low,closeadj),n)
    pdi=100.0*_wilder(_plus_dm(high,low),n)/atr.replace(0.0,np.nan); mdi=100.0*_wilder(_minus_dm(high,low),n)/atr.replace(0.0,np.nan)
    dx=100.0*(pdi-mdi).abs()/(pdi+mdi).replace(0.0,np.nan)
    adx=_wilder(dx,n)
    flag=(adx > 25.0).astype(float).where(~adx.isna())
    b=flag.rolling(60,min_periods=60).mean()
    return b.diff(21).replace([np.inf,-np.inf],np.nan)

def f03ts_f03_trend_strength_metrics_pdi_14d_slope_v006_signal(high, low, close):
    n=14
    atr=_wilder(_tr(high,low,close),n)
    b=100.0 * _wilder(_plus_dm(high, low), n) / atr.replace(0.0,np.nan)
    return b.diff(5).replace([np.inf,-np.inf],np.nan)

def f03ts_f03_trend_strength_metrics_mdi_40d_slope_v007_signal(high, low, closeadj):
    n=40
    atr=_wilder(_tr(high,low,closeadj),n)
    b=100.0 * _wilder(_minus_dm(high, low), n) / atr.replace(0.0,np.nan)
    return b.diff(10).replace([np.inf,-np.inf],np.nan)

def f03ts_f03_trend_strength_metrics_aroonosc_14d_slope_v008_signal(close):
    n=14
    au=close.rolling(n+1,min_periods=n+1).apply(lambda x:100.0*(n-(n-int(np.argmax(x))))/n,raw=True)
    ad=close.rolling(n+1,min_periods=n+1).apply(lambda x:100.0*(n-(n-int(np.argmin(x))))/n,raw=True)
    b=au - ad
    return b.diff(5).replace([np.inf,-np.inf],np.nan)

def f03ts_f03_trend_strength_metrics_aroonosc_50d_slope_v009_signal(closeadj):
    n=50
    au=closeadj.rolling(n+1,min_periods=n+1).apply(lambda x:100.0*(n-(n-int(np.argmax(x))))/n,raw=True)
    ad=closeadj.rolling(n+1,min_periods=n+1).apply(lambda x:100.0*(n-(n-int(np.argmin(x))))/n,raw=True)
    b=au - ad
    return b.diff(21).replace([np.inf,-np.inf],np.nan)

def f03ts_f03_trend_strength_metrics_aroondiff_25d_slope_v010_signal(high, low):
    n=25
    au=high.rolling(n+1,min_periods=n+1).apply(lambda x:100.0*(n-(n-int(np.argmax(x))))/n,raw=True)
    ad=low.rolling(n+1,min_periods=n+1).apply(lambda x:100.0*(n-(n-int(np.argmin(x))))/n,raw=True)
    b=au - ad
    return b.diff(10).replace([np.inf,-np.inf],np.nan)

def f03ts_f03_trend_strength_metrics_aroonsign_30d_slope_v011_signal(closeadj):
    n=30
    au=closeadj.rolling(n+1,min_periods=n+1).apply(lambda x:100.0*(n-(n-int(np.argmax(x))))/n,raw=True)
    ad=closeadj.rolling(n+1,min_periods=n+1).apply(lambda x:100.0*(n-(n-int(np.argmin(x))))/n,raw=True)
    b=np.sign(au - ad)
    return b.diff(10).replace([np.inf,-np.inf],np.nan)

def f03ts_f03_trend_strength_metrics_aroonconv_21d_slope_v012_signal(close):
    n=21
    au=close.rolling(n+1,min_periods=n+1).apply(lambda x:100.0*(n-(n-int(np.argmax(x))))/n,raw=True)
    ad=close.rolling(n+1,min_periods=n+1).apply(lambda x:100.0*(n-(n-int(np.argmin(x))))/n,raw=True)
    b=au + ad
    return b.diff(5).replace([np.inf,-np.inf],np.nan)

def f03ts_f03_trend_strength_metrics_vortexdiff_14d_slope_v013_signal(high, low, close):
    n=14
    tr_n=_tr(high,low,close).rolling(n,min_periods=n).sum()
    vp=(high-low.shift(1)).abs().rolling(n,min_periods=n).sum()/tr_n.replace(0.0,np.nan); vm=(low-high.shift(1)).abs().rolling(n,min_periods=n).sum()/tr_n.replace(0.0,np.nan)
    b=vp - vm
    return b.diff(5).replace([np.inf,-np.inf],np.nan)

def f03ts_f03_trend_strength_metrics_vortexabs_30d_slope_v014_signal(high, low, closeadj):
    n=30
    tr_n=_tr(high,low,closeadj).rolling(n,min_periods=n).sum()
    vp=(high-low.shift(1)).abs().rolling(n,min_periods=n).sum()/tr_n.replace(0.0,np.nan); vm=(low-high.shift(1)).abs().rolling(n,min_periods=n).sum()/tr_n.replace(0.0,np.nan)
    b=(vp - vm).abs()
    return b.diff(21).replace([np.inf,-np.inf],np.nan)

def f03ts_f03_trend_strength_metrics_vortexratio_60d_slope_v015_signal(high, low, closeadj):
    n=60
    tr_n=_tr(high,low,closeadj).rolling(n,min_periods=n).sum()
    vp=(high-low.shift(1)).abs().rolling(n,min_periods=n).sum()/tr_n.replace(0.0,np.nan); vm=(low-high.shift(1)).abs().rolling(n,min_periods=n).sum()/tr_n.replace(0.0,np.nan)
    b=np.log(vp.replace(0.0,np.nan) / vm.replace(0.0,np.nan))
    return b.diff(21).replace([np.inf,-np.inf],np.nan)

def f03ts_f03_trend_strength_metrics_chop_14d_slope_v016_signal(high, low, close):
    n=14
    tr_n=_tr(high,low,close).rolling(n,min_periods=n).sum()
    hh=high.rolling(n,min_periods=n).max(); ll=low.rolling(n,min_periods=n).min()
    b=-100.0 * np.log10(tr_n / (hh - ll).replace(0.0,np.nan)) / np.log10(n)
    return b.diff(5).replace([np.inf,-np.inf],np.nan)

def f03ts_f03_trend_strength_metrics_chop_40d_slope_v017_signal(high, low, closeadj):
    n=40
    tr_n=_tr(high,low,closeadj).rolling(n,min_periods=n).sum()
    hh=high.rolling(n,min_periods=n).max(); ll=low.rolling(n,min_periods=n).min()
    b=-100.0 * np.log10(tr_n / (hh - ll).replace(0.0,np.nan)) / np.log10(n)
    return b.diff(10).replace([np.inf,-np.inf],np.nan)

def f03ts_f03_trend_strength_metrics_choprank_120d_slope_v018_signal(high, low, closeadj):
    n=40
    tr_n=_tr(high,low,closeadj).rolling(n,min_periods=n).sum()
    hh=high.rolling(n,min_periods=n).max(); ll=low.rolling(n,min_periods=n).min()
    chop = 100.0 * np.log10(tr_n / (hh - ll).replace(0.0,np.nan)) / np.log10(n)
    b=chop.rolling(120,min_periods=120).rank(pct=True)
    return b.diff(21).replace([np.inf,-np.inf],np.nan)

def f03ts_f03_trend_strength_metrics_tsi_25_13_slope_v019_signal(close):
    d=close.diff()
    n=d.ewm(span=25, adjust=False,min_periods=25).mean().ewm(span=13, adjust=False,min_periods=13).mean()
    dn=d.abs().ewm(span=25, adjust=False,min_periods=25).mean().ewm(span=13, adjust=False,min_periods=13).mean()
    b=100.0 * n / dn.replace(0.0,np.nan)
    return b.diff(5).replace([np.inf,-np.inf],np.nan)

def f03ts_f03_trend_strength_metrics_tsi_50_25_slope_v020_signal(closeadj):
    d=closeadj.diff()
    n=d.ewm(span=50, adjust=False,min_periods=50).mean().ewm(span=25, adjust=False,min_periods=25).mean()
    dn=d.abs().ewm(span=50, adjust=False,min_periods=50).mean().ewm(span=25, adjust=False,min_periods=25).mean()
    b=100.0 * n / dn.replace(0.0,np.nan)
    return b.diff(21).replace([np.inf,-np.inf],np.nan)

def f03ts_f03_trend_strength_metrics_tsiabs_25_13_slope_v021_signal(close):
    d=close.diff()
    n=d.ewm(span=25, adjust=False,min_periods=25).mean().ewm(span=13, adjust=False,min_periods=13).mean()
    dn=d.abs().ewm(span=25, adjust=False,min_periods=25).mean().ewm(span=13, adjust=False,min_periods=13).mean()
    b=100.0 * n.abs() / dn.replace(0.0,np.nan)
    return b.diff(10).replace([np.inf,-np.inf],np.nan)

def f03ts_f03_trend_strength_metrics_kst_30d_slope_v022_signal(closeadj):
    r1 = closeadj.pct_change(10).rolling(10,min_periods=10).mean()
    r2 = closeadj.pct_change(15).rolling(10,min_periods=10).mean()
    r3 = closeadj.pct_change(20).rolling(10,min_periods=10).mean()
    r4 = closeadj.pct_change(30).rolling(15,min_periods=15).mean()
    b=1.0 * r1 + 2.0 * r2 + 3.0 * r3 + 4.0 * r4
    return b.diff(10).replace([np.inf,-np.inf],np.nan)

def f03ts_f03_trend_strength_metrics_kstlong_120d_slope_v023_signal(closeadj):
    r1 = closeadj.pct_change(40).rolling(20,min_periods=20).mean()
    r2 = closeadj.pct_change(60).rolling(20,min_periods=20).mean()
    r3 = closeadj.pct_change(90).rolling(30,min_periods=30).mean()
    r4 = closeadj.pct_change(120).rolling(40,min_periods=40).mean()
    b=1.0 * r1 + 2.0 * r2 + 3.0 * r3 + 4.0 * r4
    return b.diff(63).replace([np.inf,-np.inf],np.nan)

def f03ts_f03_trend_strength_metrics_kefr_10d_slope_v024_signal(close):
    n=10
    b=(close - close.shift(n)).abs() / close.diff().abs().rolling(n,min_periods=n).sum().replace(0.0,np.nan)
    return b.diff(5).replace([np.inf,-np.inf],np.nan)

def f03ts_f03_trend_strength_metrics_kefr_40d_slope_v025_signal(closeadj):
    n=40
    b=(closeadj - closeadj.shift(n)).abs() / closeadj.diff().abs().rolling(n,min_periods=n).sum().replace(0.0,np.nan)
    return b.diff(10).replace([np.inf,-np.inf],np.nan)

def f03ts_f03_trend_strength_metrics_kefr_120d_slope_v026_signal(closeadj):
    n=120
    b=(closeadj - closeadj.shift(n)).abs() / closeadj.diff().abs().rolling(n,min_periods=n).sum().replace(0.0,np.nan)
    return b.diff(63).replace([np.inf,-np.inf],np.nan)

def f03ts_f03_trend_strength_metrics_kefrsigned_30d_slope_v027_signal(closeadj):
    n=30
    raw=closeadj - closeadj.shift(n)
    v=closeadj.diff().abs().rolling(n,min_periods=n).sum()
    b=raw / v.replace(0.0,np.nan)
    return b.diff(21).replace([np.inf,-np.inf],np.nan)

def f03ts_f03_trend_strength_metrics_kefrhl_25d_slope_v028_signal(high, low):
    n=25
    mid=0.5 * (high + low)
    b=(mid - mid.shift(n)).abs() / mid.diff().abs().rolling(n,min_periods=n).sum().replace(0.0,np.nan)
    return b.diff(10).replace([np.inf,-np.inf],np.nan)

def f03ts_f03_trend_strength_metrics_r2lin_20d_slope_v029_signal(close):
    n=20
    def _r2(x):
        if not np.all(np.isfinite(x)):return np.nan
        t=np.arange(n,dtype=float); a=np.polyfit(t,x,1)
        yhat = a[0] * t + a[1]
        ss_res = float(np.sum((x - yhat) ** 2)); ss_tot = float(np.sum((x - x.mean()) ** 2))
        if ss_tot <= 0: return np.nan
        return 1.0 - ss_res / ss_tot
    b=close.rolling(n,min_periods=n).apply(_r2, raw=True)
    return b.diff(5).replace([np.inf,-np.inf],np.nan)

def f03ts_f03_trend_strength_metrics_r2lin_63d_slope_v030_signal(closeadj):
    n=63
    def _r2(x):
        if not np.all(np.isfinite(x)):return np.nan
        t=np.arange(n,dtype=float); a=np.polyfit(t,x,1)
        yhat = a[0] * t + a[1]
        ss_res = float(np.sum((x - yhat) ** 2)); ss_tot = float(np.sum((x - x.mean()) ** 2))
        if ss_tot <= 0: return np.nan
        return 1.0 - ss_res / ss_tot
    b=closeadj.rolling(n,min_periods=n).apply(_r2, raw=True)
    return b.diff(21).replace([np.inf,-np.inf],np.nan)

def f03ts_f03_trend_strength_metrics_r2log_120d_slope_v031_signal(closeadj):
    n=120
    def _r2(x):
        if np.any(~np.isfinite(x)) or np.any(x <= 0): return np.nan
        y = np.log(x); t = np.arange(n, dtype=float)
        a = np.polyfit(t, y, 1)
        yhat = a[0] * t + a[1]
        ss_res = float(np.sum((y - yhat) ** 2)); ss_tot = float(np.sum((y - y.mean()) ** 2))
        if ss_tot <= 0: return np.nan
        return 1.0 - ss_res / ss_tot
    b=closeadj.rolling(n,min_periods=n).apply(_r2, raw=True)
    return b.diff(63).replace([np.inf,-np.inf],np.nan)

def f03ts_f03_trend_strength_metrics_logregslp_60d_slope_v032_signal(closeadj):
    n=60
    def _slope(x):
        if np.any(~np.isfinite(x)) or np.any(x <= 0): return np.nan
        y = np.log(x); t = np.arange(n, dtype=float)
        return float(np.polyfit(t, y, 1)[0])
    b=closeadj.rolling(n,min_periods=n).apply(_slope, raw=True)
    return b.diff(21).replace([np.inf,-np.inf],np.nan)

def f03ts_f03_trend_strength_metrics_regrres_30d_slope_v033_signal(closeadj):
    n=30
    def _resstd(x):
        if not np.all(np.isfinite(x)):return np.nan
        t=np.arange(n,dtype=float); a=np.polyfit(t,x,1)
        yhat = a[0] * t + a[1]
        return float(np.std(x - yhat, ddof=1))
    b=closeadj.rolling(n,min_periods=n).apply(_resstd, raw=True)
    return b.diff(10).replace([np.inf,-np.inf],np.nan)

def f03ts_f03_trend_strength_metrics_robtrend_40d_slope_v034_signal(closeadj):
    n=40
    def _calc(x):
        if not np.all(np.isfinite(x)):return np.nan
        t=np.arange(n,dtype=float); a=np.polyfit(t,x,1)
        resid=x-(a[0]*t+a[1])
        mad = float(np.median(np.abs(resid-np.median(resid))))
        if mad<=0:return np.nan
        return abs(float(a[0]))/mad
    b=closeadj.rolling(n,min_periods=n).apply(_calc, raw=True)
    return b.diff(21).replace([np.inf,-np.inf],np.nan)

def f03ts_f03_trend_strength_metrics_poly2coef_50d_slope_v035_signal(closeadj):
    n=50
    def _quad(x):
        if not np.all(np.isfinite(x)):return np.nan
        t = np.arange(n, dtype=float) / n
        a = np.polyfit(t, x, 2)
        return float(a[0])
    b=closeadj.rolling(n,min_periods=n).apply(_quad, raw=True)
    return b.diff(10).replace([np.inf,-np.inf],np.nan)

def f03ts_f03_trend_strength_metrics_lastresid_30d_slope_v036_signal(closeadj):
    n=30
    def _resz(x):
        if not np.all(np.isfinite(x)):return np.nan
        t=np.arange(n,dtype=float); a=np.polyfit(t,x,1)
        resid=x-(a[0]*t+a[1])
        sd=float(np.std(resid,ddof=1))
        if sd<=0:return np.nan
        return float(resid[-1]/sd)
    b=closeadj.rolling(n,min_periods=n).apply(_resz, raw=True)
    return b.diff(21).replace([np.inf,-np.inf],np.nan)

def f03ts_f03_trend_strength_metrics_hurstrs_80d_slope_v037_signal(closeadj):
    n=80
    def _h(x):
        x=np.asarray(x,dtype=float)
        if not np.all(np.isfinite(x)):return np.nan
        r=np.diff(np.log(x))
        if r.size<8:return np.nan
        y=r-r.mean(); z=np.cumsum(y); R=z.max()-z.min(); S=r.std(ddof=1)
        if S<=0 or R<=0:return np.nan
        return float(np.log(R/S)/np.log(len(r)))
    b=closeadj.rolling(n,min_periods=n).apply(_h, raw=True)
    return b.diff(21).replace([np.inf,-np.inf],np.nan)

def f03ts_f03_trend_strength_metrics_hurstrs_160d_slope_v038_signal(closeadj):
    n=160
    def _h(x):
        x=np.asarray(x,dtype=float)
        if not np.all(np.isfinite(x)):return np.nan
        r=np.diff(np.log(x))
        if r.size<8:return np.nan
        y=r-r.mean(); z=np.cumsum(y); R=z.max()-z.min(); S=r.std(ddof=1)
        if S<=0 or R<=0:return np.nan
        return float(np.log(R/S)/np.log(len(r)))
    b=closeadj.rolling(n,min_periods=n).apply(_h, raw=True)
    return b.diff(63).replace([np.inf,-np.inf],np.nan)

def f03ts_f03_trend_strength_metrics_varratio_30d_slope_v039_signal(closeadj):
    n=30; q = 5
    r1=np.log(closeadj).diff(); rq=np.log(closeadj).diff(q)
    v1=r1.rolling(n,min_periods=n).var(ddof=1); vq=rq.rolling(n,min_periods=n).var(ddof=1)
    b=vq / (q * v1.replace(0.0,np.nan)) - 1.0
    return b.diff(10).replace([np.inf,-np.inf],np.nan)

def f03ts_f03_trend_strength_metrics_varratio_100d_slope_v040_signal(closeadj):
    n=100; q = 10
    r1=np.log(closeadj).diff(); rq=np.log(closeadj).diff(q)
    v1=r1.rolling(n,min_periods=n).var(ddof=1); vq=rq.rolling(n,min_periods=n).var(ddof=1)
    b=vq / (q * v1.replace(0.0,np.nan)) - 1.0
    return b.diff(63).replace([np.inf,-np.inf],np.nan)

def f03ts_f03_trend_strength_metrics_mks_30d_slope_v041_signal(closeadj):
    n=30; norm=n*(n-1)/2.0
    def _mk(x):
        if not np.all(np.isfinite(x)):return np.nan
        s=0
        for i in range(n-1):
            d=x[i+1:]-x[i]; s+=int(np.sum(d>0)-np.sum(d<0))
        return s/norm
    b=closeadj.rolling(n,min_periods=n).apply(_mk, raw=True)
    return b.diff(21).replace([np.inf,-np.inf],np.nan)

def f03ts_f03_trend_strength_metrics_mksabs_60d_slope_v042_signal(closeadj):
    n=60; norm=n*(n-1)/2.0
    def _mk(x):
        if not np.all(np.isfinite(x)):return np.nan
        s=0
        for i in range(n-1):
            d=x[i+1:]-x[i]; s+=int(np.sum(d>0)-np.sum(d<0))
        return s/norm
    raw=closeadj.rolling(n,min_periods=n).apply(_mk, raw=True)
    b=raw.rolling(120,min_periods=120).rank(pct=True)
    return b.diff(21).replace([np.inf,-np.inf],np.nan)

def f03ts_f03_trend_strength_metrics_uprun_20d_slope_v043_signal(close):
    n=20; diff=close.diff()
    def _lup(x):
        if np.any(np.isnan(x)):return np.nan
        best=0; cur=0
        for v in x:
            if v>0:
                cur+=1
                if cur>best:best=cur
            else: cur=0
        return float(best)
    b=diff.rolling(n,min_periods=n).apply(_lup,raw=True)
    return b.diff(5).replace([np.inf,-np.inf],np.nan)

def f03ts_f03_trend_strength_metrics_dnrun_60d_slope_v044_signal(closeadj):
    n=60; diff=closeadj.diff()
    def _ldn(x):
        if np.any(np.isnan(x)):return np.nan
        best=0; cur=0
        for v in x:
            if v<0:
                cur+=1
                if cur>best:best=cur
            else: cur=0
        return float(best)
    b=diff.rolling(n,min_periods=n).apply(_ldn,raw=True)
    return b.diff(21).replace([np.inf,-np.inf],np.nan)

def f03ts_f03_trend_strength_metrics_signfrac_40d_slope_v045_signal(closeadj):
    n=40
    diff=closeadj.diff()
    cum = closeadj - closeadj.shift(n)
    sd=np.sign(diff); sc = np.sign(cum)
    flag=(sd == sc).astype(float).where(~sd.isna() & ~sc.isna())
    b=flag.rolling(n,min_periods=n).mean()
    return b.diff(10).replace([np.inf,-np.inf],np.nan)

def f03ts_f03_trend_strength_metrics_upfrac_15d_slope_v046_signal(close):
    n=15
    flag=(close.diff() > 0).astype(float).where(~close.diff().isna())
    b=flag.rolling(n,min_periods=n).mean()
    return b.diff(5).replace([np.inf,-np.inf],np.nan)

def f03ts_f03_trend_strength_metrics_dirpersist_50d_slope_v047_signal(closeadj):
    n=50
    sgn=np.sign(closeadj.diff())
    b=sgn.rolling(n,min_periods=n).sum().abs() / n
    return b.diff(21).replace([np.inf,-np.inf],np.nan)

def f03ts_f03_trend_strength_metrics_smaplusdm_20d_slope_v048_signal(high, low):
    n=20
    tr_proxy = (high - low).rolling(n,min_periods=n).mean()
    b=_plus_dm(high, low).rolling(n,min_periods=n).mean() / tr_proxy.replace(0.0,np.nan)
    return b.diff(5).replace([np.inf,-np.inf],np.nan)

def f03ts_f03_trend_strength_metrics_smaminusdm_60d_slope_v049_signal(high, low):
    n=60
    tr_proxy = (high - low).rolling(n,min_periods=n).mean()
    b=_minus_dm(high, low).rolling(n,min_periods=n).mean() / tr_proxy.replace(0.0,np.nan)
    return b.diff(21).replace([np.inf,-np.inf],np.nan)

def f03ts_f03_trend_strength_metrics_dmrank_120d_slope_v050_signal(high, low):
    pdm = _wilder(_plus_dm(high, low), 14)
    mdm = _wilder(_minus_dm(high, low), 14)
    b=(pdm - mdm).rolling(120,min_periods=120).rank(pct=True)
    return b.diff(63).replace([np.inf,-np.inf],np.nan)

def f03ts_f03_trend_strength_metrics_adxregime_14d_slope_v051_signal(high, low, close):
    n=14
    atr=_wilder(_tr(high,low,close),n)
    pdi=100.0*_wilder(_plus_dm(high,low),n)/atr.replace(0.0,np.nan); mdi=100.0*_wilder(_minus_dm(high,low),n)/atr.replace(0.0,np.nan)
    dx=100.0*(pdi-mdi).abs()/(pdi+mdi).replace(0.0,np.nan)
    adx=_wilder(dx,n)
    b=np.sign(adx - 25.0)
    return b.diff(10).replace([np.inf,-np.inf],np.nan)

def f03ts_f03_trend_strength_metrics_adxhigh_50d_slope_v052_signal(high, low, closeadj):
    n=14
    atr=_wilder(_tr(high,low,closeadj),n)
    pdi=100.0*_wilder(_plus_dm(high,low),n)/atr.replace(0.0,np.nan); mdi=100.0*_wilder(_minus_dm(high,low),n)/atr.replace(0.0,np.nan)
    dx=100.0*(pdi-mdi).abs()/(pdi+mdi).replace(0.0,np.nan)
    adx=_wilder(dx,n)
    flag=(adx > 30.0).astype(float).where(~adx.isna())
    b=flag.rolling(50,min_periods=50).sum()
    return b.diff(21).replace([np.inf,-np.inf],np.nan)

def f03ts_f03_trend_strength_metrics_bullbearcnt_30d_slope_v053_signal(closeadj):
    direction=np.sign(closeadj - closeadj.shift(20))
    daily=np.sign(closeadj.diff())
    agree=direction * daily
    b=agree.rolling(30,min_periods=30).sum()
    return b.diff(10).replace([np.inf,-np.inf],np.nan)

def f03ts_f03_trend_strength_metrics_aroonstrong_50d_slope_v054_signal(closeadj):
    n=25
    au=closeadj.rolling(n+1,min_periods=n+1).apply(lambda x:100.0*(n-(n-int(np.argmax(x))))/n,raw=True)
    ad=closeadj.rolling(n+1,min_periods=n+1).apply(lambda x:100.0*(n-(n-int(np.argmin(x))))/n,raw=True)
    bullish = (au > 70.0).astype(float); bearish = (ad > 70.0).astype(float)
    b=(bullish - bearish).rolling(50,min_periods=50).sum()
    return b.diff(21).replace([np.inf,-np.inf],np.nan)

def f03ts_f03_trend_strength_metrics_adxdiff_30d_slope_v055_signal(high, low, closeadj):
    def _adx(n):
        atr=_wilder(_tr(high,low,closeadj),n)
        pdi=100.0*_wilder(_plus_dm(high, low), n) / atr.replace(0.0,np.nan)
        mdi=100.0*_wilder(_minus_dm(high, low), n) / atr.replace(0.0,np.nan)
        dx = 100.0 * (pdi - mdi).abs() / (pdi + mdi).replace(0.0,np.nan)
        return _wilder(dx, n)
    b=np.sign(_adx(14) - _adx(60))
    return b.diff(10).replace([np.inf,-np.inf],np.nan)

def f03ts_f03_trend_strength_metrics_kerdiff_30d_slope_v056_signal(closeadj):
    def _ker(n):
        d=(closeadj - closeadj.shift(n)).abs()
        v=closeadj.diff().abs().rolling(n,min_periods=n).sum()
        return d / v.replace(0.0,np.nan)
    b=_ker(20) - _ker(60)
    return b.diff(21).replace([np.inf,-np.inf],np.nan)

def f03ts_f03_trend_strength_metrics_tsidiff_30d_slope_v057_signal(closeadj):
    def _tsi(r, s):
        d=closeadj.diff()
        n=d.ewm(span=r, adjust=False,min_periods=r).mean().ewm(span=s, adjust=False,min_periods=s).mean()
        dn=d.abs().ewm(span=r, adjust=False,min_periods=r).mean().ewm(span=s, adjust=False,min_periods=s).mean()
        return 100.0 * n / dn.replace(0.0,np.nan)
    b=_tsi(25, 13) - _tsi(50, 25)
    return b.diff(10).replace([np.inf,-np.inf],np.nan)

def f03ts_f03_trend_strength_metrics_tanhker_30d_slope_v058_signal(closeadj):
    dir60 = np.sign(closeadj - closeadj.shift(60))
    s5 = np.sign(closeadj.rolling(5,min_periods=5).mean().diff(5))
    s20 = np.sign(closeadj.rolling(20,min_periods=20).mean().diff(5))
    s50 = np.sign(closeadj.rolling(50,min_periods=50).mean().diff(10))
    s100 = np.sign(closeadj.rolling(100,min_periods=100).mean().diff(21))
    agree=((s5 == dir60).astype(float) + (s20 == dir60).astype(float)
             + (s50 == dir60).astype(float) + (s100 == dir60).astype(float))
    mask=dir60.isna() | s5.isna() | s20.isna() | s50.isna() | s100.isna()
    b=agree.where(~mask)
    return b.diff(21).replace([np.inf,-np.inf],np.nan)

def f03ts_f03_trend_strength_metrics_arctanmk_40d_slope_v059_signal(closeadj):
    n=40; norm=n*(n-1)/2.0
    def _mk(x):
        if not np.all(np.isfinite(x)):return np.nan
        s=0
        for i in range(n-1):
            d=x[i+1:]-x[i]; s+=int(np.sum(d>0)-np.sum(d<0))
        return s/norm
    raw=closeadj.rolling(n,min_periods=n).apply(_mk, raw=True)
    b=np.arctan(3.0 * raw) / (np.pi / 2.0)
    return b.diff(10).replace([np.inf,-np.inf],np.nan)

def f03ts_f03_trend_strength_metrics_adxslope_30d_slope_v060_signal(high, low, closeadj):
    n=14
    atr=_wilder(_tr(high,low,closeadj),n)
    pdi=100.0*_wilder(_plus_dm(high,low),n)/atr.replace(0.0,np.nan); mdi=100.0*_wilder(_minus_dm(high,low),n)/atr.replace(0.0,np.nan)
    dx=100.0*(pdi-mdi).abs()/(pdi+mdi).replace(0.0,np.nan)
    adx=_wilder(dx,n)
    b=adx.diff(5)
    return b.diff(10).replace([np.inf,-np.inf],np.nan)

def f03ts_f03_trend_strength_metrics_adxcurv_40d_slope_v061_signal(high, low, closeadj):
    n=14
    atr=_wilder(_tr(high,low,closeadj),n)
    pdi=100.0*_wilder(_plus_dm(high,low),n)/atr.replace(0.0,np.nan); mdi=100.0*_wilder(_minus_dm(high,low),n)/atr.replace(0.0,np.nan)
    dx=100.0*(pdi-mdi).abs()/(pdi+mdi).replace(0.0,np.nan)
    adx=_wilder(dx,n)
    b=adx - 2.0 * adx.shift(10) + adx.shift(20)
    return b.diff(10).replace([np.inf,-np.inf],np.nan)

def f03ts_f03_trend_strength_metrics_corrtrend_25d_slope_v062_signal(close):
    n=25
    def _rc(x):
        if not np.all(np.isfinite(x)):return np.nan
        rx = pd.Series(x).rank().to_numpy()
        rt = np.arange(1, n + 1, dtype=float)
        return float(np.corrcoef(rx, rt)[0, 1])
    b=close.rolling(n,min_periods=n).apply(_rc, raw=True)
    return b.diff(10).replace([np.inf,-np.inf],np.nan)

def f03ts_f03_trend_strength_metrics_corrtrend_120d_slope_v063_signal(closeadj):
    n=80
    absdiff = closeadj.diff().abs()
    def _rc(x):
        if not np.all(np.isfinite(x)):return np.nan
        rx = pd.Series(x).rank().to_numpy()
        rt = np.arange(1, n + 1, dtype=float)
        c = np.corrcoef(rx, rt)
        return float(abs(c[0, 1]))
    b=absdiff.rolling(n,min_periods=n).apply(_rc, raw=True)
    return b.diff(21).replace([np.inf,-np.inf],np.nan)

def f03ts_f03_trend_strength_metrics_signdiff_30d_slope_v064_signal(closeadj):
    n=30
    b=np.sign(closeadj.diff()).rolling(n,min_periods=n).sum() / n
    return b.diff(10).replace([np.inf,-np.inf],np.nan)

def f03ts_f03_trend_strength_metrics_signagree_25d_slope_v065_signal(close):
    n=25
    sgn=np.sign(close.diff())
    b=(sgn * sgn.shift(1)).rolling(n,min_periods=n).mean()
    return b.diff(5).replace([np.inf,-np.inf],np.nan)

def f03ts_f03_trend_strength_metrics_acfr1_60d_slope_v066_signal(closeadj):
    n=60
    r=np.log(closeadj).diff()
    def _ac(x):
        x = np.asarray(x, dtype=float)
        if not np.all(np.isfinite(x)):return np.nan
        a = x[:-1]; b_ = x[1:]
        if a.std() <= 0 or b_.std() <= 0: return np.nan
        return float(np.corrcoef(a, b_)[0, 1])
    b=r.rolling(n,min_periods=n).apply(_ac, raw=True)
    return b.diff(21).replace([np.inf,-np.inf],np.nan)

def f03ts_f03_trend_strength_metrics_dmi_xover_30d_slope_v067_signal(high, low, closeadj):
    n=30
    pdi=100.0*_wilder(_plus_dm(high, low), 14) / _wilder(_tr(high, low, closeadj), 14).replace(0.0,np.nan)
    mdi=100.0*_wilder(_minus_dm(high, low), 14) / _wilder(_tr(high, low, closeadj), 14).replace(0.0,np.nan)
    s=np.sign(pdi - mdi)
    xover = (s != s.shift(1)).astype(float).where(~s.isna() & ~s.shift(1).isna())
    b=-xover.rolling(n,min_periods=n).sum()
    return b.diff(10).replace([np.inf,-np.inf],np.nan)

def f03ts_f03_trend_strength_metrics_tdays_dmihigh_60d_slope_v068_signal(high, low, closeadj):
    n=14
    atr=_wilder(_tr(high,low,closeadj),n)
    pdi=100.0*_wilder(_plus_dm(high,low),n)/atr.replace(0.0,np.nan); mdi=100.0*_wilder(_minus_dm(high,low),n)/atr.replace(0.0,np.nan)
    cond=((pdi - mdi).abs() > 30.0).astype(float).where(~pdi.isna() & ~mdi.isna())
    def _dsince(x):
        idx = np.where(x > 0.5)[0]
        if idx.size == 0: return 60.0
        return float(len(x) - 1 - idx[-1])
    b=cond.rolling(60,min_periods=60).apply(_dsince, raw=True)
    return b.diff(21).replace([np.inf,-np.inf],np.nan)

def f03ts_f03_trend_strength_metrics_tslowstr_30d_slope_v069_signal(high, low, closeadj):
    n=14
    atr=_wilder(_tr(high,low,closeadj),n)
    pdi=100.0*_wilder(_plus_dm(high,low),n)/atr.replace(0.0,np.nan); mdi=100.0*_wilder(_minus_dm(high,low),n)/atr.replace(0.0,np.nan)
    dx=100.0*(pdi-mdi).abs()/(pdi+mdi).replace(0.0,np.nan)
    adx=_wilder(dx,n)
    q33 = adx.rolling(120,min_periods=120).quantile(0.33)
    flag=(adx < q33).astype(float).where(~adx.isna() & ~q33.isna())
    b=flag.rolling(30,min_periods=30).mean()
    return b.diff(10).replace([np.inf,-np.inf],np.nan)

def f03ts_f03_trend_strength_metrics_chopslope_30d_slope_v070_signal(high, low, closeadj):
    n=14
    tr_n=_tr(high,low,closeadj).rolling(n,min_periods=n).sum()
    hh=high.rolling(n,min_periods=n).max(); ll=low.rolling(n,min_periods=n).min()
    chop = -100.0 * np.log10(tr_n / (hh - ll).replace(0.0,np.nan)) / np.log10(n)
    b=chop.diff(10)
    return b.diff(10).replace([np.inf,-np.inf],np.nan)

def f03ts_f03_trend_strength_metrics_aroonslope_30d_slope_v071_signal(closeadj):
    n=25
    au=closeadj.rolling(n+1,min_periods=n+1).apply(lambda x:100.0*(n-(n-int(np.argmax(x))))/n,raw=True)
    ad=closeadj.rolling(n+1,min_periods=n+1).apply(lambda x:100.0*(n-(n-int(np.argmin(x))))/n,raw=True)
    osc=au - ad
    b=osc.diff(5)
    return b.diff(10).replace([np.inf,-np.inf],np.nan)

def f03ts_f03_trend_strength_metrics_vortexslope_30d_slope_v072_signal(high, low, closeadj):
    n=21
    tr_n=_tr(high,low,closeadj).rolling(n,min_periods=n).sum()
    vp=(high-low.shift(1)).abs().rolling(n,min_periods=n).sum()/tr_n.replace(0.0,np.nan); vm=(low-high.shift(1)).abs().rolling(n,min_periods=n).sum()/tr_n.replace(0.0,np.nan)
    b=(vp - vm).abs().diff(10)
    return b.diff(5).replace([np.inf,-np.inf],np.nan)

def f03ts_f03_trend_strength_metrics_persistz_60d_slope_v073_signal(closeadj):
    n=60
    sgn=np.sign(closeadj.diff())
    s=sgn.rolling(n,min_periods=n).sum().abs()
    mu=s.rolling(120,min_periods=120).mean()
    sd=s.rolling(120,min_periods=120).std(ddof=1)
    b=(s - mu) / sd.replace(0.0,np.nan)
    return b.diff(21).replace([np.inf,-np.inf],np.nan)

def f03ts_f03_trend_strength_metrics_efrhl_50d_slope_v074_signal(high, low):
    n=50
    mid=0.5 * (high + low)
    b=(mid - mid.shift(n)) / mid.diff().abs().rolling(n,min_periods=n).sum().replace(0.0,np.nan)
    return b.diff(21).replace([np.inf,-np.inf],np.nan)

def f03ts_f03_trend_strength_metrics_efrkam_15d_slope_v075_signal(close):
    n=15
    er=(close - close.shift(n)).abs() / close.diff().abs().rolling(n,min_periods=n).sum().replace(0.0,np.nan)
    b=er ** 2
    return b.diff(5).replace([np.inf,-np.inf],np.nan)


def f03ts_f03_trend_strength_metrics_adx_8d_slope_v076_signal(high, low, close):
    n=8
    atr=_wilder(_tr(high,low,close),n)
    pdi=100.0*_wilder(_plus_dm(high,low),n)/atr.replace(0.0,np.nan); mdi=100.0*_wilder(_minus_dm(high,low),n)/atr.replace(0.0,np.nan)
    dx=100.0*(pdi-mdi).abs()/(pdi+mdi).replace(0.0,np.nan)
    b=_wilder(dx, n)
    return b.diff(10).replace([np.inf,-np.inf],np.nan)

def f03ts_f03_trend_strength_metrics_adxrank_120d_slope_v077_signal(high, low, closeadj):
    n=14
    atr=_wilder(_tr(high,low,closeadj),n)
    pdi=100.0*_wilder(_plus_dm(high,low),n)/atr.replace(0.0,np.nan); mdi=100.0*_wilder(_minus_dm(high,low),n)/atr.replace(0.0,np.nan)
    dx=100.0*(pdi-mdi).abs()/(pdi+mdi).replace(0.0,np.nan)
    adx=_wilder(dx,n)
    b=adx.rolling(120,min_periods=120).rank(pct=True)
    return b.diff(63).replace([np.inf,-np.inf],np.nan)

def f03ts_f03_trend_strength_metrics_pdimrnk_60d_slope_v078_signal(high, low, closeadj):
    n=21
    atr=_wilder(_tr(high,low,closeadj),n)
    pdi=100.0*_wilder(_plus_dm(high,low),n)/atr.replace(0.0,np.nan); mdi=100.0*_wilder(_minus_dm(high,low),n)/atr.replace(0.0,np.nan)
    b=np.sign(pdi - mdi)
    return b.diff(10).replace([np.inf,-np.inf],np.nan)

def f03ts_f03_trend_strength_metrics_dxraw_14d_slope_v079_signal(high, low, close):
    n=14
    atr=_wilder(_tr(high,low,close),n)
    pdi=100.0*_wilder(_plus_dm(high,low),n)/atr.replace(0.0,np.nan); mdi=100.0*_wilder(_minus_dm(high,low),n)/atr.replace(0.0,np.nan)
    b=100.0 * (pdi - mdi).abs() / (pdi + mdi).replace(0.0,np.nan)
    return b.diff(5).replace([np.inf,-np.inf],np.nan)

def f03ts_f03_trend_strength_metrics_adxz_60d_slope_v080_signal(high, low, closeadj):
    n=14
    atr=_wilder(_tr(high,low,closeadj),n)
    pdi=100.0*_wilder(_plus_dm(high,low),n)/atr.replace(0.0,np.nan); mdi=100.0*_wilder(_minus_dm(high,low),n)/atr.replace(0.0,np.nan)
    dx=100.0*(pdi-mdi).abs()/(pdi+mdi).replace(0.0,np.nan)
    adx=_wilder(dx,n)
    mu=adx.rolling(60,min_periods=60).mean(); sd = adx.rolling(60,min_periods=60).std(ddof=1)
    b=(adx - mu) / sd.replace(0.0,np.nan)
    return b.diff(21).replace([np.inf,-np.inf],np.nan)

def f03ts_f03_trend_strength_metrics_aroonup_18d_slope_v081_signal(close):
    n=18
    b=close.rolling(n+1,min_periods=n+1).apply(lambda x:100.0*(n-(n-int(np.argmax(x))))/n,raw=True)
    return b.diff(10).replace([np.inf,-np.inf],np.nan)

def f03ts_f03_trend_strength_metrics_aroondn_40d_slope_v082_signal(closeadj):
    n=40
    b=closeadj.rolling(n+1,min_periods=n+1).apply(lambda x:100.0*(n-(n-int(np.argmin(x))))/n,raw=True)
    return b.diff(10).replace([np.inf,-np.inf],np.nan)

def f03ts_f03_trend_strength_metrics_aroonlog_25d_slope_v083_signal(closeadj):
    n=25
    au=closeadj.rolling(n+1,min_periods=n+1).apply(lambda x:100.0*(n-(n-int(np.argmax(x))))/n,raw=True)
    ad=closeadj.rolling(n+1,min_periods=n+1).apply(lambda x:100.0*(n-(n-int(np.argmin(x))))/n,raw=True)
    b=np.log((au + 1.0) / (ad + 1.0))
    return b.diff(21).replace([np.inf,-np.inf],np.nan)

def f03ts_f03_trend_strength_metrics_viplus_21d_slope_v084_signal(high, low, close):
    n=21
    tr_n=_tr(high,low,close).rolling(n,min_periods=n).sum()
    b=(high - low.shift(1)).abs().rolling(n,min_periods=n).sum() / tr_n.replace(0.0,np.nan)
    return b.diff(5).replace([np.inf,-np.inf],np.nan)

def f03ts_f03_trend_strength_metrics_viminus_40d_slope_v085_signal(high, low, closeadj):
    n=40
    tr_n=_tr(high,low,closeadj).rolling(n,min_periods=n).sum()
    b=(low - high.shift(1)).abs().rolling(n,min_periods=n).sum() / tr_n.replace(0.0,np.nan)
    return b.diff(21).replace([np.inf,-np.inf],np.nan)

def f03ts_f03_trend_strength_metrics_visum_50d_slope_v086_signal(high, low, closeadj):
    n=50
    tr_n=_tr(high,low,closeadj).rolling(n,min_periods=n).sum()
    vp=(high-low.shift(1)).abs().rolling(n,min_periods=n).sum()/tr_n.replace(0.0,np.nan); vm=(low-high.shift(1)).abs().rolling(n,min_periods=n).sum()/tr_n.replace(0.0,np.nan)
    b=vp + vm
    return b.diff(10).replace([np.inf,-np.inf],np.nan)

def f03ts_f03_trend_strength_metrics_chop_28d_slope_v087_signal(high, low, closeadj):
    n=28
    tr_n=_tr(high,low,closeadj).rolling(n,min_periods=n).sum()
    hh=high.rolling(n,min_periods=n).max(); ll=low.rolling(n,min_periods=n).min()
    b=-100.0 * np.log10(tr_n / (hh - ll).replace(0.0,np.nan)) / np.log10(n)
    return b.diff(21).replace([np.inf,-np.inf],np.nan)

def f03ts_f03_trend_strength_metrics_chopdiff_30d_slope_v088_signal(high, low, closeadj):
    def _chop(n):
        tr_n=_tr(high,low,closeadj).rolling(n,min_periods=n).sum()
        hh=high.rolling(n,min_periods=n).max(); ll=low.rolling(n,min_periods=n).min()
        return 100.0 * np.log10(tr_n / (hh - ll).replace(0.0,np.nan)) / np.log10(n)
    b=_chop(14) - _chop(56)
    return b.diff(10).replace([np.inf,-np.inf],np.nan)

def f03ts_f03_trend_strength_metrics_tsi_13_7_slope_v089_signal(close):
    d=close.diff()
    n=d.ewm(span=13, adjust=False,min_periods=13).mean().ewm(span=7, adjust=False,min_periods=7).mean()
    dn=d.abs().ewm(span=13, adjust=False,min_periods=13).mean().ewm(span=7, adjust=False,min_periods=7).mean()
    b=100.0 * n / dn.replace(0.0,np.nan)
    return b.diff(5).replace([np.inf,-np.inf],np.nan)

def f03ts_f03_trend_strength_metrics_tsihigh_25_13_slope_v090_signal(high):
    d=high.diff()
    n=d.ewm(span=25, adjust=False,min_periods=25).mean().ewm(span=13, adjust=False,min_periods=13).mean()
    dn=d.abs().ewm(span=25, adjust=False,min_periods=25).mean().ewm(span=13, adjust=False,min_periods=13).mean()
    b=100.0 * n / dn.replace(0.0,np.nan)
    return b.diff(10).replace([np.inf,-np.inf],np.nan)

def f03ts_f03_trend_strength_metrics_kefr_5d_slope_v091_signal(close):
    n=5
    b=(close - close.shift(n)).abs() / close.diff().abs().rolling(n,min_periods=n).sum().replace(0.0,np.nan)
    return b.diff(5).replace([np.inf,-np.inf],np.nan)

def f03ts_f03_trend_strength_metrics_kefr_80d_slope_v092_signal(closeadj):
    n=80
    b=(closeadj - closeadj.shift(n)).abs() / closeadj.diff().abs().rolling(n,min_periods=n).sum().replace(0.0,np.nan)
    return b.diff(21).replace([np.inf,-np.inf],np.nan)

def f03ts_f03_trend_strength_metrics_kerhi_50d_slope_v093_signal(high):
    n=50
    b=(high - high.shift(n)).abs() / high.diff().abs().rolling(n,min_periods=n).sum().replace(0.0,np.nan)
    return b.diff(21).replace([np.inf,-np.inf],np.nan)

def f03ts_f03_trend_strength_metrics_kerlo_50d_slope_v094_signal(high, low):
    n=50
    dh = (high - high.shift(n)).abs(); vh = high.diff().abs().rolling(n,min_periods=n).sum()
    erh = dh / vh.replace(0.0,np.nan)
    dl = (low - low.shift(n)).abs(); vl = low.diff().abs().rolling(n,min_periods=n).sum()
    erl = dl / vl.replace(0.0,np.nan)
    b=erh - erl
    return b.diff(10).replace([np.inf,-np.inf],np.nan)

def f03ts_f03_trend_strength_metrics_r2lin_40d_slope_v095_signal(closeadj):
    n=40
    def _r2(x):
        if not np.all(np.isfinite(x)):return np.nan
        t=np.arange(n,dtype=float); a=np.polyfit(t,x,1); yhat = a[0] * t + a[1]
        ss_res = float(np.sum((x - yhat) ** 2)); ss_tot = float(np.sum((x - x.mean()) ** 2))
        if ss_tot <= 0: return np.nan
        return 1.0 - ss_res / ss_tot
    b=closeadj.rolling(n,min_periods=n).apply(_r2, raw=True)
    return b.diff(21).replace([np.inf,-np.inf],np.nan)

def f03ts_f03_trend_strength_metrics_logregslp_30d_slope_v096_signal(closeadj):
    n=30
    def _slope(x):
        if np.any(~np.isfinite(x)) or np.any(x <= 0): return np.nan
        y = np.log(x); t = np.arange(n, dtype=float)
        return float(np.polyfit(t, y, 1)[0])
    b=closeadj.rolling(n,min_periods=n).apply(_slope, raw=True)
    return b.diff(10).replace([np.inf,-np.inf],np.nan)

def f03ts_f03_trend_strength_metrics_logregslp_180d_slope_v097_signal(closeadj):
    n=180
    def _slope(x):
        if np.any(~np.isfinite(x)) or np.any(x <= 0): return np.nan
        y = np.log(x); t = np.arange(n, dtype=float)
        return float(np.polyfit(t, y, 1)[0])
    b=closeadj.rolling(n,min_periods=n).apply(_slope, raw=True)
    return b.diff(63).replace([np.inf,-np.inf],np.nan)

def f03ts_f03_trend_strength_metrics_regresid_60d_slope_v098_signal(closeadj):
    n=60
    def _cv(x):
        if np.any(~np.isfinite(x)) or x.mean() == 0: return np.nan
        t=np.arange(n,dtype=float); a=np.polyfit(t,x,1); resid=x-(a[0]*t+a[1])
        return float(np.std(resid, ddof=1) / abs(x.mean()))
    b=closeadj.rolling(n,min_periods=n).apply(_cv, raw=True)
    return b.diff(21).replace([np.inf,-np.inf],np.nan)

def f03ts_f03_trend_strength_metrics_regrsnr_50d_slope_v099_signal(closeadj):
    n=50
    def _snr(x):
        if not np.all(np.isfinite(x)):return np.nan
        t=np.arange(n,dtype=float); a=np.polyfit(t,x,1); resid=x-(a[0]*t+a[1])
        s=float(np.std(resid, ddof=1))
        if s <= 0: return np.nan
        return float(a[0]) * n / s
    b=closeadj.rolling(n,min_periods=n).apply(_snr, raw=True)
    return b.diff(10).replace([np.inf,-np.inf],np.nan)

def f03ts_f03_trend_strength_metrics_polylin_40d_slope_v100_signal(closeadj):
    n=40
    def _lin(x):
        if not np.all(np.isfinite(x)):return np.nan
        t = np.arange(n, dtype=float) / n
        a = np.polyfit(t, x, 2)
        return float(a[1])
    b=closeadj.rolling(n,min_periods=n).apply(_lin, raw=True)
    return b.diff(21).replace([np.inf,-np.inf],np.nan)

def f03ts_f03_trend_strength_metrics_polyquad_120d_slope_v101_signal(closeadj):
    n=120
    def _quad(x):
        if not np.all(np.isfinite(x)):return np.nan
        t = np.arange(n, dtype=float) / n
        a = np.polyfit(t, x, 2)
        return float(a[0])
    b=closeadj.rolling(n,min_periods=n).apply(_quad, raw=True)
    return b.diff(63).replace([np.inf,-np.inf],np.nan)

def f03ts_f03_trend_strength_metrics_hurstrs_60d_slope_v102_signal(closeadj):
    n=60
    def _h(x):
        x=np.asarray(x,dtype=float)
        if not np.all(np.isfinite(x)):return np.nan
        r=np.diff(np.log(x))
        if r.size<8:return np.nan
        y=r-r.mean(); z=np.cumsum(y); R=z.max()-z.min(); S=r.std(ddof=1)
        if S<=0 or R<=0:return np.nan
        return float(np.log(R/S)/np.log(len(r)))
    b=closeadj.rolling(n,min_periods=n).apply(_h, raw=True)
    return b.diff(10).replace([np.inf,-np.inf],np.nan)

def f03ts_f03_trend_strength_metrics_varratio_q20_120d_slope_v103_signal(closeadj):
    n=120; q = 20
    r1=np.log(closeadj).diff(); rq=np.log(closeadj).diff(q)
    v1=r1.rolling(n,min_periods=n).var(ddof=1); vq=rq.rolling(n,min_periods=n).var(ddof=1)
    b=vq / (q * v1.replace(0.0,np.nan)) - 1.0
    return b.diff(21).replace([np.inf,-np.inf],np.nan)

def f03ts_f03_trend_strength_metrics_hurstdiff_120d_slope_v104_signal(closeadj):
    def _h(x):
        x=np.asarray(x,dtype=float)
        if not np.all(np.isfinite(x)):return np.nan
        r=np.diff(np.log(x))
        if r.size<8:return np.nan
        y=r-r.mean(); z=np.cumsum(y); R=z.max()-z.min(); S=r.std(ddof=1)
        if S<=0 or R<=0:return np.nan
        return float(np.log(R/S)/np.log(len(r)))
    h60 = closeadj.rolling(60,min_periods=60).apply(_h, raw=True)
    h120 = closeadj.rolling(120,min_periods=120).apply(_h, raw=True)
    b=h60 - h120
    return b.diff(63).replace([np.inf,-np.inf],np.nan)

def f03ts_f03_trend_strength_metrics_mk_15d_slope_v105_signal(close):
    n=15; norm=n*(n-1)/2.0
    def _mk(x):
        if not np.all(np.isfinite(x)):return np.nan
        s=0
        for i in range(n-1):
            d=x[i+1:]-x[i]; s+=int(np.sum(d>0)-np.sum(d<0))
        return s/norm
    b=close.rolling(n,min_periods=n).apply(_mk, raw=True)
    return b.diff(5).replace([np.inf,-np.inf],np.nan)

def f03ts_f03_trend_strength_metrics_mk_90d_slope_v106_signal(closeadj):
    n=90; norm=n*(n-1)/2.0
    def _mk(x):
        if not np.all(np.isfinite(x)):return np.nan
        s=0
        for i in range(n-1):
            d=x[i+1:]-x[i]; s+=int(np.sum(d>0)-np.sum(d<0))
        return s/norm
    b=closeadj.rolling(n,min_periods=n).apply(_mk, raw=True)
    return b.diff(63).replace([np.inf,-np.inf],np.nan)

def f03ts_f03_trend_strength_metrics_anymonotone_30d_slope_v107_signal(closeadj):
    n=30
    def _longest(x):
        x = np.asarray(x, dtype=float)
        if not np.all(np.isfinite(x)):return np.nan
        d=np.sign(np.diff(x))
        best = 1; cur = 1
        for i in range(1, len(d)):
            if d[i] == d[i - 1] and d[i] != 0:
                cur += 1
                if cur > best: best = cur
            else:
                cur = 1
        return float(best)
    b=closeadj.rolling(n,min_periods=n).apply(_longest, raw=True)
    return b.diff(10).replace([np.inf,-np.inf],np.nan)

def f03ts_f03_trend_strength_metrics_uprunlong_120d_slope_v108_signal(closeadj):
    n=120
    def _up(x):
        x = np.asarray(x, dtype=float)
        if not np.all(np.isfinite(x)):return np.nan
        d=np.sign(np.diff(x))
        best = 0; cur = 0
        for v in d:
            if v > 0:
                cur += 1
                if cur > best: best = cur
            else:
                cur = 0
        return float(best)
    b=closeadj.rolling(n,min_periods=n).apply(_up, raw=True)
    return b.diff(63).replace([np.inf,-np.inf],np.nan)

def f03ts_f03_trend_strength_metrics_dirsignmean_8d_slope_v109_signal(close):
    n=8
    b=np.sign(close.diff()).rolling(n,min_periods=n).mean()
    return b.diff(5).replace([np.inf,-np.inf],np.nan)

def f03ts_f03_trend_strength_metrics_acclbal_45d_slope_v110_signal(closeadj):
    n=45
    b=np.sign(closeadj.diff()).rolling(n,min_periods=n).sum()
    return b.diff(10).replace([np.inf,-np.inf],np.nan)

def f03ts_f03_trend_strength_metrics_sameside_60d_slope_v111_signal(closeadj):
    s=closeadj.rolling(20,min_periods=20).mean()
    rel = np.sign(closeadj - s)
    n=60
    def _longest_same(x):
        x = np.asarray(x, dtype=float)
        if not np.all(np.isfinite(x)):return np.nan
        best = 0; cur = 0; prev = 0
        for v in x:
            if v == prev and v != 0:
                cur += 1
            else:
                cur = 1
            if cur > best: best = cur
            prev = v
        return float(best)
    b=rel.rolling(n,min_periods=n).apply(_longest_same, raw=True)
    return b.diff(21).replace([np.inf,-np.inf],np.nan)

def f03ts_f03_trend_strength_metrics_efrmulti_30d_slope_v112_signal(closeadj):
    def _ksg(n):
        return np.sign((closeadj - closeadj.shift(n)) / (closeadj.diff().abs().rolling(n,min_periods=n).sum().replace(0.0,np.nan)))
    b=_ksg(10) + _ksg(20) + _ksg(40) + _ksg(80) + _ksg(160)
    return b.diff(10).replace([np.inf,-np.inf],np.nan)

def f03ts_f03_trend_strength_metrics_efragree_30d_slope_v113_signal(closeadj):
    s20 = np.sign(closeadj - closeadj.shift(20))
    s60 = np.sign(closeadj - closeadj.shift(60))
    s120 = np.sign(closeadj - closeadj.shift(120))
    agree=((s20 == s60).astype(float) + (s20 == s120).astype(float) + (s60 == s120).astype(float))
    mask=s20.isna() | s60.isna() | s120.isna()
    b=agree.where(~mask)
    return b.diff(10).replace([np.inf,-np.inf],np.nan)

def f03ts_f03_trend_strength_metrics_sigmoidker_25d_slope_v114_signal(closeadj):
    n=25
    raw=closeadj - closeadj.shift(n)
    v=closeadj.diff().abs().rolling(n,min_periods=n).sum()
    er=raw / v.replace(0.0,np.nan)
    b=1.0 / (1.0 + np.exp(-5.0 * er))
    return b.diff(10).replace([np.inf,-np.inf],np.nan)

def f03ts_f03_trend_strength_metrics_arctsi_30d_slope_v115_signal(closeadj):
    diff=closeadj.diff()
    num=diff.ewm(span=13, adjust=False,min_periods=13).mean().ewm(span=7, adjust=False,min_periods=7).mean()
    den=diff.abs().ewm(span=13, adjust=False,min_periods=13).mean().ewm(span=7, adjust=False,min_periods=7).mean()
    tsi=100.0 * num / den.replace(0.0,np.nan)
    flag=(tsi.abs() > 25.0).astype(float).where(~tsi.isna())
    b=flag.rolling(60,min_periods=60).mean()
    return b.diff(21).replace([np.inf,-np.inf],np.nan)

def f03ts_f03_trend_strength_metrics_pricedispr_40d_slope_v116_signal(closeadj):
    n=40
    r=np.log(closeadj).diff()
    mu=r.rolling(n,min_periods=n).mean(); sd = r.rolling(n,min_periods=n).std(ddof=1)
    b=sd / mu.abs().replace(0.0,np.nan)
    return b.diff(10).replace([np.inf,-np.inf],np.nan)

def f03ts_f03_trend_strength_metrics_pricesnr_60d_slope_v117_signal(closeadj):
    n=60
    r=np.log(closeadj).diff()
    mu=r.rolling(n,min_periods=n).mean(); sd = r.rolling(n,min_periods=n).std(ddof=1)
    b=mu.abs() * np.sqrt(n) / sd.replace(0.0,np.nan)
    return b.diff(21).replace([np.inf,-np.inf],np.nan)

def f03ts_f03_trend_strength_metrics_rangertr_50d_slope_v118_signal(high, low, closeadj):
    n=50
    hh=high.rolling(n,min_periods=n).max(); ll=low.rolling(n,min_periods=n).min()
    tr_sum = _tr(high, low, closeadj).rolling(n,min_periods=n).sum()
    b=(hh - ll) / tr_sum.replace(0.0,np.nan)
    return b.diff(21).replace([np.inf,-np.inf],np.nan)

def f03ts_f03_trend_strength_metrics_bullbarpct_40d_slope_v119_signal(close, open_):
    flag=(close > open_).astype(float).where(~close.isna() & ~open_.isna())
    b=flag.rolling(40,min_periods=40).mean()
    return b.diff(10).replace([np.inf,-np.inf],np.nan)

def f03ts_f03_trend_strength_metrics_directnbody_30d_slope_v120_signal(close, open_):
    body=close - open_
    s=body.rolling(30,min_periods=30).sum(); a = body.abs().rolling(30,min_periods=30).sum()
    b=s / a.replace(0.0,np.nan)
    return b.diff(21).replace([np.inf,-np.inf],np.nan)

def f03ts_f03_trend_strength_metrics_hhseq_30d_slope_v121_signal(high):
    cond=(high > high.shift(1).rolling(5,min_periods=5).max()).astype(float).where(~high.isna())
    b=cond.rolling(30,min_periods=30).sum()
    return b.diff(10).replace([np.inf,-np.inf],np.nan)

def f03ts_f03_trend_strength_metrics_llseq_60d_slope_v122_signal(low):
    cond=(low < low.shift(1).rolling(10,min_periods=10).min()).astype(float).where(~low.isna())
    b=cond.rolling(60,min_periods=60).sum()
    return b.diff(21).replace([np.inf,-np.inf],np.nan)

def f03ts_f03_trend_strength_metrics_atrtrend_30d_slope_v123_signal(high, low, closeadj):
    n=30
    move=closeadj - closeadj.shift(n)
    tr_sum = _tr(high, low, closeadj).rolling(n,min_periods=n).sum()
    raw=move / tr_sum.replace(0.0,np.nan)
    b=np.tanh(3.0 * raw)
    return b.diff(10).replace([np.inf,-np.inf],np.nan)

def f03ts_f03_trend_strength_metrics_atrtrendlong_120d_slope_v124_signal(high, low, closeadj):
    n=120
    move=closeadj - closeadj.shift(n)
    tr_sum = _tr(high, low, closeadj).rolling(n,min_periods=n).sum()
    b=move / tr_sum.replace(0.0,np.nan)
    return b.diff(63).replace([np.inf,-np.inf],np.nan)

def f03ts_f03_trend_strength_metrics_daysflip_60d_slope_v125_signal(closeadj):
    s=closeadj.rolling(20,min_periods=20).mean()
    sign = np.sign(closeadj - s)
    flip=(sign != sign.shift(1)).astype(float).where(~sign.isna() & ~sign.shift(1).isna())
    def _ds(x):
        idx = np.where(x > 0.5)[0]
        if idx.size == 0: return 60.0
        return float(len(x) - 1 - idx[-1])
    b=flip.rolling(60,min_periods=60).apply(_ds, raw=True)
    return b.diff(21).replace([np.inf,-np.inf],np.nan)

def f03ts_f03_trend_strength_metrics_daysadxhi_120d_slope_v126_signal(high, low, closeadj):
    n=14
    atr=_wilder(_tr(high,low,closeadj),n)
    pdi=100.0*_wilder(_plus_dm(high,low),n)/atr.replace(0.0,np.nan); mdi=100.0*_wilder(_minus_dm(high,low),n)/atr.replace(0.0,np.nan)
    dx=100.0*(pdi-mdi).abs()/(pdi+mdi).replace(0.0,np.nan)
    adx=_wilder(dx,n)
    cond=(adx > 40.0).astype(float).where(~adx.isna())
    def _ds(x):
        idx = np.where(x > 0.5)[0]
        if idx.size == 0: return 120.0
        return float(len(x) - 1 - idx[-1])
    b=cond.rolling(120,min_periods=120).apply(_ds, raw=True)
    return b.diff(63).replace([np.inf,-np.inf],np.nan)

def f03ts_f03_trend_strength_metrics_chopcurv_40d_slope_v127_signal(high, low, closeadj):
    n=20
    tr_n=_tr(high,low,closeadj).rolling(n,min_periods=n).sum()
    hh=high.rolling(n,min_periods=n).max(); ll=low.rolling(n,min_periods=n).min()
    nchop = -100.0 * np.log10(tr_n / (hh - ll).replace(0.0,np.nan)) / np.log10(n)
    b=nchop - 2.0 * nchop.shift(10) + nchop.shift(20)
    return b.diff(10).replace([np.inf,-np.inf],np.nan)

def f03ts_f03_trend_strength_metrics_kerrank_100d_slope_v128_signal(closeadj):
    n=30
    d=(closeadj - closeadj.shift(n)).abs(); v = closeadj.diff().abs().rolling(n,min_periods=n).sum()
    er=d / v.replace(0.0,np.nan)
    b=er.rolling(100,min_periods=100).rank(pct=True)
    return b.diff(63).replace([np.inf,-np.inf],np.nan)

def f03ts_f03_trend_strength_metrics_tsi_rank_120d_slope_v129_signal(closeadj):
    diff=closeadj.diff()
    num=diff.ewm(span=25, adjust=False,min_periods=25).mean().ewm(span=13, adjust=False,min_periods=13).mean()
    den=diff.abs().ewm(span=25, adjust=False,min_periods=25).mean().ewm(span=13, adjust=False,min_periods=13).mean()
    tsi=100.0 * num / den.replace(0.0,np.nan)
    b=tsi.rolling(120,min_periods=120).rank(pct=True)
    return b.diff(63).replace([np.inf,-np.inf],np.nan)

def f03ts_f03_trend_strength_metrics_aroonrank_120d_slope_v130_signal(closeadj):
    n=25
    au=closeadj.rolling(n+1,min_periods=n+1).apply(lambda x:100.0*(n-(n-int(np.argmax(x))))/n,raw=True)
    ad=closeadj.rolling(n+1,min_periods=n+1).apply(lambda x:100.0*(n-(n-int(np.argmin(x))))/n,raw=True)
    osc=au - ad
    b=osc.rolling(120,min_periods=120).rank(pct=True)
    return b.diff(63).replace([np.inf,-np.inf],np.nan)

def f03ts_f03_trend_strength_metrics_distargmax_30d_slope_v131_signal(closeadj):
    n=30
    b=closeadj.rolling(n,min_periods=n).apply(lambda x: float(len(x) - 1 - int(np.argmax(x))), raw=True)
    return b.diff(10).replace([np.inf,-np.inf],np.nan)

def f03ts_f03_trend_strength_metrics_distargmin_60d_slope_v132_signal(closeadj):
    n=60
    b=closeadj.rolling(n,min_periods=n).apply(lambda x: float(len(x) - 1 - int(np.argmin(x))), raw=True)
    return b.diff(21).replace([np.inf,-np.inf],np.nan)

def f03ts_f03_trend_strength_metrics_kstsig_30d_slope_v133_signal(closeadj):
    r1 = closeadj.pct_change(10).rolling(10,min_periods=10).mean()
    r2 = closeadj.pct_change(15).rolling(10,min_periods=10).mean()
    r3 = closeadj.pct_change(20).rolling(10,min_periods=10).mean()
    r4 = closeadj.pct_change(30).rolling(15,min_periods=15).mean()
    kst = 1.0 * r1 + 2.0 * r2 + 3.0 * r3 + 4.0 * r4
    sig=kst.rolling(9,min_periods=9).mean()
    b=kst - sig
    return b.diff(10).replace([np.inf,-np.inf],np.nan)

def f03ts_f03_trend_strength_metrics_kstsign_30d_slope_v134_signal(closeadj):
    r1 = closeadj.pct_change(10).rolling(10,min_periods=10).mean()
    r2 = closeadj.pct_change(15).rolling(10,min_periods=10).mean()
    r3 = closeadj.pct_change(20).rolling(10,min_periods=10).mean()
    r4 = closeadj.pct_change(30).rolling(15,min_periods=15).mean()
    kst = 1.0 * r1 + 2.0 * r2 + 3.0 * r3 + 4.0 * r4
    b=np.sign(kst)
    return b.diff(21).replace([np.inf,-np.inf],np.nan)

def f03ts_f03_trend_strength_metrics_stochmom_30d_slope_v135_signal(closeadj):
    n=30
    y = np.log(closeadj)
    hh = y.rolling(n,min_periods=n).max(); ll = y.rolling(n,min_periods=n).min()
    b=(y - ll) / (hh - ll).replace(0.0,np.nan)
    return b.diff(21).replace([np.inf,-np.inf],np.nan)

def f03ts_f03_trend_strength_metrics_atrdrift_50d_slope_v136_signal(high, low, closeadj):
    tr = _tr(high, low, closeadj); atr = _wilder(tr, 14)
    n=50
    def _slope(x):
        if np.any(~np.isfinite(x)) or np.any(x <= 0): return np.nan
        y = np.log(x); t = np.arange(n, dtype=float)
        return float(np.polyfit(t, y, 1)[0])
    b=atr.rolling(n,min_periods=n).apply(_slope, raw=True)
    return b.diff(21).replace([np.inf,-np.inf],np.nan)

def f03ts_f03_trend_strength_metrics_mkmulti_60d_slope_v139_signal(closeadj):
    def _mk(n):
        norm = n * (n - 1) / 2.0
        def _f(x):
            if not np.all(np.isfinite(x)):return np.nan
            s=0
            for i in range(n - 1):
                d=x[i + 1:] - x[i]
                s += int(np.sum(d > 0) - np.sum(d < 0))
            return s / norm
        return closeadj.rolling(n,min_periods=n).apply(_f, raw=True)
    m20 = _mk(20); m40 = _mk(40); m60 = _mk(60); m80 = _mk(80)
    pos = (m20 > 0).astype(float) + (m40 > 0).astype(float) + (m60 > 0).astype(float) + (m80 > 0).astype(float)
    mask=m20.isna() | m40.isna() | m60.isna() | m80.isna()
    b=pos.where(~mask)
    return b.diff(21).replace([np.inf,-np.inf],np.nan)

def f03ts_f03_trend_strength_metrics_r2multi_80d_slope_v140_signal(closeadj):
    def _r2(n):
        def _f(x):
            if not np.all(np.isfinite(x)):return np.nan
            t = np.arange(n, dtype=float)
            a = np.polyfit(t, x, 1); yhat = a[0] * t + a[1]
            ss_res = float(np.sum((x - yhat) ** 2)); ss_tot = float(np.sum((x - x.mean()) ** 2))
            if ss_tot <= 0: return np.nan
            return 1.0 - ss_res / ss_tot
        return closeadj.rolling(n,min_periods=n).apply(_f, raw=True)
    b=(_r2(20) + _r2(40) + _r2(80)) / 3.0
    return b.diff(21).replace([np.inf,-np.inf],np.nan)

def f03ts_f03_trend_strength_metrics_kerfracmid_40d_slope_v141_signal(closeadj):
    n=20
    d=(closeadj - closeadj.shift(n)).abs(); v = closeadj.diff().abs().rolling(n,min_periods=n).sum()
    er=d / v.replace(0.0,np.nan)
    flag=(er > 0.5).astype(float).where(~er.isna())
    b=flag.rolling(40,min_periods=40).mean()
    return b.diff(10).replace([np.inf,-np.inf],np.nan)

def f03ts_f03_trend_strength_metrics_chopreg_80d_slope_v142_signal(high, low, closeadj):
    n=14
    tr_n=_tr(high,low,closeadj).rolling(n,min_periods=n).sum()
    hh=high.rolling(n,min_periods=n).max(); ll=low.rolling(n,min_periods=n).min()
    chop = 100.0 * np.log10(tr_n / (hh - ll).replace(0.0,np.nan)) / np.log10(n)
    flag=(chop > 61.8).astype(float).where(~chop.isna())
    b=flag.rolling(80,min_periods=80).mean()
    return b.diff(21).replace([np.inf,-np.inf],np.nan)

def f03ts_f03_trend_strength_metrics_hlmidslope_30d_slope_v143_signal(high, low):
    n=30
    mid=0.5 * (high + low)
    sma = mid.rolling(n,min_periods=n).mean()
    b=sma.diff(5) / sma.replace(0.0,np.nan)
    return b.diff(10).replace([np.inf,-np.inf],np.nan)

def f03ts_f03_trend_strength_metrics_typmompow_25d_slope_v144_signal(high, low, close):
    n=25
    typ=(high + low + close) / 3.0
    d=(typ - typ.shift(n)).abs(); v = typ.diff().abs().rolling(n,min_periods=n).sum()
    b=(d / v.replace(0.0,np.nan)) ** 2
    return b.diff(5).replace([np.inf,-np.inf],np.nan)

def f03ts_f03_trend_strength_metrics_vrdiff_120d_slope_v145_signal(closeadj):
    n=120
    r1 = np.log(closeadj).diff()
    v1 = r1.rolling(n,min_periods=n).var(ddof=1)
    vq2 = np.log(closeadj).diff(2).rolling(n,min_periods=n).var(ddof=1)
    vq10 = np.log(closeadj).diff(10).rolling(n,min_periods=n).var(ddof=1)
    b=(vq2 / (2 * v1.replace(0.0,np.nan))) - (vq10 / (10 * v1.replace(0.0,np.nan)))
    return b.diff(63).replace([np.inf,-np.inf],np.nan)

def f03ts_f03_trend_strength_metrics_robslp_25d_slope_v146_signal(closeadj):
    n=25
    def _ts(x):
        if not np.all(np.isfinite(x)):return np.nan
        slopes = []
        for i in range(n - 1):
            slopes.append((x[-1] - x[i]) / (n - 1 - i + 1e-9))
        return float(np.median(slopes))
    b=closeadj.rolling(n,min_periods=n).apply(_ts, raw=True)
    return b.diff(10).replace([np.inf,-np.inf],np.nan)

def f03ts_f03_trend_strength_metrics_plusminusratio_30d_slope_v147_signal(high, low):
    pdm = _plus_dm(high, low).rolling(20,min_periods=20).mean()
    mdm = _minus_dm(high, low).rolling(20,min_periods=20).mean()
    b=(pdm - mdm) / (pdm + mdm).replace(0.0,np.nan)
    return b.diff(10).replace([np.inf,-np.inf],np.nan)

def f03ts_f03_trend_strength_metrics_signz_50d_slope_v148_signal(closeadj):
    n=50
    s=np.sign(closeadj.diff()).rolling(n,min_periods=n).sum() / n
    sd=s.rolling(100,min_periods=100).std(ddof=1)
    b=s / sd.replace(0.0,np.nan)
    return b.diff(21).replace([np.inf,-np.inf],np.nan)

def f03ts_f03_trend_strength_metrics_trrng_30d_slope_v149_signal(high, low, closeadj):
    n=30
    move=(closeadj - closeadj.shift(n)).abs()
    rng=high.rolling(n,min_periods=n).max() - low.rolling(n,min_periods=n).min()
    b=np.log((move + 1e-12) / rng.replace(0.0,np.nan))
    return b.diff(21).replace([np.inf,-np.inf],np.nan)

def f03ts_f03_trend_strength_metrics_efqctile_50d_slope_v150_signal(closeadj):
    n=50
    d=(closeadj - closeadj.shift(n)).abs(); v = closeadj.diff().abs().rolling(n,min_periods=n).sum()
    er=d / v.replace(0.0,np.nan)
    med=er.rolling(50,min_periods=50).median()
    b=er - med
    return b.diff(21).replace([np.inf,-np.inf],np.nan)


def _e(fn, *inputs):
    return fn.__name__, {"inputs": list(inputs), "func": fn}


f03_trend_strength_metrics_slope_001_150_REGISTRY = dict([
_e(f03ts_f03_trend_strength_metrics_adx_50d_slope_v002_signal,"high","low","closeadj"),
_e(f03ts_f03_trend_strength_metrics_dmidiff_21d_slope_v003_signal,"high","low","close"),
_e(f03ts_f03_trend_strength_metrics_dmiratio_30d_slope_v004_signal,"high","low","closeadj"),
_e(f03ts_f03_trend_strength_metrics_adxstrong_60d_slope_v005_signal,"high","low","closeadj"),
_e(f03ts_f03_trend_strength_metrics_pdi_14d_slope_v006_signal,"high","low","close"),
_e(f03ts_f03_trend_strength_metrics_mdi_40d_slope_v007_signal,"high","low","closeadj"),
_e(f03ts_f03_trend_strength_metrics_aroonosc_14d_slope_v008_signal,"close"),
_e(f03ts_f03_trend_strength_metrics_aroonosc_50d_slope_v009_signal,"closeadj"),
_e(f03ts_f03_trend_strength_metrics_aroondiff_25d_slope_v010_signal,"high","low"),
_e(f03ts_f03_trend_strength_metrics_aroonsign_30d_slope_v011_signal,"closeadj"),
_e(f03ts_f03_trend_strength_metrics_aroonconv_21d_slope_v012_signal,"close"),
_e(f03ts_f03_trend_strength_metrics_vortexdiff_14d_slope_v013_signal,"high","low","close"),
_e(f03ts_f03_trend_strength_metrics_vortexabs_30d_slope_v014_signal,"high","low","closeadj"),
_e(f03ts_f03_trend_strength_metrics_vortexratio_60d_slope_v015_signal,"high","low","closeadj"),
_e(f03ts_f03_trend_strength_metrics_chop_14d_slope_v016_signal,"high","low","close"),
_e(f03ts_f03_trend_strength_metrics_chop_40d_slope_v017_signal,"high","low","closeadj"),
_e(f03ts_f03_trend_strength_metrics_choprank_120d_slope_v018_signal,"high","low","closeadj"),
_e(f03ts_f03_trend_strength_metrics_tsi_25_13_slope_v019_signal,"close"),
_e(f03ts_f03_trend_strength_metrics_tsi_50_25_slope_v020_signal,"closeadj"),
_e(f03ts_f03_trend_strength_metrics_tsiabs_25_13_slope_v021_signal,"close"),
_e(f03ts_f03_trend_strength_metrics_kst_30d_slope_v022_signal,"closeadj"),
_e(f03ts_f03_trend_strength_metrics_kstlong_120d_slope_v023_signal,"closeadj"),
_e(f03ts_f03_trend_strength_metrics_kefr_10d_slope_v024_signal,"close"),
_e(f03ts_f03_trend_strength_metrics_kefr_40d_slope_v025_signal,"closeadj"),
_e(f03ts_f03_trend_strength_metrics_kefr_120d_slope_v026_signal,"closeadj"),
_e(f03ts_f03_trend_strength_metrics_kefrsigned_30d_slope_v027_signal,"closeadj"),
_e(f03ts_f03_trend_strength_metrics_kefrhl_25d_slope_v028_signal,"high","low"),
_e(f03ts_f03_trend_strength_metrics_r2lin_20d_slope_v029_signal,"close"),
_e(f03ts_f03_trend_strength_metrics_r2lin_63d_slope_v030_signal,"closeadj"),
_e(f03ts_f03_trend_strength_metrics_r2log_120d_slope_v031_signal,"closeadj"),
_e(f03ts_f03_trend_strength_metrics_logregslp_60d_slope_v032_signal,"closeadj"),
_e(f03ts_f03_trend_strength_metrics_regrres_30d_slope_v033_signal,"closeadj"),
_e(f03ts_f03_trend_strength_metrics_robtrend_40d_slope_v034_signal,"closeadj"),
_e(f03ts_f03_trend_strength_metrics_poly2coef_50d_slope_v035_signal,"closeadj"),
_e(f03ts_f03_trend_strength_metrics_lastresid_30d_slope_v036_signal,"closeadj"),
_e(f03ts_f03_trend_strength_metrics_hurstrs_80d_slope_v037_signal,"closeadj"),
_e(f03ts_f03_trend_strength_metrics_hurstrs_160d_slope_v038_signal,"closeadj"),
_e(f03ts_f03_trend_strength_metrics_varratio_30d_slope_v039_signal,"closeadj"),
_e(f03ts_f03_trend_strength_metrics_varratio_100d_slope_v040_signal,"closeadj"),
_e(f03ts_f03_trend_strength_metrics_mks_30d_slope_v041_signal,"closeadj"),
_e(f03ts_f03_trend_strength_metrics_mksabs_60d_slope_v042_signal,"closeadj"),
_e(f03ts_f03_trend_strength_metrics_uprun_20d_slope_v043_signal,"close"),
_e(f03ts_f03_trend_strength_metrics_dnrun_60d_slope_v044_signal,"closeadj"),
_e(f03ts_f03_trend_strength_metrics_signfrac_40d_slope_v045_signal,"closeadj"),
_e(f03ts_f03_trend_strength_metrics_upfrac_15d_slope_v046_signal,"close"),
_e(f03ts_f03_trend_strength_metrics_dirpersist_50d_slope_v047_signal,"closeadj"),
_e(f03ts_f03_trend_strength_metrics_smaplusdm_20d_slope_v048_signal,"high","low"),
_e(f03ts_f03_trend_strength_metrics_smaminusdm_60d_slope_v049_signal,"high","low"),
_e(f03ts_f03_trend_strength_metrics_dmrank_120d_slope_v050_signal,"high","low"),
_e(f03ts_f03_trend_strength_metrics_adxregime_14d_slope_v051_signal,"high","low","close"),
_e(f03ts_f03_trend_strength_metrics_adxhigh_50d_slope_v052_signal,"high","low","closeadj"),
_e(f03ts_f03_trend_strength_metrics_bullbearcnt_30d_slope_v053_signal,"closeadj"),
_e(f03ts_f03_trend_strength_metrics_aroonstrong_50d_slope_v054_signal,"closeadj"),
_e(f03ts_f03_trend_strength_metrics_adxdiff_30d_slope_v055_signal,"high","low","closeadj"),
_e(f03ts_f03_trend_strength_metrics_kerdiff_30d_slope_v056_signal,"closeadj"),
_e(f03ts_f03_trend_strength_metrics_tsidiff_30d_slope_v057_signal,"closeadj"),
_e(f03ts_f03_trend_strength_metrics_tanhker_30d_slope_v058_signal,"closeadj"),
_e(f03ts_f03_trend_strength_metrics_arctanmk_40d_slope_v059_signal,"closeadj"),
_e(f03ts_f03_trend_strength_metrics_adxslope_30d_slope_v060_signal,"high","low","closeadj"),
_e(f03ts_f03_trend_strength_metrics_adxcurv_40d_slope_v061_signal,"high","low","closeadj"),
_e(f03ts_f03_trend_strength_metrics_corrtrend_25d_slope_v062_signal,"close"),
_e(f03ts_f03_trend_strength_metrics_corrtrend_120d_slope_v063_signal,"closeadj"),
_e(f03ts_f03_trend_strength_metrics_signdiff_30d_slope_v064_signal,"closeadj"),
_e(f03ts_f03_trend_strength_metrics_signagree_25d_slope_v065_signal,"close"),
_e(f03ts_f03_trend_strength_metrics_acfr1_60d_slope_v066_signal,"closeadj"),
_e(f03ts_f03_trend_strength_metrics_dmi_xover_30d_slope_v067_signal,"high","low","closeadj"),
_e(f03ts_f03_trend_strength_metrics_tdays_dmihigh_60d_slope_v068_signal,"high","low","closeadj"),
_e(f03ts_f03_trend_strength_metrics_tslowstr_30d_slope_v069_signal,"high","low","closeadj"),
_e(f03ts_f03_trend_strength_metrics_chopslope_30d_slope_v070_signal,"high","low","closeadj"),
_e(f03ts_f03_trend_strength_metrics_aroonslope_30d_slope_v071_signal,"closeadj"),
_e(f03ts_f03_trend_strength_metrics_vortexslope_30d_slope_v072_signal,"high","low","closeadj"),
_e(f03ts_f03_trend_strength_metrics_persistz_60d_slope_v073_signal,"closeadj"),
_e(f03ts_f03_trend_strength_metrics_efrhl_50d_slope_v074_signal,"high","low"),
_e(f03ts_f03_trend_strength_metrics_efrkam_15d_slope_v075_signal,"close"),
_e(f03ts_f03_trend_strength_metrics_adx_8d_slope_v076_signal,"high","low","close"),
_e(f03ts_f03_trend_strength_metrics_adxrank_120d_slope_v077_signal,"high","low","closeadj"),
_e(f03ts_f03_trend_strength_metrics_pdimrnk_60d_slope_v078_signal,"high","low","closeadj"),
_e(f03ts_f03_trend_strength_metrics_dxraw_14d_slope_v079_signal,"high","low","close"),
_e(f03ts_f03_trend_strength_metrics_adxz_60d_slope_v080_signal,"high","low","closeadj"),
_e(f03ts_f03_trend_strength_metrics_aroonup_18d_slope_v081_signal,"close"),
_e(f03ts_f03_trend_strength_metrics_aroondn_40d_slope_v082_signal,"closeadj"),
_e(f03ts_f03_trend_strength_metrics_aroonlog_25d_slope_v083_signal,"closeadj"),
_e(f03ts_f03_trend_strength_metrics_viplus_21d_slope_v084_signal,"high","low","close"),
_e(f03ts_f03_trend_strength_metrics_viminus_40d_slope_v085_signal,"high","low","closeadj"),
_e(f03ts_f03_trend_strength_metrics_visum_50d_slope_v086_signal,"high","low","closeadj"),
_e(f03ts_f03_trend_strength_metrics_chop_28d_slope_v087_signal,"high","low","closeadj"),
_e(f03ts_f03_trend_strength_metrics_chopdiff_30d_slope_v088_signal,"high","low","closeadj"),
_e(f03ts_f03_trend_strength_metrics_tsi_13_7_slope_v089_signal,"close"),
_e(f03ts_f03_trend_strength_metrics_tsihigh_25_13_slope_v090_signal,"high"),
_e(f03ts_f03_trend_strength_metrics_kefr_5d_slope_v091_signal,"close"),
_e(f03ts_f03_trend_strength_metrics_kefr_80d_slope_v092_signal,"closeadj"),
_e(f03ts_f03_trend_strength_metrics_kerhi_50d_slope_v093_signal,"high"),
_e(f03ts_f03_trend_strength_metrics_kerlo_50d_slope_v094_signal,"high","low"),
_e(f03ts_f03_trend_strength_metrics_r2lin_40d_slope_v095_signal,"closeadj"),
_e(f03ts_f03_trend_strength_metrics_logregslp_30d_slope_v096_signal,"closeadj"),
_e(f03ts_f03_trend_strength_metrics_logregslp_180d_slope_v097_signal,"closeadj"),
_e(f03ts_f03_trend_strength_metrics_regresid_60d_slope_v098_signal,"closeadj"),
_e(f03ts_f03_trend_strength_metrics_regrsnr_50d_slope_v099_signal,"closeadj"),
_e(f03ts_f03_trend_strength_metrics_polylin_40d_slope_v100_signal,"closeadj"),
_e(f03ts_f03_trend_strength_metrics_polyquad_120d_slope_v101_signal,"closeadj"),
_e(f03ts_f03_trend_strength_metrics_hurstrs_60d_slope_v102_signal,"closeadj"),
_e(f03ts_f03_trend_strength_metrics_varratio_q20_120d_slope_v103_signal,"closeadj"),
_e(f03ts_f03_trend_strength_metrics_hurstdiff_120d_slope_v104_signal,"closeadj"),
_e(f03ts_f03_trend_strength_metrics_mk_15d_slope_v105_signal,"close"),
_e(f03ts_f03_trend_strength_metrics_mk_90d_slope_v106_signal,"closeadj"),
_e(f03ts_f03_trend_strength_metrics_anymonotone_30d_slope_v107_signal,"closeadj"),
_e(f03ts_f03_trend_strength_metrics_uprunlong_120d_slope_v108_signal,"closeadj"),
_e(f03ts_f03_trend_strength_metrics_dirsignmean_8d_slope_v109_signal,"close"),
_e(f03ts_f03_trend_strength_metrics_acclbal_45d_slope_v110_signal,"closeadj"),
_e(f03ts_f03_trend_strength_metrics_sameside_60d_slope_v111_signal,"closeadj"),
_e(f03ts_f03_trend_strength_metrics_efrmulti_30d_slope_v112_signal,"closeadj"),
_e(f03ts_f03_trend_strength_metrics_efragree_30d_slope_v113_signal,"closeadj"),
_e(f03ts_f03_trend_strength_metrics_sigmoidker_25d_slope_v114_signal,"closeadj"),
_e(f03ts_f03_trend_strength_metrics_arctsi_30d_slope_v115_signal,"closeadj"),
_e(f03ts_f03_trend_strength_metrics_pricedispr_40d_slope_v116_signal,"closeadj"),
_e(f03ts_f03_trend_strength_metrics_pricesnr_60d_slope_v117_signal,"closeadj"),
_e(f03ts_f03_trend_strength_metrics_rangertr_50d_slope_v118_signal,"high","low","closeadj"),
_e(f03ts_f03_trend_strength_metrics_bullbarpct_40d_slope_v119_signal,"close","open"),
_e(f03ts_f03_trend_strength_metrics_directnbody_30d_slope_v120_signal,"close","open"),
_e(f03ts_f03_trend_strength_metrics_hhseq_30d_slope_v121_signal,"high"),
_e(f03ts_f03_trend_strength_metrics_llseq_60d_slope_v122_signal,"low"),
_e(f03ts_f03_trend_strength_metrics_atrtrend_30d_slope_v123_signal,"high","low","closeadj"),
_e(f03ts_f03_trend_strength_metrics_atrtrendlong_120d_slope_v124_signal,"high","low","closeadj"),
_e(f03ts_f03_trend_strength_metrics_daysflip_60d_slope_v125_signal,"closeadj"),
_e(f03ts_f03_trend_strength_metrics_daysadxhi_120d_slope_v126_signal,"high","low","closeadj"),
_e(f03ts_f03_trend_strength_metrics_chopcurv_40d_slope_v127_signal,"high","low","closeadj"),
_e(f03ts_f03_trend_strength_metrics_kerrank_100d_slope_v128_signal,"closeadj"),
_e(f03ts_f03_trend_strength_metrics_tsi_rank_120d_slope_v129_signal,"closeadj"),
_e(f03ts_f03_trend_strength_metrics_aroonrank_120d_slope_v130_signal,"closeadj"),
_e(f03ts_f03_trend_strength_metrics_distargmax_30d_slope_v131_signal,"closeadj"),
_e(f03ts_f03_trend_strength_metrics_distargmin_60d_slope_v132_signal,"closeadj"),
_e(f03ts_f03_trend_strength_metrics_kstsig_30d_slope_v133_signal,"closeadj"),
_e(f03ts_f03_trend_strength_metrics_kstsign_30d_slope_v134_signal,"closeadj"),
_e(f03ts_f03_trend_strength_metrics_stochmom_30d_slope_v135_signal,"closeadj"),
_e(f03ts_f03_trend_strength_metrics_atrdrift_50d_slope_v136_signal,"high","low","closeadj"),
_e(f03ts_f03_trend_strength_metrics_mkmulti_60d_slope_v139_signal,"closeadj"),
_e(f03ts_f03_trend_strength_metrics_r2multi_80d_slope_v140_signal,"closeadj"),
_e(f03ts_f03_trend_strength_metrics_kerfracmid_40d_slope_v141_signal,"closeadj"),
_e(f03ts_f03_trend_strength_metrics_chopreg_80d_slope_v142_signal,"high","low","closeadj"),
_e(f03ts_f03_trend_strength_metrics_hlmidslope_30d_slope_v143_signal,"high","low"),
_e(f03ts_f03_trend_strength_metrics_typmompow_25d_slope_v144_signal,"high","low","close"),
_e(f03ts_f03_trend_strength_metrics_vrdiff_120d_slope_v145_signal,"closeadj"),
_e(f03ts_f03_trend_strength_metrics_robslp_25d_slope_v146_signal,"closeadj"),
_e(f03ts_f03_trend_strength_metrics_plusminusratio_30d_slope_v147_signal,"high","low"),
_e(f03ts_f03_trend_strength_metrics_signz_50d_slope_v148_signal,"closeadj"),
_e(f03ts_f03_trend_strength_metrics_trrng_30d_slope_v149_signal,"high","low","closeadj"),
_e(f03ts_f03_trend_strength_metrics_efqctile_50d_slope_v150_signal,"closeadj"),
])


def _synthetic_inputs(n=800,seed=42):
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
    for name,entry in f03_trend_strength_metrics_slope_001_150_REGISTRY.items():
        out=entry["func"](*[df[c] for c in entry["inputs"]])
        assert isinstance(out,pd.Series); assert len(out)==len(df)
        clean=out.dropna(); assert len(clean)>0
        assert float(clean.std())>0.0 or clean.nunique()>1
        results[name]=out
    warm=252
    frac=sum(1 for s in results.values() if s.iloc[warm:].isna().mean()<0.5)/len(results)
    assert frac>=0.80
    A=pd.concat({n:results[n] for n in results},axis=1).iloc[warm:].replace([np.inf,-np.inf],np.nan)
    C=A.corr(min_periods=50).abs(); np.fill_diagonal(C.values,0.0)
    mc=float(C.max().max())
    assert mc<=0.95+1e-9,f"max pairwise |corr|={mc:.4f} exceeds 0.95"
    print(f"OK slope_001_150: {len(results)} features, max |corr|={mc:.4f}, coverage_ok={frac:.2%}")


if __name__ == "__main__":
    _self_test()
