import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
TRADING_DAYS_TWOYEAR = 504
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


def _rank(s, w):
    return s.rolling(w, min_periods=max(2, w // 2)).rank(pct=True) - 0.5


def _f51_share(num, den):
    return num / den.replace(0, np.nan)


def _f51_skew(put, cll):
    return put / (put + cll).replace(0, np.nan)


def _f51_growth(s, w):
    return np.log(s.replace(0, np.nan) / s.shift(w).replace(0, np.nan))


def _f51_logratio(a, b):
    return np.log(a.replace(0, np.nan) / b.replace(0, np.nan))


def _f51_herf(a, b, c):
    tot = (a + b + c).replace(0, np.nan)
    sa = a / tot
    sb = b / tot
    sc = c / tot
    return sa * sa + sb * sb + sc * sc



def f51om_f51_ownership_mix_concentration_fndsharea_252d_jerk_v001_signal(fndvalue, totalvalue):
    base = _f51_share(fndvalue, totalvalue)
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f51om_f51_ownership_mix_concentration_fndshareza_252d_jerk_v002_signal(fndvalue, totalvalue):
    s = _f51_share(fndvalue, totalvalue)
    base = _z(s, 252)
    d1 = base - base.shift(84)
    d2 = d1 - d1.shift(84)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f51om_f51_ownership_mix_concentration_fndshareranka_504d_jerk_v003_signal(fndvalue, totalvalue):
    s = _f51_share(fndvalue, totalvalue)
    base = _rank(s, 504)
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f51om_f51_ownership_mix_concentration_undsharea_252d_jerk_v004_signal(undvalue, totalvalue):
    base = _f51_share(undvalue, totalvalue)
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f51om_f51_ownership_mix_concentration_undshareranka_504d_jerk_v005_signal(undvalue, totalvalue):
    s = _f51_share(undvalue, totalvalue)
    base = _rank(s, 504)
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f51om_f51_ownership_mix_concentration_prfsharea_252d_jerk_v006_signal(fndvalue, undvalue, totalvalue):
    prf = (totalvalue - fndvalue - undvalue).clip(lower=0)
    base = prf / totalvalue.replace(0, np.nan)
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f51om_f51_ownership_mix_concentration_fndundlogra_252d_jerk_v007_signal(fndvalue, undvalue, totalvalue):
    prf = (totalvalue - fndvalue - undvalue).clip(lower=0)
    base = _f51_logratio(prf, undvalue) - _f51_logratio(fndvalue, totalvalue)
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f51om_f51_ownership_mix_concentration_fndundlogrza_126d_jerk_v008_signal(fndvalue, undvalue):
    r = _f51_logratio(fndvalue, undvalue)
    base = _z(r, 126)
    d1 = base - base.shift(42)
    d2 = d1 - d1.shift(42)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f51om_f51_ownership_mix_concentration_netsharea_252d_jerk_v009_signal(fndvalue, undvalue, totalvalue):
    base = (fndvalue - undvalue) / totalvalue.replace(0, np.nan)
    d1 = base - base.shift(84)
    d2 = d1 - d1.shift(84)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f51om_f51_ownership_mix_concentration_nonfundimba_252d_jerk_v010_signal(fndvalue, undvalue, totalvalue):
    prf = (totalvalue - fndvalue - undvalue).clip(lower=0)
    base = (undvalue - prf).abs() / (undvalue + prf).replace(0, np.nan)
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f51om_f51_ownership_mix_concentration_nonfundimbza_252d_jerk_v011_signal(fndvalue, undvalue, totalvalue):
    prf = (totalvalue - fndvalue - undvalue).clip(lower=0)
    imb = (undvalue - prf).abs() / (undvalue + prf).replace(0, np.nan)
    base = _z(imb, 252)
    d1 = base - base.shift(84)
    d2 = d1 - d1.shift(84)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f51om_f51_ownership_mix_concentration_herfvalimba_252d_jerk_v012_signal(fndvalue, undvalue, totalvalue):
    prf = (totalvalue - fndvalue - undvalue).clip(lower=0)
    base = (fndvalue - prf).abs() / (fndvalue + prf).replace(0, np.nan)
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f51om_f51_ownership_mix_concentration_herfcntza_252d_jerk_v013_signal(fndholders, undholders, prfholders):
    h = _f51_herf(fndholders, undholders, prfholders)
    base = _z(h, 252)
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f51om_f51_ownership_mix_concentration_nfbreadthimba_252d_jerk_v014_signal(undholders, prfholders):
    base = (undholders - prfholders).abs() / (undholders + prfholders).replace(0, np.nan)
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f51om_f51_ownership_mix_concentration_prfcntsharea_252d_jerk_v015_signal(fndholders, undholders, prfholders):
    tot = (fndholders + undholders + prfholders).replace(0, np.nan)
    base = prfholders / tot
    d1 = base - base.shift(84)
    d2 = d1 - d1.shift(84)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f51om_f51_ownership_mix_concentration_avgholdvala_252d_jerk_v016_signal(totalvalue, fndholders, undholders, prfholders):
    tot = (fndholders + undholders + prfholders).replace(0, np.nan)
    base = totalvalue / tot
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f51om_f51_ownership_mix_concentration_fndcntgrowa_63d_jerk_v017_signal(fndholders):
    base = _f51_growth(fndholders, 63)
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f51om_f51_ownership_mix_concentration_fndundcntlogra_252d_jerk_v018_signal(fndholders, undholders):
    base = _f51_logratio(fndholders, undholders)
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f51om_f51_ownership_mix_concentration_prfvalticketgapa_252d_jerk_v019_signal(prfvalue, prfholders, undvalue, undholders):
    tp = prfvalue / prfholders.replace(0, np.nan)
    tu = undvalue / undholders.replace(0, np.nan)
    base = _f51_logratio(tp, tu)
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f51om_f51_ownership_mix_concentration_fndticketa_252d_jerk_v020_signal(fndvalue, fndholders):
    base = fndvalue / fndholders.replace(0, np.nan)
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f51om_f51_ownership_mix_concentration_fndticketza_252d_jerk_v021_signal(fndvalue, fndholders):
    t = fndvalue / fndholders.replace(0, np.nan)
    base = _z(t, 252)
    d1 = base - base.shift(84)
    d2 = d1 - d1.shift(84)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f51om_f51_ownership_mix_concentration_ticketspreada_252d_jerk_v022_signal(fndvalue, fndholders, undvalue, undholders):
    tf = fndvalue / fndholders.replace(0, np.nan)
    tu = undvalue / undholders.replace(0, np.nan)
    base = _f51_logratio(tf, tu)
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f51om_f51_ownership_mix_concentration_undticketa_252d_jerk_v023_signal(undvalue, undholders):
    base = undvalue / undholders.replace(0, np.nan)
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f51om_f51_ownership_mix_concentration_prfticketa_252d_jerk_v024_signal(prfvalue, prfholders):
    base = prfvalue / prfholders.replace(0, np.nan)
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f51om_f51_ownership_mix_concentration_putskewa_252d_jerk_v025_signal(putvalue, cllvalue):
    base = _f51_skew(putvalue, cllvalue)
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f51om_f51_ownership_mix_concentration_putskewza_252d_jerk_v026_signal(putvalue, cllvalue):
    s = _f51_skew(putvalue, cllvalue)
    base = _z(s, 252)
    d1 = base - base.shift(84)
    d2 = d1 - d1.shift(84)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f51om_f51_ownership_mix_concentration_putskewranka_504d_jerk_v027_signal(putvalue, cllvalue):
    s = _f51_skew(putvalue, cllvalue)
    base = _rank(s, 504)
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f51om_f51_ownership_mix_concentration_putcntskewa_252d_jerk_v028_signal(putholders, cllholders):
    base = _f51_skew(putholders, cllholders)
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f51om_f51_ownership_mix_concentration_putcntskewza_252d_jerk_v029_signal(putholders, cllholders):
    s = _f51_skew(putholders, cllholders)
    base = _z(s, 252)
    d1 = base - base.shift(84)
    d2 = d1 - d1.shift(84)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f51om_f51_ownership_mix_concentration_optbreadtha_252d_jerk_v030_signal(putholders, cllholders, shrholders):
    base = (putholders + cllholders) / shrholders.replace(0, np.nan)
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f51om_f51_ownership_mix_concentration_callbreadtha_252d_jerk_v031_signal(cllholders, shrholders):
    base = cllholders / shrholders.replace(0, np.nan)
    d1 = base - base.shift(84)
    d2 = d1 - d1.shift(84)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f51om_f51_ownership_mix_concentration_putbreadtha_252d_jerk_v032_signal(putholders, shrholders):
    base = putholders / shrholders.replace(0, np.nan)
    d1 = base - base.shift(84)
    d2 = d1 - d1.shift(84)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f51om_f51_ownership_mix_concentration_callbreadthza_252d_jerk_v033_signal(cllholders, shrholders):
    r = cllholders / shrholders.replace(0, np.nan)
    base = _z(r, 252)
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f51om_f51_ownership_mix_concentration_optfoota_252d_jerk_v034_signal(cllvalue, putvalue, totalvalue):
    base = (cllvalue + putvalue) / totalvalue.replace(0, np.nan)
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f51om_f51_ownership_mix_concentration_optfootza_252d_jerk_v035_signal(cllvalue, putvalue, totalvalue):
    r = (cllvalue + putvalue) / totalvalue.replace(0, np.nan)
    base = _z(r, 252)
    d1 = base - base.shift(84)
    d2 = d1 - d1.shift(84)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f51om_f51_ownership_mix_concentration_optnetsharea_252d_jerk_v036_signal(cllvalue, putvalue, totalvalue):
    base = (cllvalue - putvalue) / totalvalue.replace(0, np.nan)
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f51om_f51_ownership_mix_concentration_putvalsharea_252d_jerk_v037_signal(putvalue, undvalue):
    base = putvalue / (putvalue + undvalue).replace(0, np.nan)
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f51om_f51_ownership_mix_concentration_cllvalsharea_252d_jerk_v038_signal(cllvalue, totalvalue):
    base = _f51_share(cllvalue, totalvalue)
    d1 = base - base.shift(84)
    d2 = d1 - d1.shift(84)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f51om_f51_ownership_mix_concentration_optvsfnda_252d_jerk_v039_signal(cllvalue, putvalue, undvalue):
    base = _f51_logratio(cllvalue + putvalue, undvalue)
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f51om_f51_ownership_mix_concentration_cllvsfnda_252d_jerk_v040_signal(cllvalue, fndvalue):
    base = _f51_logratio(cllvalue, fndvalue)
    d1 = base - base.shift(84)
    d2 = d1 - d1.shift(84)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f51om_f51_ownership_mix_concentration_putvsfnda_252d_jerk_v041_signal(putvalue, fndvalue):
    base = _f51_logratio(putvalue, fndvalue)
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f51om_f51_ownership_mix_concentration_pota_252d_jerk_v042_signal(percentoftotal):
    base = percentoftotal
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f51om_f51_ownership_mix_concentration_potza_252d_jerk_v043_signal(percentoftotal):
    base = _z(percentoftotal, 252)
    d1 = base - base.shift(84)
    d2 = d1 - d1.shift(84)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f51om_f51_ownership_mix_concentration_potranka_504d_jerk_v044_signal(percentoftotal):
    base = _rank(percentoftotal, 504)
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f51om_f51_ownership_mix_concentration_callputticketa_252d_jerk_v045_signal(cllvalue, cllholders, putvalue, putholders):
    tc = cllvalue / cllholders.replace(0, np.nan)
    tp = putvalue / putholders.replace(0, np.nan)
    base = _f51_logratio(tc, tp)
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f51om_f51_ownership_mix_concentration_putticketa_252d_jerk_v046_signal(putvalue, putholders):
    base = putvalue / putholders.replace(0, np.nan)
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f51om_f51_ownership_mix_concentration_cllticketa_252d_jerk_v047_signal(cllvalue, cllholders):
    base = cllvalue / cllholders.replace(0, np.nan)
    d1 = base - base.shift(84)
    d2 = d1 - d1.shift(84)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f51om_f51_ownership_mix_concentration_mixqa_252d_jerk_v048_signal(fndvalue, totalvalue, putvalue, cllvalue):
    fs = _f51_share(fndvalue, totalvalue)
    foot = (putvalue + cllvalue) / totalvalue.replace(0, np.nan)
    base = fs - foot
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f51om_f51_ownership_mix_concentration_fndvcgapa_252d_jerk_v049_signal(fndvalue, totalvalue, fndholders, undholders, prfholders):
    vs = _f51_share(fndvalue, totalvalue)
    cs = fndholders / (fndholders + undholders + prfholders).replace(0, np.nan)
    base = vs - cs
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f51om_f51_ownership_mix_concentration_undvcgapa_252d_jerk_v050_signal(undvalue, totalvalue, fndholders, undholders, prfholders):
    vs = _f51_share(undvalue, totalvalue)
    cs = undholders / (fndholders + undholders + prfholders).replace(0, np.nan)
    base = vs - cs
    d1 = base - base.shift(84)
    d2 = d1 - d1.shift(84)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f51om_f51_ownership_mix_concentration_potfnda_252d_jerk_v051_signal(percentoftotal, fndvalue, totalvalue):
    s = _f51_share(fndvalue, totalvalue)
    base = percentoftotal * s
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f51om_f51_ownership_mix_concentration_potputa_252d_jerk_v052_signal(percentoftotal, putvalue, cllvalue):
    ps = _f51_skew(putvalue, cllvalue)
    base = percentoftotal * (ps - 0.5)
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f51om_f51_ownership_mix_concentration_shrfndgrowa_63d_jerk_v053_signal(shrholders, fndholders):
    base = _f51_growth(shrholders, 63) - _f51_growth(fndholders, 63)
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f51om_f51_ownership_mix_concentration_putvalgrowa_63d_jerk_v054_signal(putvalue, totalvalue):
    base = _f51_growth(putvalue, 63) - _f51_growth(totalvalue, 63)
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f51om_f51_ownership_mix_concentration_cllvalgrowa_63d_jerk_v055_signal(cllvalue, totalvalue):
    base = _f51_growth(cllvalue, 63) - _f51_growth(totalvalue, 63)
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f51om_f51_ownership_mix_concentration_optcntneta_63d_jerk_v056_signal(cllholders, putholders):
    base = _f51_growth(cllholders, 63) - _f51_growth(putholders, 63)
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f51om_f51_ownership_mix_concentration_undcntgrowa_63d_jerk_v057_signal(undholders):
    base = _f51_growth(undholders, 63)
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f51om_f51_ownership_mix_concentration_prfcntgrowa_63d_jerk_v058_signal(prfholders):
    base = _f51_growth(prfholders, 63)
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f51om_f51_ownership_mix_concentration_shrcntgrowa_63d_jerk_v059_signal(shrholders):
    base = _f51_growth(shrholders, 63)
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f51om_f51_ownership_mix_concentration_totvalgrowa_63d_jerk_v060_signal(totalvalue):
    base = _f51_growth(totalvalue, 63)
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f51om_f51_ownership_mix_concentration_fndvalgrowa_63d_jerk_v061_signal(fndvalue):
    base = _f51_growth(fndvalue, 63)
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f51om_f51_ownership_mix_concentration_undvalgrowa_63d_jerk_v062_signal(undvalue):
    base = _f51_growth(undvalue, 63)
    d1 = base - base.shift(21)
    d2 = d1 - d1.shift(21)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f51om_f51_ownership_mix_concentration_fndcntxvalsharea_252d_jerk_v063_signal(fndholders, undholders, prfholders, fndvalue, totalvalue):
    fc = fndholders / (fndholders + undholders + prfholders).replace(0, np.nan)
    vs = _f51_share(fndvalue, totalvalue)
    base = fc * vs
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f51om_f51_ownership_mix_concentration_stressa_252d_jerk_v064_signal(putvalue, cllvalue, totalvalue, undvalue):
    ps = _f51_skew(putvalue, cllvalue)
    foot = (putvalue + cllvalue) / totalvalue.replace(0, np.nan)
    us = _f51_share(undvalue, totalvalue)
    base = (ps - 0.5) * foot + 0.5 * us
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f51om_f51_ownership_mix_concentration_potcallqa_252d_jerk_v065_signal(percentoftotal, putholders, cllholders):
    ps = _f51_skew(putholders, cllholders)
    base = percentoftotal * (1.0 - ps)
    d1 = base - base.shift(84)
    d2 = d1 - d1.shift(84)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f51om_f51_ownership_mix_concentration_undprfvallogra_252d_jerk_v066_signal(fndvalue, undvalue, totalvalue):
    prf = (totalvalue - fndvalue - undvalue).clip(lower=0)
    base = _f51_logratio(undvalue, prf)
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f51om_f51_ownership_mix_concentration_undcntshareza_252d_jerk_v067_signal(fndholders, undholders, prfholders):
    tot = (fndholders + undholders + prfholders).replace(0, np.nan)
    s = undholders / tot
    base = _z(s, 252)
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f51om_f51_ownership_mix_concentration_optcntbreadthlogra_252d_jerk_v068_signal(cllholders, putholders, undholders):
    base = _f51_logratio(cllholders + putholders, undholders)
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f51om_f51_ownership_mix_concentration_optnetshareza_252d_jerk_v069_signal(cllvalue, putvalue, totalvalue):
    r = (cllvalue - putvalue) / totalvalue.replace(0, np.nan)
    base = _z(r, 252)
    d1 = base - base.shift(84)
    d2 = d1 - d1.shift(84)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f51om_f51_ownership_mix_concentration_putvalshareza_252d_jerk_v070_signal(putvalue, totalvalue):
    s = _f51_share(putvalue, totalvalue)
    base = _z(s, 252)
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f51om_f51_ownership_mix_concentration_undshareza_252d_jerk_v071_signal(undvalue, totalvalue):
    s = _f51_share(undvalue, totalvalue)
    base = _z(s, 252)
    d1 = base - base.shift(84)
    d2 = d1 - d1.shift(84)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f51om_f51_ownership_mix_concentration_prfshareza_252d_jerk_v072_signal(fndvalue, undvalue, totalvalue):
    prf = (totalvalue - fndvalue - undvalue).clip(lower=0)
    s = prf / totalvalue.replace(0, np.nan)
    base = _z(s, 252)
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f51om_f51_ownership_mix_concentration_cllvalvscllcnta_252d_jerk_v073_signal(cllvalue, totalvalue, cllholders, shrholders):
    vs = _f51_share(cllvalue, totalvalue)
    cs = cllholders / (cllholders + shrholders).replace(0, np.nan)
    base = vs - cs
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f51om_f51_ownership_mix_concentration_optvalcntgapa_252d_jerk_v074_signal(cllvalue, putvalue, totalvalue, cllholders, putholders, shrholders):
    vshare = (cllvalue + putvalue) / totalvalue.replace(0, np.nan)
    cshare = (cllholders + putholders) / (cllholders + putholders + shrholders).replace(0, np.nan)
    base = vshare - cshare
    d1 = base - base.shift(63)
    d2 = d1 - d1.shift(63)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f51om_f51_ownership_mix_concentration_putvalvsputcnta_252d_jerk_v075_signal(putvalue, totalvalue, putholders, shrholders):
    vs = _f51_share(putvalue, totalvalue)
    cs = putholders / (putholders + shrholders).replace(0, np.nan)
    base = vs - cs
    d1 = base - base.shift(84)
    d2 = d1 - d1.shift(84)
    result = d2
    return result.replace([np.inf, -np.inf], np.nan)


def f51om_f51_ownership_mix_concentration_fndshareb_252d_jerk_v076_signal(fndvalue, totalvalue):
    base = _f51_share(fndvalue, totalvalue)
    scale = base.abs().rolling(126, min_periods=63).mean()
    g1 = (base - base.shift(126)) / scale.replace(0, np.nan)
    result = g1 - g1.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)


def f51om_f51_ownership_mix_concentration_fndsharezb_252d_jerk_v077_signal(fndvalue, totalvalue):
    s = _f51_share(fndvalue, totalvalue)
    base = _z(s, 252)
    scale = base.abs().rolling(168, min_periods=84).mean()
    g1 = (base - base.shift(168)) / scale.replace(0, np.nan)
    result = g1 - g1.shift(168)
    return result.replace([np.inf, -np.inf], np.nan)


def f51om_f51_ownership_mix_concentration_fndsharerankb_504d_jerk_v078_signal(fndvalue, totalvalue):
    s = _f51_share(fndvalue, totalvalue)
    base = _rank(s, 504)
    scale = base.abs().rolling(126, min_periods=63).mean()
    g1 = (base - base.shift(126)) / scale.replace(0, np.nan)
    result = g1 - g1.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)


