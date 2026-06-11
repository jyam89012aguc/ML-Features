"""f17_volatility_regime jerk features 001-150 (2nd derivative). Inline base formulas, diff(k) per ROC bracket."""
from __future__ import annotations
import numpy as np
import pandas as pd
_INF=[np.inf,-np.inf]
def _j(b,k):return b-2.0*b.shift(k)+b.shift(2*k)

def _vol(s,n):
    return np.log(s/s.shift(1)).rolling(n,min_periods=n).std()

def _rank_mp(x,mp):
    if not np.isfinite(x[-1]):return np.nan
    y=x[~np.isnan(x)]
    if len(y)<mp:return np.nan
    return float(np.mean(y[:-1]<x[-1]))
def _R15(x):return _rank_mp(x,15)
def _R30(x):return _rank_mp(x,30)
def _R40(x):return _rank_mp(x,40)
def _R50(x):return _rank_mp(x,50)
def _R60(x):return _rank_mp(x,60)
def _R100(x):return _rank_mp(x,100)
def _qi(x,p,mp,op):
    if not np.isfinite(x[-1]) or len(x[~np.isnan(x)])<mp:return np.nan
    y=x[~np.isnan(x)]; th=np.quantile(y[:-1],p)
    return 1.0 if (op=='>' and x[-1]>th) or (op=='>=' and x[-1]>=th) or (op=='<' and x[-1]<th) or (op=='<=' and x[-1]<=th) else 0.0
def _Q4(x):return _qi(x,0.75,50,'>=')
def _Q4S(x):return _qi(x,0.75,50,'>')
def _Q1(x):return _qi(x,0.25,50,'<=')
def _Q1S(x):return _qi(x,0.25,50,'<')
def _P90(x):return _qi(x,0.9,50,'>')
def _P10(x):return _qi(x,0.1,50,'<')
def _TC(x):
    if not np.isfinite(x[-1]) or len(x[~np.isnan(x)])<50:return np.nan
    y=x[~np.isnan(x)]
    a,b=np.quantile(y[:-1],[1/3.0,2/3.0])
    v0=x[-1]
    return 1.0 if v0<a else (2.0 if v0<b else 3.0)
def _BS(x):
    idx=np.where(x>0.5)[0]
    return float(len(x)) if idx.size==0 else float(len(x)-1-idx[-1])
def _bucket(x,edges,mp):
    if not np.isfinite(x[-1]) or len(x[~np.isnan(x)])<mp:return np.nan
    y=x[~np.isnan(x)]
    qs=np.quantile(y[:-1],edges)
    v0=x[-1]; b=1.0
    for q in qs:
        if v0>q: b += 1.0
    return float(b)
def _BK4(x):return _bucket(x,[0.25,0.5,0.75],50)
def _BK5(x):return _bucket(x,[0.2,0.4,0.6,0.8],60)
def _BK10(x):return _bucket(x,np.arange(1,10)/10.0,60)
def _MAD(x):return float(np.mean(np.abs(x-np.mean(x))))
def _streak_eq_last(x):
    cur=x[-1]
    if not np.isfinite(cur):return np.nan
    c=0
    for w in x[::-1]:
        if w==cur: c += 1
        else: break
    return float(c)
def _consec_above(x):
    c=0
    for w in x[::-1]:
        if not np.isfinite(w):return np.nan
        if w>0.5: c += 1
        else: break
    return float(c)
def _maxrun_above(x):
    if not np.all(np.isfinite(x)):return np.nan
    best=0; cur=0
    for w in x:
        if w>0.5:
            cur += 1
            if cur>best: best=cur
        else: cur=0
    return float(best)
def f17vr_f17_volatility_regime_volquartile_21on252_jerk_v001_signal(closeadj):b=_vol(closeadj,21).rolling(252,60).apply(_BK4,raw=True);return _j(b,63).replace(_INF,np.nan)
def f17vr_f17_volatility_regime_quintile_chg_ind_21on252_jerk_v002_signal(closeadj):
    qn=_vol(closeadj,21).rolling(252,60).apply(_BK5,raw=True); b=np.sign(qn-qn.shift(5));return _j(b,63).replace(_INF,np.nan)
def _BK10_40(x):return _bucket(x,np.arange(1,10)/10.0,40)
def f17vr_f17_volatility_regime_decile_absret_120d_jerk_v003_signal(close):
    b=np.log(close/close.shift(1)).abs().rolling(120,40).apply(_BK10_40,raw=True);return _j(b,21).replace(_INF,np.nan)
def f17vr_f17_volatility_regime_volquartile1_ind_21d_jerk_v004_signal(closeadj):b=_vol(closeadj,21).rolling(252,60).apply(_Q1,raw=True);return _j(b,63).replace(_INF,np.nan)
def f17vr_f17_volatility_regime_volquartile4_ind_21d_jerk_v005_signal(closeadj):b=_vol(closeadj,21).rolling(252,60).apply(_Q4,raw=True);return _j(b,63).replace(_INF,np.nan)
def _quin(p):
    return np.floor(p*5.0).clip(0,4)+1.0
def f17vr_f17_volatility_regime_multih_quintile_5_21_63_jerk_v006_signal(closeadj):
    p5=_vol(closeadj,5).rolling(252,60).apply(_R60,raw=True)
    p21=_vol(closeadj,21).rolling(252,60).apply(_R60,raw=True)
    p63=_vol(closeadj,63).rolling(252,60).apply(_R60,raw=True)
    b=(_quin(p5)+_quin(p21)+_quin(p63));return _j(b,63).replace(_INF,np.nan)
def f17vr_f17_volatility_regime_vol21_over_med252_jerk_v007_signal(closeadj):
    v=_vol(closeadj,21); med=v.rolling(252,60).median(); b=(v/med.replace(0.0,np.nan));return _j(b,63).replace(_INF,np.nan)
def f17vr_f17_volatility_regime_volz_21on252_jerk_v008_signal(closeadj):
    v=_vol(closeadj,21); mu=v.rolling(252,60).mean(); sd=v.rolling(252,60).std(); b=((v-mu)/sd.replace(0.0,np.nan));return _j(b,63).replace(_INF,np.nan)
def f17vr_f17_volatility_regime_volpctrank_21on120_jerk_v009_signal(closeadj):b=_vol(closeadj,21).rolling(120,30).apply(_R30,raw=True);return _j(b,21).replace(_INF,np.nan)
def f17vr_f17_volatility_regime_volpctrank_42on500_jerk_v010_signal(closeadj):b=_vol(closeadj,42).rolling(500,100).apply(_R100,raw=True);return _j(b,63).replace(_INF,np.nan)
def f17vr_f17_volatility_regime_volpct_largeret_42d_jerk_v011_signal(close):
    a=np.log(close/close.shift(1)).abs(); med=a.rolling(42,20).median(); flag=(a>2.0*med).astype(float).where(~a.isna() & ~med.isna()); b=flag.rolling(42,20).mean();return _j(b,10).replace(_INF,np.nan)
def _frac_last(x):
    if not np.isfinite(x[-1]):return np.nan
    return float(np.mean(x==x[-1]))
def f17vr_f17_volatility_regime_regimestab_frac_60d_jerk_v012_signal(closeadj):
    reg=_vol(closeadj,21).rolling(252,60).apply(_TC,raw=True)
    b=reg.rolling(60,30).apply(_frac_last,raw=True);return _j(b,21).replace(_INF,np.nan)
def f17vr_f17_volatility_regime_transitioncount_90d_jerk_v013_signal(closeadj):
    reg=_vol(closeadj,21).rolling(252,60).apply(_TC,raw=True); chg=(reg != reg.shift(1)).astype(float).where(~reg.isna() & ~reg.shift(1).isna()); b=chg.rolling(90,30).sum();return _j(b,21).replace(_INF,np.nan)
def f17vr_f17_volatility_regime_volexpansion_5m63_jerk_v014_signal(closeadj):b=(_vol(closeadj,5)-_vol(closeadj,63));return _j(b,21).replace(_INF,np.nan)
def f17vr_f17_volatility_regime_streak_currentregime_60d_jerk_v015_signal(closeadj):
    reg=_vol(closeadj,21).rolling(252,60).apply(_TC,raw=True); b=reg.rolling(60,20).apply(_streak_eq_last,raw=True);return _j(b,21).replace(_INF,np.nan)
def f17vr_f17_volatility_regime_vol_HLrange_pct_42d_jerk_v016_signal(closeadj):
    v=_vol(closeadj,21); hi=v.rolling(42,20).max(); lo=v.rolling(42,20).min(); b=((hi-lo)/hi.replace(0.0,np.nan));return _j(b,10).replace(_INF,np.nan)
def f17vr_f17_volatility_regime_daysinhighvol_120d_jerk_v017_signal(closeadj):
    ind=_vol(closeadj,21).rolling(252,60).apply(_Q4,raw=True); b=ind.rolling(120,40).sum();return _j(b,21).replace(_INF,np.nan)
def f17vr_f17_volatility_regime_ret_x_highvol_ind_jerk_v019_signal(closeadj):
    r=np.log(closeadj/closeadj.shift(21)); ind=_vol(closeadj,21).rolling(252,60).apply(_Q4,raw=True); b=(r*ind);return _j(b,63).replace(_INF,np.nan)
def f17vr_f17_volatility_regime_ret_x_lowvol_ind_jerk_v020_signal(closeadj):
    r=np.log(closeadj/closeadj.shift(21)); ind=_vol(closeadj,21).rolling(252,60).apply(_Q1,raw=True); b=(r*ind);return _j(b,63).replace(_INF,np.nan)
def f17vr_f17_volatility_regime_sharpe_42d_currentvol_jerk_v021_signal(closeadj):
    r=np.log(closeadj/closeadj.shift(1)); sr=r.rolling(42,20).mean()/r.rolling(42,20).std().replace(0.0,np.nan); qb=_vol(closeadj,21).rolling(252,60).apply(_BK4,raw=True); b=(sr*qb);return _j(b,21).replace(_INF,np.nan)

def _ar1_resid(x):
    if not np.all(np.isfinite(x)):return np.nan
    y=x[1:]; yl=x[:-1]
    muY=y.mean(); muL=yl.mean()
    cov=np.sum((yl-muL)*(y-muY))
    var=np.sum((yl-muL)**2)
    if var==0.0:return np.nan
    b=cov/var; a=muY-b*muL
    return float(y[-1]-(a+b*yl[-1]))
def f17vr_f17_volatility_regime_volresid_AR1_120d_jerk_v022_signal(closeadj):b=_vol(closeadj,21).rolling(120,40).apply(_ar1_resid,raw=True);return _j(b,21).replace(_INF,np.nan)
def f17vr_f17_volatility_regime_volgap_pct_42on252_jerk_v023_signal(closeadj):
    v=_vol(closeadj,42); med=v.rolling(252,60).median(); b=((v-med)/med.replace(0.0,np.nan));return _j(b,63).replace(_INF,np.nan)
def f17vr_f17_volatility_regime_highvolon_p90_jerk_v024_signal(closeadj):b=_vol(closeadj,21).rolling(252,60).apply(_P90,raw=True);return _j(b,63).replace(_INF,np.nan)
def f17vr_f17_volatility_regime_lowvolon_p10_jerk_v025_signal(closeadj):b=_vol(closeadj,21).rolling(252,60).apply(_P10,raw=True);return _j(b,63).replace(_INF,np.nan)
def f17vr_f17_volatility_regime_expanding_state_42d_jerk_v026_signal(closeadj):
    v=_vol(closeadj,21); mu=v.rolling(42,20).mean(); b=(v>mu).astype(float).where(~v.isna() & ~mu.isna());return _j(b,10).replace(_INF,np.nan)
def _ext_p15p85(x):
    if not np.isfinite(x[-1]) or len(x[~np.isnan(x)])<40:return np.nan
    y=x[~np.isnan(x)]
    return 1.0 if (x[-1]<np.quantile(y[:-1],0.15) or x[-1]>np.quantile(y[:-1],0.85)) else 0.0
