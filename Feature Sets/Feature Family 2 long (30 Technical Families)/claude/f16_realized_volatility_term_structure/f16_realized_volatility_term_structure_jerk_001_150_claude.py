"""f16_realized_volatility_term_structure jerk features 001-150 (2nd derivative).
Each jerk feature is base - 2*base.shift(k) + base.shift(2k) where k follows
the ROC bracket of the primary window. NaN policy: replace([inf,-inf],nan)."""
from __future__ import annotations

import inspect

import numpy as np
import pandas as pd


def _ac1(x):
    x = np.asarray(x, dtype=float)
    if np.any(~np.isfinite(x)) or x.size < 5:
        return np.nan
    a = x[:-1]; b = x[1:]
    sa = a.std(ddof=0); sb = b.std(ddof=0)
    if sa <= 0 or sb <= 0:
        return np.nan
    return float(((a - a.mean()) * (b - b.mean())).mean() / (sa * sb))


def _ds(x, cap):
    idx = np.where(x > 0.5)[0]
    if idx.size == 0:
        return float(cap)
    return float(len(x) - 1 - idx[-1])


def _j(s, k):
    return s - 2.0 * s.shift(k) + s.shift(2 * k)


# --- 001-075 jerk: 2nd derivative of base 001-075 ---

def f16vt_f16_realized_volatility_term_structure_rv_5d_jerk_v001_signal(close):
    r=np.log(close).diff(); b=r.rolling(5,min_periods=5).std(ddof=1) * np.sqrt(252.0)
    return _j(b, 5).replace([np.inf,-np.inf],np.nan)

def f16vt_f16_realized_volatility_term_structure_rv_63d_jerk_v002_signal(closeadj):
    r=np.log(closeadj).diff(); b=r.rolling(63,min_periods=63).std(ddof=1) * np.sqrt(252.0)
    return _j(b, 21).replace([np.inf,-np.inf],np.nan)

def f16vt_f16_realized_volatility_term_structure_rv_252d_jerk_v003_signal(closeadj):
    r=np.log(closeadj).diff(); b=r.rolling(252,min_periods=252).std(ddof=1) * np.sqrt(252.0)
    return _j(b, 63).replace([np.inf,-np.inf],np.nan)

def f16vt_f16_realized_volatility_term_structure_rvratio_5_21_jerk_v004_signal(close):
    r=np.log(close).diff()
    b=r.rolling(5,min_periods=5).std(ddof=1) / r.rolling(21,min_periods=21).std(ddof=1).replace(0.0,np.nan)
    return _j(b, 10).replace([np.inf,-np.inf],np.nan)

def f16vt_f16_realized_volatility_term_structure_rvratio_21_63_jerk_v005_signal(closeadj):
    r=np.log(closeadj).diff()
    b=r.rolling(21,min_periods=21).std(ddof=1) / r.rolling(63,min_periods=63).std(ddof=1).replace(0.0,np.nan)
    return _j(b, 10).replace([np.inf,-np.inf],np.nan)

def f16vt_f16_realized_volatility_term_structure_rvratio_63_252_jerk_v006_signal(closeadj):
    r=np.log(closeadj).diff()
    b=r.rolling(63,min_periods=63).std(ddof=1) / r.rolling(252,min_periods=252).std(ddof=1).replace(0.0,np.nan)
    return _j(b, 5).replace([np.inf,-np.inf],np.nan)

def f16vt_f16_realized_volatility_term_structure_termpctrank_5_252_jerk_v007_signal(closeadj):
    r=np.log(closeadj).diff()
    v5=r.rolling(5,min_periods=5).std(ddof=1); v252=r.rolling(252,min_periods=252).std(ddof=1)
    ratio=v5 / v252.replace(0.0,np.nan)
    b=ratio.rolling(120,min_periods=80).rank(pct=True)
    return _j(b, 63).replace([np.inf,-np.inf],np.nan)

def f16vt_f16_realized_volatility_term_structure_invertcount_5_21_jerk_v008_signal(close):
    r=np.log(close).diff()
    v5=r.rolling(5,min_periods=5).std(ddof=1); v21=r.rolling(21,min_periods=21).std(ddof=1)
    inv=(v5 > v21).astype(float).where(~v5.isna() & ~v21.isna())
    b=inv.rolling(30,min_periods=30).sum()
    return _j(b, 10).replace([np.inf,-np.inf],np.nan)

def f16vt_f16_realized_volatility_term_structure_logslope_21_252_jerk_v009_signal(closeadj):
    r=np.log(closeadj).diff()
    v21=r.rolling(21,min_periods=21).std(ddof=1); v252=r.rolling(252,min_periods=252).std(ddof=1)
    ls=np.log(v21 / v252.replace(0.0,np.nan))
    b=np.sign(ls).where(~ls.isna())
    return _j(b, 63).replace([np.inf,-np.inf],np.nan)

def f16vt_f16_realized_volatility_term_structure_curv_5_21_63_jerk_v010_signal(closeadj):
    r=np.log(closeadj).diff()
    v5=r.rolling(5,min_periods=5).std(ddof=1); v21=r.rolling(21,min_periods=21).std(ddof=1); v63=r.rolling(63,min_periods=63).std(ddof=1)
    b=v5 - 2.0 * v21 + v63
    return _j(b, 10).replace([np.inf,-np.inf],np.nan)

def f16vt_f16_realized_volatility_term_structure_curv_21_63_252_jerk_v011_signal(closeadj):
    r=np.log(closeadj).diff()
    v21=r.rolling(21,min_periods=21).std(ddof=1); v63=r.rolling(63,min_periods=63).std(ddof=1); v252=r.rolling(252,min_periods=252).std(ddof=1)
    b=v21 - 2.0 * v63 + v252
    return _j(b, 21).replace([np.inf,-np.inf],np.nan)

def f16vt_f16_realized_volatility_term_structure_convexity_jerk_v012_signal(closeadj):
    r=np.log(closeadj).diff()
    v5=r.rolling(5,min_periods=5).std(ddof=1); v21=r.rolling(21,min_periods=21).std(ddof=1); v63=r.rolling(63,min_periods=63).std(ddof=1)
    cx=0.5 * (v5 + v63) - v21
    b=np.sign(cx).where(~cx.isna())
    return _j(b, 21).replace([np.inf,-np.inf],np.nan)

def f16vt_f16_realized_volatility_term_structure_vol21slope_5d_jerk_v013_signal(closeadj):
    r=np.log(closeadj).diff(); v21=r.rolling(21,min_periods=21).std(ddof=1)
    b=v21.diff(5)
    return _j(b, 10).replace([np.inf,-np.inf],np.nan)

def f16vt_f16_realized_volatility_term_structure_vol63slope_21d_jerk_v014_signal(closeadj):
    r=np.log(closeadj).diff(); v63=r.rolling(63,min_periods=63).std(ddof=1)
    b=v63.diff(21)
    return _j(b, 21).replace([np.inf,-np.inf],np.nan)

def f16vt_f16_realized_volatility_term_structure_vol21accel_jerk_v015_signal(closeadj):
    r=np.log(closeadj).diff(); v21=r.rolling(21,min_periods=21).std(ddof=1)
    b=v21 - 2.0 * v21.shift(5) + v21.shift(10)
    return _j(b, 10).replace([np.inf,-np.inf],np.nan)

def f16vt_f16_realized_volatility_term_structure_volpct_21on252_jerk_v016_signal(closeadj):
    r=np.log(closeadj).diff(); v21=r.rolling(21,min_periods=21).std(ddof=1)
    b=v21.rolling(252,min_periods=252).rank(pct=True)
    return _j(b, 21).replace([np.inf,-np.inf],np.nan)

def f16vt_f16_realized_volatility_term_structure_volz_21on120_jerk_v017_signal(closeadj):
    r=np.log(closeadj).diff(); v21=r.rolling(21,min_periods=21).std(ddof=1)
    mu=v21.rolling(120,min_periods=120).mean(); sd=v21.rolling(120,min_periods=120).std(ddof=1)
    b=(v21 - mu) / sd.replace(0.0,np.nan)
    return _j(b, 5).replace([np.inf,-np.inf],np.nan)

def f16vt_f16_realized_volatility_term_structure_volquint_5d_jerk_v018_signal(closeadj):
    r=np.log(closeadj).diff(); v5=r.rolling(5,min_periods=5).std(ddof=1)
    p=v5.rolling(252,min_periods=252).rank(pct=True)
    b=(p * 5.0).apply(np.ceil).clip(lower=1.0,upper=5.0)
    return _j(b, 21).replace([np.inf,-np.inf],np.nan)

def f16vt_f16_realized_volatility_term_structure_dayssince_volp90_jerk_v019_signal(closeadj):
    r=np.log(closeadj).diff(); v21=r.rolling(21,min_periods=21).std(ddof=1)
    p90=v21.rolling(252,min_periods=252).quantile(0.9)
    hit=(v21 > p90).astype(float).where(~v21.isna() & ~p90.isna())
    b=hit.rolling(100,min_periods=100).apply(lambda x: _ds(x, 100.0), raw=True)
    return _j(b, 21).replace([np.inf,-np.inf],np.nan)

def f16vt_f16_realized_volatility_term_structure_streakhighvol_jerk_v020_signal(closeadj):
    r=np.log(closeadj).diff(); v21=r.rolling(21,min_periods=21).std(ddof=1)
    med=v21.rolling(252,min_periods=252).median()
    h=(v21 > med).astype(float).where(~v21.isna() & ~med.isna())
    grp=(h != h.shift(1)).cumsum(); b=h.groupby(grp).cumsum() * h
    return _j(b, 10).replace([np.inf,-np.inf],np.nan)

def f16vt_f16_realized_volatility_term_structure_hlrvratio_21d_jerk_v021_signal(high, low, close):
    n=21; rng=(high - low) / close.replace(0.0,np.nan)
    rv_rng=rng.rolling(n,min_periods=n).std(ddof=1)
    rv_ret=np.log(close).diff().rolling(n,min_periods=n).std(ddof=1)
    b=rv_rng / rv_ret.replace(0.0,np.nan)
    return _j(b, 10).replace([np.inf,-np.inf],np.nan)

def f16vt_f16_realized_volatility_term_structure_hlrvratio_63d_jerk_v022_signal(high, low, closeadj):
    n=63; rng=(high - low) / closeadj.replace(0.0,np.nan)
    rv_rng=rng.rolling(n,min_periods=n).std(ddof=1)
    rv_ret=np.log(closeadj).diff().rolling(n,min_periods=n).std(ddof=1)
    b=rv_rng / rv_ret.replace(0.0,np.nan)
    return _j(b, 21).replace([np.inf,-np.inf],np.nan)

def f16vt_f16_realized_volatility_term_structure_retskew_21d_jerk_v023_signal(close):
    r=np.log(close).diff(); b=r.rolling(21,min_periods=21).skew()
    return _j(b, 5).replace([np.inf,-np.inf],np.nan)

def f16vt_f16_realized_volatility_term_structure_retskew_63d_jerk_v024_signal(closeadj):
    r=np.log(closeadj).diff(); b=r.rolling(63,min_periods=63).skew()
    return _j(b, 21).replace([np.inf,-np.inf],np.nan)

