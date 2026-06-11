import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
TRADING_DAYS_TWOYEAR = 504
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


def _rank(s, w):
    return s.rolling(w, min_periods=max(1, w // 4)).rank(pct=True) - 0.5


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


def _dlog(s, k):
    return np.log(s.replace(0, np.nan)) - np.log(s.shift(k).replace(0, np.nan))


# ===== f22 operating-leverage primitives (revenue-vs-profit GROWTH sensitivity only) =====
# NOTE: on real data opinc == gp - opex exactly; contribution-as-(revenue-opex) constructs
# collapse into incremental op margin, so they are NOT used here.  Diversification is by
# FACET (slope / yoy / ema / rank / dispersion / asymmetry / sign-mag / streak / elasticity).
def _f22ol_dol(opinc, revenue, k):
    gr = revenue.pct_change(k)
    go = opinc.pct_change(k)
    return go / gr.replace(0, np.nan)


def _f22ol_dol_ebit(ebit, revenue, k):
    gr = revenue.pct_change(k)
    ge = ebit.pct_change(k)
    return ge / gr.replace(0, np.nan)


def _f22ol_incmargin(opinc, revenue, k):
    do = opinc - opinc.shift(k)
    dr = revenue - revenue.shift(k)
    return do / dr.replace(0, np.nan)


def _f22ol_incgm(gp, revenue, k):
    dg = gp - gp.shift(k)
    dr = revenue - revenue.shift(k)
    return dg / dr.replace(0, np.nan)


def _f22ol_spread_op(opinc, revenue, k):
    return _dlog(opinc, k) - _dlog(revenue, k)


def _f22ol_spread_gp(gp, revenue, k):
    return _dlog(gp, k) - _dlog(revenue, k)


def _f22ol_spread_ebit(ebit, revenue, k):
    return _dlog(ebit, k) - _dlog(revenue, k)


def _f22ol_opexscale(opex, revenue, k):
    r = opex / revenue.replace(0, np.nan)
    return -(r - r.shift(k))


def _f22ol_gpscale(gp, revenue, k):
    r = gp / revenue.replace(0, np.nan)
    return r - r.shift(k)


def _f22ol_fixedabsorb(opinc, opex, k):
    do = opinc - opinc.shift(k)
    dx = opex - opex.shift(k)
    return do / dx.replace(0, np.nan)


def _f22ol_opexelas(opex, revenue, k):
    return _dlog(opex, k) / _dlog(revenue, k).replace(0, np.nan)


def _f22ol_gpelas(gp, revenue, k):
    return _dlog(gp, k) / _dlog(revenue, k).replace(0, np.nan)


def _f22ol_ebitelas(ebit, revenue, k):
    return _dlog(ebit, k) / _dlog(revenue, k).replace(0, np.nan)


def _f22ol_gpopxlev(gp, opex, k):
    # contribution-style lever: gross-profit growth per unit opex growth
    return _dlog(gp, k) / _dlog(opex, k).replace(0, np.nan)


def _f22ol_flowthru(gp, opinc, k):
    do = opinc - opinc.shift(k)
    dg = gp - gp.shift(k)
    return do / dg.replace(0, np.nan)


# ============================================================
# change in op spread over a quarter
def f22ol_f22_operating_leverage_spropchg_252d_base_v076_signal(opinc, revenue):
    s = _f22ol_spread_op(opinc, revenue, 252)
    b = s - s.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# change in gp spread over a quarter
def f22ol_f22_operating_leverage_sprgpchg_252d_base_v077_signal(gp, revenue):
    s = _f22ol_spread_gp(gp, revenue, 252)
    b = s - s.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# change in incremental op margin
def f22ol_f22_operating_leverage_incmopchg_252d_base_v078_signal(opinc, revenue):
    im = _f22ol_incmargin(opinc, revenue, 252)
    b = im - im.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# change in opex absorption
def f22ol_f22_operating_leverage_opxabschg_252d_base_v079_signal(opex, revenue):
    s = _f22ol_opexscale(opex, revenue, 252)
    b = s - s.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# change in fixed-cost lever
def f22ol_f22_operating_leverage_fixlevchg_252d_base_v080_signal(opinc, opex):
    s = _f22ol_fixedabsorb(opinc, opex, 252)
    b = s - s.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DOL stability mean/std (information-ratio of the lever)
def f22ol_f22_operating_leverage_dol_stab_252d_base_v081_signal(opinc, revenue):
    d = _f22ol_dol(opinc, revenue, 63)
    b = _mean(d, 252) / _std(d, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed incremental op margin
def f22ol_f22_operating_leverage_incmop_ema_126d_base_v082_signal(opinc, revenue):
    im = _f22ol_incmargin(opinc, revenue, 126)
    b = im.ewm(span=63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed gp spread
def f22ol_f22_operating_leverage_sprgp_ema_126d_base_v083_signal(gp, revenue):
    s = _f22ol_spread_gp(gp, revenue, 126)
    b = s.ewm(span=63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# change in the gp-per-opex contribution lever (cost-base leverage momentum)
def f22ol_f22_operating_leverage_gpopxlev_chg_252d_base_v084_signal(gp, opex):
    e = np.tanh(_f22ol_gpopxlev(gp, opex, 252) / 3.0)
    b = e - e.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# change in gp elasticity
def f22ol_f22_operating_leverage_gpelas_chg_252d_base_v085_signal(gp, revenue):
    e = np.tanh(_f22ol_gpelas(gp, revenue, 252) / 3.0)
    b = e - e.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# change in gross-to-operating flow-through ratio (opex-drag momentum)
def f22ol_f22_operating_leverage_flowthru_chg_252d_base_v086_signal(gp, opinc):
    f = np.tanh(_f22ol_flowthru(gp, opinc, 252) / 3.0)
    b = f - f.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# year-over-year change in op spread
def f22ol_f22_operating_leverage_sprop_yoy_252d_base_v087_signal(opinc, revenue):
    s = _f22ol_spread_op(opinc, revenue, 252)
    b = s - s.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# year-over-year change in incremental op margin
def f22ol_f22_operating_leverage_incmop_yoy_252d_base_v088_signal(opinc, revenue):
    im = _f22ol_incmargin(opinc, revenue, 252)
    b = im - im.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# year-over-year change in the gp-per-opex contribution lever
def f22ol_f22_operating_leverage_gpopxlev_yoy_252d_base_v089_signal(gp, opex):
    e = np.tanh(_f22ol_gpopxlev(gp, opex, 252) / 3.0)
    b = e - e.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# year-over-year change in DOL
def f22ol_f22_operating_leverage_dol_yoy_252d_base_v090_signal(opinc, revenue):
    d = np.tanh(_f22ol_dol(opinc, revenue, 252) / 5.0)
    b = d - d.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gp spread times revenue growth
def f22ol_f22_operating_leverage_sprXgrow_gp_252d_base_v091_signal(gp, revenue):
    s = _f22ol_spread_gp(gp, revenue, 252)
    g = _dlog(revenue, 252)
    b = s * g
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# opex absorption times revenue growth
def f22ol_f22_operating_leverage_opxabsXgrow_252d_base_v092_signal(opex, revenue):
    a = _f22ol_opexscale(opex, revenue, 252)
    g = _dlog(revenue, 252)
    b = a * g
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# change in ebit spread
def f22ol_f22_operating_leverage_sprebitchg_252d_base_v093_signal(ebit, revenue):
    s = _f22ol_spread_ebit(ebit, revenue, 252)
    b = s - s.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# bounded DOL 126d
def f22ol_f22_operating_leverage_doltanh_126d_base_v094_signal(opinc, revenue):
    d = _f22ol_dol(opinc, revenue, 126)
    b = np.tanh(d / 5.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# incremental gross margin dispersion 42/63/126
def f22ol_f22_operating_leverage_incmgp_disp_252d_base_v095_signal(gp, revenue):
    m1 = _f22ol_incgm(gp, revenue, 42)
    m2 = _f22ol_incgm(gp, revenue, 63)
    m3 = _f22ol_incgm(gp, revenue, 126)
    b = pd.concat([m1, m2, m3], axis=1).std(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# sign x sqrt-magnitude of gp spread
def f22ol_f22_operating_leverage_sprgpsignmag_252d_base_v096_signal(gp, revenue):
    s = _f22ol_spread_gp(gp, revenue, 252)
    b = np.sign(s) * (s.abs() ** 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ebit-spread net-sign streak over a year
def f22ol_f22_operating_leverage_sprebitposstreak_252d_base_v097_signal(ebit, revenue):
    s = _f22ol_spread_ebit(ebit, revenue, 63)
    b = np.sign(s).rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# incremental op margin net-sign streak over a year
def f22ol_f22_operating_leverage_incmopposstreak_252d_base_v098_signal(opinc, revenue):
    im = _f22ol_incmargin(opinc, revenue, 63)
    b = np.sign(im).rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fixed-lever net-sign streak over a year
def f22ol_f22_operating_leverage_fixlevposstreak_252d_base_v099_signal(opinc, opex):
    s = _f22ol_fixedabsorb(opinc, opex, 63)
    b = np.sign(s).rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# change in DOL over a quarter
def f22ol_f22_operating_leverage_dolop_chg_252d_base_v100_signal(opinc, revenue):
    d = np.tanh(_f22ol_dol(opinc, revenue, 252) / 5.0)
    b = d - d.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed incremental gross margin
def f22ol_f22_operating_leverage_incmgp_ema_126d_base_v101_signal(gp, revenue):
    im = _f22ol_incgm(gp, revenue, 126)
    b = im.ewm(span=63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed op spread
def f22ol_f22_operating_leverage_sprop_ema_126d_base_v102_signal(opinc, revenue):
    s = _f22ol_spread_op(opinc, revenue, 126)
    b = s.ewm(span=63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# rank of ebit elasticity 252d (cost-leverage percentile, distinct from its change)
def f22ol_f22_operating_leverage_ebitelas_rank_252d_base_v103_signal(ebit, revenue):
    e = np.tanh(_f22ol_ebitelas(ebit, revenue, 252) / 3.0)
    b = _rank(e, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# rank incremental op margin 126d
def f22ol_f22_operating_leverage_incmop_rank126_126d_base_v104_signal(opinc, revenue):
    b = _rank(_f22ol_incmargin(opinc, revenue, 126), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# rank gp spread 126d
def f22ol_f22_operating_leverage_sprgp_rank126_126d_base_v105_signal(gp, revenue):
    b = _rank(_f22ol_spread_gp(gp, revenue, 126), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# rank DOL 126d
def f22ol_f22_operating_leverage_dol_rank126_126d_base_v106_signal(opinc, revenue):
    b = _rank(_f22ol_dol(opinc, revenue, 126), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# sign x sqrt-mag of DOL excess over 1 (amplification beyond unit lever)
def f22ol_f22_operating_leverage_dolop_signmag_252d_base_v107_signal(opinc, revenue):
    d = _f22ol_dol(opinc, revenue, 252) - 1.0
    b = np.sign(d) * (d.abs() ** 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# rank op spread 126d
def f22ol_f22_operating_leverage_sprop_rank126_126d_base_v108_signal(opinc, revenue):
    b = _rank(_f22ol_spread_op(opinc, revenue, 126), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# year-over-year change in opex absorption
def f22ol_f22_operating_leverage_opxabs_yoy_252d_base_v109_signal(opex, revenue):
    s = _f22ol_opexscale(opex, revenue, 252)
    b = s - s.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# year-over-year change in gp/revenue scale
def f22ol_f22_operating_leverage_gpscl_yoy_252d_base_v110_signal(gp, revenue):
    s = _f22ol_gpscale(gp, revenue, 252)
    b = s - s.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# year-over-year change in incremental gross margin
def f22ol_f22_operating_leverage_incmgp_yoy_252d_base_v111_signal(gp, revenue):
    im = _f22ol_incgm(gp, revenue, 252)
    b = im - im.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# change in ebit-DOL over a quarter
def f22ol_f22_operating_leverage_dolebit_chg_252d_base_v112_signal(ebit, revenue):
    d = np.tanh(_f22ol_dol_ebit(ebit, revenue, 252) / 5.0)
    b = d - d.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# incremental op margin volatility 126d
def f22ol_f22_operating_leverage_incmopvol126_126d_base_v113_signal(opinc, revenue):
    im = _f22ol_incmargin(opinc, revenue, 63)
    b = im.rolling(126, min_periods=63).std()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# sign x sqrt-mag op spread 126d
def f22ol_f22_operating_leverage_sprop_signmag126_126d_base_v114_signal(opinc, revenue):
    s = _f22ol_spread_op(opinc, revenue, 126)
    b = np.sign(s) * (s.abs() ** 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# rank incremental op margin 504d
def f22ol_f22_operating_leverage_incmop_rank504_504d_base_v115_signal(opinc, revenue):
    b = _rank(_f22ol_incmargin(opinc, revenue, 504), 756)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# rank gp-per-opex contribution lever 126d
def f22ol_f22_operating_leverage_gpopxlev_rank126_126d_base_v116_signal(gp, opex):
    e = np.tanh(_f22ol_gpopxlev(gp, opex, 126) / 3.0)
    b = _rank(e, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# rank gp spread 504d
def f22ol_f22_operating_leverage_sprgp_rank504_504d_base_v117_signal(gp, revenue):
    b = _rank(_f22ol_spread_gp(gp, revenue, 504), 756)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# volatility of ebit spread
def f22ol_f22_operating_leverage_sprebitvol_252d_base_v118_signal(ebit, revenue):
    s = _f22ol_spread_ebit(ebit, revenue, 63)
    b = s.rolling(252, min_periods=126).std()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# incremental gross margin volatility 126d
def f22ol_f22_operating_leverage_incmgpvol126_126d_base_v119_signal(gp, revenue):
    im = _f22ol_incgm(gp, revenue, 63)
    b = im.rolling(126, min_periods=63).std()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gp scale volatility 126d
def f22ol_f22_operating_leverage_gpsclvol126_126d_base_v120_signal(gp, revenue):
    s = _f22ol_gpscale(gp, revenue, 63)
    b = s.rolling(126, min_periods=63).std()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# opex absorption volatility 126d
def f22ol_f22_operating_leverage_opxabsvol126_126d_base_v121_signal(opex, revenue):
    s = _f22ol_opexscale(opex, revenue, 63)
    b = s.rolling(126, min_periods=63).std()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gp-spread net-sign streak 126d
def f22ol_f22_operating_leverage_sprgpposstreak126_126d_base_v122_signal(gp, revenue):
    s = _f22ol_spread_gp(gp, revenue, 63)
    b = np.sign(s).rolling(126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# incremental op margin net-sign streak 126d
def f22ol_f22_operating_leverage_incmopposstreak126_126d_base_v123_signal(opinc, revenue):
    im = _f22ol_incmargin(opinc, revenue, 63)
    b = np.sign(im).rolling(126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# operating break-even DISTANCE magnitude 126d (continuous distance to zero op margin)
def f22ol_f22_operating_leverage_bedist_op126_126d_base_v124_signal(opinc, revenue):
    d = opinc / revenue.replace(0, np.nan)
    sm = np.sign(d) * (d.abs() ** 0.5)
    b = sm.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# opex-absorption net-sign streak 126d
def f22ol_f22_operating_leverage_opxabsstreak126_126d_base_v125_signal(opex, revenue):
    s = _f22ol_opexscale(opex, revenue, 63)
    b = np.sign(s).rolling(126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# sign x sqrt-mag incremental op margin
def f22ol_f22_operating_leverage_incmop_signmag_252d_base_v126_signal(opinc, revenue):
    im = _f22ol_incmargin(opinc, revenue, 252)
    b = np.sign(im) * (im.abs() ** 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# sign x sqrt-mag incremental gross margin
def f22ol_f22_operating_leverage_incmgp_signmag_252d_base_v127_signal(gp, revenue):
    im = _f22ol_incgm(gp, revenue, 252)
    b = np.sign(im) * (im.abs() ** 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# sign x sqrt-mag gp-per-opex contribution lever
def f22ol_f22_operating_leverage_gpopxlev_signmag_252d_base_v128_signal(gp, opex):
    e = _f22ol_gpopxlev(gp, opex, 252) - 1.0
    b = np.sign(e) * (e.abs() ** 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# sign x sqrt-mag ebit spread
def f22ol_f22_operating_leverage_sprebit_signmag_252d_base_v129_signal(ebit, revenue):
    s = _f22ol_spread_ebit(ebit, revenue, 252)
    b = np.sign(s) * (s.abs() ** 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# op spread times revenue growth 126d
def f22ol_f22_operating_leverage_sprXgrow_op126_126d_base_v130_signal(opinc, revenue):
    s = _f22ol_spread_op(opinc, revenue, 126)
    g = _dlog(revenue, 126)
    b = s * g
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# incremental gross margin times revenue growth 126d
def f22ol_f22_operating_leverage_incmgpXgrow126_126d_base_v131_signal(gp, revenue):
    im = _f22ol_incgm(gp, revenue, 126)
    g = _dlog(revenue, 126)
    b = im * g
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# opex absorption times revenue growth 126d
def f22ol_f22_operating_leverage_opxabsXgrow126_126d_base_v132_signal(opex, revenue):
    a = _f22ol_opexscale(opex, revenue, 126)
    g = _dlog(revenue, 126)
    b = a * g
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DOL dispersion across 63/126/252 windows (multi-horizon lever disagreement)
def f22ol_f22_operating_leverage_dol_disp_252d_base_v133_signal(opinc, revenue):
    d1 = np.tanh(_f22ol_dol(opinc, revenue, 63) / 5.0)
    d2 = np.tanh(_f22ol_dol(opinc, revenue, 126) / 5.0)
    d3 = np.tanh(_f22ol_dol(opinc, revenue, 252) / 5.0)
    b = pd.concat([d1, d2, d3], axis=1).std(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# spread dispersion across lines 126d
def f22ol_f22_operating_leverage_sprdisp_lines126_126d_base_v134_signal(opinc, gp, ebit, revenue):
    a = _f22ol_spread_op(opinc, revenue, 126)
    c = _f22ol_spread_gp(gp, revenue, 126)
    e = _f22ol_spread_ebit(ebit, revenue, 126)
    b = pd.concat([a, c, e], axis=1).std(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gross-to-operating flow-through ratio 504d (long-horizon opex drag)
def f22ol_f22_operating_leverage_flowthru504_504d_base_v135_signal(gp, opinc):
    b = np.tanh(_f22ol_flowthru(gp, opinc, 504) / 3.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# incremental gross margin momentum (acceleration)
def f22ol_f22_operating_leverage_incmgp_mom_252d_base_v136_signal(gp, revenue):
    im = _f22ol_incgm(gp, revenue, 126)
    ch = im - im.shift(63)
    b = ch - ch.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DOL momentum (acceleration)
def f22ol_f22_operating_leverage_dol_mom_252d_base_v137_signal(opinc, revenue):
    d = np.tanh(_f22ol_dol(opinc, revenue, 126) / 5.0)
    ch = d - d.shift(63)
    b = ch - ch.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# z gp spread 126d
def f22ol_f22_operating_leverage_sprgpz126_126d_base_v138_signal(gp, revenue):
    b = _z(_f22ol_spread_gp(gp, revenue, 126), 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# z incremental op margin 126d
def f22ol_f22_operating_leverage_incmopz126_126d_base_v139_signal(opinc, revenue):
    b = _z(_f22ol_incmargin(opinc, revenue, 126), 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# z opex elasticity
def f22ol_f22_operating_leverage_opxelasz_252d_base_v140_signal(opex, revenue):
    b = _z(np.tanh(_f22ol_opexelas(opex, revenue, 252) / 3.0), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gp-per-opex contribution lever acceleration (momentum of the cost-base lever)
def f22ol_f22_operating_leverage_gpopxlev_mom_252d_base_v141_signal(gp, opex):
    e = np.tanh(_f22ol_gpopxlev(gp, opex, 126) / 3.0)
    ch = e - e.shift(63)
    b = ch - ch.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# z ebit-DOL
def f22ol_f22_operating_leverage_dolebitz_252d_base_v142_signal(ebit, revenue):
    b = _z(np.tanh(_f22ol_dol_ebit(ebit, revenue, 252) / 5.0), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# rank gross safety buffer change
def f22ol_f22_operating_leverage_safetygp_rank_252d_base_v143_signal(gp, opex):
    buf = (gp - opex) / gp.replace(0, np.nan)
    ch = buf - buf.shift(252)
    b = _rank(ch, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ebit break-even DISTANCE magnitude 126d (continuous distance to zero ebit margin)
def f22ol_f22_operating_leverage_bedist_ebit126_126d_base_v144_signal(ebit, revenue):
    d = ebit / revenue.replace(0, np.nan)
    sm = np.sign(d) * (d.abs() ** 0.5)
    b = sm.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# sign x sqrt-mag incremental op margin 504d
def f22ol_f22_operating_leverage_incmop_504signmag_504d_base_v145_signal(opinc, revenue):
    im = _f22ol_incmargin(opinc, revenue, 504)
    b = np.sign(im) * (im.abs() ** 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# rank op spread 504d
def f22ol_f22_operating_leverage_sprop_504rank_504d_base_v146_signal(opinc, revenue):
    b = _rank(_f22ol_spread_op(opinc, revenue, 504), 756)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# DOL volatility 504d
def f22ol_f22_operating_leverage_dolop_vol504_504d_base_v147_signal(opinc, revenue):
    d = np.tanh(_f22ol_dol(opinc, revenue, 126) / 5.0)
    b = d.rolling(504, min_periods=252).std()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# rank incremental gross margin 504d
def f22ol_f22_operating_leverage_incmgp_rank504_504d_base_v148_signal(gp, revenue):
    b = _rank(_f22ol_incgm(gp, revenue, 504), 756)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# rank gp-per-opex contribution lever 504d (gross-line cost leverage percentile)
def f22ol_f22_operating_leverage_gpopxlev_rank504_504d_base_v149_signal(gp, opex):
    e = np.tanh(_f22ol_gpopxlev(gp, opex, 504) / 3.0)
    b = _rank(e, 756)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# op spread volatility 126d
def f22ol_f22_operating_leverage_sprop_vol126_126d_base_v150_signal(opinc, revenue):
    s = _f22ol_spread_op(opinc, revenue, 63)
    b = s.rolling(126, min_periods=63).std()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f22ol_f22_operating_leverage_spropchg_252d_base_v076_signal,
    f22ol_f22_operating_leverage_sprgpchg_252d_base_v077_signal,
    f22ol_f22_operating_leverage_incmopchg_252d_base_v078_signal,
    f22ol_f22_operating_leverage_opxabschg_252d_base_v079_signal,
    f22ol_f22_operating_leverage_fixlevchg_252d_base_v080_signal,
    f22ol_f22_operating_leverage_dol_stab_252d_base_v081_signal,
    f22ol_f22_operating_leverage_incmop_ema_126d_base_v082_signal,
    f22ol_f22_operating_leverage_sprgp_ema_126d_base_v083_signal,
    f22ol_f22_operating_leverage_gpopxlev_chg_252d_base_v084_signal,
    f22ol_f22_operating_leverage_gpelas_chg_252d_base_v085_signal,
    f22ol_f22_operating_leverage_flowthru_chg_252d_base_v086_signal,
    f22ol_f22_operating_leverage_sprop_yoy_252d_base_v087_signal,
    f22ol_f22_operating_leverage_incmop_yoy_252d_base_v088_signal,
    f22ol_f22_operating_leverage_gpopxlev_yoy_252d_base_v089_signal,
    f22ol_f22_operating_leverage_dol_yoy_252d_base_v090_signal,
    f22ol_f22_operating_leverage_sprXgrow_gp_252d_base_v091_signal,
    f22ol_f22_operating_leverage_opxabsXgrow_252d_base_v092_signal,
    f22ol_f22_operating_leverage_sprebitchg_252d_base_v093_signal,
    f22ol_f22_operating_leverage_doltanh_126d_base_v094_signal,
    f22ol_f22_operating_leverage_incmgp_disp_252d_base_v095_signal,
    f22ol_f22_operating_leverage_sprgpsignmag_252d_base_v096_signal,
    f22ol_f22_operating_leverage_sprebitposstreak_252d_base_v097_signal,
    f22ol_f22_operating_leverage_incmopposstreak_252d_base_v098_signal,
    f22ol_f22_operating_leverage_fixlevposstreak_252d_base_v099_signal,
    f22ol_f22_operating_leverage_dolop_chg_252d_base_v100_signal,
    f22ol_f22_operating_leverage_incmgp_ema_126d_base_v101_signal,
    f22ol_f22_operating_leverage_sprop_ema_126d_base_v102_signal,
    f22ol_f22_operating_leverage_ebitelas_rank_252d_base_v103_signal,
    f22ol_f22_operating_leverage_incmop_rank126_126d_base_v104_signal,
    f22ol_f22_operating_leverage_sprgp_rank126_126d_base_v105_signal,
    f22ol_f22_operating_leverage_dol_rank126_126d_base_v106_signal,
    f22ol_f22_operating_leverage_dolop_signmag_252d_base_v107_signal,
    f22ol_f22_operating_leverage_sprop_rank126_126d_base_v108_signal,
    f22ol_f22_operating_leverage_opxabs_yoy_252d_base_v109_signal,
    f22ol_f22_operating_leverage_gpscl_yoy_252d_base_v110_signal,
    f22ol_f22_operating_leverage_incmgp_yoy_252d_base_v111_signal,
    f22ol_f22_operating_leverage_dolebit_chg_252d_base_v112_signal,
    f22ol_f22_operating_leverage_incmopvol126_126d_base_v113_signal,
    f22ol_f22_operating_leverage_sprop_signmag126_126d_base_v114_signal,
    f22ol_f22_operating_leverage_incmop_rank504_504d_base_v115_signal,
    f22ol_f22_operating_leverage_gpopxlev_rank126_126d_base_v116_signal,
    f22ol_f22_operating_leverage_sprgp_rank504_504d_base_v117_signal,
    f22ol_f22_operating_leverage_sprebitvol_252d_base_v118_signal,
    f22ol_f22_operating_leverage_incmgpvol126_126d_base_v119_signal,
    f22ol_f22_operating_leverage_gpsclvol126_126d_base_v120_signal,
    f22ol_f22_operating_leverage_opxabsvol126_126d_base_v121_signal,
    f22ol_f22_operating_leverage_sprgpposstreak126_126d_base_v122_signal,
    f22ol_f22_operating_leverage_incmopposstreak126_126d_base_v123_signal,
    f22ol_f22_operating_leverage_bedist_op126_126d_base_v124_signal,
    f22ol_f22_operating_leverage_opxabsstreak126_126d_base_v125_signal,
    f22ol_f22_operating_leverage_incmop_signmag_252d_base_v126_signal,
    f22ol_f22_operating_leverage_incmgp_signmag_252d_base_v127_signal,
    f22ol_f22_operating_leverage_gpopxlev_signmag_252d_base_v128_signal,
    f22ol_f22_operating_leverage_sprebit_signmag_252d_base_v129_signal,
    f22ol_f22_operating_leverage_sprXgrow_op126_126d_base_v130_signal,
    f22ol_f22_operating_leverage_incmgpXgrow126_126d_base_v131_signal,
    f22ol_f22_operating_leverage_opxabsXgrow126_126d_base_v132_signal,
    f22ol_f22_operating_leverage_dol_disp_252d_base_v133_signal,
    f22ol_f22_operating_leverage_sprdisp_lines126_126d_base_v134_signal,
    f22ol_f22_operating_leverage_flowthru504_504d_base_v135_signal,
    f22ol_f22_operating_leverage_incmgp_mom_252d_base_v136_signal,
    f22ol_f22_operating_leverage_dol_mom_252d_base_v137_signal,
    f22ol_f22_operating_leverage_sprgpz126_126d_base_v138_signal,
    f22ol_f22_operating_leverage_incmopz126_126d_base_v139_signal,
    f22ol_f22_operating_leverage_opxelasz_252d_base_v140_signal,
    f22ol_f22_operating_leverage_gpopxlev_mom_252d_base_v141_signal,
    f22ol_f22_operating_leverage_dolebitz_252d_base_v142_signal,
    f22ol_f22_operating_leverage_safetygp_rank_252d_base_v143_signal,
    f22ol_f22_operating_leverage_bedist_ebit126_126d_base_v144_signal,
    f22ol_f22_operating_leverage_incmop_504signmag_504d_base_v145_signal,
    f22ol_f22_operating_leverage_sprop_504rank_504d_base_v146_signal,
    f22ol_f22_operating_leverage_dolop_vol504_504d_base_v147_signal,
    f22ol_f22_operating_leverage_incmgp_rank504_504d_base_v148_signal,
    f22ol_f22_operating_leverage_gpopxlev_rank504_504d_base_v149_signal,
    f22ol_f22_operating_leverage_sprop_vol126_126d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}


F22_OPERATING_LEVERAGE_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0004, 0.032, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    close = pd.Series(closeadj.values, name="close")
    openp = pd.Series(close.shift(1).fillna(close.iloc[0]).values
                      * (1 + np.random.normal(0, 0.012, n)), name="open")
    high = pd.Series(np.maximum(close, openp) * (1 + np.abs(np.random.normal(0, 0.02, n))), name="high")
    low = pd.Series(np.minimum(close, openp) * (1 - np.abs(np.random.normal(0, 0.02, n))), name="low")
    volume = pd.Series(np.abs(np.random.normal(1.2e6, 7e5, n)) + 5e4, name="volume")

    def _fund(seed, base=1e8, drift=0.03, vol=0.07, allow_neg=False):
        g = np.random.default_rng(seed)
        steps = np.repeat(g.normal(drift, vol, n // 63 + 1), 63)[:n]
        s = base * np.exp(np.cumsum(steps / 63))
        if allow_neg:
            s = s - base * 0.6
        return pd.Series(s, name=None)

    def _margin(seed, lo, hi, rho=0.995):
        g = np.random.default_rng(seed)
        e = g.normal(0, 0.01, n)
        ar = np.zeros(n)
        for t in range(1, n):
            ar[t] = rho * ar[t - 1] + e[t]
        m = (ar - ar.min()) / (ar.max() - ar.min() + 1e-9)
        return pd.Series(lo + (hi - lo) * m, name=None)

    revenue = _fund(1, base=1.2e8, drift=0.035, vol=0.06).rename("revenue")
    opex = _fund(2, base=7.0e7, drift=0.030, vol=0.05).rename("opex")
    gp = (revenue * _margin(10, 0.34, 0.62)).rename("gp")
    opinc = (revenue * _margin(11, -0.16, 0.26)).rename("opinc")
    ebit = (revenue * _margin(12, -0.05, 0.27)).rename("ebit")

    cols = {"closeadj": closeadj, "close": close, "open": openp, "high": high,
            "low": low, "volume": volume, "revenue": revenue, "opex": opex,
            "gp": gp, "opinc": opinc, "ebit": ebit}

    ALLOW = {"open", "high", "low", "close", "closeadj", "volume", "revenue", "revenueusd",
             "deferredrev", "gp", "grossmargin", "opinc", "opex", "sgna", "cor", "rnd",
             "sbcomp", "ebit", "ebitda", "ebitdamargin", "netinc", "netinccmn", "netmargin",
             "eps", "epsdil", "fcf", "fcfps", "ncfo", "ncff", "ncfi", "ncfcommon", "ncfdebt",
             "ncfbus", "capex", "depamor", "sharesbas", "shareswa", "shareswadil", "assets",
             "assetsc", "tangibles", "intangibles", "ppnenet", "investments", "inventory",
             "receivables", "payables", "equity", "retearn", "workingcapital", "debt", "debtc",
             "debtnc", "liabilities", "liabilitiesc", "cashneq", "currentratio", "roic", "roe",
             "roa", "ros", "assetturnover", "invcap", "intexp", "taxexp", "ebt", "sps", "bvps",
             "de", "ncfdiv", "dps", "divyield", "payoutratio", "prefdivis", "marketcap", "ev",
             "evebit", "evebitda", "pe", "pb", "ps", "shrholders", "shrvalue", "shrunits",
             "totalvalue", "percentoftotal", "fndholders", "undholders", "prfholders",
             "dbtholders", "putholders", "putvalue", "cllholders", "cllvalue", "wntholders",
             "wntvalue", "dbtvalue"}
    FUND = {"revenue", "revenueusd", "deferredrev", "gp", "grossmargin", "opinc", "opex",
            "sgna", "cor", "rnd", "sbcomp", "ebit", "ebitda", "ebitdamargin", "netinc",
            "netinccmn", "netmargin", "eps", "epsdil", "fcf", "fcfps", "ncfo", "ncff", "ncfi",
            "ncfcommon", "ncfdebt", "ncfbus", "capex", "depamor", "sharesbas", "shareswa",
            "shareswadil", "assets", "assetsc", "tangibles", "intangibles", "ppnenet",
            "investments", "inventory", "receivables", "payables", "equity", "retearn",
            "workingcapital", "debt", "debtc", "debtnc", "liabilities", "liabilitiesc",
            "cashneq", "currentratio", "roic", "roe", "roa", "ros", "assetturnover", "invcap",
            "intexp", "taxexp", "ebt", "sps", "bvps", "de", "ncfdiv", "dps", "divyield",
            "payoutratio", "prefdivis"}

    n_features = 0
    nan_ok = 0
    results = {}
    for name, meta in REGISTRY.items():
        inp = meta["inputs"]
        assert set(inp) <= ALLOW, "%s inputs not in allowlist: %s" % (name, inp)
        assert len(set(inp) & FUND) >= 1, "%s has no fundamental column" % name
        fn = meta["func"]
        args = [cols[c] for c in inp]
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

    print("OK f22_operating_leverage_base_076_150_claude: %d features pass" % n_features)
