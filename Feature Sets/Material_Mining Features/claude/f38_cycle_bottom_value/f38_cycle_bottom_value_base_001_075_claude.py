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
    # cheapness from price/book: small pb -> deep value. inverse so high = cheap.
    return 1.0 / pb.replace(0, np.nan)


def _f38_cheap_ev(evebitda):
    # cheapness from EV/EBITDA: small -> cheap. inverse so high = cheap.
    return 1.0 / evebitda.replace(0, np.nan)


def _f38_net_cash(cashneq, debt):
    # balance-sheet survival: cash minus debt (positive = net cash, survivable).
    return cashneq - debt


def _f38_net_cash_ratio(cashneq, debt):
    # cash-to-debt coverage (>1 = cash > debt, the survival gate).
    return cashneq / debt.replace(0, np.nan)


def _f38_tang_backing(tangibles, marketcap):
    # tangible asset backing per unit of market value (asset floor).
    return tangibles / marketcap.replace(0, np.nan)


def _f38_solv_gate(cashneq, debt):
    # soft survival gate in [0,1]: smoothly rewards cash>debt.
    nd = (debt - cashneq)
    return 1.0 / (1.0 + np.exp(nd / (cashneq.abs() + 1.0)))


# ============================================================
# deep P/B cheapness gated by net-cash solvency (level composite)
def f38cb_f38_cycle_bottom_value_cheappb_netcash_252d_base_v001_signal(pb, cashneq, debt):
    cheap = _f38_cheap_pb(pb)
    gate = _f38_solv_gate(cashneq, debt)
    b = cheap * gate
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/EBITDA cheapness vs its 63d EMA, gated by cash/debt coverage (de-trended)
def f38cb_f38_cycle_bottom_value_cheapev_cashcov_252d_base_v002_signal(evebitda, cashneq, debt):
    cheap = _f38_cheap_ev(evebitda)
    cheap_d = cheap - cheap.ewm(span=63, min_periods=21).mean()
    cov = _f38_net_cash_ratio(cashneq, debt).clip(upper=10.0)
    b = cheap_d * cov
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cheap P/B z-scored, weighted by tangible backing vs market cap
def f38cb_f38_cycle_bottom_value_pbz_tangback_252d_base_v003_signal(pb, tangibles, marketcap):
    cheapz = _z(_f38_cheap_pb(pb), 252)
    back = _f38_tang_backing(tangibles, marketcap)
    b = cheapz * back
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# bombed-out-but-solvent: low EV/EBITDA AND net cash positive (product of standardized facets)
def f38cb_f38_cycle_bottom_value_evnetcash_252d_base_v004_signal(evebitda, cashneq, debt):
    cheapz = _z(_f38_cheap_ev(evebitda), 252)
    solvz = _z(_f38_net_cash(cashneq, debt), 252)
    b = cheapz + solvz
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# discount-to-tangible-book gated by solvency: (tangibles-marketcap)/marketcap * gate
def f38cb_f38_cycle_bottom_value_navdisc_gate_base_v005_signal(tangibles, marketcap, cashneq, debt):
    disc = (tangibles - marketcap) / marketcap.replace(0, np.nan)
    gate = _f38_solv_gate(cashneq, debt)
    b = disc * gate
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cheapness composite rank: blend of inverse-pb and inverse-evebitda, gated by cash/debt
def f38cb_f38_cycle_bottom_value_blendcheap_cov_252d_base_v006_signal(pb, evebitda, cashneq, debt):
    blend = 0.5 * _rank(_f38_cheap_pb(pb), 252) + 0.5 * _rank(_f38_cheap_ev(evebitda), 252)
    cov = _f38_net_cash_ratio(cashneq, debt).clip(upper=8.0)
    b = blend * cov
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tangible backing per book equity, scaled by cheap P/B (asset-rich AND cheap)
def f38cb_f38_cycle_bottom_value_tangeq_cheap_base_v007_signal(tangibles, equity, pb):
    tq = tangibles / equity.replace(0, np.nan)
    cheap = _f38_cheap_pb(pb)
    b = tq * cheap
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-cash as fraction of market cap (z), interacting with EV/EBITDA cheapness sign
def f38cb_f38_cycle_bottom_value_netcashmc_ev_base_v008_signal(cashneq, debt, marketcap, evebitda):
    ncmc = _z(_f38_net_cash(cashneq, debt) / marketcap.replace(0, np.nan), 252)
    cheap = _f38_cheap_ev(evebitda)
    cheap_d = cheap - _mean(cheap, 252)
    b = ncmc * np.sign(cheap_d) * (cheap_d.abs() ** 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# equity book yield momentum (rising book yield) gated by net-cash solvency
def f38cb_f38_cycle_bottom_value_bookyld_solv_base_v009_signal(equity, marketcap, cashneq, debt):
    byld = equity / marketcap.replace(0, np.nan)
    bmom = byld - byld.shift(63)
    gate = _f38_solv_gate(cashneq, debt)
    b = bmom * gate
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cheap P/B momentum (getting cheaper) confirmed by improving cash coverage
def f38cb_f38_cycle_bottom_value_pbmom_covmom_252d_base_v010_signal(pb, cashneq, debt):
    cheap = _f38_cheap_pb(pb)
    cheapmom = cheap - cheap.shift(63)
    cov = _f38_net_cash_ratio(cashneq, debt)
    covmom = cov - cov.shift(63)
    b = np.sign(cheapmom) * np.sign(covmom) * (cheapmom.abs() * (1.0 + covmom.abs().clip(upper=5.0)))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# deep value flag intensity: how far below mid-cycle P/B, gated by cash>debt
def f38cb_f38_cycle_bottom_value_pbtrough_gate_504d_base_v011_signal(pb, cashneq, debt):
    midcycle = _mean(pb, 504)
    trough = (midcycle - pb) / midcycle.replace(0, np.nan)
    gate = _f38_solv_gate(cashneq, debt)
    b = trough * gate
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/EBITDA trough distance vs 504d mean, plus tangible-backing z (additive cheap+asset)
def f38cb_f38_cycle_bottom_value_evtrough_tang_504d_base_v012_signal(evebitda, tangibles, marketcap):
    midcycle = _mean(evebitda, 504)
    trough = (midcycle - evebitda) / midcycle.replace(0, np.nan)
    back = _z(_f38_tang_backing(tangibles, marketcap), 252)
    b = trough + 0.3 * back
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash/debt coverage z-scored, multiplied by cheap P/B level
def f38cb_f38_cycle_bottom_value_covz_pb_252d_base_v013_signal(cashneq, debt, pb):
    covz = _z(_f38_net_cash_ratio(cashneq, debt), 252)
    cheap = _f38_cheap_pb(pb)
    b = covz * cheap
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tangible-asset floor relative to debt (asset coverage of debt) x EV cheapness
def f38cb_f38_cycle_bottom_value_tangdebt_ev_base_v014_signal(tangibles, debt, evebitda):
    tcov = tangibles / debt.replace(0, np.nan)
    cheap = _f38_cheap_ev(evebitda)
    b = tcov.clip(upper=20.0) * cheap
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# bombed-and-solvent score: rank(cheap pb) + rank(net cash ratio) summed
def f38cb_f38_cycle_bottom_value_pbrank_covrank_252d_base_v015_signal(pb, cashneq, debt):
    pr = _rank(_f38_cheap_pb(pb), 252)
    cr = _rank(_f38_net_cash_ratio(cashneq, debt), 252)
    b = pr + cr
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# value gap: tangible backing rank times EV/EBITDA cheapness momentum (asset-rich getting cheaper)
def f38cb_f38_cycle_bottom_value_tangminus_ev_base_v016_signal(tangibles, marketcap, evebitda):
    back = _rank(_f38_tang_backing(tangibles, marketcap), 252) + 0.5
    cheap = _f38_cheap_ev(evebitda)
    cheapmom = cheap - cheap.shift(63)
    b = back * cheapmom
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net cash per equity (war chest) z-spread vs deep P/B cheapness z (rank-additive)
def f38cb_f38_cycle_bottom_value_warchest_pb_base_v017_signal(cashneq, debt, equity, pb):
    warchest = _f38_net_cash(cashneq, debt) / equity.replace(0, np.nan)
    cheap = _f38_cheap_pb(pb)
    b = _rank(warchest, 126) * (_rank(cheap, 126) + 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# survival-buffer change x cheapness: Δ(cash-debt)/tangibles times inverse EV/EBITDA
def f38cb_f38_cycle_bottom_value_buffer_ev_base_v018_signal(cashneq, debt, tangibles, evebitda):
    buffer = _f38_net_cash(cashneq, debt) / tangibles.replace(0, np.nan)
    bufchg = buffer - buffer.shift(63)
    cheap = _f38_cheap_ev(evebitda)
    b = bufchg * cheap
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cheap-multiple percentile within cycle (1260d) plus net-cash-ratio percentile (additive rank)
def f38cb_f38_cycle_bottom_value_pbcyclrank_gate_1260d_base_v019_signal(pb, cashneq, debt):
    cheaprank = _rank(_f38_cheap_pb(pb), 1260)
    covrank = _rank(_f38_net_cash_ratio(cashneq, debt), 1260)
    b = cheaprank + covrank
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/EBITDA cyclical percentile gated by tangible backing > 0.5 of marketcap
def f38cb_f38_cycle_bottom_value_evcyclrank_back_1260d_base_v020_signal(evebitda, tangibles, marketcap):
    cheaprank = _rank(_f38_cheap_ev(evebitda), 1260)
    back = _f38_tang_backing(tangibles, marketcap)
    gate = 1.0 / (1.0 + np.exp(-(back - 0.5) * 4.0))
    b = cheaprank * gate
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# enterprise-value-on-tangibles inverted, z-scored vs its own 252d history (cheap-on-assets extremity)
def f38cb_f38_cycle_bottom_value_evtang_inv_base_v021_signal(marketcap, debt, cashneq, tangibles):
    ev = marketcap + debt - cashneq
    ev_to_tang = ev / tangibles.replace(0, np.nan)
    inv = 1.0 / ev_to_tang.replace(0, np.nan)
    b = _z(inv, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# P/B and net-cash both improving: combined deep-value-arming signal
def f38cb_f38_cycle_bottom_value_pbnetcash_arm_252d_base_v022_signal(pb, cashneq, debt, equity):
    cheap = _z(_f38_cheap_pb(pb), 252)
    ncq = _z(_f38_net_cash(cashneq, debt) / equity.replace(0, np.nan), 252)
    b = (cheap + ncq) / 2.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tangible backing minus P/B richness (asset-floor cheapness)
def f38cb_f38_cycle_bottom_value_tangfloor_pb_base_v023_signal(tangibles, marketcap, pb):
    back = _f38_tang_backing(tangibles, marketcap)
    cheap = _f38_cheap_pb(pb)
    b = back * cheap
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-cash coverage of EV (z) times sign of EV/EBITDA cheapness deviation
def f38cb_f38_cycle_bottom_value_netcashev_cheap_base_v024_signal(cashneq, debt, marketcap, evebitda):
    ev = marketcap + debt - cashneq
    cover = _z(_f38_net_cash(cashneq, debt) / ev.replace(0, np.nan), 504)
    cheap = _f38_cheap_ev(evebitda)
    cheap_d = cheap - _mean(cheap, 504)
    b = cover * np.tanh(5.0 * cheap_d)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# value+solvency Z composite (equal-weight three pillars): cheap pb, cheap ev, net cash
def f38cb_f38_cycle_bottom_value_triple_252d_base_v025_signal(pb, evebitda, cashneq, debt):
    a = _z(_f38_cheap_pb(pb), 252)
    c = _z(_f38_cheap_ev(evebitda), 252)
    s = _z(_f38_net_cash(cashneq, debt), 252)
    b = (a + c + s) / 3.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# deep discount: how far P/B below its 1260d min-band (demeaned), gated by cash-coverage rank
def f38cb_f38_cycle_bottom_value_pbminband_cov_1260d_base_v026_signal(pb, cashneq, debt):
    lo = _rmin(pb, 1260)
    nearfloor = lo / pb.replace(0, np.nan)
    nearfloor_d = nearfloor - _mean(nearfloor, 252)
    cov = _rank(_f38_net_cash_ratio(cashneq, debt), 252) + 0.5
    b = nearfloor_d * cov
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tangible backing dispersion-adjusted, scaled by inverse EV/EBITDA (stable-asset cheapness)
def f38cb_f38_cycle_bottom_value_tangstab_ev_252d_base_v027_signal(tangibles, marketcap, evebitda):
    back = _f38_tang_backing(tangibles, marketcap)
    stab = back / (1.0 + _std(back, 252))
    cheap = _f38_cheap_ev(evebitda)
    b = stab * cheap
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# survival-weighted cheapness: cheap P/B times sigmoid of tangibles-cover-debt
def f38cb_f38_cycle_bottom_value_pb_tangcoverdebt_base_v028_signal(pb, tangibles, debt):
    cheap = _f38_cheap_pb(pb)
    cover = tangibles / debt.replace(0, np.nan)
    gate = 1.0 / (1.0 + np.exp(-(cover - 1.0)))
    b = cheap * gate
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net cash to marketcap rank minus EV-richness rank (solvency-cheapness rank spread)
def f38cb_f38_cycle_bottom_value_ncmcz_evz_252d_base_v029_signal(cashneq, debt, marketcap, evebitda):
    ncmc = _rank(_f38_net_cash(cashneq, debt) / marketcap.replace(0, np.nan), 504)
    cheap = _rank(_f38_cheap_ev(evebitda), 504)
    b = ncmc + cheap
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# equity-to-debt solvency gate times deep P/B cheapness
def f38cb_f38_cycle_bottom_value_eqdebt_pb_base_v030_signal(equity, debt, pb):
    eqd = equity / debt.replace(0, np.nan)
    gate = 1.0 / (1.0 + np.exp(-(eqd - 1.0)))
    cheap = _f38_cheap_pb(pb)
    b = cheap * gate
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cyclical-low blended multiple (geo mean of inverses) momentum, gated by net cash
def f38cb_f38_cycle_bottom_value_geocheap_gate_base_v031_signal(pb, evebitda, cashneq, debt):
    geo = np.sqrt(_f38_cheap_pb(pb).clip(lower=0) * _f38_cheap_ev(evebitda).clip(lower=0))
    geomom = geo - geo.shift(21)
    gate = _f38_solv_gate(cashneq, debt)
    b = geomom * gate
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tangible book per share proxy (tangibles/marketcap inverse-pb interaction)
def f38cb_f38_cycle_bottom_value_tangmc_invpb_base_v032_signal(tangibles, marketcap, pb):
    a = _z(tangibles / marketcap.replace(0, np.nan), 252)
    c = _z(_f38_cheap_pb(pb), 252)
    b = a * c
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-cash trend (improving balance sheet) at cheap EV multiple
def f38cb_f38_cycle_bottom_value_netcashtrend_ev_252d_base_v033_signal(cashneq, debt, evebitda):
    nc = _f38_net_cash(cashneq, debt)
    trend = (nc - nc.shift(126)) / (nc.abs() + 1.0)
    cheap = _f38_cheap_ev(evebitda)
    b = trend * cheap
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# how cheap on P/B relative to peers-over-time (1260 rank) AND tangible-backed
def f38cb_f38_cycle_bottom_value_pbrank_tangback_1260d_base_v034_signal(pb, tangibles, marketcap):
    pr = _rank(_f38_cheap_pb(pb), 1260)
    back = _f38_tang_backing(tangibles, marketcap)
    b = pr * (1.0 + back.clip(upper=3.0))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# enterprise value vs equity (leverage of price) inverted z, plus cash-coverage z (additive)
def f38cb_f38_cycle_bottom_value_eveq_cov_base_v035_signal(marketcap, debt, cashneq, equity):
    ev = marketcap + debt - cashneq
    ev_eq = ev / equity.replace(0, np.nan)
    inv = 1.0 / ev_eq.replace(0, np.nan)
    cov = _f38_net_cash_ratio(cashneq, debt)
    b = _z(inv, 252) - _z(cov, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cheapness acceleration toward trough confirmed by debt paydown (debt falling)
def f38cb_f38_cycle_bottom_value_pbtrough_delev_252d_base_v036_signal(pb, debt, cashneq):
    cheap = _f38_cheap_pb(pb)
    cheapchg = cheap - cheap.shift(63)
    delev = (debt.shift(63) - debt) / (debt.shift(63).abs() + 1.0)
    gate = _f38_solv_gate(cashneq, debt)
    b = cheapchg * (1.0 + delev) * gate
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tangible-backing yield vs EV/EBITDA: tangibles/EV inverted-multiple interaction
def f38cb_f38_cycle_bottom_value_tangev_evcheap_base_v037_signal(tangibles, marketcap, debt, cashneq, evebitda):
    ev = marketcap + debt - cashneq
    tang_ev = tangibles / ev.replace(0, np.nan)
    cheap = _f38_cheap_ev(evebitda)
    b = _z(tang_ev, 252) + _z(cheap, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net cash months-of-survival proxy (z) minus cheap-pb (z): solvency-vs-cheapness spread
def f38cb_f38_cycle_bottom_value_survmonths_pb_base_v038_signal(cashneq, debt, pb):
    surv = cashneq / (debt.replace(0, np.nan) * 0.1 + 1.0)
    cheap = _f38_cheap_pb(pb)
    b = _z(np.log1p(surv.clip(lower=0)), 252) - _z(cheap, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# multi-pillar minimum: bottleneck of cheap-pb, cheap-ev, net-cash (weakest-link value)
def f38cb_f38_cycle_bottom_value_bottleneck_252d_base_v039_signal(pb, evebitda, cashneq, debt):
    a = _rank(_f38_cheap_pb(pb), 252)
    c = _rank(_f38_cheap_ev(evebitda), 252)
    s = _rank(_f38_net_cash(cashneq, debt), 252)
    stacked = pd.concat([a, c, s], axis=1)
    b = stacked.min(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tangible book erosion-adjusted cheapness: tangibles stable & P/B cheap
def f38cb_f38_cycle_bottom_value_tangerode_pb_252d_base_v040_signal(tangibles, pb):
    erode = (tangibles - tangibles.shift(126)) / (tangibles.shift(126).abs() + 1.0)
    cheap = _f38_cheap_pb(pb)
    b = (1.0 + erode.clip(lower=-0.9)) * cheap
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash-rich-cheap: cashneq/marketcap times inverse-EV multiple
def f38cb_f38_cycle_bottom_value_cashmc_ev_base_v041_signal(cashneq, marketcap, evebitda):
    cashmc = cashneq / marketcap.replace(0, np.nan)
    cheap = _f38_cheap_ev(evebitda)
    b = cashmc * cheap
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-debt to equity inverted (low leverage) times cheap-pb
def f38cb_f38_cycle_bottom_value_netdebteq_pb_base_v042_signal(debt, cashneq, equity, pb):
    nde = (debt - cashneq) / equity.replace(0, np.nan)
    lowlev = 1.0 / (1.0 + np.exp(nde))
    cheap = _f38_cheap_pb(pb)
    b = lowlev * cheap
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# value-trap avoidance: cheap-pb only when tangibles/marketcap above its 252d median
def f38cb_f38_cycle_bottom_value_trapavoid_252d_base_v043_signal(pb, tangibles, marketcap):
    back = _f38_tang_backing(tangibles, marketcap)
    med = _mean(back, 252)
    qual = (back - med)
    cheap = _f38_cheap_pb(pb)
    b = cheap * np.tanh(qual)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# enterprise multiple distance below its 252d EMA, gated by cash coverage
def f38cb_f38_cycle_bottom_value_evema_cov_252d_base_v044_signal(evebitda, cashneq, debt):
    ema = evebitda.ewm(span=126, min_periods=63).mean()
    below = (ema - evebitda) / ema.replace(0, np.nan)
    cov = _f38_net_cash_ratio(cashneq, debt).clip(upper=8.0)
    b = below * cov
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# combined deep-value × solvency interaction, tanh-bounded
def f38cb_f38_cycle_bottom_value_interact_tanh_252d_base_v045_signal(pb, cashneq, debt):
    cheap = _z(_f38_cheap_pb(pb), 252)
    solv = _z(_f38_net_cash_ratio(cashneq, debt), 252)
    b = np.tanh(cheap) * np.tanh(solv)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tangible-asset coverage of total obligations (tangibles vs debt) z, x cheap EV
def f38cb_f38_cycle_bottom_value_tangcov_evz_252d_base_v046_signal(tangibles, debt, evebitda):
    cov = _z(tangibles / debt.replace(0, np.nan), 252)
    cheap = _z(_f38_cheap_ev(evebitda), 252)
    b = cov + cheap
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# graham net-net floor (tangibles-debt)/marketcap percentile, x cheap-pb percentile
def f38cb_f38_cycle_bottom_value_netnet_pb_base_v047_signal(tangibles, debt, marketcap, pb):
    netnet = (tangibles - debt) / marketcap.replace(0, np.nan)
    nr = _rank(netnet, 1260) + 0.5
    pr = _rank(_f38_cheap_pb(pb), 1260) + 0.5
    b = nr * pr
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# how deep below cycle-mid the blended multiple is, gated by net cash positive
def f38cb_f38_cycle_bottom_value_blendtrough_gate_504d_base_v048_signal(pb, evebitda, cashneq, debt):
    cpb = (_mean(pb, 504) - pb) / _mean(pb, 504).replace(0, np.nan)
    cev = (_mean(evebitda, 504) - evebitda) / _mean(evebitda, 504).replace(0, np.nan)
    gate = _f38_solv_gate(cashneq, debt)
    b = (cpb + cev) * gate
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash buffer dispersion-stability times cheap-pb (stable cash + cheap)
def f38cb_f38_cycle_bottom_value_cashstab_pb_252d_base_v049_signal(cashneq, debt, pb):
    nc = _f38_net_cash(cashneq, debt)
    stab = _mean(nc, 252) / (_std(nc, 252) + 1.0)
    cheap = _f38_cheap_pb(pb)
    b = np.tanh(stab / 1e7) * cheap
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tangible-backed enterprise yield: tangibles/EV ranked, x net-cash ratio
def f38cb_f38_cycle_bottom_value_tangevyld_cov_1260d_base_v050_signal(tangibles, marketcap, debt, cashneq):
    ev = marketcap + debt - cashneq
    tyld = _rank(tangibles / ev.replace(0, np.nan), 1260)
    cov = _f38_net_cash_ratio(cashneq, debt).clip(upper=8.0)
    b = tyld * cov
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# equity yield gated by tangible backing above debt (solvent book)
def f38cb_f38_cycle_bottom_value_eqyld_tangdebt_base_v051_signal(equity, marketcap, tangibles, debt):
    eqyld = equity / marketcap.replace(0, np.nan)
    cover = tangibles / debt.replace(0, np.nan)
    gate = 1.0 / (1.0 + np.exp(-(cover - 1.0)))
    b = eqyld * gate
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cheap-pb sign×magnitude (sqrt) gated by net cash sign (solvent deep value)
def f38cb_f38_cycle_bottom_value_pbsqrt_netcashsign_base_v052_signal(pb, cashneq, debt):
    cheap = _f38_cheap_pb(pb)
    mag = np.sign(cheap) * (cheap.abs() ** 0.5)
    nc = _f38_net_cash(cashneq, debt)
    gate = (nc > 0).astype(float) * 0.5 + 0.5
    b = mag * gate
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# inverse EV/EBITDA percentile (504) minus tangible-backing percentile (504): cheap-vs-asset spread
def f38cb_f38_cycle_bottom_value_evpct_tang_504d_base_v053_signal(evebitda, tangibles, marketcap):
    pct = _rank(_f38_cheap_ev(evebitda), 504)
    backpct = _rank(_f38_tang_backing(tangibles, marketcap), 504)
    b = pct - backpct
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# excess-cash buffer (smooth cash-over-debt cushion) times cheap-pb deviation
def f38cb_f38_cycle_bottom_value_excesscash_pb_base_v054_signal(cashneq, debt, pb):
    cushion = (cashneq - debt) / (cashneq.abs() + debt.abs() + 1.0)
    smooth = cushion.ewm(span=63, min_periods=21).mean()
    cheap = _f38_cheap_pb(pb)
    cheap_d = cheap - _mean(cheap, 252)
    b = (0.5 + np.tanh(smooth)) * cheap_d
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tangible book to marketcap minus EV/EBITDA richness (combined value gap z)
def f38cb_f38_cycle_bottom_value_valuegap_252d_base_v055_signal(tangibles, marketcap, evebitda):
    gap = tangibles / marketcap.replace(0, np.nan)
    rich = evebitda
    b = _z(gap, 252) - _z(rich, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# survivable deep value: min(cheap-pb-rank, netcash-rank) times tangible backing
def f38cb_f38_cycle_bottom_value_survvalue_252d_base_v056_signal(pb, cashneq, debt, tangibles, marketcap):
    pr = _rank(_f38_cheap_pb(pb), 252)
    nr = _rank(_f38_net_cash(cashneq, debt), 252)
    stacked = pd.concat([pr, nr], axis=1)
    floor = stacked.min(axis=1)
    back = _f38_tang_backing(tangibles, marketcap)
    b = floor * (0.5 + back.clip(upper=3.0))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/EBITDA below 1260d min-band gated by equity-to-debt solvency
def f38cb_f38_cycle_bottom_value_evfloor_eqdebt_1260d_base_v057_signal(evebitda, equity, debt):
    lo = _rmin(evebitda, 1260)
    nearfloor = lo / evebitda.replace(0, np.nan)
    eqd = equity / debt.replace(0, np.nan)
    gate = 1.0 / (1.0 + np.exp(-(eqd - 1.0)))
    b = nearfloor * gate
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# log net-cash-to-marketcap momentum, plus cheap-pb momentum (additive value+cash, change space)
def f38cb_f38_cycle_bottom_value_lognc_logpb_base_v058_signal(cashneq, debt, marketcap, pb):
    nc = _f38_net_cash(cashneq, debt)
    lognc = np.sign(nc) * np.log1p(nc.abs() / (marketcap.replace(0, np.nan)))
    logpb = np.log(_f38_cheap_pb(pb).clip(lower=1e-6))
    b = (lognc - lognc.shift(63)) + 0.3 * (logpb - logpb.shift(63))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tangible-asset intensity (tangibles/equity) x net cash positive x cheap-pb gate
def f38cb_f38_cycle_bottom_value_tangint_solv_base_v059_signal(tangibles, equity, cashneq, debt, pb):
    ti = tangibles / equity.replace(0, np.nan)
    gate = _f38_solv_gate(cashneq, debt)
    cheap = _z(_f38_cheap_pb(pb), 252)
    b = ti * gate * np.tanh(cheap)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash-to-debt momentum (deleveraging-via-cash) confirmed by cheap EV
def f38cb_f38_cycle_bottom_value_covmom_ev_252d_base_v060_signal(cashneq, debt, evebitda):
    cov = _f38_net_cash_ratio(cashneq, debt)
    mom = cov - cov.shift(126)
    cheap = _f38_cheap_ev(evebitda)
    b = mom * cheap
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# combined cyclical-trough composite: z(invpb)+z(invev)+z(cashneq/marketcap)
def f38cb_f38_cycle_bottom_value_trough3_252d_base_v061_signal(pb, evebitda, cashneq, marketcap):
    a = _z(_f38_cheap_pb(pb), 252)
    c = _z(_f38_cheap_ev(evebitda), 252)
    s = _z(cashneq / marketcap.replace(0, np.nan), 252)
    b = (a + c + s) / 3.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tangibles-per-marketcap trend (asset-base growth) at cheap pb
def f38cb_f38_cycle_bottom_value_backtrend_pb_252d_base_v062_signal(tangibles, marketcap, pb):
    back = _f38_tang_backing(tangibles, marketcap)
    trend = back - back.shift(126)
    cheap = _f38_cheap_pb(pb)
    b = trend * cheap
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# distress-adjusted cheapness deviation: demeaned inverse-pb downweighted when debt>cash
def f38cb_f38_cycle_bottom_value_distadj_pb_base_v063_signal(pb, cashneq, debt):
    cheap = _f38_cheap_pb(pb)
    cheap_d = cheap - _mean(cheap, 252)
    distress = (debt - cashneq) / (debt.abs() + cashneq.abs() + 1.0)
    b = np.tanh(8.0 * cheap_d) * (1.0 - np.tanh(distress.clip(lower=0)))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-net working floor (tangibles+cash-debt) per marketcap z, minus EV-richness z
def f38cb_f38_cycle_bottom_value_netnetfloor_ev_base_v064_signal(tangibles, cashneq, debt, marketcap, evebitda):
    floor = (tangibles + cashneq - debt) / marketcap.replace(0, np.nan)
    b = _z(floor, 504) - _z(evebitda, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cheap-multiple dispersion (volatility of inverse-pb) times cash-coverage rank
def f38cb_f38_cycle_bottom_value_cheapstab_cov_252d_base_v065_signal(pb, cashneq, debt):
    cheap = _f38_cheap_pb(pb)
    disp = _std(cheap, 63) / (_mean(cheap, 63).abs() + 1e-6)
    cov = _rank(_f38_net_cash_ratio(cashneq, debt), 252)
    b = disp * cov
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# enterprise-to-tangibles below 504d mean (asset cheap), gated by net cash
def f38cb_f38_cycle_bottom_value_evtangtrough_gate_504d_base_v066_signal(marketcap, debt, cashneq, tangibles):
    ev = marketcap + debt - cashneq
    et = ev / tangibles.replace(0, np.nan)
    trough = (_mean(et, 504) - et) / _mean(et, 504).replace(0, np.nan)
    gate = _f38_solv_gate(cashneq, debt)
    b = trough * gate
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash-coverage of debt percentile (1260) x inverse-pb percentile (1260) product
def f38cb_f38_cycle_bottom_value_covpct_pbpct_1260d_base_v067_signal(cashneq, debt, pb):
    cp = _rank(_f38_net_cash_ratio(cashneq, debt), 1260)
    pp = _rank(_f38_cheap_pb(pb), 1260)
    b = (cp + 0.5) * (pp + 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tangible book yield over equity book yield diff, gated cheap EV (asset-vs-book quality)
def f38cb_f38_cycle_bottom_value_tangvseq_ev_base_v068_signal(tangibles, equity, marketcap, evebitda):
    tyld = tangibles / marketcap.replace(0, np.nan)
    eyld = equity / marketcap.replace(0, np.nan)
    cheap = _f38_cheap_ev(evebitda)
    b = (tyld - eyld) * (1.0 + np.tanh(cheap))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# survivable-trough flag intensity: cheap (pb<252d med) AND solvent (cash>debt)
def f38cb_f38_cycle_bottom_value_dualflag_252d_base_v069_signal(pb, cashneq, debt):
    cheapflag = (pb < _mean(pb, 252)).astype(float)
    solvflag = (cashneq > debt).astype(float)
    both = cheapflag * solvflag
    depth = (_mean(pb, 252) - pb) / _mean(pb, 252).replace(0, np.nan)
    b = both.rolling(63, min_periods=21).mean() + depth
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net cash as fraction of tangibles (liquid-asset share) momentum x inverse-pb sign
def f38cb_f38_cycle_bottom_value_liqshare_pb_base_v070_signal(cashneq, debt, tangibles, pb):
    liq = _f38_net_cash(cashneq, debt) / tangibles.replace(0, np.nan)
    liqmom = liq - liq.shift(126)
    cheap = _f38_cheap_pb(pb)
    b = liqmom * _rank(cheap, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# how far EV/EBITDA below its 1260d median in std units, plus net-cash-ratio z (additive deep value+cash)
def f38cb_f38_cycle_bottom_value_evdeepz_gate_1260d_base_v071_signal(evebitda, cashneq, debt):
    deepz = -_z(evebitda, 1260)
    covz = _z(_f38_net_cash_ratio(cashneq, debt), 1260)
    b = deepz + covz
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tangible-asset coverage growth x cheap-pb (improving asset backing while cheap)
def f38cb_f38_cycle_bottom_value_tangcovgrow_pb_252d_base_v072_signal(tangibles, debt, pb):
    cov = tangibles / debt.replace(0, np.nan)
    grow = (cov - cov.shift(126)) / (cov.shift(126).abs() + 1.0)
    cheap = _f38_cheap_pb(pb)
    b = grow * cheap
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# composite armed: product of three sigmoid gates (cheap-pb, cheap-ev, cash>debt)
def f38cb_f38_cycle_bottom_value_armgates_252d_base_v073_signal(pb, evebitda, cashneq, debt):
    g1 = 1.0 / (1.0 + np.exp(-_z(_f38_cheap_pb(pb), 252)))
    g2 = 1.0 / (1.0 + np.exp(-_z(_f38_cheap_ev(evebitda), 252)))
    g3 = _f38_solv_gate(cashneq, debt)
    b = g1 * g2 * g3
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# equity-to-marketcap (book yield) z minus cash-coverage z (book-yield-vs-coverage tension)
def f38cb_f38_cycle_bottom_value_bookyld_cov_base_v074_signal(equity, marketcap, cashneq, debt):
    byld = equity / marketcap.replace(0, np.nan)
    cov = _f38_net_cash_ratio(cashneq, debt)
    b = _z(byld, 504) - _z(cov, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# deep-value+solvency composite ranked over cycle (final blended cycle-bottom score)
def f38cb_f38_cycle_bottom_value_cyclescore_1260d_base_v075_signal(pb, evebitda, cashneq, debt, tangibles, marketcap):
    a = _rank(_f38_cheap_pb(pb), 1260)
    c = _rank(_f38_cheap_ev(evebitda), 1260)
    s = _rank(_f38_net_cash_ratio(cashneq, debt), 1260)
    t = _rank(tangibles / marketcap.replace(0, np.nan), 1260)
    b = (a + c + s + t) / 4.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f38cb_f38_cycle_bottom_value_cheappb_netcash_252d_base_v001_signal,
    f38cb_f38_cycle_bottom_value_cheapev_cashcov_252d_base_v002_signal,
    f38cb_f38_cycle_bottom_value_pbz_tangback_252d_base_v003_signal,
    f38cb_f38_cycle_bottom_value_evnetcash_252d_base_v004_signal,
    f38cb_f38_cycle_bottom_value_navdisc_gate_base_v005_signal,
    f38cb_f38_cycle_bottom_value_blendcheap_cov_252d_base_v006_signal,
    f38cb_f38_cycle_bottom_value_tangeq_cheap_base_v007_signal,
    f38cb_f38_cycle_bottom_value_netcashmc_ev_base_v008_signal,
    f38cb_f38_cycle_bottom_value_bookyld_solv_base_v009_signal,
    f38cb_f38_cycle_bottom_value_pbmom_covmom_252d_base_v010_signal,
    f38cb_f38_cycle_bottom_value_pbtrough_gate_504d_base_v011_signal,
    f38cb_f38_cycle_bottom_value_evtrough_tang_504d_base_v012_signal,
    f38cb_f38_cycle_bottom_value_covz_pb_252d_base_v013_signal,
    f38cb_f38_cycle_bottom_value_tangdebt_ev_base_v014_signal,
    f38cb_f38_cycle_bottom_value_pbrank_covrank_252d_base_v015_signal,
    f38cb_f38_cycle_bottom_value_tangminus_ev_base_v016_signal,
    f38cb_f38_cycle_bottom_value_warchest_pb_base_v017_signal,
    f38cb_f38_cycle_bottom_value_buffer_ev_base_v018_signal,
    f38cb_f38_cycle_bottom_value_pbcyclrank_gate_1260d_base_v019_signal,
    f38cb_f38_cycle_bottom_value_evcyclrank_back_1260d_base_v020_signal,
    f38cb_f38_cycle_bottom_value_evtang_inv_base_v021_signal,
    f38cb_f38_cycle_bottom_value_pbnetcash_arm_252d_base_v022_signal,
    f38cb_f38_cycle_bottom_value_tangfloor_pb_base_v023_signal,
    f38cb_f38_cycle_bottom_value_netcashev_cheap_base_v024_signal,
    f38cb_f38_cycle_bottom_value_triple_252d_base_v025_signal,
    f38cb_f38_cycle_bottom_value_pbminband_cov_1260d_base_v026_signal,
    f38cb_f38_cycle_bottom_value_tangstab_ev_252d_base_v027_signal,
    f38cb_f38_cycle_bottom_value_pb_tangcoverdebt_base_v028_signal,
    f38cb_f38_cycle_bottom_value_ncmcz_evz_252d_base_v029_signal,
    f38cb_f38_cycle_bottom_value_eqdebt_pb_base_v030_signal,
    f38cb_f38_cycle_bottom_value_geocheap_gate_base_v031_signal,
    f38cb_f38_cycle_bottom_value_tangmc_invpb_base_v032_signal,
    f38cb_f38_cycle_bottom_value_netcashtrend_ev_252d_base_v033_signal,
    f38cb_f38_cycle_bottom_value_pbrank_tangback_1260d_base_v034_signal,
    f38cb_f38_cycle_bottom_value_eveq_cov_base_v035_signal,
    f38cb_f38_cycle_bottom_value_pbtrough_delev_252d_base_v036_signal,
    f38cb_f38_cycle_bottom_value_tangev_evcheap_base_v037_signal,
    f38cb_f38_cycle_bottom_value_survmonths_pb_base_v038_signal,
    f38cb_f38_cycle_bottom_value_bottleneck_252d_base_v039_signal,
    f38cb_f38_cycle_bottom_value_tangerode_pb_252d_base_v040_signal,
    f38cb_f38_cycle_bottom_value_cashmc_ev_base_v041_signal,
    f38cb_f38_cycle_bottom_value_netdebteq_pb_base_v042_signal,
    f38cb_f38_cycle_bottom_value_trapavoid_252d_base_v043_signal,
    f38cb_f38_cycle_bottom_value_evema_cov_252d_base_v044_signal,
    f38cb_f38_cycle_bottom_value_interact_tanh_252d_base_v045_signal,
    f38cb_f38_cycle_bottom_value_tangcov_evz_252d_base_v046_signal,
    f38cb_f38_cycle_bottom_value_netnet_pb_base_v047_signal,
    f38cb_f38_cycle_bottom_value_blendtrough_gate_504d_base_v048_signal,
    f38cb_f38_cycle_bottom_value_cashstab_pb_252d_base_v049_signal,
    f38cb_f38_cycle_bottom_value_tangevyld_cov_1260d_base_v050_signal,
    f38cb_f38_cycle_bottom_value_eqyld_tangdebt_base_v051_signal,
    f38cb_f38_cycle_bottom_value_pbsqrt_netcashsign_base_v052_signal,
    f38cb_f38_cycle_bottom_value_evpct_tang_504d_base_v053_signal,
    f38cb_f38_cycle_bottom_value_excesscash_pb_base_v054_signal,
    f38cb_f38_cycle_bottom_value_valuegap_252d_base_v055_signal,
    f38cb_f38_cycle_bottom_value_survvalue_252d_base_v056_signal,
    f38cb_f38_cycle_bottom_value_evfloor_eqdebt_1260d_base_v057_signal,
    f38cb_f38_cycle_bottom_value_lognc_logpb_base_v058_signal,
    f38cb_f38_cycle_bottom_value_tangint_solv_base_v059_signal,
    f38cb_f38_cycle_bottom_value_covmom_ev_252d_base_v060_signal,
    f38cb_f38_cycle_bottom_value_trough3_252d_base_v061_signal,
    f38cb_f38_cycle_bottom_value_backtrend_pb_252d_base_v062_signal,
    f38cb_f38_cycle_bottom_value_distadj_pb_base_v063_signal,
    f38cb_f38_cycle_bottom_value_netnetfloor_ev_base_v064_signal,
    f38cb_f38_cycle_bottom_value_cheapstab_cov_252d_base_v065_signal,
    f38cb_f38_cycle_bottom_value_evtangtrough_gate_504d_base_v066_signal,
    f38cb_f38_cycle_bottom_value_covpct_pbpct_1260d_base_v067_signal,
    f38cb_f38_cycle_bottom_value_tangvseq_ev_base_v068_signal,
    f38cb_f38_cycle_bottom_value_dualflag_252d_base_v069_signal,
    f38cb_f38_cycle_bottom_value_liqshare_pb_base_v070_signal,
    f38cb_f38_cycle_bottom_value_evdeepz_gate_1260d_base_v071_signal,
    f38cb_f38_cycle_bottom_value_tangcovgrow_pb_252d_base_v072_signal,
    f38cb_f38_cycle_bottom_value_armgates_252d_base_v073_signal,
    f38cb_f38_cycle_bottom_value_bookyld_cov_base_v074_signal,
    f38cb_f38_cycle_bottom_value_cyclescore_1260d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F38_CYCLE_BOTTOM_VALUE_REGISTRY_001_075 = REGISTRY


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

    # metrics: small positive multiples (~0.3-5)
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

    print("OK f38_cycle_bottom_value_base_001_075_claude: %d features pass" % n_features)