def f16vt_f16_realized_volatility_term_structure_retkurt_21d_jerk_v025_signal(close):
    r=np.log(close).diff(); b=r.rolling(21,min_periods=21).kurt()
    return _j(b, 10).replace([np.inf,-np.inf],np.nan)

def f16vt_f16_realized_volatility_term_structure_retkurt_63d_jerk_v026_signal(closeadj):
    r=np.log(closeadj).diff(); b=r.rolling(63,min_periods=63).kurt()
    return _j(b, 21).replace([np.inf,-np.inf],np.nan)

def f16vt_f16_realized_volatility_term_structure_downvol_21d_jerk_v027_signal(close):
    r=np.log(close).diff(); neg=r.where(r < 0)
    b=neg.rolling(21,min_periods=10).std(ddof=1) * np.sqrt(252.0)
    return _j(b, 5).replace([np.inf,-np.inf],np.nan)

def f16vt_f16_realized_volatility_term_structure_upvol_63d_jerk_v028_signal(closeadj):
    r=np.log(closeadj).diff(); pos=r.where(r > 0)
    b=pos.rolling(63,min_periods=30).std(ddof=1) * np.sqrt(252.0)
    return _j(b, 21).replace([np.inf,-np.inf],np.nan)

def f16vt_f16_realized_volatility_term_structure_varasym_42d_jerk_v029_signal(closeadj):
    n=42; r=np.log(closeadj).diff()
    pos=r.where(r > 0); neg=r.where(r < 0)
    vp=pos.rolling(n,min_periods=15).var(ddof=1); vn=neg.rolling(n,min_periods=15).var(ddof=1)
    b=vp - vn
    return _j(b, 10).replace([np.inf,-np.inf],np.nan)

def f16vt_f16_realized_volatility_term_structure_absretacf1_30d_jerk_v030_signal(closeadj):
    r=np.log(closeadj).diff().abs()
    b=r.rolling(30,min_periods=30).apply(_ac1, raw=True)
    return _j(b, 10).replace([np.inf,-np.inf],np.nan)

def f16vt_f16_realized_volatility_term_structure_sqretacf1_60d_jerk_v031_signal(closeadj):
    r=(np.log(closeadj).diff()) ** 2
    b=r.rolling(60,min_periods=60).apply(_ac1, raw=True)
    return _j(b, 21).replace([np.inf,-np.inf],np.nan)

def f16vt_f16_realized_volatility_term_structure_volpersist_30d_jerk_v032_signal(closeadj):
    r=np.log(closeadj).diff(); v21=r.rolling(21,min_periods=21).std(ddof=1)
    med=v21.rolling(252,min_periods=252).median()
    above=(v21 > med).astype(float).where(~v21.isna() & ~med.isna())
    b=above.rolling(30,min_periods=30).mean()
    return _j(b, 10).replace([np.inf,-np.inf],np.nan)

def f16vt_f16_realized_volatility_term_structure_curveR2_4pt_jerk_v033_signal(closeadj):
    r=np.log(closeadj).diff()
    v5=r.rolling(5,min_periods=5).std(ddof=1); v21=r.rolling(21,min_periods=21).std(ddof=1)
    v63=r.rolling(63,min_periods=63).std(ddof=1); v252=r.rolling(252,min_periods=252).std(ddof=1)
    x=np.log(np.array([5.0, 21.0, 63.0, 252.0])); xm=x - x.mean(); sxx=(xm * xm).sum()
    def _r2(row):
        y=np.array(row,dtype=float)
        if np.any(~np.isfinite(y)) or np.any(y <= 0): return np.nan
        ly=np.log(y); lym=ly - ly.mean(); syy=(lym * lym).sum()
        if syy <= 0: return np.nan
        be=(xm * lym).sum() / sxx; rss=((lym - be * xm) ** 2).sum()
        return float(1.0 - rss / syy)
    df=pd.concat([v5, v21, v63, v252], axis=1)
    b=df.apply(_r2, axis=1)
    return _j(b, 63).replace([np.inf,-np.inf],np.nan)

def f16vt_f16_realized_volatility_term_structure_curveslopesign_jerk_v034_signal(closeadj):
    r=np.log(closeadj).diff()
    v5=r.rolling(5,min_periods=5).std(ddof=1); v21=r.rolling(21,min_periods=21).std(ddof=1)
    v63=r.rolling(63,min_periods=63).std(ddof=1); v252=r.rolling(252,min_periods=252).std(ddof=1)
    x=np.log(np.array([5.0, 21.0, 63.0, 252.0])); xm=x - x.mean(); sxx=(xm * xm).sum()
    def _sl(row):
        y=np.array(row,dtype=float)
        if np.any(~np.isfinite(y)) or np.any(y <= 0): return np.nan
        ly=np.log(y); lym=ly - ly.mean()
        s=(xm * lym).sum() / sxx
        if s > 0: return 1.0
        if s < 0: return -1.0
        return 0.0
    df=pd.concat([v5, v21, v63, v252], axis=1)
    b=df.apply(_sl, axis=1)
    return _j(b, 21).replace([np.inf,-np.inf],np.nan)

def f16vt_f16_realized_volatility_term_structure_invertedsign_jerk_v035_signal(closeadj):
    r=np.log(closeadj).diff()
    v5=r.rolling(5,min_periods=5).std(ddof=1); v63=r.rolling(63,min_periods=63).std(ddof=1)
    b=np.sign(v5 - v63).where(~v5.isna() & ~v63.isna())
    return _j(b, 21).replace([np.inf,-np.inf],np.nan)

def f16vt_f16_realized_volatility_term_structure_invertedfrac_60d_jerk_v036_signal(closeadj):
    r=np.log(closeadj).diff()
    v5=r.rolling(5,min_periods=5).std(ddof=1); v63=r.rolling(63,min_periods=63).std(ddof=1)
    inv=(v5 > v63).astype(float).where(~v5.isna() & ~v63.isna())
    b=inv.rolling(60,min_periods=60).mean()
    return _j(b, 21).replace([np.inf,-np.inf],np.nan)

def f16vt_f16_realized_volatility_term_structure_volconeshort_5on120_jerk_v037_signal(close):
    r=np.log(close).diff(); v5=r.rolling(5,min_periods=5).std(ddof=1)
    lo=v5.rolling(120,min_periods=120).min(); hi=v5.rolling(120,min_periods=120).max()
    b=(v5 - lo) / (hi - lo).replace(0.0,np.nan)
    return _j(b, 63).replace([np.inf,-np.inf],np.nan)

def f16vt_f16_realized_volatility_term_structure_volconedelta_jerk_v038_signal(closeadj):
    r=np.log(closeadj).diff()
    v5=r.rolling(5,min_periods=5).std(ddof=1); v63=r.rolling(63,min_periods=63).std(ddof=1)
    lo5=v5.rolling(120,min_periods=120).min(); hi5=v5.rolling(120,min_periods=120).max()
    lo63=v63.rolling(252,min_periods=252).min(); hi63=v63.rolling(252,min_periods=252).max()
    c5=(v5 - lo5) / (hi5 - lo5).replace(0.0,np.nan)
    c63=(v63 - lo63) / (hi63 - lo63).replace(0.0,np.nan)
    b=c5 - c63
    return _j(b, 21).replace([np.inf,-np.inf],np.nan)

def f16vt_f16_realized_volatility_term_structure_voldirsign_21d_jerk_v039_signal(closeadj):
    r=np.log(closeadj).diff(); v21=r.rolling(21,min_periods=21).std(ddof=1)
    b=np.sign(v21.diff(5)).where(~v21.isna())
    return _j(b, 10).replace([np.inf,-np.inf],np.nan)

def f16vt_f16_realized_volatility_term_structure_volcontract_30d_jerk_v040_signal(closeadj):
    r=np.log(closeadj).diff(); v21=r.rolling(21,min_periods=21).std(ddof=1)
    mn=v21.rolling(30,min_periods=30).min()
    b=(v21 <= mn).astype(float).where(~v21.isna() & ~mn.isna())
    return _j(b, 10).replace([np.inf,-np.inf],np.nan)

def f16vt_f16_realized_volatility_term_structure_volexpand_30d_jerk_v041_signal(closeadj):
    r=np.log(closeadj).diff(); v21=r.rolling(21,min_periods=21).std(ddof=1)
    mx=v21.shift(1).rolling(30,min_periods=30).max()
    b=(v21 > mx).astype(float).where(~v21.isna() & ~mx.isna())
    return _j(b, 10).replace([np.inf,-np.inf],np.nan)

def f16vt_f16_realized_volatility_term_structure_avgvol_3h_jerk_v042_signal(closeadj):
    r=np.log(closeadj).diff()
    v5=r.rolling(5,min_periods=5).std(ddof=1); v21=r.rolling(21,min_periods=21).std(ddof=1); v63=r.rolling(63,min_periods=63).std(ddof=1)
    b=(v5 + v21 + v63) / 3.0
    return _j(b, 10).replace([np.inf,-np.inf],np.nan)

def f16vt_f16_realized_volatility_term_structure_volhdisp_3h_jerk_v043_signal(closeadj):
    r=np.log(closeadj).diff()
    v5=r.rolling(5,min_periods=5).std(ddof=1); v21=r.rolling(21,min_periods=21).std(ddof=1); v63=r.rolling(63,min_periods=63).std(ddof=1)
    df=pd.concat([v5, v21, v63], axis=1)
    b=df.std(axis=1, ddof=1)
    return _j(b, 10).replace([np.inf,-np.inf],np.nan)

def f16vt_f16_realized_volatility_term_structure_medianvol_4h_jerk_v044_signal(closeadj):
    r=np.log(closeadj).diff()
    v5=r.rolling(5,min_periods=5).std(ddof=1); v21=r.rolling(21,min_periods=21).std(ddof=1)
    v63=r.rolling(63,min_periods=63).std(ddof=1); v252=r.rolling(252,min_periods=252).std(ddof=1)
    df=pd.concat([v5, v21, v63, v252], axis=1)
    b=df.median(axis=1)
    return _j(b, 21).replace([np.inf,-np.inf],np.nan)

def f16vt_f16_realized_volatility_term_structure_arctanlogvol_21d_jerk_v045_signal(closeadj):
    r=np.log(closeadj).diff(); v21=r.rolling(21,min_periods=21).std(ddof=1)
    b=np.arctan(np.log(v21.replace(0.0,np.nan)))
    return _j(b, 10).replace([np.inf,-np.inf],np.nan)

def f16vt_f16_realized_volatility_term_structure_tanhvolzdelta_jerk_v046_signal(closeadj):
    r=np.log(closeadj).diff()
    v5=r.rolling(5,min_periods=5).std(ddof=1); v63=r.rolling(63,min_periods=63).std(ddof=1)
    z5=(v5 - v5.rolling(120,min_periods=80).mean()) / v5.rolling(120,min_periods=80).std(ddof=1).replace(0.0,np.nan)
    z63=(v63 - v63.rolling(120,min_periods=80).mean()) / v63.rolling(120,min_periods=80).std(ddof=1).replace(0.0,np.nan)
    b=np.tanh(z5 - z63)
    return _j(b, 21).replace([np.inf,-np.inf],np.nan)

