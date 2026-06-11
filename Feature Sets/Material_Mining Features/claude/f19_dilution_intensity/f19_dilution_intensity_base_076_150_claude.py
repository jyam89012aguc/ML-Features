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


def _rsum(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _rank(s, w):
    return s.rolling(w, min_periods=max(1, w // 4)).rank(pct=True) - 0.5


# ===== folder domain primitives (dilution intensity) =====
def _f19_growth(shares, w):
    return np.log(shares.replace(0, np.nan) / shares.shift(w).replace(0, np.nan))


def _f19_dil_rate(shares, w):
    return shares / shares.shift(w).replace(0, np.nan) - 1.0


def _f19_creep(shareswadil, shareswa):
    return shareswadil / shareswa.replace(0, np.nan) - 1.0


def _f19_issuance(ncfcommon):
    return -ncfcommon


def _f19_streak(cond):
    grp = (~cond).cumsum()
    return cond.groupby(grp).cumsum()


# ============================================================
# monthly basic-share dilution rate (granular issuance pulse)
def f19di_f19_dilution_intensity_basrate_21d_base_v076_signal(sharesbas):
    b = _f19_dil_rate(sharesbas, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# weekly basic-share dilution rate (shelf-takedown granularity)
def f19di_f19_dilution_intensity_basrate_5d_base_v077_signal(sharesbas):
    b = _f19_dil_rate(sharesbas, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# diluted-count monthly dilution rate, z-scored vs 252d history
def f19di_f19_dilution_intensity_dilrate_21d_base_v078_signal(shareswadil):
    r = _f19_dil_rate(shareswadil, 21)
    b = _z(r, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# weighted-avg dilution rate, percentile-ranked vs 504d history
def f19di_f19_dilution_intensity_warate_rank_base_v079_signal(shareswa):
    r = _f19_dil_rate(shareswa, 63)
    b = _rank(r, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# basic-share dilution skewness over a year (lumpy vs symmetric issuance)
def f19di_f19_dilution_intensity_dilskew_252d_base_v080_signal(sharesbas):
    r = sharesbas.pct_change(21)
    b = r.rolling(252, min_periods=126).skew()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# basic-share dilution kurtosis over a year (fat-tailed raise shocks)
def f19di_f19_dilution_intensity_dilkurt_252d_base_v081_signal(sharesbas):
    r = sharesbas.pct_change(21)
    b = r.rolling(252, min_periods=126).kurt()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dilution dormancy: trailing-year mean monthly dilution relative to its 2y peak (activity)
def f19di_f19_dilution_intensity_dormant_252d_base_v082_signal(sharesbas):
    r = sharesbas.pct_change(21).clip(lower=0)
    activity = _mean(r, 252)
    peak = _rmax(_mean(r, 252), 504)
    b = activity / peak.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net issuance / |trailing issuance| centered (raise vs return-capital tilt)
def f19di_f19_dilution_intensity_issbalance_base_v083_signal(ncfcommon):
    iss = _f19_issuance(ncfcommon)
    pos = _rsum(iss.clip(lower=0), 252)
    neg = _rsum((-iss).clip(lower=0), 252)
    b = (pos - neg) / (pos + neg).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# issuance volatility regime: 63d issuance std vs 252d issuance std (raise turbulence)
def f19di_f19_dilution_intensity_issvolregime_base_v084_signal(ncfcommon):
    iss = _f19_issuance(ncfcommon)
    short = _std(iss, 63)
    long = _std(iss, 252)
    b = short / long.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cumulative issuance momentum: 63d issuance vs the issuance 126d ago
def f19di_f19_dilution_intensity_issmom_base_v085_signal(ncfcommon):
    q = _rsum(_f19_issuance(ncfcommon), 63)
    b = q - q.shift(126)
    scale = q.abs().rolling(252, min_periods=63).mean()
    b = b / scale.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# creep level percentile-ranked vs 1260d history (deep overhang regime)
def f19di_f19_dilution_intensity_creeprank_1260d_base_v086_signal(shareswadil, shareswa):
    c = _f19_creep(shareswadil, shareswa)
    b = _rank(c, 1260)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# creep velocity over a month (rapid option/warrant expansion)
def f19di_f19_dilution_intensity_creepvel_21d_base_v087_signal(shareswadil, shareswa):
    c = _f19_creep(shareswadil, shareswa)
    b = c - c.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# basic vs diluted dilution-rate correlation breakdown (divergence sign-streak)
def f19di_f19_dilution_intensity_bddiverge_base_v088_signal(sharesbas, shareswadil):
    db = sharesbas.pct_change(21)
    dd = shareswadil.pct_change(21)
    div = (dd - db)
    b = np.tanh(60.0 * div)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# issuance per-share monthly, smoothed by EMA (steady raise drag)
def f19di_f19_dilution_intensity_isspersh_ema_base_v089_signal(ncfcommon, sharesbas):
    ips = _f19_issuance(ncfcommon) / sharesbas.replace(0, np.nan)
    fast = ips.ewm(span=21, min_periods=10).mean()
    slow = ips.ewm(span=126, min_periods=42).mean()
    b = fast - slow
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# big-raise intensity: trailing-year mean of issuance that exceeds +1 rolling-std (tail raises)
def f19di_f19_dilution_intensity_bigraisecnt_base_v090_signal(ncfcommon):
    iss = _f19_issuance(ncfcommon)
    sd = _std(iss, 252)
    excess = (iss - sd).clip(lower=0)
    norm = excess / sd.replace(0, np.nan)
    b = norm.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dilution acceleration sign agreement: do 21d and 63d dilution accelerate together
def f19di_f19_dilution_intensity_dilaccelagree_base_v091_signal(sharesbas):
    a21 = sharesbas.pct_change(21) - sharesbas.pct_change(21).shift(21)
    a63 = sharesbas.pct_change(63) - sharesbas.pct_change(63).shift(63)
    agree = (np.sign(a21) == np.sign(a63)).astype(float)
    b = agree.rolling(252, min_periods=126).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# diluted-creep convexity: 2nd difference of creep over a quarter
def f19di_f19_dilution_intensity_creepconvex_base_v092_signal(shareswadil, shareswa):
    c = _f19_creep(shareswadil, shareswa)
    b = c - 2.0 * c.shift(63) + c.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# issuance Herfindahl: concentration of monthly raises over a year (lumpiness)
def f19di_f19_dilution_intensity_isshhi_base_v093_signal(ncfcommon):
    pos = _f19_issuance(ncfcommon).clip(lower=0)
    tot = _rsum(pos, 252)
    share = pos / tot.replace(0, np.nan)
    b = (share ** 2).rolling(252, min_periods=126).sum()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# basic-share level vs its own 63d EMA (very recent issuance overextension)
def f19di_f19_dilution_intensity_basema63_base_v094_signal(sharesbas):
    ema = sharesbas.ewm(span=63, min_periods=21).mean()
    b = sharesbas / ema.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# weighted-avg vs basic gap z-scored (intra-period issuance timing extremity)
def f19di_f19_dilution_intensity_baswagapz_base_v095_signal(sharesbas, shareswa):
    gap = sharesbas / shareswa.replace(0, np.nan) - 1.0
    b = _z(gap, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dilution drawdown: how far the dilution rate has fallen from its 252d peak (raise slowdown)
def f19di_f19_dilution_intensity_paceslow_base_v096_signal(sharesbas):
    pace = sharesbas.pct_change(63)
    peak = _rmax(pace, 252)
    b = pace - peak
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# issuance reversal magnitude: mean absolute month-over-month change in net issuance
def f19di_f19_dilution_intensity_issflips_base_v097_signal(ncfcommon):
    iss = _f19_issuance(ncfcommon)
    chg = (iss - iss.shift(21)).abs()
    scale = iss.abs().rolling(252, min_periods=126).mean()
    b = _mean(chg, 252) / scale.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# creep dispersion ratio: short-window vs long-window creep volatility
def f19di_f19_dilution_intensity_creepdispratio_base_v098_signal(shareswadil, shareswa):
    c = _f19_creep(shareswadil, shareswa)
    short = _std(c, 63)
    long = _std(c, 252)
    b = short / long.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# basic-share dilution autocorrelation proxy (persistent vs choppy issuance)
def f19di_f19_dilution_intensity_dilpersist_base_v099_signal(sharesbas):
    r = sharesbas.pct_change(21)
    prod = r * r.shift(21)
    b = prod.rolling(252, min_periods=126).mean()
    sd = _std(r, 252)
    b = b / (sd.replace(0, np.nan) ** 2)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net issuance vs creep interaction (raising into existing overhang = stress)
def f19di_f19_dilution_intensity_issoverhang_base_v100_signal(ncfcommon, shareswadil, shareswa):
    issz = _z(_rsum(_f19_issuance(ncfcommon), 63), 252)
    cz = _z(_f19_creep(shareswadil, shareswa), 252)
    b = issz * cz
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# diluted-count two-year cumulative dilution, differenced (multi-cycle pace change)
def f19di_f19_dilution_intensity_dilgrow1260chg_base_v101_signal(shareswadil):
    g = _f19_growth(shareswadil, 504)
    b = g - g.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# share-base quarterly dilution minus its cross-time 1260d median (regime distance)
def f19di_f19_dilution_intensity_dilregimedist_base_v102_signal(sharesbas):
    r = sharesbas.pct_change(63)
    med = r.rolling(1260, min_periods=504).median()
    iqr = (r.rolling(1260, min_periods=504).quantile(0.75)
           - r.rolling(1260, min_periods=504).quantile(0.25))
    b = (r - med) / iqr.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net issuance recency-weighted score (recent raises dominate)
def f19di_f19_dilution_intensity_issrecentwt_base_v103_signal(ncfcommon):
    iss = _f19_issuance(ncfcommon)
    w = np.arange(1, 64)
    raw = iss.rolling(63, min_periods=21).apply(
        lambda a: np.average(a, weights=w[-len(a):]) if len(a) > 0 else np.nan, raw=True)
    scale = iss.abs().rolling(252, min_periods=63).mean()
    b = raw / scale.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# longest consecutive net-issuance streak (sustained raising) over 2y
def f19di_f19_dilution_intensity_raisestreak_base_v104_signal(ncfcommon):
    raised = _f19_issuance(ncfcommon) > 0
    streak = _f19_streak(raised)
    b = streak.rolling(504, min_periods=252).max()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# basic-share dilution vs weighted-avg dilution beta (sensitivity of headline to ongoing)
def f19di_f19_dilution_intensity_dilbeta_base_v105_signal(sharesbas, shareswa):
    db = sharesbas.pct_change(21)
    dw = shareswa.pct_change(21)
    cov = (db * dw).rolling(252, min_periods=126).mean() - (
        _mean(db, 252) * _mean(dw, 252))
    var = _std(dw, 252) ** 2
    b = cov / var.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# creep level minus its 504d EMA (overhang displacement)
def f19di_f19_dilution_intensity_creepdisp_ema_base_v106_signal(shareswadil, shareswa):
    c = _f19_creep(shareswadil, shareswa)
    b = c - c.ewm(span=252, min_periods=84).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# issuance burst flag: above-90th-pct trailing-year raise, recency-counted
def f19di_f19_dilution_intensity_issextreme_base_v107_signal(ncfcommon):
    iss = _f19_issuance(ncfcommon)
    thr = iss.rolling(504, min_periods=252).quantile(0.90)
    hot = (iss > thr).astype(float)
    b = hot.rolling(63, min_periods=21).sum()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dilution rate range-position within its own 504d distribution (where in cycle)
def f19di_f19_dilution_intensity_dilcyclepos_base_v108_signal(sharesbas):
    r = sharesbas.pct_change(63)
    hi = _rmax(r, 504)
    lo = _rmin(r, 504)
    b = (r - lo) / (hi - lo).replace(0, np.nan) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# diluted-creep range position: where current overhang sits in its 252d min-max band
def f19di_f19_dilution_intensity_creepnewhi_base_v109_signal(shareswadil, shareswa):
    c = _f19_creep(shareswadil, shareswa)
    hi = c.rolling(252, min_periods=126).max()
    lo = c.rolling(252, min_periods=126).min()
    b = (c - lo) / (hi - lo).replace(0, np.nan) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# issuance trend slope via simple regression of cumulative issuance (financing direction)
def f19di_f19_dilution_intensity_issslope_base_v110_signal(ncfcommon):
    cum = _f19_issuance(ncfcommon).cumsum()

    def _slope(a):
        x = np.arange(len(a))
        xm = x.mean()
        d = ((x - xm) ** 2).sum()
        return ((x - xm) * (a - a.mean())).sum() / d if d > 0 else np.nan

    raw = cum.rolling(126, min_periods=63).apply(_slope, raw=True)
    scale = cum.abs().rolling(252, min_periods=63).mean()
    b = raw / scale.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# diluted-share dilution dispersion over a year (erratic full-dilution)
def f19di_f19_dilution_intensity_dildisp252_base_v111_signal(shareswadil):
    r = shareswadil.pct_change(21)
    b = _std(r, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# basic-share dilution z minus diluted dilution z (which count is abnormally hot)
def f19di_f19_dilution_intensity_zdiverge_base_v112_signal(sharesbas, shareswadil):
    zb = _z(sharesbas.pct_change(63), 252)
    zd = _z(shareswadil.pct_change(63), 252)
    b = zb - zd
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cumulative issuance per share over 1260d, differenced (multi-cycle raise pace change)
def f19di_f19_dilution_intensity_isspersh1260_base_v113_signal(ncfcommon, sharesbas):
    ips = _rsum(_f19_issuance(ncfcommon), 252) / sharesbas.replace(0, np.nan)
    b = ips - ips.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# share-count step detector: max single-day jump over a quarter (offering event)
def f19di_f19_dilution_intensity_stepjump_base_v114_signal(sharesbas):
    step = sharesbas.pct_change(1)
    b = _rmax(step, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of trailing year share count strictly increasing day-over-day (steady creep)
def f19di_f19_dilution_intensity_monotone_base_v115_signal(sharesbas):
    up = (sharesbas > sharesbas.shift(1)).astype(float)
    b = up.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net issuance vs its 504d max (raise exhaustion / peaked financing)
def f19di_f19_dilution_intensity_issexhaust_base_v116_signal(ncfcommon):
    q = _rsum(_f19_issuance(ncfcommon), 63)
    peak = _rmax(q, 504)
    scale = q.abs().rolling(504, min_periods=126).mean()
    b = (q - peak) / scale.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# diluted-vs-basic creep slope (overhang building or unwinding)
def f19di_f19_dilution_intensity_creepslope_base_v117_signal(shareswadil, shareswa):
    c = _f19_creep(shareswadil, shareswa)

    def _slope(a):
        x = np.arange(len(a))
        xm = x.mean()
        d = ((x - xm) ** 2).sum()
        return ((x - xm) * (a - a.mean())).sum() / d if d > 0 else np.nan

    b = c.rolling(126, min_periods=63).apply(_slope, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# basic-share dilution downside semideviation (asymmetry of issuance vs buyback)
def f19di_f19_dilution_intensity_dilsemidev_base_v118_signal(sharesbas):
    r = sharesbas.pct_change(21)
    pos = r.clip(lower=0)
    b = _std(pos, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# weighted-avg dilution year-over-year change (operational share creep trend)
def f19di_f19_dilution_intensity_wayoy_base_v119_signal(shareswa):
    g = _f19_growth(shareswa, 252)
    prev = g.shift(252)
    b = (g - prev) / (g.abs() + prev.abs() + 1e-9)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# issuance-to-dilution lag: corr of issuance with NEXT-month dilution (lead-lag)
def f19di_f19_dilution_intensity_isslead_base_v120_signal(ncfcommon, sharesbas):
    iss = _z(_f19_issuance(ncfcommon), 126)
    dilnext = _z(sharesbas.pct_change(21).shift(-21), 126)
    prod = iss * dilnext
    b = prod.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# diluted-share dilution acceleration (2nd diff of 63d diluted growth)
def f19di_f19_dilution_intensity_dilaccel2_base_v121_signal(shareswadil):
    g = _f19_growth(shareswadil, 63)
    b = g - 2.0 * g.shift(63) + g.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dilution-rate regime distance scaled by run-length (cyclical issuance persistence)
def f19di_f19_dilution_intensity_dilcross_base_v122_signal(sharesbas):
    r = sharesbas.pct_change(63)
    med = r.rolling(504, min_periods=252).median()
    above = r > med
    run = _f19_streak(above) + _f19_streak(~above)
    dist = (r - med) / (r.rolling(504, min_periods=252).std().replace(0, np.nan))
    b = dist * np.log1p(run)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# financing-tilt crossover: fast vs slow normalized net-issuance EMA (regime shift)
def f19di_f19_dilution_intensity_isstilt_base_v123_signal(ncfcommon):
    iss = _f19_issuance(ncfcommon)
    scale = iss.abs().rolling(252, min_periods=126).mean()
    norm = iss / scale.replace(0, np.nan)
    b = norm.ewm(span=21, min_periods=10).mean() - norm.ewm(span=126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# basic-share half-year dilution minus diluted half-year dilution (overhang absorption)
def f19di_f19_dilution_intensity_absorb_base_v124_signal(sharesbas, shareswadil):
    gb = _f19_growth(sharesbas, 126)
    gd = _f19_growth(shareswadil, 126)
    b = gb - gd
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# issuance burst clustering: variance of monthly issuance gaps (bursty timing)
def f19di_f19_dilution_intensity_isscluster_base_v125_signal(ncfcommon):
    iss = _f19_issuance(ncfcommon)
    hot = (iss > iss.rolling(252, min_periods=126).median()).astype(float)
    run = _f19_streak(hot < 0.5)
    b = _std(run, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# diluted dilution risk-adjusted (1y growth over its own 252d vol)
def f19di_f19_dilution_intensity_dilsharpe_base_v126_signal(shareswadil):
    g = shareswadil.pct_change(63)
    mu = _mean(g, 252)
    sd = _std(g, 252)
    b = mu / sd.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# basic-vs-weighted spread regime distance (period-end issuance loading)
def f19di_f19_dilution_intensity_baswaregime_base_v127_signal(sharesbas, shareswa):
    spr = sharesbas / shareswa.replace(0, np.nan) - 1.0
    med = spr.rolling(504, min_periods=252).median()
    sd = spr.rolling(504, min_periods=252).std()
    b = (spr - med) / sd.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# overhang relief: drop from trailing-year peak creep, scaled by creep level (deleveraging)
def f19di_f19_dilution_intensity_creeprelief_base_v128_signal(shareswadil, shareswa):
    c = _f19_creep(shareswadil, shareswa)
    mx = _rmax(c, 252)
    b = (mx - c) / (c.abs() + 0.01)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# issuance trend curvature (2nd diff of trailing-quarter issuance)
def f19di_f19_dilution_intensity_isscurv_base_v129_signal(ncfcommon):
    q = _rsum(_f19_issuance(ncfcommon), 63)
    accel = q - 2.0 * q.shift(63) + q.shift(126)
    scale = q.abs().rolling(252, min_periods=63).mean()
    b = accel / scale.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# basic-share dilution entropy proxy: dispersion of dilution sign over a year
def f19di_f19_dilution_intensity_dilentropy_base_v130_signal(sharesbas):
    up = (sharesbas.pct_change(21) > 0).astype(float)
    p = up.rolling(252, min_periods=126).mean().clip(1e-6, 1 - 1e-6)
    b = -(p * np.log(p) + (1 - p) * np.log(1 - p))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# diluted-count dilution vs its trailing 504d expectation (full-dilution surprise)
def f19di_f19_dilution_intensity_dilsurprise2_base_v131_signal(shareswadil):
    g = _f19_growth(shareswadil, 126)
    expect = g.ewm(span=252, min_periods=84).mean()
    sd = _std(g, 252)
    b = (g - expect) / sd.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-issuance-funded dilution: issuance/share interacted with share growth sign
def f19di_f19_dilution_intensity_issfunded_base_v132_signal(ncfcommon, sharesbas):
    ips = _rsum(_f19_issuance(ncfcommon), 63) / sharesbas.replace(0, np.nan)
    dilsign = np.sign(sharesbas.pct_change(63))
    raw = ips * dilsign
    b = _rank(raw, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# basic-share dilution rate vs weighted dilution rate ratio (headline amplification)
def f19di_f19_dilution_intensity_amplif_base_v133_signal(sharesbas, shareswa):
    rb = sharesbas.pct_change(63)
    rw = shareswa.pct_change(63)
    b = (rb - rw) / (rb.abs() + rw.abs() + 1e-9)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# share-count whipsaw: ratio of 5d dilution noise to 63d dilution trend
def f19di_f19_dilution_intensity_whipsaw_base_v134_signal(sharesbas):
    noise = _std(sharesbas.pct_change(5), 63)
    trend = _f19_growth(sharesbas, 63).abs()
    b = noise / (trend + 1e-9)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# issuance per-share vs creep change interaction (dilutive raise effectiveness)
def f19di_f19_dilution_intensity_raiseeff_base_v135_signal(ncfcommon, shareswadil, shareswa):
    ips = _z(_rsum(_f19_issuance(ncfcommon), 252) / shareswadil.replace(0, np.nan), 504)
    dc = _z(_f19_creep(shareswadil, shareswa).diff(252), 504)
    b = ips - dc
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# diluted-creep short-term mean-reversion gap normalized by long-run dispersion
def f19di_f19_dilution_intensity_creepmr_base_v136_signal(shareswadil, shareswa):
    c = _f19_creep(shareswadil, shareswa)
    gap = c - _mean(c, 63)
    sd = _std(c, 504)
    b = gap / sd.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# basic-share dilution upside capture: fraction of yearly dilution from top-3 months
def f19di_f19_dilution_intensity_topmonths_base_v137_signal(sharesbas):
    r = sharesbas.pct_change(21).clip(lower=0)

    def _top3(a):
        s = np.sort(a)[::-1]
        tot = a.sum()
        return s[:3].sum() / tot if tot > 0 else np.nan

    b = r.rolling(252, min_periods=126).apply(_top3, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net issuance / share growth coverage ratio z-scored (cash efficiency of dilution)
def f19di_f19_dilution_intensity_coveragez_base_v138_signal(ncfcommon, sharesbas):
    iss = _rsum(_f19_issuance(ncfcommon), 126)
    add = (sharesbas - sharesbas.shift(126)).clip(lower=1.0)
    ratio = iss / add
    b = _z(ratio, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# diluted-share dilution streak fraction (relentless full-dilution count)
def f19di_f19_dilution_intensity_dilstreakfrac_base_v139_signal(shareswadil):
    up = (shareswadil > shareswadil.shift(21)).astype(float)
    b = up.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# issuance pulse asymmetry: skew of monthly net-issuance over a year
def f19di_f19_dilution_intensity_issskew_base_v140_signal(ncfcommon):
    iss = _f19_issuance(ncfcommon)
    b = iss.rolling(252, min_periods=126).skew()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# basic dilution vs five-year dilution rank (long-cycle dilution percentile)
def f19di_f19_dilution_intensity_dilcyclerank_base_v141_signal(sharesbas):
    r = sharesbas.pct_change(126)
    b = _rank(r, 1260)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# creep-weighted issuance: per-share raise scaled by overhang level (compounding dilution)
def f19di_f19_dilution_intensity_creepwtiss_base_v142_signal(ncfcommon, sharesbas, shareswadil, shareswa):
    ips = _rsum(_f19_issuance(ncfcommon), 252) / sharesbas.replace(0, np.nan)
    c = _f19_creep(shareswadil, shareswa).clip(lower=0)
    raw = ips * (1.0 + c)
    b = _z(raw, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# share-base dilution drawdown duration: months since last dilution acceleration peak
def f19di_f19_dilution_intensity_pacepeakage_base_v143_signal(sharesbas):
    pace = sharesbas.pct_change(63)

    def _age(a):
        return (len(a) - 1 - int(np.argmax(a))) / float(len(a))

    b = pace.rolling(252, min_periods=126).apply(_age, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# diluted vs basic dilution-rate dispersion spread (overhang adds volatility)
def f19di_f19_dilution_intensity_dispspread_base_v144_signal(sharesbas, shareswadil):
    db = _std(sharesbas.pct_change(21), 252)
    dd = _std(shareswadil.pct_change(21), 252)
    b = dd - db
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net issuance flow vs basic dilution flow ratio (cash-per-dilution efficiency, bounded)
def f19di_f19_dilution_intensity_cashperdil_base_v145_signal(ncfcommon, sharesbas):
    iss = _rsum(_f19_issuance(ncfcommon), 252)
    dil = _f19_growth(sharesbas, 252)
    b = np.tanh(iss / (iss.abs().rolling(504, min_periods=126).mean().replace(0, np.nan) * (dil + 0.05)))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# weighted-avg dilution acceleration (2nd diff of 63d wa-growth)
def f19di_f19_dilution_intensity_waaccel_base_v146_signal(shareswa):
    g = _f19_growth(shareswa, 63)
    b = g - 2.0 * g.shift(63) + g.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# overhang volatility regime: short vs long dispersion of creep changes (unstable overhang)
def f19di_f19_dilution_intensity_creephigh_base_v147_signal(shareswadil, shareswa):
    dc = _f19_creep(shareswadil, shareswa).diff(21)
    short = _std(dc, 63)
    long = _std(dc, 504)
    b = short / long.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# issuance-adjusted dilution momentum: dilution mom dampened by recent capital returned
def f19di_f19_dilution_intensity_netdilmom_base_v148_signal(ncfcommon, sharesbas):
    dilmom = _f19_growth(sharesbas, 126) - _f19_growth(sharesbas, 126).shift(63)
    ret = (-_f19_issuance(ncfcommon)).clip(lower=0)
    retz = _z(_rsum(ret, 126), 504)
    b = _z(dilmom, 504) - retz
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# basic-share dilution: ratio of last quarter dilution to trailing-year max quarter (peak pace)
def f19di_f19_dilution_intensity_pacevspeak_base_v149_signal(sharesbas):
    q = sharesbas.pct_change(63)
    peak = _rmax(q, 252)
    b = q / peak.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# composite dilution-intensity z: blend of share growth, creep, and per-share issuance
def f19di_f19_dilution_intensity_compositez_base_v150_signal(sharesbas, shareswadil, shareswa, ncfcommon):
    z1 = _z(_f19_growth(sharesbas, 252), 504)
    z2 = _z(_f19_creep(shareswadil, shareswa).diff(252), 504)
    z3 = _z(_rsum(_f19_issuance(ncfcommon), 252) / sharesbas.replace(0, np.nan), 504)
    b = (z1 + z2 + z3) / 3.0 - z1.rolling(126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f19di_f19_dilution_intensity_basrate_21d_base_v076_signal,
    f19di_f19_dilution_intensity_basrate_5d_base_v077_signal,
    f19di_f19_dilution_intensity_dilrate_21d_base_v078_signal,
    f19di_f19_dilution_intensity_warate_rank_base_v079_signal,
    f19di_f19_dilution_intensity_dilskew_252d_base_v080_signal,
    f19di_f19_dilution_intensity_dilkurt_252d_base_v081_signal,
    f19di_f19_dilution_intensity_dormant_252d_base_v082_signal,
    f19di_f19_dilution_intensity_issbalance_base_v083_signal,
    f19di_f19_dilution_intensity_issvolregime_base_v084_signal,
    f19di_f19_dilution_intensity_issmom_base_v085_signal,
    f19di_f19_dilution_intensity_creeprank_1260d_base_v086_signal,
    f19di_f19_dilution_intensity_creepvel_21d_base_v087_signal,
    f19di_f19_dilution_intensity_bddiverge_base_v088_signal,
    f19di_f19_dilution_intensity_isspersh_ema_base_v089_signal,
    f19di_f19_dilution_intensity_bigraisecnt_base_v090_signal,
    f19di_f19_dilution_intensity_dilaccelagree_base_v091_signal,
    f19di_f19_dilution_intensity_creepconvex_base_v092_signal,
    f19di_f19_dilution_intensity_isshhi_base_v093_signal,
    f19di_f19_dilution_intensity_basema63_base_v094_signal,
    f19di_f19_dilution_intensity_baswagapz_base_v095_signal,
    f19di_f19_dilution_intensity_paceslow_base_v096_signal,
    f19di_f19_dilution_intensity_issflips_base_v097_signal,
    f19di_f19_dilution_intensity_creepdispratio_base_v098_signal,
    f19di_f19_dilution_intensity_dilpersist_base_v099_signal,
    f19di_f19_dilution_intensity_issoverhang_base_v100_signal,
    f19di_f19_dilution_intensity_dilgrow1260chg_base_v101_signal,
    f19di_f19_dilution_intensity_dilregimedist_base_v102_signal,
    f19di_f19_dilution_intensity_issrecentwt_base_v103_signal,
    f19di_f19_dilution_intensity_raisestreak_base_v104_signal,
    f19di_f19_dilution_intensity_dilbeta_base_v105_signal,
    f19di_f19_dilution_intensity_creepdisp_ema_base_v106_signal,
    f19di_f19_dilution_intensity_issextreme_base_v107_signal,
    f19di_f19_dilution_intensity_dilcyclepos_base_v108_signal,
    f19di_f19_dilution_intensity_creepnewhi_base_v109_signal,
    f19di_f19_dilution_intensity_issslope_base_v110_signal,
    f19di_f19_dilution_intensity_dildisp252_base_v111_signal,
    f19di_f19_dilution_intensity_zdiverge_base_v112_signal,
    f19di_f19_dilution_intensity_isspersh1260_base_v113_signal,
    f19di_f19_dilution_intensity_stepjump_base_v114_signal,
    f19di_f19_dilution_intensity_monotone_base_v115_signal,
    f19di_f19_dilution_intensity_issexhaust_base_v116_signal,
    f19di_f19_dilution_intensity_creepslope_base_v117_signal,
    f19di_f19_dilution_intensity_dilsemidev_base_v118_signal,
    f19di_f19_dilution_intensity_wayoy_base_v119_signal,
    f19di_f19_dilution_intensity_isslead_base_v120_signal,
    f19di_f19_dilution_intensity_dilaccel2_base_v121_signal,
    f19di_f19_dilution_intensity_dilcross_base_v122_signal,
    f19di_f19_dilution_intensity_isstilt_base_v123_signal,
    f19di_f19_dilution_intensity_absorb_base_v124_signal,
    f19di_f19_dilution_intensity_isscluster_base_v125_signal,
    f19di_f19_dilution_intensity_dilsharpe_base_v126_signal,
    f19di_f19_dilution_intensity_baswaregime_base_v127_signal,
    f19di_f19_dilution_intensity_creeprelief_base_v128_signal,
    f19di_f19_dilution_intensity_isscurv_base_v129_signal,
    f19di_f19_dilution_intensity_dilentropy_base_v130_signal,
    f19di_f19_dilution_intensity_dilsurprise2_base_v131_signal,
    f19di_f19_dilution_intensity_issfunded_base_v132_signal,
    f19di_f19_dilution_intensity_amplif_base_v133_signal,
    f19di_f19_dilution_intensity_whipsaw_base_v134_signal,
    f19di_f19_dilution_intensity_raiseeff_base_v135_signal,
    f19di_f19_dilution_intensity_creepmr_base_v136_signal,
    f19di_f19_dilution_intensity_topmonths_base_v137_signal,
    f19di_f19_dilution_intensity_coveragez_base_v138_signal,
    f19di_f19_dilution_intensity_dilstreakfrac_base_v139_signal,
    f19di_f19_dilution_intensity_issskew_base_v140_signal,
    f19di_f19_dilution_intensity_dilcyclerank_base_v141_signal,
    f19di_f19_dilution_intensity_creepwtiss_base_v142_signal,
    f19di_f19_dilution_intensity_pacepeakage_base_v143_signal,
    f19di_f19_dilution_intensity_dispspread_base_v144_signal,
    f19di_f19_dilution_intensity_cashperdil_base_v145_signal,
    f19di_f19_dilution_intensity_waaccel_base_v146_signal,
    f19di_f19_dilution_intensity_creephigh_base_v147_signal,
    f19di_f19_dilution_intensity_netdilmom_base_v148_signal,
    f19di_f19_dilution_intensity_pacevspeak_base_v149_signal,
    f19di_f19_dilution_intensity_compositez_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F19_DILUTION_INTENSITY_REGISTRY_076_150 = REGISTRY


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

    sharesbas = _fund(101, base=8e7, drift=0.04, vol=0.06).rename("sharesbas")
    shareswa = _fund(102, base=7.6e7, drift=0.038, vol=0.05).rename("shareswa")
    shareswadil = _fund(103, base=8.4e7, drift=0.045, vol=0.07).rename("shareswadil")
    _raise = _fund(104, base=2e7, drift=0.02, vol=0.5)
    _return = _fund(105, base=1.6e7, drift=0.02, vol=0.45)
    ncfcommon = (_return - _raise).rename("ncfcommon")

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

    print("OK f19_dilution_intensity_base_076_150_claude: %d features pass" % n_features)
