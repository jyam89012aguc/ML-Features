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


# ===== folder domain primitives (52-week / multi-year ANCHORING) =====
def _f07_anchor_gap_hi(close, w):
    hi = close.rolling(w, min_periods=max(1, w // 2)).max()
    return np.log(close.replace(0, np.nan) / hi.replace(0, np.nan))


def _f07_anchor_gap_lo(close, w):
    lo = close.rolling(w, min_periods=max(1, w // 2)).min()
    return np.log(close.replace(0, np.nan) / lo.replace(0, np.nan))


def _f07_newhigh_flag(close, w):
    hi = close.rolling(w, min_periods=max(1, w // 2)).max()
    return (close >= hi * 0.99999).astype(float)


def _f07_newlow_flag(close, w):
    lo = close.rolling(w, min_periods=max(1, w // 2)).min()
    return (close <= lo * 1.00001).astype(float)


def _f07_freq(flag, cw):
    return flag.rolling(cw, min_periods=max(1, cw // 2)).mean()


def _f07_entries(flag, cw):
    ent = ((flag == 1) & (flag.shift(1) == 0)).astype(float)
    return ent.rolling(cw, min_periods=max(1, cw // 2)).sum()


def _f07_dryrun(flag):
    no = (1.0 - flag)
    return no.groupby((no == 0).cumsum()).cumsum()


def _f07_bandpos(close, w):
    hi = close.rolling(w, min_periods=max(1, w // 2)).max()
    lo = close.rolling(w, min_periods=max(1, w // 2)).min()
    return (close - lo) / (hi - lo).replace(0, np.nan)


def _f07_anchor_dist(close, wa, wb):
    a = close.rolling(wa, min_periods=max(1, wa // 2)).max()
    b = close.rolling(wb, min_periods=max(1, wb // 2)).max()
    return np.log(a.replace(0, np.nan) / b.replace(0, np.nan))


# ============================================================
# ----- 126d (half-year) band anchoring forms -----

# 126d perch instability: rolling std of the band position over a quarter, ranked (churn, not level)
def f07fw_f07_fiftytwo_week_position_posz_126d_base_v076_signal(closeadj):
    pos = _f07_bandpos(closeadj, 126)
    roam = pos.rolling(63, min_periods=21).std()
    b = _rank(roam, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 126d band position ranked vs its own 252d history
def f07fw_f07_fiftytwo_week_position_posrank_126d_base_v077_signal(closeadj):
    b = _rank(_f07_bandpos(closeadj, 126), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# spread between 126d and 504d band positions (short vs long perch tension)
def f07fw_f07_fiftytwo_week_position_postension_126v504_base_v078_signal(closeadj):
    b = _f07_bandpos(closeadj, 126) - _f07_bandpos(closeadj, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 126d anchoring gap (price vs half-year high) z-scored vs its 126d history
def f07fw_f07_fiftytwo_week_position_gapz_126d_base_v079_signal(closeadj):
    g = _f07_anchor_gap_hi(closeadj, 126)
    b = _z(g, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 126d anchoring gap displacement vs its 42d average (short anchor pull-back)
def f07fw_f07_fiftytwo_week_position_gapdisp_126d_base_v080_signal(closeadj):
    g = _f07_anchor_gap_hi(closeadj, 126)
    b = g - g.rolling(42, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# new-half-year-high frequency over the last quarter (short anchor refresh)
def f07fw_f07_fiftytwo_week_position_nhfreq63_126d_base_v081_signal(closeadj):
    flag = _f07_newhigh_flag(closeadj, 126)
    g = _f07_anchor_gap_hi(closeadj, 126)
    b = _f07_freq(flag, 63) + 0.25 * g
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 126d upper-third occupancy CHANGE over a quarter (regime shift, not regime level)
def f07fw_f07_fiftytwo_week_position_uppershare_126d_base_v082_signal(closeadj):
    pos = _f07_bandpos(closeadj, 126)
    occ = (pos >= 0.6667).astype(float).rolling(126, min_periods=63).mean()
    b = occ - occ.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 126d band-position roam (std over the half year)
def f07fw_f07_fiftytwo_week_position_posroam_126d_base_v083_signal(closeadj):
    pos = _f07_bandpos(closeadj, 126)
    b = pos.rolling(126, min_periods=63).std()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ----- 63d (quarter) band anchoring forms -----

# 63d band position ranked vs its own 252d history (short perch percentile)
def f07fw_f07_fiftytwo_week_position_posrank_63d_base_v084_signal(closeadj):
    b = _rank(_f07_bandpos(closeadj, 63), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 63d anchoring gap z-scored vs its 126d history (quarter anchor extremity)
def f07fw_f07_fiftytwo_week_position_gapz_63d_base_v085_signal(closeadj):
    g = _f07_anchor_gap_hi(closeadj, 63)
    b = _z(g, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# quarter-vs-annual perch tension, de-trended by its own slow EMA (relative perch tension)
def f07fw_f07_fiftytwo_week_position_postension_63v252_base_v086_signal(closeadj):
    spr = _f07_bandpos(closeadj, 63) - _f07_bandpos(closeadj, 252)
    b = spr - spr.ewm(span=63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 63d anchoring gap displacement vs 21d average (fast anchor pull-back)
def f07fw_f07_fiftytwo_week_position_gapdisp_63d_base_v087_signal(closeadj):
    g = _f07_anchor_gap_hi(closeadj, 63)
    b = g - g.rolling(21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ----- multi-window anchor refresh / frequency forms -----

# 504d new-2yr-high frequency over the last quarter (durable short-window refresh)
def f07fw_f07_fiftytwo_week_position_nhfreq63_504d_base_v088_signal(closeadj):
    flag = _f07_newhigh_flag(closeadj, 504)
    g = _f07_anchor_gap_hi(closeadj, 504)
    b = _f07_freq(flag, 63) + 0.2 * g
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 1260d new-5yr-high entries over the last year (rare multi-year refresh episodes)
def f07fw_f07_fiftytwo_week_position_nhentries_1260d_base_v089_signal(closeadj):
    flag = _f07_newhigh_flag(closeadj, 1260)
    g = _f07_anchor_gap_hi(closeadj, 1260)
    b = _f07_entries(flag, 252) + 3.0 * g.rolling(126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# new-low entries 504d over the last year, low-gap weighted (durable trough episodes)
def f07fw_f07_fiftytwo_week_position_nlentries_504d_base_v090_signal(closeadj):
    flag = _f07_newlow_flag(closeadj, 504)
    g = _f07_anchor_gap_lo(closeadj, 504)
    b = _f07_entries(flag, 252) + 2.0 * g.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# new-high frequency acceleration 504d (quarter freq minus half-year freq)
def f07fw_f07_fiftytwo_week_position_nhaccel_504d_base_v091_signal(closeadj):
    flag = _f07_newhigh_flag(closeadj, 504)
    b = _f07_freq(flag, 63) - _f07_freq(flag, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# new-high frequency 126-window minus 252-window (refresh-pace divergence), gap-blended
def f07fw_f07_fiftytwo_week_position_nhfreqdiv_base_v092_signal(closeadj):
    f126 = _f07_freq(_f07_newhigh_flag(closeadj, 126), 126)
    f252 = _f07_freq(_f07_newhigh_flag(closeadj, 252), 126)
    g = _f07_anchor_gap_hi(closeadj, 126) - _f07_anchor_gap_hi(closeadj, 252)
    b = (f126 - f252) + 0.5 * g
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# new-high frequency 63d ranked vs its 252d history (unusual short-burst leadership)
def f07fw_f07_fiftytwo_week_position_nhfreqrank63_252d_base_v093_signal(closeadj):
    flag = _f07_newhigh_flag(closeadj, 252)
    freq = _f07_freq(flag, 21)
    b = _rank(freq, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ----- anchor dry-spell / recency (streak-based, NOT raw days-since) -----

# bars-since-last-252d-high streak, z-scored vs 252d history (recency extremity)
def f07fw_f07_fiftytwo_week_position_recencyz_252d_base_v094_signal(closeadj):
    since = _f07_dryrun(_f07_newhigh_flag(closeadj, 252))
    b = _z(since, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# bars-since-last-504d-high streak ranked vs 252d history
def f07fw_f07_fiftytwo_week_position_recencyrank_504d_base_v095_signal(closeadj):
    since = _f07_dryrun(_f07_newhigh_flag(closeadj, 504))
    b = _rank(since, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# high-recency minus low-recency streak balance, ranked (which extreme is staler)
def f07fw_f07_fiftytwo_week_position_recencybal_252d_base_v096_signal(closeadj):
    sh = _f07_dryrun(_f07_newhigh_flag(closeadj, 252))
    sl = _f07_dryrun(_f07_newlow_flag(closeadj, 252))
    b = _rank(sh - sl, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# new-high dry-spell deepening: current streak minus its quarter-ago value
def f07fw_f07_fiftytwo_week_position_drymom_252d_base_v097_signal(closeadj):
    since = _f07_dryrun(_f07_newhigh_flag(closeadj, 252))
    b = since - since.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ----- nested anchor (52w vs 5y) distance forms -----

# nested-high distance 504 vs 1260 blended with the 504d anchor gap (2yr vs 5y freshness)
def f07fw_f07_fiftytwo_week_position_anchdisthi_504v1260_base_v098_signal(closeadj):
    d = _f07_anchor_dist(closeadj, 504, 1260)
    g = _f07_anchor_gap_hi(closeadj, 504)
    b = d + 0.3 * g
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# nested-low distance 504 vs 1260, ranked vs 252d history
def f07fw_f07_fiftytwo_week_position_anchdistlo_504v1260_base_v099_signal(closeadj):
    a = _rmin(closeadj, 504)
    b2 = _rmin(closeadj, 1260)
    d = np.log(a.replace(0, np.nan) / b2.replace(0, np.nan))
    b = _rank(d, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# nested-anchor freshness: 252d high vs 1260d high, change over a half year (catching up)
def f07fw_f07_fiftytwo_week_position_anchdistmom_252v1260_base_v100_signal(closeadj):
    d = _f07_anchor_dist(closeadj, 252, 1260)
    b = d - d.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# span-ratio 252 vs 504 (annual band width relative to two-year band width), ranked
def f07fw_f07_fiftytwo_week_position_spanratio_252v504_base_v101_signal(closeadj):
    s = np.log(_rmax(closeadj, 252).replace(0, np.nan) / _rmin(closeadj, 252).replace(0, np.nan))
    l = np.log(_rmax(closeadj, 504).replace(0, np.nan) / _rmin(closeadj, 504).replace(0, np.nan))
    b = _rank(s / l.replace(0, np.nan), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# nested-low freshness CHANGE: half-year change in the 252d-vs-1260d low distance (trough catching up)
def f07fw_f07_fiftytwo_week_position_trofreshstreak_1260_base_v102_signal(closeadj):
    lo252 = _rmin(closeadj, 252)
    lo1260 = _rmin(closeadj, 1260)
    dist = np.log(lo252.replace(0, np.nan) / lo1260.replace(0, np.nan))
    b = dist - dist.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ----- anchor amplitude / span regime forms -----

# 504d log span ranked vs its 252d history (two-year amplitude percentile)
def f07fw_f07_fiftytwo_week_position_amprank_504d_base_v103_signal(closeadj):
    span = np.log(_rmax(closeadj, 504).replace(0, np.nan) / _rmin(closeadj, 504).replace(0, np.nan))
    b = _rank(span, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 252d span change over a half year, vol-normalized (band widening pace)
def f07fw_f07_fiftytwo_week_position_spanmom126_252d_base_v104_signal(closeadj):
    span = np.log(_rmax(closeadj, 252).replace(0, np.nan) / _rmin(closeadj, 252).replace(0, np.nan))
    chg = span - span.shift(126)
    vol = closeadj.pct_change().rolling(63, min_periods=21).std()
    b = chg / vol.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 252d span contraction regime: fraction of quarter span sits below its 252d median
def f07fw_f07_fiftytwo_week_position_spancontract_252d_base_v105_signal(closeadj):
    span = np.log(_rmax(closeadj, 252).replace(0, np.nan) / _rmin(closeadj, 252).replace(0, np.nan))
    med = span.rolling(252, min_periods=126).median()
    narrow = (span < med).astype(float)
    b = narrow.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# how far the 504d high sits above the 504d mean (long upper extension), z-scored
def f07fw_f07_fiftytwo_week_position_hiextz_504d_base_v106_signal(closeadj):
    hi = _rmax(closeadj, 504)
    mn = _mean(closeadj, 504)
    ext = (hi - mn) / mn.replace(0, np.nan)
    b = _z(ext, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 1260d lower-third occupancy over the last year (deep multi-year basing regime)
def f07fw_f07_fiftytwo_week_position_lowershare_1260d_base_v107_signal(closeadj):
    pos = _f07_bandpos(closeadj, 1260)
    b = (pos <= 0.3333).astype(float).rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ----- anchoring-gap higher-order / interaction forms -----

# anchoring-gap kurtosis-ish: share of quarter the gap is an outlier vs its 252d band
def f07fw_f07_fiftytwo_week_position_gapoutlier_252d_base_v108_signal(closeadj):
    g = _f07_anchor_gap_hi(closeadj, 252)
    z = _z(g, 252)
    out = (z.abs() >= 1.5).astype(float)
    b = out.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# anchoring-gap slope: quarter-over-quarter change in the smoothed 504d gap, ranked
def f07fw_f07_fiftytwo_week_position_gapslope_504d_base_v109_signal(closeadj):
    g = _f07_anchor_gap_hi(closeadj, 504).ewm(span=21, min_periods=10).mean()
    chg = g - g.shift(63)
    b = _rank(chg, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# anchoring-gap autocorrelation proxy: gap displacement times its own one-month lag
def f07fw_f07_fiftytwo_week_position_gappersist_252d_base_v110_signal(closeadj):
    g = _f07_anchor_gap_hi(closeadj, 252)
    disp = g - g.rolling(63, min_periods=21).mean()
    b = np.sign(disp) * np.sign(disp.shift(21)) * disp.abs()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# low-side anchoring-gap displacement vs its 63d average (basing-band pull)
def f07fw_f07_fiftytwo_week_position_logapdisp_252d_base_v111_signal(closeadj):
    g = _f07_anchor_gap_lo(closeadj, 252)
    b = g - g.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# low-side anchoring-gap (504d) RESIDUAL vs the 252d low-gap, z-scored (basing pull net of annual)
def f07fw_f07_fiftytwo_week_position_logapz_504d_base_v112_signal(closeadj):
    g504 = _f07_anchor_gap_lo(closeadj, 504)
    g252 = _f07_anchor_gap_lo(closeadj, 252)
    b = _z(g504 - g252, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# anchor-pull asymmetry 504d CHANGE over a half year (which 2yr anchor is gaining dominance)
def f07fw_f07_fiftytwo_week_position_gapasym_504d_base_v113_signal(closeadj):
    gh = _f07_anchor_gap_hi(closeadj, 504).abs()
    gl = _f07_anchor_gap_lo(closeadj, 504).abs()
    asym = (gl - gh) / (gl + gh).replace(0, np.nan)
    b = asym - asym.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# anchoring-gap regime persistence run: longest deep-gap run over the year (504d gap)
def f07fw_f07_fiftytwo_week_position_gapregimerun_504d_base_v114_signal(closeadj):
    g = _f07_anchor_gap_hi(closeadj, 504)
    med = g.rolling(252, min_periods=126).median()
    deep = (g < med).astype(float)
    run = deep.groupby((deep == 0).cumsum()).cumsum()
    b = run.rolling(252, min_periods=126).max()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ----- band-position regime / occupancy forms -----

# 504d band-position edge occupancy (time near 2yr-band edges) over the year
def f07fw_f07_fiftytwo_week_position_edgeshare_504d_base_v115_signal(closeadj):
    pos = _f07_bandpos(closeadj, 504)
    edge = ((pos <= 0.2) | (pos >= 0.8)).astype(float)
    b = edge.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# band-position tercile-transition rate (504d) blended with roam (regime churn)
def f07fw_f07_fiftytwo_week_position_regimechurn_504d_base_v116_signal(closeadj):
    pos = _f07_bandpos(closeadj, 504)
    terc = np.floor(pos.clip(0, 0.9999) * 3.0)
    moved = (terc != terc.shift(1)).astype(float)
    b = moved.rolling(126, min_periods=63).mean() + 0.2 * pos.rolling(63, min_periods=21).std()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# upper-third occupancy minus its slow EMA (2yr regime occupancy displacement)
def f07fw_f07_fiftytwo_week_position_upperdisp_504d_base_v117_signal(closeadj):
    pos = _f07_bandpos(closeadj, 504)
    up = (pos >= 0.6667).astype(float).rolling(126, min_periods=63).mean()
    b = up - up.ewm(span=126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# band-position percentile momentum 252d (change over a month in the ranked perch)
def f07fw_f07_fiftytwo_week_position_posrankmom_252d_base_v118_signal(closeadj):
    r = _rank(_f07_bandpos(closeadj, 252), 252)
    b = r - r.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# band-position dispersion across 63/126/252 (short-anchor disagreement)
def f07fw_f07_fiftytwo_week_position_posdisp_short_base_v119_signal(closeadj):
    b = pd.concat([_f07_bandpos(closeadj, 63),
                   _f07_bandpos(closeadj, 126),
                   _f07_bandpos(closeadj, 252)], axis=1).std(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ----- intraday-anchor (true high/low) forms -----

# true-high anchoring gap 504d ranked vs 252d history (intraday 2yr anchor percentile)
def f07fw_f07_fiftytwo_week_position_truegaprank_504d_base_v120_signal(closeadj, high):
    hi = high.rolling(504, min_periods=252).max()
    g = np.log(closeadj.replace(0, np.nan) / hi.replace(0, np.nan))
    b = _rank(g, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# true-low anchoring gap 504d displacement vs its 63d average (intraday basing pull-off)
def f07fw_f07_fiftytwo_week_position_truelogapz_504d_base_v121_signal(closeadj, low):
    lo = low.rolling(504, min_periods=252).min()
    g = np.log(closeadj.replace(0, np.nan) / lo.replace(0, np.nan))
    b = g - g.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# intraday-band 252d position ranked, then de-trended by its own slow EMA
def f07fw_f07_fiftytwo_week_position_truebanddisp_252d_base_v122_signal(closeadj, high, low):
    hi = high.rolling(252, min_periods=126).max()
    lo = low.rolling(252, min_periods=126).min()
    pos = (closeadj - lo) / (hi - lo).replace(0, np.nan)
    r = _rank(pos, 252)
    b = r - r.ewm(span=63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# intraday-high premium 504d: true 2yr high vs close-based 2yr high (range overstatement)
def f07fw_f07_fiftytwo_week_position_truehiprem_504d_base_v123_signal(closeadj, high):
    hi_true = high.rolling(504, min_periods=252).max()
    hi_close = closeadj.rolling(504, min_periods=252).max()
    b = np.log(hi_true.replace(0, np.nan) / hi_close.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# intraday-low discount 504d (true 2yr low vs close-based 2yr low)
def f07fw_f07_fiftytwo_week_position_truelodisc_504d_base_v124_signal(closeadj, low):
    lo_true = low.rolling(504, min_periods=252).min()
    lo_close = closeadj.rolling(504, min_periods=252).min()
    b = np.log(lo_close.replace(0, np.nan) / lo_true.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# intraday day-range relative to the 252d intraday band width (where today sits in the year)
def f07fw_f07_fiftytwo_week_position_intrarngshare_252d_base_v125_signal(closeadj, high, low):
    band = (high.rolling(252, min_periods=126).max()
            - low.rolling(252, min_periods=126).min())
    day = (high - low)
    b = (day / band.replace(0, np.nan)).rolling(21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ----- composites / interaction forms (regime-distinct) -----

# leadership decay: new-high frequency NOW minus a quarter ago, plus entry burst (refresh trend)
def f07fw_f07_fiftytwo_week_position_leaddecay_252d_base_v126_signal(closeadj):
    flag = _f07_newhigh_flag(closeadj, 252)
    freq = _f07_freq(flag, 63)
    ent = _f07_entries(flag, 63)
    b = (freq - freq.shift(63)) + 0.1 * ent
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# basing maturity: low-anchor dry-spell length ranked, net of low-gap CHANGE (old-but-stabilizing trough)
def f07fw_f07_fiftytwo_week_position_basematurity_252d_base_v127_signal(closeadj):
    since = _f07_dryrun(_f07_newlow_flag(closeadj, 252))
    g = _f07_anchor_gap_lo(closeadj, 252)
    gchg = g - g.shift(63)
    b = _rank(since, 252) - _rank(gchg, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# anchor-pull net sign-magnitude CHANGE over a month (how net anchor pull is shifting)
def f07fw_f07_fiftytwo_week_position_netpullsm_252d_base_v128_signal(closeadj):
    gh = _f07_anchor_gap_hi(closeadj, 252)
    gl = _f07_anchor_gap_lo(closeadj, 252)
    sh = np.sign(gh) * (gh.abs() ** 0.5)
    sl = np.sign(gl) * (gl.abs() ** 0.5)
    net = sh + sl
    b = net - net.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# refresh-vs-stale composite ranked: new-high freq minus high dry-spell rank
def f07fw_f07_fiftytwo_week_position_activeanchor_252d_base_v129_signal(closeadj):
    freq = _rank(_f07_freq(_f07_newhigh_flag(closeadj, 252), 63), 252)
    since = _rank(_f07_dryrun(_f07_newhigh_flag(closeadj, 252)), 252)
    b = freq - since
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# anchoring-gap displacement interacted with band-position roam (pull under churn)
def f07fw_f07_fiftytwo_week_position_pullchurn_252d_base_v130_signal(closeadj):
    g = _f07_anchor_gap_hi(closeadj, 252)
    disp = g - g.rolling(63, min_periods=21).mean()
    roam = _f07_bandpos(closeadj, 252).rolling(63, min_periods=21).std()
    b = disp * roam
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# year-over-year band-position rank change (this year's perch percentile vs last year's)
def f07fw_f07_fiftytwo_week_position_posrankyoy_252d_base_v131_signal(closeadj):
    r = _rank(_f07_bandpos(closeadj, 252), 252)
    b = r - r.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# new-high vs new-low entry-rate spread 504d (durable refresh-side skew)
def f07fw_f07_fiftytwo_week_position_entryskew_504d_base_v132_signal(closeadj):
    eh = _f07_entries(_f07_newhigh_flag(closeadj, 504), 252)
    el = _f07_entries(_f07_newlow_flag(closeadj, 504), 252)
    b = (eh - el) / (eh + el + 1.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 1260d band-position z-scored vs its own 252d history (multi-year perch extremity)
def f07fw_f07_fiftytwo_week_position_posz_1260d_base_v133_signal(closeadj):
    b = _z(_f07_bandpos(closeadj, 1260), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# anchoring-gap tanh momentum over a quarter (squashed quarterly anchor pull change)
def f07fw_f07_fiftytwo_week_position_gaptanhq_252d_base_v134_signal(closeadj):
    g = _f07_anchor_gap_hi(closeadj, 252)
    chg = g - g.shift(63)
    b = np.tanh(12.0 * chg)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# anchor-freshness composite: nested-high closeness ranked plus refresh-frequency rank
def f07fw_f07_fiftytwo_week_position_freshcomposite_252d_base_v135_signal(closeadj):
    d = _f07_anchor_dist(closeadj, 252, 1260)
    freq = _f07_freq(_f07_newhigh_flag(closeadj, 252), 126)
    b = _rank(d, 252) + _rank(freq, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# band-position kurtic extremity: time-share in the extreme deciles of the 252d band
def f07fw_f07_fiftytwo_week_position_extremeshare_252d_base_v136_signal(closeadj):
    pos = _f07_bandpos(closeadj, 252)
    ext = ((pos <= 0.1) | (pos >= 0.9)).astype(float)
    b = ext.rolling(126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# nested-anchor distance dispersion across (252v504, 252v1260, 504v1260) ladder
def f07fw_f07_fiftytwo_week_position_ladderdisp_base_v137_signal(closeadj):
    d1 = _f07_anchor_dist(closeadj, 252, 504)
    d2 = _f07_anchor_dist(closeadj, 252, 1260)
    d3 = _f07_anchor_dist(closeadj, 504, 1260)
    b = pd.concat([d1, d2, d3], axis=1).std(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# pullback-from-leadership count: deep-gap days that were PRECEDED within a month by a fresh high
def f07fw_f07_fiftytwo_week_position_dipbuy_252d_base_v138_signal(closeadj):
    g = _f07_anchor_gap_hi(closeadj, 252)
    flag = _f07_newhigh_flag(closeadj, 252)
    far = (g < g.rolling(252, min_periods=126).median()).astype(float)
    recent_high = flag.shift(1).rolling(21, min_periods=10).max().fillna(0)
    event = (far * recent_high)
    b = event.rolling(252, min_periods=126).sum()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# low-side anchoring-gap year-over-year change (basing-band reset vs a year ago)
def f07fw_f07_fiftytwo_week_position_logapyoy_252d_base_v139_signal(closeadj):
    g = _f07_anchor_gap_lo(closeadj, 252)
    raw = g - g.shift(252)
    b = _z(raw, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# anchor-amplitude asymmetry: upper extension minus lower extension (252d band lopsidedness)
def f07fw_f07_fiftytwo_week_position_extasym_252d_base_v140_signal(closeadj):
    hi = _rmax(closeadj, 252)
    lo = _rmin(closeadj, 252)
    mn = _mean(closeadj, 252)
    up = (hi - mn) / mn.replace(0, np.nan)
    dn = (mn - lo) / mn.replace(0, np.nan)
    b = (up - dn) / (up + dn).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 504d band-position roam ranked vs 252d history (how unsettled the 2yr perch is)
def f07fw_f07_fiftytwo_week_position_roamrank_504d_base_v141_signal(closeadj):
    roam = _f07_bandpos(closeadj, 504).rolling(126, min_periods=63).std()
    b = _rank(roam, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# anchoring-gap convexity 504d: smoothed second difference over a quarter
def f07fw_f07_fiftytwo_week_position_gapcurv_504d_base_v142_signal(closeadj):
    g = _f07_anchor_gap_hi(closeadj, 504).ewm(span=42, min_periods=21).mean()
    b = g - 2.0 * g.shift(42) + g.shift(84)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# new-high frequency 252d minus 504d new-2yr-high frequency (window-refresh divergence)
def f07fw_f07_fiftytwo_week_position_refreshdiv_252v504_base_v143_signal(closeadj):
    f1 = _f07_freq(_f07_newhigh_flag(closeadj, 252), 126)
    f2 = _f07_freq(_f07_newhigh_flag(closeadj, 504), 126)
    g = _f07_anchor_gap_hi(closeadj, 252) - _f07_anchor_gap_hi(closeadj, 504)
    b = (f1 - f2) + 0.5 * g
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# perch divergence in rank space: 504d ranked perch minus 126d ranked perch
def f07fw_f07_fiftytwo_week_position_perchdiv_126v504_base_v144_signal(closeadj):
    r504 = _rank(_f07_bandpos(closeadj, 504), 252)
    r126 = _rank(_f07_bandpos(closeadj, 126), 252)
    b = r504 - r126
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# anchoring-gap stability: inverse dispersion of the 252d gap over a quarter, ranked
def f07fw_f07_fiftytwo_week_position_gapstability_252d_base_v145_signal(closeadj):
    g = _f07_anchor_gap_hi(closeadj, 252)
    disp = g.rolling(63, min_periods=21).std()
    b = _rank(-disp, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# refresh-then-fade: new-high entries over a quarter blended with current gap depth
def f07fw_f07_fiftytwo_week_position_peakfade_252d_base_v146_signal(closeadj):
    ent = _f07_entries(_f07_newhigh_flag(closeadj, 252), 63)
    g = _f07_anchor_gap_hi(closeadj, 252)
    b = ent + 5.0 * g
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# multi-year anchor occupancy skew: upper minus lower 1260d-band time-share (5y regime)
def f07fw_f07_fiftytwo_week_position_occskew_1260d_base_v147_signal(closeadj):
    pos = _f07_bandpos(closeadj, 1260)
    up = (pos >= 0.6667).astype(float).rolling(252, min_periods=126).mean()
    dn = (pos <= 0.3333).astype(float).rolling(252, min_periods=126).mean()
    b = (up - dn) / (up + dn).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# anchor-gap displacement ranked 504d minus its own 126d-lagged rank (relative anchor shift)
def f07fw_f07_fiftytwo_week_position_gaprankshift_504d_base_v148_signal(closeadj):
    g = _f07_anchor_gap_hi(closeadj, 504)
    disp = g - g.rolling(126, min_periods=63).mean()
    r = _rank(disp, 252)
    b = r - r.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# composite basing-turn regime: new-high freq rising blended with low dry-spell length
def f07fw_f07_fiftytwo_week_position_turnregime_252d_base_v149_signal(closeadj):
    nhfreq = _f07_freq(_f07_newhigh_flag(closeadj, 252), 63)
    rising = (nhfreq - nhfreq.shift(63))
    lo_since = _f07_dryrun(_f07_newlow_flag(closeadj, 252))
    b = np.tanh(8.0 * rising) + 0.005 * lo_since
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# full-ladder anchor-pull blend de-trended by the 252d gap (long-anchor residual pull)
def f07fw_f07_fiftytwo_week_position_gapblend_multi_base_v150_signal(closeadj):
    z1 = _z(_f07_anchor_gap_hi(closeadj, 252), 252)
    z2 = _z(_f07_anchor_gap_hi(closeadj, 504), 252)
    z3 = _z(_f07_anchor_gap_hi(closeadj, 1260), 504)
    b = (z1 + z2 + z3) / 3.0 - z1
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f07fw_f07_fiftytwo_week_position_posz_126d_base_v076_signal,
    f07fw_f07_fiftytwo_week_position_posrank_126d_base_v077_signal,
    f07fw_f07_fiftytwo_week_position_postension_126v504_base_v078_signal,
    f07fw_f07_fiftytwo_week_position_gapz_126d_base_v079_signal,
    f07fw_f07_fiftytwo_week_position_gapdisp_126d_base_v080_signal,
    f07fw_f07_fiftytwo_week_position_nhfreq63_126d_base_v081_signal,
    f07fw_f07_fiftytwo_week_position_uppershare_126d_base_v082_signal,
    f07fw_f07_fiftytwo_week_position_posroam_126d_base_v083_signal,
    f07fw_f07_fiftytwo_week_position_posrank_63d_base_v084_signal,
    f07fw_f07_fiftytwo_week_position_gapz_63d_base_v085_signal,
    f07fw_f07_fiftytwo_week_position_postension_63v252_base_v086_signal,
    f07fw_f07_fiftytwo_week_position_gapdisp_63d_base_v087_signal,
    f07fw_f07_fiftytwo_week_position_nhfreq63_504d_base_v088_signal,
    f07fw_f07_fiftytwo_week_position_nhentries_1260d_base_v089_signal,
    f07fw_f07_fiftytwo_week_position_nlentries_504d_base_v090_signal,
    f07fw_f07_fiftytwo_week_position_nhaccel_504d_base_v091_signal,
    f07fw_f07_fiftytwo_week_position_nhfreqdiv_base_v092_signal,
    f07fw_f07_fiftytwo_week_position_nhfreqrank63_252d_base_v093_signal,
    f07fw_f07_fiftytwo_week_position_recencyz_252d_base_v094_signal,
    f07fw_f07_fiftytwo_week_position_recencyrank_504d_base_v095_signal,
    f07fw_f07_fiftytwo_week_position_recencybal_252d_base_v096_signal,
    f07fw_f07_fiftytwo_week_position_drymom_252d_base_v097_signal,
    f07fw_f07_fiftytwo_week_position_anchdisthi_504v1260_base_v098_signal,
    f07fw_f07_fiftytwo_week_position_anchdistlo_504v1260_base_v099_signal,
    f07fw_f07_fiftytwo_week_position_anchdistmom_252v1260_base_v100_signal,
    f07fw_f07_fiftytwo_week_position_spanratio_252v504_base_v101_signal,
    f07fw_f07_fiftytwo_week_position_trofreshstreak_1260_base_v102_signal,
    f07fw_f07_fiftytwo_week_position_amprank_504d_base_v103_signal,
    f07fw_f07_fiftytwo_week_position_spanmom126_252d_base_v104_signal,
    f07fw_f07_fiftytwo_week_position_spancontract_252d_base_v105_signal,
    f07fw_f07_fiftytwo_week_position_hiextz_504d_base_v106_signal,
    f07fw_f07_fiftytwo_week_position_lowershare_1260d_base_v107_signal,
    f07fw_f07_fiftytwo_week_position_gapoutlier_252d_base_v108_signal,
    f07fw_f07_fiftytwo_week_position_gapslope_504d_base_v109_signal,
    f07fw_f07_fiftytwo_week_position_gappersist_252d_base_v110_signal,
    f07fw_f07_fiftytwo_week_position_logapdisp_252d_base_v111_signal,
    f07fw_f07_fiftytwo_week_position_logapz_504d_base_v112_signal,
    f07fw_f07_fiftytwo_week_position_gapasym_504d_base_v113_signal,
    f07fw_f07_fiftytwo_week_position_gapregimerun_504d_base_v114_signal,
    f07fw_f07_fiftytwo_week_position_edgeshare_504d_base_v115_signal,
    f07fw_f07_fiftytwo_week_position_regimechurn_504d_base_v116_signal,
    f07fw_f07_fiftytwo_week_position_upperdisp_504d_base_v117_signal,
    f07fw_f07_fiftytwo_week_position_posrankmom_252d_base_v118_signal,
    f07fw_f07_fiftytwo_week_position_posdisp_short_base_v119_signal,
    f07fw_f07_fiftytwo_week_position_truegaprank_504d_base_v120_signal,
    f07fw_f07_fiftytwo_week_position_truelogapz_504d_base_v121_signal,
    f07fw_f07_fiftytwo_week_position_truebanddisp_252d_base_v122_signal,
    f07fw_f07_fiftytwo_week_position_truehiprem_504d_base_v123_signal,
    f07fw_f07_fiftytwo_week_position_truelodisc_504d_base_v124_signal,
    f07fw_f07_fiftytwo_week_position_intrarngshare_252d_base_v125_signal,
    f07fw_f07_fiftytwo_week_position_leaddecay_252d_base_v126_signal,
    f07fw_f07_fiftytwo_week_position_basematurity_252d_base_v127_signal,
    f07fw_f07_fiftytwo_week_position_netpullsm_252d_base_v128_signal,
    f07fw_f07_fiftytwo_week_position_activeanchor_252d_base_v129_signal,
    f07fw_f07_fiftytwo_week_position_pullchurn_252d_base_v130_signal,
    f07fw_f07_fiftytwo_week_position_posrankyoy_252d_base_v131_signal,
    f07fw_f07_fiftytwo_week_position_entryskew_504d_base_v132_signal,
    f07fw_f07_fiftytwo_week_position_posz_1260d_base_v133_signal,
    f07fw_f07_fiftytwo_week_position_gaptanhq_252d_base_v134_signal,
    f07fw_f07_fiftytwo_week_position_freshcomposite_252d_base_v135_signal,
    f07fw_f07_fiftytwo_week_position_extremeshare_252d_base_v136_signal,
    f07fw_f07_fiftytwo_week_position_ladderdisp_base_v137_signal,
    f07fw_f07_fiftytwo_week_position_dipbuy_252d_base_v138_signal,
    f07fw_f07_fiftytwo_week_position_logapyoy_252d_base_v139_signal,
    f07fw_f07_fiftytwo_week_position_extasym_252d_base_v140_signal,
    f07fw_f07_fiftytwo_week_position_roamrank_504d_base_v141_signal,
    f07fw_f07_fiftytwo_week_position_gapcurv_504d_base_v142_signal,
    f07fw_f07_fiftytwo_week_position_refreshdiv_252v504_base_v143_signal,
    f07fw_f07_fiftytwo_week_position_perchdiv_126v504_base_v144_signal,
    f07fw_f07_fiftytwo_week_position_gapstability_252d_base_v145_signal,
    f07fw_f07_fiftytwo_week_position_peakfade_252d_base_v146_signal,
    f07fw_f07_fiftytwo_week_position_occskew_1260d_base_v147_signal,
    f07fw_f07_fiftytwo_week_position_gaprankshift_504d_base_v148_signal,
    f07fw_f07_fiftytwo_week_position_turnregime_252d_base_v149_signal,
    f07fw_f07_fiftytwo_week_position_gapblend_multi_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F07_FIFTYTWO_WEEK_POSITION_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0004, 0.032, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    close = pd.Series(closeadj.values, name="close")
    openp = pd.Series(close.shift(1).fillna(close.iloc[0]).values
                      * (1 + np.random.normal(0, 0.012, n)), name="open")
    high = pd.Series(np.maximum(close, openp)
                     * (1 + np.abs(np.random.normal(0, 0.02, n))), name="high")
    low = pd.Series(np.minimum(close, openp)
                    * (1 - np.abs(np.random.normal(0, 0.02, n))), name="low")
    volume = pd.Series(np.abs(np.random.normal(1.2e6, 7e5, n)) + 5e4, name="volume")

    cols = {"closeadj": closeadj, "close": close, "open": openp,
            "high": high, "low": low, "volume": volume}

    ALLOW = {"open", "high", "low", "close", "closeadj", "volume"}

    n_features = 0
    nan_ok = 0
    results = {}
    for name, meta in REGISTRY.items():
        assert set(meta["inputs"]) <= ALLOW, "%s inputs %s not in allowlist" % (name, meta["inputs"])
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

    print("OK f07_fiftytwo_week_position_base_076_150_claude: %d features pass" % n_features)