def _cl_clusters(x):
    c=0; prev=0.0
    for w in x:
        if not np.isfinite(w):return np.nan
        if w>0.5 and prev<=0.5: c += 1
        prev=w
    return float(c)
def _avg_runlen(x):
    runs=[]; cur=x[0]; cnt=1
    for w in x[1:]:
        if not np.isfinite(w) or not np.isfinite(cur):return np.nan
        if w==cur: cnt += 1
        else: runs.append(cnt); cur=w; cnt=1
    runs.append(cnt)
    return float(np.mean(runs))
def f17vr_f17_volatility_regime_extreme_state_120d_jerk_v027_signal(closeadj):
    b=_vol(closeadj,21).rolling(120,40).apply(_ext_p15p85,raw=True);return _j(b,21).replace(_INF,np.nan)
def f17vr_f17_volatility_regime_highvol_clusters_120d_jerk_v028_signal(closeadj):
    ind=_vol(closeadj,21).rolling(252,60).apply(_P90,raw=True)
    b=ind.rolling(120,60).apply(_cl_clusters,raw=True);return _j(b,21).replace(_INF,np.nan)
def f17vr_f17_volatility_regime_runlen_currentreg_120d_jerk_v029_signal(closeadj):
    reg=_vol(closeadj,21).rolling(252,60).apply(_TC,raw=True)
    b=reg.rolling(120,60).apply(_avg_runlen,raw=True);return _j(b,63).replace(_INF,np.nan)
def f17vr_f17_volatility_regime_ewmavoldiff_94m97_jerk_v031_signal(closeadj):
    r=np.log(closeadj/closeadj.shift(1)); fast=np.sqrt(r.pow(2).ewm(alpha=0.06,adjust=False,min_periods=20).mean()); slow=np.sqrt(r.pow(2).ewm(alpha=0.03,adjust=False,min_periods=20).mean()); b=np.log(fast/slow);return _j(b,21).replace(_INF,np.nan)
def f17vr_f17_volatility_regime_absret_surprise_60d_jerk_v032_signal(close):
    a=np.log(close/close.shift(1)).abs(); b=(a-a.rolling(60,60).mean());return _j(b,21).replace(_INF,np.nan)
def f17vr_f17_volatility_regime_voljump_ind_21d_jerk_v033_signal(closeadj):
    v=_vol(closeadj,21); d=v.diff(1); sd=d.rolling(60,30).std(); b=(d>2.0*sd).astype(float).where(~d.isna() & ~sd.isna());return _j(b,10).replace(_INF,np.nan)
def f17vr_f17_volatility_regime_dayssince_volspike_120d_jerk_v034_signal(closeadj):
    v=_vol(closeadj,21); d=v.diff(1); sd=d.rolling(60,30).std(); flag=(d>2.0*sd).astype(float).where(~d.isna() & ~sd.isna()); b=flag.rolling(120,40).apply(_BS,raw=True);return _j(b,21).replace(_INF,np.nan)

def _detr_sigmoid(x):
    if not np.all(np.isfinite(x)):return np.nan
    n=len(x); t=np.arange(n,dtype=float)
    muT=t.mean(); muX=x.mean()
    cov=np.sum((t-muT)*(x-muX))
    var=np.sum((t-muT)**2)
    if var==0.0:return np.nan
    b=cov/var; a=muX-b*muT
    resid_last=x[-1]-(a+b*t[-1])
    mad=float(np.mean(np.abs(x-np.mean(x))))
    if mad==0.0:return np.nan
    z=resid_last/mad
    return float(1.0/(1.0+np.exp(-max(min(z,30.0),-30.0))))
def f17vr_f17_volatility_regime_sigmoid_volresid_120d_jerk_v035_signal(closeadj):b=_vol(closeadj,21).rolling(120,40).apply(_detr_sigmoid,raw=True);return _j(b,21).replace(_INF,np.nan)
def f17vr_f17_volatility_regime_arctan_volcurv_60d_jerk_v036_signal(closeadj):
    v=_vol(closeadj,21); curv=v-2.0*v.shift(10)+v.shift(20); sd=v.rolling(60,20).std(); z=curv/sd.replace(0.0,np.nan); b=np.arctan(3.0*z.clip(-30.0,30.0));return _j(b,21).replace(_INF,np.nan)
def f17vr_f17_volatility_regime_tanh_volsurprise_42d_jerk_v037_signal(closeadj):
    v=_vol(closeadj,21); mu=v.rolling(42,20).mean(); sd=v.rolling(42,20).std(); s=(v-mu)/sd.replace(0.0,np.nan); b=np.tanh(s.clip(-30.0,30.0));return _j(b,10).replace(_INF,np.nan)
def f17vr_f17_volatility_regime_dayssince_enter_highvol_252d_jerk_v038_signal(closeadj):
    ind=_vol(closeadj,21).rolling(252,60).apply(_P90,raw=True); enter=((ind>0.5) & (ind.shift(1)<=0.5)).astype(float).where(~ind.isna() & ~ind.shift(1).isna()); b=enter.rolling(252,60).apply(_BS,raw=True);return _j(b,63).replace(_INF,np.nan)
def f17vr_f17_volatility_regime_dayssince_exit_lowvol_252d_jerk_v039_signal(closeadj):
    ind=_vol(closeadj,21).rolling(252,60).apply(_P10,raw=True); exit_=((ind<0.5) & (ind.shift(1)>=0.5)).astype(float).where(~ind.isna() & ~ind.shift(1).isna()); b=exit_.rolling(252,60).apply(_BS,raw=True);return _j(b,63).replace(_INF,np.nan)
def f17vr_f17_volatility_regime_regimewidth_p10p90_252d_jerk_v040_signal(closeadj):
    v=_vol(closeadj,21); p90=v.rolling(252,60).quantile(0.9); p10=v.rolling(252,60).quantile(0.1); med=v.rolling(252,60).median(); b=((p90-p10)/med.replace(0.0,np.nan));return _j(b,63).replace(_INF,np.nan)
def _cons_sign(x):
    if not np.all(np.isfinite(x)) or len(x)<10:return np.nan
    m=float(np.sign(np.sum(x)))
    if m==0.0:return 0.5
    return float(np.mean(x==m))
def f17vr_f17_volatility_regime_volsign_consistency_42d_jerk_v041_signal(closeadj):
    s=np.sign(_vol(closeadj,21).diff(1))
    b=s.rolling(42,20).apply(_cons_sign,raw=True);return _j(b,21).replace(_INF,np.nan)
def f17vr_f17_volatility_regime_volofvol_60d_jerk_v042_signal(closeadj):b=_vol(closeadj,21).rolling(60,30).std();return _j(b,10).replace(_INF,np.nan)

def _corr_t(x):
    if not np.all(np.isfinite(x)):return np.nan
    n=len(x); t=np.arange(n,dtype=float)
    muT=t.mean(); muX=x.mean()
    cov=np.sum((t-muT)*(x-muX))
    vt=np.sum((t-muT)**2); vx=np.sum((x-muX)**2)
    if vt==0.0 or vx==0.0:return np.nan
    return float(cov/np.sqrt(vt*vx))
def f17vr_f17_volatility_regime_vol_corrwith_time_60d_jerk_v043_signal(closeadj):b=_vol(closeadj,21).rolling(60,20).apply(_corr_t,raw=True);return _j(b,21).replace(_INF,np.nan)
def f17vr_f17_volatility_regime_consec_vol_uptick_60d_jerk_v044_signal(closeadj):
    d=_vol(closeadj,21).diff(1); s=(d>0).astype(float).where(~d.isna()); b=s.rolling(60,20).apply(_maxrun_above,raw=True);return _j(b,10).replace(_INF,np.nan)
def f17vr_f17_volatility_regime_vol_zerocrossings_60d_jerk_v045_signal(closeadj):
    v=_vol(closeadj,21); med60=v.rolling(60,20).median(); d=v-med60; sgn=np.sign(d); cross=(sgn != sgn.shift(1)).astype(float).where(~sgn.isna() & ~sgn.shift(1).isna()); b=cross.rolling(60,20).sum();return _j(b,21).replace(_INF,np.nan)
def _D10(x):
    if not np.isfinite(x[-1]) or len(x[~np.isnan(x)])<50:return np.nan
    y=x[~np.isnan(x)]
    return float(np.floor(np.mean(y[:-1]<x[-1])*10.0))


def f17vr_f17_volatility_regime_decile_transitions_90d_jerk_v046_signal(closeadj):
    dc=_vol(closeadj,21).rolling(252,60).apply(_D10,raw=True); chg=(dc.diff().abs()>1.0).astype(float).where(~dc.isna() & ~dc.shift(1).isna()); b=chg.rolling(90,30).sum();return _j(b,21).replace(_INF,np.nan)
def f17vr_f17_volatility_regime_volcurvature_15d_jerk_v047_signal(closeadj):
    v=_vol(closeadj,21); b=(v-2.0*v.shift(7)+v.shift(14));return _j(b,10).replace(_INF,np.nan)
def f17vr_f17_volatility_regime_nhorizons_inhigh_5to63_jerk_v048_signal(closeadj):
    out=pd.Series(0.0,index=closeadj.index,dtype=float)
    mask=pd.Series(True,index=closeadj.index)
    for h in (5,10,21,42,63):
        ind=_vol(closeadj,h).rolling(252,60).apply(_Q4S,raw=True)
        out=out+ind.fillna(0.0); mask=mask & ~ind.isna()
    b=out.where(mask);return _j(b,63).replace(_INF,np.nan)
def f17vr_f17_volatility_regime_nhorizons_inlow_5to63_jerk_v049_signal(closeadj):
    out=pd.Series(0.0,index=closeadj.index,dtype=float)
    mask=pd.Series(True,index=closeadj.index)
    for h in (5,10,21,42,63):
        ind=_vol(closeadj,h).rolling(252,60).apply(_Q1S,raw=True)
        out=out+ind.fillna(0.0); mask=mask & ~ind.isna()
    b=out.where(mask);return _j(b,63).replace(_INF,np.nan)
def f17vr_f17_volatility_regime_medianvol_horizons_jerk_v050_signal(closeadj):
    cols=[_vol(closeadj,h).rolling(252,60).apply(_R50,raw=True) for h in (10,21,42,63)]; b=pd.concat(cols,axis=1).median(axis=1);return _j(b,63).replace(_INF,np.nan)
def f17vr_f17_volatility_regime_volpctrange_horizons_jerk_v051_signal(closeadj):
    cols=[_vol(closeadj,h).rolling(252,60).apply(_R50,raw=True) for h in (10,21,42,63)]; M=pd.concat(cols,axis=1); b=(M.max(axis=1)-M.min(axis=1));return _j(b,63).replace(_INF,np.nan)
def _BK4_40(x):return _bucket(x,[0.25,0.5,0.75],40)
def _BK5_100(x):return _bucket(x,[0.2,0.4,0.6,0.8],100)
def f17vr_f17_volatility_regime_volquartile_5on120_jerk_v052_signal(close):b=_vol(close,5).rolling(120,40).apply(_BK4_40,raw=True);return _j(b,21).replace(_INF,np.nan)
def f17vr_f17_volatility_regime_volquintile_63on500_jerk_v053_signal(closeadj):b=_vol(closeadj,63).rolling(500,120).apply(_BK5_100,raw=True);return _j(b,63).replace(_INF,np.nan)
def f17vr_f17_volatility_regime_volupshocks_count_42d_jerk_v054_signal(closeadj):
    v=_vol(closeadj,21); d=v.diff(1); mad=d.abs().rolling(60,20).median(); flag=(d>mad).astype(float).where(~d.isna() & ~mad.isna()); b=flag.rolling(42,20).sum();return _j(b,21).replace(_INF,np.nan)
def f17vr_f17_volatility_regime_volabsdev_med_252d_jerk_v055_signal(closeadj):
    v=_vol(closeadj,21); med=v.rolling(252,60).median(); b=(v-med).abs();return _j(b,63).replace(_INF,np.nan)