def f51om_f51_ownership_mix_concentration_undshareb_252d_jerk_v079_signal(undvalue, totalvalue):
    base = _f51_share(undvalue, totalvalue)
    scale = base.abs().rolling(126, min_periods=63).mean()
    g1 = (base - base.shift(126)) / scale.replace(0, np.nan)
    result = g1 - g1.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)


def f51om_f51_ownership_mix_concentration_undsharerankb_504d_jerk_v080_signal(undvalue, totalvalue):
    s = _f51_share(undvalue, totalvalue)
    base = _rank(s, 504)
    scale = base.abs().rolling(126, min_periods=63).mean()
    g1 = (base - base.shift(126)) / scale.replace(0, np.nan)
    result = g1 - g1.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)


def f51om_f51_ownership_mix_concentration_prfshareb_252d_jerk_v081_signal(fndvalue, undvalue, totalvalue):
    prf = (totalvalue - fndvalue - undvalue).clip(lower=0)
    base = prf / totalvalue.replace(0, np.nan)
    scale = base.abs().rolling(126, min_periods=63).mean()
    g1 = (base - base.shift(126)) / scale.replace(0, np.nan)
    result = g1 - g1.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)


def f51om_f51_ownership_mix_concentration_fndundlogrb_252d_jerk_v082_signal(fndvalue, undvalue, totalvalue):
    prf = (totalvalue - fndvalue - undvalue).clip(lower=0)
    base = _f51_logratio(prf, undvalue) - _f51_logratio(fndvalue, totalvalue)
    scale = base.abs().rolling(126, min_periods=63).mean()
    g1 = (base - base.shift(126)) / scale.replace(0, np.nan)
    result = g1 - g1.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)


