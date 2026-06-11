"""jerk 001-150."""
import numpy as np
import pandas as pd
def _sma(s,n): return s.rolling(n,n).mean()
def _ema(s,n): return s.ewm(span=n,adjust=False,min_periods=n).mean()
def _wma(s,n):
    w=np.arange(1,n+1,dtype=float); w/=w.sum()
    return s.rolling(n,n).apply(lambda x:float(np.dot(x,w)),raw=True)
def _hma(s,n):
    half=max(2,n//2); sqn=max(2,int(np.sqrt(n)))
    return _wma(2.0*_wma(s,half)-_wma(s,n),sqn)
def _dema(s,n):
    e1=_ema(s,n); return 2.0*e1-_ema(e1,n)
def _tema(s,n):
    e1=_ema(s,n); e2=_ema(e1,n); return 3.0*e1-3.0*e2+_ema(e2,n)
def _zlema(s,n): return _ema(s+(s-s.shift(max(1,(n-1)//2))),n)
def _kama(s,n,fast=2,slow=30):
    direction=(s-s.shift(n)).abs()
    volatility=s.diff().abs().rolling(n,n).sum()
    er=direction/volatility.replace(0.0,np.nan)
    sc=(er*(2.0/(fast+1)-2.0/(slow+1))+2.0/(slow+1))**2
    out=pd.Series(np.nan,index=s.index,dtype=float)
    prev=np.nan; sv=s.values; scv=sc.values
    for i in range(len(s)):
        if i<n or not np.isfinite(scv[i]) or not np.isfinite(sv[i]):
            continue
        if not np.isfinite(prev):
            prev=sv[i]
        else:
            prev=prev+scv[i]*(sv[i]-prev)
        out.iat[i]=prev
    return out
def _alma(s,n,offset=0.85,sigma=6.0):
    m=offset*(n-1); sig=n/sigma
    w=np.exp(-((np.arange(n)-m)**2)/(2.0*sig*sig)); w/=w.sum()
    return s.rolling(n,n).apply(lambda x:float(np.dot(x,w)),raw=True)
def _mcginley(s,n):
    out=pd.Series(np.nan,index=s.index,dtype=float)
    prev=np.nan; sv=s.values
    seed_i=None
    for i in range(len(s)):
        if not np.isfinite(sv[i]):
            continue
        if seed_i is None and i>=n-1:
            prev=float(np.mean(sv[i-n+1:i+1]))
            seed_i=i
            out.iat[i]=prev
        elif seed_i is not None and i>seed_i:
            denom=float(n)*(sv[i]/prev)**4
            if denom==0.0 or not np.isfinite(denom):
                continue
            prev=prev+(sv[i]-prev)/denom
            out.iat[i]=prev
    return out
def _vwma(s,v,n): return (s*v).rolling(n,n).sum()/v.rolling(n,n).sum().replace(0.0,np.nan)
def _trimmed_mean(s,n,trim=0.1):
    def _f(x):
        k=int(np.floor(trim*len(x)))
        if k*2>=len(x):
            return np.nan
        y=np.sort(x)
        return float(np.mean(y[k:len(y)-k]))
    return s.rolling(n,n).apply(_f,raw=True)
def _winsor_mean(s,n,q=0.1):
    def _f(x):
        lo=np.quantile(x,q); hi=np.quantile(x,1.0-q)
        y=np.clip(x,lo,hi)
        return float(np.mean(y))
    return s.rolling(n,n).apply(_f,raw=True)
def _hurst_rs(x):
    n=len(x)
    if n<16: return np.nan
    y=np.asarray(x,dtype=float)
    if not np.all(np.isfinite(y)): return np.nan
    mean=y.mean()
    dev=y-mean
    z=np.cumsum(dev)
    R=z.max()-z.min()
    S=y.std(ddof=0)
    if S==0.0 or not np.isfinite(R/S) or R/S<=0.0: return np.nan
    return float(np.log(R/S)/np.log(n))
def _streak(x):
    idx=np.where(x>0.5)[0]
    return float(len(x)) if idx.size==0 else float(len(x)-1-idx[-1])
def _consec(x):
    c=0
    for v in x[::-1]:
        if v>0.5: c+=1
        else: break
    return float(c)
def _slope_norm(x):
    n=len(x); t=np.arange(n,dtype=float)
    mt=t.mean(); mx=x.mean()
    cov=np.sum((t-mt)*(x-mx)); vr=np.sum((t-mt)**2)
    if vr==0.0 or not np.isfinite(mx) or mx==0.0: return np.nan
    return float((cov/vr)/mx)
def _rsq(x):
    n=len(x); t=np.arange(n,dtype=float)
    mt=t.mean(); mx=x.mean()
    cov=np.sum((t-mt)*(x-mx))
    vt=np.sum((t-mt)**2); vx=np.sum((x-mx)**2)
    if vt==0.0 or vx==0.0: return np.nan
    r=cov/np.sqrt(vt*vx)
    return float(r*r)
def _resid_std(x):
    n=len(x); t=np.arange(n,dtype=float)
    mt=t.mean(); mx=x.mean()
    cov=np.sum((t-mt)*(x-mx)); vt=np.sum((t-mt)**2)
    if vt==0.0 or not np.isfinite(mx) or mx==0.0: return np.nan
    bb=cov/vt; a=mx-bb*mt
    return float(np.std(x-(a+bb*t))/abs(mx))
def _mad(x): return float(np.mean(np.abs(x-np.mean(x))))
def _ac1(x):
    s=pd.Series(x); return float(s.autocorr(lag=1)) if s.std()>0 else np.nan
def _ac5(x):
    s=pd.Series(x); return float(s.autocorr(lag=5)) if s.std()>0 else np.nan
def f01ms_f01_moving_average_systems_logclose_t3_30d_jerk_v001_signal(closeadj):
    n=30; k=10
    e1=_ema(closeadj,n); e2=_ema(e1,n); e3=_ema(e2,n)
    e4=_ema(e3,n); e5=_ema(e4,n); e6=_ema(e5,n)
    v=0.7
    c1=-v**3; c2=3.0*v**2+3.0*v**3
    c3=-6.0*v**2-3.0*v-3.0*v**3
    c4=1.0+3.0*v+v**3+3.0*v**2
    t3=c1*e6+c2*e5+c3*e4+c4*e3
    b=np.log(closeadj/t3)
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f01ms_f01_moving_average_systems_sign_close_wilder45_jerk_v002_signal(closeadj):
    k=21
    w=closeadj.ewm(alpha=1.0/45.0,adjust=False,min_periods=45).mean()
    b=np.sign(closeadj-w)
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f01ms_f01_moving_average_systems_sign_mcginley_sma_60d_jerk_v003_signal(closeadj):
    k=21
    b=np.sign(_mcginley(closeadj,60)-_sma(closeadj,60))
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f01ms_f01_moving_average_systems_sign_close_zlema18_jerk_v004_signal(close):
    k=5
    b=np.sign(close-_zlema(close,18))
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f01ms_f01_moving_average_systems_logclose_kama_35d_jerk_v005_signal(closeadj):
    k=21
    b=np.log(closeadj/_kama(closeadj,35))
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f01ms_f01_moving_average_systems_t3_ema_diff_30d_jerk_v006_signal(closeadj):
    n=30; k=21
    e1=_ema(closeadj,n); e2=_ema(e1,n); e3=_ema(e2,n)
    e4=_ema(e3,n); e5=_ema(e4,n); e6=_ema(e5,n)
    v=0.7
    c1=-v**3; c2=3.0*v**2+3.0*v**3
    c3=-6.0*v**2-3.0*v-3.0*v**3
    c4=1.0+3.0*v+v**3+3.0*v**2
    t3=c1*e6+c2*e5+c3*e4+c4*e3
    b=np.log(t3/_ema(closeadj,n))
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f01ms_f01_moving_average_systems_sign_tema_dema_25d_jerk_v007_signal(closeadj):
    n=25; k=10
    e1=_ema(closeadj,n); e2=_ema(e1,n); e3=_ema(e2,n)
    tema=3.0*e1-3.0*e2+e3
    dema=2.0*e1-e2
    b=np.sign(tema-dema)
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f01ms_f01_moving_average_systems_kama_sma_diff_50d_jerk_v008_signal(closeadj):
    k=21
    b=np.log(_kama(closeadj,50)/_sma(closeadj,50))
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f01ms_f01_moving_average_systems_sign_zlema_ema_22d_jerk_v009_signal(close):
    k=10
    b=np.sign(_zlema(close,22)-_ema(close,22))
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f01ms_f01_moving_average_systems_wilder_ema_diff_30d_jerk_v010_signal(closeadj):
    k=10
    w=closeadj.ewm(alpha=1.0/30.0,adjust=False,min_periods=30).mean()
    b=np.log(w/_ema(closeadj,30))
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f01ms_f01_moving_average_systems_trimmed_sma_diff_40d_jerk_v011_signal(closeadj):
    n=40; k=10
    trim=_trimmed_mean(closeadj,n,0.1)
    b=np.log(trim/_sma(closeadj,n))
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f01ms_f01_moving_average_systems_winsor_sma_diff_60d_jerk_v012_signal(closeadj):
    n=60; k=21
    wins=_winsor_mean(closeadj,n,0.1)
    b=np.log(wins/_sma(closeadj,n))
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f01ms_f01_moving_average_systems_logclose_trimmed_18d_jerk_v013_signal(close):
    k=5
    b=np.log(close/_trimmed_mean(close,18,0.1))
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f01ms_f01_moving_average_systems_z_close_sma15_45d_jerk_v014_signal(close):
    k=10
    m=_sma(close,15)
    sig=close.rolling(45,45).std()
    b=(close-m)/sig.replace(0.0,np.nan)
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f01ms_f01_moving_average_systems_z_close_ema40_100d_jerk_v015_signal(closeadj):
    k=21
    e=_ema(closeadj,40)
    sig=closeadj.rolling(100,100).std()
    b=(closeadj-e)/sig.replace(0.0,np.nan)
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f01ms_f01_moving_average_systems_z_close_sma120_252d_jerk_v016_signal(closeadj):
    k=63
    m=_sma(closeadj,120)
    sig=closeadj.rolling(252,252).std()
    b=(closeadj-m)/sig.replace(0.0,np.nan)
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f01ms_f01_moving_average_systems_sigmoid_dist_ema20_jerk_v017_signal(close):
    k=10
    e=_ema(close,20)
    d=close-e
    mad=d.rolling(15,15).apply(_mad,raw=True)
    z=d/mad.replace(0.0,np.nan)
    b=1.0/(1.0+np.exp(-z.clip(-30.0,30.0)))
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f01ms_f01_moving_average_systems_sigmoid_ma_slope_60d_jerk_v018_signal(closeadj):
    k=21
    m=_sma(closeadj,60)
    sl=m.diff(21)
    sig=sl.rolling(60,60).std()
    z=sl/sig.replace(0.0,np.nan)
    b=1.0/(1.0+np.exp(-z.clip(-30.0,30.0)))
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f01ms_f01_moving_average_systems_pctB_close_sma20_band_jerk_v019_signal(close):
    n=20; k=10
    m=_sma(close,n)
    sd=close.rolling(n,n).std()
    upper=m+2.0*sd; lower=m-2.0*sd
    b=(close-lower)/(upper-lower).replace(0.0,np.nan)
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f01ms_f01_moving_average_systems_pctB_width_50d_jerk_v020_signal(closeadj):
    n=50; k=10
    e=_ema(closeadj,n)
    sd=closeadj.rolling(n,n).std()
    b=4.0*sd/e
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f01ms_f01_moving_average_systems_ma_velocity_sma25_jerk_v021_signal(closeadj):
    k=10
    m=_sma(closeadj,25)
    b=m.diff(5)/m
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f01ms_f01_moving_average_systems_ma_velocity_ema60_jerk_v022_signal(closeadj):
    k=21
    e=_ema(closeadj,60)
    b=e.diff(10)/e
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f01ms_f01_moving_average_systems_ma_velocity_hma20_jerk_v023_signal(close):
    k=5
    h=_hma(close,20)
    b=h.diff(3)/h
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f01ms_f01_moving_average_systems_slope_spread_sma10_40_jerk_v024_signal(close):
    k=10
    s10=_sma(close,10); s40=_sma(close,40)
    b=s10.diff(5)/s10-s40.diff(5)/s40
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f01ms_f01_moving_average_systems_slope_spread_ema30_100_jerk_v025_signal(closeadj):
    k=63
    e30=_ema(closeadj,30); e100=_ema(closeadj,100)
    b=e30.diff(10)/e30-e100.diff(10)/e100
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f01ms_f01_moving_average_systems_daysince_sma_5_15_40d_jerk_v026_signal(close):
    k=10
    diff=_sma(close,5)-_sma(close,15)
    s=np.sign(diff)
    flip=(s!=s.shift(1)).astype(float).where(~s.isna()&~s.shift(1).isna())
    b=flip.rolling(40,40).apply(_streak,raw=True)
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f01ms_f01_moving_average_systems_daysince_wma_15_45_80d_jerk_v027_signal(closeadj):
    k=21
    diff=_wma(closeadj,15)-_wma(closeadj,45)
    s=np.sign(diff)
    flip=(s!=s.shift(1)).astype(float).where(~s.isna()&~s.shift(1).isna())
    b=flip.rolling(80,80).apply(_streak,raw=True)
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f01ms_f01_moving_average_systems_streak_above_sma10_50d_jerk_v028_signal(close):
    k=21
    sgn=(close>_sma(close,10)).astype(float).where(~_sma(close,10).isna())
    b=sgn.rolling(50,50).apply(_consec,raw=True)
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f01ms_f01_moving_average_systems_streak_below_ema40_120d_jerk_v029_signal(closeadj):
    k=63
    sgn=(closeadj<_ema(closeadj,40)).astype(float).where(~_ema(closeadj,40).isna())
    b=sgn.rolling(120,120).apply(_consec,raw=True)
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f01ms_f01_moving_average_systems_hurst_close_60d_jerk_v030_signal(closeadj):
    k=21
    r=np.log(closeadj/closeadj.shift(1))
    b=r.rolling(60,60).apply(_hurst_rs,raw=True)
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f01ms_f01_moving_average_systems_hurst_close_120d_jerk_v031_signal(closeadj):
    k=63
    r=np.log(closeadj/closeadj.shift(1))
    b=r.rolling(120,120).apply(_hurst_rs,raw=True)
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f01ms_f01_moving_average_systems_mad_std_ratio_30d_jerk_v032_signal(closeadj):
    k=10
    d=closeadj-_sma(closeadj,30)
    mad=d.rolling(30,30).apply(_mad,raw=True)
    sd=d.rolling(30,30).std()
    b=mad/sd.replace(0.0,np.nan)
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f01ms_f01_moving_average_systems_mad_std_ratio_ema_80d_jerk_v033_signal(closeadj):
    k=21
    d=closeadj-_ema(closeadj,80)
    mad=d.rolling(80,80).apply(_mad,raw=True)
    sd=d.rolling(80,80).std()
    b=mad/sd.replace(0.0,np.nan)
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f01ms_f01_moving_average_systems_regslope_sma15_30d_jerk_v034_signal(close):
    k=10
    b=_sma(close,15).rolling(30,30).apply(_slope_norm,raw=True)
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f01ms_f01_moving_average_systems_regslope_ema60_80d_jerk_v035_signal(closeadj):
    k=21
    b=_ema(closeadj,60).rolling(80,80).apply(_slope_norm,raw=True)
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f01ms_f01_moving_average_systems_rsq_sma30_60d_jerk_v036_signal(closeadj):
    k=21
    b=_sma(closeadj,30).rolling(60,60).apply(_rsq,raw=True)
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f01ms_f01_moving_average_systems_rsq_ema100_120d_jerk_v037_signal(closeadj):
    k=21
    b=_ema(closeadj,100).rolling(120,120).apply(_rsq,raw=True)
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f01ms_f01_moving_average_systems_regresid_sma40_50d_jerk_v038_signal(closeadj):
    k=21
    b=_sma(closeadj,40).rolling(50,50).apply(_resid_std,raw=True)
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f01ms_f01_moving_average_systems_stoch_close_sma20_30d_jerk_v039_signal(close):
    k=10
    m=_sma(close,20)
    hi=m.rolling(30,30).max(); lo=m.rolling(30,30).min()
    b=(close-lo)/(hi-lo).replace(0.0,np.nan)
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f01ms_f01_moving_average_systems_stoch_ema_50_100d_jerk_v040_signal(closeadj):
    k=21
    e=_ema(closeadj,50)
    hi=e.rolling(100,100).max(); lo=e.rolling(100,100).min()
    b=(e-lo)/(hi-lo).replace(0.0,np.nan)
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f01ms_f01_moving_average_systems_dev_autocorr_sma20_40d_jerk_v041_signal(close):
    k=10
    d=close-_sma(close,20)
    b=d.rolling(40,40).apply(_ac1,raw=False)
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f01ms_f01_moving_average_systems_dev_autocorr_ema40_60d_jerk_v042_signal(closeadj):
    k=21
    d=closeadj-_ema(closeadj,40)
    b=d.rolling(60,60).apply(_ac5,raw=False)
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f01ms_f01_moving_average_systems_return_autocorr_30d_jerk_v043_signal(close):
    k=10
    r=close.pct_change()
    b=r.rolling(30,30).apply(_ac1,raw=False)
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f01ms_f01_moving_average_systems_return_autocorr_100d_jerk_v044_signal(closeadj):
    k=21
    r=closeadj.pct_change()
    b=r.rolling(100,100).apply(_ac5,raw=False)
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f01ms_f01_moving_average_systems_return_skew_50d_jerk_v045_signal(closeadj):
    k=21
    r=np.log(closeadj/closeadj.shift(1))
    b=r.rolling(50,50).skew()
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f01ms_f01_moving_average_systems_rank_close_sma25_45d_jerk_v046_signal(close):
    k=10
    d=close-_sma(close,25)
    b=d.rolling(45,45).rank(pct=True)
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f01ms_f01_moving_average_systems_rank_logclose_ema80_180d_jerk_v047_signal(closeadj):
    k=63
    d=np.log(closeadj/_ema(closeadj,80))
    b=d.rolling(180,180).rank(pct=True)
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f01ms_f01_moving_average_systems_rank_hma40_120d_jerk_v048_signal(closeadj):
    k=21
    d=_hma(closeadj,40)-_sma(closeadj,40)
    b=d.rolling(120,120).rank(pct=True)
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f01ms_f01_moving_average_systems_ribbon_iqr_wma_70d_jerk_v049_signal(closeadj):
    k=21
    w=[_wma(closeadj,kk) for kk in (12,24,36,48,60,70)]
    mat=pd.concat(w,axis=1)
    iqr=mat.quantile(0.75,axis=1)-mat.quantile(0.25,axis=1)
    b=iqr/closeadj
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f01ms_f01_moving_average_systems_ribbon_position_50d_jerk_v050_signal(closeadj):
    k=21
    sn=[_sma(closeadj,kk) for kk in (10,20,30,40,50)]
    cnt=pd.Series(0.0,index=closeadj.index)
    mask=~sn[0].isna()
    for s in sn:
        cnt=cnt+(closeadj>s).astype(float)
        mask=mask&~s.isna()
    b=cnt.where(mask)
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f01ms_f01_moving_average_systems_ribbon_skew_60d_jerk_v051_signal(closeadj):
    k=21
    e=[_ema(closeadj,kk) for kk in (12,24,36,48,60)]
    mat=pd.concat(e,axis=1)
    b=mat.skew(axis=1)
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f01ms_f01_moving_average_systems_ma_acc_signum_30d_jerk_v052_signal(closeadj):
    k=10
    m=_sma(closeadj,30)
    b=np.sign(m.diff(5).diff(5))
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f01ms_f01_moving_average_systems_count_ma_pos_slopes_45d_jerk_v053_signal(closeadj):
    k=21
    sigs=[
        (_sma(closeadj,20).diff(21)>0).astype(float),
        (_ema(closeadj,30).diff(21)>0).astype(float),
        (_wma(closeadj,40).diff(21)>0).astype(float),
        (_hma(closeadj,25).diff(21)>0).astype(float),
        ((2.0*_ema(closeadj,20)-_ema(_ema(closeadj,20),20)).diff(21)>0).astype(float),
    ]
    mat=pd.concat(sigs,axis=1)
    mask=~_sma(closeadj,20).diff(21).isna()&~_hma(closeadj,25).diff(21).isna()
    b=mat.sum(axis=1).where(mask)
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f01ms_f01_moving_average_systems_ma_velocity_zscore_35d_jerk_v054_signal(closeadj):
    k=10
    e=_ema(closeadj,35)
    v=e.diff(5)
    b=(v-v.rolling(90,90).mean())/v.rolling(90,90).std()
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f01ms_f01_moving_average_systems_arctan_dist_sma10_jerk_v055_signal(close):
    k=5
    m=_sma(close,10)
    sig=close.rolling(10,10).std()
    b=np.arctan((close-m)/sig.replace(0.0,np.nan))
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f01ms_f01_moving_average_systems_tanh_dist_ema120_jerk_v056_signal(closeadj):
    k=63
    e=_ema(closeadj,120)
    sig=closeadj.rolling(60,60).std()
    b=np.tanh((closeadj-e)/sig.replace(0.0,np.nan))
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f01ms_f01_moving_average_systems_corr_sma_ema_50d_jerk_v057_signal(closeadj):
    k=21
    b=_sma(closeadj,15).rolling(50,50).corr(_ema(closeadj,15))
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f01ms_f01_moving_average_systems_corr_hma_wma_80d_jerk_v058_signal(closeadj):
    k=21
    b=_hma(closeadj,20).rolling(80,80).corr(_wma(closeadj,20))
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f01ms_f01_moving_average_systems_sign_close_wma15_jerk_v059_signal(close):
    k=10
    b=np.sign(close-_wma(close,15))
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f01ms_f01_moving_average_systems_sign_close_zlema35_jerk_v060_signal(closeadj):
    k=21
    b=np.sign(closeadj-_zlema(closeadj,35))
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f01ms_f01_moving_average_systems_sign_wma10_wma35_jerk_v061_signal(close):
    k=10
    b=np.sign(_wma(close,10)-_wma(close,35))
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f01ms_f01_moving_average_systems_sign_tema30_tema60_jerk_v062_signal(closeadj):
    k=21
    b=np.sign(_tema(closeadj,30)-_tema(closeadj,60))
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f01ms_f01_moving_average_systems_slope_positive_frac_sma25_45d_jerk_v063_signal(closeadj):
    k=10
    m=_sma(closeadj,25)
    pos=(m.diff(5)>0).astype(float).where(~m.diff(5).isna())
    b=pos.rolling(45,45).mean()
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f01ms_f01_moving_average_systems_slope_positive_frac_ema80_120d_jerk_v064_signal(closeadj):
    k=21
    e=_ema(closeadj,80)
    pos=(e.diff(21)>0).astype(float).where(~e.diff(21).isna())
    b=pos.rolling(120,120).mean()
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f01ms_f01_moving_average_systems_curv_ema25_norm_jerk_v065_signal(closeadj):
    k=10
    e=_ema(closeadj,25)
    c=e-2.0*e.shift(5)+e.shift(10)
    sig=e.rolling(20,20).std()
    b=c/sig.replace(0.0,np.nan)
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f01ms_f01_moving_average_systems_curv_wma50_norm_jerk_v066_signal(closeadj):
    k=21
    w=_wma(closeadj,50)
    c=w-2.0*w.shift(10)+w.shift(20)
    sig=w.rolling(40,40).std()
    b=c/sig.replace(0.0,np.nan)
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f01ms_f01_moving_average_systems_dv_efficiency_30d_jerk_v067_signal(closeadj,volume):
    k=10
    m=_sma(closeadj,30)
    dv=(closeadj*volume).rolling(30,30).mean()
    b=(m.diff(10).abs())/dv
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f01ms_f01_moving_average_systems_volprice_ma_corr_60d_jerk_v068_signal(closeadj,volume):
    k=21
    b=_sma(closeadj,15).rolling(60,60).corr(_sma(volume,15))
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f01ms_f01_moving_average_systems_corr_close_sma_lag20_60d_jerk_v069_signal(closeadj):
    k=21
    b=closeadj.rolling(60,60).corr(_sma(closeadj,15).shift(20))
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f01ms_f01_moving_average_systems_ma_range_sma30_50d_jerk_v070_signal(closeadj):
    k=10
    m=_sma(closeadj,30)
    rng=m.rolling(50,50).max()-m.rolling(50,50).min()
    b=rng/closeadj
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f01ms_f01_moving_average_systems_ma_range_ema60_120d_jerk_v071_signal(closeadj):
    k=21
    e=_ema(closeadj,60)
    rng=e.rolling(120,120).max()-e.rolling(120,120).min()
    b=rng/e
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f01ms_f01_moving_average_systems_xover_mag_z_sma_30_90_jerk_v072_signal(closeadj):
    k=21
    mag=(_sma(closeadj,30)-_sma(closeadj,90)).abs()/closeadj
    b=(mag-mag.rolling(60,60).mean())/mag.rolling(60,60).std()
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f01ms_f01_moving_average_systems_ker_25d_jerk_v073_signal(closeadj):
    k=10
    n=25
    direction=(closeadj-closeadj.shift(n)).abs()
    volatility=closeadj.diff().abs().rolling(n,n).sum()
    b=direction/volatility.replace(0.0,np.nan)
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f01ms_f01_moving_average_systems_ker_80d_jerk_v074_signal(closeadj):
    k=21
    n=80
    direction=(closeadj-closeadj.shift(n)).abs()
    volatility=closeadj.diff().abs().rolling(n,n).sum()
    b=direction/volatility.replace(0.0,np.nan)
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f01ms_f01_moving_average_systems_reversion_rate_sma20_50d_jerk_v075_signal(closeadj):
    k=21
    diff=closeadj-_sma(closeadj,20)
    s=np.sign(diff)
    flip=(s!=s.shift(1)).astype(float).where(~s.isna()&~s.shift(1).isna())
    b=flip.rolling(50,50).sum()/50.0
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f01ms_f01_moving_average_systems_sign_close_sma8d_jerk_v076_signal(close):
    k=10
    b=np.sign(close-_sma(close,8))
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f01ms_f01_moving_average_systems_sign_close_sma50d_jerk_v077_signal(closeadj):
    k=21
    b=np.sign(closeadj-_sma(closeadj,50))
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f01ms_f01_moving_average_systems_sign_close_sma200d_jerk_v078_signal(closeadj):
    k=63
    b=np.sign(closeadj-_sma(closeadj,200))
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f01ms_f01_moving_average_systems_sign_sma5_sma20_jerk_v079_signal(close):
    k=10
    b=np.sign(_sma(close,5)-_sma(close,20))
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f01ms_f01_moving_average_systems_sign_ema20_ema50_jerk_v080_signal(closeadj):
    k=21
    b=np.sign(_ema(closeadj,20)-_ema(closeadj,50))
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f01ms_f01_moving_average_systems_sign_sma50_sma200_jerk_v081_signal(closeadj):
    k=63
    b=np.sign(_sma(closeadj,50)-_sma(closeadj,200))
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f01ms_f01_moving_average_systems_sign_hma30_hma90_jerk_v082_signal(closeadj):
    k=21
    b=np.sign(_hma(closeadj,30)-_hma(closeadj,90))
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f01ms_f01_moving_average_systems_sign_vwma_sma_30d_jerk_v083_signal(closeadj,volume):
    k=10
    b=np.sign(_vwma(closeadj,volume,30)-_sma(closeadj,30))
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f01ms_f01_moving_average_systems_daysince_close_sma20_30d_jerk_v084_signal(closeadj):
    k=10
    diff=closeadj-_sma(closeadj,20)
    s=np.sign(diff)
    flip=(s!=s.shift(1)).astype(float).where(~s.isna()&~s.shift(1).isna())
    b=flip.rolling(30,30).apply(_streak,raw=True)
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f01ms_f01_moving_average_systems_daysince_close_sma50_100d_jerk_v085_signal(closeadj):
    k=21
    diff=closeadj-_sma(closeadj,50)
    s=np.sign(diff)
    flip=(s!=s.shift(1)).astype(float).where(~s.isna()&~s.shift(1).isna())
    b=flip.rolling(100,100).apply(_streak,raw=True)
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f01ms_f01_moving_average_systems_daysince_ema_2050_150d_jerk_v086_signal(closeadj):
    k=63
    diff=_ema(closeadj,20)-_ema(closeadj,50)
    s=np.sign(diff)
    flip=(s!=s.shift(1)).astype(float).where(~s.isna()&~s.shift(1).isna())
    b=flip.rolling(150,150).apply(_streak,raw=True)
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f01ms_f01_moving_average_systems_daysince_sma_50200_252d_jerk_v087_signal(closeadj):
    k=63
    diff=_sma(closeadj,50)-_sma(closeadj,200)
    s=np.sign(diff)
    flip=(s!=s.shift(1)).astype(float).where(~s.isna()&~s.shift(1).isna())
    b=flip.rolling(252,252).apply(_streak,raw=True)
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f01ms_f01_moving_average_systems_crossfreq_close_sma20_30d_jerk_v088_signal(closeadj):
    k=10
    diff=closeadj-_sma(closeadj,20)
    s=np.sign(diff)
    flip=(s!=s.shift(1)).astype(float).where(~s.isna()&~s.shift(1).isna())
    b=flip.rolling(30,30).sum()
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f01ms_f01_moving_average_systems_crossfreq_ema_1040_120d_jerk_v089_signal(closeadj):
    k=21
    diff=_ema(closeadj,10)-_ema(closeadj,40)
    s=np.sign(diff)
    flip=(s!=s.shift(1)).astype(float).where(~s.isna()&~s.shift(1).isna())
    b=flip.rolling(120,120).sum()
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f01ms_f01_moving_average_systems_crossfreq_sma_50200_252d_jerk_v090_signal(closeadj):
    k=63
    diff=_sma(closeadj,50)-_sma(closeadj,200)
    s=np.sign(diff)
    flip=(s!=s.shift(1)).astype(float).where(~s.isna()&~s.shift(1).isna())
    b=flip.rolling(252,252).sum()
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f01ms_f01_moving_average_systems_fracabove_sma20_60d_jerk_v091_signal(closeadj):
    k=21
    diff=closeadj-_sma(closeadj,20)
    sgn=(diff>0).astype(float).where(~diff.isna())
    b=sgn.rolling(60,60).mean()
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f01ms_f01_moving_average_systems_fracabove_sma200_120d_jerk_v092_signal(closeadj):
    k=21
    diff=closeadj-_sma(closeadj,200)
    sgn=(diff>0).astype(float).where(~diff.isna())
    b=sgn.rolling(120,120).mean()
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f01ms_f01_moving_average_systems_fracabove_ema50_30d_jerk_v093_signal(closeadj):
    k=10
    diff=closeadj-_ema(closeadj,50)
    sgn=(diff>0).astype(float).where(~diff.isna())
    b=sgn.rolling(30,30).mean()
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f01ms_f01_moving_average_systems_ribbon_order_short_jerk_v094_signal(closeadj):
    k=21
    sn=[_sma(closeadj,kk) for kk in (8,16,24,32,40)]
    cnt=pd.Series(0.0,index=closeadj.index)
    mask=~sn[0].isna()
    for i in range(len(sn)):
        for j in range(i+1,len(sn)):
            cnt=cnt+(sn[i]>sn[j]).astype(float)
            mask=mask&~sn[i].isna()&~sn[j].isna()
    b=cnt.where(mask)
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f01ms_f01_moving_average_systems_ribbon_order_long_jerk_v095_signal(closeadj):
    k=21
    sn=[_ema(closeadj,kk) for kk in (20,40,60,80,100)]
    cnt=pd.Series(0.0,index=closeadj.index)
    mask=~sn[0].isna()
    for i in range(len(sn)):
        for j in range(i+1,len(sn)):
            cnt=cnt+(sn[i]>sn[j]).astype(float)
            mask=mask&~sn[i].isna()&~sn[j].isna()
    b=cnt.where(mask)
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f01ms_f01_moving_average_systems_ribbon_dispnorm_50d_jerk_v096_signal(closeadj):
    k=21
    e=[_ema(closeadj,kk) for kk in (10,20,30,40,50)]
    mat=pd.concat(e,axis=1)
    b=(mat.max(axis=1)-mat.min(axis=1))/mat.mean(axis=1)
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f01ms_f01_moving_average_systems_ribbon_cv_80d_jerk_v097_signal(closeadj):
    k=21
    e=[_ema(closeadj,kk) for kk in (15,30,45,60,80)]
    mat=pd.concat(e,axis=1)
    b=mat.std(axis=1)/mat.mean(axis=1)
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f01ms_f01_moving_average_systems_kernel_disp_25d_jerk_v098_signal(closeadj):
    n=25; k=10
    a=_sma(closeadj,n); b1=_ema(closeadj,n); c=_wma(closeadj,n)
    d=_hma(closeadj,n); e=_alma(closeadj,n)
    mat=pd.concat([a,b1,c,d,e],axis=1)
    b=mat.std(axis=1)/mat.mean(axis=1)
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f01ms_f01_moving_average_systems_kernel_agree_30d_jerk_v099_signal(closeadj):
    n=30; k=21
    sigs=[(closeadj>_sma(closeadj,n)).astype(float),
          (closeadj>_ema(closeadj,n)).astype(float),
          (closeadj>_wma(closeadj,n)).astype(float),
          (closeadj>_hma(closeadj,n)).astype(float),
          (closeadj>_dema(closeadj,n)).astype(float)]
    mat=pd.concat(sigs,axis=1)
    mask=~_sma(closeadj,n).isna()&~_hma(closeadj,n).isna()&~_dema(closeadj,n).isna()
    b=mat.sum(axis=1).where(mask)
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f01ms_f01_moving_average_systems_rank_logclose_sma20_120d_jerk_v100_signal(closeadj):
    k=63
    d=np.log(closeadj/_sma(closeadj,20))
    b=d.rolling(120,120).rank(pct=True)
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f01ms_f01_moving_average_systems_rank_ema_2050_diff_252d_jerk_v101_signal(closeadj):
    k=63
    d=np.log(_ema(closeadj,20)/_ema(closeadj,50))
    b=d.rolling(252,252).rank(pct=True)
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f01ms_f01_moving_average_systems_rank_sma_50200_diff_252d_jerk_v102_signal(closeadj):
    k=63
    d=np.log(_sma(closeadj,50)/_sma(closeadj,200))
    b=d.rolling(252,252).rank(pct=True)
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f01ms_f01_moving_average_systems_rank_dist_sma60_30d_jerk_v103_signal(closeadj):
    k=10
    d=closeadj-_sma(closeadj,60)
    b=d.rolling(30,30).rank(pct=True)
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f01ms_f01_moving_average_systems_tanh_z_ema30_jerk_v104_signal(closeadj):
    n=30; k=10
    e=_ema(closeadj,n)
    sig=(closeadj-e).rolling(n,n).std()
    b=np.tanh((closeadj-e)/sig.replace(0.0,np.nan))
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f01ms_f01_moving_average_systems_arctan_z_sma60_jerk_v105_signal(closeadj):
    n=60; k=21
    m=_sma(closeadj,n)
    sig=(closeadj-m).rolling(n,n).std()
    b=np.arctan((closeadj-m)/sig.replace(0.0,np.nan))
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f01ms_f01_moving_average_systems_slope_sign_sma30_jerk_v106_signal(closeadj):
    k=21
    m=_sma(closeadj,30)
    b=np.sign(m-m.shift(10))
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f01ms_f01_moving_average_systems_slope_sign_sma100_jerk_v107_signal(closeadj):
    k=21
    m=_sma(closeadj,100)
    b=np.sign(m-m.shift(21))
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f01ms_f01_moving_average_systems_slope_diff_2060_jerk_v108_signal(closeadj):
    k=10
    b=_sma(closeadj,20).pct_change(10)-_sma(closeadj,60).pct_change(10)
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f01ms_f01_moving_average_systems_ma_slope_streak_30d_jerk_v109_signal(closeadj):
    k=21
    m=_sma(closeadj,30)
    s=np.sign(m-m.shift(10))
    flip=(s!=s.shift(1)).astype(float).where(~s.isna()&~s.shift(1).isna())
    b=flip.rolling(50,50).apply(_streak,raw=True)
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f01ms_f01_moving_average_systems_curv_sma30_jerk_v110_signal(closeadj):
    k=10
    m=_sma(closeadj,30)
    b=(m-2.0*m.shift(5)+m.shift(10))/m
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f01ms_f01_moving_average_systems_curv_ema80_jerk_v111_signal(closeadj):
    k=21
    e=_ema(closeadj,80)
    b=(e-2.0*e.shift(10)+e.shift(20))/e
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f01ms_f01_moving_average_systems_curv_sign_hma40_jerk_v112_signal(closeadj):
    k=21
    h=_hma(closeadj,40)
    b=np.sign(h-2.0*h.shift(10)+h.shift(20))
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f01ms_f01_moving_average_systems_high_ma_low_ma_30d_jerk_v113_signal(high,low):
    k=10
    b=np.log(_sma(high,30)/_sma(low,30))
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f01ms_f01_moving_average_systems_high_ma_low_ma_60d_jerk_v114_signal(high,low):
    k=21
    b=np.log(_ema(high,60)/_ema(low,60))
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f01ms_f01_moving_average_systems_typ_close_diff_50d_jerk_v115_signal(high,low,closeadj):
    k=21
    typ=(high+low+closeadj)/3.0
    b=np.log(_sma(typ,50)/_sma(closeadj,50))
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f01ms_f01_moving_average_systems_hl2_close_diff_25d_jerk_v116_signal(high,low,closeadj):
    k=10
    hl2=0.5*(high+low)
    b=np.log(_ema(hl2,25)/_ema(closeadj,25))
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f01ms_f01_moving_average_systems_ohlc4_close_diff_30d_jerk_v117_signal(open_,high,low,close):
    k=21
    ohlc4=(open_+high+low+close)/4.0
    b=np.log(_wma(ohlc4,30)/_wma(close,30))
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f01ms_f01_moving_average_systems_high_low_ma_ratio_logz_45d_jerk_v118_signal(high,low):
    k=21
    n=45
    sp=np.log(_sma(high,n)/_sma(low,n))
    b=(sp-sp.rolling(60,60).mean())/sp.rolling(60,60).std()
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f01ms_f01_moving_average_systems_high_ma_close_ma_70d_jerk_v119_signal(high,closeadj):
    k=21
    b=np.log(_sma(high,70)/_sma(closeadj,70))
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f01ms_f01_moving_average_systems_updnratio_25d_jerk_v120_signal(close):
    k=10
    n=25
    pc=close.shift(1)
    up_mask=(close>pc).astype(float).where(~pc.isna())
    dn_mask=(close<pc).astype(float).where(~pc.isna())
    upm=(close*up_mask).rolling(n,n).sum()/up_mask.rolling(n,n).sum().replace(0.0,np.nan)
    dnm=(close*dn_mask).rolling(n,n).sum()/dn_mask.rolling(n,n).sum().replace(0.0,np.nan)
    b=np.log(upm/dnm)
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f01ms_f01_moving_average_systems_upma_sma_diff_60d_jerk_v121_signal(closeadj):
    k=21
    n=60
    pc=closeadj.shift(1)
    up_mask=(closeadj>pc).astype(float).where(~pc.isna())
    upm=(closeadj*up_mask).rolling(n,n).sum()/up_mask.rolling(n,n).sum().replace(0.0,np.nan)
    b=np.log(upm/_sma(closeadj,n))
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f01ms_f01_moving_average_systems_vwma_sma_diff_25d_jerk_v122_signal(close,volume):
    k=10
    b=np.log(_vwma(close,volume,25)/_sma(close,25))
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f01ms_f01_moving_average_systems_vwma_short_long_diff_jerk_v123_signal(closeadj,volume):
    k=21
    b=np.log(_vwma(closeadj,volume,15)/_vwma(closeadj,volume,60))
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f01ms_f01_moving_average_systems_sign_vwma60_sma60_jerk_v124_signal(closeadj,volume):
    k=21
    b=np.sign(_vwma(closeadj,volume,60)-_sma(closeadj,60))
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f01ms_f01_moving_average_systems_median_sma_diff_40d_jerk_v125_signal(closeadj):
    k=10
    b=np.log(closeadj.rolling(40,40).median()/_sma(closeadj,40))
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f01ms_f01_moving_average_systems_q75_q25_log_60d_jerk_v126_signal(closeadj):
    k=21
    b=np.log(closeadj.rolling(60,60).quantile(0.75)/closeadj.rolling(60,60).quantile(0.25))
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f01ms_f01_moving_average_systems_close_above_median_30d_jerk_v127_signal(closeadj):
    k=10
    med=closeadj.rolling(30,30).median()
    sgn=(closeadj>med).astype(float).where(~med.isna())
    b=sgn.rolling(30,30).mean()
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f01ms_f01_moving_average_systems_geom_arith_diff_50d_jerk_v128_signal(closeadj):
    k=21
    n=50
    geom=np.exp(np.log(closeadj.replace(0.0,np.nan)).rolling(n,n).mean())
    b=np.log(geom/_sma(closeadj,n))
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f01ms_f01_moving_average_systems_harm_geom_diff_25d_jerk_v129_signal(close):
    k=10
    n=25
    harm=n/(1.0/close.replace(0.0,np.nan)).rolling(n,n).sum()
    geom=np.exp(np.log(close.replace(0.0,np.nan)).rolling(n,n).mean())
    b=np.log(harm/geom)
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f01ms_f01_moving_average_systems_corr_close_sma20_30d_jerk_v130_signal(closeadj):
    k=10
    b=closeadj.rolling(30,30).corr(_sma(closeadj,20))
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f01ms_f01_moving_average_systems_corr_sma20_sma60_120d_jerk_v131_signal(closeadj):
    k=21
    b=_sma(closeadj,20).rolling(120,120).corr(_sma(closeadj,60))
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f01ms_f01_moving_average_systems_corr_ema30_lag10_60d_jerk_v132_signal(closeadj):
    k=21
    e=_ema(closeadj,30)
    b=e.rolling(60,60).corr(e.shift(10))
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f01ms_f01_moving_average_systems_dist_std_sma30_jerk_v133_signal(closeadj):
    k=10
    m=_sma(closeadj,30)
    b=(closeadj-m).rolling(30,30).std()/closeadj
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f01ms_f01_moving_average_systems_dist_std_ema60_jerk_v134_signal(closeadj):
    k=21
    e=_ema(closeadj,60)
    b=(closeadj-e).rolling(60,60).std()/closeadj
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f01ms_f01_moving_average_systems_argmax_close_above_ma_60d_jerk_v135_signal(closeadj):
    k=21
    n=60
    d=closeadj-_sma(closeadj,20)
    def _amax(x):
        if np.any(~np.isfinite(x)): return np.nan
        return float(int(np.argmax(x)))/float(n-1)
    b=d.rolling(n,n).apply(_amax,raw=True)
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f01ms_f01_moving_average_systems_hma_sma_diff_45d_jerk_v136_signal(closeadj):
    k=21
    b=np.log(_hma(closeadj,45)/_sma(closeadj,45))
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f01ms_f01_moving_average_systems_alma_sma_diff_80d_jerk_v137_signal(closeadj):
    k=21
    b=np.log(_alma(closeadj,80)/_sma(closeadj,80))
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f01ms_f01_moving_average_systems_wma_sma_diff_30d_jerk_v138_signal(closeadj):
    k=10
    b=np.log(_wma(closeadj,30)/_sma(closeadj,30))
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f01ms_f01_moving_average_systems_ema_12_26_diff_jerk_v139_signal(close):
    k=21
    b=np.log(_ema(close,12)/_ema(close,26))
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f01ms_f01_moving_average_systems_hma_20_80_diff_jerk_v140_signal(closeadj):
    k=63
    b=np.log(_hma(closeadj,20)/_hma(closeadj,80))
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f01ms_f01_moving_average_systems_wma_10_30_diff_jerk_v141_signal(close):
    k=10
    b=np.log(_wma(close,10)/_wma(close,30))
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f01ms_f01_moving_average_systems_ma_distance_zscore_30d_jerk_v142_signal(closeadj):
    k=10
    n=30
    d=closeadj-_sma(closeadj,n)
    b=(d-d.rolling(90,90).mean())/d.rolling(90,90).std()
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f01ms_f01_moving_average_systems_crossmag_sma_50200_jerk_v143_signal(closeadj):
    k=63
    b=(_sma(closeadj,50)-_sma(closeadj,200)).abs()/closeadj
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f01ms_f01_moving_average_systems_ma_dist_argmin_60d_jerk_v144_signal(closeadj):
    k=21
    n=60
    d=closeadj-_sma(closeadj,n)
    def _amin(x):
        if np.any(~np.isfinite(x)): return np.nan
        return float(int(np.argmin(x)))/float(n-1)
    b=d.rolling(n,n).apply(_amin,raw=True)
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f01ms_f01_moving_average_systems_logclose_sma_8d_jerk_v145_signal(close):
    k=5
    b=np.log(close/_sma(close,8))
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f01ms_f01_moving_average_systems_logclose_sma_50d_jerk_v146_signal(closeadj):
    k=21
    b=np.log(closeadj/_sma(closeadj,50))
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f01ms_f01_moving_average_systems_logclose_sma_252d_jerk_v147_signal(closeadj):
    k=63
    b=np.log(closeadj/_sma(closeadj,252))
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f01ms_f01_moving_average_systems_ma_skew_60d_jerk_v148_signal(closeadj):
    k=21
    d=closeadj-_sma(closeadj,60)
    b=d.rolling(60,60).skew()
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f01ms_f01_moving_average_systems_ma_kurt_60d_jerk_v149_signal(closeadj):
    k=21
    d=closeadj-_sma(closeadj,60)
    b=d.rolling(60,60).kurt()
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
def f01ms_f01_moving_average_systems_ema_acceleration_30d_jerk_v150_signal(closeadj):
    k=10
    b=_ema(closeadj,30).pct_change(5).diff(5)
    return (b-2.0*b.shift(k)+b.shift(2*k)).replace([np.inf,-np.inf],np.nan)
f01_moving_average_systems_jerk_001_150_REGISTRY={
"f01ms_f01_moving_average_systems_logclose_t3_30d_jerk_v001_signal":{"inputs":["closeadj"],"func":f01ms_f01_moving_average_systems_logclose_t3_30d_jerk_v001_signal},
"f01ms_f01_moving_average_systems_sign_close_wilder45_jerk_v002_signal":{"inputs":["closeadj"],"func":f01ms_f01_moving_average_systems_sign_close_wilder45_jerk_v002_signal},
"f01ms_f01_moving_average_systems_sign_mcginley_sma_60d_jerk_v003_signal":{"inputs":["closeadj"],"func":f01ms_f01_moving_average_systems_sign_mcginley_sma_60d_jerk_v003_signal},
"f01ms_f01_moving_average_systems_sign_close_zlema18_jerk_v004_signal":{"inputs":["close"],"func":f01ms_f01_moving_average_systems_sign_close_zlema18_jerk_v004_signal},
"f01ms_f01_moving_average_systems_logclose_kama_35d_jerk_v005_signal":{"inputs":["closeadj"],"func":f01ms_f01_moving_average_systems_logclose_kama_35d_jerk_v005_signal},
"f01ms_f01_moving_average_systems_t3_ema_diff_30d_jerk_v006_signal":{"inputs":["closeadj"],"func":f01ms_f01_moving_average_systems_t3_ema_diff_30d_jerk_v006_signal},
"f01ms_f01_moving_average_systems_sign_tema_dema_25d_jerk_v007_signal":{"inputs":["closeadj"],"func":f01ms_f01_moving_average_systems_sign_tema_dema_25d_jerk_v007_signal},
"f01ms_f01_moving_average_systems_kama_sma_diff_50d_jerk_v008_signal":{"inputs":["closeadj"],"func":f01ms_f01_moving_average_systems_kama_sma_diff_50d_jerk_v008_signal},
"f01ms_f01_moving_average_systems_sign_zlema_ema_22d_jerk_v009_signal":{"inputs":["close"],"func":f01ms_f01_moving_average_systems_sign_zlema_ema_22d_jerk_v009_signal},
"f01ms_f01_moving_average_systems_wilder_ema_diff_30d_jerk_v010_signal":{"inputs":["closeadj"],"func":f01ms_f01_moving_average_systems_wilder_ema_diff_30d_jerk_v010_signal},
"f01ms_f01_moving_average_systems_trimmed_sma_diff_40d_jerk_v011_signal":{"inputs":["closeadj"],"func":f01ms_f01_moving_average_systems_trimmed_sma_diff_40d_jerk_v011_signal},
"f01ms_f01_moving_average_systems_winsor_sma_diff_60d_jerk_v012_signal":{"inputs":["closeadj"],"func":f01ms_f01_moving_average_systems_winsor_sma_diff_60d_jerk_v012_signal},
"f01ms_f01_moving_average_systems_logclose_trimmed_18d_jerk_v013_signal":{"inputs":["close"],"func":f01ms_f01_moving_average_systems_logclose_trimmed_18d_jerk_v013_signal},
"f01ms_f01_moving_average_systems_z_close_sma15_45d_jerk_v014_signal":{"inputs":["close"],"func":f01ms_f01_moving_average_systems_z_close_sma15_45d_jerk_v014_signal},
"f01ms_f01_moving_average_systems_z_close_ema40_100d_jerk_v015_signal":{"inputs":["closeadj"],"func":f01ms_f01_moving_average_systems_z_close_ema40_100d_jerk_v015_signal},
"f01ms_f01_moving_average_systems_z_close_sma120_252d_jerk_v016_signal":{"inputs":["closeadj"],"func":f01ms_f01_moving_average_systems_z_close_sma120_252d_jerk_v016_signal},
"f01ms_f01_moving_average_systems_sigmoid_dist_ema20_jerk_v017_signal":{"inputs":["close"],"func":f01ms_f01_moving_average_systems_sigmoid_dist_ema20_jerk_v017_signal},
"f01ms_f01_moving_average_systems_sigmoid_ma_slope_60d_jerk_v018_signal":{"inputs":["closeadj"],"func":f01ms_f01_moving_average_systems_sigmoid_ma_slope_60d_jerk_v018_signal},
"f01ms_f01_moving_average_systems_pctB_close_sma20_band_jerk_v019_signal":{"inputs":["close"],"func":f01ms_f01_moving_average_systems_pctB_close_sma20_band_jerk_v019_signal},
"f01ms_f01_moving_average_systems_pctB_width_50d_jerk_v020_signal":{"inputs":["closeadj"],"func":f01ms_f01_moving_average_systems_pctB_width_50d_jerk_v020_signal},
"f01ms_f01_moving_average_systems_ma_velocity_sma25_jerk_v021_signal":{"inputs":["closeadj"],"func":f01ms_f01_moving_average_systems_ma_velocity_sma25_jerk_v021_signal},
"f01ms_f01_moving_average_systems_ma_velocity_ema60_jerk_v022_signal":{"inputs":["closeadj"],"func":f01ms_f01_moving_average_systems_ma_velocity_ema60_jerk_v022_signal},
"f01ms_f01_moving_average_systems_ma_velocity_hma20_jerk_v023_signal":{"inputs":["close"],"func":f01ms_f01_moving_average_systems_ma_velocity_hma20_jerk_v023_signal},
"f01ms_f01_moving_average_systems_slope_spread_sma10_40_jerk_v024_signal":{"inputs":["close"],"func":f01ms_f01_moving_average_systems_slope_spread_sma10_40_jerk_v024_signal},
"f01ms_f01_moving_average_systems_slope_spread_ema30_100_jerk_v025_signal":{"inputs":["closeadj"],"func":f01ms_f01_moving_average_systems_slope_spread_ema30_100_jerk_v025_signal},
"f01ms_f01_moving_average_systems_daysince_sma_5_15_40d_jerk_v026_signal":{"inputs":["close"],"func":f01ms_f01_moving_average_systems_daysince_sma_5_15_40d_jerk_v026_signal},
"f01ms_f01_moving_average_systems_daysince_wma_15_45_80d_jerk_v027_signal":{"inputs":["closeadj"],"func":f01ms_f01_moving_average_systems_daysince_wma_15_45_80d_jerk_v027_signal},
"f01ms_f01_moving_average_systems_streak_above_sma10_50d_jerk_v028_signal":{"inputs":["close"],"func":f01ms_f01_moving_average_systems_streak_above_sma10_50d_jerk_v028_signal},
"f01ms_f01_moving_average_systems_streak_below_ema40_120d_jerk_v029_signal":{"inputs":["closeadj"],"func":f01ms_f01_moving_average_systems_streak_below_ema40_120d_jerk_v029_signal},
"f01ms_f01_moving_average_systems_hurst_close_60d_jerk_v030_signal":{"inputs":["closeadj"],"func":f01ms_f01_moving_average_systems_hurst_close_60d_jerk_v030_signal},
"f01ms_f01_moving_average_systems_hurst_close_120d_jerk_v031_signal":{"inputs":["closeadj"],"func":f01ms_f01_moving_average_systems_hurst_close_120d_jerk_v031_signal},
"f01ms_f01_moving_average_systems_mad_std_ratio_30d_jerk_v032_signal":{"inputs":["closeadj"],"func":f01ms_f01_moving_average_systems_mad_std_ratio_30d_jerk_v032_signal},
"f01ms_f01_moving_average_systems_mad_std_ratio_ema_80d_jerk_v033_signal":{"inputs":["closeadj"],"func":f01ms_f01_moving_average_systems_mad_std_ratio_ema_80d_jerk_v033_signal},
"f01ms_f01_moving_average_systems_regslope_sma15_30d_jerk_v034_signal":{"inputs":["close"],"func":f01ms_f01_moving_average_systems_regslope_sma15_30d_jerk_v034_signal},
"f01ms_f01_moving_average_systems_regslope_ema60_80d_jerk_v035_signal":{"inputs":["closeadj"],"func":f01ms_f01_moving_average_systems_regslope_ema60_80d_jerk_v035_signal},
"f01ms_f01_moving_average_systems_rsq_sma30_60d_jerk_v036_signal":{"inputs":["closeadj"],"func":f01ms_f01_moving_average_systems_rsq_sma30_60d_jerk_v036_signal},
"f01ms_f01_moving_average_systems_rsq_ema100_120d_jerk_v037_signal":{"inputs":["closeadj"],"func":f01ms_f01_moving_average_systems_rsq_ema100_120d_jerk_v037_signal},
"f01ms_f01_moving_average_systems_regresid_sma40_50d_jerk_v038_signal":{"inputs":["closeadj"],"func":f01ms_f01_moving_average_systems_regresid_sma40_50d_jerk_v038_signal},
"f01ms_f01_moving_average_systems_stoch_close_sma20_30d_jerk_v039_signal":{"inputs":["close"],"func":f01ms_f01_moving_average_systems_stoch_close_sma20_30d_jerk_v039_signal},
"f01ms_f01_moving_average_systems_stoch_ema_50_100d_jerk_v040_signal":{"inputs":["closeadj"],"func":f01ms_f01_moving_average_systems_stoch_ema_50_100d_jerk_v040_signal},
"f01ms_f01_moving_average_systems_dev_autocorr_sma20_40d_jerk_v041_signal":{"inputs":["close"],"func":f01ms_f01_moving_average_systems_dev_autocorr_sma20_40d_jerk_v041_signal},
"f01ms_f01_moving_average_systems_dev_autocorr_ema40_60d_jerk_v042_signal":{"inputs":["closeadj"],"func":f01ms_f01_moving_average_systems_dev_autocorr_ema40_60d_jerk_v042_signal},
"f01ms_f01_moving_average_systems_return_autocorr_30d_jerk_v043_signal":{"inputs":["close"],"func":f01ms_f01_moving_average_systems_return_autocorr_30d_jerk_v043_signal},
"f01ms_f01_moving_average_systems_return_autocorr_100d_jerk_v044_signal":{"inputs":["closeadj"],"func":f01ms_f01_moving_average_systems_return_autocorr_100d_jerk_v044_signal},
"f01ms_f01_moving_average_systems_return_skew_50d_jerk_v045_signal":{"inputs":["closeadj"],"func":f01ms_f01_moving_average_systems_return_skew_50d_jerk_v045_signal},
"f01ms_f01_moving_average_systems_rank_close_sma25_45d_jerk_v046_signal":{"inputs":["close"],"func":f01ms_f01_moving_average_systems_rank_close_sma25_45d_jerk_v046_signal},
"f01ms_f01_moving_average_systems_rank_logclose_ema80_180d_jerk_v047_signal":{"inputs":["closeadj"],"func":f01ms_f01_moving_average_systems_rank_logclose_ema80_180d_jerk_v047_signal},
"f01ms_f01_moving_average_systems_rank_hma40_120d_jerk_v048_signal":{"inputs":["closeadj"],"func":f01ms_f01_moving_average_systems_rank_hma40_120d_jerk_v048_signal},
"f01ms_f01_moving_average_systems_ribbon_iqr_wma_70d_jerk_v049_signal":{"inputs":["closeadj"],"func":f01ms_f01_moving_average_systems_ribbon_iqr_wma_70d_jerk_v049_signal},
"f01ms_f01_moving_average_systems_ribbon_position_50d_jerk_v050_signal":{"inputs":["closeadj"],"func":f01ms_f01_moving_average_systems_ribbon_position_50d_jerk_v050_signal},
"f01ms_f01_moving_average_systems_ribbon_skew_60d_jerk_v051_signal":{"inputs":["closeadj"],"func":f01ms_f01_moving_average_systems_ribbon_skew_60d_jerk_v051_signal},
"f01ms_f01_moving_average_systems_ma_acc_signum_30d_jerk_v052_signal":{"inputs":["closeadj"],"func":f01ms_f01_moving_average_systems_ma_acc_signum_30d_jerk_v052_signal},
"f01ms_f01_moving_average_systems_count_ma_pos_slopes_45d_jerk_v053_signal":{"inputs":["closeadj"],"func":f01ms_f01_moving_average_systems_count_ma_pos_slopes_45d_jerk_v053_signal},
"f01ms_f01_moving_average_systems_ma_velocity_zscore_35d_jerk_v054_signal":{"inputs":["closeadj"],"func":f01ms_f01_moving_average_systems_ma_velocity_zscore_35d_jerk_v054_signal},
"f01ms_f01_moving_average_systems_arctan_dist_sma10_jerk_v055_signal":{"inputs":["close"],"func":f01ms_f01_moving_average_systems_arctan_dist_sma10_jerk_v055_signal},
"f01ms_f01_moving_average_systems_tanh_dist_ema120_jerk_v056_signal":{"inputs":["closeadj"],"func":f01ms_f01_moving_average_systems_tanh_dist_ema120_jerk_v056_signal},
"f01ms_f01_moving_average_systems_corr_sma_ema_50d_jerk_v057_signal":{"inputs":["closeadj"],"func":f01ms_f01_moving_average_systems_corr_sma_ema_50d_jerk_v057_signal},
"f01ms_f01_moving_average_systems_corr_hma_wma_80d_jerk_v058_signal":{"inputs":["closeadj"],"func":f01ms_f01_moving_average_systems_corr_hma_wma_80d_jerk_v058_signal},
"f01ms_f01_moving_average_systems_sign_close_wma15_jerk_v059_signal":{"inputs":["close"],"func":f01ms_f01_moving_average_systems_sign_close_wma15_jerk_v059_signal},
"f01ms_f01_moving_average_systems_sign_close_zlema35_jerk_v060_signal":{"inputs":["closeadj"],"func":f01ms_f01_moving_average_systems_sign_close_zlema35_jerk_v060_signal},
"f01ms_f01_moving_average_systems_sign_wma10_wma35_jerk_v061_signal":{"inputs":["close"],"func":f01ms_f01_moving_average_systems_sign_wma10_wma35_jerk_v061_signal},
"f01ms_f01_moving_average_systems_sign_tema30_tema60_jerk_v062_signal":{"inputs":["closeadj"],"func":f01ms_f01_moving_average_systems_sign_tema30_tema60_jerk_v062_signal},
"f01ms_f01_moving_average_systems_slope_positive_frac_sma25_45d_jerk_v063_signal":{"inputs":["closeadj"],"func":f01ms_f01_moving_average_systems_slope_positive_frac_sma25_45d_jerk_v063_signal},
"f01ms_f01_moving_average_systems_slope_positive_frac_ema80_120d_jerk_v064_signal":{"inputs":["closeadj"],"func":f01ms_f01_moving_average_systems_slope_positive_frac_ema80_120d_jerk_v064_signal},
"f01ms_f01_moving_average_systems_curv_ema25_norm_jerk_v065_signal":{"inputs":["closeadj"],"func":f01ms_f01_moving_average_systems_curv_ema25_norm_jerk_v065_signal},
"f01ms_f01_moving_average_systems_curv_wma50_norm_jerk_v066_signal":{"inputs":["closeadj"],"func":f01ms_f01_moving_average_systems_curv_wma50_norm_jerk_v066_signal},
"f01ms_f01_moving_average_systems_dv_efficiency_30d_jerk_v067_signal":{"inputs":["closeadj","volume"],"func":f01ms_f01_moving_average_systems_dv_efficiency_30d_jerk_v067_signal},
"f01ms_f01_moving_average_systems_volprice_ma_corr_60d_jerk_v068_signal":{"inputs":["closeadj","volume"],"func":f01ms_f01_moving_average_systems_volprice_ma_corr_60d_jerk_v068_signal},
"f01ms_f01_moving_average_systems_corr_close_sma_lag20_60d_jerk_v069_signal":{"inputs":["closeadj"],"func":f01ms_f01_moving_average_systems_corr_close_sma_lag20_60d_jerk_v069_signal},
"f01ms_f01_moving_average_systems_ma_range_sma30_50d_jerk_v070_signal":{"inputs":["closeadj"],"func":f01ms_f01_moving_average_systems_ma_range_sma30_50d_jerk_v070_signal},
"f01ms_f01_moving_average_systems_ma_range_ema60_120d_jerk_v071_signal":{"inputs":["closeadj"],"func":f01ms_f01_moving_average_systems_ma_range_ema60_120d_jerk_v071_signal},
"f01ms_f01_moving_average_systems_xover_mag_z_sma_30_90_jerk_v072_signal":{"inputs":["closeadj"],"func":f01ms_f01_moving_average_systems_xover_mag_z_sma_30_90_jerk_v072_signal},
"f01ms_f01_moving_average_systems_ker_25d_jerk_v073_signal":{"inputs":["closeadj"],"func":f01ms_f01_moving_average_systems_ker_25d_jerk_v073_signal},
"f01ms_f01_moving_average_systems_ker_80d_jerk_v074_signal":{"inputs":["closeadj"],"func":f01ms_f01_moving_average_systems_ker_80d_jerk_v074_signal},
"f01ms_f01_moving_average_systems_reversion_rate_sma20_50d_jerk_v075_signal":{"inputs":["closeadj"],"func":f01ms_f01_moving_average_systems_reversion_rate_sma20_50d_jerk_v075_signal},
"f01ms_f01_moving_average_systems_sign_close_sma8d_jerk_v076_signal":{"inputs":["close"],"func":f01ms_f01_moving_average_systems_sign_close_sma8d_jerk_v076_signal},
"f01ms_f01_moving_average_systems_sign_close_sma50d_jerk_v077_signal":{"inputs":["closeadj"],"func":f01ms_f01_moving_average_systems_sign_close_sma50d_jerk_v077_signal},
"f01ms_f01_moving_average_systems_sign_close_sma200d_jerk_v078_signal":{"inputs":["closeadj"],"func":f01ms_f01_moving_average_systems_sign_close_sma200d_jerk_v078_signal},
"f01ms_f01_moving_average_systems_sign_sma5_sma20_jerk_v079_signal":{"inputs":["close"],"func":f01ms_f01_moving_average_systems_sign_sma5_sma20_jerk_v079_signal},
"f01ms_f01_moving_average_systems_sign_ema20_ema50_jerk_v080_signal":{"inputs":["closeadj"],"func":f01ms_f01_moving_average_systems_sign_ema20_ema50_jerk_v080_signal},
"f01ms_f01_moving_average_systems_sign_sma50_sma200_jerk_v081_signal":{"inputs":["closeadj"],"func":f01ms_f01_moving_average_systems_sign_sma50_sma200_jerk_v081_signal},
"f01ms_f01_moving_average_systems_sign_hma30_hma90_jerk_v082_signal":{"inputs":["closeadj"],"func":f01ms_f01_moving_average_systems_sign_hma30_hma90_jerk_v082_signal},
"f01ms_f01_moving_average_systems_sign_vwma_sma_30d_jerk_v083_signal":{"inputs":["closeadj","volume"],"func":f01ms_f01_moving_average_systems_sign_vwma_sma_30d_jerk_v083_signal},
"f01ms_f01_moving_average_systems_daysince_close_sma20_30d_jerk_v084_signal":{"inputs":["closeadj"],"func":f01ms_f01_moving_average_systems_daysince_close_sma20_30d_jerk_v084_signal},
"f01ms_f01_moving_average_systems_daysince_close_sma50_100d_jerk_v085_signal":{"inputs":["closeadj"],"func":f01ms_f01_moving_average_systems_daysince_close_sma50_100d_jerk_v085_signal},
"f01ms_f01_moving_average_systems_daysince_ema_2050_150d_jerk_v086_signal":{"inputs":["closeadj"],"func":f01ms_f01_moving_average_systems_daysince_ema_2050_150d_jerk_v086_signal},
"f01ms_f01_moving_average_systems_daysince_sma_50200_252d_jerk_v087_signal":{"inputs":["closeadj"],"func":f01ms_f01_moving_average_systems_daysince_sma_50200_252d_jerk_v087_signal},
"f01ms_f01_moving_average_systems_crossfreq_close_sma20_30d_jerk_v088_signal":{"inputs":["closeadj"],"func":f01ms_f01_moving_average_systems_crossfreq_close_sma20_30d_jerk_v088_signal},
"f01ms_f01_moving_average_systems_crossfreq_ema_1040_120d_jerk_v089_signal":{"inputs":["closeadj"],"func":f01ms_f01_moving_average_systems_crossfreq_ema_1040_120d_jerk_v089_signal},
"f01ms_f01_moving_average_systems_crossfreq_sma_50200_252d_jerk_v090_signal":{"inputs":["closeadj"],"func":f01ms_f01_moving_average_systems_crossfreq_sma_50200_252d_jerk_v090_signal},
"f01ms_f01_moving_average_systems_fracabove_sma20_60d_jerk_v091_signal":{"inputs":["closeadj"],"func":f01ms_f01_moving_average_systems_fracabove_sma20_60d_jerk_v091_signal},
"f01ms_f01_moving_average_systems_fracabove_sma200_120d_jerk_v092_signal":{"inputs":["closeadj"],"func":f01ms_f01_moving_average_systems_fracabove_sma200_120d_jerk_v092_signal},
"f01ms_f01_moving_average_systems_fracabove_ema50_30d_jerk_v093_signal":{"inputs":["closeadj"],"func":f01ms_f01_moving_average_systems_fracabove_ema50_30d_jerk_v093_signal},
"f01ms_f01_moving_average_systems_ribbon_order_short_jerk_v094_signal":{"inputs":["closeadj"],"func":f01ms_f01_moving_average_systems_ribbon_order_short_jerk_v094_signal},
"f01ms_f01_moving_average_systems_ribbon_order_long_jerk_v095_signal":{"inputs":["closeadj"],"func":f01ms_f01_moving_average_systems_ribbon_order_long_jerk_v095_signal},
"f01ms_f01_moving_average_systems_ribbon_dispnorm_50d_jerk_v096_signal":{"inputs":["closeadj"],"func":f01ms_f01_moving_average_systems_ribbon_dispnorm_50d_jerk_v096_signal},
"f01ms_f01_moving_average_systems_ribbon_cv_80d_jerk_v097_signal":{"inputs":["closeadj"],"func":f01ms_f01_moving_average_systems_ribbon_cv_80d_jerk_v097_signal},
"f01ms_f01_moving_average_systems_kernel_disp_25d_jerk_v098_signal":{"inputs":["closeadj"],"func":f01ms_f01_moving_average_systems_kernel_disp_25d_jerk_v098_signal},
"f01ms_f01_moving_average_systems_kernel_agree_30d_jerk_v099_signal":{"inputs":["closeadj"],"func":f01ms_f01_moving_average_systems_kernel_agree_30d_jerk_v099_signal},
"f01ms_f01_moving_average_systems_rank_logclose_sma20_120d_jerk_v100_signal":{"inputs":["closeadj"],"func":f01ms_f01_moving_average_systems_rank_logclose_sma20_120d_jerk_v100_signal},
"f01ms_f01_moving_average_systems_rank_ema_2050_diff_252d_jerk_v101_signal":{"inputs":["closeadj"],"func":f01ms_f01_moving_average_systems_rank_ema_2050_diff_252d_jerk_v101_signal},
"f01ms_f01_moving_average_systems_rank_sma_50200_diff_252d_jerk_v102_signal":{"inputs":["closeadj"],"func":f01ms_f01_moving_average_systems_rank_sma_50200_diff_252d_jerk_v102_signal},
"f01ms_f01_moving_average_systems_rank_dist_sma60_30d_jerk_v103_signal":{"inputs":["closeadj"],"func":f01ms_f01_moving_average_systems_rank_dist_sma60_30d_jerk_v103_signal},
"f01ms_f01_moving_average_systems_tanh_z_ema30_jerk_v104_signal":{"inputs":["closeadj"],"func":f01ms_f01_moving_average_systems_tanh_z_ema30_jerk_v104_signal},
"f01ms_f01_moving_average_systems_arctan_z_sma60_jerk_v105_signal":{"inputs":["closeadj"],"func":f01ms_f01_moving_average_systems_arctan_z_sma60_jerk_v105_signal},
"f01ms_f01_moving_average_systems_slope_sign_sma30_jerk_v106_signal":{"inputs":["closeadj"],"func":f01ms_f01_moving_average_systems_slope_sign_sma30_jerk_v106_signal},
"f01ms_f01_moving_average_systems_slope_sign_sma100_jerk_v107_signal":{"inputs":["closeadj"],"func":f01ms_f01_moving_average_systems_slope_sign_sma100_jerk_v107_signal},
"f01ms_f01_moving_average_systems_slope_diff_2060_jerk_v108_signal":{"inputs":["closeadj"],"func":f01ms_f01_moving_average_systems_slope_diff_2060_jerk_v108_signal},
"f01ms_f01_moving_average_systems_ma_slope_streak_30d_jerk_v109_signal":{"inputs":["closeadj"],"func":f01ms_f01_moving_average_systems_ma_slope_streak_30d_jerk_v109_signal},
"f01ms_f01_moving_average_systems_curv_sma30_jerk_v110_signal":{"inputs":["closeadj"],"func":f01ms_f01_moving_average_systems_curv_sma30_jerk_v110_signal},
"f01ms_f01_moving_average_systems_curv_ema80_jerk_v111_signal":{"inputs":["closeadj"],"func":f01ms_f01_moving_average_systems_curv_ema80_jerk_v111_signal},
"f01ms_f01_moving_average_systems_curv_sign_hma40_jerk_v112_signal":{"inputs":["closeadj"],"func":f01ms_f01_moving_average_systems_curv_sign_hma40_jerk_v112_signal},
"f01ms_f01_moving_average_systems_high_ma_low_ma_30d_jerk_v113_signal":{"inputs":["high","low"],"func":f01ms_f01_moving_average_systems_high_ma_low_ma_30d_jerk_v113_signal},
"f01ms_f01_moving_average_systems_high_ma_low_ma_60d_jerk_v114_signal":{"inputs":["high","low"],"func":f01ms_f01_moving_average_systems_high_ma_low_ma_60d_jerk_v114_signal},
"f01ms_f01_moving_average_systems_typ_close_diff_50d_jerk_v115_signal":{"inputs":["high","low","closeadj"],"func":f01ms_f01_moving_average_systems_typ_close_diff_50d_jerk_v115_signal},
"f01ms_f01_moving_average_systems_hl2_close_diff_25d_jerk_v116_signal":{"inputs":["high","low","closeadj"],"func":f01ms_f01_moving_average_systems_hl2_close_diff_25d_jerk_v116_signal},
"f01ms_f01_moving_average_systems_ohlc4_close_diff_30d_jerk_v117_signal":{"inputs":["open","high","low","close"],"func":f01ms_f01_moving_average_systems_ohlc4_close_diff_30d_jerk_v117_signal},
"f01ms_f01_moving_average_systems_high_low_ma_ratio_logz_45d_jerk_v118_signal":{"inputs":["high","low"],"func":f01ms_f01_moving_average_systems_high_low_ma_ratio_logz_45d_jerk_v118_signal},
"f01ms_f01_moving_average_systems_high_ma_close_ma_70d_jerk_v119_signal":{"inputs":["high","closeadj"],"func":f01ms_f01_moving_average_systems_high_ma_close_ma_70d_jerk_v119_signal},
"f01ms_f01_moving_average_systems_updnratio_25d_jerk_v120_signal":{"inputs":["close"],"func":f01ms_f01_moving_average_systems_updnratio_25d_jerk_v120_signal},
"f01ms_f01_moving_average_systems_upma_sma_diff_60d_jerk_v121_signal":{"inputs":["closeadj"],"func":f01ms_f01_moving_average_systems_upma_sma_diff_60d_jerk_v121_signal},
"f01ms_f01_moving_average_systems_vwma_sma_diff_25d_jerk_v122_signal":{"inputs":["close","volume"],"func":f01ms_f01_moving_average_systems_vwma_sma_diff_25d_jerk_v122_signal},
"f01ms_f01_moving_average_systems_vwma_short_long_diff_jerk_v123_signal":{"inputs":["closeadj","volume"],"func":f01ms_f01_moving_average_systems_vwma_short_long_diff_jerk_v123_signal},
"f01ms_f01_moving_average_systems_sign_vwma60_sma60_jerk_v124_signal":{"inputs":["closeadj","volume"],"func":f01ms_f01_moving_average_systems_sign_vwma60_sma60_jerk_v124_signal},
"f01ms_f01_moving_average_systems_median_sma_diff_40d_jerk_v125_signal":{"inputs":["closeadj"],"func":f01ms_f01_moving_average_systems_median_sma_diff_40d_jerk_v125_signal},
"f01ms_f01_moving_average_systems_q75_q25_log_60d_jerk_v126_signal":{"inputs":["closeadj"],"func":f01ms_f01_moving_average_systems_q75_q25_log_60d_jerk_v126_signal},
"f01ms_f01_moving_average_systems_close_above_median_30d_jerk_v127_signal":{"inputs":["closeadj"],"func":f01ms_f01_moving_average_systems_close_above_median_30d_jerk_v127_signal},
"f01ms_f01_moving_average_systems_geom_arith_diff_50d_jerk_v128_signal":{"inputs":["closeadj"],"func":f01ms_f01_moving_average_systems_geom_arith_diff_50d_jerk_v128_signal},
"f01ms_f01_moving_average_systems_harm_geom_diff_25d_jerk_v129_signal":{"inputs":["close"],"func":f01ms_f01_moving_average_systems_harm_geom_diff_25d_jerk_v129_signal},
"f01ms_f01_moving_average_systems_corr_close_sma20_30d_jerk_v130_signal":{"inputs":["closeadj"],"func":f01ms_f01_moving_average_systems_corr_close_sma20_30d_jerk_v130_signal},
"f01ms_f01_moving_average_systems_corr_sma20_sma60_120d_jerk_v131_signal":{"inputs":["closeadj"],"func":f01ms_f01_moving_average_systems_corr_sma20_sma60_120d_jerk_v131_signal},
"f01ms_f01_moving_average_systems_corr_ema30_lag10_60d_jerk_v132_signal":{"inputs":["closeadj"],"func":f01ms_f01_moving_average_systems_corr_ema30_lag10_60d_jerk_v132_signal},
"f01ms_f01_moving_average_systems_dist_std_sma30_jerk_v133_signal":{"inputs":["closeadj"],"func":f01ms_f01_moving_average_systems_dist_std_sma30_jerk_v133_signal},
"f01ms_f01_moving_average_systems_dist_std_ema60_jerk_v134_signal":{"inputs":["closeadj"],"func":f01ms_f01_moving_average_systems_dist_std_ema60_jerk_v134_signal},
"f01ms_f01_moving_average_systems_argmax_close_above_ma_60d_jerk_v135_signal":{"inputs":["closeadj"],"func":f01ms_f01_moving_average_systems_argmax_close_above_ma_60d_jerk_v135_signal},
"f01ms_f01_moving_average_systems_hma_sma_diff_45d_jerk_v136_signal":{"inputs":["closeadj"],"func":f01ms_f01_moving_average_systems_hma_sma_diff_45d_jerk_v136_signal},
"f01ms_f01_moving_average_systems_alma_sma_diff_80d_jerk_v137_signal":{"inputs":["closeadj"],"func":f01ms_f01_moving_average_systems_alma_sma_diff_80d_jerk_v137_signal},
"f01ms_f01_moving_average_systems_wma_sma_diff_30d_jerk_v138_signal":{"inputs":["closeadj"],"func":f01ms_f01_moving_average_systems_wma_sma_diff_30d_jerk_v138_signal},
"f01ms_f01_moving_average_systems_ema_12_26_diff_jerk_v139_signal":{"inputs":["close"],"func":f01ms_f01_moving_average_systems_ema_12_26_diff_jerk_v139_signal},
"f01ms_f01_moving_average_systems_hma_20_80_diff_jerk_v140_signal":{"inputs":["closeadj"],"func":f01ms_f01_moving_average_systems_hma_20_80_diff_jerk_v140_signal},
"f01ms_f01_moving_average_systems_wma_10_30_diff_jerk_v141_signal":{"inputs":["close"],"func":f01ms_f01_moving_average_systems_wma_10_30_diff_jerk_v141_signal},
"f01ms_f01_moving_average_systems_ma_distance_zscore_30d_jerk_v142_signal":{"inputs":["closeadj"],"func":f01ms_f01_moving_average_systems_ma_distance_zscore_30d_jerk_v142_signal},
"f01ms_f01_moving_average_systems_crossmag_sma_50200_jerk_v143_signal":{"inputs":["closeadj"],"func":f01ms_f01_moving_average_systems_crossmag_sma_50200_jerk_v143_signal},
"f01ms_f01_moving_average_systems_ma_dist_argmin_60d_jerk_v144_signal":{"inputs":["closeadj"],"func":f01ms_f01_moving_average_systems_ma_dist_argmin_60d_jerk_v144_signal},
"f01ms_f01_moving_average_systems_logclose_sma_8d_jerk_v145_signal":{"inputs":["close"],"func":f01ms_f01_moving_average_systems_logclose_sma_8d_jerk_v145_signal},
"f01ms_f01_moving_average_systems_logclose_sma_50d_jerk_v146_signal":{"inputs":["closeadj"],"func":f01ms_f01_moving_average_systems_logclose_sma_50d_jerk_v146_signal},
"f01ms_f01_moving_average_systems_logclose_sma_252d_jerk_v147_signal":{"inputs":["closeadj"],"func":f01ms_f01_moving_average_systems_logclose_sma_252d_jerk_v147_signal},
"f01ms_f01_moving_average_systems_ma_skew_60d_jerk_v148_signal":{"inputs":["closeadj"],"func":f01ms_f01_moving_average_systems_ma_skew_60d_jerk_v148_signal},
"f01ms_f01_moving_average_systems_ma_kurt_60d_jerk_v149_signal":{"inputs":["closeadj"],"func":f01ms_f01_moving_average_systems_ma_kurt_60d_jerk_v149_signal},
"f01ms_f01_moving_average_systems_ema_acceleration_30d_jerk_v150_signal":{"inputs":["closeadj"],"func":f01ms_f01_moving_average_systems_ema_acceleration_30d_jerk_v150_signal},
}
def _synthetic_inputs(n=800,seed=42):
    rng=np.random.default_rng(seed)
    seg=n//4
    rest=n-3*seg
    ret=np.concatenate([
        rng.normal(0.0012,0.011,seg),
        rng.normal(-0.0005,0.018,seg),
        rng.normal(-0.0010,0.014,seg),
        rng.normal(0.0008,0.012,rest),
    ])
    close=50.0*np.exp(np.cumsum(ret))
    adj_drift=rng.normal(0.0,0.0003,size=n).cumsum()
    closeadj=close*np.exp(adj_drift)
    intraday=rng.normal(0.0,0.008,size=n)
    open_=close*np.exp(-intraday*0.5)
    high=np.maximum(close,open_)*np.exp(np.abs(rng.normal(0.0,0.006,size=n)))
    low=np.minimum(close,open_)*np.exp(-np.abs(rng.normal(0.0,0.006,size=n)))
    volume=rng.lognormal(mean=13.0,sigma=0.6,size=n)
    idx=pd.RangeIndex(n)
    return pd.DataFrame({
        "open":pd.Series(open_,index=idx,dtype=float),
        "high":pd.Series(high,index=idx,dtype=float),
        "low":pd.Series(low,index=idx,dtype=float),
        "close":pd.Series(close,index=idx,dtype=float),
        "closeadj":pd.Series(closeadj,index=idx,dtype=float),
        "volume":pd.Series(volume,index=idx,dtype=float),
    })
def _self_test():
    df=_synthetic_inputs(n=800,seed=42)
    results={}
    for name,entry in f01_moving_average_systems_jerk_001_150_REGISTRY.items():
        args=[df[col] for col in entry["inputs"]]
        out=entry["func"](*args)
        assert isinstance(out,pd.Series),f"{name}: not a Series"
        assert len(out)==len(df),f"{name}: length mismatch"
        clean=out.dropna()
        assert len(clean)>0,f"{name}: all NaN"
        assert float(clean.std())>0.0 or clean.nunique()>1,f"{name}: constant/all-zero"
        results[name]=out
    warm=252
    coverage_ok=sum(1 for s in results.values() if s.iloc[warm:].isna().mean()<0.5)
    frac=coverage_ok/len(results)
    assert frac>=0.80,f"NaN-coverage too low: {frac:.2%} have <50% NaN after warm-up"
    aligned=pd.concat({n:results[n] for n in results},axis=1).iloc[warm:]
    aligned=aligned.replace([np.inf,-np.inf],np.nan)
    corr=aligned.corr(min_periods=50).abs()
    np.fill_diagonal(corr.values,0.0)
    max_corr=float(corr.max().max())
    if max_corr>0.95:
        print(f"FAILING max |corr| = {max_corr:.4f}. Top pairs:")
        for i,a in enumerate(corr.columns):
            for j,b in enumerate(corr.columns):
                if j>i and corr.iloc[i,j]>0.94:
                    print(f"  {a}  vs  {b}  ->  {corr.iloc[i,j]:.4f}")
    assert max_corr<=0.95+1e-9,f"max pairwise |corr|={max_corr:.4f} exceeds 0.95"
    print(f"OK jerk_001_150: {len(results)} features, max |corr|={max_corr:.4f}, coverage_ok={frac:.2%}")
if __name__=="__main__":
    _self_test()