def f17vr_f17_volatility_regime_vol_skew_ratio_42d_jerk_v056_signal(closeadj):
    v=_vol(closeadj,21); p10=v.rolling(42,20).quantile(0.1); p50=v.rolling(42,20).median(); p90=v.rolling(42,20).quantile(0.9); b=((p90-p50)/(p50-p10).replace(0.0,np.nan));return _j(b,10).replace(_INF,np.nan)
def f17vr_f17_volatility_regime_volentry_count_p75_120d_jerk_v057_signal(closeadj):
    ind=_vol(closeadj,21).rolling(252,60).apply(_Q4,raw=True); enter=((ind>0.5) & (ind.shift(1)<=0.5)).astype(float).where(~ind.isna() & ~ind.shift(1).isna()); b=enter.rolling(120,40).sum();return _j(b,21).replace(_INF,np.nan)
def f17vr_f17_volatility_regime_volpctrank_diff_21_42_jerk_v058_signal(closeadj):
    p21=_vol(closeadj,21).rolling(252,60).apply(_R50,raw=True); p42=_vol(closeadj,42).rolling(252,60).apply(_R50,raw=True); b=(p21-p42);return _j(b,63).replace(_INF,np.nan)
def f17vr_f17_volatility_regime_ret_x_volz_42d_jerk_v059_signal(closeadj):
    r=np.log(closeadj/closeadj.shift(21)); v=_vol(closeadj,21); mu=v.rolling(120,40).mean(); sd=v.rolling(120,40).std(); z=(v-mu)/sd.replace(0.0,np.nan); b=(r*z);return _j(b,63).replace(_INF,np.nan)
def f17vr_f17_volatility_regime_voljump_freq_252d_jerk_v060_signal(closeadj):
    v=_vol(closeadj,21); d=v.diff(1); sd=d.rolling(60,30).std(); flag=(d>2.0*sd).astype(float).where(~d.isna() & ~sd.isna()); b=flag.rolling(252,80).sum();return _j(b,63).replace(_INF,np.nan)
def f17vr_f17_volatility_regime_signdiff_vol5_vol21_jerk_v061_signal(close):b=np.sign(_vol(close,5)-_vol(close,21));return _j(b,5).replace(_INF,np.nan)

def _normslope(x):
    n=len(x); t=np.arange(n,dtype=float)
    mean_t=t.mean(); mean_x=x.mean()
    cov=np.sum((t-mean_t)*(x-mean_x))
    var=np.sum((t-mean_t)**2)
    if var==0.0 or not np.isfinite(mean_x) or mean_x==0.0:return np.nan
    return float((cov/var)/mean_x)
def f17vr_f17_volatility_regime_vol_drift_30d_jerk_v062_signal(closeadj):b=_vol(closeadj,21).rolling(30,15).apply(_normslope,raw=True);return _j(b,10).replace(_INF,np.nan)
def f17vr_f17_volatility_regime_volupcross_med_252d_jerk_v063_signal(closeadj):
    v=_vol(closeadj,21); med=v.rolling(252,60).median(); above=(v>med).astype(float).where(~v.isna() & ~med.isna()); cross=((above>0.5) & (above.shift(1)<=0.5)).astype(float).where(~above.isna() & ~above.shift(1).isna()); b=cross.rolling(120,40).sum();return _j(b,63).replace(_INF,np.nan)
def f17vr_f17_volatility_regime_volstreak_above_med_60d_jerk_v064_signal(closeadj):
    v=_vol(closeadj,21); med=v.rolling(252,60).median(); above=(v>med).astype(float).where(~v.isna() & ~med.isna()); b=above.rolling(60,30).apply(_consec_above,raw=True);return _j(b,21).replace(_INF,np.nan)
def _maxrun_eqlast(x):
    cur=x[-1]
    if not np.isfinite(cur):return np.nan
    runs=[]; rcur=x[0]; cnt=1
    for w in x[1:]:
        if not np.isfinite(w):return np.nan
        if w==rcur: cnt += 1
        else:
            if rcur==cur: runs.append(cnt)
            rcur=w; cnt=1
    if rcur==cur: runs.append(cnt)
    return 0.0 if not runs else float(max(runs))
def f17vr_f17_volatility_regime_max_time_in_currentreg_180d_jerk_v065_signal(closeadj):
    reg=_vol(closeadj,21).rolling(252,60).apply(_TC,raw=True)
    b=reg.rolling(180,60).apply(_maxrun_eqlast,raw=True);return _j(b,63).replace(_INF,np.nan)
def f17vr_f17_volatility_regime_kurt_vol21_60d_jerk_v066_signal(closeadj):b=_vol(closeadj,21).rolling(60,30).kurt();return _j(b,21).replace(_INF,np.nan)
def f17vr_f17_volatility_regime_skew_vol21_60d_jerk_v067_signal(closeadj):b=_vol(closeadj,21).rolling(60,30).skew();return _j(b,10).replace(_INF,np.nan)
def f17vr_f17_volatility_regime_madstd_vol21_60d_jerk_v068_signal(closeadj):
    v=_vol(closeadj,21); mad=v.rolling(60,30).apply(_MAD,raw=True); sd=v.rolling(60,30).std(); b=(mad/sd.replace(0.0,np.nan));return _j(b,21).replace(_INF,np.nan)
def f17vr_f17_volatility_regime_signagree_p75_5_21_63_jerk_v069_signal(closeadj):
    cols_hi=[]; cols_lo=[]
    for h in (5,21,63):
        v=_vol(closeadj,h)
        cols_hi.append(v.rolling(252,60).apply(_Q4S,raw=True))
        cols_lo.append(v.rolling(252,60).apply(_Q1S,raw=True))
    H=pd.concat(cols_hi,axis=1).sum(axis=1)
    L=pd.concat(cols_lo,axis=1).sum(axis=1)
    out=pd.Series(0.0,index=closeadj.index,dtype=float)
    out=out.where(~H.isna() & ~L.isna())
    out=out.mask(H>=3.0,1.0).mask(L>=3.0,-1.0)
    b=out;return _j(b,63).replace(_INF,np.nan)
def f17vr_f17_volatility_regime_volstability_iqr_120d_jerk_v070_signal(closeadj):
    v=_vol(closeadj,21); q1=v.rolling(120,40).quantile(0.25); q3=v.rolling(120,40).quantile(0.75); med=v.rolling(120,40).median(); b=((q3-q1)/med.replace(0.0,np.nan));return _j(b,21).replace(_INF,np.nan)
def f17vr_f17_volatility_regime_volrank_diff_short_long_jerk_v072_signal(closeadj):
    a=_vol(closeadj,5).rolling(120,40).apply(_R40,raw=True); b=_vol(closeadj,63).rolling(500,120).apply(_R100,raw=True); b=(a-b);return _j(b,63).replace(_INF,np.nan)
def _dsx(x,mp,fn):
    if not np.isfinite(x[-1]) or len(x[~np.isnan(x)])<mp:return np.nan
    return float(len(x)-1-int(fn(x)))
def _dsmin(x):return _dsx(x,50,np.argmin)
def _dsmax(x):return _dsx(x,50,np.argmax)
def f17vr_f17_volatility_regime_dayssince_minvol_252d_jerk_v073_signal(closeadj):
    b=_vol(closeadj,21).rolling(252,60).apply(_dsmin,raw=True);return _j(b,63).replace(_INF,np.nan)
def f17vr_f17_volatility_regime_dayssince_maxvol_252d_jerk_v074_signal(closeadj):
    b=_vol(closeadj,21).rolling(252,60).apply(_dsmax,raw=True);return _j(b,63).replace(_INF,np.nan)
def f17vr_f17_volatility_regime_volminusewma_94_jerk_v075_signal(closeadj):
    v21=_vol(closeadj,21); r=np.log(closeadj/closeadj.shift(1)); ewmav=np.sqrt(r.pow(2).ewm(alpha=0.06,adjust=False,min_periods=20).mean()); b=(np.log(v21)-np.log(ewmav));return _j(b,21).replace(_INF,np.nan)
def f17vr_f17_volatility_regime_parkvol_quartile_21on252_jerk_v076_signal(high,low,closeadj):
    r2=(np.log(high/low) ** 2)/(4.0*np.log(2.0)); pv=np.sqrt(r2.rolling(21,21).mean()); b=pv.rolling(252,60).apply(_BK4,raw=True);return _j(b,63).replace(_INF,np.nan)
def f17vr_f17_volatility_regime_HLrange_z_42d_jerk_v077_signal(high,low):
    r=np.log(high/low); m21=r.rolling(21,21).mean(); mu=m21.rolling(252,60).mean(); sd=m21.rolling(252,60).std(); b=((m21-mu)/sd.replace(0.0,np.nan));return _j(b,63).replace(_INF,np.nan)
def _dsmax60(x):return _dsx(x,60,np.argmax)
def f17vr_f17_volatility_regime_HLrange_dayssincemax_180d_jerk_v078_signal(high,low):
    b=np.log(high/low).rolling(180,60).apply(_dsmax60,raw=True);return _j(b,63).replace(_INF,np.nan)
def f17vr_f17_volatility_regime_gkvol_p75_ind_30d_jerk_v079_signal(open_,high,low,close):
    rs=0.5*(np.log(high/low) ** 2)-(2.0*np.log(2.0)-1.0)*(np.log(close/open_) ** 2); gk=np.sqrt(rs.rolling(20,20).mean()); b=gk.rolling(252,60).apply(_Q4S,raw=True);return _j(b,63).replace(_INF,np.nan)
def f17vr_f17_volatility_regime_rangetonormal_42d_jerk_v080_signal(high,low,closeadj):
    r2=(np.log(high/low) ** 2)/(4.0*np.log(2.0)); pv=np.sqrt(r2.rolling(21,21).mean()); cv=np.log(closeadj/closeadj.shift(1)).rolling(21,21).std(); b=np.log(pv/cv.replace(0.0,np.nan));return _j(b,10).replace(_INF,np.nan)
def f17vr_f17_volatility_regime_downvol_p90_42d_jerk_v081_signal(closeadj):
    r=np.log(closeadj/closeadj.shift(1)); dv=np.sqrt(r.clip(upper=0.0).pow(2).rolling(42,42).mean()); b=dv.rolling(252,60).apply(_P90,raw=True);return _j(b,63).replace(_INF,np.nan)
def f17vr_f17_volatility_regime_upvol_decile_252d_jerk_v082_signal(closeadj):
    r=np.log(closeadj/closeadj.shift(1)); uv=np.sqrt(r.clip(lower=0.0).pow(2).rolling(42,42).mean()); b=uv.rolling(252,60).apply(_BK10,raw=True);return _j(b,63).replace(_INF,np.nan)
def f17vr_f17_volatility_regime_downup_voldiff_z_42d_jerk_v083_signal(closeadj):
    r=np.log(closeadj/closeadj.shift(1))
    neg=r.clip(upper=0.0)
    pos=r.clip(lower=0.0)
    dv=np.sqrt(neg.pow(2).rolling(42,42).mean())
    uv=np.sqrt(pos.pow(2).rolling(42,42).mean())
    d=dv-uv
    mu=d.rolling(200,60).mean()
    sd=d.rolling(200,60).std()
    b=((d-mu)/sd.replace(0.0,np.nan));return _j(b,21).replace(_INF,np.nan)
def f17vr_f17_volatility_regime_madvol_quintile_21on252_jerk_v084_signal(closeadj):
    r=np.log(closeadj/closeadj.shift(1)); mv=r.rolling(21,21).apply(_MAD,raw=True); b=mv.rolling(252,60).apply(_BK5,raw=True);return _j(b,63).replace(_INF,np.nan)
def f17vr_f17_volatility_regime_madvol_pctrank_42on500_jerk_v085_signal(closeadj):
    r=np.log(closeadj/closeadj.shift(1)); mv=r.rolling(42,42).apply(_MAD,raw=True); b=mv.rolling(500,120).apply(_R100,raw=True);return _j(b,63).replace(_INF,np.nan)