def f16vt_f16_realized_volatility_term_structure_sigmoidvolpct_jerk_v047_signal(closeadj):
    r=np.log(closeadj).diff(); v63=r.rolling(63,min_periods=63).std(ddof=1)
    p=v63.rolling(252,min_periods=252).rank(pct=True)
    b=1.0 / (1.0 + np.exp(-6.0 * (p - 0.5)))
    return _j(b, 21).replace([np.inf,-np.inf],np.nan)

def f16vt_f16_realized_volatility_term_structure_madstd_ratio_21d_jerk_v048_signal(close):
    n=21; r=np.log(close).diff(); mu=r.rolling(n,min_periods=n).mean()
    mad=(r - mu).abs().rolling(n,min_periods=n).mean(); sd=r.rolling(n,min_periods=n).std(ddof=1)
    b=mad / sd.replace(0.0,np.nan)
    return _j(b, 10).replace([np.inf,-np.inf],np.nan)

def f16vt_f16_realized_volatility_term_structure_rms_42d_jerk_v049_signal(closeadj):
    n=42; r=np.log(closeadj).diff()
    b=np.sqrt((r * r).rolling(n,min_periods=n).mean())
    return _j(b, 10).replace([np.inf,-np.inf],np.nan)

def f16vt_f16_realized_volatility_term_structure_rvarratio_5_63_jerk_v050_signal(closeadj):
    r=np.log(closeadj).diff()
    rv5=(r * r).rolling(5,min_periods=5).mean(); rv63=(r * r).rolling(63,min_periods=63).mean()
    b=rv5 / rv63.replace(0.0,np.nan)
    return _j(b, 10).replace([np.inf,-np.inf],np.nan)

def f16vt_f16_realized_volatility_term_structure_qvariation_30d_jerk_v052_signal(closeadj):
    r=np.log(closeadj).diff()
    b=(r * r).rolling(30,min_periods=30).sum()
    return _j(b, 10).replace([np.inf,-np.inf],np.nan)

def f16vt_f16_realized_volatility_term_structure_roughness_30d_jerk_v053_signal(closeadj):
    n=30; r=np.log(closeadj).diff()
    num=r.diff().abs().rolling(n,min_periods=n).sum(); den=r.abs().rolling(n,min_periods=n).sum()
    b=num / den.replace(0.0,np.nan)
    return _j(b, 10).replace([np.inf,-np.inf],np.nan)

def f16vt_f16_realized_volatility_term_structure_voldiffsign_21m63_jerk_v054_signal(closeadj):
    r=np.log(closeadj).diff()
    v21=r.rolling(21,min_periods=21).std(ddof=1); v63=r.rolling(63,min_periods=63).std(ddof=1)
    d=v21 - v63
    b=np.sign(d).where(~d.isna())
    return _j(b, 21).replace([np.inf,-np.inf],np.nan)

def f16vt_f16_realized_volatility_term_structure_voldiffz_5m63_jerk_v055_signal(closeadj):
    r=np.log(closeadj).diff()
    v5=r.rolling(5,min_periods=5).std(ddof=1); v63=r.rolling(63,min_periods=63).std(ddof=1)
    d=v5 - v63
    mu=d.rolling(120,min_periods=80).mean(); sd=d.rolling(120,min_periods=80).std(ddof=1)
    b=(d - mu) / sd.replace(0.0,np.nan)
    return _j(b, 63).replace([np.inf,-np.inf],np.nan)

def f16vt_f16_realized_volatility_term_structure_volofvol_long_jerk_v057_signal(closeadj):
    r=np.log(closeadj).diff(); v63=r.rolling(63,min_periods=63).std(ddof=1)
    sd=v63.rolling(126,min_periods=126).std(ddof=1); mu=v63.rolling(126,min_periods=126).mean()
    b=sd / mu.replace(0.0,np.nan)
    return _j(b, 21).replace([np.inf,-np.inf],np.nan)

def f16vt_f16_realized_volatility_term_structure_curvres21_jerk_v058_signal(closeadj):
    r=np.log(closeadj).diff()
    v5=r.rolling(5,min_periods=5).std(ddof=1); v21=r.rolling(21,min_periods=21).std(ddof=1)
    v63=r.rolling(63,min_periods=63).std(ddof=1); v252=r.rolling(252,min_periods=252).std(ddof=1)
    x_pts=np.log(np.array([5.0, 63.0, 252.0])); xm=x_pts - x_pts.mean(); sxx=(xm * xm).sum()
    x21=np.log(21.0)
    def _res(row):
        a, be, c, t = row
        ys=np.array([a, be, c], dtype=float)
        if np.any(~np.isfinite(ys)) or np.any(ys <= 0) or not np.isfinite(t) or t <= 0: return np.nan
        ly=np.log(ys); lym=ly - ly.mean()
        slope=(xm * lym).sum() / sxx; intercept=ly.mean() - slope * x_pts.mean()
        pred=intercept + slope * x21
        return float(np.log(t) - pred)
    df=pd.concat([v5, v63, v252, v21], axis=1)
    b=df.apply(_res, axis=1)
    return _j(b, 21).replace([np.inf,-np.inf],np.nan)

def f16vt_f16_realized_volatility_term_structure_volpctslope_21d_jerk_v059_signal(closeadj):
    r=np.log(closeadj).diff(); v21=r.rolling(21,min_periods=21).std(ddof=1)
    p=v21.rolling(252,min_periods=252).rank(pct=True)
    b=p.diff(10)
    return _j(b, 10).replace([np.inf,-np.inf],np.nan)

def f16vt_f16_realized_volatility_term_structure_logvolslope_63d_jerk_v060_signal(closeadj):
    r=np.log(closeadj).diff(); v63=r.rolling(63,min_periods=63).std(ddof=1)
    d=np.log(v63.replace(0.0,np.nan)).diff(21)
    b=np.sign(d).where(~d.isna())
    return _j(b, 21).replace([np.inf,-np.inf],np.nan)

def f16vt_f16_realized_volatility_term_structure_bipower_ratio_42d_jerk_v061_signal(closeadj):
    n=42; r=np.log(closeadj).diff(); ra=r.abs()
    bv=(ra * ra.shift(1)).rolling(n,min_periods=n).sum() * (np.pi / 2.0)
    qv=(r * r).rolling(n,min_periods=n).sum()
    b=bv / qv.replace(0.0,np.nan)
    return _j(b, 10).replace([np.inf,-np.inf],np.nan)

def f16vt_f16_realized_volatility_term_structure_jumpcomp_42d_jerk_v062_signal(closeadj):
    n=42; r=np.log(closeadj).diff(); ra=r.abs()
    rv=(r * r).rolling(n,min_periods=n).sum()
    bv=(ra * ra.shift(1)).rolling(n,min_periods=n).sum() * (np.pi / 2.0)
    j=(rv - bv).clip(lower=0.0)
    b=j / rv.replace(0.0,np.nan)
    return _j(b, 10).replace([np.inf,-np.inf],np.nan)

def f16vt_f16_realized_volatility_term_structure_curveskew_4h_jerk_v063_signal(closeadj):
    r=np.log(closeadj).diff()
    v5=r.rolling(5,min_periods=5).std(ddof=1); v21=r.rolling(21,min_periods=21).std(ddof=1)
    v63=r.rolling(63,min_periods=63).std(ddof=1); v252=r.rolling(252,min_periods=252).std(ddof=1)
    df=pd.concat([v5, v21, v63, v252], axis=1)
    b=df.skew(axis=1)
    return _j(b, 21).replace([np.inf,-np.inf],np.nan)

def f16vt_f16_realized_volatility_term_structure_curvekurt_4h_jerk_v064_signal(closeadj):
    r=np.log(closeadj).diff()
    v5=r.rolling(5,min_periods=5).std(ddof=1); v21=r.rolling(21,min_periods=21).std(ddof=1)
    v63=r.rolling(63,min_periods=63).std(ddof=1); v252=r.rolling(252,min_periods=252).std(ddof=1)
    df=pd.concat([v5, v21, v63, v252], axis=1)
    b=df.kurt(axis=1)
    return _j(b, 21).replace([np.inf,-np.inf],np.nan)

def f16vt_f16_realized_volatility_term_structure_daystrough_60d_jerk_v065_signal(closeadj):
    r=np.log(closeadj).diff(); v21=r.rolling(21,min_periods=21).std(ddof=1)
    mn=v21.rolling(60,min_periods=60).min()
    hit=(v21 <= mn * 1.0001).astype(float).where(~v21.isna() & ~mn.isna())
    b=hit.rolling(60,min_periods=60).apply(lambda x: _ds(x, 60.0), raw=True)
    return _j(b, 21).replace([np.inf,-np.inf],np.nan)

def f16vt_f16_realized_volatility_term_structure_dayspeak_120d_jerk_v066_signal(closeadj):
    r=np.log(closeadj).diff(); v21=r.rolling(21,min_periods=21).std(ddof=1)
    mx=v21.rolling(120,min_periods=120).max()
    hit=(v21 >= mx * 0.9999).astype(float).where(~v21.isna() & ~mx.isna())
    b=hit.rolling(120,min_periods=120).apply(lambda x: _ds(x, 120.0), raw=True)
    return _j(b, 63).replace([np.inf,-np.inf],np.nan)

def f16vt_f16_realized_volatility_term_structure_volsigncnt_3h_jerk_v067_signal(closeadj):
    r=np.log(closeadj).diff()
    v5=r.rolling(5,min_periods=5).std(ddof=1); v21=r.rolling(21,min_periods=21).std(ddof=1); v63=r.rolling(63,min_periods=63).std(ddof=1)
    s5=(v5.diff(5) > 0).astype(float).where(~v5.isna()); s21=(v21.diff(5) > 0).astype(float).where(~v21.isna()); s63=(v63.diff(5) > 0).astype(float).where(~v63.isna())
    b=s5 + s21 + s63
    return _j(b, 10).replace([np.inf,-np.inf],np.nan)

def f16vt_f16_realized_volatility_term_structure_logHLstd_5d_jerk_v068_signal(high, low):
    n=5; s=np.log(high / low.replace(0.0,np.nan))
    b=s.rolling(n,min_periods=n).std(ddof=1)
    return _j(b, 5).replace([np.inf,-np.inf],np.nan)

def f16vt_f16_realized_volatility_term_structure_logHLstd_63d_jerk_v069_signal(high, low):
    n=63; s=np.log(high / low.replace(0.0,np.nan))
    b=s.rolling(n,min_periods=n).std(ddof=1)
    return _j(b, 21).replace([np.inf,-np.inf],np.nan)

def f16vt_f16_realized_volatility_term_structure_HLcurvature_jerk_v070_signal(high, low):
    s=np.log(high / low.replace(0.0,np.nan))
    sv5=s.rolling(5,min_periods=5).std(ddof=1); sv21=s.rolling(21,min_periods=21).std(ddof=1); sv63=s.rolling(63,min_periods=63).std(ddof=1)
    b=sv5 - 2.0 * sv21 + sv63
    return _j(b, 21).replace([np.inf,-np.inf],np.nan)