def f51om_f51_ownership_mix_concentration_fndundlogrzb_126d_jerk_v083_signal(fndvalue, undvalue):
    r = _f51_logratio(fndvalue, undvalue)
    base = _z(r, 126)
    scale = base.abs().rolling(84, min_periods=42).mean()
    g1 = (base - base.shift(84)) / scale.replace(0, np.nan)
    result = g1 - g1.shift(84)
    return result.replace([np.inf, -np.inf], np.nan)


def f51om_f51_ownership_mix_concentration_netshareb_252d_jerk_v084_signal(fndvalue, undvalue, totalvalue):
    base = (fndvalue - undvalue) / totalvalue.replace(0, np.nan)
    scale = base.abs().rolling(168, min_periods=84).mean()
    g1 = (base - base.shift(168)) / scale.replace(0, np.nan)
    result = g1 - g1.shift(168)
    return result.replace([np.inf, -np.inf], np.nan)


def f51om_f51_ownership_mix_concentration_nonfundimbb_252d_jerk_v085_signal(fndvalue, undvalue, totalvalue):
    prf = (totalvalue - fndvalue - undvalue).clip(lower=0)
    base = (undvalue - prf).abs() / (undvalue + prf).replace(0, np.nan)
    scale = base.abs().rolling(126, min_periods=63).mean()
    g1 = (base - base.shift(126)) / scale.replace(0, np.nan)
    result = g1 - g1.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)


def f51om_f51_ownership_mix_concentration_nonfundimbzb_252d_jerk_v086_signal(fndvalue, undvalue, totalvalue):
    prf = (totalvalue - fndvalue - undvalue).clip(lower=0)
    imb = (undvalue - prf).abs() / (undvalue + prf).replace(0, np.nan)
    base = _z(imb, 252)
    scale = base.abs().rolling(168, min_periods=84).mean()
    g1 = (base - base.shift(168)) / scale.replace(0, np.nan)
    result = g1 - g1.shift(168)
    return result.replace([np.inf, -np.inf], np.nan)


def f51om_f51_ownership_mix_concentration_herfvalimbb_252d_jerk_v087_signal(fndvalue, undvalue, totalvalue):
    prf = (totalvalue - fndvalue - undvalue).clip(lower=0)
    base = (fndvalue - prf).abs() / (fndvalue + prf).replace(0, np.nan)
    scale = base.abs().rolling(126, min_periods=63).mean()
    g1 = (base - base.shift(126)) / scale.replace(0, np.nan)
    result = g1 - g1.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)


def f51om_f51_ownership_mix_concentration_herfcntzb_252d_jerk_v088_signal(fndholders, undholders, prfholders):
    h = _f51_herf(fndholders, undholders, prfholders)
    base = _z(h, 252)
    scale = base.abs().rolling(126, min_periods=63).mean()
    g1 = (base - base.shift(126)) / scale.replace(0, np.nan)
    result = g1 - g1.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)


def f51om_f51_ownership_mix_concentration_nfbreadthimbb_252d_jerk_v089_signal(undholders, prfholders):
    base = (undholders - prfholders).abs() / (undholders + prfholders).replace(0, np.nan)
    scale = base.abs().rolling(126, min_periods=63).mean()
    g1 = (base - base.shift(126)) / scale.replace(0, np.nan)
    result = g1 - g1.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)


def f51om_f51_ownership_mix_concentration_prfcntshareb_252d_jerk_v090_signal(fndholders, undholders, prfholders):
    tot = (fndholders + undholders + prfholders).replace(0, np.nan)
    base = prfholders / tot
    scale = base.abs().rolling(168, min_periods=84).mean()
    g1 = (base - base.shift(168)) / scale.replace(0, np.nan)
    result = g1 - g1.shift(168)
    return result.replace([np.inf, -np.inf], np.nan)


def f51om_f51_ownership_mix_concentration_avgholdvalb_252d_jerk_v091_signal(totalvalue, fndholders, undholders, prfholders):
    tot = (fndholders + undholders + prfholders).replace(0, np.nan)
    base = totalvalue / tot
    scale = base.abs().rolling(126, min_periods=63).mean()
    g1 = (base - base.shift(126)) / scale.replace(0, np.nan)
    result = g1 - g1.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)


