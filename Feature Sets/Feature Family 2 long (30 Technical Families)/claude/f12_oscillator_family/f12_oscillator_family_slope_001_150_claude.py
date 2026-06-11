from __future__ import annotations
import numpy as np
import pandas as pd

def _W(x,n): return x.clip(lower=0.0).ewm(alpha=1.0/float(n),adjust=False,min_periods=n).mean()

def _LH(h,l,n): return l.rolling(n,min_periods=n).min(),h.rolling(n,min_periods=n).max()

def _RG(h, l, n):
    ll = l.rolling(n, min_periods=n).min()
    hh = h.rolling(n, min_periods=n).max()
    return (hh - ll).replace(0.0, np.nan), ll, hh

def _C(h, l, c, n):
    tp = (h + l + c) / 3.0
    sma = tp.rolling(n, min_periods=n).mean()
    mad = (tp - sma).abs().rolling(n, min_periods=n).mean()
    return (tp - sma) / (0.015 * mad.replace(0.0, np.nan))

def _MF(h, l, c, v, n):
    tp = (h + l + c) / 3.0
    rmf = tp * v
    dlt = tp.diff()
    pos = rmf.where(dlt > 0, 0.0)
    neg = rmf.where(dlt < 0, 0.0)
    mr = pos.rolling(n, min_periods=n).sum() / neg.rolling(n, min_periods=n).sum().replace(0.0, np.nan)
    return 100.0 - 100.0 / (1.0 + mr)

def _UO(h, l, c):
    pc = c.shift(1)
    tl = pd.concat([l, pc], axis=1).min(axis=1)
    th = pd.concat([h, pc], axis=1).max(axis=1)
    bp = c - tl
    trv = th - tl
    a7 = bp.rolling(7, min_periods=7).sum() / trv.rolling(7, min_periods=7).sum().replace(0.0, np.nan)
    a14 = bp.rolling(14, min_periods=14).sum() / trv.rolling(14, min_periods=14).sum().replace(0.0, np.nan)
    a28 = bp.rolling(28, min_periods=28).sum() / trv.rolling(28, min_periods=28).sum().replace(0.0, np.nan)
    return 100.0 * (4.0 * a7 + 2.0 * a14 + a28) / 7.0

def _SK(h, l, c, n):
    ll = l.rolling(n, min_periods=n).min()
    hh = h.rolling(n, min_periods=n).max()
    return 100.0 * (c - ll) / (hh - ll).replace(0.0, np.nan)

def _WR(h, l, c, n):
    ll = l.rolling(n, min_periods=n).min()
    hh = h.rolling(n, min_periods=n).max()
    return -100.0 * (hh - c) / (hh - ll).replace(0.0, np.nan)

def f12os_f12_oscillator_family_rsi_7d_slope_v001_signal(close):
  n=7
  d=close.diff()
  au=_W(d,n)
  ad=_W(-d,n)
  rs=au/ad.replace(0.0,np.nan)
  b=100.0-100.0/(1.0+rs)
  return b.diff(10).replace([np.inf,-np.inf],np.nan)
def f12os_f12_oscillator_family_rsi_14d_slope_v002_signal(close):
  n=14
  d=close.diff()
  au=_W(d,n)
  ad=_W(-d,n)
  rs=au/ad.replace(0.0,np.nan)
  b=100.0-100.0/(1.0+rs)
  return b.diff(5).replace([np.inf,-np.inf],np.nan)
def f12os_f12_oscillator_family_rsi_50d_slope_v003_signal(closeadj):
  n=50
  d=closeadj.diff()
  au=_W(d,n)
  ad=_W(-d,n)
  rs=au/ad.replace(0.0,np.nan)
  b=100.0-100.0/(1.0+rs)
  return (b.diff(21)/b.abs().rolling(60,min_periods=60).mean().replace(0.0,np.nan)).replace([np.inf,-np.inf],np.nan)
def f12os_f12_oscillator_family_rsidsmid_21d_slope_v004_signal(close):
  n=21
  d=close.diff()
  au=_W(d,n)
  ad=_W(-d,n)
  rs=au/ad.replace(0.0,np.nan)
  rsi=100.0-100.0/(1.0+rs)
  sgn=np.sign(rsi-50.0)
  flip=(sgn!=sgn.shift(1)).astype(float).where(~sgn.isna()&~sgn.shift(1).isna())
  def _ds(x):
    idx=np.where(x>0.5)[0]
    if idx.size==0:return 100.0
    return float(len(x)-1-idx[-1])
  b=flip.rolling(100,min_periods=100).apply(_ds,raw=True)
  return b.diff(10).replace([np.inf,-np.inf],np.nan)
def f12os_f12_oscillator_family_rsidiff21_30d_slope_v005_signal(closeadj):
  n=30
  d=closeadj.diff()
  au=_W(d,n)
  ad=_W(-d,n)
  rs=au/ad.replace(0.0,np.nan)
  rsi=100.0-100.0/(1.0+rs)
  b=rsi-rsi.rolling(21,min_periods=21).mean()
  return b.diff(10).replace([np.inf,-np.inf],np.nan)
def f12os_f12_oscillator_family_rsisma_60d_slope_v006_signal(closeadj):
  n=14
  d=closeadj.diff()
  au=_W(d,n)
  ad=_W(-d,n)
  rs=au/ad.replace(0.0,np.nan)
  rsi=100.0-100.0/(1.0+rs)
  b=rsi.rolling(30,min_periods=30).mean()
  return b.diff(21).replace([np.inf,-np.inf],np.nan)
def f12os_f12_oscillator_family_rsisign_14d_slope_v007_signal(close):
  n=14
  d=close.diff()
  au=_W(d,n)
  ad=_W(-d,n)
  rs=au/ad.replace(0.0,np.nan)
  b=np.sign((100.0-100.0/(1.0+rs))-50.0)
  return b.diff(5).replace([np.inf,-np.inf],np.nan)
def f12os_f12_oscillator_family_rsiob_20d_slope_v008_signal(close):
  n=14
  d=close.diff()
  au=_W(d,n)
  ad=_W(-d,n)
  rs=au/ad.replace(0.0,np.nan)
  rsi=100.0-100.0/(1.0+rs)
  fl=(rsi>70.0).astype(float).where(~rsi.isna())
  b=fl.rolling(20,min_periods=20).sum()
  return b.diff(10).replace([np.inf,-np.inf],np.nan)
def f12os_f12_oscillator_family_rsios_30d_slope_v009_signal(closeadj):
  n=14
  d=closeadj.diff()
  au=_W(d,n)
  ad=_W(-d,n)
  rs=au/ad.replace(0.0,np.nan)
  rsi=100.0-100.0/(1.0+rs)
  fl=(rsi<30.0).astype(float).where(~rsi.isna())
  b=fl.rolling(30,min_periods=30).sum()
  return b.diff(21).replace([np.inf,-np.inf],np.nan)
def f12os_f12_oscillator_family_rsidsob_60d_slope_v010_signal(closeadj):
  n=14
  d=closeadj.diff()
  au=_W(d,n)
  ad=_W(-d,n)
  rs=au/ad.replace(0.0,np.nan)
  rsi=100.0-100.0/(1.0+rs)
  cond=(rsi>70.0).astype(float).where(~rsi.isna())
  def _ds(x):
    idx=np.where(x>0.5)[0]
    if idx.size==0:return 60.0
    return float(len(x)-1-idx[-1])
  b=cond.rolling(60,min_periods=60).apply(_ds,raw=True)
  return b.diff(21).replace([np.inf,-np.inf],np.nan)
def f12os_f12_oscillator_family_rsidsos_80d_slope_v011_signal(closeadj):
  n=14
  d=closeadj.diff()
  au=_W(d,n)
  ad=_W(-d,n)
  rs=au/ad.replace(0.0,np.nan)
  rsi=100.0-100.0/(1.0+rs)
  cond=(rsi<30.0).astype(float).where(~rsi.isna())
  def _ds(x):
    idx=np.where(x>0.5)[0]
    if idx.size==0:return 80.0
    return float(len(x)-1-idx[-1])
  b=cond.rolling(80,min_periods=80).apply(_ds,raw=True)
  return b.diff(21).replace([np.inf,-np.inf],np.nan)
def f12os_f12_oscillator_family_rsirank_120d_slope_v012_signal(closeadj):
  n=14
  d=closeadj.diff()
  au=_W(d,n)
  ad=_W(-d,n)
  rs=au/ad.replace(0.0,np.nan)
  rsi=100.0-100.0/(1.0+rs)
  b=rsi.rolling(120,min_periods=120).rank(pct=True)
  return b.diff(63).replace([np.inf,-np.inf],np.nan)
def f12os_f12_oscillator_family_rsivar_80d_slope_v013_signal(closeadj):
  n=14
  d=closeadj.diff()
  au=_W(d,n)
  ad=_W(-d,n)
  rs=au/ad.replace(0.0,np.nan)
  rsi=100.0-100.0/(1.0+rs)
  b=rsi.rolling(80,min_periods=80).std(ddof=1)
  return b.diff(21).replace([np.inf,-np.inf],np.nan)
def f12os_f12_oscillator_family_rsixmid_60d_slope_v014_signal(close):
  n=14
  d=close.diff()
  au=_W(d,n)
  ad=_W(-d,n)
  rs=au/ad.replace(0.0,np.nan)
  rsi=100.0-100.0/(1.0+rs)
  sgn=np.sign(rsi-50.0)
  fl=(sgn!=sgn.shift(1)).astype(float).where(~sgn.isna()&~sgn.shift(1).isna())
  b=fl.rolling(60,min_periods=60).sum()
  return b.diff(21).replace([np.inf,-np.inf],np.nan)
def f12os_f12_oscillator_family_rsifloor_120d_slope_v015_signal(closeadj):
  n=14
  d=closeadj.diff()
  au=_W(d,n)
  ad=_W(-d,n)
  rs=au/ad.replace(0.0,np.nan)
  rsi=100.0-100.0/(1.0+rs)
  b=rsi.rolling(120,min_periods=120).min()
  return b.diff(63).replace([np.inf,-np.inf],np.nan)
def f12os_f12_oscillator_family_stochk_5d_slope_v016_signal(high,low,close):
  b=_SK(high,low,close,5)
  return b.diff(5).replace([np.inf,-np.inf],np.nan)
def f12os_f12_oscillator_family_stochk_14d_slope_v017_signal(high,low,close):
  b=_SK(high,low,close,14)
  return b.diff(10).replace([np.inf,-np.inf],np.nan)
def f12os_f12_oscillator_family_stochk_50d_slope_v018_signal(high,low,closeadj):
  b=_SK(high,low,closeadj,50)
  return b.diff(21).replace([np.inf,-np.inf],np.nan)
def f12os_f12_oscillator_family_stochd_14d_slope_v019_signal(high,low,close):
  k=_SK(high,low,close,14)
  b=k.rolling(3,min_periods=3).mean()
  return b.diff(5).replace([np.inf,-np.inf],np.nan)
def f12os_f12_oscillator_family_stochkd_14d_slope_v020_signal(high,low,close):
  k=_SK(high,low,close,14)
  d=k.rolling(3,min_periods=3).mean()
  b=k-d
  return b.diff(10).replace([np.inf,-np.inf],np.nan)
def f12os_f12_oscillator_family_stochkdxover_50d_slope_v021_signal(high,low,closeadj):
  k=_SK(high,low,closeadj,14)
  d=k.rolling(3,min_periods=3).mean()
  s=np.sign(k-d)
  xo=(s!=s.shift(1)).astype(float).where(~s.isna()&~s.shift(1).isna())
  b=xo.rolling(50,min_periods=50).sum()
  return b.diff(21).replace([np.inf,-np.inf],np.nan)