def f17vr_f17_volatility_regime_absret_avg_pctrank_30on252_jerk_v086_signal(closeadj):
    a=np.log(closeadj/closeadj.shift(1)).abs(); m30=a.rolling(30,15).mean(); b=m30.rolling(252,60).apply(_R50,raw=True);return _j(b,63).replace(_INF,np.nan)
def f17vr_f17_volatility_regime_absret_max_pctrank_120d_jerk_v087_signal(closeadj):
    a=np.log(closeadj/closeadj.shift(1)).abs(); mx=a.rolling(10,5).max(); b=mx.rolling(120,40).apply(_R30,raw=True);return _j(b,21).replace(_INF,np.nan)
def _cvar5(x):
    if not np.all(np.isfinite(x)):return np.nan
    tail=x[x<=np.quantile(x,0.05)]
    return float(np.mean(tail)) if tail.size>0 else np.nan
def f17vr_f17_volatility_regime_cvar5_pctrank_42on252_jerk_v088_signal(closeadj):
    c=np.log(closeadj/closeadj.shift(1)).rolling(42,21).apply(_cvar5,raw=True)
    b=c.rolling(252,60).apply(_R50,raw=True);return _j(b,63).replace(_INF,np.nan)
def f17vr_f17_volatility_regime_var5_above_threshold_60d_jerk_v089_signal(closeadj):
    r=np.log(closeadj/closeadj.shift(1)); q5=r.rolling(60,30).quantile(0.05); a=r.abs(); med=a.rolling(60,30).median(); b=(q5<-2.0*med).astype(float).where(~q5.isna() & ~med.isna());return _j(b,10).replace(_INF,np.nan)
def _ent_linspace(x):
    if not np.all(np.isfinite(x)) or len(x)<10:return np.nan
    lo=x.min(); hi=x.max()
    if hi==lo:return 0.0
    cnt,_=np.histogram(x,bins=np.linspace(lo,hi,6))
    p=cnt/cnt.sum(); p=p[p>0]
    return float(-np.sum(p*np.log(p)))
def f17vr_f17_volatility_regime_retentropy_bins_42d_jerk_v090_signal(closeadj):
    b=np.log(closeadj/closeadj.shift(1)).rolling(42,21).apply(_ent_linspace,raw=True);return _j(b,21).replace(_INF,np.nan)
def f17vr_f17_volatility_regime_abs_ret_entropy_60d_jerk_v091_signal(closeadj):
    a=np.log(closeadj/closeadj.shift(1)).abs()
    cv=a.rolling(60,30).std()/a.rolling(60,30).mean().replace(0.0,np.nan)
    med252=a.rolling(252,120).median().replace(0.0,np.nan)
    b=(cv/med252);return _j(b,21).replace(_INF,np.nan)
def f17vr_f17_volatility_regime_post_highvol_60d_jerk_v092_signal(closeadj):
    v=_vol(closeadj,21); mu=v.rolling(252,60).mean(); above=(v>mu).astype(float).where(~v.isna() & ~mu.isna()); b=above.rolling(60,30).mean();return _j(b,21).replace(_INF,np.nan)
def f17vr_f17_volatility_regime_post_highvol_smoothed_30d_jerk_v093_signal(closeadj):
    ind=_vol(closeadj,21).rolling(252,60).apply(_Q4S,raw=True); b=ind.ewm(alpha=0.1,adjust=False,min_periods=20).mean();return _j(b,63).replace(_INF,np.nan)

def _mad_robust(x):
    return float(np.median(np.abs(x-np.median(x))))
def f17vr_f17_volatility_regime_adapt_threshold_ind_84d_jerk_v094_signal(closeadj):
    v=_vol(closeadj,21); med=v.rolling(84,30).median(); mad=v.rolling(84,30).apply(_mad_robust,raw=True); th=med+1.5*mad; b=(v>th).astype(float).where(~v.isna() & ~th.isna());return _j(b,21).replace(_INF,np.nan)
def f17vr_f17_volatility_regime_adapt_low_threshold_84d_jerk_v095_signal(closeadj):
    v=_vol(closeadj,21); med=v.rolling(84,30).median(); mad=v.rolling(84,30).apply(_mad_robust,raw=True); th=med-1.0*mad; b=(v<th).astype(float).where(~v.isna() & ~th.isna());return _j(b,21).replace(_INF,np.nan)
def f17vr_f17_volatility_regime_semiIQR_high_pctrank_60d_jerk_v096_signal(closeadj):
    r=np.log(closeadj/closeadj.shift(1)); u=r.rolling(60,30).quantile(0.9)-r.rolling(60,30).quantile(0.5); b=u.rolling(252,60).apply(_R60,raw=True);return _j(b,63).replace(_INF,np.nan)
def f17vr_f17_volatility_regime_semiIQR_low_pctrank_60d_jerk_v097_signal(closeadj):
    r=np.log(closeadj/closeadj.shift(1)); u=r.rolling(60,30).quantile(0.5)-r.rolling(60,30).quantile(0.1); b=u.rolling(252,60).apply(_R60,raw=True);return _j(b,63).replace(_INF,np.nan)
def f17vr_f17_volatility_regime_kurt_excessflag_42d_jerk_v098_signal(closeadj):
    r=np.log(closeadj/closeadj.shift(1)); k=r.rolling(42,21).kurt(); b=(k>1.5).astype(float).where(~k.isna());return _j(b,10).replace(_INF,np.nan)
def f17vr_f17_volatility_regime_kurtpctrank_42on252_jerk_v099_signal(closeadj):
    r=np.log(closeadj/closeadj.shift(1)); k=r.rolling(42,21).kurt(); b=k.rolling(252,60).apply(_R50,raw=True);return _j(b,63).replace(_INF,np.nan)
def f17vr_f17_volatility_regime_NRcount_4_42d_jerk_v100_signal(high,low):
    rng=high-low; cur_min=rng.rolling(4,4).min(); flag=(rng<=cur_min).astype(float).where(~rng.isna() & ~cur_min.isna()); b=flag.rolling(42,20).sum();return _j(b,10).replace(_INF,np.nan)
def f17vr_f17_volatility_regime_WRcount_4_42d_jerk_v101_signal(high,low):
    rng=high-low; cur_max=rng.rolling(4,4).max(); flag=(rng>=cur_max).astype(float).where(~rng.isna() & ~cur_max.isna()); b=flag.rolling(42,20).sum();return _j(b,21).replace(_INF,np.nan)
def f17vr_f17_volatility_regime_HLavg_z_60d_jerk_v102_signal(high,low):
    rng=(high-low)/((high+low)/2.0); m21=rng.rolling(21,21).mean(); mu=m21.rolling(60,30).mean(); sd=m21.rolling(60,30).std(); b=((m21-mu)/sd.replace(0.0,np.nan));return _j(b,21).replace(_INF,np.nan)
def f17vr_f17_volatility_regime_ewmavol_lam97_jerk_v103_signal(closeadj):
    r=np.log(closeadj/closeadj.shift(1)); b=np.sqrt(r.pow(2).ewm(alpha=0.03,adjust=False,min_periods=20).mean());return _j(b,10).replace(_INF,np.nan)
def f17vr_f17_volatility_regime_ewmavol_decile_94_252d_jerk_v104_signal(closeadj):
    r=np.log(closeadj/closeadj.shift(1)); ev=np.sqrt(r.pow(2).ewm(alpha=0.06,adjust=False,min_periods=20).mean()); b=ev.rolling(252,60).apply(_BK10,raw=True);return _j(b,63).replace(_INF,np.nan)
def _D10_60(x):
    if not np.isfinite(x[-1]) or len(x[~np.isnan(x)])<60:return np.nan
    y=x[~np.isnan(x)]
    return float(np.floor(np.mean(y[:-1]<x[-1])*10.0))
def f17vr_f17_volatility_regime_decile_jumpcount_42d_jerk_v105_signal(closeadj):
    dc=_vol(closeadj,21).rolling(252,60).apply(_D10_60,raw=True)
    jump=(dc.diff().abs()>=3.0).astype(float).where(~dc.isna() & ~dc.shift(1).isna())
    b=jump.rolling(42,20).sum();return _j(b,21).replace(_INF,np.nan)
def f17vr_f17_volatility_regime_volzeroup_count_120d_jerk_v106_signal(closeadj):
    v=_vol(closeadj,21); mu=v.rolling(120,40).mean(); above=(v>mu).astype(float).where(~v.isna() & ~mu.isna()); cross=((above>0.5) & (above.shift(1)<=0.5)).astype(float).where(~above.isna() & ~above.shift(1).isna()); b=cross.rolling(120,40).sum();return _j(b,21).replace(_INF,np.nan)
def f17vr_f17_volatility_regime_avgret_in_high_quart_252d_jerk_v107_signal(closeadj):
    r=np.log(closeadj/closeadj.shift(1)); ind=_vol(closeadj,21).rolling(252,60).apply(_Q4,raw=True); num=(r*ind).rolling(252,60).sum(); den=ind.rolling(252,60).sum(); b=(num/den.replace(0.0,np.nan));return _j(b,63).replace(_INF,np.nan)
def f17vr_f17_volatility_regime_winrate_in_lowvol_252d_jerk_v108_signal(closeadj):
    r=np.log(closeadj/closeadj.shift(1)); ind=_vol(closeadj,21).rolling(252,60).apply(_Q1,raw=True); win=((r>0).astype(float)*ind).rolling(252,60).sum(); cnt=ind.rolling(252,60).sum(); b=(win/cnt.replace(0.0,np.nan));return _j(b,63).replace(_INF,np.nan)
def f17vr_f17_volatility_regime_HLrange_acceleration_30d_jerk_v109_signal(high,low):
    r2=(np.log(high/low) ** 2)/(4.0*np.log(2.0)); pv=np.sqrt(r2.rolling(21,21).mean()); curv=pv-2.0*pv.shift(15)+pv.shift(30); sd=pv.rolling(60,30).std(); z=curv/sd.replace(0.0,np.nan); b=np.tanh(z.clip(-30.0,30.0));return _j(b,21).replace(_INF,np.nan)
def f17vr_f17_volatility_regime_sigmoid_madvol_z_120d_jerk_v110_signal(closeadj):
    r=np.log(closeadj/closeadj.shift(1)); mv=r.rolling(21,21).apply(_MAD,raw=True); mu=mv.rolling(120,40).mean(); sd=mv.rolling(120,40).std(); z=(mv-mu)/sd.replace(0.0,np.nan); b=(1.0/(1.0+np.exp(-z.clip(-30.0,30.0))));return _j(b,63).replace(_INF,np.nan)
def f17vr_f17_volatility_regime_cusum_absret_42d_jerk_v111_signal(closeadj):
    a=np.log(closeadj/closeadj.shift(1)).abs(); med=a.rolling(42,21).median(); dev=a-med; b=dev.rolling(21,11).sum();return _j(b,10).replace(_INF,np.nan)
def f17vr_f17_volatility_regime_cusum_signlogret_30d_jerk_v112_signal(closeadj):
    r=np.log(closeadj/closeadj.shift(1)); b=np.sign(r).rolling(30,15).sum();return _j(b,10).replace(_INF,np.nan)
def f17vr_f17_volatility_regime_co_oc_ratio_42d_jerk_v113_signal(open_,closeadj):
    co=np.log(closeadj/open_); cc=np.log(closeadj/closeadj.shift(1)); s_co=co.rolling(42,21).std(); s_cc=cc.rolling(42,21).std(); b=(s_co/s_cc.replace(0.0,np.nan));return _j(b,21).replace(_INF,np.nan)
def f17vr_f17_volatility_regime_oc_quartile_42on252_jerk_v114_signal(open_,closeadj):
    a=np.log(closeadj/open_).abs(); m=a.rolling(21,21).mean(); b=m.rolling(252,60).apply(_BK4,raw=True);return _j(b,63).replace(_INF,np.nan)
def f17vr_f17_volatility_regime_logvol_window_ratio_30over120_jerk_v115_signal(closeadj):
    r=np.log(closeadj/closeadj.shift(1)); s30=r.rolling(30,15).std(); s120=r.rolling(120,40).std(); b=np.log(s30/s120.replace(0.0,np.nan));return _j(b,21).replace(_INF,np.nan)