def f16vt_f16_realized_volatility_term_structure_vol5_volofvol_jerk_v071_signal(closeadj):
    r=np.log(closeadj).diff()
    v5=r.rolling(5,min_periods=5).std(ddof=1); v21=r.rolling(21,min_periods=21).std(ddof=1)
    vov=v21.rolling(63,min_periods=63).std(ddof=1)
    b=v5 / vov.replace(0.0,np.nan)
    return _j(b, 10).replace([np.inf,-np.inf],np.nan)

def f16vt_f16_realized_volatility_term_structure_madratio_5_63_jerk_v072_signal(closeadj):
    r=np.log(closeadj).diff()
    mu5=r.rolling(5,min_periods=5).mean(); mu63=r.rolling(63,min_periods=63).mean()
    mad5=(r - mu5).abs().rolling(5,min_periods=5).mean(); mad63=(r - mu63).abs().rolling(63,min_periods=63).mean()
    b=mad5 / mad63.replace(0.0,np.nan)
    return _j(b, 21).replace([np.inf,-np.inf],np.nan)

def f16vt_f16_realized_volatility_term_structure_volzdiff_5_63_jerk_v073_signal(closeadj):
    r=np.log(closeadj).diff()
    v5=r.rolling(5,min_periods=5).std(ddof=1); v63=r.rolling(63,min_periods=63).std(ddof=1)
    p5=v5.rolling(252,min_periods=252).rank(pct=True); p63=v63.rolling(252,min_periods=252).rank(pct=True)
    b=p5 - p63
    return _j(b, 21).replace([np.inf,-np.inf],np.nan)

def f16vt_f16_realized_volatility_term_structure_highvolstreak_42d_jerk_v074_signal(closeadj):
    n=42; r=np.log(closeadj).diff().abs()
    q90=r.rolling(252,min_periods=252).quantile(0.9)
    hit=(r > q90).astype(float).where(~r.isna() & ~q90.isna())
    b=hit.rolling(n,min_periods=n).sum()
    return _j(b, 21).replace([np.inf,-np.inf],np.nan)

def f16vt_f16_realized_volatility_term_structure_normterm_60d_jerk_v075_signal(closeadj):
    r=np.log(closeadj).diff()
    v5=r.rolling(5,min_periods=5).std(ddof=1); v21=r.rolling(21,min_periods=21).std(ddof=1); v63=r.rolling(63,min_periods=63).std(ddof=1)
    norm=((v5 < v21) & (v21 < v63)).astype(float).where(~v5.isna() & ~v21.isna() & ~v63.isna())
    b=norm.rolling(60,min_periods=60).mean()
    return _j(b, 21).replace([np.inf,-np.inf],np.nan)


# --- 076-150 jerk: 2nd derivative of base 076-150 ---

def f16vt_f16_realized_volatility_term_structure_ewmavol_lam94_jerk_v076_signal(closeadj):
    r=np.log(closeadj).diff()
    b=np.sqrt((r * r).ewm(alpha=0.06, adjust=False, min_periods=20).mean())
    return _j(b, 5).replace([np.inf,-np.inf],np.nan)

def f16vt_f16_realized_volatility_term_structure_ewma_sign_94_97_jerk_v077_signal(closeadj):
    r=np.log(closeadj).diff()
    e94=np.sqrt((r * r).ewm(alpha=0.06, adjust=False, min_periods=20).mean())
    e97=np.sqrt((r * r).ewm(alpha=0.03, adjust=False, min_periods=40).mean())
    d=e94 - e97
    b=np.sign(d).where(~d.isna())
    return _j(b, 21).replace([np.inf,-np.inf],np.nan)

def f16vt_f16_realized_volatility_term_structure_ewmaratio_94_97_jerk_v078_signal(closeadj):
    r=np.log(closeadj).diff()
    e94=np.sqrt((r * r).ewm(alpha=0.06, adjust=False, min_periods=20).mean())
    e97=np.sqrt((r * r).ewm(alpha=0.03, adjust=False, min_periods=40).mean())
    b=e94 / e97.replace(0.0,np.nan)
    return (_j(b, 10) / b.abs().rolling(21,min_periods=10).mean().replace(0.0,np.nan)).replace([np.inf,-np.inf],np.nan)

def f16vt_f16_realized_volatility_term_structure_garchpersist_jerk_v079_signal(closeadj):
    n=60; r=np.log(closeadj).diff(); v21=r.rolling(21,min_periods=21).std(ddof=1)
    b=v21.rolling(n,min_periods=n).apply(_ac1, raw=True)
    return _j(b, 21).replace([np.inf,-np.inf],np.nan)

def f16vt_f16_realized_volatility_term_structure_volperdraw_42d_jerk_v080_signal(closeadj):
    n=42; r=np.log(closeadj).diff(); v21=r.rolling(21,min_periods=21).std(ddof=1)
    rmx=closeadj.rolling(n,min_periods=n).max()
    dd=(rmx - closeadj) / rmx.replace(0.0,np.nan)
    b=v21 / dd.replace(0.0,np.nan)
    return _j(b, 10).replace([np.inf,-np.inf],np.nan)

def f16vt_f16_realized_volatility_term_structure_volentropy_30d_jerk_v081_signal(closeadj):
    n=30; r=np.log(closeadj).diff(); v21=r.rolling(21,min_periods=21).std(ddof=1)
    med=v21.rolling(252,min_periods=252).median()
    h=(v21 > med).astype(float).where(~v21.isna() & ~med.isna())
    def _ent(x):
        p=float(np.nanmean(x))
        if not np.isfinite(p) or p <= 0.0 or p >= 1.0: return 0.0
        return float(-(p * np.log(p) + (1.0 - p) * np.log(1.0 - p)))
    b=h.rolling(n,min_periods=n).apply(_ent, raw=True)
    return _j(b, 10).replace([np.inf,-np.inf],np.nan)

def f16vt_f16_realized_volatility_term_structure_volsurge_5over63_jerk_v082_signal(closeadj):
    r=np.log(closeadj).diff()
    v5=r.rolling(5,min_periods=5).std(ddof=1); v63=r.rolling(63,min_periods=63).std(ddof=1)
    b=(v5 > 2.0 * v63).astype(float).where(~v5.isna() & ~v63.isna())
    return _j(b, 21).replace([np.inf,-np.inf],np.nan)

def f16vt_f16_realized_volatility_term_structure_volsurgefrac_60d_jerk_v083_signal(closeadj):
    r=np.log(closeadj).diff()
    v5=r.rolling(5,min_periods=5).std(ddof=1); v63=r.rolling(63,min_periods=63).std(ddof=1)
    s=(v5 > 1.5 * v63).astype(float).where(~v5.isna() & ~v63.isna())
    b=s.rolling(60,min_periods=60).mean()
    return _j(b, 21).replace([np.inf,-np.inf],np.nan)

def f16vt_f16_realized_volatility_term_structure_volrankslope_63d_jerk_v084_signal(closeadj):
    r=np.log(closeadj).diff(); v63=r.rolling(63,min_periods=63).std(ddof=1)
    p=v63.rolling(252,min_periods=252).rank(pct=True)
    b=p.diff(21)
    return _j(b, 21).replace([np.inf,-np.inf],np.nan)

def f16vt_f16_realized_volatility_term_structure_kurtpct_42d_jerk_v085_signal(closeadj):
    r=np.log(closeadj).diff(); k=r.rolling(42,min_periods=42).kurt()
    b=k.rolling(252,min_periods=120).rank(pct=True)
    return _j(b, 21).replace([np.inf,-np.inf],np.nan)

def f16vt_f16_realized_volatility_term_structure_skewpct_42d_jerk_v086_signal(closeadj):
    r=np.log(closeadj).diff(); k=r.rolling(42,min_periods=42).skew()
    b=k.rolling(252,min_periods=120).rank(pct=True)
    return _j(b, 21).replace([np.inf,-np.inf],np.nan)

def f16vt_f16_realized_volatility_term_structure_downvolratio_5_63_jerk_v087_signal(closeadj):
    r=np.log(closeadj).diff(); neg=r.where(r < 0)
    d5=neg.rolling(5,min_periods=3).std(ddof=1); d63=neg.rolling(63,min_periods=30).std(ddof=1)
    b=d5 / d63.replace(0.0,np.nan)
    return _j(b, 21).replace([np.inf,-np.inf],np.nan)

def f16vt_f16_realized_volatility_term_structure_updownratio_42d_jerk_v088_signal(closeadj):
    n=42; r=np.log(closeadj).diff()
    pos=r.where(r > 0); neg=r.where(r < 0)
    up=pos.rolling(n,min_periods=15).std(ddof=1); dn=neg.rolling(n,min_periods=15).std(ddof=1)
    b=up / dn.replace(0.0,np.nan)
    return _j(b, 10).replace([np.inf,-np.inf],np.nan)

def f16vt_f16_realized_volatility_term_structure_rangereal_5d_jerk_v089_signal(high, low, close):
    n=5; s=np.log(high / low.replace(0.0,np.nan)); rng_mean=s.rolling(n,min_periods=n).mean()
    r=np.log(close).diff(); rv=r.rolling(n,min_periods=n).std(ddof=1)
    b=rng_mean / rv.replace(0.0,np.nan)
    return _j(b, 5).replace([np.inf,-np.inf],np.nan)

def f16vt_f16_realized_volatility_term_structure_rangereal_63d_jerk_v090_signal(high, low, closeadj):
    n=63; s=np.log(high / low.replace(0.0,np.nan)); rng_mean=s.rolling(n,min_periods=n).mean()
    r=np.log(closeadj).diff(); rv=r.rolling(n,min_periods=n).std(ddof=1)
    b=rng_mean / rv.replace(0.0,np.nan)
    return _j(b, 21).replace([np.inf,-np.inf],np.nan)

def f16vt_f16_realized_volatility_term_structure_gktermratio_jerk_v091_signal(open_, high, low, close):
    gk=0.5 * (np.log(high / low.replace(0.0,np.nan))) ** 2 - (2.0 * np.log(2.0) - 1.0) * (np.log(close / open_.replace(0.0,np.nan))) ** 2
    g21=gk.rolling(21,min_periods=21).mean(); g63=gk.rolling(63,min_periods=63).mean()
    b=g21 / g63.replace(0.0,np.nan)
    return _j(b, 21).replace([np.inf,-np.inf],np.nan)

def f16vt_f16_realized_volatility_term_structure_volz_5on60_jerk_v092_signal(close):
    n=60; r=np.log(close).diff(); v5=r.rolling(5,min_periods=5).std(ddof=1)
    mu=v5.rolling(n,min_periods=n).mean(); sd=v5.rolling(n,min_periods=n).std(ddof=1)
    b=(v5 - mu) / sd.replace(0.0,np.nan)
    return (_j(b, 10) / b.abs().rolling(21,min_periods=10).mean().replace(0.0,np.nan)).replace([np.inf,-np.inf],np.nan)