def f51om_f51_ownership_mix_concentration_fndcntgrowb_63d_jerk_v092_signal(fndholders):
    base = _f51_growth(fndholders, 63)
    scale = base.abs().rolling(42, min_periods=21).mean()
    g1 = (base - base.shift(42)) / scale.replace(0, np.nan)
    result = g1 - g1.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)


def f51om_f51_ownership_mix_concentration_fndundcntlogrb_252d_jerk_v093_signal(fndholders, undholders):
    base = _f51_logratio(fndholders, undholders)
    scale = base.abs().rolling(126, min_periods=63).mean()
    g1 = (base - base.shift(126)) / scale.replace(0, np.nan)
    result = g1 - g1.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)


def f51om_f51_ownership_mix_concentration_prfvalticketgapb_252d_jerk_v094_signal(prfvalue, prfholders, undvalue, undholders):
    tp = prfvalue / prfholders.replace(0, np.nan)
    tu = undvalue / undholders.replace(0, np.nan)
    base = _f51_logratio(tp, tu)
    scale = base.abs().rolling(126, min_periods=63).mean()
    g1 = (base - base.shift(126)) / scale.replace(0, np.nan)
    result = g1 - g1.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)


def f51om_f51_ownership_mix_concentration_fndticketb_252d_jerk_v095_signal(fndvalue, fndholders):
    base = fndvalue / fndholders.replace(0, np.nan)
    scale = base.abs().rolling(126, min_periods=63).mean()
    g1 = (base - base.shift(126)) / scale.replace(0, np.nan)
    result = g1 - g1.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)


def f51om_f51_ownership_mix_concentration_fndticketzb_252d_jerk_v096_signal(fndvalue, fndholders):
    t = fndvalue / fndholders.replace(0, np.nan)
    base = _z(t, 252)
    scale = base.abs().rolling(168, min_periods=84).mean()
    g1 = (base - base.shift(168)) / scale.replace(0, np.nan)
    result = g1 - g1.shift(168)
    return result.replace([np.inf, -np.inf], np.nan)


def f51om_f51_ownership_mix_concentration_ticketspreadb_252d_jerk_v097_signal(fndvalue, fndholders, undvalue, undholders):
    tf = fndvalue / fndholders.replace(0, np.nan)
    tu = undvalue / undholders.replace(0, np.nan)
    base = _f51_logratio(tf, tu)
    scale = base.abs().rolling(126, min_periods=63).mean()
    g1 = (base - base.shift(126)) / scale.replace(0, np.nan)
    result = g1 - g1.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)


def f51om_f51_ownership_mix_concentration_undticketb_252d_jerk_v098_signal(undvalue, undholders):
    base = undvalue / undholders.replace(0, np.nan)
    scale = base.abs().rolling(126, min_periods=63).mean()
    g1 = (base - base.shift(126)) / scale.replace(0, np.nan)
    result = g1 - g1.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)


def f51om_f51_ownership_mix_concentration_prfticketb_252d_jerk_v099_signal(prfvalue, prfholders):
    base = prfvalue / prfholders.replace(0, np.nan)
    scale = base.abs().rolling(126, min_periods=63).mean()
    g1 = (base - base.shift(126)) / scale.replace(0, np.nan)
    result = g1 - g1.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)


def f51om_f51_ownership_mix_concentration_putskewb_252d_jerk_v100_signal(putvalue, cllvalue):
    base = _f51_skew(putvalue, cllvalue)
    scale = base.abs().rolling(126, min_periods=63).mean()
    g1 = (base - base.shift(126)) / scale.replace(0, np.nan)
    result = g1 - g1.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)


def f51om_f51_ownership_mix_concentration_putskewzb_252d_jerk_v101_signal(putvalue, cllvalue):
    s = _f51_skew(putvalue, cllvalue)
    base = _z(s, 252)
    scale = base.abs().rolling(168, min_periods=84).mean()
    g1 = (base - base.shift(168)) / scale.replace(0, np.nan)
    result = g1 - g1.shift(168)
    return result.replace([np.inf, -np.inf], np.nan)


def f51om_f51_ownership_mix_concentration_putskewrankb_504d_jerk_v102_signal(putvalue, cllvalue):
    s = _f51_skew(putvalue, cllvalue)
    base = _rank(s, 504)
    scale = base.abs().rolling(126, min_periods=63).mean()
    g1 = (base - base.shift(126)) / scale.replace(0, np.nan)
    result = g1 - g1.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)


def f51om_f51_ownership_mix_concentration_putcntskewb_252d_jerk_v103_signal(putholders, cllholders):
    base = _f51_skew(putholders, cllholders)
    scale = base.abs().rolling(126, min_periods=63).mean()
    g1 = (base - base.shift(126)) / scale.replace(0, np.nan)
    result = g1 - g1.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)


def f51om_f51_ownership_mix_concentration_putcntskewzb_252d_jerk_v104_signal(putholders, cllholders):
    s = _f51_skew(putholders, cllholders)
    base = _z(s, 252)
    scale = base.abs().rolling(168, min_periods=84).mean()
    g1 = (base - base.shift(168)) / scale.replace(0, np.nan)
    result = g1 - g1.shift(168)
    return result.replace([np.inf, -np.inf], np.nan)


def f51om_f51_ownership_mix_concentration_optbreadthb_252d_jerk_v105_signal(putholders, cllholders, shrholders):
    base = (putholders + cllholders) / shrholders.replace(0, np.nan)
    scale = base.abs().rolling(126, min_periods=63).mean()
    g1 = (base - base.shift(126)) / scale.replace(0, np.nan)
    result = g1 - g1.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)


def f51om_f51_ownership_mix_concentration_callbreadthb_252d_jerk_v106_signal(cllholders, shrholders):
    base = cllholders / shrholders.replace(0, np.nan)
    scale = base.abs().rolling(168, min_periods=84).mean()
    g1 = (base - base.shift(168)) / scale.replace(0, np.nan)
    result = g1 - g1.shift(168)
    return result.replace([np.inf, -np.inf], np.nan)


def f51om_f51_ownership_mix_concentration_putbreadthb_252d_jerk_v107_signal(putholders, shrholders):
    base = putholders / shrholders.replace(0, np.nan)
    scale = base.abs().rolling(168, min_periods=84).mean()
    g1 = (base - base.shift(168)) / scale.replace(0, np.nan)
    result = g1 - g1.shift(168)
    return result.replace([np.inf, -np.inf], np.nan)


def f51om_f51_ownership_mix_concentration_callbreadthzb_252d_jerk_v108_signal(cllholders, shrholders):
    r = cllholders / shrholders.replace(0, np.nan)
    base = _z(r, 252)
    scale = base.abs().rolling(126, min_periods=63).mean()
    g1 = (base - base.shift(126)) / scale.replace(0, np.nan)
    result = g1 - g1.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)


def f51om_f51_ownership_mix_concentration_optfootb_252d_jerk_v109_signal(cllvalue, putvalue, totalvalue):
    base = (cllvalue + putvalue) / totalvalue.replace(0, np.nan)
    scale = base.abs().rolling(126, min_periods=63).mean()
    g1 = (base - base.shift(126)) / scale.replace(0, np.nan)
    result = g1 - g1.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)


def f51om_f51_ownership_mix_concentration_optfootzb_252d_jerk_v110_signal(cllvalue, putvalue, totalvalue):
    r = (cllvalue + putvalue) / totalvalue.replace(0, np.nan)
    base = _z(r, 252)
    scale = base.abs().rolling(168, min_periods=84).mean()
    g1 = (base - base.shift(168)) / scale.replace(0, np.nan)
    result = g1 - g1.shift(168)
    return result.replace([np.inf, -np.inf], np.nan)


def f51om_f51_ownership_mix_concentration_optnetshareb_252d_jerk_v111_signal(cllvalue, putvalue, totalvalue):
    base = (cllvalue - putvalue) / totalvalue.replace(0, np.nan)
    scale = base.abs().rolling(126, min_periods=63).mean()
    g1 = (base - base.shift(126)) / scale.replace(0, np.nan)
    result = g1 - g1.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)


def f51om_f51_ownership_mix_concentration_putvalshareb_252d_jerk_v112_signal(putvalue, undvalue):
    base = putvalue / (putvalue + undvalue).replace(0, np.nan)
    scale = base.abs().rolling(126, min_periods=63).mean()
    g1 = (base - base.shift(126)) / scale.replace(0, np.nan)
    result = g1 - g1.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)


def f51om_f51_ownership_mix_concentration_cllvalshareb_252d_jerk_v113_signal(cllvalue, totalvalue):
    base = _f51_share(cllvalue, totalvalue)
    scale = base.abs().rolling(168, min_periods=84).mean()
    g1 = (base - base.shift(168)) / scale.replace(0, np.nan)
    result = g1 - g1.shift(168)
    return result.replace([np.inf, -np.inf], np.nan)