def f17vr_f17_volatility_regime_vol_zscore_dyn_60d_jerk_v116_signal(closeadj):
    v=_vol(closeadj,21); mu=v.rolling(60,30).mean(); sd=v.rolling(60,30).std(); b=((v-mu)/sd.replace(0.0,np.nan));return _j(b,10).replace(_INF,np.nan)
def f17vr_f17_volatility_regime_downup_volratio_42d_jerk_v119_signal(closeadj):
    r=np.log(closeadj/closeadj.shift(1)); neg=r.clip(upper=0.0); pos=r.clip(lower=0.0); dv=np.sqrt(neg.pow(2).rolling(42,42).mean()); uv=np.sqrt(pos.pow(2).rolling(42,42).mean()); b=(dv/uv.replace(0.0,np.nan));return _j(b,10).replace(_INF,np.nan)
def f17vr_f17_volatility_regime_downup_ratio_pctrank_252d_jerk_v120_signal(closeadj):
    r=np.log(closeadj/closeadj.shift(1)); dv=np.sqrt(r.clip(upper=0.0).pow(2).rolling(42,42).mean()); uv=np.sqrt(r.clip(lower=0.0).pow(2).rolling(42,42).mean()); ratio=dv/uv.replace(0.0,np.nan); b=ratio.rolling(252,60).apply(_R50,raw=True);return _j(b,63).replace(_INF,np.nan)
def f17vr_f17_volatility_regime_madstd_vs_norm_42d_jerk_v121_signal(closeadj):
    r=np.log(closeadj/closeadj.shift(1)); mv=r.rolling(21,21).apply(_MAD,raw=True); sv=r.rolling(21,21).std(); b=(mv/sv.replace(0.0,np.nan)-0.7979);return _j(b,10).replace(_INF,np.nan)
def f17vr_f17_volatility_regime_voldd_60d_jerk_v122_signal(closeadj):
    v=_vol(closeadj,21); mx=v.rolling(60,30).max(); b=(1.0-v/mx.replace(0.0,np.nan));return _j(b,10).replace(_INF,np.nan)
def f17vr_f17_volatility_regime_volup_30d_jerk_v123_signal(closeadj):
    v=_vol(closeadj,21); mn=v.rolling(30,15).min(); b=(v/mn.replace(0.0,np.nan)-1.0);return _j(b,10).replace(_INF,np.nan)
def _argminpos(x):
    if not np.all(np.isfinite(x)) or len(x)<2:return np.nan
    return float(int(np.argmin(x))/(len(x)-1))
def f17vr_f17_volatility_regime_vol_minargpos_60d_jerk_v124_signal(closeadj):
    b=_vol(closeadj,21).rolling(60,30).apply(_argminpos,raw=True);return _j(b,21).replace(_INF,np.nan)
def f17vr_f17_volatility_regime_bayes_evidence_log_60d_jerk_v125_signal(closeadj):
    v=_vol(closeadj,21)
    q75=v.rolling(252,60).quantile(0.75)
    q25=v.rolling(252,60).quantile(0.25)
    mad=v.rolling(252,60).apply(_MAD,raw=True).replace(0.0,np.nan)
    b=(((v-q25).abs()-(v-q75).abs())/mad);return _j(b,63).replace(_INF,np.nan)
def f17vr_f17_volatility_regime_close_above_avg_pct_in_lowvol_120d_jerk_v126_signal(close):
    s21=close.rolling(21,21).mean(); r=np.log(close/close.shift(1)); v=r.rolling(21,21).std(); med=v.rolling(252,60).median(); j=((close>s21) & (v<med)).astype(float).where(~s21.isna() & ~v.isna() & ~med.isna()); b=j.rolling(120,60).mean();return _j(b,21).replace(_INF,np.nan)
def f17vr_f17_volatility_regime_vol5_volpct_diff_252d_jerk_v127_signal(close):
    r=np.log(close/close.shift(1)); v5=r.rolling(5,5).std(); pr=v5.rolling(252,60).apply(_R50,raw=True); b=(pr-pr.shift(10));return _j(b,63).replace(_INF,np.nan)
def f17vr_f17_volatility_regime_HLrange_z_diff_120d_jerk_v128_signal(high,low):
    r=np.log(high/low); m=r.rolling(21,21).mean(); mu=m.rolling(120,40).mean(); sd=m.rolling(120,40).std(); z=(m-mu)/sd.replace(0.0,np.nan); b=(z-z.shift(10));return _j(b,21).replace(_INF,np.nan)
def f17vr_f17_volatility_regime_persistence_vol_dot_42d_jerk_v129_signal(closeadj):
    v=_vol(closeadj,21); s=np.sign(v.diff(1)); b=s.rolling(42,20).sum();return _j(b,21).replace(_INF,np.nan)
def f17vr_f17_volatility_regime_volpark_drift_30d_jerk_v130_signal(high,low):
    r2=(np.log(high/low) ** 2)/(4.0*np.log(2.0)); pv=np.sqrt(r2.rolling(21,21).mean()); b=pv.rolling(30,15).apply(_normslope,raw=True);return _j(b,10).replace(_INF,np.nan)
def f17vr_f17_volatility_regime_GKvol_z_120d_jerk_v131_signal(open_,high,low,close):
    rs=0.5*(np.log(high/low) ** 2)-(2.0*np.log(2.0)-1.0)*(np.log(close/open_) ** 2); gk=np.sqrt(rs.rolling(20,20).mean()); mu=gk.rolling(120,40).mean(); sd=gk.rolling(120,40).std(); b=((gk-mu)/sd.replace(0.0,np.nan));return _j(b,21).replace(_INF,np.nan)
def f17vr_f17_volatility_regime_vol_robust_iqr_42d_jerk_v132_signal(closeadj):
    r=np.log(closeadj/closeadj.shift(1)); q75=r.rolling(42,21).quantile(0.75); q25=r.rolling(42,21).quantile(0.25); b=((q75-q25)/1.349);return _j(b,21).replace(_INF,np.nan)
def _P10_40(x):return _qi(x,0.1,40,'<')
def f17vr_f17_volatility_regime_dayssince_lowvol_120d_jerk_v133_signal(closeadj):
    ind=_vol(closeadj,21).rolling(120,40).apply(_P10_40,raw=True)
    b=ind.rolling(120,40).apply(_BS,raw=True);return _j(b,21).replace(_INF,np.nan)
def f17vr_f17_volatility_regime_volprovexits_252d_jerk_v134_signal(closeadj):
    ind=_vol(closeadj,21).rolling(252,60).apply(_Q4,raw=True); exit_=((ind<0.5) & (ind.shift(1)>=0.5)).astype(float).where(~ind.isna() & ~ind.shift(1).isna()); b=exit_.rolling(252,60).sum();return _j(b,63).replace(_INF,np.nan)
def _maxrun_sameval(x):
    if not np.all(np.isfinite(x)):return np.nan
    best=1; cur=1
    for i in range(1,len(x)):
        if x[i]==x[i-1] and x[i] != 0.0:
            cur += 1
            if cur>best: best=cur
        else: cur=1
    return float(best)
def f17vr_f17_volatility_regime_max_runtype_120d_jerk_v136_signal(closeadj):
    s=np.sign(np.log(closeadj/closeadj.shift(1)))
    b=s.rolling(120,60).apply(_maxrun_sameval,raw=True);return _j(b,21).replace(_INF,np.nan)
def f17vr_f17_volatility_regime_voldelta_log_60d_jerk_v137_signal(closeadj):
    v=_vol(closeadj,21); b=(np.log(v)-np.log(v.shift(63)));return _j(b,21).replace(_INF,np.nan)
def f17vr_f17_volatility_regime_HL_ZB_4_42d_jerk_v138_signal(high,low):
    rng=high-low; med=rng.rolling(42,21).median(); flag=(rng>1.8*med).astype(float).where(~rng.isna() & ~med.isna()); b=flag.rolling(42,21).sum();return _j(b,10).replace(_INF,np.nan)
def f17vr_f17_volatility_regime_vol_rank_corr_diff_30_120_jerk_v139_signal(closeadj):
    v=_vol(closeadj,21)
    a=v.rolling(30,15).apply(_R15,raw=True)
    b=v.rolling(120,40).apply(_R40,raw=True)
    b=(a-b);return _j(b,21).replace(_INF,np.nan)
def f17vr_f17_volatility_regime_park_close_disp_120d_jerk_v140_signal(high,low,closeadj):
    r2=(np.log(high/low) ** 2)/(4.0*np.log(2.0)); pv=np.sqrt(r2.rolling(21,21).mean()); cv=np.log(closeadj/closeadj.shift(1)).rolling(21,21).std(); ratio=np.log(pv/cv.replace(0.0,np.nan)); b=ratio.rolling(120,40).std();return _j(b,21).replace(_INF,np.nan)
def f17vr_f17_volatility_regime_lowvol_streak_max_252d_jerk_v141_signal(closeadj):
    ind=_vol(closeadj,21).rolling(252,60).apply(_Q1,raw=True); b=ind.rolling(252,60).apply(_maxrun_above,raw=True);return _j(b,63).replace(_INF,np.nan)
def f17vr_f17_volatility_regime_volsum_above_p50_42d_jerk_v142_signal(closeadj):
    v=_vol(closeadj,21); med=v.rolling(252,60).median(); excess=(v-med).where(v>med,0.0); b=excess.rolling(42,20).sum();return _j(b,21).replace(_INF,np.nan)
def f17vr_f17_volatility_regime_vol_sign_bal_42d_jerk_v143_signal(closeadj):
    v=_vol(closeadj,21); med60=v.rolling(60,30).median(); b=np.sign(v-med60).rolling(42,20).sum();return _j(b,10).replace(_INF,np.nan)
def f17vr_f17_volatility_regime_vol_normality_test_60d_jerk_v144_signal(closeadj):
    v=_vol(closeadj,21); mu=v.rolling(60,30).mean(); sd=v.rolling(60,30).std(); b=(sd/mu.replace(0.0,np.nan));return _j(b,21).replace(_INF,np.nan)
def f17vr_f17_volatility_regime_HL_zerocross_med_60d_jerk_v145_signal(high,low):
    m21=np.log(high/low).rolling(21,21).mean()
    sgn=np.sign(m21-m21.rolling(120,40).median())
    cross=(sgn != sgn.shift(1)).astype(float).where(~sgn.isna() & ~sgn.shift(1).isna())
    b=cross.rolling(60,20).sum();return _j(b,21).replace(_INF,np.nan)
def f17vr_f17_volatility_regime_volstateprob_logit_42d_jerk_v146_signal(closeadj):
    ind=_vol(closeadj,21).rolling(252,60).apply(_Q4,raw=True); recent=ind.rolling(42,20).mean(); prior=ind.rolling(252,60).mean(); r_c=recent.clip(0.01,0.99); p_c=prior.clip(0.01,0.99); b=(np.log(r_c/(1.0-r_c))-np.log(p_c/(1.0-p_c)));return _j(b,10).replace(_INF,np.nan)
def _ent_unique(x):
    if not np.all(np.isfinite(x)) or len(x)<10:return np.nan
    u,c=np.unique(x,return_counts=True)
    p=c/c.sum()
    return float(-np.sum(p*np.log(p)))
def f17vr_f17_volatility_regime_vol_distentropy_3bin_120d_jerk_v147_signal(closeadj):
    reg=_vol(closeadj,21).rolling(252,60).apply(_TC,raw=True)
    b=reg.rolling(120,60).apply(_ent_unique,raw=True);return _j(b,21).replace(_INF,np.nan)
def f17vr_f17_volatility_regime_vol_dispersion_60d_jerk_v148_signal(closeadj):
    r=np.log(closeadj/closeadj.shift(1)); v5=r.rolling(5,5).std(); mu=v5.rolling(60,30).mean(); sd=v5.rolling(60,30).std(); b=(sd/mu.replace(0.0,np.nan));return _j(b,21).replace(_INF,np.nan)