def f16vt_f16_realized_volatility_term_structure_volz_252on500_jerk_v093_signal(closeadj):
    r=np.log(closeadj).diff(); v252=r.rolling(252,min_periods=252).std(ddof=1)
    mu=v252.rolling(500,min_periods=300).mean(); sd=v252.rolling(500,min_periods=300).std(ddof=1)
    b=(v252 - mu) / sd.replace(0.0,np.nan)
    return _j(b, 21).replace([np.inf,-np.inf],np.nan)

def f16vt_f16_realized_volatility_term_structure_madcurv_jerk_v094_signal(closeadj):
    r=np.log(closeadj).diff()
    def _mad(x, n):
        mu=x.rolling(n,min_periods=n).mean()
        return (x - mu).abs().rolling(n,min_periods=n).mean()
    m5=_mad(r, 5); m21=_mad(r, 21); m63=_mad(r, 63)
    b=m5 - 2.0 * m21 + m63
    return _j(b, 21).replace([np.inf,-np.inf],np.nan)

def f16vt_f16_realized_volatility_term_structure_vol_aboveMA_42d_jerk_v095_signal(closeadj):
    n=42; r=np.log(closeadj).diff(); v5=r.rolling(5,min_periods=5).std(ddof=1)
    mu=v5.rolling(21,min_periods=21).mean()
    flag=(v5 > mu).astype(float).where(~v5.isna() & ~mu.isna())
    b=flag.rolling(n,min_periods=n).mean()
    return _j(b, 10).replace([np.inf,-np.inf],np.nan)

def f16vt_f16_realized_volatility_term_structure_geomean_vols_jerk_v096_signal(closeadj):
    r=np.log(closeadj).diff()
    v5=r.rolling(5,min_periods=5).std(ddof=1); v21=r.rolling(21,min_periods=21).std(ddof=1); v63=r.rolling(63,min_periods=63).std(ddof=1)
    b=np.exp((np.log(v5.replace(0.0,np.nan)) + np.log(v21.replace(0.0,np.nan)) + np.log(v63.replace(0.0,np.nan))) / 3.0)
    return (_j(b, 63) / b.abs().rolling(63,min_periods=30).mean().replace(0.0,np.nan)).replace([np.inf,-np.inf],np.nan)

def f16vt_f16_realized_volatility_term_structure_volratio_rank_21_252_jerk_v097_signal(closeadj):
    r=np.log(closeadj).diff()
    v21=r.rolling(21,min_periods=21).std(ddof=1); v252=r.rolling(252,min_periods=252).std(ddof=1)
    ratio=v21 / v252.replace(0.0,np.nan)
    b=ratio.rolling(252,min_periods=120).rank(pct=True)
    return _j(b, 63).replace([np.inf,-np.inf],np.nan)

def f16vt_f16_realized_volatility_term_structure_curv_rank_jerk_v098_signal(closeadj):
    r=np.log(closeadj).diff()
    v5=r.rolling(5,min_periods=5).std(ddof=1); v21=r.rolling(21,min_periods=21).std(ddof=1); v63=r.rolling(63,min_periods=63).std(ddof=1)
    c=v5 - 2.0 * v21 + v63
    b=c.rolling(252,min_periods=120).rank(pct=True)
    return _j(b, 21).replace([np.inf,-np.inf],np.nan)

def f16vt_f16_realized_volatility_term_structure_sortino_vol_42d_jerk_v099_signal(closeadj):
    n=42; r=np.log(closeadj).diff(); mu=r.rolling(n,min_periods=n).mean()
    neg=r.where(r < 0); dn=neg.rolling(n,min_periods=15).std(ddof=1)
    b=mu / dn.replace(0.0,np.nan)
    return _j(b, 10).replace([np.inf,-np.inf],np.nan)

def f16vt_f16_realized_volatility_term_structure_volgap_5_21_pct_jerk_v100_signal(close):
    r=np.log(close).diff()
    v5=r.rolling(5,min_periods=5).std(ddof=1); v21=r.rolling(21,min_periods=21).std(ddof=1)
    b=(v5 - v21) / v21.replace(0.0,np.nan)
    return (_j(b, 5) / b.abs().rolling(21,min_periods=10).mean().replace(0.0,np.nan)).replace([np.inf,-np.inf],np.nan)

def f16vt_f16_realized_volatility_term_structure_volgap_63_252_pct_jerk_v101_signal(closeadj):
    r=np.log(closeadj).diff()
    v63=r.rolling(63,min_periods=63).std(ddof=1); v252=r.rolling(252,min_periods=252).std(ddof=1)
    b=(v63 - v252) / v252.replace(0.0,np.nan)
    return (_j(b, 21) / b.abs().rolling(63,min_periods=30).mean().replace(0.0,np.nan)).replace([np.inf,-np.inf],np.nan)

def f16vt_f16_realized_volatility_term_structure_kurtskew_diff_42d_jerk_v102_signal(closeadj):
    n=42; r=np.log(closeadj).diff()
    k=r.rolling(n,min_periods=n).kurt(); s=r.rolling(n,min_periods=n).skew()
    b=k - 3.0 * s.abs()
    return _j(b, 10).replace([np.inf,-np.inf],np.nan)

def f16vt_f16_realized_volatility_term_structure_termclass_jerk_v103_signal(closeadj):
    r=np.log(closeadj).diff()
    v5=r.rolling(5,min_periods=5).std(ddof=1); v21=r.rolling(21,min_periods=21).std(ddof=1); v63=r.rolling(63,min_periods=63).std(ddof=1)
    df=pd.concat([v5, v21, v63], axis=1)
    def _cls(row):
        a, be, c = row
        if not (np.isfinite(a) and np.isfinite(be) and np.isfinite(c)): return np.nan
        if a < be and be < c: return 0.0
        if be > a and be > c: return 1.0
        if be < a and be < c: return 2.0
        if a > be and be > c: return 3.0
        return 4.0
    b=df.apply(_cls, axis=1)
    return _j(b, 21).replace([np.inf,-np.inf],np.nan)

def f16vt_f16_realized_volatility_term_structure_hlvolslope_42d_jerk_v104_signal(high, low):
    s=np.log(high / low.replace(0.0,np.nan)); sv21=s.rolling(21,min_periods=21).std(ddof=1)
    b=sv21.diff(10)
    return _j(b, 10).replace([np.inf,-np.inf],np.nan)

def f16vt_f16_realized_volatility_term_structure_volofvol_rank_jerk_v105_signal(closeadj):
    r=np.log(closeadj).diff(); v21=r.rolling(21,min_periods=21).std(ddof=1)
    vov=v21.rolling(63,min_periods=63).std(ddof=1)
    b=vov.rolling(252,min_periods=120).rank(pct=True)
    return _j(b, 21).replace([np.inf,-np.inf],np.nan)

def f16vt_f16_realized_volatility_term_structure_lowvol_streak_jerk_v106_signal(closeadj):
    r=np.log(closeadj).diff(); v21=r.rolling(21,min_periods=21).std(ddof=1)
    q25=v21.rolling(252,min_periods=252).quantile(0.25)
    h=(v21 < q25).astype(float).where(~v21.isna() & ~q25.isna())
    grp=(h != h.shift(1)).cumsum(); b=h.groupby(grp).cumsum() * h
    return _j(b, 21).replace([np.inf,-np.inf],np.nan)

def f16vt_f16_realized_volatility_term_structure_absretvar_30d_jerk_v107_signal(closeadj):
    r=np.log(closeadj).diff().abs()
    b=r.rolling(30,min_periods=30).var(ddof=1)
    return _j(b, 10).replace([np.inf,-np.inf],np.nan)

def f16vt_f16_realized_volatility_term_structure_var95_42d_jerk_v108_signal(closeadj):
    n=42; r=np.log(closeadj).diff()
    b=r.rolling(n,min_periods=n).quantile(0.05)
    return _j(b, 10).replace([np.inf,-np.inf],np.nan)

def f16vt_f16_realized_volatility_term_structure_var95_120d_jerk_v109_signal(closeadj):
    n=120; r=np.log(closeadj).diff()
    b=r.rolling(n,min_periods=n).quantile(0.05)
    return _j(b, 21).replace([np.inf,-np.inf],np.nan)

def f16vt_f16_realized_volatility_term_structure_es95_42d_jerk_v110_signal(closeadj):
    n=42; r=np.log(closeadj).diff()
    def _es(x):
        x=np.asarray(x,dtype=float)
        if np.any(~np.isfinite(x)) or x.size < 10: return np.nan
        q=np.quantile(x, 0.05); tail=x[x <= q]
        if tail.size == 0: return np.nan
        return float(tail.mean())
    b=r.rolling(n,min_periods=n).apply(_es, raw=True)
    return _j(b, 10).replace([np.inf,-np.inf],np.nan)

def f16vt_f16_realized_volatility_term_structure_iqr_21d_jerk_v111_signal(close):
    n=21; r=np.log(close).diff()
    q75=r.rolling(n,min_periods=n).quantile(0.75); q25=r.rolling(n,min_periods=n).quantile(0.25)
    b=q75 - q25
    return _j(b, 5).replace([np.inf,-np.inf],np.nan)

def f16vt_f16_realized_volatility_term_structure_iqr_63d_jerk_v112_signal(closeadj):
    n=63; r=np.log(closeadj).diff()
    q75=r.rolling(n,min_periods=n).quantile(0.75); q25=r.rolling(n,min_periods=n).quantile(0.25)
    b=q75 - q25
    return _j(b, 21).replace([np.inf,-np.inf],np.nan)

def f16vt_f16_realized_volatility_term_structure_iqrratio_21_63_jerk_v113_signal(closeadj):
    r=np.log(closeadj).diff()
    iqr21=r.rolling(21,min_periods=21).quantile(0.75) - r.rolling(21,min_periods=21).quantile(0.25)
    iqr63=r.rolling(63,min_periods=63).quantile(0.75) - r.rolling(63,min_periods=63).quantile(0.25)
    b=iqr21 / iqr63.replace(0.0,np.nan)
    return _j(b, 21).replace([np.inf,-np.inf],np.nan)

def f16vt_f16_realized_volatility_term_structure_madmed_21d_jerk_v114_signal(close):
    n=21; r=np.log(close).diff(); med=r.rolling(n,min_periods=n).median()
    b=(r - med).abs().rolling(n,min_periods=n).median()
    return _j(b, 5).replace([np.inf,-np.inf],np.nan)

def f16vt_f16_realized_volatility_term_structure_bigmove_3sigma_42d_jerk_v115_signal(closeadj):
    n=42; r=np.log(closeadj).diff()
    sd=r.rolling(252,min_periods=252).std(ddof=1)
    flag=(r.abs() > 3.0 * sd).astype(float).where(~r.isna() & ~sd.isna())
    b=flag.rolling(n,min_periods=n).sum()
    return _j(b, 21).replace([np.inf,-np.inf],np.nan)