def f51om_f51_ownership_mix_concentration_optvsfndb_252d_jerk_v114_signal(cllvalue, putvalue, undvalue):
    base = _f51_logratio(cllvalue + putvalue, undvalue)
    scale = base.abs().rolling(126, min_periods=63).mean()
    g1 = (base - base.shift(126)) / scale.replace(0, np.nan)
    result = g1 - g1.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)


def f51om_f51_ownership_mix_concentration_cllvsfndb_252d_jerk_v115_signal(cllvalue, fndvalue):
    base = _f51_logratio(cllvalue, fndvalue)
    scale = base.abs().rolling(168, min_periods=84).mean()
    g1 = (base - base.shift(168)) / scale.replace(0, np.nan)
    result = g1 - g1.shift(168)
    return result.replace([np.inf, -np.inf], np.nan)


def f51om_f51_ownership_mix_concentration_putvsfndb_252d_jerk_v116_signal(putvalue, fndvalue):
    base = _f51_logratio(putvalue, fndvalue)
    scale = base.abs().rolling(126, min_periods=63).mean()
    g1 = (base - base.shift(126)) / scale.replace(0, np.nan)
    result = g1 - g1.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)


def f51om_f51_ownership_mix_concentration_potb_252d_jerk_v117_signal(percentoftotal):
    base = percentoftotal
    scale = base.abs().rolling(126, min_periods=63).mean()
    g1 = (base - base.shift(126)) / scale.replace(0, np.nan)
    result = g1 - g1.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)


def f51om_f51_ownership_mix_concentration_potzb_252d_jerk_v118_signal(percentoftotal):
    base = _z(percentoftotal, 252)
    scale = base.abs().rolling(168, min_periods=84).mean()
    g1 = (base - base.shift(168)) / scale.replace(0, np.nan)
    result = g1 - g1.shift(168)
    return result.replace([np.inf, -np.inf], np.nan)


def f51om_f51_ownership_mix_concentration_potrankb_504d_jerk_v119_signal(percentoftotal):
    base = _rank(percentoftotal, 504)
    scale = base.abs().rolling(126, min_periods=63).mean()
    g1 = (base - base.shift(126)) / scale.replace(0, np.nan)
    result = g1 - g1.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)


def f51om_f51_ownership_mix_concentration_callputticketb_252d_jerk_v120_signal(cllvalue, cllholders, putvalue, putholders):
    tc = cllvalue / cllholders.replace(0, np.nan)
    tp = putvalue / putholders.replace(0, np.nan)
    base = _f51_logratio(tc, tp)
    scale = base.abs().rolling(126, min_periods=63).mean()
    g1 = (base - base.shift(126)) / scale.replace(0, np.nan)
    result = g1 - g1.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)


def f51om_f51_ownership_mix_concentration_putticketb_252d_jerk_v121_signal(putvalue, putholders):
    base = putvalue / putholders.replace(0, np.nan)
    scale = base.abs().rolling(126, min_periods=63).mean()
    g1 = (base - base.shift(126)) / scale.replace(0, np.nan)
    result = g1 - g1.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)


def f51om_f51_ownership_mix_concentration_cllticketb_252d_jerk_v122_signal(cllvalue, cllholders):
    base = cllvalue / cllholders.replace(0, np.nan)
    scale = base.abs().rolling(168, min_periods=84).mean()
    g1 = (base - base.shift(168)) / scale.replace(0, np.nan)
    result = g1 - g1.shift(168)
    return result.replace([np.inf, -np.inf], np.nan)


def f51om_f51_ownership_mix_concentration_mixqb_252d_jerk_v123_signal(fndvalue, totalvalue, putvalue, cllvalue):
    fs = _f51_share(fndvalue, totalvalue)
    foot = (putvalue + cllvalue) / totalvalue.replace(0, np.nan)
    base = fs - foot
    scale = base.abs().rolling(126, min_periods=63).mean()
    g1 = (base - base.shift(126)) / scale.replace(0, np.nan)
    result = g1 - g1.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)


def f51om_f51_ownership_mix_concentration_fndvcgapb_252d_jerk_v124_signal(fndvalue, totalvalue, fndholders, undholders, prfholders):
    vs = _f51_share(fndvalue, totalvalue)
    cs = fndholders / (fndholders + undholders + prfholders).replace(0, np.nan)
    base = vs - cs
    scale = base.abs().rolling(126, min_periods=63).mean()
    g1 = (base - base.shift(126)) / scale.replace(0, np.nan)
    result = g1 - g1.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)


def f51om_f51_ownership_mix_concentration_undvcgapb_252d_jerk_v125_signal(undvalue, totalvalue, fndholders, undholders, prfholders):
    vs = _f51_share(undvalue, totalvalue)
    cs = undholders / (fndholders + undholders + prfholders).replace(0, np.nan)
    base = vs - cs
    scale = base.abs().rolling(168, min_periods=84).mean()
    g1 = (base - base.shift(168)) / scale.replace(0, np.nan)
    result = g1 - g1.shift(168)
    return result.replace([np.inf, -np.inf], np.nan)


def f51om_f51_ownership_mix_concentration_potfndb_252d_jerk_v126_signal(percentoftotal, fndvalue, totalvalue):
    s = _f51_share(fndvalue, totalvalue)
    base = percentoftotal * s
    scale = base.abs().rolling(126, min_periods=63).mean()
    g1 = (base - base.shift(126)) / scale.replace(0, np.nan)
    result = g1 - g1.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)


def f51om_f51_ownership_mix_concentration_potputb_252d_jerk_v127_signal(percentoftotal, putvalue, cllvalue):
    ps = _f51_skew(putvalue, cllvalue)
    base = percentoftotal * (ps - 0.5)
    scale = base.abs().rolling(126, min_periods=63).mean()
    g1 = (base - base.shift(126)) / scale.replace(0, np.nan)
    result = g1 - g1.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)


def f51om_f51_ownership_mix_concentration_shrfndgrowb_63d_jerk_v128_signal(shrholders, fndholders):
    base = _f51_growth(shrholders, 63) - _f51_growth(fndholders, 63)
    scale = base.abs().rolling(42, min_periods=21).mean()
    g1 = (base - base.shift(42)) / scale.replace(0, np.nan)
    result = g1 - g1.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)


def f51om_f51_ownership_mix_concentration_putvalgrowb_63d_jerk_v129_signal(putvalue, totalvalue):
    base = _f51_growth(putvalue, 63) - _f51_growth(totalvalue, 63)
    scale = base.abs().rolling(42, min_periods=21).mean()
    g1 = (base - base.shift(42)) / scale.replace(0, np.nan)
    result = g1 - g1.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)


def f51om_f51_ownership_mix_concentration_cllvalgrowb_63d_jerk_v130_signal(cllvalue, totalvalue):
    base = _f51_growth(cllvalue, 63) - _f51_growth(totalvalue, 63)
    scale = base.abs().rolling(42, min_periods=21).mean()
    g1 = (base - base.shift(42)) / scale.replace(0, np.nan)
    result = g1 - g1.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)


def f51om_f51_ownership_mix_concentration_optcntnetb_63d_jerk_v131_signal(cllholders, putholders):
    base = _f51_growth(cllholders, 63) - _f51_growth(putholders, 63)
    scale = base.abs().rolling(42, min_periods=21).mean()
    g1 = (base - base.shift(42)) / scale.replace(0, np.nan)
    result = g1 - g1.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)


def f51om_f51_ownership_mix_concentration_undcntgrowb_63d_jerk_v132_signal(undholders):
    base = _f51_growth(undholders, 63)
    scale = base.abs().rolling(42, min_periods=21).mean()
    g1 = (base - base.shift(42)) / scale.replace(0, np.nan)
    result = g1 - g1.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)


def f51om_f51_ownership_mix_concentration_prfcntgrowb_63d_jerk_v133_signal(prfholders):
    base = _f51_growth(prfholders, 63)
    scale = base.abs().rolling(42, min_periods=21).mean()
    g1 = (base - base.shift(42)) / scale.replace(0, np.nan)
    result = g1 - g1.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)


def f51om_f51_ownership_mix_concentration_shrcntgrowb_63d_jerk_v134_signal(shrholders):
    base = _f51_growth(shrholders, 63)
    scale = base.abs().rolling(42, min_periods=21).mean()
    g1 = (base - base.shift(42)) / scale.replace(0, np.nan)
    result = g1 - g1.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)


def f51om_f51_ownership_mix_concentration_totvalgrowb_63d_jerk_v135_signal(totalvalue):
    base = _f51_growth(totalvalue, 63)
    scale = base.abs().rolling(42, min_periods=21).mean()
    g1 = (base - base.shift(42)) / scale.replace(0, np.nan)
    result = g1 - g1.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)


