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
# sales-per-share level: log scale of sps (size of per-share revenue)
def f20rs_f20_revenue_scale_per_share_spslevel_base_v001_signal(sps):
    b = _f20_scale(sps)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# sales-per-share 63d log growth
def f20rs_f20_revenue_scale_per_share_spsgr_63d_base_v002_signal(sps):
    b = _f20_loggrowth(sps, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# sales-per-share 126d log growth
def f20rs_f20_revenue_scale_per_share_spsgr_126d_base_v003_signal(sps):
    b = _f20_loggrowth(sps, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# sales-per-share 252d log growth (annual per-share revenue expansion)
def f20rs_f20_revenue_scale_per_share_spsgr_252d_base_v004_signal(sps):
    b = _f20_loggrowth(sps, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# sales-per-share 504d log growth (multi-year per-share scale)
def f20rs_f20_revenue_scale_per_share_spsgr_504d_base_v005_signal(sps):
    b = _f20_loggrowth(sps, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue scale: log of total revenue (company size)
def f20rs_f20_revenue_scale_per_share_revscale_base_v006_signal(revenue):
    b = _f20_scale(revenue)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue 63d log growth
def f20rs_f20_revenue_scale_per_share_revgr_63d_base_v007_signal(revenue):
    b = _f20_loggrowth(revenue, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue 252d log growth
def f20rs_f20_revenue_scale_per_share_revgr_252d_base_v008_signal(revenue):
    b = _f20_loggrowth(revenue, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# constructed revenue-per-share scale, de-trended vs its own 252d mean (level extremity)
def f20rs_f20_revenue_scale_per_share_revpershare_base_v009_signal(revenue, shareswa):
    lrps = _f20_scale(_f20_pershare(revenue, shareswa))
    b = lrps - _mean(lrps, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# constructed revenue-per-share 252d growth, z-scored vs its own 252d history
def f20rs_f20_revenue_scale_per_share_rpsgr_252d_base_v010_signal(revenue, shareswa):
    rps = _f20_pershare(revenue, shareswa)
    g = _f20_loggrowth(rps, 252)
    b = _z(g, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# USD-vs-reported revenue divergence (FX translation gap)
def f20rs_f20_revenue_scale_per_share_fxdiv_base_v011_signal(revenue, revenueusd):
    b = _f20_fxdiverge(revenue, revenueusd)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# USD revenue scale de-trended vs its own 252d EMA (USD size displacement)
def f20rs_f20_revenue_scale_per_share_usdscale_base_v012_signal(revenueusd):
    lu = _f20_scale(revenueusd)
    b = lu - lu.ewm(span=252, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# USD revenue scaling-pace spread: short (63d) USD log-growth minus long (189d) USD
# log-growth, both annualized (is the recent USD size ramp faster than the trailing
# three-quarter pace? an asymmetric window-spread facet with no equal-arm twin)
def f20rs_f20_revenue_scale_per_share_usdpacespread_base_v013_signal(revenueusd):
    g_short = _f20_loggrowth(revenueusd, 63) * (252.0 / 63.0)
    g_long = _f20_loggrowth(revenueusd, 189) * (252.0 / 189.0)
    b = g_short - g_long
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# per-share revenue inflection: sps growth acceleration (252d)
def f20rs_f20_revenue_scale_per_share_spsaccel_252d_base_v014_signal(sps):
    b = _f20_accel(sps, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# per-share revenue inflection: sps growth acceleration (126d)
def f20rs_f20_revenue_scale_per_share_spsaccel_126d_base_v015_signal(sps):
    b = _f20_accel(sps, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# sps z-score vs own 252d history (per-share scale extremity)
def f20rs_f20_revenue_scale_per_share_spsz_252d_base_v016_signal(sps):
    b = _z(sps, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue z-score vs own 252d history
def f20rs_f20_revenue_scale_per_share_revz_252d_base_v017_signal(revenue):
    b = _z(revenue, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# sps short-vs-long growth spread (63d vs 252d per-share momentum)
def f20rs_f20_revenue_scale_per_share_spsgrspr_base_v018_signal(sps):
    s = _f20_loggrowth(sps, 63)
    l = _f20_loggrowth(sps, 252)
    b = s - l
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue short-vs-long growth spread (63d vs 252d)
def f20rs_f20_revenue_scale_per_share_revgrspr_base_v019_signal(revenue):
    s = _f20_loggrowth(revenue, 63)
    l = _f20_loggrowth(revenue, 252)
    b = s - l
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dilution drag intensity: share-growth as a fraction of revenue growth (how much
# of top-line expansion is eaten by dilution), 252d, ranked vs 504d history
def f20rs_f20_revenue_scale_per_share_dildrag_252d_base_v020_signal(revenue, shareswa):
    rg = _f20_loggrowth(revenue, 252)
    shg = _f20_loggrowth(shareswa, 252)
    frac = shg / (rg.abs() + 0.02)
    b = _rank(frac, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# share-count growth (dilution pace), 252d
def f20rs_f20_revenue_scale_per_share_shgr_252d_base_v021_signal(shareswa):
    b = _f20_loggrowth(shareswa, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cumulative dilution wedge: how far log-shares has drifted from its 252d-ago level,
# squashed to bound the cumulative dilution overhang on per-share scale
def f20rs_f20_revenue_scale_per_share_scalegap_base_v022_signal(revenue, shareswa):
    rsc = _f20_scale(revenue)
    rps = _f20_scale(_f20_pershare(revenue, shareswa))
    wedge = rsc - rps
    b = np.tanh(8.0 * (wedge - wedge.shift(126)))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# sps growth percentile rank vs 504d history
def f20rs_f20_revenue_scale_per_share_spsgrrank_base_v023_signal(sps):
    g = _f20_loggrowth(sps, 252)
    b = _rank(g, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# per-share revenue LEVEL percentile rank vs 504d history (where current per-share
# scale sits in its own multi-year size distribution; a SCALE-level facet, not growth)
def f20rs_f20_revenue_scale_per_share_rpslevelrank_base_v024_signal(revenue, shareswa):
    rps = _f20_pershare(revenue, shareswa)
    b = _rank(_f20_scale(rps), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FX divergence z-score vs own 252d history (translation regime shift)
def f20rs_f20_revenue_scale_per_share_fxdivz_base_v025_signal(revenue, revenueusd):
    d = _f20_fxdiverge(revenue, revenueusd)
    b = _z(d, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# USD-vs-reported growth divergence (252d growth gap)
def f20rs_f20_revenue_scale_per_share_usdgrgap_base_v026_signal(revenue, revenueusd):
    rg = _f20_loggrowth(revenue, 252)
    ug = _f20_loggrowth(revenueusd, 252)
    b = rg - ug
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# sps growth stability: mean/std of 63d growth over 252d (smooth compounding)
def f20rs_f20_revenue_scale_per_share_spsstab_base_v027_signal(sps):
    g = _f20_loggrowth(sps, 63)
    m = _mean(g, 252)
    sd = _std(g, 252).replace(0, np.nan)
    b = m / sd
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue growth stability (info-ratio of 63d growth over 252d)
def f20rs_f20_revenue_scale_per_share_revstab_base_v028_signal(revenue):
    g = _f20_loggrowth(revenue, 63)
    m = _mean(g, 252)
    sd = _std(g, 252).replace(0, np.nan)
    b = m / sd
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# sps distance from its 252d max (per-share scale drawdown)
def f20rs_f20_revenue_scale_per_share_spsdd_base_v029_signal(sps):
    hi = _rmax(sps, 252)
    b = sps / hi.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue size dispersion: 252d rolling std of log-revenue divided by its 252d mean level
# (coefficient-of-variation of the SIZE LEVEL -- how stretched the revenue scale has been
# over the window; a level-dispersion facet, not a growth-direction count)
def f20rs_f20_revenue_scale_per_share_revsizedisp_base_v030_signal(revenue):
    ls = _f20_scale(revenue)
    b = _std(ls, 252) / _mean(ls, 252).abs().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# sps rebound momentum: change over a quarter in recovery-off-252d-min (rebound accel)
def f20rs_f20_revenue_scale_per_share_spsrecov_base_v031_signal(sps):
    lo = _rmin(sps, 252)
    rec = sps / lo.replace(0, np.nan) - 1.0
    b = rec - rec.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue range position within 504d scale band, z-scored vs its own 252d history
def f20rs_f20_revenue_scale_per_share_revrngpos_base_v032_signal(revenue):
    hi = _rmax(revenue, 504)
    lo = _rmin(revenue, 504)
    pos = (revenue - lo) / (hi - lo).replace(0, np.nan)
    b = _z(pos, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# sps range-position momentum: quarter-over-quarter change in 504d band position
def f20rs_f20_revenue_scale_per_share_spsrngpos_base_v033_signal(sps):
    hi = _rmax(sps, 504)
    lo = _rmin(sps, 504)
    pos = (sps - lo) / (hi - lo).replace(0, np.nan)
    b = pos - pos.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# per-share scale efficiency: sps growth per unit of dilution (252d)
def f20rs_f20_revenue_scale_per_share_spspereff_base_v034_signal(sps, shareswa):
    spsg = _f20_loggrowth(sps, 252)
    shg = _f20_loggrowth(shareswa, 252).abs() + 0.01
    b = spsg / shg
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# per-share scale dispersion across windows: std of rps log-growth measured over
# 63/126/252/504 windows (term-structure spread of per-share scaling, a curvature/
# dispersion facet distinct from any single-window per-share acceleration)
def f20rs_f20_revenue_scale_per_share_rpstermdisp_base_v035_signal(revenue, shareswa):
    rps = _f20_pershare(revenue, shareswa)
    g1 = _f20_loggrowth(rps, 63) * (252.0 / 63.0)
    g2 = _f20_loggrowth(rps, 126) * (252.0 / 126.0)
    g3 = _f20_loggrowth(rps, 252)
    g4 = _f20_loggrowth(rps, 504) * (252.0 / 504.0)
    b = pd.concat([g1, g2, g3, g4], axis=1).std(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# sps 21d sequential growth (near-term per-share revenue momentum)
def f20rs_f20_revenue_scale_per_share_spsseq_21d_base_v036_signal(sps):
    b = _f20_loggrowth(sps, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue 21d sequential growth
def f20rs_f20_revenue_scale_per_share_revseq_21d_base_v037_signal(revenue):
    b = _f20_loggrowth(revenue, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# sps CAGR durability: annualized 504d growth, z-scored vs its own 252d history
def f20rs_f20_revenue_scale_per_share_spscagr_base_v038_signal(sps):
    cagr = _f20_loggrowth(sps, 504) * (252.0 / 504.0)
    b = _z(cagr, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dilution-adjusted scaling smoothness: net 504d per-share (sps) log-gain net of the
# 504d share-count log-gain, divided by the summed absolute 63d per-share moves over the
# window (a directionality/efficiency ratio of clean per-share compounding -- high when
# per-share scale advanced in a straight line; uses shareswa, distinct from any CAGR rank)
def f20rs_f20_revenue_scale_per_share_cleaneff_base_v039_signal(sps, shareswa):
    net = _f20_loggrowth(sps, 504) - _f20_loggrowth(shareswa, 504)
    path = _f20_loggrowth(sps, 63).abs().rolling(504, min_periods=252).sum()
    b = net / path.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# USD revenue scale convexity: signed squared z of USD log-scale (size-extremity)
def f20rs_f20_revenue_scale_per_share_usdscalerank_base_v040_signal(revenueusd):
    z = _z(_f20_scale(revenueusd), 504)
    b = np.sign(z) * (z.abs() ** 1.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# sps vs its slow EMA (per-share scale displacement)
def f20rs_f20_revenue_scale_per_share_spsdisp_base_v041_signal(sps):
    ls = _f20_scale(sps)
    b = ls - ls.ewm(span=126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue vs its slow EMA (revenue scale displacement)
def f20rs_f20_revenue_scale_per_share_revdisp_base_v042_signal(revenue):
    ls = _f20_scale(revenue)
    b = ls - ls.ewm(span=126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# per-share vs total scale co-movement: 252d rolling correlation between log-sps and
# log-revenue levels (when buybacks/dilution decouple per-share scale from total size the
# correlation drops; a level-coupling facet that does not collapse to share-growth)
def f20rs_f20_revenue_scale_per_share_pstotcouple_base_v043_signal(sps, revenue):
    ls = _f20_scale(sps)
    lr = _f20_scale(revenue)
    b = ls.rolling(252, min_periods=126).corr(lr)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FX divergence momentum (change in translation gap over a quarter)
def f20rs_f20_revenue_scale_per_share_fxdivmom_base_v044_signal(revenue, revenueusd):
    d = _f20_fxdiverge(revenue, revenueusd)
    b = d - d.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# per-share growth breadth minus magnitude: tanh of revenue growth net of share growth
def f20rs_f20_revenue_scale_per_share_spsgrtanh_base_v045_signal(revenue, shareswa):
    rg = _f20_loggrowth(revenue, 126)
    shg = _f20_loggrowth(shareswa, 126)
    b = np.tanh(4.0 * (rg - shg)) - np.tanh(4.0 * rg)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue-per-share scale times growth (large & growing per-share, sign-magnitude)
def f20rs_f20_revenue_scale_per_share_rpsscalexgr_base_v046_signal(revenue, shareswa):
    rps = _f20_pershare(revenue, shareswa)
    g = _f20_loggrowth(rps, 252)
    b = np.sign(g) * (g.abs() ** 0.5) * _z(_f20_scale(rps), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# shareswa scale (log share base, dilution size context)
def f20rs_f20_revenue_scale_per_share_shscale_base_v047_signal(shareswa):
    b = _z(_f20_scale(shareswa), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue growth acceleration (252d level of accel)
def f20rs_f20_revenue_scale_per_share_revaccel_252d_base_v048_signal(revenue):
    b = _f20_accel(revenue, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# USD revenue growth acceleration (126d)
def f20rs_f20_revenue_scale_per_share_usdaccel_126d_base_v049_signal(revenueusd):
    b = _f20_accel(revenueusd, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# sps growth risk-adjusted by per-share scale volatility (252d)
def f20rs_f20_revenue_scale_per_share_spsgrvol_base_v050_signal(sps):
    g = _f20_loggrowth(sps, 63)
    vol = _std(_f20_loggrowth(sps, 21), 252).replace(0, np.nan)
    b = g / vol
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue scale percentile rank vs 504d (size-tier position)
def f20rs_f20_revenue_scale_per_share_revscalerank_base_v051_signal(revenue):
    b = _rank(_f20_scale(revenue), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# per-share revenue inflection sign: is sps growth now above its 252d typical?
def f20rs_f20_revenue_scale_per_share_spsinflect_base_v052_signal(sps):
    g = _f20_loggrowth(sps, 63)
    typ = _mean(g, 252)
    b = g - typ
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# per-share revenue growth skew: 252d rolling skewness of 21d rps log-growth
# (asymmetry of the per-share scaling path: jumpy up vs grinding down)
def f20rs_f20_revenue_scale_per_share_rpsgrskew_base_v053_signal(revenue, shareswa):
    rps = _f20_pershare(revenue, shareswa)
    g = _f20_loggrowth(rps, 21)
    b = g.rolling(252, min_periods=126).skew()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# sps year-over-year growth change (acceleration via two annual windows)
def f20rs_f20_revenue_scale_per_share_spsyoychg_base_v054_signal(sps):
    g = _f20_loggrowth(sps, 252)
    b = g - g.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue scale convexity: squared deviation from 252d mean (scale dispersion)
def f20rs_f20_revenue_scale_per_share_revconvex_base_v055_signal(revenue):
    ls = _f20_scale(revenue)
    z = _z(ls, 252)
    b = np.sign(z) * (z ** 2)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# scale-vs-growth quadrant: sps size-rank combined with sps growth-rank
# (big-and-growing per-share signature; both percentile facets)
def f20rs_f20_revenue_scale_per_share_scalecomp_base_v056_signal(sps):
    rsize = _rank(_f20_scale(sps), 504)
    rgrow = _rank(_f20_loggrowth(sps, 126), 504)
    b = rsize * rgrow
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth balance: signed gap between revenue and sps 252d growth, z-scored (which scales faster)
def f20rs_f20_revenue_scale_per_share_grcomp_base_v057_signal(revenue, sps):
    g1 = _f20_loggrowth(revenue, 252)
    g2 = _f20_loggrowth(sps, 252)
    b = _z(g1 - g2, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FX divergence absolute magnitude smoothed (translation exposure intensity)
def f20rs_f20_revenue_scale_per_share_fxmag_base_v058_signal(revenue, revenueusd):
    d = _f20_fxdiverge(revenue, revenueusd).abs()
    b = _mean(d, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# sps 126d momentum smoothed by EMA (persistent per-share trend)
def f20rs_f20_revenue_scale_per_share_spsmomema_base_v059_signal(sps):
    g = _f20_loggrowth(sps, 126)
    b = g.ewm(span=63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dilution-penalized scale gain: revenue 252d growth minus 3x share-growth, ranked
def f20rs_f20_revenue_scale_per_share_cleanscale_base_v060_signal(revenue, shareswa):
    rg = _f20_loggrowth(revenue, 252)
    shg = _f20_loggrowth(shareswa, 252)
    penalized = rg - 3.0 * shg
    b = _rank(penalized, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# USD-per-share scale band position: where USD-per-share sits in its 504d log-range,
# centered (a bounded 0-centered level position, distinct from z-score / skew facets)
def f20rs_f20_revenue_scale_per_share_usdpsband_base_v061_signal(revenueusd, shareswa):
    ls = _f20_scale(_f20_pershare(revenueusd, shareswa))
    hi = _rmax(ls, 504)
    lo = _rmin(ls, 504)
    b = (ls - lo) / (hi - lo).replace(0, np.nan) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# USD per-share revenue inflection: 126d acceleration of USD-per-share, z-scored
def f20rs_f20_revenue_scale_per_share_usdpsgr_base_v062_signal(revenueusd, shareswa):
    ups = _f20_pershare(revenueusd, shareswa)
    a = _f20_accel(ups, 126)
    b = _z(a, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# sps growth-term curvature: convexity across 63/126/252 annual-growth windows
def f20rs_f20_revenue_scale_per_share_spsgrdisp_base_v063_signal(sps):
    g1 = _f20_loggrowth(sps, 63) * (252.0 / 63.0)
    g2 = _f20_loggrowth(sps, 126) * (252.0 / 126.0)
    g3 = _f20_loggrowth(sps, 252)
    b = g1 - 2.0 * g2 + g3
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue scale streak: fraction of last year revenue made new 252d highs
def f20rs_f20_revenue_scale_per_share_revhifreq_base_v064_signal(revenue):
    hi = _rmax(revenue, 252)
    is_hi = (revenue >= hi * 0.99999).astype(float)
    b = is_hi.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# sps scale streak: fraction of last year sps at new 252d highs (per-share records)
def f20rs_f20_revenue_scale_per_share_spshifreq_base_v065_signal(sps):
    hi = _rmax(sps, 252)
    is_hi = (sps >= hi * 0.99999).astype(float)
    b = is_hi.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue contraction-quarter count (quarters of negative 63d growth in last year)
def f20rs_f20_revenue_scale_per_share_revcontract_base_v066_signal(revenue):
    g = _f20_loggrowth(revenue, 63)
    neg = (g < 0).astype(float)
    b = neg.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# sps acceleration smoothed and EMA-persisted (durable per-share inflection)
def f20rs_f20_revenue_scale_per_share_spsaccelrank_base_v067_signal(sps):
    a = _f20_accel(sps, 63)
    b = a.ewm(span=126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue-per-share floor cushion: log distance of rps above its trailing 504d min,
# z-scored vs its own 252d history (how much per-share scale has built off the trough)
def f20rs_f20_revenue_scale_per_share_rpsfloor_base_v068_signal(revenue, shareswa):
    rps = _f20_pershare(revenue, shareswa)
    lo = _rmin(rps, 504)
    cushion = np.log(rps.replace(0, np.nan) / lo.replace(0, np.nan))
    b = _z(cushion, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FX translation instability: rolling 126d std of the log(usd/reported) gap
def f20rs_f20_revenue_scale_per_share_fxscalegap_base_v069_signal(revenue, revenueusd):
    gap = _f20_scale(revenueusd) - _f20_scale(revenue)
    b = _std(gap, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# per-share scale pain index: average depth below the trailing 252d peak over the last
# 126d (continuous sustained-per-share-contraction facet; deeper & longer = more negative)
def f20rs_f20_revenue_scale_per_share_spspain_base_v070_signal(sps):
    hi = _rmax(sps, 252)
    underwater = (sps / hi.replace(0, np.nan) - 1.0).clip(upper=0.0)
    b = underwater.rolling(126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue growth minus USD growth, smoothed (FX-driven growth wedge)
def f20rs_f20_revenue_scale_per_share_fxgrwedge_base_v071_signal(revenue, revenueusd):
    rg = _f20_loggrowth(revenue, 126)
    ug = _f20_loggrowth(revenueusd, 126)
    b = (rg - ug).ewm(span=63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# per-share scale momentum vs share-base momentum: dilution-adjusted ratio rank
def f20rs_f20_revenue_scale_per_share_psvssh_base_v072_signal(sps, shareswa):
    spsg = _f20_loggrowth(sps, 252)
    shg = _f20_loggrowth(shareswa, 252).abs() + 0.005
    ratio = spsg / shg
    b = _rank(ratio, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# per-share inflection regime: fraction of last 252d that sps acceleration (126d) was
# positive, centered (count facet of sustained per-share scaling inflection; uses sps
# so distinct from f18 raw-revenue acceleration rank)
def f20rs_f20_revenue_scale_per_share_spsinflectreg_base_v073_signal(sps):
    a = _f20_accel(sps, 126)
    pos = (a > 0).astype(float)
    b = pos.rolling(252, min_periods=126).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# combined per-share inflection: sps accel sign times revenue growth magnitude
def f20rs_f20_revenue_scale_per_share_inflectx_base_v074_signal(sps, revenue):
    a = _f20_accel(sps, 126)
    rg = _f20_loggrowth(revenue, 126)
    b = np.sign(a) * rg.abs()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# durable per-share scaling: sps growth held positive fraction of last year
def f20rs_f20_revenue_scale_per_share_spsdurable_base_v075_signal(sps):
    g = _f20_loggrowth(sps, 63)
    pos = (g > 0).astype(float)
    frac = pos.rolling(252, min_periods=126).mean()
    b = frac * _mean(g, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f20rs_f20_revenue_scale_per_share_spslevel_base_v001_signal,
    f20rs_f20_revenue_scale_per_share_spsgr_63d_base_v002_signal,
    f20rs_f20_revenue_scale_per_share_spsgr_126d_base_v003_signal,
    f20rs_f20_revenue_scale_per_share_spsgr_252d_base_v004_signal,
    f20rs_f20_revenue_scale_per_share_spsgr_504d_base_v005_signal,
    f20rs_f20_revenue_scale_per_share_revscale_base_v006_signal,
    f20rs_f20_revenue_scale_per_share_revgr_63d_base_v007_signal,
    f20rs_f20_revenue_scale_per_share_revgr_252d_base_v008_signal,
    f20rs_f20_revenue_scale_per_share_revpershare_base_v009_signal,
    f20rs_f20_revenue_scale_per_share_rpsgr_252d_base_v010_signal,
    f20rs_f20_revenue_scale_per_share_fxdiv_base_v011_signal,
    f20rs_f20_revenue_scale_per_share_usdscale_base_v012_signal,
    f20rs_f20_revenue_scale_per_share_usdpacespread_base_v013_signal,
    f20rs_f20_revenue_scale_per_share_spsaccel_252d_base_v014_signal,
    f20rs_f20_revenue_scale_per_share_spsaccel_126d_base_v015_signal,
    f20rs_f20_revenue_scale_per_share_spsz_252d_base_v016_signal,
    f20rs_f20_revenue_scale_per_share_revz_252d_base_v017_signal,
    f20rs_f20_revenue_scale_per_share_spsgrspr_base_v018_signal,
    f20rs_f20_revenue_scale_per_share_revgrspr_base_v019_signal,
    f20rs_f20_revenue_scale_per_share_dildrag_252d_base_v020_signal,
    f20rs_f20_revenue_scale_per_share_shgr_252d_base_v021_signal,
    f20rs_f20_revenue_scale_per_share_scalegap_base_v022_signal,
    f20rs_f20_revenue_scale_per_share_spsgrrank_base_v023_signal,
    f20rs_f20_revenue_scale_per_share_rpslevelrank_base_v024_signal,
    f20rs_f20_revenue_scale_per_share_fxdivz_base_v025_signal,
    f20rs_f20_revenue_scale_per_share_usdgrgap_base_v026_signal,
    f20rs_f20_revenue_scale_per_share_spsstab_base_v027_signal,
    f20rs_f20_revenue_scale_per_share_revstab_base_v028_signal,
    f20rs_f20_revenue_scale_per_share_spsdd_base_v029_signal,
    f20rs_f20_revenue_scale_per_share_revsizedisp_base_v030_signal,
    f20rs_f20_revenue_scale_per_share_spsrecov_base_v031_signal,
    f20rs_f20_revenue_scale_per_share_revrngpos_base_v032_signal,
    f20rs_f20_revenue_scale_per_share_spsrngpos_base_v033_signal,
    f20rs_f20_revenue_scale_per_share_spspereff_base_v034_signal,
    f20rs_f20_revenue_scale_per_share_rpstermdisp_base_v035_signal,
    f20rs_f20_revenue_scale_per_share_spsseq_21d_base_v036_signal,
    f20rs_f20_revenue_scale_per_share_revseq_21d_base_v037_signal,
    f20rs_f20_revenue_scale_per_share_spscagr_base_v038_signal,
    f20rs_f20_revenue_scale_per_share_cleaneff_base_v039_signal,
    f20rs_f20_revenue_scale_per_share_usdscalerank_base_v040_signal,
    f20rs_f20_revenue_scale_per_share_spsdisp_base_v041_signal,
    f20rs_f20_revenue_scale_per_share_revdisp_base_v042_signal,
    f20rs_f20_revenue_scale_per_share_pstotcouple_base_v043_signal,
    f20rs_f20_revenue_scale_per_share_fxdivmom_base_v044_signal,
    f20rs_f20_revenue_scale_per_share_spsgrtanh_base_v045_signal,
    f20rs_f20_revenue_scale_per_share_rpsscalexgr_base_v046_signal,
    f20rs_f20_revenue_scale_per_share_shscale_base_v047_signal,
    f20rs_f20_revenue_scale_per_share_revaccel_252d_base_v048_signal,
    f20rs_f20_revenue_scale_per_share_usdaccel_126d_base_v049_signal,
    f20rs_f20_revenue_scale_per_share_spsgrvol_base_v050_signal,
    f20rs_f20_revenue_scale_per_share_revscalerank_base_v051_signal,
    f20rs_f20_revenue_scale_per_share_spsinflect_base_v052_signal,
    f20rs_f20_revenue_scale_per_share_rpsgrskew_base_v053_signal,
    f20rs_f20_revenue_scale_per_share_spsyoychg_base_v054_signal,
    f20rs_f20_revenue_scale_per_share_revconvex_base_v055_signal,
    f20rs_f20_revenue_scale_per_share_scalecomp_base_v056_signal,
    f20rs_f20_revenue_scale_per_share_grcomp_base_v057_signal,
    f20rs_f20_revenue_scale_per_share_fxmag_base_v058_signal,
    f20rs_f20_revenue_scale_per_share_spsmomema_base_v059_signal,
    f20rs_f20_revenue_scale_per_share_cleanscale_base_v060_signal,
    f20rs_f20_revenue_scale_per_share_usdpsband_base_v061_signal,
    f20rs_f20_revenue_scale_per_share_usdpsgr_base_v062_signal,
    f20rs_f20_revenue_scale_per_share_spsgrdisp_base_v063_signal,
    f20rs_f20_revenue_scale_per_share_revhifreq_base_v064_signal,
    f20rs_f20_revenue_scale_per_share_spshifreq_base_v065_signal,
    f20rs_f20_revenue_scale_per_share_revcontract_base_v066_signal,
    f20rs_f20_revenue_scale_per_share_spsaccelrank_base_v067_signal,
    f20rs_f20_revenue_scale_per_share_rpsfloor_base_v068_signal,
    f20rs_f20_revenue_scale_per_share_fxscalegap_base_v069_signal,
    f20rs_f20_revenue_scale_per_share_spspain_base_v070_signal,
    f20rs_f20_revenue_scale_per_share_fxgrwedge_base_v071_signal,
    f20rs_f20_revenue_scale_per_share_psvssh_base_v072_signal,
    f20rs_f20_revenue_scale_per_share_spsinflectreg_base_v073_signal,
    f20rs_f20_revenue_scale_per_share_inflectx_base_v074_signal,
    f20rs_f20_revenue_scale_per_share_spsdurable_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F20_REVENUE_SCALE_PER_SHARE_REGISTRY_001_075 = REGISTRY


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

    print("OK f20_revenue_scale_per_share_base_001_075_claude: %d features pass" % n_features)