def f17vr_f17_volatility_regime_close_minus_open_voldiff_42d_jerk_v149_signal(open_,closeadj):
    a=np.log(closeadj/open_); b=np.log(closeadj/closeadj.shift(1)); b=(a.rolling(42,21).std()-b.rolling(42,21).std());return _j(b,10).replace(_INF,np.nan)
def f17vr_f17_volatility_regime_volmaxminus_minmin_60d_jerk_v150_signal(closeadj):
    v=_vol(closeadj,21); hi=v.rolling(60,30).max(); lo=v.rolling(60,30).min(); b=(hi-lo);return _j(b,21).replace(_INF,np.nan)

f17_volatility_regime_jerk_001_150_REGISTRY={
"f17vr_f17_volatility_regime_volquartile_21on252_jerk_v001_signal":{"inputs":["closeadj"],"func":f17vr_f17_volatility_regime_volquartile_21on252_jerk_v001_signal},
"f17vr_f17_volatility_regime_quintile_chg_ind_21on252_jerk_v002_signal":{"inputs":["closeadj"],"func":f17vr_f17_volatility_regime_quintile_chg_ind_21on252_jerk_v002_signal},
"f17vr_f17_volatility_regime_decile_absret_120d_jerk_v003_signal":{"inputs":["close"],"func":f17vr_f17_volatility_regime_decile_absret_120d_jerk_v003_signal},
"f17vr_f17_volatility_regime_volquartile1_ind_21d_jerk_v004_signal":{"inputs":["closeadj"],"func":f17vr_f17_volatility_regime_volquartile1_ind_21d_jerk_v004_signal},
"f17vr_f17_volatility_regime_volquartile4_ind_21d_jerk_v005_signal":{"inputs":["closeadj"],"func":f17vr_f17_volatility_regime_volquartile4_ind_21d_jerk_v005_signal},
"f17vr_f17_volatility_regime_multih_quintile_5_21_63_jerk_v006_signal":{"inputs":["closeadj"],"func":f17vr_f17_volatility_regime_multih_quintile_5_21_63_jerk_v006_signal},
"f17vr_f17_volatility_regime_vol21_over_med252_jerk_v007_signal":{"inputs":["closeadj"],"func":f17vr_f17_volatility_regime_vol21_over_med252_jerk_v007_signal},
"f17vr_f17_volatility_regime_volz_21on252_jerk_v008_signal":{"inputs":["closeadj"],"func":f17vr_f17_volatility_regime_volz_21on252_jerk_v008_signal},
"f17vr_f17_volatility_regime_volpctrank_21on120_jerk_v009_signal":{"inputs":["closeadj"],"func":f17vr_f17_volatility_regime_volpctrank_21on120_jerk_v009_signal},
"f17vr_f17_volatility_regime_volpctrank_42on500_jerk_v010_signal":{"inputs":["closeadj"],"func":f17vr_f17_volatility_regime_volpctrank_42on500_jerk_v010_signal},
"f17vr_f17_volatility_regime_volpct_largeret_42d_jerk_v011_signal":{"inputs":["close"],"func":f17vr_f17_volatility_regime_volpct_largeret_42d_jerk_v011_signal},
"f17vr_f17_volatility_regime_regimestab_frac_60d_jerk_v012_signal":{"inputs":["closeadj"],"func":f17vr_f17_volatility_regime_regimestab_frac_60d_jerk_v012_signal},
"f17vr_f17_volatility_regime_transitioncount_90d_jerk_v013_signal":{"inputs":["closeadj"],"func":f17vr_f17_volatility_regime_transitioncount_90d_jerk_v013_signal},
"f17vr_f17_volatility_regime_volexpansion_5m63_jerk_v014_signal":{"inputs":["closeadj"],"func":f17vr_f17_volatility_regime_volexpansion_5m63_jerk_v014_signal},
"f17vr_f17_volatility_regime_streak_currentregime_60d_jerk_v015_signal":{"inputs":["closeadj"],"func":f17vr_f17_volatility_regime_streak_currentregime_60d_jerk_v015_signal},
"f17vr_f17_volatility_regime_vol_HLrange_pct_42d_jerk_v016_signal":{"inputs":["closeadj"],"func":f17vr_f17_volatility_regime_vol_HLrange_pct_42d_jerk_v016_signal},
"f17vr_f17_volatility_regime_daysinhighvol_120d_jerk_v017_signal":{"inputs":["closeadj"],"func":f17vr_f17_volatility_regime_daysinhighvol_120d_jerk_v017_signal},
"f17vr_f17_volatility_regime_ret_x_highvol_ind_jerk_v019_signal":{"inputs":["closeadj"],"func":f17vr_f17_volatility_regime_ret_x_highvol_ind_jerk_v019_signal},
"f17vr_f17_volatility_regime_ret_x_lowvol_ind_jerk_v020_signal":{"inputs":["closeadj"],"func":f17vr_f17_volatility_regime_ret_x_lowvol_ind_jerk_v020_signal},
"f17vr_f17_volatility_regime_sharpe_42d_currentvol_jerk_v021_signal":{"inputs":["closeadj"],"func":f17vr_f17_volatility_regime_sharpe_42d_currentvol_jerk_v021_signal},
"f17vr_f17_volatility_regime_volresid_AR1_120d_jerk_v022_signal":{"inputs":["closeadj"],"func":f17vr_f17_volatility_regime_volresid_AR1_120d_jerk_v022_signal},
"f17vr_f17_volatility_regime_volgap_pct_42on252_jerk_v023_signal":{"inputs":["closeadj"],"func":f17vr_f17_volatility_regime_volgap_pct_42on252_jerk_v023_signal},
"f17vr_f17_volatility_regime_highvolon_p90_jerk_v024_signal":{"inputs":["closeadj"],"func":f17vr_f17_volatility_regime_highvolon_p90_jerk_v024_signal},
"f17vr_f17_volatility_regime_lowvolon_p10_jerk_v025_signal":{"inputs":["closeadj"],"func":f17vr_f17_volatility_regime_lowvolon_p10_jerk_v025_signal},
"f17vr_f17_volatility_regime_expanding_state_42d_jerk_v026_signal":{"inputs":["closeadj"],"func":f17vr_f17_volatility_regime_expanding_state_42d_jerk_v026_signal},
"f17vr_f17_volatility_regime_extreme_state_120d_jerk_v027_signal":{"inputs":["closeadj"],"func":f17vr_f17_volatility_regime_extreme_state_120d_jerk_v027_signal},
"f17vr_f17_volatility_regime_highvol_clusters_120d_jerk_v028_signal":{"inputs":["closeadj"],"func":f17vr_f17_volatility_regime_highvol_clusters_120d_jerk_v028_signal},
"f17vr_f17_volatility_regime_runlen_currentreg_120d_jerk_v029_signal":{"inputs":["closeadj"],"func":f17vr_f17_volatility_regime_runlen_currentreg_120d_jerk_v029_signal},
"f17vr_f17_volatility_regime_ewmavoldiff_94m97_jerk_v031_signal":{"inputs":["closeadj"],"func":f17vr_f17_volatility_regime_ewmavoldiff_94m97_jerk_v031_signal},
"f17vr_f17_volatility_regime_absret_surprise_60d_jerk_v032_signal":{"inputs":["close"],"func":f17vr_f17_volatility_regime_absret_surprise_60d_jerk_v032_signal},
"f17vr_f17_volatility_regime_voljump_ind_21d_jerk_v033_signal":{"inputs":["closeadj"],"func":f17vr_f17_volatility_regime_voljump_ind_21d_jerk_v033_signal},
"f17vr_f17_volatility_regime_dayssince_volspike_120d_jerk_v034_signal":{"inputs":["closeadj"],"func":f17vr_f17_volatility_regime_dayssince_volspike_120d_jerk_v034_signal},
"f17vr_f17_volatility_regime_sigmoid_volresid_120d_jerk_v035_signal":{"inputs":["closeadj"],"func":f17vr_f17_volatility_regime_sigmoid_volresid_120d_jerk_v035_signal},
"f17vr_f17_volatility_regime_arctan_volcurv_60d_jerk_v036_signal":{"inputs":["closeadj"],"func":f17vr_f17_volatility_regime_arctan_volcurv_60d_jerk_v036_signal},
"f17vr_f17_volatility_regime_tanh_volsurprise_42d_jerk_v037_signal":{"inputs":["closeadj"],"func":f17vr_f17_volatility_regime_tanh_volsurprise_42d_jerk_v037_signal},
"f17vr_f17_volatility_regime_dayssince_enter_highvol_252d_jerk_v038_signal":{"inputs":["closeadj"],"func":f17vr_f17_volatility_regime_dayssince_enter_highvol_252d_jerk_v038_signal},
"f17vr_f17_volatility_regime_dayssince_exit_lowvol_252d_jerk_v039_signal":{"inputs":["closeadj"],"func":f17vr_f17_volatility_regime_dayssince_exit_lowvol_252d_jerk_v039_signal},
"f17vr_f17_volatility_regime_regimewidth_p10p90_252d_jerk_v040_signal":{"inputs":["closeadj"],"func":f17vr_f17_volatility_regime_regimewidth_p10p90_252d_jerk_v040_signal},
"f17vr_f17_volatility_regime_volsign_consistency_42d_jerk_v041_signal":{"inputs":["closeadj"],"func":f17vr_f17_volatility_regime_volsign_consistency_42d_jerk_v041_signal},
"f17vr_f17_volatility_regime_volofvol_60d_jerk_v042_signal":{"inputs":["closeadj"],"func":f17vr_f17_volatility_regime_volofvol_60d_jerk_v042_signal},
"f17vr_f17_volatility_regime_vol_corrwith_time_60d_jerk_v043_signal":{"inputs":["closeadj"],"func":f17vr_f17_volatility_regime_vol_corrwith_time_60d_jerk_v043_signal},
"f17vr_f17_volatility_regime_consec_vol_uptick_60d_jerk_v044_signal":{"inputs":["closeadj"],"func":f17vr_f17_volatility_regime_consec_vol_uptick_60d_jerk_v044_signal},
"f17vr_f17_volatility_regime_vol_zerocrossings_60d_jerk_v045_signal":{"inputs":["closeadj"],"func":f17vr_f17_volatility_regime_vol_zerocrossings_60d_jerk_v045_signal},
"f17vr_f17_volatility_regime_decile_transitions_90d_jerk_v046_signal":{"inputs":["closeadj"],"func":f17vr_f17_volatility_regime_decile_transitions_90d_jerk_v046_signal},
"f17vr_f17_volatility_regime_volcurvature_15d_jerk_v047_signal":{"inputs":["closeadj"],"func":f17vr_f17_volatility_regime_volcurvature_15d_jerk_v047_signal},
"f17vr_f17_volatility_regime_nhorizons_inhigh_5to63_jerk_v048_signal":{"inputs":["closeadj"],"func":f17vr_f17_volatility_regime_nhorizons_inhigh_5to63_jerk_v048_signal},
"f17vr_f17_volatility_regime_nhorizons_inlow_5to63_jerk_v049_signal":{"inputs":["closeadj"],"func":f17vr_f17_volatility_regime_nhorizons_inlow_5to63_jerk_v049_signal},
"f17vr_f17_volatility_regime_medianvol_horizons_jerk_v050_signal":{"inputs":["closeadj"],"func":f17vr_f17_volatility_regime_medianvol_horizons_jerk_v050_signal},
"f17vr_f17_volatility_regime_volpctrange_horizons_jerk_v051_signal":{"inputs":["closeadj"],"func":f17vr_f17_volatility_regime_volpctrange_horizons_jerk_v051_signal},
"f17vr_f17_volatility_regime_volquartile_5on120_jerk_v052_signal":{"inputs":["close"],"func":f17vr_f17_volatility_regime_volquartile_5on120_jerk_v052_signal},
"f17vr_f17_volatility_regime_volquintile_63on500_jerk_v053_signal":{"inputs":["closeadj"],"func":f17vr_f17_volatility_regime_volquintile_63on500_jerk_v053_signal},
"f17vr_f17_volatility_regime_volupshocks_count_42d_jerk_v054_signal":{"inputs":["closeadj"],"func":f17vr_f17_volatility_regime_volupshocks_count_42d_jerk_v054_signal},
"f17vr_f17_volatility_regime_volabsdev_med_252d_jerk_v055_signal":{"inputs":["closeadj"],"func":f17vr_f17_volatility_regime_volabsdev_med_252d_jerk_v055_signal},
"f17vr_f17_volatility_regime_vol_skew_ratio_42d_jerk_v056_signal":{"inputs":["closeadj"],"func":f17vr_f17_volatility_regime_vol_skew_ratio_42d_jerk_v056_signal},
"f17vr_f17_volatility_regime_volentry_count_p75_120d_jerk_v057_signal":{"inputs":["closeadj"],"func":f17vr_f17_volatility_regime_volentry_count_p75_120d_jerk_v057_signal},
"f17vr_f17_volatility_regime_volpctrank_diff_21_42_jerk_v058_signal":{"inputs":["closeadj"],"func":f17vr_f17_volatility_regime_volpctrank_diff_21_42_jerk_v058_signal},
"f17vr_f17_volatility_regime_ret_x_volz_42d_jerk_v059_signal":{"inputs":["closeadj"],"func":f17vr_f17_volatility_regime_ret_x_volz_42d_jerk_v059_signal},
"f17vr_f17_volatility_regime_voljump_freq_252d_jerk_v060_signal":{"inputs":["closeadj"],"func":f17vr_f17_volatility_regime_voljump_freq_252d_jerk_v060_signal},
"f17vr_f17_volatility_regime_signdiff_vol5_vol21_jerk_v061_signal":{"inputs":["close"],"func":f17vr_f17_volatility_regime_signdiff_vol5_vol21_jerk_v061_signal},
"f17vr_f17_volatility_regime_vol_drift_30d_jerk_v062_signal":{"inputs":["closeadj"],"func":f17vr_f17_volatility_regime_vol_drift_30d_jerk_v062_signal},
"f17vr_f17_volatility_regime_volupcross_med_252d_jerk_v063_signal":{"inputs":["closeadj"],"func":f17vr_f17_volatility_regime_volupcross_med_252d_jerk_v063_signal},
"f17vr_f17_volatility_regime_volstreak_above_med_60d_jerk_v064_signal":{"inputs":["closeadj"],"func":f17vr_f17_volatility_regime_volstreak_above_med_60d_jerk_v064_signal},
"f17vr_f17_volatility_regime_max_time_in_currentreg_180d_jerk_v065_signal":{"inputs":["closeadj"],"func":f17vr_f17_volatility_regime_max_time_in_currentreg_180d_jerk_v065_signal},
"f17vr_f17_volatility_regime_kurt_vol21_60d_jerk_v066_signal":{"inputs":["closeadj"],"func":f17vr_f17_volatility_regime_kurt_vol21_60d_jerk_v066_signal},
"f17vr_f17_volatility_regime_skew_vol21_60d_jerk_v067_signal":{"inputs":["closeadj"],"func":f17vr_f17_volatility_regime_skew_vol21_60d_jerk_v067_signal},
"f17vr_f17_volatility_regime_madstd_vol21_60d_jerk_v068_signal":{"inputs":["closeadj"],"func":f17vr_f17_volatility_regime_madstd_vol21_60d_jerk_v068_signal},
"f17vr_f17_volatility_regime_signagree_p75_5_21_63_jerk_v069_signal":{"inputs":["closeadj"],"func":f17vr_f17_volatility_regime_signagree_p75_5_21_63_jerk_v069_signal},
"f17vr_f17_volatility_regime_volstability_iqr_120d_jerk_v070_signal":{"inputs":["closeadj"],"func":f17vr_f17_volatility_regime_volstability_iqr_120d_jerk_v070_signal},
"f17vr_f17_volatility_regime_volrank_diff_short_long_jerk_v072_signal":{"inputs":["closeadj"],"func":f17vr_f17_volatility_regime_volrank_diff_short_long_jerk_v072_signal},
"f17vr_f17_volatility_regime_dayssince_minvol_252d_jerk_v073_signal":{"inputs":["closeadj"],"func":f17vr_f17_volatility_regime_dayssince_minvol_252d_jerk_v073_signal},
"f17vr_f17_volatility_regime_dayssince_maxvol_252d_jerk_v074_signal":{"inputs":["closeadj"],"func":f17vr_f17_volatility_regime_dayssince_maxvol_252d_jerk_v074_signal},
"f17vr_f17_volatility_regime_volminusewma_94_jerk_v075_signal":{"inputs":["closeadj"],"func":f17vr_f17_volatility_regime_volminusewma_94_jerk_v075_signal},
"f17vr_f17_volatility_regime_parkvol_quartile_21on252_jerk_v076_signal":{"inputs":["high","low","closeadj"],"func":f17vr_f17_volatility_regime_parkvol_quartile_21on252_jerk_v076_signal},
"f17vr_f17_volatility_regime_HLrange_z_42d_jerk_v077_signal":{"inputs":["high","low"],"func":f17vr_f17_volatility_regime_HLrange_z_42d_jerk_v077_signal},
"f17vr_f17_volatility_regime_HLrange_dayssincemax_180d_jerk_v078_signal":{"inputs":["high","low"],"func":f17vr_f17_volatility_regime_HLrange_dayssincemax_180d_jerk_v078_signal},
"f17vr_f17_volatility_regime_gkvol_p75_ind_30d_jerk_v079_signal":{"inputs":["open","high","low","close"],"func":f17vr_f17_volatility_regime_gkvol_p75_ind_30d_jerk_v079_signal},
"f17vr_f17_volatility_regime_rangetonormal_42d_jerk_v080_signal":{"inputs":["high","low","closeadj"],"func":f17vr_f17_volatility_regime_rangetonormal_42d_jerk_v080_signal},
"f17vr_f17_volatility_regime_downvol_p90_42d_jerk_v081_signal":{"inputs":["closeadj"],"func":f17vr_f17_volatility_regime_downvol_p90_42d_jerk_v081_signal},
"f17vr_f17_volatility_regime_upvol_decile_252d_jerk_v082_signal":{"inputs":["closeadj"],"func":f17vr_f17_volatility_regime_upvol_decile_252d_jerk_v082_signal},
"f17vr_f17_volatility_regime_downup_voldiff_z_42d_jerk_v083_signal":{"inputs":["closeadj"],"func":f17vr_f17_volatility_regime_downup_voldiff_z_42d_jerk_v083_signal},
"f17vr_f17_volatility_regime_madvol_quintile_21on252_jerk_v084_signal":{"inputs":["closeadj"],"func":f17vr_f17_volatility_regime_madvol_quintile_21on252_jerk_v084_signal},
"f17vr_f17_volatility_regime_madvol_pctrank_42on500_jerk_v085_signal":{"inputs":["closeadj"],"func":f17vr_f17_volatility_regime_madvol_pctrank_42on500_jerk_v085_signal},
"f17vr_f17_volatility_regime_absret_avg_pctrank_30on252_jerk_v086_signal":{"inputs":["closeadj"],"func":f17vr_f17_volatility_regime_absret_avg_pctrank_30on252_jerk_v086_signal},
"f17vr_f17_volatility_regime_absret_max_pctrank_120d_jerk_v087_signal":{"inputs":["closeadj"],"func":f17vr_f17_volatility_regime_absret_max_pctrank_120d_jerk_v087_signal},
"f17vr_f17_volatility_regime_cvar5_pctrank_42on252_jerk_v088_signal":{"inputs":["closeadj"],"func":f17vr_f17_volatility_regime_cvar5_pctrank_42on252_jerk_v088_signal},
"f17vr_f17_volatility_regime_var5_above_threshold_60d_jerk_v089_signal":{"inputs":["closeadj"],"func":f17vr_f17_volatility_regime_var5_above_threshold_60d_jerk_v089_signal},
"f17vr_f17_volatility_regime_retentropy_bins_42d_jerk_v090_signal":{"inputs":["closeadj"],"func":f17vr_f17_volatility_regime_retentropy_bins_42d_jerk_v090_signal},
"f17vr_f17_volatility_regime_abs_ret_entropy_60d_jerk_v091_signal":{"inputs":["closeadj"],"func":f17vr_f17_volatility_regime_abs_ret_entropy_60d_jerk_v091_signal},
"f17vr_f17_volatility_regime_post_highvol_60d_jerk_v092_signal":{"inputs":["closeadj"],"func":f17vr_f17_volatility_regime_post_highvol_60d_jerk_v092_signal},
"f17vr_f17_volatility_regime_post_highvol_smoothed_30d_jerk_v093_signal":{"inputs":["closeadj"],"func":f17vr_f17_volatility_regime_post_highvol_smoothed_30d_jerk_v093_signal},
"f17vr_f17_volatility_regime_adapt_threshold_ind_84d_jerk_v094_signal":{"inputs":["closeadj"],"func":f17vr_f17_volatility_regime_adapt_threshold_ind_84d_jerk_v094_signal},
"f17vr_f17_volatility_regime_adapt_low_threshold_84d_jerk_v095_signal":{"inputs":["closeadj"],"func":f17vr_f17_volatility_regime_adapt_low_threshold_84d_jerk_v095_signal},
"f17vr_f17_volatility_regime_semiIQR_high_pctrank_60d_jerk_v096_signal":{"inputs":["closeadj"],"func":f17vr_f17_volatility_regime_semiIQR_high_pctrank_60d_jerk_v096_signal},
"f17vr_f17_volatility_regime_semiIQR_low_pctrank_60d_jerk_v097_signal":{"inputs":["closeadj"],"func":f17vr_f17_volatility_regime_semiIQR_low_pctrank_60d_jerk_v097_signal},
"f17vr_f17_volatility_regime_kurt_excessflag_42d_jerk_v098_signal":{"inputs":["closeadj"],"func":f17vr_f17_volatility_regime_kurt_excessflag_42d_jerk_v098_signal},
"f17vr_f17_volatility_regime_kurtpctrank_42on252_jerk_v099_signal":{"inputs":["closeadj"],"func":f17vr_f17_volatility_regime_kurtpctrank_42on252_jerk_v099_signal},
"f17vr_f17_volatility_regime_NRcount_4_42d_jerk_v100_signal":{"inputs":["high","low"],"func":f17vr_f17_volatility_regime_NRcount_4_42d_jerk_v100_signal},
"f17vr_f17_volatility_regime_WRcount_4_42d_jerk_v101_signal":{"inputs":["high","low"],"func":f17vr_f17_volatility_regime_WRcount_4_42d_jerk_v101_signal},
"f17vr_f17_volatility_regime_HLavg_z_60d_jerk_v102_signal":{"inputs":["high","low"],"func":f17vr_f17_volatility_regime_HLavg_z_60d_jerk_v102_signal},
"f17vr_f17_volatility_regime_ewmavol_lam97_jerk_v103_signal":{"inputs":["closeadj"],"func":f17vr_f17_volatility_regime_ewmavol_lam97_jerk_v103_signal},
"f17vr_f17_volatility_regime_ewmavol_decile_94_252d_jerk_v104_signal":{"inputs":["closeadj"],"func":f17vr_f17_volatility_regime_ewmavol_decile_94_252d_jerk_v104_signal},
"f17vr_f17_volatility_regime_decile_jumpcount_42d_jerk_v105_signal":{"inputs":["closeadj"],"func":f17vr_f17_volatility_regime_decile_jumpcount_42d_jerk_v105_signal},
"f17vr_f17_volatility_regime_volzeroup_count_120d_jerk_v106_signal":{"inputs":["closeadj"],"func":f17vr_f17_volatility_regime_volzeroup_count_120d_jerk_v106_signal},
"f17vr_f17_volatility_regime_avgret_in_high_quart_252d_jerk_v107_signal":{"inputs":["closeadj"],"func":f17vr_f17_volatility_regime_avgret_in_high_quart_252d_jerk_v107_signal},
"f17vr_f17_volatility_regime_winrate_in_lowvol_252d_jerk_v108_signal":{"inputs":["closeadj"],"func":f17vr_f17_volatility_regime_winrate_in_lowvol_252d_jerk_v108_signal},
"f17vr_f17_volatility_regime_HLrange_acceleration_30d_jerk_v109_signal":{"inputs":["high","low"],"func":f17vr_f17_volatility_regime_HLrange_acceleration_30d_jerk_v109_signal},
"f17vr_f17_volatility_regime_sigmoid_madvol_z_120d_jerk_v110_signal":{"inputs":["closeadj"],"func":f17vr_f17_volatility_regime_sigmoid_madvol_z_120d_jerk_v110_signal},
"f17vr_f17_volatility_regime_cusum_absret_42d_jerk_v111_signal":{"inputs":["closeadj"],"func":f17vr_f17_volatility_regime_cusum_absret_42d_jerk_v111_signal},
"f17vr_f17_volatility_regime_cusum_signlogret_30d_jerk_v112_signal":{"inputs":["closeadj"],"func":f17vr_f17_volatility_regime_cusum_signlogret_30d_jerk_v112_signal},
"f17vr_f17_volatility_regime_co_oc_ratio_42d_jerk_v113_signal":{"inputs":["open","closeadj"],"func":f17vr_f17_volatility_regime_co_oc_ratio_42d_jerk_v113_signal},
"f17vr_f17_volatility_regime_oc_quartile_42on252_jerk_v114_signal":{"inputs":["open","closeadj"],"func":f17vr_f17_volatility_regime_oc_quartile_42on252_jerk_v114_signal},
"f17vr_f17_volatility_regime_logvol_window_ratio_30over120_jerk_v115_signal":{"inputs":["closeadj"],"func":f17vr_f17_volatility_regime_logvol_window_ratio_30over120_jerk_v115_signal},
"f17vr_f17_volatility_regime_vol_zscore_dyn_60d_jerk_v116_signal":{"inputs":["closeadj"],"func":f17vr_f17_volatility_regime_vol_zscore_dyn_60d_jerk_v116_signal},
"f17vr_f17_volatility_regime_downup_volratio_42d_jerk_v119_signal":{"inputs":["closeadj"],"func":f17vr_f17_volatility_regime_downup_volratio_42d_jerk_v119_signal},
"f17vr_f17_volatility_regime_downup_ratio_pctrank_252d_jerk_v120_signal":{"inputs":["closeadj"],"func":f17vr_f17_volatility_regime_downup_ratio_pctrank_252d_jerk_v120_signal},
"f17vr_f17_volatility_regime_madstd_vs_norm_42d_jerk_v121_signal":{"inputs":["closeadj"],"func":f17vr_f17_volatility_regime_madstd_vs_norm_42d_jerk_v121_signal},
"f17vr_f17_volatility_regime_voldd_60d_jerk_v122_signal":{"inputs":["closeadj"],"func":f17vr_f17_volatility_regime_voldd_60d_jerk_v122_signal},
"f17vr_f17_volatility_regime_volup_30d_jerk_v123_signal":{"inputs":["closeadj"],"func":f17vr_f17_volatility_regime_volup_30d_jerk_v123_signal},
"f17vr_f17_volatility_regime_vol_minargpos_60d_jerk_v124_signal":{"inputs":["closeadj"],"func":f17vr_f17_volatility_regime_vol_minargpos_60d_jerk_v124_signal},
"f17vr_f17_volatility_regime_bayes_evidence_log_60d_jerk_v125_signal":{"inputs":["closeadj"],"func":f17vr_f17_volatility_regime_bayes_evidence_log_60d_jerk_v125_signal},
"f17vr_f17_volatility_regime_close_above_avg_pct_in_lowvol_120d_jerk_v126_signal":{"inputs":["close"],"func":f17vr_f17_volatility_regime_close_above_avg_pct_in_lowvol_120d_jerk_v126_signal},
"f17vr_f17_volatility_regime_vol5_volpct_diff_252d_jerk_v127_signal":{"inputs":["close"],"func":f17vr_f17_volatility_regime_vol5_volpct_diff_252d_jerk_v127_signal},
"f17vr_f17_volatility_regime_HLrange_z_diff_120d_jerk_v128_signal":{"inputs":["high","low"],"func":f17vr_f17_volatility_regime_HLrange_z_diff_120d_jerk_v128_signal},
"f17vr_f17_volatility_regime_persistence_vol_dot_42d_jerk_v129_signal":{"inputs":["closeadj"],"func":f17vr_f17_volatility_regime_persistence_vol_dot_42d_jerk_v129_signal},
"f17vr_f17_volatility_regime_volpark_drift_30d_jerk_v130_signal":{"inputs":["high","low"],"func":f17vr_f17_volatility_regime_volpark_drift_30d_jerk_v130_signal},
"f17vr_f17_volatility_regime_GKvol_z_120d_jerk_v131_signal":{"inputs":["open","high","low","close"],"func":f17vr_f17_volatility_regime_GKvol_z_120d_jerk_v131_signal},
"f17vr_f17_volatility_regime_vol_robust_iqr_42d_jerk_v132_signal":{"inputs":["closeadj"],"func":f17vr_f17_volatility_regime_vol_robust_iqr_42d_jerk_v132_signal},
"f17vr_f17_volatility_regime_dayssince_lowvol_120d_jerk_v133_signal":{"inputs":["closeadj"],"func":f17vr_f17_volatility_regime_dayssince_lowvol_120d_jerk_v133_signal},
"f17vr_f17_volatility_regime_volprovexits_252d_jerk_v134_signal":{"inputs":["closeadj"],"func":f17vr_f17_volatility_regime_volprovexits_252d_jerk_v134_signal},
"f17vr_f17_volatility_regime_max_runtype_120d_jerk_v136_signal":{"inputs":["closeadj"],"func":f17vr_f17_volatility_regime_max_runtype_120d_jerk_v136_signal},
"f17vr_f17_volatility_regime_voldelta_log_60d_jerk_v137_signal":{"inputs":["closeadj"],"func":f17vr_f17_volatility_regime_voldelta_log_60d_jerk_v137_signal},
"f17vr_f17_volatility_regime_HL_ZB_4_42d_jerk_v138_signal":{"inputs":["high","low"],"func":f17vr_f17_volatility_regime_HL_ZB_4_42d_jerk_v138_signal},
"f17vr_f17_volatility_regime_vol_rank_corr_diff_30_120_jerk_v139_signal":{"inputs":["closeadj"],"func":f17vr_f17_volatility_regime_vol_rank_corr_diff_30_120_jerk_v139_signal},
"f17vr_f17_volatility_regime_park_close_disp_120d_jerk_v140_signal":{"inputs":["high","low","closeadj"],"func":f17vr_f17_volatility_regime_park_close_disp_120d_jerk_v140_signal},
"f17vr_f17_volatility_regime_lowvol_streak_max_252d_jerk_v141_signal":{"inputs":["closeadj"],"func":f17vr_f17_volatility_regime_lowvol_streak_max_252d_jerk_v141_signal},
"f17vr_f17_volatility_regime_volsum_above_p50_42d_jerk_v142_signal":{"inputs":["closeadj"],"func":f17vr_f17_volatility_regime_volsum_above_p50_42d_jerk_v142_signal},
"f17vr_f17_volatility_regime_vol_sign_bal_42d_jerk_v143_signal":{"inputs":["closeadj"],"func":f17vr_f17_volatility_regime_vol_sign_bal_42d_jerk_v143_signal},
"f17vr_f17_volatility_regime_vol_normality_test_60d_jerk_v144_signal":{"inputs":["closeadj"],"func":f17vr_f17_volatility_regime_vol_normality_test_60d_jerk_v144_signal},
"f17vr_f17_volatility_regime_HL_zerocross_med_60d_jerk_v145_signal":{"inputs":["high","low"],"func":f17vr_f17_volatility_regime_HL_zerocross_med_60d_jerk_v145_signal},
"f17vr_f17_volatility_regime_volstateprob_logit_42d_jerk_v146_signal":{"inputs":["closeadj"],"func":f17vr_f17_volatility_regime_volstateprob_logit_42d_jerk_v146_signal},
"f17vr_f17_volatility_regime_vol_distentropy_3bin_120d_jerk_v147_signal":{"inputs":["closeadj"],"func":f17vr_f17_volatility_regime_vol_distentropy_3bin_120d_jerk_v147_signal},
"f17vr_f17_volatility_regime_vol_dispersion_60d_jerk_v148_signal":{"inputs":["closeadj"],"func":f17vr_f17_volatility_regime_vol_dispersion_60d_jerk_v148_signal},
"f17vr_f17_volatility_regime_close_minus_open_voldiff_42d_jerk_v149_signal":{"inputs":["open","closeadj"],"func":f17vr_f17_volatility_regime_close_minus_open_voldiff_42d_jerk_v149_signal},
"f17vr_f17_volatility_regime_volmaxminus_minmin_60d_jerk_v150_signal":{"inputs":["closeadj"],"func":f17vr_f17_volatility_regime_volmaxminus_minmin_60d_jerk_v150_signal},
}

