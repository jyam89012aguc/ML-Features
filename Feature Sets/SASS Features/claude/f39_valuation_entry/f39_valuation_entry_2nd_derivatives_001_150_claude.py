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


# ===== generic helpers =====
def _z(s, w):
    m = s.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = s.rolling(w, min_periods=max(1, w // 2)).std()
    return (s - m) / sd.replace(0, np.nan)


def _mean(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _std(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


def _rank(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).rank(pct=True) - 0.5


def _rmin(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rmax(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _f39_cheap_z(mult, w):
    return -_z(mult, w)


def _f39_yield(num, denom):
    return num / denom.replace(0, np.nan)


def _f39_inv(mult):
    return 1.0 / mult.replace(0, np.nan)


def _f39_rng_cheap(mult, w):
    hi = _rmax(mult, w)
    lo = _rmin(mult, w)
    return (hi - mult) / (hi - lo).replace(0, np.nan)


def _roc(s, w):
    return s - s.shift(w)


def f39ve_f39_valuation_entry_pez_252d_slope_v001_signal(pe):
    base = -_z(pe, 252)
    d1 = base - base.shift(5)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_pez_252d_slope_v002_signal(pe):
    base = -_z(pe, 252)
    d1 = base - base.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_pez_252d_slope_v003_signal(pe):
    base = -_z(pe, 252)
    d1 = base - base.shift(63)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_pbz_252d_slope_v004_signal(pb):
    base = -_z(pb, 252)
    d1 = base - base.shift(5)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_pbz_252d_slope_v005_signal(pb):
    base = -_z(pb, 252)
    d1 = base - base.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_pbz_252d_slope_v006_signal(pb):
    base = -_z(pb, 252)
    d1 = base - base.shift(63)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_psz_252d_slope_v007_signal(ps):
    base = -_z(ps, 252)
    d1 = base - base.shift(5)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_psz_252d_slope_v008_signal(ps):
    base = -_z(ps, 252)
    d1 = base - base.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_psz_252d_slope_v009_signal(ps):
    base = -_z(ps, 252)
    d1 = base - base.shift(63)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_evebitdaz_252d_slope_v010_signal(evebitda):
    base = -_z(evebitda, 252)
    d1 = base - base.shift(5)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_evebitdaz_252d_slope_v011_signal(evebitda):
    base = -_z(evebitda, 252)
    d1 = base - base.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_evebitdaz_252d_slope_v012_signal(evebitda):
    base = -_z(evebitda, 252)
    d1 = base - base.shift(63)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_evebitz_252d_slope_v013_signal(evebit):
    base = -_z(evebit, 252)
    d1 = base - base.shift(5)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_evebitz_252d_slope_v014_signal(evebit):
    base = -_z(evebit, 252)
    d1 = base - base.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_evebitz_252d_slope_v015_signal(evebit):
    base = -_z(evebit, 252)
    d1 = base - base.shift(63)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_earnyld_252d_slope_v016_signal(netinc, marketcap):
    base = _f39_yield(netinc, marketcap)
    d1 = base - base.shift(5)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_earnyld_252d_slope_v017_signal(netinc, marketcap):
    base = _f39_yield(netinc, marketcap)
    d1 = base - base.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_earnyld_252d_slope_v018_signal(netinc, marketcap):
    base = _f39_yield(netinc, marketcap)
    d1 = base - base.shift(63)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_fcfyld_252d_slope_v019_signal(fcf, marketcap):
    base = _f39_yield(fcf, marketcap)
    d1 = base - base.shift(5)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_fcfyld_252d_slope_v020_signal(fcf, marketcap):
    base = _f39_yield(fcf, marketcap)
    d1 = base - base.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_fcfyld_252d_slope_v021_signal(fcf, marketcap):
    base = _f39_yield(fcf, marketcap)
    d1 = base - base.shift(63)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_bookyld_252d_slope_v022_signal(equity, marketcap):
    base = _f39_yield(equity, marketcap)
    d1 = base - base.shift(5)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_bookyld_252d_slope_v023_signal(equity, marketcap):
    base = _f39_yield(equity, marketcap)
    d1 = base - base.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_bookyld_252d_slope_v024_signal(equity, marketcap):
    base = _f39_yield(equity, marketcap)
    d1 = base - base.shift(63)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_salesyld_252d_slope_v025_signal(revenue, marketcap):
    base = _f39_yield(revenue, marketcap)
    d1 = base - base.shift(5)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_salesyld_252d_slope_v026_signal(revenue, marketcap):
    base = _f39_yield(revenue, marketcap)
    d1 = base - base.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_salesyld_252d_slope_v027_signal(revenue, marketcap):
    base = _f39_yield(revenue, marketcap)
    d1 = base - base.shift(63)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_evfcf_252d_slope_v028_signal(fcf, ev):
    base = _f39_yield(fcf, ev)
    d1 = base - base.shift(5)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_evfcf_252d_slope_v029_signal(fcf, ev):
    base = _f39_yield(fcf, ev)
    d1 = base - base.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_evfcf_252d_slope_v030_signal(fcf, ev):
    base = _f39_yield(fcf, ev)
    d1 = base - base.shift(63)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_evearn_252d_slope_v031_signal(netinc, ev):
    base = _f39_yield(netinc, ev)
    d1 = base - base.shift(5)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_evearn_252d_slope_v032_signal(netinc, ev):
    base = _f39_yield(netinc, ev)
    d1 = base - base.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_evearn_252d_slope_v033_signal(netinc, ev):
    base = _f39_yield(netinc, ev)
    d1 = base - base.shift(63)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_evsales_252d_slope_v034_signal(revenue, ev):
    base = _f39_yield(revenue, ev)
    d1 = base - base.shift(5)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_evsales_252d_slope_v035_signal(revenue, ev):
    base = _f39_yield(revenue, ev)
    d1 = base - base.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_evsales_252d_slope_v036_signal(revenue, ev):
    base = _f39_yield(revenue, ev)
    d1 = base - base.shift(63)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_evbook_252d_slope_v037_signal(equity, ev):
    base = _f39_yield(equity, ev)
    d1 = base - base.shift(5)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_evbook_252d_slope_v038_signal(equity, ev):
    base = _f39_yield(equity, ev)
    d1 = base - base.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_evbook_252d_slope_v039_signal(equity, ev):
    base = _f39_yield(equity, ev)
    d1 = base - base.shift(63)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_peinv_252d_slope_v040_signal(pe):
    base = _f39_inv(pe)
    d1 = base - base.shift(5)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_peinv_252d_slope_v041_signal(pe):
    base = _f39_inv(pe)
    d1 = base - base.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_peinv_252d_slope_v042_signal(pe):
    base = _f39_inv(pe)
    d1 = base - base.shift(63)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_pbinv_252d_slope_v043_signal(pb):
    base = _f39_inv(pb)
    d1 = base - base.shift(5)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_pbinv_252d_slope_v044_signal(pb):
    base = _f39_inv(pb)
    d1 = base - base.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_pbinv_252d_slope_v045_signal(pb):
    base = _f39_inv(pb)
    d1 = base - base.shift(63)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_psinv_252d_slope_v046_signal(ps):
    base = _f39_inv(ps)
    d1 = base - base.shift(5)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_psinv_252d_slope_v047_signal(ps):
    base = _f39_inv(ps)
    d1 = base - base.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_psinv_252d_slope_v048_signal(ps):
    base = _f39_inv(ps)
    d1 = base - base.shift(63)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_evebitdainv_252d_slope_v049_signal(evebitda):
    base = _f39_inv(evebitda)
    d1 = base - base.shift(5)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_evebitdainv_252d_slope_v050_signal(evebitda):
    base = _f39_inv(evebitda)
    d1 = base - base.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_evebitdainv_252d_slope_v051_signal(evebitda):
    base = _f39_inv(evebitda)
    d1 = base - base.shift(63)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_evebitinv_252d_slope_v052_signal(evebit):
    base = _f39_inv(evebit)
    d1 = base - base.shift(5)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_evebitinv_252d_slope_v053_signal(evebit):
    base = _f39_inv(evebit)
    d1 = base - base.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_evebitinv_252d_slope_v054_signal(evebit):
    base = _f39_inv(evebit)
    d1 = base - base.shift(63)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_perng_252d_slope_v055_signal(pe):
    base = _f39_rng_cheap(pe, 252)
    d1 = base - base.shift(5)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_perng_252d_slope_v056_signal(pe):
    base = _f39_rng_cheap(pe, 252)
    d1 = base - base.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_perng_252d_slope_v057_signal(pe):
    base = _f39_rng_cheap(pe, 252)
    d1 = base - base.shift(63)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_pbrng_252d_slope_v058_signal(pb, equity, marketcap):
    base = _z(_f39_yield(equity, marketcap), 252) - _f39_cheap_z(pb, 252)
    d1 = base - base.shift(5)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_pbrng_252d_slope_v059_signal(pb, equity, marketcap):
    base = _z(_f39_yield(equity, marketcap), 252) - _f39_cheap_z(pb, 252)
    d1 = base - base.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_pbrng_252d_slope_v060_signal(pb, equity, marketcap):
    base = _z(_f39_yield(equity, marketcap), 252) - _f39_cheap_z(pb, 252)
    d1 = base - base.shift(63)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_psrng_504d_slope_v061_signal(ps):
    base = _f39_rng_cheap(ps, 504)
    d1 = base - base.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_psrng_504d_slope_v062_signal(ps):
    base = _f39_rng_cheap(ps, 504)
    d1 = base - base.shift(63)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_psrng_504d_slope_v063_signal(ps):
    base = _f39_rng_cheap(ps, 504)
    d1 = base - base.shift(126)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_evebitdarng_504d_slope_v064_signal(evebitda):
    base = _f39_rng_cheap(evebitda, 504)
    d1 = base - base.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_evebitdarng_504d_slope_v065_signal(evebitda):
    base = _f39_rng_cheap(evebitda, 504)
    d1 = base - base.shift(63)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_evebitdarng_504d_slope_v066_signal(evebitda):
    base = _f39_rng_cheap(evebitda, 504)
    d1 = base - base.shift(126)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_totyld_252d_slope_v067_signal(netinc, fcf, marketcap):
    base = (netinc + fcf) / marketcap.replace(0, np.nan)
    d1 = base - base.shift(5)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_totyld_252d_slope_v068_signal(netinc, fcf, marketcap):
    base = (netinc + fcf) / marketcap.replace(0, np.nan)
    d1 = base - base.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_totyld_252d_slope_v069_signal(netinc, fcf, marketcap):
    base = (netinc + fcf) / marketcap.replace(0, np.nan)
    d1 = base - base.shift(63)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_earnfcfgap_252d_slope_v070_signal(netinc, fcf, marketcap):
    base = (fcf - netinc) / marketcap.replace(0, np.nan)
    d1 = base - base.shift(5)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_earnfcfgap_252d_slope_v071_signal(netinc, fcf, marketcap):
    base = (fcf - netinc) / marketcap.replace(0, np.nan)
    d1 = base - base.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_earnfcfgap_252d_slope_v072_signal(netinc, fcf, marketcap):
    base = (fcf - netinc) / marketcap.replace(0, np.nan)
    d1 = base - base.shift(63)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_eyrank_504d_slope_v073_signal(netinc, marketcap):
    base = _rank(_f39_yield(netinc, marketcap), 504)
    d1 = base - base.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_eyrank_504d_slope_v074_signal(netinc, marketcap):
    base = _rank(_f39_yield(netinc, marketcap), 504)
    d1 = base - base.shift(63)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_eyrank_504d_slope_v075_signal(netinc, marketcap):
    base = _rank(_f39_yield(netinc, marketcap), 504)
    d1 = base - base.shift(126)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_fyrank_504d_slope_v076_signal(fcf, marketcap):
    base = _rank(_f39_yield(fcf, marketcap), 504)
    d1 = base - base.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_fyrank_504d_slope_v077_signal(fcf, marketcap):
    base = _rank(_f39_yield(fcf, marketcap), 504)
    d1 = base - base.shift(63)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_fyrank_504d_slope_v078_signal(fcf, marketcap):
    base = _rank(_f39_yield(fcf, marketcap), 504)
    d1 = base - base.shift(126)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_byrank_504d_slope_v079_signal(equity, marketcap):
    base = _rank(_f39_yield(equity, marketcap), 504)
    d1 = base - base.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_byrank_504d_slope_v080_signal(equity, marketcap):
    base = _rank(_f39_yield(equity, marketcap), 504)
    d1 = base - base.shift(63)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_byrank_504d_slope_v081_signal(equity, marketcap):
    base = _rank(_f39_yield(equity, marketcap), 504)
    d1 = base - base.shift(126)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_blend3_252d_slope_v082_signal(pe, pb, ps):
    base = (-_rank(pe, 252) - _rank(pb, 252) - _rank(ps, 252)) / 3.0
    d1 = base - base.shift(5)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_blend3_252d_slope_v083_signal(pe, pb, ps):
    base = (-_rank(pe, 252) - _rank(pb, 252) - _rank(ps, 252)) / 3.0
    d1 = base - base.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_blend3_252d_slope_v084_signal(pe, pb, ps):
    base = (-_rank(pe, 252) - _rank(pb, 252) - _rank(ps, 252)) / 3.0
    d1 = base - base.shift(63)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_blendev_252d_slope_v085_signal(evebitda, evebit):
    base = (-_rank(evebitda, 252) - _rank(evebit, 252)) / 2.0
    d1 = base - base.shift(5)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_blendev_252d_slope_v086_signal(evebitda, evebit):
    base = (-_rank(evebitda, 252) - _rank(evebit, 252)) / 2.0
    d1 = base - base.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_blendev_252d_slope_v087_signal(evebitda, evebit):
    base = (-_rank(evebitda, 252) - _rank(evebit, 252)) / 2.0
    d1 = base - base.shift(63)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_sprpeps_252d_slope_v088_signal(netinc, revenue, marketcap):
    base = _z(_f39_yield(netinc, marketcap), 252) - _z(_f39_yield(revenue, marketcap), 252)
    d1 = base - base.shift(5)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_sprpeps_252d_slope_v089_signal(netinc, revenue, marketcap):
    base = _z(_f39_yield(netinc, marketcap), 252) - _z(_f39_yield(revenue, marketcap), 252)
    d1 = base - base.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_sprpeps_252d_slope_v090_signal(netinc, revenue, marketcap):
    base = _z(_f39_yield(netinc, marketcap), 252) - _z(_f39_yield(revenue, marketcap), 252)
    d1 = base - base.shift(63)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_sprpbev_252d_slope_v091_signal(pb, evebitda):
    base = _f39_inv(pb) - _f39_inv(evebitda)
    d1 = base - base.shift(5)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_sprpbev_252d_slope_v092_signal(pb, evebitda):
    base = _f39_inv(pb) - _f39_inv(evebitda)
    d1 = base - base.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_sprpbev_252d_slope_v093_signal(pb, evebitda):
    base = _f39_inv(pb) - _f39_inv(evebitda)
    d1 = base - base.shift(63)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_evsalesz_252d_slope_v094_signal(ev, revenue):
    base = -_z(_f39_yield(ev, revenue), 252)
    d1 = base - base.shift(5)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_evsalesz_252d_slope_v095_signal(ev, revenue):
    base = -_z(_f39_yield(ev, revenue), 252)
    d1 = base - base.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_evsalesz_252d_slope_v096_signal(ev, revenue):
    base = -_z(_f39_yield(ev, revenue), 252)
    d1 = base - base.shift(63)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_evfcfz_252d_slope_v097_signal(ev, fcf):
    base = -_z(_f39_yield(ev, fcf), 252)
    d1 = base - base.shift(5)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_evfcfz_252d_slope_v098_signal(ev, fcf):
    base = -_z(_f39_yield(ev, fcf), 252)
    d1 = base - base.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_evfcfz_252d_slope_v099_signal(ev, fcf):
    base = -_z(_f39_yield(ev, fcf), 252)
    d1 = base - base.shift(63)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_eylongz_504d_slope_v100_signal(netinc, marketcap):
    base = _z(_f39_yield(netinc, marketcap), 504)
    d1 = base - base.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_eylongz_504d_slope_v101_signal(netinc, marketcap):
    base = _z(_f39_yield(netinc, marketcap), 504)
    d1 = base - base.shift(63)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_eylongz_504d_slope_v102_signal(netinc, marketcap):
    base = _z(_f39_yield(netinc, marketcap), 504)
    d1 = base - base.shift(126)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_fylongz_504d_slope_v103_signal(fcf, marketcap):
    base = _z(_f39_yield(fcf, marketcap), 504)
    d1 = base - base.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_fylongz_504d_slope_v104_signal(fcf, marketcap):
    base = _z(_f39_yield(fcf, marketcap), 504)
    d1 = base - base.shift(63)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_fylongz_504d_slope_v105_signal(fcf, marketcap):
    base = _z(_f39_yield(fcf, marketcap), 504)
    d1 = base - base.shift(126)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_pelog_252d_slope_v106_signal(pe):
    med = pe.rolling(252, min_periods=126).median()
    base = -(np.log(pe.replace(0, np.nan)) - np.log(med.replace(0, np.nan)))
    d1 = base - base.shift(5)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_pelog_252d_slope_v107_signal(pe):
    med = pe.rolling(252, min_periods=126).median()
    base = -(np.log(pe.replace(0, np.nan)) - np.log(med.replace(0, np.nan)))
    d1 = base - base.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_pelog_252d_slope_v108_signal(pe):
    med = pe.rolling(252, min_periods=126).median()
    base = -(np.log(pe.replace(0, np.nan)) - np.log(med.replace(0, np.nan)))
    d1 = base - base.shift(63)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_pslog_252d_slope_v109_signal(ps):
    med = ps.rolling(252, min_periods=126).median()
    base = -(np.log(ps.replace(0, np.nan)) - np.log(med.replace(0, np.nan)))
    d1 = base - base.shift(5)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_pslog_252d_slope_v110_signal(ps):
    med = ps.rolling(252, min_periods=126).median()
    base = -(np.log(ps.replace(0, np.nan)) - np.log(med.replace(0, np.nan)))
    d1 = base - base.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_pslog_252d_slope_v111_signal(ps):
    med = ps.rolling(252, min_periods=126).median()
    base = -(np.log(ps.replace(0, np.nan)) - np.log(med.replace(0, np.nan)))
    d1 = base - base.shift(63)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_evebitdalog_252d_slope_v112_signal(evebitda):
    med = evebitda.rolling(252, min_periods=126).median()
    base = -(np.log(evebitda.replace(0, np.nan)) - np.log(med.replace(0, np.nan)))
    d1 = base - base.shift(5)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_evebitdalog_252d_slope_v113_signal(evebitda):
    med = evebitda.rolling(252, min_periods=126).median()
    base = -(np.log(evebitda.replace(0, np.nan)) - np.log(med.replace(0, np.nan)))
    d1 = base - base.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_evebitdalog_252d_slope_v114_signal(evebitda):
    med = evebitda.rolling(252, min_periods=126).median()
    base = -(np.log(evebitda.replace(0, np.nan)) - np.log(med.replace(0, np.nan)))
    d1 = base - base.shift(63)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_graham_504d_slope_v115_signal(pe, pb):
    gp = 1.0 / (pe * pb).replace(0, np.nan)
    base = _rank(gp, 504)
    d1 = base - base.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_graham_504d_slope_v116_signal(pe, pb):
    gp = 1.0 / (pe * pb).replace(0, np.nan)
    base = _rank(gp, 504)
    d1 = base - base.shift(63)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_graham_504d_slope_v117_signal(pe, pb):
    gp = 1.0 / (pe * pb).replace(0, np.nan)
    base = _rank(gp, 504)
    d1 = base - base.shift(126)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_grahamz_252d_slope_v118_signal(pe, pb):
    gp = 1.0 / (pe * pb).replace(0, np.nan)
    base = _z(gp, 252)
    d1 = base - base.shift(5)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_grahamz_252d_slope_v119_signal(pe, pb):
    gp = 1.0 / (pe * pb).replace(0, np.nan)
    base = _z(gp, 252)
    d1 = base - base.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_grahamz_252d_slope_v120_signal(pe, pb):
    gp = 1.0 / (pe * pb).replace(0, np.nan)
    base = _z(gp, 252)
    d1 = base - base.shift(63)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_evtotyld_252d_slope_v121_signal(netinc, fcf, ev):
    base = (netinc + fcf) / ev.replace(0, np.nan)
    d1 = base - base.shift(5)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_evtotyld_252d_slope_v122_signal(netinc, fcf, ev):
    base = (netinc + fcf) / ev.replace(0, np.nan)
    d1 = base - base.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_evtotyld_252d_slope_v123_signal(netinc, fcf, ev):
    base = (netinc + fcf) / ev.replace(0, np.nan)
    d1 = base - base.shift(63)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_capgap_252d_slope_v124_signal(netinc, marketcap, ev):
    base = _f39_yield(netinc, marketcap) - _f39_yield(netinc, ev)
    d1 = base - base.shift(5)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_capgap_252d_slope_v125_signal(netinc, marketcap, ev):
    base = _f39_yield(netinc, marketcap) - _f39_yield(netinc, ev)
    d1 = base - base.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_capgap_252d_slope_v126_signal(netinc, marketcap, ev):
    base = _f39_yield(netinc, marketcap) - _f39_yield(netinc, ev)
    d1 = base - base.shift(63)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_fcfcapgap_252d_slope_v127_signal(fcf, marketcap, ev):
    base = _f39_yield(fcf, marketcap) - _f39_yield(fcf, ev)
    d1 = base - base.shift(5)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_fcfcapgap_252d_slope_v128_signal(fcf, marketcap, ev):
    base = _f39_yield(fcf, marketcap) - _f39_yield(fcf, ev)
    d1 = base - base.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_fcfcapgap_252d_slope_v129_signal(fcf, marketcap, ev):
    base = _f39_yield(fcf, marketcap) - _f39_yield(fcf, ev)
    d1 = base - base.shift(63)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_salesevz_252d_slope_v130_signal(equity, revenue, ev):
    base = _z(_f39_yield(equity, ev), 252) - _z(_f39_yield(revenue, ev), 252)
    d1 = base - base.shift(5)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_salesevz_252d_slope_v131_signal(equity, revenue, ev):
    base = _z(_f39_yield(equity, ev), 252) - _z(_f39_yield(revenue, ev), 252)
    d1 = base - base.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_salesevz_252d_slope_v132_signal(equity, revenue, ev):
    base = _z(_f39_yield(equity, ev), 252) - _z(_f39_yield(revenue, ev), 252)
    d1 = base - base.shift(63)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_eqcapz_126d_slope_v133_signal(equity, marketcap):
    base = _z(_f39_yield(equity, marketcap), 126)
    d1 = base - base.shift(5)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_eqcapz_126d_slope_v134_signal(equity, marketcap):
    base = _z(_f39_yield(equity, marketcap), 126)
    d1 = base - base.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_eqcapz_126d_slope_v135_signal(equity, marketcap):
    base = _z(_f39_yield(equity, marketcap), 126)
    d1 = base - base.shift(63)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_pe5yr_1260d_slope_v136_signal(pe):
    lo = _rmin(pe, 1260)
    hi = _rmax(pe, 1260)
    base = (hi - pe) / (hi - lo).replace(0, np.nan)
    d1 = base - base.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_pe5yr_1260d_slope_v137_signal(pe):
    lo = _rmin(pe, 1260)
    hi = _rmax(pe, 1260)
    base = (hi - pe) / (hi - lo).replace(0, np.nan)
    d1 = base - base.shift(63)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_pe5yr_1260d_slope_v138_signal(pe):
    lo = _rmin(pe, 1260)
    hi = _rmax(pe, 1260)
    base = (hi - pe) / (hi - lo).replace(0, np.nan)
    d1 = base - base.shift(126)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_evebitda5yr_1260d_slope_v139_signal(netinc, ev):
    base = _rank(_f39_yield(netinc, ev), 1260)
    d1 = base - base.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_evebitda5yr_1260d_slope_v140_signal(netinc, ev):
    base = _rank(_f39_yield(netinc, ev), 1260)
    d1 = base - base.shift(63)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_evebitda5yr_1260d_slope_v141_signal(netinc, ev):
    base = _rank(_f39_yield(netinc, ev), 1260)
    d1 = base - base.shift(126)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_eqevlog_504d_slope_v142_signal(marketcap, ev):
    lev = np.log(ev.replace(0, np.nan) / marketcap.replace(0, np.nan))
    base = -_rank(lev, 504)
    d1 = base - base.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_eqevlog_504d_slope_v143_signal(marketcap, ev):
    lev = np.log(ev.replace(0, np.nan) / marketcap.replace(0, np.nan))
    base = -_rank(lev, 504)
    d1 = base - base.shift(63)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_eqevlog_504d_slope_v144_signal(marketcap, ev):
    lev = np.log(ev.replace(0, np.nan) / marketcap.replace(0, np.nan))
    base = -_rank(lev, 504)
    d1 = base - base.shift(126)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_revcapz_504d_slope_v145_signal(revenue, marketcap):
    base = _z(_f39_yield(revenue, marketcap), 504)
    d1 = base - base.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_revcapz_504d_slope_v146_signal(revenue, marketcap):
    base = _z(_f39_yield(revenue, marketcap), 504)
    d1 = base - base.shift(63)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_revcapz_504d_slope_v147_signal(revenue, marketcap):
    base = _z(_f39_yield(revenue, marketcap), 504)
    d1 = base - base.shift(126)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_evinvmean_252d_slope_v148_signal(evebitda, evebit):
    base = (_f39_inv(evebitda) + _f39_inv(evebit)) / 2.0
    d1 = base - base.shift(5)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_evinvmean_252d_slope_v149_signal(evebitda, evebit):
    base = (_f39_inv(evebitda) + _f39_inv(evebit)) / 2.0
    d1 = base - base.shift(21)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


def f39ve_f39_valuation_entry_evinvmean_252d_slope_v150_signal(evebitda, evebit):
    base = (_f39_inv(evebitda) + _f39_inv(evebit)) / 2.0
    d1 = base - base.shift(63)
    result = d1
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f39ve_f39_valuation_entry_pez_252d_slope_v001_signal,
    f39ve_f39_valuation_entry_pez_252d_slope_v002_signal,
    f39ve_f39_valuation_entry_pez_252d_slope_v003_signal,
    f39ve_f39_valuation_entry_pbz_252d_slope_v004_signal,
    f39ve_f39_valuation_entry_pbz_252d_slope_v005_signal,
    f39ve_f39_valuation_entry_pbz_252d_slope_v006_signal,
    f39ve_f39_valuation_entry_psz_252d_slope_v007_signal,
    f39ve_f39_valuation_entry_psz_252d_slope_v008_signal,
    f39ve_f39_valuation_entry_psz_252d_slope_v009_signal,
    f39ve_f39_valuation_entry_evebitdaz_252d_slope_v010_signal,
    f39ve_f39_valuation_entry_evebitdaz_252d_slope_v011_signal,
    f39ve_f39_valuation_entry_evebitdaz_252d_slope_v012_signal,
    f39ve_f39_valuation_entry_evebitz_252d_slope_v013_signal,
    f39ve_f39_valuation_entry_evebitz_252d_slope_v014_signal,
    f39ve_f39_valuation_entry_evebitz_252d_slope_v015_signal,
    f39ve_f39_valuation_entry_earnyld_252d_slope_v016_signal,
    f39ve_f39_valuation_entry_earnyld_252d_slope_v017_signal,
    f39ve_f39_valuation_entry_earnyld_252d_slope_v018_signal,
    f39ve_f39_valuation_entry_fcfyld_252d_slope_v019_signal,
    f39ve_f39_valuation_entry_fcfyld_252d_slope_v020_signal,
    f39ve_f39_valuation_entry_fcfyld_252d_slope_v021_signal,
    f39ve_f39_valuation_entry_bookyld_252d_slope_v022_signal,
    f39ve_f39_valuation_entry_bookyld_252d_slope_v023_signal,
    f39ve_f39_valuation_entry_bookyld_252d_slope_v024_signal,
    f39ve_f39_valuation_entry_salesyld_252d_slope_v025_signal,
    f39ve_f39_valuation_entry_salesyld_252d_slope_v026_signal,
    f39ve_f39_valuation_entry_salesyld_252d_slope_v027_signal,
    f39ve_f39_valuation_entry_evfcf_252d_slope_v028_signal,
    f39ve_f39_valuation_entry_evfcf_252d_slope_v029_signal,
    f39ve_f39_valuation_entry_evfcf_252d_slope_v030_signal,
    f39ve_f39_valuation_entry_evearn_252d_slope_v031_signal,
    f39ve_f39_valuation_entry_evearn_252d_slope_v032_signal,
    f39ve_f39_valuation_entry_evearn_252d_slope_v033_signal,
    f39ve_f39_valuation_entry_evsales_252d_slope_v034_signal,
    f39ve_f39_valuation_entry_evsales_252d_slope_v035_signal,
    f39ve_f39_valuation_entry_evsales_252d_slope_v036_signal,
    f39ve_f39_valuation_entry_evbook_252d_slope_v037_signal,
    f39ve_f39_valuation_entry_evbook_252d_slope_v038_signal,
    f39ve_f39_valuation_entry_evbook_252d_slope_v039_signal,
    f39ve_f39_valuation_entry_peinv_252d_slope_v040_signal,
    f39ve_f39_valuation_entry_peinv_252d_slope_v041_signal,
    f39ve_f39_valuation_entry_peinv_252d_slope_v042_signal,
    f39ve_f39_valuation_entry_pbinv_252d_slope_v043_signal,
    f39ve_f39_valuation_entry_pbinv_252d_slope_v044_signal,
    f39ve_f39_valuation_entry_pbinv_252d_slope_v045_signal,
    f39ve_f39_valuation_entry_psinv_252d_slope_v046_signal,
    f39ve_f39_valuation_entry_psinv_252d_slope_v047_signal,
    f39ve_f39_valuation_entry_psinv_252d_slope_v048_signal,
    f39ve_f39_valuation_entry_evebitdainv_252d_slope_v049_signal,
    f39ve_f39_valuation_entry_evebitdainv_252d_slope_v050_signal,
    f39ve_f39_valuation_entry_evebitdainv_252d_slope_v051_signal,
    f39ve_f39_valuation_entry_evebitinv_252d_slope_v052_signal,
    f39ve_f39_valuation_entry_evebitinv_252d_slope_v053_signal,
    f39ve_f39_valuation_entry_evebitinv_252d_slope_v054_signal,
    f39ve_f39_valuation_entry_perng_252d_slope_v055_signal,
    f39ve_f39_valuation_entry_perng_252d_slope_v056_signal,
    f39ve_f39_valuation_entry_perng_252d_slope_v057_signal,
    f39ve_f39_valuation_entry_pbrng_252d_slope_v058_signal,
    f39ve_f39_valuation_entry_pbrng_252d_slope_v059_signal,
    f39ve_f39_valuation_entry_pbrng_252d_slope_v060_signal,
    f39ve_f39_valuation_entry_psrng_504d_slope_v061_signal,
    f39ve_f39_valuation_entry_psrng_504d_slope_v062_signal,
    f39ve_f39_valuation_entry_psrng_504d_slope_v063_signal,
    f39ve_f39_valuation_entry_evebitdarng_504d_slope_v064_signal,
    f39ve_f39_valuation_entry_evebitdarng_504d_slope_v065_signal,
    f39ve_f39_valuation_entry_evebitdarng_504d_slope_v066_signal,
    f39ve_f39_valuation_entry_totyld_252d_slope_v067_signal,
    f39ve_f39_valuation_entry_totyld_252d_slope_v068_signal,
    f39ve_f39_valuation_entry_totyld_252d_slope_v069_signal,
    f39ve_f39_valuation_entry_earnfcfgap_252d_slope_v070_signal,
    f39ve_f39_valuation_entry_earnfcfgap_252d_slope_v071_signal,
    f39ve_f39_valuation_entry_earnfcfgap_252d_slope_v072_signal,
    f39ve_f39_valuation_entry_eyrank_504d_slope_v073_signal,
    f39ve_f39_valuation_entry_eyrank_504d_slope_v074_signal,
    f39ve_f39_valuation_entry_eyrank_504d_slope_v075_signal,
    f39ve_f39_valuation_entry_fyrank_504d_slope_v076_signal,
    f39ve_f39_valuation_entry_fyrank_504d_slope_v077_signal,
    f39ve_f39_valuation_entry_fyrank_504d_slope_v078_signal,
    f39ve_f39_valuation_entry_byrank_504d_slope_v079_signal,
    f39ve_f39_valuation_entry_byrank_504d_slope_v080_signal,
    f39ve_f39_valuation_entry_byrank_504d_slope_v081_signal,
    f39ve_f39_valuation_entry_blend3_252d_slope_v082_signal,
    f39ve_f39_valuation_entry_blend3_252d_slope_v083_signal,
    f39ve_f39_valuation_entry_blend3_252d_slope_v084_signal,
    f39ve_f39_valuation_entry_blendev_252d_slope_v085_signal,
    f39ve_f39_valuation_entry_blendev_252d_slope_v086_signal,
    f39ve_f39_valuation_entry_blendev_252d_slope_v087_signal,
    f39ve_f39_valuation_entry_sprpeps_252d_slope_v088_signal,
    f39ve_f39_valuation_entry_sprpeps_252d_slope_v089_signal,
    f39ve_f39_valuation_entry_sprpeps_252d_slope_v090_signal,
    f39ve_f39_valuation_entry_sprpbev_252d_slope_v091_signal,
    f39ve_f39_valuation_entry_sprpbev_252d_slope_v092_signal,
    f39ve_f39_valuation_entry_sprpbev_252d_slope_v093_signal,
    f39ve_f39_valuation_entry_evsalesz_252d_slope_v094_signal,
    f39ve_f39_valuation_entry_evsalesz_252d_slope_v095_signal,
    f39ve_f39_valuation_entry_evsalesz_252d_slope_v096_signal,
    f39ve_f39_valuation_entry_evfcfz_252d_slope_v097_signal,
    f39ve_f39_valuation_entry_evfcfz_252d_slope_v098_signal,
    f39ve_f39_valuation_entry_evfcfz_252d_slope_v099_signal,
    f39ve_f39_valuation_entry_eylongz_504d_slope_v100_signal,
    f39ve_f39_valuation_entry_eylongz_504d_slope_v101_signal,
    f39ve_f39_valuation_entry_eylongz_504d_slope_v102_signal,
    f39ve_f39_valuation_entry_fylongz_504d_slope_v103_signal,
    f39ve_f39_valuation_entry_fylongz_504d_slope_v104_signal,
    f39ve_f39_valuation_entry_fylongz_504d_slope_v105_signal,
    f39ve_f39_valuation_entry_pelog_252d_slope_v106_signal,
    f39ve_f39_valuation_entry_pelog_252d_slope_v107_signal,
    f39ve_f39_valuation_entry_pelog_252d_slope_v108_signal,
    f39ve_f39_valuation_entry_pslog_252d_slope_v109_signal,
    f39ve_f39_valuation_entry_pslog_252d_slope_v110_signal,
    f39ve_f39_valuation_entry_pslog_252d_slope_v111_signal,
    f39ve_f39_valuation_entry_evebitdalog_252d_slope_v112_signal,
    f39ve_f39_valuation_entry_evebitdalog_252d_slope_v113_signal,
    f39ve_f39_valuation_entry_evebitdalog_252d_slope_v114_signal,
    f39ve_f39_valuation_entry_graham_504d_slope_v115_signal,
    f39ve_f39_valuation_entry_graham_504d_slope_v116_signal,
    f39ve_f39_valuation_entry_graham_504d_slope_v117_signal,
    f39ve_f39_valuation_entry_grahamz_252d_slope_v118_signal,
    f39ve_f39_valuation_entry_grahamz_252d_slope_v119_signal,
    f39ve_f39_valuation_entry_grahamz_252d_slope_v120_signal,
    f39ve_f39_valuation_entry_evtotyld_252d_slope_v121_signal,
    f39ve_f39_valuation_entry_evtotyld_252d_slope_v122_signal,
    f39ve_f39_valuation_entry_evtotyld_252d_slope_v123_signal,
    f39ve_f39_valuation_entry_capgap_252d_slope_v124_signal,
    f39ve_f39_valuation_entry_capgap_252d_slope_v125_signal,
    f39ve_f39_valuation_entry_capgap_252d_slope_v126_signal,
    f39ve_f39_valuation_entry_fcfcapgap_252d_slope_v127_signal,
    f39ve_f39_valuation_entry_fcfcapgap_252d_slope_v128_signal,
    f39ve_f39_valuation_entry_fcfcapgap_252d_slope_v129_signal,
    f39ve_f39_valuation_entry_salesevz_252d_slope_v130_signal,
    f39ve_f39_valuation_entry_salesevz_252d_slope_v131_signal,
    f39ve_f39_valuation_entry_salesevz_252d_slope_v132_signal,
    f39ve_f39_valuation_entry_eqcapz_126d_slope_v133_signal,
    f39ve_f39_valuation_entry_eqcapz_126d_slope_v134_signal,
    f39ve_f39_valuation_entry_eqcapz_126d_slope_v135_signal,
    f39ve_f39_valuation_entry_pe5yr_1260d_slope_v136_signal,
    f39ve_f39_valuation_entry_pe5yr_1260d_slope_v137_signal,
    f39ve_f39_valuation_entry_pe5yr_1260d_slope_v138_signal,
    f39ve_f39_valuation_entry_evebitda5yr_1260d_slope_v139_signal,
    f39ve_f39_valuation_entry_evebitda5yr_1260d_slope_v140_signal,
    f39ve_f39_valuation_entry_evebitda5yr_1260d_slope_v141_signal,
    f39ve_f39_valuation_entry_eqevlog_504d_slope_v142_signal,
    f39ve_f39_valuation_entry_eqevlog_504d_slope_v143_signal,
    f39ve_f39_valuation_entry_eqevlog_504d_slope_v144_signal,
    f39ve_f39_valuation_entry_revcapz_504d_slope_v145_signal,
    f39ve_f39_valuation_entry_revcapz_504d_slope_v146_signal,
    f39ve_f39_valuation_entry_revcapz_504d_slope_v147_signal,
    f39ve_f39_valuation_entry_evinvmean_252d_slope_v148_signal,
    f39ve_f39_valuation_entry_evinvmean_252d_slope_v149_signal,
    f39ve_f39_valuation_entry_evinvmean_252d_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F39_VALUATION_ENTRY_REGISTRY_SLOPE_001_150 = REGISTRY


def _build_inputs():
    np.random.seed(42)
    n = 1500

    def _fund(seed, base=1e8, drift=0.02, vol=0.05, allow_neg=False):
        g = np.random.default_rng(seed)
        steps = np.repeat(g.normal(drift, vol, n // 63 + 1), 63)[:n]
        s = base * np.exp(np.cumsum(steps / 63))
        if allow_neg:
            s = s - base * 0.3
        return pd.Series(s, name=None)

    pe = _fund(1, base=18.0, drift=0.01, vol=0.06).rename("pe")
    pb = _fund(2, base=3.0, drift=0.01, vol=0.07).rename("pb")
    ps = _fund(3, base=4.0, drift=0.01, vol=0.06).rename("ps")
    evebit = _fund(4, base=16.0, drift=0.01, vol=0.06).rename("evebit")
    evebitda = _fund(5, base=11.0, drift=0.01, vol=0.06).rename("evebitda")
    marketcap = _fund(6, base=5e9, drift=0.02, vol=0.05).rename("marketcap")
    ev = _fund(7, base=6e9, drift=0.02, vol=0.05).rename("ev")
    revenue = _fund(8, base=2e9, drift=0.02, vol=0.05).rename("revenue")
    equity = _fund(9, base=3e9, drift=0.02, vol=0.05).rename("equity")
    netinc = _fund(10, base=4e8, drift=0.015, vol=0.08, allow_neg=True).rename("netinc")
    fcf = _fund(11, base=3.5e8, drift=0.015, vol=0.09, allow_neg=True).rename("fcf")

    return {"pe": pe, "pb": pb, "ps": ps, "ev": ev, "evebit": evebit,
            "evebitda": evebitda, "marketcap": marketcap, "fcf": fcf,
            "netinc": netinc, "revenue": revenue, "equity": equity}


if __name__ == "__main__":
    cols = _build_inputs()

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
        assert q.nunique() > 50, "%s_nun" % (name,)
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

    print("OK f39_valuation_entry_2nd_derivatives_001_150_claude: %d features pass" % n_features)
