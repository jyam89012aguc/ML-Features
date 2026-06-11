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
# EBITDA-margin (ebitda/revenue) is a MARGIN owned by f25 and is NOT computed here.
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


# ============================================================
# ---- EV/EBITDA (reported) extra facets not used in file 1 ----
def f41cv_f41_cycle_valuation_multiples_evebdrep_cheapz252_252d_base_v076_signal(evebitda):
    m = evebitda.where(evebitda > 0, np.nan)
    b = -_z(m, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f41cv_f41_cycle_valuation_multiples_evebdrep_cheaprnk252_252d_base_v077_signal(evebitda):
    m = evebitda.where(evebitda > 0, np.nan)
    b = -_rank(m, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f41cv_f41_cycle_valuation_multiples_evebdrep_lowgapmom504_504d_base_v078_signal(evebitda):
    m = evebitda.where(evebitda > 0, np.nan)
    g = _f41_lowgap(m, 504)
    b = g - g.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f41cv_f41_cycle_valuation_multiples_evebdrep_chg126_126d_base_v079_signal(evebitda):
    m = evebitda.where(evebitda > 0, np.nan)
    b = np.log(m / m.shift(126))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f41cv_f41_cycle_valuation_multiples_evebdrep_reratio126_126d_base_v080_signal(evebitda):
    m = evebitda.where(evebitda > 0, np.nan)
    b = m / _mean(m, 126).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f41cv_f41_cycle_valuation_multiples_evebdrep_cheapstreak252_252d_base_v081_signal(evebitda):
    m = evebitda.where(evebitda > 0, np.nan)
    cheap = (m < _median(m, 252)).astype(float)
    b = cheap.rolling(126, min_periods=63).sum() / 126.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f41cv_f41_cycle_valuation_multiples_evebdrep_vol252_252d_base_v082_signal(evebitda):
    m = evebitda.where(evebitda > 0, np.nan)
    b = _std(np.log(m / m.shift(21)), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- EV/EBITDA (computed ev/ebitda): facets distinct from the reported metric & file 1 ----
def f41cv_f41_cycle_valuation_multiples_evebd_cheapz252_252d_base_v083_signal(ev, ebitda):
    m = _f41_ev_ebitda(ev, ebitda)
    b = -_z(m, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f41cv_f41_cycle_valuation_multiples_evebd_robcheapz504_504d_base_v084_signal(ev, ebitda):
    m = _f41_ev_ebitda(ev, ebitda)
    b = -_madz(m, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f41cv_f41_cycle_valuation_multiples_evebd_midgap1260_1260d_base_v085_signal(ev, ebitda):
    m = _f41_ev_ebitda(ev, ebitda)
    b = -_f41_midgap(m, 1260)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f41cv_f41_cycle_valuation_multiples_evebd_chg252_252d_base_v086_signal(ev, ebitda):
    m = _f41_ev_ebitda(ev, ebitda)
    b = np.log(m / m.shift(252))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- EBITDA YIELD (ebitda/ev) extra facets ----
def f41cv_f41_cycle_valuation_multiples_ebdyld_midgapmom504_504d_base_v087_signal(ebitda, ev):
    y = _f41_ebitda_yield(ebitda, ev)
    g = _f41_midgap(y, 504)
    b = g - g.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f41cv_f41_cycle_valuation_multiples_ebdyld_chg63_63d_base_v088_signal(ebitda, ev):
    y = _f41_ebitda_yield(ebitda, ev)
    b = y - y.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f41cv_f41_cycle_valuation_multiples_ebdyld_vol126_126d_base_v089_signal(ebitda, ev):
    y = _f41_ebitda_yield(ebitda, ev)
    b = _std(y - y.shift(21), 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- P/E extra facets not used in file 1 ----
def f41cv_f41_cycle_valuation_multiples_pe_cheaprnk504_504d_base_v090_signal(pe):
    m = pe.where(pe > 0, np.nan)
    b = -_rank(m, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f41cv_f41_cycle_valuation_multiples_pe_reratio504_504d_base_v091_signal(pe):
    m = pe.where(pe > 0, np.nan)
    b = m / _mean(m, 504).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f41cv_f41_cycle_valuation_multiples_pe_chg126_126d_base_v092_signal(pe):
    m = pe.where(pe > 0, np.nan)
    b = np.log(m / m.shift(126))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f41cv_f41_cycle_valuation_multiples_pe_dearstreak504_504d_base_v093_signal(pe):
    m = pe.where(pe > 0, np.nan)
    dear = (m > _median(m, 504)).astype(float)
    b = dear.rolling(252, min_periods=126).sum() / 252.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- EV/EBIT (reported) extra facets ----
def f41cv_f41_cycle_valuation_multiples_evebitrep_robcheapz252_252d_base_v094_signal(evebit):
    m = evebit.where(evebit > 0, np.nan)
    b = -_madz(m, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f41cv_f41_cycle_valuation_multiples_evebitrep_cheaprnk504_504d_base_v095_signal(evebit):
    m = evebit.where(evebit > 0, np.nan)
    b = -_rank(m, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f41cv_f41_cycle_valuation_multiples_evebitrep_midgap1260_1260d_base_v096_signal(evebit):
    m = evebit.where(evebit > 0, np.nan)
    b = -_f41_midgap(m, 1260)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f41cv_f41_cycle_valuation_multiples_evebitrep_reratio504_504d_base_v097_signal(evebit):
    m = evebit.where(evebit > 0, np.nan)
    b = m / _mean(m, 504).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f41cv_f41_cycle_valuation_multiples_evebitrep_chg63_63d_base_v098_signal(evebit):
    m = evebit.where(evebit > 0, np.nan)
    b = np.log(m / m.shift(63))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f41cv_f41_cycle_valuation_multiples_evebitrep_accel126_126d_base_v099_signal(evebit):
    m = evebit.where(evebit > 0, np.nan)
    g = np.log(m / m.shift(63))
    b = g - g.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- EBIT/EBITDA wedge extra facets (D&A intensity in the rating) ----
def f41cv_f41_cycle_valuation_multiples_ebitebdwedge_rnk252_252d_base_v100_signal(evebit, evebitda):
    a = evebit.where(evebit > 0, np.nan)
    e = evebitda.where(evebitda > 0, np.nan)
    w = np.log(a.replace(0, np.nan) / e.replace(0, np.nan))
    b = _rank(w, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f41cv_f41_cycle_valuation_multiples_ebitebdwedge_chg126_126d_base_v101_signal(evebit, evebitda):
    a = evebit.where(evebit > 0, np.nan)
    e = evebitda.where(evebitda > 0, np.nan)
    w = np.log(a.replace(0, np.nan) / e.replace(0, np.nan))
    b = w - w.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- P/S extra facets not used in file 1 ----
def f41cv_f41_cycle_valuation_multiples_ps_cheapz504_504d_base_v102_signal(ps):
    m = ps.where(ps > 0, np.nan)
    b = -_z(m, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f41cv_f41_cycle_valuation_multiples_ps_cheaprnk504_504d_base_v103_signal(ps):
    m = ps.where(ps > 0, np.nan)
    b = -_rank(m, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f41cv_f41_cycle_valuation_multiples_ps_midgap1260_1260d_base_v104_signal(ps):
    m = ps.where(ps > 0, np.nan)
    b = -_f41_midgap(m, 1260)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f41cv_f41_cycle_valuation_multiples_ps_reratio504_504d_base_v105_signal(ps):
    m = ps.where(ps > 0, np.nan)
    b = m / _mean(m, 504).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f41cv_f41_cycle_valuation_multiples_ps_chg126_126d_base_v106_signal(ps):
    m = ps.where(ps > 0, np.nan)
    b = np.log(m / m.shift(126))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f41cv_f41_cycle_valuation_multiples_ps_cheapstreak252_252d_base_v107_signal(ps):
    m = ps.where(ps > 0, np.nan)
    cheap = (m < _median(m, 252)).astype(float)
    b = cheap.rolling(126, min_periods=63).sum() / 126.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- SALES YIELD (revenue/ev) extra facets (margin-free EV-sales lens vs f43) ----
def f41cv_f41_cycle_valuation_multiples_salyld_rnk252_252d_base_v108_signal(revenue, ev):
    y = _f41_sales_yield(revenue, ev)
    b = _rank(y, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f41cv_f41_cycle_valuation_multiples_salyld_robz504_504d_base_v109_signal(revenue, ev):
    y = _f41_sales_yield(revenue, ev)
    b = _madz(y, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f41cv_f41_cycle_valuation_multiples_psXevebit_rnkspr504_504d_base_v110_signal(ps, evebit):
    p = ps.where(ps > 0, np.nan)
    e = evebit.where(evebit > 0, np.nan)
    b = _rank(p, 504) - _rank(e, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f41cv_f41_cycle_valuation_multiples_salyld_troughgap504_504d_base_v111_signal(revenue, ev):
    y = _f41_sales_yield(revenue, ev)
    b = np.log(y.replace(0, np.nan) / _rmax(y, 504).replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- MARKETCAP/REVENUE extra facets ----
def f41cv_f41_cycle_valuation_multiples_mcaprev_robcheapz504_504d_base_v112_signal(marketcap, revenue):
    m = _f41_mcap_sales(marketcap, revenue)
    b = -_madz(m, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f41cv_f41_cycle_valuation_multiples_mcaprev_cheaprnk252_252d_base_v113_signal(marketcap, revenue):
    m = _f41_mcap_sales(marketcap, revenue)
    b = -_rank(m, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f41cv_f41_cycle_valuation_multiples_mcaprev_reratio504_504d_base_v114_signal(marketcap, revenue):
    m = _f41_mcap_sales(marketcap, revenue)
    b = m / _mean(m, 504).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f41cv_f41_cycle_valuation_multiples_mcaprev_chg63_63d_base_v115_signal(marketcap, revenue):
    m = _f41_mcap_sales(marketcap, revenue)
    b = np.log(m / m.shift(63))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- MARKETCAP/EBITDA extra facets ----
def f41cv_f41_cycle_valuation_multiples_mcapebd_cheapz252_252d_base_v116_signal(marketcap, ebitda):
    m = _f41_mcap_ebitda(marketcap, ebitda)
    b = -_z(m, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f41cv_f41_cycle_valuation_multiples_mcapebd_reratio504_504d_base_v117_signal(marketcap, ebitda):
    m = _f41_mcap_ebitda(marketcap, ebitda)
    b = m / _mean(m, 504).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f41cv_f41_cycle_valuation_multiples_mcapebd_chg63_63d_base_v118_signal(marketcap, ebitda):
    m = _f41_mcap_ebitda(marketcap, ebitda)
    b = np.log(m / m.shift(63))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- EV/MARKETCAP (net-debt loading) extra facets ----
def f41cv_f41_cycle_valuation_multiples_evmcap_midgap504_504d_base_v119_signal(ev, marketcap):
    m = ev / marketcap.replace(0, np.nan)
    b = _f41_midgap(m, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f41cv_f41_cycle_valuation_multiples_evmcap_chg63_63d_base_v120_signal(ev, marketcap):
    m = ev / marketcap.replace(0, np.nan)
    b = m - m.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f41cv_f41_cycle_valuation_multiples_evmcap_chg252_252d_base_v121_signal(ev, marketcap):
    m = ev / marketcap.replace(0, np.nan)
    b = m - m.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- CROSS-MULTIPLE SPREADS (which lens is cheaper) — distinct pairs from file 1 ----
def f41cv_f41_cycle_valuation_multiples_evsXevebd_zspr504_504d_base_v122_signal(ev, revenue, ebitda):
    es = _f41_ev_sales(ev, revenue)
    ee = _f41_ev_ebitda(ev, ebitda)
    b = _z(es, 504) - _z(ee, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f41cv_f41_cycle_valuation_multiples_peXps_rnkspr252_252d_base_v123_signal(pe, ps):
    p = pe.where(pe > 0, np.nan)
    s = ps.where(ps > 0, np.nan)
    b = _rank(p, 252) - _rank(s, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f41cv_f41_cycle_valuation_multiples_evebitXevebd_zspr252_252d_base_v124_signal(evebit, evebitda):
    a = evebit.where(evebit > 0, np.nan)
    e = evebitda.where(evebitda > 0, np.nan)
    b = _z(a, 252) - _z(e, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f41cv_f41_cycle_valuation_multiples_mcaprevXmcapebd_rnkspr252_252d_base_v125_signal(marketcap, revenue, ebitda):
    s = _f41_mcap_sales(marketcap, revenue)
    e = _f41_mcap_ebitda(marketcap, ebitda)
    b = _rank(s, 252) - _rank(e, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- BLENDED CHEAPNESS composites (f41-owned) — distinct combos/windows from file 1 ----
def f41cv_f41_cycle_valuation_multiples_blend_cheapz504_504d_base_v126_signal(evebitda, pe, ps):
    e = -_z(evebitda.where(evebitda > 0, np.nan), 504)
    p = -_z(pe.where(pe > 0, np.nan), 504)
    s = -_z(ps.where(ps > 0, np.nan), 504)
    b = pd.concat([e, p, s], axis=1).mean(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f41cv_f41_cycle_valuation_multiples_blend_cheaprnk126_126d_base_v127_signal(evebitda, evebit, ps):
    e1 = -_rank(evebitda.where(evebitda > 0, np.nan), 126)
    e2 = -_rank(evebit.where(evebit > 0, np.nan), 126)
    s = -_rank(ps.where(ps > 0, np.nan), 126)
    b = pd.concat([e1, e2, s], axis=1).mean(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f41cv_f41_cycle_valuation_multiples_blend_lowgap504_504d_base_v128_signal(evebitda, pe, evebit):
    e = _f41_lowgap(evebitda.where(evebitda > 0, np.nan), 504)
    p = _f41_lowgap(pe.where(pe > 0, np.nan), 504)
    a = _f41_lowgap(evebit.where(evebit > 0, np.nan), 504)
    b = pd.concat([e, p, a], axis=1).mean(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f41cv_f41_cycle_valuation_multiples_blend_peakgap1260_1260d_base_v129_signal(evebitda, pe, ps):
    e = _f41_peakgap(evebitda.where(evebitda > 0, np.nan), 1260)
    p = _f41_peakgap(pe.where(pe > 0, np.nan), 1260)
    s = _f41_peakgap(ps.where(ps > 0, np.nan), 1260)
    b = pd.concat([e, p, s], axis=1).mean(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f41cv_f41_cycle_valuation_multiples_blend_midgap1260_1260d_base_v130_signal(evebit, pe, ps):
    e = -_f41_midgap(evebit.where(evebit > 0, np.nan), 1260)
    p = -_f41_midgap(pe.where(pe > 0, np.nan), 1260)
    s = -_f41_midgap(ps.where(ps > 0, np.nan), 1260)
    b = pd.concat([e, p, s], axis=1).mean(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- BLENDED re-rating momentum at a second horizon ----
def f41cv_f41_cycle_valuation_multiples_blend_rerate126_126d_base_v131_signal(evebitda, pe, ps):
    e = -_z(evebitda.where(evebitda > 0, np.nan), 252)
    p = -_z(pe.where(pe > 0, np.nan), 252)
    s = -_z(ps.where(ps > 0, np.nan), 252)
    c = pd.concat([e, p, s], axis=1).mean(axis=1)
    b = c - c.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- VALUATION DISPERSION at 504d and rank-space ----
def f41cv_f41_cycle_valuation_multiples_multdisp_z504_504d_base_v132_signal(evebitda, pe, ps):
    e = _z(evebitda.where(evebitda > 0, np.nan), 504)
    p = _z(pe.where(pe > 0, np.nan), 504)
    s = _z(ps.where(ps > 0, np.nan), 504)
    b = pd.concat([e, p, s], axis=1).std(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f41cv_f41_cycle_valuation_multiples_multdisp_rnk252_252d_base_v133_signal(evebit, pe, ps):
    e = _rank(evebit.where(evebit > 0, np.nan), 252)
    p = _rank(pe.where(pe > 0, np.nan), 252)
    s = _rank(ps.where(ps > 0, np.nan), 252)
    b = pd.concat([e, p, s], axis=1).std(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- BLENDED YIELD composites (enterprise richness) ----
def f41cv_f41_cycle_valuation_multiples_blendyld_rnk252_252d_base_v134_signal(ebitda, revenue, ev):
    ey = _f41_ebitda_yield(ebitda, ev)
    sy = _f41_sales_yield(revenue, ev)
    b = (_rank(ey, 252) + _rank(sy, 252)) / 2.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f41cv_f41_cycle_valuation_multiples_blendyld_disp252_252d_base_v135_signal(ebitda, revenue, ev):
    ey = _z(_f41_ebitda_yield(ebitda, ev), 252)
    sy = _z(_f41_sales_yield(revenue, ev), 252)
    b = (ey - sy).abs()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- EARNINGS-vs-SALES yield gaps at extra horizons (cross-denominator relative value) ----
def f41cv_f41_cycle_valuation_multiples_yldgap_ebdVsy_252d_base_v136_signal(ebitda, revenue, ev):
    ey = _f41_ebitda_yield(ebitda, ev)
    sy = _f41_sales_yield(revenue, ev)
    b = _z(ey, 252) - _z(sy, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f41cv_f41_cycle_valuation_multiples_yldgap_eyVebd_252d_base_v137_signal(pe, ebitda, ev):
    ey = _f41_earnings_yield(pe)
    by = _f41_ebitda_yield(ebitda, ev)
    b = _z(ey, 252) - _z(by, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- Composite cheapness vs its own one-year-ago level (cycle re-rating, yoy) ----
def f41cv_f41_cycle_valuation_multiples_blend_cheapyoy_252d_base_v138_signal(evebitda, pe, ps):
    e = -_z(evebitda.where(evebitda > 0, np.nan), 252)
    p = -_z(pe.where(pe > 0, np.nan), 252)
    s = -_z(ps.where(ps > 0, np.nan), 252)
    c = pd.concat([e, p, s], axis=1).mean(axis=1)
    b = c - c.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- EV/EBITDA cheapness vs P/E cheapness disagreement (enterprise vs equity lens) ----
def f41cv_f41_cycle_valuation_multiples_evebdVpe_cheapspr504_504d_base_v139_signal(evebitda, pe):
    e = -_z(evebitda.where(evebitda > 0, np.nan), 504)
    p = -_z(pe.where(pe > 0, np.nan), 504)
    b = e - p
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- Blended multiple level composite (scale-free average of standardized multiples) ----
def f41cv_f41_cycle_valuation_multiples_blend_richlvl252_252d_base_v140_signal(evebitda, evebit, ps):
    e1 = _z(evebitda.where(evebitda > 0, np.nan), 252)
    e2 = _z(evebit.where(evebit > 0, np.nan), 252)
    s = _z(ps.where(ps > 0, np.nan), 252)
    b = pd.concat([e1, e2, s], axis=1).mean(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- EV/EBIT cycle-trough re-rating (recovery of the multiple off its low) ----
def f41cv_f41_cycle_valuation_multiples_evebitrep_lowgapmom504_504d_base_v141_signal(evebit):
    m = evebit.where(evebit > 0, np.nan)
    g = _f41_lowgap(m, 504)
    b = g - g.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- P/E mid-cycle gap momentum (re-rating speed vs normalized level) ----
def f41cv_f41_cycle_valuation_multiples_pe_midgapmom504_504d_base_v142_signal(pe):
    m = pe.where(pe > 0, np.nan)
    g = _f41_midgap(m, 504)
    b = g - g.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- EV/EBITDA reported mid-cycle gap momentum ----
def f41cv_f41_cycle_valuation_multiples_evebdrep_midgapmom504_504d_base_v143_signal(evebitda):
    m = evebitda.where(evebitda > 0, np.nan)
    g = _f41_midgap(m, 504)
    b = g - g.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- P/S vs EV/Sales yield consistency (equity vs enterprise sales lens) ----
def f41cv_f41_cycle_valuation_multiples_psVsalyld_zspr252_252d_base_v144_signal(ps, revenue, ev):
    p = _z(ps.where(ps > 0, np.nan), 252)
    sy = _z(_f41_sales_yield(revenue, ev), 252)
    b = p + sy
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- Blended cheapness dispersion-weighted score (clarity-scaled cheapness) ----
def f41cv_f41_cycle_valuation_multiples_blend_clarcheap252_252d_base_v145_signal(evebitda, pe, ps):
    e = -_z(evebitda.where(evebitda > 0, np.nan), 252)
    p = -_z(pe.where(pe > 0, np.nan), 252)
    s = -_z(ps.where(ps > 0, np.nan), 252)
    stk = pd.concat([e, p, s], axis=1)
    disp = stk.std(axis=1).replace(0, np.nan)
    b = stk.mean(axis=1) / disp
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- EV/EBITDA reported peak-gap momentum (de-rating from prior peak rating) ----
def f41cv_f41_cycle_valuation_multiples_evebdrep_peakgapmom1260_1260d_base_v146_signal(evebitda):
    m = evebitda.where(evebitda > 0, np.nan)
    g = _f41_peakgap(m, 1260)
    b = g - g.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- P/E vs EV/EBIT cheapness gap at 252d (earnings-multiple basis) ----
def f41cv_f41_cycle_valuation_multiples_peVevebit_cheapspr252_252d_base_v147_signal(pe, evebit):
    p = -_z(pe.where(pe > 0, np.nan), 252)
    e = -_z(evebit.where(evebit > 0, np.nan), 252)
    b = p - e
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- Blended yield mid-cycle gap (enterprise yield vs its own normal) ----
def f41cv_f41_cycle_valuation_multiples_blendyld_midgap504_504d_base_v148_signal(ebitda, revenue, ev):
    ey = _f41_ebitda_yield(ebitda, ev)
    sy = _f41_sales_yield(revenue, ev)
    c = (ey + sy) / 2.0
    b = _f41_midgap(c, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- P/S re-rating off cycle low (recovery of the sales rating) ----
def f41cv_f41_cycle_valuation_multiples_ps_lowgapmom504_504d_base_v149_signal(ps):
    m = ps.where(ps > 0, np.nan)
    g = _f41_lowgap(m, 504)
    b = g - g.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- Composite cheapness percentile vs its own 504d history (rank of blend) ----
def f41cv_f41_cycle_valuation_multiples_blend_cheaphistrnk504_504d_base_v150_signal(evebitda, pe, ps):
    e = -_z(evebitda.where(evebitda > 0, np.nan), 252)
    p = -_z(pe.where(pe > 0, np.nan), 252)
    s = -_z(ps.where(ps > 0, np.nan), 252)
    c = pd.concat([e, p, s], axis=1).mean(axis=1)
    b = _rank(c, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f41cv_f41_cycle_valuation_multiples_evebdrep_cheapz252_252d_base_v076_signal,
    f41cv_f41_cycle_valuation_multiples_evebdrep_cheaprnk252_252d_base_v077_signal,
    f41cv_f41_cycle_valuation_multiples_evebdrep_lowgapmom504_504d_base_v078_signal,
    f41cv_f41_cycle_valuation_multiples_evebdrep_chg126_126d_base_v079_signal,
    f41cv_f41_cycle_valuation_multiples_evebdrep_reratio126_126d_base_v080_signal,
    f41cv_f41_cycle_valuation_multiples_evebdrep_cheapstreak252_252d_base_v081_signal,
    f41cv_f41_cycle_valuation_multiples_evebdrep_vol252_252d_base_v082_signal,
    f41cv_f41_cycle_valuation_multiples_evebd_cheapz252_252d_base_v083_signal,
    f41cv_f41_cycle_valuation_multiples_evebd_robcheapz504_504d_base_v084_signal,
    f41cv_f41_cycle_valuation_multiples_evebd_midgap1260_1260d_base_v085_signal,
    f41cv_f41_cycle_valuation_multiples_evebd_chg252_252d_base_v086_signal,
    f41cv_f41_cycle_valuation_multiples_ebdyld_midgapmom504_504d_base_v087_signal,
    f41cv_f41_cycle_valuation_multiples_ebdyld_chg63_63d_base_v088_signal,
    f41cv_f41_cycle_valuation_multiples_ebdyld_vol126_126d_base_v089_signal,
    f41cv_f41_cycle_valuation_multiples_pe_cheaprnk504_504d_base_v090_signal,
    f41cv_f41_cycle_valuation_multiples_pe_reratio504_504d_base_v091_signal,
    f41cv_f41_cycle_valuation_multiples_pe_chg126_126d_base_v092_signal,
    f41cv_f41_cycle_valuation_multiples_pe_dearstreak504_504d_base_v093_signal,
    f41cv_f41_cycle_valuation_multiples_evebitrep_robcheapz252_252d_base_v094_signal,
    f41cv_f41_cycle_valuation_multiples_evebitrep_cheaprnk504_504d_base_v095_signal,
    f41cv_f41_cycle_valuation_multiples_evebitrep_midgap1260_1260d_base_v096_signal,
    f41cv_f41_cycle_valuation_multiples_evebitrep_reratio504_504d_base_v097_signal,
    f41cv_f41_cycle_valuation_multiples_evebitrep_chg63_63d_base_v098_signal,
    f41cv_f41_cycle_valuation_multiples_evebitrep_accel126_126d_base_v099_signal,
    f41cv_f41_cycle_valuation_multiples_ebitebdwedge_rnk252_252d_base_v100_signal,
    f41cv_f41_cycle_valuation_multiples_ebitebdwedge_chg126_126d_base_v101_signal,
    f41cv_f41_cycle_valuation_multiples_ps_cheapz504_504d_base_v102_signal,
    f41cv_f41_cycle_valuation_multiples_ps_cheaprnk504_504d_base_v103_signal,
    f41cv_f41_cycle_valuation_multiples_ps_midgap1260_1260d_base_v104_signal,
    f41cv_f41_cycle_valuation_multiples_ps_reratio504_504d_base_v105_signal,
    f41cv_f41_cycle_valuation_multiples_ps_chg126_126d_base_v106_signal,
    f41cv_f41_cycle_valuation_multiples_ps_cheapstreak252_252d_base_v107_signal,
    f41cv_f41_cycle_valuation_multiples_salyld_rnk252_252d_base_v108_signal,
    f41cv_f41_cycle_valuation_multiples_salyld_robz504_504d_base_v109_signal,
    f41cv_f41_cycle_valuation_multiples_psXevebit_rnkspr504_504d_base_v110_signal,
    f41cv_f41_cycle_valuation_multiples_salyld_troughgap504_504d_base_v111_signal,
    f41cv_f41_cycle_valuation_multiples_mcaprev_robcheapz504_504d_base_v112_signal,
    f41cv_f41_cycle_valuation_multiples_mcaprev_cheaprnk252_252d_base_v113_signal,
    f41cv_f41_cycle_valuation_multiples_mcaprev_reratio504_504d_base_v114_signal,
    f41cv_f41_cycle_valuation_multiples_mcaprev_chg63_63d_base_v115_signal,
    f41cv_f41_cycle_valuation_multiples_mcapebd_cheapz252_252d_base_v116_signal,
    f41cv_f41_cycle_valuation_multiples_mcapebd_reratio504_504d_base_v117_signal,
    f41cv_f41_cycle_valuation_multiples_mcapebd_chg63_63d_base_v118_signal,
    f41cv_f41_cycle_valuation_multiples_evmcap_midgap504_504d_base_v119_signal,
    f41cv_f41_cycle_valuation_multiples_evmcap_chg63_63d_base_v120_signal,
    f41cv_f41_cycle_valuation_multiples_evmcap_chg252_252d_base_v121_signal,
    f41cv_f41_cycle_valuation_multiples_evsXevebd_zspr504_504d_base_v122_signal,
    f41cv_f41_cycle_valuation_multiples_peXps_rnkspr252_252d_base_v123_signal,
    f41cv_f41_cycle_valuation_multiples_evebitXevebd_zspr252_252d_base_v124_signal,
    f41cv_f41_cycle_valuation_multiples_mcaprevXmcapebd_rnkspr252_252d_base_v125_signal,
    f41cv_f41_cycle_valuation_multiples_blend_cheapz504_504d_base_v126_signal,
    f41cv_f41_cycle_valuation_multiples_blend_cheaprnk126_126d_base_v127_signal,
    f41cv_f41_cycle_valuation_multiples_blend_lowgap504_504d_base_v128_signal,
    f41cv_f41_cycle_valuation_multiples_blend_peakgap1260_1260d_base_v129_signal,
    f41cv_f41_cycle_valuation_multiples_blend_midgap1260_1260d_base_v130_signal,
    f41cv_f41_cycle_valuation_multiples_blend_rerate126_126d_base_v131_signal,
    f41cv_f41_cycle_valuation_multiples_multdisp_z504_504d_base_v132_signal,
    f41cv_f41_cycle_valuation_multiples_multdisp_rnk252_252d_base_v133_signal,
    f41cv_f41_cycle_valuation_multiples_blendyld_rnk252_252d_base_v134_signal,
    f41cv_f41_cycle_valuation_multiples_blendyld_disp252_252d_base_v135_signal,
    f41cv_f41_cycle_valuation_multiples_yldgap_ebdVsy_252d_base_v136_signal,
    f41cv_f41_cycle_valuation_multiples_yldgap_eyVebd_252d_base_v137_signal,
    f41cv_f41_cycle_valuation_multiples_blend_cheapyoy_252d_base_v138_signal,
    f41cv_f41_cycle_valuation_multiples_evebdVpe_cheapspr504_504d_base_v139_signal,
    f41cv_f41_cycle_valuation_multiples_blend_richlvl252_252d_base_v140_signal,
    f41cv_f41_cycle_valuation_multiples_evebitrep_lowgapmom504_504d_base_v141_signal,
    f41cv_f41_cycle_valuation_multiples_pe_midgapmom504_504d_base_v142_signal,
    f41cv_f41_cycle_valuation_multiples_evebdrep_midgapmom504_504d_base_v143_signal,
    f41cv_f41_cycle_valuation_multiples_psVsalyld_zspr252_252d_base_v144_signal,
    f41cv_f41_cycle_valuation_multiples_blend_clarcheap252_252d_base_v145_signal,
    f41cv_f41_cycle_valuation_multiples_evebdrep_peakgapmom1260_1260d_base_v146_signal,
    f41cv_f41_cycle_valuation_multiples_peVevebit_cheapspr252_252d_base_v147_signal,
    f41cv_f41_cycle_valuation_multiples_blendyld_midgap504_504d_base_v148_signal,
    f41cv_f41_cycle_valuation_multiples_ps_lowgapmom504_504d_base_v149_signal,
    f41cv_f41_cycle_valuation_multiples_blend_cheaphistrnk504_504d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F41_CYCLE_VALUATION_MULTIPLES_REGISTRY_076_150 = REGISTRY


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

    assert n_features == 75, n_features
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

    print("OK f41_cycle_valuation_multiples_base_076_150_claude: %d features pass" % n_features)
