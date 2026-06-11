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


# ============================================================
# cheap-pb minus cycle-mean (504), gated by tangibles-cover-debt sigmoid
def f38cb_f38_cycle_bottom_value_pbdev_tangcov_504d_base_v076_signal(pb, tangibles, debt):
    cheap = _f38_cheap_pb(pb)
    dev = cheap - _mean(cheap, 504)
    cover = tangibles / debt.replace(0, np.nan)
    gate = 1.0 / (1.0 + np.exp(-(cover - 1.0)))
    b = dev * gate
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net cash / EV ranked over cycle, times inverse-pb ranked (two-pillar percentile product)
def f38cb_f38_cycle_bottom_value_ncevpct_pbpct_1260d_base_v077_signal(cashneq, debt, marketcap, pb):
    ev = _f38_ev(marketcap, debt, cashneq)
    ncev = _rank(_f38_net_cash(cashneq, debt) / ev.replace(0, np.nan), 1260) + 0.5
    pp = _rank(_f38_cheap_pb(pb), 1260) + 0.5
    b = ncev * pp
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tangible backing minus equity backing (intangible drag), gated cheap-ev
def f38cb_f38_cycle_bottom_value_intdrag_ev_base_v078_signal(tangibles, equity, marketcap, evebitda):
    drag = (tangibles - equity) / marketcap.replace(0, np.nan)
    cheap = _f38_cheap_ev(evebitda)
    b = drag * np.tanh(cheap)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# blended-multiple z (cheap pb + cheap ev) times net-cash sign-magnitude