def f12os_f12_oscillator_family_stochob_50d_slope_v022_signal(high,low,closeadj):
  k=_SK(high,low,closeadj,14)
  fl=(k>80.0).astype(float).where(~k.isna())
  b=fl.rolling(50,min_periods=50).mean()
  return b.diff(10).replace([np.inf,-np.inf],np.nan)
def f12os_f12_oscillator_family_stochstreakob_30d_slope_v023_signal(high,low,closeadj):
  k=_SK(high,low,closeadj,14)
  cond=(k>80.0).astype(float).where(~k.isna())
  def _st(x):
    c=0.0
    for v in x[::-1]:
      if v>0.5:c+=1.0
      else:break
    return c
  b=cond.rolling(30,min_periods=30).apply(_st,raw=True)
  return b.diff(10).replace([np.inf,-np.inf],np.nan)
def f12os_f12_oscillator_family_stochcent_30d_slope_v024_signal(high,low,closeadj):
  b=_SK(high,low,closeadj,30)-50.0
  return b.diff(21).replace([np.inf,-np.inf],np.nan)
def f12os_f12_oscillator_family_willr_7d_slope_v025_signal(high,low,close):
  b=_WR(high,low,close,7)
  return b.diff(5).replace([np.inf,-np.inf],np.nan)
def f12os_f12_oscillator_family_willrxlow_100d_slope_v026_signal(high,low,closeadj):
  wr=_WR(high,low,closeadj,21)
  fl=(wr<-80.0).astype(float).where(~wr.isna())
  b=fl.rolling(100,min_periods=100).mean()
  return b.diff(21).replace([np.inf,-np.inf],np.nan)
def f12os_f12_oscillator_family_willrdsmid_21d_slope_v027_signal(high,low,close):
  wr=_WR(high,low,close,21)
  sgn=np.sign(wr+50.0)
  flip=(sgn!=sgn.shift(1)).astype(float).where(~sgn.isna()&~sgn.shift(1).isna())
  def _ds(x):
    idx=np.where(x>0.5)[0]
    if idx.size==0:return 80.0
    return float(len(x)-1-idx[-1])
  b=flip.rolling(80,min_periods=80).apply(_ds,raw=True)
  return b.diff(10).replace([np.inf,-np.inf],np.nan)
def f12os_f12_oscillator_family_cci_14d_slope_v028_signal(high,low,close):
  n=14
  tp=(high+low+close)/3.0
  sma=tp.rolling(n,min_periods=n).mean()
  mad=(tp-sma).abs().rolling(n,min_periods=n).mean()
  b=(tp-sma)/(0.015*mad.replace(0.0,np.nan))
  return b.diff(5).replace([np.inf,-np.inf],np.nan)
def f12os_f12_oscillator_family_cci_50d_slope_v029_signal(high,low,closeadj):
  n=50
  tp=(high+low+closeadj)/3.0
  sma=tp.rolling(n,min_periods=n).mean()
  mad=(tp-sma).abs().rolling(n,min_periods=n).mean()
  b=(tp-sma)/(0.015*mad.replace(0.0,np.nan))
  return b.diff(21).replace([np.inf,-np.inf],np.nan)
def f12os_f12_oscillator_family_ccitanh_20d_slope_v030_signal(high,low,close):
  n=20
  tp=(high+low+close)/3.0
  sma=tp.rolling(n,min_periods=n).mean()
  mad=(tp-sma).abs().rolling(n,min_periods=n).mean()
  cci=(tp-sma)/(0.015*mad.replace(0.0,np.nan))
  b=np.tanh(cci/100.0)
  return b.diff(5).replace([np.inf,-np.inf],np.nan)
def f12os_f12_oscillator_family_cciob_40d_slope_v031_signal(high,low,closeadj):
  n=20
  tp=(high+low+closeadj)/3.0
  sma=tp.rolling(n,min_periods=n).mean()
  mad=(tp-sma).abs().rolling(n,min_periods=n).mean()
  cci=(tp-sma)/(0.015*mad.replace(0.0,np.nan))
  fl=(cci>100.0).astype(float).where(~cci.isna())
  b=fl.rolling(40,min_periods=40).mean()
  return b.diff(10).replace([np.inf,-np.inf],np.nan)
def f12os_f12_oscillator_family_cciextrm_120d_slope_v032_signal(high,low,closeadj):
  n=20
  tp=(high+low+closeadj)/3.0
  sma=tp.rolling(n,min_periods=n).mean()
  mad=(tp-sma).abs().rolling(n,min_periods=n).mean()
  cci=(tp-sma)/(0.015*mad.replace(0.0,np.nan))
  b=cci.abs().rolling(120,min_periods=120).max()
  return b.diff(63).replace([np.inf,-np.inf],np.nan)
def f12os_f12_oscillator_family_ccisign_30d_slope_v033_signal(high,low,closeadj):
  n=30
  tp=(high+low+closeadj)/3.0
  sma=tp.rolling(n,min_periods=n).mean()
  mad=(tp-sma).abs().rolling(n,min_periods=n).mean()
  cci=(tp-sma)/(0.015*mad.replace(0.0,np.nan))
  b=np.sign(cci)
  return b.diff(21).replace([np.inf,-np.inf],np.nan)
def f12os_f12_oscillator_family_mfi_14d_slope_v034_signal(high,low,close,volume):
  n=14
  tp=(high+low+close)/3.0; rmf=tp*volume; dlt=tp.diff()
  pos=rmf.where(dlt>0,0.0); neg=rmf.where(dlt<0,0.0)
  mr=pos.rolling(n,min_periods=n).sum()/neg.rolling(n,min_periods=n).sum().replace(0.0,np.nan)
  b=100.0-100.0/(1.0+mr)
  return b.diff(5).replace([np.inf,-np.inf],np.nan)
def f12os_f12_oscillator_family_mfi_30d_slope_v035_signal(high,low,closeadj,volume):
  n=30
  tp=(high+low+closeadj)/3.0; rmf=tp*volume; dlt=tp.diff()
  pos=rmf.where(dlt>0,0.0); neg=rmf.where(dlt<0,0.0)
  mr=pos.rolling(n,min_periods=n).sum()/neg.rolling(n,min_periods=n).sum().replace(0.0,np.nan)
  b=100.0-100.0/(1.0+mr)
  return b.diff(21).replace([np.inf,-np.inf],np.nan)
def f12os_f12_oscillator_family_mfinorm_21d_slope_v036_signal(high,low,close,volume):
  n=21
  tp=(high+low+close)/3.0; rmf=tp*volume; dlt=tp.diff()
  pos=rmf.where(dlt>0,0.0); neg=rmf.where(dlt<0,0.0)
  mr=pos.rolling(n,min_periods=n).sum()/neg.rolling(n,min_periods=n).sum().replace(0.0,np.nan)
  mfi=100.0-100.0/(1.0+mr)
  b=(mfi-50.0)/50.0
  return b.diff(10).replace([np.inf,-np.inf],np.nan)
def f12os_f12_oscillator_family_uo_7_14_28_slope_v037_signal(high,low,close):
  b=_UO(high,low,close)
  return b.diff(10).replace([np.inf,-np.inf],np.nan)
def f12os_f12_oscillator_family_uolong_14_28_56_slope_v038_signal(high,low,closeadj):
  pc=closeadj.shift(1)
  tl=pd.concat([low,pc],axis=1).min(axis=1); th=pd.concat([high,pc],axis=1).max(axis=1)
  bp=closeadj-tl; trv=th-tl
  a1=bp.rolling(14,min_periods=14).sum()/trv.rolling(14,min_periods=14).sum().replace(0.0,np.nan)
  a2=bp.rolling(28,min_periods=28).sum()/trv.rolling(28,min_periods=28).sum().replace(0.0,np.nan)
  a3=bp.rolling(56,min_periods=56).sum()/trv.rolling(56,min_periods=56).sum().replace(0.0,np.nan)
  b=100.0*(4.0*a1+2.0*a2+a3)/7.0
  return b.diff(21).replace([np.inf,-np.inf],np.nan)
def f12os_f12_oscillator_family_aopct_5_34_slope_v039_signal(high,low):
  mp=0.5*(high+low)
  s=mp.rolling(5,min_periods=5).mean(); l=mp.rolling(34,min_periods=34).mean()
  b=100.0*(s-l)/l.replace(0.0,np.nan)
  return b.diff(5).replace([np.inf,-np.inf],np.nan)
def f12os_f12_oscillator_family_aoz_60d_slope_v040_signal(high,low):
  mp=0.5*(high+low)
  ao=mp.rolling(5,min_periods=5).mean()-mp.rolling(34,min_periods=34).mean()
  mu=ao.rolling(60,min_periods=60).mean(); sd=ao.rolling(60,min_periods=60).std(ddof=1)
  b=(ao-mu)/sd.replace(0.0,np.nan)
  return b.diff(21).replace([np.inf,-np.inf],np.nan)
