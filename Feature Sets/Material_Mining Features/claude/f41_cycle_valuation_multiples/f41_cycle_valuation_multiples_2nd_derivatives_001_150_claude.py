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


def _median(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).median()


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


def _rmax(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rmin(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rank(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).rank(pct=True) - 0.5


def _madz(s, w):
    med = s.rolling(w, min_periods=max(1, w // 2)).median()
    mad = (s - med).abs().rolling(w, min_periods=max(1, w // 2)).median()
    return (s - med) / (1.4826 * mad).replace(0, np.nan)


# ===== folder domain primitives (cycle VALUATION multiples & yields ONLY) =====
def _f41_ev_ebitda(ev, ebitda):
    return ev / ebitda.where(ebitda > 0, np.nan)


def _f41_ev_sales(ev, revenue):
    return ev / revenue.where(revenue > 0, np.nan)


def _f41_mcap_ebitda(marketcap, ebitda):
    return marketcap / ebitda.where(ebitda > 0, np.nan)


def _f41_mcap_sales(marketcap, revenue):
    return marketcap / revenue.where(revenue > 0, np.nan)


def _f41_ebitda_yield(ebitda, ev):
    return ebitda.where(ebitda > 0, np.nan) / ev.replace(0, np.nan)


def _f41_sales_yield(revenue, ev):
    return revenue.where(revenue > 0, np.nan) / ev.replace(0, np.nan)


def _f41_earnings_yield(pe):
    return 1.0 / pe.where(pe > 0, np.nan)


def _f41_cycle_pos(mult, w):
    lo = mult.rolling(w, min_periods=max(1, w // 2)).min()
    hi = mult.rolling(w, min_periods=max(1, w // 2)).max()
    return (mult - lo) / (hi - lo).replace(0, np.nan)


def _f41_midgap(mult, w):
    med = mult.rolling(w, min_periods=max(1, w // 2)).median()
    return np.log(mult.replace(0, np.nan) / med.replace(0, np.nan))


def _f41_lowgap(mult, w):
    return mult / mult.rolling(w, min_periods=max(1, w // 2)).min().replace(0, np.nan) - 1.0


def _f41_peakgap(mult, w):
    return np.log(mult.replace(0, np.nan) / _rmax(mult, w).replace(0, np.nan))


def f41cv_f41_cycle_valuation_multiples_evebdrep_lvl_1d_slope_v001_signal(evebitda):
    m = evebitda.where(evebitda > 0, np.nan)
    b = m
    d = b - b.shift(5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f41cv_f41_cycle_valuation_multiples_evebdrep_robcheapz252_252d_slope_v002_signal(evebitda):
    m = evebitda.where(evebitda > 0, np.nan)
    b = -_madz(m, 252)
    d = b - b.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f41cv_f41_cycle_valuation_multiples_evebdrep_robcheapz504_504d_slope_v003_signal(evebitda):
    m = evebitda.where(evebitda > 0, np.nan)
    b = -_madz(m, 504)
    d = b - b.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f41cv_f41_cycle_valuation_multiples_evebdrep_midgap1260_1260d_slope_v004_signal(evebitda):
    m = evebitda.where(evebitda > 0, np.nan)
    b = -_f41_midgap(m, 1260)
    d = b - b.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f41cv_f41_cycle_valuation_multiples_evebdrep_cyclepos1260_1260d_slope_v005_signal(evebitda):
    m = evebitda.where(evebitda > 0, np.nan)
    b = _f41_cycle_pos(m, 1260)
    d = b - b.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f41cv_f41_cycle_valuation_multiples_evebdrep_reratio252_252d_slope_v006_signal(evebitda):
    m = evebitda.where(evebitda > 0, np.nan)
    b = m / _mean(m, 252).replace(0, np.nan)
    d = b - b.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f41cv_f41_cycle_valuation_multiples_evebdrep_chg63_63d_slope_v007_signal(evebitda):
    m = evebitda.where(evebitda > 0, np.nan)
    b = np.log(m / m.shift(63))
    d = b - b.shift(5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f41cv_f41_cycle_valuation_multiples_evebd_cheaprnk252_252d_slope_v008_signal(ev, ebitda):
    m = _f41_ev_ebitda(ev, ebitda)
    b = -_rank(m, 252)
    d = b - b.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f41cv_f41_cycle_valuation_multiples_evebd_cheaprnk504_504d_slope_v009_signal(ev, ebitda):
    m = _f41_ev_ebitda(ev, ebitda)
    b = -_rank(m, 504)
    d = b - b.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f41cv_f41_cycle_valuation_multiples_evebd_repgap_1d_slope_v010_signal(ev, ebitda, evebitda):
    m = _f41_ev_ebitda(ev, ebitda)
    r = evebitda.where(evebitda > 0, np.nan)
    b = np.log(m.replace(0, np.nan) / r.replace(0, np.nan))
    d = b - b.shift(5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f41cv_f41_cycle_valuation_multiples_evebd_reratio252_252d_slope_v011_signal(ev, ebitda):
    m = _f41_ev_ebitda(ev, ebitda)
    b = m / _mean(m, 252).replace(0, np.nan)
    d = b - b.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f41cv_f41_cycle_valuation_multiples_ebdyld_chg126_126d_slope_v012_signal(ebitda, ev):
    y = _f41_ebitda_yield(ebitda, ev)
    b = y - y.shift(126)
    d = b - b.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f41cv_f41_cycle_valuation_multiples_ebdyld_highstreak252_252d_slope_v013_signal(ebitda, ev):
    y = _f41_ebitda_yield(ebitda, ev)
    rich = (y > _median(y, 252)).astype(float)
    b = rich.rolling(126, min_periods=63).sum() / 126.0
    d = b - b.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f41cv_f41_cycle_valuation_multiples_ebdyld_vol252_252d_slope_v014_signal(ebitda, ev):
    y = _f41_ebitda_yield(ebitda, ev)
    b = _std(y - y.shift(21), 252)
    d = b - b.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f41cv_f41_cycle_valuation_multiples_ebdyld_accel126_126d_slope_v015_signal(ebitda, ev):
    y = _f41_ebitda_yield(ebitda, ev)
    g = y - y.shift(63)
    b = g - g.shift(63)
    d = b - b.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f41cv_f41_cycle_valuation_multiples_pe_lvl_1d_slope_v016_signal(pe):
    m = pe.where(pe > 0, np.nan)
    b = m
    d = b - b.shift(5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f41cv_f41_cycle_valuation_multiples_pe_cheapz252_252d_slope_v017_signal(pe):
    m = pe.where(pe > 0, np.nan)
    b = -_z(m, 252)
    d = b - b.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f41cv_f41_cycle_valuation_multiples_pe_cheapz504_504d_slope_v018_signal(pe):
    m = pe.where(pe > 0, np.nan)
    b = -_z(m, 504)
    d = b - b.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f41cv_f41_cycle_valuation_multiples_pe_cheaprnk126_126d_slope_v019_signal(pe):
    m = pe.where(pe > 0, np.nan)
    b = -_rank(m, 126)
    d = b - b.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f41cv_f41_cycle_valuation_multiples_pe_midgap504_504d_slope_v020_signal(pe):
    m = pe.where(pe > 0, np.nan)
    b = -_f41_midgap(m, 504)
    d = b - b.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f41cv_f41_cycle_valuation_multiples_pe_cycleposmom1260_1260d_slope_v021_signal(pe):
    m = pe.where(pe > 0, np.nan)
    cp = _f41_cycle_pos(m, 1260)
    b = cp - cp.shift(126)
    d = b - b.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f41cv_f41_cycle_valuation_multiples_pe_lowgapmom504_504d_slope_v022_signal(pe):
    m = pe.where(pe > 0, np.nan)
    g = _f41_lowgap(m, 504)
    b = g - g.shift(63)
    d = b - b.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f41cv_f41_cycle_valuation_multiples_pe_voloverlvl252_252d_slope_v023_signal(pe):
    m = pe.where(pe > 0, np.nan)
    b = _std(np.log(m / m.shift(21)), 252)
    d = b - b.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f41cv_f41_cycle_valuation_multiples_pe_chg63_63d_slope_v024_signal(pe):
    m = pe.where(pe > 0, np.nan)
    b = np.log(m / m.shift(63))
    d = b - b.shift(5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f41cv_f41_cycle_valuation_multiples_pe_chg252_252d_slope_v025_signal(pe):
    m = pe.where(pe > 0, np.nan)
    b = np.log(m / m.shift(252))
    d = b - b.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f41cv_f41_cycle_valuation_multiples_pe_robcheapz252_252d_slope_v026_signal(pe):
    m = pe.where(pe > 0, np.nan)
    b = -_madz(m, 252)
    d = b - b.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f41cv_f41_cycle_valuation_multiples_peXevebd_zspr252_252d_slope_v027_signal(pe, evebitda):
    p = pe.where(pe > 0, np.nan)
    e = evebitda.where(evebitda > 0, np.nan)
    b = _z(p, 252) - _z(e, 252)
    d = b - b.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f41cv_f41_cycle_valuation_multiples_pe_cheapstreak252_252d_slope_v028_signal(pe):
    m = pe.where(pe > 0, np.nan)
    cheap = (m < _median(m, 252)).astype(float)
    b = cheap.rolling(126, min_periods=63).sum() / 126.0
    d = b - b.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f41cv_f41_cycle_valuation_multiples_pe_accel126_126d_slope_v029_signal(pe):
    m = pe.where(pe > 0, np.nan)
    g = np.log(m / m.shift(63))
    b = g - g.shift(63)
    d = b - b.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f41cv_f41_cycle_valuation_multiples_evebitrep_lvl_1d_slope_v030_signal(evebit):
    m = evebit.where(evebit > 0, np.nan)
    b = m
    d = b - b.shift(5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f41cv_f41_cycle_valuation_multiples_evebitrep_cheapz252_252d_slope_v031_signal(evebit):
    m = evebit.where(evebit > 0, np.nan)
    b = -_z(m, 252)
    d = b - b.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f41cv_f41_cycle_valuation_multiples_evebitrep_cheapz504_504d_slope_v032_signal(evebit):
    m = evebit.where(evebit > 0, np.nan)
    b = -_z(m, 504)
    d = b - b.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f41cv_f41_cycle_valuation_multiples_evebitrep_cheaprnk252_252d_slope_v033_signal(evebit):
    m = evebit.where(evebit > 0, np.nan)
    b = -_rank(m, 252)
    d = b - b.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f41cv_f41_cycle_valuation_multiples_evebitrep_midgap504_504d_slope_v034_signal(evebit):
    m = evebit.where(evebit > 0, np.nan)
    b = -_f41_midgap(m, 504)
    d = b - b.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f41cv_f41_cycle_valuation_multiples_evebitrep_cyclepos1260_1260d_slope_v035_signal(evebit):
    m = evebit.where(evebit > 0, np.nan)
    b = _f41_cycle_pos(m, 1260)
    d = b - b.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f41cv_f41_cycle_valuation_multiples_evebitrep_dearstreak252_252d_slope_v036_signal(evebit):
    m = evebit.where(evebit > 0, np.nan)
    dear = (m > _median(m, 252)).astype(float)
    b = dear.rolling(126, min_periods=63).sum() / 126.0
    d = b - b.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f41cv_f41_cycle_valuation_multiples_evebitrep_peakgap1260_1260d_slope_v037_signal(evebit):
    m = evebit.where(evebit > 0, np.nan)
    b = _f41_peakgap(m, 1260)
    d = b - b.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f41cv_f41_cycle_valuation_multiples_evebitrep_chg126_126d_slope_v038_signal(evebit):
    m = evebit.where(evebit > 0, np.nan)
    b = np.log(m / m.shift(126))
    d = b - b.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f41cv_f41_cycle_valuation_multiples_ebitebdwedge_lvl_1d_slope_v039_signal(evebit, evebitda):
    a = evebit.where(evebit > 0, np.nan)
    e = evebitda.where(evebitda > 0, np.nan)
    b = np.log(a.replace(0, np.nan) / e.replace(0, np.nan))
    d = b - b.shift(5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f41cv_f41_cycle_valuation_multiples_ebitebdwedge_z252_252d_slope_v040_signal(evebit, evebitda):
    a = evebit.where(evebit > 0, np.nan)
    e = evebitda.where(evebitda > 0, np.nan)
    w = np.log(a.replace(0, np.nan) / e.replace(0, np.nan))
    b = _z(w, 252)
    d = b - b.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f41cv_f41_cycle_valuation_multiples_ps_lvl_1d_slope_v041_signal(ps):
    m = ps.where(ps > 0, np.nan)
    b = m
    d = b - b.shift(5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f41cv_f41_cycle_valuation_multiples_ps_cheapz252_252d_slope_v042_signal(ps):
    m = ps.where(ps > 0, np.nan)
    b = -_z(m, 252)
    d = b - b.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f41cv_f41_cycle_valuation_multiples_ps_robcheapz504_504d_slope_v043_signal(ps):
    m = ps.where(ps > 0, np.nan)
    b = -_madz(m, 504)
    d = b - b.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f41cv_f41_cycle_valuation_multiples_ps_cheaprnk252_252d_slope_v044_signal(ps):
    m = ps.where(ps > 0, np.nan)
    b = -_rank(m, 252)
    d = b - b.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f41cv_f41_cycle_valuation_multiples_ps_midgapmom504_504d_slope_v045_signal(ps):
    m = ps.where(ps > 0, np.nan)
    g = _f41_midgap(m, 504)
    b = g - g.shift(63)
    d = b - b.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f41cv_f41_cycle_valuation_multiples_ps_peakgap1260_1260d_slope_v046_signal(ps):
    m = ps.where(ps > 0, np.nan)
    b = _f41_peakgap(m, 1260)
    d = b - b.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f41cv_f41_cycle_valuation_multiples_ps_chg63_63d_slope_v047_signal(ps):
    m = ps.where(ps > 0, np.nan)
    b = np.log(m / m.shift(63))
    d = b - b.shift(5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f41cv_f41_cycle_valuation_multiples_ps_chg252_252d_slope_v048_signal(ps):
    m = ps.where(ps > 0, np.nan)
    b = np.log(m / m.shift(252))
    d = b - b.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f41cv_f41_cycle_valuation_multiples_salyld_lvl_1d_slope_v049_signal(revenue, ev):
    y = _f41_sales_yield(revenue, ev)
    b = y
    d = b - b.shift(5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f41cv_f41_cycle_valuation_multiples_salyld_richz252_252d_slope_v050_signal(revenue, ev):
    y = _f41_sales_yield(revenue, ev)
    b = _z(y, 252)
    d = b - b.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f41cv_f41_cycle_valuation_multiples_salyld_midgap504_504d_slope_v051_signal(revenue, ev):
    y = _f41_sales_yield(revenue, ev)
    b = _f41_midgap(y, 504)
    d = b - b.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f41cv_f41_cycle_valuation_multiples_salyld_chg126_126d_slope_v052_signal(revenue, ev):
    y = _f41_sales_yield(revenue, ev)
    b = y - y.shift(126)
    d = b - b.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f41cv_f41_cycle_valuation_multiples_mcaprev_lvl_1d_slope_v053_signal(marketcap, revenue):
    m = _f41_mcap_sales(marketcap, revenue)
    b = m
    d = b - b.shift(5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f41cv_f41_cycle_valuation_multiples_mcaprev_cheaprnk504_504d_slope_v054_signal(marketcap, revenue):
    m = _f41_mcap_sales(marketcap, revenue)
    b = -_rank(m, 504)
    d = b - b.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f41cv_f41_cycle_valuation_multiples_mcaprev_midgap1260_1260d_slope_v055_signal(marketcap, revenue):
    m = _f41_mcap_sales(marketcap, revenue)
    b = -_f41_midgap(m, 1260)
    d = b - b.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f41cv_f41_cycle_valuation_multiples_mcaprev_chg126_126d_slope_v056_signal(marketcap, revenue):
    m = _f41_mcap_sales(marketcap, revenue)
    b = np.log(m / m.shift(126))
    d = b - b.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f41cv_f41_cycle_valuation_multiples_mcapebd_lvl_1d_slope_v057_signal(marketcap, ebitda):
    m = _f41_mcap_ebitda(marketcap, ebitda)
    b = m
    d = b - b.shift(5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f41cv_f41_cycle_valuation_multiples_mcapebd_cheaprnk252_252d_slope_v058_signal(marketcap, ebitda):
    m = _f41_mcap_ebitda(marketcap, ebitda)
    b = -_rank(m, 252)
    d = b - b.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f41cv_f41_cycle_valuation_multiples_mcapebd_cheapz504_504d_slope_v059_signal(marketcap, ebitda):
    m = _f41_mcap_ebitda(marketcap, ebitda)
    b = -_z(m, 504)
    d = b - b.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f41cv_f41_cycle_valuation_multiples_mcapebd_chg126_126d_slope_v060_signal(marketcap, ebitda):
    m = _f41_mcap_ebitda(marketcap, ebitda)
    b = np.log(m / m.shift(126))
    d = b - b.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f41cv_f41_cycle_valuation_multiples_evmcap_lvl_1d_slope_v061_signal(ev, marketcap):
    m = ev / marketcap.replace(0, np.nan)
    b = m
    d = b - b.shift(5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f41cv_f41_cycle_valuation_multiples_evmcap_z252_252d_slope_v062_signal(ev, marketcap):
    m = ev / marketcap.replace(0, np.nan)
    b = _z(m, 252)
    d = b - b.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f41cv_f41_cycle_valuation_multiples_evmcap_chg126_126d_slope_v063_signal(ev, marketcap):
    m = ev / marketcap.replace(0, np.nan)
    b = m - m.shift(126)
    d = b - b.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f41cv_f41_cycle_valuation_multiples_evmcap_cheaprnk504_504d_slope_v064_signal(ev, marketcap):
    m = ev / marketcap.replace(0, np.nan)
    b = -_rank(m, 504)
    d = b - b.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f41cv_f41_cycle_valuation_multiples_evsXevebd_rnkspr252_252d_slope_v065_signal(ev, revenue, ebitda):
    es = _f41_ev_sales(ev, revenue)
    ee = _f41_ev_ebitda(ev, ebitda)
    b = _rank(es, 252) - _rank(ee, 252)
    d = b - b.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f41cv_f41_cycle_valuation_multiples_peXevebit_rnkspr252_252d_slope_v066_signal(pe, evebit):
    p = pe.where(pe > 0, np.nan)
    e = evebit.where(evebit > 0, np.nan)
    b = _rank(p, 252) - _rank(e, 252)
    d = b - b.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f41cv_f41_cycle_valuation_multiples_psXevebd_zspr252_252d_slope_v067_signal(ps, evebitda):
    p = ps.where(ps > 0, np.nan)
    e = evebitda.where(evebitda > 0, np.nan)
    b = _z(p, 252) - _z(e, 252)
    d = b - b.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f41cv_f41_cycle_valuation_multiples_blend_cheaprnk252_252d_slope_v068_signal(evebitda, pe, ps):
    e = -_rank(evebitda.where(evebitda > 0, np.nan), 252)
    p = -_rank(pe.where(pe > 0, np.nan), 252)
    s = -_rank(ps.where(ps > 0, np.nan), 252)
    b = pd.concat([e, p, s], axis=1).mean(axis=1)
    d = b - b.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f41cv_f41_cycle_valuation_multiples_blend_cheaprnk504_504d_slope_v069_signal(evebit, pe, ps):
    e = -_rank(evebit.where(evebit > 0, np.nan), 504)
    p = -_rank(pe.where(pe > 0, np.nan), 504)
    s = -_rank(ps.where(ps > 0, np.nan), 504)
    b = pd.concat([e, p, s], axis=1).mean(axis=1)
    d = b - b.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f41cv_f41_cycle_valuation_multiples_blend_cheapz252_252d_slope_v070_signal(evebitda, evebit, pe):
    e1 = -_z(evebitda.where(evebitda > 0, np.nan), 252)
    e2 = -_z(evebit.where(evebit > 0, np.nan), 252)
    p = -_z(pe.where(pe > 0, np.nan), 252)
    b = pd.concat([e1, e2, p], axis=1).mean(axis=1)
    d = b - b.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f41cv_f41_cycle_valuation_multiples_blend_midgap504_504d_slope_v071_signal(evebitda, pe, ps):
    e = -_f41_midgap(evebitda.where(evebitda > 0, np.nan), 504)
    p = -_f41_midgap(pe.where(pe > 0, np.nan), 504)
    s = -_f41_midgap(ps.where(ps > 0, np.nan), 504)
    b = pd.concat([e, p, s], axis=1).mean(axis=1)
    d = b - b.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f41cv_f41_cycle_valuation_multiples_multdisp_z252_252d_slope_v072_signal(evebitda, pe, ps):
    e = _z(evebitda.where(evebitda > 0, np.nan), 252)
    p = _z(pe.where(pe > 0, np.nan), 252)
    s = _z(ps.where(ps > 0, np.nan), 252)
    b = pd.concat([e, p, s], axis=1).std(axis=1)
    d = b - b.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f41cv_f41_cycle_valuation_multiples_blendyld_z252_252d_slope_v073_signal(ebitda, revenue, ev):
    ey = _f41_ebitda_yield(ebitda, ev)
    sy = _f41_sales_yield(revenue, ev)
    b = (_z(ey, 252) + _z(sy, 252)) / 2.0
    d = b - b.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f41cv_f41_cycle_valuation_multiples_blend_rerate63_63d_slope_v074_signal(evebitda, pe, ps):
    e = -_z(evebitda.where(evebitda > 0, np.nan), 252)
    p = -_z(pe.where(pe > 0, np.nan), 252)
    s = -_z(ps.where(ps > 0, np.nan), 252)
    c = pd.concat([e, p, s], axis=1).mean(axis=1)
    b = c - c.shift(63)
    d = b - b.shift(5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f41cv_f41_cycle_valuation_multiples_yldgap_eyVsy_252d_slope_v075_signal(pe, revenue, ev):
    ey = _f41_earnings_yield(pe)
    sy = _f41_sales_yield(revenue, ev)
    b = _z(ey, 252) - _z(sy, 252)
    d = b - b.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f41cv_f41_cycle_valuation_multiples_evebdrep_cheapz252_252d_slope_v076_signal(evebitda):
    m = evebitda.where(evebitda > 0, np.nan)
    b = -_z(m, 252)
    d = b - b.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f41cv_f41_cycle_valuation_multiples_evebdrep_cheaprnk252_252d_slope_v077_signal(evebitda):
    m = evebitda.where(evebitda > 0, np.nan)
    b = -_rank(m, 252)
    d = b - b.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f41cv_f41_cycle_valuation_multiples_evebdrep_lowgapmom504_504d_slope_v078_signal(evebitda):
    m = evebitda.where(evebitda > 0, np.nan)
    g = _f41_lowgap(m, 504)
    b = g - g.shift(63)
    d = b - b.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f41cv_f41_cycle_valuation_multiples_evebdrep_chg126_126d_slope_v079_signal(evebitda):
    m = evebitda.where(evebitda > 0, np.nan)
    b = np.log(m / m.shift(126))
    d = b - b.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f41cv_f41_cycle_valuation_multiples_evebdrep_reratio126_126d_slope_v080_signal(evebitda):
    m = evebitda.where(evebitda > 0, np.nan)
    b = m / _mean(m, 126).replace(0, np.nan)
    d = b - b.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f41cv_f41_cycle_valuation_multiples_evebdrep_cheapstreak252_252d_slope_v081_signal(evebitda):
    m = evebitda.where(evebitda > 0, np.nan)
    cheap = (m < _median(m, 252)).astype(float)
    b = cheap.rolling(126, min_periods=63).sum() / 126.0
    d = b - b.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f41cv_f41_cycle_valuation_multiples_evebdrep_vol252_252d_slope_v082_signal(evebitda):
    m = evebitda.where(evebitda > 0, np.nan)
    b = _std(np.log(m / m.shift(21)), 252)
    d = b - b.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f41cv_f41_cycle_valuation_multiples_evebd_cheapz252_252d_slope_v083_signal(ev, ebitda):
    m = _f41_ev_ebitda(ev, ebitda)
    b = -_z(m, 252)
    d = b - b.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f41cv_f41_cycle_valuation_multiples_evebd_robcheapz504_504d_slope_v084_signal(ev, ebitda):
    m = _f41_ev_ebitda(ev, ebitda)
    b = -_madz(m, 504)
    d = b - b.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f41cv_f41_cycle_valuation_multiples_evebd_midgap1260_1260d_slope_v085_signal(ev, ebitda):
    m = _f41_ev_ebitda(ev, ebitda)
    b = -_f41_midgap(m, 1260)
    d = b - b.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f41cv_f41_cycle_valuation_multiples_evebd_chg252_252d_slope_v086_signal(ev, ebitda):
    m = _f41_ev_ebitda(ev, ebitda)
    b = np.log(m / m.shift(252))
    d = b - b.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f41cv_f41_cycle_valuation_multiples_ebdyld_midgapmom504_504d_slope_v087_signal(ebitda, ev):
    y = _f41_ebitda_yield(ebitda, ev)
    g = _f41_midgap(y, 504)
    b = g - g.shift(63)
    d = b - b.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f41cv_f41_cycle_valuation_multiples_ebdyld_chg63_63d_slope_v088_signal(ebitda, ev):
    y = _f41_ebitda_yield(ebitda, ev)
    b = y - y.shift(63)
    d = b - b.shift(5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f41cv_f41_cycle_valuation_multiples_ebdyld_vol126_126d_slope_v089_signal(ebitda, ev):
    y = _f41_ebitda_yield(ebitda, ev)
    b = _std(y - y.shift(21), 126)
    d = b - b.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f41cv_f41_cycle_valuation_multiples_pe_cheaprnk504_504d_slope_v090_signal(pe):
    m = pe.where(pe > 0, np.nan)
    b = -_rank(m, 504)
    d = b - b.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f41cv_f41_cycle_valuation_multiples_pe_reratio504_504d_slope_v091_signal(pe):
    m = pe.where(pe > 0, np.nan)
    b = m / _mean(m, 504).replace(0, np.nan)
    d = b - b.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f41cv_f41_cycle_valuation_multiples_pe_chg126_126d_slope_v092_signal(pe):
    m = pe.where(pe > 0, np.nan)
    b = np.log(m / m.shift(126))
    d = b - b.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f41cv_f41_cycle_valuation_multiples_pe_dearstreak504_504d_slope_v093_signal(pe):
    m = pe.where(pe > 0, np.nan)
    dear = (m > _median(m, 504)).astype(float)
    b = dear.rolling(252, min_periods=126).sum() / 252.0
    d = b - b.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f41cv_f41_cycle_valuation_multiples_evebitrep_robcheapz252_252d_slope_v094_signal(evebit):
    m = evebit.where(evebit > 0, np.nan)
    b = -_madz(m, 252)
    d = b - b.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f41cv_f41_cycle_valuation_multiples_evebitrep_cheaprnk504_504d_slope_v095_signal(evebit):
    m = evebit.where(evebit > 0, np.nan)
    b = -_rank(m, 504)
    d = b - b.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f41cv_f41_cycle_valuation_multiples_evebitrep_midgap1260_1260d_slope_v096_signal(evebit):
    m = evebit.where(evebit > 0, np.nan)
    b = -_f41_midgap(m, 1260)
    d = b - b.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f41cv_f41_cycle_valuation_multiples_evebitrep_reratio504_504d_slope_v097_signal(evebit):
    m = evebit.where(evebit > 0, np.nan)
    b = m / _mean(m, 504).replace(0, np.nan)
    d = b - b.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f41cv_f41_cycle_valuation_multiples_evebitrep_chg63_63d_slope_v098_signal(evebit):
    m = evebit.where(evebit > 0, np.nan)
    b = np.log(m / m.shift(63))
    d = b - b.shift(5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f41cv_f41_cycle_valuation_multiples_evebitrep_accel126_126d_slope_v099_signal(evebit):
    m = evebit.where(evebit > 0, np.nan)
    g = np.log(m / m.shift(63))
    b = g - g.shift(63)
    d = b - b.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f41cv_f41_cycle_valuation_multiples_ebitebdwedge_rnk252_252d_slope_v100_signal(evebit, evebitda):
    a = evebit.where(evebit > 0, np.nan)
    e = evebitda.where(evebitda > 0, np.nan)
    w = np.log(a.replace(0, np.nan) / e.replace(0, np.nan))
    b = _rank(w, 252)
    d = b - b.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f41cv_f41_cycle_valuation_multiples_ebitebdwedge_chg126_126d_slope_v101_signal(evebit, evebitda):
    a = evebit.where(evebit > 0, np.nan)
    e = evebitda.where(evebitda > 0, np.nan)
    w = np.log(a.replace(0, np.nan) / e.replace(0, np.nan))
    b = w - w.shift(126)
    d = b - b.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f41cv_f41_cycle_valuation_multiples_ps_cheapz504_504d_slope_v102_signal(ps):
    m = ps.where(ps > 0, np.nan)
    b = -_z(m, 504)
    d = b - b.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f41cv_f41_cycle_valuation_multiples_ps_cheaprnk504_504d_slope_v103_signal(ps):
    m = ps.where(ps > 0, np.nan)
    b = -_rank(m, 504)
    d = b - b.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f41cv_f41_cycle_valuation_multiples_ps_midgap1260_1260d_slope_v104_signal(ps):
    m = ps.where(ps > 0, np.nan)
    b = -_f41_midgap(m, 1260)
    d = b - b.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f41cv_f41_cycle_valuation_multiples_ps_reratio504_504d_slope_v105_signal(ps):
    m = ps.where(ps > 0, np.nan)
    b = m / _mean(m, 504).replace(0, np.nan)
    d = b - b.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f41cv_f41_cycle_valuation_multiples_ps_chg126_126d_slope_v106_signal(ps):
    m = ps.where(ps > 0, np.nan)
    b = np.log(m / m.shift(126))
    d = b - b.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f41cv_f41_cycle_valuation_multiples_ps_cheapstreak252_252d_slope_v107_signal(ps):
    m = ps.where(ps > 0, np.nan)
    cheap = (m < _median(m, 252)).astype(float)
    b = cheap.rolling(126, min_periods=63).sum() / 126.0
    d = b - b.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f41cv_f41_cycle_valuation_multiples_salyld_rnk252_252d_slope_v108_signal(revenue, ev):
    y = _f41_sales_yield(revenue, ev)
    b = _rank(y, 252)
    d = b - b.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f41cv_f41_cycle_valuation_multiples_salyld_robz504_504d_slope_v109_signal(revenue, ev):
    y = _f41_sales_yield(revenue, ev)
    b = _madz(y, 504)
    d = b - b.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f41cv_f41_cycle_valuation_multiples_psXevebit_rnkspr504_504d_slope_v110_signal(ps, evebit):
    p = ps.where(ps > 0, np.nan)
    e = evebit.where(evebit > 0, np.nan)
    b = _rank(p, 504) - _rank(e, 504)
    d = b - b.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f41cv_f41_cycle_valuation_multiples_salyld_troughgap504_504d_slope_v111_signal(revenue, ev):
    y = _f41_sales_yield(revenue, ev)
    b = np.log(y.replace(0, np.nan) / _rmax(y, 504).replace(0, np.nan))
    d = b - b.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f41cv_f41_cycle_valuation_multiples_mcaprev_robcheapz504_504d_slope_v112_signal(marketcap, revenue):
    m = _f41_mcap_sales(marketcap, revenue)
    b = -_madz(m, 504)
    d = b - b.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f41cv_f41_cycle_valuation_multiples_mcaprev_cheaprnk252_252d_slope_v113_signal(marketcap, revenue):
    m = _f41_mcap_sales(marketcap, revenue)
    b = -_rank(m, 252)
    d = b - b.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f41cv_f41_cycle_valuation_multiples_mcaprev_reratio504_504d_slope_v114_signal(marketcap, revenue):
    m = _f41_mcap_sales(marketcap, revenue)
    b = m / _mean(m, 504).replace(0, np.nan)
    d = b - b.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f41cv_f41_cycle_valuation_multiples_mcaprev_chg63_63d_slope_v115_signal(marketcap, revenue):
    m = _f41_mcap_sales(marketcap, revenue)
    b = np.log(m / m.shift(63))
    d = b - b.shift(5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f41cv_f41_cycle_valuation_multiples_mcapebd_cheapz252_252d_slope_v116_signal(marketcap, ebitda):
    m = _f41_mcap_ebitda(marketcap, ebitda)
    b = -_z(m, 252)
    d = b - b.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f41cv_f41_cycle_valuation_multiples_mcapebd_reratio504_504d_slope_v117_signal(marketcap, ebitda):
    m = _f41_mcap_ebitda(marketcap, ebitda)
    b = m / _mean(m, 504).replace(0, np.nan)
    d = b - b.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f41cv_f41_cycle_valuation_multiples_mcapebd_chg63_63d_slope_v118_signal(marketcap, ebitda):
    m = _f41_mcap_ebitda(marketcap, ebitda)
    b = np.log(m / m.shift(63))
    d = b - b.shift(5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f41cv_f41_cycle_valuation_multiples_evmcap_midgap504_504d_slope_v119_signal(ev, marketcap):
    m = ev / marketcap.replace(0, np.nan)
    b = _f41_midgap(m, 504)
    d = b - b.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f41cv_f41_cycle_valuation_multiples_evmcap_chg63_63d_slope_v120_signal(ev, marketcap):
    m = ev / marketcap.replace(0, np.nan)
    b = m - m.shift(63)
    d = b - b.shift(5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f41cv_f41_cycle_valuation_multiples_evmcap_chg252_252d_slope_v121_signal(ev, marketcap):
    m = ev / marketcap.replace(0, np.nan)
    b = m - m.shift(252)
    d = b - b.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f41cv_f41_cycle_valuation_multiples_evsXevebd_zspr504_504d_slope_v122_signal(ev, revenue, ebitda):
    es = _f41_ev_sales(ev, revenue)
    ee = _f41_ev_ebitda(ev, ebitda)
    b = _z(es, 504) - _z(ee, 504)
    d = b - b.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f41cv_f41_cycle_valuation_multiples_peXps_rnkspr252_252d_slope_v123_signal(pe, ps):
    p = pe.where(pe > 0, np.nan)
    s = ps.where(ps > 0, np.nan)
    b = _rank(p, 252) - _rank(s, 252)
    d = b - b.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f41cv_f41_cycle_valuation_multiples_evebitXevebd_zspr252_252d_slope_v124_signal(evebit, evebitda):
    a = evebit.where(evebit > 0, np.nan)
    e = evebitda.where(evebitda > 0, np.nan)
    b = _z(a, 252) - _z(e, 252)
    d = b - b.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f41cv_f41_cycle_valuation_multiples_mcaprevXmcapebd_rnkspr252_252d_slope_v125_signal(marketcap, revenue, ebitda):
    s = _f41_mcap_sales(marketcap, revenue)
    e = _f41_mcap_ebitda(marketcap, ebitda)
    b = _rank(s, 252) - _rank(e, 252)
    d = b - b.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f41cv_f41_cycle_valuation_multiples_blend_cheapz504_504d_slope_v126_signal(evebitda, pe, ps):
    e = -_z(evebitda.where(evebitda > 0, np.nan), 504)
    p = -_z(pe.where(pe > 0, np.nan), 504)
    s = -_z(ps.where(ps > 0, np.nan), 504)
    b = pd.concat([e, p, s], axis=1).mean(axis=1)
    d = b - b.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f41cv_f41_cycle_valuation_multiples_blend_cheaprnk126_126d_slope_v127_signal(evebitda, evebit, ps):
    e1 = -_rank(evebitda.where(evebitda > 0, np.nan), 126)
    e2 = -_rank(evebit.where(evebit > 0, np.nan), 126)
    s = -_rank(ps.where(ps > 0, np.nan), 126)
    b = pd.concat([e1, e2, s], axis=1).mean(axis=1)
    d = b - b.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f41cv_f41_cycle_valuation_multiples_blend_lowgap504_504d_slope_v128_signal(evebitda, pe, evebit):
    e = _f41_lowgap(evebitda.where(evebitda > 0, np.nan), 504)
    p = _f41_lowgap(pe.where(pe > 0, np.nan), 504)
    a = _f41_lowgap(evebit.where(evebit > 0, np.nan), 504)
    b = pd.concat([e, p, a], axis=1).mean(axis=1)
    d = b - b.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f41cv_f41_cycle_valuation_multiples_blend_peakgap1260_1260d_slope_v129_signal(evebitda, pe, ps):
    e = _f41_peakgap(evebitda.where(evebitda > 0, np.nan), 1260)
    p = _f41_peakgap(pe.where(pe > 0, np.nan), 1260)
    s = _f41_peakgap(ps.where(ps > 0, np.nan), 1260)
    b = pd.concat([e, p, s], axis=1).mean(axis=1)
    d = b - b.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f41cv_f41_cycle_valuation_multiples_blend_midgap1260_1260d_slope_v130_signal(evebit, pe, ps):
    e = -_f41_midgap(evebit.where(evebit > 0, np.nan), 1260)
    p = -_f41_midgap(pe.where(pe > 0, np.nan), 1260)
    s = -_f41_midgap(ps.where(ps > 0, np.nan), 1260)
    b = pd.concat([e, p, s], axis=1).mean(axis=1)
    d = b - b.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f41cv_f41_cycle_valuation_multiples_blend_rerate126_126d_slope_v131_signal(evebitda, pe, ps):
    e = -_z(evebitda.where(evebitda > 0, np.nan), 252)
    p = -_z(pe.where(pe > 0, np.nan), 252)
    s = -_z(ps.where(ps > 0, np.nan), 252)
    c = pd.concat([e, p, s], axis=1).mean(axis=1)
    b = c - c.shift(126)
    d = b - b.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f41cv_f41_cycle_valuation_multiples_multdisp_z504_504d_slope_v132_signal(evebitda, pe, ps):
    e = _z(evebitda.where(evebitda > 0, np.nan), 504)
    p = _z(pe.where(pe > 0, np.nan), 504)
    s = _z(ps.where(ps > 0, np.nan), 504)
    b = pd.concat([e, p, s], axis=1).std(axis=1)
    d = b - b.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f41cv_f41_cycle_valuation_multiples_multdisp_rnk252_252d_slope_v133_signal(evebit, pe, ps):
    e = _rank(evebit.where(evebit > 0, np.nan), 252)
    p = _rank(pe.where(pe > 0, np.nan), 252)
    s = _rank(ps.where(ps > 0, np.nan), 252)
    b = pd.concat([e, p, s], axis=1).std(axis=1)
    d = b - b.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f41cv_f41_cycle_valuation_multiples_blendyld_rnk252_252d_slope_v134_signal(ebitda, revenue, ev):
    ey = _f41_ebitda_yield(ebitda, ev)
    sy = _f41_sales_yield(revenue, ev)
    b = (_rank(ey, 252) + _rank(sy, 252)) / 2.0
    d = b - b.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f41cv_f41_cycle_valuation_multiples_blendyld_disp252_252d_slope_v135_signal(ebitda, revenue, ev):
    ey = _z(_f41_ebitda_yield(ebitda, ev), 252)
    sy = _z(_f41_sales_yield(revenue, ev), 252)
    b = (ey - sy).abs()
    d = b - b.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f41cv_f41_cycle_valuation_multiples_yldgap_ebdVsy_252d_slope_v136_signal(ebitda, revenue, ev):
    ey = _f41_ebitda_yield(ebitda, ev)
    sy = _f41_sales_yield(revenue, ev)
    b = _z(ey, 252) - _z(sy, 252)
    d = b - b.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f41cv_f41_cycle_valuation_multiples_yldgap_eyVebd_252d_slope_v137_signal(pe, ebitda, ev):
    ey = _f41_earnings_yield(pe)
    by = _f41_ebitda_yield(ebitda, ev)
    b = _z(ey, 252) - _z(by, 252)
    d = b - b.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f41cv_f41_cycle_valuation_multiples_blend_cheapyoy_252d_slope_v138_signal(evebitda, pe, ps):
    e = -_z(evebitda.where(evebitda > 0, np.nan), 252)
    p = -_z(pe.where(pe > 0, np.nan), 252)
    s = -_z(ps.where(ps > 0, np.nan), 252)
    c = pd.concat([e, p, s], axis=1).mean(axis=1)
    b = c - c.shift(252)
    d = b - b.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f41cv_f41_cycle_valuation_multiples_evebdVpe_cheapspr504_504d_slope_v139_signal(evebitda, pe):
    e = -_z(evebitda.where(evebitda > 0, np.nan), 504)
    p = -_z(pe.where(pe > 0, np.nan), 504)
    b = e - p
    d = b - b.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f41cv_f41_cycle_valuation_multiples_blend_richlvl252_252d_slope_v140_signal(evebitda, evebit, ps):
    e1 = _z(evebitda.where(evebitda > 0, np.nan), 252)
    e2 = _z(evebit.where(evebit > 0, np.nan), 252)
    s = _z(ps.where(ps > 0, np.nan), 252)
    b = pd.concat([e1, e2, s], axis=1).mean(axis=1)
    d = b - b.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f41cv_f41_cycle_valuation_multiples_evebitrep_lowgapmom504_504d_slope_v141_signal(evebit):
    m = evebit.where(evebit > 0, np.nan)
    g = _f41_lowgap(m, 504)
    b = g - g.shift(63)
    d = b - b.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f41cv_f41_cycle_valuation_multiples_pe_midgapmom504_504d_slope_v142_signal(pe):
    m = pe.where(pe > 0, np.nan)
    g = _f41_midgap(m, 504)
    b = g - g.shift(63)
    d = b - b.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f41cv_f41_cycle_valuation_multiples_evebdrep_midgapmom504_504d_slope_v143_signal(evebitda):
    m = evebitda.where(evebitda > 0, np.nan)
    g = _f41_midgap(m, 504)
    b = g - g.shift(63)
    d = b - b.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f41cv_f41_cycle_valuation_multiples_psVsalyld_zspr252_252d_slope_v144_signal(ps, revenue, ev):
    p = _z(ps.where(ps > 0, np.nan), 252)
    sy = _z(_f41_sales_yield(revenue, ev), 252)
    b = p + sy
    d = b - b.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f41cv_f41_cycle_valuation_multiples_blend_clarcheap252_252d_slope_v145_signal(evebitda, pe, ps):
    e = -_z(evebitda.where(evebitda > 0, np.nan), 252)
    p = -_z(pe.where(pe > 0, np.nan), 252)
    s = -_z(ps.where(ps > 0, np.nan), 252)
    stk = pd.concat([e, p, s], axis=1)
    disp = stk.std(axis=1).replace(0, np.nan)
    b = stk.mean(axis=1) / disp
    d = b - b.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f41cv_f41_cycle_valuation_multiples_evebdrep_peakgapmom1260_1260d_slope_v146_signal(evebitda):
    m = evebitda.where(evebitda > 0, np.nan)
    g = _f41_peakgap(m, 1260)
    b = g - g.shift(126)
    d = b - b.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f41cv_f41_cycle_valuation_multiples_peVevebit_cheapspr252_252d_slope_v147_signal(pe, evebit):
    p = -_z(pe.where(pe > 0, np.nan), 252)
    e = -_z(evebit.where(evebit > 0, np.nan), 252)
    b = p - e
    d = b - b.shift(21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f41cv_f41_cycle_valuation_multiples_blendyld_midgap504_504d_slope_v148_signal(ebitda, revenue, ev):
    ey = _f41_ebitda_yield(ebitda, ev)
    sy = _f41_sales_yield(revenue, ev)
    c = (ey + sy) / 2.0
    b = _f41_midgap(c, 504)
    d = b - b.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f41cv_f41_cycle_valuation_multiples_ps_lowgapmom504_504d_slope_v149_signal(ps):
    m = ps.where(ps > 0, np.nan)
    g = _f41_lowgap(m, 504)
    b = g - g.shift(63)
    d = b - b.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f41cv_f41_cycle_valuation_multiples_blend_cheaphistrnk504_504d_slope_v150_signal(evebitda, pe, ps):
    e = -_z(evebitda.where(evebitda > 0, np.nan), 252)
    p = -_z(pe.where(pe > 0, np.nan), 252)
    s = -_z(ps.where(ps > 0, np.nan), 252)
    c = pd.concat([e, p, s], axis=1).mean(axis=1)
    b = _rank(c, 504)
    d = b - b.shift(63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f41cv_f41_cycle_valuation_multiples_evebdrep_lvl_1d_slope_v001_signal,
    f41cv_f41_cycle_valuation_multiples_evebdrep_robcheapz252_252d_slope_v002_signal,
    f41cv_f41_cycle_valuation_multiples_evebdrep_robcheapz504_504d_slope_v003_signal,
    f41cv_f41_cycle_valuation_multiples_evebdrep_midgap1260_1260d_slope_v004_signal,
    f41cv_f41_cycle_valuation_multiples_evebdrep_cyclepos1260_1260d_slope_v005_signal,
    f41cv_f41_cycle_valuation_multiples_evebdrep_reratio252_252d_slope_v006_signal,
    f41cv_f41_cycle_valuation_multiples_evebdrep_chg63_63d_slope_v007_signal,
    f41cv_f41_cycle_valuation_multiples_evebd_cheaprnk252_252d_slope_v008_signal,
    f41cv_f41_cycle_valuation_multiples_evebd_cheaprnk504_504d_slope_v009_signal,
    f41cv_f41_cycle_valuation_multiples_evebd_repgap_1d_slope_v010_signal,
    f41cv_f41_cycle_valuation_multiples_evebd_reratio252_252d_slope_v011_signal,
    f41cv_f41_cycle_valuation_multiples_ebdyld_chg126_126d_slope_v012_signal,
    f41cv_f41_cycle_valuation_multiples_ebdyld_highstreak252_252d_slope_v013_signal,
    f41cv_f41_cycle_valuation_multiples_ebdyld_vol252_252d_slope_v014_signal,
    f41cv_f41_cycle_valuation_multiples_ebdyld_accel126_126d_slope_v015_signal,
    f41cv_f41_cycle_valuation_multiples_pe_lvl_1d_slope_v016_signal,
    f41cv_f41_cycle_valuation_multiples_pe_cheapz252_252d_slope_v017_signal,
    f41cv_f41_cycle_valuation_multiples_pe_cheapz504_504d_slope_v018_signal,
    f41cv_f41_cycle_valuation_multiples_pe_cheaprnk126_126d_slope_v019_signal,
    f41cv_f41_cycle_valuation_multiples_pe_midgap504_504d_slope_v020_signal,
    f41cv_f41_cycle_valuation_multiples_pe_cycleposmom1260_1260d_slope_v021_signal,
    f41cv_f41_cycle_valuation_multiples_pe_lowgapmom504_504d_slope_v022_signal,
    f41cv_f41_cycle_valuation_multiples_pe_voloverlvl252_252d_slope_v023_signal,
    f41cv_f41_cycle_valuation_multiples_pe_chg63_63d_slope_v024_signal,
    f41cv_f41_cycle_valuation_multiples_pe_chg252_252d_slope_v025_signal,
    f41cv_f41_cycle_valuation_multiples_pe_robcheapz252_252d_slope_v026_signal,
    f41cv_f41_cycle_valuation_multiples_peXevebd_zspr252_252d_slope_v027_signal,
    f41cv_f41_cycle_valuation_multiples_pe_cheapstreak252_252d_slope_v028_signal,
    f41cv_f41_cycle_valuation_multiples_pe_accel126_126d_slope_v029_signal,
    f41cv_f41_cycle_valuation_multiples_evebitrep_lvl_1d_slope_v030_signal,
    f41cv_f41_cycle_valuation_multiples_evebitrep_cheapz252_252d_slope_v031_signal,
    f41cv_f41_cycle_valuation_multiples_evebitrep_cheapz504_504d_slope_v032_signal,
    f41cv_f41_cycle_valuation_multiples_evebitrep_cheaprnk252_252d_slope_v033_signal,
    f41cv_f41_cycle_valuation_multiples_evebitrep_midgap504_504d_slope_v034_signal,
    f41cv_f41_cycle_valuation_multiples_evebitrep_cyclepos1260_1260d_slope_v035_signal,
    f41cv_f41_cycle_valuation_multiples_evebitrep_dearstreak252_252d_slope_v036_signal,
    f41cv_f41_cycle_valuation_multiples_evebitrep_peakgap1260_1260d_slope_v037_signal,
    f41cv_f41_cycle_valuation_multiples_evebitrep_chg126_126d_slope_v038_signal,
    f41cv_f41_cycle_valuation_multiples_ebitebdwedge_lvl_1d_slope_v039_signal,
    f41cv_f41_cycle_valuation_multiples_ebitebdwedge_z252_252d_slope_v040_signal,
    f41cv_f41_cycle_valuation_multiples_ps_lvl_1d_slope_v041_signal,
    f41cv_f41_cycle_valuation_multiples_ps_cheapz252_252d_slope_v042_signal,
    f41cv_f41_cycle_valuation_multiples_ps_robcheapz504_504d_slope_v043_signal,
    f41cv_f41_cycle_valuation_multiples_ps_cheaprnk252_252d_slope_v044_signal,
    f41cv_f41_cycle_valuation_multiples_ps_midgapmom504_504d_slope_v045_signal,
    f41cv_f41_cycle_valuation_multiples_ps_peakgap1260_1260d_slope_v046_signal,
    f41cv_f41_cycle_valuation_multiples_ps_chg63_63d_slope_v047_signal,
    f41cv_f41_cycle_valuation_multiples_ps_chg252_252d_slope_v048_signal,
    f41cv_f41_cycle_valuation_multiples_salyld_lvl_1d_slope_v049_signal,
    f41cv_f41_cycle_valuation_multiples_salyld_richz252_252d_slope_v050_signal,
    f41cv_f41_cycle_valuation_multiples_salyld_midgap504_504d_slope_v051_signal,
    f41cv_f41_cycle_valuation_multiples_salyld_chg126_126d_slope_v052_signal,
    f41cv_f41_cycle_valuation_multiples_mcaprev_lvl_1d_slope_v053_signal,
    f41cv_f41_cycle_valuation_multiples_mcaprev_cheaprnk504_504d_slope_v054_signal,
    f41cv_f41_cycle_valuation_multiples_mcaprev_midgap1260_1260d_slope_v055_signal,
    f41cv_f41_cycle_valuation_multiples_mcaprev_chg126_126d_slope_v056_signal,
    f41cv_f41_cycle_valuation_multiples_mcapebd_lvl_1d_slope_v057_signal,
    f41cv_f41_cycle_valuation_multiples_mcapebd_cheaprnk252_252d_slope_v058_signal,
    f41cv_f41_cycle_valuation_multiples_mcapebd_cheapz504_504d_slope_v059_signal,
    f41cv_f41_cycle_valuation_multiples_mcapebd_chg126_126d_slope_v060_signal,
    f41cv_f41_cycle_valuation_multiples_evmcap_lvl_1d_slope_v061_signal,
    f41cv_f41_cycle_valuation_multiples_evmcap_z252_252d_slope_v062_signal,
    f41cv_f41_cycle_valuation_multiples_evmcap_chg126_126d_slope_v063_signal,
    f41cv_f41_cycle_valuation_multiples_evmcap_cheaprnk504_504d_slope_v064_signal,
    f41cv_f41_cycle_valuation_multiples_evsXevebd_rnkspr252_252d_slope_v065_signal,
    f41cv_f41_cycle_valuation_multiples_peXevebit_rnkspr252_252d_slope_v066_signal,
    f41cv_f41_cycle_valuation_multiples_psXevebd_zspr252_252d_slope_v067_signal,
    f41cv_f41_cycle_valuation_multiples_blend_cheaprnk252_252d_slope_v068_signal,
    f41cv_f41_cycle_valuation_multiples_blend_cheaprnk504_504d_slope_v069_signal,
    f41cv_f41_cycle_valuation_multiples_blend_cheapz252_252d_slope_v070_signal,
    f41cv_f41_cycle_valuation_multiples_blend_midgap504_504d_slope_v071_signal,
    f41cv_f41_cycle_valuation_multiples_multdisp_z252_252d_slope_v072_signal,
    f41cv_f41_cycle_valuation_multiples_blendyld_z252_252d_slope_v073_signal,
    f41cv_f41_cycle_valuation_multiples_blend_rerate63_63d_slope_v074_signal,
    f41cv_f41_cycle_valuation_multiples_yldgap_eyVsy_252d_slope_v075_signal,
    f41cv_f41_cycle_valuation_multiples_evebdrep_cheapz252_252d_slope_v076_signal,
    f41cv_f41_cycle_valuation_multiples_evebdrep_cheaprnk252_252d_slope_v077_signal,
    f41cv_f41_cycle_valuation_multiples_evebdrep_lowgapmom504_504d_slope_v078_signal,
    f41cv_f41_cycle_valuation_multiples_evebdrep_chg126_126d_slope_v079_signal,
    f41cv_f41_cycle_valuation_multiples_evebdrep_reratio126_126d_slope_v080_signal,
    f41cv_f41_cycle_valuation_multiples_evebdrep_cheapstreak252_252d_slope_v081_signal,
    f41cv_f41_cycle_valuation_multiples_evebdrep_vol252_252d_slope_v082_signal,
    f41cv_f41_cycle_valuation_multiples_evebd_cheapz252_252d_slope_v083_signal,
    f41cv_f41_cycle_valuation_multiples_evebd_robcheapz504_504d_slope_v084_signal,
    f41cv_f41_cycle_valuation_multiples_evebd_midgap1260_1260d_slope_v085_signal,
    f41cv_f41_cycle_valuation_multiples_evebd_chg252_252d_slope_v086_signal,
    f41cv_f41_cycle_valuation_multiples_ebdyld_midgapmom504_504d_slope_v087_signal,
    f41cv_f41_cycle_valuation_multiples_ebdyld_chg63_63d_slope_v088_signal,
    f41cv_f41_cycle_valuation_multiples_ebdyld_vol126_126d_slope_v089_signal,
    f41cv_f41_cycle_valuation_multiples_pe_cheaprnk504_504d_slope_v090_signal,
    f41cv_f41_cycle_valuation_multiples_pe_reratio504_504d_slope_v091_signal,
    f41cv_f41_cycle_valuation_multiples_pe_chg126_126d_slope_v092_signal,
    f41cv_f41_cycle_valuation_multiples_pe_dearstreak504_504d_slope_v093_signal,
    f41cv_f41_cycle_valuation_multiples_evebitrep_robcheapz252_252d_slope_v094_signal,
    f41cv_f41_cycle_valuation_multiples_evebitrep_cheaprnk504_504d_slope_v095_signal,
    f41cv_f41_cycle_valuation_multiples_evebitrep_midgap1260_1260d_slope_v096_signal,
    f41cv_f41_cycle_valuation_multiples_evebitrep_reratio504_504d_slope_v097_signal,
    f41cv_f41_cycle_valuation_multiples_evebitrep_chg63_63d_slope_v098_signal,
    f41cv_f41_cycle_valuation_multiples_evebitrep_accel126_126d_slope_v099_signal,
    f41cv_f41_cycle_valuation_multiples_ebitebdwedge_rnk252_252d_slope_v100_signal,
    f41cv_f41_cycle_valuation_multiples_ebitebdwedge_chg126_126d_slope_v101_signal,
    f41cv_f41_cycle_valuation_multiples_ps_cheapz504_504d_slope_v102_signal,
    f41cv_f41_cycle_valuation_multiples_ps_cheaprnk504_504d_slope_v103_signal,
    f41cv_f41_cycle_valuation_multiples_ps_midgap1260_1260d_slope_v104_signal,
    f41cv_f41_cycle_valuation_multiples_ps_reratio504_504d_slope_v105_signal,
    f41cv_f41_cycle_valuation_multiples_ps_chg126_126d_slope_v106_signal,
    f41cv_f41_cycle_valuation_multiples_ps_cheapstreak252_252d_slope_v107_signal,
    f41cv_f41_cycle_valuation_multiples_salyld_rnk252_252d_slope_v108_signal,
    f41cv_f41_cycle_valuation_multiples_salyld_robz504_504d_slope_v109_signal,
    f41cv_f41_cycle_valuation_multiples_psXevebit_rnkspr504_504d_slope_v110_signal,
    f41cv_f41_cycle_valuation_multiples_salyld_troughgap504_504d_slope_v111_signal,
    f41cv_f41_cycle_valuation_multiples_mcaprev_robcheapz504_504d_slope_v112_signal,
    f41cv_f41_cycle_valuation_multiples_mcaprev_cheaprnk252_252d_slope_v113_signal,
    f41cv_f41_cycle_valuation_multiples_mcaprev_reratio504_504d_slope_v114_signal,
    f41cv_f41_cycle_valuation_multiples_mcaprev_chg63_63d_slope_v115_signal,
    f41cv_f41_cycle_valuation_multiples_mcapebd_cheapz252_252d_slope_v116_signal,
    f41cv_f41_cycle_valuation_multiples_mcapebd_reratio504_504d_slope_v117_signal,
    f41cv_f41_cycle_valuation_multiples_mcapebd_chg63_63d_slope_v118_signal,
    f41cv_f41_cycle_valuation_multiples_evmcap_midgap504_504d_slope_v119_signal,
    f41cv_f41_cycle_valuation_multiples_evmcap_chg63_63d_slope_v120_signal,
    f41cv_f41_cycle_valuation_multiples_evmcap_chg252_252d_slope_v121_signal,
    f41cv_f41_cycle_valuation_multiples_evsXevebd_zspr504_504d_slope_v122_signal,
    f41cv_f41_cycle_valuation_multiples_peXps_rnkspr252_252d_slope_v123_signal,
    f41cv_f41_cycle_valuation_multiples_evebitXevebd_zspr252_252d_slope_v124_signal,
    f41cv_f41_cycle_valuation_multiples_mcaprevXmcapebd_rnkspr252_252d_slope_v125_signal,
    f41cv_f41_cycle_valuation_multiples_blend_cheapz504_504d_slope_v126_signal,
    f41cv_f41_cycle_valuation_multiples_blend_cheaprnk126_126d_slope_v127_signal,
    f41cv_f41_cycle_valuation_multiples_blend_lowgap504_504d_slope_v128_signal,
    f41cv_f41_cycle_valuation_multiples_blend_peakgap1260_1260d_slope_v129_signal,
    f41cv_f41_cycle_valuation_multiples_blend_midgap1260_1260d_slope_v130_signal,
    f41cv_f41_cycle_valuation_multiples_blend_rerate126_126d_slope_v131_signal,
    f41cv_f41_cycle_valuation_multiples_multdisp_z504_504d_slope_v132_signal,
    f41cv_f41_cycle_valuation_multiples_multdisp_rnk252_252d_slope_v133_signal,
    f41cv_f41_cycle_valuation_multiples_blendyld_rnk252_252d_slope_v134_signal,
    f41cv_f41_cycle_valuation_multiples_blendyld_disp252_252d_slope_v135_signal,
    f41cv_f41_cycle_valuation_multiples_yldgap_ebdVsy_252d_slope_v136_signal,
    f41cv_f41_cycle_valuation_multiples_yldgap_eyVebd_252d_slope_v137_signal,
    f41cv_f41_cycle_valuation_multiples_blend_cheapyoy_252d_slope_v138_signal,
    f41cv_f41_cycle_valuation_multiples_evebdVpe_cheapspr504_504d_slope_v139_signal,
    f41cv_f41_cycle_valuation_multiples_blend_richlvl252_252d_slope_v140_signal,
    f41cv_f41_cycle_valuation_multiples_evebitrep_lowgapmom504_504d_slope_v141_signal,
    f41cv_f41_cycle_valuation_multiples_pe_midgapmom504_504d_slope_v142_signal,
    f41cv_f41_cycle_valuation_multiples_evebdrep_midgapmom504_504d_slope_v143_signal,
    f41cv_f41_cycle_valuation_multiples_psVsalyld_zspr252_252d_slope_v144_signal,
    f41cv_f41_cycle_valuation_multiples_blend_clarcheap252_252d_slope_v145_signal,
    f41cv_f41_cycle_valuation_multiples_evebdrep_peakgapmom1260_1260d_slope_v146_signal,
    f41cv_f41_cycle_valuation_multiples_peVevebit_cheapspr252_252d_slope_v147_signal,
    f41cv_f41_cycle_valuation_multiples_blendyld_midgap504_504d_slope_v148_signal,
    f41cv_f41_cycle_valuation_multiples_ps_lowgapmom504_504d_slope_v149_signal,
    f41cv_f41_cycle_valuation_multiples_blend_cheaphistrnk504_504d_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F41_CYCLE_VALUATION_MULTIPLES_REGISTRY_2ND_001_150 = REGISTRY


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

    pe = _fund(101, base=15.0, drift=0.0, vol=0.11).rename("pe")
    evebitda = _fund(102, base=8.0, drift=0.0, vol=0.12).rename("evebitda")
    evebit = _fund(103, base=12.0, drift=0.0, vol=0.11).rename("evebit")
    ps = _fund(104, base=3.0, drift=0.0, vol=0.12).rename("ps")
    ev = _fund(105, base=1.2e9, drift=0.0, vol=0.09).rename("ev")
    marketcap = _fund(106, base=9e8, drift=0.0, vol=0.10).rename("marketcap")
    ebitda = _fund(107, base=1.5e8, drift=0.0, vol=0.13).rename("ebitda")
    revenue = _fund(108, base=6e8, drift=0.0, vol=0.08).rename("revenue")

    cols = {
        "pe": pe, "evebitda": evebitda, "evebit": evebit, "ps": ps,
        "ev": ev, "marketcap": marketcap, "ebitda": ebitda, "revenue": revenue,
    }

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

    print("OK f41_cycle_valuation_multiples_2nd_derivatives_001_150_claude: %d features pass" % n_features)