def _synthetic_inputs(n=800,seed=42):
    rng=np.random.default_rng(seed); seg=n//4; rest=n-3*seg
    ret=np.concatenate([rng.normal(0.0012,0.011,seg),rng.normal(-0.0005,0.018,seg),rng.normal(-0.0010,0.014,seg),rng.normal(0.0008,0.012,rest)])
    close=50.0*np.exp(np.cumsum(ret))
    closeadj=close*np.exp(rng.normal(0.0,0.0003,size=n).cumsum())
    intraday=rng.normal(0.0,0.008,size=n)
    open_=close*np.exp(-intraday*0.5)
    high=np.maximum(close,open_)*np.exp(np.abs(rng.normal(0.0,0.006,size=n)))
    low=np.minimum(close,open_)*np.exp(-np.abs(rng.normal(0.0,0.006,size=n)))
    volume=rng.lognormal(mean=13.0,sigma=0.6,size=n)
    idx=pd.RangeIndex(n)
    return pd.DataFrame({"open":pd.Series(open_,index=idx,dtype=float),"high":pd.Series(high,index=idx,dtype=float),"low":pd.Series(low,index=idx,dtype=float),"close":pd.Series(close,index=idx,dtype=float),"closeadj":pd.Series(closeadj,index=idx,dtype=float),"volume":pd.Series(volume,index=idx,dtype=float)})

