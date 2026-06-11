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


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


def _rmax(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rmin(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rank(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).rank(pct=True) - 0.5


# ===== folder domain primitives (revenue scale / per-share) =====
def _f20_loggrowth(s, w):
    return np.log(s.replace(0, np.nan) / s.shift(w).replace(0, np.nan))


def _f20_pershare(rev, sh):
    return rev / sh.replace(0, np.nan)


def _f20_scale(s):
    return np.log(s.replace(0, np.nan))


def _f20_accel(s, w):
    g = np.log(s.replace(0, np.nan) / s.shift(w).replace(0, np.nan))
    return g - g.shift(w)


def _f20_fxdiverge(reported, usd):
    return reported / usd.replace(0, np.nan) - 1.0


# ============================================================
# sps growth efficiency ratio: net 252d change over summed 21d path (smoothness)
def f20rs_f20_revenue_scale_per_share_spseff_base_v076_signal(sps):
    net = (sps - sps.shift(252)).abs()
    path = sps.diff().abs().rolling(252, min_periods=126).sum()
    b = net / path.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue growth efficiency ratio (directionality of revenue scaling)
def f20rs_f20_revenue_scale_per_share_reveff_base_v077_signal(revenue):
    net = (revenue - revenue.shift(252)).abs()
    path = revenue.diff().abs().rolling(252, min_periods=126).sum()
    b = net / path.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# sps log-scale slope via 63d linear-ish difference normalized (per-share trend strength)
def f20rs_f20_revenue_scale_per_share_spsslopez_base_v078_signal(sps):
    ls = _f20_scale(sps)
    sl = (ls - ls.shift(63)) / 63.0
    b = _z(sl, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dilution drawdown / buyback signal: log distance of the share count below its trailing
# 504d MAXIMUM (negative only when the float has been reduced from a peak -- captures
# buyback-driven share shrinkage; a pure share-count level facet, distinct from raw-
# revenue slope-z in f18 and from share-growth velocity features)
def f20rs_f20_revenue_scale_per_share_shbuyback_base_v079_signal(shareswa):
    hi = _rmax(shareswa, 504)
    b = np.log(shareswa.replace(0, np.nan) / hi.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# sps scale headroom: distance below own 504d max (per-share scale ceiling gap)
def f20rs_f20_revenue_scale_per_share_spsceil_base_v080_signal(sps):
    hi = _rmax(sps, 504)
    b = np.log(sps.replace(0, np.nan) / hi.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue floor distance: how far revenue sits above its 504d min (scale cushion)
def f20rs_f20_revenue_scale_per_share_revfloor_base_v081_signal(revenue):
    lo = _rmin(revenue, 504)
    b = np.log(revenue.replace(0, np.nan) / lo.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# sps level relative to its 126d EMA (short per-share scale displacement)
def f20rs_f20_revenue_scale_per_share_spsema_base_v082_signal(sps):
    ls = _f20_scale(sps)
    b = ls - ls.ewm(span=63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue scale robust displacement: log-revenue minus its 252d median, scaled by the
# 252d median-absolute-deviation (robust outlier-aware size extremity; distinct from the
# EMA-displacement and mean-z facets which are dominated by the smooth trend)
def f20rs_f20_revenue_scale_per_share_revrobustz_base_v083_signal(revenue):
    ls = _f20_scale(revenue)
    med = ls.rolling(252, min_periods=126).median()
    mad = (ls - med).abs().rolling(252, min_periods=126).median()
    b = (ls - med) / mad.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# USD revenue growth z-scored vs own history (USD scaling extremity)
def f20rs_f20_revenue_scale_per_share_usdgrz_base_v084_signal(revenueusd):
    g = _f20_loggrowth(revenueusd, 252)
    b = _z(g, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FX divergence trend: 126d slope of the reported-vs-USD gap (translation drift)
def f20rs_f20_revenue_scale_per_share_fxtrend_base_v085_signal(revenue, revenueusd):
    d = _f20_fxdiverge(revenue, revenueusd)
    b = (d - d.shift(126)) / 126.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FX divergence rank vs own 504d history (translation regime percentile)
def f20rs_f20_revenue_scale_per_share_fxrank_base_v086_signal(revenue, revenueusd):
    d = _f20_fxdiverge(revenue, revenueusd)
    b = _rank(d, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dilution coupling: 252d rolling correlation between 21d rps-growth and 21d share-count
# growth (is per-share scaling moving with or against the share base? negative = clean
# buyback-driven per-share gains; a coupling facet distinct from level/z features)
def f20rs_f20_revenue_scale_per_share_pscouple_base_v087_signal(revenue, shareswa):
    rpsg = _f20_loggrowth(_f20_pershare(revenue, shareswa), 21)
    shg = _f20_loggrowth(shareswa, 21)
    b = rpsg.rolling(252, min_periods=126).corr(shg)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# share-count acceleration (dilution inflection, 126d)
def f20rs_f20_revenue_scale_per_share_shaccel_base_v088_signal(shareswa):
    b = _f20_accel(shareswa, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# sps growth minus share growth, EMA-smoothed (durable clean per-share scaling)
def f20rs_f20_revenue_scale_per_share_cleanps_base_v089_signal(sps, shareswa):
    spsg = _f20_loggrowth(sps, 126)
    shg = _f20_loggrowth(shareswa, 126)
    b = (spsg - shg).ewm(span=63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue scale relative to a 2-year-ago anchor (multi-year size memory)
def f20rs_f20_revenue_scale_per_share_revmemory_base_v090_signal(revenue):
    anchor = _rmax(revenue, 504).shift(126)
    b = np.log(revenue.replace(0, np.nan) / anchor.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# sps scale relative to 2-year-ago anchor (multi-year per-share memory)
def f20rs_f20_revenue_scale_per_share_spsmemory_base_v091_signal(sps):
    anchor = _rmax(sps, 504).shift(126)
    b = np.log(sps.replace(0, np.nan) / anchor.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue growth volatility (instability of the scaling pace, 252d)
def f20rs_f20_revenue_scale_per_share_revgrvol_base_v092_signal(revenue):
    g = _f20_loggrowth(revenue, 21)
    b = _std(g, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# sps growth volatility (per-share scaling instability)
def f20rs_f20_revenue_scale_per_share_spsgrvol2_base_v093_signal(sps):
    g = _f20_loggrowth(sps, 21)
    b = _std(g, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# share-base scale percentile: where the current diluted share count sits in its own 504d
# distribution (size of the dilution base; a pure share-count scale facet with no
# per-share or revenue twin -- larger rank = company has grown its float to a new high)
def f20rs_f20_revenue_scale_per_share_shbaserank_base_v094_signal(shareswa):
    b = _rank(_f20_scale(shareswa), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue 126d growth de-meaned vs its own 252d typical (scaling-pace inflection)
def f20rs_f20_revenue_scale_per_share_revinflect_base_v095_signal(revenue):
    g = _f20_loggrowth(revenue, 126)
    b = g - _mean(g, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# USD scaling consistency over a long horizon: 504d info-ratio of 126d USD-revenue
# log-growth (mean over std) -- durable, smooth USD-size compounding measured on a longer
# growth window and horizon than the other stability facets (distinct window combination)
def f20rs_f20_revenue_scale_per_share_usdconsist_base_v096_signal(revenueusd):
    g = _f20_loggrowth(revenueusd, 126)
    b = _mean(g, 504) / _std(g, 504).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# sps new-high recency: fraction of last 504d sps sat in its top decile band
def f20rs_f20_revenue_scale_per_share_spstopband_base_v097_signal(sps):
    hi = _rmax(sps, 504)
    lo = _rmin(sps, 504)
    pos = (sps - lo) / (hi - lo).replace(0, np.nan)
    top = (pos >= 0.9).astype(float)
    b = top.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue scale acceleration de-meaned (size-growth inflection level)
def f20rs_f20_revenue_scale_per_share_revaccelz_base_v098_signal(revenue):
    a = _f20_accel(revenue, 126)
    b = _z(a, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# combined scaling quality: sps growth times sps growth-stability (durable per-share)
def f20rs_f20_revenue_scale_per_share_spsquality_base_v099_signal(sps):
    g = _f20_loggrowth(sps, 126)
    stab = _mean(_f20_loggrowth(sps, 21), 252) / _std(_f20_loggrowth(sps, 21), 252).replace(0, np.nan)
    b = np.tanh(g) * np.tanh(stab)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue scaling quality: revenue growth times revenue growth-stability
def f20rs_f20_revenue_scale_per_share_revquality_base_v100_signal(revenue):
    g = _f20_loggrowth(revenue, 126)
    stab = _mean(_f20_loggrowth(revenue, 21), 252) / _std(_f20_loggrowth(revenue, 21), 252).replace(0, np.nan)
    b = np.tanh(g) * np.tanh(stab)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# per-share scale momentum spread: sps short vs long EMA of log-scale (trend regime)
def f20rs_f20_revenue_scale_per_share_spstrendreg_base_v101_signal(sps):
    ls = _f20_scale(sps)
    fast = ls.ewm(span=42, min_periods=21).mean()
    slow = ls.ewm(span=189, min_periods=63).mean()
    b = fast - slow
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue scale trend regime (fast vs slow EMA of log revenue)
def f20rs_f20_revenue_scale_per_share_revtrendreg_base_v102_signal(revenue):
    ls = _f20_scale(revenue)
    fast = ls.ewm(span=42, min_periods=21).mean()
    slow = ls.ewm(span=189, min_periods=63).mean()
    b = fast - slow
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FX-divergence sign-magnitude (translation tilt, square-root compressed)
def f20rs_f20_revenue_scale_per_share_fxsignmag_base_v103_signal(revenue, revenueusd):
    d = _f20_fxdiverge(revenue, revenueusd)
    b = np.sign(d) * (d.abs() ** 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# per-share scaling tail-heaviness: 252d rolling kurtosis of 21d rps log-growth
# (do per-share moves arrive in fat-tailed bursts? a distribution-shape facet, distinct
# from risk-adjusted growth / vol features)
def f20rs_f20_revenue_scale_per_share_rpsgrkurt_base_v104_signal(revenue, shareswa):
    rps = _f20_pershare(revenue, shareswa)
    g = _f20_loggrowth(rps, 21)
    b = g.rolling(252, min_periods=126).kurt()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# sps growth percentile vs revenue growth percentile (per-share leadership)
def f20rs_f20_revenue_scale_per_share_psleader_base_v105_signal(sps, revenue):
    rs = _rank(_f20_loggrowth(sps, 252), 504)
    rr = _rank(_f20_loggrowth(revenue, 252), 504)
    b = rs - rr
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue scale drawdown depth smoothed (sustained revenue contraction)
def f20rs_f20_revenue_scale_per_share_revddsm_base_v106_signal(revenue):
    hi = _rmax(revenue, 504)
    dd = revenue / hi.replace(0, np.nan) - 1.0
    b = _mean(dd, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# sps scale drawdown depth smoothed (sustained per-share contraction)
def f20rs_f20_revenue_scale_per_share_spsddsm_base_v107_signal(sps):
    hi = _rmax(sps, 504)
    dd = sps / hi.replace(0, np.nan) - 1.0
    b = _mean(dd, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# share-count growth streak: fraction of last year with positive 63d dilution
def f20rs_f20_revenue_scale_per_share_dilstreak_base_v108_signal(shareswa):
    g = _f20_loggrowth(shareswa, 63)
    pos = (g > 0).astype(float)
    b = pos.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue scale convexity vs sps scale convexity blend (combined size curvature)
def f20rs_f20_revenue_scale_per_share_sizecurve_base_v109_signal(revenue, sps):
    zr = _z(_f20_scale(revenue), 252)
    zs = _z(_f20_scale(sps), 252)
    b = np.sign(zr) * (zr ** 2) - np.sign(zs) * (zs ** 2)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# USD-per-share scale curvature: discrete 2nd difference of log USD-per-share across 63d
# arms (convexity/concavity of the per-share scaling path; a shape facet distinct from
# level-displacement and FX-level-wedge features)
def f20rs_f20_revenue_scale_per_share_usdpscurv_base_v110_signal(revenueusd, shareswa):
    ups = _f20_scale(_f20_pershare(revenueusd, shareswa))
    b = ups.shift(126) - 2.0 * ups.shift(63) + ups
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue scaling persistence: autocorrelation-style sign-consistency of 21d growth
def f20rs_f20_revenue_scale_per_share_revpersist_base_v111_signal(revenue):
    g = _f20_loggrowth(revenue, 21)
    sg = np.sign(g)
    b = (sg * sg.shift(21)).rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# sps scaling persistence (sign-consistency of per-share growth)
def f20rs_f20_revenue_scale_per_share_spspersist_base_v112_signal(sps):
    g = _f20_loggrowth(sps, 21)
    sg = np.sign(g)
    b = (sg * sg.shift(21)).rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue 504d growth z-scored (multi-year size expansion extremity)
def f20rs_f20_revenue_scale_per_share_revlonggrz_base_v113_signal(revenue):
    g = _f20_loggrowth(revenue, 504)
    b = _z(g, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# sps 504d growth percentile rank (multi-year per-share expansion regime)
def f20rs_f20_revenue_scale_per_share_spslongrank_base_v114_signal(sps):
    g = _f20_loggrowth(sps, 504)
    b = _rank(g, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# scaling wedge: revenue growth minus USD growth, ranked (FX contribution percentile)
def f20rs_f20_revenue_scale_per_share_fxcontrib_base_v115_signal(revenue, revenueusd):
    rg = _f20_loggrowth(revenue, 252)
    ug = _f20_loggrowth(revenueusd, 252)
    b = _rank(rg - ug, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# per-share inflection breadth: sign of sps accel times revenue accel agreement
def f20rs_f20_revenue_scale_per_share_inflectagree_base_v116_signal(sps, revenue):
    a1 = np.sign(_f20_accel(sps, 126))
    a2 = np.sign(_f20_accel(revenue, 126))
    agree = (a1 * a2)
    b = agree.rolling(126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue scale momentum normalized by its long-run drift (relative acceleration)
def f20rs_f20_revenue_scale_per_share_relaccel_base_v117_signal(revenue):
    g63 = _f20_loggrowth(revenue, 63)
    drift = _mean(_f20_loggrowth(revenue, 63), 504)
    b = g63 / (drift.abs() + 0.01) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# sps scale momentum normalized by long-run drift (relative per-share acceleration)
def f20rs_f20_revenue_scale_per_share_spsrelaccel_base_v118_signal(sps):
    g63 = _f20_loggrowth(sps, 63)
    drift = _mean(_f20_loggrowth(sps, 63), 504)
    b = g63 / (drift.abs() + 0.01) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# size-tier distance: revenue log-scale minus its 504d median (above/below typical size)
def f20rs_f20_revenue_scale_per_share_sizetier_base_v119_signal(revenue):
    ls = _f20_scale(revenue)
    med = ls.rolling(504, min_periods=126).median()
    b = ls - med
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# sps size-tier distance vs 504d median (per-share above/below typical)
def f20rs_f20_revenue_scale_per_share_spssizetier_base_v120_signal(sps):
    ls = _f20_scale(sps)
    med = ls.rolling(504, min_periods=126).median()
    b = ls - med
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue-per-share scale interaction: rps growth weighted by rps scale rank
def f20rs_f20_revenue_scale_per_share_rpsweighted_base_v121_signal(revenue, shareswa):
    rps = _f20_pershare(revenue, shareswa)
    g = _f20_loggrowth(rps, 126)
    w = _rank(_f20_scale(rps), 504) + 0.5
    b = g * w
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FX divergence momentum acceleration (change in translation drift, jerk-of-gap)
def f20rs_f20_revenue_scale_per_share_fxgapaccel_base_v122_signal(revenue, revenueusd):
    d = _f20_fxdiverge(revenue, revenueusd)
    mom = d - d.shift(63)
    b = mom - mom.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue scaling autocorrelation: 252d rolling correlation of 21d revenue log-growth
# with its own 63d-lagged value (does scaling momentum persist or mean-revert? a
# persistence facet, structurally unlike acceleration-balance forms)
def f20rs_f20_revenue_scale_per_share_revgracf_base_v123_signal(revenue):
    g = _f20_loggrowth(revenue, 21)
    b = g.rolling(252, min_periods=126).corr(g.shift(63))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# per-share scaling short-lag autocorrelation: 252d rolling correlation of 21d sps
# log-growth with its own 21d-lagged value (does last month's per-share momentum carry
# into this month? a persistence facet distinct from growth dispersion/amplitude)
def f20rs_f20_revenue_scale_per_share_spsgracf_base_v124_signal(sps):
    g = _f20_loggrowth(sps, 21)
    b = g.rolling(252, min_periods=126).corr(g.shift(21))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# per-share scaling vs dilution net regime: tanh(sps growth) minus tanh(share growth)
def f20rs_f20_revenue_scale_per_share_netscale_base_v125_signal(sps, shareswa):
    sg = _f20_loggrowth(sps, 252)
    shg = _f20_loggrowth(shareswa, 252)
    b = np.tanh(3.0 * sg) - np.tanh(8.0 * shg)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue scale recovery rate: 252d recovery off min divided by months since min
def f20rs_f20_revenue_scale_per_share_revrecovrate_base_v126_signal(revenue):
    def _dsl(a):
        return (len(a) - 1 - int(np.argmin(a))) / float(len(a))
    lo = _rmin(revenue, 252)
    rec = revenue / lo.replace(0, np.nan) - 1.0
    dsl = revenue.rolling(252, min_periods=126).apply(_dsl, raw=True).replace(0, np.nan)
    b = rec / dsl
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# sps scale recovery rate (per-share rebound speed off the 252d trough)
def f20rs_f20_revenue_scale_per_share_spsrecovrate_base_v127_signal(sps):
    def _dsl(a):
        return (len(a) - 1 - int(np.argmin(a))) / float(len(a))
    lo = _rmin(sps, 252)
    rec = sps / lo.replace(0, np.nan) - 1.0
    dsl = sps.rolling(252, min_periods=126).apply(_dsl, raw=True).replace(0, np.nan)
    b = rec / dsl
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue growth dispersion (rolling std of 63d growth, scaling turbulence)
def f20rs_f20_revenue_scale_per_share_revturb_base_v128_signal(revenue):
    g = _f20_loggrowth(revenue, 63)
    b = _std(g, 252) / (_mean(g, 252).abs() + 0.01)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# sps growth coefficient of variation (per-share scaling turbulence)
def f20rs_f20_revenue_scale_per_share_spsturb_base_v129_signal(sps):
    g = _f20_loggrowth(sps, 63)
    b = _std(g, 252) / (_mean(g, 252).abs() + 0.01)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# USD revenue scale relative to reported scale, smoothed (persistent FX level wedge)
def f20rs_f20_revenue_scale_per_share_fxlevelwedge_base_v130_signal(revenue, revenueusd):
    wedge = _f20_scale(revenueusd) - _f20_scale(revenue)
    b = wedge.ewm(span=126, min_periods=42).mean() - wedge.ewm(span=504, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# sps 252d range-position momentum (per-share positioning drift over a month)
def f20rs_f20_revenue_scale_per_share_spsnearpos_base_v131_signal(sps):
    hi = _rmax(sps, 252)
    lo = _rmin(sps, 252)
    pos = (sps - lo) / (hi - lo).replace(0, np.nan)
    b = pos - pos.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue 252d range-position momentum (size positioning drift over a month)
def f20rs_f20_revenue_scale_per_share_revnearpos_base_v132_signal(revenue):
    hi = _rmax(revenue, 252)
    lo = _rmin(revenue, 252)
    pos = (revenue - lo) / (hi - lo).replace(0, np.nan)
    b = pos - pos.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# per-share revenue scaling vs share dilution interaction (clean-growth product)
def f20rs_f20_revenue_scale_per_share_cleanprod_base_v133_signal(revenue, shareswa):
    rg = _f20_loggrowth(revenue, 126)
    shg = _f20_loggrowth(shareswa, 126)
    b = np.sign(rg) * np.sqrt(rg.abs()) * (1.0 - np.tanh(10.0 * shg.clip(lower=0)))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue size-rank momentum: change in revenue scale percentile over a quarter
def f20rs_f20_revenue_scale_per_share_sizerankmom_base_v134_signal(revenue):
    r = _rank(_f20_scale(revenue), 504)
    b = r - r.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# sps size-rank momentum (per-share size percentile drift)
def f20rs_f20_revenue_scale_per_share_spssizerankmom_base_v135_signal(sps):
    r = _rank(_f20_scale(sps), 504)
    b = r - r.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue growth-of-growth (third-order pace inflection via accel change)
def f20rs_f20_revenue_scale_per_share_revjerk_base_v136_signal(revenue):
    a = _f20_accel(revenue, 63)
    b = a - a.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# sps growth-of-growth (per-share third-order inflection)
def f20rs_f20_revenue_scale_per_share_spsjerk_base_v137_signal(sps):
    a = _f20_accel(sps, 63)
    b = a - a.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue scale amplitude expansion: change in 252d normalized span over a quarter
def f20rs_f20_revenue_scale_per_share_revspan_base_v138_signal(revenue):
    hi = _rmax(revenue, 252)
    lo = _rmin(revenue, 252)
    span = (hi - lo) / revenue.replace(0, np.nan)
    b = span - span.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# sps scale squeeze ratio: 63d high-low span relative to the 252d high-low span of sps
# (per-share scale range compression vs expansion regime; a squeeze-ratio facet distinct
# from the quarter-over-quarter span-change features)
def f20rs_f20_revenue_scale_per_share_spssqueeze_base_v139_signal(sps):
    span_s = _rmax(sps, 63) - _rmin(sps, 63)
    span_l = (_rmax(sps, 252) - _rmin(sps, 252)).replace(0, np.nan)
    b = span_s / span_l
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# USD scaling vol term-structure: ratio of short (63d) to long (252d) dispersion of
# 21d USD-revenue log-growth (is per-period scaling getting choppier or calmer? a
# vol-ratio facet, structurally unlike the mean/std info-ratio stability features)
def f20rs_f20_revenue_scale_per_share_usdvolratio_base_v140_signal(revenueusd):
    g = _f20_loggrowth(revenueusd, 21)
    short = _std(g, 63)
    long = _std(g, 252).replace(0, np.nan)
    b = short / long - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# per-share scale vs revenue scale lead-lag: rps growth minus revenue growth (63d)
def f20rs_f20_revenue_scale_per_share_pslead63_base_v141_signal(revenue, shareswa):
    rps = _f20_pershare(revenue, shareswa)
    rpsg = _f20_loggrowth(rps, 63)
    rg = _f20_loggrowth(revenue, 63)
    b = _z(rpsg - rg, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue scale stretch: log-revenue minus 252d max (negative headroom)
def f20rs_f20_revenue_scale_per_share_revstretch_base_v142_signal(revenue):
    hi = _rmax(revenue, 252)
    raw = np.log(revenue.replace(0, np.nan) / hi.replace(0, np.nan))
    b = _z(raw, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# sps scale stretch z (per-share negative headroom de-trended)
def f20rs_f20_revenue_scale_per_share_spsstretch_base_v143_signal(sps):
    hi = _rmax(sps, 252)
    raw = np.log(sps.replace(0, np.nan) / hi.replace(0, np.nan))
    b = _z(raw, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# composite scaling momentum: average tanh of sps & revenue 126d growth
def f20rs_f20_revenue_scale_per_share_scalemom_base_v144_signal(sps, revenue):
    sg = np.tanh(3.0 * _f20_loggrowth(sps, 126))
    rg = np.tanh(3.0 * _f20_loggrowth(revenue, 126))
    b = (sg + rg) / 2.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dilution-overhang index: cumulative log-share gain over 504d, bounded
def f20rs_f20_revenue_scale_per_share_diloverhang_base_v145_signal(shareswa):
    g = _f20_loggrowth(shareswa, 504)
    b = np.tanh(6.0 * g)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# per-share vs total acceleration leadership: percentile rank of sps 126d acceleration
# minus percentile rank of revenue 126d acceleration (is per-share inflection leading or
# lagging total-size inflection? a dilution-driven accel-leadership facet)
def f20rs_f20_revenue_scale_per_share_accellead_base_v146_signal(sps, revenue):
    rs = _rank(_f20_accel(sps, 126), 504)
    rr = _rank(_f20_accel(revenue, 126), 504)
    b = rs - rr
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# scaling-through-dilution regime: fraction of last 252d where per-share revenue rose
# (63d rps growth > 0) WHILE the share base also expanded (63d share growth > 0) -- i.e.
# the company out-grew its own dilution; a co-occurrence count facet distinct from any
# growth-per-dilution ratio rank
def f20rs_f20_revenue_scale_per_share_outgrowdil_base_v147_signal(revenue, shareswa):
    rpsg = _f20_loggrowth(_f20_pershare(revenue, shareswa), 63)
    shg = _f20_loggrowth(shareswa, 63)
    both = ((rpsg > 0) & (shg > 0)).astype(float)
    b = both.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue drawdown-recovery balance momentum (shift in contraction/rebound mix)
def f20rs_f20_revenue_scale_per_share_revdrbal_base_v148_signal(revenue):
    hi = _rmax(revenue, 504)
    lo = _rmin(revenue, 504)
    dd = (hi - revenue) / hi.replace(0, np.nan)
    rec = (revenue - lo) / lo.replace(0, np.nan)
    bal = (rec - dd) / (rec + dd).replace(0, np.nan)
    b = bal - bal.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# sps drawdown-recovery balance momentum (shift in per-share contraction/rebound mix)
def f20rs_f20_revenue_scale_per_share_spsdrbal_base_v149_signal(sps):
    hi = _rmax(sps, 504)
    lo = _rmin(sps, 504)
    dd = (hi - sps) / hi.replace(0, np.nan)
    rec = (sps - lo) / lo.replace(0, np.nan)
    bal = (rec - dd) / (rec + dd).replace(0, np.nan)
    b = bal - bal.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# durable per-share compounding: sps positive-growth fraction times annualized drift
def f20rs_f20_revenue_scale_per_share_spscompound_base_v150_signal(sps):
    g = _f20_loggrowth(sps, 63)
    posfrac = (g > 0).astype(float).rolling(504, min_periods=126).mean()
    drift = _mean(g, 504) * (252.0 / 63.0)
    b = (posfrac - 0.5) * drift
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f20rs_f20_revenue_scale_per_share_spseff_base_v076_signal,
    f20rs_f20_revenue_scale_per_share_reveff_base_v077_signal,
    f20rs_f20_revenue_scale_per_share_spsslopez_base_v078_signal,
    f20rs_f20_revenue_scale_per_share_shbuyback_base_v079_signal,
    f20rs_f20_revenue_scale_per_share_spsceil_base_v080_signal,
    f20rs_f20_revenue_scale_per_share_revfloor_base_v081_signal,
    f20rs_f20_revenue_scale_per_share_spsema_base_v082_signal,
    f20rs_f20_revenue_scale_per_share_revrobustz_base_v083_signal,
    f20rs_f20_revenue_scale_per_share_usdgrz_base_v084_signal,
    f20rs_f20_revenue_scale_per_share_fxtrend_base_v085_signal,
    f20rs_f20_revenue_scale_per_share_fxrank_base_v086_signal,
    f20rs_f20_revenue_scale_per_share_pscouple_base_v087_signal,
    f20rs_f20_revenue_scale_per_share_shaccel_base_v088_signal,
    f20rs_f20_revenue_scale_per_share_cleanps_base_v089_signal,
    f20rs_f20_revenue_scale_per_share_revmemory_base_v090_signal,
    f20rs_f20_revenue_scale_per_share_spsmemory_base_v091_signal,
    f20rs_f20_revenue_scale_per_share_revgrvol_base_v092_signal,
    f20rs_f20_revenue_scale_per_share_spsgrvol2_base_v093_signal,
    f20rs_f20_revenue_scale_per_share_shbaserank_base_v094_signal,
    f20rs_f20_revenue_scale_per_share_revinflect_base_v095_signal,
    f20rs_f20_revenue_scale_per_share_usdconsist_base_v096_signal,
    f20rs_f20_revenue_scale_per_share_spstopband_base_v097_signal,
    f20rs_f20_revenue_scale_per_share_revaccelz_base_v098_signal,
    f20rs_f20_revenue_scale_per_share_spsquality_base_v099_signal,
    f20rs_f20_revenue_scale_per_share_revquality_base_v100_signal,
    f20rs_f20_revenue_scale_per_share_spstrendreg_base_v101_signal,
    f20rs_f20_revenue_scale_per_share_revtrendreg_base_v102_signal,
    f20rs_f20_revenue_scale_per_share_fxsignmag_base_v103_signal,
    f20rs_f20_revenue_scale_per_share_rpsgrkurt_base_v104_signal,
    f20rs_f20_revenue_scale_per_share_psleader_base_v105_signal,
    f20rs_f20_revenue_scale_per_share_revddsm_base_v106_signal,
    f20rs_f20_revenue_scale_per_share_spsddsm_base_v107_signal,
    f20rs_f20_revenue_scale_per_share_dilstreak_base_v108_signal,
    f20rs_f20_revenue_scale_per_share_sizecurve_base_v109_signal,
    f20rs_f20_revenue_scale_per_share_usdpscurv_base_v110_signal,
    f20rs_f20_revenue_scale_per_share_revpersist_base_v111_signal,
    f20rs_f20_revenue_scale_per_share_spspersist_base_v112_signal,
    f20rs_f20_revenue_scale_per_share_revlonggrz_base_v113_signal,
    f20rs_f20_revenue_scale_per_share_spslongrank_base_v114_signal,
    f20rs_f20_revenue_scale_per_share_fxcontrib_base_v115_signal,
    f20rs_f20_revenue_scale_per_share_inflectagree_base_v116_signal,
    f20rs_f20_revenue_scale_per_share_relaccel_base_v117_signal,
    f20rs_f20_revenue_scale_per_share_spsrelaccel_base_v118_signal,
    f20rs_f20_revenue_scale_per_share_sizetier_base_v119_signal,
    f20rs_f20_revenue_scale_per_share_spssizetier_base_v120_signal,
    f20rs_f20_revenue_scale_per_share_rpsweighted_base_v121_signal,
    f20rs_f20_revenue_scale_per_share_fxgapaccel_base_v122_signal,
    f20rs_f20_revenue_scale_per_share_revgracf_base_v123_signal,
    f20rs_f20_revenue_scale_per_share_spsgracf_base_v124_signal,
    f20rs_f20_revenue_scale_per_share_netscale_base_v125_signal,
    f20rs_f20_revenue_scale_per_share_revrecovrate_base_v126_signal,
    f20rs_f20_revenue_scale_per_share_spsrecovrate_base_v127_signal,
    f20rs_f20_revenue_scale_per_share_revturb_base_v128_signal,
    f20rs_f20_revenue_scale_per_share_spsturb_base_v129_signal,
    f20rs_f20_revenue_scale_per_share_fxlevelwedge_base_v130_signal,
    f20rs_f20_revenue_scale_per_share_spsnearpos_base_v131_signal,
    f20rs_f20_revenue_scale_per_share_revnearpos_base_v132_signal,
    f20rs_f20_revenue_scale_per_share_cleanprod_base_v133_signal,
    f20rs_f20_revenue_scale_per_share_sizerankmom_base_v134_signal,
    f20rs_f20_revenue_scale_per_share_spssizerankmom_base_v135_signal,
    f20rs_f20_revenue_scale_per_share_revjerk_base_v136_signal,
    f20rs_f20_revenue_scale_per_share_spsjerk_base_v137_signal,
    f20rs_f20_revenue_scale_per_share_revspan_base_v138_signal,
    f20rs_f20_revenue_scale_per_share_spssqueeze_base_v139_signal,
    f20rs_f20_revenue_scale_per_share_usdvolratio_base_v140_signal,
    f20rs_f20_revenue_scale_per_share_pslead63_base_v141_signal,
    f20rs_f20_revenue_scale_per_share_revstretch_base_v142_signal,
    f20rs_f20_revenue_scale_per_share_spsstretch_base_v143_signal,
    f20rs_f20_revenue_scale_per_share_scalemom_base_v144_signal,
    f20rs_f20_revenue_scale_per_share_diloverhang_base_v145_signal,
    f20rs_f20_revenue_scale_per_share_accellead_base_v146_signal,
    f20rs_f20_revenue_scale_per_share_outgrowdil_base_v147_signal,
    f20rs_f20_revenue_scale_per_share_revdrbal_base_v148_signal,
    f20rs_f20_revenue_scale_per_share_spsdrbal_base_v149_signal,
    f20rs_f20_revenue_scale_per_share_spscompound_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F20_REVENUE_SCALE_PER_SHARE_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500

    def _fund(seed, base=1e8, drift=0.03, vol=0.07, allow_neg=False):
        g = np.random.default_rng(seed)
        steps = np.repeat(g.normal(drift, vol, n // 63 + 1), 63)[:n]
        s = base * np.exp(np.cumsum(steps / 63))
        if allow_neg:
            s = s - base * 0.6
        return pd.Series(s, name=None)

    revenue = _fund(2001, base=2.5e8, drift=0.035, vol=0.08).rename("revenue")
    _rng = np.random.default_rng(2002)
    _fx = 1.0 + 0.18 * np.sin(np.linspace(0, 14, n)) + np.cumsum(_rng.normal(0, 0.006, n))
    _fx = np.clip(_fx, 0.7, 1.5)
    revenueusd = (revenue * _fx).rename("revenueusd")
    shareswa = _fund(2003, base=8e7, drift=0.012, vol=0.02).rename("shareswa")
    sps = _fund(2004, base=3.1, drift=0.03, vol=0.06).rename("sps")

    cols = {"revenue": revenue, "revenueusd": revenueusd,
            "shareswa": shareswa, "sps": sps}

    ALLOW = {
        "open", "high", "low", "close", "closeadj", "volume",
        "revenue", "revenueusd", "deferredrev", "gp", "grossmargin", "opinc", "opex",
        "sgna", "cor", "rnd", "sbcomp", "ebit", "ebitda", "ebitdamargin", "netinc",
        "netinccmn", "netmargin", "eps", "epsdil", "fcf", "fcfps", "ncfo", "ncff",
        "ncfi", "ncfcommon", "ncfdebt", "ncfbus", "capex", "depamor", "sharesbas",
        "shareswa", "shareswadil", "assets", "assetsc", "tangibles", "intangibles",
        "ppnenet", "investments", "inventory", "receivables", "payables", "equity",
        "retearn", "workingcapital", "debt", "debtc", "debtnc", "liabilities",
        "liabilitiesc", "cashneq", "currentratio", "roic", "roe", "roa", "ros",
        "assetturnover", "invcap", "intexp", "taxexp", "ebt", "sps", "bvps", "de",
        "ncfdiv", "dps", "divyield", "payoutratio", "prefdivis",
        "marketcap", "ev", "evebit", "evebitda", "pe", "pb", "ps",
        "shrholders", "shrvalue", "shrunits", "totalvalue", "percentoftotal",
        "fndholders", "undholders", "prfholders", "dbtholders", "putholders",
        "putvalue", "cllholders", "cllvalue", "wntholders", "wntvalue", "dbtvalue",
    }

    n_features = 0
    nan_ok = 0
    results = {}
    for name, meta in REGISTRY.items():
        assert set(meta["inputs"]) <= ALLOW, "%s inputs %s" % (name, meta["inputs"])
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

    print("OK f20_revenue_scale_per_share_base_076_150_claude: %d features pass" % n_features)