def f16vt_f16_realized_volatility_term_structure_termGini_jerk_v116_signal(closeadj):
    r=np.log(closeadj).diff()
    v5=r.rolling(5,min_periods=5).std(ddof=1); v21=r.rolling(21,min_periods=21).std(ddof=1)
    v63=r.rolling(63,min_periods=63).std(ddof=1); v252=r.rolling(252,min_periods=252).std(ddof=1)
    df=pd.concat([v5, v21, v63, v252], axis=1)
    def _g(row):
        y=np.asarray(row,dtype=float)
        if np.any(~np.isfinite(y)) or np.any(y <= 0): return np.nan
        ys=np.sort(y); nrm=ys.sum()
        if nrm <= 0: return np.nan
        cum=np.cumsum(ys) / nrm; n=len(y)
        return float(1.0 - 2.0 * (cum.sum() - 0.5) / n)
    b=df.apply(_g, axis=1)
    return _j(b, 21).replace([np.inf,-np.inf],np.nan)

def f16vt_f16_realized_volatility_term_structure_volgap_pct_5_252_jerk_v117_signal(closeadj):
    r=np.log(closeadj).diff()
    v5=r.rolling(5,min_periods=5).std(ddof=1); v252=r.rolling(252,min_periods=252).std(ddof=1)
    p5=v5.rolling(252,min_periods=120).rank(pct=True); p252=v252.rolling(500,min_periods=260).rank(pct=True)
    b=np.sign(p5 - p252).where(~p5.isna() & ~p252.isna())
    return _j(b, 63).replace([np.inf,-np.inf],np.nan)

def f16vt_f16_realized_volatility_term_structure_vovslope_jerk_v118_signal(closeadj):
    r=np.log(closeadj).diff(); v21=r.rolling(21,min_periods=21).std(ddof=1)
    vov=v21.rolling(63,min_periods=63).std(ddof=1)
    b=vov.diff(21)
    return _j(b, 21).replace([np.inf,-np.inf],np.nan)

def f16vt_f16_realized_volatility_term_structure_voldiragree_jerk_v119_signal(closeadj):
    r=np.log(closeadj).diff()
    v5=r.rolling(5,min_periods=5).std(ddof=1); v21=r.rolling(21,min_periods=21).std(ddof=1)
    d5=v5.diff(5); d21=v21.diff(5)
    out=pd.Series(np.where((d5 > 0) & (d21 > 0), 1.0, np.where((d5 < 0) & (d21 < 0), -1.0, 0.0)), index=v5.index, dtype=float)
    b=out.where(~d5.isna() & ~d21.isna())
    return _j(b, 10).replace([np.inf,-np.inf],np.nan)

def f16vt_f16_realized_volatility_term_structure_curvesmooth_jerk_v120_signal(closeadj):
    r=np.log(closeadj).diff()
    v5=r.rolling(5,min_periods=5).std(ddof=1); v21=r.rolling(21,min_periods=21).std(ddof=1); v63=r.rolling(63,min_periods=63).std(ddof=1)
    b=(v5 - v21).abs() + (v63 - v21).abs()
    return _j(b, 10).replace([np.inf,-np.inf],np.nan)

def f16vt_f16_realized_volatility_term_structure_volxover_60d_jerk_v121_signal(closeadj):
    n=60; r=np.log(closeadj).diff()
    v5=r.rolling(5,min_periods=5).std(ddof=1); v21=r.rolling(21,min_periods=21).std(ddof=1)
    s=np.sign(v5 - v21)
    flip=(s != s.shift(1)).astype(float).where(~s.isna() & ~s.shift(1).isna())
    b=flip.rolling(n,min_periods=n).sum()
    return _j(b, 21).replace([np.inf,-np.inf],np.nan)

def f16vt_f16_realized_volatility_term_structure_argmaxhorizon_jerk_v122_signal(closeadj):
    r=np.log(closeadj).diff()
    v5=r.rolling(5,min_periods=5).std(ddof=1); v21=r.rolling(21,min_periods=21).std(ddof=1)
    v63=r.rolling(63,min_periods=63).std(ddof=1); v252=r.rolling(252,min_periods=252).std(ddof=1)
    df=pd.concat([v5, v21, v63, v252], axis=1)
    def _a(row):
        y=np.asarray(row,dtype=float)
        if np.any(~np.isfinite(y)): return np.nan
        return float(np.argmax(y))
    b=df.apply(_a, axis=1)
    return _j(b, 21).replace([np.inf,-np.inf],np.nan)

def f16vt_f16_realized_volatility_term_structure_sumr2_21on63_jerk_v123_signal(closeadj):
    r=np.log(closeadj).diff()
    rv21=(r * r).rolling(21,min_periods=21).sum(); rv63=(r * r).rolling(63,min_periods=63).sum()
    b=rv21 / rv63.replace(0.0,np.nan)
    return _j(b, 21).replace([np.inf,-np.inf],np.nan)

def f16vt_f16_realized_volatility_term_structure_volhalflife_jerk_v124_signal(closeadj):
    n=120; r=np.log(closeadj).diff()
    v21=np.log(r.rolling(21,min_periods=21).std(ddof=1).replace(0.0,np.nan))
    def _hl(x):
        x=np.asarray(x,dtype=float)
        if np.any(~np.isfinite(x)) or x.size < 30: return np.nan
        a=x[:-1]; bb=x[1:]; sa=a.std(ddof=0); sb=bb.std(ddof=0)
        if sa <= 0 or sb <= 0: return np.nan
        rho=float(((a - a.mean()) * (bb - bb.mean())).mean() / (sa * sb))
        if rho >= 0.999 or rho <= -0.999: return 252.0
        if rho <= 0: return 1.0
        return float(min(252.0, -np.log(2.0) / np.log(rho)))
    b=v21.rolling(n,min_periods=n).apply(_hl, raw=True)
    return _j(b, 63).replace([np.inf,-np.inf],np.nan)

def f16vt_f16_realized_volatility_term_structure_volmeanshift_jerk_v125_signal(closeadj):
    r=np.log(closeadj).diff(); v21=r.rolling(21,min_periods=21).std(ddof=1)
    m1=v21.rolling(21,min_periods=21).mean(); m2=v21.rolling(63,min_periods=63).mean()
    b=m1 - m2
    return _j(b, 21).replace([np.inf,-np.inf],np.nan)

def f16vt_f16_realized_volatility_term_structure_vol2derivpct_jerk_v126_signal(closeadj):
    r=np.log(closeadj).diff(); v21=r.rolling(21,min_periods=21).std(ddof=1)
    accel=(v21 - 2.0 * v21.shift(5) + v21.shift(10)).abs()
    b=accel.rolling(252,min_periods=120).rank(pct=True)
    return _j(b, 21).replace([np.inf,-np.inf],np.nan)

def f16vt_f16_realized_volatility_term_structure_volrank_diff_5_21_jerk_v127_signal(close):
    r=np.log(close).diff()
    v5=r.rolling(5,min_periods=5).std(ddof=1); v21=r.rolling(21,min_periods=21).std(ddof=1)
    p5=v5.rolling(120,min_periods=80).rank(pct=True); p21=v21.rolling(120,min_periods=80).rank(pct=True)
    b=p5 - p21
    return _j(b, 10).replace([np.inf,-np.inf],np.nan)

def f16vt_f16_realized_volatility_term_structure_signedvol_21d_jerk_v128_signal(close):
    r=np.log(close).diff(); mu=r.rolling(21,min_periods=21).mean(); v21=r.rolling(21,min_periods=21).std(ddof=1)
    b=np.sign(mu) * v21
    return _j(b, 10).replace([np.inf,-np.inf],np.nan)

def f16vt_f16_realized_volatility_term_structure_ewma_termratio_jerk_v129_signal(closeadj):
    r=np.log(closeadj).diff()
    e=np.sqrt((r * r).ewm(alpha=0.06, adjust=False, min_periods=20).mean())
    v63=r.rolling(63,min_periods=63).std(ddof=1)
    b=e / v63.replace(0.0,np.nan)
    return _j(b, 21).replace([np.inf,-np.inf],np.nan)

def f16vt_f16_realized_volatility_term_structure_volcorr_5_63_jerk_v130_signal(closeadj):
    r=np.log(closeadj).diff()
    v5=r.rolling(5,min_periods=5).std(ddof=1); v63=r.rolling(63,min_periods=63).std(ddof=1)
    b=v5.rolling(63,min_periods=40).corr(v63)
    return _j(b, 21).replace([np.inf,-np.inf],np.nan)

def f16vt_f16_realized_volatility_term_structure_bvrv_diff_21_63_jerk_v131_signal(closeadj):
    r=np.log(closeadj).diff(); ra=r.abs()
    bv21=(ra * ra.shift(1)).rolling(21,min_periods=21).sum() * (np.pi / 2.0)
    rv21=(r * r).rolling(21,min_periods=21).sum()
    bv63=(ra * ra.shift(1)).rolling(63,min_periods=63).sum() * (np.pi / 2.0)
    rv63=(r * r).rolling(63,min_periods=63).sum()
    b=(bv21 / rv21.replace(0.0,np.nan)) - (bv63 / rv63.replace(0.0,np.nan))
    return _j(b, 21).replace([np.inf,-np.inf],np.nan)

def f16vt_f16_realized_volatility_term_structure_tailasym_42d_jerk_v132_signal(closeadj):
    n=42; r=np.log(closeadj).diff()
    mn=r.rolling(n,min_periods=n).min().abs(); mx=r.rolling(n,min_periods=n).max()
    b=mn / mx.replace(0.0,np.nan)
    return _j(b, 10).replace([np.inf,-np.inf],np.nan)

def f16vt_f16_realized_volatility_term_structure_hlrange_63d_jerk_v134_signal(high, low, closeadj):
    n=63
    b=((high - low) / closeadj.replace(0.0,np.nan)).rolling(n,min_periods=n).mean()
    return _j(b, 21).replace([np.inf,-np.inf],np.nan)

def f16vt_f16_realized_volatility_term_structure_hlrange_zscore_jerk_v135_signal(high, low, closeadj):
    rng=(high - low) / closeadj.replace(0.0,np.nan)
    m21=rng.rolling(21,min_periods=21).mean()
    mu=m21.rolling(252,min_periods=120).mean(); sd=m21.rolling(252,min_periods=120).std(ddof=1)
    b=(m21 - mu) / sd.replace(0.0,np.nan)
    return _j(b, 21).replace([np.inf,-np.inf],np.nan)

def f16vt_f16_realized_volatility_term_structure_volaccelsign_jerk_v136_signal(closeadj):
    r=np.log(closeadj).diff(); v21=r.rolling(21,min_periods=21).std(ddof=1)
    acc=v21.diff(5).diff(5)
    b=np.sign(acc).where(~acc.isna())
    return _j(b, 10).replace([np.inf,-np.inf],np.nan)

def f16vt_f16_realized_volatility_term_structure_skewratio_21_63_jerk_v137_signal(closeadj):
    r=np.log(closeadj).diff()
    b=r.rolling(21,min_periods=21).skew() - r.rolling(63,min_periods=63).skew()
    return _j(b, 21).replace([np.inf,-np.inf],np.nan)

def f16vt_f16_realized_volatility_term_structure_kurtdiff_21_63_jerk_v138_signal(closeadj):
    r=np.log(closeadj).diff()
    b=r.rolling(21,min_periods=21).kurt() - r.rolling(63,min_periods=63).kurt()
    return _j(b, 21).replace([np.inf,-np.inf],np.nan)

