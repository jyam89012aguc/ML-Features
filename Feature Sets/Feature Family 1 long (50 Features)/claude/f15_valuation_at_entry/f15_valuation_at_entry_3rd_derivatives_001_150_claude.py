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


def _slope_diff_norm(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _jerk(s, w):
    sl = s.diff(periods=w) / s.abs().replace(0, np.nan)
    return sl.diff(periods=w)


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


# 5d jerk of 21d PE level
def f15ve_f15_valuation_at_entry_pelevel_21d_jerk_v001_signal(netinc, marketcap):
    base = _f15_pe_level(netinc, marketcap, 21) * marketcap
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 21d PE level
def f15ve_f15_valuation_at_entry_pelevel_21d_jerk_v002_signal(netinc, marketcap):
    base = _f15_pe_level(netinc, marketcap, 21) * marketcap
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d PE level
def f15ve_f15_valuation_at_entry_pelevel_63d_jerk_v003_signal(netinc, marketcap):
    base = _f15_pe_level(netinc, marketcap, 63) * marketcap
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 63d PE level
def f15ve_f15_valuation_at_entry_pelevel_63d_jerk_v004_signal(netinc, marketcap):
    base = _f15_pe_level(netinc, marketcap, 63) * marketcap
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 126d PE level
def f15ve_f15_valuation_at_entry_pelevel_126d_jerk_v005_signal(netinc, marketcap):
    base = _f15_pe_level(netinc, marketcap, 126) * marketcap
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 126d PE level
def f15ve_f15_valuation_at_entry_pelevel_126d_jerk_v006_signal(netinc, marketcap):
    base = _f15_pe_level(netinc, marketcap, 126) * marketcap
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 252d PE level
def f15ve_f15_valuation_at_entry_pelevel_252d_jerk_v007_signal(netinc, marketcap):
    base = _f15_pe_level(netinc, marketcap, 252) * marketcap
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d PE level
def f15ve_f15_valuation_at_entry_pelevel_252d_jerk_v008_signal(netinc, marketcap):
    base = _f15_pe_level(netinc, marketcap, 252) * marketcap
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 504d PE level
def f15ve_f15_valuation_at_entry_pelevel_504d_jerk_v009_signal(netinc, marketcap):
    base = _f15_pe_level(netinc, marketcap, 504) * marketcap
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 504d PE level
def f15ve_f15_valuation_at_entry_pelevel_504d_jerk_v010_signal(netinc, marketcap):
    base = _f15_pe_level(netinc, marketcap, 504) * marketcap
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of 21d PB level
def f15ve_f15_valuation_at_entry_pblevel_21d_jerk_v011_signal(equity, marketcap):
    base = _f15_valuation_level(marketcap, equity, 21) * marketcap
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 21d PB
def f15ve_f15_valuation_at_entry_pblevel_21d_jerk_v012_signal(equity, marketcap):
    base = _f15_valuation_level(marketcap, equity, 21) * marketcap
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d PB
def f15ve_f15_valuation_at_entry_pblevel_63d_jerk_v013_signal(equity, marketcap):
    base = _f15_valuation_level(marketcap, equity, 63) * marketcap
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 63d PB
def f15ve_f15_valuation_at_entry_pblevel_63d_jerk_v014_signal(equity, marketcap):
    base = _f15_valuation_level(marketcap, equity, 63) * marketcap
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 252d PB
def f15ve_f15_valuation_at_entry_pblevel_252d_jerk_v015_signal(equity, marketcap):
    base = _f15_valuation_level(marketcap, equity, 252) * marketcap
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d PB
def f15ve_f15_valuation_at_entry_pblevel_252d_jerk_v016_signal(equity, marketcap):
    base = _f15_valuation_level(marketcap, equity, 252) * marketcap
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 504d PB
def f15ve_f15_valuation_at_entry_pblevel_504d_jerk_v017_signal(equity, marketcap):
    base = _f15_valuation_level(marketcap, equity, 504) * marketcap
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 504d PB
def f15ve_f15_valuation_at_entry_pblevel_504d_jerk_v018_signal(equity, marketcap):
    base = _f15_valuation_level(marketcap, equity, 504) * marketcap
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of 21d PS
def f15ve_f15_valuation_at_entry_pslevel_21d_jerk_v019_signal(revenue, marketcap):
    base = _f15_valuation_level(marketcap, revenue, 21) * marketcap
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d PS
def f15ve_f15_valuation_at_entry_pslevel_63d_jerk_v020_signal(revenue, marketcap):
    base = _f15_valuation_level(marketcap, revenue, 63) * marketcap
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 63d PS
def f15ve_f15_valuation_at_entry_pslevel_63d_jerk_v021_signal(revenue, marketcap):
    base = _f15_valuation_level(marketcap, revenue, 63) * marketcap
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 252d PS
def f15ve_f15_valuation_at_entry_pslevel_252d_jerk_v022_signal(revenue, marketcap):
    base = _f15_valuation_level(marketcap, revenue, 252) * marketcap
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d PS
def f15ve_f15_valuation_at_entry_pslevel_252d_jerk_v023_signal(revenue, marketcap):
    base = _f15_valuation_level(marketcap, revenue, 252) * marketcap
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 504d PS
def f15ve_f15_valuation_at_entry_pslevel_504d_jerk_v024_signal(revenue, marketcap):
    base = _f15_valuation_level(marketcap, revenue, 504) * marketcap
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 504d PS
def f15ve_f15_valuation_at_entry_pslevel_504d_jerk_v025_signal(revenue, marketcap):
    base = _f15_valuation_level(marketcap, revenue, 504) * marketcap
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of 21d EV/EBITDA
def f15ve_f15_valuation_at_entry_evebitda_21d_jerk_v026_signal(ev, ebitda):
    base = _f15_ev_multiple(ev, ebitda, 21) * ev
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d EV/EBITDA
def f15ve_f15_valuation_at_entry_evebitda_63d_jerk_v027_signal(ev, ebitda):
    base = _f15_ev_multiple(ev, ebitda, 63) * ev
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 63d EV/EBITDA
def f15ve_f15_valuation_at_entry_evebitda_63d_jerk_v028_signal(ev, ebitda):
    base = _f15_ev_multiple(ev, ebitda, 63) * ev
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 252d EV/EBITDA
def f15ve_f15_valuation_at_entry_evebitda_252d_jerk_v029_signal(ev, ebitda):
    base = _f15_ev_multiple(ev, ebitda, 252) * ev
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d EV/EBITDA
def f15ve_f15_valuation_at_entry_evebitda_252d_jerk_v030_signal(ev, ebitda):
    base = _f15_ev_multiple(ev, ebitda, 252) * ev
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 504d EV/EBITDA
def f15ve_f15_valuation_at_entry_evebitda_504d_jerk_v031_signal(ev, ebitda):
    base = _f15_ev_multiple(ev, ebitda, 504) * ev
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 504d EV/EBITDA
def f15ve_f15_valuation_at_entry_evebitda_504d_jerk_v032_signal(ev, ebitda):
    base = _f15_ev_multiple(ev, ebitda, 504) * ev
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d EV/EBIT
def f15ve_f15_valuation_at_entry_evebit_63d_jerk_v033_signal(ev, opinc):
    base = _f15_ev_multiple(ev, opinc, 63) * ev
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d EV/EBIT
def f15ve_f15_valuation_at_entry_evebit_252d_jerk_v034_signal(ev, opinc):
    base = _f15_ev_multiple(ev, opinc, 252) * ev
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 504d EV/EBIT
def f15ve_f15_valuation_at_entry_evebit_504d_jerk_v035_signal(ev, opinc):
    base = _f15_ev_multiple(ev, opinc, 504) * ev
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d EV/Rev
def f15ve_f15_valuation_at_entry_evrev_63d_jerk_v036_signal(ev, revenue):
    base = _f15_ev_multiple(ev, revenue, 63) * ev
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d EV/Rev
def f15ve_f15_valuation_at_entry_evrev_252d_jerk_v037_signal(ev, revenue):
    base = _f15_ev_multiple(ev, revenue, 252) * ev
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 504d EV/Rev
def f15ve_f15_valuation_at_entry_evrev_504d_jerk_v038_signal(ev, revenue):
    base = _f15_ev_multiple(ev, revenue, 504) * ev
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d EV/FCF
def f15ve_f15_valuation_at_entry_evfcf_63d_jerk_v039_signal(ev, fcf):
    base = _f15_ev_multiple(ev, fcf, 63) * ev
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d EV/FCF
def f15ve_f15_valuation_at_entry_evfcf_252d_jerk_v040_signal(ev, fcf):
    base = _f15_ev_multiple(ev, fcf, 252) * ev
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 504d EV/FCF
def f15ve_f15_valuation_at_entry_evfcf_504d_jerk_v041_signal(ev, fcf):
    base = _f15_ev_multiple(ev, fcf, 504) * ev
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d EV/NCFO
def f15ve_f15_valuation_at_entry_evncfo_63d_jerk_v042_signal(ev, ncfo):
    base = _f15_ev_multiple(ev, ncfo, 63) * ev
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d EV/NCFO
def f15ve_f15_valuation_at_entry_evncfo_252d_jerk_v043_signal(ev, ncfo):
    base = _f15_ev_multiple(ev, ncfo, 252) * ev
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d EV/GP
def f15ve_f15_valuation_at_entry_evgp_63d_jerk_v044_signal(ev, gp):
    base = _f15_ev_multiple(ev, gp, 63) * ev
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d EV/GP
def f15ve_f15_valuation_at_entry_evgp_252d_jerk_v045_signal(ev, gp):
    base = _f15_ev_multiple(ev, gp, 252) * ev
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d P/FCF
def f15ve_f15_valuation_at_entry_pfcf_63d_jerk_v046_signal(fcf, marketcap):
    base = _f15_valuation_level(marketcap, fcf, 63) * marketcap
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d P/FCF
def f15ve_f15_valuation_at_entry_pfcf_252d_jerk_v047_signal(fcf, marketcap):
    base = _f15_valuation_level(marketcap, fcf, 252) * marketcap
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 504d P/FCF
def f15ve_f15_valuation_at_entry_pfcf_504d_jerk_v048_signal(fcf, marketcap):
    base = _f15_valuation_level(marketcap, fcf, 504) * marketcap
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d P/NCFO
def f15ve_f15_valuation_at_entry_pncfo_63d_jerk_v049_signal(ncfo, marketcap):
    base = _f15_valuation_level(marketcap, ncfo, 63) * marketcap
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d P/NCFO
def f15ve_f15_valuation_at_entry_pncfo_252d_jerk_v050_signal(ncfo, marketcap):
    base = _f15_valuation_level(marketcap, ncfo, 252) * marketcap
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d P/GP
def f15ve_f15_valuation_at_entry_pgp_63d_jerk_v051_signal(gp, marketcap):
    base = _f15_valuation_level(marketcap, gp, 63) * marketcap
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d P/GP
def f15ve_f15_valuation_at_entry_pgp_252d_jerk_v052_signal(gp, marketcap):
    base = _f15_valuation_level(marketcap, gp, 252) * marketcap
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 504d P/GP
def f15ve_f15_valuation_at_entry_pgp_504d_jerk_v053_signal(gp, marketcap):
    base = _f15_valuation_level(marketcap, gp, 504) * marketcap
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d P/Opinc
def f15ve_f15_valuation_at_entry_popinc_63d_jerk_v054_signal(opinc, marketcap):
    base = _f15_valuation_level(marketcap, opinc, 63) * marketcap
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d P/Opinc
def f15ve_f15_valuation_at_entry_popinc_252d_jerk_v055_signal(opinc, marketcap):
    base = _f15_valuation_level(marketcap, opinc, 252) * marketcap
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 504d P/Opinc
def f15ve_f15_valuation_at_entry_popinc_504d_jerk_v056_signal(opinc, marketcap):
    base = _f15_valuation_level(marketcap, opinc, 504) * marketcap
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d earnings yield
def f15ve_f15_valuation_at_entry_eyield_63d_jerk_v057_signal(netinc, marketcap):
    base = _f15_valuation_level(netinc, marketcap, 63) * marketcap
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d earnings yield
def f15ve_f15_valuation_at_entry_eyield_252d_jerk_v058_signal(netinc, marketcap):
    base = _f15_valuation_level(netinc, marketcap, 252) * marketcap
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d sales yield
def f15ve_f15_valuation_at_entry_syield_252d_jerk_v059_signal(revenue, marketcap):
    base = _f15_valuation_level(revenue, marketcap, 252) * marketcap
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d fcf yield
def f15ve_f15_valuation_at_entry_fcfyield_252d_jerk_v060_signal(fcf, marketcap):
    base = _f15_valuation_level(fcf, marketcap, 252) * marketcap
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d ebitda yield
def f15ve_f15_valuation_at_entry_ebitdayield_252d_jerk_v061_signal(ebitda, ev):
    base = _f15_valuation_level(ebitda, ev, 252) * ev
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d gp yield
def f15ve_f15_valuation_at_entry_gpyield_252d_jerk_v062_signal(gp, ev):
    base = _f15_valuation_level(gp, ev, 252) * ev
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d ncfo yield
def f15ve_f15_valuation_at_entry_ncfoyield_252d_jerk_v063_signal(ncfo, ev):
    base = _f15_valuation_level(ncfo, ev, 252) * ev
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d EV/Capex
def f15ve_f15_valuation_at_entry_evcapex_63d_jerk_v064_signal(ev, capex):
    base = _f15_ev_multiple(ev, capex, 63) * ev
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d EV/Capex
def f15ve_f15_valuation_at_entry_evcapex_252d_jerk_v065_signal(ev, capex):
    base = _f15_ev_multiple(ev, capex, 252) * ev
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d P/Capex
def f15ve_f15_valuation_at_entry_pcapex_63d_jerk_v066_signal(capex, marketcap):
    base = _f15_valuation_level(marketcap, capex, 63) * marketcap
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d P/Capex
def f15ve_f15_valuation_at_entry_pcapex_252d_jerk_v067_signal(capex, marketcap):
    base = _f15_valuation_level(marketcap, capex, 252) * marketcap
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d P/Assets
def f15ve_f15_valuation_at_entry_passet_252d_jerk_v068_signal(assets, marketcap):
    base = _f15_valuation_level(marketcap, assets, 252) * marketcap
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 504d P/Assets
def f15ve_f15_valuation_at_entry_passet_504d_jerk_v069_signal(assets, marketcap):
    base = _f15_valuation_level(marketcap, assets, 504) * marketcap
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d EV/Assets
def f15ve_f15_valuation_at_entry_evassets_252d_jerk_v070_signal(ev, assets):
    base = _f15_ev_multiple(ev, assets, 252) * ev
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d P/Retearn
def f15ve_f15_valuation_at_entry_pretearn_252d_jerk_v071_signal(retearn, marketcap):
    base = _f15_valuation_level(marketcap, retearn, 252) * marketcap
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d EV/Equity
def f15ve_f15_valuation_at_entry_evequity_252d_jerk_v072_signal(ev, equity):
    base = _f15_ev_multiple(ev, equity, 252) * ev
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d EV/Debt
def f15ve_f15_valuation_at_entry_evdebt_252d_jerk_v073_signal(ev, debt):
    base = _f15_ev_multiple(ev, debt, 252) * ev
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d EV/Sharesbas
def f15ve_f15_valuation_at_entry_evpershare_252d_jerk_v074_signal(ev, sharesbas):
    base = _f15_ev_multiple(ev, sharesbas, 252) * ev
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d EV/Workingcapital
def f15ve_f15_valuation_at_entry_evwc_252d_jerk_v075_signal(ev, workingcapital):
    base = _f15_ev_multiple(ev, workingcapital, 252) * ev
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d PE deviation
def f15ve_f15_valuation_at_entry_pelevdev_63d_jerk_v076_signal(netinc, marketcap):
    p = _f15_pe_level(netinc, marketcap, 21)
    avg = _mean(p, 63)
    base = (p - avg) * marketcap
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d PE deviation
def f15ve_f15_valuation_at_entry_pelevdev_252d_jerk_v077_signal(netinc, marketcap):
    p = _f15_pe_level(netinc, marketcap, 21)
    avg = _mean(p, 252)
    base = (p - avg) * marketcap
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d PB deviation
def f15ve_f15_valuation_at_entry_pblevdev_252d_jerk_v078_signal(equity, marketcap):
    p = _f15_valuation_level(marketcap, equity, 21)
    avg = _mean(p, 252)
    base = (p - avg) * marketcap
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d PS deviation
def f15ve_f15_valuation_at_entry_pslevdev_252d_jerk_v079_signal(revenue, marketcap):
    p = _f15_valuation_level(marketcap, revenue, 21)
    avg = _mean(p, 252)
    base = (p - avg) * marketcap
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d EV/EBITDA deviation
def f15ve_f15_valuation_at_entry_evebitdadev_252d_jerk_v080_signal(ev, ebitda):
    p = _f15_ev_multiple(ev, ebitda, 21)
    avg = _mean(p, 252)
    base = (p - avg) * ev
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 252d PE z-score
def f15ve_f15_valuation_at_entry_pelevelz_252d_jerk_v081_signal(netinc, marketcap):
    p = _f15_pe_level(netinc, marketcap, 63)
    base = _z(p, 252) * marketcap / 1e9
    sl = _diff(base, 21)
    result = _diff(sl, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 504d PE z-score
def f15ve_f15_valuation_at_entry_pelevelz_504d_jerk_v082_signal(netinc, marketcap):
    p = _f15_pe_level(netinc, marketcap, 252)
    base = _z(p, 504) * marketcap / 1e9
    sl = _diff(base, 63)
    result = _diff(sl, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d EV/EBITDA z-score
def f15ve_f15_valuation_at_entry_evebitdaz_252d_jerk_v083_signal(ev, ebitda):
    p = _f15_ev_multiple(ev, ebitda, 63)
    base = _z(p, 252) * ev / 1e9
    sl = _diff(base, 63)
    result = _diff(sl, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d PB z-score
def f15ve_f15_valuation_at_entry_pblevelz_252d_jerk_v084_signal(equity, marketcap):
    p = _f15_valuation_level(marketcap, equity, 63)
    base = _z(p, 252) * marketcap / 1e9
    sl = _diff(base, 63)
    result = _diff(sl, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d PS z-score
def f15ve_f15_valuation_at_entry_pslevelz_252d_jerk_v085_signal(revenue, marketcap):
    p = _f15_valuation_level(marketcap, revenue, 63)
    base = _z(p, 252) * marketcap / 1e9
    sl = _diff(base, 63)
    result = _diff(sl, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of pe column smoothed 21d
def f15ve_f15_valuation_at_entry_peraw_21d_jerk_v086_signal(pe, marketcap):
    base = _f15_valuation_level(pe * marketcap, marketcap, 21) * marketcap
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of pe column smoothed 63d
def f15ve_f15_valuation_at_entry_peraw_63d_jerk_v087_signal(pe, marketcap):
    base = _f15_valuation_level(pe * marketcap, marketcap, 63) * marketcap
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of pb column smoothed 63d
def f15ve_f15_valuation_at_entry_pbraw_63d_jerk_v088_signal(pb, marketcap):
    base = _f15_valuation_level(pb * marketcap, marketcap, 63) * marketcap
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of pb column smoothed 252d
def f15ve_f15_valuation_at_entry_pbraw_252d_jerk_v089_signal(pb, marketcap):
    base = _f15_valuation_level(pb * marketcap, marketcap, 252) * marketcap
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of ps column smoothed 252d
def f15ve_f15_valuation_at_entry_psraw_252d_jerk_v090_signal(ps, marketcap):
    base = _f15_valuation_level(ps * marketcap, marketcap, 252) * marketcap
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of evebitda column smoothed 252d
def f15ve_f15_valuation_at_entry_evebitdaraw_252d_jerk_v091_signal(evebitda, ev):
    base = _f15_valuation_level(evebitda * ev, ev, 252) * ev
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of evebit column smoothed 252d
def f15ve_f15_valuation_at_entry_evebitraw_252d_jerk_v092_signal(evebit, ev):
    base = _f15_valuation_level(evebit * ev, ev, 252) * ev
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of (PE/PB ratio at 252d)
def f15ve_f15_valuation_at_entry_pe_to_pb_252d_jerk_v093_signal(netinc, equity, marketcap):
    a = _f15_pe_level(netinc, marketcap, 252)
    b = _f15_valuation_level(marketcap, equity, 252)
    base = (a / b.replace(0, np.nan)) * marketcap
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of (EV/EBITDA / PE) at 252d
def f15ve_f15_valuation_at_entry_evebitda_to_pe_252d_jerk_v094_signal(ev, ebitda, netinc, marketcap):
    a = _f15_ev_multiple(ev, ebitda, 252)
    b = _f15_pe_level(netinc, marketcap, 252)
    base = (a / b.replace(0, np.nan)) * marketcap
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of (PB / PS) at 252d
def f15ve_f15_valuation_at_entry_pb_to_ps_252d_jerk_v095_signal(equity, revenue, marketcap):
    a = _f15_valuation_level(marketcap, equity, 252)
    b = _f15_valuation_level(marketcap, revenue, 252)
    base = (a / b.replace(0, np.nan)) * marketcap
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of (EV/EBIT / EV/EBITDA) at 252d
def f15ve_f15_valuation_at_entry_evebit_to_evebitda_252d_jerk_v096_signal(ev, opinc, ebitda):
    a = _f15_ev_multiple(ev, opinc, 252)
    b = _f15_ev_multiple(ev, ebitda, 252)
    base = (a / b.replace(0, np.nan)) * ev
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of (PE_63d / PE_252d) recent vs trend
def f15ve_f15_valuation_at_entry_pe_recent_vs_trend_jerk_v097_signal(netinc, marketcap):
    a = _f15_pe_level(netinc, marketcap, 63)
    b = _f15_pe_level(netinc, marketcap, 252)
    base = (a / b.replace(0, np.nan)) * marketcap
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of (PS_63d / PS_252d)
def f15ve_f15_valuation_at_entry_ps_recent_vs_trend_jerk_v098_signal(revenue, marketcap):
    a = _f15_valuation_level(marketcap, revenue, 63)
    b = _f15_valuation_level(marketcap, revenue, 252)
    base = (a / b.replace(0, np.nan)) * marketcap
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of (EV/EBITDA_63d / EV/EBITDA_252d)
def f15ve_f15_valuation_at_entry_evebitda_recent_vs_trend_jerk_v099_signal(ev, ebitda):
    a = _f15_ev_multiple(ev, ebitda, 63)
    b = _f15_ev_multiple(ev, ebitda, 252)
    base = (a / b.replace(0, np.nan)) * ev
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of blendedval 252d
def f15ve_f15_valuation_at_entry_blendedval_252d_jerk_v100_signal(netinc, equity, revenue, marketcap):
    pe_l = _f15_pe_level(netinc, marketcap, 252)
    pb_l = _f15_valuation_level(marketcap, equity, 252)
    ps_l = _f15_valuation_level(marketcap, revenue, 252)
    base = (pe_l + pb_l + ps_l) * marketcap
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of blendedevmult 252d
def f15ve_f15_valuation_at_entry_blendedevmult_252d_jerk_v101_signal(ev, ebitda, opinc):
    e1 = _f15_ev_multiple(ev, ebitda, 252)
    e2 = _f15_ev_multiple(ev, opinc, 252)
    base = (e1 + e2) * ev
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of position-in-504d-range PE
def f15ve_f15_valuation_at_entry_pelevpos_504d_jerk_v102_signal(netinc, marketcap):
    p = _f15_pe_level(netinc, marketcap, 63)
    hi = p.rolling(504, min_periods=126).max()
    lo = p.rolling(504, min_periods=126).min()
    base = ((p - lo) / (hi - lo).replace(0, np.nan)) * marketcap
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of position-in-504d-range PB
def f15ve_f15_valuation_at_entry_pblevpos_504d_jerk_v103_signal(equity, marketcap):
    p = _f15_valuation_level(marketcap, equity, 63)
    hi = p.rolling(504, min_periods=126).max()
    lo = p.rolling(504, min_periods=126).min()
    base = ((p - lo) / (hi - lo).replace(0, np.nan)) * marketcap
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of position-in-504d-range EV/EBITDA
def f15ve_f15_valuation_at_entry_evebitdapos_504d_jerk_v104_signal(ev, ebitda):
    p = _f15_ev_multiple(ev, ebitda, 63)
    hi = p.rolling(504, min_periods=126).max()
    lo = p.rolling(504, min_periods=126).min()
    base = ((p - lo) / (hi - lo).replace(0, np.nan)) * ev
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of PE relative to 504d hi
def f15ve_f15_valuation_at_entry_perelhi_504d_jerk_v105_signal(netinc, marketcap):
    p = _f15_pe_level(netinc, marketcap, 63)
    hi = p.rolling(504, min_periods=126).max()
    base = (p / hi.replace(0, np.nan)) * marketcap
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of PB relative to 504d hi
def f15ve_f15_valuation_at_entry_pbrelhi_504d_jerk_v106_signal(equity, marketcap):
    p = _f15_valuation_level(marketcap, equity, 63)
    hi = p.rolling(504, min_periods=126).max()
    base = (p / hi.replace(0, np.nan)) * marketcap
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of PS relative to 504d hi
def f15ve_f15_valuation_at_entry_psrelhi_504d_jerk_v107_signal(revenue, marketcap):
    p = _f15_valuation_level(marketcap, revenue, 63)
    hi = p.rolling(504, min_periods=126).max()
    base = (p / hi.replace(0, np.nan)) * marketcap
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of EV/EBITDA relative to 504d hi
def f15ve_f15_valuation_at_entry_evebitdarelhi_504d_jerk_v108_signal(ev, ebitda):
    p = _f15_ev_multiple(ev, ebitda, 63)
    hi = p.rolling(504, min_periods=126).max()
    base = (p / hi.replace(0, np.nan)) * ev
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of richpe count
def f15ve_f15_valuation_at_entry_richpe_count_252d_jerk_v109_signal(netinc, marketcap):
    p = _f15_pe_level(netinc, marketcap, 21)
    avg = _mean(p, 252)
    flag = (p > avg).astype(float)
    base = flag.rolling(252, min_periods=63).sum() * marketcap
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of richevebitda count
def f15ve_f15_valuation_at_entry_richevebitda_count_252d_jerk_v110_signal(ev, ebitda):
    p = _f15_ev_multiple(ev, ebitda, 21)
    avg = _mean(p, 252)
    flag = (p > avg).astype(float)
    base = flag.rolling(252, min_periods=63).sum() * ev
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of cheapevebitda count
def f15ve_f15_valuation_at_entry_cheapevebitda_count_252d_jerk_v111_signal(ev, ebitda):
    p = _f15_ev_multiple(ev, ebitda, 21)
    avg = _mean(p, 252)
    flag = (p < avg).astype(float)
    base = flag.rolling(252, min_periods=63).sum() * ev
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of cheappe count 504d
def f15ve_f15_valuation_at_entry_cheappe_count_504d_jerk_v112_signal(netinc, marketcap):
    p = _f15_pe_level(netinc, marketcap, 21)
    avg = _mean(p, 504)
    flag = (p < avg).astype(float)
    base = flag.rolling(504, min_periods=126).sum() * marketcap
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of EPS yield 252d
def f15ve_f15_valuation_at_entry_epsyield_252d_jerk_v113_signal(eps, marketcap, closeadj):
    base = _f15_valuation_level(eps, closeadj, 252) * marketcap
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of EPS x close 21d
def f15ve_f15_valuation_at_entry_epsxprice_21d_jerk_v114_signal(eps, marketcap, closeadj):
    base = _f15_valuation_level(eps * closeadj, closeadj, 21) * marketcap
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of cheapcomp 252d
def f15ve_f15_valuation_at_entry_cheapcomp_252d_jerk_v115_signal(netinc, equity, revenue, marketcap):
    pe_l = _f15_pe_level(netinc, marketcap, 252)
    pb_l = _f15_valuation_level(marketcap, equity, 252)
    ps_l = _f15_valuation_level(marketcap, revenue, 252)
    s = (pe_l + pb_l + ps_l).replace(0, np.nan)
    base = (1.0 / s) * marketcap
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of EV/Liabilities 252d
def f15ve_f15_valuation_at_entry_evintens_252d_jerk_v116_signal(ev, liabilities):
    a = _f15_ev_multiple(ev, liabilities, 252)
    base = a * ev
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of P/Workingcapital 252d
def f15ve_f15_valuation_at_entry_pwc_252d_jerk_v117_signal(workingcapital, marketcap):
    a = _f15_valuation_level(marketcap, workingcapital, 252)
    base = a * marketcap
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of net debt proxy 252d
def f15ve_f15_valuation_at_entry_netdebt_252d_jerk_v118_signal(ev, marketcap):
    a = _f15_valuation_level(ev - marketcap, marketcap, 252)
    base = a * marketcap
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of pricepershare 252d
def f15ve_f15_valuation_at_entry_pricepershare_252d_jerk_v119_signal(sharesbas, marketcap):
    a = _f15_valuation_level(marketcap, sharesbas, 252)
    base = a * marketcap
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of evcomp 252d
def f15ve_f15_valuation_at_entry_evcomp_252d_jerk_v120_signal(ev, revenue, ebitda):
    a = _f15_ev_multiple(ev, revenue, 252)
    b = _f15_ev_multiple(ev, ebitda, 252)
    base = (a + b) * ev
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of low_mult 252d
def f15ve_f15_valuation_at_entry_lowmult_252d_jerk_v121_signal(netinc, revenue, marketcap):
    pe_l = _f15_pe_level(netinc, marketcap, 252)
    ps_l = _f15_valuation_level(marketcap, revenue, 252)
    lo = pd.concat([pe_l, ps_l], axis=1).min(axis=1)
    base = lo * marketcap
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of high_evmult 252d
def f15ve_f15_valuation_at_entry_highevmult_252d_jerk_v122_signal(ev, ebitda, opinc):
    a = _f15_ev_multiple(ev, ebitda, 252)
    b = _f15_ev_multiple(ev, opinc, 252)
    hi = pd.concat([a, b], axis=1).max(axis=1)
    base = hi * ev
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of log(PE) 252d
def f15ve_f15_valuation_at_entry_logpe_252d_jerk_v123_signal(netinc, marketcap):
    p = _f15_pe_level(netinc, marketcap, 252)
    base = np.log(p.replace(0, np.nan).abs()) * marketcap
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of log(EV/EBITDA) 252d
def f15ve_f15_valuation_at_entry_logevebitda_252d_jerk_v124_signal(ev, ebitda):
    p = _f15_ev_multiple(ev, ebitda, 252)
    base = np.log(p.replace(0, np.nan).abs()) * ev
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of PE squared 21d
def f15ve_f15_valuation_at_entry_pesq_21d_jerk_v125_signal(netinc, marketcap):
    p = _f15_pe_level(netinc, marketcap, 21)
    base = p * p.abs() * marketcap
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of PE squared 252d
def f15ve_f15_valuation_at_entry_pesq_252d_jerk_v126_signal(netinc, marketcap):
    p = _f15_pe_level(netinc, marketcap, 252)
    base = p * p.abs() * marketcap
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of EV/EBITDA squared 252d
def f15ve_f15_valuation_at_entry_evebitdasq_252d_jerk_v127_signal(ev, ebitda):
    p = _f15_ev_multiple(ev, ebitda, 252)
    base = p * p.abs() * ev
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of PB squared 252d
def f15ve_f15_valuation_at_entry_pbsq_252d_jerk_v128_signal(equity, marketcap):
    p = _f15_valuation_level(marketcap, equity, 252)
    base = p * p.abs() * marketcap
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of PS squared 252d
def f15ve_f15_valuation_at_entry_pssq_252d_jerk_v129_signal(revenue, marketcap):
    p = _f15_valuation_level(marketcap, revenue, 252)
    base = p * p.abs() * marketcap
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of EV/EBITDA EMA 21d
def f15ve_f15_valuation_at_entry_evebitda_ema_21d_jerk_v130_signal(ev, ebitda):
    base = (_f15_ev_multiple(ev, ebitda, 21).ewm(span=21, adjust=False).mean()) * ev
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of PE EMA 63d
def f15ve_f15_valuation_at_entry_pe_ema_63d_jerk_v131_signal(netinc, marketcap):
    base = (_f15_pe_level(netinc, marketcap, 63).ewm(span=63, adjust=False).mean()) * marketcap
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of PB EMA 252d
def f15ve_f15_valuation_at_entry_pb_ema_252d_jerk_v132_signal(equity, marketcap):
    base = (_f15_valuation_level(marketcap, equity, 252).ewm(span=252, adjust=False).mean()) * marketcap
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of PS EMA 252d
def f15ve_f15_valuation_at_entry_ps_ema_252d_jerk_v133_signal(revenue, marketcap):
    base = (_f15_valuation_level(marketcap, revenue, 252).ewm(span=252, adjust=False).mean()) * marketcap
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of EV/EBITDA EMA 252d
def f15ve_f15_valuation_at_entry_evebitda_ema_252d_jerk_v134_signal(ev, ebitda):
    base = (_f15_ev_multiple(ev, ebitda, 252).ewm(span=252, adjust=False).mean()) * ev
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of PE x sharesbas
def f15ve_f15_valuation_at_entry_pe_xshares_252d_jerk_v135_signal(netinc, marketcap, sharesbas):
    p = _f15_pe_level(netinc, marketcap, 252)
    base = p * sharesbas
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of EV/EBITDA x assets
def f15ve_f15_valuation_at_entry_evebitda_xassets_252d_jerk_v136_signal(ev, ebitda, assets):
    p = _f15_ev_multiple(ev, ebitda, 252)
    base = p * assets
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of PB x equity
def f15ve_f15_valuation_at_entry_pb_xequity_252d_jerk_v137_signal(equity, marketcap):
    p = _f15_valuation_level(marketcap, equity, 252)
    base = p * equity
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 21d eyield x mkt
def f15ve_f15_valuation_at_entry_eyield_21d_jerk_v138_signal(netinc, marketcap):
    base = _f15_valuation_level(netinc, marketcap, 21) * marketcap
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 21d syield x mkt
def f15ve_f15_valuation_at_entry_syield_21d_jerk_v139_signal(revenue, marketcap):
    base = _f15_valuation_level(revenue, marketcap, 21) * marketcap
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 21d fcfyield x mkt
def f15ve_f15_valuation_at_entry_fcfyield_21d_jerk_v140_signal(fcf, marketcap):
    base = _f15_valuation_level(fcf, marketcap, 21) * marketcap
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 21d ebitdayield x ev
def f15ve_f15_valuation_at_entry_ebitdayield_21d_jerk_v141_signal(ebitda, ev):
    base = _f15_valuation_level(ebitda, ev, 21) * ev
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of net debt to ebitda
def f15ve_f15_valuation_at_entry_netdebt_ebitda_252d_jerk_v142_signal(ev, marketcap, ebitda):
    nd = ev - marketcap
    base = _f15_ev_multiple(nd, ebitda, 252) * ev
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of FCF/EV yield
def f15ve_f15_valuation_at_entry_fcfyield_ev_252d_jerk_v143_signal(fcf, ev):
    base = _f15_valuation_level(fcf, ev, 252) * ev
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of GP/marketcap yield 252d
def f15ve_f15_valuation_at_entry_gpyield_mkt_252d_jerk_v144_signal(gp, marketcap):
    base = _f15_valuation_level(gp, marketcap, 252) * marketcap
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of opinc/marketcap yield 252d
def f15ve_f15_valuation_at_entry_opincyield_mkt_252d_jerk_v145_signal(opinc, marketcap):
    base = _f15_valuation_level(opinc, marketcap, 252) * marketcap
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of ncfo/marketcap yield 252d
def f15ve_f15_valuation_at_entry_ncfoyield_mkt_252d_jerk_v146_signal(ncfo, marketcap):
    base = _f15_valuation_level(ncfo, marketcap, 252) * marketcap
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of retearn/equity x mkt
def f15ve_f15_valuation_at_entry_retearn_equity_252d_jerk_v147_signal(retearn, equity, marketcap):
    base = _f15_valuation_level(retearn, equity, 252) * marketcap
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of EV / (EBITDA - capex)
def f15ve_f15_valuation_at_entry_ev_ebitdamcapex_252d_jerk_v148_signal(ev, ebitda, capex):
    denom = ebitda - capex
    base = _f15_ev_multiple(ev, denom, 252) * ev
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of EV / intexp
def f15ve_f15_valuation_at_entry_ev_intexp_252d_jerk_v149_signal(ev, intexp):
    base = _f15_ev_multiple(ev, intexp, 252) * ev
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of full composite
def f15ve_f15_valuation_at_entry_fullcomp_252d_jerk_v150_signal(netinc, equity, revenue, marketcap, ev, ebitda):
    pe_l = _f15_pe_level(netinc, marketcap, 252)
    pb_l = _f15_valuation_level(marketcap, equity, 252)
    ps_l = _f15_valuation_level(marketcap, revenue, 252)
    eve = _f15_ev_multiple(ev, ebitda, 252)
    base = (pe_l + pb_l + ps_l + eve) * marketcap
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f15ve_f15_valuation_at_entry_pelevel_21d_jerk_v001_signal,
    f15ve_f15_valuation_at_entry_pelevel_21d_jerk_v002_signal,
    f15ve_f15_valuation_at_entry_pelevel_63d_jerk_v003_signal,
    f15ve_f15_valuation_at_entry_pelevel_63d_jerk_v004_signal,
    f15ve_f15_valuation_at_entry_pelevel_126d_jerk_v005_signal,
    f15ve_f15_valuation_at_entry_pelevel_126d_jerk_v006_signal,
    f15ve_f15_valuation_at_entry_pelevel_252d_jerk_v007_signal,
    f15ve_f15_valuation_at_entry_pelevel_252d_jerk_v008_signal,
    f15ve_f15_valuation_at_entry_pelevel_504d_jerk_v009_signal,
    f15ve_f15_valuation_at_entry_pelevel_504d_jerk_v010_signal,
    f15ve_f15_valuation_at_entry_pblevel_21d_jerk_v011_signal,
    f15ve_f15_valuation_at_entry_pblevel_21d_jerk_v012_signal,
    f15ve_f15_valuation_at_entry_pblevel_63d_jerk_v013_signal,
    f15ve_f15_valuation_at_entry_pblevel_63d_jerk_v014_signal,
    f15ve_f15_valuation_at_entry_pblevel_252d_jerk_v015_signal,
    f15ve_f15_valuation_at_entry_pblevel_252d_jerk_v016_signal,
    f15ve_f15_valuation_at_entry_pblevel_504d_jerk_v017_signal,
    f15ve_f15_valuation_at_entry_pblevel_504d_jerk_v018_signal,
    f15ve_f15_valuation_at_entry_pslevel_21d_jerk_v019_signal,
    f15ve_f15_valuation_at_entry_pslevel_63d_jerk_v020_signal,
    f15ve_f15_valuation_at_entry_pslevel_63d_jerk_v021_signal,
    f15ve_f15_valuation_at_entry_pslevel_252d_jerk_v022_signal,
    f15ve_f15_valuation_at_entry_pslevel_252d_jerk_v023_signal,
    f15ve_f15_valuation_at_entry_pslevel_504d_jerk_v024_signal,
    f15ve_f15_valuation_at_entry_pslevel_504d_jerk_v025_signal,
    f15ve_f15_valuation_at_entry_evebitda_21d_jerk_v026_signal,
    f15ve_f15_valuation_at_entry_evebitda_63d_jerk_v027_signal,
    f15ve_f15_valuation_at_entry_evebitda_63d_jerk_v028_signal,
    f15ve_f15_valuation_at_entry_evebitda_252d_jerk_v029_signal,
    f15ve_f15_valuation_at_entry_evebitda_252d_jerk_v030_signal,
    f15ve_f15_valuation_at_entry_evebitda_504d_jerk_v031_signal,
    f15ve_f15_valuation_at_entry_evebitda_504d_jerk_v032_signal,
    f15ve_f15_valuation_at_entry_evebit_63d_jerk_v033_signal,
    f15ve_f15_valuation_at_entry_evebit_252d_jerk_v034_signal,
    f15ve_f15_valuation_at_entry_evebit_504d_jerk_v035_signal,
    f15ve_f15_valuation_at_entry_evrev_63d_jerk_v036_signal,
    f15ve_f15_valuation_at_entry_evrev_252d_jerk_v037_signal,
    f15ve_f15_valuation_at_entry_evrev_504d_jerk_v038_signal,
    f15ve_f15_valuation_at_entry_evfcf_63d_jerk_v039_signal,
    f15ve_f15_valuation_at_entry_evfcf_252d_jerk_v040_signal,
    f15ve_f15_valuation_at_entry_evfcf_504d_jerk_v041_signal,
    f15ve_f15_valuation_at_entry_evncfo_63d_jerk_v042_signal,
    f15ve_f15_valuation_at_entry_evncfo_252d_jerk_v043_signal,
    f15ve_f15_valuation_at_entry_evgp_63d_jerk_v044_signal,
    f15ve_f15_valuation_at_entry_evgp_252d_jerk_v045_signal,
    f15ve_f15_valuation_at_entry_pfcf_63d_jerk_v046_signal,
    f15ve_f15_valuation_at_entry_pfcf_252d_jerk_v047_signal,
    f15ve_f15_valuation_at_entry_pfcf_504d_jerk_v048_signal,
    f15ve_f15_valuation_at_entry_pncfo_63d_jerk_v049_signal,
    f15ve_f15_valuation_at_entry_pncfo_252d_jerk_v050_signal,
    f15ve_f15_valuation_at_entry_pgp_63d_jerk_v051_signal,
    f15ve_f15_valuation_at_entry_pgp_252d_jerk_v052_signal,
    f15ve_f15_valuation_at_entry_pgp_504d_jerk_v053_signal,
    f15ve_f15_valuation_at_entry_popinc_63d_jerk_v054_signal,
    f15ve_f15_valuation_at_entry_popinc_252d_jerk_v055_signal,
    f15ve_f15_valuation_at_entry_popinc_504d_jerk_v056_signal,
    f15ve_f15_valuation_at_entry_eyield_63d_jerk_v057_signal,
    f15ve_f15_valuation_at_entry_eyield_252d_jerk_v058_signal,
    f15ve_f15_valuation_at_entry_syield_252d_jerk_v059_signal,
    f15ve_f15_valuation_at_entry_fcfyield_252d_jerk_v060_signal,
    f15ve_f15_valuation_at_entry_ebitdayield_252d_jerk_v061_signal,
    f15ve_f15_valuation_at_entry_gpyield_252d_jerk_v062_signal,
    f15ve_f15_valuation_at_entry_ncfoyield_252d_jerk_v063_signal,
    f15ve_f15_valuation_at_entry_evcapex_63d_jerk_v064_signal,
    f15ve_f15_valuation_at_entry_evcapex_252d_jerk_v065_signal,
    f15ve_f15_valuation_at_entry_pcapex_63d_jerk_v066_signal,
    f15ve_f15_valuation_at_entry_pcapex_252d_jerk_v067_signal,
    f15ve_f15_valuation_at_entry_passet_252d_jerk_v068_signal,
    f15ve_f15_valuation_at_entry_passet_504d_jerk_v069_signal,
    f15ve_f15_valuation_at_entry_evassets_252d_jerk_v070_signal,
    f15ve_f15_valuation_at_entry_pretearn_252d_jerk_v071_signal,
    f15ve_f15_valuation_at_entry_evequity_252d_jerk_v072_signal,
    f15ve_f15_valuation_at_entry_evdebt_252d_jerk_v073_signal,
    f15ve_f15_valuation_at_entry_evpershare_252d_jerk_v074_signal,
    f15ve_f15_valuation_at_entry_evwc_252d_jerk_v075_signal,
    f15ve_f15_valuation_at_entry_pelevdev_63d_jerk_v076_signal,
    f15ve_f15_valuation_at_entry_pelevdev_252d_jerk_v077_signal,
    f15ve_f15_valuation_at_entry_pblevdev_252d_jerk_v078_signal,
    f15ve_f15_valuation_at_entry_pslevdev_252d_jerk_v079_signal,
    f15ve_f15_valuation_at_entry_evebitdadev_252d_jerk_v080_signal,
    f15ve_f15_valuation_at_entry_pelevelz_252d_jerk_v081_signal,
    f15ve_f15_valuation_at_entry_pelevelz_504d_jerk_v082_signal,
    f15ve_f15_valuation_at_entry_evebitdaz_252d_jerk_v083_signal,
    f15ve_f15_valuation_at_entry_pblevelz_252d_jerk_v084_signal,
    f15ve_f15_valuation_at_entry_pslevelz_252d_jerk_v085_signal,
    f15ve_f15_valuation_at_entry_peraw_21d_jerk_v086_signal,
    f15ve_f15_valuation_at_entry_peraw_63d_jerk_v087_signal,
    f15ve_f15_valuation_at_entry_pbraw_63d_jerk_v088_signal,
    f15ve_f15_valuation_at_entry_pbraw_252d_jerk_v089_signal,
    f15ve_f15_valuation_at_entry_psraw_252d_jerk_v090_signal,
    f15ve_f15_valuation_at_entry_evebitdaraw_252d_jerk_v091_signal,
    f15ve_f15_valuation_at_entry_evebitraw_252d_jerk_v092_signal,
    f15ve_f15_valuation_at_entry_pe_to_pb_252d_jerk_v093_signal,
    f15ve_f15_valuation_at_entry_evebitda_to_pe_252d_jerk_v094_signal,
    f15ve_f15_valuation_at_entry_pb_to_ps_252d_jerk_v095_signal,
    f15ve_f15_valuation_at_entry_evebit_to_evebitda_252d_jerk_v096_signal,
    f15ve_f15_valuation_at_entry_pe_recent_vs_trend_jerk_v097_signal,
    f15ve_f15_valuation_at_entry_ps_recent_vs_trend_jerk_v098_signal,
    f15ve_f15_valuation_at_entry_evebitda_recent_vs_trend_jerk_v099_signal,
    f15ve_f15_valuation_at_entry_blendedval_252d_jerk_v100_signal,
    f15ve_f15_valuation_at_entry_blendedevmult_252d_jerk_v101_signal,
    f15ve_f15_valuation_at_entry_pelevpos_504d_jerk_v102_signal,
    f15ve_f15_valuation_at_entry_pblevpos_504d_jerk_v103_signal,
    f15ve_f15_valuation_at_entry_evebitdapos_504d_jerk_v104_signal,
    f15ve_f15_valuation_at_entry_perelhi_504d_jerk_v105_signal,
    f15ve_f15_valuation_at_entry_pbrelhi_504d_jerk_v106_signal,
    f15ve_f15_valuation_at_entry_psrelhi_504d_jerk_v107_signal,
    f15ve_f15_valuation_at_entry_evebitdarelhi_504d_jerk_v108_signal,
    f15ve_f15_valuation_at_entry_richpe_count_252d_jerk_v109_signal,
    f15ve_f15_valuation_at_entry_richevebitda_count_252d_jerk_v110_signal,
    f15ve_f15_valuation_at_entry_cheapevebitda_count_252d_jerk_v111_signal,
    f15ve_f15_valuation_at_entry_cheappe_count_504d_jerk_v112_signal,
    f15ve_f15_valuation_at_entry_epsyield_252d_jerk_v113_signal,
    f15ve_f15_valuation_at_entry_epsxprice_21d_jerk_v114_signal,
    f15ve_f15_valuation_at_entry_cheapcomp_252d_jerk_v115_signal,
    f15ve_f15_valuation_at_entry_evintens_252d_jerk_v116_signal,
    f15ve_f15_valuation_at_entry_pwc_252d_jerk_v117_signal,
    f15ve_f15_valuation_at_entry_netdebt_252d_jerk_v118_signal,
    f15ve_f15_valuation_at_entry_pricepershare_252d_jerk_v119_signal,
    f15ve_f15_valuation_at_entry_evcomp_252d_jerk_v120_signal,
    f15ve_f15_valuation_at_entry_lowmult_252d_jerk_v121_signal,
    f15ve_f15_valuation_at_entry_highevmult_252d_jerk_v122_signal,
    f15ve_f15_valuation_at_entry_logpe_252d_jerk_v123_signal,
    f15ve_f15_valuation_at_entry_logevebitda_252d_jerk_v124_signal,
    f15ve_f15_valuation_at_entry_pesq_21d_jerk_v125_signal,
    f15ve_f15_valuation_at_entry_pesq_252d_jerk_v126_signal,
    f15ve_f15_valuation_at_entry_evebitdasq_252d_jerk_v127_signal,
    f15ve_f15_valuation_at_entry_pbsq_252d_jerk_v128_signal,
    f15ve_f15_valuation_at_entry_pssq_252d_jerk_v129_signal,
    f15ve_f15_valuation_at_entry_evebitda_ema_21d_jerk_v130_signal,
    f15ve_f15_valuation_at_entry_pe_ema_63d_jerk_v131_signal,
    f15ve_f15_valuation_at_entry_pb_ema_252d_jerk_v132_signal,
    f15ve_f15_valuation_at_entry_ps_ema_252d_jerk_v133_signal,
    f15ve_f15_valuation_at_entry_evebitda_ema_252d_jerk_v134_signal,
    f15ve_f15_valuation_at_entry_pe_xshares_252d_jerk_v135_signal,
    f15ve_f15_valuation_at_entry_evebitda_xassets_252d_jerk_v136_signal,
    f15ve_f15_valuation_at_entry_pb_xequity_252d_jerk_v137_signal,
    f15ve_f15_valuation_at_entry_eyield_21d_jerk_v138_signal,
    f15ve_f15_valuation_at_entry_syield_21d_jerk_v139_signal,
    f15ve_f15_valuation_at_entry_fcfyield_21d_jerk_v140_signal,
    f15ve_f15_valuation_at_entry_ebitdayield_21d_jerk_v141_signal,
    f15ve_f15_valuation_at_entry_netdebt_ebitda_252d_jerk_v142_signal,
    f15ve_f15_valuation_at_entry_fcfyield_ev_252d_jerk_v143_signal,
    f15ve_f15_valuation_at_entry_gpyield_mkt_252d_jerk_v144_signal,
    f15ve_f15_valuation_at_entry_opincyield_mkt_252d_jerk_v145_signal,
    f15ve_f15_valuation_at_entry_ncfoyield_mkt_252d_jerk_v146_signal,
    f15ve_f15_valuation_at_entry_retearn_equity_252d_jerk_v147_signal,
    f15ve_f15_valuation_at_entry_ev_ebitdamcapex_252d_jerk_v148_signal,
    f15ve_f15_valuation_at_entry_ev_intexp_252d_jerk_v149_signal,
    f15ve_f15_valuation_at_entry_fullcomp_252d_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F15_VALUATION_AT_ENTRY_REGISTRY_JERK = REGISTRY


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
    assert n_features == 150, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f15_valuation_at_entry_3rd_derivatives_001_150_claude: {n_features} features pass")