def f38cb_f38_cycle_bottom_value_blendz_ncsign_252d_base_v079_signal(pb, evebitda, cashneq, debt):
    blend = _z(_f38_cheap_pb(pb), 252) + _z(_f38_cheap_ev(evebitda), 252)
    nc = _f38_net_cash(cashneq, debt)
    b = blend * np.sign(nc) * (nc.abs() ** 0.25 / 100.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash-coverage of debt EMA-deviation (improving liquidity) times cheap-pb
def f38cb_f38_cycle_bottom_value_covema_pb_252d_base_v080_signal(cashneq, debt, pb):
    cov = _f38_net_cash_ratio(cashneq, debt)
    dev = cov - cov.ewm(span=126, min_periods=63).mean()
    cheap = _f38_cheap_pb(pb)
    b = dev * cheap
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tangible asset floor per share growth, gated by net cash positive (asset accretion while solvent)
def f38cb_f38_cycle_bottom_value_tangfloorgrow_gate_252d_base_v081_signal(tangibles, marketcap, cashneq, debt):
    back = _f38_tang_backing(tangibles, marketcap)
    grow = back - back.shift(126)
    gate = _f38_solv_gate(cashneq, debt)
    b = grow * gate
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# deep value at trough: how far inverse-ev above its 252 median, x cash coverage rank
def f38cb_f38_cycle_bottom_value_evabovemed_covrank_252d_base_v082_signal(evebitda, cashneq, debt):
    cheap = _f38_cheap_ev(evebitda)
    above = cheap - _mean(cheap, 252)
    covrank = _rank(_f38_net_cash_ratio(cashneq, debt), 252) + 0.5
    b = above * covrank
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# enterprise value to tangibles, inverted and z-scored, plus net-cash ratio z
def f38cb_f38_cycle_bottom_value_evtanginv_cov_504d_base_v083_signal(marketcap, debt, cashneq, tangibles):
    ev = _f38_ev(marketcap, debt, cashneq)
    inv = tangibles / ev.replace(0, np.nan)
    b = _z(inv, 504) + 0.5 * _z(_f38_net_cash_ratio(cashneq, debt), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cheap-pb percentile spread short vs long window (cheapness regime shift), gated solvency
def f38cb_f38_cycle_bottom_value_pbpctspr_gate_base_v084_signal(pb, cashneq, debt):
    short = _rank(_f38_cheap_pb(pb), 252)
    long = _rank(_f38_cheap_pb(pb), 1260)
    gate = _f38_solv_gate(cashneq, debt)
    b = (short - long) * gate
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net cash buffer per tangibles z, plus inverse-ev z (liquid-asset-backed cheapness)
def f38cb_f38_cycle_bottom_value_liqtang_ev_252d_base_v085_signal(cashneq, debt, tangibles, evebitda):
    liq = _z(_f38_net_cash(cashneq, debt) / tangibles.replace(0, np.nan), 252)
    cheap = _z(_f38_cheap_ev(evebitda), 252)
    b = liq + cheap
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# equity-to-debt coverage growth (deleveraging) x cheap-pb deviation
def f38cb_f38_cycle_bottom_value_eqdebtgrow_pb_252d_base_v086_signal(equity, debt, pb):
    cov = equity / debt.replace(0, np.nan)
    grow = (cov - cov.shift(126)) / (cov.shift(126).abs() + 1.0)
    cheap = _f38_cheap_pb(pb)
    dev = cheap - _mean(cheap, 252)
    b = grow * np.tanh(8.0 * dev)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# combined trough-and-solvent: min(cheap-ev rank, cash-cov rank) x tangible backing rank
def f38cb_f38_cycle_bottom_value_minsolv_back_252d_base_v087_signal(evebitda, cashneq, debt, tangibles, marketcap):
    cr = _rank(_f38_cheap_ev(evebitda), 252)
    sr = _rank(_f38_net_cash_ratio(cashneq, debt), 252)
    stacked = pd.concat([cr, sr], axis=1)
    floor = stacked.min(axis=1)
    back = _rank(_f38_tang_backing(tangibles, marketcap), 252) + 0.5
    b = floor * back
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-net floor (tangibles+cash-debt)/marketcap momentum, gated cheap-pb
def f38cb_f38_cycle_bottom_value_netnetmom_pb_252d_base_v088_signal(tangibles, cashneq, debt, marketcap, pb):
    floor = (tangibles + cashneq - debt) / marketcap.replace(0, np.nan)
    mom = floor - floor.shift(63)
    cheap = _rank(_f38_cheap_pb(pb), 252) + 0.5
    b = mom * cheap
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# inverse-pb dispersion (cheapness volatility) times cash-coverage deviation
def f38cb_f38_cycle_bottom_value_pbdisp_covdev_252d_base_v089_signal(pb, cashneq, debt):
    cheap = _f38_cheap_pb(pb)
    disp = _std(cheap, 63) / (_mean(cheap, 63).abs() + 1e-6)
    cov = _f38_net_cash_ratio(cashneq, debt)
    covdev = cov - _mean(cov, 252)
    b = disp * np.tanh(covdev)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tangibles-cover-debt ranked over cycle, plus inverse-ev ranked (asset-coverage + cheapness)
def f38cb_f38_cycle_bottom_value_tangcovrank_evrank_1260d_base_v090_signal(tangibles, debt, evebitda):
    tc = _rank(tangibles / debt.replace(0, np.nan), 1260)
    cr = _rank(_f38_cheap_ev(evebitda), 1260)
    b = tc + cr
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# excess net cash (cash-debt)/marketcap z, times sign of cheap-pb deviation
def f38cb_f38_cycle_bottom_value_excessnc_pbsign_252d_base_v091_signal(cashneq, debt, marketcap, pb):
    excess = _z(_f38_net_cash(cashneq, debt) / marketcap.replace(0, np.nan), 252)
    cheap = _f38_cheap_pb(pb)
    cheap_d = cheap - _mean(cheap, 252)
    b = excess * np.tanh(8.0 * cheap_d)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# how deep below 1260 mean the EV/EBITDA is (fraction), gated by equity-to-debt
def f38cb_f38_cycle_bottom_value_evdeepfrac_eqdebt_1260d_base_v092_signal(evebitda, equity, debt):
    deep = (_mean(evebitda, 1260) - evebitda) / _mean(evebitda, 1260).replace(0, np.nan)
    eqd = equity / debt.replace(0, np.nan)
    gate = 1.0 / (1.0 + np.exp(-(eqd - 1.0)))
    b = deep * gate
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tangible backing acceleration (asset-base inflection) times cheap-ev rank
def f38cb_f38_cycle_bottom_value_backaccel_ev_252d_base_v093_signal(tangibles, marketcap, evebitda):
    back = _f38_tang_backing(tangibles, marketcap)
    accel = (back - back.shift(63)) - (back.shift(63) - back.shift(126))
    cheap = _rank(_f38_cheap_ev(evebitda), 252) + 0.5
    b = accel * cheap
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# survival gate persistence (fraction of year solvent) times cheap-ev deviation
def f38cb_f38_cycle_bottom_value_gatepersist_ev_252d_base_v094_signal(cashneq, debt, evebitda):
    gate = _f38_solv_gate(cashneq, debt)
    persist = _mean(gate, 252)
    cheap = _f38_cheap_ev(evebitda)
    dev = cheap - _mean(cheap, 252)
    b = persist * dev
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash-to-marketcap minus debt-to-marketcap (net-cash yield) x cheap-pb sign-magnitude
def f38cb_f38_cycle_bottom_value_ncyld_pbmag_base_v095_signal(cashneq, debt, marketcap, pb):
    ncyld = (cashneq - debt) / marketcap.replace(0, np.nan)
    cheap = _f38_cheap_pb(pb)
    mag = np.sign(cheap) * (cheap.abs() ** 0.5)
    b = np.tanh(ncyld) * mag
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# enterprise-to-equity inverted percentile, x cash-coverage percentile (cheap-on-book + solvent)
def f38cb_f38_cycle_bottom_value_eveqpct_covpct_1260d_base_v096_signal(marketcap, debt, cashneq, equity):
    ev = _f38_ev(marketcap, debt, cashneq)
    inv = equity / ev.replace(0, np.nan)
    ip = _rank(inv, 1260) + 0.5
    cp = _rank(_f38_net_cash_ratio(cashneq, debt), 1260) + 0.5
    b = ip * cp
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# blended cheapness (geo-mean inverses) z, plus tangible-backing z (cheap with asset floor)
def f38cb_f38_cycle_bottom_value_geoz_backz_252d_base_v097_signal(pb, evebitda, tangibles, marketcap):
    geo = np.sqrt(_f38_cheap_pb(pb).clip(lower=0) * _f38_cheap_ev(evebitda).clip(lower=0))
    back = _f38_tang_backing(tangibles, marketcap)
    b = _z(geo, 252) + _z(back, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt-paydown momentum confirmed by cheap-ev (deleveraging value)
def f38cb_f38_cycle_bottom_value_delev_ev_252d_base_v098_signal(debt, cashneq, evebitda):
    delev = (debt.shift(126) - debt) / (debt.shift(126).abs() + 1.0)
    gate = _f38_solv_gate(cashneq, debt)
    cheap = _f38_cheap_ev(evebitda)
    b = delev * gate * cheap
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tangible book minus market cap discount (NAV gap) percentile, x cash-coverage
def f38cb_f38_cycle_bottom_value_navgappct_cov_504d_base_v099_signal(tangibles, marketcap, cashneq, debt):
    gap = (tangibles - marketcap) / marketcap.replace(0, np.nan)
    gp = _rank(gap, 504) + 0.5
    cov = _f38_net_cash_ratio(cashneq, debt).clip(upper=8.0)
    b = gp * cov
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cheap-pb z minus cheap-pb z one year ago (cheapness inflection), gated net cash
def f38cb_f38_cycle_bottom_value_pbzinfl_gate_252d_base_v100_signal(pb, cashneq, debt):
    cz = _z(_f38_cheap_pb(pb), 252)
    infl = cz - cz.shift(252)
    gate = _f38_solv_gate(cashneq, debt)
    b = infl * gate
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-cash war chest per equity rank x inverse-ev rank (capital-armed deep value)
def f38cb_f38_cycle_bottom_value_warchesteq_ev_1260d_base_v101_signal(cashneq, debt, equity, evebitda):
    wc = _rank(_f38_net_cash(cashneq, debt) / equity.replace(0, np.nan), 1260) + 0.5
    cr = _rank(_f38_cheap_ev(evebitda), 1260) + 0.5
    b = wc * cr
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tangibles/EV percentile minus EV-richness percentile (asset-yield vs richness spread)
def f38cb_f38_cycle_bottom_value_tangevyld_spr_1260d_base_v102_signal(tangibles, marketcap, debt, cashneq, evebitda):
    ev = _f38_ev(marketcap, debt, cashneq)
    ty = _rank(tangibles / ev.replace(0, np.nan), 1260)
    rich = _rank(evebitda, 1260)
    b = ty - rich
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash-coverage stability (mean/std) times cheap-pb percentile (durable solvency + cheap)
def f38cb_f38_cycle_bottom_value_covstab_pb_252d_base_v103_signal(cashneq, debt, pb):
    cov = _f38_net_cash_ratio(cashneq, debt)
    stab = _mean(cov, 252) / (_std(cov, 252) + 1e-6)
    cheap = _rank(_f38_cheap_pb(pb), 504) + 0.5
    b = np.tanh(stab) * cheap
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# composite three-pillar minimum percentile (weakest of cheap-pb, cheap-ev, net cash)
def f38cb_f38_cycle_bottom_value_minpillar_1260d_base_v104_signal(pb, evebitda, cashneq, debt):
    a = _rank(_f38_cheap_pb(pb), 1260)
    c = _rank(_f38_cheap_ev(evebitda), 1260)
    s = _rank(_f38_net_cash(cashneq, debt), 1260)
    b = pd.concat([a, c, s], axis=1).min(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# enterprise value drawdown from 1260d max (EV bombed), gated by net cash positive
def f38cb_f38_cycle_bottom_value_evdd_gate_1260d_base_v105_signal(marketcap, debt, cashneq):
    ev = _f38_ev(marketcap, debt, cashneq)
    dd = ev / _rmax(ev, 1260).replace(0, np.nan) - 1.0
    gate = _f38_solv_gate(cashneq, debt)
    b = dd * gate
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tangible-coverage-of-debt z times inverse-pb z (asset-secured cheapness)
def f38cb_f38_cycle_bottom_value_tangcovz_pbz_252d_base_v106_signal(tangibles, debt, pb):
    tc = _z(tangibles / debt.replace(0, np.nan), 252)
    cz = _z(_f38_cheap_pb(pb), 252)
    b = tc * cz
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cheap-ev streak below median (persistently cheap quarters), x cash coverage
def f38cb_f38_cycle_bottom_value_evcheapstreak_cov_252d_base_v107_signal(evebitda, cashneq, debt):
    cheapflag = (evebitda < _mean(evebitda, 252)).astype(float)
    streak = cheapflag.rolling(126, min_periods=63).mean()
    cov = _f38_net_cash_ratio(cashneq, debt).clip(upper=8.0)
    b = streak * cov
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-cash-to-EV z minus inverse-pb z (cash-richness vs book-cheapness divergence)
def f38cb_f38_cycle_bottom_value_ncev_pb_div_504d_base_v108_signal(cashneq, debt, marketcap, pb):
    ev = _f38_ev(marketcap, debt, cashneq)
    ncev = _z(_f38_net_cash(cashneq, debt) / ev.replace(0, np.nan), 504)
    cz = _z(_f38_cheap_pb(pb), 504)
    b = ncev - cz
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tangible asset share of book (tangibles/equity) trend times cheap-ev
def f38cb_f38_cycle_bottom_value_tangshare_ev_252d_base_v109_signal(tangibles, equity, evebitda):
    share = tangibles / equity.replace(0, np.nan)
    trend = share - share.shift(126)
    cheap = _f38_cheap_ev(evebitda)
    b = trend * np.tanh(cheap)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# combined value+solvency tanh interaction (cheap-ev x cash-coverage), bounded
def f38cb_f38_cycle_bottom_value_evcov_tanh_252d_base_v110_signal(evebitda, cashneq, debt):
    cheap = _z(_f38_cheap_ev(evebitda), 252)
    cov = _z(_f38_net_cash_ratio(cashneq, debt), 252)
    b = np.tanh(cheap) * np.tanh(cov)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# marketcap-to-tangibles (price vs asset floor) inverted z, gated by net cash
def f38cb_f38_cycle_bottom_value_mctanginv_gate_252d_base_v111_signal(marketcap, tangibles, cashneq, debt):
    pt = marketcap / tangibles.replace(0, np.nan)
    inv = _z(1.0 / pt.replace(0, np.nan), 252)
    gate = _f38_solv_gate(cashneq, debt)
    b = inv * gate
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash coverage 252-min (worst recent liquidity) times cheap-pb (cheap with floor on solvency)
def f38cb_f38_cycle_bottom_value_covmin_pb_252d_base_v112_signal(cashneq, debt, pb):
    cov = _f38_net_cash_ratio(cashneq, debt)
    worst = _rmin(cov, 252)
    cheap = _f38_cheap_pb(pb)
    b = np.tanh(worst) * cheap
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# inverse-pb minus inverse-ev (which multiple cheaper), gated by net cash positive
def f38cb_f38_cycle_bottom_value_multiplespr_gate_base_v113_signal(pb, evebitda, cashneq, debt):
    spr = _z(_f38_cheap_pb(pb), 252) - _z(_f38_cheap_ev(evebitda), 252)
    gate = _f38_solv_gate(cashneq, debt)
    b = spr * gate
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net cash trend (balance-sheet repair) confirmed by cheap-pb rank
def f38cb_f38_cycle_bottom_value_ncrepair_pb_252d_base_v114_signal(cashneq, debt, pb):
    nc = _f38_net_cash(cashneq, debt)
    repair = (nc - nc.shift(126)) / (nc.abs() + 1.0)
    cheap = _rank(_f38_cheap_pb(pb), 252) + 0.5
    b = repair * cheap
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tangibles+cash floor coverage of debt (survival floor) x inverse-ev percentile
def f38cb_f38_cycle_bottom_value_survfloor_ev_252d_base_v115_signal(tangibles, cashneq, debt, evebitda):
    floor = (tangibles + cashneq) / debt.replace(0, np.nan)
    cheap = _rank(_f38_cheap_ev(evebitda), 504) + 0.5
    b = np.tanh(floor / 5.0) * cheap
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# equity book yield deviation times cash-coverage deviation (joint mean-reversion)
def f38cb_f38_cycle_bottom_value_byld_cov_revert_252d_base_v116_signal(equity, marketcap, cashneq, debt):
    byld = equity / marketcap.replace(0, np.nan)
    bd = byld - _mean(byld, 252)
    cov = _f38_net_cash_ratio(cashneq, debt)
    cd = cov - _mean(cov, 252)
    b = np.sign(bd) * np.sign(cd) * (bd.abs() * cd.abs()) ** 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cheap multiple percentile (1260) blended (pb,ev avg) times tangible backing rank
def f38cb_f38_cycle_bottom_value_blendpct_back_1260d_base_v117_signal(pb, evebitda, tangibles, marketcap):
    blend = 0.5 * _rank(_f38_cheap_pb(pb), 1260) + 0.5 * _rank(_f38_cheap_ev(evebitda), 1260)
    back = _rank(_f38_tang_backing(tangibles, marketcap), 1260) + 0.5
    b = blend * back
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-debt/equity (leverage) z inverted, plus inverse-ev z (low-lever cheap)
def f38cb_f38_cycle_bottom_value_ndeinv_ev_252d_base_v118_signal(debt, cashneq, equity, evebitda):
    nde = (debt - cashneq) / equity.replace(0, np.nan)
    b = -_z(nde, 252) + _z(_f38_cheap_ev(evebitda), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tangible NAV discount (tangibles vs marketcap) acceleration, gated cheap-pb
def f38cb_f38_cycle_bottom_value_navaccel_pb_252d_base_v119_signal(tangibles, marketcap, pb):
    nav = _f38_tang_backing(tangibles, marketcap)
    accel = (nav - nav.shift(63)) - (nav.shift(63) - nav.shift(126))
    cheap = _rank(_f38_cheap_pb(pb), 252) + 0.5
    b = accel * cheap
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# excess cash coverage (above 1) momentum times inverse-pb deviation magnitude (arming-up cheap)
def f38cb_f38_cycle_bottom_value_excesscovpct_pb_504d_base_v120_signal(cashneq, debt, pb):
    excess = _f38_net_cash_ratio(cashneq, debt) - 1.0
    exmom = excess - excess.shift(63)
    cheap = _f38_cheap_pb(pb)
    dev = np.tanh(8.0 * (cheap - _mean(cheap, 252)))
    b = exmom * dev
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/EBITDA below its 504d EMA (de-trended cheap) plus net-cash/marketcap z
def f38cb_f38_cycle_bottom_value_evema_ncmc_504d_base_v121_signal(evebitda, cashneq, debt, marketcap):
    ema = evebitda.ewm(span=252, min_periods=126).mean()
    below = (ema - evebitda) / ema.replace(0, np.nan)
    ncmc = _z(_f38_net_cash(cashneq, debt) / marketcap.replace(0, np.nan), 252)
    b = below + 0.3 * ncmc
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tangibles-cover-debt minus 1 (asset surplus) times inverse-ev sign-magnitude
def f38cb_f38_cycle_bottom_value_assetsurplus_ev_base_v122_signal(tangibles, debt, evebitda):
    surplus = tangibles / debt.replace(0, np.nan) - 1.0
    cheap = _f38_cheap_ev(evebitda)
    mag = np.sign(cheap) * (cheap.abs() ** 0.5)
    b = np.tanh(surplus) * mag
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net cash ratio inflection (Δ year over year) times cheap-pb percentile
def f38cb_f38_cycle_bottom_value_covinfl_pb_252d_base_v123_signal(cashneq, debt, pb):
    cov = _f38_net_cash_ratio(cashneq, debt)
    infl = cov - cov.shift(252)
    cheap = _rank(_f38_cheap_pb(pb), 252) + 0.5
    b = infl * cheap
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV-to-tangibles inverted momentum (asset-cheapening) gated by tangibles>debt
def f38cb_f38_cycle_bottom_value_evrich_tanggate_504d_base_v124_signal(marketcap, debt, cashneq, tangibles):
    ev = _f38_ev(marketcap, debt, cashneq)
    et = ev / tangibles.replace(0, np.nan)
    inv = 1.0 / et.replace(0, np.nan)
    mom = inv - inv.shift(63)
    cover = tangibles / debt.replace(0, np.nan)
    gate = 1.0 / (1.0 + np.exp(-(cover - 1.0)))
    b = mom * gate
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# blended deep-value z (cheap pb + cheap ev) minus richness drift, x solvency gate
def f38cb_f38_cycle_bottom_value_deepvalz_gate_252d_base_v125_signal(pb, evebitda, cashneq, debt):
    dvz = (_z(_f38_cheap_pb(pb), 252) + _z(_f38_cheap_ev(evebitda), 252)) / 2.0
    gate = _f38_solv_gate(cashneq, debt)
    b = dvz * gate
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash buffer per marketcap minus tangible-backing (liquid vs fixed asset mix) x cheap-pb
def f38cb_f38_cycle_bottom_value_liqfixmix_pb_base_v126_signal(cashneq, debt, marketcap, tangibles, pb):
    liq = _f38_net_cash(cashneq, debt) / marketcap.replace(0, np.nan)
    fix = _f38_tang_backing(tangibles, marketcap)
    mix = _z(liq, 252) - _z(fix, 252)
    cheap = _rank(_f38_cheap_pb(pb), 252) + 0.5
    b = mix * cheap
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# how far inverse-ev percentile above inverse-pb percentile (which multiple cheaper), gated cash
def f38cb_f38_cycle_bottom_value_evvspbpct_gate_1260d_base_v127_signal(evebitda, pb, cashneq, debt):
    spr = _rank(_f38_cheap_ev(evebitda), 1260) - _rank(_f38_cheap_pb(pb), 1260)
    gate = _f38_solv_gate(cashneq, debt)
    b = spr * gate
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tangible coverage of net debt (assets vs net obligations) x inverse-pb deviation
def f38cb_f38_cycle_bottom_value_tangnetdebt_pb_base_v128_signal(tangibles, debt, cashneq, pb):
    nd = (debt - cashneq).clip(lower=1.0)
    cover = tangibles / nd
    cheap = _f38_cheap_pb(pb)
    dev = cheap - _mean(cheap, 252)
    b = np.tanh(cover / 5.0) * dev
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash-coverage momentum z times cheap-ev momentum z (joint improvement)
def f38cb_f38_cycle_bottom_value_covmom_evmom_252d_base_v129_signal(cashneq, debt, evebitda):
    cov = _f38_net_cash_ratio(cashneq, debt)
    cm = _z(cov - cov.shift(63), 252)
    cheap = _f38_cheap_ev(evebitda)
    em = _z(cheap - cheap.shift(63), 252)
    b = cm * em
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# graham net-net (tangibles-debt)/marketcap above 1 (deep asset value) x cash coverage
def f38cb_f38_cycle_bottom_value_grahamnet_cov_base_v130_signal(tangibles, debt, marketcap, cashneq):
    netnet = (tangibles - debt) / marketcap.replace(0, np.nan)
    cov = _f38_net_cash_ratio(cashneq, debt).clip(upper=8.0)
    b = np.tanh(netnet) * cov
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# inverse-pb 252-max (cheapest recently) minus current (mean-reversion room), gated solvency
def f38cb_f38_cycle_bottom_value_pbcheaproom_gate_252d_base_v131_signal(pb, cashneq, debt):
    cheap = _f38_cheap_pb(pb)
    room = _rmax(cheap, 252) - cheap
    gate = _f38_solv_gate(cashneq, debt)
    b = room * gate
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tangible backing z plus net-cash ratio z minus EV-richness z (three-way composite)
def f38cb_f38_cycle_bottom_value_threeway_252d_base_v132_signal(tangibles, marketcap, cashneq, debt, evebitda):
    a = _z(_f38_tang_backing(tangibles, marketcap), 252)
    s = _z(_f38_net_cash_ratio(cashneq, debt), 252)
    r = _z(evebitda, 252)
    b = (a + s - r) / 3.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash-rich fraction (cashneq/(tangibles+cash)) momentum x cheap-pb percentile
def f38cb_f38_cycle_bottom_value_cashrich_pb_base_v133_signal(cashneq, tangibles, pb):
    rich = cashneq / (tangibles + cashneq).replace(0, np.nan)
    richmom = rich - rich.shift(63)
    cheap = _rank(_f38_cheap_pb(pb), 252) + 0.5
    b = richmom * cheap
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# enterprise-value-to-tangibles trough (below 504 min-band) gated by net cash
def f38cb_f38_cycle_bottom_value_evtangfloor_gate_504d_base_v134_signal(marketcap, debt, cashneq, tangibles):
    ev = _f38_ev(marketcap, debt, cashneq)
    et = ev / tangibles.replace(0, np.nan)
    nearfloor = _rmin(et, 504) / et.replace(0, np.nan)
    gate = _f38_solv_gate(cashneq, debt)
    b = nearfloor * gate
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cheap-pb and cheap-ev both below own median streak (joint-cheap regime) x cash coverage
def f38cb_f38_cycle_bottom_value_jointcheap_cov_252d_base_v135_signal(pb, evebitda, cashneq, debt):
    pcheap = (pb < _mean(pb, 252)).astype(float)
    echeap = (evebitda < _mean(evebitda, 252)).astype(float)
    joint = (pcheap * echeap).rolling(63, min_periods=21).mean()
    cov = _f38_net_cash_ratio(cashneq, debt).clip(upper=8.0)
    b = joint * cov
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-cash yield (cash-debt)/marketcap percentile minus EV-richness percentile
def f38cb_f38_cycle_bottom_value_ncyldpct_evpct_1260d_base_v136_signal(cashneq, debt, marketcap, evebitda):
    ncyld = _rank((cashneq - debt) / marketcap.replace(0, np.nan), 1260)
    rich = _rank(evebitda, 1260)
    b = ncyld - rich
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tangibles per equity (asset intensity) z times inverse-ev z (asset-heavy cheap)
def f38cb_f38_cycle_bottom_value_tangint_evz_252d_base_v137_signal(tangibles, equity, evebitda):
    ti = _z(tangibles / equity.replace(0, np.nan), 252)
    cz = _z(_f38_cheap_ev(evebitda), 252)
    b = ti * cz
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cheap-pb momentum (getting cheaper) times cash-coverage above-1 indicator-smooth (solvent-cheap)
def f38cb_f38_cycle_bottom_value_pbdev_solvsmooth_252d_base_v138_signal(pb, cashneq, debt):
    cheap = _f38_cheap_pb(pb)
    mom = cheap - cheap.shift(63)
    solv = np.tanh((_f38_net_cash_ratio(cashneq, debt) - 1.0).ewm(span=42, min_periods=21).mean())
    b = mom * (0.5 + 0.5 * solv)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# enterprise value per equity inverted momentum (re-rating cheaper) gated by net cash
def f38cb_f38_cycle_bottom_value_eveqinvmom_gate_252d_base_v139_signal(marketcap, debt, cashneq, equity):
    ev = _f38_ev(marketcap, debt, cashneq)
    inv = equity / ev.replace(0, np.nan)
    mom = inv - inv.shift(63)
    gate = _f38_solv_gate(cashneq, debt)
    b = mom * gate
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tangible asset backing minus EV-richness, both ranked over cycle (asset-yield spread)
def f38cb_f38_cycle_bottom_value_backminusrich_1260d_base_v140_signal(tangibles, marketcap, evebitda):
    back = _rank(_f38_tang_backing(tangibles, marketcap), 1260)
    rich = _rank(evebitda, 1260)
    b = back - rich
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net cash buffer dispersion-stability times cheap-ev (durable liquidity + cheap)
def f38cb_f38_cycle_bottom_value_ncstab_ev_252d_base_v141_signal(cashneq, debt, evebitda):
    nc = _f38_net_cash(cashneq, debt)
    stab = _mean(nc, 252) / (_std(nc, 252) + 1.0)
    cheap = _f38_cheap_ev(evebitda)
    dev = cheap - _mean(cheap, 252)
    b = np.tanh(stab / 1e7) * dev
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# blended cheapness rank x (1 - distress) where distress=(debt-cash)/(debt+cash)
def f38cb_f38_cycle_bottom_value_blendrank_solv_252d_base_v142_signal(pb, evebitda, cashneq, debt):
    blend = 0.5 * _rank(_f38_cheap_pb(pb), 252) + 0.5 * _rank(_f38_cheap_ev(evebitda), 252) + 0.5
    distress = ((debt - cashneq) / (debt.abs() + cashneq.abs() + 1.0)).clip(lower=0)
    b = blend * (1.0 - np.tanh(distress))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tangibles+cash-debt (net-net) z trend (improving floor) x cheap-pb
def f38cb_f38_cycle_bottom_value_netnetztrend_pb_252d_base_v143_signal(tangibles, cashneq, debt, marketcap, pb):
    floor = (tangibles + cashneq - debt) / marketcap.replace(0, np.nan)
    fz = _z(floor, 252)
    trend = fz - fz.shift(63)
    cheap = _rank(_f38_cheap_pb(pb), 252) + 0.5
    b = trend * cheap
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# inverse-ev momentum x cash-coverage rank x tangible-backing (full composite product)
def f38cb_f38_cycle_bottom_value_fullcomp_252d_base_v144_signal(evebitda, cashneq, debt, tangibles, marketcap):
    cheap = _f38_cheap_ev(evebitda)
    mom = np.tanh(20.0 * (cheap - cheap.shift(63)))
    cov = _rank(_f38_net_cash_ratio(cashneq, debt), 252) + 0.5
    back = np.tanh(_f38_tang_backing(tangibles, marketcap))
    b = mom * cov * back
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# equity-to-marketcap (book yield) minus pb-implied (consistency check) gated by cash
def f38cb_f38_cycle_bottom_value_bookconsist_gate_252d_base_v145_signal(equity, marketcap, pb, cashneq, debt):
    byld = equity / marketcap.replace(0, np.nan)
    pbimplied = _f38_cheap_pb(pb)
    consist = _z(byld, 252) - _z(pbimplied, 252)
    gate = _f38_solv_gate(cashneq, debt)
    b = consist * gate
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash coverage drawdown from 1260 max (liquidity deterioration) x cheap-pb (cheap-but-deteriorating)
def f38cb_f38_cycle_bottom_value_covdd_pb_1260d_base_v146_signal(cashneq, debt, pb):
    cov = _f38_net_cash_ratio(cashneq, debt)
    dd = cov / _rmax(cov, 1260).replace(0, np.nan) - 1.0
    cheap = _rank(_f38_cheap_pb(pb), 252) + 0.5
    b = dd * cheap
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tangible backing percentile x net-cash percentile x inverse-pb percentile (triple rank product)
def f38cb_f38_cycle_bottom_value_triplepct_1260d_base_v147_signal(tangibles, marketcap, cashneq, debt, pb):
    t = _rank(_f38_tang_backing(tangibles, marketcap), 1260) + 0.5
    s = _rank(_f38_net_cash(cashneq, debt), 1260) + 0.5
    p = _rank(_f38_cheap_pb(pb), 1260) + 0.5
    b = t * s * p
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# enterprise multiple z below zero count (cheap quarters) x cash coverage deviation
def f38cb_f38_cycle_bottom_value_evcheapcount_cov_504d_base_v148_signal(evebitda, cashneq, debt):
    cheapz = _z(_f38_cheap_ev(evebitda), 252)
    count = (cheapz > 0).astype(float).rolling(126, min_periods=63).mean()
    cov = _f38_net_cash_ratio(cashneq, debt)
    covdev = cov - _mean(cov, 252)
    b = count * np.tanh(covdev)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# combined cheap+solvent+asset score, EMA-smoothed (persistent cycle-bottom signal)
def f38cb_f38_cycle_bottom_value_persistscore_252d_base_v149_signal(pb, evebitda, cashneq, debt, tangibles, marketcap):
    a = _z(_f38_cheap_pb(pb), 252)
    c = _z(_f38_cheap_ev(evebitda), 252)
    s = _z(_f38_net_cash_ratio(cashneq, debt), 252)
    t = _z(_f38_tang_backing(tangibles, marketcap), 252)
    score = (a + c + s + t) / 4.0
    b = score.ewm(span=63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# final cycle-bottom composite: blended-cheapness rank gated by survival sigmoid x asset floor
def f38cb_f38_cycle_bottom_value_finalcompo_1260d_base_v150_signal(pb, evebitda, cashneq, debt, tangibles, marketcap):
    blend = 0.5 * _rank(_f38_cheap_pb(pb), 1260) + 0.5 * _rank(_f38_cheap_ev(evebitda), 1260) + 0.5
    gate = _f38_solv_gate(cashneq, debt)
    floor = np.tanh((tangibles - debt) / marketcap.replace(0, np.nan))
    b = blend * gate * (0.5 + 0.5 * floor)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f38cb_f38_cycle_bottom_value_pbdev_tangcov_504d_base_v076_signal,
    f38cb_f38_cycle_bottom_value_ncevpct_pbpct_1260d_base_v077_signal,
    f38cb_f38_cycle_bottom_value_intdrag_ev_base_v078_signal,
    f38cb_f38_cycle_bottom_value_blendz_ncsign_252d_base_v079_signal,
    f38cb_f38_cycle_bottom_value_covema_pb_252d_base_v080_signal,
    f38cb_f38_cycle_bottom_value_tangfloorgrow_gate_252d_base_v081_signal,
    f38cb_f38_cycle_bottom_value_evabovemed_covrank_252d_base_v082_signal,
    f38cb_f38_cycle_bottom_value_evtanginv_cov_504d_base_v083_signal,
    f38cb_f38_cycle_bottom_value_pbpctspr_gate_base_v084_signal,
    f38cb_f38_cycle_bottom_value_liqtang_ev_252d_base_v085_signal,
    f38cb_f38_cycle_bottom_value_eqdebtgrow_pb_252d_base_v086_signal,
    f38cb_f38_cycle_bottom_value_minsolv_back_252d_base_v087_signal,
    f38cb_f38_cycle_bottom_value_netnetmom_pb_252d_base_v088_signal,
    f38cb_f38_cycle_bottom_value_pbdisp_covdev_252d_base_v089_signal,
    f38cb_f38_cycle_bottom_value_tangcovrank_evrank_1260d_base_v090_signal,
    f38cb_f38_cycle_bottom_value_excessnc_pbsign_252d_base_v091_signal,
    f38cb_f38_cycle_bottom_value_evdeepfrac_eqdebt_1260d_base_v092_signal,
    f38cb_f38_cycle_bottom_value_backaccel_ev_252d_base_v093_signal,
    f38cb_f38_cycle_bottom_value_gatepersist_ev_252d_base_v094_signal,
    f38cb_f38_cycle_bottom_value_ncyld_pbmag_base_v095_signal,
    f38cb_f38_cycle_bottom_value_eveqpct_covpct_1260d_base_v096_signal,
    f38cb_f38_cycle_bottom_value_geoz_backz_252d_base_v097_signal,
    f38cb_f38_cycle_bottom_value_delev_ev_252d_base_v098_signal,
    f38cb_f38_cycle_bottom_value_navgappct_cov_504d_base_v099_signal,
    f38cb_f38_cycle_bottom_value_pbzinfl_gate_252d_base_v100_signal,
    f38cb_f38_cycle_bottom_value_warchesteq_ev_1260d_base_v101_signal,
    f38cb_f38_cycle_bottom_value_tangevyld_spr_1260d_base_v102_signal,
    f38cb_f38_cycle_bottom_value_covstab_pb_252d_base_v103_signal,
    f38cb_f38_cycle_bottom_value_minpillar_1260d_base_v104_signal,
    f38cb_f38_cycle_bottom_value_evdd_gate_1260d_base_v105_signal,
    f38cb_f38_cycle_bottom_value_tangcovz_pbz_252d_base_v106_signal,
    f38cb_f38_cycle_bottom_value_evcheapstreak_cov_252d_base_v107_signal,
    f38cb_f38_cycle_bottom_value_ncev_pb_div_504d_base_v108_signal,
    f38cb_f38_cycle_bottom_value_tangshare_ev_252d_base_v109_signal,
    f38cb_f38_cycle_bottom_value_evcov_tanh_252d_base_v110_signal,
    f38cb_f38_cycle_bottom_value_mctanginv_gate_252d_base_v111_signal,
    f38cb_f38_cycle_bottom_value_covmin_pb_252d_base_v112_signal,
    f38cb_f38_cycle_bottom_value_multiplespr_gate_base_v113_signal,
    f38cb_f38_cycle_bottom_value_ncrepair_pb_252d_base_v114_signal,
    f38cb_f38_cycle_bottom_value_survfloor_ev_252d_base_v115_signal,
    f38cb_f38_cycle_bottom_value_byld_cov_revert_252d_base_v116_signal,
    f38cb_f38_cycle_bottom_value_blendpct_back_1260d_base_v117_signal,
    f38cb_f38_cycle_bottom_value_ndeinv_ev_252d_base_v118_signal,
    f38cb_f38_cycle_bottom_value_navaccel_pb_252d_base_v119_signal,
    f38cb_f38_cycle_bottom_value_excesscovpct_pb_504d_base_v120_signal,
    f38cb_f38_cycle_bottom_value_evema_ncmc_504d_base_v121_signal,
    f38cb_f38_cycle_bottom_value_assetsurplus_ev_base_v122_signal,
    f38cb_f38_cycle_bottom_value_covinfl_pb_252d_base_v123_signal,
    f38cb_f38_cycle_bottom_value_evrich_tanggate_504d_base_v124_signal,
    f38cb_f38_cycle_bottom_value_deepvalz_gate_252d_base_v125_signal,
    f38cb_f38_cycle_bottom_value_liqfixmix_pb_base_v126_signal,
    f38cb_f38_cycle_bottom_value_evvspbpct_gate_1260d_base_v127_signal,
    f38cb_f38_cycle_bottom_value_tangnetdebt_pb_base_v128_signal,
    f38cb_f38_cycle_bottom_value_covmom_evmom_252d_base_v129_signal,
    f38cb_f38_cycle_bottom_value_grahamnet_cov_base_v130_signal,
    f38cb_f38_cycle_bottom_value_pbcheaproom_gate_252d_base_v131_signal,
    f38cb_f38_cycle_bottom_value_threeway_252d_base_v132_signal,
    f38cb_f38_cycle_bottom_value_cashrich_pb_base_v133_signal,
    f38cb_f38_cycle_bottom_value_evtangfloor_gate_504d_base_v134_signal,
    f38cb_f38_cycle_bottom_value_jointcheap_cov_252d_base_v135_signal,
    f38cb_f38_cycle_bottom_value_ncyldpct_evpct_1260d_base_v136_signal,
    f38cb_f38_cycle_bottom_value_tangint_evz_252d_base_v137_signal,
    f38cb_f38_cycle_bottom_value_pbdev_solvsmooth_252d_base_v138_signal,
    f38cb_f38_cycle_bottom_value_eveqinvmom_gate_252d_base_v139_signal,
    f38cb_f38_cycle_bottom_value_backminusrich_1260d_base_v140_signal,
    f38cb_f38_cycle_bottom_value_ncstab_ev_252d_base_v141_signal,
    f38cb_f38_cycle_bottom_value_blendrank_solv_252d_base_v142_signal,
    f38cb_f38_cycle_bottom_value_netnetztrend_pb_252d_base_v143_signal,
    f38cb_f38_cycle_bottom_value_fullcomp_252d_base_v144_signal,
    f38cb_f38_cycle_bottom_value_bookconsist_gate_252d_base_v145_signal,
    f38cb_f38_cycle_bottom_value_covdd_pb_1260d_base_v146_signal,
    f38cb_f38_cycle_bottom_value_triplepct_1260d_base_v147_signal,
    f38cb_f38_cycle_bottom_value_evcheapcount_cov_504d_base_v148_signal,
    f38cb_f38_cycle_bottom_value_persistscore_252d_base_v149_signal,
    f38cb_f38_cycle_bottom_value_finalcompo_1260d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F38_CYCLE_BOTTOM_VALUE_REGISTRY_076_150 = REGISTRY


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

    print("OK f38_cycle_bottom_value_base_076_150_claude: %d features pass" % n_features)