def f16vt_f16_realized_volatility_term_structure_q9diff_21_63_jerk_v139_signal(closeadj):
    r=np.log(closeadj).diff()
    b=r.rolling(21,min_periods=21).quantile(0.9) - r.rolling(63,min_periods=63).quantile(0.9)
    return _j(b, 21).replace([np.inf,-np.inf],np.nan)

def f16vt_f16_realized_volatility_term_structure_tanh_volvar_42d_jerk_v140_signal(closeadj):
    r=np.log(closeadj).diff(); v5=r.rolling(5,min_periods=5).std(ddof=1)
    mu=v5.rolling(42,min_periods=42).mean(); var=v5.rolling(42,min_periods=42).var(ddof=1)
    cov2=var / (mu * mu).replace(0.0,np.nan)
    b=np.tanh(cov2 * 5.0)
    return _j(b, 10).replace([np.inf,-np.inf],np.nan)

def f16vt_f16_realized_volatility_term_structure_arctanslope_jerk_v141_signal(closeadj):
    r=np.log(closeadj).diff()
    v5=r.rolling(5,min_periods=5).std(ddof=1); v63=r.rolling(63,min_periods=63).std(ddof=1); v252=r.rolling(252,min_periods=252).std(ddof=1)
    x=np.log(np.array([5.0, 63.0, 252.0])); xm=x - x.mean(); sxx=(xm * xm).sum()
    def _s(row):
        y=np.array(row,dtype=float)
        if np.any(~np.isfinite(y)) or np.any(y <= 0): return np.nan
        ly=np.log(y); lym=ly - ly.mean()
        return float(np.arctan((xm * lym).sum() / sxx))
    df=pd.concat([v5, v63, v252], axis=1)
    b=df.apply(_s, axis=1)
    return _j(b, 21).replace([np.inf,-np.inf],np.nan)

def f16vt_f16_realized_volatility_term_structure_ddvolasym_42d_jerk_v142_signal(closeadj):
    n=42; rm=closeadj.rolling(n,min_periods=n).max(); rmn=closeadj.rolling(n,min_periods=n).min()
    dd=(closeadj - rm) / rm.replace(0.0,np.nan); du=(closeadj - rmn) / rmn.replace(0.0,np.nan)
    b=du.abs() - dd.abs()
    return _j(b, 10).replace([np.inf,-np.inf],np.nan)

def f16vt_f16_realized_volatility_term_structure_volsignstreak_jerk_v143_signal(closeadj):
    r=np.log(closeadj).diff(); v21=r.rolling(21,min_periods=21).std(ddof=1)
    s=np.sign(v21.diff()).where(~v21.isna() & ~v21.diff().isna())
    grp=(s != s.shift(1)).cumsum(); streak=s.groupby(grp).cumcount() + 1
    b=streak * np.sign(s)
    return _j(b, 21).replace([np.inf,-np.inf],np.nan)

def f16vt_f16_realized_volatility_term_structure_regimecombo_jerk_v144_signal(closeadj):
    r=np.log(closeadj).diff()
    v5=r.rolling(5,min_periods=5).std(ddof=1); v63=r.rolling(63,min_periods=63).std(ddof=1)
    p5=v5.rolling(120,min_periods=80).rank(pct=True); p63=v63.rolling(252,min_periods=120).rank(pct=True)
    b=((p5 > 0.7) & (p63 < 0.3)).astype(float).where(~p5.isna() & ~p63.isna())
    return _j(b, 21).replace([np.inf,-np.inf],np.nan)

def f16vt_f16_realized_volatility_term_structure_curvslopediff_jerk_v145_signal(closeadj):
    r=np.log(closeadj).diff()
    v5=r.rolling(5,min_periods=5).std(ddof=1); v21=r.rolling(21,min_periods=21).std(ddof=1); v63=r.rolling(63,min_periods=63).std(ddof=1)
    b=(v5 - v21).diff(5) + (v63 - v21).diff(5)
    return _j(b, 21).replace([np.inf,-np.inf],np.nan)

def f16vt_f16_realized_volatility_term_structure_arctan_volpersist_jerk_v146_signal(closeadj):
    n=60; r=np.log(closeadj).diff(); v21=r.rolling(21,min_periods=21).std(ddof=1)
    def _ac5(x):
        x=np.asarray(x,dtype=float)
        if np.any(~np.isfinite(x)) or x.size < 12: return np.nan
        a=x[:-5]; bb=x[5:]; sa=a.std(ddof=0); sb=bb.std(ddof=0)
        if sa <= 0 or sb <= 0: return np.nan
        return float(((a - a.mean()) * (bb - bb.mean())).mean() / (sa * sb))
    ac=v21.rolling(n,min_periods=n).apply(_ac5, raw=True)
    b=np.arctan(ac * 2.0)
    return _j(b, 21).replace([np.inf,-np.inf],np.nan)

def f16vt_f16_realized_volatility_term_structure_tailcount_60d_jerk_v147_signal(closeadj):
    n=60; r=np.log(closeadj).diff().abs()
    q95=r.rolling(252,min_periods=252).quantile(0.95)
    flag=(r > q95).astype(float).where(~r.isna() & ~q95.isna())
    b=flag.rolling(n,min_periods=n).sum()
    return _j(b, 21).replace([np.inf,-np.inf],np.nan)

def f16vt_f16_realized_volatility_term_structure_roughratio_30_120_jerk_v148_signal(closeadj):
    r=np.log(closeadj).diff()
    n30=r.diff().abs().rolling(30,min_periods=30).sum(); d30=r.abs().rolling(30,min_periods=30).sum()
    n120=r.diff().abs().rolling(120,min_periods=120).sum(); d120=r.abs().rolling(120,min_periods=120).sum()
    r30=n30 / d30.replace(0.0,np.nan); r120=n120 / d120.replace(0.0,np.nan)
    b=r30 / r120.replace(0.0,np.nan)
    return _j(b, 21).replace([np.inf,-np.inf],np.nan)

def f16vt_f16_realized_volatility_term_structure_volltrend_60d_jerk_v149_signal(closeadj):
    n=60; r=np.log(closeadj).diff(); v21=r.rolling(21,min_periods=21).std(ddof=1)
    t=pd.Series(np.arange(len(v21), dtype=float), index=v21.index)
    b=v21.rolling(n,min_periods=n).corr(t)
    return _j(b, 21).replace([np.inf,-np.inf],np.nan)

def f16vt_f16_realized_volatility_term_structure_volstickyabove_jerk_v150_signal(closeadj):
    n=21; r=np.log(closeadj).diff()
    v5=r.rolling(5,min_periods=5).std(ddof=1); v21=r.rolling(21,min_periods=21).std(ddof=1); v63=r.rolling(63,min_periods=63).std(ddof=1)
    inv=((v5 > v21) & (v21 > v63)).astype(float).where(~v5.isna() & ~v21.isna() & ~v63.isna())
    b=inv.rolling(n,min_periods=n).mean()
    return _j(b, 10).replace([np.inf,-np.inf],np.nan)


# ---------------------------------------------------------------------------
# Registry (introspection-based for compactness)
# ---------------------------------------------------------------------------


