import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
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


def _diff(s, n):
    return s.diff(periods=n)


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


# ===== folder domain primitives =====
def _f15_valuation_level(numerator, denominator, w):
    n = _mean(numerator, w)
    d = _mean(denominator, w)
    return n / d.replace(0, np.nan).abs()


def _f15_pe_level(netinc, marketcap, w):
    e = _mean(netinc, w)
    return marketcap / e.replace(0, np.nan).abs()


def _f15_ev_multiple(ev, fund, w):
    f = _mean(fund, w)
    return ev / f.replace(0, np.nan).abs()


# 21d PE level on netinc and marketcap
def f15ve_f15_valuation_at_entry_pelevel_21d_base_v001_signal(netinc, marketcap):
    result = _f15_pe_level(netinc, marketcap, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d PE level
def f15ve_f15_valuation_at_entry_pelevel_63d_base_v002_signal(netinc, marketcap):
    result = _f15_pe_level(netinc, marketcap, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d PE level
def f15ve_f15_valuation_at_entry_pelevel_126d_base_v003_signal(netinc, marketcap):
    result = _f15_pe_level(netinc, marketcap, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d PE level
def f15ve_f15_valuation_at_entry_pelevel_252d_base_v004_signal(netinc, marketcap):
    result = _f15_pe_level(netinc, marketcap, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d PE level
def f15ve_f15_valuation_at_entry_pelevel_504d_base_v005_signal(netinc, marketcap):
    result = _f15_pe_level(netinc, marketcap, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# pe column smoothed 21d, scaled by marketcap
def f15ve_f15_valuation_at_entry_peraw_21d_base_v006_signal(pe, marketcap):
    result = _f15_valuation_level(pe * marketcap, marketcap, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# pe column smoothed 63d, scaled by marketcap
def f15ve_f15_valuation_at_entry_peraw_63d_base_v007_signal(pe, marketcap):
    result = _f15_valuation_level(pe * marketcap, marketcap, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# pe column smoothed 252d, scaled by marketcap
def f15ve_f15_valuation_at_entry_peraw_252d_base_v008_signal(pe, marketcap):
    result = _f15_valuation_level(pe * marketcap, marketcap, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d PB level
def f15ve_f15_valuation_at_entry_pblevel_21d_base_v009_signal(equity, marketcap):
    result = _f15_valuation_level(marketcap, equity, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d PB level
def f15ve_f15_valuation_at_entry_pblevel_63d_base_v010_signal(equity, marketcap):
    result = _f15_valuation_level(marketcap, equity, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d PB level
def f15ve_f15_valuation_at_entry_pblevel_252d_base_v011_signal(equity, marketcap):
    result = _f15_valuation_level(marketcap, equity, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d PB level
def f15ve_f15_valuation_at_entry_pblevel_504d_base_v012_signal(equity, marketcap):
    result = _f15_valuation_level(marketcap, equity, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# pb column smoothed
def f15ve_f15_valuation_at_entry_pbraw_63d_base_v013_signal(pb, marketcap):
    result = _f15_valuation_level(pb * marketcap, marketcap, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# pb column smoothed
def f15ve_f15_valuation_at_entry_pbraw_252d_base_v014_signal(pb, marketcap):
    result = _f15_valuation_level(pb * marketcap, marketcap, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d PS level
def f15ve_f15_valuation_at_entry_pslevel_21d_base_v015_signal(revenue, marketcap):
    result = _f15_valuation_level(marketcap, revenue, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d PS level
def f15ve_f15_valuation_at_entry_pslevel_63d_base_v016_signal(revenue, marketcap):
    result = _f15_valuation_level(marketcap, revenue, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d PS level
def f15ve_f15_valuation_at_entry_pslevel_252d_base_v017_signal(revenue, marketcap):
    result = _f15_valuation_level(marketcap, revenue, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d PS level
def f15ve_f15_valuation_at_entry_pslevel_504d_base_v018_signal(revenue, marketcap):
    result = _f15_valuation_level(marketcap, revenue, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# ps column smoothed
def f15ve_f15_valuation_at_entry_psraw_63d_base_v019_signal(ps, marketcap):
    result = _f15_valuation_level(ps * marketcap, marketcap, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# ps column smoothed
def f15ve_f15_valuation_at_entry_psraw_252d_base_v020_signal(ps, marketcap):
    result = _f15_valuation_level(ps * marketcap, marketcap, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d EV/EBITDA multiple
def f15ve_f15_valuation_at_entry_evebitdalevel_21d_base_v021_signal(ev, ebitda):
    result = _f15_ev_multiple(ev, ebitda, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d EV/EBITDA multiple
def f15ve_f15_valuation_at_entry_evebitdalevel_63d_base_v022_signal(ev, ebitda):
    result = _f15_ev_multiple(ev, ebitda, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d EV/EBITDA multiple
def f15ve_f15_valuation_at_entry_evebitdalevel_252d_base_v023_signal(ev, ebitda):
    result = _f15_ev_multiple(ev, ebitda, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d EV/EBITDA multiple
def f15ve_f15_valuation_at_entry_evebitdalevel_504d_base_v024_signal(ev, ebitda):
    result = _f15_ev_multiple(ev, ebitda, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# evebitda column smoothed
def f15ve_f15_valuation_at_entry_evebitdaraw_63d_base_v025_signal(evebitda, ev):
    result = _f15_valuation_level(evebitda * ev, ev, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# evebitda column smoothed 252d
def f15ve_f15_valuation_at_entry_evebitdaraw_252d_base_v026_signal(evebitda, ev):
    result = _f15_valuation_level(evebitda * ev, ev, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d EV/EBIT (uses opinc as ebit proxy)
def f15ve_f15_valuation_at_entry_evebitlevel_21d_base_v027_signal(ev, opinc):
    result = _f15_ev_multiple(ev, opinc, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d EV/EBIT
def f15ve_f15_valuation_at_entry_evebitlevel_63d_base_v028_signal(ev, opinc):
    result = _f15_ev_multiple(ev, opinc, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d EV/EBIT
def f15ve_f15_valuation_at_entry_evebitlevel_252d_base_v029_signal(ev, opinc):
    result = _f15_ev_multiple(ev, opinc, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d EV/EBIT
def f15ve_f15_valuation_at_entry_evebitlevel_504d_base_v030_signal(ev, opinc):
    result = _f15_ev_multiple(ev, opinc, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# evebit column smoothed
def f15ve_f15_valuation_at_entry_evebitraw_63d_base_v031_signal(evebit, ev):
    result = _f15_valuation_level(evebit * ev, ev, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# evebit column smoothed 252d
def f15ve_f15_valuation_at_entry_evebitraw_252d_base_v032_signal(evebit, ev):
    result = _f15_valuation_level(evebit * ev, ev, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d EV / revenue
def f15ve_f15_valuation_at_entry_evrev_21d_base_v033_signal(ev, revenue):
    result = _f15_ev_multiple(ev, revenue, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d EV / revenue
def f15ve_f15_valuation_at_entry_evrev_63d_base_v034_signal(ev, revenue):
    result = _f15_ev_multiple(ev, revenue, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d EV / revenue
def f15ve_f15_valuation_at_entry_evrev_252d_base_v035_signal(ev, revenue):
    result = _f15_ev_multiple(ev, revenue, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d EV / revenue
def f15ve_f15_valuation_at_entry_evrev_504d_base_v036_signal(ev, revenue):
    result = _f15_ev_multiple(ev, revenue, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d EV / fcf
def f15ve_f15_valuation_at_entry_evfcf_21d_base_v037_signal(ev, fcf):
    result = _f15_ev_multiple(ev, fcf, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d EV / fcf
def f15ve_f15_valuation_at_entry_evfcf_63d_base_v038_signal(ev, fcf):
    result = _f15_ev_multiple(ev, fcf, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d EV / fcf
def f15ve_f15_valuation_at_entry_evfcf_252d_base_v039_signal(ev, fcf):
    result = _f15_ev_multiple(ev, fcf, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d EV / fcf
def f15ve_f15_valuation_at_entry_evfcf_504d_base_v040_signal(ev, fcf):
    result = _f15_ev_multiple(ev, fcf, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d EV / ncfo
def f15ve_f15_valuation_at_entry_evncfo_21d_base_v041_signal(ev, ncfo):
    result = _f15_ev_multiple(ev, ncfo, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d EV / ncfo
def f15ve_f15_valuation_at_entry_evncfo_63d_base_v042_signal(ev, ncfo):
    result = _f15_ev_multiple(ev, ncfo, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d EV / ncfo
def f15ve_f15_valuation_at_entry_evncfo_252d_base_v043_signal(ev, ncfo):
    result = _f15_ev_multiple(ev, ncfo, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d EV / ncfo
def f15ve_f15_valuation_at_entry_evncfo_504d_base_v044_signal(ev, ncfo):
    result = _f15_ev_multiple(ev, ncfo, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d EV / gp (gross profit yield)
def f15ve_f15_valuation_at_entry_evgp_21d_base_v045_signal(ev, gp):
    result = _f15_ev_multiple(ev, gp, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d EV / gp
def f15ve_f15_valuation_at_entry_evgp_63d_base_v046_signal(ev, gp):
    result = _f15_ev_multiple(ev, gp, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d EV / gp
def f15ve_f15_valuation_at_entry_evgp_252d_base_v047_signal(ev, gp):
    result = _f15_ev_multiple(ev, gp, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d marketcap / fcf (P/FCF)
def f15ve_f15_valuation_at_entry_pfcf_21d_base_v048_signal(fcf, marketcap):
    result = _f15_valuation_level(marketcap, fcf, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d marketcap / fcf
def f15ve_f15_valuation_at_entry_pfcf_63d_base_v049_signal(fcf, marketcap):
    result = _f15_valuation_level(marketcap, fcf, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d marketcap / fcf
def f15ve_f15_valuation_at_entry_pfcf_252d_base_v050_signal(fcf, marketcap):
    result = _f15_valuation_level(marketcap, fcf, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d marketcap / fcf
def f15ve_f15_valuation_at_entry_pfcf_504d_base_v051_signal(fcf, marketcap):
    result = _f15_valuation_level(marketcap, fcf, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d marketcap / ncfo
def f15ve_f15_valuation_at_entry_pncfo_21d_base_v052_signal(ncfo, marketcap):
    result = _f15_valuation_level(marketcap, ncfo, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d marketcap / ncfo
def f15ve_f15_valuation_at_entry_pncfo_63d_base_v053_signal(ncfo, marketcap):
    result = _f15_valuation_level(marketcap, ncfo, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d marketcap / ncfo
def f15ve_f15_valuation_at_entry_pncfo_252d_base_v054_signal(ncfo, marketcap):
    result = _f15_valuation_level(marketcap, ncfo, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d marketcap / gp
def f15ve_f15_valuation_at_entry_pgp_21d_base_v055_signal(gp, marketcap):
    result = _f15_valuation_level(marketcap, gp, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d marketcap / gp
def f15ve_f15_valuation_at_entry_pgp_63d_base_v056_signal(gp, marketcap):
    result = _f15_valuation_level(marketcap, gp, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d marketcap / gp
def f15ve_f15_valuation_at_entry_pgp_252d_base_v057_signal(gp, marketcap):
    result = _f15_valuation_level(marketcap, gp, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d marketcap / gp
def f15ve_f15_valuation_at_entry_pgp_504d_base_v058_signal(gp, marketcap):
    result = _f15_valuation_level(marketcap, gp, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d marketcap / opinc (P/EBIT)
def f15ve_f15_valuation_at_entry_popinc_21d_base_v059_signal(opinc, marketcap):
    result = _f15_valuation_level(marketcap, opinc, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d marketcap / opinc
def f15ve_f15_valuation_at_entry_popinc_63d_base_v060_signal(opinc, marketcap):
    result = _f15_valuation_level(marketcap, opinc, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d marketcap / opinc
def f15ve_f15_valuation_at_entry_popinc_252d_base_v061_signal(opinc, marketcap):
    result = _f15_valuation_level(marketcap, opinc, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d marketcap / opinc
def f15ve_f15_valuation_at_entry_popinc_504d_base_v062_signal(opinc, marketcap):
    result = _f15_valuation_level(marketcap, opinc, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d earnings yield (1/PE) times marketcap
def f15ve_f15_valuation_at_entry_eyield_21d_base_v063_signal(netinc, marketcap):
    inv = _f15_pe_level(netinc, marketcap, 21)
    result = marketcap / inv.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d earnings yield x marketcap
def f15ve_f15_valuation_at_entry_eyield_63d_base_v064_signal(netinc, marketcap):
    inv = _f15_pe_level(netinc, marketcap, 63)
    result = marketcap / inv.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d earnings yield x marketcap
def f15ve_f15_valuation_at_entry_eyield_252d_base_v065_signal(netinc, marketcap):
    inv = _f15_pe_level(netinc, marketcap, 252)
    result = marketcap / inv.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d sales yield (rev/marketcap) times marketcap
def f15ve_f15_valuation_at_entry_syield_21d_base_v066_signal(revenue, marketcap):
    inv = _f15_valuation_level(marketcap, revenue, 21)
    result = marketcap / inv.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sales yield x marketcap
def f15ve_f15_valuation_at_entry_syield_252d_base_v067_signal(revenue, marketcap):
    inv = _f15_valuation_level(marketcap, revenue, 252)
    result = marketcap / inv.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d FCF yield x marketcap
def f15ve_f15_valuation_at_entry_fcfyield_21d_base_v068_signal(fcf, marketcap):
    inv = _f15_valuation_level(marketcap, fcf, 21)
    result = marketcap / inv.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d FCF yield x marketcap
def f15ve_f15_valuation_at_entry_fcfyield_252d_base_v069_signal(fcf, marketcap):
    inv = _f15_valuation_level(marketcap, fcf, 252)
    result = marketcap / inv.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d EBITDA yield x ev
def f15ve_f15_valuation_at_entry_ebitdayield_21d_base_v070_signal(ebitda, ev):
    inv = _f15_ev_multiple(ev, ebitda, 21)
    result = ev / inv.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d EBITDA yield x ev
def f15ve_f15_valuation_at_entry_ebitdayield_252d_base_v071_signal(ebitda, ev):
    inv = _f15_ev_multiple(ev, ebitda, 252)
    result = ev / inv.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d PE level x current marketcap (capitalised)
def f15ve_f15_valuation_at_entry_pelevelxmcap_63d_base_v072_signal(netinc, marketcap):
    p = _f15_pe_level(netinc, marketcap, 63)
    result = p * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d PB level x current marketcap
def f15ve_f15_valuation_at_entry_pblevelxmcap_252d_base_v073_signal(equity, marketcap):
    p = _f15_valuation_level(marketcap, equity, 252)
    result = p * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d EV/EBITDA x ev (capitalised)
def f15ve_f15_valuation_at_entry_evebitdaxev_252d_base_v074_signal(ev, ebitda):
    p = _f15_ev_multiple(ev, ebitda, 252)
    result = p * ev / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d PS x marketcap
def f15ve_f15_valuation_at_entry_psxmcap_252d_base_v075_signal(revenue, marketcap):
    p = _f15_valuation_level(marketcap, revenue, 252)
    result = p * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f15ve_f15_valuation_at_entry_pelevel_21d_base_v001_signal,
    f15ve_f15_valuation_at_entry_pelevel_63d_base_v002_signal,
    f15ve_f15_valuation_at_entry_pelevel_126d_base_v003_signal,
    f15ve_f15_valuation_at_entry_pelevel_252d_base_v004_signal,
    f15ve_f15_valuation_at_entry_pelevel_504d_base_v005_signal,
    f15ve_f15_valuation_at_entry_peraw_21d_base_v006_signal,
    f15ve_f15_valuation_at_entry_peraw_63d_base_v007_signal,
    f15ve_f15_valuation_at_entry_peraw_252d_base_v008_signal,
    f15ve_f15_valuation_at_entry_pblevel_21d_base_v009_signal,
    f15ve_f15_valuation_at_entry_pblevel_63d_base_v010_signal,
    f15ve_f15_valuation_at_entry_pblevel_252d_base_v011_signal,
    f15ve_f15_valuation_at_entry_pblevel_504d_base_v012_signal,
    f15ve_f15_valuation_at_entry_pbraw_63d_base_v013_signal,
    f15ve_f15_valuation_at_entry_pbraw_252d_base_v014_signal,
    f15ve_f15_valuation_at_entry_pslevel_21d_base_v015_signal,
    f15ve_f15_valuation_at_entry_pslevel_63d_base_v016_signal,
    f15ve_f15_valuation_at_entry_pslevel_252d_base_v017_signal,
    f15ve_f15_valuation_at_entry_pslevel_504d_base_v018_signal,
    f15ve_f15_valuation_at_entry_psraw_63d_base_v019_signal,
    f15ve_f15_valuation_at_entry_psraw_252d_base_v020_signal,
    f15ve_f15_valuation_at_entry_evebitdalevel_21d_base_v021_signal,
    f15ve_f15_valuation_at_entry_evebitdalevel_63d_base_v022_signal,
    f15ve_f15_valuation_at_entry_evebitdalevel_252d_base_v023_signal,
    f15ve_f15_valuation_at_entry_evebitdalevel_504d_base_v024_signal,
    f15ve_f15_valuation_at_entry_evebitdaraw_63d_base_v025_signal,
    f15ve_f15_valuation_at_entry_evebitdaraw_252d_base_v026_signal,
    f15ve_f15_valuation_at_entry_evebitlevel_21d_base_v027_signal,
    f15ve_f15_valuation_at_entry_evebitlevel_63d_base_v028_signal,
    f15ve_f15_valuation_at_entry_evebitlevel_252d_base_v029_signal,
    f15ve_f15_valuation_at_entry_evebitlevel_504d_base_v030_signal,
    f15ve_f15_valuation_at_entry_evebitraw_63d_base_v031_signal,
    f15ve_f15_valuation_at_entry_evebitraw_252d_base_v032_signal,
    f15ve_f15_valuation_at_entry_evrev_21d_base_v033_signal,
    f15ve_f15_valuation_at_entry_evrev_63d_base_v034_signal,
    f15ve_f15_valuation_at_entry_evrev_252d_base_v035_signal,
    f15ve_f15_valuation_at_entry_evrev_504d_base_v036_signal,
    f15ve_f15_valuation_at_entry_evfcf_21d_base_v037_signal,
    f15ve_f15_valuation_at_entry_evfcf_63d_base_v038_signal,
    f15ve_f15_valuation_at_entry_evfcf_252d_base_v039_signal,
    f15ve_f15_valuation_at_entry_evfcf_504d_base_v040_signal,
    f15ve_f15_valuation_at_entry_evncfo_21d_base_v041_signal,
    f15ve_f15_valuation_at_entry_evncfo_63d_base_v042_signal,
    f15ve_f15_valuation_at_entry_evncfo_252d_base_v043_signal,
    f15ve_f15_valuation_at_entry_evncfo_504d_base_v044_signal,
    f15ve_f15_valuation_at_entry_evgp_21d_base_v045_signal,
    f15ve_f15_valuation_at_entry_evgp_63d_base_v046_signal,
    f15ve_f15_valuation_at_entry_evgp_252d_base_v047_signal,
    f15ve_f15_valuation_at_entry_pfcf_21d_base_v048_signal,
    f15ve_f15_valuation_at_entry_pfcf_63d_base_v049_signal,
    f15ve_f15_valuation_at_entry_pfcf_252d_base_v050_signal,
    f15ve_f15_valuation_at_entry_pfcf_504d_base_v051_signal,
    f15ve_f15_valuation_at_entry_pncfo_21d_base_v052_signal,
    f15ve_f15_valuation_at_entry_pncfo_63d_base_v053_signal,
    f15ve_f15_valuation_at_entry_pncfo_252d_base_v054_signal,
    f15ve_f15_valuation_at_entry_pgp_21d_base_v055_signal,
    f15ve_f15_valuation_at_entry_pgp_63d_base_v056_signal,
    f15ve_f15_valuation_at_entry_pgp_252d_base_v057_signal,
    f15ve_f15_valuation_at_entry_pgp_504d_base_v058_signal,
    f15ve_f15_valuation_at_entry_popinc_21d_base_v059_signal,
    f15ve_f15_valuation_at_entry_popinc_63d_base_v060_signal,
    f15ve_f15_valuation_at_entry_popinc_252d_base_v061_signal,
    f15ve_f15_valuation_at_entry_popinc_504d_base_v062_signal,
    f15ve_f15_valuation_at_entry_eyield_21d_base_v063_signal,
    f15ve_f15_valuation_at_entry_eyield_63d_base_v064_signal,
    f15ve_f15_valuation_at_entry_eyield_252d_base_v065_signal,
    f15ve_f15_valuation_at_entry_syield_21d_base_v066_signal,
    f15ve_f15_valuation_at_entry_syield_252d_base_v067_signal,
    f15ve_f15_valuation_at_entry_fcfyield_21d_base_v068_signal,
    f15ve_f15_valuation_at_entry_fcfyield_252d_base_v069_signal,
    f15ve_f15_valuation_at_entry_ebitdayield_21d_base_v070_signal,
    f15ve_f15_valuation_at_entry_ebitdayield_252d_base_v071_signal,
    f15ve_f15_valuation_at_entry_pelevelxmcap_63d_base_v072_signal,
    f15ve_f15_valuation_at_entry_pblevelxmcap_252d_base_v073_signal,
    f15ve_f15_valuation_at_entry_evebitdaxev_252d_base_v074_signal,
    f15ve_f15_valuation_at_entry_psxmcap_252d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F15_VALUATION_AT_ENTRY_REGISTRY_001_075 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(np.random.normal(0.0005, 0.02, n))), name="closeadj")
    revenue = pd.Series(5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.005, n))), name="revenue")
    netinc = pd.Series(5e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="netinc")
    fcf = pd.Series(3e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="fcf")
    ncfo = pd.Series(4e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="ncfo")
    equity = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.004, n))), name="equity")
    debt = pd.Series(5e8 * np.exp(np.cumsum(np.random.normal(0.0001, 0.005, n))), name="debt")
    assets = pd.Series(2e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.003, n))), name="assets")
    ebitda = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.006, n))), name="ebitda")
    capex = pd.Series(3e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="capex")
    eps = pd.Series(1.0 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="eps")
    sharesbas = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(0.0001, 0.002, n))), name="sharesbas")
    opinc = pd.Series(8e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.007, n))), name="opinc")
    gp = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.005, n))), name="gp")
    workingcapital = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0001, 0.006, n))), name="workingcapital")
    currentratio = pd.Series(1.8 * np.exp(np.cumsum(np.random.normal(0.0, 0.003, n))), name="currentratio")
    intexp = pd.Series(2e7 * np.exp(np.cumsum(np.random.normal(0.0001, 0.004, n))), name="intexp")
    liabilities = pd.Series(8e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.004, n))), name="liabilities")
    retearn = pd.Series(5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.005, n))), name="retearn")
    marketcap = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0005, 0.015, n))), name="marketcap")
    ev = marketcap + debt - 0.3 * marketcap
    ev = pd.Series(ev.values, name="ev")
    evebit = ev / opinc.replace(0, np.nan)
    evebit = pd.Series(evebit.values, name="evebit")
    evebitda = ev / ebitda.replace(0, np.nan)
    evebitda = pd.Series(evebitda.values, name="evebitda")
    pe = marketcap / netinc.replace(0, np.nan)
    pe = pd.Series(pe.values, name="pe")
    pb = marketcap / equity.replace(0, np.nan)
    pb = pd.Series(pb.values, name="pb")
    ps = marketcap / revenue.replace(0, np.nan)
    ps = pd.Series(ps.values, name="ps")
    cols = {"closeadj": closeadj, "revenue": revenue, "netinc": netinc, "fcf": fcf, "ncfo": ncfo,
            "equity": equity, "debt": debt, "assets": assets, "ebitda": ebitda, "capex": capex,
            "eps": eps, "sharesbas": sharesbas, "opinc": opinc, "gp": gp, "workingcapital": workingcapital,
            "currentratio": currentratio, "intexp": intexp, "liabilities": liabilities, "retearn": retearn,
            "marketcap": marketcap, "ev": ev, "evebit": evebit, "evebitda": evebitda,
            "pe": pe, "pb": pb, "ps": ps}
    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f15_valuation", "_f15_pe", "_f15_ev")
    for name, meta in REGISTRY.items():
        fn = meta["func"]
        args = [cols[c] for c in meta["inputs"]]
        y1 = fn(*args)
        y2 = fn(*args)
        pd.testing.assert_series_equal(y1, y2)
        q = y1.iloc[504:].dropna()
        assert len(q) > 0, name
        assert q.nunique() > 50, f"{name} nunique={q.nunique()}"
        assert q.std() > 0, name
        assert not q.isna().all(), name
        if y1.iloc[504:].isna().mean() < 0.5:
            nan_ok += 1
        src = inspect.getsource(fn)
        assert any(p in src for p in domain_primitives), name
        n_features += 1
    assert n_features == 75, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f15_valuation_at_entry_base_001_075_claude: {n_features} features pass")
