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


def _rmax(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rmin(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rank(s, w):
    return s.rolling(w, min_periods=max(1, w // 4)).rank(pct=True) - 0.5


# ===== folder domain primitives: cycle-bottom value = cheapness GATED by solvency =====
def _f38_cheap_pb(pb):
    return 1.0 / pb.replace(0, np.nan)


def _f38_cheap_ev(evebitda):
    return 1.0 / evebitda.replace(0, np.nan)


def _f38_net_cash(cashneq, debt):
    return cashneq - debt


def _f38_net_cash_ratio(cashneq, debt):
    return cashneq / debt.replace(0, np.nan)


def _f38_tang_backing(tangibles, marketcap):
    return tangibles / marketcap.replace(0, np.nan)


def _f38_solv_gate(cashneq, debt):
    nd = (debt - cashneq)
    return 1.0 / (1.0 + np.exp(nd / (cashneq.abs() + 1.0)))


def _f38_ev(marketcap, debt, cashneq):
    return marketcap + debt - cashneq


# short aliases (keep derivative bodies compact while staying fully inline)
_cp = _f38_cheap_pb
_ce = _f38_cheap_ev
_nc = _f38_net_cash
_ncr = _f38_net_cash_ratio
_tb = _f38_tang_backing
_sg = _f38_solv_gate
_ev = _f38_ev


def f38cb_f38_cycle_bottom_value_cheappb_netcash_tanh_252d_jerk_v001_signal(pb, cashneq, debt):
    cheap = _cp(pb); gate = _sg(cashneq, debt); b = cheap * gate; b = np.tanh(b / (b.abs().rolling(126, min_periods=42).mean() + 1e-9))
    b = b.replace([np.inf, -np.inf], np.nan)
    o = (b - 2.0 * b.shift(63) + b.shift(126)) / 3969.0
    return o.replace([np.inf, -np.inf], np.nan)
def f38cb_f38_cycle_bottom_value_cheapev_cov_shortlong_252d_jerk_v002_signal(evebitda, cashneq, debt):
    cheap = _ce(evebitda); cov = _ncr(cashneq, debt).clip(upper=10.0); b = cheap * cov; b = _mean(b, 21) - _mean(b, 126)
    b = b.replace([np.inf, -np.inf], np.nan)
    o = (b - 2.0 * b.shift(63) + b.shift(126)) / 3969.0
    return o.replace([np.inf, -np.inf], np.nan)
def f38cb_f38_cycle_bottom_value_pbz_tangback_z504_252d_jerk_v003_signal(pb, tangibles, marketcap):
    cheapz = _z(_cp(pb), 252); back = _tb(tangibles, marketcap); b = cheapz * back; b = _z(b, 504)
    b = b.replace([np.inf, -np.inf], np.nan)
    o = (b - 2.0 * b.shift(63) + b.shift(126)) / 3969.0
    return o.replace([np.inf, -np.inf], np.nan)
def f38cb_f38_cycle_bottom_value_evnetcash_rank504_252d_jerk_v004_signal(evebitda, cashneq, debt):
    cz = _z(_ce(evebitda), 252); sz = _z(_nc(cashneq, debt), 252); b = cz + sz; b = _rank(b, 504)
    b = b.replace([np.inf, -np.inf], np.nan)
    o = (b - 2.0 * b.shift(63) + b.shift(126)) / 3969.0
    return o.replace([np.inf, -np.inf], np.nan)
def f38cb_f38_cycle_bottom_value_navdisc_gate_zscoremr_252d_jerk_v005_signal(tangibles, marketcap, cashneq, debt):
    disc = (tangibles - marketcap) / marketcap.replace(0, np.nan); gate = _sg(cashneq, debt); b = disc * gate; b = _z(b, 126) - _z(b, 252)
    b = b.replace([np.inf, -np.inf], np.nan)
    o = (b - 2.0 * b.shift(63) + b.shift(126)) / 3969.0
    return o.replace([np.inf, -np.inf], np.nan)
def f38cb_f38_cycle_bottom_value_blendcheap_cov_logmag_252d_jerk_v006_signal(pb, evebitda, cashneq, debt):
    blend = 0.5 * _rank(_cp(pb), 252) + 0.5 * _rank(_ce(evebitda), 252); cov = _ncr(cashneq, debt).clip(upper=8.0); b = blend * cov; b = np.sign(b) * np.log1p(b.abs())
    b = b.replace([np.inf, -np.inf], np.nan)
    o = (b - 2.0 * b.shift(63) + b.shift(126)) / 3969.0
    return o.replace([np.inf, -np.inf], np.nan)
def f38cb_f38_cycle_bottom_value_tangeq_cheap_emaratio_252d_jerk_v007_signal(tangibles, equity, pb):
    tq = tangibles / equity.replace(0, np.nan); cheap = _cp(pb); b = tq * cheap; b = b / (b.ewm(span=126, min_periods=42).mean().abs() + 1e-9)
    b = b.replace([np.inf, -np.inf], np.nan)
    o = (b - 2.0 * b.shift(63) + b.shift(126)) / 3969.0
    return o.replace([np.inf, -np.inf], np.nan)
def f38cb_f38_cycle_bottom_value_netcashmc_ev_lvl_252d_jerk_v008_signal(cashneq, debt, marketcap, evebitda):
    ncmc = _nc(cashneq, debt) / marketcap.replace(0, np.nan); cheap = _ce(evebitda); b = ncmc * cheap
    b = b.replace([np.inf, -np.inf], np.nan)
    o = (b - 2.0 * b.shift(63) + b.shift(126)) / 3969.0
    return o.replace([np.inf, -np.inf], np.nan)
def f38cb_f38_cycle_bottom_value_bookyld_solv_z252_252d_jerk_v009_signal(equity, marketcap, cashneq, debt):
    byld = equity / marketcap.replace(0, np.nan); gate = _sg(cashneq, debt); b = byld * gate; b = _z(b, 252)
    b = b.replace([np.inf, -np.inf], np.nan)
    o = (b - 2.0 * b.shift(63) + b.shift(126)) / 3969.0
    return o.replace([np.inf, -np.inf], np.nan)
def f38cb_f38_cycle_bottom_value_warchest_pb_rank252_252d_jerk_v010_signal(cashneq, debt, equity, pb):
    wc = _nc(cashneq, debt) / equity.replace(0, np.nan); cheap = _cp(pb); b = wc * cheap; b = _rank(b, 252)
    b = b.replace([np.inf, -np.inf], np.nan)
    o = (b - 2.0 * b.shift(63) + b.shift(126)) / 3969.0
    return o.replace([np.inf, -np.inf], np.nan)
def f38cb_f38_cycle_bottom_value_buffer_ev_ratio_252d_jerk_v011_signal(cashneq, debt, tangibles, evebitda):
    buf = _nc(cashneq, debt) / tangibles.replace(0, np.nan); cheap = _ce(evebitda); b = buf * cheap; b = b / (_mean(b, 252).abs() + 1e-9)
    b = b.replace([np.inf, -np.inf], np.nan)
    o = (b - 2.0 * b.shift(63) + b.shift(126)) / 3969.0
    return o.replace([np.inf, -np.inf], np.nan)
def f38cb_f38_cycle_bottom_value_evtang_inv_emadisp_252d_jerk_v012_signal(marketcap, debt, cashneq, tangibles):
    ev = _ev(marketcap, debt, cashneq); et = ev / tangibles.replace(0, np.nan); b = 1.0 / et.replace(0, np.nan); b = b - b.ewm(span=63, min_periods=21).mean()
    b = b.replace([np.inf, -np.inf], np.nan)
    o = (b - 2.0 * b.shift(63) + b.shift(126)) / 3969.0
    return o.replace([np.inf, -np.inf], np.nan)
def f38cb_f38_cycle_bottom_value_tangfloor_pb_sqrtmag_252d_jerk_v013_signal(tangibles, marketcap, pb):
    back = _tb(tangibles, marketcap); cheap = _cp(pb); b = back * cheap; b = np.sign(b) * (b.abs() ** 0.5)
    b = b.replace([np.inf, -np.inf], np.nan)
    o = (b - 2.0 * b.shift(63) + b.shift(126)) / 3969.0
    return o.replace([np.inf, -np.inf], np.nan)
def f38cb_f38_cycle_bottom_value_netcashev_cheap_tanh_252d_jerk_v014_signal(cashneq, debt, marketcap, evebitda):
    ev = _ev(marketcap, debt, cashneq); cover = _nc(cashneq, debt) / ev.replace(0, np.nan); cheap = _ce(evebitda); b = cover * cheap; b = np.tanh(b / (b.abs().rolling(126, min_periods=42).mean() + 1e-9))
    b = b.replace([np.inf, -np.inf], np.nan)
    o = (b - 2.0 * b.shift(63) + b.shift(126)) / 3969.0
    return o.replace([np.inf, -np.inf], np.nan)
def f38cb_f38_cycle_bottom_value_triple_shortlong_252d_jerk_v015_signal(pb, evebitda, cashneq, debt):
    a = _z(_cp(pb), 252); c = _z(_ce(evebitda), 252); s = _z(_nc(cashneq, debt), 252); b = (a + c + s) / 3.0; b = _mean(b, 21) - _mean(b, 126)
    b = b.replace([np.inf, -np.inf], np.nan)
    o = (b - 2.0 * b.shift(63) + b.shift(126)) / 3969.0
    return o.replace([np.inf, -np.inf], np.nan)
def f38cb_f38_cycle_bottom_value_tangdebt_ev_z504_252d_jerk_v016_signal(tangibles, debt, evebitda):
    tcov = (tangibles / debt.replace(0, np.nan)).clip(upper=20.0); cheap = _ce(evebitda); b = tcov * cheap; b = _z(b, 504)
    b = b.replace([np.inf, -np.inf], np.nan)
    o = (b - 2.0 * b.shift(63) + b.shift(126)) / 3969.0
    return o.replace([np.inf, -np.inf], np.nan)
def f38cb_f38_cycle_bottom_value_eqdebt_pb_rank504_252d_jerk_v017_signal(equity, debt, pb):
    eqd = equity / debt.replace(0, np.nan); gate = 1.0 / (1.0 + np.exp(-(eqd - 1.0))); cheap = _cp(pb); b = cheap * gate; b = _rank(b, 504)
    b = b.replace([np.inf, -np.inf], np.nan)
    o = (b - 2.0 * b.shift(63) + b.shift(126)) / 3969.0
    return o.replace([np.inf, -np.inf], np.nan)
def f38cb_f38_cycle_bottom_value_netdebteq_pb_zscoremr_252d_jerk_v018_signal(debt, cashneq, equity, pb):
    nde = (debt - cashneq) / equity.replace(0, np.nan); low = 1.0 / (1.0 + np.exp(nde)); cheap = _cp(pb); b = low * cheap; b = _z(b, 126) - _z(b, 252)
    b = b.replace([np.inf, -np.inf], np.nan)
    o = (b - 2.0 * b.shift(63) + b.shift(126)) / 3969.0
    return o.replace([np.inf, -np.inf], np.nan)
def f38cb_f38_cycle_bottom_value_cashmc_ev_logmag_252d_jerk_v019_signal(cashneq, marketcap, evebitda):
    cashmc = cashneq / marketcap.replace(0, np.nan); cheap = _ce(evebitda); b = cashmc * cheap; b = np.sign(b) * np.log1p(b.abs())
    b = b.replace([np.inf, -np.inf], np.nan)
    o = (b - 2.0 * b.shift(63) + b.shift(126)) / 3969.0
    return o.replace([np.inf, -np.inf], np.nan)
def f38cb_f38_cycle_bottom_value_ncmctang_emaratio_252d_jerk_v020_signal(cashneq, debt, tangibles, pb):
    liq = _nc(cashneq, debt) / tangibles.replace(0, np.nan); cheap = _cp(pb); b = np.tanh(liq) * cheap; b = b / (b.ewm(span=126, min_periods=42).mean().abs() + 1e-9)
    b = b.replace([np.inf, -np.inf], np.nan)
    o = (b - 2.0 * b.shift(63) + b.shift(126)) / 3969.0
    return o.replace([np.inf, -np.inf], np.nan)
def f38cb_f38_cycle_bottom_value_eveq_cov_lvl_252d_jerk_v021_signal(marketcap, debt, cashneq, equity):
    ev = _ev(marketcap, debt, cashneq); inv = equity / ev.replace(0, np.nan); cov = _ncr(cashneq, debt).clip(upper=8.0); b = inv * cov
    b = b.replace([np.inf, -np.inf], np.nan)
    o = (b - 2.0 * b.shift(63) + b.shift(126)) / 3969.0
    return o.replace([np.inf, -np.inf], np.nan)
def f38cb_f38_cycle_bottom_value_tangcov_evz_z252_252d_jerk_v022_signal(tangibles, debt, evebitda):
    cov = _z(tangibles / debt.replace(0, np.nan), 252); cheap = _z(_ce(evebitda), 252); b = cov + cheap; b = _z(b, 252)
    b = b.replace([np.inf, -np.inf], np.nan)
    o = (b - 2.0 * b.shift(63) + b.shift(126)) / 3969.0
    return o.replace([np.inf, -np.inf], np.nan)
def f38cb_f38_cycle_bottom_value_netnet_mc_rank252_252d_jerk_v023_signal(tangibles, debt, marketcap, pb):
    netnet = (tangibles - debt) / marketcap.replace(0, np.nan); cheap = _cp(pb); b = netnet * (1.0 + np.tanh(cheap)); b = _rank(b, 252)
    b = b.replace([np.inf, -np.inf], np.nan)
    o = (b - 2.0 * b.shift(63) + b.shift(126)) / 3969.0
    return o.replace([np.inf, -np.inf], np.nan)
def f38cb_f38_cycle_bottom_value_bookyld_cov_ratio_252d_jerk_v024_signal(equity, marketcap, cashneq, debt):
    byld = equity / marketcap.replace(0, np.nan); cov = _ncr(cashneq, debt).clip(upper=8.0); b = byld * cov; b = b / (_mean(b, 252).abs() + 1e-9)
    b = b.replace([np.inf, -np.inf], np.nan)
    o = (b - 2.0 * b.shift(63) + b.shift(126)) / 3969.0
    return o.replace([np.inf, -np.inf], np.nan)
def f38cb_f38_cycle_bottom_value_excesscash_pb_emadisp_252d_jerk_v025_signal(cashneq, debt, pb):
    cushion = (cashneq - debt) / (cashneq.abs() + debt.abs() + 1.0); cheap = _cp(pb); b = np.tanh(cushion) * cheap; b = b - b.ewm(span=63, min_periods=21).mean()
    b = b.replace([np.inf, -np.inf], np.nan)
    o = (b - 2.0 * b.shift(63) + b.shift(126)) / 3969.0
    return o.replace([np.inf, -np.inf], np.nan)
def f38cb_f38_cycle_bottom_value_survfloor_ev_sqrtmag_252d_jerk_v026_signal(tangibles, cashneq, debt, evebitda):
    floor = (tangibles + cashneq) / debt.replace(0, np.nan); cheap = _ce(evebitda); b = np.tanh(floor / 5.0) * cheap; b = np.sign(b) * (b.abs() ** 0.5)
    b = b.replace([np.inf, -np.inf], np.nan)
    o = (b - 2.0 * b.shift(63) + b.shift(126)) / 3969.0
    return o.replace([np.inf, -np.inf], np.nan)
def f38cb_f38_cycle_bottom_value_tangint_ev_tanh_252d_jerk_v027_signal(tangibles, equity, evebitda):
    ti = tangibles / equity.replace(0, np.nan); cheap = _ce(evebitda); b = np.tanh(ti) * cheap; b = np.tanh(b / (b.abs().rolling(126, min_periods=42).mean() + 1e-9))
    b = b.replace([np.inf, -np.inf], np.nan)
    o = (b - 2.0 * b.shift(63) + b.shift(126)) / 3969.0
    return o.replace([np.inf, -np.inf], np.nan)
def f38cb_f38_cycle_bottom_value_mctanginv_gate_shortlong_252d_jerk_v028_signal(marketcap, tangibles, cashneq, debt):
    pt = marketcap / tangibles.replace(0, np.nan); inv = 1.0 / pt.replace(0, np.nan); gate = _sg(cashneq, debt); b = inv * gate; b = _mean(b, 21) - _mean(b, 126)
    b = b.replace([np.inf, -np.inf], np.nan)
    o = (b - 2.0 * b.shift(63) + b.shift(126)) / 3969.0
    return o.replace([np.inf, -np.inf], np.nan)
def f38cb_f38_cycle_bottom_value_grahamnet_cov_z504_252d_jerk_v029_signal(tangibles, debt, marketcap, cashneq):
    netnet = (tangibles - debt) / marketcap.replace(0, np.nan); cov = _ncr(cashneq, debt).clip(upper=8.0); b = np.tanh(netnet) * cov; b = _z(b, 504)
    b = b.replace([np.inf, -np.inf], np.nan)
    o = (b - 2.0 * b.shift(63) + b.shift(126)) / 3969.0
    return o.replace([np.inf, -np.inf], np.nan)
def f38cb_f38_cycle_bottom_value_threeway_rank504_252d_jerk_v030_signal(tangibles, marketcap, cashneq, debt, evebitda):
    a = _z(_tb(tangibles, marketcap), 252); s = _z(_ncr(cashneq, debt), 252); rr = _z(evebitda, 252); b = (a + s - rr) / 3.0; b = _rank(b, 504)
    b = b.replace([np.inf, -np.inf], np.nan)
    o = (b - 2.0 * b.shift(63) + b.shift(126)) / 3969.0
    return o.replace([np.inf, -np.inf], np.nan)
def f38cb_f38_cycle_bottom_value_liqfix_pb_zscoremr_252d_jerk_v031_signal(cashneq, debt, marketcap, tangibles, pb):
    liq = _nc(cashneq, debt) / marketcap.replace(0, np.nan); fix = _tb(tangibles, marketcap); mix = _z(liq, 252) - _z(fix, 252); cheap = _rank(_cp(pb), 252) + 0.5; b = mix * cheap; b = _z(b, 126) - _z(b, 252)
    b = b.replace([np.inf, -np.inf], np.nan)
    o = (b - 2.0 * b.shift(63) + b.shift(126)) / 3969.0
    return o.replace([np.inf, -np.inf], np.nan)
def f38cb_f38_cycle_bottom_value_evtangtrough_logmag_504d_jerk_v032_signal(marketcap, debt, cashneq, tangibles):
    ev = _ev(marketcap, debt, cashneq); et = ev / tangibles.replace(0, np.nan); trough = (_mean(et, 504) - et) / _mean(et, 504).replace(0, np.nan); b = trough; b = np.sign(b) * np.log1p(b.abs())
    b = b.replace([np.inf, -np.inf], np.nan)
    o = (b - 2.0 * b.shift(63) + b.shift(126)) / 3969.0
    return o.replace([np.inf, -np.inf], np.nan)
def f38cb_f38_cycle_bottom_value_pbtrough_gate_emaratio_504d_jerk_v033_signal(pb, cashneq, debt):
    mid = _mean(pb, 504); trough = (mid - pb) / mid.replace(0, np.nan); gate = _sg(cashneq, debt); b = trough * gate; b = b / (b.ewm(span=126, min_periods=42).mean().abs() + 1e-9)
    b = b.replace([np.inf, -np.inf], np.nan)
    o = (b - 2.0 * b.shift(63) + b.shift(126)) / 3969.0
    return o.replace([np.inf, -np.inf], np.nan)
def f38cb_f38_cycle_bottom_value_evtrough_tang_lvl_504d_jerk_v034_signal(evebitda, tangibles, marketcap):
    mid = _mean(evebitda, 504); trough = (mid - evebitda) / mid.replace(0, np.nan); back = _z(_tb(tangibles, marketcap), 252); b = trough + 0.3 * back
    b = b.replace([np.inf, -np.inf], np.nan)
    o = (b - 2.0 * b.shift(63) + b.shift(126)) / 3969.0
    return o.replace([np.inf, -np.inf], np.nan)
def f38cb_f38_cycle_bottom_value_cashrich_pb_z252_252d_jerk_v035_signal(cashneq, tangibles, pb):
    rich = cashneq / (tangibles + cashneq).replace(0, np.nan); cheap = _cp(pb); b = rich * cheap; b = _z(b, 252)
    b = b.replace([np.inf, -np.inf], np.nan)
    o = (b - 2.0 * b.shift(63) + b.shift(126)) / 3969.0
    return o.replace([np.inf, -np.inf], np.nan)
def f38cb_f38_cycle_bottom_value_assetsurplus_ev_rank252_252d_jerk_v036_signal(tangibles, debt, evebitda):
    surplus = tangibles / debt.replace(0, np.nan) - 1.0; cheap = _ce(evebitda); b = np.tanh(surplus) * np.tanh(cheap); b = _rank(b, 252)
    b = b.replace([np.inf, -np.inf], np.nan)
    o = (b - 2.0 * b.shift(63) + b.shift(126)) / 3969.0
    return o.replace([np.inf, -np.inf], np.nan)
def f38cb_f38_cycle_bottom_value_evdeep_gate_ratio_1260d_jerk_v037_signal(evebitda, cashneq, debt):
    deepz = -_z(evebitda, 1260); gate = _sg(cashneq, debt); b = deepz * gate; b = b / (_mean(b, 252).abs() + 1e-9)
    b = b.replace([np.inf, -np.inf], np.nan)
    o = (b - 2.0 * b.shift(126) + b.shift(252)) / 15876.0
    return o.replace([np.inf, -np.inf], np.nan)
def f38cb_f38_cycle_bottom_value_pbdeep_cov_emadisp_1260d_jerk_v038_signal(pb, cashneq, debt):
    deepz = _z(_cp(pb), 1260); cov = _ncr(cashneq, debt).clip(upper=8.0); b = deepz * cov; b = b - b.ewm(span=63, min_periods=21).mean()
    b = b.replace([np.inf, -np.inf], np.nan)
    o = (b - 2.0 * b.shift(126) + b.shift(252)) / 15876.0
    return o.replace([np.inf, -np.inf], np.nan)
def f38cb_f38_cycle_bottom_value_netnetfloor_ev_sqrtmag_504d_jerk_v039_signal(tangibles, cashneq, debt, marketcap, evebitda):
    floor = (tangibles + cashneq - debt) / marketcap.replace(0, np.nan); b = _z(floor, 504) - _z(evebitda, 504); b = np.sign(b) * (b.abs() ** 0.5)
    b = b.replace([np.inf, -np.inf], np.nan)
    o = (b - 2.0 * b.shift(63) + b.shift(126)) / 3969.0
    return o.replace([np.inf, -np.inf], np.nan)
def f38cb_f38_cycle_bottom_value_tangcoverdebt_pb_tanh_252d_jerk_v040_signal(tangibles, debt, pb):
    cover = tangibles / debt.replace(0, np.nan); gate = 1.0 / (1.0 + np.exp(-(cover - 1.0))); cheap = _cp(pb); b = cheap * gate; b = np.tanh(b / (b.abs().rolling(126, min_periods=42).mean() + 1e-9))
    b = b.replace([np.inf, -np.inf], np.nan)
    o = (b - 2.0 * b.shift(63) + b.shift(126)) / 3969.0
    return o.replace([np.inf, -np.inf], np.nan)
def f38cb_f38_cycle_bottom_value_evev_ncyld_shortlong_1260d_jerk_v041_signal(marketcap, debt, cashneq, evebitda):
    ev = _ev(marketcap, debt, cashneq); ncyld = _nc(cashneq, debt) / ev.replace(0, np.nan); cheap = _z(_ce(evebitda), 1260); b = _z(ncyld, 1260) + cheap; b = _mean(b, 21) - _mean(b, 126)
    b = b.replace([np.inf, -np.inf], np.nan)
    o = (b - 2.0 * b.shift(126) + b.shift(252)) / 15876.0
    return o.replace([np.inf, -np.inf], np.nan)
def f38cb_f38_cycle_bottom_value_tangshare_solv_z504_252d_jerk_v042_signal(tangibles, equity, cashneq, debt):
    share = tangibles / equity.replace(0, np.nan); gate = _sg(cashneq, debt); b = np.tanh(share) * gate; b = _z(b, 504)
    b = b.replace([np.inf, -np.inf], np.nan)
    o = (b - 2.0 * b.shift(63) + b.shift(126)) / 3969.0
    return o.replace([np.inf, -np.inf], np.nan)
def f38cb_f38_cycle_bottom_value_pbcov_geo_rank504_252d_jerk_v043_signal(pb, cashneq, debt):
    cheap = _cp(pb); cov = _ncr(cashneq, debt).clip(lower=0.0); b = np.sqrt(cheap.clip(lower=0) * cov); b = _rank(b, 504)
    b = b.replace([np.inf, -np.inf], np.nan)
    o = (b - 2.0 * b.shift(63) + b.shift(126)) / 3969.0
    return o.replace([np.inf, -np.inf], np.nan)
def f38cb_f38_cycle_bottom_value_cheappb_netcash_zscoremr_252d_jerk_v044_signal(pb, cashneq, debt):
    cheap = _cp(pb); gate = _sg(cashneq, debt); b = cheap * gate; b = _z(b, 126) - _z(b, 252)
    b = b.replace([np.inf, -np.inf], np.nan)
    o = (b - 2.0 * b.shift(21) + b.shift(42)) / 441.0
    return o.replace([np.inf, -np.inf], np.nan)
def f38cb_f38_cycle_bottom_value_cheapev_cov_z252_252d_jerk_v045_signal(evebitda, cashneq, debt):
    cheap = _ce(evebitda); cov = _ncr(cashneq, debt).clip(upper=10.0); b = cheap * cov; b = _z(b, 252)
    b = b.replace([np.inf, -np.inf], np.nan)
    o = (b - 2.0 * b.shift(21) + b.shift(42)) / 441.0
    return o.replace([np.inf, -np.inf], np.nan)
def f38cb_f38_cycle_bottom_value_pbz_tangback_emaratio_252d_jerk_v046_signal(pb, tangibles, marketcap):
    cheapz = _z(_cp(pb), 252); back = _tb(tangibles, marketcap); b = cheapz * back; b = b / (b.ewm(span=126, min_periods=42).mean().abs() + 1e-9)
    b = b.replace([np.inf, -np.inf], np.nan)
    o = (b - 2.0 * b.shift(21) + b.shift(42)) / 441.0
    return o.replace([np.inf, -np.inf], np.nan)
def f38cb_f38_cycle_bottom_value_evnetcash_lvl_252d_jerk_v047_signal(evebitda, cashneq, debt):
    cz = _z(_ce(evebitda), 252); sz = _z(_nc(cashneq, debt), 252); b = cz + sz
    b = b.replace([np.inf, -np.inf], np.nan)
    o = (b - 2.0 * b.shift(21) + b.shift(42)) / 441.0
    return o.replace([np.inf, -np.inf], np.nan)
def f38cb_f38_cycle_bottom_value_navdisc_gate_z252_252d_jerk_v048_signal(tangibles, marketcap, cashneq, debt):
    disc = (tangibles - marketcap) / marketcap.replace(0, np.nan); gate = _sg(cashneq, debt); b = disc * gate; b = _z(b, 252)
    b = b.replace([np.inf, -np.inf], np.nan)
    o = (b - 2.0 * b.shift(21) + b.shift(42)) / 441.0
    return o.replace([np.inf, -np.inf], np.nan)
def f38cb_f38_cycle_bottom_value_blendcheap_cov_rank252_252d_jerk_v049_signal(pb, evebitda, cashneq, debt):
    blend = 0.5 * _rank(_cp(pb), 252) + 0.5 * _rank(_ce(evebitda), 252); cov = _ncr(cashneq, debt).clip(upper=8.0); b = blend * cov; b = _rank(b, 252)
    b = b.replace([np.inf, -np.inf], np.nan)
    o = (b - 2.0 * b.shift(21) + b.shift(42)) / 441.0
    return o.replace([np.inf, -np.inf], np.nan)
def f38cb_f38_cycle_bottom_value_tangeq_cheap_ratio_252d_jerk_v050_signal(tangibles, equity, pb):
    tq = tangibles / equity.replace(0, np.nan); cheap = _cp(pb); b = tq * cheap; b = b / (_mean(b, 252).abs() + 1e-9)
    b = b.replace([np.inf, -np.inf], np.nan)
    o = (b - 2.0 * b.shift(21) + b.shift(42)) / 441.0
    return o.replace([np.inf, -np.inf], np.nan)
def f38cb_f38_cycle_bottom_value_netcashmc_ev_emadisp_252d_jerk_v051_signal(cashneq, debt, marketcap, evebitda):
    ncmc = _nc(cashneq, debt) / marketcap.replace(0, np.nan); cheap = _ce(evebitda); b = ncmc * cheap; b = b - b.ewm(span=63, min_periods=21).mean()
    b = b.replace([np.inf, -np.inf], np.nan)
    o = (b - 2.0 * b.shift(21) + b.shift(42)) / 441.0
    return o.replace([np.inf, -np.inf], np.nan)
def f38cb_f38_cycle_bottom_value_bookyld_solv_sqrtmag_252d_jerk_v052_signal(equity, marketcap, cashneq, debt):
    byld = equity / marketcap.replace(0, np.nan); gate = _sg(cashneq, debt); b = byld * gate; b = np.sign(b) * (b.abs() ** 0.5)
    b = b.replace([np.inf, -np.inf], np.nan)
    o = (b - 2.0 * b.shift(21) + b.shift(42)) / 441.0
    return o.replace([np.inf, -np.inf], np.nan)
def f38cb_f38_cycle_bottom_value_warchest_pb_tanh_252d_jerk_v053_signal(cashneq, debt, equity, pb):
    wc = _nc(cashneq, debt) / equity.replace(0, np.nan); cheap = _cp(pb); b = wc * cheap; b = np.tanh(b / (b.abs().rolling(126, min_periods=42).mean() + 1e-9))
    b = b.replace([np.inf, -np.inf], np.nan)
    o = (b - 2.0 * b.shift(21) + b.shift(42)) / 441.0
    return o.replace([np.inf, -np.inf], np.nan)
def f38cb_f38_cycle_bottom_value_buffer_ev_shortlong_252d_jerk_v054_signal(cashneq, debt, tangibles, evebitda):
    buf = _nc(cashneq, debt) / tangibles.replace(0, np.nan); cheap = _ce(evebitda); b = buf * cheap; b = _mean(b, 21) - _mean(b, 126)
    b = b.replace([np.inf, -np.inf], np.nan)
    o = (b - 2.0 * b.shift(21) + b.shift(42)) / 441.0
    return o.replace([np.inf, -np.inf], np.nan)
def f38cb_f38_cycle_bottom_value_evtang_inv_z504_252d_jerk_v055_signal(marketcap, debt, cashneq, tangibles):
    ev = _ev(marketcap, debt, cashneq); et = ev / tangibles.replace(0, np.nan); b = 1.0 / et.replace(0, np.nan); b = _z(b, 504)
    b = b.replace([np.inf, -np.inf], np.nan)
    o = (b - 2.0 * b.shift(21) + b.shift(42)) / 441.0
    return o.replace([np.inf, -np.inf], np.nan)
def f38cb_f38_cycle_bottom_value_tangfloor_pb_rank504_252d_jerk_v056_signal(tangibles, marketcap, pb):
    back = _tb(tangibles, marketcap); cheap = _cp(pb); b = back * cheap; b = _rank(b, 504)
    b = b.replace([np.inf, -np.inf], np.nan)
    o = (b - 2.0 * b.shift(21) + b.shift(42)) / 441.0
    return o.replace([np.inf, -np.inf], np.nan)
def f38cb_f38_cycle_bottom_value_netcashev_cheap_zscoremr_252d_jerk_v057_signal(cashneq, debt, marketcap, evebitda):
    ev = _ev(marketcap, debt, cashneq); cover = _nc(cashneq, debt) / ev.replace(0, np.nan); cheap = _ce(evebitda); b = cover * cheap; b = _z(b, 126) - _z(b, 252)
    b = b.replace([np.inf, -np.inf], np.nan)
    o = (b - 2.0 * b.shift(21) + b.shift(42)) / 441.0
    return o.replace([np.inf, -np.inf], np.nan)
def f38cb_f38_cycle_bottom_value_triple_logmag_252d_jerk_v058_signal(pb, evebitda, cashneq, debt):
    a = _z(_cp(pb), 252); c = _z(_ce(evebitda), 252); s = _z(_nc(cashneq, debt), 252); b = (a + c + s) / 3.0; b = np.sign(b) * np.log1p(b.abs())
    b = b.replace([np.inf, -np.inf], np.nan)
    o = (b - 2.0 * b.shift(21) + b.shift(42)) / 441.0
    return o.replace([np.inf, -np.inf], np.nan)
def f38cb_f38_cycle_bottom_value_tangdebt_ev_emaratio_252d_jerk_v059_signal(tangibles, debt, evebitda):
    tcov = (tangibles / debt.replace(0, np.nan)).clip(upper=20.0); cheap = _ce(evebitda); b = tcov * cheap; b = b / (b.ewm(span=126, min_periods=42).mean().abs() + 1e-9)
    b = b.replace([np.inf, -np.inf], np.nan)
    o = (b - 2.0 * b.shift(21) + b.shift(42)) / 441.0
    return o.replace([np.inf, -np.inf], np.nan)
def f38cb_f38_cycle_bottom_value_eqdebt_pb_lvl_252d_jerk_v060_signal(equity, debt, pb):
    eqd = equity / debt.replace(0, np.nan); gate = 1.0 / (1.0 + np.exp(-(eqd - 1.0))); cheap = _cp(pb); b = cheap * gate
    b = b.replace([np.inf, -np.inf], np.nan)
    o = (b - 2.0 * b.shift(21) + b.shift(42)) / 441.0
    return o.replace([np.inf, -np.inf], np.nan)
def f38cb_f38_cycle_bottom_value_netdebteq_pb_z252_252d_jerk_v061_signal(debt, cashneq, equity, pb):
    nde = (debt - cashneq) / equity.replace(0, np.nan); low = 1.0 / (1.0 + np.exp(nde)); cheap = _cp(pb); b = low * cheap; b = _z(b, 252)
    b = b.replace([np.inf, -np.inf], np.nan)
    o = (b - 2.0 * b.shift(21) + b.shift(42)) / 441.0
    return o.replace([np.inf, -np.inf], np.nan)
def f38cb_f38_cycle_bottom_value_cashmc_ev_rank252_252d_jerk_v062_signal(cashneq, marketcap, evebitda):
    cashmc = cashneq / marketcap.replace(0, np.nan); cheap = _ce(evebitda); b = cashmc * cheap; b = _rank(b, 252)
    b = b.replace([np.inf, -np.inf], np.nan)
    o = (b - 2.0 * b.shift(21) + b.shift(42)) / 441.0
    return o.replace([np.inf, -np.inf], np.nan)
def f38cb_f38_cycle_bottom_value_ncmctang_ratio_252d_jerk_v063_signal(cashneq, debt, tangibles, pb):
    liq = _nc(cashneq, debt) / tangibles.replace(0, np.nan); cheap = _cp(pb); b = np.tanh(liq) * cheap; b = b / (_mean(b, 252).abs() + 1e-9)
    b = b.replace([np.inf, -np.inf], np.nan)
    o = (b - 2.0 * b.shift(21) + b.shift(42)) / 441.0
    return o.replace([np.inf, -np.inf], np.nan)
def f38cb_f38_cycle_bottom_value_eveq_cov_emadisp_252d_jerk_v064_signal(marketcap, debt, cashneq, equity):
    ev = _ev(marketcap, debt, cashneq); inv = equity / ev.replace(0, np.nan); cov = _ncr(cashneq, debt).clip(upper=8.0); b = inv * cov; b = b - b.ewm(span=63, min_periods=21).mean()
    b = b.replace([np.inf, -np.inf], np.nan)
    o = (b - 2.0 * b.shift(21) + b.shift(42)) / 441.0
    return o.replace([np.inf, -np.inf], np.nan)
def f38cb_f38_cycle_bottom_value_tangcov_evz_sqrtmag_252d_jerk_v065_signal(tangibles, debt, evebitda):
    cov = _z(tangibles / debt.replace(0, np.nan), 252); cheap = _z(_ce(evebitda), 252); b = cov + cheap; b = np.sign(b) * (b.abs() ** 0.5)
    b = b.replace([np.inf, -np.inf], np.nan)
    o = (b - 2.0 * b.shift(21) + b.shift(42)) / 441.0
    return o.replace([np.inf, -np.inf], np.nan)
def f38cb_f38_cycle_bottom_value_netnet_mc_tanh_252d_jerk_v066_signal(tangibles, debt, marketcap, pb):
    netnet = (tangibles - debt) / marketcap.replace(0, np.nan); cheap = _cp(pb); b = netnet * (1.0 + np.tanh(cheap)); b = np.tanh(b / (b.abs().rolling(126, min_periods=42).mean() + 1e-9))
    b = b.replace([np.inf, -np.inf], np.nan)
    o = (b - 2.0 * b.shift(21) + b.shift(42)) / 441.0
    return o.replace([np.inf, -np.inf], np.nan)
def f38cb_f38_cycle_bottom_value_bookyld_cov_shortlong_252d_jerk_v067_signal(equity, marketcap, cashneq, debt):
    byld = equity / marketcap.replace(0, np.nan); cov = _ncr(cashneq, debt).clip(upper=8.0); b = byld * cov; b = _mean(b, 21) - _mean(b, 126)
    b = b.replace([np.inf, -np.inf], np.nan)
    o = (b - 2.0 * b.shift(21) + b.shift(42)) / 441.0
    return o.replace([np.inf, -np.inf], np.nan)
def f38cb_f38_cycle_bottom_value_excesscash_pb_z504_252d_jerk_v068_signal(cashneq, debt, pb):
    cushion = (cashneq - debt) / (cashneq.abs() + debt.abs() + 1.0); cheap = _cp(pb); b = np.tanh(cushion) * cheap; b = _z(b, 504)
    b = b.replace([np.inf, -np.inf], np.nan)
    o = (b - 2.0 * b.shift(21) + b.shift(42)) / 441.0
    return o.replace([np.inf, -np.inf], np.nan)
def f38cb_f38_cycle_bottom_value_survfloor_ev_rank504_252d_jerk_v069_signal(tangibles, cashneq, debt, evebitda):
    floor = (tangibles + cashneq) / debt.replace(0, np.nan); cheap = _ce(evebitda); b = np.tanh(floor / 5.0) * cheap; b = _rank(b, 504)
    b = b.replace([np.inf, -np.inf], np.nan)
    o = (b - 2.0 * b.shift(21) + b.shift(42)) / 441.0
    return o.replace([np.inf, -np.inf], np.nan)
def f38cb_f38_cycle_bottom_value_tangint_ev_zscoremr_252d_jerk_v070_signal(tangibles, equity, evebitda):
    ti = tangibles / equity.replace(0, np.nan); cheap = _ce(evebitda); b = np.tanh(ti) * cheap; b = _z(b, 126) - _z(b, 252)
    b = b.replace([np.inf, -np.inf], np.nan)
    o = (b - 2.0 * b.shift(21) + b.shift(42)) / 441.0
    return o.replace([np.inf, -np.inf], np.nan)
def f38cb_f38_cycle_bottom_value_mctanginv_gate_logmag_252d_jerk_v071_signal(marketcap, tangibles, cashneq, debt):
    pt = marketcap / tangibles.replace(0, np.nan); inv = 1.0 / pt.replace(0, np.nan); gate = _sg(cashneq, debt); b = inv * gate; b = np.sign(b) * np.log1p(b.abs())
    b = b.replace([np.inf, -np.inf], np.nan)
    o = (b - 2.0 * b.shift(21) + b.shift(42)) / 441.0
    return o.replace([np.inf, -np.inf], np.nan)
def f38cb_f38_cycle_bottom_value_grahamnet_cov_emaratio_252d_jerk_v072_signal(tangibles, debt, marketcap, cashneq):
    netnet = (tangibles - debt) / marketcap.replace(0, np.nan); cov = _ncr(cashneq, debt).clip(upper=8.0); b = np.tanh(netnet) * cov; b = b / (b.ewm(span=126, min_periods=42).mean().abs() + 1e-9)
    b = b.replace([np.inf, -np.inf], np.nan)
    o = (b - 2.0 * b.shift(21) + b.shift(42)) / 441.0
    return o.replace([np.inf, -np.inf], np.nan)
def f38cb_f38_cycle_bottom_value_threeway_lvl_252d_jerk_v073_signal(tangibles, marketcap, cashneq, debt, evebitda):
    a = _z(_tb(tangibles, marketcap), 252); s = _z(_ncr(cashneq, debt), 252); rr = _z(evebitda, 252); b = (a + s - rr) / 3.0
    b = b.replace([np.inf, -np.inf], np.nan)
    o = (b - 2.0 * b.shift(21) + b.shift(42)) / 441.0
    return o.replace([np.inf, -np.inf], np.nan)
def f38cb_f38_cycle_bottom_value_liqfix_pb_z252_252d_jerk_v074_signal(cashneq, debt, marketcap, tangibles, pb):
    liq = _nc(cashneq, debt) / marketcap.replace(0, np.nan); fix = _tb(tangibles, marketcap); mix = _z(liq, 252) - _z(fix, 252); cheap = _rank(_cp(pb), 252) + 0.5; b = mix * cheap; b = _z(b, 252)
    b = b.replace([np.inf, -np.inf], np.nan)
    o = (b - 2.0 * b.shift(21) + b.shift(42)) / 441.0
    return o.replace([np.inf, -np.inf], np.nan)
def f38cb_f38_cycle_bottom_value_evtangtrough_rank252_504d_jerk_v075_signal(marketcap, debt, cashneq, tangibles):
    ev = _ev(marketcap, debt, cashneq); et = ev / tangibles.replace(0, np.nan); trough = (_mean(et, 504) - et) / _mean(et, 504).replace(0, np.nan); b = trough; b = _rank(b, 252)
    b = b.replace([np.inf, -np.inf], np.nan)
    o = (b - 2.0 * b.shift(21) + b.shift(42)) / 441.0
    return o.replace([np.inf, -np.inf], np.nan)
def f38cb_f38_cycle_bottom_value_pbtrough_gate_ratio_504d_jerk_v076_signal(pb, cashneq, debt):
    mid = _mean(pb, 504); trough = (mid - pb) / mid.replace(0, np.nan); gate = _sg(cashneq, debt); b = trough * gate; b = b / (_mean(b, 252).abs() + 1e-9)
    b = b.replace([np.inf, -np.inf], np.nan)
    o = (b - 2.0 * b.shift(21) + b.shift(42)) / 441.0
    return o.replace([np.inf, -np.inf], np.nan)
def f38cb_f38_cycle_bottom_value_evtrough_tang_emadisp_504d_jerk_v077_signal(evebitda, tangibles, marketcap):
    mid = _mean(evebitda, 504); trough = (mid - evebitda) / mid.replace(0, np.nan); back = _z(_tb(tangibles, marketcap), 252); b = trough + 0.3 * back; b = b - b.ewm(span=63, min_periods=21).mean()
    b = b.replace([np.inf, -np.inf], np.nan)
    o = (b - 2.0 * b.shift(21) + b.shift(42)) / 441.0
    return o.replace([np.inf, -np.inf], np.nan)
def f38cb_f38_cycle_bottom_value_cashrich_pb_sqrtmag_252d_jerk_v078_signal(cashneq, tangibles, pb):
    rich = cashneq / (tangibles + cashneq).replace(0, np.nan); cheap = _cp(pb); b = rich * cheap; b = np.sign(b) * (b.abs() ** 0.5)
    b = b.replace([np.inf, -np.inf], np.nan)
    o = (b - 2.0 * b.shift(21) + b.shift(42)) / 441.0
    return o.replace([np.inf, -np.inf], np.nan)
def f38cb_f38_cycle_bottom_value_assetsurplus_ev_tanh_252d_jerk_v079_signal(tangibles, debt, evebitda):
    surplus = tangibles / debt.replace(0, np.nan) - 1.0; cheap = _ce(evebitda); b = np.tanh(surplus) * np.tanh(cheap); b = np.tanh(b / (b.abs().rolling(126, min_periods=42).mean() + 1e-9))
    b = b.replace([np.inf, -np.inf], np.nan)
    o = (b - 2.0 * b.shift(21) + b.shift(42)) / 441.0
    return o.replace([np.inf, -np.inf], np.nan)
def f38cb_f38_cycle_bottom_value_evdeep_gate_shortlong_1260d_jerk_v080_signal(evebitda, cashneq, debt):
    deepz = -_z(evebitda, 1260); gate = _sg(cashneq, debt); b = deepz * gate; b = _mean(b, 21) - _mean(b, 126)
    b = b.replace([np.inf, -np.inf], np.nan)
    o = (b - 2.0 * b.shift(63) + b.shift(126)) / 3969.0
    return o.replace([np.inf, -np.inf], np.nan)
def f38cb_f38_cycle_bottom_value_pbdeep_cov_z504_1260d_jerk_v081_signal(pb, cashneq, debt):
    deepz = _z(_cp(pb), 1260); cov = _ncr(cashneq, debt).clip(upper=8.0); b = deepz * cov; b = _z(b, 504)
    b = b.replace([np.inf, -np.inf], np.nan)
    o = (b - 2.0 * b.shift(63) + b.shift(126)) / 3969.0
    return o.replace([np.inf, -np.inf], np.nan)
def f38cb_f38_cycle_bottom_value_netnetfloor_ev_rank504_504d_jerk_v082_signal(tangibles, cashneq, debt, marketcap, evebitda):
    floor = (tangibles + cashneq - debt) / marketcap.replace(0, np.nan); b = _z(floor, 504) - _z(evebitda, 504); b = _rank(b, 504)
    b = b.replace([np.inf, -np.inf], np.nan)
    o = (b - 2.0 * b.shift(21) + b.shift(42)) / 441.0
    return o.replace([np.inf, -np.inf], np.nan)
def f38cb_f38_cycle_bottom_value_tangcoverdebt_pb_zscoremr_252d_jerk_v083_signal(tangibles, debt, pb):
    cover = tangibles / debt.replace(0, np.nan); gate = 1.0 / (1.0 + np.exp(-(cover - 1.0))); cheap = _cp(pb); b = cheap * gate; b = _z(b, 126) - _z(b, 252)
    b = b.replace([np.inf, -np.inf], np.nan)
    o = (b - 2.0 * b.shift(21) + b.shift(42)) / 441.0
    return o.replace([np.inf, -np.inf], np.nan)
def f38cb_f38_cycle_bottom_value_evev_ncyld_logmag_1260d_jerk_v084_signal(marketcap, debt, cashneq, evebitda):
    ev = _ev(marketcap, debt, cashneq); ncyld = _nc(cashneq, debt) / ev.replace(0, np.nan); cheap = _z(_ce(evebitda), 1260); b = _z(ncyld, 1260) + cheap; b = np.sign(b) * np.log1p(b.abs())
    b = b.replace([np.inf, -np.inf], np.nan)
    o = (b - 2.0 * b.shift(63) + b.shift(126)) / 3969.0
    return o.replace([np.inf, -np.inf], np.nan)
def f38cb_f38_cycle_bottom_value_tangshare_solv_emaratio_252d_jerk_v085_signal(tangibles, equity, cashneq, debt):
    share = tangibles / equity.replace(0, np.nan); gate = _sg(cashneq, debt); b = np.tanh(share) * gate; b = b / (b.ewm(span=126, min_periods=42).mean().abs() + 1e-9)
    b = b.replace([np.inf, -np.inf], np.nan)
    o = (b - 2.0 * b.shift(21) + b.shift(42)) / 441.0
    return o.replace([np.inf, -np.inf], np.nan)
def f38cb_f38_cycle_bottom_value_pbcov_geo_lvl_252d_jerk_v086_signal(pb, cashneq, debt):
    cheap = _cp(pb); cov = _ncr(cashneq, debt).clip(lower=0.0); b = np.sqrt(cheap.clip(lower=0) * cov)
    b = b.replace([np.inf, -np.inf], np.nan)
    o = (b - 2.0 * b.shift(21) + b.shift(42)) / 441.0
    return o.replace([np.inf, -np.inf], np.nan)
def f38cb_f38_cycle_bottom_value_cheappb_netcash_z252_252d_jerk_v087_signal(pb, cashneq, debt):
    cheap = _cp(pb); gate = _sg(cashneq, debt); b = cheap * gate; b = _z(b, 252)
    b = b.replace([np.inf, -np.inf], np.nan)
    o = (b - 2.0 * b.shift(84) + b.shift(168)) / 7056.0
    return o.replace([np.inf, -np.inf], np.nan)
def f38cb_f38_cycle_bottom_value_cheapev_cov_z504_252d_jerk_v088_signal(evebitda, cashneq, debt):
    cheap = _ce(evebitda); cov = _ncr(cashneq, debt).clip(upper=10.0); b = cheap * cov; b = _z(b, 504)
    b = b.replace([np.inf, -np.inf], np.nan)
    o = (b - 2.0 * b.shift(84) + b.shift(168)) / 7056.0
    return o.replace([np.inf, -np.inf], np.nan)
def f38cb_f38_cycle_bottom_value_pbz_tangback_ratio_252d_jerk_v089_signal(pb, tangibles, marketcap):
    cheapz = _z(_cp(pb), 252); back = _tb(tangibles, marketcap); b = cheapz * back; b = b / (_mean(b, 252).abs() + 1e-9)
    b = b.replace([np.inf, -np.inf], np.nan)
    o = (b - 2.0 * b.shift(84) + b.shift(168)) / 7056.0
    return o.replace([np.inf, -np.inf], np.nan)
def f38cb_f38_cycle_bottom_value_evnetcash_emadisp_252d_jerk_v090_signal(evebitda, cashneq, debt):
    cz = _z(_ce(evebitda), 252); sz = _z(_nc(cashneq, debt), 252); b = cz + sz; b = b - b.ewm(span=63, min_periods=21).mean()
    b = b.replace([np.inf, -np.inf], np.nan)
    o = (b - 2.0 * b.shift(84) + b.shift(168)) / 7056.0
    return o.replace([np.inf, -np.inf], np.nan)
def f38cb_f38_cycle_bottom_value_navdisc_gate_sqrtmag_252d_jerk_v091_signal(tangibles, marketcap, cashneq, debt):
    disc = (tangibles - marketcap) / marketcap.replace(0, np.nan); gate = _sg(cashneq, debt); b = disc * gate; b = np.sign(b) * (b.abs() ** 0.5)
    b = b.replace([np.inf, -np.inf], np.nan)
    o = (b - 2.0 * b.shift(84) + b.shift(168)) / 7056.0
    return o.replace([np.inf, -np.inf], np.nan)
def f38cb_f38_cycle_bottom_value_blendcheap_cov_tanh_252d_jerk_v092_signal(pb, evebitda, cashneq, debt):
    blend = 0.5 * _rank(_cp(pb), 252) + 0.5 * _rank(_ce(evebitda), 252); cov = _ncr(cashneq, debt).clip(upper=8.0); b = blend * cov; b = np.tanh(b / (b.abs().rolling(126, min_periods=42).mean() + 1e-9))
    b = b.replace([np.inf, -np.inf], np.nan)
    o = (b - 2.0 * b.shift(84) + b.shift(168)) / 7056.0
    return o.replace([np.inf, -np.inf], np.nan)
def f38cb_f38_cycle_bottom_value_tangeq_cheap_shortlong_252d_jerk_v093_signal(tangibles, equity, pb):
    tq = tangibles / equity.replace(0, np.nan); cheap = _cp(pb); b = tq * cheap; b = _mean(b, 21) - _mean(b, 126)
    b = b.replace([np.inf, -np.inf], np.nan)
    o = (b - 2.0 * b.shift(84) + b.shift(168)) / 7056.0
    return o.replace([np.inf, -np.inf], np.nan)
def f38cb_f38_cycle_bottom_value_netcashmc_ev_z504_252d_jerk_v094_signal(cashneq, debt, marketcap, evebitda):
    ncmc = _nc(cashneq, debt) / marketcap.replace(0, np.nan); cheap = _ce(evebitda); b = ncmc * cheap; b = _z(b, 504)
    b = b.replace([np.inf, -np.inf], np.nan)
    o = (b - 2.0 * b.shift(84) + b.shift(168)) / 7056.0
    return o.replace([np.inf, -np.inf], np.nan)
def f38cb_f38_cycle_bottom_value_bookyld_solv_rank504_252d_jerk_v095_signal(equity, marketcap, cashneq, debt):
    byld = equity / marketcap.replace(0, np.nan); gate = _sg(cashneq, debt); b = byld * gate; b = _rank(b, 504)
    b = b.replace([np.inf, -np.inf], np.nan)
    o = (b - 2.0 * b.shift(84) + b.shift(168)) / 7056.0
    return o.replace([np.inf, -np.inf], np.nan)
def f38cb_f38_cycle_bottom_value_warchest_pb_zscoremr_252d_jerk_v096_signal(cashneq, debt, equity, pb):
    wc = _nc(cashneq, debt) / equity.replace(0, np.nan); cheap = _cp(pb); b = wc * cheap; b = _z(b, 126) - _z(b, 252)
    b = b.replace([np.inf, -np.inf], np.nan)
    o = (b - 2.0 * b.shift(84) + b.shift(168)) / 7056.0
    return o.replace([np.inf, -np.inf], np.nan)
def f38cb_f38_cycle_bottom_value_buffer_ev_logmag_252d_jerk_v097_signal(cashneq, debt, tangibles, evebitda):
    buf = _nc(cashneq, debt) / tangibles.replace(0, np.nan); cheap = _ce(evebitda); b = buf * cheap; b = np.sign(b) * np.log1p(b.abs())
    b = b.replace([np.inf, -np.inf], np.nan)
    o = (b - 2.0 * b.shift(84) + b.shift(168)) / 7056.0
    return o.replace([np.inf, -np.inf], np.nan)
def f38cb_f38_cycle_bottom_value_evtang_inv_emaratio_252d_jerk_v098_signal(marketcap, debt, cashneq, tangibles):
    ev = _ev(marketcap, debt, cashneq); et = ev / tangibles.replace(0, np.nan); b = 1.0 / et.replace(0, np.nan); b = b / (b.ewm(span=126, min_periods=42).mean().abs() + 1e-9)
    b = b.replace([np.inf, -np.inf], np.nan)
    o = (b - 2.0 * b.shift(84) + b.shift(168)) / 7056.0
    return o.replace([np.inf, -np.inf], np.nan)
def f38cb_f38_cycle_bottom_value_tangfloor_pb_lvl_252d_jerk_v099_signal(tangibles, marketcap, pb):
    back = _tb(tangibles, marketcap); cheap = _cp(pb); b = back * cheap
    b = b.replace([np.inf, -np.inf], np.nan)
    o = (b - 2.0 * b.shift(84) + b.shift(168)) / 7056.0
    return o.replace([np.inf, -np.inf], np.nan)
def f38cb_f38_cycle_bottom_value_netcashev_cheap_z252_252d_jerk_v100_signal(cashneq, debt, marketcap, evebitda):
    ev = _ev(marketcap, debt, cashneq); cover = _nc(cashneq, debt) / ev.replace(0, np.nan); cheap = _ce(evebitda); b = cover * cheap; b = _z(b, 252)
    b = b.replace([np.inf, -np.inf], np.nan)
    o = (b - 2.0 * b.shift(84) + b.shift(168)) / 7056.0
    return o.replace([np.inf, -np.inf], np.nan)
def f38cb_f38_cycle_bottom_value_triple_rank252_252d_jerk_v101_signal(pb, evebitda, cashneq, debt):
    a = _z(_cp(pb), 252); c = _z(_ce(evebitda), 252); s = _z(_nc(cashneq, debt), 252); b = (a + c + s) / 3.0; b = _rank(b, 252)
    b = b.replace([np.inf, -np.inf], np.nan)
    o = (b - 2.0 * b.shift(84) + b.shift(168)) / 7056.0
    return o.replace([np.inf, -np.inf], np.nan)
def f38cb_f38_cycle_bottom_value_tangdebt_ev_ratio_252d_jerk_v102_signal(tangibles, debt, evebitda):
    tcov = (tangibles / debt.replace(0, np.nan)).clip(upper=20.0); cheap = _ce(evebitda); b = tcov * cheap; b = b / (_mean(b, 252).abs() + 1e-9)
    b = b.replace([np.inf, -np.inf], np.nan)
    o = (b - 2.0 * b.shift(84) + b.shift(168)) / 7056.0
    return o.replace([np.inf, -np.inf], np.nan)
def f38cb_f38_cycle_bottom_value_eqdebt_pb_emadisp_252d_jerk_v103_signal(equity, debt, pb):
    eqd = equity / debt.replace(0, np.nan); gate = 1.0 / (1.0 + np.exp(-(eqd - 1.0))); cheap = _cp(pb); b = cheap * gate; b = b - b.ewm(span=63, min_periods=21).mean()
    b = b.replace([np.inf, -np.inf], np.nan)
    o = (b - 2.0 * b.shift(84) + b.shift(168)) / 7056.0
    return o.replace([np.inf, -np.inf], np.nan)
def f38cb_f38_cycle_bottom_value_netdebteq_pb_sqrtmag_252d_jerk_v104_signal(debt, cashneq, equity, pb):
    nde = (debt - cashneq) / equity.replace(0, np.nan); low = 1.0 / (1.0 + np.exp(nde)); cheap = _cp(pb); b = low * cheap; b = np.sign(b) * (b.abs() ** 0.5)
    b = b.replace([np.inf, -np.inf], np.nan)
    o = (b - 2.0 * b.shift(84) + b.shift(168)) / 7056.0
    return o.replace([np.inf, -np.inf], np.nan)
def f38cb_f38_cycle_bottom_value_cashmc_ev_tanh_252d_jerk_v105_signal(cashneq, marketcap, evebitda):
    cashmc = cashneq / marketcap.replace(0, np.nan); cheap = _ce(evebitda); b = cashmc * cheap; b = np.tanh(b / (b.abs().rolling(126, min_periods=42).mean() + 1e-9))
    b = b.replace([np.inf, -np.inf], np.nan)
    o = (b - 2.0 * b.shift(84) + b.shift(168)) / 7056.0
    return o.replace([np.inf, -np.inf], np.nan)
def f38cb_f38_cycle_bottom_value_ncmctang_shortlong_252d_jerk_v106_signal(cashneq, debt, tangibles, pb):
    liq = _nc(cashneq, debt) / tangibles.replace(0, np.nan); cheap = _cp(pb); b = np.tanh(liq) * cheap; b = _mean(b, 21) - _mean(b, 126)
    b = b.replace([np.inf, -np.inf], np.nan)
    o = (b - 2.0 * b.shift(84) + b.shift(168)) / 7056.0
    return o.replace([np.inf, -np.inf], np.nan)
def f38cb_f38_cycle_bottom_value_eveq_cov_z504_252d_jerk_v107_signal(marketcap, debt, cashneq, equity):
    ev = _ev(marketcap, debt, cashneq); inv = equity / ev.replace(0, np.nan); cov = _ncr(cashneq, debt).clip(upper=8.0); b = inv * cov; b = _z(b, 504)
    b = b.replace([np.inf, -np.inf], np.nan)
    o = (b - 2.0 * b.shift(84) + b.shift(168)) / 7056.0
    return o.replace([np.inf, -np.inf], np.nan)
def f38cb_f38_cycle_bottom_value_tangcov_evz_rank504_252d_jerk_v108_signal(tangibles, debt, evebitda):
    cov = _z(tangibles / debt.replace(0, np.nan), 252); cheap = _z(_ce(evebitda), 252); b = cov + cheap; b = _rank(b, 504)
    b = b.replace([np.inf, -np.inf], np.nan)
    o = (b - 2.0 * b.shift(84) + b.shift(168)) / 7056.0
    return o.replace([np.inf, -np.inf], np.nan)
def f38cb_f38_cycle_bottom_value_netnet_mc_zscoremr_252d_jerk_v109_signal(tangibles, debt, marketcap, pb):
    netnet = (tangibles - debt) / marketcap.replace(0, np.nan); cheap = _cp(pb); b = netnet * (1.0 + np.tanh(cheap)); b = _z(b, 126) - _z(b, 252)
    b = b.replace([np.inf, -np.inf], np.nan)
    o = (b - 2.0 * b.shift(84) + b.shift(168)) / 7056.0
    return o.replace([np.inf, -np.inf], np.nan)
def f38cb_f38_cycle_bottom_value_bookyld_cov_logmag_252d_jerk_v110_signal(equity, marketcap, cashneq, debt):
    byld = equity / marketcap.replace(0, np.nan); cov = _ncr(cashneq, debt).clip(upper=8.0); b = byld * cov; b = np.sign(b) * np.log1p(b.abs())
    b = b.replace([np.inf, -np.inf], np.nan)
    o = (b - 2.0 * b.shift(84) + b.shift(168)) / 7056.0
    return o.replace([np.inf, -np.inf], np.nan)
def f38cb_f38_cycle_bottom_value_excesscash_pb_emaratio_252d_jerk_v111_signal(cashneq, debt, pb):
    cushion = (cashneq - debt) / (cashneq.abs() + debt.abs() + 1.0); cheap = _cp(pb); b = np.tanh(cushion) * cheap; b = b / (b.ewm(span=126, min_periods=42).mean().abs() + 1e-9)
    b = b.replace([np.inf, -np.inf], np.nan)
    o = (b - 2.0 * b.shift(84) + b.shift(168)) / 7056.0
    return o.replace([np.inf, -np.inf], np.nan)
def f38cb_f38_cycle_bottom_value_survfloor_ev_lvl_252d_jerk_v112_signal(tangibles, cashneq, debt, evebitda):
    floor = (tangibles + cashneq) / debt.replace(0, np.nan); cheap = _ce(evebitda); b = np.tanh(floor / 5.0) * cheap
    b = b.replace([np.inf, -np.inf], np.nan)
    o = (b - 2.0 * b.shift(84) + b.shift(168)) / 7056.0
    return o.replace([np.inf, -np.inf], np.nan)
def f38cb_f38_cycle_bottom_value_tangint_ev_z252_252d_jerk_v113_signal(tangibles, equity, evebitda):
    ti = tangibles / equity.replace(0, np.nan); cheap = _ce(evebitda); b = np.tanh(ti) * cheap; b = _z(b, 252)
    b = b.replace([np.inf, -np.inf], np.nan)
    o = (b - 2.0 * b.shift(84) + b.shift(168)) / 7056.0
    return o.replace([np.inf, -np.inf], np.nan)
def f38cb_f38_cycle_bottom_value_mctanginv_gate_rank252_252d_jerk_v114_signal(marketcap, tangibles, cashneq, debt):
    pt = marketcap / tangibles.replace(0, np.nan); inv = 1.0 / pt.replace(0, np.nan); gate = _sg(cashneq, debt); b = inv * gate; b = _rank(b, 252)
    b = b.replace([np.inf, -np.inf], np.nan)
    o = (b - 2.0 * b.shift(84) + b.shift(168)) / 7056.0
    return o.replace([np.inf, -np.inf], np.nan)
def f38cb_f38_cycle_bottom_value_grahamnet_cov_ratio_252d_jerk_v115_signal(tangibles, debt, marketcap, cashneq):
    netnet = (tangibles - debt) / marketcap.replace(0, np.nan); cov = _ncr(cashneq, debt).clip(upper=8.0); b = np.tanh(netnet) * cov; b = b / (_mean(b, 252).abs() + 1e-9)
    b = b.replace([np.inf, -np.inf], np.nan)
    o = (b - 2.0 * b.shift(84) + b.shift(168)) / 7056.0
    return o.replace([np.inf, -np.inf], np.nan)
def f38cb_f38_cycle_bottom_value_threeway_emadisp_252d_jerk_v116_signal(tangibles, marketcap, cashneq, debt, evebitda):
    a = _z(_tb(tangibles, marketcap), 252); s = _z(_ncr(cashneq, debt), 252); rr = _z(evebitda, 252); b = (a + s - rr) / 3.0; b = b - b.ewm(span=63, min_periods=21).mean()
    b = b.replace([np.inf, -np.inf], np.nan)
    o = (b - 2.0 * b.shift(84) + b.shift(168)) / 7056.0
    return o.replace([np.inf, -np.inf], np.nan)
def f38cb_f38_cycle_bottom_value_liqfix_pb_sqrtmag_252d_jerk_v117_signal(cashneq, debt, marketcap, tangibles, pb):
    liq = _nc(cashneq, debt) / marketcap.replace(0, np.nan); fix = _tb(tangibles, marketcap); mix = _z(liq, 252) - _z(fix, 252); cheap = _rank(_cp(pb), 252) + 0.5; b = mix * cheap; b = np.sign(b) * (b.abs() ** 0.5)
    b = b.replace([np.inf, -np.inf], np.nan)
    o = (b - 2.0 * b.shift(84) + b.shift(168)) / 7056.0
    return o.replace([np.inf, -np.inf], np.nan)
def f38cb_f38_cycle_bottom_value_evtangtrough_tanh_504d_jerk_v118_signal(marketcap, debt, cashneq, tangibles):
    ev = _ev(marketcap, debt, cashneq); et = ev / tangibles.replace(0, np.nan); trough = (_mean(et, 504) - et) / _mean(et, 504).replace(0, np.nan); b = trough; b = np.tanh(b / (b.abs().rolling(126, min_periods=42).mean() + 1e-9))
    b = b.replace([np.inf, -np.inf], np.nan)
    o = (b - 2.0 * b.shift(84) + b.shift(168)) / 7056.0
    return o.replace([np.inf, -np.inf], np.nan)
def f38cb_f38_cycle_bottom_value_pbtrough_gate_shortlong_504d_jerk_v119_signal(pb, cashneq, debt):
    mid = _mean(pb, 504); trough = (mid - pb) / mid.replace(0, np.nan); gate = _sg(cashneq, debt); b = trough * gate; b = _mean(b, 21) - _mean(b, 126)
    b = b.replace([np.inf, -np.inf], np.nan)
    o = (b - 2.0 * b.shift(84) + b.shift(168)) / 7056.0
    return o.replace([np.inf, -np.inf], np.nan)
def f38cb_f38_cycle_bottom_value_evtrough_tang_z504_504d_jerk_v120_signal(evebitda, tangibles, marketcap):
    mid = _mean(evebitda, 504); trough = (mid - evebitda) / mid.replace(0, np.nan); back = _z(_tb(tangibles, marketcap), 252); b = trough + 0.3 * back; b = _z(b, 504)
    b = b.replace([np.inf, -np.inf], np.nan)
    o = (b - 2.0 * b.shift(84) + b.shift(168)) / 7056.0
    return o.replace([np.inf, -np.inf], np.nan)
def f38cb_f38_cycle_bottom_value_cashrich_pb_rank504_252d_jerk_v121_signal(cashneq, tangibles, pb):
    rich = cashneq / (tangibles + cashneq).replace(0, np.nan); cheap = _cp(pb); b = rich * cheap; b = _rank(b, 504)
    b = b.replace([np.inf, -np.inf], np.nan)
    o = (b - 2.0 * b.shift(84) + b.shift(168)) / 7056.0
    return o.replace([np.inf, -np.inf], np.nan)
def f38cb_f38_cycle_bottom_value_assetsurplus_ev_zscoremr_252d_jerk_v122_signal(tangibles, debt, evebitda):
    surplus = tangibles / debt.replace(0, np.nan) - 1.0; cheap = _ce(evebitda); b = np.tanh(surplus) * np.tanh(cheap); b = _z(b, 126) - _z(b, 252)
    b = b.replace([np.inf, -np.inf], np.nan)
    o = (b - 2.0 * b.shift(84) + b.shift(168)) / 7056.0
    return o.replace([np.inf, -np.inf], np.nan)
def f38cb_f38_cycle_bottom_value_evdeep_gate_logmag_1260d_jerk_v123_signal(evebitda, cashneq, debt):
    deepz = -_z(evebitda, 1260); gate = _sg(cashneq, debt); b = deepz * gate; b = np.sign(b) * np.log1p(b.abs())
    b = b.replace([np.inf, -np.inf], np.nan)
    o = (b - 2.0 * b.shift(189) + b.shift(378)) / 35721.0
    return o.replace([np.inf, -np.inf], np.nan)
def f38cb_f38_cycle_bottom_value_pbdeep_cov_emaratio_1260d_jerk_v124_signal(pb, cashneq, debt):
    deepz = _z(_cp(pb), 1260); cov = _ncr(cashneq, debt).clip(upper=8.0); b = deepz * cov; b = b / (b.ewm(span=126, min_periods=42).mean().abs() + 1e-9)
    b = b.replace([np.inf, -np.inf], np.nan)
    o = (b - 2.0 * b.shift(189) + b.shift(378)) / 35721.0
    return o.replace([np.inf, -np.inf], np.nan)
def f38cb_f38_cycle_bottom_value_netnetfloor_ev_lvl_504d_jerk_v125_signal(tangibles, cashneq, debt, marketcap, evebitda):
    floor = (tangibles + cashneq - debt) / marketcap.replace(0, np.nan); b = _z(floor, 504) - _z(evebitda, 504)
    b = b.replace([np.inf, -np.inf], np.nan)
    o = (b - 2.0 * b.shift(84) + b.shift(168)) / 7056.0
    return o.replace([np.inf, -np.inf], np.nan)
def f38cb_f38_cycle_bottom_value_tangcoverdebt_pb_z252_252d_jerk_v126_signal(tangibles, debt, pb):
    cover = tangibles / debt.replace(0, np.nan); gate = 1.0 / (1.0 + np.exp(-(cover - 1.0))); cheap = _cp(pb); b = cheap * gate; b = _z(b, 252)
    b = b.replace([np.inf, -np.inf], np.nan)
    o = (b - 2.0 * b.shift(84) + b.shift(168)) / 7056.0
    return o.replace([np.inf, -np.inf], np.nan)
def f38cb_f38_cycle_bottom_value_evev_ncyld_rank252_1260d_jerk_v127_signal(marketcap, debt, cashneq, evebitda):
    ev = _ev(marketcap, debt, cashneq); ncyld = _nc(cashneq, debt) / ev.replace(0, np.nan); cheap = _z(_ce(evebitda), 1260); b = _z(ncyld, 1260) + cheap; b = _rank(b, 252)
    b = b.replace([np.inf, -np.inf], np.nan)
    o = (b - 2.0 * b.shift(189) + b.shift(378)) / 35721.0
    return o.replace([np.inf, -np.inf], np.nan)
def f38cb_f38_cycle_bottom_value_tangshare_solv_ratio_252d_jerk_v128_signal(tangibles, equity, cashneq, debt):
    share = tangibles / equity.replace(0, np.nan); gate = _sg(cashneq, debt); b = np.tanh(share) * gate; b = b / (_mean(b, 252).abs() + 1e-9)
    b = b.replace([np.inf, -np.inf], np.nan)
    o = (b - 2.0 * b.shift(84) + b.shift(168)) / 7056.0
    return o.replace([np.inf, -np.inf], np.nan)
def f38cb_f38_cycle_bottom_value_pbcov_geo_emadisp_252d_jerk_v129_signal(pb, cashneq, debt):
    cheap = _cp(pb); cov = _ncr(cashneq, debt).clip(lower=0.0); b = np.sqrt(cheap.clip(lower=0) * cov); b = b - b.ewm(span=63, min_periods=21).mean()
    b = b.replace([np.inf, -np.inf], np.nan)
    o = (b - 2.0 * b.shift(84) + b.shift(168)) / 7056.0
    return o.replace([np.inf, -np.inf], np.nan)
def f38cb_f38_cycle_bottom_value_cheappb_netcash_sqrtmag_252d_jerk_v130_signal(pb, cashneq, debt):
    cheap = _cp(pb); gate = _sg(cashneq, debt); b = cheap * gate; b = np.sign(b) * (b.abs() ** 0.5)
    b = b.replace([np.inf, -np.inf], np.nan)
    o = (b - 2.0 * b.shift(52) + b.shift(104)) / 2704.0
    return o.replace([np.inf, -np.inf], np.nan)
def f38cb_f38_cycle_bottom_value_cheapev_cov_rank252_252d_jerk_v131_signal(evebitda, cashneq, debt):
    cheap = _ce(evebitda); cov = _ncr(cashneq, debt).clip(upper=10.0); b = cheap * cov; b = _rank(b, 252)
    b = b.replace([np.inf, -np.inf], np.nan)
    o = (b - 2.0 * b.shift(52) + b.shift(104)) / 2704.0
    return o.replace([np.inf, -np.inf], np.nan)
def f38cb_f38_cycle_bottom_value_pbz_tangback_shortlong_252d_jerk_v132_signal(pb, tangibles, marketcap):
    cheapz = _z(_cp(pb), 252); back = _tb(tangibles, marketcap); b = cheapz * back; b = _mean(b, 21) - _mean(b, 126)
    b = b.replace([np.inf, -np.inf], np.nan)
    o = (b - 2.0 * b.shift(52) + b.shift(104)) / 2704.0
    return o.replace([np.inf, -np.inf], np.nan)
def f38cb_f38_cycle_bottom_value_evnetcash_z504_252d_jerk_v133_signal(evebitda, cashneq, debt):
    cz = _z(_ce(evebitda), 252); sz = _z(_nc(cashneq, debt), 252); b = cz + sz; b = _z(b, 504)
    b = b.replace([np.inf, -np.inf], np.nan)
    o = (b - 2.0 * b.shift(52) + b.shift(104)) / 2704.0
    return o.replace([np.inf, -np.inf], np.nan)
def f38cb_f38_cycle_bottom_value_navdisc_gate_rank504_252d_jerk_v134_signal(tangibles, marketcap, cashneq, debt):
    disc = (tangibles - marketcap) / marketcap.replace(0, np.nan); gate = _sg(cashneq, debt); b = disc * gate; b = _rank(b, 504)
    b = b.replace([np.inf, -np.inf], np.nan)
    o = (b - 2.0 * b.shift(52) + b.shift(104)) / 2704.0
    return o.replace([np.inf, -np.inf], np.nan)
def f38cb_f38_cycle_bottom_value_blendcheap_cov_zscoremr_252d_jerk_v135_signal(pb, evebitda, cashneq, debt):
    blend = 0.5 * _rank(_cp(pb), 252) + 0.5 * _rank(_ce(evebitda), 252); cov = _ncr(cashneq, debt).clip(upper=8.0); b = blend * cov; b = _z(b, 126) - _z(b, 252)
    b = b.replace([np.inf, -np.inf], np.nan)
    o = (b - 2.0 * b.shift(52) + b.shift(104)) / 2704.0
    return o.replace([np.inf, -np.inf], np.nan)
def f38cb_f38_cycle_bottom_value_tangeq_cheap_logmag_252d_jerk_v136_signal(tangibles, equity, pb):
    tq = tangibles / equity.replace(0, np.nan); cheap = _cp(pb); b = tq * cheap; b = np.sign(b) * np.log1p(b.abs())
    b = b.replace([np.inf, -np.inf], np.nan)
    o = (b - 2.0 * b.shift(52) + b.shift(104)) / 2704.0
    return o.replace([np.inf, -np.inf], np.nan)
def f38cb_f38_cycle_bottom_value_netcashmc_ev_emaratio_252d_jerk_v137_signal(cashneq, debt, marketcap, evebitda):
    ncmc = _nc(cashneq, debt) / marketcap.replace(0, np.nan); cheap = _ce(evebitda); b = ncmc * cheap; b = b / (b.ewm(span=126, min_periods=42).mean().abs() + 1e-9)
    b = b.replace([np.inf, -np.inf], np.nan)
    o = (b - 2.0 * b.shift(52) + b.shift(104)) / 2704.0
    return o.replace([np.inf, -np.inf], np.nan)
def f38cb_f38_cycle_bottom_value_bookyld_solv_lvl_252d_jerk_v138_signal(equity, marketcap, cashneq, debt):
    byld = equity / marketcap.replace(0, np.nan); gate = _sg(cashneq, debt); b = byld * gate
    b = b.replace([np.inf, -np.inf], np.nan)
    o = (b - 2.0 * b.shift(52) + b.shift(104)) / 2704.0
    return o.replace([np.inf, -np.inf], np.nan)
def f38cb_f38_cycle_bottom_value_warchest_pb_z252_252d_jerk_v139_signal(cashneq, debt, equity, pb):
    wc = _nc(cashneq, debt) / equity.replace(0, np.nan); cheap = _cp(pb); b = wc * cheap; b = _z(b, 252)
    b = b.replace([np.inf, -np.inf], np.nan)
    o = (b - 2.0 * b.shift(52) + b.shift(104)) / 2704.0
    return o.replace([np.inf, -np.inf], np.nan)
def f38cb_f38_cycle_bottom_value_buffer_ev_rank252_252d_jerk_v140_signal(cashneq, debt, tangibles, evebitda):
    buf = _nc(cashneq, debt) / tangibles.replace(0, np.nan); cheap = _ce(evebitda); b = buf * cheap; b = _rank(b, 252)
    b = b.replace([np.inf, -np.inf], np.nan)
    o = (b - 2.0 * b.shift(52) + b.shift(104)) / 2704.0
    return o.replace([np.inf, -np.inf], np.nan)
def f38cb_f38_cycle_bottom_value_evtang_inv_ratio_252d_jerk_v141_signal(marketcap, debt, cashneq, tangibles):
    ev = _ev(marketcap, debt, cashneq); et = ev / tangibles.replace(0, np.nan); b = 1.0 / et.replace(0, np.nan); b = b / (_mean(b, 252).abs() + 1e-9)
    b = b.replace([np.inf, -np.inf], np.nan)
    o = (b - 2.0 * b.shift(52) + b.shift(104)) / 2704.0
    return o.replace([np.inf, -np.inf], np.nan)
def f38cb_f38_cycle_bottom_value_tangfloor_pb_emadisp_252d_jerk_v142_signal(tangibles, marketcap, pb):
    back = _tb(tangibles, marketcap); cheap = _cp(pb); b = back * cheap; b = b - b.ewm(span=63, min_periods=21).mean()
    b = b.replace([np.inf, -np.inf], np.nan)
    o = (b - 2.0 * b.shift(52) + b.shift(104)) / 2704.0
    return o.replace([np.inf, -np.inf], np.nan)
def f38cb_f38_cycle_bottom_value_netcashev_cheap_sqrtmag_252d_jerk_v143_signal(cashneq, debt, marketcap, evebitda):
    ev = _ev(marketcap, debt, cashneq); cover = _nc(cashneq, debt) / ev.replace(0, np.nan); cheap = _ce(evebitda); b = cover * cheap; b = np.sign(b) * (b.abs() ** 0.5)
    b = b.replace([np.inf, -np.inf], np.nan)
    o = (b - 2.0 * b.shift(52) + b.shift(104)) / 2704.0
    return o.replace([np.inf, -np.inf], np.nan)
def f38cb_f38_cycle_bottom_value_triple_tanh_252d_jerk_v144_signal(pb, evebitda, cashneq, debt):
    a = _z(_cp(pb), 252); c = _z(_ce(evebitda), 252); s = _z(_nc(cashneq, debt), 252); b = (a + c + s) / 3.0; b = np.tanh(b / (b.abs().rolling(126, min_periods=42).mean() + 1e-9))
    b = b.replace([np.inf, -np.inf], np.nan)
    o = (b - 2.0 * b.shift(52) + b.shift(104)) / 2704.0
    return o.replace([np.inf, -np.inf], np.nan)
def f38cb_f38_cycle_bottom_value_tangdebt_ev_shortlong_252d_jerk_v145_signal(tangibles, debt, evebitda):
    tcov = (tangibles / debt.replace(0, np.nan)).clip(upper=20.0); cheap = _ce(evebitda); b = tcov * cheap; b = _mean(b, 21) - _mean(b, 126)
    b = b.replace([np.inf, -np.inf], np.nan)
    o = (b - 2.0 * b.shift(52) + b.shift(104)) / 2704.0
    return o.replace([np.inf, -np.inf], np.nan)
def f38cb_f38_cycle_bottom_value_eqdebt_pb_z504_252d_jerk_v146_signal(equity, debt, pb):
    eqd = equity / debt.replace(0, np.nan); gate = 1.0 / (1.0 + np.exp(-(eqd - 1.0))); cheap = _cp(pb); b = cheap * gate; b = _z(b, 504)
    b = b.replace([np.inf, -np.inf], np.nan)
    o = (b - 2.0 * b.shift(52) + b.shift(104)) / 2704.0
    return o.replace([np.inf, -np.inf], np.nan)
def f38cb_f38_cycle_bottom_value_netdebteq_pb_rank504_252d_jerk_v147_signal(debt, cashneq, equity, pb):
    nde = (debt - cashneq) / equity.replace(0, np.nan); low = 1.0 / (1.0 + np.exp(nde)); cheap = _cp(pb); b = low * cheap; b = _rank(b, 504)
    b = b.replace([np.inf, -np.inf], np.nan)
    o = (b - 2.0 * b.shift(52) + b.shift(104)) / 2704.0
    return o.replace([np.inf, -np.inf], np.nan)
def f38cb_f38_cycle_bottom_value_cashmc_ev_zscoremr_252d_jerk_v148_signal(cashneq, marketcap, evebitda):
    cashmc = cashneq / marketcap.replace(0, np.nan); cheap = _ce(evebitda); b = cashmc * cheap; b = _z(b, 126) - _z(b, 252)
    b = b.replace([np.inf, -np.inf], np.nan)
    o = (b - 2.0 * b.shift(52) + b.shift(104)) / 2704.0
    return o.replace([np.inf, -np.inf], np.nan)
def f38cb_f38_cycle_bottom_value_ncmctang_logmag_252d_jerk_v149_signal(cashneq, debt, tangibles, pb):
    liq = _nc(cashneq, debt) / tangibles.replace(0, np.nan); cheap = _cp(pb); b = np.tanh(liq) * cheap; b = np.sign(b) * np.log1p(b.abs())
    b = b.replace([np.inf, -np.inf], np.nan)
    o = (b - 2.0 * b.shift(52) + b.shift(104)) / 2704.0
    return o.replace([np.inf, -np.inf], np.nan)
def f38cb_f38_cycle_bottom_value_eveq_cov_emaratio_252d_jerk_v150_signal(marketcap, debt, cashneq, equity):
    ev = _ev(marketcap, debt, cashneq); inv = equity / ev.replace(0, np.nan); cov = _ncr(cashneq, debt).clip(upper=8.0); b = inv * cov; b = b / (b.ewm(span=126, min_periods=42).mean().abs() + 1e-9)
    b = b.replace([np.inf, -np.inf], np.nan)
    o = (b - 2.0 * b.shift(52) + b.shift(104)) / 2704.0
    return o.replace([np.inf, -np.inf], np.nan)
_FEATURES = [
    f38cb_f38_cycle_bottom_value_cheappb_netcash_tanh_252d_jerk_v001_signal,
    f38cb_f38_cycle_bottom_value_cheapev_cov_shortlong_252d_jerk_v002_signal,
    f38cb_f38_cycle_bottom_value_pbz_tangback_z504_252d_jerk_v003_signal,
    f38cb_f38_cycle_bottom_value_evnetcash_rank504_252d_jerk_v004_signal,
    f38cb_f38_cycle_bottom_value_navdisc_gate_zscoremr_252d_jerk_v005_signal,
    f38cb_f38_cycle_bottom_value_blendcheap_cov_logmag_252d_jerk_v006_signal,
    f38cb_f38_cycle_bottom_value_tangeq_cheap_emaratio_252d_jerk_v007_signal,
    f38cb_f38_cycle_bottom_value_netcashmc_ev_lvl_252d_jerk_v008_signal,
    f38cb_f38_cycle_bottom_value_bookyld_solv_z252_252d_jerk_v009_signal,
    f38cb_f38_cycle_bottom_value_warchest_pb_rank252_252d_jerk_v010_signal,
    f38cb_f38_cycle_bottom_value_buffer_ev_ratio_252d_jerk_v011_signal,
    f38cb_f38_cycle_bottom_value_evtang_inv_emadisp_252d_jerk_v012_signal,
    f38cb_f38_cycle_bottom_value_tangfloor_pb_sqrtmag_252d_jerk_v013_signal,
    f38cb_f38_cycle_bottom_value_netcashev_cheap_tanh_252d_jerk_v014_signal,
    f38cb_f38_cycle_bottom_value_triple_shortlong_252d_jerk_v015_signal,
    f38cb_f38_cycle_bottom_value_tangdebt_ev_z504_252d_jerk_v016_signal,
    f38cb_f38_cycle_bottom_value_eqdebt_pb_rank504_252d_jerk_v017_signal,
    f38cb_f38_cycle_bottom_value_netdebteq_pb_zscoremr_252d_jerk_v018_signal,
    f38cb_f38_cycle_bottom_value_cashmc_ev_logmag_252d_jerk_v019_signal,
    f38cb_f38_cycle_bottom_value_ncmctang_emaratio_252d_jerk_v020_signal,
    f38cb_f38_cycle_bottom_value_eveq_cov_lvl_252d_jerk_v021_signal,
    f38cb_f38_cycle_bottom_value_tangcov_evz_z252_252d_jerk_v022_signal,
    f38cb_f38_cycle_bottom_value_netnet_mc_rank252_252d_jerk_v023_signal,
    f38cb_f38_cycle_bottom_value_bookyld_cov_ratio_252d_jerk_v024_signal,
    f38cb_f38_cycle_bottom_value_excesscash_pb_emadisp_252d_jerk_v025_signal,
    f38cb_f38_cycle_bottom_value_survfloor_ev_sqrtmag_252d_jerk_v026_signal,
    f38cb_f38_cycle_bottom_value_tangint_ev_tanh_252d_jerk_v027_signal,
    f38cb_f38_cycle_bottom_value_mctanginv_gate_shortlong_252d_jerk_v028_signal,
    f38cb_f38_cycle_bottom_value_grahamnet_cov_z504_252d_jerk_v029_signal,
    f38cb_f38_cycle_bottom_value_threeway_rank504_252d_jerk_v030_signal,
    f38cb_f38_cycle_bottom_value_liqfix_pb_zscoremr_252d_jerk_v031_signal,
    f38cb_f38_cycle_bottom_value_evtangtrough_logmag_504d_jerk_v032_signal,
    f38cb_f38_cycle_bottom_value_pbtrough_gate_emaratio_504d_jerk_v033_signal,
    f38cb_f38_cycle_bottom_value_evtrough_tang_lvl_504d_jerk_v034_signal,
    f38cb_f38_cycle_bottom_value_cashrich_pb_z252_252d_jerk_v035_signal,
    f38cb_f38_cycle_bottom_value_assetsurplus_ev_rank252_252d_jerk_v036_signal,
    f38cb_f38_cycle_bottom_value_evdeep_gate_ratio_1260d_jerk_v037_signal,
    f38cb_f38_cycle_bottom_value_pbdeep_cov_emadisp_1260d_jerk_v038_signal,
    f38cb_f38_cycle_bottom_value_netnetfloor_ev_sqrtmag_504d_jerk_v039_signal,
    f38cb_f38_cycle_bottom_value_tangcoverdebt_pb_tanh_252d_jerk_v040_signal,
    f38cb_f38_cycle_bottom_value_evev_ncyld_shortlong_1260d_jerk_v041_signal,
    f38cb_f38_cycle_bottom_value_tangshare_solv_z504_252d_jerk_v042_signal,
    f38cb_f38_cycle_bottom_value_pbcov_geo_rank504_252d_jerk_v043_signal,
    f38cb_f38_cycle_bottom_value_cheappb_netcash_zscoremr_252d_jerk_v044_signal,
    f38cb_f38_cycle_bottom_value_cheapev_cov_z252_252d_jerk_v045_signal,
    f38cb_f38_cycle_bottom_value_pbz_tangback_emaratio_252d_jerk_v046_signal,
    f38cb_f38_cycle_bottom_value_evnetcash_lvl_252d_jerk_v047_signal,
    f38cb_f38_cycle_bottom_value_navdisc_gate_z252_252d_jerk_v048_signal,
    f38cb_f38_cycle_bottom_value_blendcheap_cov_rank252_252d_jerk_v049_signal,
    f38cb_f38_cycle_bottom_value_tangeq_cheap_ratio_252d_jerk_v050_signal,
    f38cb_f38_cycle_bottom_value_netcashmc_ev_emadisp_252d_jerk_v051_signal,
    f38cb_f38_cycle_bottom_value_bookyld_solv_sqrtmag_252d_jerk_v052_signal,
    f38cb_f38_cycle_bottom_value_warchest_pb_tanh_252d_jerk_v053_signal,
    f38cb_f38_cycle_bottom_value_buffer_ev_shortlong_252d_jerk_v054_signal,
    f38cb_f38_cycle_bottom_value_evtang_inv_z504_252d_jerk_v055_signal,
    f38cb_f38_cycle_bottom_value_tangfloor_pb_rank504_252d_jerk_v056_signal,
    f38cb_f38_cycle_bottom_value_netcashev_cheap_zscoremr_252d_jerk_v057_signal,
    f38cb_f38_cycle_bottom_value_triple_logmag_252d_jerk_v058_signal,
    f38cb_f38_cycle_bottom_value_tangdebt_ev_emaratio_252d_jerk_v059_signal,
    f38cb_f38_cycle_bottom_value_eqdebt_pb_lvl_252d_jerk_v060_signal,
    f38cb_f38_cycle_bottom_value_netdebteq_pb_z252_252d_jerk_v061_signal,
    f38cb_f38_cycle_bottom_value_cashmc_ev_rank252_252d_jerk_v062_signal,
    f38cb_f38_cycle_bottom_value_ncmctang_ratio_252d_jerk_v063_signal,
    f38cb_f38_cycle_bottom_value_eveq_cov_emadisp_252d_jerk_v064_signal,
    f38cb_f38_cycle_bottom_value_tangcov_evz_sqrtmag_252d_jerk_v065_signal,
    f38cb_f38_cycle_bottom_value_netnet_mc_tanh_252d_jerk_v066_signal,
    f38cb_f38_cycle_bottom_value_bookyld_cov_shortlong_252d_jerk_v067_signal,
    f38cb_f38_cycle_bottom_value_excesscash_pb_z504_252d_jerk_v068_signal,
    f38cb_f38_cycle_bottom_value_survfloor_ev_rank504_252d_jerk_v069_signal,
    f38cb_f38_cycle_bottom_value_tangint_ev_zscoremr_252d_jerk_v070_signal,
    f38cb_f38_cycle_bottom_value_mctanginv_gate_logmag_252d_jerk_v071_signal,
    f38cb_f38_cycle_bottom_value_grahamnet_cov_emaratio_252d_jerk_v072_signal,
    f38cb_f38_cycle_bottom_value_threeway_lvl_252d_jerk_v073_signal,
    f38cb_f38_cycle_bottom_value_liqfix_pb_z252_252d_jerk_v074_signal,
    f38cb_f38_cycle_bottom_value_evtangtrough_rank252_504d_jerk_v075_signal,
    f38cb_f38_cycle_bottom_value_pbtrough_gate_ratio_504d_jerk_v076_signal,
    f38cb_f38_cycle_bottom_value_evtrough_tang_emadisp_504d_jerk_v077_signal,
    f38cb_f38_cycle_bottom_value_cashrich_pb_sqrtmag_252d_jerk_v078_signal,
    f38cb_f38_cycle_bottom_value_assetsurplus_ev_tanh_252d_jerk_v079_signal,
    f38cb_f38_cycle_bottom_value_evdeep_gate_shortlong_1260d_jerk_v080_signal,
    f38cb_f38_cycle_bottom_value_pbdeep_cov_z504_1260d_jerk_v081_signal,
    f38cb_f38_cycle_bottom_value_netnetfloor_ev_rank504_504d_jerk_v082_signal,
    f38cb_f38_cycle_bottom_value_tangcoverdebt_pb_zscoremr_252d_jerk_v083_signal,
    f38cb_f38_cycle_bottom_value_evev_ncyld_logmag_1260d_jerk_v084_signal,
    f38cb_f38_cycle_bottom_value_tangshare_solv_emaratio_252d_jerk_v085_signal,
    f38cb_f38_cycle_bottom_value_pbcov_geo_lvl_252d_jerk_v086_signal,
    f38cb_f38_cycle_bottom_value_cheappb_netcash_z252_252d_jerk_v087_signal,
    f38cb_f38_cycle_bottom_value_cheapev_cov_z504_252d_jerk_v088_signal,
    f38cb_f38_cycle_bottom_value_pbz_tangback_ratio_252d_jerk_v089_signal,
    f38cb_f38_cycle_bottom_value_evnetcash_emadisp_252d_jerk_v090_signal,
    f38cb_f38_cycle_bottom_value_navdisc_gate_sqrtmag_252d_jerk_v091_signal,
    f38cb_f38_cycle_bottom_value_blendcheap_cov_tanh_252d_jerk_v092_signal,
    f38cb_f38_cycle_bottom_value_tangeq_cheap_shortlong_252d_jerk_v093_signal,
    f38cb_f38_cycle_bottom_value_netcashmc_ev_z504_252d_jerk_v094_signal,
    f38cb_f38_cycle_bottom_value_bookyld_solv_rank504_252d_jerk_v095_signal,
    f38cb_f38_cycle_bottom_value_warchest_pb_zscoremr_252d_jerk_v096_signal,
    f38cb_f38_cycle_bottom_value_buffer_ev_logmag_252d_jerk_v097_signal,
    f38cb_f38_cycle_bottom_value_evtang_inv_emaratio_252d_jerk_v098_signal,
    f38cb_f38_cycle_bottom_value_tangfloor_pb_lvl_252d_jerk_v099_signal,
    f38cb_f38_cycle_bottom_value_netcashev_cheap_z252_252d_jerk_v100_signal,
    f38cb_f38_cycle_bottom_value_triple_rank252_252d_jerk_v101_signal,
    f38cb_f38_cycle_bottom_value_tangdebt_ev_ratio_252d_jerk_v102_signal,
    f38cb_f38_cycle_bottom_value_eqdebt_pb_emadisp_252d_jerk_v103_signal,
    f38cb_f38_cycle_bottom_value_netdebteq_pb_sqrtmag_252d_jerk_v104_signal,
    f38cb_f38_cycle_bottom_value_cashmc_ev_tanh_252d_jerk_v105_signal,
    f38cb_f38_cycle_bottom_value_ncmctang_shortlong_252d_jerk_v106_signal,
    f38cb_f38_cycle_bottom_value_eveq_cov_z504_252d_jerk_v107_signal,
    f38cb_f38_cycle_bottom_value_tangcov_evz_rank504_252d_jerk_v108_signal,
    f38cb_f38_cycle_bottom_value_netnet_mc_zscoremr_252d_jerk_v109_signal,
    f38cb_f38_cycle_bottom_value_bookyld_cov_logmag_252d_jerk_v110_signal,
    f38cb_f38_cycle_bottom_value_excesscash_pb_emaratio_252d_jerk_v111_signal,
    f38cb_f38_cycle_bottom_value_survfloor_ev_lvl_252d_jerk_v112_signal,
    f38cb_f38_cycle_bottom_value_tangint_ev_z252_252d_jerk_v113_signal,
    f38cb_f38_cycle_bottom_value_mctanginv_gate_rank252_252d_jerk_v114_signal,
    f38cb_f38_cycle_bottom_value_grahamnet_cov_ratio_252d_jerk_v115_signal,
    f38cb_f38_cycle_bottom_value_threeway_emadisp_252d_jerk_v116_signal,
    f38cb_f38_cycle_bottom_value_liqfix_pb_sqrtmag_252d_jerk_v117_signal,
    f38cb_f38_cycle_bottom_value_evtangtrough_tanh_504d_jerk_v118_signal,
    f38cb_f38_cycle_bottom_value_pbtrough_gate_shortlong_504d_jerk_v119_signal,
    f38cb_f38_cycle_bottom_value_evtrough_tang_z504_504d_jerk_v120_signal,
    f38cb_f38_cycle_bottom_value_cashrich_pb_rank504_252d_jerk_v121_signal,
    f38cb_f38_cycle_bottom_value_assetsurplus_ev_zscoremr_252d_jerk_v122_signal,
    f38cb_f38_cycle_bottom_value_evdeep_gate_logmag_1260d_jerk_v123_signal,
    f38cb_f38_cycle_bottom_value_pbdeep_cov_emaratio_1260d_jerk_v124_signal,
    f38cb_f38_cycle_bottom_value_netnetfloor_ev_lvl_504d_jerk_v125_signal,
    f38cb_f38_cycle_bottom_value_tangcoverdebt_pb_z252_252d_jerk_v126_signal,
    f38cb_f38_cycle_bottom_value_evev_ncyld_rank252_1260d_jerk_v127_signal,
    f38cb_f38_cycle_bottom_value_tangshare_solv_ratio_252d_jerk_v128_signal,
    f38cb_f38_cycle_bottom_value_pbcov_geo_emadisp_252d_jerk_v129_signal,
    f38cb_f38_cycle_bottom_value_cheappb_netcash_sqrtmag_252d_jerk_v130_signal,
    f38cb_f38_cycle_bottom_value_cheapev_cov_rank252_252d_jerk_v131_signal,
    f38cb_f38_cycle_bottom_value_pbz_tangback_shortlong_252d_jerk_v132_signal,
    f38cb_f38_cycle_bottom_value_evnetcash_z504_252d_jerk_v133_signal,
    f38cb_f38_cycle_bottom_value_navdisc_gate_rank504_252d_jerk_v134_signal,
    f38cb_f38_cycle_bottom_value_blendcheap_cov_zscoremr_252d_jerk_v135_signal,
    f38cb_f38_cycle_bottom_value_tangeq_cheap_logmag_252d_jerk_v136_signal,
    f38cb_f38_cycle_bottom_value_netcashmc_ev_emaratio_252d_jerk_v137_signal,
    f38cb_f38_cycle_bottom_value_bookyld_solv_lvl_252d_jerk_v138_signal,
    f38cb_f38_cycle_bottom_value_warchest_pb_z252_252d_jerk_v139_signal,
    f38cb_f38_cycle_bottom_value_buffer_ev_rank252_252d_jerk_v140_signal,
    f38cb_f38_cycle_bottom_value_evtang_inv_ratio_252d_jerk_v141_signal,
    f38cb_f38_cycle_bottom_value_tangfloor_pb_emadisp_252d_jerk_v142_signal,
    f38cb_f38_cycle_bottom_value_netcashev_cheap_sqrtmag_252d_jerk_v143_signal,
    f38cb_f38_cycle_bottom_value_triple_tanh_252d_jerk_v144_signal,
    f38cb_f38_cycle_bottom_value_tangdebt_ev_shortlong_252d_jerk_v145_signal,
    f38cb_f38_cycle_bottom_value_eqdebt_pb_z504_252d_jerk_v146_signal,
    f38cb_f38_cycle_bottom_value_netdebteq_pb_rank504_252d_jerk_v147_signal,
    f38cb_f38_cycle_bottom_value_cashmc_ev_zscoremr_252d_jerk_v148_signal,
    f38cb_f38_cycle_bottom_value_ncmctang_logmag_252d_jerk_v149_signal,
    f38cb_f38_cycle_bottom_value_eveq_cov_emaratio_252d_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F38_CYCLE_BOTTOM_VALUE_REGISTRY_001_150 = REGISTRY


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

    pb = _fund(1, base=1.5, drift=-0.01, vol=0.12).clip(lower=0.05).rename("pb")
    evebitda = _fund(2, base=6.0, drift=-0.01, vol=0.12).clip(lower=0.3).rename("evebitda")
    marketcap = _fund(3, base=5e8, drift=0.0, vol=0.10).rename("marketcap")
    equity = _fund(4, base=4e8, drift=0.0, vol=0.09).rename("equity")
    tangibles = _fund(5, base=3.5e8, drift=0.0, vol=0.08).rename("tangibles")
    debt = _fund(6, base=2e8, drift=0.0, vol=0.10).rename("debt")
    cashneq = _fund(7, base=2.2e8, drift=0.0, vol=0.11).rename("cashneq")

    cols = {"pb": pb, "evebitda": evebitda, "marketcap": marketcap,
            "equity": equity, "tangibles": tangibles, "debt": debt, "cashneq": cashneq}
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

    print("OK f38_cycle_bottom_value_3rd_derivatives_001_150_claude: %d features pass" % n_features)