_ALL_FNS = [
    f16vt_f16_realized_volatility_term_structure_rv_5d_jerk_v001_signal, f16vt_f16_realized_volatility_term_structure_rv_63d_jerk_v002_signal, f16vt_f16_realized_volatility_term_structure_rv_252d_jerk_v003_signal,
    f16vt_f16_realized_volatility_term_structure_rvratio_5_21_jerk_v004_signal, f16vt_f16_realized_volatility_term_structure_rvratio_21_63_jerk_v005_signal, f16vt_f16_realized_volatility_term_structure_rvratio_63_252_jerk_v006_signal,
    f16vt_f16_realized_volatility_term_structure_termpctrank_5_252_jerk_v007_signal, f16vt_f16_realized_volatility_term_structure_invertcount_5_21_jerk_v008_signal, f16vt_f16_realized_volatility_term_structure_logslope_21_252_jerk_v009_signal,
    f16vt_f16_realized_volatility_term_structure_curv_5_21_63_jerk_v010_signal, f16vt_f16_realized_volatility_term_structure_curv_21_63_252_jerk_v011_signal, f16vt_f16_realized_volatility_term_structure_convexity_jerk_v012_signal,
    f16vt_f16_realized_volatility_term_structure_vol21slope_5d_jerk_v013_signal, f16vt_f16_realized_volatility_term_structure_vol63slope_21d_jerk_v014_signal, f16vt_f16_realized_volatility_term_structure_vol21accel_jerk_v015_signal,
    f16vt_f16_realized_volatility_term_structure_volpct_21on252_jerk_v016_signal, f16vt_f16_realized_volatility_term_structure_volz_21on120_jerk_v017_signal, f16vt_f16_realized_volatility_term_structure_volquint_5d_jerk_v018_signal,
    f16vt_f16_realized_volatility_term_structure_dayssince_volp90_jerk_v019_signal, f16vt_f16_realized_volatility_term_structure_streakhighvol_jerk_v020_signal,
    f16vt_f16_realized_volatility_term_structure_hlrvratio_21d_jerk_v021_signal, f16vt_f16_realized_volatility_term_structure_hlrvratio_63d_jerk_v022_signal,
    f16vt_f16_realized_volatility_term_structure_retskew_21d_jerk_v023_signal, f16vt_f16_realized_volatility_term_structure_retskew_63d_jerk_v024_signal, f16vt_f16_realized_volatility_term_structure_retkurt_21d_jerk_v025_signal, f16vt_f16_realized_volatility_term_structure_retkurt_63d_jerk_v026_signal,
    f16vt_f16_realized_volatility_term_structure_downvol_21d_jerk_v027_signal, f16vt_f16_realized_volatility_term_structure_upvol_63d_jerk_v028_signal, f16vt_f16_realized_volatility_term_structure_varasym_42d_jerk_v029_signal,
    f16vt_f16_realized_volatility_term_structure_absretacf1_30d_jerk_v030_signal, f16vt_f16_realized_volatility_term_structure_sqretacf1_60d_jerk_v031_signal, f16vt_f16_realized_volatility_term_structure_volpersist_30d_jerk_v032_signal,
    f16vt_f16_realized_volatility_term_structure_curveR2_4pt_jerk_v033_signal, f16vt_f16_realized_volatility_term_structure_curveslopesign_jerk_v034_signal, f16vt_f16_realized_volatility_term_structure_invertedsign_jerk_v035_signal,
    f16vt_f16_realized_volatility_term_structure_invertedfrac_60d_jerk_v036_signal, f16vt_f16_realized_volatility_term_structure_volconeshort_5on120_jerk_v037_signal, f16vt_f16_realized_volatility_term_structure_volconedelta_jerk_v038_signal,
    f16vt_f16_realized_volatility_term_structure_voldirsign_21d_jerk_v039_signal, f16vt_f16_realized_volatility_term_structure_volcontract_30d_jerk_v040_signal, f16vt_f16_realized_volatility_term_structure_volexpand_30d_jerk_v041_signal,
    f16vt_f16_realized_volatility_term_structure_avgvol_3h_jerk_v042_signal, f16vt_f16_realized_volatility_term_structure_volhdisp_3h_jerk_v043_signal, f16vt_f16_realized_volatility_term_structure_medianvol_4h_jerk_v044_signal,
    f16vt_f16_realized_volatility_term_structure_arctanlogvol_21d_jerk_v045_signal, f16vt_f16_realized_volatility_term_structure_tanhvolzdelta_jerk_v046_signal, f16vt_f16_realized_volatility_term_structure_sigmoidvolpct_jerk_v047_signal,
    f16vt_f16_realized_volatility_term_structure_madstd_ratio_21d_jerk_v048_signal, f16vt_f16_realized_volatility_term_structure_rms_42d_jerk_v049_signal, f16vt_f16_realized_volatility_term_structure_rvarratio_5_63_jerk_v050_signal,
    f16vt_f16_realized_volatility_term_structure_volofvol_long_jerk_v057_signal, f16vt_f16_realized_volatility_term_structure_curvres21_jerk_v058_signal, f16vt_f16_realized_volatility_term_structure_volpctslope_21d_jerk_v059_signal,
    f16vt_f16_realized_volatility_term_structure_logvolslope_63d_jerk_v060_signal, f16vt_f16_realized_volatility_term_structure_bipower_ratio_42d_jerk_v061_signal, f16vt_f16_realized_volatility_term_structure_jumpcomp_42d_jerk_v062_signal,
    f16vt_f16_realized_volatility_term_structure_curveskew_4h_jerk_v063_signal, f16vt_f16_realized_volatility_term_structure_curvekurt_4h_jerk_v064_signal, f16vt_f16_realized_volatility_term_structure_daystrough_60d_jerk_v065_signal,
    f16vt_f16_realized_volatility_term_structure_dayspeak_120d_jerk_v066_signal, f16vt_f16_realized_volatility_term_structure_volsigncnt_3h_jerk_v067_signal, f16vt_f16_realized_volatility_term_structure_logHLstd_5d_jerk_v068_signal,
    f16vt_f16_realized_volatility_term_structure_logHLstd_63d_jerk_v069_signal, f16vt_f16_realized_volatility_term_structure_HLcurvature_jerk_v070_signal, f16vt_f16_realized_volatility_term_structure_vol5_volofvol_jerk_v071_signal,
    f16vt_f16_realized_volatility_term_structure_madratio_5_63_jerk_v072_signal, f16vt_f16_realized_volatility_term_structure_volzdiff_5_63_jerk_v073_signal, f16vt_f16_realized_volatility_term_structure_highvolstreak_42d_jerk_v074_signal,
    f16vt_f16_realized_volatility_term_structure_normterm_60d_jerk_v075_signal,
    f16vt_f16_realized_volatility_term_structure_ewmavol_lam94_jerk_v076_signal, f16vt_f16_realized_volatility_term_structure_ewma_sign_94_97_jerk_v077_signal, f16vt_f16_realized_volatility_term_structure_ewmaratio_94_97_jerk_v078_signal,
    f16vt_f16_realized_volatility_term_structure_garchpersist_jerk_v079_signal, f16vt_f16_realized_volatility_term_structure_volperdraw_42d_jerk_v080_signal, f16vt_f16_realized_volatility_term_structure_volentropy_30d_jerk_v081_signal,
    f16vt_f16_realized_volatility_term_structure_volsurge_5over63_jerk_v082_signal, f16vt_f16_realized_volatility_term_structure_volsurgefrac_60d_jerk_v083_signal, f16vt_f16_realized_volatility_term_structure_volrankslope_63d_jerk_v084_signal,
    f16vt_f16_realized_volatility_term_structure_kurtpct_42d_jerk_v085_signal, f16vt_f16_realized_volatility_term_structure_skewpct_42d_jerk_v086_signal, f16vt_f16_realized_volatility_term_structure_downvolratio_5_63_jerk_v087_signal,
    f16vt_f16_realized_volatility_term_structure_updownratio_42d_jerk_v088_signal, f16vt_f16_realized_volatility_term_structure_rangereal_5d_jerk_v089_signal, f16vt_f16_realized_volatility_term_structure_rangereal_63d_jerk_v090_signal,
    f16vt_f16_realized_volatility_term_structure_gktermratio_jerk_v091_signal, f16vt_f16_realized_volatility_term_structure_volz_5on60_jerk_v092_signal, f16vt_f16_realized_volatility_term_structure_volz_252on500_jerk_v093_signal,
    f16vt_f16_realized_volatility_term_structure_madcurv_jerk_v094_signal, f16vt_f16_realized_volatility_term_structure_vol_aboveMA_42d_jerk_v095_signal, f16vt_f16_realized_volatility_term_structure_geomean_vols_jerk_v096_signal,
    f16vt_f16_realized_volatility_term_structure_volratio_rank_21_252_jerk_v097_signal, f16vt_f16_realized_volatility_term_structure_curv_rank_jerk_v098_signal, f16vt_f16_realized_volatility_term_structure_sortino_vol_42d_jerk_v099_signal,
    f16vt_f16_realized_volatility_term_structure_volgap_5_21_pct_jerk_v100_signal, f16vt_f16_realized_volatility_term_structure_volgap_63_252_pct_jerk_v101_signal, f16vt_f16_realized_volatility_term_structure_kurtskew_diff_42d_jerk_v102_signal,
    f16vt_f16_realized_volatility_term_structure_termclass_jerk_v103_signal, f16vt_f16_realized_volatility_term_structure_hlvolslope_42d_jerk_v104_signal, f16vt_f16_realized_volatility_term_structure_volofvol_rank_jerk_v105_signal,
    f16vt_f16_realized_volatility_term_structure_lowvol_streak_jerk_v106_signal, f16vt_f16_realized_volatility_term_structure_absretvar_30d_jerk_v107_signal, f16vt_f16_realized_volatility_term_structure_var95_42d_jerk_v108_signal,
    f16vt_f16_realized_volatility_term_structure_var95_120d_jerk_v109_signal, f16vt_f16_realized_volatility_term_structure_es95_42d_jerk_v110_signal, f16vt_f16_realized_volatility_term_structure_iqr_21d_jerk_v111_signal,
    f16vt_f16_realized_volatility_term_structure_iqr_63d_jerk_v112_signal, f16vt_f16_realized_volatility_term_structure_iqrratio_21_63_jerk_v113_signal, f16vt_f16_realized_volatility_term_structure_madmed_21d_jerk_v114_signal,
    f16vt_f16_realized_volatility_term_structure_bigmove_3sigma_42d_jerk_v115_signal, f16vt_f16_realized_volatility_term_structure_termGini_jerk_v116_signal, f16vt_f16_realized_volatility_term_structure_volgap_pct_5_252_jerk_v117_signal,
    f16vt_f16_realized_volatility_term_structure_vovslope_jerk_v118_signal, f16vt_f16_realized_volatility_term_structure_voldiragree_jerk_v119_signal, f16vt_f16_realized_volatility_term_structure_curvesmooth_jerk_v120_signal,
    f16vt_f16_realized_volatility_term_structure_volxover_60d_jerk_v121_signal, f16vt_f16_realized_volatility_term_structure_argmaxhorizon_jerk_v122_signal, f16vt_f16_realized_volatility_term_structure_sumr2_21on63_jerk_v123_signal,
    f16vt_f16_realized_volatility_term_structure_volhalflife_jerk_v124_signal, f16vt_f16_realized_volatility_term_structure_volmeanshift_jerk_v125_signal, f16vt_f16_realized_volatility_term_structure_vol2derivpct_jerk_v126_signal,
    f16vt_f16_realized_volatility_term_structure_volrank_diff_5_21_jerk_v127_signal, f16vt_f16_realized_volatility_term_structure_signedvol_21d_jerk_v128_signal, f16vt_f16_realized_volatility_term_structure_ewma_termratio_jerk_v129_signal,
    f16vt_f16_realized_volatility_term_structure_volcorr_5_63_jerk_v130_signal, f16vt_f16_realized_volatility_term_structure_bvrv_diff_21_63_jerk_v131_signal, f16vt_f16_realized_volatility_term_structure_tailasym_42d_jerk_v132_signal,
    f16vt_f16_realized_volatility_term_structure_volaccelsign_jerk_v136_signal, f16vt_f16_realized_volatility_term_structure_skewratio_21_63_jerk_v137_signal, f16vt_f16_realized_volatility_term_structure_kurtdiff_21_63_jerk_v138_signal,
    f16vt_f16_realized_volatility_term_structure_q9diff_21_63_jerk_v139_signal, f16vt_f16_realized_volatility_term_structure_tanh_volvar_42d_jerk_v140_signal, f16vt_f16_realized_volatility_term_structure_arctanslope_jerk_v141_signal,
    f16vt_f16_realized_volatility_term_structure_ddvolasym_42d_jerk_v142_signal, f16vt_f16_realized_volatility_term_structure_volsignstreak_jerk_v143_signal, f16vt_f16_realized_volatility_term_structure_regimecombo_jerk_v144_signal,
    f16vt_f16_realized_volatility_term_structure_curvslopediff_jerk_v145_signal, f16vt_f16_realized_volatility_term_structure_arctan_volpersist_jerk_v146_signal, f16vt_f16_realized_volatility_term_structure_tailcount_60d_jerk_v147_signal,
    f16vt_f16_realized_volatility_term_structure_roughratio_30_120_jerk_v148_signal, f16vt_f16_realized_volatility_term_structure_volltrend_60d_jerk_v149_signal, f16vt_f16_realized_volatility_term_structure_volstickyabove_jerk_v150_signal,
]
_ALL_FNS = sorted(
    [
        v for name, v in globals().items()
        if name.startswith("f16vt_f16_realized_volatility_term_structure_")
        and name.endswith("_signal")
        and callable(v)
    ],
    key=lambda fn: fn.__name__,
)

def _build_registry():
    reg = {}
    for v in _ALL_FNS:
        sig = inspect.signature(v)
        inputs = [(p if p != "open_" else "open") for p in sig.parameters]
        reg[v.__name__] = {"inputs": inputs, "func": v}
    return reg


f16_realized_volatility_term_structure_jerk_001_150_REGISTRY = _build_registry()
assert len(f16_realized_volatility_term_structure_jerk_001_150_REGISTRY) == len(_ALL_FNS), "jerk registry length mismatch"


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
    for name, entry in f16_realized_volatility_term_structure_jerk_001_150_REGISTRY.items():
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
        cnt = 0
        for i, a in enumerate(corr.columns):
            for j, b in enumerate(corr.columns):
                if j > i and corr.iloc[i, j] > 0.94:
                    print(f"  {a}  vs  {b}  ->  {corr.iloc[i, j]:.4f}")
                    cnt += 1
                    if cnt > 30: break
            if cnt > 30: break
    assert max_corr <= 0.95 + 1e-9, f"max pairwise |corr|={max_corr:.4f} exceeds 0.95"
    print(f"OK jerk_001_150: {len(results)} features, max |corr|={max_corr:.4f}, coverage_ok={frac:.2%}")


if __name__ == "__main__":
    _self_test()