def f51om_f51_ownership_mix_concentration_fndvalgrowb_63d_jerk_v136_signal(fndvalue):
    base = _f51_growth(fndvalue, 63)
    scale = base.abs().rolling(42, min_periods=21).mean()
    g1 = (base - base.shift(42)) / scale.replace(0, np.nan)
    result = g1 - g1.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)


def f51om_f51_ownership_mix_concentration_undvalgrowb_63d_jerk_v137_signal(undvalue):
    base = _f51_growth(undvalue, 63)
    scale = base.abs().rolling(42, min_periods=21).mean()
    g1 = (base - base.shift(42)) / scale.replace(0, np.nan)
    result = g1 - g1.shift(42)
    return result.replace([np.inf, -np.inf], np.nan)


def f51om_f51_ownership_mix_concentration_fndcntxvalshareb_252d_jerk_v138_signal(fndholders, undholders, prfholders, fndvalue, totalvalue):
    fc = fndholders / (fndholders + undholders + prfholders).replace(0, np.nan)
    vs = _f51_share(fndvalue, totalvalue)
    base = fc * vs
    scale = base.abs().rolling(126, min_periods=63).mean()
    g1 = (base - base.shift(126)) / scale.replace(0, np.nan)
    result = g1 - g1.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)


def f51om_f51_ownership_mix_concentration_stressb_252d_jerk_v139_signal(putvalue, cllvalue, totalvalue, undvalue):
    ps = _f51_skew(putvalue, cllvalue)
    foot = (putvalue + cllvalue) / totalvalue.replace(0, np.nan)
    us = _f51_share(undvalue, totalvalue)
    base = (ps - 0.5) * foot + 0.5 * us
    scale = base.abs().rolling(126, min_periods=63).mean()
    g1 = (base - base.shift(126)) / scale.replace(0, np.nan)
    result = g1 - g1.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)


def f51om_f51_ownership_mix_concentration_potcallqb_252d_jerk_v140_signal(percentoftotal, putholders, cllholders):
    ps = _f51_skew(putholders, cllholders)
    base = percentoftotal * (1.0 - ps)
    scale = base.abs().rolling(168, min_periods=84).mean()
    g1 = (base - base.shift(168)) / scale.replace(0, np.nan)
    result = g1 - g1.shift(168)
    return result.replace([np.inf, -np.inf], np.nan)


def f51om_f51_ownership_mix_concentration_undprfvallogrb_252d_jerk_v141_signal(fndvalue, undvalue, totalvalue):
    prf = (totalvalue - fndvalue - undvalue).clip(lower=0)
    base = _f51_logratio(undvalue, prf)
    scale = base.abs().rolling(126, min_periods=63).mean()
    g1 = (base - base.shift(126)) / scale.replace(0, np.nan)
    result = g1 - g1.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)


def f51om_f51_ownership_mix_concentration_undcntsharezb_252d_jerk_v142_signal(fndholders, undholders, prfholders):
    tot = (fndholders + undholders + prfholders).replace(0, np.nan)
    s = undholders / tot
    base = _z(s, 252)
    scale = base.abs().rolling(126, min_periods=63).mean()
    g1 = (base - base.shift(126)) / scale.replace(0, np.nan)
    result = g1 - g1.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)


def f51om_f51_ownership_mix_concentration_optcntbreadthlogrb_252d_jerk_v143_signal(cllholders, putholders, undholders):
    base = _f51_logratio(cllholders + putholders, undholders)
    scale = base.abs().rolling(126, min_periods=63).mean()
    g1 = (base - base.shift(126)) / scale.replace(0, np.nan)
    result = g1 - g1.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)


def f51om_f51_ownership_mix_concentration_optnetsharezb_252d_jerk_v144_signal(cllvalue, putvalue, totalvalue):
    r = (cllvalue - putvalue) / totalvalue.replace(0, np.nan)
    base = _z(r, 252)
    scale = base.abs().rolling(168, min_periods=84).mean()
    g1 = (base - base.shift(168)) / scale.replace(0, np.nan)
    result = g1 - g1.shift(168)
    return result.replace([np.inf, -np.inf], np.nan)


def f51om_f51_ownership_mix_concentration_putvalsharezb_252d_jerk_v145_signal(putvalue, totalvalue):
    s = _f51_share(putvalue, totalvalue)
    base = _z(s, 252)
    scale = base.abs().rolling(126, min_periods=63).mean()
    g1 = (base - base.shift(126)) / scale.replace(0, np.nan)
    result = g1 - g1.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)


def f51om_f51_ownership_mix_concentration_undsharezb_252d_jerk_v146_signal(undvalue, totalvalue):
    s = _f51_share(undvalue, totalvalue)
    base = _z(s, 252)
    scale = base.abs().rolling(168, min_periods=84).mean()
    g1 = (base - base.shift(168)) / scale.replace(0, np.nan)
    result = g1 - g1.shift(168)
    return result.replace([np.inf, -np.inf], np.nan)


def f51om_f51_ownership_mix_concentration_prfsharezb_252d_jerk_v147_signal(fndvalue, undvalue, totalvalue):
    prf = (totalvalue - fndvalue - undvalue).clip(lower=0)
    s = prf / totalvalue.replace(0, np.nan)
    base = _z(s, 252)
    scale = base.abs().rolling(126, min_periods=63).mean()
    g1 = (base - base.shift(126)) / scale.replace(0, np.nan)
    result = g1 - g1.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)


def f51om_f51_ownership_mix_concentration_cllvalvscllcntb_252d_jerk_v148_signal(cllvalue, totalvalue, cllholders, shrholders):
    vs = _f51_share(cllvalue, totalvalue)
    cs = cllholders / (cllholders + shrholders).replace(0, np.nan)
    base = vs - cs
    scale = base.abs().rolling(126, min_periods=63).mean()
    g1 = (base - base.shift(126)) / scale.replace(0, np.nan)
    result = g1 - g1.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)


def f51om_f51_ownership_mix_concentration_optvalcntgapb_252d_jerk_v149_signal(cllvalue, putvalue, totalvalue, cllholders, putholders, shrholders):
    vshare = (cllvalue + putvalue) / totalvalue.replace(0, np.nan)
    cshare = (cllholders + putholders) / (cllholders + putholders + shrholders).replace(0, np.nan)
    base = vshare - cshare
    scale = base.abs().rolling(126, min_periods=63).mean()
    g1 = (base - base.shift(126)) / scale.replace(0, np.nan)
    result = g1 - g1.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)