def f12os_f12_oscillator_family_dpo_20d_slope_v041_signal(close):
  n=20
  b=close-close.rolling(n,min_periods=n).mean().shift(n//2+1)
  return b.diff(10).replace([np.inf,-np.inf],np.nan)
def f12os_f12_oscillator_family_dpoxsign_60d_slope_v042_signal(closeadj):
  n=20
  dpo=closeadj-closeadj.rolling(n,min_periods=n).mean().shift(n//2+1)
  sgn=np.sign(dpo)
  fl=(sgn!=sgn.shift(1)).astype(float).where(~sgn.isna()&~sgn.shift(1).isna())
  b=fl.rolling(60,min_periods=60).sum()
  return b.diff(21).replace([np.inf,-np.inf],np.nan)
def f12os_f12_oscillator_family_stochrsi_14d_slope_v043_signal(close):
  n=14
  d=close.diff()
  au=_W(d,n)
  ad=_W(-d,n)
  rs=au/ad.replace(0.0,np.nan)
  rsi=100.0-100.0/(1.0+rs)
  lo=rsi.rolling(n,min_periods=n).min(); hi=rsi.rolling(n,min_periods=n).max()
  b=(rsi-lo)/(hi-lo).replace(0.0,np.nan)
  return b.diff(5).replace([np.inf,-np.inf],np.nan)
def f12os_f12_oscillator_family_stochrsi_50d_slope_v044_signal(closeadj):
  n=50
  d=closeadj.diff()
  au=_W(d,n)
  ad=_W(-d,n)
  rs=au/ad.replace(0.0,np.nan)
  rsi=100.0-100.0/(1.0+rs)
  lo=rsi.rolling(n,min_periods=n).min(); hi=rsi.rolling(n,min_periods=n).max()
  b=(rsi-lo)/(hi-lo).replace(0.0,np.nan)
  return b.diff(21).replace([np.inf,-np.inf],np.nan)
def f12os_f12_oscillator_family_chaikin_3_10_slope_v045_signal(high,low,close,volume):
  clv=((close-low)-(high-close))/(high-low).replace(0.0,np.nan)
  adl=(clv*volume).cumsum()
  b=adl.ewm(span=3,adjust=False,min_periods=3).mean()-adl.ewm(span=10,adjust=False,min_periods=10).mean()
  return b.diff(5).replace([np.inf,-np.inf],np.nan)
def f12os_f12_oscillator_family_chaikinrank_120d_slope_v046_signal(high,low,close,volume):
  clv=((close-low)-(high-close))/(high-low).replace(0.0,np.nan)
  adl=(clv*volume).cumsum()
  co=adl.ewm(span=6,adjust=False,min_periods=6).mean()-adl.ewm(span=20,adjust=False,min_periods=20).mean()
  b=co.rolling(120,min_periods=120).rank(pct=True)
  return b.diff(63).replace([np.inf,-np.inf],np.nan)
def f12os_f12_oscillator_family_klinger_34_55_slope_v047_signal(high,low,close,volume):
  tp=(high+low+close)/3.0
  trend=np.sign(tp-tp.shift(1)); dm=(high-low); cm=dm.copy()
  same=(trend==trend.shift(1))&trend.notna()&trend.shift(1).notna()
  cm=cm.where(~same,cm.shift(1)+dm)
  vf=volume*trend*(2.0*(dm/cm.replace(0.0,np.nan))-1.0)*100.0
  b=vf.ewm(span=34,adjust=False,min_periods=34).mean()-vf.ewm(span=55,adjust=False,min_periods=55).mean()
  return b.diff(21).replace([np.inf,-np.inf],np.nan)
def f12os_f12_oscillator_family_bias_10d_slope_v048_signal(close):
  n=10
  s=close.rolling(n,min_periods=n).mean()
  b=100.0*(close-s)/s.replace(0.0,np.nan)
  return (b.diff(10)/b.abs().rolling(20,min_periods=20).mean().replace(0.0,np.nan)).replace([np.inf,-np.inf],np.nan)
def f12os_f12_oscillator_family_bias_60d_slope_v049_signal(closeadj):
  n=60
  s=closeadj.rolling(n,min_periods=n).mean()
  b=100.0*(closeadj-s)/s.replace(0.0,np.nan)
  return (b.diff(10).abs()*np.sign(b.diff(10))/b.abs().rolling(60,min_periods=60).mean().replace(0.0,np.nan)).replace([np.inf,-np.inf],np.nan)
def f12os_f12_oscillator_family_rsistochzdiff_30d_slope_v050_signal(high,low,closeadj):
  n=14
  d=closeadj.diff()
  au=_W(d,n)
  ad=_W(-d,n)
  rs=au/ad.replace(0.0,np.nan)
  rsi=100.0-100.0/(1.0+rs)
  ll,hh=_LH(high,low,n)
  k=100.0*(closeadj-ll)/(hh-ll).replace(0.0,np.nan)
  zr=(rsi-rsi.rolling(60,min_periods=60).mean())/rsi.rolling(60,min_periods=60).std(ddof=1).replace(0.0,np.nan)
  zk=(k-k.rolling(60,min_periods=60).mean())/k.rolling(60,min_periods=60).std(ddof=1).replace(0.0,np.nan)
  b=zr-zk
  return b.diff(10).replace([np.inf,-np.inf],np.nan)
def f12os_f12_oscillator_family_rsicciagree_50d_slope_v051_signal(high,low,closeadj):
  n=14
  d=closeadj.diff()
  au=_W(d,n)
  ad=_W(-d,n)
  rs=au/ad.replace(0.0,np.nan)
  rsi=100.0-100.0/(1.0+rs)
  cci=_C(high,low,closeadj,20)
  prod=np.sign(rsi-50.0)*np.sign(cci)
  b=prod.rolling(50,min_periods=50).mean()
  return b.diff(21).replace([np.inf,-np.inf],np.nan)
def f12os_f12_oscillator_family_oscobcnt_30d_slope_v052_signal(high,low,closeadj):
  n=14
  d=closeadj.diff()
  au=_W(d,n)
  ad=_W(-d,n)
  rs=au/ad.replace(0.0,np.nan)
  rsi=100.0-100.0/(1.0+rs)
  ll,hh=_LH(high,low,n)
  k=100.0*(closeadj-ll)/(hh-ll).replace(0.0,np.nan)
  cci=_C(high,low,closeadj,20)
  fl=((rsi>70.0)&(k>80.0)&(cci>100.0)).astype(float).where(~rsi.isna()&~k.isna()&~cci.isna())
  b=fl.rolling(30,min_periods=30).sum()
  return b.diff(10).replace([np.inf,-np.inf],np.nan)
def f12os_f12_oscillator_family_oscdisp_30d_slope_v053_signal(high,low,closeadj):
  n=14
  d=closeadj.diff()
  au=_W(d,n)
  ad=_W(-d,n)
  rs=au/ad.replace(0.0,np.nan)
  rsi=100.0-100.0/(1.0+rs)
  ll,hh=_LH(high,low,n)
  k=100.0*(closeadj-ll)/(hh-ll).replace(0.0,np.nan)
  wr_norm=100.0+(-100.0*(hh-closeadj)/(hh-ll).replace(0.0,np.nan))
  b=pd.concat([rsi,k,wr_norm],axis=1).std(axis=1,ddof=1)
  return b.diff(10).replace([np.inf,-np.inf],np.nan)
def f12os_f12_oscillator_family_oscbullcnt_30d_slope_v054_signal(high,low,closeadj):
  n=14
  d=closeadj.diff()
  au=_W(d,n)
  ad=_W(-d,n)
  rs=au/ad.replace(0.0,np.nan)
  rsi=100.0-100.0/(1.0+rs)
  ll,hh=_LH(high,low,n)
  k=100.0*(closeadj-ll)/(hh-ll).replace(0.0,np.nan)
  wr=-100.0*(hh-closeadj)/(hh-ll).replace(0.0,np.nan)
  b=((rsi>50.0).astype(float).where(~rsi.isna())+(k>50.0).astype(float).where(~k.isna())+(wr>-50.0).astype(float).where(~wr.isna()))
  return b.diff(21).replace([np.inf,-np.inf],np.nan)
def f12os_f12_oscillator_family_stochzkurt_60d_slope_v055_signal(high,low,closeadj):
  k=_SK(high,low,closeadj,14)
  b=k.rolling(60,min_periods=60).kurt()
  return b.diff(21).replace([np.inf,-np.inf],np.nan)
def f12os_f12_oscillator_family_rsidouble_30d_slope_v056_signal(closeadj):
  n=14
  d=closeadj.diff()
  au=_W(d,n)
  ad=_W(-d,n)
  rs=au/ad.replace(0.0,np.nan)
  rsi=100.0-100.0/(1.0+rs)
  b=rsi.rolling(5,min_periods=5).mean().rolling(10,min_periods=10).mean()
  return b.diff(10).replace([np.inf,-np.inf],np.nan)
def f12os_f12_oscillator_family_stochskew_60d_slope_v057_signal(high,low,closeadj):
  k=_SK(high,low,closeadj,14)
  b=k.rolling(60,min_periods=60).skew()
  return b.diff(21).replace([np.inf,-np.inf],np.nan)
def f12os_f12_oscillator_family_rsiabs50_25d_slope_v058_signal(close):
  n=25
  d=close.diff()
  au=_W(d,n)
  ad=_W(-d,n)
  rs=au/ad.replace(0.0,np.nan)
  rsi=100.0-100.0/(1.0+rs)
  b=(rsi-50.0).abs()
  return b.diff(10).replace([np.inf,-np.inf],np.nan)
def f12os_f12_oscillator_family_stochrange_50d_slope_v059_signal(high,low,closeadj):
  k=_SK(high,low,closeadj,14)
  b=k.rolling(50,min_periods=50).max()-k.rolling(50,min_periods=50).min()
  return b.diff(21).replace([np.inf,-np.inf],np.nan)
def f12os_f12_oscillator_family_ccixsign_60d_slope_v060_signal(high,low,closeadj):
  n=20
  tp=(high+low+closeadj)/3.0
  sma=tp.rolling(n,min_periods=n).mean(); mad=(tp-sma).abs().rolling(n,min_periods=n).mean()
  cci=(tp-sma)/(0.015*mad.replace(0.0,np.nan))
  sgn=np.sign(cci)
  fl=(sgn!=sgn.shift(1)).astype(float).where(~sgn.isna()&~sgn.shift(1).isna())
  b=fl.rolling(60,min_periods=60).sum()
  return b.diff(21).replace([np.inf,-np.inf],np.nan)
def f12os_f12_oscillator_family_rsistreaktop_30d_slope_v061_signal(close):
  n=14
  d=close.diff()
  au=_W(d,n)
  ad=_W(-d,n)
  rs=au/ad.replace(0.0,np.nan)
  rsi=100.0-100.0/(1.0+rs)
  cond=(rsi>50.0).astype(float).where(~rsi.isna())
  def _st(x):
    c=0.0
    for v in x[::-1]:
      if v>0.5:c+=1.0
      else:break
    return c
  b=cond.rolling(30,min_periods=30).apply(_st,raw=True)
  return b.diff(10).replace([np.inf,-np.inf],np.nan)
def f12os_f12_oscillator_family_aoabs_50d_slope_v062_signal(high,low):
  mp=0.5*(high+low)
  b=(mp.rolling(5,min_periods=5).mean()-mp.rolling(34,min_periods=34).mean()).abs()
  return b.diff(21).replace([np.inf,-np.inf],np.nan)
def f12os_f12_oscillator_family_mfi_rsidiff_30d_slope_v063_signal(high,low,closeadj,volume):
  n=14
  tp=(high+low+closeadj)/3.0; rmf=tp*volume; dlt=tp.diff()
  pos=rmf.where(dlt>0,0.0); neg=rmf.where(dlt<0,0.0)
  mr=pos.rolling(n,min_periods=n).sum()/neg.rolling(n,min_periods=n).sum().replace(0.0,np.nan)
  mfi=100.0-100.0/(1.0+mr)
  d=closeadj.diff()
  au=_W(d,n)
  ad=_W(-d,n)
  rs=au/ad.replace(0.0,np.nan)
  rsi=100.0-100.0/(1.0+rs)
  b=mfi-rsi
  return b.diff(10).replace([np.inf,-np.inf],np.nan)
def f12os_f12_oscillator_family_stochkdpath_50d_slope_v064_signal(high,low,closeadj):
  k=_SK(high,low,closeadj,14)
  d=k.rolling(3,min_periods=3).mean()
  b=(k-d).abs().rolling(50,min_periods=50).sum()
  return b.diff(21).replace([np.inf,-np.inf],np.nan)
def f12os_f12_oscillator_family_uoslp_30d_slope_v065_signal(high,low,closeadj):
  uo=_UO(high,low,closeadj)
  b=uo.diff(10)
  return b.diff(10).replace([np.inf,-np.inf],np.nan)
def f12os_f12_oscillator_family_dpostreak_30d_slope_v066_signal(closeadj):
  n=40
  s=closeadj-closeadj.rolling(n,min_periods=n).mean().shift(n//2+1)
  cond=(s>0.0).astype(float).where(~s.isna())
  def _st(x):
    c=0.0
    for v in x[::-1]:
      if v>0.5:c+=1.0
      else:break
    return c
  b=cond.rolling(30,min_periods=30).apply(_st,raw=True)
  return b.diff(10).replace([np.inf,-np.inf],np.nan)
def f12os_f12_oscillator_family_stochrsisma_21d_slope_v067_signal(close):
  n=14
  d=close.diff()
  au=_W(d,n)
  ad=_W(-d,n)
  rs=au/ad.replace(0.0,np.nan)
  rsi=100.0-100.0/(1.0+rs)
  lo=rsi.rolling(n,min_periods=n).min(); hi=rsi.rolling(n,min_periods=n).max()
  srsi=(rsi-lo)/(hi-lo).replace(0.0,np.nan)
  b=srsi.rolling(7,min_periods=7).mean()
  return b.diff(5).replace([np.inf,-np.inf],np.nan)
def f12os_f12_oscillator_family_aobullbear_50d_slope_v068_signal(high,low):
  mp=0.5*(high+low)
  ao=mp.rolling(5,min_periods=5).mean()-mp.rolling(34,min_periods=34).mean()
  fl=(ao>0.0).astype(float).where(~ao.isna())
  b=fl.rolling(50,min_periods=50).mean()
  return b.diff(21).replace([np.inf,-np.inf],np.nan)
def f12os_f12_oscillator_family_biaspct_30d_slope_v069_signal(closeadj):
  n=20
  s=closeadj.rolling(n,min_periods=n).mean()
  bv=100.0*(closeadj-s)/s.replace(0.0,np.nan)
  b=bv.rolling(120,min_periods=120).rank(pct=True)
  return b.diff(21).replace([np.inf,-np.inf],np.nan)
def f12os_f12_oscillator_family_ccinegrun_30d_slope_v070_signal(high,low,closeadj):
  n=14
  tp=(high+low+closeadj)/3.0
  sma=tp.rolling(n,min_periods=n).mean(); mad=(tp-sma).abs().rolling(n,min_periods=n).mean()
  cci=(tp-sma)/(0.015*mad.replace(0.0,np.nan))
  cond=(cci<-100.0).astype(float).where(~cci.isna())
  def _st(x):
    c=0.0
    for v in x[::-1]:
      if v>0.5:c+=1.0
      else:break
    return c
  b=cond.rolling(30,min_periods=30).apply(_st,raw=True)
  return b.diff(10).replace([np.inf,-np.inf],np.nan)
def f12os_f12_oscillator_family_rsimedian_60d_slope_v071_signal(closeadj):
  n=14
  d=closeadj.diff()
  au=_W(d,n)
  ad=_W(-d,n)
  rs=au/ad.replace(0.0,np.nan)
  rsi=100.0-100.0/(1.0+rs)
  b=rsi.rolling(60,min_periods=60).median()
  return b.diff(21).replace([np.inf,-np.inf],np.nan)
def f12os_f12_oscillator_family_mfivlog_50d_slope_v072_signal(high,low,closeadj,volume):
  n=50
  tp=(high+low+closeadj)/3.0; rmf=tp*volume; dlt=tp.diff()
  pos=rmf.where(dlt>0,0.0); neg=rmf.where(dlt<0,0.0)
  mr=pos.rolling(n,min_periods=n).sum()/neg.rolling(n,min_periods=n).sum().replace(0.0,np.nan)
  mfi=100.0-100.0/(1.0+mr)
  b=np.log(mfi.replace(0.0,np.nan)/(100.0-mfi).replace(0.0,np.nan))
  return b.diff(10).replace([np.inf,-np.inf],np.nan)
def f12os_f12_oscillator_family_chaikinsign_40d_slope_v073_signal(high,low,close,volume):
  clv=((close-low)-(high-close))/(high-low).replace(0.0,np.nan)
  adl=(clv*volume).cumsum()
  co=adl.ewm(span=3,adjust=False,min_periods=3).mean()-adl.ewm(span=10,adjust=False,min_periods=10).mean()
  b=np.sign(co)
  return b.diff(21).replace([np.inf,-np.inf],np.nan)
def f12os_f12_oscillator_family_stochkrng_50d_slope_v074_signal(high,low,close):
  k=_SK(high,low,close,14)
  b=k-k.rolling(50,min_periods=50).mean()
  return b.diff(21).replace([np.inf,-np.inf],np.nan)
def f12os_f12_oscillator_family_rsivolratio_30d_slope_v075_signal(closeadj):
  n1=7; d=closeadj.diff()
  au1=_W(d,n1)
  ad1=_W(-d,n1)
  rs1=au1/ad1.replace(0.0,np.nan); r1=100.0-100.0/(1.0+rs1)
  n2=50
  au2=_W(d,n2)
  ad2=_W(-d,n2)
  rs2=au2/ad2.replace(0.0,np.nan); r2=100.0-100.0/(1.0+rs2)
  b=(r1-r2)/((r1-50.0).abs()+(r2-50.0).abs()+1.0)
  return b.diff(10).replace([np.inf,-np.inf],np.nan)

# --- File 2 slopes (v076-v150) ---
def f12os_f12_oscillator_family_rsi_21d_slope_v076_signal(close):
  n=21
  d=close.diff()
  au=_W(d,n)
  ad=_W(-d,n)
  rs=au/ad.replace(0.0,np.nan)
  b=100.0-100.0/(1.0+rs)
  return b.diff(10).replace([np.inf,-np.inf],np.nan)
def f12os_f12_oscillator_family_rsi_100d_slope_v077_signal(closeadj):
  n=100
  d=closeadj.diff()
  au=_W(d,n)
  ad=_W(-d,n)
  rs=au/ad.replace(0.0,np.nan)
  b=100.0-100.0/(1.0+rs)
  return b.diff(63).replace([np.inf,-np.inf],np.nan)
def f12os_f12_oscillator_family_rsiema_30d_slope_v078_signal(closeadj):
  n=14
  d=closeadj.diff()
  au=_W(d,n)
  ad=_W(-d,n)
  rs=au/ad.replace(0.0,np.nan)
  rsi=100.0-100.0/(1.0+rs)
  b=rsi.ewm(span=10,adjust=False,min_periods=10).mean()
  return b.diff(10).replace([np.inf,-np.inf],np.nan)
def f12os_f12_oscillator_family_rsiceil_120d_slope_v079_signal(closeadj):
  n=14
  d=closeadj.diff()
  au=_W(d,n)
  ad=_W(-d,n)
  rs=au/ad.replace(0.0,np.nan)
  rsi=100.0-100.0/(1.0+rs)
  b=rsi.rolling(120,min_periods=120).max()
  return b.diff(21).replace([np.inf,-np.inf],np.nan)
def f12os_f12_oscillator_family_rsispan_80d_slope_v080_signal(closeadj):
  n=14
  d=closeadj.diff()
  au=_W(d,n)
  ad=_W(-d,n)
  rs=au/ad.replace(0.0,np.nan)
  rsi=100.0-100.0/(1.0+rs)
  b=rsi.rolling(80,min_periods=80).max()-rsi.rolling(80,min_periods=80).min()
  return b.diff(21).replace([np.inf,-np.inf],np.nan)
def f12os_f12_oscillator_family_rsistreakbot_30d_slope_v081_signal(closeadj):
  n=14
  d=closeadj.diff()
  au=_W(d,n)
  ad=_W(-d,n)
  rs=au/ad.replace(0.0,np.nan)
  rsi=100.0-100.0/(1.0+rs)
  cond=(rsi<50.0).astype(float).where(~rsi.isna())
  def _st(x):
    c=0.0
    for v in x[::-1]:
      if v>0.5:c+=1.0
      else:break
    return c
  b=cond.rolling(30,min_periods=30).apply(_st,raw=True)
  return b.diff(10).replace([np.inf,-np.inf],np.nan)
def f12os_f12_oscillator_family_rsiextrm_80d_slope_v082_signal(closeadj):
  n=14
  d=closeadj.diff()
  au=_W(d,n)
  ad=_W(-d,n)
  rs=au/ad.replace(0.0,np.nan)
  rsi=100.0-100.0/(1.0+rs)
  fl=((rsi>70.0)|(rsi<30.0)).astype(float).where(~rsi.isna())
  b=fl.rolling(80,min_periods=80).sum()
  return b.diff(21).replace([np.inf,-np.inf],np.nan)
def f12os_f12_oscillator_family_rsiiqr_60d_slope_v083_signal(closeadj):
  n=14
  d=closeadj.diff()
  au=_W(d,n)
  ad=_W(-d,n)
  rs=au/ad.replace(0.0,np.nan)
  rsi=100.0-100.0/(1.0+rs)
  b=rsi.rolling(60,min_periods=60).quantile(0.75)-rsi.rolling(60,min_periods=60).quantile(0.25)
  return b.diff(21).replace([np.inf,-np.inf],np.nan)
def f12os_f12_oscillator_family_rsigap_30d_slope_v084_signal(closeadj):
  n=14
  d=closeadj.diff()
  au=_W(d,n)
  ad=_W(-d,n)
  rs=au/ad.replace(0.0,np.nan)
  rsi=100.0-100.0/(1.0+rs)
  b=rsi-rsi.rolling(30,min_periods=30).median()
  return b.diff(21).replace([np.inf,-np.inf],np.nan)
def f12os_f12_oscillator_family_rsisig_15d_slope_v085_signal(close):
  n=2
  d=close.diff()
  au=_W(d,n)
  ad=_W(-d,n)
  rs=au/ad.replace(0.0,np.nan)
  b=100.0-100.0/(1.0+rs)
  return b.diff(5).replace([np.inf,-np.inf],np.nan)
def f12os_f12_oscillator_family_stochk_21d_slope_v086_signal(high,low,close):
  b=_SK(high,low,close,21)
  return b.diff(10).replace([np.inf,-np.inf],np.nan)
def f12os_f12_oscillator_family_stochkpos_50d_slope_v087_signal(high,low,closeadj):
  k=_SK(high,low,closeadj,14)
  b=(k>50.0).astype(float).where(~k.isna()).rolling(50,min_periods=50).sum()
  return b.diff(21).replace([np.inf,-np.inf],np.nan)
def f12os_f12_oscillator_family_stochds_80d_slope_v088_signal(high,low,closeadj):
  k=_SK(high,low,closeadj,14)
  cond=(k>80.0).astype(float).where(~k.isna())
  def _ds(x):
    idx=np.where(x>0.5)[0]
    if idx.size==0:return 80.0
    return float(len(x)-1-idx[-1])
  b=cond.rolling(80,min_periods=80).apply(_ds,raw=True)
  return b.diff(21).replace([np.inf,-np.inf],np.nan)
def f12os_f12_oscillator_family_stochkmed_120d_slope_v089_signal(high,low,closeadj):
  k=_SK(high,low,closeadj,14)
  b=k.rolling(120,min_periods=120).median()
  return b.diff(63).replace([np.inf,-np.inf],np.nan)
def f12os_f12_oscillator_family_stochkdslp_30d_slope_v090_signal(high,low,closeadj):
  k=_SK(high,low,closeadj,14)
  d=k.rolling(3,min_periods=3).mean()
  b=(k-d).diff(5)
  return b.diff(10).replace([np.inf,-np.inf],np.nan)
def f12os_f12_oscillator_family_stochwidemar_100d_slope_v091_signal(high,low,closeadj):
  n=100
  ll,hh=_LH(high,low,n)
  rng=(hh-ll).replace(0.0,np.nan)
  top=(hh-closeadj)/rng; bot=(closeadj-ll)/rng
  b=pd.concat([top,bot],axis=1).min(axis=1)
  return b.diff(21).replace([np.inf,-np.inf],np.nan)
def f12os_f12_oscillator_family_willrslp_50d_slope_v093_signal(high,low,closeadj):
  wr=_WR(high,low,closeadj,28)
  b=wr.diff(10)
  return b.diff(21).replace([np.inf,-np.inf],np.nan)
def f12os_f12_oscillator_family_willrxhi_50d_slope_v094_signal(high,low,closeadj):
  wr=_WR(high,low,closeadj,21)
  b=(wr>-20.0).astype(float).where(~wr.isna()).rolling(50,min_periods=50).mean()
  return b.diff(21).replace([np.inf,-np.inf],np.nan)
def f12os_f12_oscillator_family_cci_30d_slope_v095_signal(high,low,closeadj):
  n=30
  tp=(high+low+closeadj)/3.0
  sma=tp.rolling(n,min_periods=n).mean(); mad=(tp-sma).abs().rolling(n,min_periods=n).mean()
  b=(tp-sma)/(0.015*mad.replace(0.0,np.nan))
  return b.diff(21).replace([np.inf,-np.inf],np.nan)
def f12os_f12_oscillator_family_ccislope_50d_slope_v096_signal(high,low,closeadj):
  n=20
  tp=(high+low+closeadj)/3.0
  sma=tp.rolling(n,min_periods=n).mean(); mad=(tp-sma).abs().rolling(n,min_periods=n).mean()
  cci=(tp-sma)/(0.015*mad.replace(0.0,np.nan))
  b=cci.diff(10)
  return b.diff(21).replace([np.inf,-np.inf],np.nan)
def f12os_f12_oscillator_family_ccipos_60d_slope_v097_signal(high,low,closeadj):
  n=14
  tp=(high+low+closeadj)/3.0
  sma=tp.rolling(n,min_periods=n).mean(); mad=(tp-sma).abs().rolling(n,min_periods=n).mean()
  cci=(tp-sma)/(0.015*mad.replace(0.0,np.nan))
  b=(cci>0.0).astype(float).where(~cci.isna()).rolling(60,min_periods=60).mean()
  return b.diff(21).replace([np.inf,-np.inf],np.nan)
def f12os_f12_oscillator_family_cciskew_60d_slope_v098_signal(high,low,closeadj):
  n=30
  tp=(high+low+closeadj)/3.0
  sma=tp.rolling(n,min_periods=n).mean(); mad=(tp-sma).abs().rolling(n,min_periods=n).mean()
  cci=(tp-sma)/(0.015*mad.replace(0.0,np.nan))
  b=cci.rolling(60,min_periods=60).skew()
  return b.diff(21).replace([np.inf,-np.inf],np.nan)
def f12os_f12_oscillator_family_cciosmin_60d_slope_v099_signal(high,low,closeadj):
  n=20
  tp=(high+low+closeadj)/3.0
  sma=tp.rolling(n,min_periods=n).mean(); mad=(tp-sma).abs().rolling(n,min_periods=n).mean()
  cci=(tp-sma)/(0.015*mad.replace(0.0,np.nan))
  b=cci.rolling(60,min_periods=60).min()
  return b.diff(21).replace([np.inf,-np.inf],np.nan)
def f12os_f12_oscillator_family_ccids_60d_slope_v100_signal(high,low,closeadj):
  n=20
  tp=(high+low+closeadj)/3.0
  sma=tp.rolling(n,min_periods=n).mean(); mad=(tp-sma).abs().rolling(n,min_periods=n).mean()
  cci=(tp-sma)/(0.015*mad.replace(0.0,np.nan))
  cond=(cci>100.0).astype(float).where(~cci.isna())
  def _ds(x):
    idx=np.where(x>0.5)[0]
    if idx.size==0:return 60.0
    return float(len(x)-1-idx[-1])
  b=cond.rolling(60,min_periods=60).apply(_ds,raw=True)
  return b.diff(21).replace([np.inf,-np.inf],np.nan)
def f12os_f12_oscillator_family_mfi_50d_slope_v101_signal(high,low,closeadj,volume):
  n=50
  tp=(high+low+closeadj)/3.0; rmf=tp*volume; dlt=tp.diff()
  pos=rmf.where(dlt>0,0.0); neg=rmf.where(dlt<0,0.0)
  mr=pos.rolling(n,min_periods=n).sum()/neg.rolling(n,min_periods=n).sum().replace(0.0,np.nan)
  b=100.0-100.0/(1.0+mr)
  return b.diff(21).replace([np.inf,-np.inf],np.nan)
def f12os_f12_oscillator_family_mfiob_50d_slope_v102_signal(high,low,closeadj,volume):
  n=14
  tp=(high+low+closeadj)/3.0; rmf=tp*volume; dlt=tp.diff()
  pos=rmf.where(dlt>0,0.0); neg=rmf.where(dlt<0,0.0)
  mr=pos.rolling(n,min_periods=n).sum()/neg.rolling(n,min_periods=n).sum().replace(0.0,np.nan)
  mfi=100.0-100.0/(1.0+mr)
  b=(mfi>80.0).astype(float).where(~mfi.isna()).rolling(50,min_periods=50).mean()
  return b.diff(21).replace([np.inf,-np.inf],np.nan)
def f12os_f12_oscillator_family_mfislp_30d_slope_v103_signal(high,low,closeadj,volume):
  n=14
  tp=(high+low+closeadj)/3.0; rmf=tp*volume; dlt=tp.diff()
  pos=rmf.where(dlt>0,0.0); neg=rmf.where(dlt<0,0.0)
  mr=pos.rolling(n,min_periods=n).sum()/neg.rolling(n,min_periods=n).sum().replace(0.0,np.nan)
  mfi=100.0-100.0/(1.0+mr)
  b=mfi.diff(5)
  return b.diff(10).replace([np.inf,-np.inf],np.nan)
def f12os_f12_oscillator_family_mfidsos_80d_slope_v104_signal(high,low,closeadj,volume):
  n=14
  tp=(high+low+closeadj)/3.0; rmf=tp*volume; dlt=tp.diff()
  pos=rmf.where(dlt>0,0.0); neg=rmf.where(dlt<0,0.0)
  mr=pos.rolling(n,min_periods=n).sum()/neg.rolling(n,min_periods=n).sum().replace(0.0,np.nan)
  mfi=100.0-100.0/(1.0+mr)
  cond=(mfi<20.0).astype(float).where(~mfi.isna())
  def _ds(x):
    idx=np.where(x>0.5)[0]
    if idx.size==0:return 80.0
    return float(len(x)-1-idx[-1])
  b=cond.rolling(80,min_periods=80).apply(_ds,raw=True)
  return b.diff(21).replace([np.inf,-np.inf],np.nan)
def f12os_f12_oscillator_family_uodefault_slope_v105_signal(high,low,closeadj):
  b=_UO(high,low,closeadj)
  return b.diff(21).replace([np.inf,-np.inf],np.nan)
def f12os_f12_oscillator_family_uoob_50d_slope_v106_signal(high,low,closeadj):
  uo=_UO(high,low,closeadj)
  b=(uo>70.0).astype(float).where(~uo.isna()).rolling(50,min_periods=50).mean()
  return b.diff(21).replace([np.inf,-np.inf],np.nan)
def f12os_f12_oscillator_family_uorng_80d_slope_v107_signal(high,low,closeadj):
  uo=_UO(high,low,closeadj)
  b=uo.rolling(80,min_periods=80).max()-uo.rolling(80,min_periods=80).min()
  return b.diff(21).replace([np.inf,-np.inf],np.nan)
def f12os_f12_oscillator_family_aoxsign_60d_slope_v108_signal(high,low):
  mp=0.5*(high+low)
  ao=mp.rolling(5,min_periods=5).mean()-mp.rolling(34,min_periods=34).mean()
  sgn=np.sign(ao)
  fl=(sgn!=sgn.shift(1)).astype(float).where(~sgn.isna()&~sgn.shift(1).isna())
  b=fl.rolling(60,min_periods=60).sum()
  return b.diff(21).replace([np.inf,-np.inf],np.nan)
def f12os_f12_oscillator_family_aosig_30d_slope_v109_signal(high,low):
  mp=0.5*(high+low)
  ao=mp.rolling(5,min_periods=5).mean()-mp.rolling(34,min_periods=34).mean()
  sd=ao.rolling(80,min_periods=80).std(ddof=1)
  b=ao/sd.replace(0.0,np.nan)
  return b.diff(21).replace([np.inf,-np.inf],np.nan)
def f12os_f12_oscillator_family_aoslp_50d_slope_v110_signal(high,low):
  mp=0.5*(high+low)
  ao=mp.rolling(5,min_periods=5).mean()-mp.rolling(34,min_periods=34).mean()
  b=ao.diff(5)
  return b.diff(21).replace([np.inf,-np.inf],np.nan)
def f12os_f12_oscillator_family_dpo_30d_slope_v111_signal(closeadj):
  n=30
  b=closeadj-closeadj.rolling(n,min_periods=n).mean().shift(n//2+1)
  return b.diff(21).replace([np.inf,-np.inf],np.nan)
def f12os_f12_oscillator_family_dpoabs_50d_slope_v112_signal(closeadj):
  n=50
  b=(closeadj-closeadj.rolling(n,min_periods=n).mean().shift(n//2+1)).abs()
  return b.diff(21).replace([np.inf,-np.inf],np.nan)
def f12os_f12_oscillator_family_stochrsi_7d_slope_v113_signal(close):
  n=7
  d=close.diff()
  au=_W(d,n)
  ad=_W(-d,n)
  rs=au/ad.replace(0.0,np.nan)
  rsi=100.0-100.0/(1.0+rs)
  lo=rsi.rolling(n,min_periods=n).min(); hi=rsi.rolling(n,min_periods=n).max()
  b=(rsi-lo)/(hi-lo).replace(0.0,np.nan)
  return b.diff(5).replace([np.inf,-np.inf],np.nan)
def f12os_f12_oscillator_family_stochrsiob_30d_slope_v114_signal(closeadj):
  n=14
  d=closeadj.diff()
  au=_W(d,n)
  ad=_W(-d,n)
  rs=au/ad.replace(0.0,np.nan)
  rsi=100.0-100.0/(1.0+rs)
  lo=rsi.rolling(n,min_periods=n).min(); hi=rsi.rolling(n,min_periods=n).max()
  srsi=(rsi-lo)/(hi-lo).replace(0.0,np.nan)
  b=(srsi>0.8).astype(float).where(~srsi.isna()).rolling(30,min_periods=30).sum()
  return b.diff(10).replace([np.inf,-np.inf],np.nan)
def f12os_f12_oscillator_family_chaikin_10_30_slope_v115_signal(high,low,closeadj,volume):
  clv=((closeadj-low)-(high-closeadj))/(high-low).replace(0.0,np.nan)
  adl=(clv*volume).cumsum()
  b=adl.ewm(span=10,adjust=False,min_periods=10).mean()-adl.ewm(span=30,adjust=False,min_periods=30).mean()
  return b.diff(21).replace([np.inf,-np.inf],np.nan)
def f12os_f12_oscillator_family_chaikinxs_60d_slope_v116_signal(high,low,close,volume):
  clv=((close-low)-(high-close))/(high-low).replace(0.0,np.nan)
  adl=(clv*volume).cumsum()
  co=adl.ewm(span=3,adjust=False,min_periods=3).mean()-adl.ewm(span=10,adjust=False,min_periods=10).mean()
  sgn=np.sign(co)
  fl=(sgn!=sgn.shift(1)).astype(float).where(~sgn.isna()&~sgn.shift(1).isna())
  b=fl.rolling(60,min_periods=60).sum()
  return b.diff(21).replace([np.inf,-np.inf],np.nan)
def f12os_f12_oscillator_family_klingertanh_30d_slope_v117_signal(high,low,closeadj,volume):
  tp=(high+low+closeadj)/3.0
  trend=np.sign(tp-tp.shift(1)); dm=(high-low); cm=dm.copy()
  same=(trend==trend.shift(1))&trend.notna()&trend.shift(1).notna()
  cm=cm.where(~same,cm.shift(1)+dm)
  vf=volume*trend*(2.0*(dm/cm.replace(0.0,np.nan))-1.0)*100.0
  kvo=vf.ewm(span=34,adjust=False,min_periods=34).mean()-vf.ewm(span=55,adjust=False,min_periods=55).mean()
  sd=kvo.rolling(60,min_periods=60).std(ddof=1)
  b=np.tanh(kvo/sd.replace(0.0,np.nan))
  return b.diff(21).replace([np.inf,-np.inf],np.nan)
def f12os_f12_oscillator_family_bias_20d_slope_v118_signal(close):
  n=20
  s=close.rolling(n,min_periods=n).mean()
  b=100.0*(close-s)/s.replace(0.0,np.nan)
  return (b.diff(10)/b.abs().rolling(30,min_periods=30).mean().replace(0.0,np.nan)).replace([np.inf,-np.inf],np.nan)
def f12os_f12_oscillator_family_biasxsign_40d_slope_v119_signal(closeadj):
  n=20
  s=closeadj.rolling(n,min_periods=n).mean()
  bv=100.0*(closeadj-s)/s.replace(0.0,np.nan)
  sgn=np.sign(bv)
  fl=(sgn!=sgn.shift(1)).astype(float).where(~sgn.isna()&~sgn.shift(1).isna())
  b=fl.rolling(40,min_periods=40).sum()
  return b.diff(10).replace([np.inf,-np.inf],np.nan)
def f12os_f12_oscillator_family_rsimficorr_60d_slope_v120_signal(high,low,closeadj,volume):
  n=14
  d=closeadj.diff()
  au=_W(d,n)
  ad=_W(-d,n)
  rs=au/ad.replace(0.0,np.nan)
  rsi=100.0-100.0/(1.0+rs)
  tp=(high+low+closeadj)/3.0; rmf=tp*volume; dlt=tp.diff()
  pos=rmf.where(dlt>0,0.0); neg=rmf.where(dlt<0,0.0)
  mr=pos.rolling(n,min_periods=n).sum()/neg.rolling(n,min_periods=n).sum().replace(0.0,np.nan)
  mfi=100.0-100.0/(1.0+mr)
  b=rsi.rolling(60,min_periods=60).corr(mfi)
  return b.diff(21).replace([np.inf,-np.inf],np.nan)
def f12os_f12_oscillator_family_rsiccixdcorr_50d_slope_v121_signal(high,low,closeadj):
  n=14
  d=closeadj.diff()
  au=_W(d,n)
  ad=_W(-d,n)
  rs=au/ad.replace(0.0,np.nan)
  rsi=100.0-100.0/(1.0+rs)
  cci=_C(high,low,closeadj,20)
  b=rsi.rolling(50,min_periods=50).corr(cci)
  return b.diff(21).replace([np.inf,-np.inf],np.nan)
def f12os_f12_oscillator_family_oscbearcnt_30d_slope_v122_signal(high,low,closeadj):
  n=14
  d=closeadj.diff()
  au=_W(d,n)
  ad=_W(-d,n)
  rs=au/ad.replace(0.0,np.nan)
  rsi=100.0-100.0/(1.0+rs)
  ll,hh=_LH(high,low,n)
  k=100.0*(closeadj-ll)/(hh-ll).replace(0.0,np.nan)
  cci=_C(high,low,closeadj,20)
  fl=((rsi<30.0)&(k<20.0)&(cci<-100.0)).astype(float).where(~rsi.isna()&~k.isna()&~cci.isna())
  b=fl.rolling(30,min_periods=30).sum()
  return b.diff(10).replace([np.inf,-np.inf],np.nan)
def f12os_f12_oscillator_family_oscavgcent_30d_slope_v123_signal(high,low,closeadj):
  n=14
  d=closeadj.diff()
  au=_W(d,n)
  ad=_W(-d,n)
  rs=au/ad.replace(0.0,np.nan)
  rsi=100.0-100.0/(1.0+rs)
  ll,hh=_LH(high,low,n)
  k=100.0*(closeadj-ll)/(hh-ll).replace(0.0,np.nan)
  wr=-100.0*(hh-closeadj)/(hh-ll).replace(0.0,np.nan)
  cci=_C(high,low,closeadj,20)
  cci_b=25.0*np.tanh(cci/100.0)
  b=((rsi-50.0)+(k-50.0)+(wr+50.0)+cci_b)/4.0
  return b.diff(5).replace([np.inf,-np.inf],np.nan)
def f12os_f12_oscillator_family_rsicvar_50d_slope_v124_signal(closeadj):
  n=50
  d=closeadj.diff()
  au=_W(d,n)
  ad=_W(-d,n)
  rs=au/ad.replace(0.0,np.nan)
  rsi=100.0-100.0/(1.0+rs)
  mu=rsi.rolling(80,min_periods=80).mean(); sd=rsi.rolling(80,min_periods=80).std(ddof=1)
  b=sd/((mu-50.0).abs()+1.0)
  return b.diff(21).replace([np.inf,-np.inf],np.nan)
def f12os_f12_oscillator_family_stochstd_60d_slope_v125_signal(high,low,closeadj):
  k=_SK(high,low,closeadj,30)
  b=k.rolling(60,min_periods=60).std(ddof=1)
  return b.diff(21).replace([np.inf,-np.inf],np.nan)
def f12os_f12_oscillator_family_cciarctan_60d_slope_v126_signal(high,low,closeadj):
  n=60
  tp=(high+low+closeadj)/3.0
  sma=tp.rolling(n,min_periods=n).mean(); mad=(tp-sma).abs().rolling(n,min_periods=n).mean()
  cci=(tp-sma)/(0.015*mad.replace(0.0,np.nan))
  b=np.arctan(cci/200.0)
  return b.diff(63).replace([np.inf,-np.inf],np.nan)
def f12os_f12_oscillator_family_ccistreaktop_30d_slope_v127_signal(high,low,closeadj):
  n=14
  tp=(high+low+closeadj)/3.0
  sma=tp.rolling(n,min_periods=n).mean(); mad=(tp-sma).abs().rolling(n,min_periods=n).mean()
  cci=(tp-sma)/(0.015*mad.replace(0.0,np.nan))
  cond=(cci>100.0).astype(float).where(~cci.isna())
  def _st(x):
    c=0.0
    for v in x[::-1]:
      if v>0.5:c+=1.0
      else:break
    return c
  b=cond.rolling(30,min_periods=30).apply(_st,raw=True)
  return b.diff(10).replace([np.inf,-np.inf],np.nan)
def f12os_f12_oscillator_family_mfistreakob_30d_slope_v128_signal(high,low,closeadj,volume):
  n=14
  tp=(high+low+closeadj)/3.0; rmf=tp*volume; dlt=tp.diff()
  pos=rmf.where(dlt>0,0.0); neg=rmf.where(dlt<0,0.0)
  mr=pos.rolling(n,min_periods=n).sum()/neg.rolling(n,min_periods=n).sum().replace(0.0,np.nan)
  mfi=100.0-100.0/(1.0+mr)
  cond=(mfi>80.0).astype(float).where(~mfi.isna())
  def _st(x):
    c=0.0
    for v in x[::-1]:
      if v>0.5:c+=1.0
      else:break
    return c
  b=cond.rolling(30,min_periods=30).apply(_st,raw=True)
  return b.diff(10).replace([np.inf,-np.inf],np.nan)
def f12os_f12_oscillator_family_rsiparity_50d_slope_v129_signal(closeadj):
  n1=14; d=closeadj.diff()
  au=_W(d,n1)
  ad=_W(-d,n1)
  rs=au/ad.replace(0.0,np.nan); r1=100.0-100.0/(1.0+rs)
  n2=50
  au2=_W(d,n2)
  ad2=_W(-d,n2)
  rs2=au2/ad2.replace(0.0,np.nan); r2=100.0-100.0/(1.0+rs2)
  agr=(np.sign(r1-50.0)==np.sign(r2-50.0)).astype(float).where(~r1.isna()&~r2.isna())
  b=agr.rolling(50,min_periods=50).sum()
  return b.diff(21).replace([np.inf,-np.inf],np.nan)
def f12os_f12_oscillator_family_oscobds_60d_slope_v130_signal(high,low,closeadj):
  n=14
  d=closeadj.diff()
  au=_W(d,n)
  ad=_W(-d,n)
  rs=au/ad.replace(0.0,np.nan)
  rsi=100.0-100.0/(1.0+rs)
  ll,hh=_LH(high,low,n)
  k=100.0*(closeadj-ll)/(hh-ll).replace(0.0,np.nan)
  cci=_C(high,low,closeadj,20)
  cond=((rsi>70.0)&(k>80.0)&(cci>100.0)).astype(float).where(~rsi.isna()&~k.isna()&~cci.isna())
  def _ds(x):
    idx=np.where(x>0.5)[0]
    if idx.size==0:return 60.0
    return float(len(x)-1-idx[-1])
  b=cond.rolling(60,min_periods=60).apply(_ds,raw=True)
  return b.diff(10).replace([np.inf,-np.inf],np.nan)
def f12os_f12_oscillator_family_trix_15d_slope_v131_signal(closeadj):
  n=15
  e1=np.log(closeadj).ewm(span=n,adjust=False,min_periods=n).mean()
  e2=e1.ewm(span=n,adjust=False,min_periods=n).mean()
  e3=e2.ewm(span=n,adjust=False,min_periods=n).mean()
  b=10000.0*e3.diff()
  return b.diff(10).replace([np.inf,-np.inf],np.nan)
def f12os_f12_oscillator_family_trix_30d_slope_v132_signal(closeadj):
  n=30
  e1=np.log(closeadj).ewm(span=n,adjust=False,min_periods=n).mean()
  e2=e1.ewm(span=n,adjust=False,min_periods=n).mean()
  e3=e2.ewm(span=n,adjust=False,min_periods=n).mean()
  b=10000.0*e3.diff()
  return b.diff(21).replace([np.inf,-np.inf],np.nan)
def f12os_f12_oscillator_family_fisherwr_10d_slope_v133_signal(high,low,close):
  wr=_WR(high,low,close,10)
  x=((wr+50.0)/50.0).clip(-0.999,0.999)
  b=0.5*np.log((1.0+x)/(1.0-x))
  return b.diff(5).replace([np.inf,-np.inf],np.nan)
def f12os_f12_oscillator_family_kvarstd_50d_slope_v134_signal(high,low,close):
  k=_SK(high,low,close,14)
  mu=k.rolling(50,min_periods=50).mean(); sd=k.rolling(50,min_periods=50).std(ddof=1)
  b=sd/((mu-50.0).abs()+1.0)
  return b.diff(10).replace([np.inf,-np.inf],np.nan)
def f12os_f12_oscillator_family_stochrsi_30d_slope_v135_signal(closeadj):
  n=30
  d=closeadj.diff()
  au=_W(d,n)
  ad=_W(-d,n)
  rs=au/ad.replace(0.0,np.nan)
  rsi=100.0-100.0/(1.0+rs)
  lo=rsi.rolling(n,min_periods=n).min(); hi=rsi.rolling(n,min_periods=n).max()
  b=(rsi-lo)/(hi-lo).replace(0.0,np.nan)
  return b.diff(10).replace([np.inf,-np.inf],np.nan)
def f12os_f12_oscillator_family_stochrsixs_50d_slope_v136_signal(closeadj):
  n=14
  d=closeadj.diff()
  au=_W(d,n)
  ad=_W(-d,n)
  rs=au/ad.replace(0.0,np.nan)
  rsi=100.0-100.0/(1.0+rs)
  lo=rsi.rolling(n,min_periods=n).min(); hi=rsi.rolling(n,min_periods=n).max()
  srsi=(rsi-lo)/(hi-lo).replace(0.0,np.nan)
  sgn=np.sign(srsi-0.5)
  fl=(sgn!=sgn.shift(1)).astype(float).where(~sgn.isna()&~sgn.shift(1).isna())
  b=fl.rolling(50,min_periods=50).sum()
  return b.diff(21).replace([np.inf,-np.inf],np.nan)
def f12os_f12_oscillator_family_pctrnk_clmid_50d_slope_v137_signal(closeadj):
  b=(closeadj.rolling(50,min_periods=50).rank(pct=True)-0.5).abs()
  return b.diff(21).replace([np.inf,-np.inf],np.nan)
def f12os_f12_oscillator_family_pctrnk_hldiff_120d_slope_v138_signal(high,low):
  b=(high-low).rolling(120,min_periods=120).rank(pct=True)
  return b.diff(63).replace([np.inf,-np.inf],np.nan)
def f12os_f12_oscillator_family_uovariation_30d_slope_v139_signal(high,low,closeadj):
  uo=_UO(high,low,closeadj)
  b=uo.rolling(80,min_periods=80).std(ddof=1)
  return b.diff(21).replace([np.inf,-np.inf],np.nan)
def f12os_f12_oscillator_family_ccixdmu_60d_slope_v140_signal(high,low,closeadj):
  n=60
  tp=(high+low+closeadj)/3.0
  sma=tp.rolling(n,min_periods=n).mean(); mad=(tp-sma).abs().rolling(n,min_periods=n).mean()
  cci=(tp-sma)/(0.015*mad.replace(0.0,np.nan))
  b=cci-cci.rolling(30,min_periods=30).mean()
  return b.diff(21).replace([np.inf,-np.inf],np.nan)
def f12os_f12_oscillator_family_ccislpsign_60d_slope_v141_signal(high,low,closeadj):
  n=20
  tp=(high+low+closeadj)/3.0
  sma=tp.rolling(n,min_periods=n).mean(); mad=(tp-sma).abs().rolling(n,min_periods=n).mean()
  cci=(tp-sma)/(0.015*mad.replace(0.0,np.nan))
  b=np.sign(cci.diff(10))
  return b.diff(21).replace([np.inf,-np.inf],np.nan)
def f12os_f12_oscillator_family_klingersign_30d_slope_v142_signal(high,low,closeadj,volume):
  tp=(high+low+closeadj)/3.0
  trend=np.sign(tp-tp.shift(1)); dm=(high-low); cm=dm.copy()
  same=(trend==trend.shift(1))&trend.notna()&trend.shift(1).notna()
  cm=cm.where(~same,cm.shift(1)+dm)
  vf=volume*trend*(2.0*(dm/cm.replace(0.0,np.nan))-1.0)*100.0
  kvo=vf.ewm(span=34,adjust=False,min_periods=34).mean()-vf.ewm(span=55,adjust=False,min_periods=55).mean()
  b=np.sign(kvo)
  return b.diff(21).replace([np.inf,-np.inf],np.nan)
def f12os_f12_oscillator_family_uords_60d_slope_v143_signal(high,low,closeadj):
  uo=_UO(high,low,closeadj)
  cond=(uo<30.0).astype(float).where(~uo.isna())
  def _ds(x):
    idx=np.where(x>0.5)[0]
    if idx.size==0:return 60.0
    return float(len(x)-1-idx[-1])
  b=cond.rolling(60,min_periods=60).apply(_ds,raw=True)
  return b.diff(21).replace([np.inf,-np.inf],np.nan)
def f12os_f12_oscillator_family_uoxsign_60d_slope_v145_signal(high,low,closeadj):
  uo=_UO(high,low,closeadj)
  sgn=np.sign(uo-50.0)
  fl=(sgn!=sgn.shift(1)).astype(float).where(~sgn.isna()&~sgn.shift(1).isna())
  b=fl.rolling(60,min_periods=60).sum()
  return b.diff(21).replace([np.inf,-np.inf],np.nan)
def f12os_f12_oscillator_family_aotop_120d_slope_v146_signal(high,low):
  mp=0.5*(high+low)
  ao=mp.rolling(5,min_periods=5).mean()-mp.rolling(34,min_periods=34).mean()
  b=ao.rolling(120,min_periods=120).max()
  return b.diff(63).replace([np.inf,-np.inf],np.nan)
def f12os_f12_oscillator_family_aobot_120d_slope_v147_signal(high,low):
  mp=0.5*(high+low)
  ao=mp.rolling(5,min_periods=5).mean()-mp.rolling(34,min_periods=34).mean()
  b=ao.rolling(120,min_periods=120).min()
  return b.diff(63).replace([np.inf,-np.inf],np.nan)
def f12os_f12_oscillator_family_pctrnk_tr_60d_slope_v148_signal(high,low,close):
  pc=close.shift(1)
  tr=pd.concat([(high-low).abs(),(high-pc).abs(),(low-pc).abs()],axis=1).max(axis=1)
  b=tr.rolling(60,min_periods=60).rank(pct=True)
  return b.diff(21).replace([np.inf,-np.inf],np.nan)
def f12os_f12_oscillator_family_rsivol_match_40d_slope_v149_signal(closeadj,volume):
  n=14
  d=closeadj.diff()
  au=_W(d,n)
  ad=_W(-d,n)
  rs=au/ad.replace(0.0,np.nan)
  rsi=100.0-100.0/(1.0+rs)
  lv=np.log(volume.replace(0.0,np.nan))
  b=rsi.rolling(40,min_periods=40).corr(lv)
  return b.diff(10).replace([np.inf,-np.inf],np.nan)
def f12os_f12_oscillator_family_rsiwlder_5d_slope_v150_signal(close):
  n=5
  d=close.diff()
  au=_W(d,n)
  ad=_W(-d,n)
  rs=au/ad.replace(0.0,np.nan)
  b=100.0-100.0/(1.0+rs)
  sd=b.rolling(40,min_periods=40).std(ddof=1)
  return (b.diff(5)/sd.replace(0.0,np.nan)).replace([np.inf,-np.inf],np.nan)

_R = [
  (["close"], f12os_f12_oscillator_family_rsi_7d_slope_v001_signal),
  (["close"], f12os_f12_oscillator_family_rsi_14d_slope_v002_signal),
  (["closeadj"], f12os_f12_oscillator_family_rsi_50d_slope_v003_signal),
  (["close"], f12os_f12_oscillator_family_rsidsmid_21d_slope_v004_signal),
  (["closeadj"], f12os_f12_oscillator_family_rsidiff21_30d_slope_v005_signal),
  (["closeadj"], f12os_f12_oscillator_family_rsisma_60d_slope_v006_signal),
  (["close"], f12os_f12_oscillator_family_rsisign_14d_slope_v007_signal),
  (["close"], f12os_f12_oscillator_family_rsiob_20d_slope_v008_signal),
  (["closeadj"], f12os_f12_oscillator_family_rsios_30d_slope_v009_signal),
  (["closeadj"], f12os_f12_oscillator_family_rsidsob_60d_slope_v010_signal),
  (["closeadj"], f12os_f12_oscillator_family_rsidsos_80d_slope_v011_signal),
  (["closeadj"], f12os_f12_oscillator_family_rsirank_120d_slope_v012_signal),
  (["closeadj"], f12os_f12_oscillator_family_rsivar_80d_slope_v013_signal),
  (["close"], f12os_f12_oscillator_family_rsixmid_60d_slope_v014_signal),
  (["closeadj"], f12os_f12_oscillator_family_rsifloor_120d_slope_v015_signal),
  (["high", "low", "close"], f12os_f12_oscillator_family_stochk_5d_slope_v016_signal),
  (["high", "low", "close"], f12os_f12_oscillator_family_stochk_14d_slope_v017_signal),
  (["high", "low", "closeadj"], f12os_f12_oscillator_family_stochk_50d_slope_v018_signal),
  (["high", "low", "close"], f12os_f12_oscillator_family_stochd_14d_slope_v019_signal),
  (["high", "low", "close"], f12os_f12_oscillator_family_stochkd_14d_slope_v020_signal),
  (["high", "low", "closeadj"], f12os_f12_oscillator_family_stochkdxover_50d_slope_v021_signal),
  (["high", "low", "closeadj"], f12os_f12_oscillator_family_stochob_50d_slope_v022_signal),
  (["high", "low", "closeadj"], f12os_f12_oscillator_family_stochstreakob_30d_slope_v023_signal),
  (["high", "low", "closeadj"], f12os_f12_oscillator_family_stochcent_30d_slope_v024_signal),
  (["high", "low", "close"], f12os_f12_oscillator_family_willr_7d_slope_v025_signal),
  (["high", "low", "closeadj"], f12os_f12_oscillator_family_willrxlow_100d_slope_v026_signal),
  (["high", "low", "close"], f12os_f12_oscillator_family_willrdsmid_21d_slope_v027_signal),
  (["high", "low", "close"], f12os_f12_oscillator_family_cci_14d_slope_v028_signal),
  (["high", "low", "closeadj"], f12os_f12_oscillator_family_cci_50d_slope_v029_signal),
  (["high", "low", "close"], f12os_f12_oscillator_family_ccitanh_20d_slope_v030_signal),
  (["high", "low", "closeadj"], f12os_f12_oscillator_family_cciob_40d_slope_v031_signal),
  (["high", "low", "closeadj"], f12os_f12_oscillator_family_cciextrm_120d_slope_v032_signal),
  (["high", "low", "closeadj"], f12os_f12_oscillator_family_ccisign_30d_slope_v033_signal),
  (["high", "low", "close", "volume"], f12os_f12_oscillator_family_mfi_14d_slope_v034_signal),
  (["high", "low", "closeadj", "volume"], f12os_f12_oscillator_family_mfi_30d_slope_v035_signal),
  (["high", "low", "close", "volume"], f12os_f12_oscillator_family_mfinorm_21d_slope_v036_signal),
  (["high", "low", "close"], f12os_f12_oscillator_family_uo_7_14_28_slope_v037_signal),
  (["high", "low", "closeadj"], f12os_f12_oscillator_family_uolong_14_28_56_slope_v038_signal),
  (["high", "low"], f12os_f12_oscillator_family_aopct_5_34_slope_v039_signal),
  (["high", "low"], f12os_f12_oscillator_family_aoz_60d_slope_v040_signal),
  (["close"], f12os_f12_oscillator_family_dpo_20d_slope_v041_signal),
  (["closeadj"], f12os_f12_oscillator_family_dpoxsign_60d_slope_v042_signal),
  (["close"], f12os_f12_oscillator_family_stochrsi_14d_slope_v043_signal),
  (["closeadj"], f12os_f12_oscillator_family_stochrsi_50d_slope_v044_signal),
  (["high", "low", "close", "volume"], f12os_f12_oscillator_family_chaikin_3_10_slope_v045_signal),
  (["high", "low", "close", "volume"], f12os_f12_oscillator_family_chaikinrank_120d_slope_v046_signal),
  (["high", "low", "close", "volume"], f12os_f12_oscillator_family_klinger_34_55_slope_v047_signal),
  (["close"], f12os_f12_oscillator_family_bias_10d_slope_v048_signal),
  (["closeadj"], f12os_f12_oscillator_family_bias_60d_slope_v049_signal),
  (["high", "low", "closeadj"], f12os_f12_oscillator_family_rsistochzdiff_30d_slope_v050_signal),
  (["high", "low", "closeadj"], f12os_f12_oscillator_family_rsicciagree_50d_slope_v051_signal),
  (["high", "low", "closeadj"], f12os_f12_oscillator_family_oscobcnt_30d_slope_v052_signal),
  (["high", "low", "closeadj"], f12os_f12_oscillator_family_oscdisp_30d_slope_v053_signal),
  (["high", "low", "closeadj"], f12os_f12_oscillator_family_oscbullcnt_30d_slope_v054_signal),
  (["high", "low", "closeadj"], f12os_f12_oscillator_family_stochzkurt_60d_slope_v055_signal),
  (["closeadj"], f12os_f12_oscillator_family_rsidouble_30d_slope_v056_signal),
  (["high", "low", "closeadj"], f12os_f12_oscillator_family_stochskew_60d_slope_v057_signal),
  (["close"], f12os_f12_oscillator_family_rsiabs50_25d_slope_v058_signal),
  (["high", "low", "closeadj"], f12os_f12_oscillator_family_stochrange_50d_slope_v059_signal),
  (["high", "low", "closeadj"], f12os_f12_oscillator_family_ccixsign_60d_slope_v060_signal),
  (["close"], f12os_f12_oscillator_family_rsistreaktop_30d_slope_v061_signal),
  (["high", "low"], f12os_f12_oscillator_family_aoabs_50d_slope_v062_signal),
  (["high", "low", "closeadj", "volume"], f12os_f12_oscillator_family_mfi_rsidiff_30d_slope_v063_signal),
  (["high", "low", "closeadj"], f12os_f12_oscillator_family_stochkdpath_50d_slope_v064_signal),
  (["high", "low", "closeadj"], f12os_f12_oscillator_family_uoslp_30d_slope_v065_signal),
  (["closeadj"], f12os_f12_oscillator_family_dpostreak_30d_slope_v066_signal),
  (["close"], f12os_f12_oscillator_family_stochrsisma_21d_slope_v067_signal),
  (["high", "low"], f12os_f12_oscillator_family_aobullbear_50d_slope_v068_signal),
  (["closeadj"], f12os_f12_oscillator_family_biaspct_30d_slope_v069_signal),
  (["high", "low", "closeadj"], f12os_f12_oscillator_family_ccinegrun_30d_slope_v070_signal),
  (["closeadj"], f12os_f12_oscillator_family_rsimedian_60d_slope_v071_signal),
  (["high", "low", "closeadj", "volume"], f12os_f12_oscillator_family_mfivlog_50d_slope_v072_signal),
  (["high", "low", "close", "volume"], f12os_f12_oscillator_family_chaikinsign_40d_slope_v073_signal),
  (["high", "low", "close"], f12os_f12_oscillator_family_stochkrng_50d_slope_v074_signal),
  (["closeadj"], f12os_f12_oscillator_family_rsivolratio_30d_slope_v075_signal),
  (["close"], f12os_f12_oscillator_family_rsi_21d_slope_v076_signal),
  (["closeadj"], f12os_f12_oscillator_family_rsi_100d_slope_v077_signal),
  (["closeadj"], f12os_f12_oscillator_family_rsiema_30d_slope_v078_signal),
  (["closeadj"], f12os_f12_oscillator_family_rsiceil_120d_slope_v079_signal),
  (["closeadj"], f12os_f12_oscillator_family_rsispan_80d_slope_v080_signal),
  (["closeadj"], f12os_f12_oscillator_family_rsistreakbot_30d_slope_v081_signal),
  (["closeadj"], f12os_f12_oscillator_family_rsiextrm_80d_slope_v082_signal),
  (["closeadj"], f12os_f12_oscillator_family_rsiiqr_60d_slope_v083_signal),
  (["closeadj"], f12os_f12_oscillator_family_rsigap_30d_slope_v084_signal),
  (["close"], f12os_f12_oscillator_family_rsisig_15d_slope_v085_signal),
  (["high", "low", "close"], f12os_f12_oscillator_family_stochk_21d_slope_v086_signal),
  (["high", "low", "closeadj"], f12os_f12_oscillator_family_stochkpos_50d_slope_v087_signal),
  (["high", "low", "closeadj"], f12os_f12_oscillator_family_stochds_80d_slope_v088_signal),
  (["high", "low", "closeadj"], f12os_f12_oscillator_family_stochkmed_120d_slope_v089_signal),
  (["high", "low", "closeadj"], f12os_f12_oscillator_family_stochkdslp_30d_slope_v090_signal),
  (["high", "low", "closeadj"], f12os_f12_oscillator_family_stochwidemar_100d_slope_v091_signal),
  (["high", "low", "closeadj"], f12os_f12_oscillator_family_willrslp_50d_slope_v093_signal),
  (["high", "low", "closeadj"], f12os_f12_oscillator_family_willrxhi_50d_slope_v094_signal),
  (["high", "low", "closeadj"], f12os_f12_oscillator_family_cci_30d_slope_v095_signal),
  (["high", "low", "closeadj"], f12os_f12_oscillator_family_ccislope_50d_slope_v096_signal),
  (["high", "low", "closeadj"], f12os_f12_oscillator_family_ccipos_60d_slope_v097_signal),
  (["high", "low", "closeadj"], f12os_f12_oscillator_family_cciskew_60d_slope_v098_signal),
  (["high", "low", "closeadj"], f12os_f12_oscillator_family_cciosmin_60d_slope_v099_signal),
  (["high", "low", "closeadj"], f12os_f12_oscillator_family_ccids_60d_slope_v100_signal),
  (["high", "low", "closeadj", "volume"], f12os_f12_oscillator_family_mfi_50d_slope_v101_signal),
  (["high", "low", "closeadj", "volume"], f12os_f12_oscillator_family_mfiob_50d_slope_v102_signal),
  (["high", "low", "closeadj", "volume"], f12os_f12_oscillator_family_mfislp_30d_slope_v103_signal),
  (["high", "low", "closeadj", "volume"], f12os_f12_oscillator_family_mfidsos_80d_slope_v104_signal),
  (["high", "low", "closeadj"], f12os_f12_oscillator_family_uodefault_slope_v105_signal),
  (["high", "low", "closeadj"], f12os_f12_oscillator_family_uoob_50d_slope_v106_signal),
  (["high", "low", "closeadj"], f12os_f12_oscillator_family_uorng_80d_slope_v107_signal),
  (["high", "low"], f12os_f12_oscillator_family_aoxsign_60d_slope_v108_signal),
  (["high", "low"], f12os_f12_oscillator_family_aosig_30d_slope_v109_signal),
  (["high", "low"], f12os_f12_oscillator_family_aoslp_50d_slope_v110_signal),
  (["closeadj"], f12os_f12_oscillator_family_dpo_30d_slope_v111_signal),
  (["closeadj"], f12os_f12_oscillator_family_dpoabs_50d_slope_v112_signal),
  (["close"], f12os_f12_oscillator_family_stochrsi_7d_slope_v113_signal),
  (["closeadj"], f12os_f12_oscillator_family_stochrsiob_30d_slope_v114_signal),
  (["high", "low", "closeadj", "volume"], f12os_f12_oscillator_family_chaikin_10_30_slope_v115_signal),
  (["high", "low", "close", "volume"], f12os_f12_oscillator_family_chaikinxs_60d_slope_v116_signal),
  (["high", "low", "closeadj", "volume"], f12os_f12_oscillator_family_klingertanh_30d_slope_v117_signal),
  (["close"], f12os_f12_oscillator_family_bias_20d_slope_v118_signal),
  (["closeadj"], f12os_f12_oscillator_family_biasxsign_40d_slope_v119_signal),
  (["high", "low", "closeadj", "volume"], f12os_f12_oscillator_family_rsimficorr_60d_slope_v120_signal),
  (["high", "low", "closeadj"], f12os_f12_oscillator_family_rsiccixdcorr_50d_slope_v121_signal),
  (["high", "low", "closeadj"], f12os_f12_oscillator_family_oscbearcnt_30d_slope_v122_signal),
  (["high", "low", "closeadj"], f12os_f12_oscillator_family_oscavgcent_30d_slope_v123_signal),
  (["closeadj"], f12os_f12_oscillator_family_rsicvar_50d_slope_v124_signal),
  (["high", "low", "closeadj"], f12os_f12_oscillator_family_stochstd_60d_slope_v125_signal),
  (["high", "low", "closeadj"], f12os_f12_oscillator_family_cciarctan_60d_slope_v126_signal),
  (["high", "low", "closeadj"], f12os_f12_oscillator_family_ccistreaktop_30d_slope_v127_signal),
  (["high", "low", "closeadj", "volume"], f12os_f12_oscillator_family_mfistreakob_30d_slope_v128_signal),
  (["closeadj"], f12os_f12_oscillator_family_rsiparity_50d_slope_v129_signal),
  (["high", "low", "closeadj"], f12os_f12_oscillator_family_oscobds_60d_slope_v130_signal),
  (["closeadj"], f12os_f12_oscillator_family_trix_15d_slope_v131_signal),
  (["closeadj"], f12os_f12_oscillator_family_trix_30d_slope_v132_signal),
  (["high", "low", "close"], f12os_f12_oscillator_family_fisherwr_10d_slope_v133_signal),
  (["high", "low", "close"], f12os_f12_oscillator_family_kvarstd_50d_slope_v134_signal),
  (["closeadj"], f12os_f12_oscillator_family_stochrsi_30d_slope_v135_signal),
  (["closeadj"], f12os_f12_oscillator_family_stochrsixs_50d_slope_v136_signal),
  (["closeadj"], f12os_f12_oscillator_family_pctrnk_clmid_50d_slope_v137_signal),
  (["high", "low"], f12os_f12_oscillator_family_pctrnk_hldiff_120d_slope_v138_signal),
  (["high", "low", "closeadj"], f12os_f12_oscillator_family_uovariation_30d_slope_v139_signal),
  (["high", "low", "closeadj"], f12os_f12_oscillator_family_ccixdmu_60d_slope_v140_signal),
  (["high", "low", "closeadj"], f12os_f12_oscillator_family_ccislpsign_60d_slope_v141_signal),
  (["high", "low", "closeadj", "volume"], f12os_f12_oscillator_family_klingersign_30d_slope_v142_signal),
  (["high", "low", "closeadj"], f12os_f12_oscillator_family_uords_60d_slope_v143_signal),
  (["high", "low", "closeadj"], f12os_f12_oscillator_family_uoxsign_60d_slope_v145_signal),
  (["high", "low"], f12os_f12_oscillator_family_aotop_120d_slope_v146_signal),
  (["high", "low"], f12os_f12_oscillator_family_aobot_120d_slope_v147_signal),
  (["high", "low", "close"], f12os_f12_oscillator_family_pctrnk_tr_60d_slope_v148_signal),
  (["closeadj", "volume"], f12os_f12_oscillator_family_rsivol_match_40d_slope_v149_signal),
  (["close"], f12os_f12_oscillator_family_rsiwlder_5d_slope_v150_signal),
]

f12_oscillator_family_slope_001_150_REGISTRY = {f.__name__: {"inputs": i, "func": f} for i, f in _R}

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
  for name, entry in f12_oscillator_family_slope_001_150_REGISTRY.items():
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
  aligned = aligned.replace([np.inf, -np.inf], np.nan)
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
  print(f"OK slope_001_150: {len(results)} features, max |corr|={max_corr:.4f}, coverage_ok={frac:.2%}")

if __name__ == "__main__":
  _self_test()
