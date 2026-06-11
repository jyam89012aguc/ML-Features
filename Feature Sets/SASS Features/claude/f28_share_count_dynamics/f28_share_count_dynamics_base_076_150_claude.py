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


def _roc(s, w):
    return s / s.shift(w).replace(0, np.nan) - 1.0


def _logchg(s, w):
    return np.log(s.replace(0, np.nan) / s.shift(w).replace(0, np.nan))


def _rank(s, w):
    return s.rolling(w, min_periods=max(1, w // 3)).rank(pct=True) - 0.5


def _slope(s, w):
    idx = np.arange(w, dtype=float)
    idx = idx - idx.mean()
    denom = (idx ** 2).sum()

    def _f(a):
        if np.any(np.isnan(a)):
            return np.nan
        return float((idx * (a - a.mean())).sum() / denom)
    return s.rolling(w, min_periods=w).apply(_f, raw=True)


# ===== folder domain primitives (share-count dynamics) =====
def _f28_dilution(shares, w):
    return shares / shares.shift(w).replace(0, np.nan) - 1.0


def _f28_creep(shareswadil, shareswa):
    return shareswadil / shareswa.replace(0, np.nan) - 1.0


def _f28_buyback_intensity(ncfcommon, shares):
    return (-ncfcommon) / shares.replace(0, np.nan)


def _f28_net_issuance(ncfcommon, w):
    return ncfcommon.rolling(w, min_periods=max(1, w // 2)).sum()


def _f28_dilution_streak(shares, w):
    up = (shares.diff() > 0).astype(float)
    return up.rolling(w, min_periods=max(1, w // 2)).mean()


# ============================================================
# weekly dilution pace (very short share-count change)
def f28sc_f28_share_count_dynamics_dilbas_21d_base_v076_signal(sharesbas):
    b = _f28_dilution(sharesbas, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# half-year basic dilution
def f28sc_f28_share_count_dynamics_dilbas_126d_base_v077_signal(sharesbas):
    b = _f28_dilution(sharesbas, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# long-run basic dilution inflection: 504d pace relative to its 252d-ago value
def f28sc_f28_share_count_dynamics_dilbas_1260d_base_v078_signal(sharesbas):
    g = _logchg(sharesbas, 504)
    b = g - g.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# basic dilution z-scored over a five-year window (long de-trended pace)
def f28sc_f28_share_count_dynamics_dilbasz_504d_base_v079_signal(sharesbas):
    g = _logchg(sharesbas, 252)
    b = _z(g, 1260)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# weighted-average dilution five-year, percentile-ranked
def f28sc_f28_share_count_dynamics_dilwarank_1260d_base_v080_signal(shareswa):
    g = _logchg(shareswa, 252)
    b = _rank(g, 1260)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# weighted-average dilution half-year
def f28sc_f28_share_count_dynamics_dilwa_126d_base_v081_signal(shareswa):
    b = _f28_dilution(shareswa, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# weighted-average dilution dispersion across two years (erratic vs steady)
def f28sc_f28_share_count_dynamics_dilwadisp_504d_base_v082_signal(shareswa):
    g = _logchg(shareswa, 63)
    b = _std(g, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# weighted-average dilution tanh-bounded annual pace (squashed level)
def f28sc_f28_share_count_dynamics_dilwatanh_252d_base_v083_signal(shareswa):
    g = _logchg(shareswa, 252)
    b = np.tanh(20.0 * g)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# diluted-minus-basic half-year growth spread (overhang-specific dilution, half-year)
def f28sc_f28_share_count_dynamics_dildil_126d_base_v084_signal(shareswadil, sharesbas):
    gd = _logchg(shareswadil, 126)
    gb = _logchg(sharesbas, 126)
    b = gd - gb
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# diluted-share five-year dilution, de-trended vs its own 252d baseline
def f28sc_f28_share_count_dynamics_dildil_1260d_base_v085_signal(shareswadil):
    g = _logchg(shareswadil, 1260)
    b = g - g.rolling(252, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# creep momentum: change in diluted-creep over a quarter
def f28sc_f28_share_count_dynamics_creepmom_63d_base_v086_signal(shareswadil, shareswa):
    c = _f28_creep(shareswadil, shareswa)
    b = c - c.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# creep relative to its own five-year minimum (overhang vs cleanest level)
def f28sc_f28_share_count_dynamics_creepvsmin_1260d_base_v087_signal(shareswadil, shareswa):
    c = _f28_creep(shareswadil, shareswa)
    cmin = _rmin(c, 1260)
    b = c - cmin
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# creep smoothed (persistent overhang regime)
def f28sc_f28_share_count_dynamics_creepema_base_v088_signal(shareswadil, shareswa):
    c = _f28_creep(shareswadil, shareswa)
    b = c.ewm(span=126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# creep z-scored over a two-year window (de-trended overhang extremity)
def f28sc_f28_share_count_dynamics_creeprngpos_504d_base_v089_signal(shareswadil, shareswa):
    c = _f28_creep(shareswadil, shareswa)
    b = _z(c, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# buyback intensity five-year smoothed (long repurchase commitment)
def f28sc_f28_share_count_dynamics_bbintens_252d_base_v090_signal(ncfcommon, sharesbas):
    raw = _f28_buyback_intensity(ncfcommon, sharesbas)
    b = raw.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# buyback intensity momentum (change in repurchase pace over a quarter)
def f28sc_f28_share_count_dynamics_bbintensmom_63d_base_v091_signal(ncfcommon, sharesbas):
    raw = (-ncfcommon).rolling(63, min_periods=21).sum() / sharesbas.replace(0, np.nan)
    b = raw - raw.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net common flow purity over two years (long directional consistency)
def f28sc_f28_share_count_dynamics_ncfpurity_504d_base_v092_signal(ncfcommon):
    net = ncfcommon.rolling(504, min_periods=252).sum()
    gross = ncfcommon.abs().rolling(504, min_periods=252).sum()
    b = net / gross.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net common flow level z-scored over five years (issuance extremity)
def f28sc_f28_share_count_dynamics_ncfz_1260d_base_v093_signal(ncfcommon):
    q = ncfcommon.rolling(63, min_periods=21).sum()
    b = _z(q, 1260)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# share-count trend on weighted-average over five years (long dilution trajectory)
def f28sc_f28_share_count_dynamics_trendwa_1260d_base_v094_signal(shareswa):
    lg = np.log(shareswa.replace(0, np.nan))
    b = _slope(lg, 1260)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# trend on diluted shares minus trend on basic (overhang trajectory divergence)
def f28sc_f28_share_count_dynamics_trenddiv_252d_base_v095_signal(shareswadil, sharesbas):
    sd = _slope(np.log(shareswadil.replace(0, np.nan)), 252)
    sb = _slope(np.log(sharesbas.replace(0, np.nan)), 252)
    b = sd - sb
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# share-count trend half-year curvature (short vs medium dilution slope)
def f28sc_f28_share_count_dynamics_trendcurv_126d_base_v096_signal(shareswa):
    lg = np.log(shareswa.replace(0, np.nan))
    short = _slope(lg, 21)
    med = _slope(lg, 126)
    b = short - med
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dilution streak on weighted-average shares over half-year
def f28sc_f28_share_count_dynamics_dilstreak_126d_base_v097_signal(shareswa):
    b = _f28_dilution_streak(shareswa, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dilution streak depth: streak z-scored over five years
def f28sc_f28_share_count_dynamics_dilstreakz_1260d_base_v098_signal(sharesbas):
    streak = _f28_dilution_streak(sharesbas, 252)
    b = _z(streak, 1260)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net issuance acceleration: annual net flow vs prior annual net flow
def f28sc_f28_share_count_dynamics_issaccel_252d_base_v099_signal(ncfcommon):
    net = ncfcommon.rolling(252, min_periods=126).sum()
    sm = np.sign(net) * np.log1p(net.abs())
    b = sm - sm.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# share-count distance below five-year max (depth of buyback off peak count)
def f28sc_f28_share_count_dynamics_belowmax_1260d_base_v100_signal(sharesbas):
    rmax = _rmax(sharesbas, 1260)
    b = np.log(sharesbas.replace(0, np.nan) / rmax.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# share-count percentile-rank within its five-year history (issuance cycle, robust)
def f28sc_f28_share_count_dynamics_countrngpos_1260d_base_v101_signal(sharesbas):
    detr = sharesbas / _mean(sharesbas, 252).replace(0, np.nan)
    b = _rank(detr, 1260)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# share-count deviation from its 504d mean (level disequilibrium)
def f28sc_f28_share_count_dynamics_countdev_504d_base_v102_signal(sharesbas):
    m = _mean(sharesbas, 504)
    b = sharesbas / m.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# basic-vs-weighted divergence percentile-ranked (issuance-timing extremity)
def f28sc_f28_share_count_dynamics_baswadivrank_252d_base_v103_signal(sharesbas, shareswa):
    d = sharesbas / shareswa.replace(0, np.nan) - 1.0
    b = _rank(d, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# basic-vs-weighted divergence smoothed momentum (mid-period issuance trend)
def f28sc_f28_share_count_dynamics_baswadivmom_63d_base_v104_signal(sharesbas, shareswa):
    d = sharesbas / shareswa.replace(0, np.nan) - 1.0
    b = d.ewm(span=42, min_periods=21).mean() - d.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dilution per unit of issuance dispersion (risk-adjusted long dilution)
def f28sc_f28_share_count_dynamics_dilvol_504d_base_v105_signal(sharesbas):
    g = _logchg(sharesbas, 504)
    vol = _std(_logchg(sharesbas, 63), 504)
    b = g / vol.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# annual dilution scaled by net-issuance purity (dilution that is cash-funded vs not)
def f28sc_f28_share_count_dynamics_dilwasignmag_252d_base_v106_signal(shareswa, ncfcommon):
    g = _logchg(shareswa, 252)
    net = ncfcommon.rolling(252, min_periods=126).sum()
    gross = ncfcommon.abs().rolling(252, min_periods=126).sum()
    pur = net / gross.replace(0, np.nan)
    b = np.tanh(15.0 * g) * pur
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# buyback intensity percentile-ranked over five years (relative repurchase strength)
def f28sc_f28_share_count_dynamics_bbrank_1260d_base_v107_signal(ncfcommon, sharesbas):
    raw = (-ncfcommon).rolling(252, min_periods=126).sum() / sharesbas.replace(0, np.nan)
    b = _rank(raw, 1260)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# creep trajectory acceleration: half-year creep slope minus its quarter-ago slope
def f28sc_f28_share_count_dynamics_creeptrend_1260d_base_v108_signal(shareswadil, shareswa):
    c = _f28_creep(shareswadil, shareswa)
    sl = _slope(c, 126)
    b = sl - sl.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# overhang-spread dispersion: volatility of the diluted-minus-basic quarterly growth gap
def f28sc_f28_share_count_dynamics_dildildisp_504d_base_v109_signal(shareswadil, sharesbas):
    gap = _logchg(shareswadil, 63) - _logchg(sharesbas, 63)
    b = _std(gap, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net common flow EMA over a year (smoothed issuance/buyback tilt, long)
def f28sc_f28_share_count_dynamics_ncfema_252d_base_v110_signal(ncfcommon):
    q = ncfcommon.rolling(21, min_periods=10).sum()
    s = q.ewm(span=252, min_periods=84).mean()
    b = np.sign(s) * np.log1p(s.abs())
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# multi-horizon dilution disagreement on weighted-average (126/252/504)
def f28sc_f28_share_count_dynamics_dilwamultidisp_base_v111_signal(shareswa):
    g1 = _logchg(shareswa, 126)
    g2 = _logchg(shareswa, 252)
    g3 = _logchg(shareswa, 504)
    b = pd.concat([g1, g2, g3], axis=1).std(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dilution efficiency-ratio on weighted-average (smoothness of count growth)
def f28sc_f28_share_count_dynamics_diler_504d_base_v112_signal(shareswa):
    lg = np.log(shareswa.replace(0, np.nan))
    net = (lg - lg.shift(504)).abs()
    path = lg.diff().abs().rolling(504, min_periods=252).sum()
    b = net / path.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# diluted-share growth vs its slow EMA (long dilution impulse on diluted count)
def f28sc_f28_share_count_dynamics_dilimpulse_252d_base_v113_signal(shareswadil):
    g = _logchg(shareswadil, 252)
    b = g - g.ewm(span=504, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# buyback-vs-dilution net stance (z-scored buyback rate minus z-scored dilution)
def f28sc_f28_share_count_dynamics_netstance_252d_base_v114_signal(ncfcommon, sharesbas):
    bb = (-ncfcommon).rolling(252, min_periods=126).sum() / sharesbas.replace(0, np.nan)
    dil = _logchg(sharesbas, 252)
    b = _z(bb, 504) - _z(dil, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# creep x diluted-growth sign (overhang building while diluting)
def f28sc_f28_share_count_dynamics_creepxdilsign_base_v115_signal(shareswadil, shareswa):
    creep = _f28_creep(shareswadil, shareswa)
    gd = _logchg(shareswadil, 126)
    b = creep * np.sign(gd)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of five years with rising diluted count (long overhang-growth persistence)
def f28sc_f28_share_count_dynamics_dildilstreak_1260d_base_v116_signal(shareswadil):
    b = _f28_dilution_streak(shareswadil, 1260)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net common flow relative to its five-year max issuance (issuance headroom)
def f28sc_f28_share_count_dynamics_issvsmax_1260d_base_v117_signal(ncfcommon):
    q = ncfcommon.rolling(252, min_periods=126).sum()
    qmax = _rmax(q, 1260)
    b = np.sign(q - qmax) * np.log1p((qmax - q).abs())
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# diluted-creep convexity over five years (squared overhang deviation)
def f28sc_f28_share_count_dynamics_creepconv_1260d_base_v118_signal(shareswadil, shareswa):
    c = _f28_creep(shareswadil, shareswa)
    dev = c - c.rolling(1260, min_periods=504).mean()
    b = np.sign(dev) * (dev ** 2)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dilution YoY acceleration on basic (second difference of annual pace)
def f28sc_f28_share_count_dynamics_dilaccel_252d_base_v119_signal(sharesbas):
    g = _logchg(sharesbas, 252)
    b = (g - g.shift(126)) - (g.shift(126) - g.shift(252))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# buyback-driven count reduction quality over five years (clean compounders)
def f28sc_f28_share_count_dynamics_reductqual_1260d_base_v120_signal(ncfcommon, sharesbas):
    net = ncfcommon.rolling(504, min_periods=252).sum()
    gross = ncfcommon.abs().rolling(504, min_periods=252).sum()
    pur = -net / gross.replace(0, np.nan)
    decline = (-_logchg(sharesbas, 504)).clip(lower=0)
    b = pur * np.log1p(decline)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# weighted-average dilution vs basic dilution rank-spread (channel divergence)
def f28sc_f28_share_count_dynamics_dilrankspr_252d_base_v121_signal(shareswa, sharesbas):
    rw = _rank(_logchg(shareswa, 252), 504)
    rb = _rank(_logchg(sharesbas, 252), 504)
    b = rw - rb
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# diluted-creep level x net issuance sign (dual-channel dilution flag)
def f28sc_f28_share_count_dynamics_creepxiss_base_v122_signal(shareswadil, shareswa, ncfcommon):
    creep = _f28_creep(shareswadil, shareswa)
    iss = ncfcommon.rolling(252, min_periods=126).sum()
    b = creep * np.sign(iss)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# share-count quarterly change z-scored over half-year (short pace extremity)
def f28sc_f28_share_count_dynamics_dilz_63d_base_v123_signal(sharesbas):
    g = _logchg(sharesbas, 63)
    b = _z(g, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# buyback intensity dispersion over five years (lumpy long-run repurchases)
def f28sc_f28_share_count_dynamics_bbdisp_1260d_base_v124_signal(ncfcommon, sharesbas):
    raw = (-ncfcommon).rolling(63, min_periods=21).sum() / sharesbas.replace(0, np.nan)
    b = _std(raw, 1260)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# count-reduction streak: fraction of five years count fell below trailing level
def f28sc_f28_share_count_dynamics_reductstreak_1260d_base_v125_signal(sharesbas):
    below = (sharesbas < sharesbas.shift(63)).astype(float)
    b = below.rolling(1260, min_periods=504).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# weighted-average dilution momentum (126d growth vs prior 126d)
def f28sc_f28_share_count_dynamics_dilwamom_126d_base_v126_signal(shareswa):
    g = _logchg(shareswa, 126)
    b = g - g.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# overhang-spread tanh-bounded: squashed diluted-minus-basic annual growth gap
def f28sc_f28_share_count_dynamics_dildiltanh_252d_base_v127_signal(shareswadil, sharesbas):
    gap = _logchg(shareswadil, 252) - _logchg(sharesbas, 252)
    b = np.tanh(200.0 * gap)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net flow purity momentum over five years (long directional shift)
def f28sc_f28_share_count_dynamics_puritymom_1260d_base_v128_signal(ncfcommon):
    net = ncfcommon.rolling(252, min_periods=126).sum()
    gross = ncfcommon.abs().rolling(252, min_periods=126).sum()
    pur = net / gross.replace(0, np.nan)
    b = pur - pur.shift(504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# share-count above five-year min (cumulative dilution off the cleanest level)
def f28sc_f28_share_count_dynamics_abovemin_1260d_base_v129_signal(sharesbas):
    rmin = _rmin(sharesbas, 1260)
    b = np.log(sharesbas.replace(0, np.nan) / rmin.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# weighted-average count deviation from five-year mean (long disequilibrium)
def f28sc_f28_share_count_dynamics_countdevwa_1260d_base_v130_signal(shareswa):
    m = _mean(shareswa, 1260)
    b = shareswa / m.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dilution acceleration sign x creep level (accelerating dilution with overhang)
def f28sc_f28_share_count_dynamics_dilaccelxcreep_base_v131_signal(sharesbas, shareswadil, shareswa):
    g = _logchg(sharesbas, 252)
    accel = g - g.shift(252)
    creep = _f28_creep(shareswadil, shareswa)
    b = np.sign(accel) * creep
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# buyback intensity vs its own half-year baseline (repurchase impulse)
def f28sc_f28_share_count_dynamics_bbimpulse_63d_base_v132_signal(ncfcommon, sharesbas):
    raw = (-ncfcommon).rolling(63, min_periods=21).sum() / sharesbas.replace(0, np.nan)
    b = raw - raw.rolling(126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# diluted-vs-basic count ratio level (static overhang multiple)
def f28sc_f28_share_count_dynamics_dilbasratio_base_v133_signal(shareswadil, sharesbas):
    b = shareswadil / sharesbas.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# diluted-vs-basic ratio momentum (overhang multiple change over a year)
def f28sc_f28_share_count_dynamics_dilbasratiomom_252d_base_v134_signal(shareswadil, sharesbas):
    r = shareswadil / sharesbas.replace(0, np.nan)
    b = r - r.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net issuance over five years sign x magnitude (lifetime issuance posture)
def f28sc_f28_share_count_dynamics_isslife_1260d_base_v135_signal(ncfcommon):
    net = _f28_net_issuance(ncfcommon, 1260)
    b = np.sign(net) * np.log1p(net.abs())
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# weighted-average count five-year range position
def f28sc_f28_share_count_dynamics_warngpos_1260d_base_v136_signal(shareswa):
    hi = _rmax(shareswa, 1260)
    lo = _rmin(shareswa, 1260)
    b = (shareswa - lo) / (hi - lo).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dilution asymmetry: up-month vs down-month share-count moves on basic, half-year
def f28sc_f28_share_count_dynamics_dilasym_126d_base_v137_signal(sharesbas):
    chg = _logchg(sharesbas, 21)
    up = (chg > 0).astype(float).rolling(126, min_periods=63).mean()
    dn = (chg < 0).astype(float).rolling(126, min_periods=63).mean()
    b = up - dn
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# creep dispersion over five years (long-run overhang volatility)
def f28sc_f28_share_count_dynamics_creepdisp_1260d_base_v138_signal(shareswadil, shareswa):
    c = _f28_creep(shareswadil, shareswa)
    b = _std(c, 1260)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# share-count growth sign-persistence on basic (consistent diluter vs buyer)
def f28sc_f28_share_count_dynamics_dilsignpersist_504d_base_v139_signal(sharesbas):
    chg = _logchg(sharesbas, 21)
    b = np.sign(chg).rolling(504, min_periods=252).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# weighted-average dilution minus buyback-cash channel (net real dilution)
def f28sc_f28_share_count_dynamics_realdil_252d_base_v140_signal(shareswa, ncfcommon, sharesbas):
    dil = _logchg(shareswa, 252)
    bb = (-ncfcommon).rolling(252, min_periods=126).sum() / sharesbas.replace(0, np.nan)
    b = _z(dil, 504) + _z(bb, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# creep momentum tanh-bounded (overhang change, squashed)
def f28sc_f28_share_count_dynamics_creepmomtanh_126d_base_v141_signal(shareswadil, shareswa):
    c = _f28_creep(shareswadil, shareswa)
    chg = c - c.shift(126)
    b = np.tanh(50.0 * chg)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# diluted-share trend slope minus weighted-average trend (overhang slope gap, half-year)
def f28sc_f28_share_count_dynamics_trenddivwa_126d_base_v142_signal(shareswadil, shareswa):
    sd = _slope(np.log(shareswadil.replace(0, np.nan)), 126)
    sw = _slope(np.log(shareswa.replace(0, np.nan)), 126)
    b = sd - sw
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net common flow magnitude relative to share base, ranked (issuance scale percentile)
def f28sc_f28_share_count_dynamics_issscale_504d_base_v143_signal(ncfcommon, sharesbas):
    mag = ncfcommon.abs().rolling(252, min_periods=126).sum() / sharesbas.replace(0, np.nan)
    b = _rank(mag, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dilution streak balance on basic over half-year (net short-run issuance bias)
def f28sc_f28_share_count_dynamics_streakbal_126d_base_v144_signal(sharesbas):
    up = (sharesbas.diff() > 0).astype(float).rolling(126, min_periods=63).mean()
    dn = (sharesbas.diff() < 0).astype(float).rolling(126, min_periods=63).mean()
    b = up - dn
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# diluted creep relative to creep one year ago, ranked (overhang change percentile)
def f28sc_f28_share_count_dynamics_creepchgrank_252d_base_v145_signal(shareswadil, shareswa):
    c = _f28_creep(shareswadil, shareswa)
    chg = c - c.shift(252)
    b = _rank(chg, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# share-count drawup off five-year clean minimum, ranked (long dilution percentile)
def f28sc_f28_share_count_dynamics_leangaprank_1260d_base_v146_signal(sharesbas):
    lo = _rmin(sharesbas, 1260)
    gap = np.log(sharesbas.replace(0, np.nan) / lo.replace(0, np.nan))
    b = _rank(gap, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dual-channel reduction score: rank of net buyback cash times rank of count decline (5y)
def f28sc_f28_share_count_dynamics_bbeff_1260d_base_v147_signal(ncfcommon, sharesbas):
    net = ncfcommon.rolling(504, min_periods=252).sum()
    cash_rank = _rank(-net, 504)
    decline_rank = _rank(-_logchg(sharesbas, 504), 504)
    b = cash_rank * decline_rank
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# weighted-average dilution acceleration as level (annual change in quarterly pace)
def f28sc_f28_share_count_dynamics_dilwaaccel_63d_base_v148_signal(shareswa):
    g = _logchg(shareswa, 63)
    b = g - g.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dilution funding mix: option-overhang creep vs cash-issuance share of total dilution
def f28sc_f28_share_count_dynamics_creeprngpos_1260d_base_v149_signal(shareswadil, shareswa, ncfcommon, sharesbas):
    creep = _f28_creep(shareswadil, shareswa).abs()
    iss = (ncfcommon.rolling(504, min_periods=252).sum() / sharesbas.replace(0, np.nan)).abs()
    b = creep / (creep + iss + 1e-9) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# combined dilution-pressure composite: dilution rank + creep rank + issuance-purity
def f28sc_f28_share_count_dynamics_dilpressure_252d_base_v150_signal(sharesbas, shareswadil, shareswa, ncfcommon):
    dilr = _rank(_logchg(sharesbas, 252), 504)
    creepr = _rank(_f28_creep(shareswadil, shareswa), 504)
    net = ncfcommon.rolling(252, min_periods=126).sum()
    gross = ncfcommon.abs().rolling(252, min_periods=126).sum()
    pur = net / gross.replace(0, np.nan)
    b = dilr + creepr + 0.5 * pur
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f28sc_f28_share_count_dynamics_dilbas_21d_base_v076_signal,
    f28sc_f28_share_count_dynamics_dilbas_126d_base_v077_signal,
    f28sc_f28_share_count_dynamics_dilbas_1260d_base_v078_signal,
    f28sc_f28_share_count_dynamics_dilbasz_504d_base_v079_signal,
    f28sc_f28_share_count_dynamics_dilwarank_1260d_base_v080_signal,
    f28sc_f28_share_count_dynamics_dilwa_126d_base_v081_signal,
    f28sc_f28_share_count_dynamics_dilwadisp_504d_base_v082_signal,
    f28sc_f28_share_count_dynamics_dilwatanh_252d_base_v083_signal,
    f28sc_f28_share_count_dynamics_dildil_126d_base_v084_signal,
    f28sc_f28_share_count_dynamics_dildil_1260d_base_v085_signal,
    f28sc_f28_share_count_dynamics_creepmom_63d_base_v086_signal,
    f28sc_f28_share_count_dynamics_creepvsmin_1260d_base_v087_signal,
    f28sc_f28_share_count_dynamics_creepema_base_v088_signal,
    f28sc_f28_share_count_dynamics_creeprngpos_504d_base_v089_signal,
    f28sc_f28_share_count_dynamics_bbintens_252d_base_v090_signal,
    f28sc_f28_share_count_dynamics_bbintensmom_63d_base_v091_signal,
    f28sc_f28_share_count_dynamics_ncfpurity_504d_base_v092_signal,
    f28sc_f28_share_count_dynamics_ncfz_1260d_base_v093_signal,
    f28sc_f28_share_count_dynamics_trendwa_1260d_base_v094_signal,
    f28sc_f28_share_count_dynamics_trenddiv_252d_base_v095_signal,
    f28sc_f28_share_count_dynamics_trendcurv_126d_base_v096_signal,
    f28sc_f28_share_count_dynamics_dilstreak_126d_base_v097_signal,
    f28sc_f28_share_count_dynamics_dilstreakz_1260d_base_v098_signal,
    f28sc_f28_share_count_dynamics_issaccel_252d_base_v099_signal,
    f28sc_f28_share_count_dynamics_belowmax_1260d_base_v100_signal,
    f28sc_f28_share_count_dynamics_countrngpos_1260d_base_v101_signal,
    f28sc_f28_share_count_dynamics_countdev_504d_base_v102_signal,
    f28sc_f28_share_count_dynamics_baswadivrank_252d_base_v103_signal,
    f28sc_f28_share_count_dynamics_baswadivmom_63d_base_v104_signal,
    f28sc_f28_share_count_dynamics_dilvol_504d_base_v105_signal,
    f28sc_f28_share_count_dynamics_dilwasignmag_252d_base_v106_signal,
    f28sc_f28_share_count_dynamics_bbrank_1260d_base_v107_signal,
    f28sc_f28_share_count_dynamics_creeptrend_1260d_base_v108_signal,
    f28sc_f28_share_count_dynamics_dildildisp_504d_base_v109_signal,
    f28sc_f28_share_count_dynamics_ncfema_252d_base_v110_signal,
    f28sc_f28_share_count_dynamics_dilwamultidisp_base_v111_signal,
    f28sc_f28_share_count_dynamics_diler_504d_base_v112_signal,
    f28sc_f28_share_count_dynamics_dilimpulse_252d_base_v113_signal,
    f28sc_f28_share_count_dynamics_netstance_252d_base_v114_signal,
    f28sc_f28_share_count_dynamics_creepxdilsign_base_v115_signal,
    f28sc_f28_share_count_dynamics_dildilstreak_1260d_base_v116_signal,
    f28sc_f28_share_count_dynamics_issvsmax_1260d_base_v117_signal,
    f28sc_f28_share_count_dynamics_creepconv_1260d_base_v118_signal,
    f28sc_f28_share_count_dynamics_dilaccel_252d_base_v119_signal,
    f28sc_f28_share_count_dynamics_reductqual_1260d_base_v120_signal,
    f28sc_f28_share_count_dynamics_dilrankspr_252d_base_v121_signal,
    f28sc_f28_share_count_dynamics_creepxiss_base_v122_signal,
    f28sc_f28_share_count_dynamics_dilz_63d_base_v123_signal,
    f28sc_f28_share_count_dynamics_bbdisp_1260d_base_v124_signal,
    f28sc_f28_share_count_dynamics_reductstreak_1260d_base_v125_signal,
    f28sc_f28_share_count_dynamics_dilwamom_126d_base_v126_signal,
    f28sc_f28_share_count_dynamics_dildiltanh_252d_base_v127_signal,
    f28sc_f28_share_count_dynamics_puritymom_1260d_base_v128_signal,
    f28sc_f28_share_count_dynamics_abovemin_1260d_base_v129_signal,
    f28sc_f28_share_count_dynamics_countdevwa_1260d_base_v130_signal,
    f28sc_f28_share_count_dynamics_dilaccelxcreep_base_v131_signal,
    f28sc_f28_share_count_dynamics_bbimpulse_63d_base_v132_signal,
    f28sc_f28_share_count_dynamics_dilbasratio_base_v133_signal,
    f28sc_f28_share_count_dynamics_dilbasratiomom_252d_base_v134_signal,
    f28sc_f28_share_count_dynamics_isslife_1260d_base_v135_signal,
    f28sc_f28_share_count_dynamics_warngpos_1260d_base_v136_signal,
    f28sc_f28_share_count_dynamics_dilasym_126d_base_v137_signal,
    f28sc_f28_share_count_dynamics_creepdisp_1260d_base_v138_signal,
    f28sc_f28_share_count_dynamics_dilsignpersist_504d_base_v139_signal,
    f28sc_f28_share_count_dynamics_realdil_252d_base_v140_signal,
    f28sc_f28_share_count_dynamics_creepmomtanh_126d_base_v141_signal,
    f28sc_f28_share_count_dynamics_trenddivwa_126d_base_v142_signal,
    f28sc_f28_share_count_dynamics_issscale_504d_base_v143_signal,
    f28sc_f28_share_count_dynamics_streakbal_126d_base_v144_signal,
    f28sc_f28_share_count_dynamics_creepchgrank_252d_base_v145_signal,
    f28sc_f28_share_count_dynamics_leangaprank_1260d_base_v146_signal,
    f28sc_f28_share_count_dynamics_bbeff_1260d_base_v147_signal,
    f28sc_f28_share_count_dynamics_dilwaaccel_63d_base_v148_signal,
    f28sc_f28_share_count_dynamics_creeprngpos_1260d_base_v149_signal,
    f28sc_f28_share_count_dynamics_dilpressure_252d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F28_SHARE_COUNT_DYNAMICS_REGISTRY_076_150 = REGISTRY


def _fund(seed, base=1e8, drift=0.02, vol=0.05, allow_neg=False, n=1500):
    g = np.random.default_rng(seed)
    steps = np.repeat(g.normal(drift, vol, n // 63 + 1), 63)[:n]
    s = base * np.exp(np.cumsum(steps / 63))
    if allow_neg:
        s = s - base * 0.3
    return pd.Series(s, name=None)


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    sharesbas = _fund(101, base=5e8, drift=0.015, vol=0.04).rename("sharesbas")
    shareswa = _fund(102, base=4.9e8, drift=0.015, vol=0.04).rename("shareswa")
    _overhang = _fund(103, base=1.0, drift=0.01, vol=0.06).values
    shareswadil = (shareswa * (1.0 + 0.02 + 0.06 * np.clip(_overhang / _overhang[0] - 1.0, -0.5, None))).rename("shareswadil")
    _ncf_rng = np.random.default_rng(104)
    _ncf_steps = np.repeat(_ncf_rng.normal(0.0, 1.0, n // 63 + 1), 63)[:n]
    ncfcommon = pd.Series(_ncf_steps * 5e6 + _fund(105, base=1e6, drift=0.0, vol=0.4, allow_neg=True).values,
                          name="ncfcommon")

    cols = {"sharesbas": sharesbas, "shareswa": shareswa,
            "shareswadil": shareswadil, "ncfcommon": ncfcommon}

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
        assert q.nunique() > 50, "%s nunique=%d" % (name, q.nunique())
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

    print("OK f28_share_count_dynamics_base_076_150_claude: %d features pass" % n_features)
