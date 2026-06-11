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
    return s.rolling(w, min_periods=max(1, w // 2)).rank(pct=True) - 0.5


# ===== folder domain primitives (valuation-vs-cycle) =====
def _f43_growth(s, w):
    return np.log(s.replace(0, np.nan) / s.shift(w).replace(0, np.nan))


def _f43_peg(mult, growth):
    g = (growth * 100.0)
    return mult / g.replace(0, np.nan)


def _f43_rangepos(s, w):
    hi = _rmax(s, w)
    lo = _rmin(s, w)
    return (s - lo) / (hi - lo).replace(0, np.nan)


def _f43_implied_evebitda(ev, ebitda):
    return ev / ebitda.replace(0, np.nan)


def _f43_implied_evsales(ev, revenue):
    return ev / revenue.replace(0, np.nan)


def _f43_margin(ebitda, revenue):
    return ebitda / revenue.replace(0, np.nan)


# ============================================================
# EV/EBITDA gap from 63d-ago level scaled by EBITDA-growth (re-rate vs short cycle)
def f43vc_f43_valuation_vs_cycle_evebitdashortgap_63d_base_v076_signal(evebitda, ebitda):
    vg = np.log(evebitda.replace(0, np.nan) / evebitda.shift(63).replace(0, np.nan))
    eg = _f43_growth(ebitda, 63)
    b = vg - eg
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/Sales percentile within 1260d range (where in cycle the multiple sits)
def f43vc_f43_valuation_vs_cycle_evsalesrng_1260d_base_v077_signal(ev, revenue):
    evs = _f43_implied_evsales(ev, revenue)
    b = _f43_rangepos(evs, 1260) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# P/B-to-revenue-growth (log discount form)
def f43vc_f43_valuation_vs_cycle_pbrevgap_252d_base_v078_signal(pb, revenue):
    g = _f43_growth(revenue, 252)
    b = np.log(pb.replace(0, np.nan)) - g.clip(-1.0, 1.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/EBITDA z conditioned on revenue acceleration (rich-while-accelerating)
def f43vc_f43_valuation_vs_cycle_richaccel_252d_base_v079_signal(evebitda, revenue):
    vz = _z(evebitda, 252)
    accel = _f43_growth(revenue, 63) - _f43_growth(revenue, 126)
    b = vz * np.sign(accel)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# marketcap/EBITDA gap from its 504d mean (equity multiple cycle deviation)
def f43vc_f43_valuation_vs_cycle_mcapebgap_504d_base_v080_signal(marketcap, ebitda):
    mult = marketcap / ebitda.replace(0, np.nan)
    m = _mean(mult, 504)
    b = (mult - m) / m.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/EBITDA-to-growth using 504d growth (long-cycle PEG)
def f43vc_f43_valuation_vs_cycle_longpeg_504d_base_v081_signal(evebitda, ebitda):
    g = _f43_growth(ebitda, 504)
    peg = _f43_peg(evebitda, g)
    b = _z(peg, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue cycle phase minus EV/Sales cycle phase (cheap-vs-cycle rangepos gap)
def f43vc_f43_valuation_vs_cycle_phasegap_504d_base_v082_signal(ev, revenue):
    evs = _f43_implied_evsales(ev, revenue)
    cp = _f43_rangepos(revenue, 504)
    vp = _f43_rangepos(evs, 504)
    b = cp - vp
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/EBITDA mean-reversion half-life proxy: gap autocorr over 21d
def f43vc_f43_valuation_vs_cycle_mrpersist_252d_base_v083_signal(evebitda):
    gap = evebitda - _mean(evebitda, 252)
    b = gap * gap.shift(21) / (_std(gap, 252) ** 2).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# P/B vs EBITDA-margin cycle: asset multiple z minus margin z (book vs profitability)
def f43vc_f43_valuation_vs_cycle_pbmargin_252d_base_v084_signal(pb, ebitda, revenue):
    margin = _f43_margin(ebitda, revenue)
    b = _z(pb, 252) - _z(margin, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/EBITDA distance above 252d mean per unit of revenue growth (cost-of-growth)
def f43vc_f43_valuation_vs_cycle_costofgrowth_252d_base_v085_signal(evebitda, revenue):
    gap = (evebitda - _mean(evebitda, 252)) / _mean(evebitda, 252).replace(0, np.nan)
    g = _f43_growth(revenue, 252).abs() + 0.05
    b = gap / g
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# marketcap/revenue z vs revenue cycle position interaction
def f43vc_f43_valuation_vs_cycle_psphase_252d_base_v086_signal(marketcap, revenue):
    ps = marketcap / revenue.replace(0, np.nan)
    psz = _z(ps, 252)
    phase = _f43_rangepos(revenue, 252) - 0.5
    b = psz + phase
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/EBITDA rich-regime entries over 252d (count of crossing above +1 sigma)
def f43vc_f43_valuation_vs_cycle_richentries_252d_base_v087_signal(evebitda):
    z = _z(evebitda, 252)
    rich = (z > 1.0).astype(float)
    entries = ((rich == 1) & (rich.shift(1) == 0)).astype(float)
    b = entries.rolling(252, min_periods=126).sum() + z.clip(lower=0).rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/Sales cheap-regime time over 252d (fraction below 252d median)
def f43vc_f43_valuation_vs_cycle_evscheaptime_252d_base_v088_signal(ev, revenue):
    evs = _f43_implied_evsales(ev, revenue)
    med = evs.rolling(252, min_periods=126).median()
    below = (evs < med).astype(float)
    b = below.rolling(252, min_periods=126).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# implied EV/EBITDA vs P/B spread (enterprise vs equity-book valuation tension)
def f43vc_f43_valuation_vs_cycle_evbookspr_252d_base_v089_signal(ev, ebitda, pb):
    eve = _f43_implied_evebitda(ev, ebitda)
    b = _z(eve, 252) - _z(pb, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/EBITDA-to-EBITDA-momentum elasticity over half cycle
def f43vc_f43_valuation_vs_cycle_elastlong_126d_base_v090_signal(evebitda, ebitda):
    dm = _f43_growth(evebitda, 126)
    dg = _f43_growth(ebitda, 126)
    b = dm / (dg.abs() + 0.05)
    b = _rank(b, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth-adjusted EV/EBITDA: multiple minus 10x revenue growth (fair-multiple gap)
def f43vc_f43_valuation_vs_cycle_gadjeve_252d_base_v091_signal(evebitda, revenue):
    g = _f43_growth(revenue, 252)
    b = evebitda - 10.0 * g
    b = _z(b, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/EBITDA vs its 1260d trough multiple, log scale (re-rating off cycle low)
def f43vc_f43_valuation_vs_cycle_offlow_1260d_base_v092_signal(evebitda):
    lo = _rmin(evebitda, 1260)
    b = np.log(evebitda.replace(0, np.nan) / lo.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# P/B vs 1260d trough (book multiple re-rating off cycle low)
def f43vc_f43_valuation_vs_cycle_pbofflow_1260d_base_v093_signal(pb):
    lo = _rmin(pb, 1260)
    b = np.log(pb.replace(0, np.nan) / lo.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# multiple re-rating divergence: EV/EBITDA momentum minus P/B momentum
def f43vc_f43_valuation_vs_cycle_reratediv_63d_base_v094_signal(evebitda, pb):
    me = _f43_growth(evebitda, 63)
    mp = _f43_growth(pb, 63)
    b = me - mp
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# valuation z minus cycle-phase z (EV/EBITDA rich vs EBITDA cycle position)
def f43vc_f43_valuation_vs_cycle_valcyclez_252d_base_v095_signal(evebitda, ebitda):
    vz = _z(evebitda, 252)
    cz = _z(_f43_rangepos(ebitda, 252), 252)
    b = vz - cz
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/Sales-to-growth change over a quarter (PEG trend)
def f43vc_f43_valuation_vs_cycle_evspegchg_252d_base_v096_signal(ev, revenue):
    evs = _f43_implied_evsales(ev, revenue)
    g = _f43_growth(revenue, 252)
    peg = _f43_peg(evs, g)
    b = peg - peg.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# blended multiple (avg of EV/EBITDA z & EV/Sales z) detrended (composite re-rating)
def f43vc_f43_valuation_vs_cycle_blendmult_252d_base_v097_signal(evebitda, ev, revenue):
    evs = _f43_implied_evsales(ev, revenue)
    b = 0.5 * _z(evebitda, 252) + 0.5 * _z(evs, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue growth z minus EV growth z (top-line outrunning enterprise value)
def f43vc_f43_valuation_vs_cycle_revoutrun_252d_base_v098_signal(revenue, ev):
    rz = _z(_f43_growth(revenue, 126), 252)
    ez = _z(_f43_growth(ev, 126), 252)
    b = rz - ez
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/EBITDA cheap rank gated by positive margin trend (cheap & improving)
def f43vc_f43_valuation_vs_cycle_cheapimprove_504d_base_v099_signal(evebitda, ebitda, revenue):
    cheap = -_rank(evebitda, 504)
    margin = _f43_margin(ebitda, revenue)
    mt = np.sign(margin - _mean(margin, 252))
    b = cheap * mt
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# distance of EV/EBITDA from its growth-implied band midpoint (residual richness)
def f43vc_f43_valuation_vs_cycle_bandresid_252d_base_v100_signal(evebitda, revenue):
    cyclepos = _f43_rangepos(revenue, 252)
    lo = _rmin(evebitda, 252)
    hi = _rmax(evebitda, 252)
    fair = lo + (hi - lo) * cyclepos
    b = (evebitda - fair) / (hi - lo).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/EBITDA acceleration: 2nd difference normalized (re-rating curvature)
def f43vc_f43_valuation_vs_cycle_multcurv_63d_base_v101_signal(evebitda):
    le = np.log(evebitda.replace(0, np.nan))
    b = le - 2.0 * le.shift(63) + le.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# marketcap/revenue rank minus revenue-growth rank (price-vs-growth percentile gap)
def f43vc_f43_valuation_vs_cycle_psrankgap_504d_base_v102_signal(marketcap, revenue):
    ps = marketcap / revenue.replace(0, np.nan)
    pr = _rank(ps, 504)
    gr = _rank(_f43_growth(revenue, 252), 504)
    b = pr - gr
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/EBITDA-to-EBITDA-margin: multiple per unit of margin (quality-adj valuation)
def f43vc_f43_valuation_vs_cycle_multpermargin_252d_base_v103_signal(evebitda, ebitda, revenue):
    margin = _f43_margin(ebitda, revenue)
    b = evebitda * margin
    b = _z(b, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/EBITDA vs EV/Sales convergence speed (margin-cycle re-rating velocity)
def f43vc_f43_valuation_vs_cycle_convspeed_252d_base_v104_signal(ev, ebitda, revenue):
    eve = _f43_implied_evebitda(ev, ebitda)
    evs = _f43_implied_evsales(ev, revenue)
    spread = np.log(eve.replace(0, np.nan)) - np.log(evs.replace(0, np.nan))
    b = spread - spread.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/EBITDA cheap relative to where revenue is in 1260d cycle (deep cheap-late)
def f43vc_f43_valuation_vs_cycle_deepcheaplate_1260d_base_v105_signal(evebitda, revenue):
    cheap = -_z(evebitda, 504)
    late = _f43_rangepos(revenue, 1260)
    b = cheap * late
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# valuation z change YoY (how the cheapness regime shifted over a year)
def f43vc_f43_valuation_vs_cycle_valzyoy_252d_base_v106_signal(evebitda):
    vz = _z(evebitda, 252)
    b = vz - vz.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/EBITDA per revenue cycle position, ranked (multiple cost across cycle)
def f43vc_f43_valuation_vs_cycle_multcostrank_504d_base_v107_signal(evebitda, revenue):
    phase = _f43_rangepos(revenue, 252) + 0.1
    cost = evebitda / phase.replace(0, np.nan)
    b = _rank(cost, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# P/B cheap rank gated by EBITDA up-cycle (cheap-asset & earnings-rising)
def f43vc_f43_valuation_vs_cycle_pbcheapup_504d_base_v108_signal(pb, ebitda):
    cheap = -_rank(pb, 504)
    up = (ebitda > _mean(ebitda, 252)).astype(float)
    b = cheap * (0.5 + up)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/EBITDA dispersion-scaled mean-reversion gap (gap per unit of recent vol)
def f43vc_f43_valuation_vs_cycle_volscaledgap_252d_base_v109_signal(evebitda):
    gap = evebitda - _mean(evebitda, 252)
    vol = _std(evebitda.diff(), 63)
    b = gap / vol.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/Sales vs revenue-cycle z interaction (cheap-but-late composite)
def f43vc_f43_valuation_vs_cycle_evslatecomp_252d_base_v110_signal(ev, revenue):
    evs = _f43_implied_evsales(ev, revenue)
    cheap = -_z(evs, 252)
    late = _z(_f43_rangepos(revenue, 252), 252)
    b = cheap + 0.5 * late
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# multiple expansion vs revenue expansion ratio (how much re-rate per growth)
def f43vc_f43_valuation_vs_cycle_reratepergrowth_252d_base_v111_signal(evebitda, revenue):
    dm = _f43_growth(evebitda, 252)
    dr = _f43_growth(revenue, 252)
    b = dm / (dr.abs() + 0.05) * np.sign(dr)
    b = _z(b, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/EBITDA gap from mid-cycle vs P/B gap from mid-cycle (which multiple stretched)
def f43vc_f43_valuation_vs_cycle_midstretch_504d_base_v112_signal(evebitda, pb):
    eg = (evebitda - _mean(evebitda, 504)) / _mean(evebitda, 504).replace(0, np.nan)
    pg = (pb - _mean(pb, 504)) / _mean(pb, 504).replace(0, np.nan)
    b = eg - pg
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue-growth-weighted EV/Sales cheapness rank (cheap-per-growth)
def f43vc_f43_valuation_vs_cycle_gwcheap_504d_base_v113_signal(ev, revenue):
    evs = _f43_implied_evsales(ev, revenue)
    g = _f43_growth(revenue, 252)
    cheap = -_rank(evs, 504)
    b = cheap * (1.0 + np.tanh(5.0 * g))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/EBITDA above-mean streak length (persistence of rich regime)
def f43vc_f43_valuation_vs_cycle_richstreak_252d_base_v114_signal(evebitda):
    rich = (evebitda > _mean(evebitda, 252)).astype(float)
    grp = (rich != rich.shift(1)).cumsum()
    streak = rich.groupby(grp).cumsum()
    b = streak * np.sign(rich - 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/Sales below-mean streak length (persistence of cheap regime)
def f43vc_f43_valuation_vs_cycle_cheapstreak_252d_base_v115_signal(ev, revenue):
    evs = _f43_implied_evsales(ev, revenue)
    cheap = (evs < _mean(evs, 252)).astype(float)
    grp = (cheap != cheap.shift(1)).cumsum()
    streak = cheap.groupby(grp).cumsum()
    b = streak
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/EBITDA-to-growth where growth is EBITDA half-cycle, ranked
def f43vc_f43_valuation_vs_cycle_pegrankhalf_504d_base_v116_signal(evebitda, ebitda):
    g = _f43_growth(ebitda, 126)
    peg = _f43_peg(evebitda, g)
    b = _rank(peg, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# marketcap growth minus EBITDA growth (equity re-rating vs earnings cycle)
def f43vc_f43_valuation_vs_cycle_mcapebrerate_252d_base_v117_signal(marketcap, ebitda):
    gm = _f43_growth(marketcap, 252)
    ge = _f43_growth(ebitda, 252)
    b = gm - ge
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/EBITDA distance from 252d mean, tanh-bounded and growth-signed
def f43vc_f43_valuation_vs_cycle_signedgap_252d_base_v118_signal(evebitda, revenue):
    gap = (evebitda - _mean(evebitda, 252)) / _std(evebitda, 252).replace(0, np.nan)
    g = np.sign(_f43_growth(revenue, 126))
    b = np.tanh(gap) * g
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/Sales 63d vs 252d ratio (short-term re-rating vs cycle baseline)
def f43vc_f43_valuation_vs_cycle_evsfastslow_252d_base_v119_signal(ev, revenue):
    evs = _f43_implied_evsales(ev, revenue)
    b = _mean(evs, 63) / _mean(evs, 252).replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# P/B 63d vs 252d ratio (book multiple short-cycle drift)
def f43vc_f43_valuation_vs_cycle_pbfastslow_252d_base_v120_signal(pb):
    b = _mean(pb, 63) / _mean(pb, 252).replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/EBITDA cheapness minus margin-cycle position (cheap-vs-profit-cycle)
def f43vc_f43_valuation_vs_cycle_cheapvsmargin_252d_base_v121_signal(evebitda, ebitda, revenue):
    cheap = -_z(evebitda, 252)
    margin = _f43_margin(ebitda, revenue)
    mp = _z(_f43_rangepos(margin, 252), 252)
    b = cheap - mp
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# valuation overshoot probability proxy: fraction of 63d EV/EBITDA above +1.5 sigma
def f43vc_f43_valuation_vs_cycle_overprob_252d_base_v122_signal(evebitda):
    z = _z(evebitda, 252)
    hot = (z > 1.5).astype(float)
    b = hot.rolling(63, min_periods=21).mean() + 0.05 * z
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/EBITDA mean-reversion gap signed and square-root compressed
def f43vc_f43_valuation_vs_cycle_sqrtgap_504d_base_v123_signal(evebitda):
    z = _z(evebitda, 504)
    b = np.sign(z) * (z.abs() ** 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/Sales-to-growth dispersion: std of PEG over 252d (valuation-growth instability)
def f43vc_f43_valuation_vs_cycle_pegdisp_252d_base_v124_signal(ev, revenue):
    evs = _f43_implied_evsales(ev, revenue)
    g = _f43_growth(revenue, 252)
    peg = _f43_peg(evs, g)
    b = _std(peg, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/EBITDA cheapness conditioned on EBITDA 1260d trough proximity (deep value)
def f43vc_f43_valuation_vs_cycle_troughval_1260d_base_v125_signal(evebitda, ebitda):
    cheap = -_z(evebitda, 252)
    troughprox = (1.0 - _f43_rangepos(ebitda, 1260))
    b = cheap * troughprox
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# multiple-vs-growth correlation proxy: product of z(mult) and z(growth) over 252d
def f43vc_f43_valuation_vs_cycle_valgrowthcoup_252d_base_v126_signal(evebitda, ebitda):
    vz = _z(evebitda, 252)
    gz = _z(_f43_growth(ebitda, 126), 252)
    b = (vz * gz).rolling(126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/EBITDA cheapness-rank scaled by EBITDA margin level (quality-adj cheapness)
def f43vc_f43_valuation_vs_cycle_qadjgap_504d_base_v127_signal(evebitda, ebitda, revenue):
    cheaprank = -_rank(evebitda, 504)
    margin = _f43_margin(ebitda, revenue)
    mrank = _rank(margin, 504) + 0.5
    b = cheaprank * (0.5 + mrank)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# marketcap/EBITDA cycle-phase velocity (change in 1260d rangepos over a quarter)
def f43vc_f43_valuation_vs_cycle_mcapebrng_1260d_base_v128_signal(marketcap, ebitda):
    mult = marketcap / ebitda.replace(0, np.nan)
    rp = _f43_rangepos(mult, 1260)
    b = rp - rp.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/EBITDA gap minus EV/Sales gap from respective means (multiple disagreement)
def f43vc_f43_valuation_vs_cycle_multdisagree_252d_base_v129_signal(ev, ebitda, revenue):
    eve = _f43_implied_evebitda(ev, ebitda)
    evs = _f43_implied_evsales(ev, revenue)
    ge = (eve - _mean(eve, 252)) / _mean(eve, 252).replace(0, np.nan)
    gs = (evs - _mean(evs, 252)) / _mean(evs, 252).replace(0, np.nan)
    b = ge - gs
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/EBITDA re-rating consistency: fraction of last quarter multiple rose
def f43vc_f43_valuation_vs_cycle_reratecons_252d_base_v130_signal(evebitda):
    up = (evebitda.diff() > 0).astype(float)
    b = up.rolling(63, min_periods=21).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cheap-and-growing composite: low EV/EBITDA z plus high EBITDA growth z
def f43vc_f43_valuation_vs_cycle_cheapgrowcomp_252d_base_v131_signal(evebitda, ebitda):
    cheap = -_z(evebitda, 252)
    grow = _z(_f43_growth(ebitda, 252), 252)
    b = 0.6 * cheap + 0.4 * grow
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/EBITDA peak-to-current de-rating fraction over 252d (cyclical compression)
def f43vc_f43_valuation_vs_cycle_derate_252d_base_v132_signal(evebitda):
    hi = _rmax(evebitda, 252)
    b = (hi - evebitda) / hi.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/Sales trough-to-current re-rating fraction over 252d (cyclical expansion)
def f43vc_f43_valuation_vs_cycle_evsexpand_252d_base_v133_signal(ev, revenue):
    evs = _f43_implied_evsales(ev, revenue)
    lo = _rmin(evs, 252)
    b = (evs - lo) / lo.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# valuation-vs-cycle composite: EV/EBITDA z minus average of cycle-phase ranks
def f43vc_f43_valuation_vs_cycle_compositephase_252d_base_v134_signal(evebitda, revenue, ebitda):
    vz = _z(evebitda, 252)
    phase = 0.5 * _f43_rangepos(revenue, 252) + 0.5 * _f43_rangepos(ebitda, 252)
    b = vz - _z(phase, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/EBITDA growth-adjusted z, where adjustment is revenue cycle phase
def f43vc_f43_valuation_vs_cycle_phaseadjz_252d_base_v135_signal(evebitda, revenue):
    vz = _z(evebitda, 252)
    phase = _f43_rangepos(revenue, 504)
    b = vz / (0.5 + phase)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/EBITDA acceleration vs EBITDA acceleration (2nd-order re-rating divergence)
def f43vc_f43_valuation_vs_cycle_accelgap_126d_base_v136_signal(evebitda, ebitda):
    am = _f43_growth(evebitda, 63) - _f43_growth(evebitda, 126)
    ae = _f43_growth(ebitda, 63) - _f43_growth(ebitda, 126)
    b = am - ae
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# marketcap/revenue mean-reversion gap normalized by std (price-sales cheapness)
def f43vc_f43_valuation_vs_cycle_psmrgap_504d_base_v137_signal(marketcap, revenue):
    ps = marketcap / revenue.replace(0, np.nan)
    b = (ps - _mean(ps, 504)) / _std(ps, 504).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/EBITDA below-trend depth integrated over 126d (sustained cheapness area)
def f43vc_f43_valuation_vs_cycle_cheaparea_252d_base_v138_signal(evebitda):
    z = _z(evebitda, 252)
    below = (-z).clip(lower=0)
    b = below.rolling(126, min_periods=63).sum()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/EBITDA-to-growth ratio gated by sign agreement (mult & growth same direction)
def f43vc_f43_valuation_vs_cycle_signagree_252d_base_v139_signal(evebitda, ebitda):
    dm = _f43_growth(evebitda, 63)
    dg = _f43_growth(ebitda, 63)
    agree = np.sign(dm) * np.sign(dg)
    b = agree * (dm.abs() + dg.abs())
    b = _z(b, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/Sales vs EV/EBITDA-implied-margin discrepancy (margin-cycle valuation gap)
def f43vc_f43_valuation_vs_cycle_marginvalgap_252d_base_v140_signal(ev, revenue, ebitda):
    evs = _f43_implied_evsales(ev, revenue)
    eve = _f43_implied_evebitda(ev, ebitda)
    implied_margin = evs / eve.replace(0, np.nan)
    actual_margin = _f43_margin(ebitda, revenue)
    b = (implied_margin - actual_margin)
    b = _z(b, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/EBITDA cheap relative to its own 1260d distribution, smoothed (deep-cycle value)
def f43vc_f43_valuation_vs_cycle_deeprank_1260d_base_v141_signal(evebitda):
    r = _rank(evebitda, 1260)
    b = (-r).ewm(span=42, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue growth minus marketcap growth ranked (cheapening-via-growth percentile)
def f43vc_f43_valuation_vs_cycle_cheapenrank_504d_base_v142_signal(revenue, marketcap):
    gap = _f43_growth(revenue, 252) - _f43_growth(marketcap, 252)
    b = _rank(gap, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/EBITDA z times EBITDA-cycle-phase distance from mid (rich-at-extremes)
def f43vc_f43_valuation_vs_cycle_richextreme_252d_base_v143_signal(evebitda, ebitda):
    vz = _z(evebitda, 252)
    extreme = (_f43_rangepos(ebitda, 252) - 0.5).abs()
    b = vz * extreme
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# P/B-to-EBITDA-margin: book multiple per unit margin (asset quality valuation)
def f43vc_f43_valuation_vs_cycle_pbpermargin_252d_base_v144_signal(pb, ebitda, revenue):
    margin = _f43_margin(ebitda, revenue)
    b = pb / (margin.abs() + 0.05)
    b = _z(b, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/EBITDA gap from 252d-ago value (absolute re-rating over a year)
def f43vc_f43_valuation_vs_cycle_yoymult_252d_base_v145_signal(evebitda):
    b = (evebitda - evebitda.shift(252)) / evebitda.shift(252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue-growth-conditioned EV/Sales: cheap when growing, penalized when shrinking
def f43vc_f43_valuation_vs_cycle_condevs_252d_base_v146_signal(ev, revenue):
    evs = _f43_implied_evsales(ev, revenue)
    g = _f43_growth(revenue, 252)
    cheap = -_z(evs, 252)
    b = cheap * np.where(g.values >= 0, 1.0, -1.0)
    b = pd.Series(b, index=evs.index)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/EBITDA distance above 504d median per EBITDA-growth-rank (cost-of-growth rank)
def f43vc_f43_valuation_vs_cycle_costgrowthrank_504d_base_v147_signal(evebitda, ebitda):
    med = evebitda.rolling(504, min_periods=252).median()
    gap = (evebitda - med) / med.replace(0, np.nan)
    gr = _rank(_f43_growth(ebitda, 252), 504) + 0.5 + 0.1
    b = gap / gr
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# blended cheap-vs-cycle: EV/EBITDA & P/B cheapness minus revenue & EBITDA cycle phase
def f43vc_f43_valuation_vs_cycle_fullcomposite_252d_base_v148_signal(evebitda, pb, revenue, ebitda):
    cheap = -(0.5 * _z(evebitda, 252) + 0.5 * _z(pb, 252))
    phase = 0.5 * _f43_rangepos(revenue, 252) + 0.5 * _f43_rangepos(ebitda, 252)
    b = cheap + (phase - 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/EBITDA log-multiple slope over 126d minus EBITDA log slope (half-cycle re-rate)
def f43vc_f43_valuation_vs_cycle_halfsloperr_126d_base_v149_signal(evebitda, ebitda):
    ms = np.log(evebitda.replace(0, np.nan)).diff(126)
    es = np.log(ebitda.replace(0, np.nan)).diff(126)
    b = ms - 0.5 * es
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# valuation tension velocity: change in (EV/EBITDA rangepos - revenue rangepos)
def f43vc_f43_valuation_vs_cycle_tensionvel_252d_base_v150_signal(evebitda, revenue):
    vp = _f43_rangepos(evebitda, 252)
    cp = _f43_rangepos(revenue, 252)
    tension = vp - cp
    b = tension - tension.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f43vc_f43_valuation_vs_cycle_evebitdashortgap_63d_base_v076_signal,
    f43vc_f43_valuation_vs_cycle_evsalesrng_1260d_base_v077_signal,
    f43vc_f43_valuation_vs_cycle_pbrevgap_252d_base_v078_signal,
    f43vc_f43_valuation_vs_cycle_richaccel_252d_base_v079_signal,
    f43vc_f43_valuation_vs_cycle_mcapebgap_504d_base_v080_signal,
    f43vc_f43_valuation_vs_cycle_longpeg_504d_base_v081_signal,
    f43vc_f43_valuation_vs_cycle_phasegap_504d_base_v082_signal,
    f43vc_f43_valuation_vs_cycle_mrpersist_252d_base_v083_signal,
    f43vc_f43_valuation_vs_cycle_pbmargin_252d_base_v084_signal,
    f43vc_f43_valuation_vs_cycle_costofgrowth_252d_base_v085_signal,
    f43vc_f43_valuation_vs_cycle_psphase_252d_base_v086_signal,
    f43vc_f43_valuation_vs_cycle_richentries_252d_base_v087_signal,
    f43vc_f43_valuation_vs_cycle_evscheaptime_252d_base_v088_signal,
    f43vc_f43_valuation_vs_cycle_evbookspr_252d_base_v089_signal,
    f43vc_f43_valuation_vs_cycle_elastlong_126d_base_v090_signal,
    f43vc_f43_valuation_vs_cycle_gadjeve_252d_base_v091_signal,
    f43vc_f43_valuation_vs_cycle_offlow_1260d_base_v092_signal,
    f43vc_f43_valuation_vs_cycle_pbofflow_1260d_base_v093_signal,
    f43vc_f43_valuation_vs_cycle_reratediv_63d_base_v094_signal,
    f43vc_f43_valuation_vs_cycle_valcyclez_252d_base_v095_signal,
    f43vc_f43_valuation_vs_cycle_evspegchg_252d_base_v096_signal,
    f43vc_f43_valuation_vs_cycle_blendmult_252d_base_v097_signal,
    f43vc_f43_valuation_vs_cycle_revoutrun_252d_base_v098_signal,
    f43vc_f43_valuation_vs_cycle_cheapimprove_504d_base_v099_signal,
    f43vc_f43_valuation_vs_cycle_bandresid_252d_base_v100_signal,
    f43vc_f43_valuation_vs_cycle_multcurv_63d_base_v101_signal,
    f43vc_f43_valuation_vs_cycle_psrankgap_504d_base_v102_signal,
    f43vc_f43_valuation_vs_cycle_multpermargin_252d_base_v103_signal,
    f43vc_f43_valuation_vs_cycle_convspeed_252d_base_v104_signal,
    f43vc_f43_valuation_vs_cycle_deepcheaplate_1260d_base_v105_signal,
    f43vc_f43_valuation_vs_cycle_valzyoy_252d_base_v106_signal,
    f43vc_f43_valuation_vs_cycle_multcostrank_504d_base_v107_signal,
    f43vc_f43_valuation_vs_cycle_pbcheapup_504d_base_v108_signal,
    f43vc_f43_valuation_vs_cycle_volscaledgap_252d_base_v109_signal,
    f43vc_f43_valuation_vs_cycle_evslatecomp_252d_base_v110_signal,
    f43vc_f43_valuation_vs_cycle_reratepergrowth_252d_base_v111_signal,
    f43vc_f43_valuation_vs_cycle_midstretch_504d_base_v112_signal,
    f43vc_f43_valuation_vs_cycle_gwcheap_504d_base_v113_signal,
    f43vc_f43_valuation_vs_cycle_richstreak_252d_base_v114_signal,
    f43vc_f43_valuation_vs_cycle_cheapstreak_252d_base_v115_signal,
    f43vc_f43_valuation_vs_cycle_pegrankhalf_504d_base_v116_signal,
    f43vc_f43_valuation_vs_cycle_mcapebrerate_252d_base_v117_signal,
    f43vc_f43_valuation_vs_cycle_signedgap_252d_base_v118_signal,
    f43vc_f43_valuation_vs_cycle_evsfastslow_252d_base_v119_signal,
    f43vc_f43_valuation_vs_cycle_pbfastslow_252d_base_v120_signal,
    f43vc_f43_valuation_vs_cycle_cheapvsmargin_252d_base_v121_signal,
    f43vc_f43_valuation_vs_cycle_overprob_252d_base_v122_signal,
    f43vc_f43_valuation_vs_cycle_sqrtgap_504d_base_v123_signal,
    f43vc_f43_valuation_vs_cycle_pegdisp_252d_base_v124_signal,
    f43vc_f43_valuation_vs_cycle_troughval_1260d_base_v125_signal,
    f43vc_f43_valuation_vs_cycle_valgrowthcoup_252d_base_v126_signal,
    f43vc_f43_valuation_vs_cycle_qadjgap_504d_base_v127_signal,
    f43vc_f43_valuation_vs_cycle_mcapebrng_1260d_base_v128_signal,
    f43vc_f43_valuation_vs_cycle_multdisagree_252d_base_v129_signal,
    f43vc_f43_valuation_vs_cycle_reratecons_252d_base_v130_signal,
    f43vc_f43_valuation_vs_cycle_cheapgrowcomp_252d_base_v131_signal,
    f43vc_f43_valuation_vs_cycle_derate_252d_base_v132_signal,
    f43vc_f43_valuation_vs_cycle_evsexpand_252d_base_v133_signal,
    f43vc_f43_valuation_vs_cycle_compositephase_252d_base_v134_signal,
    f43vc_f43_valuation_vs_cycle_phaseadjz_252d_base_v135_signal,
    f43vc_f43_valuation_vs_cycle_accelgap_126d_base_v136_signal,
    f43vc_f43_valuation_vs_cycle_psmrgap_504d_base_v137_signal,
    f43vc_f43_valuation_vs_cycle_cheaparea_252d_base_v138_signal,
    f43vc_f43_valuation_vs_cycle_signagree_252d_base_v139_signal,
    f43vc_f43_valuation_vs_cycle_marginvalgap_252d_base_v140_signal,
    f43vc_f43_valuation_vs_cycle_deeprank_1260d_base_v141_signal,
    f43vc_f43_valuation_vs_cycle_cheapenrank_504d_base_v142_signal,
    f43vc_f43_valuation_vs_cycle_richextreme_252d_base_v143_signal,
    f43vc_f43_valuation_vs_cycle_pbpermargin_252d_base_v144_signal,
    f43vc_f43_valuation_vs_cycle_yoymult_252d_base_v145_signal,
    f43vc_f43_valuation_vs_cycle_condevs_252d_base_v146_signal,
    f43vc_f43_valuation_vs_cycle_costgrowthrank_504d_base_v147_signal,
    f43vc_f43_valuation_vs_cycle_fullcomposite_252d_base_v148_signal,
    f43vc_f43_valuation_vs_cycle_halfsloperr_126d_base_v149_signal,
    f43vc_f43_valuation_vs_cycle_tensionvel_252d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F43_VALUATION_VS_CYCLE_REGISTRY_076_150 = REGISTRY


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

    print("OK f43_valuation_vs_cycle_base_076_150_claude: %d features pass" % n_features)
