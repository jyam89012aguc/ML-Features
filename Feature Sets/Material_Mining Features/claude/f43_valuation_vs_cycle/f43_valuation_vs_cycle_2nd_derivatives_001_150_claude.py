import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
TRADING_DAYS_TWOYEAR = 504
TRADING_DAYS_FIVEYEAR = 1260
TRADING_DAYS_HALF = 126
TRADING_DAYS_QUARTER = 63
TRADING_DAYS_MONTH = 21
TRADING_DAYS_WEEK = 5


def _z(s, w):
    m = s.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = s.rolling(w, min_periods=max(1, w // 2)).std()
    return (s - m) / sd.replace(0, np.nan)


def _mean(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _std(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _rmax(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rmin(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rank(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).rank(pct=True) - 0.5


def _growth(s, w):
    return np.log(s.replace(0, np.nan) / s.shift(w).replace(0, np.nan))


def _rangepos(s, w):
    hi = _rmax(s, w)
    lo = _rmin(s, w)
    return (s - lo) / (hi - lo).replace(0, np.nan)


def _evsales(ev, revenue):
    return ev / revenue.replace(0, np.nan)


def _evebitda(ev, ebitda):
    return ev / ebitda.replace(0, np.nan)


def f43vc_f43_valuation_vs_cycle_evebitdamrgap_21d_slope_v001_signal(evebitda):
    m=_mean(evebitda,252)
    base=(evebitda-m)/m.replace(0,np.nan)
    drv = base
    d = drv.diff(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f43vc_f43_valuation_vs_cycle_pbmrgap_21d_slope_v002_signal(pb):
    m=_mean(pb,252)
    base=(pb-m)/m.replace(0,np.nan)
    drv = base
    d = drv.diff(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f43vc_f43_valuation_vs_cycle_evsalesmrgap_21d_slope_v003_signal(ev, revenue):
    evs=_evsales(ev,revenue)
    m=_mean(evs,252)
    base=(evs-m)/m.replace(0,np.nan)
    drv = base
    d = drv.diff(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f43vc_f43_valuation_vs_cycle_psmrgap_21d_slope_v004_signal(marketcap, revenue):
    ps=marketcap/revenue.replace(0,np.nan)
    m=_mean(ps,252)
    base=(ps-m)/m.replace(0,np.nan)
    drv = base
    d = drv.diff(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f43vc_f43_valuation_vs_cycle_mcapebmrgap_21d_slope_v005_signal(marketcap, ebitda):
    mu=marketcap/ebitda.replace(0,np.nan)
    m=_mean(mu,252)
    base=(mu-m)/m.replace(0,np.nan)
    drv = base
    d = drv.diff(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f43vc_f43_valuation_vs_cycle_evebitdaz_63d_slope_v006_signal(evebitda):
    base=_z(evebitda,504)
    drv = base
    d = drv.diff(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f43vc_f43_valuation_vs_cycle_pbz_21d_slope_v007_signal(pb):
    base=_z(pb,252)
    drv = base
    d = drv.diff(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f43vc_f43_valuation_vs_cycle_evsalesz_21d_slope_v008_signal(ev, revenue):
    base=_z(_evsales(ev,revenue),252)
    drv = base
    d = drv.diff(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f43vc_f43_valuation_vs_cycle_psz_21d_slope_v009_signal(marketcap, revenue):
    base=_z(marketcap/revenue.replace(0,np.nan),252)
    drv = base
    d = drv.diff(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f43vc_f43_valuation_vs_cycle_mcapebz_63d_slope_v010_signal(marketcap, ebitda):
    base=_z(marketcap/ebitda.replace(0,np.nan),504)
    drv = base
    d = drv.diff(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f43vc_f43_valuation_vs_cycle_evebitdapeg_21d_slope_v011_signal(evebitda, ebitda):
    g=_growth(ebitda,252)
    base=np.log(evebitda.replace(0,np.nan))-g.clip(-1,1)
    drv = base
    d = drv.diff(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f43vc_f43_valuation_vs_cycle_evsalespeg_21d_slope_v012_signal(ev, revenue):
    evs=_evsales(ev,revenue)
    g=_growth(revenue,252)
    base=np.log(evs.replace(0,np.nan))-g.clip(-1,1)
    drv = base
    d = drv.diff(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f43vc_f43_valuation_vs_cycle_pbpeg_21d_slope_v013_signal(pb, ebitda):
    g=_growth(ebitda,252)
    base=_rank(pb,252)-_rank(g,252)
    drv = base
    d = drv.diff(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f43vc_f43_valuation_vs_cycle_pspeg_21d_slope_v014_signal(marketcap, revenue):
    ps=marketcap/revenue.replace(0,np.nan)
    g=_growth(revenue,252)
    base=np.log(ps.replace(0,np.nan))-2.0*g.clip(-1,1)
    drv = base
    d = drv.diff(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f43vc_f43_valuation_vs_cycle_evrerate_21d_slope_v015_signal(ev, ebitda):
    base=_growth(ev,252)-_growth(ebitda,252)
    drv = base
    d = drv.diff(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f43vc_f43_valuation_vs_cycle_mcaprerate_21d_slope_v016_signal(marketcap, revenue):
    base=_growth(marketcap,252)-_growth(revenue,252)
    drv = base
    d = drv.diff(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f43vc_f43_valuation_vs_cycle_evebrerate_21d_slope_v017_signal(evebitda, ebitda):
    base=_growth(evebitda,252)-0.5*_growth(ebitda,252)
    drv = base
    d = drv.diff(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f43vc_f43_valuation_vs_cycle_mcapebrr_21d_slope_v018_signal(marketcap, ebitda):
    base=_growth(marketcap,252)-_growth(ebitda,252)
    drv = base
    d = drv.diff(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f43vc_f43_valuation_vs_cycle_growthcatchup_21d_slope_v019_signal(evebitda, revenue):
    base=_growth(revenue,252)-_growth(evebitda,252)
    drv = base
    d = drv.diff(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f43vc_f43_valuation_vs_cycle_evebitdarng_63d_slope_v020_signal(evebitda):
    base=_rangepos(evebitda,1260)-0.5
    drv = base
    d = drv.diff(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f43vc_f43_valuation_vs_cycle_pbrng_63d_slope_v021_signal(pb):
    base=_rangepos(pb,504)-0.5
    drv = base
    d = drv.diff(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f43vc_f43_valuation_vs_cycle_evsalesrng_63d_slope_v022_signal(ev, revenue):
    base=_rangepos(_evsales(ev,revenue),1260)-0.5
    drv = base
    d = drv.diff(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f43vc_f43_valuation_vs_cycle_psrng_63d_slope_v023_signal(marketcap, revenue):
    base=_rangepos(marketcap/revenue.replace(0,np.nan),1260)-0.5
    drv = base
    d = drv.diff(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f43vc_f43_valuation_vs_cycle_tension_21d_slope_v024_signal(evebitda, revenue):
    base=_rangepos(evebitda,252)-_rangepos(revenue,252)
    drv = base
    d = drv.diff(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f43vc_f43_valuation_vs_cycle_pbtension_63d_slope_v025_signal(pb, ebitda):
    base=_rangepos(pb,504)-_rangepos(ebitda,504)
    drv = base
    d = drv.diff(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f43vc_f43_valuation_vs_cycle_phasegap_63d_slope_v026_signal(ev, revenue):
    evs=_evsales(ev,revenue)
    base=_rangepos(revenue,504)-_rangepos(evs,504)
    drv = base
    d = drv.diff(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f43vc_f43_valuation_vs_cycle_midcyclegap_63d_slope_v027_signal(evebitda):
    med=evebitda.rolling(1260,min_periods=504).median()
    base=(evebitda-med)/med.replace(0,np.nan)
    drv = base
    d = drv.diff(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f43vc_f43_valuation_vs_cycle_pbmidcycle_63d_slope_v028_signal(pb):
    med=pb.rolling(1260,min_periods=504).median()
    base=(pb-med)/med.replace(0,np.nan)
    drv = base
    d = drv.diff(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f43vc_f43_valuation_vs_cycle_offtrough_63d_slope_v029_signal(evebitda):
    lo=_rmin(evebitda,1260)
    base=evebitda/lo.replace(0,np.nan)-1.0
    drv = base
    d = drv.diff(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f43vc_f43_valuation_vs_cycle_pbnav_21d_slope_v030_signal(pb, revenue):
    g=_growth(revenue,252)
    base=np.log(pb.replace(0,np.nan))-1.5*g.clip(-1,1)
    drv = base
    d = drv.diff(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f43vc_f43_valuation_vs_cycle_evsofflow_63d_slope_v031_signal(ev, revenue):
    evs=_evsales(ev,revenue)
    lo=_rmin(evs,1260)
    base=np.log(evs.replace(0,np.nan)/lo.replace(0,np.nan))
    drv = base
    d = drv.diff(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f43vc_f43_valuation_vs_cycle_downcycleval_21d_slope_v032_signal(evebitda, ebitda):
    vz=_z(evebitda,252)
    down=(ebitda<_mean(ebitda,252)).astype(float)
    base=vz*(1.0+down)
    drv = base
    d = drv.diff(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f43vc_f43_valuation_vs_cycle_upcycleval_21d_slope_v033_signal(pb, revenue):
    vz=_z(pb,252)
    up=(revenue>_mean(revenue,252)).astype(float)
    base=vz*(1.0+up)
    drv = base
    d = drv.diff(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f43vc_f43_valuation_vs_cycle_valphase_21d_slope_v034_signal(evebitda, revenue):
    vz=_z(evebitda,252)
    phase=_rangepos(revenue,252)-0.5
    base=vz*(1.0+phase)
    drv = base
    d = drv.diff(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f43vc_f43_valuation_vs_cycle_blendedgap_21d_slope_v035_signal(evebitda, pb, ebitda):
    vz=0.5*_z(evebitda,252)+0.5*_z(pb,252)
    gz=_z(_growth(ebitda,252),252)
    base=vz-gz
    drv = base
    d = drv.diff(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f43vc_f43_valuation_vs_cycle_blendmult_21d_slope_v036_signal(evebitda, ev, revenue):
    evs=_evsales(ev,revenue)
    base=0.5*_z(evebitda,252)+0.5*_z(evs,252)
    drv = base
    d = drv.diff(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f43vc_f43_valuation_vs_cycle_cheapgrowcomp_21d_slope_v037_signal(evebitda, ebitda):
    cheap=-_z(evebitda,252)
    grow=_z(_growth(ebitda,252),252)
    base=0.6*cheap+0.4*grow
    drv = base
    d = drv.diff(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f43vc_f43_valuation_vs_cycle_marginrerate_21d_slope_v038_signal(ev, ebitda, revenue):
    eve=_evebitda(ev,ebitda)
    evs=_evsales(ev,revenue)
    sp=np.log(eve.replace(0,np.nan))-np.log(evs.replace(0,np.nan))
    base=sp-_mean(sp,252)
    drv = base
    d = drv.diff(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f43vc_f43_valuation_vs_cycle_multpermargin_21d_slope_v039_signal(evebitda, ebitda, revenue):
    margin=ebitda/revenue.replace(0,np.nan)
    base=_z(evebitda*margin,252)
    drv = base
    d = drv.diff(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f43vc_f43_valuation_vs_cycle_pbmargin_21d_slope_v040_signal(pb, ebitda, revenue):
    margin=ebitda/revenue.replace(0,np.nan)
    base=_z(pb,252)-_z(margin,252)
    drv = base
    d = drv.diff(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f43vc_f43_valuation_vs_cycle_logdetrend_21d_slope_v041_signal(marketcap, revenue):
    ps=marketcap/revenue.replace(0,np.nan)
    lp=np.log(ps.replace(0,np.nan))
    fast=lp.ewm(span=21,min_periods=10).mean()
    slow=lp.ewm(span=252,min_periods=63).mean()
    base=fast-slow
    drv = base
    d = drv.diff(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f43vc_f43_valuation_vs_cycle_pblogdetrend_63d_slope_v042_signal(pb):
    lp=np.log(pb.replace(0,np.nan))
    base=lp-lp.ewm(span=504,min_periods=126).mean()
    drv = base
    d = drv.diff(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f43vc_f43_valuation_vs_cycle_multdiverge_21d_slope_v043_signal(evebitda, pb):
    base=_z(evebitda,252)-_z(pb,252)
    drv = base
    d = drv.diff(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f43vc_f43_valuation_vs_cycle_evbookspr_21d_slope_v044_signal(ev, ebitda, pb):
    eve=_evebitda(ev,ebitda)
    base=_z(eve,252)-_z(pb,252)
    drv = base
    d = drv.diff(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f43vc_f43_valuation_vs_cycle_pegrank_63d_slope_v045_signal(evebitda, ebitda):
    g=_growth(ebitda,252)
    peg=evebitda/(g*100.0).replace(0,np.nan)
    base=_rank(peg,504)
    drv = base
    d = drv.diff(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f43vc_f43_valuation_vs_cycle_deeprank_63d_slope_v046_signal(evebitda):
    base=-_rank(evebitda,1260)
    drv = base
    d = drv.diff(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f43vc_f43_valuation_vs_cycle_blendrank_63d_slope_v047_signal(evebitda, pb, revenue):
    valr=0.5*_rank(evebitda,504)+0.5*_rank(pb,504)
    gr=_rank(_growth(revenue,252),504)
    base=valr-gr
    drv = base
    d = drv.diff(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f43vc_f43_valuation_vs_cycle_deepcheaplate_63d_slope_v048_signal(evebitda, revenue):
    cheap=-_rank(evebitda,504)
    late=_rangepos(revenue,1260)-0.5
    base=cheap+late
    drv = base
    d = drv.diff(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f43vc_f43_valuation_vs_cycle_troughval_63d_slope_v049_signal(evebitda, ebitda):
    cheap=-_z(evebitda,252)
    tp=(1.0-_rangepos(ebitda,1260))
    base=cheap*tp
    drv = base
    d = drv.diff(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f43vc_f43_valuation_vs_cycle_invcycleval_21d_slope_v050_signal(ev, revenue):
    evs=_evsales(ev,revenue)
    gap=(evs-_mean(evs,252))/_mean(evs,252).replace(0,np.nan)
    inv=(1.0-_rangepos(revenue,252))
    base=gap*inv
    drv = base
    d = drv.diff(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f43vc_f43_valuation_vs_cycle_evebfastslow_21d_slope_v051_signal(evebitda):
    base=_mean(evebitda,63)/_mean(evebitda,252).replace(0,np.nan)-1.0
    drv = base
    d = drv.diff(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f43vc_f43_valuation_vs_cycle_pbfastslow_21d_slope_v052_signal(pb):
    base=_mean(pb,63)/_mean(pb,252).replace(0,np.nan)-1.0
    drv = base
    d = drv.diff(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f43vc_f43_valuation_vs_cycle_evsfastslow_21d_slope_v053_signal(ev, revenue):
    evs=_evsales(ev,revenue)
    base=_mean(evs,63)/_mean(evs,252).replace(0,np.nan)-1.0
    drv = base
    d = drv.diff(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f43vc_f43_valuation_vs_cycle_yoyrerate_21d_slope_v054_signal(evebitda, ebitda):
    vg=_rangepos(evebitda,252)
    eg=_rangepos(ebitda,252)
    base=vg-eg
    drv = base
    d = drv.diff(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f43vc_f43_valuation_vs_cycle_yoymult_21d_slope_v055_signal(evebitda):
    base=(evebitda-evebitda.shift(252))/evebitda.shift(252).replace(0,np.nan)
    drv = base
    d = drv.diff(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f43vc_f43_valuation_vs_cycle_scaledgap_21d_slope_v056_signal(evebitda, revenue):
    gap=-(_z(evebitda,252))
    g=(1.0+_growth(revenue,252).clip(lower=-0.5))
    base=gap*g
    drv = base
    d = drv.diff(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f43vc_f43_valuation_vs_cycle_volscaledgap_21d_slope_v057_signal(evebitda):
    gap=evebitda-_mean(evebitda,252)
    vol=_std(evebitda.diff(),63)
    base=gap/vol.replace(0,np.nan)
    drv = base
    d = drv.diff(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f43vc_f43_valuation_vs_cycle_costofgrowth_21d_slope_v058_signal(evebitda, revenue):
    gap=(evebitda-_mean(evebitda,252))/_mean(evebitda,252).replace(0,np.nan)
    g=_growth(revenue,252).abs()+0.05
    base=gap/g
    drv = base
    d = drv.diff(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f43vc_f43_valuation_vs_cycle_dispratio_21d_slope_v059_signal(evebitda, revenue):
    vd=_std(_growth(evebitda,21),252)
    cd=_std(_growth(revenue,21),252)
    base=vd/cd.replace(0,np.nan)
    drv = base
    d = drv.diff(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f43vc_f43_valuation_vs_cycle_pegdisp_21d_slope_v060_signal(ev, revenue):
    evs=_evsales(ev,revenue)
    g=_growth(revenue,252)
    peg=evs/(g*100.0).replace(0,np.nan)
    base=_std(peg,252)
    drv = base
    d = drv.diff(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f43vc_f43_valuation_vs_cycle_elasticity_21d_slope_v061_signal(evebitda, ebitda):
    dm=_growth(evebitda,63)
    dg=_growth(ebitda,63)
    base=_z(dm/(dg.abs()+0.05),252)
    drv = base
    d = drv.diff(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f43vc_f43_valuation_vs_cycle_reratepergrowth_21d_slope_v062_signal(evebitda, revenue):
    dm=_growth(evebitda,252)
    dr=_growth(revenue,252)
    base=_z(dm/(dr.abs()+0.05)*np.sign(dr),252)
    drv = base
    d = drv.diff(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f43vc_f43_valuation_vs_cycle_valstructure_21d_slope_v063_signal(ev, revenue, ebitda):
    evs=_evsales(ev,revenue)
    eve=_evebitda(ev,ebitda)
    margin=ebitda/revenue.replace(0,np.nan)
    base=(eve*margin-evs)/evs.replace(0,np.nan)
    drv = base
    d = drv.diff(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f43vc_f43_valuation_vs_cycle_evsexprate_21d_slope_v064_signal(ev, revenue, ebitda):
    evs=_evsales(ev,revenue)
    margin=ebitda/revenue.replace(0,np.nan)
    base=_z(evs*margin,252)
    drv = base
    d = drv.diff(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f43vc_f43_valuation_vs_cycle_midstretch_63d_slope_v065_signal(evebitda, pb):
    eg=(evebitda-_mean(evebitda,504))/_mean(evebitda,504).replace(0,np.nan)
    pg=(pb-_mean(pb,504))/_mean(pb,504).replace(0,np.nan)
    base=eg-pg
    drv = base
    d = drv.diff(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f43vc_f43_valuation_vs_cycle_derate_21d_slope_v066_signal(evebitda):
    hi=_rmax(evebitda,252)
    base=(hi-evebitda)/hi.replace(0,np.nan)
    drv = base
    d = drv.diff(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f43vc_f43_valuation_vs_cycle_evsexpand_21d_slope_v067_signal(ev, revenue):
    evs=_evsales(ev,revenue)
    lo=_rmin(evs,252)
    base=(evs-lo)/lo.replace(0,np.nan)
    drv = base
    d = drv.diff(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f43vc_f43_valuation_vs_cycle_evscompress_63d_slope_v068_signal(ev, revenue):
    evs=_evsales(ev,revenue)
    hi=_rmax(evs,504)
    base=(hi-evs)/hi.replace(0,np.nan)
    drv = base
    d = drv.diff(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f43vc_f43_valuation_vs_cycle_compositephase_21d_slope_v069_signal(evebitda, revenue, ebitda):
    vz=_z(evebitda,252)
    phase=0.5*_rangepos(revenue,252)+0.5*_rangepos(ebitda,252)
    base=vz-_z(phase,252)
    drv = base
    d = drv.diff(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f43vc_f43_valuation_vs_cycle_valcyclez_21d_slope_v070_signal(evebitda, ebitda):
    vz=_z(evebitda,252)
    cz=_z(_rangepos(ebitda,252),252)
    base=vz-cz
    drv = base
    d = drv.diff(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f43vc_f43_valuation_vs_cycle_fairresid_21d_slope_v071_signal(evebitda, ebitda):
    cp=_rangepos(ebitda,252)
    lo=_rmin(evebitda,252)
    hi=_rmax(evebitda,252)
    fair=lo+(hi-lo)*cp
    base=(evebitda-fair)/fair.replace(0,np.nan)
    drv = base
    d = drv.diff(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f43vc_f43_valuation_vs_cycle_revoutrun_21d_slope_v072_signal(revenue, ev):
    rz=_z(_growth(revenue,126),252)
    ez=_z(_growth(ev,126),252)
    base=rz-ez
    drv = base
    d = drv.diff(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f43vc_f43_valuation_vs_cycle_cheapenrank_63d_slope_v073_signal(revenue, marketcap):
    gap=_growth(revenue,252)-_growth(marketcap,252)
    base=_rank(gap,504)
    drv = base
    d = drv.diff(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f43vc_f43_valuation_vs_cycle_psrankgap_63d_slope_v074_signal(marketcap, revenue):
    ps=marketcap/revenue.replace(0,np.nan)
    base=_rank(ps,504)-_rank(_growth(revenue,252),504)
    drv = base
    d = drv.diff(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f43vc_f43_valuation_vs_cycle_valgrowthcoup_21d_slope_v075_signal(evebitda, ebitda):
    vz=_z(evebitda,252)
    gz=_z(_growth(ebitda,126),252)
    base=(vz*gz).rolling(126,min_periods=63).mean()
    drv = base
    d = drv.diff(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f43vc_f43_valuation_vs_cycle_richextreme_21d_slope_v076_signal(evebitda, ebitda):
    vz=_z(evebitda,252)
    ex=(_rangepos(ebitda,252)-0.5).abs()
    base=vz*ex
    drv = base
    d = drv.diff(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f43vc_f43_valuation_vs_cycle_phaseadjz_21d_slope_v077_signal(evebitda, revenue):
    vz=_z(evebitda,252)
    phase=_rangepos(revenue,504)
    base=vz/(0.5+phase)
    drv = base
    d = drv.diff(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f43vc_f43_valuation_vs_cycle_pbsqrtgap_63d_slope_v078_signal(pb):
    z=_z(pb,504)
    base=np.sign(z)*(z.abs()**0.5)
    drv = base
    d = drv.diff(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f43vc_f43_valuation_vs_cycle_signedgap_21d_slope_v079_signal(evebitda, revenue):
    gap=(evebitda-_mean(evebitda,252))/_std(evebitda,252).replace(0,np.nan)
    g=np.sign(_growth(revenue,126))
    base=np.tanh(gap)*g
    drv = base
    d = drv.diff(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f43vc_f43_valuation_vs_cycle_marginvalgap_21d_slope_v080_signal(ev, revenue, ebitda):
    evs=_evsales(ev,revenue)
    eve=_evebitda(ev,ebitda)
    im=evs/eve.replace(0,np.nan)
    am=ebitda/revenue.replace(0,np.nan)
    base=_z(im-am,252)
    drv = base
    d = drv.diff(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f43vc_f43_valuation_vs_cycle_cheapvsmargin_21d_slope_v081_signal(evebitda, ebitda, revenue):
    cheap=-_z(evebitda,252)
    margin=ebitda/revenue.replace(0,np.nan)
    mp=_z(_rangepos(margin,252),252)
    base=cheap-mp
    drv = base
    d = drv.diff(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f43vc_f43_valuation_vs_cycle_gadjeve_21d_slope_v082_signal(evebitda, revenue):
    g=_growth(revenue,252)
    base=_z(evebitda-10.0*g,252)
    drv = base
    d = drv.diff(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f43vc_f43_valuation_vs_cycle_gadjevsales_63d_slope_v083_signal(ev, revenue):
    mult=_evsales(ev,revenue)
    g=_growth(revenue,252).clip(lower=0.001)
    base=_rank(mult/(1.0+g),504)
    drv = base
    d = drv.diff(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f43vc_f43_valuation_vs_cycle_cheaparea_21d_slope_v084_signal(evebitda):
    z=_z(evebitda,252)
    below=(-z).clip(lower=0)
    base=below.rolling(126,min_periods=63).sum()
    drv = base
    d = drv.diff(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f43vc_f43_valuation_vs_cycle_cheaptime_21d_slope_v085_signal(evebitda):
    below=(evebitda<_mean(evebitda,252)).astype(float)
    base=below.rolling(252,min_periods=126).mean()-0.5
    drv = base
    d = drv.diff(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f43vc_f43_valuation_vs_cycle_mcapebgap_63d_slope_v086_signal(marketcap, ebitda):
    mu=marketcap/ebitda.replace(0,np.nan)
    m=_mean(mu,504)
    base=(mu-m)/m.replace(0,np.nan)
    drv = base
    d = drv.diff(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f43vc_f43_valuation_vs_cycle_mcapebpeg_21d_slope_v087_signal(marketcap, ebitda):
    mu=marketcap/ebitda.replace(0,np.nan)
    g=_growth(ebitda,252)
    base=_z(mu,252)-3.0*g.clip(-1,1)
    drv = base
    d = drv.diff(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f43vc_f43_valuation_vs_cycle_implieddrift_21d_slope_v088_signal(ev, ebitda, evebitda):
    im=_evebitda(ev,ebitda)
    base=(im-evebitda)/evebitda.replace(0,np.nan)
    drv = base
    d = drv.diff(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f43vc_f43_valuation_vs_cycle_peakwarn_21d_slope_v089_signal(evebitda, ebitda):
    base=_z(_growth(evebitda,63)-_growth(ebitda,63),252)
    drv = base
    d = drv.diff(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f43vc_f43_valuation_vs_cycle_evebitdamrgapz_21d_slope_v090_signal(evebitda):
    m=_mean(evebitda,252)
    base=(evebitda-m)/m.replace(0,np.nan)
    drv = base.ewm(span=63, min_periods=21).mean()
    d = drv.diff(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f43vc_f43_valuation_vs_cycle_pbmrgapz_21d_slope_v091_signal(pb):
    m=_mean(pb,252)
    base=(pb-m)/m.replace(0,np.nan)
    drv = base.ewm(span=63, min_periods=21).mean()
    d = drv.diff(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f43vc_f43_valuation_vs_cycle_evsalesmrgapz_21d_slope_v092_signal(ev, revenue):
    evs=_evsales(ev,revenue)
    m=_mean(evs,252)
    base=(evs-m)/m.replace(0,np.nan)
    drv = base.ewm(span=63, min_periods=21).mean()
    d = drv.diff(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f43vc_f43_valuation_vs_cycle_psmrgapz_21d_slope_v093_signal(marketcap, revenue):
    ps=marketcap/revenue.replace(0,np.nan)
    m=_mean(ps,252)
    base=(ps-m)/m.replace(0,np.nan)
    drv = base.ewm(span=63, min_periods=21).mean()
    d = drv.diff(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f43vc_f43_valuation_vs_cycle_mcapebmrgapz_21d_slope_v094_signal(marketcap, ebitda):
    mu=marketcap/ebitda.replace(0,np.nan)
    m=_mean(mu,252)
    base=(mu-m)/m.replace(0,np.nan)
    drv = base.ewm(span=63, min_periods=21).mean()
    d = drv.diff(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f43vc_f43_valuation_vs_cycle_evebitdazz_63d_slope_v095_signal(evebitda):
    base=_z(evebitda,504)
    drv = base.ewm(span=63, min_periods=21).mean()
    d = drv.diff(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f43vc_f43_valuation_vs_cycle_pbzz_21d_slope_v096_signal(pb):
    base=_z(pb,252)
    drv = base.ewm(span=63, min_periods=21).mean()
    d = drv.diff(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f43vc_f43_valuation_vs_cycle_evsaleszz_21d_slope_v097_signal(ev, revenue):
    base=_z(_evsales(ev,revenue),252)
    drv = base.ewm(span=63, min_periods=21).mean()
    d = drv.diff(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f43vc_f43_valuation_vs_cycle_pszz_21d_slope_v098_signal(marketcap, revenue):
    base=_z(marketcap/revenue.replace(0,np.nan),252)
    drv = base.ewm(span=63, min_periods=21).mean()
    d = drv.diff(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f43vc_f43_valuation_vs_cycle_mcapebzz_63d_slope_v099_signal(marketcap, ebitda):
    base=_z(marketcap/ebitda.replace(0,np.nan),504)
    drv = base.ewm(span=63, min_periods=21).mean()
    d = drv.diff(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f43vc_f43_valuation_vs_cycle_evebitdapegz_21d_slope_v100_signal(evebitda, ebitda):
    g=_growth(ebitda,252)
    base=np.log(evebitda.replace(0,np.nan))-g.clip(-1,1)
    drv = base.ewm(span=63, min_periods=21).mean()
    d = drv.diff(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f43vc_f43_valuation_vs_cycle_evsalespegz_21d_slope_v101_signal(ev, revenue):
    evs=_evsales(ev,revenue)
    g=_growth(revenue,252)
    base=np.log(evs.replace(0,np.nan))-g.clip(-1,1)
    drv = base.ewm(span=63, min_periods=21).mean()
    d = drv.diff(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f43vc_f43_valuation_vs_cycle_pbpegz_21d_slope_v102_signal(pb, ebitda):
    g=_growth(ebitda,252)
    base=_rank(pb,252)-_rank(g,252)
    drv = base.ewm(span=63, min_periods=21).mean()
    d = drv.diff(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f43vc_f43_valuation_vs_cycle_pspegz_21d_slope_v103_signal(marketcap, revenue):
    ps=marketcap/revenue.replace(0,np.nan)
    g=_growth(revenue,252)
    base=np.log(ps.replace(0,np.nan))-2.0*g.clip(-1,1)
    drv = base.ewm(span=63, min_periods=21).mean()
    d = drv.diff(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f43vc_f43_valuation_vs_cycle_evreratez_21d_slope_v104_signal(ev, ebitda):
    base=_growth(ev,252)-_growth(ebitda,252)
    drv = base.ewm(span=63, min_periods=21).mean()
    d = drv.diff(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f43vc_f43_valuation_vs_cycle_mcapreratez_21d_slope_v105_signal(marketcap, revenue):
    base=_growth(marketcap,252)-_growth(revenue,252)
    drv = base.ewm(span=63, min_periods=21).mean()
    d = drv.diff(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f43vc_f43_valuation_vs_cycle_evebreratez_21d_slope_v106_signal(evebitda, ebitda):
    base=_growth(evebitda,252)-0.5*_growth(ebitda,252)
    drv = base.ewm(span=63, min_periods=21).mean()
    d = drv.diff(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f43vc_f43_valuation_vs_cycle_mcapebrrz_21d_slope_v107_signal(marketcap, ebitda):
    base=_growth(marketcap,252)-_growth(ebitda,252)
    drv = base.ewm(span=63, min_periods=21).mean()
    d = drv.diff(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f43vc_f43_valuation_vs_cycle_growthcatchupz_21d_slope_v108_signal(evebitda, revenue):
    base=_growth(revenue,252)-_growth(evebitda,252)
    drv = base.ewm(span=63, min_periods=21).mean()
    d = drv.diff(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f43vc_f43_valuation_vs_cycle_evebitdarngz_63d_slope_v109_signal(evebitda):
    base=_rangepos(evebitda,1260)-0.5
    drv = base.ewm(span=63, min_periods=21).mean()
    d = drv.diff(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f43vc_f43_valuation_vs_cycle_pbrngz_63d_slope_v110_signal(pb):
    base=_rangepos(pb,504)-0.5
    drv = base.ewm(span=63, min_periods=21).mean()
    d = drv.diff(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f43vc_f43_valuation_vs_cycle_evsalesrngz_63d_slope_v111_signal(ev, revenue):
    base=_rangepos(_evsales(ev,revenue),1260)-0.5
    drv = base.ewm(span=63, min_periods=21).mean()
    d = drv.diff(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f43vc_f43_valuation_vs_cycle_psrngz_63d_slope_v112_signal(marketcap, revenue):
    base=_rangepos(marketcap/revenue.replace(0,np.nan),1260)-0.5
    drv = base.ewm(span=63, min_periods=21).mean()
    d = drv.diff(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f43vc_f43_valuation_vs_cycle_tensionz_21d_slope_v113_signal(evebitda, revenue):
    base=_rangepos(evebitda,252)-_rangepos(revenue,252)
    drv = base.ewm(span=63, min_periods=21).mean()
    d = drv.diff(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f43vc_f43_valuation_vs_cycle_pbtensionz_63d_slope_v114_signal(pb, ebitda):
    base=_rangepos(pb,504)-_rangepos(ebitda,504)
    drv = base.ewm(span=63, min_periods=21).mean()
    d = drv.diff(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f43vc_f43_valuation_vs_cycle_phasegapz_63d_slope_v115_signal(ev, revenue):
    evs=_evsales(ev,revenue)
    base=_rangepos(revenue,504)-_rangepos(evs,504)
    drv = base.ewm(span=63, min_periods=21).mean()
    d = drv.diff(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f43vc_f43_valuation_vs_cycle_midcyclegapz_63d_slope_v116_signal(evebitda):
    med=evebitda.rolling(1260,min_periods=504).median()
    base=(evebitda-med)/med.replace(0,np.nan)
    drv = base.ewm(span=63, min_periods=21).mean()
    d = drv.diff(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f43vc_f43_valuation_vs_cycle_pbmidcyclez_63d_slope_v117_signal(pb):
    med=pb.rolling(1260,min_periods=504).median()
    base=(pb-med)/med.replace(0,np.nan)
    drv = base.ewm(span=63, min_periods=21).mean()
    d = drv.diff(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f43vc_f43_valuation_vs_cycle_offtroughz_63d_slope_v118_signal(evebitda):
    lo=_rmin(evebitda,1260)
    base=evebitda/lo.replace(0,np.nan)-1.0
    drv = base.ewm(span=63, min_periods=21).mean()
    d = drv.diff(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f43vc_f43_valuation_vs_cycle_pbnavz_21d_slope_v119_signal(pb, revenue):
    g=_growth(revenue,252)
    base=np.log(pb.replace(0,np.nan))-1.5*g.clip(-1,1)
    drv = base.ewm(span=63, min_periods=21).mean()
    d = drv.diff(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f43vc_f43_valuation_vs_cycle_evsofflowz_63d_slope_v120_signal(ev, revenue):
    evs=_evsales(ev,revenue)
    lo=_rmin(evs,1260)
    base=np.log(evs.replace(0,np.nan)/lo.replace(0,np.nan))
    drv = base.ewm(span=63, min_periods=21).mean()
    d = drv.diff(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f43vc_f43_valuation_vs_cycle_downcyclevalz_21d_slope_v121_signal(evebitda, ebitda):
    vz=_z(evebitda,252)
    down=(ebitda<_mean(ebitda,252)).astype(float)
    base=vz*(1.0+down)
    drv = base.ewm(span=63, min_periods=21).mean()
    d = drv.diff(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f43vc_f43_valuation_vs_cycle_upcyclevalz_21d_slope_v122_signal(pb, revenue):
    vz=_z(pb,252)
    up=(revenue>_mean(revenue,252)).astype(float)
    base=vz*(1.0+up)
    drv = base.ewm(span=63, min_periods=21).mean()
    d = drv.diff(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f43vc_f43_valuation_vs_cycle_valphasez_21d_slope_v123_signal(evebitda, revenue):
    vz=_z(evebitda,252)
    phase=_rangepos(revenue,252)-0.5
    base=vz*(1.0+phase)
    drv = base.ewm(span=63, min_periods=21).mean()
    d = drv.diff(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f43vc_f43_valuation_vs_cycle_blendedgapz_21d_slope_v124_signal(evebitda, pb, ebitda):
    vz=0.5*_z(evebitda,252)+0.5*_z(pb,252)
    gz=_z(_growth(ebitda,252),252)
    base=vz-gz
    drv = base.ewm(span=63, min_periods=21).mean()
    d = drv.diff(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f43vc_f43_valuation_vs_cycle_blendmultz_21d_slope_v125_signal(evebitda, ev, revenue):
    evs=_evsales(ev,revenue)
    base=0.5*_z(evebitda,252)+0.5*_z(evs,252)
    drv = base.ewm(span=63, min_periods=21).mean()
    d = drv.diff(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f43vc_f43_valuation_vs_cycle_cheapgrowcompz_21d_slope_v126_signal(evebitda, ebitda):
    cheap=-_z(evebitda,252)
    grow=_z(_growth(ebitda,252),252)
    base=0.6*cheap+0.4*grow
    drv = base.ewm(span=63, min_periods=21).mean()
    d = drv.diff(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f43vc_f43_valuation_vs_cycle_marginreratez_21d_slope_v127_signal(ev, ebitda, revenue):
    eve=_evebitda(ev,ebitda)
    evs=_evsales(ev,revenue)
    sp=np.log(eve.replace(0,np.nan))-np.log(evs.replace(0,np.nan))
    base=sp-_mean(sp,252)
    drv = base.ewm(span=63, min_periods=21).mean()
    d = drv.diff(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f43vc_f43_valuation_vs_cycle_multpermarginz_21d_slope_v128_signal(evebitda, ebitda, revenue):
    margin=ebitda/revenue.replace(0,np.nan)
    base=_z(evebitda*margin,252)
    drv = base.ewm(span=63, min_periods=21).mean()
    d = drv.diff(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f43vc_f43_valuation_vs_cycle_pbmarginz_21d_slope_v129_signal(pb, ebitda, revenue):
    margin=ebitda/revenue.replace(0,np.nan)
    base=_z(pb,252)-_z(margin,252)
    drv = base.ewm(span=63, min_periods=21).mean()
    d = drv.diff(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f43vc_f43_valuation_vs_cycle_logdetrendz_21d_slope_v130_signal(marketcap, revenue):
    ps=marketcap/revenue.replace(0,np.nan)
    lp=np.log(ps.replace(0,np.nan))
    fast=lp.ewm(span=21,min_periods=10).mean()
    slow=lp.ewm(span=252,min_periods=63).mean()
    base=fast-slow
    drv = base.ewm(span=63, min_periods=21).mean()
    d = drv.diff(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f43vc_f43_valuation_vs_cycle_pblogdetrendz_63d_slope_v131_signal(pb):
    lp=np.log(pb.replace(0,np.nan))
    base=lp-lp.ewm(span=504,min_periods=126).mean()
    drv = base.ewm(span=63, min_periods=21).mean()
    d = drv.diff(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f43vc_f43_valuation_vs_cycle_multdivergez_21d_slope_v132_signal(evebitda, pb):
    base=_z(evebitda,252)-_z(pb,252)
    drv = base.ewm(span=63, min_periods=21).mean()
    d = drv.diff(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f43vc_f43_valuation_vs_cycle_evbooksprz_21d_slope_v133_signal(ev, ebitda, pb):
    eve=_evebitda(ev,ebitda)
    base=_z(eve,252)-_z(pb,252)
    drv = base.ewm(span=63, min_periods=21).mean()
    d = drv.diff(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f43vc_f43_valuation_vs_cycle_pegrankz_63d_slope_v134_signal(evebitda, ebitda):
    g=_growth(ebitda,252)
    peg=evebitda/(g*100.0).replace(0,np.nan)
    base=_rank(peg,504)
    drv = base.ewm(span=63, min_periods=21).mean()
    d = drv.diff(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f43vc_f43_valuation_vs_cycle_deeprankz_63d_slope_v135_signal(evebitda):
    base=-_rank(evebitda,1260)
    drv = base.ewm(span=63, min_periods=21).mean()
    d = drv.diff(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f43vc_f43_valuation_vs_cycle_blendrankz_63d_slope_v136_signal(evebitda, pb, revenue):
    valr=0.5*_rank(evebitda,504)+0.5*_rank(pb,504)
    gr=_rank(_growth(revenue,252),504)
    base=valr-gr
    drv = base.ewm(span=63, min_periods=21).mean()
    d = drv.diff(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f43vc_f43_valuation_vs_cycle_deepcheaplatez_63d_slope_v137_signal(evebitda, revenue):
    cheap=-_rank(evebitda,504)
    late=_rangepos(revenue,1260)-0.5
    base=cheap+late
    drv = base.ewm(span=63, min_periods=21).mean()
    d = drv.diff(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f43vc_f43_valuation_vs_cycle_troughvalz_63d_slope_v138_signal(evebitda, ebitda):
    cheap=-_z(evebitda,252)
    tp=(1.0-_rangepos(ebitda,1260))
    base=cheap*tp
    drv = base.ewm(span=63, min_periods=21).mean()
    d = drv.diff(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f43vc_f43_valuation_vs_cycle_invcyclevalz_21d_slope_v139_signal(ev, revenue):
    evs=_evsales(ev,revenue)
    gap=(evs-_mean(evs,252))/_mean(evs,252).replace(0,np.nan)
    inv=(1.0-_rangepos(revenue,252))
    base=gap*inv
    drv = base.ewm(span=63, min_periods=21).mean()
    d = drv.diff(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f43vc_f43_valuation_vs_cycle_evebfastslowz_21d_slope_v140_signal(evebitda):
    base=_mean(evebitda,63)/_mean(evebitda,252).replace(0,np.nan)-1.0
    drv = base.ewm(span=63, min_periods=21).mean()
    d = drv.diff(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f43vc_f43_valuation_vs_cycle_pbfastslowz_21d_slope_v141_signal(pb):
    base=_mean(pb,63)/_mean(pb,252).replace(0,np.nan)-1.0
    drv = base.ewm(span=63, min_periods=21).mean()
    d = drv.diff(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f43vc_f43_valuation_vs_cycle_evsfastslowz_21d_slope_v142_signal(ev, revenue):
    evs=_evsales(ev,revenue)
    base=_mean(evs,63)/_mean(evs,252).replace(0,np.nan)-1.0
    drv = base.ewm(span=63, min_periods=21).mean()
    d = drv.diff(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f43vc_f43_valuation_vs_cycle_yoyreratez_21d_slope_v143_signal(evebitda, ebitda):
    vg=_rangepos(evebitda,252)
    eg=_rangepos(ebitda,252)
    base=vg-eg
    drv = base.ewm(span=63, min_periods=21).mean()
    d = drv.diff(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f43vc_f43_valuation_vs_cycle_yoymultz_21d_slope_v144_signal(evebitda):
    base=(evebitda-evebitda.shift(252))/evebitda.shift(252).replace(0,np.nan)
    drv = base.ewm(span=63, min_periods=21).mean()
    d = drv.diff(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f43vc_f43_valuation_vs_cycle_scaledgapz_21d_slope_v145_signal(evebitda, revenue):
    gap=-(_z(evebitda,252))
    g=(1.0+_growth(revenue,252).clip(lower=-0.5))
    base=gap*g
    drv = base.ewm(span=63, min_periods=21).mean()
    d = drv.diff(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f43vc_f43_valuation_vs_cycle_volscaledgapz_21d_slope_v146_signal(evebitda):
    gap=evebitda-_mean(evebitda,252)
    vol=_std(evebitda.diff(),63)
    base=gap/vol.replace(0,np.nan)
    drv = base.ewm(span=63, min_periods=21).mean()
    d = drv.diff(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f43vc_f43_valuation_vs_cycle_costofgrowthz_21d_slope_v147_signal(evebitda, revenue):
    gap=(evebitda-_mean(evebitda,252))/_mean(evebitda,252).replace(0,np.nan)
    g=_growth(revenue,252).abs()+0.05
    base=gap/g
    drv = base.ewm(span=63, min_periods=21).mean()
    d = drv.diff(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f43vc_f43_valuation_vs_cycle_dispratioz_21d_slope_v148_signal(evebitda, revenue):
    vd=_std(_growth(evebitda,21),252)
    cd=_std(_growth(revenue,21),252)
    base=vd/cd.replace(0,np.nan)
    drv = base.ewm(span=63, min_periods=21).mean()
    d = drv.diff(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f43vc_f43_valuation_vs_cycle_pegdispz_21d_slope_v149_signal(ev, revenue):
    evs=_evsales(ev,revenue)
    g=_growth(revenue,252)
    peg=evs/(g*100.0).replace(0,np.nan)
    base=_std(peg,252)
    drv = base.ewm(span=63, min_periods=21).mean()
    d = drv.diff(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


def f43vc_f43_valuation_vs_cycle_elasticityz_21d_slope_v150_signal(evebitda, ebitda):
    dm=_growth(evebitda,63)
    dg=_growth(ebitda,63)
    base=_z(dm/(dg.abs()+0.05),252)
    drv = base.ewm(span=63, min_periods=21).mean()
    d = drv.diff(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f43vc_f43_valuation_vs_cycle_evebitdamrgap_21d_slope_v001_signal,
    f43vc_f43_valuation_vs_cycle_pbmrgap_21d_slope_v002_signal,
    f43vc_f43_valuation_vs_cycle_evsalesmrgap_21d_slope_v003_signal,
    f43vc_f43_valuation_vs_cycle_psmrgap_21d_slope_v004_signal,
    f43vc_f43_valuation_vs_cycle_mcapebmrgap_21d_slope_v005_signal,
    f43vc_f43_valuation_vs_cycle_evebitdaz_63d_slope_v006_signal,
    f43vc_f43_valuation_vs_cycle_pbz_21d_slope_v007_signal,
    f43vc_f43_valuation_vs_cycle_evsalesz_21d_slope_v008_signal,
    f43vc_f43_valuation_vs_cycle_psz_21d_slope_v009_signal,
    f43vc_f43_valuation_vs_cycle_mcapebz_63d_slope_v010_signal,
    f43vc_f43_valuation_vs_cycle_evebitdapeg_21d_slope_v011_signal,
    f43vc_f43_valuation_vs_cycle_evsalespeg_21d_slope_v012_signal,
    f43vc_f43_valuation_vs_cycle_pbpeg_21d_slope_v013_signal,
    f43vc_f43_valuation_vs_cycle_pspeg_21d_slope_v014_signal,
    f43vc_f43_valuation_vs_cycle_evrerate_21d_slope_v015_signal,
    f43vc_f43_valuation_vs_cycle_mcaprerate_21d_slope_v016_signal,
    f43vc_f43_valuation_vs_cycle_evebrerate_21d_slope_v017_signal,
    f43vc_f43_valuation_vs_cycle_mcapebrr_21d_slope_v018_signal,
    f43vc_f43_valuation_vs_cycle_growthcatchup_21d_slope_v019_signal,
    f43vc_f43_valuation_vs_cycle_evebitdarng_63d_slope_v020_signal,
    f43vc_f43_valuation_vs_cycle_pbrng_63d_slope_v021_signal,
    f43vc_f43_valuation_vs_cycle_evsalesrng_63d_slope_v022_signal,
    f43vc_f43_valuation_vs_cycle_psrng_63d_slope_v023_signal,
    f43vc_f43_valuation_vs_cycle_tension_21d_slope_v024_signal,
    f43vc_f43_valuation_vs_cycle_pbtension_63d_slope_v025_signal,
    f43vc_f43_valuation_vs_cycle_phasegap_63d_slope_v026_signal,
    f43vc_f43_valuation_vs_cycle_midcyclegap_63d_slope_v027_signal,
    f43vc_f43_valuation_vs_cycle_pbmidcycle_63d_slope_v028_signal,
    f43vc_f43_valuation_vs_cycle_offtrough_63d_slope_v029_signal,
    f43vc_f43_valuation_vs_cycle_pbnav_21d_slope_v030_signal,
    f43vc_f43_valuation_vs_cycle_evsofflow_63d_slope_v031_signal,
    f43vc_f43_valuation_vs_cycle_downcycleval_21d_slope_v032_signal,
    f43vc_f43_valuation_vs_cycle_upcycleval_21d_slope_v033_signal,
    f43vc_f43_valuation_vs_cycle_valphase_21d_slope_v034_signal,
    f43vc_f43_valuation_vs_cycle_blendedgap_21d_slope_v035_signal,
    f43vc_f43_valuation_vs_cycle_blendmult_21d_slope_v036_signal,
    f43vc_f43_valuation_vs_cycle_cheapgrowcomp_21d_slope_v037_signal,
    f43vc_f43_valuation_vs_cycle_marginrerate_21d_slope_v038_signal,
    f43vc_f43_valuation_vs_cycle_multpermargin_21d_slope_v039_signal,
    f43vc_f43_valuation_vs_cycle_pbmargin_21d_slope_v040_signal,
    f43vc_f43_valuation_vs_cycle_logdetrend_21d_slope_v041_signal,
    f43vc_f43_valuation_vs_cycle_pblogdetrend_63d_slope_v042_signal,
    f43vc_f43_valuation_vs_cycle_multdiverge_21d_slope_v043_signal,
    f43vc_f43_valuation_vs_cycle_evbookspr_21d_slope_v044_signal,
    f43vc_f43_valuation_vs_cycle_pegrank_63d_slope_v045_signal,
    f43vc_f43_valuation_vs_cycle_deeprank_63d_slope_v046_signal,
    f43vc_f43_valuation_vs_cycle_blendrank_63d_slope_v047_signal,
    f43vc_f43_valuation_vs_cycle_deepcheaplate_63d_slope_v048_signal,
    f43vc_f43_valuation_vs_cycle_troughval_63d_slope_v049_signal,
    f43vc_f43_valuation_vs_cycle_invcycleval_21d_slope_v050_signal,
    f43vc_f43_valuation_vs_cycle_evebfastslow_21d_slope_v051_signal,
    f43vc_f43_valuation_vs_cycle_pbfastslow_21d_slope_v052_signal,
    f43vc_f43_valuation_vs_cycle_evsfastslow_21d_slope_v053_signal,
    f43vc_f43_valuation_vs_cycle_yoyrerate_21d_slope_v054_signal,
    f43vc_f43_valuation_vs_cycle_yoymult_21d_slope_v055_signal,
    f43vc_f43_valuation_vs_cycle_scaledgap_21d_slope_v056_signal,
    f43vc_f43_valuation_vs_cycle_volscaledgap_21d_slope_v057_signal,
    f43vc_f43_valuation_vs_cycle_costofgrowth_21d_slope_v058_signal,
    f43vc_f43_valuation_vs_cycle_dispratio_21d_slope_v059_signal,
    f43vc_f43_valuation_vs_cycle_pegdisp_21d_slope_v060_signal,
    f43vc_f43_valuation_vs_cycle_elasticity_21d_slope_v061_signal,
    f43vc_f43_valuation_vs_cycle_reratepergrowth_21d_slope_v062_signal,
    f43vc_f43_valuation_vs_cycle_valstructure_21d_slope_v063_signal,
    f43vc_f43_valuation_vs_cycle_evsexprate_21d_slope_v064_signal,
    f43vc_f43_valuation_vs_cycle_midstretch_63d_slope_v065_signal,
    f43vc_f43_valuation_vs_cycle_derate_21d_slope_v066_signal,
    f43vc_f43_valuation_vs_cycle_evsexpand_21d_slope_v067_signal,
    f43vc_f43_valuation_vs_cycle_evscompress_63d_slope_v068_signal,
    f43vc_f43_valuation_vs_cycle_compositephase_21d_slope_v069_signal,
    f43vc_f43_valuation_vs_cycle_valcyclez_21d_slope_v070_signal,
    f43vc_f43_valuation_vs_cycle_fairresid_21d_slope_v071_signal,
    f43vc_f43_valuation_vs_cycle_revoutrun_21d_slope_v072_signal,
    f43vc_f43_valuation_vs_cycle_cheapenrank_63d_slope_v073_signal,
    f43vc_f43_valuation_vs_cycle_psrankgap_63d_slope_v074_signal,
    f43vc_f43_valuation_vs_cycle_valgrowthcoup_21d_slope_v075_signal,
    f43vc_f43_valuation_vs_cycle_richextreme_21d_slope_v076_signal,
    f43vc_f43_valuation_vs_cycle_phaseadjz_21d_slope_v077_signal,
    f43vc_f43_valuation_vs_cycle_pbsqrtgap_63d_slope_v078_signal,
    f43vc_f43_valuation_vs_cycle_signedgap_21d_slope_v079_signal,
    f43vc_f43_valuation_vs_cycle_marginvalgap_21d_slope_v080_signal,
    f43vc_f43_valuation_vs_cycle_cheapvsmargin_21d_slope_v081_signal,
    f43vc_f43_valuation_vs_cycle_gadjeve_21d_slope_v082_signal,
    f43vc_f43_valuation_vs_cycle_gadjevsales_63d_slope_v083_signal,
    f43vc_f43_valuation_vs_cycle_cheaparea_21d_slope_v084_signal,
    f43vc_f43_valuation_vs_cycle_cheaptime_21d_slope_v085_signal,
    f43vc_f43_valuation_vs_cycle_mcapebgap_63d_slope_v086_signal,
    f43vc_f43_valuation_vs_cycle_mcapebpeg_21d_slope_v087_signal,
    f43vc_f43_valuation_vs_cycle_implieddrift_21d_slope_v088_signal,
    f43vc_f43_valuation_vs_cycle_peakwarn_21d_slope_v089_signal,
    f43vc_f43_valuation_vs_cycle_evebitdamrgapz_21d_slope_v090_signal,
    f43vc_f43_valuation_vs_cycle_pbmrgapz_21d_slope_v091_signal,
    f43vc_f43_valuation_vs_cycle_evsalesmrgapz_21d_slope_v092_signal,
    f43vc_f43_valuation_vs_cycle_psmrgapz_21d_slope_v093_signal,
    f43vc_f43_valuation_vs_cycle_mcapebmrgapz_21d_slope_v094_signal,
    f43vc_f43_valuation_vs_cycle_evebitdazz_63d_slope_v095_signal,
    f43vc_f43_valuation_vs_cycle_pbzz_21d_slope_v096_signal,
    f43vc_f43_valuation_vs_cycle_evsaleszz_21d_slope_v097_signal,
    f43vc_f43_valuation_vs_cycle_pszz_21d_slope_v098_signal,
    f43vc_f43_valuation_vs_cycle_mcapebzz_63d_slope_v099_signal,
    f43vc_f43_valuation_vs_cycle_evebitdapegz_21d_slope_v100_signal,
    f43vc_f43_valuation_vs_cycle_evsalespegz_21d_slope_v101_signal,
    f43vc_f43_valuation_vs_cycle_pbpegz_21d_slope_v102_signal,
    f43vc_f43_valuation_vs_cycle_pspegz_21d_slope_v103_signal,
    f43vc_f43_valuation_vs_cycle_evreratez_21d_slope_v104_signal,
    f43vc_f43_valuation_vs_cycle_mcapreratez_21d_slope_v105_signal,
    f43vc_f43_valuation_vs_cycle_evebreratez_21d_slope_v106_signal,
    f43vc_f43_valuation_vs_cycle_mcapebrrz_21d_slope_v107_signal,
    f43vc_f43_valuation_vs_cycle_growthcatchupz_21d_slope_v108_signal,
    f43vc_f43_valuation_vs_cycle_evebitdarngz_63d_slope_v109_signal,
    f43vc_f43_valuation_vs_cycle_pbrngz_63d_slope_v110_signal,
    f43vc_f43_valuation_vs_cycle_evsalesrngz_63d_slope_v111_signal,
    f43vc_f43_valuation_vs_cycle_psrngz_63d_slope_v112_signal,
    f43vc_f43_valuation_vs_cycle_tensionz_21d_slope_v113_signal,
    f43vc_f43_valuation_vs_cycle_pbtensionz_63d_slope_v114_signal,
    f43vc_f43_valuation_vs_cycle_phasegapz_63d_slope_v115_signal,
    f43vc_f43_valuation_vs_cycle_midcyclegapz_63d_slope_v116_signal,
    f43vc_f43_valuation_vs_cycle_pbmidcyclez_63d_slope_v117_signal,
    f43vc_f43_valuation_vs_cycle_offtroughz_63d_slope_v118_signal,
    f43vc_f43_valuation_vs_cycle_pbnavz_21d_slope_v119_signal,
    f43vc_f43_valuation_vs_cycle_evsofflowz_63d_slope_v120_signal,
    f43vc_f43_valuation_vs_cycle_downcyclevalz_21d_slope_v121_signal,
    f43vc_f43_valuation_vs_cycle_upcyclevalz_21d_slope_v122_signal,
    f43vc_f43_valuation_vs_cycle_valphasez_21d_slope_v123_signal,
    f43vc_f43_valuation_vs_cycle_blendedgapz_21d_slope_v124_signal,
    f43vc_f43_valuation_vs_cycle_blendmultz_21d_slope_v125_signal,
    f43vc_f43_valuation_vs_cycle_cheapgrowcompz_21d_slope_v126_signal,
    f43vc_f43_valuation_vs_cycle_marginreratez_21d_slope_v127_signal,
    f43vc_f43_valuation_vs_cycle_multpermarginz_21d_slope_v128_signal,
    f43vc_f43_valuation_vs_cycle_pbmarginz_21d_slope_v129_signal,
    f43vc_f43_valuation_vs_cycle_logdetrendz_21d_slope_v130_signal,
    f43vc_f43_valuation_vs_cycle_pblogdetrendz_63d_slope_v131_signal,
    f43vc_f43_valuation_vs_cycle_multdivergez_21d_slope_v132_signal,
    f43vc_f43_valuation_vs_cycle_evbooksprz_21d_slope_v133_signal,
    f43vc_f43_valuation_vs_cycle_pegrankz_63d_slope_v134_signal,
    f43vc_f43_valuation_vs_cycle_deeprankz_63d_slope_v135_signal,
    f43vc_f43_valuation_vs_cycle_blendrankz_63d_slope_v136_signal,
    f43vc_f43_valuation_vs_cycle_deepcheaplatez_63d_slope_v137_signal,
    f43vc_f43_valuation_vs_cycle_troughvalz_63d_slope_v138_signal,
    f43vc_f43_valuation_vs_cycle_invcyclevalz_21d_slope_v139_signal,
    f43vc_f43_valuation_vs_cycle_evebfastslowz_21d_slope_v140_signal,
    f43vc_f43_valuation_vs_cycle_pbfastslowz_21d_slope_v141_signal,
    f43vc_f43_valuation_vs_cycle_evsfastslowz_21d_slope_v142_signal,
    f43vc_f43_valuation_vs_cycle_yoyreratez_21d_slope_v143_signal,
    f43vc_f43_valuation_vs_cycle_yoymultz_21d_slope_v144_signal,
    f43vc_f43_valuation_vs_cycle_scaledgapz_21d_slope_v145_signal,
    f43vc_f43_valuation_vs_cycle_volscaledgapz_21d_slope_v146_signal,
    f43vc_f43_valuation_vs_cycle_costofgrowthz_21d_slope_v147_signal,
    f43vc_f43_valuation_vs_cycle_dispratioz_21d_slope_v148_signal,
    f43vc_f43_valuation_vs_cycle_pegdispz_21d_slope_v149_signal,
    f43vc_f43_valuation_vs_cycle_elasticityz_21d_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F43_VALUATION_VS_CYCLE_REGISTRY_SLOPE_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500

    def _fund(seed, base=1e8, drift=0.0, vol=0.08, allow_neg=False):
        g = np.random.default_rng(seed)
        steps = np.repeat(g.normal(drift, vol, n // 63 + 1), 63)[:n]
        s = base * np.exp(np.cumsum(steps / 63))
        if allow_neg:
            s = s - base * 0.5
        return pd.Series(s, name=None)

    evebitda = _fund(1, base=8.0, drift=0.02, vol=0.05).rename("evebitda")
    pb = _fund(2, base=1.5, drift=0.015, vol=0.05).rename("pb")
    ev = _fund(3, base=5e8, drift=0.03, vol=0.07).rename("ev")
    marketcap = _fund(4, base=4e8, drift=0.03, vol=0.07).rename("marketcap")
    revenue = _fund(5, base=2e8, drift=0.025, vol=0.06).rename("revenue")
    ebitda = _fund(6, base=6e7, drift=0.025, vol=0.08).rename("ebitda")

    cols = {"evebitda": evebitda, "pb": pb, "ev": ev,
            "marketcap": marketcap, "revenue": revenue, "ebitda": ebitda}

    n_features = 0
    nan_ok = 0
    results = {}
    for name, meta in REGISTRY.items():
        fn = meta["func"]
        args = [cols[c] for c in meta["inputs"]]
        y1 = fn(*args)
        y2 = fn(*args)
        pd.testing.assert_series_equal(y1, y2)
        q = y1.iloc[504:].dropna()
        assert len(q) > 0, name
        assert q.nunique() > 20, "%s nunique=%d" % (name, q.nunique())
        assert q.std() > 0, name
        assert not q.isna().all(), name
        nan_ratio = y1.iloc[504:].isna().mean()
        if nan_ratio < 0.5:
            nan_ok += 1
        results[name] = y1.iloc[504:]
        n_features += 1

    assert n_features == 150, n_features
    assert nan_ok >= int(0.8 * n_features), "nan_ok=%d/%d" % (nan_ok, n_features)

    items = list(results.items())
    for i in range(len(items)):
        ni, si = items[i]
        ai = si.dropna()
        for j in range(i + 1, len(items)):
            nj, sj = items[j]
            aj = sj.dropna()
            idx = ai.index.intersection(aj.index)
            if len(idx) < 30:
                continue
            c = ai.loc[idx].corr(aj.loc[idx])
            if c is None or np.isnan(c):
                continue
            assert abs(c) <= 0.97, "CORR %s vs %s = %.4f" % (ni, nj, c)

    print("OK f43_valuation_vs_cycle_2nd_derivatives_001_150_claude: %d features pass" % n_features)