def _self_test():
    df=_synthetic_inputs(n=800,seed=42)
    results={}
    for name,entry in f17_volatility_regime_jerk_001_150_REGISTRY.items():
        out=entry["func"](*[df[c] for c in entry["inputs"]])
        assert isinstance(out,pd.Series) and len(out)==len(df),f"{name}: shape"
        clean=out.dropna()
        assert len(clean)>0,f"{name}: all NaN"
        assert float(clean.std())>0.0 or clean.nunique()>1,f"{name}: constant"
        results[name]=out
    warm=252
    frac=sum(1 for s in results.values() if s.iloc[warm:].isna().mean()<0.5)/len(results)
    assert frac>=0.80,f"coverage {frac:.2%}"
    A=pd.concat({n:results[n] for n in results},axis=1).iloc[warm:].replace(_INF,np.nan)
    C=A.corr(min_periods=50).abs(); np.fill_diagonal(C.values,0.0)
    mc=float(C.max().max())
    if mc>0.95:
        for i,a in enumerate(C.columns):
            for j,b in enumerate(C.columns):
                if j>i and C.iloc[i,j]>0.94: print(f"  {a} vs {b} -> {C.iloc[i,j]:.4f}")
    assert mc<=0.95+1e-9,f"max |corr|={mc:.4f}"
    print(f"OK jerk_001_150: {len(results)} features, max |corr|={mc:.4f}, coverage_ok={frac:.2%}")

if __name__=="__main__":
    _self_test()