def f51om_f51_ownership_mix_concentration_putvalvsputcntb_252d_jerk_v150_signal(putvalue, totalvalue, putholders, shrholders):
    vs = _f51_share(putvalue, totalvalue)
    cs = putholders / (putholders + shrholders).replace(0, np.nan)
    base = vs - cs
    scale = base.abs().rolling(168, min_periods=84).mean()
    g1 = (base - base.shift(168)) / scale.replace(0, np.nan)
    result = g1 - g1.shift(168)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f51om_f51_ownership_mix_concentration_fndsharea_252d_jerk_v001_signal,
    f51om_f51_ownership_mix_concentration_fndshareza_252d_jerk_v002_signal,
    f51om_f51_ownership_mix_concentration_fndshareranka_504d_jerk_v003_signal,
    f51om_f51_ownership_mix_concentration_undsharea_252d_jerk_v004_signal,
    f51om_f51_ownership_mix_concentration_undshareranka_504d_jerk_v005_signal,
    f51om_f51_ownership_mix_concentration_prfsharea_252d_jerk_v006_signal,
    f51om_f51_ownership_mix_concentration_fndundlogra_252d_jerk_v007_signal,
    f51om_f51_ownership_mix_concentration_fndundlogrza_126d_jerk_v008_signal,
    f51om_f51_ownership_mix_concentration_netsharea_252d_jerk_v009_signal,
    f51om_f51_ownership_mix_concentration_nonfundimba_252d_jerk_v010_signal,
    f51om_f51_ownership_mix_concentration_nonfundimbza_252d_jerk_v011_signal,
    f51om_f51_ownership_mix_concentration_herfvalimba_252d_jerk_v012_signal,
    f51om_f51_ownership_mix_concentration_herfcntza_252d_jerk_v013_signal,
    f51om_f51_ownership_mix_concentration_nfbreadthimba_252d_jerk_v014_signal,
    f51om_f51_ownership_mix_concentration_prfcntsharea_252d_jerk_v015_signal,
    f51om_f51_ownership_mix_concentration_avgholdvala_252d_jerk_v016_signal,
    f51om_f51_ownership_mix_concentration_fndcntgrowa_63d_jerk_v017_signal,
    f51om_f51_ownership_mix_concentration_fndundcntlogra_252d_jerk_v018_signal,
    f51om_f51_ownership_mix_concentration_prfvalticketgapa_252d_jerk_v019_signal,
    f51om_f51_ownership_mix_concentration_fndticketa_252d_jerk_v020_signal,
    f51om_f51_ownership_mix_concentration_fndticketza_252d_jerk_v021_signal,
    f51om_f51_ownership_mix_concentration_ticketspreada_252d_jerk_v022_signal,
    f51om_f51_ownership_mix_concentration_undticketa_252d_jerk_v023_signal,
    f51om_f51_ownership_mix_concentration_prfticketa_252d_jerk_v024_signal,
    f51om_f51_ownership_mix_concentration_putskewa_252d_jerk_v025_signal,
    f51om_f51_ownership_mix_concentration_putskewza_252d_jerk_v026_signal,
    f51om_f51_ownership_mix_concentration_putskewranka_504d_jerk_v027_signal,
    f51om_f51_ownership_mix_concentration_putcntskewa_252d_jerk_v028_signal,
    f51om_f51_ownership_mix_concentration_putcntskewza_252d_jerk_v029_signal,
    f51om_f51_ownership_mix_concentration_optbreadtha_252d_jerk_v030_signal,
    f51om_f51_ownership_mix_concentration_callbreadtha_252d_jerk_v031_signal,
    f51om_f51_ownership_mix_concentration_putbreadtha_252d_jerk_v032_signal,
    f51om_f51_ownership_mix_concentration_callbreadthza_252d_jerk_v033_signal,
    f51om_f51_ownership_mix_concentration_optfoota_252d_jerk_v034_signal,
    f51om_f51_ownership_mix_concentration_optfootza_252d_jerk_v035_signal,
    f51om_f51_ownership_mix_concentration_optnetsharea_252d_jerk_v036_signal,
    f51om_f51_ownership_mix_concentration_putvalsharea_252d_jerk_v037_signal,
    f51om_f51_ownership_mix_concentration_cllvalsharea_252d_jerk_v038_signal,
    f51om_f51_ownership_mix_concentration_optvsfnda_252d_jerk_v039_signal,
    f51om_f51_ownership_mix_concentration_cllvsfnda_252d_jerk_v040_signal,
    f51om_f51_ownership_mix_concentration_putvsfnda_252d_jerk_v041_signal,
    f51om_f51_ownership_mix_concentration_pota_252d_jerk_v042_signal,
    f51om_f51_ownership_mix_concentration_potza_252d_jerk_v043_signal,
    f51om_f51_ownership_mix_concentration_potranka_504d_jerk_v044_signal,
    f51om_f51_ownership_mix_concentration_callputticketa_252d_jerk_v045_signal,
    f51om_f51_ownership_mix_concentration_putticketa_252d_jerk_v046_signal,
    f51om_f51_ownership_mix_concentration_cllticketa_252d_jerk_v047_signal,
    f51om_f51_ownership_mix_concentration_mixqa_252d_jerk_v048_signal,
    f51om_f51_ownership_mix_concentration_fndvcgapa_252d_jerk_v049_signal,
    f51om_f51_ownership_mix_concentration_undvcgapa_252d_jerk_v050_signal,
    f51om_f51_ownership_mix_concentration_potfnda_252d_jerk_v051_signal,
    f51om_f51_ownership_mix_concentration_potputa_252d_jerk_v052_signal,
    f51om_f51_ownership_mix_concentration_shrfndgrowa_63d_jerk_v053_signal,
    f51om_f51_ownership_mix_concentration_putvalgrowa_63d_jerk_v054_signal,
    f51om_f51_ownership_mix_concentration_cllvalgrowa_63d_jerk_v055_signal,
    f51om_f51_ownership_mix_concentration_optcntneta_63d_jerk_v056_signal,
    f51om_f51_ownership_mix_concentration_undcntgrowa_63d_jerk_v057_signal,
    f51om_f51_ownership_mix_concentration_prfcntgrowa_63d_jerk_v058_signal,
    f51om_f51_ownership_mix_concentration_shrcntgrowa_63d_jerk_v059_signal,
    f51om_f51_ownership_mix_concentration_totvalgrowa_63d_jerk_v060_signal,
    f51om_f51_ownership_mix_concentration_fndvalgrowa_63d_jerk_v061_signal,
    f51om_f51_ownership_mix_concentration_undvalgrowa_63d_jerk_v062_signal,
    f51om_f51_ownership_mix_concentration_fndcntxvalsharea_252d_jerk_v063_signal,
    f51om_f51_ownership_mix_concentration_stressa_252d_jerk_v064_signal,
    f51om_f51_ownership_mix_concentration_potcallqa_252d_jerk_v065_signal,
    f51om_f51_ownership_mix_concentration_undprfvallogra_252d_jerk_v066_signal,
    f51om_f51_ownership_mix_concentration_undcntshareza_252d_jerk_v067_signal,
    f51om_f51_ownership_mix_concentration_optcntbreadthlogra_252d_jerk_v068_signal,
    f51om_f51_ownership_mix_concentration_optnetshareza_252d_jerk_v069_signal,
    f51om_f51_ownership_mix_concentration_putvalshareza_252d_jerk_v070_signal,
    f51om_f51_ownership_mix_concentration_undshareza_252d_jerk_v071_signal,
    f51om_f51_ownership_mix_concentration_prfshareza_252d_jerk_v072_signal,
    f51om_f51_ownership_mix_concentration_cllvalvscllcnta_252d_jerk_v073_signal,
    f51om_f51_ownership_mix_concentration_optvalcntgapa_252d_jerk_v074_signal,
    f51om_f51_ownership_mix_concentration_putvalvsputcnta_252d_jerk_v075_signal,
    f51om_f51_ownership_mix_concentration_fndshareb_252d_jerk_v076_signal,
    f51om_f51_ownership_mix_concentration_fndsharezb_252d_jerk_v077_signal,
    f51om_f51_ownership_mix_concentration_fndsharerankb_504d_jerk_v078_signal,
    f51om_f51_ownership_mix_concentration_undshareb_252d_jerk_v079_signal,
    f51om_f51_ownership_mix_concentration_undsharerankb_504d_jerk_v080_signal,
    f51om_f51_ownership_mix_concentration_prfshareb_252d_jerk_v081_signal,
    f51om_f51_ownership_mix_concentration_fndundlogrb_252d_jerk_v082_signal,
    f51om_f51_ownership_mix_concentration_fndundlogrzb_126d_jerk_v083_signal,
    f51om_f51_ownership_mix_concentration_netshareb_252d_jerk_v084_signal,
    f51om_f51_ownership_mix_concentration_nonfundimbb_252d_jerk_v085_signal,
    f51om_f51_ownership_mix_concentration_nonfundimbzb_252d_jerk_v086_signal,
    f51om_f51_ownership_mix_concentration_herfvalimbb_252d_jerk_v087_signal,
    f51om_f51_ownership_mix_concentration_herfcntzb_252d_jerk_v088_signal,
    f51om_f51_ownership_mix_concentration_nfbreadthimbb_252d_jerk_v089_signal,
    f51om_f51_ownership_mix_concentration_prfcntshareb_252d_jerk_v090_signal,
    f51om_f51_ownership_mix_concentration_avgholdvalb_252d_jerk_v091_signal,
    f51om_f51_ownership_mix_concentration_fndcntgrowb_63d_jerk_v092_signal,
    f51om_f51_ownership_mix_concentration_fndundcntlogrb_252d_jerk_v093_signal,
    f51om_f51_ownership_mix_concentration_prfvalticketgapb_252d_jerk_v094_signal,
    f51om_f51_ownership_mix_concentration_fndticketb_252d_jerk_v095_signal,
    f51om_f51_ownership_mix_concentration_fndticketzb_252d_jerk_v096_signal,
    f51om_f51_ownership_mix_concentration_ticketspreadb_252d_jerk_v097_signal,
    f51om_f51_ownership_mix_concentration_undticketb_252d_jerk_v098_signal,
    f51om_f51_ownership_mix_concentration_prfticketb_252d_jerk_v099_signal,
    f51om_f51_ownership_mix_concentration_putskewb_252d_jerk_v100_signal,
    f51om_f51_ownership_mix_concentration_putskewzb_252d_jerk_v101_signal,
    f51om_f51_ownership_mix_concentration_putskewrankb_504d_jerk_v102_signal,
    f51om_f51_ownership_mix_concentration_putcntskewb_252d_jerk_v103_signal,
    f51om_f51_ownership_mix_concentration_putcntskewzb_252d_jerk_v104_signal,
    f51om_f51_ownership_mix_concentration_optbreadthb_252d_jerk_v105_signal,
    f51om_f51_ownership_mix_concentration_callbreadthb_252d_jerk_v106_signal,
    f51om_f51_ownership_mix_concentration_putbreadthb_252d_jerk_v107_signal,
    f51om_f51_ownership_mix_concentration_callbreadthzb_252d_jerk_v108_signal,
    f51om_f51_ownership_mix_concentration_optfootb_252d_jerk_v109_signal,
    f51om_f51_ownership_mix_concentration_optfootzb_252d_jerk_v110_signal,
    f51om_f51_ownership_mix_concentration_optnetshareb_252d_jerk_v111_signal,
    f51om_f51_ownership_mix_concentration_putvalshareb_252d_jerk_v112_signal,
    f51om_f51_ownership_mix_concentration_cllvalshareb_252d_jerk_v113_signal,
    f51om_f51_ownership_mix_concentration_optvsfndb_252d_jerk_v114_signal,
    f51om_f51_ownership_mix_concentration_cllvsfndb_252d_jerk_v115_signal,
    f51om_f51_ownership_mix_concentration_putvsfndb_252d_jerk_v116_signal,
    f51om_f51_ownership_mix_concentration_potb_252d_jerk_v117_signal,
    f51om_f51_ownership_mix_concentration_potzb_252d_jerk_v118_signal,
    f51om_f51_ownership_mix_concentration_potrankb_504d_jerk_v119_signal,
    f51om_f51_ownership_mix_concentration_callputticketb_252d_jerk_v120_signal,
    f51om_f51_ownership_mix_concentration_putticketb_252d_jerk_v121_signal,
    f51om_f51_ownership_mix_concentration_cllticketb_252d_jerk_v122_signal,
    f51om_f51_ownership_mix_concentration_mixqb_252d_jerk_v123_signal,
    f51om_f51_ownership_mix_concentration_fndvcgapb_252d_jerk_v124_signal,
    f51om_f51_ownership_mix_concentration_undvcgapb_252d_jerk_v125_signal,
    f51om_f51_ownership_mix_concentration_potfndb_252d_jerk_v126_signal,
    f51om_f51_ownership_mix_concentration_potputb_252d_jerk_v127_signal,
    f51om_f51_ownership_mix_concentration_shrfndgrowb_63d_jerk_v128_signal,
    f51om_f51_ownership_mix_concentration_putvalgrowb_63d_jerk_v129_signal,
    f51om_f51_ownership_mix_concentration_cllvalgrowb_63d_jerk_v130_signal,
    f51om_f51_ownership_mix_concentration_optcntnetb_63d_jerk_v131_signal,
    f51om_f51_ownership_mix_concentration_undcntgrowb_63d_jerk_v132_signal,
    f51om_f51_ownership_mix_concentration_prfcntgrowb_63d_jerk_v133_signal,
    f51om_f51_ownership_mix_concentration_shrcntgrowb_63d_jerk_v134_signal,
    f51om_f51_ownership_mix_concentration_totvalgrowb_63d_jerk_v135_signal,
    f51om_f51_ownership_mix_concentration_fndvalgrowb_63d_jerk_v136_signal,
    f51om_f51_ownership_mix_concentration_undvalgrowb_63d_jerk_v137_signal,
    f51om_f51_ownership_mix_concentration_fndcntxvalshareb_252d_jerk_v138_signal,
    f51om_f51_ownership_mix_concentration_stressb_252d_jerk_v139_signal,
    f51om_f51_ownership_mix_concentration_potcallqb_252d_jerk_v140_signal,
    f51om_f51_ownership_mix_concentration_undprfvallogrb_252d_jerk_v141_signal,
    f51om_f51_ownership_mix_concentration_undcntsharezb_252d_jerk_v142_signal,
    f51om_f51_ownership_mix_concentration_optcntbreadthlogrb_252d_jerk_v143_signal,
    f51om_f51_ownership_mix_concentration_optnetsharezb_252d_jerk_v144_signal,
    f51om_f51_ownership_mix_concentration_putvalsharezb_252d_jerk_v145_signal,
    f51om_f51_ownership_mix_concentration_undsharezb_252d_jerk_v146_signal,
    f51om_f51_ownership_mix_concentration_prfsharezb_252d_jerk_v147_signal,
    f51om_f51_ownership_mix_concentration_cllvalvscllcntb_252d_jerk_v148_signal,
    f51om_f51_ownership_mix_concentration_optvalcntgapb_252d_jerk_v149_signal,
    f51om_f51_ownership_mix_concentration_putvalvsputcntb_252d_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F51_OWNERSHIP_MIX_CONCENTRATION_REGISTRY_3RD_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500

    ALLOW = {
        "open", "high", "low", "close", "closeadj", "volume",
        "revenue", "revenueusd", "deferredrev", "gp", "grossmargin", "opinc", "opex",
        "sgna", "cor", "rnd", "sbcomp", "ebit", "ebitda", "ebitdamargin", "netinc",
        "netinccmn", "netmargin", "eps", "epsdil", "fcf", "fcfps", "ncfo", "ncff",
        "ncfi", "ncfcommon", "ncfdebt", "ncfbus", "capex", "depamor", "sharesbas",
        "shareswa", "shareswadil", "assets", "assetsc", "tangibles", "intangibles",
        "ppnenet", "investments", "inventory", "receivables", "payables", "equity",
        "retearn", "workingcapital", "debt", "debtc", "debtnc", "liabilities",
        "liabilitiesc", "cashneq", "currentratio", "roic", "roe", "roa", "ros",
        "assetturnover", "invcap", "intexp", "taxexp", "ebt", "sps", "bvps", "tbvps",
        "de", "ncfdiv", "ncfinv", "dps", "divyield", "payoutratio", "prefdivis",
        "netincdis", "marketcap", "ev", "evebit", "evebitda", "pe", "pb", "ps",
        "shrholders", "shrvalue", "shrunits", "totalvalue", "percentoftotal",
        "fndholders", "undholders", "prfholders", "dbtholders", "putholders",
        "putvalue", "cllholders", "cllvalue", "wntholders", "wntvalue", "dbtvalue",
        "fndvalue", "undvalue", "prfvalue", "fndunits", "undunits",
    }

    def _fund(seed, base=1e8, drift=0.03, vol=0.07, allow_neg=False):
        g = np.random.default_rng(seed)
        steps = np.repeat(g.normal(drift, vol, n // 63 + 1), 63)[:n]
        s = base * np.exp(np.cumsum(steps / 63))
        if allow_neg:
            s = s - base * 0.6
        return pd.Series(s, name=None)

    fndvalue = _fund(201, base=5.0e8, drift=0.05, vol=0.10).rename("fndvalue")
    undvalue = _fund(202, base=2.5e8, drift=0.03, vol=0.12).rename("undvalue")
    prfvalue = _fund(203, base=1.2e8, drift=0.02, vol=0.13).rename("prfvalue")
    totalvalue = (fndvalue + undvalue + prfvalue
                  + _fund(204, base=1.0e8, drift=0.025, vol=0.09)).rename("totalvalue")
    fndholders = _fund(205, base=300.0, drift=0.05, vol=0.10).rename("fndholders")
    undholders = _fund(206, base=180.0, drift=0.03, vol=0.12).rename("undholders")
    prfholders = _fund(207, base=90.0, drift=0.02, vol=0.13).rename("prfholders")
    shrholders = _fund(208, base=420.0, drift=0.045, vol=0.10).rename("shrholders")
    cllholders = _fund(209, base=60.0, drift=0.04, vol=0.15).rename("cllholders")
    putholders = _fund(210, base=45.0, drift=0.035, vol=0.16).rename("putholders")
    cllvalue = _fund(211, base=8.0e7, drift=0.04, vol=0.16).rename("cllvalue")
    putvalue = _fund(212, base=6.0e7, drift=0.05, vol=0.17).rename("putvalue")
    percentoftotal = (_fund(213, base=0.04, drift=0.02, vol=0.10)
                      .clip(upper=0.95)).rename("percentoftotal")

    cols = {
        "fndvalue": fndvalue, "undvalue": undvalue, "prfvalue": prfvalue,
        "totalvalue": totalvalue, "fndholders": fndholders, "undholders": undholders,
        "prfholders": prfholders, "shrholders": shrholders, "cllholders": cllholders,
        "putholders": putholders, "cllvalue": cllvalue, "putvalue": putvalue,
        "percentoftotal": percentoftotal,
    }

    own = {"shrholders", "shrvalue", "shrunits", "totalvalue", "percentoftotal",
           "fndholders", "undholders", "prfholders", "dbtholders", "putholders",
           "putvalue", "cllholders", "cllvalue", "wntholders", "wntvalue",
           "dbtvalue", "fndvalue", "undvalue", "prfvalue", "fndunits", "undunits"}

    n_features = 0
    nan_ok = 0
    results = {}
    for name, meta in REGISTRY.items():
        assert set(meta["inputs"]) <= ALLOW, "BAD INPUTS %s: %s" % (name, meta["inputs"])
        assert len(set(meta["inputs"]) & own) >= 1, "NO OWNERSHIP COL %s" % name
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

    print("OK f51_ownership_mix_concentration_3rd_derivatives_001_150_claude: %d features pass" % n_features)